local var_0_0 = class("ItemInfoLayer", import("..base.BaseUI"))
local var_0_1 = 5
local var_0_2 = 11
local var_0_3 = {
	RESOLVE = 2,
	COMPOSE = 1
}

def var_0_0.getUIName(arg_1_0):
	return "ItemInfoUI"

def var_0_0.init(arg_2_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf, False, {
		weight = arg_2_0.getWeightFromData()
	})

	arg_2_0.window = arg_2_0.findTF("window")

	setText(arg_2_0.window.Find("top/bg/infomation/title"), i18n("words_information"))

	arg_2_0.btnContent = arg_2_0.window.Find("actions")
	arg_2_0.okBtn = arg_2_0.btnContent.Find("ok_button")

	setText(arg_2_0.okBtn.Find("pic"), i18n("msgbox_text_confirm"))

	arg_2_0.useBtn = arg_2_0.btnContent.Find("use_button")
	arg_2_0.batchUseBtn = arg_2_0.btnContent.Find("batch_use_button")
	arg_2_0.useOneBtn = arg_2_0.btnContent.Find("use_one_button")
	arg_2_0.composeBtn = arg_2_0.btnContent.Find("compose_button")
	arg_2_0.resolveBtn = arg_2_0.btnContent.Find("resolve_button")

	setText(arg_2_0.resolveBtn.Find("pic"), i18n("msgbox_text_analyse"))

	arg_2_0.loveRepairBtn = arg_2_0.btnContent.Find("love_lettle_repair_button")

	setText(arg_2_0.loveRepairBtn.Find("pic"), i18n("loveletter_exchange_button"))

	arg_2_0.metaskillBtn = arg_2_0.btnContent.Find("metaskill_use_btn")

	setText(arg_2_0.metaskillBtn.Find("pic"), i18n("msgbox_text_use"))

	arg_2_0.itemTF = arg_2_0.window.Find("item")
	arg_2_0.operatePanel = arg_2_0.findTF("operate")
	arg_2_0.countTF = arg_2_0.operatePanel.Find("item/left/own/Text").GetComponent(typeof(Text))
	arg_2_0.keepFateTog = arg_2_0.operatePanel.Find("got/keep_tog")

	setText(arg_2_0.keepFateTog.Find("label"), i18n("keep_fate_tip"))

	arg_2_0.operateBtns = {}
	arg_2_0.operateBtns.Confirm = arg_2_0.operatePanel.Find("actions/confirm_button")
	arg_2_0.operateBtns.Cancel = arg_2_0.operatePanel.Find("actions/cancel_button")
	arg_2_0.operateBtns.Resolve = arg_2_0.operatePanel.Find("actions/resolve_button")

	setText(arg_2_0.operateBtns.Confirm.Find("label"), i18n("msgbox_text_confirm"))
	setText(arg_2_0.operateBtns.Cancel.Find("label"), i18n("msgbox_text_cancel"))
	setText(arg_2_0.operateBtns.Resolve.Find("label"), i18n("msgbox_text_analyse"))
	SetActive(arg_2_0.operatePanel, False)
	SetActive(arg_2_0.window, True)

	arg_2_0.operateMode = None
	arg_2_0.operateBonusList = arg_2_0.operatePanel.Find("got/panel_bg/list")
	arg_2_0.operateBonusTpl = arg_2_0.operatePanel.Find("got/panel_bg/list/item")
	arg_2_0.operateCountdesc = arg_2_0.operatePanel.Find("count/image_text")
	arg_2_0.operateValue = arg_2_0.operatePanel.Find("count/number_panel/value")
	arg_2_0.operateLeftButton = arg_2_0.operatePanel.Find("count/number_panel/left")
	arg_2_0.operateRightButton = arg_2_0.operatePanel.Find("count/number_panel/right")
	arg_2_0.operateMaxButton = arg_2_0.operatePanel.Find("count/max")

def var_0_0.setDrop(arg_3_0, arg_3_1):
	if arg_3_1.type == DROP_TYPE_SHIP:
		arg_3_0.setItemInfo(arg_3_1, arg_3_0.itemTF)
	elif arg_3_1.type == DROP_TYPE_ITEM:
		arg_3_1.count = getProxy(BagProxy).getItemCountById(arg_3_1.id)

		arg_3_0.setItem(arg_3_1)
	else
		assert(False, "do not support current kind of type. " .. arg_3_1.type)

