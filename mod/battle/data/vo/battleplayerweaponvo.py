ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattlePlayerWeaponVO = class("BattlePlayerWeaponVO")
var_0_0.Battle.BattlePlayerWeaponVO.__name = "BattlePlayerWeaponVO"

local var_0_3 = var_0_0.Battle.BattlePlayerWeaponVO

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_1_0)

	arg_1_0._GCD = arg_1_1

	arg_1_0.Reset()

def var_0_3.Reset(arg_2_0):
	arg_2_0._isOverLoad = False
	arg_2_0._current = arg_2_0._GCD
	arg_2_0._max = arg_2_0._GCD
	arg_2_0._count = 0
	arg_2_0._total = 0
	arg_2_0._weaponList = {}
	arg_2_0._overHeatList = {}
	arg_2_0._readyList = {}
	arg_2_0._chargingList = {}

def var_0_3.Update(arg_3_0, arg_3_1):
	if arg_3_0._current < arg_3_0._max:
		local var_3_0 = arg_3_1 - arg_3_0._reloadStartTime

		if var_3_0 >= arg_3_0._max:
			arg_3_0._current = arg_3_0._max
			arg_3_0._reloadStartTime = None

			for iter_3_0, iter_3_1 in ipairs(arg_3_0._chargingList):
				iter_3_1.UpdateReload()

			arg_3_0.DispatchOverLoadChange()
		else
			arg_3_0._current = var_3_0

def var_0_3.PlayFocus(arg_4_0, arg_4_1, arg_4_2):
	var_0_0.Battle.BattleCameraUtil.GetInstance().FocusCharacter(arg_4_1, var_0_1.CAST_CAM_ZOOM_IN_DURATION)
	var_0_0.Battle.BattleCameraUtil.GetInstance().ZoomCamara(None, var_0_1.CAST_CAM_ZOOM_SIZE, var_0_1.CAST_CAM_ZOOM_IN_DURATION, True)
	var_0_0.Battle.BattleCameraUtil.GetInstance().BulletTime(var_0_1.SPEED_FACTOR_FOCUS_CHARACTER, var_0_1.FOCUS_MAP_RATE, arg_4_1)

	arg_4_0._focus = True

	if arg_4_0._focusTimer:
		pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_4_0._focusTimer)

	local function var_4_0()
		pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_4_0._focusTimer)

		arg_4_0._focusTimer = None

		arg_4_2()

	arg_4_0._focusTimer = pg.TimeMgr.GetInstance().AddBattleTimer("", -1, var_0_1.CAST_CAM_ZOOM_IN_DURATION, var_4_0, True)

def var_0_3.PlayCutIn(arg_6_0, arg_6_1, arg_6_2):
	var_0_0.Battle.BattleCameraUtil.GetInstance().CutInPainting(arg_6_1, arg_6_2)

def var_0_3.ResetFocus(arg_7_0):
	return

def var_0_3.CancelFocus(arg_8_0):
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_8_0._focusTimer)

	arg_8_0._focusTimer = None

def var_0_3.GetWeaponList(arg_9_0):
	return arg_9_0._weaponList

