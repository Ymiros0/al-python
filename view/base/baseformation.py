local var_0_0 = class("BaseFormation")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	arg_1_0._mainTf = arg_1_1
	arg_1_0._heroContainer = arg_1_2
	arg_1_0._heroInfoTpl = arg_1_3
	arg_1_0._gridTFs = arg_1_4
	arg_1_0._widthRate = rtf(arg_1_0._mainTf).rect.width / UnityEngine.Screen.width
	arg_1_0._heightRate = rtf(arg_1_0._mainTf).rect.height / UnityEngine.Screen.height
	arg_1_0._halfWidth = rtf(arg_1_0._mainTf).rect.width / 2
	arg_1_0._halfHeight = rtf(arg_1_0._mainTf).rect.height / 2
	arg_1_0._offset = arg_1_0._heroContainer.localPosition
	arg_1_0._eventTriggers = {}

	pg.DelegateInfo.New(arg_1_0)

def var_0_0.SetFleetVO(arg_2_0, arg_2_1):
	arg_2_0._currentFleetVO = arg_2_1

def var_0_0.SetShipVOs(arg_3_0, arg_3_1):
	arg_3_0._shipVOs = arg_3_1

def var_0_0.DisableTip(arg_4_0):
	arg_4_0._disableTip = True

def var_0_0.ForceDropChar(arg_5_0):
	if arg_5_0._currentDragDelegate:
		arg_5_0._forceDropCharacter = True

		LuaHelper.triggerEndDrag(arg_5_0._currentDragDelegate)

def var_0_0.AddHeroInfoModify(arg_6_0, arg_6_1):
	arg_6_0._heroInfoModifyCb = arg_6_1

def var_0_0.AddLongPress(arg_7_0, arg_7_1):
	arg_7_0._longPressCb = arg_7_1

def var_0_0.AddClick(arg_8_0, arg_8_1):
	arg_8_0._click = arg_8_1

def var_0_0.AddBeginDrag(arg_9_0, arg_9_1):
	arg_9_0._beginDrag = arg_9_1

def var_0_0.AddEndDrag(arg_10_0, arg_10_1):
	arg_10_0._endDrag = arg_10_1

def var_0_0.AddCheckBeginDrag(arg_11_0, arg_11_1):
	arg_11_0._checkBeginDrag = arg_11_1

def var_0_0.AddShiftOnly(arg_12_0, arg_12_1):
	arg_12_0._shiftOnly = arg_12_1

def var_0_0.AddRemoveShip(arg_13_0, arg_13_1):
	arg_13_0._removeShip = arg_13_1

def var_0_0.AddCheckRemove(arg_14_0, arg_14_1):
	arg_14_0._checkRemove = arg_14_1

def var_0_0.AddCheckSwitch(arg_15_0, arg_15_1):
	arg_15_0._checkSwitch = arg_15_1

def var_0_0.AddSwitchToDisplayMode(arg_16_0, arg_16_1):
	arg_16_0._switchToDisplayModeHandler = arg_16_1

def var_0_0.AddSwitchToShiftMode(arg_17_0, arg_17_1):
	arg_17_0._switchToShiftModeHandler = arg_17_1

def var_0_0.AddSwitchToPreviewMode(arg_18_0, arg_18_1):
	arg_18_0._swtichToPreviewModeHandler = arg_18_1

def var_0_0.AddGridTipClick(arg_19_0, arg_19_1):
	arg_19_0._gridTipClick = arg_19_1

def var_0_0.AddLoadComplete(arg_20_0, arg_20_1):
	arg_20_0._loadComplete = arg_20_1

def var_0_0.GenCharInfo(arg_21_0, arg_21_1, arg_21_2):
	return {
		heroInfoTF = arg_21_1,
		spineRole = arg_21_2
	}

