local var_0_0 = class("ChargeScene", import("...base.BaseUI"))

var_0_0.TYPE_DIAMOND = 1
var_0_0.TYPE_GIFT = 2
var_0_0.TYPE_ITEM = 3

def var_0_0.getUIName(arg_1_0):
	return "ChargeShopUI"

def var_0_0.onBackPressed(arg_2_0):
	arg_2_0.closeView()

def var_0_0.preload(arg_3_0, arg_3_1):
	local var_3_0 = getProxy(ShopsProxy)

	local function var_3_1()
		local var_4_0 = var_3_0.getFirstChargeList()
		local var_4_1 = var_3_0.getChargedList()
		local var_4_2 = var_3_0.GetNormalList()
		local var_4_3 = var_3_0.GetNormalGroupList()

		if var_4_0:
			arg_3_0.setFirstChargeIds(var_4_0)

		if var_4_1:
			arg_3_0.setChargedList(var_4_1)

		if var_4_2:
			arg_3_0.setNormalList(var_4_2)

		if var_4_3:
			arg_3_0.setNormalGroupList(var_4_3)

		arg_3_1()

	if var_3_0.ShouldRefreshChargeList():
		pg.m02.sendNotification(GAME.GET_CHARGE_LIST, {
			callback = var_3_1
		})
	else
		var_3_1()

def var_0_0.setPlayer(arg_5_0, arg_5_1):
	arg_5_0.player = arg_5_1

def var_0_0.setFirstChargeIds(arg_6_0, arg_6_1):
	arg_6_0.firstChargeIds = arg_6_1

def var_0_0.setChargedList(arg_7_0, arg_7_1):
	arg_7_0.chargedList = arg_7_1

def var_0_0.setNormalList(arg_8_0, arg_8_1):
	arg_8_0.normalList = arg_8_1

def var_0_0.setNormalGroupList(arg_9_0, arg_9_1):
	arg_9_0.normalGroupList = arg_9_1

	arg_9_0.addRefreshTimer(GetZeroTime())

def var_0_0.ResUISettings(arg_10_0):
	return True