def var_0_0.setItemInfo(arg_4_0, arg_4_1, arg_4_2):
	updateDrop(arg_4_2.Find("left/IconTpl"), setmetatable({
		count = 0
	}, {
		__index = arg_4_1
	}))
	UpdateOwnDisplay(arg_4_2.Find("left/own"), arg_4_1)
	RegisterDetailButton(arg_4_0, arg_4_2.Find("left/detail"), arg_4_1)
	setText(arg_4_2.Find("display_panel/name_container/name/Text"), arg_4_1.getConfig("name"))
	setText(arg_4_2.Find("display_panel/desc/Text"), arg_4_1.desc)

	local var_4_0 = arg_4_2.Find("display_panel/name_container/shiptype")

	setActive(var_4_0, arg_4_1.type == DROP_TYPE_SHIP)

	if arg_4_1.type == DROP_TYPE_SHIP:
		GetImageSpriteFromAtlasAsync("shiptype", shipType2print(arg_4_1.getConfig("type")), var_4_0, False)

def var_0_0.updateItemCount(arg_5_0, arg_5_1):
	arg_5_0.countTF.text = arg_5_1

def var_0_0.setItem(arg_6_0, arg_6_1):
	arg_6_0.setItemInfo(arg_6_1, arg_6_0.itemTF)

	arg_6_0.itemVO = arg_6_1.getSubClass()

	eachChild(arg_6_0.btnContent, function(arg_7_0)
		setActive(arg_7_0, arg_7_0 == arg_6_0.okBtn))

	if not Item.CanInBag(arg_6_0.itemVO.id):
		return

	local var_6_0 = arg_6_0.itemVO.getConfig("compose_number")

	if var_6_0 > 0 and var_6_0 <= arg_6_0.itemVO.count:
		arg_6_0.setItemInfo(arg_6_1, arg_6_0.operatePanel.Find("item"))

		arg_6_0.operateMax = arg_6_0.itemVO.count / var_6_0

		setActive(arg_6_0.composeBtn, True)
		setActive(arg_6_0.okBtn, False)

	if arg_6_0.itemVO.getConfig("usage") == ItemUsage.SOS:
		setText(arg_6_0.useBtn.Find("text"), 1)
		setActive(arg_6_0.useBtn, True)
		setActive(arg_6_0.okBtn, False)

	local var_6_1 = arg_6_0.itemVO.getConfig("type")

	if arg_6_0.itemVO.CanOpen():
		setText(arg_6_0.useBtn.Find("text"), 1)
		setActive(arg_6_0.useBtn, True)

		if arg_6_0.itemVO.count > 1:
			setText(arg_6_0.batchUseBtn.Find("text"), math.min(arg_6_0.itemVO.count, 10))
			setActive(arg_6_0.batchUseBtn, True)

		setActive(arg_6_0.okBtn, False)
	elif var_6_1 == Item.BLUEPRINT_TYPE:
		local var_6_2 = getProxy(TechnologyProxy)
		local var_6_3 = var_6_2.GetBlueprint4Item(arg_6_0.itemVO.id)

		if not LOCK_FRAGMENT_SHOP and var_6_3 and var_6_2.getBluePrintById(var_6_3).isMaxLevel():
			setActive(arg_6_0.resolveBtn, True)
			arg_6_0.UpdateBlueprintResolveNum()

		arg_6_0.setItemInfo(arg_6_1, arg_6_0.operatePanel.Find("item"))
	elif var_6_1 == Item.TEC_SPEEDUP_TYPE:
		setActive(arg_6_0.resolveBtn, True)
		arg_6_0.UpdateSpeedUpResolveNum()
		arg_6_0.setItemInfo(arg_6_1, arg_6_0.operatePanel.Find("item"))
	elif var_6_1 == Item.LOVE_LETTER_TYPE:
		local var_6_4 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_LOVE_LETTER)

		setActive(arg_6_0.loveRepairBtn, var_6_4 and not var_6_4.isEnd() and var_6_4.data1 > 0 and arg_6_0.itemVO.extra == 31201)
		onButton(arg_6_0, arg_6_0.loveRepairBtn, function()
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("loveletter_exchange_confirm"),
				def onYes:()
					arg_6_0.emit(ItemInfoMediator.EXCHANGE_LOVE_LETTER_ITEM, var_6_4.id)
			}), SFX_PANEL)
	elif var_6_1 == Item.METALESSON_TYPE:
		setActive(arg_6_0.metaskillBtn, True)
		onButton(arg_6_0, arg_6_0.metaskillBtn, function()
			arg_6_0.closeView()
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.METACHARACTER), SFX_PANEL)
	elif var_6_1 == Item.SKIN_ASSIGNED_TYPE:
		setActive(arg_6_0.useOneBtn, arg_6_0.contextData.confirmCall)
		onButton(arg_6_0, arg_6_0.useOneBtn, function()
			arg_6_0.contextData.confirmCall()
			arg_6_0.closeView(), SFX_PANEL)

