local var_0_0 = class("ProposeUI", import("..base.BaseUI"))
local var_0_1 = {
	1,
	2,
	3,
	4,
	4,
	5,
	5,
	7,
	7,
	7,
	7,
	6,
	7
}

var_0_0.nationSpriteIndex = {
	cn = 5,
	de = 4,
	cm = 0,
	jp = 3,
	np = 9,
	sn = 6,
	en = 2,
	um = 11,
	mnf = 8,
	bili = 10,
	ff = 7,
	us = 1
}

def var_0_0.getUIName(arg_1_0):
	return "ProposeUI"

def var_0_0.setShip(arg_2_0, arg_2_1):
	arg_2_0.shipVO = arg_2_1
	arg_2_0.proposeType = arg_2_0.shipVO.getProposeType()

	arg_2_0.setShipGroupID(arg_2_0.shipVO.getGroupId())

def var_0_0.setShipGroupID(arg_3_0, arg_3_1):
	arg_3_0.shipGroupID = arg_3_1

def var_0_0.setWeddingReviewSkinID(arg_4_0, arg_4_1):
	arg_4_0.reviewSkinID = arg_4_1

def var_0_0.setBagProxy(arg_5_0, arg_5_1):
	arg_5_0.bagProxy = arg_5_1

def var_0_0.setPlayer(arg_6_0, arg_6_1):
	arg_6_0.player = arg_6_1

def var_0_0.init(arg_7_0):
	arg_7_0.storybg = arg_7_0.findTF("close/bg")
	arg_7_0.bgAdd = arg_7_0.findTF("add")

	setActive(arg_7_0.storybg, False)
	setActive(arg_7_0.bgAdd, False)

	arg_7_0.targetActorTF = arg_7_0.findTF("actor_middle")
	arg_7_0.maskTF = arg_7_0.findTF("mask")
	arg_7_0.skipBtn = arg_7_0.findTF("skip_button")
	arg_7_0.actorPainting = None
	arg_7_0.materialFace = arg_7_0._tf.Find("Resource/face").GetComponent(typeof(Image)).material
	arg_7_0.materialPaint = arg_7_0._tf.Find("Resource/paint").GetComponent(typeof(Image)).material
	arg_7_0.finishCallback = arg_7_0.contextData.finishCallback
	arg_7_0.commonTF = GameObject.Find("OverlayCamera/Overlay/UIMain/common")
	arg_7_0.exchangePanel = arg_7_0._tf.Find("exchange_panel")

	local var_7_0 = arg_7_0.exchangePanel.Find("window/msg_panel/content")

	setText(var_7_0.Find("text"), i18n("word_propose_cost_tip2"))

	local var_7_1 = pg.gameset.vow_prop_conversion.description

	for iter_7_0, iter_7_1 in ipairs(var_7_1):
		local var_7_2 = Drop.New({
			count = 1,
			type = DROP_TYPE_ITEM,
			id = iter_7_1
		})

		updateDrop(var_7_0.Find("icon_" .. iter_7_0), var_7_2)
		onButton(arg_7_0, var_7_0.Find("icon_" .. iter_7_0), function()
			arg_7_0.emit(BaseUI.ON_DROP, var_7_2), SFX_PANEL)

	onButton(arg_7_0, arg_7_0.exchangePanel.Find("bg"), function()
		arg_7_0.hideExchangePanel(), SFX_CANCEL)
	onButton(arg_7_0, arg_7_0.exchangePanel.Find("window/top/btnBack"), function()
		arg_7_0.hideExchangePanel(), SFX_CANCEL)
	onButton(arg_7_0, arg_7_0.exchangePanel.Find("window/button_container/cancel"), function()
		arg_7_0.hideExchangePanel(), SFX_CANCEL)
	onButton(arg_7_0, arg_7_0.exchangePanel.Find("window/button_container/confirm"), function()
		if getProxy(BagProxy).getItemCountById(ITEM_ID_FOR_PROPOSE) > 0:
			arg_7_0.emit(ProposeMediator.EXCHANGE_TIARA)
		else
			ItemTipPanel.ShowRingBuyTip()

		arg_7_0.hideExchangePanel(), SFX_CONFIRM)

	arg_7_0.tweenList = {}

def var_0_0.didEnter(arg_13_0):
	arg_13_0.emit(ProposeMediator.HIDE_SHIP_MAIN_WORD)

	if arg_13_0.commonTF:
		setActive(arg_13_0.commonTF, False)

	if arg_13_0.contextData.review:
		arg_13_0.weddingReview = True
		arg_13_0.proposeType = arg_13_0.contextData.group.getProposeType()

		local var_13_0 = arg_13_0.contextData.group.getNation()

		arg_13_0.bgName = Nation.Nation2BG(var_13_0) or Nation.Nation2BG(0)

		onButton(arg_13_0, arg_13_0.skipBtn, function()
			arg_13_0.closeView(), SFX_CANCEL)
		pg.UIMgr.GetInstance().BlurPanel(arg_13_0._tf)
		arg_13_0.doPlay()
	else
		arg_13_0.doMain()

def var_0_0.doPlay(arg_15_0):
	setActive(arg_15_0.skipBtn, arg_15_0.weddingReview)
	arg_15_0.setMask(True)
	pg.BgmMgr.GetInstance().TempPlay("wedding")
	arg_15_0.showProposePanel()