def var_0_0.ClearHeroContainer(arg_22_0):
	if arg_22_0._characterList:
		arg_22_0.RecycleCharacterList(arg_22_0._currentFleetVO.getTeamByName(TeamType.Main), arg_22_0._characterList[TeamType.Main])
		arg_22_0.RecycleCharacterList(arg_22_0._currentFleetVO.getTeamByName(TeamType.Vanguard), arg_22_0._characterList[TeamType.Vanguard])
		arg_22_0.RecycleCharacterList(arg_22_0._currentFleetVO.getTeamByName(TeamType.Submarine), arg_22_0._characterList[TeamType.Submarine])

	removeAllChildren(arg_22_0._heroContainer)

def var_0_0.LoadAllCharacter(arg_23_0):
	arg_23_0.ClearHeroContainer()

	arg_23_0._characterList = {
		[TeamType.Vanguard] = {},
		[TeamType.Main] = {},
		[TeamType.Submarine] = {}
	}

	local function var_23_0(arg_24_0, arg_24_1, arg_24_2, arg_24_3)
		if arg_23_0._exited:
			return

		local var_24_0 = arg_23_0._shipVOs[arg_24_1]
		local var_24_1 = tf(Instantiate(arg_23_0._heroInfoTpl))

		var_24_1.SetParent(arg_23_0._heroContainer, False)
		SetActive(var_24_1, True)
		arg_24_0.SetParent(var_24_1)
		arg_24_0.SetRaycastTarget(False)
		arg_24_0.SetLocalScale(Vector3(0.8, 0.8, 1))
		arg_24_0.SetLayer(Layer.UI)
		arg_24_0.modelRoot.transform.SetAsFirstSibling()

		if arg_23_0._heroInfoModifyCb != None:
			arg_23_0._heroInfoModifyCb(var_24_1, var_24_0, arg_24_0)

		local var_24_2 = arg_23_0.GenCharInfo(var_24_1, arg_24_0)
		local var_24_3 = arg_23_0._characterList[arg_24_2]

		var_24_3[arg_24_3] = var_24_2

		local var_24_4, var_24_5, var_24_6 = arg_24_0.CreateInterface()

		arg_23_0._eventTriggers[var_24_6] = True

		pg.DelegateInfo.Add(arg_23_0, var_24_5.onLongPressed)

		var_24_5.longPressThreshold = 1

		var_24_5.onLongPressed.RemoveAllListeners()
		var_24_5.onLongPressed.AddListener(function()
			if arg_23_0._longPressCb != None:
				arg_23_0._longPressCb(var_24_1, var_24_0, arg_23_0._currentFleetVO, arg_24_2))
		pg.DelegateInfo.Add(arg_23_0, var_24_4.onModelClick)
		var_24_4.onModelClick.AddListener(function()
			if arg_23_0._click != None:
				arg_23_0._click(var_24_0, arg_24_2, arg_23_0._currentFleetVO))
		var_24_6.AddBeginDragFunc(function()
			if arg_23_0._modelDrag:
				return

			if arg_23_0._checkBeginDrag and not arg_23_0._checkBeginDrag(var_24_0, arg_24_2, arg_23_0._currentFleetVO):
				return

			arg_23_0._modelDrag = arg_24_0.modelRoot
			arg_23_0._currentDragDelegate = var_24_6

			LeanTween.cancel(arg_24_0.modelRoot)
			var_24_1.SetAsLastSibling()
			arg_23_0.SwitchToShiftMode(var_24_1, arg_24_2)
			arg_24_0.SetAction("tuozhuai")

			if arg_23_0._beginDrag:
				arg_23_0._beginDrag(var_24_1)

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_HOME_DRAG))
		var_24_6.AddDragFunc(function(arg_28_0, arg_28_1)
			if arg_23_0._modelDrag != arg_24_0.modelRoot:
				return

			var_24_1.localPosition = Vector3(arg_28_1.position.x * arg_23_0._widthRate - arg_23_0._halfWidth - arg_23_0._offset.x, arg_28_1.position.y * arg_23_0._heightRate - arg_23_0._halfHeight - arg_23_0._offset.y, -22))
		var_24_6.AddDragEndFunc(function(arg_29_0, arg_29_1)
			if arg_23_0._modelDrag != arg_24_0.modelRoot:
				return

			arg_23_0._modelDrag = False

			local var_29_0 = arg_23_0._forceDropCharacter

			arg_23_0._forceDropCharacter = None
			arg_23_0._currentDragDelegate = None

			arg_24_0.SetAction("stand")

			local function var_29_1()
				arg_23_0.SwitchToDisplayMode()
				arg_23_0.SortSiblingIndex()

				if arg_23_0._shiftOnly != None:
					arg_23_0._shiftOnly(arg_23_0._currentFleetVO)

			if var_29_0:
				var_29_1()

				return

			local function var_29_2()
				for iter_31_0, iter_31_1 in ipairs(var_24_3):
					if iter_31_1.heroInfoTF == var_24_1:
						iter_31_1.spineRole.Dispose()
						var_24_1.gameObject.Destroy()
						table.remove(var_24_3, iter_31_0)

						break

				arg_23_0.SwitchToDisplayMode()
				arg_23_0.SortSiblingIndex()

				if arg_23_0._removeShip != None:
					arg_23_0._removeShip(var_24_0, arg_23_0._currentFleetVO)

			local var_29_3, var_29_4 = arg_23_0.GetShipPos(arg_23_0._currentFleetVO, var_24_0)

			if arg_29_1.position.x < UnityEngine.Screen.width * 0.15 or arg_29_1.position.x > UnityEngine.Screen.width * 0.87 or arg_29_1.position.y < UnityEngine.Screen.height * 0.18 or arg_29_1.position.y > UnityEngine.Screen.height * 0.7:
				if arg_23_0._checkRemove != None:
					arg_23_0._checkRemove(var_29_1, var_29_2, var_24_0, arg_23_0._currentFleetVO, var_29_4)
			else
				var_29_1()

			if arg_23_0._endDrag != None:
				arg_23_0._endDrag(var_24_1)

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_HOME_PUT))
		arg_23_0.SetCharacterPos(arg_24_2, arg_24_3, var_24_2)

	local var_23_1 = {}

	local function var_23_2(arg_32_0, arg_32_1)
		for iter_32_0, iter_32_1 in ipairs(arg_32_0):
			table.insert(var_23_1, function(arg_33_0)
				local var_33_0 = SpineRole.New(arg_23_0._shipVOs[iter_32_1])

				var_33_0.Load(function()
					var_23_0(var_33_0, iter_32_1, arg_32_1, iter_32_0)
					arg_33_0(), None, var_33_0.ORBIT_KEY_UI))

	local var_23_3 = arg_23_0._currentFleetVO.getFleetType()

	if var_23_3 == FleetType.Normal:
		var_23_2(arg_23_0._currentFleetVO.getTeamByName(TeamType.Vanguard), TeamType.Vanguard)
		var_23_2(arg_23_0._currentFleetVO.getTeamByName(TeamType.Main), TeamType.Main)
	elif var_23_3 == FleetType.Submarine:
		var_23_2(arg_23_0._currentFleetVO.getTeamByName(TeamType.Submarine), TeamType.Submarine)

	pg.UIMgr.GetInstance().LoadingOn()
	parallelAsync(var_23_1, function(arg_35_0)
		pg.UIMgr.GetInstance().LoadingOff()

		if arg_23_0._exited:
			return

		arg_23_0.SortSiblingIndex()

		if arg_23_0._loadComplete:
			arg_23_0._loadComplete())

