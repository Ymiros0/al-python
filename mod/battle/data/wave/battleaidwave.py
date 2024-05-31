ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleAidWave = class("BattleAidWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleAidWave.__name = "BattleAidWave"

local var_0_2 = var_0_0.Battle.BattleAidWave

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor(arg_1_0)

def var_0_2.SetWaveData(arg_2_0, arg_2_1):
	var_0_2.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._vanguardUnitList = arg_2_0._param.vanguard_unitList
	arg_2_0._mainUnitList = arg_2_0._param.main_unitList
	arg_2_0._subUnitList = arg_2_0._param.sub_unitList
	arg_2_0._killList = arg_2_0._param.kill_list

def var_0_2.DoWave(arg_3_0):
	var_0_2.super.DoWave(arg_3_0)

	local var_3_0 = var_0_0.Battle.BattleDataProxy.GetInstance()

	if arg_3_0._killList != None:
		local var_3_1 = var_3_0.GetFriendlyShipList()

		for iter_3_0, iter_3_1 in ipairs(arg_3_0._killList):
			for iter_3_2, iter_3_3 in pairs(var_3_1):
				if iter_3_3.GetTemplateID() == iter_3_1:
					iter_3_3.Retreat()

	if arg_3_0._vanguardUnitList != None:
		for iter_3_4, iter_3_5 in ipairs(arg_3_0._vanguardUnitList):
			local var_3_2 = {}

			for iter_3_6, iter_3_7 in ipairs(iter_3_5.equipment):
				var_3_2[#var_3_2 + 1] = {
					skin = 0,
					id = iter_3_7
				}

			local var_3_3 = Clone(iter_3_5)

			var_3_3.equipment = var_3_2
			var_3_3.baseProperties = iter_3_5.properties

			local var_3_4 = var_3_0.SpawnVanguard(var_3_3, var_0_1.FRIENDLY_CODE)

			var_3_0.InitUnitWeaponCD(var_3_4)
			var_3_0.InitAidUnitStatistics(var_3_4)

	if arg_3_0._mainUnitList != None:
		for iter_3_8, iter_3_9 in ipairs(arg_3_0._mainUnitList):
			local var_3_5 = {}

			for iter_3_10, iter_3_11 in ipairs(iter_3_9.equipment):
				var_3_5[#var_3_5 + 1] = {
					skin = 0,
					id = iter_3_11
				}

			local var_3_6 = Clone(iter_3_9)

			var_3_6.equipment = var_3_5
			var_3_6.baseProperties = iter_3_9.properties

			local var_3_7 = var_3_0.SpawnMain(var_3_6, var_0_1.FRIENDLY_CODE)

			var_3_0.InitUnitWeaponCD(var_3_7)
			var_3_0.InitAidUnitStatistics(var_3_7)

	if arg_3_0._subUnitList != None:
		for iter_3_12, iter_3_13 in ipairs(arg_3_0._subUnitList):
			local var_3_8 = {}

			for iter_3_14, iter_3_15 in ipairs(iter_3_13.equipment):
				var_3_8[#var_3_8 + 1] = {
					skin = 0,
					id = iter_3_15
				}

			local var_3_9 = Clone(iter_3_13)

			var_3_9.equipment = var_3_8
			var_3_9.baseProperties = iter_3_13.properties

			local var_3_10 = var_3_0.SpawnSub(var_3_9, var_0_1.FRIENDLY_CODE)

			var_3_0.InitAidUnitStatistics(var_3_10)

	arg_3_0.doPass()
