ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleAntiSeaBulletFactory = singletonClass("BattleAntiSeaBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleAntiSeaBulletFactory.__name = "BattleAntiSeaBulletFactory"

local var_0_1 = var_0_0.Battle.BattleAntiSeaBulletFactory

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0._tmpTimerList = {}
end

function var_0_1.NeutralizeBullet(arg_2_0)
	for iter_2_0, iter_2_1 in pairs(arg_2_0._tmpTimerList) do
		pg.TimeMgr.GetInstance():RemoveBattleTimer(iter_2_1)

		arg_2_0._tmpTimerList[iter_2_1] = nil
	end
end

function var_0_1.CreateBullet(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5)
	local var_3_0 = arg_3_2:GetTemplate().hit_type
	local var_3_1 = arg_3_0:GetDataProxy()
	local var_3_2 = arg_3_2:GetDirectHitUnit()

	if not var_3_2 then
		var_3_1:RemoveBulletUnit(arg_3_2:GetUniqueID())

		return
	end

	local var_3_3 = var_3_2:GetUniqueID()
	local var_3_4 = arg_3_0:GetSceneMediator():GetCharacter(var_3_3)

	if not var_3_4 then
		var_3_1:RemoveBulletUnit(arg_3_2:GetUniqueID())

		return
	end

	local var_3_5 = var_3_0.range
	local var_3_6
	local var_3_7
	local var_3_8

	local function var_3_9()
		if var_3_6 then
			local var_4_0
			local var_4_1 = var_3_4:GetPosition():Clone()

			if var_3_2:IsAlive() and var_3_4 then
				var_4_0 = var_4_1:Add(Vector3(math.random(var_3_5) - var_3_5 * 0.5, 0, math.random(var_3_5) - var_3_5 * 0.5))
			else
				var_4_0 = var_4_1
			end

			local var_4_2, var_4_3 = arg_3_0:GetFXPool():GetFX(arg_3_2:GetTemplate().hit_fx)

			pg.EffectMgr.GetInstance():PlayBattleEffect(var_4_2, var_4_3:Add(var_4_0), true)
		end
	end

	local function var_3_10()
		if var_3_2:IsAlive() then
			var_3_1:HandleDamage(arg_3_2, var_3_2)
			var_3_1:RemoveBulletUnit(arg_3_2:GetUniqueID())
		end

		pg.TimeMgr.GetInstance():RemoveBattleTimer(var_3_6)

		arg_3_0._tmpTimerList[var_3_6] = nil
		var_3_6 = nil
	end

	var_3_6 = pg.TimeMgr.GetInstance():AddBattleTimer("antiAirTimer", 0, 0.5, var_3_10, true)
	arg_3_0._tmpTimerList[var_3_6] = var_3_6

	if arg_3_4 ~= nil then
		arg_3_0:PlayFireFX(arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5, nil)

		local var_3_11 = pg.TimeMgr.GetInstance():AddBattleTimer("showHitFXTimer", -1, 0.1, var_3_9, true)

		arg_3_0._tmpTimerList[var_3_11] = var_3_11

		var_3_9()
	else
		var_3_1:HandleDamage(arg_3_2, var_3_2)
		var_3_1:RemoveBulletUnit(arg_3_2:GetUniqueID())
	end
end
