local var_0_0 = class("AwardInfoLayer", import("..base.BaseUI"))

var_0_0.TITLE = {
	COMMANDER = "commander",
	RYZA = "ryza",
	ITEM = "item",
	SHIP = "ship",
	REVERT = "revert",
	ESCORT = "escort"
}

local var_0_1 = 0.15
local var_0_2 = 340
local var_0_3 = 564

def var_0_0.getUIName(arg_1_0):
	return "AwardInfoUI"

def var_0_0.init(arg_2_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf, False, {
		weight = LayerWeightConst.THIRD_LAYER
	})

	arg_2_0.awards = _.select(arg_2_0.contextData.items or {}, function(arg_3_0)
		return arg_3_0.type != DROP_TYPE_ICON_FRAME and arg_3_0.type != DROP_TYPE_CHAT_FRAME)
	arg_2_0._itemsWindow = arg_2_0._tf.Find("items")
	arg_2_0.spriteMask = arg_2_0._itemsWindow.Find("SpriteMask")
	arg_2_0.title = arg_2_0.contextData.title or var_0_0.TITLE.ITEM

	for iter_2_0, iter_2_1 in pairs(var_0_0.TITLE):
		setActive(arg_2_0._itemsWindow.Find("titles/title_" .. iter_2_1), arg_2_0.title == iter_2_1)

	if arg_2_0.title == var_0_0.TITLE.COMMANDER:
		eachChild(arg_2_0._itemsWindow.Find("titles/title_commander"), function(arg_4_0)
			setActive(arg_4_0, arg_4_0.name == arg_2_0.contextData.titleExtra))

	local var_2_0 = {
		items_scroll = arg_2_0._itemsWindow.Find("items_scroll/content"),
		ships = arg_2_0._itemsWindow.Find("ships")
	}

	if arg_2_0.title == var_0_0.TITLE.SHIP:
		arg_2_0.container = var_2_0.ships
	else
		arg_2_0.container = var_2_0.items_scroll

		scrollTo(arg_2_0.container, None, 1)

		arg_2_0.windowLayout = arg_2_0._itemsWindow.Find("items_scroll").GetComponent(typeof(LayoutElement))

	GetOrAddComponent(arg_2_0.container, "CanvasGroup").alpha = 1

	for iter_2_2, iter_2_3 in pairs(var_2_0):
		setActive(arg_2_0._itemsWindow.Find(iter_2_2), arg_2_0.container == iter_2_3)

	setLocalScale(arg_2_0._itemsWindow, Vector3(0.5, 0.5, 0.5))

	arg_2_0.itemTpl = arg_2_0._itemsWindow.Find("item_tpl")
	arg_2_0.shipTpl = arg_2_0._itemsWindow.Find("ship_tpl")
	arg_2_0.extraBouns = arg_2_0._itemsWindow.Find("titles/extra_bouns")

	setActive(arg_2_0.extraBouns, arg_2_0.contextData.extraBonus)

	arg_2_0.continueBtn = arg_2_0.findTF("items/close")

	local var_2_1 = arg_2_0._tf.Find("decorations")

	if arg_2_0.title == var_0_0.TITLE.SHIP:
		setLocalScale(var_2_1, Vector3.New(1.25, 1.25, 1))
	else
		setLocalScale(var_2_1, Vector3.one)

	arg_2_0.blinks = {}
	arg_2_0.tweenItems = {}
	arg_2_0.shipCardTpl = arg_2_0._tf.GetComponent("ItemList").prefabItem[0]

	arg_2_0._tf.SetAsLastSibling()

	arg_2_0.metaRepeatAwardTF = arg_2_0.findTF("MetaShipRepeatAward")

def var_0_0.doAnim(arg_5_0, arg_5_1):
	LeanTween.scale(rtf(arg_5_0._itemsWindow), Vector3(1, 1, 1), 0.15).setEase(LeanTweenType.linear).setOnComplete(System.Action(function()
		if arg_5_0.exited:
			return

		arg_5_1()))

