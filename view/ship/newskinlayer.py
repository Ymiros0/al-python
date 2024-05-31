local var_0_0 = class("NewSkinLayer", import("..base.BaseUI"))

var_0_0.PAINT_DURATION = 0.35
var_0_0.STAR_DURATION = 0.5

local var_0_1 = 19

def var_0_0.getUIName(arg_1_0):
	return "NewSkinUI"

def var_0_0.preload(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0.contextData.skinId
	local var_2_1 = pg.ship_skin_template[var_2_0]
	local var_2_2 = var_2_1.ship_group
	local var_2_3 = var_2_2 * 10 + 1
	local var_2_4 = pg.ship_data_statistics[var_2_3]
	local var_2_5

	if var_2_1.bg_sp and var_2_1.bg_sp != "":
		var_2_5 = var_2_1.bg_sp
	else
		var_2_5 = var_2_1.bg and #var_2_1.bg > 0 and var_2_1.bg or var_2_1.rarity_bg and #var_2_1.rarity_bg > 0 and var_2_1.rarity_bg

	local var_2_6

	var_2_6 = var_2_5 and "bg/star_level_bg_" .. var_2_5 or "newshipbg/bg_" .. shipRarity2bgPrint(var_2_4.rarity, ShipGroup.IsBluePrintGroup(var_2_2), ShipGroup.IsMetaGroup(var_2_2))

	GetSpriteFromAtlasAsync(var_2_6, "", arg_2_1)

def var_0_0.setShipVOs(arg_3_0, arg_3_1):
	arg_3_0.shipVOs = arg_3_1
	arg_3_0.sameShipVOs = arg_3_0.getSameGroupShips()

def var_0_0.init(arg_4_0):
	arg_4_0._shake = arg_4_0.findTF("shake_panel")
	arg_4_0._shade = arg_4_0.findTF("shade")
	arg_4_0._bg = arg_4_0._shake.Find("bg")
	arg_4_0._staticBg = arg_4_0._bg.Find("static_bg")
	arg_4_0._paintingTF = arg_4_0._shake.Find("paint")
	arg_4_0._dialogue = arg_4_0._shake.Find("dialogue")
	arg_4_0._skinName = arg_4_0._dialogue.Find("name").GetComponent(typeof(Text))
	arg_4_0._left = arg_4_0._shake.Find("left_panel")
	arg_4_0._viewBtn = arg_4_0._left.Find("view_btn")
	arg_4_0._shareBtn = arg_4_0._left.Find("share_btn")
	arg_4_0.clickTF = arg_4_0._shake.Find("click")
	arg_4_0.newTF = arg_4_0._shake.Find("New")
	arg_4_0.timelimit = arg_4_0._shake.Find("timelimit")

	setActive(arg_4_0.newTF, False)

	arg_4_0.changeSkinBtn = arg_4_0.findTF("set_skin_btn", arg_4_0._shake)
	arg_4_0.selectPanel = arg_4_0.findTF("select_ship_panel")
	arg_4_0.selectPanelCloseBtn = arg_4_0.findTF("window/top/btnBack", arg_4_0.selectPanel)
	arg_4_0.shipContent = arg_4_0.findTF("window/sliders/scroll_rect/content", arg_4_0.selectPanel)
	arg_4_0.shipCardTpl = arg_4_0._tf.GetComponent("ItemList").prefabItem[0]
	arg_4_0.confirmChangeBtn = arg_4_0.findTF("window/exchange_btn", arg_4_0.selectPanel)
	arg_4_0.flagShipToggle = arg_4_0.findTF("window/flag_ship", arg_4_0.selectPanel)

	setActive(arg_4_0.selectPanel, False)

	arg_4_0.isTimeLimit = arg_4_0.contextData.timeLimit

	setActive(arg_4_0.timelimit, arg_4_0.isTimeLimit)
	pg.UIMgr.GetInstance().OverlayPanel(arg_4_0._tf, {
		weight = LayerWeightConst.SECOND_LAYER
	})

	arg_4_0.isLoadBg = False

def var_0_0.voice(arg_5_0, arg_5_1):
	if not arg_5_1:
		return

	arg_5_0.stopVoice()

	arg_5_0._currentVoice = arg_5_1

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_5_1)