def var_0_0.doMain(arg_16_0):
	onButton(arg_16_0, arg_16_0.skipBtn, function()
		arg_16_0.closeView(), SFX_CANCEL)
	onButton(arg_16_0, arg_16_0.findTF("close0"), function()
		if arg_16_0.proposeEndFlag:
			arg_16_0.DisplayRenamePanel()
		else
			arg_16_0.closeView(), SFX_CANCEL)
	onButton(arg_16_0, arg_16_0.findTF("close_end"), function()
		if arg_16_0.proposeEndFlag:
			arg_16_0.DisplayRenamePanel()
		else
			arg_16_0.closeView(), SFX_CANCEL)

	local var_16_0 = arg_16_0.shipVO.getConfigTable().nationality
	local var_16_1 = "Propose" .. Nation.Nation2Side(var_16_0) .. "UI"

	arg_16_0.bgName = Nation.Nation2BG(var_16_0) or Nation.Nation2BG(0)

	PoolMgr.GetInstance().GetUI(var_16_1, True, function(arg_20_0)
		if arg_16_0.exited:
			PoolMgr.GetInstance().ReturnUI(var_16_1, arg_20_0)

			return

		arg_16_0.window = tf(arg_20_0)

		setParent(tf(arg_20_0), arg_16_0.findTF("window"))

		arg_16_0.intimacyTF = arg_16_0.findTF("intimacy/icon", arg_16_0.window)
		arg_16_0.intimacyValueTF = arg_16_0.findTF("intimacy/value", arg_16_0.window)
		arg_16_0.button = arg_16_0.findTF("button", arg_16_0.window)
		arg_16_0.intimacyDesc = arg_16_0.findTF("desc", arg_16_0.window)
		arg_16_0.intimacydescTime = arg_16_0.findTF("descPic/desc_time", arg_16_0.window)
		arg_16_0.intimacyDescPic = arg_16_0.findTF("descPic", arg_16_0.window)
		arg_16_0.intimacyBuffDesc = arg_16_0.findTF("desc_buff", arg_16_0.window)
		arg_16_0._paintingTF = arg_16_0.findTF("paintMask/paint", arg_16_0.window)
		arg_16_0.intimacyAchieved = arg_16_0.findTF("intimacy/achieved", arg_16_0.window)
		arg_16_0.intimacyNoAchieved = arg_16_0.findTF("intimacy/no_achieved", arg_16_0.window)
		arg_16_0.ringAchieved = arg_16_0.findTF("ringCount/achieved", arg_16_0.window)
		arg_16_0.ringNoAchieved = arg_16_0.findTF("ringCount/no_achieved", arg_16_0.window)
		arg_16_0.ringValue = arg_16_0.findTF("ringCount/value", arg_16_0.window)
		arg_16_0.nameTF = arg_16_0.findTF("title1/Text", arg_16_0.window)
		arg_16_0.shipNameTF = arg_16_0.findTF("title2/Text", arg_16_0.window)
		arg_16_0.campTF = arg_16_0.findTF("Camp", arg_16_0.window)
		arg_16_0.doneTF = arg_16_0.findTF("done", arg_16_0.window)
		arg_16_0.CampSprite = arg_16_0.findTF("CampSprite", arg_16_0.window)

		setActive(arg_16_0.window, True)
		setText(arg_16_0.nameTF, arg_16_0.player.name)
		setText(arg_16_0.shipNameTF, arg_16_0.shipVO.getName())

		if arg_16_0.CampSprite:
			local var_20_0 = getImageSprite(arg_16_0.findTF(Nation.Nation2Print(var_16_0), arg_16_0.CampSprite))

			if not var_20_0:
				warning("找不到印花, shipConfigId. " .. arg_16_0.shipVO.configId)
				setActive(arg_16_0.campTF, False)
			else
				setImageSprite(arg_16_0.campTF, var_20_0, False)
				setActive(arg_16_0.campTF, True)

		setIntimacyIcon(arg_16_0.intimacyTF, arg_16_0.shipVO.getIntimacyIcon())

		local var_20_1, var_20_2 = arg_16_0.shipVO.getIntimacyDetail()

		setText(arg_16_0.intimacyValueTF, i18n("propose_intimacy_tip", var_20_2))

		if var_20_2 >= 100:
			setTextColor(arg_16_0.intimacyValueTF, Color.white)
		else
			setTextColor(arg_16_0.intimacyValueTF, Color.New(0.5843137254901961, 0.5215686274509804, 0.40784313725490196))

		setActive(arg_16_0.intimacyAchieved, arg_16_0.shipVO.propose or var_20_2 >= 100)
		setActive(arg_16_0.intimacyNoAchieved, var_20_2 < 100 and not arg_16_0.shipVO.propose)
		arg_16_0.onUpdateItemCount()
		setActive(arg_16_0.doneTF, arg_16_0.shipVO.propose)

		local var_20_3, var_20_4 = arg_16_0.shipVO.getIntimacyInfo()

		if arg_16_0.shipVO.propose:
			if arg_16_0.intimacyDescPic:
				setActive(arg_16_0.intimacyDescPic, True)
				arg_16_0.onUpdateIntimacydescTime(arg_16_0.shipVO.proposeTime)

			if arg_16_0.intimacyDesc:
				setActive(arg_16_0.intimacyDesc, not arg_16_0.intimacyDescPic)

				local var_20_5 = arg_16_0.getProposeText()

				setText(arg_16_0.intimacyDesc, var_20_5)
		else
			if arg_16_0.intimacyDesc and GetComponent(arg_16_0.intimacyDesc, "VerticalText"):
				GetComponent(arg_16_0.intimacyDesc, "VerticalText").enabled = False

			if arg_16_0.intimacyDescPic:
				setActive(arg_16_0.intimacyDescPic, False)

			if arg_16_0.intimacyDesc:
				setActive(arg_16_0.intimacyDesc, True)
				setText(arg_16_0.intimacyDesc, i18n(var_20_4, arg_16_0.shipVO.name))

		setText(arg_16_0.intimacyBuffDesc, "*" .. i18n(var_20_4 .. "_buff"))
		arg_16_0.loadChar()
		pg.UIMgr.GetInstance().BlurPanel(arg_16_0._tf, False, {
			weight = LayerWeightConst.SECOND_LAYER
		})
		setActive(arg_16_0.button, not arg_16_0.shipVO.ShowPropose())

		local var_20_6 = not arg_16_0.shipVO.propose and var_20_1 <= var_20_2
		local var_20_7 = arg_16_0.shipVO.propose and not arg_16_0.shipVO.ShowPropose()

		arg_16_0.button.GetComponent(typeof(Button)).interactable = var_20_6 or var_20_7

		onButton(arg_16_0, arg_16_0.button, function()
			if var_20_6:
				local var_21_0 = arg_16_0.bagProxy.getItemCountById(arg_16_0.getProposeItemId())

				if var_21_0 < 1:
					if arg_16_0.proposeType == "imas":
						arg_16_0.showExchangePanel()
					else
						ItemTipPanel.ShowRingBuyTip()

					return

				local var_21_1, var_21_2 = ShipStatus.ShipStatusCheck("onPropose", arg_16_0.shipVO)

				if not var_21_1:
					pg.TipsMgr.GetInstance().ShowTips(var_21_2)

					return

				arg_16_0.checkPaintingRes(arg_16_0.shipVO, function()
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("word_propose_cost_tip" .. (arg_16_0.proposeType == "imas" and "1" or ""), var_21_0),
						def onYes:()
							if arg_16_0.intimacydescTime:
								arg_16_0.onUpdateIntimacydescTime(pg.TimeMgr.GetInstance().GetServerTime())

							arg_16_0.hideWindow()
							setActive(arg_16_0.window, False)
							arg_16_0.doPlay()
					}))
			elif var_20_7:
				function arg_16_0.afterRegisterCall()
					arg_16_0.afterRegisterCall = None

					pg.TipsMgr.GetInstance().ShowTips(i18n("word_propose_switch_tip"))
					arg_16_0.closeView()

				arg_16_0.emit(ProposeMediator.REGISTER_SHIP, arg_16_0.shipVO.id)
			else
				arg_16_0.closeView(), SFX_PANEL))

