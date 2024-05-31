local var_0_0 = class("NewDodgemResultGradePage", import("..NewBattleResultGradePage"))

def var_0_0.LoadBG(arg_1_0, arg_1_1):
	local var_1_0 = "CommonBg"

	ResourceMgr.Inst.getAssetAsync("BattleResultItems/" .. var_1_0, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_2_0)
		if arg_1_0.exited or IsNil(arg_2_0):
			if arg_1_1:
				arg_1_1()

			return

		Object.Instantiate(arg_2_0, arg_1_0.bgTr).transform.SetAsFirstSibling()

		if arg_1_1:
			arg_1_1()), False, False)

def var_0_0.RegisterEvent(arg_3_0, arg_3_1):
	seriesAsync({
		function(arg_4_0)
			var_0_0.super.RegisterEvent(arg_3_0, arg_4_0),
		function(arg_5_0)
			removeOnButton(arg_3_0._tf)
			arg_3_0.LoadPainitingContainer(arg_5_0),
		function(arg_6_0)
			arg_3_0.MovePainting(arg_6_0)
	}, function()
		onButton(arg_3_0, arg_3_0._tf, function()
			arg_3_1(), SFX_PANEL))

def var_0_0.MovePainting(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.paintingTr.parent

	LeanTween.value(var_9_0.gameObject, 2500, 587, 0.3).setOnUpdate(System.Action_float(function(arg_10_0)
		var_9_0.localPosition = Vector3(arg_10_0, 0, 0))).setOnComplete(System.Action(arg_9_1))

	local var_9_1 = Vector2(-247, 213)
	local var_9_2 = arg_9_0.gradePanel.anchoredPosition

	LeanTween.value(arg_9_0.gradePanel.gameObject, var_9_2, var_9_2 + var_9_1, 0.29).setOnUpdate(System.Action_UnityEngine_Vector2(function(arg_11_0)
		arg_9_0.gradePanel.anchoredPosition3D = Vector3(arg_11_0.x, arg_11_0.y, 0)))

def var_0_0.GetGetObjectives(arg_12_0):
	local var_12_0 = arg_12_0.contextData
	local var_12_1 = {}
	local var_12_2 = var_12_0.statistics.dodgemResult
	local var_12_3 = i18n("battle_result_total_score")

	table.insert(var_12_1, {
		text = setColorStr(var_12_3, "#FFFFFFFF"),
		value = setColorStr(var_12_2.score, COLOR_BLUE)
	})

	local var_12_4 = i18n("battle_result_max_combo")

	table.insert(var_12_1, {
		text = setColorStr(var_12_4, "#FFFFFFFF"),
		value = setColorStr(var_12_2.maxCombo, COLOR_YELLOW)
	})

	return var_12_1

def var_0_0.LoadPainitingContainer(arg_13_0, arg_13_1):
	ResourceMgr.Inst.getAssetAsync("BattleResultItems/Painting", "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_14_0)
		if arg_13_0.exited:
			return

		local var_14_0 = Object.Instantiate(arg_14_0, arg_13_0.bgTr)

		arg_13_0.UpdatePainting(var_14_0, arg_13_1)), True, True)

def var_0_0.UpdatePainting(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = arg_15_1.transform.Find("painting")
	local var_15_1 = arg_15_0.GetFlagShip()
	local var_15_2 = var_15_1.getPainting()

	setPaintingPrefabAsync(var_15_0, var_15_2, "biandui", function()
		ShipExpressionHelper.SetExpression(findTF(var_15_0, "fitter").GetChild(0), var_15_2, ShipWordHelper.WORD_TYPE_MVP)
		arg_15_2())
	arg_15_0.DisplayShipDialogue(arg_15_1.transform.Find("chat"), var_15_1)

	arg_15_0.paintingTr = var_15_0
	arg_15_1.transform.localPosition = Vector3(2500, 0, 0)

	arg_15_1.transform.SetSiblingIndex(2)
	setActive(arg_15_0.objectiveContainer.parent, False)

def var_0_0.DisplayShipDialogue(arg_17_0, arg_17_1, arg_17_2):
	local var_17_0
	local var_17_1
	local var_17_2

	if arg_17_0.contextData.score > 1:
		local var_17_3, var_17_4

		var_17_3, var_17_4, var_17_1 = ShipWordHelper.GetWordAndCV(arg_17_2.skinId, ShipWordHelper.WORD_TYPE_MVP)
	else
		local var_17_5, var_17_6

		var_17_5, var_17_6, var_17_1 = ShipWordHelper.GetWordAndCV(arg_17_2.skinId, ShipWordHelper.WORD_TYPE_LOSE)

	local var_17_7 = arg_17_1.Find("Text").GetComponent(typeof(Text))

	var_17_7.text = var_17_1
	var_17_7.alignment = #var_17_1 > CHAT_POP_STR_LEN and TextAnchor.MiddleLeft or TextAnchor.MiddleCenter

def var_0_0.GetFlagShip(arg_18_0):
	return Ship.New({
		id = 9999,
		configId = 205021,
		skin_id = 205020
	})

def var_0_0.OnDestroy(arg_19_0):
	if arg_19_0.paintingTr:
		local var_19_0 = arg_19_0.GetFlagShip()

		retPaintingPrefab(arg_19_0.paintingTr, var_19_0.getPainting())

	var_0_0.super.OnDestroy(arg_19_0)

return var_0_0
