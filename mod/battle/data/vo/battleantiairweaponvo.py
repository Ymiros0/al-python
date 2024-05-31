ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleAttr
local var_0_3 = var_0_1.AntiAirConfig

var_0_0.Battle.BattleAntiAirWeaponVO = class("BattleAntiAirWeaponVO", var_0_0.Battle.BattlePlayerWeaponVO)
var_0_0.Battle.BattleAntiAirWeaponVO.__name = "BattleAntiAirWeaponVO"

local var_0_4 = var_0_0.Battle.BattleAntiAirWeaponVO

def var_0_4.Ctor(arg_1_0, arg_1_1):
	var_0_4.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._restoreDenominator = var_0_3.const_A

	arg_1_0.ResetCost()

	arg_1_0._restoreInterval = var_0_3.Restore_Interval

def var_0_4.SetBattleFleetVO(arg_2_0, arg_2_1):
	arg_2_0._battleFleetVO = arg_2_1

def var_0_4.AppendWeapon(arg_3_0, arg_3_1):
	var_0_4.super.AppendWeapon(arg_3_0, arg_3_1)
	arg_3_1.SetTotalDurabilityInfo(arg_3_0)

def var_0_4.RemoveWeapon(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.deleteElementFromArray(arg_4_1, arg_4_0._weaponList)

	arg_4_0._total = arg_4_0._total - 1
	arg_4_0._count = arg_4_0._count - 1

	return var_4_0

def var_0_4.SetMax(arg_5_0, arg_5_1):
	if arg_5_1 > arg_5_0._max:
		arg_5_0._current = arg_5_0._current + (arg_5_1 - arg_5_0._max)

	var_0_4.super.SetMax(arg_5_0, arg_5_1)

	if arg_5_0._current > arg_5_0._max:
		arg_5_0._current = arg_5_0._max

def var_0_4.SetAverageReload(arg_6_0, arg_6_1):
	arg_6_0._fleetReload = arg_6_1

def var_0_4.GetMaxRange(arg_7_0):
	local var_7_0 = arg_7_0._battleFleetVO.GetScoutList()
	local var_7_1 = 0
	local var_7_2 = #var_7_0

	if var_7_2 > 0:
		local var_7_3

		for iter_7_0 = 1, var_7_2:
			if #var_7_0[iter_7_0].GetAntiAirWeapon() > 0:
				var_7_3 = var_7_0[iter_7_0]

				break

		if var_7_3:
			local var_7_4 = var_7_3.GetAntiAirWeapon()

			for iter_7_1, iter_7_2 in ipairs(var_7_4):
				var_7_1 = math.max(var_7_1, iter_7_2.GetTemplateData().range)

	return var_7_1

def var_0_4.SetActive(arg_8_0, arg_8_1):
	for iter_8_0, iter_8_1 in ipairs(arg_8_0._weaponList):
		iter_8_1.SetActive(arg_8_1)

def var_0_4.Restore(arg_9_0):
	arg_9_0._current = arg_9_0._current + arg_9_0._fleetReload / arg_9_0._restoreDenominator

	arg_9_0.checkRestorState()

def var_0_4.RestoreRate(arg_10_0, arg_10_1):
	arg_10_0._current = arg_10_0._current + arg_10_0._max * arg_10_1

	arg_10_0.checkRestorState()

def var_0_4.checkRestorState(arg_11_0):
	if arg_11_0._current >= arg_11_0._max:
		arg_11_0._current = arg_11_0._max
		arg_11_0._restoreDenominator = var_0_3.const_A
		arg_11_0._isOverLoad = False

		arg_11_0.RemoveRestoreTimer()
		arg_11_0.DispatchOverLoadChange()

def var_0_4.Consume(arg_12_0):
	arg_12_0.RemoveRestoreTimer()

	arg_12_0._current = arg_12_0._current - arg_12_0._consumeNormal

	if arg_12_0._current <= 0:
		arg_12_0._current = 0
		arg_12_0._restoreDenominator = var_0_3.const_B
		arg_12_0._isOverLoad = True

		arg_12_0.DispatchOverLoadChange()

def var_0_4.ResetCost(arg_13_0, arg_13_1):
	arg_13_0._consumeNormal = arg_13_1 or var_0_3.const_N

def var_0_4.AddRestoreTimer(arg_14_0):
	if arg_14_0._restoreTimer or arg_14_0._current >= arg_14_0._max:
		return

	local function var_14_0()
		arg_14_0.Restore()

	arg_14_0._restoreTimer = pg.TimeMgr.GetInstance().AddBattleTimer("AARestoreTimer", -1, arg_14_0._restoreInterval, var_14_0, True)

def var_0_4.RemoveRestoreTimer(arg_16_0):
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_16_0._restoreTimer)

	arg_16_0._restoreTimer = None

def var_0_4.Dispose(arg_17_0):
	arg_17_0._battleFleetVO = None

	var_0_4.super.Dispose(arg_17_0)