def var_0_0.init(arg_11_0):
	arg_11_0.blurPanel = arg_11_0.findTF("blur_panel")
	arg_11_0.top = arg_11_0.findTF("adapt/top", arg_11_0.blurPanel)
	arg_11_0.frame = arg_11_0.findTF("frame")
	arg_11_0.viewContainer = arg_11_0.findTF("viewContainer")
	arg_11_0.bg = arg_11_0.findTF("viewContainer/bg")
	arg_11_0.painting = arg_11_0.findTF("frame/painting")
	arg_11_0.chat = arg_11_0.findTF("viewContainer/chat")
	arg_11_0.chatText = arg_11_0.findTF("Text", arg_11_0.chat)
	arg_11_0.switchBtn = arg_11_0.findTF("blur_panel/adapt/switch_btn")
	arg_11_0.skinShopBtn = arg_11_0.findTF("blur_panel/adapt/skin_btn")
	arg_11_0.itemToggle = arg_11_0.findTF("toggle_list/item_toggle", arg_11_0.viewContainer)
	arg_11_0.giftToggle = arg_11_0.findTF("toggle_list/gift_toggle", arg_11_0.viewContainer)
	arg_11_0.diamondToggle = arg_11_0.findTF("toggle_list/diamond_toggle", arg_11_0.viewContainer)
	arg_11_0.giftTip = arg_11_0.findTF("tip", arg_11_0.giftToggle)
	arg_11_0.chargeTipWindow = ChargeTipWindow.New(arg_11_0._tf, arg_11_0.event)

	local var_11_0 = arg_11_0.findTF("light/title", arg_11_0.diamondToggle)
	local var_11_1 = arg_11_0.findTF("dark/title", arg_11_0.diamondToggle)
	local var_11_2 = arg_11_0.findTF("light/title", arg_11_0.giftToggle)
	local var_11_3 = arg_11_0.findTF("dark/title", arg_11_0.giftToggle)
	local var_11_4 = arg_11_0.findTF("light/title", arg_11_0.itemToggle)
	local var_11_5 = arg_11_0.findTF("dark/title", arg_11_0.itemToggle)

	setText(var_11_0, i18n("shop_diamond_title"))
	setText(var_11_1, i18n("shop_diamond_title"))
	setText(var_11_2, i18n("shop_gift_title"))
	setText(var_11_3, i18n("shop_gift_title"))
	setText(var_11_4, i18n("shop_item_title"))
	setText(var_11_5, i18n("shop_item_title"))

	arg_11_0.linkTitle = {
		arg_11_0.findTF("title/title_diamond", arg_11_0.top),
		arg_11_0.findTF("title/title_gift", arg_11_0.top),
		arg_11_0.findTF("title/title_item", arg_11_0.top)
	}
	arg_11_0.toggleList = {
		arg_11_0.diamondToggle,
		arg_11_0.giftToggle,
		arg_11_0.itemToggle
	}

	arg_11_0.createLive2D()

	arg_11_0.live2dTimer = Timer.New(function()
		local var_12_0 = pg.ChargeShipTalkInfo.Actions
		local var_12_1 = var_12_0[math.random(#var_12_0)]

		if arg_11_0.checkBuyDone(var_12_1.action):
			arg_11_0.displayShipWord(None, False, var_12_1.dialog_index), 20, -1)

	arg_11_0.live2dTimer.Start()
	arg_11_0.jpUIInit()
	arg_11_0.blurView()
	arg_11_0.initSubView()

def var_0_0.didEnter(arg_13_0):
	setActive(arg_13_0.chat, False)
	onButton(arg_13_0, arg_13_0.findTF("back_button", arg_13_0.top), function()
		arg_13_0.closeView(), SFX_CANCEL)
	onButton(arg_13_0, arg_13_0.painting, function()
		arg_13_0.displayShipWord()
		arg_13_0.emit(ChargeMediator.CLICK_MING_SHI), SFX_PANEL)

	for iter_13_0 = 1, #arg_13_0.toggleList:
		local var_13_0 = arg_13_0.toggleList[iter_13_0]

		onToggle(arg_13_0, var_13_0, function(arg_16_0)
			local var_16_0 = arg_13_0.findTF("dark", var_13_0)

			setActive(var_16_0, not arg_16_0)

			if arg_16_0:
				arg_13_0.switchSubView(iter_13_0), SFX_PANEL)

	onButton(arg_13_0, arg_13_0.switchBtn, function()
		arg_13_0.emit(ChargeMediator.SWITCH_TO_SHOP, {
			warp = NewShopsScene.TYPE_SHOP_STREET
		})
		arg_13_0.stopCV(), SFX_PANEL)
	onButton(arg_13_0, arg_13_0.skinShopBtn, function()
		arg_13_0.emit(ChargeMediator.ON_SKIN_SHOP), SFX_PANEL)
	arg_13_0.updateNoRes()

	if arg_13_0.contextData.wrap != None:
		arg_13_0.switchSubViewByTogger(arg_13_0.contextData.wrap)

		arg_13_0.contextData.wrap = None
	else
		arg_13_0.switchSubViewByTogger(ChargeScene.TYPE_DIAMOND)

	arg_13_0.jpUIEnter()

def var_0_0.OnChargeSuccess(arg_19_0, arg_19_1):
	arg_19_0.chargeTipWindow.ExecuteAction("Show", arg_19_1)

def var_0_0.willExit(arg_20_0):
	arg_20_0.unBlurView()

	if arg_20_0.chargeTipWindow:
		arg_20_0.chargeTipWindow.Destroy()

		arg_20_0.chargeTipWindow = None

	if arg_20_0.heartsTimer:
		arg_20_0.heartsTimer.Stop()

		arg_20_0.heartsTimer = None

	if arg_20_0.live2dChar:
		arg_20_0.live2dChar.Dispose()

	if arg_20_0.live2dTimer:
		arg_20_0.live2dTimer.Stop()

		arg_20_0.live2dTimer = None

	if arg_20_0.giftShopView:
		arg_20_0.giftShopView.OnDestroy()

	arg_20_0.stopCV()

def var_0_0.initSubView(arg_21_0):
	arg_21_0.subViewContainer = arg_21_0.findTF("SubView", arg_21_0.viewContainer)
	arg_21_0.diamondShopView = ChargeDiamondShopView.New(arg_21_0.subViewContainer, arg_21_0.event, arg_21_0.contextData)
	arg_21_0.giftShopView = ChargeGiftShopView.New(arg_21_0.subViewContainer, arg_21_0.event, arg_21_0.contextData)
	arg_21_0.itemShopView = ChargeItemShopView.New(arg_21_0.subViewContainer, arg_21_0.event, arg_21_0.contextData)
	arg_21_0.curSubViewNum = 0
	arg_21_0.subViewList = {
		[ChargeScene.TYPE_DIAMOND] = arg_21_0.diamondShopView,
		[ChargeScene.TYPE_GIFT] = arg_21_0.giftShopView,
		[ChargeScene.TYPE_ITEM] = arg_21_0.itemShopView
	}

def var_0_0.switchSubView(arg_22_0, arg_22_1):
	if arg_22_1 == arg_22_0.curSubViewNum:
		return

	arg_22_0.subViewList[arg_22_1].setGoodData(arg_22_0.firstChargeIds, arg_22_0.chargedList, arg_22_0.normalList, arg_22_0.normalGroupList)
	arg_22_0.subViewList[arg_22_1].Reset()
	arg_22_0.subViewList[arg_22_1].Load()

	local var_22_0 = arg_22_0.subViewList[arg_22_0.curSubViewNum]

	if var_22_0:
		var_22_0.Destroy()

	arg_22_0.curSubViewNum = arg_22_1

	if PLATFORM_CODE == PLATFORM_JP:
		setActive(arg_22_0.userAgreeBtn3, arg_22_1 == var_0_0.TYPE_DIAMOND)
		setActive(arg_22_0.userAgreeBtn4, arg_22_1 == var_0_0.TYPE_DIAMOND)

	for iter_22_0, iter_22_1 in ipairs(arg_22_0.linkTitle):
		setActive(iter_22_1, iter_22_0 == arg_22_1)

def var_0_0.switchSubViewByTogger(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_0.toggleList[arg_23_1]

	triggerToggle(var_23_0, True)

def var_0_0.updateCurSubView(arg_24_0):
	local var_24_0 = arg_24_0.subViewList[arg_24_0.curSubViewNum]

	var_24_0.setGoodData(arg_24_0.firstChargeIds, arg_24_0.chargedList, arg_24_0.normalList, arg_24_0.normalGroupList)
	var_24_0.reUpdateAll()

def var_0_0.updateNoRes(arg_25_0, arg_25_1):
	if not arg_25_1:
		arg_25_1 = arg_25_0.contextData.noRes
	else
		arg_25_0.contextData.noRes = arg_25_1

	if not arg_25_1 or #arg_25_1 <= 0:
		return

	arg_25_0.contextData.noRes = {}

	local var_25_0 = getProxy(BagProxy).getData()
	local var_25_1 = ""

	for iter_25_0, iter_25_1 in ipairs(arg_25_1):
		if iter_25_1[2] > 0:
			if iter_25_1[1] == 59001:
				arg_25_1[iter_25_0][2] = iter_25_1[3] - arg_25_0.player.gold
			else
				arg_25_1[iter_25_0][2] = iter_25_1[3] - (var_25_0[iter_25_1[1]] and var_25_0[iter_25_1[1]].count or 0)

		if arg_25_1[iter_25_0][2] > 0:
			table.insert(arg_25_0.contextData.noRes, arg_25_1[iter_25_0])

	for iter_25_2, iter_25_3 in ipairs(arg_25_0.contextData.noRes):
		local var_25_2 = Item.getConfigData(iter_25_3[1]).name

		var_25_1 = var_25_1 .. i18n(iter_25_3[1] == 59001 and "text_noRes_info_tip" or "text_noRes_info_tip2", var_25_2, iter_25_3[2])

		if iter_25_2 < #arg_25_0.contextData.noRes:
			var_25_1 = var_25_1 .. i18n("text_noRes_info_tip_link")

	if var_25_1 == "":
		arg_25_0.displayShipWord(i18n("text_shop_enoughRes_tip"), False)
	else
		arg_25_0.displayShipWord(i18n("text_shop_noRes_tip", var_25_1), True)

def var_0_0.displayShipWord(arg_26_0, arg_26_1, arg_26_2, arg_26_3):
	if not arg_26_0.chatFlag:
		if not arg_26_1 and arg_26_0.contextData.noRes and #arg_26_0.contextData.noRes > 0:
			setActive(arg_26_0.chat, False)

			arg_26_0.chat.transform.localScale = Vector3(0, 0, 1)

		arg_26_0.chatFlag = True

		if not arg_26_0.isInitChatPosition:
			arg_26_0.isInitChatPosition = True

			arg_26_0.InitChatPosition()

		setActive(arg_26_0.chat, True)

		local var_26_0 = arg_26_0.player.getChargeLevel()
		local var_26_1 = arg_26_3 or math.random(1, var_26_0)
		local var_26_2

		if arg_26_3:
			var_26_2 = pg.pay_level_award[var_26_1].dialog
		else
			var_26_2 = arg_26_1 or pg.pay_level_award[var_26_1].dialog

		if not arg_26_1:
			arg_26_0.playCV(var_26_1)

		setText(arg_26_0.chatText, var_26_2)

		local var_26_3 = arg_26_0.chatText.GetComponent(typeof(Text))

		if #var_26_3.text > CHAT_POP_STR_LEN_SHORT:
			var_26_3.alignment = TextAnchor.MiddleLeft
		else
			var_26_3.alignment = TextAnchor.MiddleCenter

		;(function()
			local var_27_0 = 3
			local var_27_1 = 0.3

			LeanTween.scale(rtf(arg_26_0.chat.gameObject), Vector3.New(1, 1, 1), var_27_1).setFrom(Vector3.New(0, 0, 0)).setEase(LeanTweenType.easeOutBack).setOnComplete(System.Action(function()
				if not arg_26_2:
					LeanTween.scale(rtf(arg_26_0.chat.gameObject), Vector3.New(0, 0, 1), var_27_1).setEase(LeanTweenType.easeInBack).setDelay(var_27_1 + var_27_0).setOnComplete(System.Action(function()
						arg_26_0.chatFlag = None

						setActive(arg_26_0.chat, False)

						if arg_26_0.contextData.noRes and #arg_26_0.contextData.noRes > 0:
							arg_26_0.updateNoRes()))
				else
					arg_26_0.chatFlag = None)))()

def var_0_0.InitChatPosition(arg_30_0):
	local var_30_0 = arg_30_0.painting.localPosition + Vector3(-21, -176, 0)
	local var_30_1 = arg_30_0.painting.parent.TransformPoint(var_30_0)
	local var_30_2 = arg_30_0.chat.parent.InverseTransformPoint(var_30_1)

	arg_30_0.chat.localPosition = Vector3(var_30_2.x, var_30_2.y, 0)

def var_0_0.playHeartEffect(arg_31_0):
	if arg_31_0.heartsTimer:
		arg_31_0.heartsTimer.Stop()

	local var_31_0 = arg_31_0.painting.Find("heartsfly")

	setActive(var_31_0, True)

	arg_31_0.heartsTimer = Timer.New(function()
		setActive(var_31_0, False), 1, 1)

	arg_31_0.heartsTimer.Start()

def var_0_0.createLive2D(arg_33_0):
	local var_33_0 = Live2D.GenerateData({
		ship = Ship.New({
			configId = 312011
		}),
		scale = Vector3(75, 75, 75),
		position = Vector3(0, 0, 0),
		parent = arg_33_0.findTF("frame/painting/live2d")
	})

	arg_33_0.live2dChar = Live2D.New(var_33_0)

def var_0_0.checkBuyDone(arg_34_0, arg_34_1):
	if not arg_34_0.live2dChar:
		return

	local var_34_0

	if type(arg_34_1) == "string":
		if arg_34_1 == "damonds":
			var_34_0 = "diamond"
		else
			var_34_0 = arg_34_1
	else
		local var_34_1 = pg.shop_template[arg_34_1]

		if var_34_1 and var_34_1.effect_args and type(var_34_1.effect_args) == "table":
			for iter_34_0, iter_34_1 in ipairs(var_34_1.effect_args):
				if iter_34_1 == 1:
					var_34_0 = "gold"

	local var_34_2 = arg_34_0.preAniName == "gold" or arg_34_0.preAniName == "diamond"
	local var_34_3 = var_34_0 == "gold" or var_34_0 == "diamond"
	local var_34_4 = var_34_2 and var_34_3 or not var_34_2

	var_34_4 = var_34_0 and arg_34_0.preAniName != var_34_0 and var_34_4

	if var_34_4:
		arg_34_0.preAniName = var_34_0

		arg_34_0.live2dChar.TriggerAction(var_34_0, None, True)

	return var_34_4

def var_0_0.playCV(arg_35_0, arg_35_1):
	local var_35_0 = pg.pay_level_award[arg_35_1]
	local var_35_1

	if var_35_0 and var_35_0.cv_key != "":
		var_35_1 = "event./cv/chargeShop/" .. var_35_0.cv_key

	if var_35_1:
		arg_35_0.stopCV()

		arg_35_0._currentVoice = var_35_1

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_35_1)

def var_0_0.stopCV(arg_36_0):
	if arg_36_0._currentVoice:
		pg.CriMgr.GetInstance().UnloadSoundEffect_V3(arg_36_0._currentVoice)

	arg_36_0._currentVoice = None

def var_0_0.blurView(arg_37_0):
	pg.UIMgr.GetInstance().OverlayPanelPB(arg_37_0.viewContainer, {
		pbList = {
			arg_37_0.findTF("blurBg", arg_37_0.viewContainer)
		}
	})

def var_0_0.unBlurView(arg_38_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_38_0.viewContainer, arg_38_0.frame)

def var_0_0.jpUIInit(arg_39_0):
	if PLATFORM_CODE != PLATFORM_JP:
		return

	arg_39_0.userAgreeBtn3 = arg_39_0.findTF("frame/raw1Btn")
	arg_39_0.userAgreeBtn4 = arg_39_0.findTF("frame/raw2Btn")

def var_0_0.jpUIEnter(arg_40_0):
	if PLATFORM_CODE != PLATFORM_JP:
		return

	onButton(arg_40_0, arg_40_0.userAgreeBtn3, function()
		local var_41_0 = require("ShareCfg.UserAgreement3")

		arg_40_0.emit(ChargeMediator.OPEN_USER_AGREE, var_41_0 or ""), SFX_PANEL)
	onButton(arg_40_0, arg_40_0.userAgreeBtn4, function()
		local var_42_0 = require("ShareCfg.UserAgreement4")

		arg_40_0.emit(ChargeMediator.OPEN_USER_AGREE, var_42_0 or ""), SFX_PANEL)

def var_0_0.addRefreshTimer(arg_43_0, arg_43_1):
	local function var_43_0()
		if arg_43_0.refreshTimer:
			arg_43_0.refreshTimer.Stop()

			arg_43_0.refreshTimer = None

	var_43_0()

	arg_43_0.refreshTimer = Timer.New(function()
		local var_45_0 = arg_43_1 + 1 - pg.TimeMgr.GetInstance().GetServerTime()

		if var_45_0 <= 0:
			var_43_0()
			arg_43_0.emit(ChargeMediator.GET_CHARGE_LIST)
		else
			local var_45_1 = pg.TimeMgr.GetInstance().DescCDTime(var_45_0), 1, -1)

	arg_43_0.refreshTimer.Start()
	arg_43_0.refreshTimer.func()

def var_0_0.checkFreeGiftTag(arg_46_0):
	TagTipHelper.FreeGiftTag({
		arg_46_0.giftTip
	})

return var_0_0
