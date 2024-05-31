﻿ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattlePlayerWeaponVO = class("BattlePlayerWeaponVO")
var_0_0.Battle.BattlePlayerWeaponVO.__name = "BattlePlayerWeaponVO"

local var_0_3 = var_0_0.Battle.BattlePlayerWeaponVO

function var_0_3.Ctor(arg_1_0, arg_1_1)
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_1_0)

	arg_1_0._GCD = arg_1_1

	arg_1_0:Reset()
end

function var_0_3.Reset(arg_2_0)
	arg_2_0._isOverLoad = false
	arg_2_0._current = arg_2_0._GCD
	arg_2_0._max = arg_2_0._GCD
	arg_2_0._count = 0
	arg_2_0._total = 0
	arg_2_0._weaponList = {}
	arg_2_0._overHeatList = {}
	arg_2_0._readyList = {}
	arg_2_0._chargingList = {}
end

function var_0_3.Update(arg_3_0, arg_3_1)
	if arg_3_0._current < arg_3_0._max then
		local var_3_0 = arg_3_1 - arg_3_0._reloadStartTime

		if var_3_0 >= arg_3_0._max then
			arg_3_0._current = arg_3_0._max
			arg_3_0._reloadStartTime = nil

			for iter_3_0, iter_3_1 in ipairs(arg_3_0._chargingList) do
				iter_3_1:UpdateReload()
			end

			arg_3_0:DispatchOverLoadChange()
		else
			arg_3_0._current = var_3_0
		end
	end
end

function var_0_3.PlayFocus(arg_4_0, arg_4_1, arg_4_2)
	var_0_0.Battle.BattleCameraUtil.GetInstance():FocusCharacter(arg_4_1, var_0_1.CAST_CAM_ZOOM_IN_DURATION)
	var_0_0.Battle.BattleCameraUtil.GetInstance():ZoomCamara(nil, var_0_1.CAST_CAM_ZOOM_SIZE, var_0_1.CAST_CAM_ZOOM_IN_DURATION, true)
	var_0_0.Battle.BattleCameraUtil.GetInstance():BulletTime(var_0_1.SPEED_FACTOR_FOCUS_CHARACTER, var_0_1.FOCUS_MAP_RATE, arg_4_1)

	arg_4_0._focus = true

	if arg_4_0._focusTimer then
		pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_4_0._focusTimer)
	end

	local function var_4_0()
		pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_4_0._focusTimer)

		arg_4_0._focusTimer = nil

		arg_4_2()
	end

	arg_4_0._focusTimer = pg.TimeMgr.GetInstance():AddBattleTimer("", -1, var_0_1.CAST_CAM_ZOOM_IN_DURATION, var_4_0, true)
end

function var_0_3.PlayCutIn(arg_6_0, arg_6_1, arg_6_2)
	var_0_0.Battle.BattleCameraUtil.GetInstance():CutInPainting(arg_6_1, arg_6_2)
end

function var_0_3.ResetFocus(arg_7_0)
	return
end

function var_0_3.CancelFocus(arg_8_0)
	pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_8_0._focusTimer)

	arg_8_0._focusTimer = nil
end

function var_0_3.GetWeaponList(arg_9_0)
	return arg_9_0._weaponList
end

