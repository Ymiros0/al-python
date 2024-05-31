ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleAidWave = class("BattleAidWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleAidWave.__name = "BattleAidWave"

local var_0_2 = var_0_0.Battle.BattleAidWave

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)
end

function var_0_2.SetWaveData(arg_2_0, arg_2_1)
	var_0_2.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._vanguardUnitList = arg_2_0._param.vanguard_unitList
	arg_2_0._mainUnitList = arg_2_0._param.main_unitList
	arg_2_0._subUnitList = arg_2_0._param.sub_unitList
	arg_2_0._killList = arg_2_0._param.kill_list
end

function var_0_2.DoWave(arg_3_0)
	var_0_2.super.DoWave(arg_3_0)

	local var_3_0 = var_0_0.Battle.BattleDataProxy.GetInstance()

	if arg_3_0._killList ~= nil then
		local var_3_1 = var_3_0:GetFriendlyShipList()

		for iter_3_0, iter_3_1 in ipairs(arg_3_0._killList) do
			for iter_3_2, iter_3_3 in pairs(var_3_1) do
				if iter_3_3:GetTemplateID() == iter_3_1 then
					iter_3_3:Retreat()
				end
			end
		end
	end

	if arg_3_0._vanguardUnitList ~= nil then
		for iter_3_4, iter_3_5 in ipairs(arg_3_0._vanguardUnitList) do
			local var_3_2 = {}

			for iter_3_6, iter_3_7 in ipairs(iter_3_5.equipment) do
				var_3_2[#var_3_2 + 1] = {
					skin = 0,
					id = iter_3_7
				}
			end

			local var_3_3 = Clone(iter_3_5)

			var_3_3.equipment = var_3_2
			var_3_3.baseProperties = iter_3_5.properties

			local var_3_4 = var_3_0:SpawnVanguard(var_3_3, var_0_1.FRIENDLY_CODE)

			var_3_0.InitUnitWeaponCD(var_3_4)
			var_3_0:InitAidUnitStatistics(var_3_4)
		end
	end

	if arg_3_0._mainUnitList ~= nil then
		for iter_3_8, iter_3_9 in ipairs(arg_3_0._mainUnitList) do
			local var_3_5 = {}

			for iter_3_10, iter_3_11 in ipairs(iter_3_9.equipment) do
				var_3_5[#var_3_5 + 1] = {
					skin = 0,
					id = iter_3_11
				}
			end

			local var_3_6 = Clone(iter_3_9)

			var_3_6.equipment = var_3_5
			var_3_6.baseProperties = iter_3_9.properties

			local var_3_7 = var_3_0:SpawnMain(var_3_6, var_0_1.FRIENDLY_CODE)

			var_3_0.InitUnitWeaponCD(var_3_7)
			var_3_0:InitAidUnitStatistics(var_3_7)
		end
	end

	if arg_3_0._subUnitList ~= nil then
		for iter_3_12, iter_3_13 in ipairs(arg_3_0._subUnitList) do
			local var_3_8 = {}

			for iter_3_14, iter_3_15 in ipairs(iter_3_13.equipment) do
				var_3_8[#var_3_8 + 1] = {
					skin = 0,
					id = iter_3_15
				}
			end

			local var_3_9 = Clone(iter_3_13)

			var_3_9.equipment = var_3_8
			var_3_9.baseProperties = iter_3_13.properties

			local var_3_10 = var_3_0:SpawnSub(var_3_9, var_0_1.FRIENDLY_CODE)

			var_3_0:InitAidUnitStatistics(var_3_10)
		end
	end

	arg_3_0:doPass()
end