def var_0_0.getProposeText(arg_25_0):
	local var_25_0 = ""

	if PLATFORM_CODE == PLATFORM_CH or PLATFORM_CODE == PLATFORM_CHT:
		var_25_0 = i18n("intimacy_desc_propose", pg.TimeMgr.GetInstance().ChieseDescTime(arg_25_0.shipVO.proposeTime, True))

		if not IsNil(GetComponent(arg_25_0.intimacyDesc, "VerticalText")):
			GetComponent(arg_25_0.intimacyDesc, "VerticalText").enabled = True
			var_25_0 = i18n("intimacy_desc_propose_vertical", pg.TimeMgr.GetInstance().ChieseDescTime(arg_25_0.shipVO.proposeTime, True))
	elif PLATFORM_CODE == PLATFORM_KR:
		var_25_0 = i18n("intimacy_desc_propose", pg.TimeMgr.GetInstance().STimeDescS(arg_25_0.shipVO.proposeTime, "%Y년%m월%d일", True))

		if not IsNil(GetComponent(arg_25_0.intimacyDesc, "VerticalText")):
			GetComponent(arg_25_0.intimacyDesc, "VerticalText").enabled = True
			var_25_0 = i18n("intimacy_desc_propose_vertical", pg.TimeMgr.GetInstance().STimeDescS(arg_25_0.shipVO.proposeTime, "%Y년%m월%d일"))
	else
		var_25_0 = i18n("intimacy_desc_propose", pg.TimeMgr.GetInstance().STimeDescS(arg_25_0.shipVO.proposeTime, "%Y/%m/%d", True))

		if not IsNil(GetComponent(arg_25_0.intimacyDesc, "VerticalText")):
			GetComponent(arg_25_0.intimacyDesc, "VerticalText").enabled = True
			var_25_0 = i18n("intimacy_desc_propose_vertical", pg.TimeMgr.GetInstance().STimeDescS(arg_25_0.shipVO.proposeTime, "%Y/%m/%d"))

	return var_25_0

def var_0_0.getProposeItemId(arg_26_0):
	if arg_26_0.proposeType == "imas":
		return ITEM_ID_FOR_PROPOSE_IMAS
	else
		return ITEM_ID_FOR_PROPOSE

def var_0_0.onUpdateItemCount(arg_27_0):
	local var_27_0 = arg_27_0.bagProxy.getItemCountById(arg_27_0.getProposeItemId())

	setActive(arg_27_0.ringAchieved, arg_27_0.shipVO.propose or var_27_0 > 0)
	setActive(arg_27_0.ringNoAchieved, var_27_0 <= 0 and not arg_27_0.shipVO.propose)
	setText(arg_27_0.ringValue, i18n(arg_27_0.proposeType == "imas" and "intimacy_desc_tiara" or "intimacy_desc_ring"))

	if arg_27_0.shipVO.propose or var_27_0 > 0:
		setTextColor(arg_27_0.ringValue, Color.white)
	else
		setTextColor(arg_27_0.ringValue, Color.New(0.5843137254901961, 0.5215686274509804, 0.40784313725490196))

	if arg_27_0.proposeType == "imas":
		local var_27_1 = not arg_27_0.shipVO.propose and var_27_0 == 0

		setActive(arg_27_0.window.Find("ringCount/bg_exchange"), var_27_1)
		setActive(arg_27_0.window.Find("ringCount/icon/btn_exchange"), var_27_1)
		onButton(arg_27_0, arg_27_0.window.Find("ringCount/icon/btn_exchange"), function()
			arg_27_0.showExchangePanel(), SFX_PANEL)
	else
		setActive(arg_27_0.window.Find("ringCount/icon/base"), PLATFORM_CODE != PLATFORM_CH)
		setActive(arg_27_0.window.Find("ringCount/icon/hx"), PLATFORM_CODE == PLATFORM_CH)

def var_0_0.onUpdateIntimacydescTime(arg_29_0, arg_29_1):
	local var_29_0

	if PLATFORM_CODE == PLATFORM_JP:
		if arg_29_0.proposeType == "imas":
			var_29_0 = "%Y.%m.%d"
		else
			var_29_0 = "%B.%d,    %y"
	elif PLATFORM_CODE == PLATFORM_US:
		var_29_0 = "%B %d, %Y"
	elif arg_29_0.proposeType == "imas":
		var_29_0 = i18n("intimacy_desc_day") .. " %Y.%m.%d"
	else
		var_29_0 = "%B.%d,    %y"

	setText(arg_29_0.intimacydescTime, pg.TimeMgr.GetInstance().STimeDescS(arg_29_1, var_29_0))

def var_0_0.onBackPressed(arg_30_0):
	if isActive(arg_30_0.exchangePanel):
		arg_30_0.hideExchangePanel()

		return

	if arg_30_0.window and isActive(arg_30_0.window):
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
		triggerButton(arg_30_0.findTF("close_end"))

def var_0_0.willExit(arg_31_0):
	if arg_31_0._currentVoice:
		arg_31_0._currentVoice.PlaybackStop()

	arg_31_0._currentVoice = None

	pg.BgmMgr.GetInstance().ContinuePlay()

	if not IsNil(arg_31_0.actorPainting):
		local var_31_0 = tf(arg_31_0.actorPainting)

		if var_31_0.Find("temp_mask"):
			Destroy(var_31_0.Find("temp_mask"))

		var_31_0.GetComponent(typeof(Image)).material = None

		PoolMgr.GetInstance().ReturnPainting(arg_31_0.paintingName, arg_31_0.actorPainting)

		arg_31_0.actorPainting = None

	if arg_31_0.delayTId:
		LeanTween.cancel(arg_31_0.delayTId)

	if arg_31_0.commonTF:
		setActive(arg_31_0.commonTF, True)

	pg.UIMgr.GetInstance().UnblurPanel(arg_31_0._tf)

	if arg_31_0.l2dChar:
		arg_31_0.l2dChar.ClearPics()

		arg_31_0.l2dChar = None

	pg.Live2DMgr.GetInstance().StopLoadingLive2d(arg_31_0.live2dRequestId)

	arg_31_0.live2dRequestId = None

	if arg_31_0._delayVoiceTweenID:
		LeanTween.cancel(arg_31_0._delayVoiceTweenID)

		arg_31_0._delayVoiceTweenID = None

	if arg_31_0.tweenList:
		cancelTweens(arg_31_0.tweenList)

		arg_31_0.tweenList = None

	if arg_31_0.contextData.callback:
		arg_31_0.contextData.callback()

	if arg_31_0.finishCallback:
		arg_31_0.finishCallback()

		arg_31_0.finishCallback = None

def var_0_0.setMask(arg_32_0, arg_32_1):
	setActive(arg_32_0.maskTF, arg_32_1)

def var_0_0.bgAddAnimation(arg_33_0, arg_33_1):
	setActive(arg_33_0.storybg, True)
	arg_33_0.showbgAdd(True, arg_33_1)