function var_0_3.AppendWeapon(arg_10_0, arg_10_1)
	arg_10_0._weaponList[#arg_10_0._weaponList + 1] = arg_10_1

	if arg_10_1:GetCurrentState() == arg_10_1.STATE_READY then
		arg_10_0._count = arg_10_0._count + 1
	end

	arg_10_0._total = arg_10_0._total + 1

	arg_10_0:DispatchTotalChange()

	arg_10_0._current = arg_10_0._max

	arg_10_0:DispatchOverLoadChange()

	arg_10_0._readyList[#arg_10_0._readyList + 1] = arg_10_1
end

function var_0_3.AppendFreezeWeapon(arg_11_0, arg_11_1)
	arg_11_0._weaponList[#arg_11_0._weaponList + 1] = arg_11_1
	arg_11_0._total = arg_11_0._total + 1

	arg_11_0:DispatchTotalChange()

	if arg_11_1:GetCurrentState() == arg_11_1.STATE_READY then
		arg_11_0._count = arg_11_0._count + 1

		table.insert(arg_11_0._readyList, arg_11_1)
	elseif arg_11_1:GetCDStartTimeStamp() then
		table.insert(arg_11_0._chargingList, arg_11_1)
	else
		table.insert(arg_11_0._overHeatList, arg_11_1)
	end

	arg_11_0:resetCurrent()
	arg_11_0:refreshCD()
	arg_11_0:RefreshReloadingBar()
	arg_11_0:DispatchOverLoadChange()
end

function var_0_3.RemoveWeapon(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_0.deleteElementFromArray(arg_12_1, arg_12_0._weaponList)

	arg_12_0._total = arg_12_0._total - 1

	if arg_12_1:GetCurrentState() ~= arg_12_1.STATE_OVER_HEAT then
		arg_12_0._count = arg_12_0._count - 1

		if arg_12_0._count < 0 then
			arg_12_0._count = 0
		end

		local var_12_1 = arg_12_0.deleteElementFromArray(arg_12_1, arg_12_0._readyList)

		arg_12_0:DispatchOverLoadChange()
		arg_12_0:DispatchTotalChange(var_12_1)
	else
		if arg_12_0.deleteElementFromArray(arg_12_1, arg_12_0._chargingList) == -1 then
			arg_12_0.deleteElementFromArray(arg_12_1, arg_12_0._overHeatList)
		end

		arg_12_0:DispatchOverLoadChange()
		arg_12_0:DispatchTotalChange()
	end

	arg_12_0:refreshCD()

	return var_12_0
end

function var_0_3.refreshCD(arg_13_0)
	local var_13_0 = #arg_13_0._readyList
	local var_13_1 = #arg_13_0._chargingList

	if var_13_0 ~= 0 then
		arg_13_0._current = 1
		arg_13_0._max = 1
	elseif var_13_0 + var_13_1 == 0 then
		arg_13_0._current = 1
		arg_13_0._max = 1
	else
		local var_13_2 = arg_13_0:GetNextTimeStamp() - pg.TimeMgr.GetInstance():GetCombatTime()

		if arg_13_0._current >= arg_13_0._GCD then
			arg_13_0._max = var_13_2
		else
			local var_13_3 = math.max(arg_13_0._max, arg_13_0._GCD)

			arg_13_0._max = math.max(var_13_3 - arg_13_0._current, var_13_2)
		end

		arg_13_0:resetCurrent()
	end
end

function var_0_3.RefreshReloadingBar(arg_14_0)
	if not arg_14_0._reloadStartTime or #arg_14_0._readyList ~= 0 or arg_14_0._max == arg_14_0._GCD then
		return
	end

	local var_14_0 = arg_14_0:GetNextTimeStamp()
	local var_14_1 = arg_14_0._current / arg_14_0._max

	arg_14_0._max = var_14_0 - arg_14_0._reloadStartTime
	arg_14_0._current = var_14_1 * arg_14_0._max
end

function var_0_3.resetCurrent(arg_15_0)
	arg_15_0._current = 0
	arg_15_0._reloadStartTime = arg_15_0._jammingStarTime or pg.TimeMgr.GetInstance():GetCombatTime()
end

function var_0_3.SetMax(arg_16_0, arg_16_1)
	arg_16_0._max = arg_16_1
end

function var_0_3.GetMax(arg_17_0)
	return arg_17_0._max
end

function var_0_3.GetCurrent(arg_18_0)
	return arg_18_0._current
end

function var_0_3.IsOverLoad(arg_19_0)
	return arg_19_0._current < arg_19_0._max or arg_19_0._count < 1
end

function var_0_3.SetTotal(arg_20_0, arg_20_1)
	arg_20_0._total = arg_20_1
end

function var_0_3.GetTotal(arg_21_0)
	return arg_21_0._total
end

function var_0_3.SetCount(arg_22_0, arg_22_1)
	arg_22_0._count = arg_22_1
end

function var_0_3.GetCount(arg_23_0)
	return arg_23_0._count
end

function var_0_3.GetNextTimeStamp(arg_24_0)
	local var_24_0

	if #arg_24_0._chargingList > 0 then
		var_24_0 = arg_24_0._chargingList[1]
		tiemStampB = var_24_0:GetReloadFinishTimeStamp()

		for iter_24_0, iter_24_1 in ipairs(arg_24_0._chargingList) do
			local var_24_1 = iter_24_1:GetReloadFinishTimeStamp()

			tiemStampB = var_24_0:GetReloadFinishTimeStamp()

			if var_24_1 < tiemStampB then
				var_24_0 = iter_24_1
				tiemStampB = var_24_1
			end
		end
	end

	return tiemStampB, var_24_0
end

function var_0_3.GetCurrentWeapon(arg_25_0)
	return arg_25_0._readyList[1]
end

function var_0_3.GetHeadWeapon(arg_26_0)
	return arg_26_0:GetCurrentWeapon() or arg_26_0._chargingList[1] or arg_26_0._overHeatList[1]
end

function var_0_3.GetCurrentWeaponIconIndex(arg_27_0)
	return 0
end

function var_0_3.Plus(arg_28_0, arg_28_1)
	arg_28_0._count = arg_28_0._count + 1

	arg_28_0:DispatchCountChange()
	arg_28_0.deleteElementFromArray(arg_28_1, arg_28_0._chargingList)

	arg_28_0._readyList[#arg_28_0._readyList + 1] = arg_28_1

	local var_28_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.WEAPON_COUNT_PLUS)

	arg_28_0:DispatchEvent(var_28_0)
	arg_28_0:DispatchOverLoadChange()
end

function var_0_3.Deduct(arg_29_0, arg_29_1)
	arg_29_0:readyToOverheat(arg_29_1)

	if #arg_29_0._readyList ~= 0 then
		arg_29_0._max = arg_29_0._GCD

		arg_29_0:resetCurrent()
	elseif #arg_29_0._chargingList ~= 0 then
		local var_29_0 = arg_29_0:GetNextTimeStamp()

		arg_29_0._max = math.max(arg_29_0._GCD, var_29_0 - pg.TimeMgr.GetInstance():GetCombatTime())

		arg_29_0:resetCurrent()
	elseif arg_29_1:GetType() == var_0_0.Battle.BattleConst.EquipmentType.DISPOSABLE_TORPEDO then
		-- block empty
	else
		arg_29_0._current = 0
	end

	arg_29_0:DispatchOverLoadChange()
end

function var_0_3.InitialDeduct(arg_30_0, arg_30_1)
	arg_30_0:readyToOverheat(arg_30_1)
	arg_30_0:DispatchOverLoadChange()
end

function var_0_3.Charge(arg_31_0, arg_31_1)
	arg_31_0.deleteElementFromArray(arg_31_1, arg_31_0._overHeatList)

	arg_31_0._chargingList[#arg_31_0._chargingList + 1] = arg_31_1

	if #arg_31_0._readyList == 0 then
		local var_31_0 = arg_31_0:GetNextTimeStamp()

		arg_31_0._max = math.max(arg_31_0._GCD, var_31_0 - pg.TimeMgr.GetInstance():GetCombatTime())

		arg_31_0:resetCurrent()
	end
end

function var_0_3.ReloadBoost(arg_32_0, arg_32_1, arg_32_2)
	local var_32_0, var_32_1 = arg_32_0:GetNextTimeStamp()

	arg_32_1:ReloadBoost(arg_32_2)

	local var_32_2, var_32_3 = arg_32_0:GetNextTimeStamp()

	if var_32_1 ~= arg_32_1 and var_32_3 ~= arg_32_1 then
		-- block empty
	elseif var_32_1 == arg_32_1 and var_32_3 == arg_32_1 then
		arg_32_0:RefreshReloadingBar()
	elseif var_32_1 ~= var_32_3 then
		arg_32_0:RefreshReloadingBar()
	end
end

function var_0_3.InstantCoolDown(arg_33_0, arg_33_1)
	arg_33_0.deleteElementFromArray(arg_33_1, arg_33_0._overHeatList)

	if arg_33_0._current >= arg_33_0._GCD then
		arg_33_0._current = arg_33_0._max
		arg_33_0._reloadStartTime = nil
	else
		arg_33_0._max = arg_33_0._GCD - arg_33_0._current

		arg_33_0:resetCurrent()
	end

	arg_33_0:Plus(arg_33_1)
end

function var_0_3.DispatchBlink(arg_34_0, arg_34_1)
	local var_34_0 = {
		value = arg_34_1
	}
	local var_34_1 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.WEAPON_BUTTON_BLINK, var_34_0)

	arg_34_0:DispatchEvent(var_34_1)
end

function var_0_3.DispatchTotalChange(arg_35_0, arg_35_1)
	local var_35_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.WEAPON_TOTAL_CHANGE, {
		index = arg_35_1
	})

	arg_35_0:DispatchEvent(var_35_0)
end

function var_0_3.DispatchOverLoadChange(arg_36_0)
	local var_36_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.OVER_LOAD_CHANGE)

	arg_36_0:DispatchEvent(var_36_0)
end

function var_0_3.DispatchCountChange(arg_37_0)
	local var_37_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.COUNT_CHANGE)

	arg_37_0:DispatchEvent(var_37_0)
end

function var_0_3.DispatchInitSubIcon(arg_38_0)
	local var_38_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.INIT_SUB_ICON)

	arg_38_0:DispatchEvent(var_38_0)
