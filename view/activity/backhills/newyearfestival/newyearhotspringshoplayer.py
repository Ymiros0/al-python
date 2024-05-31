local var_0_0 = class("NewYearHotSpringShopLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "NewYearHotSpringShopUI"

def var_0_0.init(arg_2_0):
	arg_2_0.goodsContainer = arg_2_0._tf.Find("Box/Container/Goods")
	arg_2_0.chat = arg_2_0._tf.Find("Box/Bubble")
	arg_2_0.chatAnimator = GetComponent(arg_2_0.chat, typeof(Animator))
	arg_2_0.chatAnimEvent = GetComponent(arg_2_0.chat, typeof(DftAniEvent))
	arg_2_0.chatText = arg_2_0.chat.Find("BubbleText")
	arg_2_0.chatClick = arg_2_0.chat.Find("BubbleClick")

	setActive(arg_2_0.chat, False)
	setLocalScale(arg_2_0.chat, {
		x = 0,
		y = 0
	})
	setActive(arg_2_0.chat, True)

	arg_2_0.msgbox = arg_2_0._tf.Find("Msgbox")

	setActive(arg_2_0.msgbox, False)

	arg_2_0.contentText = arg_2_0.msgbox.Find("window/msg_panel/content").GetComponent("RichText")

def var_0_0.SetShop(arg_3_0, arg_3_1):
	arg_3_0.shop = arg_3_1

def var_0_0.didEnter(arg_4_0):
	onButton(arg_4_0, arg_4_0._tf.Find("Top/Back"), function()
		arg_4_0.closeView(), SOUND_BACK)
	onButton(arg_4_0, arg_4_0._tf.Find("Top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.hotspring_shop_help.tip
		}), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.msgbox.Find("BG"), function()
		setActive(arg_4_0.msgbox, False))
	onButton(arg_4_0, arg_4_0.msgbox.Find("window/button_container/Button1"), function()
		setActive(arg_4_0.msgbox, False), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.chatClick, function()
		arg_4_0.HideChat())
	onButton(arg_4_0, arg_4_0._tf.Find("Box/Spine"), function()
		arg_4_0.DisplayChat({
			"hotspring_shop_touch1",
			"hotspring_shop_touch2",
			"hotspring_shop_touch3"
		})
		arg_4_0.role.SetActionOnce("touch"))
	arg_4_0.ShowEnterMsg()

	arg_4_0.role = SpineRole.New()

	arg_4_0.role.SetData("mingshi_2")
	arg_4_0.LoadingOn()
	arg_4_0.role.Load(function()
		arg_4_0.role.SetParent(arg_4_0._tf.Find("Box/Spine"))
		arg_4_0.role.SetAction("stand")
		arg_4_0.role.SetActionCallBack(function(arg_12_0)
			if arg_12_0 == "finish":
				arg_4_0.role.SetAction("stand"))
		arg_4_0.LoadingOff(), True)
	arg_4_0.UpdateView()
	pg.UIMgr.GetInstance().BlurPanel(arg_4_0._tf)

def var_0_0.ShowEnterMsg(arg_13_0):
	local var_13_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

	if not var_13_0 or var_13_0.isEnd():
		arg_13_0.DisplayChat({
			"hotspring_shop_end"
		})

		return

	if _.all(_.values(arg_13_0.shop.goods), function(arg_14_0)
		return not arg_14_0.canPurchase()):
		arg_13_0.DisplayChat({
			"hotspring_shop_finish"
		})

		return

	arg_13_0.DisplayChat({
		"hotspring_shop_enter1",
		"hotspring_shop_enter2"
	})

def var_0_0.UpdateView(arg_15_0):
	local var_15_0 = arg_15_0.shop.getResId()
	local var_15_1 = getProxy(PlayerProxy).getRawData()[id2res(var_15_0)] or 0

	setText(arg_15_0._tf.Find("Top/Ticket/TicketText"), var_15_1)
	arg_15_0.UpdateGoods()

def var_0_0.UpdateGoods(arg_16_0):
	local var_16_0 = _.values(arg_16_0.shop.goods)

	table.sort(var_16_0, function(arg_17_0, arg_17_1)
		return arg_17_0.id < arg_17_1.id)
	UIItemList.StaticAlign(arg_16_0.goodsContainer, arg_16_0.goodsContainer.GetChild(0), #var_16_0, function(arg_18_0, arg_18_1, arg_18_2)
		if arg_18_0 != UIItemList.EventUpdate:
			return

		local var_18_0 = var_16_0[arg_18_1 + 1]
		local var_18_1 = var_18_0.canPurchase()

		setActive(arg_18_2.Find("mask"), not var_18_1)

		local var_18_2 = var_18_0.getConfig("commodity_type")
		local var_18_3 = var_18_0.getConfig("commodity_id")
		local var_18_4 = {
			type = var_18_2,
			id = var_18_3,
			count = var_18_0.getConfig("num")
		}

		updateDrop(arg_18_2.Find("Icon"), var_18_4)
		onButton(arg_16_0, arg_18_2, function()
			arg_16_0.OnClickCommodity(var_18_0, function(arg_20_0, arg_20_1)
				arg_16_0.OnPurchase(var_18_0, arg_20_1)), SFX_PANEL))