def var_0_0.showbgChurch(arg_34_0):
	table.insert(arg_34_0.tweenList, LeanTween.scale(arg_34_0.storybg, Vector3(1, 1, 1), 6).uniqueId)
	setActive(arg_34_0.churchLight, True)
	table.insert(arg_34_0.tweenList, LeanTween.delayedCall(6, System.Action(function()
		setActive(arg_34_0.churchLight, False))).uniqueId)

def var_0_0.showbgAdd(arg_36_0, arg_36_1, arg_36_2):
	local var_36_0 = arg_36_1 and 1 or 0
	local var_36_1 = arg_36_1 and 0 or 1
	local var_36_2 = GetOrAddComponent(arg_36_0.bgAdd, typeof(CanvasGroup))

	table.insert(arg_36_0.tweenList, LeanTween.alphaCanvas(var_36_2, var_36_1, arg_36_2).setFrom(var_36_0).uniqueId)
	setActive(arg_36_0.bgAdd, True)

def var_0_0.showBlackBG(arg_37_0, arg_37_1, arg_37_2, arg_37_3):
	local var_37_0 = arg_37_1 and 1 or 0
	local var_37_1 = arg_37_1 and 0 or 1
	local var_37_2 = GetOrAddComponent(arg_37_0.blackBG, typeof(CanvasGroup))

	setActive(arg_37_0.blackBG, True)
	table.insert(arg_37_0.tweenList, LeanTween.alphaCanvas(var_37_2, var_37_1, arg_37_2).setFrom(var_37_0).setOnComplete(System.Action(function()
		if arg_37_1:
			setActive(arg_37_0.blackBG, False)

		if arg_37_3:
			arg_37_3())).uniqueId)

def var_0_0.showPainting(arg_39_0, arg_39_1, arg_39_2, arg_39_3):
	local var_39_0 = {}

	if arg_39_1:
		table.insert(var_39_0, function(arg_40_0)
			arg_39_0.loadChar(arg_39_0.targetActorTF, "duihua", arg_40_0))

	seriesAsync(var_39_0, function()
		local var_41_0 = arg_39_1 and 0 or 1
		local var_41_1 = arg_39_1 and 1 or 0
		local var_41_2 = GetOrAddComponent(arg_39_0.targetActorTF, typeof(CanvasGroup))

		table.insert(arg_39_0.tweenList, LeanTween.alphaCanvas(var_41_2, var_41_1, arg_39_2).setFrom(var_41_0).setOnComplete(System.Action(function()
			if arg_39_3:
				arg_39_3())).uniqueId))

var_0_0.Live2DProposeDelayTime = 2

def var_0_0.showLive2D(arg_43_0, arg_43_1):
	setActive(arg_43_0.findTF("fitter", arg_43_0.targetActorTF), False)
	setActive(arg_43_0.findTF("live2d", arg_43_0.targetActorTF), True)

	local var_43_0 = GetOrAddComponent(arg_43_0.targetActorTF, typeof(CanvasGroup))

	table.insert(arg_43_0.tweenList, LeanTween.alphaCanvas(var_43_0, 1, var_0_0.Live2DProposeDelayTime).setFrom(0).setOnComplete(System.Action(function()
		arg_43_0.changeParamaterValue("Paramring", 1)
		arg_43_0.l2dChar.SetAction(pg.AssistantInfo.action2Id[arg_43_1]))).uniqueId)

def var_0_0.changeParamaterValue(arg_45_0, arg_45_1, arg_45_2):
	if not arg_45_1 or string.len(arg_45_1) == 0:
		return

	local var_45_0 = arg_45_0.l2dChar.GetCubismParameter(arg_45_1)

	if not var_45_0:
		return

	arg_45_0.l2dChar.AddParameterValue(var_45_0, arg_45_2, CubismParameterBlendMode.Override)

def var_0_0.hideWindow(arg_46_0):
	local var_46_0 = GetOrAddComponent(arg_46_0.window, typeof(CanvasGroup))

	var_46_0.interactable = False

	table.insert(arg_46_0.tweenList, LeanTween.alphaCanvas(var_46_0, 0, 0.2).setFrom(1).setOnComplete(System.Action(function()
		var_46_0.interactable = True)).uniqueId)

def var_0_0.stampWindow(arg_48_0):
	arg_48_0.proposeEndFlag = True

	arg_48_0.loadChar(None, None, function()
		return)
	setActive(arg_48_0.window, True)
	setActive(arg_48_0.button, False)
	setActive(arg_48_0.findTF("live2d", arg_48_0.targetActorTF), False)

	local var_48_0

	if arg_48_0.intimacyDescPic:
		setActive(arg_48_0.intimacyDescPic, True)

		var_48_0 = GetOrAddComponent(arg_48_0.intimacyDescPic, typeof(CanvasGroup))

	if arg_48_0.intimacyDesc:
		setActive(arg_48_0.intimacyDesc, not arg_48_0.intimacyDescPic)

		local var_48_1 = arg_48_0.getProposeText()

		setText(arg_48_0.intimacyDesc, var_48_1)

		var_48_0 = GetOrAddComponent(arg_48_0.intimacyDesc, typeof(CanvasGroup))

	setText(arg_48_0.intimacyBuffDesc, "")
	setActive(arg_48_0.doneTF, False)

	var_48_0.alpha = 0

	local var_48_2 = GetOrAddComponent(arg_48_0.window, typeof(CanvasGroup))

	var_48_2.interactable = False

	table.insert(arg_48_0.tweenList, LeanTween.alphaCanvas(var_48_2, 1, 0.8).setFrom(0).uniqueId)
	table.insert(arg_48_0.tweenList, LeanTween.delayedCall(1.5, System.Action(function()
		table.insert(arg_48_0.tweenList, LeanTween.alphaCanvas(var_48_0, 1, 2).setFrom(0).uniqueId))).uniqueId)

	arg_48_0.delayTId = LeanTween.delayedCall(5, System.Action(function()
		if not var_48_2:
			return

		var_48_2.interactable = True

		setActive(arg_48_0.doneTF, True)
		arg_48_0.setMask(False)
		setActive(arg_48_0.findTF("close_end"), True)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_SEAL))).id