def var_0_0.GetShipPos(arg_36_0, arg_36_1, arg_36_2):
	if not arg_36_2:
		return

	local var_36_0 = arg_36_2.getTeamType()
	local var_36_1 = arg_36_1.getTeamByName(var_36_0)

	return table.indexof(var_36_1, arg_36_2.id) or -1, var_36_0

def var_0_0.SetAllCharacterPos(arg_37_0):
	local var_37_0 = {
		TeamType.Main,
		TeamType.Vanguard,
		TeamType.Submarine
	}

	_.each(var_37_0, function(arg_38_0)
		for iter_38_0, iter_38_1 in ipairs(arg_37_0._characterList[arg_38_0]):
			arg_37_0.SetCharacterPos(arg_38_0, iter_38_0, iter_38_1))

def var_0_0.SetCharacterPos(arg_39_0, arg_39_1, arg_39_2, arg_39_3):
	assert(arg_39_0._gridTFs[arg_39_1], "没有找到编队显示对象_teamType." .. tostring(arg_39_1))

	local var_39_0 = arg_39_3.heroInfoTF
	local var_39_1 = arg_39_3.spineRole
	local var_39_2 = var_39_1.modelRoot
	local var_39_3 = arg_39_0._gridTFs[arg_39_1][arg_39_2]
	local var_39_4 = var_39_3.localPosition

	LeanTween.cancel(var_39_2)

	var_39_0.localPosition = Vector3(var_39_4.x, var_39_4.y, -15 + var_39_4.z + arg_39_2)
	var_39_2.transform.localPosition = Vector3(0, 20, 0)

	LeanTween.moveY(rtf(var_39_2), 0, 0.5).setDelay(0.5)
	SetActive(var_39_3.Find("shadow"), True)
	var_39_1.SetAction("stand")
	var_39_1.resumeRole()