def var_0_0.stopVoice(arg_6_0):
	if arg_6_0._currentVoice:
		pg.CriMgr.GetInstance().UnloadSoundEffect_V3(arg_6_0._currentVoice)

	arg_6_0._currentVoice = None

def var_0_0.setSkin(arg_7_0, arg_7_1):
	arg_7_0.cg = GetOrAddComponent(arg_7_0._tf, typeof(CanvasGroup))
	arg_7_0.cg.alpha = 0

	setActive(arg_7_0._shade, True)

	arg_7_0._shade.GetComponent(typeof(Image)).color = Color.New(0, 0, 0, 1)

	local var_7_0 = "star_level_unlock_anim_" .. arg_7_1

	if checkABExist("ui/skinunlockanim/" .. var_7_0):
		arg_7_0.playOpening(function()
			arg_7_0.setSkinPri(arg_7_1), var_7_0)
	else
		arg_7_0.setSkinPri(arg_7_1)

def var_0_0.setSkinPri(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.loadUISync("getrole")

	var_9_0.layer = LayerMask.NameToLayer("UI")
	var_9_0.transform.localPosition = Vector3(0, 0, -10)

	setParent(var_9_0, arg_9_0._tf, False)
	setActive(var_9_0, False)
	onNextTick(function()
		setActive(var_9_0, True))
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_DOCKYARD_CHARGET)

	arg_9_0.cg.alpha = 1
	arg_9_0._shade.GetComponent(typeof(Image)).color = Color.New(0, 0, 0, 0)

	arg_9_0.recyclePainting()

	arg_9_0._skinConfig = pg.ship_skin_template[arg_9_1]

	local var_9_1 = pg.ship_skin_template[arg_9_1].ship_group
	local var_9_2 = pg.ship_data_statistics[arg_9_0._skinConfig.ship_group * 10 + 1]
	local var_9_3

	if arg_9_0._skinConfig.bg_sp and arg_9_0._skinConfig.bg_sp != "":
		var_9_3 = arg_9_0._skinConfig.bg_sp
	else
		var_9_3 = arg_9_0._skinConfig.bg and #arg_9_0._skinConfig.bg > 0 and arg_9_0._skinConfig.bg or arg_9_0._skinConfig.rarity_bg and #arg_9_0._skinConfig.rarity_bg > 0 and arg_9_0._skinConfig.rarity_bg

	if var_9_3:
		pg.DynamicBgMgr.GetInstance().LoadBg(arg_9_0, var_9_3, arg_9_0._bg, arg_9_0._staticBg, function(arg_11_0)
			arg_9_0.isLoadBg = True, function(arg_12_0)
			arg_9_0.isLoadBg = True)
	else
		local var_9_4 = "newshipbg/bg_" .. shipRarity2bgPrint(var_9_2.rarity, ShipGroup.IsBluePrintGroup(var_9_1), ShipGroup.IsMetaGroup(var_9_1))

		GetSpriteFromAtlasAsync(var_9_4, "", function(arg_13_0)
			setImageSprite(arg_9_0._staticBg, arg_13_0, True)

			arg_9_0.isLoadBg = True)

	setPaintingPrefabAsync(arg_9_0._paintingTF, arg_9_0._skinConfig.painting, "huode")

	arg_9_0._skinName.text = i18n("ship_newSkin_name", arg_9_0._skinConfig.name)

	local var_9_5
	local var_9_6 = ""
	local var_9_7
	local var_9_8 = ShipWordHelper.RawGetWord(arg_9_1, ShipWordHelper.WORD_TYPE_UNLOCK)

	if var_9_8 == "":
		local var_9_9

		var_9_9, var_9_7, var_9_8 = ShipWordHelper.GetWordAndCV(arg_9_1, ShipWordHelper.WORD_TYPE_DROP)
	else
		local var_9_10

		var_9_10, var_9_7, var_9_8 = ShipWordHelper.GetWordAndCV(arg_9_1, ShipWordHelper.WORD_TYPE_UNLOCK)

	setWidgetText(arg_9_0._dialogue, SwitchSpecialChar(var_9_8, True), "desc/Text")

	arg_9_0._dialogue.transform.localScale = Vector3(0, 1, 1)

	SetActive(arg_9_0._dialogue, False)
	SetActive(arg_9_0._dialogue, True)
	LeanTween.scale(arg_9_0._dialogue, Vector3(1, 1, 1), 0.1).setOnComplete(System.Action(function()
		setActive(arg_9_0._shade, False)
		setActive(arg_9_0.clickTF, True)
		arg_9_0.voice(var_9_7)))