def var_0_0.showProposePanel(arg_52_0):
	local var_52_0 = {}

	arg_52_0.proposeSkin = ShipGroup.getProposeSkin(arg_52_0.shipGroupID)

	if arg_52_0.proposeSkin and arg_52_0.actorPainting:
		local var_52_1 = tf(arg_52_0.actorPainting)

		if var_52_1.Find("temp_mask"):
			Destroy(var_52_1.Find("temp_mask"))

		var_52_1.GetComponent(typeof(Image)).material = None

		PoolMgr.GetInstance().ReturnPainting(arg_52_0.paintingName, arg_52_0.actorPainting)

		arg_52_0.actorPainting = None

	if not arg_52_0.proposePanel:
		table.insert(var_52_0, function(arg_53_0)
			local var_53_0 = "ProposeRingUI"

			PoolMgr.GetInstance().GetUI(var_53_0, True, function(arg_54_0)
				if arg_52_0.exited:
					PoolMgr.GetInstance().ReturnUI(var_53_0, arg_54_0)

					return

				arg_52_0.proposePanel = tf(arg_54_0)

				setParent(tf(arg_54_0), arg_52_0.findTF("contain"))
				eachChild(arg_52_0.proposePanel.Find("ringBox"), function(arg_55_0)
					setActive(arg_55_0, arg_55_0.name == arg_52_0.proposeType)

					if arg_55_0.name == arg_52_0.proposeType:
						arg_52_0.ringBoxTF = arg_55_0)

				arg_52_0.ringBoxCG = GetOrAddComponent(arg_52_0.ringBoxTF, typeof(CanvasGroup))
				arg_52_0.ringBoxFull = arg_52_0.findTF("full", arg_52_0.ringBoxTF)
				arg_52_0.churchBefore = arg_52_0.findTF("before", arg_52_0.proposePanel)
				arg_52_0.churchLight = arg_52_0.findTF("light", arg_52_0.churchBefore)

				setParent(arg_52_0.churchLight, arg_52_0._tf)
				arg_52_0.churchLight.SetSiblingIndex(2)

				arg_52_0.blackBG = arg_52_0.findTF("blackbg", arg_52_0.churchBefore)
				arg_52_0.doorLightBG = arg_52_0.findTF("door_light", arg_52_0.churchBefore)
				arg_52_0.door = arg_52_0.findTF("door", arg_52_0.churchBefore)
				arg_52_0.doorAni = GetOrAddComponent(arg_52_0.door, "SpineAnimUI")

				setParent(arg_52_0.churchBefore, arg_52_0.findTF("contain"))

				arg_52_0.ringTipTF = arg_52_0.findTF("tip", arg_52_0.proposePanel)
				arg_52_0.ringTipCG = GetOrAddComponent(arg_52_0.ringTipTF, typeof(CanvasGroup))

				setText(arg_52_0.findTF("Text", arg_52_0.ringTipTF), i18n(arg_52_0.proposeType == "imas" and "word_propose_tiara_tip" or "word_propose_ring_tip"))
				setActive(arg_52_0.findTF("finger", arg_52_0.ringTipTF), False)
				LoadImageSpriteAsync(arg_52_0.bgName, arg_52_0.storybg)

				arg_52_0.storybg.localScale = Vector3(1.2, 1.2, 1.2)

				local var_54_0 = arg_52_0.weddingReview and arg_52_0.reviewSkinID or arg_52_0.shipVO.skinId

				arg_52_0.handId = pg.ship_skin_template[var_54_0].hand_id

				local var_54_1 = pg.TimeMgr.GetInstance().CurrentSTimeDesc("%Y%m%d", True)

				if SPECIAL_PROPOSE and SPECIAL_PROPOSE[1] == var_54_1:
					for iter_54_0, iter_54_1 in ipairs(SPECIAL_PROPOSE[2]):
						if iter_54_1[1] == var_54_0:
							arg_52_0.handId = iter_54_1[2]

				local var_54_2 = ({
					default = "",
					meta = "Meta_",
					imas = "Imas_"
				})[arg_52_0.proposeType] .. "ProposeHand_" .. arg_52_0.handId

				arg_52_0.handName = var_54_2

				PoolMgr.GetInstance().GetUI(var_54_2, True, function(arg_56_0)
					if arg_52_0.exited:
						PoolMgr.GetInstance().ReturnUI(var_54_2, arg_56_0)

						return

					arg_52_0.transHand = tf(arg_56_0)

					setActive(arg_52_0.transHand, False)
					setParent(arg_52_0.transHand, arg_52_0.proposePanel)
					arg_52_0.transHand.SetAsFirstSibling()

					arg_52_0.handTF = arg_52_0.findTF("hand", arg_52_0.transHand)
					arg_52_0.ringTF = arg_52_0.findTF("ring", arg_52_0.transHand)
					arg_52_0.ringCG = GetOrAddComponent(arg_52_0.ringTF, typeof(CanvasGroup))
					arg_52_0.ringAnim = arg_52_0.ringTF.GetComponent(typeof(Animator))
					arg_52_0.ringAnim.enabled = False
					arg_52_0.ringLight = arg_52_0.findTF("ring_light", arg_52_0.ringTF)
					arg_52_0.ringLightCG = GetOrAddComponent(arg_52_0.ringLight, typeof(CanvasGroup))

					arg_53_0())))

	table.insert(var_52_0, function(arg_57_0)
		table.insert(arg_52_0.tweenList, LeanTween.scale(arg_52_0.door, Vector3(2.1, 2.1, 2.1), 4).uniqueId)
		arg_52_0.doorAni.SetActionCallBack(function(arg_58_0)
			if arg_58_0 == "FINISH":
				arg_52_0.doorAni.SetActionCallBack(None)
				setActive(arg_52_0.door, False)
				arg_52_0.showBlackBG(True, 0.1)
				setActive(arg_52_0.doorLightBG, False)
				arg_57_0())
		table.insert(arg_52_0.tweenList, LeanTween.delayedCall(2, System.Action(function()
			arg_52_0.showbgAdd(False, 2))).uniqueId)
		table.insert(arg_52_0.tweenList, LeanTween.alpha(rtf(arg_52_0.doorLightBG), 1, 2).setFrom(0).uniqueId)
		arg_52_0.showBlackBG(False, 0.1)
		arg_52_0.doorAni.SetAction("OPEN", 0)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_DOOR))
	table.insert(var_52_0, function(arg_60_0)
		arg_52_0.handTF.GetComponent(typeof(Image)).color = Color.New(1, 1, 1, 0)

		arg_52_0.bgAddAnimation(2)
		table.insert(arg_52_0.tweenList, LeanTween.delayedCall(2, System.Action(function()
			arg_52_0.showPainting(True, 1.5, function()
				table.insert(arg_52_0.tweenList, LeanTween.delayedCall(1.5, System.Action(arg_60_0)).uniqueId)))).uniqueId))
	table.insert(var_52_0, function(arg_63_0)
		arg_52_0.showBlackBG(False, 1.2, function()
			arg_52_0.showBlackBG(True, 1.2))
		arg_52_0.showPainting(False, 1, arg_63_0))
	table.insert(var_52_0, function(arg_65_0)
		setAnchoredPosition(arg_52_0.handTF, {
			y = arg_52_0.handTF.rect.height
		})
		setAnchoredPosition(arg_52_0.ringTF, {
			y = 0
		})
		setActive(arg_52_0.proposePanel, True)
		setActive(arg_52_0.transHand, True)

		arg_52_0.ringBoxCG.alpha = 0
		arg_52_0.ringCG.alpha = 0

		arg_65_0())

	if arg_52_0.proposeType != "imas":
		table.insert(var_52_0, function(arg_66_0)
			table.insert(arg_52_0.tweenList, LeanTween.alpha(rtf(arg_52_0.handTF), 1, 1.2).uniqueId)
			table.insert(arg_52_0.tweenList, LeanTween.moveY(rtf(arg_52_0.handTF), 0, 2).setOnComplete(System.Action(function()
				table.insert(arg_52_0.tweenList, LeanTween.alphaCanvas(arg_52_0.ringBoxCG, 1, 1.5).setFrom(0).setOnComplete(System.Action(arg_66_0)).uniqueId))).uniqueId))
		table.insert(var_52_0, function(arg_68_0)
			table.insert(arg_52_0.tweenList, LeanTween.alpha(rtf(arg_52_0.ringBoxFull), 0, 0.6).setOnComplete(System.Action(arg_68_0)).uniqueId)
			table.insert(arg_52_0.tweenList, LeanTween.alphaCanvas(arg_52_0.ringCG, 1, 0.6).uniqueId))

	table.insert(var_52_0, function(arg_69_0)
		arg_52_0.ringCG.alpha = 1

		arg_52_0.setMask(False)
		table.insert(arg_52_0.tweenList, LeanTween.delayedCall(0.1, System.Action(arg_69_0)).uniqueId))
	table.insert(var_52_0, function(arg_70_0)
		arg_52_0.ringAnim.enabled = True

		arg_52_0.ringAnim.Play("movein")

		local var_70_0 = arg_52_0.proposeType == "imas" and 1 or 0.5

		table.insert(arg_52_0.tweenList, LeanTween.delayedCall(var_70_0, System.Action(arg_70_0)).uniqueId))
	seriesAsync(var_52_0, function()
		arg_52_0.ringAnim.Play("blink")
		table.insert(arg_52_0.tweenList, LeanTween.alphaCanvas(arg_52_0.ringTipCG, 1, 1.5).setFrom(0).setOnComplete(System.Action(function()
			setActive(arg_52_0.findTF("finger", arg_52_0.ringTipTF), True)
			arg_52_0.enableRingDrag(True))).uniqueId))