def var_0_0.ResetGrid(arg_40_0, arg_40_1, arg_40_2):
	if not arg_40_0._gridTFs[arg_40_1]:
		return

	local var_40_0 = arg_40_0._currentFleetVO.getTeamByName(arg_40_1)

	assert(var_40_0, arg_40_1)

	local var_40_1 = arg_40_0._gridTFs[arg_40_1]

	for iter_40_0, iter_40_1 in ipairs(var_40_1):
		SetActive(iter_40_1.Find("shadow"), False)
		SetActive(iter_40_1.Find("tip"), False)

	if arg_40_1 == TeamType.Main and #arg_40_0._currentFleetVO.getTeamByName(TeamType.Vanguard) == 0:
		return

	local var_40_2 = #var_40_0

	if var_40_2 < 3:
		local var_40_3 = var_40_1[var_40_2 + 1].Find("tip")

		var_40_3.GetComponent("Button").enabled = True

		onButton(arg_40_0, var_40_3, function()
			if arg_40_0._gridTipClick:
				arg_40_0._gridTipClick(arg_40_1, arg_40_0._currentFleetVO), SFX_PANEL)

		var_40_3.localScale = Vector3(0, 0, 1)

		if not arg_40_0._disableTip:
			SetActive(var_40_3, not arg_40_2)

		LeanTween.value(go(var_40_3), 0, 1, 1).setOnUpdate(System.Action_float(function(arg_42_0)
			var_40_3.localScale = Vector3(arg_42_0, arg_42_0, 1))).setEase(LeanTweenType.easeOutBack)

def var_0_0.SwitchToShiftMode(arg_43_0, arg_43_1, arg_43_2):
	assert(arg_43_0._gridTFs[arg_43_2], "没有找到编队显示对象_teamType." .. tostring(arg_43_2))

	if arg_43_0._switchToShiftModeHandler:
		arg_43_0._switchToShiftModeHandler()

	for iter_43_0 = 1, 3:
		local var_43_0 = {
			TeamType.Vanguard,
			TeamType.Main,
			TeamType.Submarine
		}

		_.each(var_43_0, function(arg_44_0)
			if arg_43_0._gridTFs[arg_44_0] and arg_43_0._gridTFs[arg_44_0][iter_43_0]:
				setActive(arg_43_0._gridTFs[arg_44_0][iter_43_0].Find("tip"), False))
		setActive(arg_43_0._gridTFs[arg_43_2][iter_43_0].Find("shadow"), False)

	local var_43_1 = arg_43_0._characterList[arg_43_2]

	for iter_43_1, iter_43_2 in ipairs(var_43_1):
		local var_43_2 = iter_43_2.heroInfoTF
		local var_43_3 = iter_43_2.spineRole
		local var_43_4 = var_43_3.modelRoot

		if var_43_2 != arg_43_1:
			LeanTween.moveY(rtf(var_43_4), var_43_4.transform.localPosition.y + 20, 0.5)

			local var_43_5, var_43_6, var_43_7 = var_43_3.GetInterface()

			arg_43_0._eventTriggers[var_43_7] = True

			var_43_7.AddPointEnterFunc(function()
				for iter_45_0, iter_45_1 in ipairs(var_43_1):
					if iter_45_1.heroInfoTF == var_43_2:
						seriesAsync({
							function(arg_46_0)
								if not arg_43_0._checkSwitch:
									return arg_46_0()

								arg_43_0._checkSwitch(arg_46_0, arg_43_0._shiftIndex, iter_45_0, arg_43_0._currentFleetVO, arg_43_2),
							function(arg_47_0)
								arg_43_0.Shift(arg_43_0._shiftIndex, iter_45_0, arg_43_2)
						})

						break)
		else
			arg_43_0._shiftIndex = iter_43_1

			var_43_3.DisableInterface()

		var_43_3.SetAction("normal")