def var_0_0.playAnim(arg_7_0, arg_7_1):
	local var_7_0 = {}

	for iter_7_0 = 1, #arg_7_0.awards:
		table.insert(var_7_0, function(arg_8_0)
			setActive(arg_7_0.container.GetChild(iter_7_0 - 1), True)

			if arg_7_0.windowLayout:
				if iter_7_0 > 5 and arg_7_0.windowLayout.preferredHeight != var_0_3:
					arg_7_0.windowLayout.preferredHeight = var_0_3

					arg_7_0.updateSpriteMaskScale()

				if iter_7_0 % 5 == 1:
					scrollTo(arg_7_0.container, None, 0)

			arg_7_0.tweeningId = LeanTween.delayedCall(var_0_1, System.Action(arg_8_0)).uniqueId)

	seriesAsync(var_7_0, function()
		arg_7_0.tweeningId = None

		if arg_7_1:
			arg_7_1())

def var_0_0.didEnter(arg_10_0):
	setActive(arg_10_0.spriteMask, True)
	onButton(arg_10_0, arg_10_0._tf, function()
		local function var_11_0()
			if arg_10_0.tweeningId:
				LeanTween.cancel(arg_10_0.tweeningId)

				arg_10_0.tweeningId = None

			arg_10_0.emit(var_0_0.ON_CLOSE)

		arg_10_0.checkPaintingRes(var_11_0), SFX_CANCEL, {
		noShip = not arg_10_0.hasShip
	})
	onButton(arg_10_0, arg_10_0.continueBtn, function()
		triggerButton(arg_10_0._tf))
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_UI_GETITEM)

	local var_10_0 = {}

	table.insert(var_10_0, function(arg_14_0)
		arg_10_0.doAnim(arg_14_0))
	arg_10_0.displayAwards()

	if arg_10_0.contextData.animation:
		eachChild(arg_10_0.container, function(arg_15_0)
			setActive(arg_15_0, False))

		GetOrAddComponent(arg_10_0.container, "CanvasGroup").alpha = 0

		table.insert(var_10_0, function(arg_16_0)
			GetOrAddComponent(arg_10_0.container, "CanvasGroup").alpha = 1

			arg_10_0.playAnim(arg_16_0))

	if arg_10_0.windowLayout:
		arg_10_0.windowLayout.preferredHeight = not arg_10_0.contextData.animation and #arg_10_0.awards > 5 and var_0_3 or var_0_2

		arg_10_0.updateSpriteMaskScale()

	seriesAsync(var_10_0, function()
		if arg_10_0.exited:
			return

		if arg_10_0.contextData.closeOnCompleted:
			triggerButton(arg_10_0._tf)

		if arg_10_0.enterCallback:
			arg_10_0.enterCallback()

			arg_10_0.enterCallback = None)

def var_0_0.onUIAnimEnd(arg_18_0, arg_18_1):
	arg_18_0.enterCallback = arg_18_1

def var_0_0.onBackPressed(arg_19_0):
	if LeanTween.isTweening(go(arg_19_0._itemsWindow)):
		return

	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_19_0._tf)

local function var_0_4(arg_20_0, arg_20_1)
	local var_20_0 = pg.ship_data_statistics[arg_20_1.id]
	local var_20_1 = Ship.New({
		configId = arg_20_1.id
	})

	var_20_1.virgin = arg_20_1.virgin

	setScrollText(findTF(arg_20_0, "content/info/name_mask/name"), var_20_1.GetColorName())
	flushShipCard(arg_20_0, var_20_1)

	local var_20_2 = findTF(arg_20_0, "content/front/new")

	setActive(var_20_2, arg_20_1.virgin)