def var_0_0.ringOn(arg_73_0):
	if arg_73_0.isRingOn:
		return

	setActive(arg_73_0.ringTipTF, False)

	arg_73_0.isRingOn = True

	arg_73_0.ringTF.GetComponent("DftAniEvent").SetEndEvent(function(arg_74_0)
		arg_73_0.ringAnim.enabled = False
		arg_73_0.isRingOn = False

		if not arg_73_0.weddingReview:
			arg_73_0.emit(ProposeMediator.ON_PROPOSE, arg_73_0.shipVO.id)
		else
			arg_73_0.RingFadeout())

	arg_73_0.ringAnim.enabled = True

	arg_73_0.ringAnim.Play("wear")

	if arg_73_0.handId == "101":
		local var_73_0 = GetOrAddComponent(arg_73_0.handTF, typeof(CanvasGroup))

		table.insert(arg_73_0.tweenList, LeanTween.alphaCanvas(var_73_0, 0, 2).uniqueId)

def var_0_0.enableRingDrag(arg_75_0, arg_75_1):
	if not arg_75_0.press:
		arg_75_0.addRingDragListenter()

	arg_75_0.press.enabled = arg_75_1

def var_0_0.addRingDragListenter(arg_76_0):
	arg_76_0.press = GetOrAddComponent(arg_76_0.proposePanel, "EventTriggerListener")

	local var_76_0

	arg_76_0.press.AddBeginDragFunc(function()
		return)
	arg_76_0.press.AddDragFunc(function(arg_78_0, arg_78_1)
		local var_78_0 = arg_78_1.position

		if not var_76_0:
			var_76_0 = var_78_0

		if var_78_0.y - var_76_0.y > 100:
			arg_76_0.setMask(True)
			arg_76_0.ringOn()
			arg_76_0.enableRingDrag(False))
	arg_76_0.press.AddDragEndFunc(function(arg_79_0, arg_79_1)
		return)

def var_0_0.RingFadeout(arg_80_0):
	local var_80_0 = {}

	if arg_80_0.proposeType == "imas":
		table.insert(var_80_0, function(arg_81_0)
			local var_81_0 = arg_80_0.ringLight.GetChild(0)

			setActive(var_81_0, True)
			table.insert(arg_80_0.tweenList, LeanTween.delayedCall(3.5, System.Action(function()
				setActive(var_81_0, False)
				arg_81_0())).uniqueId))
	else
		table.insert(var_80_0, function(arg_83_0)
			table.insert(arg_80_0.tweenList, LeanTween.alphaCanvas(arg_80_0.ringLightCG, 0.7, 0.5).setFrom(0).uniqueId)
			table.insert(arg_80_0.tweenList, LeanTween.scale(arg_80_0.ringLight, Vector3(8, 8, 8), 1).uniqueId)
			table.insert(arg_80_0.tweenList, LeanTween.rotate(arg_80_0.ringLight, 90, 3).setOnComplete(System.Action(arg_83_0)).uniqueId))
		table.insert(var_80_0, function(arg_84_0)
			table.insert(arg_80_0.tweenList, LeanTween.delayedCall(0.5, System.Action(arg_84_0)).uniqueId))

	seriesAsync(var_80_0, function()
		arg_80_0.displayShipWord("propose"))
	table.insert(arg_80_0.tweenList, LeanTween.delayedCall(1.2, System.Action(function()
		arg_80_0.showbgAdd(False, 1.8))).uniqueId)
	table.insert(arg_80_0.tweenList, LeanTween.delayedCall(3.2, System.Action(function()
		setActive(arg_80_0.proposePanel, False)
		arg_80_0.showbgAdd(True, 2))).uniqueId)

def var_0_0.displayShipWord(arg_88_0, arg_88_1):
	local var_88_0 = ShipGroup.getDefaultSkin(arg_88_0.shipGroupID)
	local var_88_1, var_88_2, var_88_3 = ShipWordHelper.GetWordAndCV(var_88_0.id, arg_88_1)
	local var_88_4

	if arg_88_0.reviewSkinID:
		var_88_4 = arg_88_0.reviewSkinID
	elif arg_88_0.proposeSkin:
		var_88_4 = arg_88_0.proposeSkin.id
	else
		var_88_4 = arg_88_0.shipVO.skinId

	local var_88_5 = ShipWordHelper.GetL2dCvCalibrate(var_88_4, arg_88_1)

	arg_88_0.showStoryUI(var_88_3)

	if var_88_2:
		local function var_88_6()
			if arg_88_0._currentVoice:
				arg_88_0._currentVoice.PlaybackStop()

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_88_2, function(arg_90_0)
				arg_88_0._currentVoice = arg_90_0)

		local var_88_7 = var_0_0.Live2DProposeDelayTime

		if not arg_88_0.useL2dOrPainting():
			var_88_7 = 0

		table.insert(arg_88_0.tweenList, LeanTween.delayedCall(var_88_7, System.Action(function()
			if arg_88_0.l2dChar and var_88_5 and var_88_5 != 0:
				arg_88_0._delayVoiceTweenID = LeanTween.delayedCall(var_88_5, System.Action(function()
					var_88_6()

					arg_88_0._delayVoiceTweenID = None)).uniqueId
			else
				var_88_6())).uniqueId)