def var_0_0.SwitchToDisplayMode(arg_48_0):
	if arg_48_0._switchToDisplayModeHandler:
		arg_48_0._switchToDisplayModeHandler()

	local function var_48_0(arg_49_0)
		for iter_49_0, iter_49_1 in ipairs(arg_49_0):
			local var_49_0 = iter_49_1.heroInfoTF
			local var_49_1 = iter_49_1.spineRole
			local var_49_2 = var_49_1.modelRoot
			local var_49_3, var_49_4, var_49_5 = var_49_1.GetInterface()

			if var_49_5:
				arg_48_0._eventTriggers[var_49_5] = True

				if var_49_5:
					var_49_5.RemovePointEnterFunc()

	arg_48_0.TurnOffPreviewMode()
	var_48_0(arg_48_0._characterList[TeamType.Vanguard])
	var_48_0(arg_48_0._characterList[TeamType.Main])
	var_48_0(arg_48_0._characterList[TeamType.Submarine])

	arg_48_0._shiftIndex = None

def var_0_0.SwitchToPreviewMode(arg_50_0):
	if arg_50_0._swtichToPreviewModeHandler:
		arg_50_0._swtichToPreviewModeHandler()

	arg_50_0.ResetGrid(TeamType.Vanguard, True)
	arg_50_0.ResetGrid(TeamType.Main, True)
	arg_50_0.ResetGrid(TeamType.Submarine, True)
	arg_50_0.SetAllCharacterPos()
	arg_50_0.SetEnableForSpineInterface(False)

def var_0_0.TurnOffPreviewMode(arg_51_0):
	arg_51_0.ResetGrid(TeamType.Vanguard)
	arg_51_0.ResetGrid(TeamType.Main)
	arg_51_0.ResetGrid(TeamType.Submarine)
	arg_51_0.SetAllCharacterPos()
	arg_51_0.SetEnableForSpineInterface(True)

def var_0_0.SetEnableForSpineInterface(arg_52_0, arg_52_1):
	local var_52_0 = {
		TeamType.Main,
		TeamType.Vanguard,
		TeamType.Submarine
	}

	_.each(var_52_0, function(arg_53_0)
		for iter_53_0, iter_53_1 in ipairs(arg_52_0._characterList[arg_53_0]):
			if arg_52_1:
				iter_53_1.spineRole.EnableInterface()
			else
				iter_53_1.spineRole.DisableInterface())

