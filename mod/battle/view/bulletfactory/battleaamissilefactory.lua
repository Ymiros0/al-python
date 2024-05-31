ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.UnitType
local var_0_2 = var_0_0.Battle.BattleConst.AircraftUnitType
local var_0_3 = var_0_0.Battle.BattleConst.CharacterUnitType

var_0_0.Battle.BattleAAMissileFactory = singletonClass("BattleAAMissileFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleAAMissileFactory.__name = "BattleAAMissileFactory"

local var_0_4 = var_0_0.Battle.BattleAAMissileFactory

function var_0_4.MakeBullet(arg_1_0)
	return var_0_0.Battle.BattleTorpedoBullet.New()
end

function var_0_4.onBulletHitFunc(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0:GetBulletData()
	local var_2_1 = var_2_0:getTrackingTarget()

	if var_2_1 == -1 then
		var_0_0.Battle.BattleCannonBulletFactory.onBulletHitFunc(arg_2_0, arg_2_1, arg_2_2)

		return
	end

	local var_2_2 = var_2_0:GetTemplate()
	local var_2_3 = var_0_4.GetDataProxy()
	local var_2_4

	if table.contains(var_0_2, arg_2_2) then
		var_2_4 = var_0_4.GetSceneMediator():GetAircraft(arg_2_1):GetUnitData()
	elseif table.contains(var_0_3, arg_2_2) then
		var_2_4 = var_0_4.GetSceneMediator():GetCharacter(arg_2_1):GetUnitData()
	end

	if not var_2_4 or not var_2_1 or var_2_4:GetUniqueID() ~= var_2_1:GetUniqueID() then
		return
	end

	var_0_0.Battle.PlayBattleSFX(var_2_0:GetHitSFX())

	local var_2_5, var_2_6 = var_0_4.GetFXPool():GetFX(arg_2_0:GetFXID())
	local var_2_7 = arg_2_0:GetTf().localPosition

	pg.EffectMgr.GetInstance():PlayBattleEffect(var_2_5, var_2_6:Add(var_2_7), true)

	local var_2_8, var_2_9 = var_2_3:HandleDamage(var_2_0, var_2_4)

	if var_2_0:GetPierceCount() <= 0 then
		var_2_0:CleanAimMark()
		var_2_3:RemoveBulletUnit(var_2_0:GetUniqueID())
	end
end

function var_0_4.onBulletMissFunc(arg_3_0)
	var_0_4.onBulletHitFunc(arg_3_0)
end

function var_0_4.MakeModel(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = arg_4_1:GetBulletData()
	local var_4_1 = var_4_0:GetTemplate()
	local var_4_2 = arg_4_0:GetDataProxy()

	if not arg_4_0:GetBulletPool():InstBullet(arg_4_1:GetModleID(), function(arg_5_0)
		arg_4_1:AddModel(arg_5_0)
	end) then
		arg_4_1:AddTempModel(arg_4_0:GetTempGOPool():GetObject())
	end

	arg_4_1:SetSpawn(arg_4_2)
	arg_4_1:SetFXFunc(arg_4_0.onBulletHitFunc, arg_4_0.onBulletMissFunc)
	arg_4_0:GetSceneMediator():AddBullet(arg_4_1)

	if var_4_0:GetIFF() ~= var_4_2:GetFriendlyCode() and var_4_1.alert_fx ~= "" then
		arg_4_1:MakeAlert(arg_4_0:GetFXPool():GetFX(var_4_1.alert_fx))
	end
end