def var_0_0.closeView(arg_12_0):
	if arg_12_0.playing:
		return

	var_0_0.super.closeView(arg_12_0)

def var_0_0.didEnter(arg_13_0):
	local var_13_0 = arg_13_0.findTF("OpenBox(Clone)")

	if var_13_0:
		SetActive(var_13_0, False)

	onButton(arg_13_0, arg_13_0._tf.Find("bg"), function()
		arg_13_0.closeView(), SFX_CANCEL)
	onButton(arg_13_0, arg_13_0._tf.Find("window/top/btnBack"), function()
		arg_13_0.closeView(), SFX_CANCEL)
	onButton(arg_13_0, arg_13_0.okBtn, function()
		arg_13_0.closeView(), SFX_CONFIRM)
	onButton(arg_13_0, arg_13_0.useBtn, function()
		arg_13_0.emit(ItemInfoMediator.USE_ITEM, arg_13_0.itemVO.id, 1), SFX_CONFIRM)
	onButton(arg_13_0, arg_13_0.batchUseBtn, function()
		arg_13_0.emit(ItemInfoMediator.USE_ITEM, arg_13_0.itemVO.id, math.min(arg_13_0.itemVO.count, 10)), SFX_CONFIRM)
	onButton(arg_13_0, arg_13_0.composeBtn, function()
		SetActive(arg_13_0.operatePanel, True)
		SetActive(arg_13_0.window, False)

		arg_13_0.operateMode = var_0_3.COMPOSE

		arg_13_0.SetOperateCount(1), SFX_CONFIRM)
	onButton(arg_13_0, arg_13_0.resolveBtn, function()
		SetActive(arg_13_0.operatePanel, True)
		SetActive(arg_13_0.window, False)

		arg_13_0.operateMode = var_0_3.RESOLVE

		arg_13_0.SetOperateCount(1), SFX_PANEL)
	pressPersistTrigger(arg_13_0.operateLeftButton, 0.5, function()
		if not arg_13_0.UpdateCount(arg_13_0.operateCount - 1):
			return

		arg_13_0.SetOperateCount(arg_13_0.operateCount - 1), None, True, True, 0.1, SFX_PANEL)
	pressPersistTrigger(arg_13_0.operateRightButton, 0.5, function()
		if not arg_13_0.UpdateCount(arg_13_0.operateCount + 1):
			return

		arg_13_0.SetOperateCount(arg_13_0.operateCount + 1), None, True, True, 0.1, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.operateMaxButton, function()
		arg_13_0.SetOperateCount(arg_13_0.operateMax), SFX_PANEL)
	onButton(arg_13_0, arg_13_0.operateBtns.Cancel, function()
		SetActive(arg_13_0.operatePanel, False)
		SetActive(arg_13_0.window, True), SFX_CANCEL)
	onButton(arg_13_0, arg_13_0.operateBtns.Confirm, function()
		arg_13_0.emit(ItemInfoMediator.COMPOSE_ITEM, arg_13_0.itemVO.id, arg_13_0.operateCount)

		local var_25_0 = arg_13_0.itemVO.getConfig("compose_number")

		if var_25_0 > arg_13_0.itemVO.count - arg_13_0.operateCount * var_25_0:
			triggerButton(arg_13_0.operateBtns.Cancel)
		else
			arg_13_0.SetOperateCount(1), SFX_CONFIRM)
	onButton(arg_13_0, arg_13_0.operateBtns.Resolve, function()
		arg_13_0.emit(ItemInfoMediator.SELL_BLUEPRINT, Drop.New({
			type = DROP_TYPE_ITEM,
			id = arg_13_0.itemVO.id,
			count = arg_13_0.operateCount
		})), SFX_CONFIRM)

	local var_13_1 = getProxy(PlayerProxy).getData()
	local var_13_2 = GetComponent(arg_13_0.keepFateTog, typeof(Toggle))

	arg_13_0.keepFateState = not var_13_1.GetCommonFlag(SHOW_DONT_KEEP_FATE_ITEM)
	var_13_2.isOn = arg_13_0.keepFateState

	local function var_13_3()
		arg_13_0.UpdateBlueprintResolveNum()
		arg_13_0.SetOperateCount(1)

	onToggle(arg_13_0, arg_13_0.keepFateTog, function(arg_28_0)
		arg_13_0.keepFateState = arg_28_0

		if arg_28_0:
			pg.m02.sendNotification(GAME.CANCEL_COMMON_FLAG, {
				flagID = SHOW_DONT_KEEP_FATE_ITEM
			})
		else
			pg.m02.sendNotification(GAME.COMMON_FLAG, {
				flagID = SHOW_DONT_KEEP_FATE_ITEM
			})

		var_13_3())
	var_13_3()

