local var_0_0 = class("CastStoryPlayer", import(".StoryPlayer"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.tpls = {
		arg_1_0._tf.Find("resource/text_tpl"),
		arg_1_0._tf.Find("resource/image_tpl"),
		arg_1_0._tf.Find("resource/list_tpl"),
		arg_1_0._tf.Find("resource/cast_tpl")
	}
	arg_1_0.layoutContainer = arg_1_0.castPanel.Find("Image")

def var_0_0.OnReset(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	setActive(arg_2_0.castPanel, True)
	setAnchoredPosition(arg_2_0.layoutContainer, {
		x = 0,
		y = 0
	})
	arg_2_3()

def var_0_0.OnEnter(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	seriesAsync({
		function(arg_4_0)
			arg_3_0.SetLayout(arg_3_1, arg_4_0),
		function(arg_5_0)
			onNextTick(arg_5_0),
		function(arg_6_0)
			arg_3_0.StartAnimation(arg_3_1, arg_6_0)
	}, arg_3_3)

def var_0_0.SetLayout(arg_7_0, arg_7_1, arg_7_2):
	removeAllChildren(arg_7_0.layoutContainer)

	local var_7_0 = arg_7_1.GetSpacing()

	arg_7_0.layoutContainer.GetComponent(typeof(VerticalLayoutGroup)).spacing = var_7_0

	local var_7_1 = arg_7_1.GetLayout()

	for iter_7_0, iter_7_1 in pairs(var_7_1):
		local var_7_2 = arg_7_0.tpls[iter_7_1.type]
		local var_7_3 = cloneTplTo(var_7_2, arg_7_0.layoutContainer)
		local var_7_4 = "InitLayoutForType" .. iter_7_1.type

		assert(arg_7_0[var_7_4], "need function >>>" .. var_7_4)
		arg_7_0[var_7_4](arg_7_0, var_7_3, iter_7_1)

	arg_7_2()

def var_0_0.InitLayoutForType1(arg_8_0, arg_8_1, arg_8_2):
	setText(arg_8_1, arg_8_2.text)

def var_0_0.InitLayoutForType2(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = LoadSprite("bg/" .. arg_9_2.path)
	local var_9_1 = arg_9_1.Find("image").GetComponent(typeof(Image))
	local var_9_2 = arg_9_1.GetComponent(typeof(LayoutElement))

	var_9_1.sprite = var_9_0

	if arg_9_2.size == Vector2.zero:
		var_9_1.SetNativeSize()

		var_9_2.preferredHeight = var_9_1.gameObject.transform.sizeDelta.y
	else
		var_9_1.gameObject.transform.sizeDelta = arg_9_2.size
		var_9_2.preferredHeight = arg_9_2.size.y

def var_0_0.InitLayoutForType3(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = arg_10_2.names
	local var_10_1 = arg_10_2.column
	local var_10_2 = arg_10_1.GetComponent(typeof(GridLayoutGroup))

	var_10_2.constraintCount = var_10_1

	local var_10_3 = var_10_2.spacing.x
	local var_10_4 = 1920 / var_10_1 - var_10_3 * (var_10_1 - 1)

	var_10_2.cellSize = Vector2(var_10_4, 30)

	local var_10_5 = var_10_1 % 2 != 0
	local var_10_6 = UIItemList.New(arg_10_1, arg_10_1.Find("1"))

	var_10_6.make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate:
			local var_11_0 = arg_11_2.GetComponent(typeof(Text))
			local var_11_1 = COLOR_WHITE

			if var_10_5:
				var_11_0.alignment = TextAnchor.MiddleCenter
			else
				local var_11_2 = arg_11_1 % 2 == 0

				var_11_0.alignment = var_11_2 and TextAnchor.MiddleRight or TextAnchor.MiddleLeft

				if var_11_2:
					var_11_1 = arg_10_2.evenColumnColor

			var_11_0.text = setColorStr(var_10_0[arg_11_1 + 1], var_11_1))
	var_10_6.align(#var_10_0)

def var_0_0.InitLayoutForType4(arg_12_0, arg_12_1, arg_12_2):
	return

def var_0_0.StartAnimation(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = arg_13_1.GetPlayTime()

	arg_13_0.PlayAnimation(var_13_0, arg_13_2)
	onButton(arg_13_0, arg_13_0._tf, function()
		removeOnButton(arg_13_0._tf)
		arg_13_0.SpeedUp(var_13_0, arg_13_2), SFX_PANEL)

def var_0_0.PlayAnimation(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = arg_15_0.castPanel.rect.height + arg_15_0.layoutContainer.sizeDelta.y
	local var_15_1 = getAnchoredPosition(arg_15_0.layoutContainer).y

	arg_15_0.TweenValue(arg_15_0.layoutContainer, var_15_1, var_15_0, arg_15_1, 0, function(arg_16_0)
		setAnchoredPosition(arg_15_0.layoutContainer, {
			y = arg_16_0
		}), function()
		removeOnButton(arg_15_0._tf)
		arg_15_2())

def var_0_0.SpeedUp(arg_18_0, arg_18_1, arg_18_2):
	arg_18_0.CancelTween(arg_18_0.layoutContainer)
	arg_18_0.PlayAnimation(arg_18_1 * 0.2, arg_18_2)

def var_0_0.RegisetEvent(arg_19_0, arg_19_1):
	var_0_0.super.RegisetEvent(arg_19_0, arg_19_1)
	triggerButton(arg_19_0._go)

return var_0_0