def var_0_0.showExitTip(arg_15_0):
	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		content = i18n("give_up_cloth_change"),
		def onYes:()
			arg_15_0.emit(var_0_0.ON_CLOSE)
	})

def var_0_0.didEnter(arg_17_0):
	local var_17_0 = ShipWordHelper.GetDefaultSkin(arg_17_0.contextData.skinId)

	arg_17_0.shipName = pg.ship_skin_template[var_17_0].name

	onButton(arg_17_0, arg_17_0._viewBtn, function()
		arg_17_0.isInView = True

		arg_17_0.paintView()
		setActive(arg_17_0.clickTF, False), SFX_PANEL)
	onButton(arg_17_0, arg_17_0._shareBtn, function()
		pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeNewSkin, None, {
			weight = LayerWeightConst.TOP_LAYER
		}), SFX_PANEL)
	onButton(arg_17_0, arg_17_0.clickTF, function()
		if arg_17_0.isInView or not arg_17_0.isLoadBg:
			return

		arg_17_0.showExitTip(), SFX_CANCEL)
	onButton(arg_17_0, arg_17_0.selectPanel, function()
		arg_17_0.closeSelectPanel(), SFX_PANEL)

	local var_17_1 = getProxy(SettingsProxy).GetSetFlagShip()

	onToggle(arg_17_0, arg_17_0.flagShipToggle, function(arg_22_0)
		arg_17_0.flagShipMark = arg_22_0, SFX_PANEL)
	triggerToggle(arg_17_0.flagShipToggle, var_17_1)
	arg_17_0.onSwitch(arg_17_0.changeSkinBtn, table.getCount(arg_17_0.sameShipVOs) > 0)

def var_0_0.onBackPressed(arg_23_0):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	if arg_23_0.isInView:
		arg_23_0.hidePaintView(True)

		return

	if isActive(arg_23_0.selectPanel):
		arg_23_0.closeSelectPanel()

		return

	if isActive(arg_23_0.clickTF):
		triggerButton(arg_23_0.clickTF)

def var_0_0.onSwitch(arg_24_0, arg_24_1, arg_24_2):
	onButton(arg_24_0, arg_24_1, function()
		if arg_24_2:
			arg_24_0.openSelectPanel()
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("err_cloth_change_noship", arg_24_0.shipName)))

def var_0_0.getSameGroupShips(arg_26_0):
	local var_26_0 = {}
	local var_26_1 = arg_26_0.contextData.skinId
	local var_26_2 = pg.ship_skin_template[var_26_1].ship_group

	for iter_26_0, iter_26_1 in pairs(arg_26_0.shipVOs):
		if iter_26_1.groupId == var_26_2:
			var_26_0[iter_26_1.id] = iter_26_1

	local var_26_3 = getProxy(BayProxy).CanUseShareSkinShips(var_26_1)

	for iter_26_2, iter_26_3 in ipairs(var_26_3):
		var_26_0[iter_26_3.id] = iter_26_3

	return var_26_0

