local var_0_0 = class("BackYardDecorationPutlistPage", import(".BackYardDecorationBasePage"))

var_0_0.SELECTED_FURNITRUE = "BackYardDecorationPutlistPage.SELECTED_FURNITRUE"

def var_0_0.getUIName(arg_1_0):
	return "BackYardPutListPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.bind(BackYardDecrationLayer.INNER_SELECTED_FURNITRUE, function(arg_3_0, arg_3_1)
		arg_2_0.Selected(arg_3_1))

	arg_2_0._bg = arg_2_0.findTF("frame")
	arg_2_0.scrollRect = arg_2_0.findTF("frame/frame/scrollrect").GetComponent("LScrollRect")
	arg_2_0.scrollRectTF = arg_2_0.findTF("frame/frame/scrollrect")
	arg_2_0.emptyTF = arg_2_0.findTF("frame/frame/empty")
	arg_2_0.arr = arg_2_0.findTF("frame/frame/arr")

	setText(arg_2_0.findTF("frame/title/Text"), i18n("courtyard_label_putlist_title"))

def var_0_0.OnInit(arg_4_0):
	var_0_0.super.OnInit(arg_4_0)
	onButton(arg_4_0, arg_4_0._tf, function()
		arg_4_0.Hide(), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.arr, function()
		arg_4_0.Hide(), SFX_PANEL)

	local function var_4_0()
		if arg_4_0.timer:
			arg_4_0.timer.Stop()

			arg_4_0.timer = None

	local function var_4_1(arg_8_0)
		arg_4_0.timer = Timer.New(arg_8_0, 0.8, 1)

		arg_4_0.timer.Start()

	local function var_4_2(arg_9_0)
		local var_9_0 = var_0_0.change2ScrPos(arg_4_0.scrollRectTF.Find("content"), arg_9_0.position)
		local var_9_1

		for iter_9_0, iter_9_1 in pairs(arg_4_0.cards):
			local var_9_2 = iter_9_1._tf
			local var_9_3 = var_9_2.localPosition.x
			local var_9_4 = var_9_2.localPosition.y
			local var_9_5 = Vector2(var_9_3 + var_9_2.rect.width / 2, var_9_4 + var_9_2.rect.height / 2)
			local var_9_6 = Vector2(var_9_3 + var_9_2.rect.width / 2, var_9_4 - var_9_2.rect.height / 2)
			local var_9_7 = Vector2(var_9_3 - var_9_2.rect.width / 2, var_9_4 - var_9_2.rect.height / 2)

			if var_9_0.x > var_9_7.x and var_9_0.x < var_9_6.x and var_9_0.y > var_9_6.y and var_9_0.y < var_9_5.y:
				var_9_1 = iter_9_1

				break

		return var_9_1

	local var_4_3 = GetOrAddComponent(arg_4_0.scrollRectTF, typeof(EventTriggerListener))

	var_4_3.AddPointDownFunc(function(arg_10_0, arg_10_1)
		local var_10_0 = var_4_2(arg_10_1)

		arg_4_0.downPosition = arg_10_1.position

		if var_10_0:
			var_4_0()
			var_4_1(function()
				arg_4_0.lock = True

				local var_11_0 = var_10_0._tf.position

				arg_4_0.contextData.furnitureDescMsgBox.ExecuteAction("SetUp", var_10_0.furniture, var_11_0, True)))
	var_4_3.AddPointUpFunc(function(arg_12_0, arg_12_1)
		var_4_0()

		if arg_4_0.lock:
			arg_4_0.contextData.furnitureDescMsgBox.ExecuteAction("Hide")
			onNextTick(function()
				arg_4_0.lock = False)
		else
			local var_12_0 = arg_12_1.position

			if Vector2.Distance(var_12_0, arg_4_0.downPosition) > 1:
				return

			local var_12_1 = var_4_2(arg_12_1)

			if var_12_1:
				arg_4_0.emit(BackYardDecorationMediator.ON_SELECTED_FURNITRUE, var_12_1.furniture.id)
				var_12_1.MarkOrUnMark(arg_4_0.card.furniture.id)

				arg_4_0.selectedId = arg_4_0.card.furniture.id

				arg_4_0.emit(var_0_0.SELECTED_FURNITRUE))

