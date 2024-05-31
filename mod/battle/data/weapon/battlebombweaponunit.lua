ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = class("BattleBombWeaponUnit", var_0_0.Battle.BattleWeaponUnit)

var_0_0.Battle.BattleBombWeaponUnit = var_0_2
var_0_2.__name = "BattleBombWeaponUnit"

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)

	arg_1_0._alertCache = {}
	arg_1_0._cacheList = {}
end

function var_0_2.Clear(arg_2_0)
	if arg_2_0._alertTimer then
		pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_2_0._alertTimer)
	end

	arg_2_0._alertTimer = nil

	for iter_2_0, iter_2_1 in pairs(arg_2_0._cacheList) do
		iter_2_1:Destroy()
	end

	var_0_2._cacheList = nil

	var_0_2.super.Clear(arg_2_0)
end

function var_0_2.HostOnEnemy(arg_3_0)
	var_0_2.super.HostOnEnemy(arg_3_0)

	if arg_3_0._preCastInfo.alertTime ~= nil then
		arg_3_0._showPrecastAlert = true

		local function var_3_0()
			arg_3_0._alertTimer:Stop()
			arg_3_0:Fire()
		end

		arg_3_0._alertTimer = pg.TimeMgr.GetInstance():AddBattleTimer("", -1, arg_3_0._preCastInfo.alertTime or 3, var_3_0, true, true)
	end
end

function var_0_2.Update(arg_5_0, arg_5_1)
	arg_5_0:UpdateReload()

	if arg_5_0._currentState == arg_5_0.STATE_READY then
		arg_5_0:updateMovementInfo()

		local var_5_0 = arg_5_0:Tracking()

		if var_5_0 then
			if arg_5_0._showPrecastAlert then
				arg_5_0:PreCast(var_5_0)
			else
				arg_5_0._currentState = arg_5_0.STATE_PRECAST_FINISH
			end
		end
	end

	if arg_5_0._currentState == arg_5_0.STATE_PRECAST_FINISH then
		arg_5_0:updateMovementInfo()

		local var_5_1 = arg_5_0:Tracking()
		local var_5_2 = arg_5_0:GetDirection()
		local var_5_3 = arg_5_0:GetAttackAngle()

		for iter_5_0, iter_5_1 in ipairs(arg_5_0._majorEmitterList) do
			iter_5_1:Ready()
		end

		for iter_5_2, iter_5_3 in ipairs(arg_5_0._majorEmitterList) do
			iter_5_3:Fire(var_5_1, var_5_2, var_5_3)
		end

		var_0_2.super.Fire(arg_5_0, var_5_1)
	end
end

function var_0_2.PreCast(arg_6_0, arg_6_1)
	arg_6_0:cacheBulletID()

	for iter_6_0, iter_6_1 in ipairs(arg_6_0._majorEmitterList) do
		iter_6_1:Ready()
	end

	for iter_6_2, iter_6_3 in ipairs(arg_6_0._majorEmitterList) do
		iter_6_3:Fire(arg_6_1, arg_6_0:GetDirection(), arg_6_0:GetAttackAngle())
	end

	var_0_2.super.PreCast(arg_6_0)
	arg_6_0._alertTimer:Start()
end

function var_0_2.AddPreCastTimer(arg_7_0)
	local function var_7_0()
		arg_7_0._currentState = arg_7_0.STATE_OVER_HEAT

		arg_7_0:RemovePrecastTimer()

		local var_8_0 = arg_7_0._preCastInfo
		local var_8_1 = var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.WEAPON_PRE_CAST_FINISH, var_8_0)

		arg_7_0._host:SetWeaponPreCastBound(false)
		arg_7_0:DispatchEvent(var_8_1)
	end

	arg_7_0._precastTimer = pg.TimeMgr.GetInstance():AddBattleTimer("weaponPrecastTimer", 0, arg_7_0._preCastInfo.time, var_7_0, true)
end

function var_0_2.createMajorEmitter(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4, arg_9_5)
	local var_9_0 = {}
	local var_9_1

	local function var_9_2()
		arg_9_0:DispatchBulletEvent(table.remove(var_9_0, 1))
	end

	local var_9_3

	local function var_9_4()
		for iter_11_0, iter_11_1 in ipairs(arg_9_0._cacheList) do
			if iter_11_1:GetState() ~= iter_11_1.STATE_STOP then
				return
			end
		end

		arg_9_0:EnterCoolDown()
	end

	local var_9_5 = var_0_0.Battle.BattleBulletEmitter.New(var_9_2, var_9_4, arg_9_1)

	arg_9_0._cacheList[var_9_5] = var_9_5

	local function var_9_6(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4)
		local var_12_0 = arg_9_0._emitBulletIDList[arg_9_2]
		local var_12_1 = arg_9_0:Spawn(var_12_0, arg_12_4)

		var_12_1:SetOffsetPriority(arg_12_3)
		var_12_1:SetShiftInfo(arg_12_0, arg_12_1)

		if arg_9_0._tmpData.aim_type == var_0_0.Battle.BattleConst.WeaponAimType.AIM and arg_12_4 ~= nil then
			var_12_1:SetRotateInfo(arg_12_4:GetBeenAimedPosition(), arg_9_0:GetBaseAngle(), arg_12_2)
		else
			var_12_1:SetRotateInfo(nil, arg_9_0:GetBaseAngle(), arg_12_2)
		end

		table.insert(var_9_0, var_12_1)
		arg_9_0:showBombAlert(var_12_1)
	end

	local function var_9_7()
		return
	end

	var_0_2.super.createMajorEmitter(arg_9_0, arg_9_1, arg_9_2, nil, var_9_6, var_9_7)
end

function var_0_2.DoAttack(arg_14_0)
	arg_14_0:TriggerBuffOnSteday()

	for iter_14_0, iter_14_1 in pairs(arg_14_0._cacheList) do
		iter_14_1:Ready()
	end

	for iter_14_2, iter_14_3 in pairs(arg_14_0._cacheList) do
		iter_14_3:Fire(nil, arg_14_0:GetDirection())
	end

	var_0_0.Battle.PlayBattleSFX(arg_14_0._tmpData.fire_sfx)
	arg_14_0:TriggerBuffOnFire()
	arg_14_0:CheckAndShake()
end

function var_0_2.showBombAlert(arg_15_0, arg_15_1)
	arg_15_1:SetExist(false)

	if arg_15_1:GetTemplate().alert_fx ~= "" then
		var_0_0.Battle.BattleBombBulletFactory.CreateBulletAlert(arg_15_1)
	end
end