def var_0_3.AppendWeapon(arg_10_0, arg_10_1):
	arg_10_0._weaponList[#arg_10_0._weaponList + 1] = arg_10_1

	if arg_10_1.GetCurrentState() == arg_10_1.STATE_READY:
		arg_10_0._count = arg_10_0._count + 1

	arg_10_0._total = arg_10_0._total + 1

	arg_10_0.DispatchTotalChange()

	arg_10_0._current = arg_10_0._max

	arg_10_0.DispatchOverLoadChange()

	arg_10_0._readyList[#arg_10_0._readyList + 1] = arg_10_1

def var_0_3.AppendFreezeWeapon(arg_11_0, arg_11_1):
	arg_11_0._weaponList[#arg_11_0._weaponList + 1] = arg_11_1
	arg_11_0._total = arg_11_0._total + 1

	arg_11_0.DispatchTotalChange()

	if arg_11_1.GetCurrentState() == arg_11_1.STATE_READY:
		arg_11_0._count = arg_11_0._count + 1

		table.insert(arg_11_0._readyList, arg_11_1)
	elif arg_11_1.GetCDStartTimeStamp():
		table.insert(arg_11_0._chargingList, arg_11_1)
	else
		table.insert(arg_11_0._overHeatList, arg_11_1)

	arg_11_0.resetCurrent()
	arg_11_0.refreshCD()
	arg_11_0.RefreshReloadingBar()
	arg_11_0.DispatchOverLoadChange()

def var_0_3.RemoveWeapon(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_0.deleteElementFromArray(arg_12_1, arg_12_0._weaponList)

	arg_12_0._total = arg_12_0._total - 1

	if arg_12_1.GetCurrentState() != arg_12_1.STATE_OVER_HEAT:
		arg_12_0._count = arg_12_0._count - 1

		if arg_12_0._count < 0:
			arg_12_0._count = 0

		local var_12_1 = arg_12_0.deleteElementFromArray(arg_12_1, arg_12_0._readyList)

		arg_12_0.DispatchOverLoadChange()
		arg_12_0.DispatchTotalChange(var_12_1)
	else
		if arg_12_0.deleteElementFromArray(arg_12_1, arg_12_0._chargingList) == -1:
			arg_12_0.deleteElementFromArray(arg_12_1, arg_12_0._overHeatList)

		arg_12_0.DispatchOverLoadChange()
		arg_12_0.DispatchTotalChange()

	arg_12_0.refreshCD()

	return var_12_0

def var_0_3.refreshCD(arg_13_0):
	local var_13_0 = #arg_13_0._readyList
	local var_13_1 = #arg_13_0._chargingList

	if var_13_0 != 0:
		arg_13_0._current = 1
		arg_13_0._max = 1
	elif var_13_0 + var_13_1 == 0:
		arg_13_0._current = 1
		arg_13_0._max = 1
	else
		local var_13_2 = arg_13_0.GetNextTimeStamp() - pg.TimeMgr.GetInstance().GetCombatTime()

		if arg_13_0._current >= arg_13_0._GCD:
			arg_13_0._max = var_13_2
		else
			local var_13_3 = math.max(arg_13_0._max, arg_13_0._GCD)

			arg_13_0._max = math.max(var_13_3 - arg_13_0._current, var_13_2)

		arg_13_0.resetCurrent()

def var_0_3.RefreshReloadingBar(arg_14_0):
	if not arg_14_0._reloadStartTime or #arg_14_0._readyList != 0 or arg_14_0._max == arg_14_0._GCD:
		return

	local var_14_0 = arg_14_0.GetNextTimeStamp()
	local var_14_1 = arg_14_0._current / arg_14_0._max

	arg_14_0._max = var_14_0 - arg_14_0._reloadStartTime
	arg_14_0._current = var_14_1 * arg_14_0._max

def var_0_3.resetCurrent(arg_15_0):
	arg_15_0._current = 0
	arg_15_0._reloadStartTime = arg_15_0._jammingStarTime or pg.TimeMgr.GetInstance().GetCombatTime()

def var_0_3.SetMax(arg_16_0, arg_16_1):
	arg_16_0._max = arg_16_1

def var_0_3.GetMax(arg_17_0):
	return arg_17_0._max

def var_0_3.GetCurrent(arg_18_0):
	return arg_18_0._current

def var_0_3.IsOverLoad(arg_19_0):
	return arg_19_0._current < arg_19_0._max or arg_19_0._count < 1

def var_0_3.SetTotal(arg_20_0, arg_20_1):
	arg_20_0._total = arg_20_1

def var_0_3.GetTotal(arg_21_0):
	return arg_21_0._total

def var_0_3.SetCount(arg_22_0, arg_22_1):
	arg_22_0._count = arg_22_1

def var_0_3.GetCount(arg_23_0):
	return arg_23_0._count

def var_0_3.GetNextTimeStamp(arg_24_0):
	local var_24_0

	if #arg_24_0._chargingList > 0:
		var_24_0 = arg_24_0._chargingList[1]
		tiemStampB = var_24_0.GetReloadFinishTimeStamp()

		for iter_24_0, iter_24_1 in ipairs(arg_24_0._chargingList):
			local var_24_1 = iter_24_1.GetReloadFinishTimeStamp()

			tiemStampB = var_24_0.GetReloadFinishTimeStamp()

			if var_24_1 < tiemStampB:
				var_24_0 = iter_24_1
				tiemStampB = var_24_1

	return tiemStampB, var_24_0

def var_0_3.GetCurrentWeapon(arg_25_0):
	return arg_25_0._readyList[1]

def var_0_3.GetHeadWeapon(arg_26_0):
	return arg_26_0.GetCurrentWeapon() or arg_26_0._chargingList[1] or arg_26_0._overHeatList[1]

def var_0_3.GetCurrentWeaponIconIndex(arg_27_0):
	return 0

def var_0_3.Plus(arg_28_0, arg_28_1):
	arg_28_0._count = arg_28_0._count + 1

	arg_28_0.DispatchCountChange()
	arg_28_0.deleteElementFromArray(arg_28_1, arg_28_0._chargingList)

	arg_28_0._readyList[#arg_28_0._readyList + 1] = arg_28_1

	local var_28_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.WEAPON_COUNT_PLUS)

	arg_28_0.DispatchEvent(var_28_0)
	arg_28_0.DispatchOverLoadChange()

def var_0_3.Deduct(arg_29_0, arg_29_1):
	arg_29_0.readyToOverheat(arg_29_1)

	if #arg_29_0._readyList != 0:
		arg_29_0._max = arg_29_0._GCD

		arg_29_0.resetCurrent()
	elif #arg_29_0._chargingList != 0:
		local var_29_0 = arg_29_0.GetNextTimeStamp()

		arg_29_0._max = math.max(arg_29_0._GCD, var_29_0 - pg.TimeMgr.GetInstance().GetCombatTime())

		arg_29_0.resetCurrent()
	elif arg_29_1.GetType() == var_0_0.Battle.BattleConst.EquipmentType.DISPOSABLE_TORPEDO:
		-- block empty
	else
		arg_29_0._current = 0

	arg_29_0.DispatchOverLoadChange()

def var_0_3.InitialDeduct(arg_30_0, arg_30_1):
	arg_30_0.readyToOverheat(arg_30_1)
	arg_30_0.DispatchOverLoadChange()

def var_0_3.Charge(arg_31_0, arg_31_1):
	arg_31_0.deleteElementFromArray(arg_31_1, arg_31_0._overHeatList)

	arg_31_0._chargingList[#arg_31_0._chargingList + 1] = arg_31_1

	if #arg_31_0._readyList == 0:
		local var_31_0 = arg_31_0.GetNextTimeStamp()

		arg_31_0._max = math.max(arg_31_0._GCD, var_31_0 - pg.TimeMgr.GetInstance().GetCombatTime())

		arg_31_0.resetCurrent()

def var_0_3.ReloadBoost(arg_32_0, arg_32_1, arg_32_2):
	local var_32_0, var_32_1 = arg_32_0.GetNextTimeStamp()

	arg_32_1.ReloadBoost(arg_32_2)

	local var_32_2, var_32_3 = arg_32_0.GetNextTimeStamp()

	if var_32_1 != arg_32_1 and var_32_3 != arg_32_1:
		-- block empty
	elif var_32_1 == arg_32_1 and var_32_3 == arg_32_1:
		arg_32_0.RefreshReloadingBar()
	elif var_32_1 != var_32_3:
		arg_32_0.RefreshReloadingBar()

def var_0_3.InstantCoolDown(arg_33_0, arg_33_1):
	arg_33_0.deleteElementFromArray(arg_33_1, arg_33_0._overHeatList)

	if arg_33_0._current >= arg_33_0._GCD:
		arg_33_0._current = arg_33_0._max
		arg_33_0._reloadStartTime = None
	else
		arg_33_0._max = arg_33_0._GCD - arg_33_0._current

		arg_33_0.resetCurrent()

	arg_33_0.Plus(arg_33_1)

def var_0_3.DispatchBlink(arg_34_0, arg_34_1):
	local var_34_0 = {
		value = arg_34_1
	}
	local var_34_1 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.WEAPON_BUTTON_BLINK, var_34_0)

	arg_34_0.DispatchEvent(var_34_1)

def var_0_3.DispatchTotalChange(arg_35_0, arg_35_1):
	local var_35_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.WEAPON_TOTAL_CHANGE, {
		index = arg_35_1
	})

	arg_35_0.DispatchEvent(var_35_0)

def var_0_3.DispatchOverLoadChange(arg_36_0):
	local var_36_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.OVER_LOAD_CHANGE)

	arg_36_0.DispatchEvent(var_36_0)

def var_0_3.DispatchCountChange(arg_37_0):
	local var_37_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.COUNT_CHANGE)

	arg_37_0.DispatchEvent(var_37_0)

def var_0_3.DispatchInitSubIcon(arg_38_0):
	local var_38_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.INIT_SUB_ICON)

	arg_38_0.DispatchEvent(var_38_0)

