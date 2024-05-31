local var_0_0 = class("FeastInvitationPage", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "FeastInvitationUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.backBtn = arg_2_0.findTF("return")
	arg_2_0.scrollrect = arg_2_0.findTF("left/scrollrect")
	arg_2_0.uilist = UIItemList.New(arg_2_0.findTF("left/scrollrect/conent"), arg_2_0.findTF("left/scrollrect/conent/tpl"))
	arg_2_0.resTicketTr = arg_2_0.findTF("res/ticket")
	arg_2_0.resGiftTr = arg_2_0.findTF("res/gift")
	arg_2_0.resTicket = arg_2_0.findTF("res/ticket/Text").GetComponent(typeof(Text))
	arg_2_0.resGift = arg_2_0.findTF("res/gift/Text").GetComponent(typeof(Text))
	arg_2_0.ticketTr = arg_2_0.findTF("main/ticket")
	arg_2_0.ticketMarkTr = arg_2_0.findTF("main/ticket/finish")
	arg_2_0.giftTr = arg_2_0.findTF("main/gift")
	arg_2_0.giftImg = arg_2_0.giftTr.Find("icon").GetComponent(typeof(Image))
	arg_2_0.giftMarkTr = arg_2_0.findTF("main/gift/finish")
	arg_2_0.ticketTxt = arg_2_0.ticketTr.Find("make/Text").GetComponent(typeof(Text))

	setText(arg_2_0.giftTr.Find("make/Text"), i18n("feast_label_give_gift"))
	setText(arg_2_0.ticketTr.Find("finish/frame/label"), i18n("feast_label_give_invitation_finish"))
	setText(arg_2_0.giftTr.Find("finish/frame/label"), i18n("feast_label_give_gift_finish"))

	arg_2_0.painting = arg_2_0.findTF("main/painting").GetComponent(typeof(Image))
	arg_2_0.puzzlePage = FeastMakeTicketPage.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.giveTicketPage = FeastGiveTicketPage.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.giveGiftPage = FeastGiveGiftPage.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.resWindow = FeastResWindow.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.homeBtn = arg_2_0.findTF("home")

def var_0_0.OnInit(arg_3_0):
	arg_3_0.bind(FeastScene.ON_SKIP_GIVE_GIFT, function(arg_4_0, arg_4_1)
		arg_3_0.giveTicketPage.ExecuteAction("Show", arg_4_1))
	arg_3_0.bind(FeastScene.ON_MAKE_TICKET, function(arg_5_0)
		arg_3_0.OnFlush()
		arg_3_0.UpdateRes())
	arg_3_0.bind(FeastScene.ON_GOT_TICKET, function(arg_6_0)
		arg_3_0.OnFlush())
	arg_3_0.bind(FeastScene.ON_GOT_GIFT, function(arg_7_0)
		arg_3_0.OnFlush()
		arg_3_0.UpdateRes())
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.homeBtn, function()
		arg_3_0.emit(BaseUI.ON_HOME), SFX_PANEL)

def var_0_0.OnFlush(arg_10_0):
	if arg_10_0.feastShip:
		arg_10_0.UpdateMain(arg_10_0.feastShip)

	local var_10_0 = getProxy(FeastProxy).getRawData().GetInvitedFeastShipList()

	arg_10_0.UpdateFeastShips(var_10_0)

def var_0_0.Show(arg_11_0):
	var_0_0.super.Show(arg_11_0)
	pg.UIMgr.GetInstance().OverlayPanel(arg_11_0._tf)

	local var_11_0 = getProxy(FeastProxy).getRawData().GetInvitedFeastShipList()

	arg_11_0.UpdateFeastShips(var_11_0)
	arg_11_0.UpdateRes()
	triggerToggle(arg_11_0.toggles[1], True)
	scrollTo(arg_11_0.scrollrect, 0, 1)

def var_0_0.UpdateRes(arg_12_0):
	local var_12_0, var_12_1 = getProxy(FeastProxy).GetConsumeList()
	local var_12_2 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

	arg_12_0.ticketCnt = var_12_2.getVitemNumber(var_12_0)
	arg_12_0.giftCnt = var_12_2.getVitemNumber(var_12_1)
	arg_12_0.resTicket.text = arg_12_0.ticketCnt
	arg_12_0.resGift.text = arg_12_0.giftCnt

	onButton(arg_12_0, arg_12_0.resTicketTr, function()
		arg_12_0.resWindow.ExecuteAction("Show", var_12_0), SFX_PANEL)
	onButton(arg_12_0, arg_12_0.resGiftTr, function()
		arg_12_0.resWindow.ExecuteAction("Show", var_12_1), SFX_PANEL)