def var_0_0.paintView(arg_27_0):
	local var_27_0 = {}
	local var_27_1 = arg_27_0._shake.childCount
	local var_27_2 = 0

	while var_27_2 < var_27_1:
		local var_27_3 = arg_27_0._shake.GetChild(var_27_2)

		if var_27_3.gameObject.activeSelf and var_27_3 != arg_27_0._paintingTF and var_27_3 != arg_27_0._bg:
			var_27_0[#var_27_0 + 1] = var_27_3

			setActive(var_27_3, False)

		var_27_2 = var_27_2 + 1

	openPortrait()

	local var_27_4 = arg_27_0._paintingTF
	local var_27_5 = var_27_4.anchoredPosition.x
	local var_27_6 = var_27_4.anchoredPosition.y
	local var_27_7 = var_27_4.rect.width
	local var_27_8 = var_27_4.rect.height
	local var_27_9 = arg_27_0._tf.rect.width / UnityEngine.Screen.width
	local var_27_10 = arg_27_0._tf.rect.height / UnityEngine.Screen.height
	local var_27_11 = var_27_7 / 2
	local var_27_12 = var_27_8 / 2
	local var_27_13
	local var_27_14

	if not LeanTween.isTweening(go(var_27_4)):
		LeanTween.moveX(rtf(var_27_4), 150, 0.5).setEase(LeanTweenType.easeInOutSine)

	local var_27_15 = GetOrAddComponent(arg_27_0._bg, "MultiTouchZoom")

	var_27_15.SetZoomTarget(arg_27_0._paintingTF)

	local var_27_16 = GetOrAddComponent(arg_27_0._bg, "EventTriggerListener")
	local var_27_17 = True

	var_27_15.enabled = True
	var_27_16.enabled = True

	local var_27_18 = False

	var_27_16.AddPointDownFunc(function(arg_28_0)
		if Input.touchCount == 1 or IsUnityEditor:
			var_27_18 = True
			var_27_17 = True
		elif Input.touchCount >= 2:
			var_27_17 = False
			var_27_18 = False)
	var_27_16.AddPointUpFunc(function(arg_29_0)
		if Input.touchCount <= 2:
			var_27_17 = True)
	var_27_16.AddBeginDragFunc(function(arg_30_0, arg_30_1)
		var_27_18 = False
		var_27_13 = arg_30_1.position.x * var_27_9 - var_27_11 - tf(arg_27_0._paintingTF).localPosition.x
		var_27_14 = arg_30_1.position.y * var_27_10 - var_27_12 - tf(arg_27_0._paintingTF).localPosition.y)
	var_27_16.AddDragFunc(function(arg_31_0, arg_31_1)
		if var_27_17:
			local var_31_0 = tf(arg_27_0._paintingTF).localPosition

			tf(arg_27_0._paintingTF).localPosition = Vector3(arg_31_1.position.x * var_27_9 - var_27_11 - var_27_13, arg_31_1.position.y * var_27_10 - var_27_12 - var_27_14, -22))
	onButton(arg_27_0, arg_27_0._bg, function()
		arg_27_0.hidePaintView(), SFX_CANCEL)

	function var_0_0.hidePaintView(arg_33_0, arg_33_1)
		if not arg_33_1 and not var_27_18:
			return

		var_27_16.enabled = False
		var_27_15.enabled = False

		RemoveComponent(arg_33_0._bg, "Button")

		for iter_33_0, iter_33_1 in ipairs(var_27_0):
			setActive(iter_33_1, True)

		closePortrait()
		LeanTween.cancel(go(arg_33_0._paintingTF))

		arg_33_0._paintingTF.localScale = Vector3(1, 1, 1)

		setAnchoredPosition(arg_33_0._paintingTF, {
			x = var_27_5,
			y = var_27_6
		})

		arg_33_0.isInView = False

		setActive(arg_33_0.clickTF, True)

def var_0_0.recyclePainting(arg_34_0):
	if arg_34_0._shipVO:
		retPaintingPrefab(arg_34_0._paintingTF, arg_34_0._shipVO.getPainting())

def var_0_0.openSelectPanel(arg_35_0):
	removeAllChildren(arg_35_0.shipContent)

	arg_35_0.isOpenSelPanel = True
	arg_35_0.selectIds = {}

	setActive(arg_35_0.selectPanel, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_35_0.selectPanel, False, {
		weight = LayerWeightConst.TOP_LAYER
	})

	arg_35_0.shipCards = {}

	local var_35_0 = {}

	for iter_35_0, iter_35_1 in pairs(arg_35_0.sameShipVOs):
		table.insert(var_35_0, iter_35_1)

	table.sort(var_35_0, function(arg_36_0, arg_36_1)
		if arg_36_0.level == arg_36_1.level:
			local var_36_0 = arg_36_0.getStar()
			local var_36_1 = arg_36_1.getStar()

			if var_36_0 == var_36_1:
				local var_36_2 = arg_36_0.inFleet and 1 or 0
				local var_36_3 = arg_36_1.inFleet and 1 or 0

				if var_36_2 == var_36_3:
					return arg_36_0.createTime < arg_36_1.createTime
				else
					return var_36_3 < var_36_2
			else
				return var_36_1 < var_36_0
		else
			return arg_36_0.level > arg_36_1.level)

	for iter_35_2, iter_35_3 in ipairs(var_35_0):
		local var_35_1 = cloneTplTo(arg_35_0.shipCardTpl, arg_35_0.shipContent)
		local var_35_2 = ShipDetailCard.New(var_35_1.gameObject)

		var_35_2.update(iter_35_3, arg_35_0.contextData.skinId)

		arg_35_0.shipCards[iter_35_3.id] = var_35_2

		onToggle(arg_35_0, var_35_2.tr, function(arg_37_0)
			var_35_2.updateSelected(arg_37_0)

			if arg_37_0:
				table.insert(arg_35_0.selectIds, var_35_2.shipVO.id)
			else
				for iter_37_0, iter_37_1 in pairs(arg_35_0.selectIds):
					if iter_37_1 == var_35_2.shipVO.id:
						table.remove(arg_35_0.selectIds, iter_37_0)

						break)

	onButton(arg_35_0, arg_35_0.confirmChangeBtn, function()
		if not arg_35_0.selectIds or #arg_35_0.selectIds <= 0:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("new_skin_no_choose"),
				weight = LayerWeightConst.TOP_LAYER + 1,
				def onYes:()
					arg_35_0.emit(var_0_0.ON_CLOSE)
			})

			return

		arg_35_0.emit(NewSkinMediator.SET_SKIN, arg_35_0.selectIds, arg_35_0.flagShipMark))
	onButton(arg_35_0, arg_35_0.selectPanelCloseBtn, function()
		arg_35_0.closeSelectPanel())