def var_0_0.useL2dOrPainting(arg_93_0):
	return checkABExist("live2d/" .. string.lower(arg_93_0.paintingName))

def var_0_0.showStoryUI(arg_94_0, arg_94_1):
	local var_94_0 = {}

	if not arg_94_0.storyTF:
		table.insert(var_94_0, function(arg_95_0)
			local var_95_0 = "ProposeStoryUI"

			PoolMgr.GetInstance().GetUI(var_95_0, True, function(arg_96_0)
				if arg_94_0.exited:
					PoolMgr.GetInstance().ReturnUI(var_95_0, arg_96_0)

					return

				arg_94_0.storyTF = tf(arg_96_0)

				setParent(tf(arg_96_0), arg_94_0.findTF("contain"))

				arg_94_0.storyCG = GetOrAddComponent(arg_94_0.storyTF, typeof(CanvasGroup))
				arg_94_0.storyContent = arg_94_0.findTF("dialogue/content", arg_94_0.storyTF)
				arg_94_0.typeWriter = arg_94_0.storyContent.GetComponent(typeof(Typewriter))
				arg_94_0.targetNameTF = arg_94_0.findTF("dialogue/content/name", arg_94_0.storyTF)
				arg_94_0._renamePanel = arg_94_0.findTF("changeName_panel", arg_94_0.storyTF)

				setText(findTF(arg_94_0._renamePanel, "frame/name_field/Placeholder"), i18n("rename_input"))
				setActive(arg_94_0._renamePanel, False)
				onButton(arg_94_0, arg_94_0.storyTF, function()
					if arg_94_0.inTypeWritter:
						arg_94_0.typeWriter.setSpeed(arg_94_0.typeWritterSpeedUp)

						return

					if not arg_94_0.initStory:
						return

					table.insert(arg_94_0.tweenList, LeanTween.alphaCanvas(arg_94_0.storyCG, 0, 1).setFrom(1).setOnComplete(System.Action(function()
						setActive(arg_94_0.storyTF, False))).uniqueId)

					if arg_94_0._currentVoice:
						arg_94_0._currentVoice.PlaybackStop()

					arg_94_0._currentVoice = None

					arg_94_0.setMask(True)
					table.insert(arg_94_0.tweenList, LeanTween.delayedCall(0.5, System.Action(function()
						if arg_94_0.weddingReview:
							arg_94_0.closeView()
						else
							arg_94_0.initChangeNamePanel()
							arg_94_0.stampWindow())).uniqueId))
				arg_95_0()))

	seriesAsync(var_94_0, function()
		if arg_94_0.useL2dOrPainting():
			arg_94_0.showLive2D("wedding")
		else
			arg_94_0.showPainting(True, 2)

		local var_100_0 = ShipGroup.getDefaultShipNameByGroupID(arg_94_0.shipGroupID)

		setText(arg_94_0.targetNameTF.Find("Text"), var_100_0)
		setText(arg_94_0.storyContent, "")

		arg_94_0.storyCG.alpha = 0

		setActive(arg_94_0.storyTF, True)

		arg_94_0.initStory = False

		table.insert(arg_94_0.tweenList, LeanTween.alphaCanvas(arg_94_0.storyCG, 1, 1).setFrom(0).setDelay(1).setOnComplete(System.Action(function()
			if findTF(arg_94_0.targetActorTF, "fitter").childCount > 0:
				ShipExpressionHelper.SetExpression(findTF(arg_94_0.targetActorTF, "fitter").GetChild(0), arg_94_0.paintingName, "propose")

			setText(arg_94_0.storyContent, arg_94_1)

			arg_94_0.onWords = True

			arg_94_0.TypeWriter()

			arg_94_0.initStory = True

			arg_94_0.setMask(False)

			if not arg_94_0.weddingReview:
				arg_94_0.showTip())).uniqueId))

def var_0_0.TypeWriter(arg_102_0):
	local var_102_0 = 0.1

	arg_102_0.inTypeWritter = True
	arg_102_0.typeWritterSpeedUp = 0.01

	arg_102_0.typeWriter.setSpeed(var_102_0)
	arg_102_0.typeWriter.Play()

	function arg_102_0.typeWriter.endFunc()
		arg_102_0.inTypeWritter = False
		arg_102_0.typeWritterSpeedUp = None

def var_0_0.loadChar(arg_104_0, arg_104_1, arg_104_2, arg_104_3):
	arg_104_1 = arg_104_1 or arg_104_0._paintingTF
	arg_104_2 = arg_104_2 or "wedding"

	local var_104_0 = {}

	if not arg_104_0.actorPainting:
		table.insert(var_104_0, function(arg_105_0)
			if arg_104_0.reviewSkinID:
				arg_104_0.paintingName = pg.ship_skin_template[arg_104_0.reviewSkinID].painting
			elif arg_104_0.proposeSkin:
				arg_104_0.paintingName = arg_104_0.proposeSkin.painting
			else
				arg_104_0.paintingName = arg_104_0.shipVO.getPainting()

			local var_105_0 = arg_104_0.paintingName

			if checkABExist("painting/" .. var_105_0 .. "_n") and PlayerPrefs.GetInt("paint_hide_other_obj_" .. var_105_0, 0) != 0:
				var_105_0 = var_105_0 .. "_n"

			PoolMgr.GetInstance().GetPainting(var_105_0, True, function(arg_106_0)
				local var_106_0 = findTF(arg_106_0, "Touch")

				if not IsNil(var_106_0):
					setActive(var_106_0, False)

				arg_104_0.actorPainting = arg_106_0

				ShipExpressionHelper.SetExpression(arg_104_0.actorPainting, arg_104_0.paintingName)
				arg_105_0())

			if checkABExist("live2d/" .. string.lower(arg_104_0.paintingName)):
				arg_104_0.createLive2D(arg_104_0.paintingName))

	seriesAsync(var_104_0, function()
		if not IsNil(arg_104_1):
			local var_107_0 = findTF(arg_104_1, "fitter")

			assert(var_107_0, "请添加子物体fitter")

			local var_107_1 = GetOrAddComponent(var_107_0, "PaintingScaler")

			var_107_1.FrameName = arg_104_2
			var_107_1.Tween = 1

			setParent(arg_104_0.actorPainting, var_107_0)

		if arg_104_3:
			arg_104_3())