def var_0_3.StartJamming(arg_39_0):
	arg_39_0._jammingStarTime = pg.TimeMgr.GetInstance().GetCombatTime()

	for iter_39_0, iter_39_1 in ipairs(arg_39_0._chargingList):
		iter_39_1.StartJamming()

def var_0_3.JammingEliminate(arg_40_0):
	for iter_40_0, iter_40_1 in ipairs(arg_40_0._chargingList):
		iter_40_1.JammingEliminate()

	if arg_40_0._reloadStartTime:
		local var_40_0 = pg.TimeMgr.GetInstance().GetCombatTime()

		if #arg_40_0._readyList != 0:
			arg_40_0._max = arg_40_0._GCD
		else
			arg_40_0._max = arg_40_0.GetNextTimeStamp() - var_40_0 + arg_40_0._current

		arg_40_0._reloadStartTime = arg_40_0._reloadStartTime + (var_40_0 - arg_40_0._jammingStarTime)

	arg_40_0._jammingStarTime = None

def var_0_3.Dispose(arg_41_0):
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_41_0._focusTimer)

	arg_41_0._focusTimer = None

	var_0_0.EventDispatcher.DetachEventDispatcher(arg_41_0)

def var_0_3.readyToOverheat(arg_42_0, arg_42_1):
	arg_42_0.deleteElementFromArray(arg_42_1, arg_42_0._readyList)

	arg_42_0._overHeatList[#arg_42_0._overHeatList + 1] = arg_42_1
	arg_42_0._count = arg_42_0._count - 1

	if arg_42_0._count < 0:
		arg_42_0._count = 0

	arg_42_0.DispatchCountChange()

def var_0_3.deleteElementFromArray(arg_43_0, arg_43_1):
	local var_43_0

	for iter_43_0, iter_43_1 in ipairs(arg_43_1):
		if arg_43_0 == iter_43_1:
			var_43_0 = iter_43_0

			break

	if var_43_0 == None:
		return -1

	for iter_43_2 = var_43_0, #arg_43_1:
		if arg_43_1[iter_43_2 + 1] != None:
			arg_43_1[iter_43_2] = arg_43_1[iter_43_2 + 1]
		else
			arg_43_1[iter_43_2] = None

	return var_43_0