def var_0_0.updateShipCards(arg_41_0):
	for iter_41_0, iter_41_1 in pairs(arg_41_0.shipCards or {}):
		local var_41_0 = arg_41_0.sameShipVOs[iter_41_0]

		if var_41_0:
			iter_41_1.update(var_41_0, arg_41_0.contextData.skinId)

def var_0_0.closeSelectPanel(arg_42_0):
	if arg_42_0.isOpenSelPanel:
		arg_42_0.isOpenSelPanel = None

		setActive(arg_42_0.selectPanel, False)
		pg.UIMgr.GetInstance().UnblurPanel(arg_42_0.selectPanel, arg_42_0._tf)

def var_0_0.playOpening(arg_43_0, arg_43_1, arg_43_2):
	pg.CpkPlayMgr.GetInstance().PlayCpkMovie(function()
		return, function()
		if arg_43_1:
			arg_43_1(), "ui/skinunlockanim", arg_43_2, False, False, {
		weight = LayerWeightConst.THIRD_LAYER
	})

def var_0_0.willExit(arg_46_0):
	pg.CpkPlayMgr.GetInstance().DisposeCpkMovie()

	local var_46_0 = arg_46_0._skinConfig.ship_group * 10 + 1
	local var_46_1 = pg.ship_data_statistics[var_46_0]

	pg.TipsMgr.GetInstance().ShowTips(i18n("ship_newSkinLayer_get", var_46_1.name, arg_46_0._skinConfig.name), COLOR_GREEN)
	arg_46_0.recyclePainting()
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_46_0._tf)
	arg_46_0.stopVoice()

	if arg_46_0.loadedCVBankName:
		pg.CriMgr.UnloadCVBank(arg_46_0.loadedCVBankName)

		arg_46_0.loadedCVBankName = None

	arg_46_0.closeSelectPanel()
	cameraPaintViewAdjust(False)

return var_0_0
