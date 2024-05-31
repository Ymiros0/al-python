local var_0_0 = class("NewBattleResultDisplayPaintingsPage", import("view.base.BaseSubView"))
local var_0_1 = 6
local var_0_2 = 295

def var_0_0.getUIName(arg_1_0):
	return "NewBattleResultDisplayPaintingsPages"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.slots = {
		arg_2_0.findTF("tpl")
	}

def var_0_0.StaticGetFinalExpandPosition(arg_3_0):
	if arg_3_0 <= var_0_1:
		return var_0_0.StaticGetExpandPosition(arg_3_0, var_0_1 - 1)
	else
		local var_3_0 = arg_3_0 - var_0_1

		return var_0_0.StaticGetExpandPosition(arg_3_0, arg_3_0 - 1) - var_3_0 * Vector2(var_0_2, 0)

def var_0_0.StaticGetExpandPosition(arg_4_0, arg_4_1):
	local var_4_0 = math.ceil(arg_4_1 / 2)
	local var_4_1 = arg_4_1 % 2 != 0
	local var_4_2

	if arg_4_0 > 6 and arg_4_0 % 2 == 0 or arg_4_0 <= 6:
		var_4_2 = var_4_1 and Vector2(-730, 72) or Vector2(-457, -72)
	else
		var_4_2 = var_4_1 and Vector2(-751, -72) or Vector2(-437, 72)

	return var_4_2 + Vector2(590, 0) * (var_4_0 - 1)

def var_0_0.GetExpandPosition(arg_5_0, arg_5_1, arg_5_2):
	return var_0_0.StaticGetExpandPosition(arg_5_1, arg_5_2)