def var_0_0.UpdateCount(arg_29_0, arg_29_1):
	if arg_29_0.operateMode == var_0_3.COMPOSE:
		local var_29_0 = arg_29_0.itemVO.getConfig("target_id")

		if not var_29_0 or var_29_0 <= 0:
			return False

		arg_29_1 = math.clamp(arg_29_1, 1, math.floor(arg_29_0.itemVO.count / arg_29_0.itemVO.getConfig("compose_number")))

		return arg_29_0.operateCount != arg_29_1
	elif arg_29_0.operateMode == var_0_3.RESOLVE:
		arg_29_1 = math.clamp(arg_29_1, 1, arg_29_0.itemVO.count)

		return arg_29_0.operateCount != arg_29_1

def var_0_0.SetOperateCount(arg_30_0, arg_30_1):
	if arg_30_0.operateMode == var_0_3.COMPOSE:
		local var_30_0 = arg_30_0.itemVO.getConfig("target_id")

		if not var_30_0 or var_30_0 <= 0:
			return

		local var_30_1 = arg_30_0.itemVO.getConfig("compose_number")

		arg_30_1 = math.clamp(arg_30_1, 1, math.floor(arg_30_0.itemVO.count / var_30_1))

		if arg_30_0.operateCount != arg_30_1:
			arg_30_0.operateCount = arg_30_1

			arg_30_0.UpdateComposeCount()

		local var_30_2 = arg_30_0.itemVO.count - arg_30_0.operateCount * var_30_1

		arg_30_0.updateItemCount(var_30_2)
	elif arg_30_0.operateMode == var_0_3.RESOLVE:
		arg_30_1 = math.clamp(arg_30_1, 0, arg_30_0.operateMax)

		if arg_30_0.operateCount != arg_30_1:
			arg_30_0.operateCount = arg_30_1

			arg_30_0.UpdateResolvePanel()
			arg_30_0.updateItemCount(arg_30_0.itemVO.count - arg_30_0.operateCount)

def var_0_0.UpdateComposeCount(arg_31_0):
	local var_31_0 = arg_31_0.operateCount

	setText(arg_31_0.operateValue, var_31_0)

	local var_31_1 = {}

	table.insert(var_31_1, {
		type = DROP_TYPE_ITEM,
		id = arg_31_0.itemVO.getConfig("target_id"),
		count = var_31_0
	})
	UIItemList.StaticAlign(arg_31_0.operateBonusList, arg_31_0.operateBonusTpl, #var_31_1, function(arg_32_0, arg_32_1, arg_32_2)
		arg_32_1 = arg_32_1 + 1

		if arg_32_0 == UIItemList.EventUpdate:
			local var_32_0 = var_31_1[arg_32_1]

			updateDrop(arg_32_2.Find("IconTpl"), var_32_0)
			onButton(arg_31_0, arg_32_2.Find("IconTpl"), function()
				arg_31_0.emit(var_0_0.ON_DROP, var_32_0), SFX_PANEL))

	for iter_31_0, iter_31_1 in pairs(arg_31_0.operateBtns):
		setActive(iter_31_1, iter_31_0 == "Confirm" or iter_31_0 == "Cancel")

	setText(arg_31_0.operateCountdesc, i18n("compose_amount_prefix"))
	setActive(arg_31_0.keepFateTog, False)

