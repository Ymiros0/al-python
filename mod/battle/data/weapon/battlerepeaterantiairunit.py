ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleEvent
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = var_0_0.Battle.BattleConst
local var_0_4 = var_0_0.Battle.BattleConfig
local var_0_5 = var_0_0.Battle.BattleDataFunction
local var_0_6 = var_0_0.Battle.BattleAttr
local var_0_7 = var_0_0.Battle.BattleVariable
local var_0_8 = class("BattleRepeaterAntiAirUnit", var_0_0.Battle.BattleWeaponUnit)

var_0_0.Battle.BattleRepeaterAntiAirUnit = var_0_8
var_0_8.__name = "BattleRepeaterAntiAirUnit"

def var_0_8.Ctor(arg_1_0):
	var_0_8.super.Ctor(arg_1_0)

	arg_1_0._dataProxy = var_0_0.Battle.BattleDataProxy.GetInstance()

def var_0_8.FilterTarget(arg_2_0):
	local var_2_0 = arg_2_0._dataProxy.GetAircraftList()
	local var_2_1 = {}
	local var_2_2 = arg_2_0._host.GetIFF()
	local var_2_3 = 1

	for iter_2_0, iter_2_1 in pairs(var_2_0):
		if iter_2_1.GetIFF() != var_2_2 and iter_2_1.IsVisitable():
			var_2_1[var_2_3] = iter_2_1
			var_2_3 = var_2_3 + 1

	return var_2_1

def var_0_8.Fire(arg_3_0):
	local function var_3_0(arg_4_0)
		if not arg_3_0._dataProxy:
			return

		local var_4_0 = {}
		local var_4_1 = arg_3_0._dataProxy.GetAircraftList()

		for iter_4_0, iter_4_1 in ipairs(arg_4_0):
			if iter_4_1.Active:
				local var_4_2 = var_4_1[iter_4_1.UID]

				if var_4_2 and var_4_2.IsVisitable():
					var_4_0[#var_4_0 + 1] = var_4_2

		local var_4_3 = var_0_2.CalculateRepaterAnitiAirTotalDamage(arg_3_0)

		while var_4_3 > 0 and #var_4_0 > 0:
			local var_4_4 = math.random(#var_4_0)
			local var_4_5 = var_4_0[var_4_4]
			local var_4_6 = var_4_5.GetMaxHP()

			var_4_3 = var_4_3 - (var_4_6 + math.random(var_0_4.AnitAirRepeaterConfig.lower_range, var_0_4.AnitAirRepeaterConfig.upper_range))

			if var_4_3 < 0:
				var_4_6 = var_4_6 + var_4_3

			if not var_0_2.RollRepeaterHitDice(arg_3_0, var_4_5):
				table.remove(var_4_0, var_4_4)
				arg_3_0._dataProxy.HandleDirectDamage(var_4_5, var_4_6, arg_3_0.GetHost())

	arg_3_0._dataProxy.SpawnColumnArea(var_0_3.AOEField.AIR, arg_3_0._host.GetIFF(), arg_3_0._host.GetPosition(), arg_3_0._tmpData.range * 2, -1, var_3_0)
	arg_3_0.EnterCoolDown()
	arg_3_0._host.PlayFX(arg_3_0._tmpData.fire_fx, True)
	var_0_0.Battle.PlayBattleSFX(arg_3_0._tmpData.fire_sfx)