def var_0_0.ClearMark(arg_14_0):
	arg_14_0.selectedId = None

	for iter_14_0, iter_14_1 in pairs(arg_14_0.cards):
		iter_14_1.MarkOrUnMark(arg_14_0.selectedId)

def var_0_0.Selected(arg_15_0, arg_15_1):
	arg_15_0.ClearMark()

	for iter_15_0, iter_15_1 in pairs(arg_15_0.cards):
		if iter_15_1.furniture and iter_15_1.furniture.id == arg_15_1:
			iter_15_1.MarkOrUnMark(arg_15_1)

			break

	arg_15_0.selectedId = arg_15_1

def var_0_0.change2ScrPos(arg_16_0, arg_16_1):
	local var_16_0 = GameObject.Find("UICamera").GetComponent("Camera")
	local var_16_1 = arg_16_0.GetComponent("RectTransform")

	return (LuaHelper.ScreenToLocal(var_16_1, arg_16_1, var_16_0))

def var_0_0.OnInitItem(arg_17_0, arg_17_1):
	local var_17_0 = BackYardDecorationPutCard.New(arg_17_1)

	arg_17_0.cards[arg_17_1] = var_17_0

def var_0_0.OnUpdateItem(arg_18_0, arg_18_1, arg_18_2):
	local var_18_0 = arg_18_0.cards[arg_18_2]

	if not var_18_0:
		arg_18_0.OnInitItem(arg_18_2)

		var_18_0 = arg_18_0.cards[arg_18_2]

	local var_18_1 = arg_18_0.displays[arg_18_1 + 1]

	var_18_0.Update(var_18_1, arg_18_0.selectedId)

def var_0_0.OnDisplayList(arg_19_0):
	arg_19_0.displays = {}

	local var_19_0 = getProxy(DormProxy).floor
	local var_19_1 = arg_19_0.dorm.GetTheme(var_19_0)
	local var_19_2 = {}

	if var_19_1:
		var_19_2 = var_19_1.GetAllFurniture()

	for iter_19_0, iter_19_1 in pairs(var_19_2):
		table.insert(arg_19_0.displays, Furniture.New({
			count = 1,
			id = iter_19_1.configId
		}))

	table.sort(arg_19_0.displays, function(arg_20_0, arg_20_1)
		return arg_20_0.getConfig("type") < arg_20_1.getConfig("type"))
	setActive(arg_19_0.emptyTF, #arg_19_0.displays == 0)
	arg_19_0.scrollRect.SetTotalCount(#arg_19_0.displays)

def var_0_0.Show(arg_21_0):
	var_0_0.super.Show(arg_21_0)

	local var_21_0 = arg_21_0._bg.anchoredPosition.x

	LeanTween.value(arg_21_0._bg.gameObject, var_21_0, 0, 0.4).setOnUpdate(System.Action_float(function(arg_22_0)
		setAnchoredPosition(arg_21_0._bg, {
			x = arg_22_0
		}))).setOnComplete(System.Action(function()
		if arg_21_0.OnShow:
			arg_21_0.OnShow(True)))

	if arg_21_0.OnShowImmediately:
		arg_21_0.OnShowImmediately()

def var_0_0.Hide(arg_24_0):
	local var_24_0 = -arg_24_0._bg.rect.width

	LeanTween.value(arg_24_0._bg.gameObject, 0, var_24_0, 0.4).setOnUpdate(System.Action_float(function(arg_25_0)
		setAnchoredPosition(arg_24_0._bg, {
			x = arg_25_0
		}))).setOnComplete(System.Action(function()
		var_0_0.super.Hide(arg_24_0)

		if arg_24_0.OnShow:
			arg_24_0.OnShow(False)))

	for iter_24_0, iter_24_1 in pairs(arg_24_0.cards):
		iter_24_1.Clear()

def var_0_0.OnDormUpdated(arg_27_0):
	arg_27_0.OnDisplayList()

def var_0_0.OnDestroy(arg_28_0):
	if arg_28_0.timer:
		arg_28_0.timer.Stop()

		arg_28_0.timer = None

return var_0_0