def var_0_0.Shift(arg_54_0, arg_54_1, arg_54_2, arg_54_3):
	assert(arg_54_0._gridTFs[arg_54_3], "没有找到编队显示对象_teamType." .. tostring(arg_54_3))

	local var_54_0 = arg_54_0._characterList[arg_54_3]
	local var_54_1 = arg_54_0._gridTFs[arg_54_3]
	local var_54_2 = var_54_0[arg_54_2]
	local var_54_3 = var_54_2.heroInfoTF
	local var_54_4 = var_54_2.spineRole.modelRoot
	local var_54_5 = var_54_1[arg_54_1].localPosition

	var_54_3.localPosition = Vector3(var_54_5.x, var_54_5.y + 20, -15 + var_54_5.z + arg_54_1)

	local var_54_6 = var_54_0[arg_54_1].spineRole.ship.id
	local var_54_7 = var_54_0[arg_54_2].spineRole.ship.id

	LeanTween.cancel(var_54_4)

	var_54_0[arg_54_1], var_54_0[arg_54_2] = var_54_0[arg_54_2], var_54_0[arg_54_1]

	arg_54_0._currentFleetVO.switchShip(arg_54_3, arg_54_1, arg_54_2, var_54_6, var_54_7)

	arg_54_0._shiftIndex = arg_54_2

def var_0_0.SortSiblingIndex(arg_55_0):
	local var_55_0 = 0
	local var_55_1 = {
		2,
		1,
		3
	}

	for iter_55_0, iter_55_1 in ipairs(var_55_1):
		local var_55_2 = arg_55_0._characterList[TeamType.Main][iter_55_1]

		if var_55_2:
			local var_55_3 = var_55_2.heroInfoTF

			tf(var_55_3).SetSiblingIndex(var_55_0)

			var_55_0 = var_55_0 + 1

	local var_55_4 = 3

	while var_55_4 > 0:
		local var_55_5 = arg_55_0._characterList[TeamType.Vanguard][var_55_4]

		if var_55_5:
			local var_55_6 = var_55_5.heroInfoTF

			tf(var_55_6).SetSiblingIndex(var_55_0)

			var_55_0 = var_55_0 + 1

		var_55_4 = var_55_4 - 1

	local var_55_7 = 3

	while var_55_7 > 0:
		local var_55_8 = arg_55_0._characterList[TeamType.Submarine][var_55_7]

		if var_55_8:
			local var_55_9 = var_55_8.heroInfoTF

			tf(var_55_9).SetSiblingIndex(var_55_0)

			var_55_0 = var_55_0 + 1

		var_55_7 = var_55_7 - 1

def var_0_0.UpdateGridVisibility(arg_56_0):
	local var_56_0 = arg_56_0._currentFleetVO.getFleetType()

	_.each(arg_56_0._gridTFs[TeamType.Main], function(arg_57_0)
		setActive(arg_57_0, var_56_0 == FleetType.Normal))
	_.each(arg_56_0._gridTFs[TeamType.Vanguard], function(arg_58_0)
		setActive(arg_58_0, var_56_0 == FleetType.Normal))
	_.each(arg_56_0._gridTFs[TeamType.Submarine], function(arg_59_0)
		setActive(arg_59_0, var_56_0 == FleetType.Submarine))

def var_0_0.RecycleCharacterList(arg_60_0, arg_60_1, arg_60_2):
	for iter_60_0, iter_60_1 in ipairs(arg_60_1):
		local var_60_0 = arg_60_2[iter_60_0]

		if var_60_0:
			var_60_0.spineRole.Dispose()

			arg_60_2[iter_60_0] = None

def var_0_0.Destroy(arg_61_0):
	arg_61_0._exited = True

	arg_61_0.RecycleCharacterList(arg_61_0._currentFleetVO.getTeamByName(TeamType.Main), arg_61_0._characterList[TeamType.Main])
	arg_61_0.RecycleCharacterList(arg_61_0._currentFleetVO.getTeamByName(TeamType.Vanguard), arg_61_0._characterList[TeamType.Vanguard])
	arg_61_0.RecycleCharacterList(arg_61_0._currentFleetVO.getTeamByName(TeamType.Submarine), arg_61_0._characterList[TeamType.Submarine])

	if arg_61_0._eventTriggers:
		for iter_61_0, iter_61_1 in pairs(arg_61_0._eventTriggers):
			ClearEventTrigger(iter_61_0)

		arg_61_0._eventTriggers = None

return var_0_0
