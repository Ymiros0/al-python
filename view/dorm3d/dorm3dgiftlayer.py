local var_0_0 = class("Dorm3dGiftLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "Dorm3dGiftUI"

def var_0_0.init(arg_2_0):
	local var_2_0 = arg_2_0._tf.Find("btn_back")

	onButton(arg_2_0, var_2_0, function()
		arg_2_0.closeView(), SFX_CANCEL)

	arg_2_0.rtGiftPanel = arg_2_0._tf.Find("gift_panel")

	eachChild(arg_2_0.rtGiftPanel.Find("content/toggles"), function(arg_4_0)
		onToggle(arg_2_0, arg_4_0, function(arg_5_0)
			if arg_5_0:
				arg_2_0.UpdateSelectToggle(arg_4_0.name), SFX_PANEL))

	local var_2_1 = arg_2_0.rtGiftPanel.Find("content/view/container")

	arg_2_0.giftItemList = UIItemList.New(var_2_1, var_2_1.Find("tpl"))

	arg_2_0.giftItemList.make(function(arg_6_0, arg_6_1, arg_6_2)
		arg_6_1 = arg_6_1 + 1

		if arg_6_0 == UIItemList.EventUpdate:
			arg_2_0.UpdateGift(arg_6_2, arg_2_0.filterGiftIds[arg_6_1]))

	arg_2_0.btnConfirm = arg_2_0.rtGiftPanel.Find("bottom/btn_confirm")

	onButton(arg_2_0, arg_2_0.btnConfirm, function()
		arg_2_0.ConfirmGiveGifts(), SFX_CONFIRM)

	arg_2_0.rtFavorPanel = arg_2_0._tf.Find("favor_panel")
	arg_2_0.rtInfoWindow = arg_2_0._tf.Find("info_window")

	onButton(arg_2_0, arg_2_0.rtInfoWindow.Find("bg"), function()
		arg_2_0.HideInfoWindow(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0.rtInfoWindow.Find("panel/title/btn_close"), function()
		arg_2_0.HideInfoWindow(), SFX_CANCEL)

	arg_2_0.rtLackWindow = arg_2_0._tf.Find("lack_window")

	onButton(arg_2_0, arg_2_0.rtLackWindow.Find("bg"), function()
		arg_2_0.HideLackWindow(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0.rtLackWindow.Find("panel/title/btn_close"), function()
		arg_2_0.HideLackWindow(), SFX_CANCEL)
	pg.UIMgr.GetInstance().OverlayPanelPB(arg_2_0._tf, {
		pbList = {
			arg_2_0.rtGiftPanel
		},
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_DORM3D
	})

def var_0_0.SetApartment(arg_12_0, arg_12_1):
	arg_12_0.apartment = arg_12_1
	arg_12_0.giftIds = arg_12_0.apartment.getGiftIds()
	arg_12_0.proxy = getProxy(ApartmentProxy)

def var_0_0.didEnter(arg_13_0):
	triggerToggle(arg_13_0.rtGiftPanel.Find("content/toggles/all"), True)
	arg_13_0.UpdateFavorPanel()
	arg_13_0.UpdateConfirmBtn()

def var_0_0.UpdateSelectToggle(arg_14_0, arg_14_1):
	if arg_14_0.toggleState == arg_14_1:
		return

	arg_14_0.toggleState = arg_14_1
	arg_14_0.filterGiftIds = underscore.filter(arg_14_0.giftIds, function(arg_15_0)
		return arg_14_1 == "all" or arg_14_1 == "normal" == (pg.dorm3d_gift[arg_15_0].ship_group_id == 0))

	table.sort(arg_14_0.filterGiftIds, CompareFuncs({
		function(arg_16_0)
			return (arg_14_0.proxy.getGiftCount(arg_16_0) > 0 and -1 or 1) * (pg.dorm3d_gift[arg_16_0].ship_group_id == 0 and 1 or 2),
		function(arg_17_0)
			return pg.dorm3d_gift[arg_17_0].ship_group_id > 0 and arg_14_0.proxy.isGiveGiftDone(arg_17_0) and 1 or 0,
		function(arg_18_0)
			return arg_18_0
	}))
	arg_14_0.giftItemList.align(#arg_14_0.filterGiftIds)

def var_0_0.UpdateGift(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0 = arg_19_1.Find("base")
	local var_19_1 = Drop.New({
		type = DROP_TYPE_DORM3D_GIFT,
		id = arg_19_2,
		count = arg_19_0.proxy.getGiftCount(arg_19_2)
	})

	updateDorm3dIcon(var_19_0.Find("Dorm3dIconTpl"), var_19_1)
	setText(var_19_0.Find("info/name"), var_19_1.getName())

	local var_19_2 = var_19_1.getConfig("ship_group_id") != 0

	setActive(var_19_0.Find("mark"), var_19_2)
	setActive(var_19_0.Find("bg/normal"), not var_19_2)
	setActive(var_19_0.Find("bg/pro"), var_19_2)
	setText(var_19_0.Find("info/Text"), i18n("dorm3d_gift_owner_num") .. string.format("%d", var_19_1.count))

	local var_19_3 = var_19_0.Find("info/effect")

	setActive(var_19_3.Find("favor"), True)

	local var_19_4 = pg.dorm3d_favor_trigger[var_19_1.cfg.favor_trigger_id].num

	setText(var_19_3.Find("favor/number"), "+" .. var_19_4)
	setActive(var_19_3.Find("story"), var_19_2)
	onButton(arg_19_0, var_19_0.Find("info/btn_info"), function()
		arg_19_0.OpenInfoWindow(var_19_1), SFX_PANEL)

	local var_19_5 = var_19_2 and arg_19_0.proxy.isGiveGiftDone(arg_19_2)
	local var_19_6 = var_19_1.count == 0 and not var_19_5

	setActive(var_19_0.Find("info/lack"), var_19_6)
	onButton(arg_19_0, var_19_0.Find("info/lack"), function()
		arg_19_0.OpenLackWindow(var_19_1), SFX_PANEL)
	setActive(arg_19_1.Find("mask"), var_19_5)
	setText(arg_19_1.Find("mask/Image/Text"), "is Done")
	onToggle(arg_19_0, arg_19_1, function(arg_22_0)
		if arg_22_0:
			arg_19_0.selectGiftId = arg_19_2

			arg_19_0.UpdateConfirmBtn()
		elif arg_19_0.selectGiftId == arg_19_2:
			arg_19_0.selectGiftId = None

			arg_19_0.UpdateConfirmBtn(), SFX_PANEL)
	setToggleEnabled(arg_19_1, not var_19_5)
	triggerToggle(arg_19_1, False)

def var_0_0.SingleUpdateGift(arg_23_0, arg_23_1):
	local var_23_0 = table.indexof(arg_23_0.filterGiftIds, arg_23_1)

	if var_23_0 > 0:
		arg_23_0.UpdateGift(arg_23_0.giftItemList.container.GetChild(var_23_0 - 1), arg_23_1)

def var_0_0.UpdateConfirmBtn(arg_24_0):
	setButtonEnabled(arg_24_0.btnConfirm, tobool(arg_24_0.selectGiftId))

def var_0_0.ConfirmGiveGifts(arg_25_0):
	if arg_25_0.proxy.getGiftCount(arg_25_0.selectGiftId) == 0:
		if pg.dorm3d_gift[arg_25_0.selectGiftId].ship_group_id > 0 and arg_25_0.proxy.isGiveGiftDone(arg_25_0.selectGiftId):
			pg.TipsMgr.GetInstance().ShowTips(i18n("该礼物已赠送"))
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("当前未拥有该礼物"))

		return

	arg_25_0.emit(Dorm3dGiftMediator.GIVE_GIFT, arg_25_0.selectGiftId)

def var_0_0.AfterGiveGift(arg_26_0, arg_26_1):
	local var_26_0 = pg.dorm3d_gift[arg_26_1]
	local var_26_1 = {}

	if var_26_0.reply_dialogue_id != 0:
		table.insert(var_26_1, function(arg_27_0)
			arg_26_0.emit(Dorm3dGiftMediator.DO_TALK, var_26_0.reply_dialogue_id, arg_27_0))

	local var_26_2 = arg_26_0.proxy.getGiftUnlockTalk(arg_26_0.apartment.configId, arg_26_1)

	if var_26_2:
		table.insert(var_26_1, function(arg_28_0)
			pg.TipsMgr.GetInstance().ShowTips(string.format("talk %d is unlocked", var_26_2))
			arg_28_0())

	seriesAsync(var_26_1, function()
		arg_26_0.emit(Dorm3dGiftMediator.CHECK_LEVEL_UP))

def var_0_0.UpdateFavorPanel(arg_30_0):
	local var_30_0 = arg_30_0.apartment.favor
	local var_30_1 = arg_30_0.apartment.getNextExp()

	setText(arg_30_0.rtFavorPanel.Find("info/Text"), string.format("Lv.%d", arg_30_0.apartment.level))
	setText(arg_30_0.rtFavorPanel.Find("info/Text_1"), string.format("<color=#FFFFFF>%d</color>/%d", var_30_0, var_30_1))
	setSlider(arg_30_0.rtFavorPanel.Find("slider"), 0, var_30_1, var_30_0)

def var_0_0.OpenInfoWindow(arg_31_0, arg_31_1):
	local var_31_0 = arg_31_0.rtInfoWindow.Find("panel")

	setText(var_31_0.Find("title/Text"), i18n("words_information"))
	updateDorm3dIcon(var_31_0.Find("middle/Dorm3dIconTpl"), arg_31_1)

	local var_31_1 = arg_31_1.getConfig("ship_group_id") != 0

	setActive(var_31_0.Find("middle/Dorm3dIconTpl/mark"), var_31_1)
	setText(var_31_0.Find("middle/Text"), "???")
	onButton(arg_31_0, var_31_0.Find("bottom/btn_buy"), function()
		pg.TipsMgr.GetInstance().ShowTips("without shop config"), SFX_CONFIRM)
	setActive(arg_31_0.rtInfoWindow, True)
	pg.UIMgr.GetInstance().OverlayPanel(arg_31_0.rtInfoWindow, {
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_DORM3D
	})

def var_0_0.HideInfoWindow(arg_33_0):
	setActive(arg_33_0.rtInfoWindow, False)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_33_0.rtInfoWindow, arg_33_0._tf)

def var_0_0.OpenLackWindow(arg_34_0, arg_34_1):
	local var_34_0 = arg_34_0.rtLackWindow.Find("panel")

	setText(var_34_0.Find("title/Text"), i18n("child_msg_title_detail"))
	updateDorm3dIcon(var_34_0.Find("middle/Dorm3dIconTpl"), arg_34_1)

	local var_34_1 = arg_34_1.getConfig("ship_group_id") != 0

	setActive(var_34_0.Find("middle/Dorm3dIconTpl/mark"), var_34_1)
	setText(var_34_0.Find("middle/info/name"), arg_34_1.getName())
	setText(var_34_0.Find("middle/info/count"), string.format("count.<color=#39bfff>%d</color>", arg_34_1.count))
	setText(var_34_0.Find("middle/info/desc"), arg_34_1.getConfig("display"))
	setText(var_34_0.Find("line/lack/Text"), "lack")

	local var_34_2 = ItemTipPanel.GetDropLackConfig(arg_34_1)
	local var_34_3 = var_34_2 and var_34_2.description or {}
	local var_34_4 = var_34_0.Find("bottom/container")

	UIItemList.StaticAlign(var_34_4, var_34_4.Find("tpl"), #var_34_3, function(arg_35_0, arg_35_1, arg_35_2)
		arg_35_1 = arg_35_1 + 1

		if arg_35_0 == UIItemList.EventUpdate:
			local var_35_0 = var_34_3[arg_35_1]
			local var_35_1, var_35_2, var_35_3 = unpack(var_35_0)

			setText(arg_35_2.Find("Text"), var_35_1)
			setText(arg_35_2.Find("btn_go/Text"), i18n("feast_res_window_go_label"))

			local var_35_4, var_35_5, var_35_6 = unpack(var_34_2)
			local var_35_7, var_35_8 = unpack(var_35_5)
			local var_35_9 = #var_35_7 > 0

			if var_35_6 and var_35_6 != 0:
				var_35_9 = var_35_9 and getProxy(ActivityProxy).IsActivityNotEnd(var_35_6)

			setActive(arg_35_2.Find("btn_go"), var_35_9)
			onButton(arg_34_0, arg_35_2.Find("btn_go"), function()
				ItemTipPanel.ConfigGoScene(var_35_7, var_35_8, function()
					arg_34_0.closeView()), SFX_PANEL))
	setActive(arg_34_0.rtLackWindow, True)
	pg.UIMgr.GetInstance().OverlayPanel(arg_34_0.rtLackWindow, {
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_DORM3D
	})

def var_0_0.HideLackWindow(arg_38_0):
	setActive(arg_38_0.rtLackWindow, False)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_38_0.rtLackWindow, arg_38_0._tf)

def var_0_0.onBackPressed(arg_39_0):
	if isActive(arg_39_0.rtInfoWindow):
		arg_39_0.HideInfoWindow()

		return

	if isActive(arg_39_0.rtLackWindow):
		arg_39_0.HideLackWindow()

		return

	var_0_0.super.onBackPressed(arg_39_0)

def var_0_0.willExit(arg_40_0):
	if isActive(arg_40_0.rtInfoWindow):
		arg_40_0.HideInfoWindow()

	if isActive(arg_40_0.rtLackWindow):
		arg_40_0.HideLackWindow()

	pg.UIMgr.GetInstance().UnblurPanel(arg_40_0._tf)

return var_0_0