def var_0_0.createLive2D(arg_108_0, arg_108_1):
	arg_108_0.live2dRequestId = pg.Live2DMgr.GetInstance().GetLive2DModelAsync(arg_108_1, function(arg_109_0)
		local var_109_0 = arg_108_0.findTF("live2d", arg_108_0.targetActorTF)

		UIUtil.SetLayerRecursively(arg_109_0, LayerMask.NameToLayer("UI"))

		local var_109_1 = arg_109_0.transform

		var_109_1.SetParent(var_109_0, True)

		local var_109_2

		if arg_108_0.reviewSkinID:
			var_109_2 = arg_108_0.reviewSkinID
		elif arg_108_0.proposeSkin:
			var_109_2 = arg_108_0.proposeSkin.id
		else
			var_109_2 = arg_108_0.shipVO.skinId

		var_109_1.localPosition = BuildVector3(pg.ship_skin_template[var_109_2].live2d_offset) + Vector3(0, 0, 100)
		var_109_1.localScale = Vector3.Scale(Vector3(1, 1, 10), var_109_1.localScale)
		arg_108_0.l2dChar = GetComponent(arg_109_0, "Live2dChar")
		arg_108_0.l2dChar.name = arg_108_1

		local var_109_3 = pg.AssistantInfo.action2Id.idle

		function arg_108_0.l2dChar.FinishAction(arg_110_0)
			if var_109_3 != arg_110_0:
				arg_108_0.l2dChar.SetAction(var_109_3)

		arg_108_0.l2dChar.SetAction(var_109_3)

		local var_109_4 = pg.ship_skin_template[var_109_2]
		local var_109_5 = var_109_4.lip_sync_gain
		local var_109_6 = var_109_4.lip_smoothing

		if var_109_5 and var_109_5 != 0:
			var_109_0.GetChild(0).GetComponent("CubismCriSrcMouthInput").Gain = var_109_5

		if var_109_6 and var_109_6 != 0:
			var_109_0.GetChild(0).GetComponent("CubismCriSrcMouthInput").Smoothing = var_109_6)

def var_0_0.showTip(arg_111_0):
	local var_111_0 = arg_111_0.proposeSkin

	if not var_111_0:
		return

	local var_111_1 = arg_111_0.findTF("tip", arg_111_0.storyTF)
	local var_111_2 = arg_111_0.findTF("Image_bg/Text", var_111_1)

	setText(var_111_2, i18n("achieve_propose_tip", var_111_0.name))
	eachChild(var_111_1.Find("Image_bg/Image"), function(arg_112_0)
		setActive(arg_112_0, arg_112_0.name == arg_111_0.proposeType))

	local var_111_3 = GetOrAddComponent(var_111_1, typeof(CanvasGroup))

	setActive(var_111_1, True)
	table.insert(arg_111_0.tweenList, LeanTween.alphaCanvas(var_111_3, 1, 0.01).setFrom(0).uniqueId)
	table.insert(arg_111_0.tweenList, LeanTween.alphaCanvas(var_111_3, 0, 1.5).setFrom(1).setDelay(4).uniqueId)

def var_0_0.initChangeNamePanel(arg_113_0):
	setText(arg_113_0._renamePanel.Find("frame/border/title"), i18n("word_propose_changename_title", arg_113_0.shipVO.getName()))
	setText(arg_113_0._renamePanel.Find("frame/setting_ship_name/text"), i18n("word_propose_changename_tip1"))
	setText(arg_113_0._renamePanel.Find("frame/text"), i18n("word_propose_changename_tip2"))

	arg_113_0._renameConfirmBtn = arg_113_0._renamePanel.Find("frame/queren")
	arg_113_0._renameCancelBtn = arg_113_0._renamePanel.Find("frame/cancel")
	arg_113_0._renameToggle = findTF(arg_113_0._renamePanel, "frame/setting_ship_name").GetComponent(typeof(Toggle))
	arg_113_0._renameRevert = arg_113_0._renamePanel.Find("frame/revert_button")
	arg_113_0._closeBtn = arg_113_0._renamePanel.Find("frame/close_btn")

	onButton(arg_113_0, arg_113_0._renameConfirmBtn, function()
		local var_114_0 = getInputText(findTF(arg_113_0._renamePanel, "frame/name_field"))

		pg.PushNotificationMgr.GetInstance().setSwitchShipName(arg_113_0._renameToggle.isOn)
		arg_113_0.emit(ProposeMediator.RENAME_SHIP, arg_113_0.shipVO.id, var_114_0), SFX_CONFIRM)
	onButton(arg_113_0, arg_113_0._renameRevert, function()
		local var_115_0 = arg_113_0.shipVO.isRemoulded() and pg.ship_skin_template[arg_113_0.shipVO.getRemouldSkinId()].name or pg.ship_data_statistics[arg_113_0.shipVO.configId].name

		setInputText(findTF(arg_113_0._renamePanel, "frame/name_field"), var_115_0), SFX_PANEL)
	onButton(arg_113_0, arg_113_0._renameCancelBtn, function()
		arg_113_0.closeView(), SFX_CANCEL)
	onButton(arg_113_0, arg_113_0._closeBtn, function()
		arg_113_0.closeView(), SFX_CANCEL)

def var_0_0.DisplayRenamePanel(arg_118_0):
	if arg_118_0.shipVO.IsXIdol():
		arg_118_0.closeView()
	else
		setParent(arg_118_0._renamePanel, arg_118_0._tf)
		setActive(arg_118_0._renamePanel, True)

		local var_118_0 = arg_118_0.shipVO.getName()

		setInputText(findTF(arg_118_0._renamePanel, "frame/name_field"), var_118_0)
		setIntimacyIcon(arg_118_0.intimacyTF, arg_118_0.shipVO.getIntimacyIcon())

def var_0_0.showExchangePanel(arg_119_0):
	setActive(arg_119_0.exchangePanel, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_119_0.exchangePanel, False, {
		weight = LayerWeightConst.SECOND_LAYER
	})

def var_0_0.hideExchangePanel(arg_120_0):
	setActive(arg_120_0.exchangePanel, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_120_0.exchangePanel, arg_120_0._tf)

def var_0_0.checkPaintingRes(arg_121_0, arg_121_1, arg_121_2):
	local var_121_0 = {}
	local var_121_1 = arg_121_1.getProposeSkin()

	if var_121_1 and var_121_1.id > 0:
		local var_121_2 = var_121_1.id

		PaintingGroupConst.AddPaintingNameBySkinID(var_121_0, var_121_2)

	local var_121_3 = {
		isShowBox = True,
		paintingNameList = var_121_0,
		finishFunc = arg_121_2
	}

	PaintingGroupConst.PaintingDownload(var_121_3)

return var_0_0