def var_0_0.UpdateFeastShips(arg_15_0, arg_15_1):
	arg_15_0.toggles = {}

	arg_15_0.uilist.make(function(arg_16_0, arg_16_1, arg_16_2)
		if arg_16_0 == UIItemList.EventUpdate:
			local var_16_0 = arg_15_1[arg_16_1 + 1]
			local var_16_1 = var_16_0.GetPrefab()

			LoadSpriteAsync("FeastIcon/" .. var_16_1, function(arg_17_0)
				local var_17_0 = arg_16_2.Find("icon").GetComponent(typeof(Image))

				var_17_0.sprite = arg_17_0

				var_17_0.SetNativeSize())
			setActive(arg_16_2.Find("finish"), var_16_0.GotGift() and var_16_0.GotTicket())
			onToggle(arg_15_0, arg_16_2, function(arg_18_0)
				if arg_18_0:
					arg_15_0.UpdateMain(var_16_0), SFX_PANEL)
			table.insert(arg_15_0.toggles, arg_16_2))
	arg_15_0.uilist.align(#arg_15_1)

local var_0_1 = {
	[0] = i18n("feast_label_make_invitation"),
	(i18n("feast_label_give_invitation"))
}

def var_0_0.UpdateMain(arg_19_0, arg_19_1):
	setActive(arg_19_0.ticketMarkTr, arg_19_1.GotTicket())
	setActive(arg_19_0.giftMarkTr, arg_19_1.GotGift())

	arg_19_0.ticketTxt.text = var_0_1[arg_19_1.GetInvitationState()]

	local var_19_0 = arg_19_1.GetPrefab()

	LoadSpriteAsync("FeastPainting/" .. var_19_0, function(arg_20_0)
		arg_19_0.painting.sprite = arg_20_0

		arg_19_0.painting.SetNativeSize())
	LoadSpriteAsync("FeastCharGift/" .. var_19_0, function(arg_21_0)
		arg_19_0.giftImg.sprite = arg_21_0

		arg_19_0.giftImg.SetNativeSize())
	onButton(arg_19_0, arg_19_0.ticketTr, function()
		if arg_19_1.HasTicket():
			arg_19_0.giveTicketPage.ExecuteAction("Show", arg_19_1)
		elif not arg_19_1.GotTicket():
			if arg_19_0.ticketCnt <= 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("feast_no_invitation"))

				return

			arg_19_0.puzzlePage.ExecuteAction("Show", arg_19_1), SFX_PANEL)
	onButton(arg_19_0, arg_19_0.giftTr, function()
		if not arg_19_1.GotTicket():
			pg.TipsMgr.GetInstance().ShowTips(i18n("feast_cant_give_gift_tip"))

			return

		if arg_19_0.giftCnt <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("feast_no_gift"))

			return

		if not arg_19_1.GotGift():
			arg_19_0.giveGiftPage.ExecuteAction("Show", arg_19_1), SFX_PANEL)

	arg_19_0.feastShip = arg_19_1

def var_0_0.Hide(arg_24_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_24_0._tf, arg_24_0._parentTf)

	if arg_24_0.puzzlePage and arg_24_0.puzzlePage.GetLoaded() and arg_24_0.puzzlePage.isShowing():
		arg_24_0.puzzlePage.Hide()

	if arg_24_0.giveTicketPage and arg_24_0.giveTicketPage.GetLoaded() and arg_24_0.giveTicketPage.isShowing():
		arg_24_0.giveTicketPage.Hide()

	if arg_24_0.giveGiftPage and arg_24_0.giveGiftPage.GetLoaded() and arg_24_0.giveGiftPage.isShowing():
		arg_24_0.giveGiftPage.Hide()

	if arg_24_0.resWindow and arg_24_0.resWindow.GetLoaded() and arg_24_0.resWindow.isShowing():
		arg_24_0.resWindow.Hide()

	var_0_0.super.Hide(arg_24_0)

	arg_24_0.feastShip = None

def var_0_0.onBackPressed(arg_25_0):
	if arg_25_0.puzzlePage and arg_25_0.puzzlePage.GetLoaded() and arg_25_0.puzzlePage.isShowing():
		arg_25_0.puzzlePage.Hide()

		return

	if arg_25_0.giveTicketPage and arg_25_0.giveTicketPage.GetLoaded() and arg_25_0.giveTicketPage.isShowing():
		if not arg_25_0.giveTicketPage.CanInterAction():
			return

		arg_25_0.giveTicketPage.Hide()

		return

	if arg_25_0.giveGiftPage and arg_25_0.giveGiftPage.GetLoaded() and arg_25_0.giveGiftPage.isShowing():
		if not arg_25_0.giveGiftPage.CanInterAction():
			return

		arg_25_0.giveGiftPage.Hide()

		return

	if arg_25_0.resWindow and arg_25_0.resWindow.GetLoaded() and arg_25_0.resWindow.isShowing():
		arg_25_0.resWindow.Hide()

		return

	if arg_25_0.isShowing():
		arg_25_0.Hide()

def var_0_0.OnDestroy(arg_26_0):
	if arg_26_0.puzzlePage:
		arg_26_0.puzzlePage.Destroy()

		arg_26_0.puzzlePage = None

	if arg_26_0.giveTicketPage:
		arg_26_0.giveTicketPage.Destroy()

		arg_26_0.giveTicketPage = None

	if arg_26_0.giveGiftPage:
		arg_26_0.giveGiftPage.Destroy()

		arg_26_0.giveGiftPage = None

	if arg_26_0.resWindow:
		arg_26_0.resWindow.Destroy()

		arg_26_0.resWindow = None

	if arg_26_0.isShowing():
		arg_26_0.Hide()

return var_0_0