end

function var_0_3.StartJamming(arg_39_0)
	arg_39_0._jammingStarTime = pg.TimeMgr.GetInstance():GetCombatTime()

	for iter_39_0, iter_39_1 in ipairs(arg_39_0._chargingList) do
		iter_39_1:StartJamming()
	end
end

function var_0_3.JammingEliminate(arg_40_0)
	for iter_40_0, iter_40_1 in ipairs(arg_40_0._chargingList) do
		iter_40_1:JammingEliminate()
	end

	if arg_40_0._reloadStartTime then
		local var_40_0 = pg.TimeMgr.GetInstance():GetCombatTime()

		if #arg_40_0._readyList ~= 0 then
			arg_40_0._max = arg_40_0._GCD
		else
			arg_40_0._max = arg_40_0:GetNextTimeStamp() - var_40_0 + arg_40_0._current
		end

		arg_40_0._reloadStartTime = arg_40_0._reloadStartTime + (var_40_0 - arg_40_0._jammingStarTime)
	end

	arg_40_0._jammingStarTime = nil
end

function var_0_3.Dispose(arg_41_0)
	pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_41_0._focusTimer)

	arg_41_0._focusTimer = nil

	var_0_0.EventDispatcher.DetachEventDispatcher(arg_41_0)
end

function var_0_3.readyToOverheat(arg_42_0, arg_42_1)
	arg_42_0.deleteElementFromArray(arg_42_1, arg_42_0._readyList)

	arg_42_0._overHeatList[#arg_42_0._overHeatList + 1] = arg_42_1
	arg_42_0._count = arg_42_0._count - 1

	if arg_42_0._count < 0 then
		arg_42_0._count = 0
	end

	arg_42_0:DispatchCountChange()
end

function var_0_3.deleteElementFromArray(arg_43_0, arg_43_1)
	local var_43_0

	for iter_43_0, iter_43_1 in ipairs(arg_43_1) do
		if arg_43_0 == iter_43_1 then
			var_43_0 = iter_43_0

			break
		end
	end

	if var_43_0 == nil then
		return -1
	end

	for iter_43_2 = var_43_0, #arg_43_1 do
		if arg_43_1[iter_43_2 + 1] ~= nil then
			arg_43_1[iter_43_2] = arg_43_1[iter_43_2 + 1]
		else
			arg_43_1[iter_43_2] = nil
		end
	end

	return var_43_0
end