def var_0_0.displayAwards(arg_21_0):
	assert(#arg_21_0.awards != 0, "items数量不能为0")
	removeAllChildren(arg_21_0.container)

	for iter_21_0 = 1, #arg_21_0.awards:
		if arg_21_0.title != var_0_0.TITLE.SHIP:
			cloneTplTo(arg_21_0.itemTpl, arg_21_0.container)
		else
			local var_21_0 = cloneTplTo(arg_21_0.shipTpl, arg_21_0.container)

			cloneTplTo(arg_21_0.shipCardTpl, var_21_0, "ship_tpl")

	if arg_21_0.title != var_0_0.TITLE.SHIP:
		for iter_21_1 = 1, #arg_21_0.awards:
			local var_21_1 = arg_21_0.container.GetChild(iter_21_1 - 1).Find("bg")
			local var_21_2 = arg_21_0.awards[iter_21_1]

			if var_21_2.type == DROP_TYPE_SHIP:
				arg_21_0.hasShip = True

			updateDrop(var_21_1, var_21_2, {
				fromAwardLayer = True
			})
			setActive(findTF(var_21_1, "icon_bg/bonus"), var_21_2.riraty)
			setActive(findTF(var_21_1, "icon_bg/bonus_catchup"), var_21_2.catchupTag)
			setActive(findTF(var_21_1, "icon_bg/bonus_event"), var_21_2.catchupActTag)

			local var_21_3 = findTF(var_21_1, "name")
			local var_21_4 = findTF(var_21_1, "name_mask")

			setActive(var_21_3, False)
			setActive(var_21_4, True)
			setScrollText(findTF(var_21_1, "name_mask/name"), var_21_2.name or getText(var_21_3))
			onButton(arg_21_0, var_21_1, function()
				if arg_21_0.tweeningId:
					return

				arg_21_0.emit(AwardInfoMediator.ON_DROP, var_21_2), SFX_PANEL)
	else
		for iter_21_2 = 1, #arg_21_0.awards:
			local var_21_5 = arg_21_0.container.GetChild(iter_21_2 - 1).Find("ship_tpl")
			local var_21_6 = arg_21_0.awards[iter_21_2]

			var_0_4(var_21_5, var_21_6)

			local var_21_7 = var_21_6.reMetaSpecialItemVO

			if var_21_7:
				local var_21_8 = cloneTplTo(arg_21_0.metaRepeatAwardTF, var_21_5)

				setLocalPosition(var_21_8, Vector3.zero)
				setLocalScale(var_21_8, Vector3.zero)

				local var_21_9 = arg_21_0.findTF("item_tpl/bg", var_21_8)

				updateDrop(var_21_9, var_21_7)
				setActive(var_21_9.Find("name"), False)
				setActive(var_21_9.Find("name_mask"), True)
				var_21_9.Find("name_mask/name").GetComponent("ScrollText").SetText(var_21_7.cfg.name)

				local function var_21_10()
					arg_21_0.managedTween(LeanTween.value, None, go(var_21_8), 0, 1, 0.3).setOnUpdate(System.Action_float(function(arg_24_0)
						setLocalScale(var_21_8, {
							x = arg_24_0,
							y = arg_24_0
						}))).setOnComplete(System.Action(function()
						setLocalScale(var_21_8, Vector3.one)))

				arg_21_0.managedTween(LeanTween.delayedCall, var_21_10, 0.3, None)

			if #arg_21_0.awards > 5:
				if iter_21_2 <= 5:
					var_21_5.anchoredPosition = Vector2.New(-50, 0)
				else
					var_21_5.anchoredPosition = Vector2.New(50, 0)

def var_0_0.ShowOrHideSpriteMask(arg_26_0, arg_26_1):
	if isActive(arg_26_0.spriteMask) == arg_26_1:
		return

	setActive(arg_26_0.spriteMask, arg_26_1)

def var_0_0.willExit(arg_27_0):
	setActive(arg_27_0.spriteMask, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_27_0._tf)

	if arg_27_0.title != var_0_0.TITLE.SHIP:
		for iter_27_0 = 0, arg_27_0.container.childCount - 1:
			clearDrop(arg_27_0.container.GetChild(iter_27_0).Find("bg"))

	if arg_27_0.blinks and #arg_27_0.blinks > 0:
		for iter_27_1, iter_27_2 in pairs(arg_27_0.blinks):
			if not IsNil(iter_27_2):
				Destroy(iter_27_2)

	if arg_27_0.contextData.removeFunc:
		arg_27_0.contextData.removeFunc()

		arg_27_0.contextData.removeFunc = None

def var_0_0.updateSpriteMaskScale(arg_28_0):
	onNextTick(function()
		if arg_28_0.exited:
			return

		setLocalScale(arg_28_0.spriteMask, Vector3(arg_28_0.spriteMask.rect.width / WHITE_DOT_SIZE * PIXEL_PER_UNIT, arg_28_0.spriteMask.rect.height / WHITE_DOT_SIZE * PIXEL_PER_UNIT, 1)))

def var_0_0.checkPaintingRes(arg_30_0, arg_30_1):
	local var_30_0 = PaintingGroupConst.GetPaintingNameListForAwardList(arg_30_0.awards)
	local var_30_1 = {
		isShowBox = False,
		paintingNameList = var_30_0,
		finishFunc = arg_30_1
	}

	PaintingGroupConst.PaintingDownload(var_30_1)

return var_0_0
