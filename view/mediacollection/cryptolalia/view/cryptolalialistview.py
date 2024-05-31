local var_0_0 = class("CryptolaliaListView", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CryptolaliaListui"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.cards = {}
	arg_2_0.scrollrect = arg_2_0.findTF("frame/view").GetComponent("LScrollRect")

	function arg_2_0.scrollrect.onInitItem(arg_3_0)
		arg_2_0.OnInitItem(arg_3_0)

	function arg_2_0.scrollrect.onUpdateItem(arg_4_0, arg_4_1)
		arg_2_0.onUpdateItem(arg_4_0, arg_4_1)

	arg_2_0.frameTr = arg_2_0.findTF("frame")
	arg_2_0.subTitleTxt = arg_2_0.findTF("frame/subtitle").GetComponent(typeof(Text))

	setText(arg_2_0.findTF("frame/title"), i18n("cryptolalia_list_title"))

def var_0_0.OnInit(arg_5_0):
	return

def var_0_0.OnInitItem(arg_6_0, arg_6_1):
	local function var_6_0()
		if not arg_6_0.cryptolaliaId:
			return

		for iter_7_0, iter_7_1 in pairs(arg_6_0.cards):
			if iter_7_1.cryptolalia.id == arg_6_0.cryptolaliaId:
				iter_7_1.Update(iter_7_1.cryptolalia, arg_6_0.langType, False)

	local var_6_1 = CryptolaliaCard.New(arg_6_1)

	onButton(arg_6_0, var_6_1._go, function()
		if arg_6_0.CanSwitch():
			var_6_0()

			arg_6_0.cryptolaliaId = var_6_1.cryptolalia.id

			var_6_1.Update(var_6_1.cryptolalia, arg_6_0.langType, True)
			arg_6_0.SelectCard(arg_6_0.cryptolaliaId), SFX_PANEL)

	arg_6_0.cards[arg_6_1] = var_6_1

def var_0_0.CanSwitch(arg_9_0):
	return not arg_9_0.scrollRect.inAnimation

def var_0_0.onUpdateItem(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = arg_10_0.cards[arg_10_2]

	if not var_10_0:
		arg_10_0.OnInitItem(arg_10_2)

		var_10_0 = arg_10_0.cards[arg_10_2]

	local var_10_1 = arg_10_0.displays[arg_10_1 + 1]
	local var_10_2 = var_10_1.id == arg_10_0.cryptolaliaId

	var_10_0.Update(var_10_1, arg_10_0.langType, var_10_2)

def var_0_0.Show(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4):
	arg_11_0.scrollRect = arg_11_4

	var_0_0.super.Show(arg_11_0)
	seriesAsync({
		function(arg_12_0)
			arg_11_0.EnterAnimation(arg_12_0),
		function(arg_13_0)
			arg_11_0.InitList(arg_11_1, arg_11_2, arg_11_3)
			arg_11_0.RegisterEvent()
			arg_13_0()
	})

def var_0_0.EnterAnimation(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_0.frameTr.sizeDelta.x

	LeanTween.value(arg_14_0._tf.gameObject, var_14_0, 0, 0.3).setOnUpdate(System.Action_float(function(arg_15_0)
		arg_14_0._tf.localPosition = Vector3(arg_15_0, arg_14_0._tf.localPosition.y, 0))).setFrom(var_14_0).setEase(LeanTweenType.easeInOutSine).setOnComplete(System.Action(arg_14_1))

def var_0_0.InitList(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	arg_16_0.cryptolaliaId = arg_16_3
	arg_16_0.langType = arg_16_2
	arg_16_0.displays = arg_16_1

	arg_16_0.scrollrect.SetTotalCount(#arg_16_0.displays)

	arg_16_0.subTitleTxt.text = i18n("cryptolalia_list_subtitle", #arg_16_0.displays)

def var_0_0.RegisterEvent(arg_17_0):
	onButton(arg_17_0, arg_17_0._tf, function()
		arg_17_0.Hide(), SFX_PANEL)

def var_0_0.Hide(arg_19_0):
	var_0_0.super.Hide(arg_19_0)
	removeOnButton(arg_19_0._tf)

	if LeanTween.isTweening(arg_19_0._tf.gameObject):
		LeanTween.cancel(arg_19_0._tf.gameObject)

def var_0_0.SelectCard(arg_20_0, arg_20_1):
	arg_20_0.emit(CryptolaliaScene.ON_SELECT, arg_20_1)

def var_0_0.OnDestroy(arg_21_0):
	for iter_21_0, iter_21_1 in pairs(arg_21_0.cards):
		iter_21_1.Dispose()

	arg_21_0.cards = {}

	ClearLScrollrect(arg_21_0.scrollrect)

return var_0_0