def var_0_0.UpdateResolvePanel(arg_34_0):
	local var_34_0 = arg_34_0.operateCount

	setText(arg_34_0.operateValue, var_34_0)

	local var_34_1 = arg_34_0.itemVO.getConfig("price")
	local var_34_2 = {}

	table.insert(var_34_2, {
		type = DROP_TYPE_RESOURCE,
		id = var_34_1[1],
		count = var_34_1[2] * var_34_0
	})
	UIItemList.StaticAlign(arg_34_0.operateBonusList, arg_34_0.operateBonusTpl, #var_34_2, function(arg_35_0, arg_35_1, arg_35_2)
		arg_35_1 = arg_35_1 + 1

		if arg_35_0 == UIItemList.EventUpdate:
			local var_35_0 = var_34_2[arg_35_1]

			updateDrop(arg_35_2.Find("IconTpl"), var_35_0)
			onButton(arg_34_0, arg_35_2.Find("IconTpl"), function()
				arg_34_0.emit(var_0_0.ON_DROP, var_35_0), SFX_PANEL))

	for iter_34_0, iter_34_1 in pairs(arg_34_0.operateBtns):
		setActive(iter_34_1, iter_34_0 == "Resolve" or iter_34_0 == "Cancel")

	setText(arg_34_0.operateCountdesc, i18n("resolve_amount_prefix"))

	if arg_34_0.itemVO.getConfig("type") == Item.TEC_SPEEDUP_TYPE:
		setActive(arg_34_0.keepFateTog, False)
	else
		setActive(arg_34_0.keepFateTog, True)

	setButtonEnabled(arg_34_0.operateBtns.Resolve, var_34_0 > 0)

def var_0_0.UpdateBlueprintResolveNum(arg_37_0):
	local var_37_0 = arg_37_0.itemVO.count

	if arg_37_0.itemVO.getConfig("type") == Item.BLUEPRINT_TYPE:
		local var_37_1 = getProxy(TechnologyProxy)
		local var_37_2 = var_37_1.GetBlueprint4Item(arg_37_0.itemVO.id)
		local var_37_3 = var_37_1.getBluePrintById(var_37_2)

		if arg_37_0.keepFateState:
			var_37_0 = arg_37_0.itemVO.count - var_37_3.getFateMaxLeftOver()
			var_37_0 = var_37_0 < 0 and 0 or var_37_0

	arg_37_0.operateMax = var_37_0

def var_0_0.UpdateSpeedUpResolveNum(arg_38_0):
	local var_38_0 = arg_38_0.itemVO.count

	if arg_38_0.itemVO.getConfig("type") == Item.TEC_SPEEDUP_TYPE:
		arg_38_0.operateMax = var_38_0

def var_0_0.willExit(arg_39_0):
	if arg_39_0.leftEventTrigger:
		ClearEventTrigger(arg_39_0.leftEventTrigger)

	if arg_39_0.rightEventTrigger:
		ClearEventTrigger(arg_39_0.rightEventTrigger)

	pg.UIMgr.GetInstance().UnblurPanel(arg_39_0._tf)

def var_0_0.PlayOpenBox(arg_40_0, arg_40_1, arg_40_2):
	if not arg_40_1 or arg_40_1 == "":
		arg_40_2()

		return

	local var_40_0 = {}
	local var_40_1 = arg_40_0.findTF(arg_40_1 .. "(Clone)")

	if var_40_1:
		arg_40_0[arg_40_1] = go(var_40_1)

	if not arg_40_0[arg_40_1]:
		table.insert(var_40_0, function(arg_41_0)
			PoolMgr.GetInstance().GetPrefab("ui/" .. string.lower(arg_40_1), "", True, function(arg_42_0)
				arg_42_0.SetActive(True)

				arg_40_0[arg_40_1] = arg_42_0

				arg_41_0()))

	seriesAsync(var_40_0, function()
		if arg_40_0.playing or not arg_40_0[arg_40_1]:
			return

		arg_40_0.playing = True

		arg_40_0[arg_40_1].SetActive(True)
		SetActive(arg_40_0.window, False)

		local var_43_0 = tf(arg_40_0[arg_40_1])

		var_43_0.SetParent(arg_40_0._tf, False)
		var_43_0.SetAsLastSibling()

		local var_43_1 = var_43_0.GetComponent("DftAniEvent")

		var_43_1.SetTriggerEvent(function(arg_44_0)
			arg_40_2())
		var_43_1.SetEndEvent(function(arg_45_0)
			if arg_40_0[arg_40_1]:
				SetActive(arg_40_0[arg_40_1], False)

				arg_40_0.playing = False

			arg_40_0.closeView())
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_EQUIPMENT_OPEN))

return var_0_0