def var_0_0.CheckRes(arg_21_0, arg_21_1, arg_21_2):
	if not arg_21_1.canPurchase():
		arg_21_0.DisplayChat({
			"hotspring_shop_exchanged"
		})

		return False

	if Drop.New({
		type = arg_21_1.getConfig("resource_category"),
		id = arg_21_1.getConfig("resource_type")
	}).getOwnedCount() < arg_21_1.getConfig("resource_num") * arg_21_2:
		arg_21_0.DisplayChat({
			"hotspring_shop_insufficient"
		})

		return False

	return True

def var_0_0.Purchase(arg_22_0, arg_22_1, arg_22_2, arg_22_3, arg_22_4):
	arg_22_0.ShowMsgbox({
		content = i18n("hotspring_shop_exchange", arg_22_1.getConfig("resource_num") * arg_22_2, arg_22_1.getConfig("num") * arg_22_2, arg_22_3),
		def onYes:()
			if arg_22_0.CheckRes(arg_22_1, arg_22_2):
				arg_22_4(arg_22_1, arg_22_2)
	})

def var_0_0.OnClickCommodity(arg_24_0, arg_24_1, arg_24_2):
	if not arg_24_0.CheckRes(arg_24_1, 1):
		return

	local var_24_0 = Drop.New({
		id = arg_24_1.getConfig("commodity_id"),
		type = arg_24_1.getConfig("commodity_type")
	})

	arg_24_0.Purchase(arg_24_1, 1, var_24_0.getConfig("name"), arg_24_2)

def var_0_0.OnPurchase(arg_25_0, arg_25_1, arg_25_2):
	local var_25_0 = arg_25_0.shop.activityId

	arg_25_0.emit(NewYearHotSpringShopMediator.ON_ACT_SHOPPING, var_25_0, 1, arg_25_1.id, arg_25_2)

def var_0_0.OnShoppingDone(arg_26_0):
	arg_26_0.DisplayChat({
		"hotspring_shop_success1",
		"hotspring_shop_success2"
	})

def var_0_0.ShowMsgbox(arg_27_0, arg_27_1):
	setActive(arg_27_0.msgbox, True)

	arg_27_0.contentText.text = arg_27_1.content

	local var_27_0 = arg_27_0.msgbox.Find("window/button_container/Button2")

	onButton(arg_27_0, var_27_0, function()
		setActive(arg_27_0.msgbox, False)
		existCall(arg_27_1.onYes), SFX_CONFIRM)

def var_0_0.DisplayChat(arg_29_0, arg_29_1):
	arg_29_0.HideChat()
	onNextTick(function()
		local var_30_0 = LeanTween.delayedCall(go(arg_29_0.chat), 10, System.Action(function()
			arg_29_0.HideChat()))

		arg_29_0.chatTween = var_30_0.uniqueId

		local var_30_1 = arg_29_1[math.random(#arg_29_1)]
		local var_30_2 = i18n(var_30_1)

		arg_29_0.chatAnimator.ResetTrigger("Shrink")
		arg_29_0.chatAnimator.SetTrigger("Pop")
		arg_29_0.chatAnimEvent.SetTriggerEvent(function()
			setText(arg_29_0.chatText, var_30_2)))

def var_0_0.HideChat(arg_33_0):
	if arg_33_0.chatTween:
		arg_33_0.chatAnimator.ResetTrigger("Pop")
		arg_33_0.chatAnimator.SetTrigger("Shrink")
		arg_33_0.chatAnimEvent.SetTriggerEvent(None)
		LeanTween.cancel(arg_33_0.chatTween)

		arg_33_0.chatTween = None

def var_0_0.LoadingOn(arg_34_0):
	if arg_34_0.animating:
		return

	arg_34_0.animating = True

	pg.UIMgr.GetInstance().LoadingOn(False)

def var_0_0.LoadingOff(arg_35_0):
	if not arg_35_0.animating:
		return

	pg.UIMgr.GetInstance().LoadingOff()

	arg_35_0.animating = False

def var_0_0.willExit(arg_36_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_36_0._tf)
	arg_36_0.HideChat()
	arg_36_0.role.Dispose()
	arg_36_0.LoadingOff()

return var_0_0