def var_0_0.GetShrinkPosition(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_0.GetExpandPosition(arg_6_1, arg_6_2)
	local var_6_1 = arg_6_2 % 2 != 0
	local var_6_2 = Vector2(-125, -936)

	if arg_6_1 > 6 and arg_6_1 % 2 == 0 or arg_6_1 <= 6:
		return var_6_1 and var_6_0 - var_6_2 or var_6_0 + var_6_2
	else
		return var_6_1 and var_6_0 + var_6_2 or var_6_0 - var_6_2

def var_0_0.SetUp(arg_7_0, arg_7_1):
	arg_7_0.Show()

	arg_7_0.displayShips = arg_7_0.ReSortFleetShips()

	seriesAsync({
		function(arg_8_0)
			arg_7_0.InitMainFleetShips(arg_8_0),
		function(arg_9_0)
			arg_7_0.DisplayMainFleet(arg_9_0),
		function(arg_10_0)
			arg_7_0.MoveMainFleetShips(arg_10_0),
		function(arg_11_0)
			arg_7_0.InitSubFleetShips(arg_11_0),
		function(arg_12_0)
			arg_7_0.DisplaySubFleet(arg_12_0),
		function(arg_13_0)
			onDelayTick(arg_13_0, 0.5)
	}, function()
		arg_7_1())

def var_0_0.ReSortFleetShips(arg_15_0):
	local var_15_0 = arg_15_0.contextData.oldMainShips
	local var_15_1 = arg_15_0.contextData.statistics.mvpShipID
	local var_15_2 = arg_15_0.contextData.statistics._flagShipID
	local var_15_3, var_15_4, var_15_5, var_15_6 = NewBattleResultUtil.SeparateMvpShip(var_15_0, var_15_1, var_15_2)
	local var_15_7 = {}

	if var_15_6 != None:
		local var_15_8 = ys.Battle.BattleDataFunction.GetPlayerShipTmpDataFromID(var_15_6.configId).type
		local var_15_9 = TeamType.GetTeamFromShipType(var_15_8)

		if var_15_9 == TeamType.Vanguard:
			NewBattleResultUtil.SpecialInsertItem(var_15_7, var_15_5, var_15_4, var_15_3, var_15_6)
		elif var_15_9 == TeamType.Main:
			NewBattleResultUtil.SpecialInsertItem(var_15_7, var_15_5, var_15_3, var_15_4, var_15_6)
		elif var_15_9 == TeamType.Submarine:
			NewBattleResultUtil.SpecialInsertItem(var_15_7, var_15_3, var_15_4, var_15_5, var_15_6)
	else
		var_15_7 = var_15_0

	return var_15_7

def var_0_0.InitSubFleetShips(arg_16_0, arg_16_1):
	if arg_16_0.exited:
		return

	local var_16_0 = arg_16_0.displayShips

	if #var_16_0 <= var_0_1:
		arg_16_1()

		return

	local var_16_1 = #var_16_0 - var_0_1

	for iter_16_0 = 1, var_16_1:
		if arg_16_0.slots[iter_16_0]:
			retPaintingPrefab(arg_16_0.slots[iter_16_0].Find("mask/painting"), var_16_0[iter_16_0].getPainting())

	local var_16_2 = {}

	for iter_16_1 = var_0_1 + 1, math.max(var_0_1, #var_16_0):
		local var_16_3 = Object.Instantiate(arg_16_0.slots[1], arg_16_0.slots[1].parent)

		table.insert(arg_16_0.slots, var_16_3)

		local var_16_4 = var_16_0[iter_16_1]

		var_16_3.localPosition = arg_16_0.GetExpandPosition(#var_16_0, iter_16_1)

		table.insert(var_16_2, function(arg_17_0)
			setPaintingPrefabAsync(var_16_3.Find("mask/painting"), var_16_4.getPainting(), "biandui", arg_17_0))

	parallelAsync(var_16_2, function()
		onDelayTick(arg_16_1, 0.05))

def var_0_0.DisplaySubFleet(arg_19_0, arg_19_1):
	if arg_19_0.exited:
		return

	arg_19_0.EffectSlots(False)

	local var_19_0 = arg_19_0.displayShips

	if #var_19_0 <= var_0_1:
		arg_19_1()

		return

	local var_19_1 = {}
	local var_19_2 = #var_19_0 - var_0_1

	for iter_19_0 = var_0_1 + 1, math.max(var_0_1, #var_19_0):
		local var_19_3 = arg_19_0.slots[iter_19_0]
		local var_19_4 = arg_19_0.GetExpandPosition(#var_19_0, iter_19_0).x
		local var_19_5 = var_19_4 - var_19_2 * var_0_2

		table.insert(var_19_1, function(arg_20_0)
			if arg_19_0.exited:
				return

			LeanTween.value(var_19_3.gameObject, var_19_4, var_19_5, 0.3).setOnUpdate(System.Action_float(function(arg_21_0)
				var_19_3.localPosition = Vector3(arg_21_0, var_19_3.localPosition.y, 0))).setEase(LeanTweenType.easeOutQuad)
			onDelayTick(function()
				if arg_19_0.exited:
					return

				setActive(var_19_3.Find("mask/blink"), True), 0.15)
			onDelayTick(function()
				if arg_19_0.exited:
					return

				setActive(var_19_3.Find("mask/blink"), False), 0.2)
			onDelayTick(arg_20_0, 0.1))

	seriesAsync(var_19_1, function()
		arg_19_0.EffectSlots(True)
		arg_19_1())

def var_0_0.EffectSlots(arg_25_0, arg_25_1):
	for iter_25_0, iter_25_1 in ipairs(arg_25_0.slots):
		if not IsNil(iter_25_1):
			setActive(iter_25_1.Find("effect"), arg_25_1)

def var_0_0.MoveMainFleetShips(arg_26_0, arg_26_1):
	if arg_26_0.exited:
		return

	local var_26_0 = #arg_26_0.displayShips

	if var_26_0 <= var_0_1:
		arg_26_1()

		return

	local var_26_1 = {}
	local var_26_2 = var_26_0 - var_0_1

	for iter_26_0, iter_26_1 in ipairs(arg_26_0.slots):
		table.insert(var_26_1, function(arg_27_0)
			local var_27_0 = arg_26_0.GetExpandPosition(var_26_0, iter_26_0).x
			local var_27_1 = var_27_0 - var_26_2 * var_0_2

			LeanTween.value(iter_26_1.gameObject, var_27_0, var_27_1, 0.3).setOnUpdate(System.Action_float(function(arg_28_0)
				iter_26_1.localPosition = Vector3(arg_28_0, iter_26_1.localPosition.y, 0))).setEase(LeanTweenType.easeOutQuad).setOnComplete(System.Action(arg_27_0)))

	parallelAsync(var_26_1, function()
		return)
	onDelayTick(function()
		if arg_26_0.exited:
			return

		arg_26_1()

		for iter_30_0 = 1, var_26_2:
			if arg_26_0.slots[iter_30_0]:
				setActive(arg_26_0.slots[iter_30_0], False), 0.05)

def var_0_0.DisplayMainFleet(arg_31_0, arg_31_1):
	if arg_31_0.exited:
		return

	local var_31_0 = {}
	local var_31_1 = var_0_1 - #arg_31_0.slots
	local var_31_2 = #arg_31_0.displayShips

	for iter_31_0, iter_31_1 in ipairs(arg_31_0.slots):
		table.insert(var_31_0, function(arg_32_0)
			if arg_31_0.exited:
				return

			local var_32_0 = var_31_1 + iter_31_0
			local var_32_1 = arg_31_0.GetExpandPosition(var_31_2, var_32_0)
			local var_32_2 = arg_31_0.GetShrinkPosition(var_31_2, var_32_0)

			LeanTween.value(iter_31_1.gameObject, var_32_2, var_32_1, 0.29).setOnUpdate(System.Action_UnityEngine_Vector2(function(arg_33_0)
				iter_31_1.localPosition = arg_33_0))
			onNextTick(arg_32_0))

	local var_31_3 = 0

	Timer.New(function()
		if arg_31_0.exited:
			return

		for iter_34_0, iter_34_1 in ipairs(arg_31_0.slots):
			setActive(iter_34_1.Find("mask/blink"), var_31_3 % 2 != 0 == (iter_34_0 % 2 != 0))

		var_31_3 = var_31_3 + 1, 0.059, 5).Start()
	Timer.New(function()
		if arg_31_0.exited:
			return

		for iter_35_0, iter_35_1 in ipairs(arg_31_0.slots):
			setActive(iter_35_1.Find("mask/blink"), False), 0.3, 1).Start()
	seriesAsync(var_31_0, function()
		arg_31_0.EffectSlots(True)
		onDelayTick(arg_31_1, 0.5))

def var_0_0.InitMainFleetShips(arg_37_0, arg_37_1):
	local var_37_0 = arg_37_0.displayShips
	local var_37_1 = math.min(var_0_1, #var_37_0)

	for iter_37_0 = 2, var_37_1:
		local var_37_2 = Object.Instantiate(arg_37_0.slots[1], arg_37_0.slots[1].parent)

		table.insert(arg_37_0.slots, var_37_2)

	local var_37_3 = {}
	local var_37_4 = var_0_1 - var_37_1

	for iter_37_1 = 1, var_37_1:
		local var_37_5 = var_37_0[iter_37_1]
		local var_37_6 = arg_37_0.slots[iter_37_1]

		var_37_6.localPosition = arg_37_0.GetShrinkPosition(#var_37_0, var_37_4 + iter_37_1)

		table.insert(var_37_3, function(arg_38_0)
			if arg_37_0.exited:
				return

			setPaintingPrefabAsync(var_37_6.Find("mask/painting"), var_37_5.getPainting(), "biandui", arg_38_0))

	parallelAsync(var_37_3, arg_37_1)

def var_0_0.OnDestroy(arg_39_0):
	arg_39_0.exited = True

	if arg_39_0.isShowing():
		arg_39_0.Hide()

	local var_39_0 = arg_39_0.displayShips or {}

	for iter_39_0, iter_39_1 in ipairs(arg_39_0.slots or {}):
		if iter_39_1:
			local var_39_1 = iter_39_1.Find("mask/painting")

			if var_39_1 and var_39_0[iter_39_0] and var_39_1.Find("fitter").childCount > 0:
				retPaintingPrefab(var_39_1, var_39_0[iter_39_0].getPainting())

		if iter_39_1 and LeanTween.isTweening(iter_39_1.gameObject):
			LeanTween.cancel(iter_39_1.gameObject)

return var_0_0
