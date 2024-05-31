local var_0_0 = class("AsideStoryPlayer", import(".StoryPlayer"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.hrzList = UIItemList.New(arg_1_0.findTF("aside", arg_1_0.asidePanel), arg_1_0.findTF("aside/aside_txt_tpl", arg_1_0.asidePanel))
	arg_1_0.vetList = UIItemList.New(arg_1_0.findTF("aside_2", arg_1_0.asidePanel), arg_1_0.findTF("aside_2/aside_txt_tpl_2", arg_1_0.asidePanel))
	arg_1_0.leftBotomVetList = UIItemList.New(arg_1_0.findTF("aside_3", arg_1_0.asidePanel), arg_1_0.findTF("aside_3/aside_txt_tpl", arg_1_0.asidePanel))
	arg_1_0.centerWithFrameVetList = UIItemList.New(arg_1_0.findTF("aside_4", arg_1_0.asidePanel), arg_1_0.findTF("aside_4/aside_txt_tpl", arg_1_0.asidePanel))
	arg_1_0.dataTxt = arg_1_0.findTF("aside_sign_date", arg_1_0.asidePanel)

def var_0_0.OnReset(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	setActive(arg_2_0.asidePanel, True)
	setActive(arg_2_0.curtain, True)
	setActive(arg_2_0.hrzList.container, False)
	setActive(arg_2_0.vetList.container, False)
	setActive(arg_2_0.leftBotomVetList.container, False)
	setActive(arg_2_0.centerWithFrameVetList.container, False)
	setActive(arg_2_0.actorPanel, False)

	arg_2_0.curtainCg.alpha = 1

	setText(arg_2_0.dataTxt, "")
	arg_2_3()

def var_0_0.OnInit(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if arg_3_1.ShouldHideBGAlpha():
		arg_3_0.color = arg_3_0.mainImg.color
		arg_3_0.mainImg.color = Color.New(1, 1, 1, 0)

	local var_3_0 = {
		function(arg_4_0)
			if arg_3_1.GetShowMode() == AsideStep.SHOW_MODE_DEFAUT:
				arg_3_0.PlayAside(arg_3_1, arg_4_0)
			else
				arg_3_0.PlayBubbleAside(arg_3_1, arg_4_0),
		function(arg_5_0)
			arg_3_0.PlayDateSign(arg_3_1, arg_5_0)
	}

	parallelAsync(var_3_0, arg_3_3)

def var_0_0.GetAsideList(arg_6_0, arg_6_1):
	local var_6_0

	if arg_6_1 == AsideStep.ASIDE_TYPE_HRZ:
		var_6_0 = arg_6_0.hrzList
	elif arg_6_1 == AsideStep.ASIDE_TYPE_VEC:
		var_6_0 = arg_6_0.vetList
	elif arg_6_1 == AsideStep.ASIDE_TYPE_LEFTBOTTOMVEC:
		var_6_0 = arg_6_0.leftBotomVetList
	elif arg_6_1 == AsideStep.ASIDE_TYPE_CENTERWITHFRAME:
		var_6_0 = arg_6_0.centerWithFrameVetList

	return var_6_0

def var_0_0.PlayAside(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = {}
	local var_7_1 = arg_7_0.GetAsideList(arg_7_1.GetAsideType())

	arg_7_0.UpdateLayoutPaddingAndSpacing(arg_7_1, var_7_1.container)

	local var_7_2 = Mathf.Sign(var_7_1.container.localScale.x)

	setActive(var_7_1.container, True)

	local var_7_3 = arg_7_1.GetSequence()

	var_7_1.make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate:
			local var_8_0 = var_7_3[arg_8_1 + 1]
			local var_8_1 = HXSet.hxLan(var_8_0[1])
			local var_8_2 = var_8_0[2]

			setText(arg_8_2, var_8_1)

			local var_8_3 = GetOrAddComponent(arg_8_2, typeof(CanvasGroup))

			var_8_3.alpha = 0

			table.insert(var_7_0, function(arg_9_0)
				arg_7_0.TweenValueForcanvasGroup(var_8_3, 0, 1, arg_7_1.sequenceSpd or 1, var_8_2, arg_9_0))

			if var_7_2 != Mathf.Sign(arg_8_2.localScale.x):
				arg_8_2.localScale = Vector3(var_7_2 * arg_8_2.localScale.x, arg_8_2.localScale.y, 1))
	var_7_1.align(#var_7_3)
	parallelAsync(var_7_0, arg_7_2)

def var_0_0.PlayBubbleAside(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = arg_10_0.GetAsideList(arg_10_1.GetAsideType())

	arg_10_0.UpdateLayoutPaddingAndSpacing(arg_10_1, var_10_0.container)

	local var_10_1 = Mathf.Sign(var_10_0.container.localScale.x)
	local var_10_2 = arg_10_1.GetSequence()

	setActive(var_10_0.container, True)

	for iter_10_0 = var_10_0.container.childCount, 1, -1:
		local var_10_3 = var_10_0.container.GetChild(iter_10_0 - 1)

		if var_10_3 != var_10_0.item:
			Object.Destroy(var_10_3.gameObject)

	local var_10_4 = {}
	local var_10_5 = 0

	for iter_10_1 = 1, #var_10_2:
		table.insert(var_10_4, function(arg_11_0)
			local var_11_0 = cloneTplTo(var_10_0.item, var_10_0.container, iter_10_1)

			setText(var_11_0, var_10_2[iter_10_1][1])

			local var_11_1 = GetOrAddComponent(var_11_0, typeof(Typewriter))

			function var_11_1.endFunc()
				arg_11_0()

			var_11_1.setSpeed(arg_10_1.GetTypewriterSpeed())
			var_11_1.Play())

	seriesAsync(var_10_4, arg_10_2)

def var_0_0.UpdateLayoutPaddingAndSpacing(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = arg_13_1.ShouldUpdateSpacing()
	local var_13_1 = arg_13_1.ShouldUpdatePadding()

	if var_13_0 or var_13_1:
		local var_13_2 = arg_13_2.GetComponent(typeof(UnityEngine.UI.HorizontalOrVerticalLayoutGroup))

		if var_13_0:
			var_13_2.spacing, arg_13_0.spacing = arg_13_1.GetSpacing(), var_13_2.spacing

		if var_13_1:
			local var_13_3, var_13_4, var_13_5, var_13_6 = arg_13_1.GetPadding()
			local var_13_7 = UnityEngine.RectOffset.New()

			var_13_7.bottom = var_13_4
			var_13_7.left = var_13_5
			var_13_7.right = var_13_6
			var_13_7.top = var_13_3
			arg_13_0.padding = var_13_2.padding
			var_13_2.padding = var_13_7

def var_0_0.PlayDateSign(arg_14_0, arg_14_1, arg_14_2):
	local var_14_0 = arg_14_1.GetDateSign()

	if not var_14_0:
		arg_14_2()

		return

	local var_14_1 = HXSet.hxLan(var_14_0[1])
	local var_14_2 = var_14_0[2]
	local var_14_3 = var_14_0[3] or {}

	setText(arg_14_0.dataTxt, var_14_1)

	local var_14_4 = GetOrAddComponent(arg_14_0.dataTxt, typeof(CanvasGroup))

	var_14_4.alpha = 0

	arg_14_0.TweenValueForcanvasGroup(var_14_4, 1, 0, arg_14_1.sequenceSpd or 1, var_14_2, arg_14_2)
	setAnchoredPosition(arg_14_0.dataTxt, Vector3(var_14_3[1], var_14_3[2], 0))

def var_0_0.OnWillClear(arg_15_0, arg_15_1, arg_15_2, arg_15_3):
	if arg_15_0.color:
		arg_15_0.mainImg.color = arg_15_0.color

	arg_15_0.color = None

	if arg_15_0.padding or arg_15_0.spacing:
		local var_15_0 = arg_15_0.GetAsideList(arg_15_1.GetAsideType())

		arg_15_0.ResetPaddingAndSpacing(var_15_0.container, arg_15_0.padding, arg_15_0.spacing)

	arg_15_0.padding = None
	arg_15_0.spacing = None

def var_0_0.ResetPaddingAndSpacing(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	local var_16_0 = arg_16_1.GetComponent(typeof(UnityEngine.UI.HorizontalOrVerticalLayoutGroup))

	if arg_16_2:
		var_16_0.padding = arg_16_2

	if arg_16_3:
		var_16_0.spacing = arg_16_3

def var_0_0.OnEnd(arg_17_0):
	return

return var_0_0
