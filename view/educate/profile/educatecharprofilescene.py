local var_0_0 = class("EducateCharProfileScene", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EducateCharProfileUI"

def var_0_0.init(arg_2_0):
	arg_2_0.backBtn = arg_2_0.findTF("adapt/top/back")
	arg_2_0.homeBtn = arg_2_0.findTF("adapt/top/home")
	arg_2_0.paintingTr = arg_2_0.findTF("main/mask/painting")
	arg_2_0.chatTf = arg_2_0.findTF("main/chat")
	arg_2_0.chatTxt = arg_2_0.chatTf.Find("Text").GetComponent(typeof(Text))
	arg_2_0.toggleUIItemList = UIItemList.New(arg_2_0.findTF("main/tag"), arg_2_0.findTF("main/tag/tpl"))
	arg_2_0.wordUIItemList = UIItemList.New(arg_2_0.findTF("main/list/content"), arg_2_0.findTF("main/list/content/tpl"))
	arg_2_0.cvLoader = EducateCharCvLoader.New()
	arg_2_0.animation = arg_2_0._tf.GetComponent(typeof(Animation))
	arg_2_0.timers = {}

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0.emit(var_0_0.ON_BACK), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.homeBtn, function()
		arg_3_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	arg_3_0.InitToggles()

def var_0_0.InitToggles(arg_6_0):
	local var_6_0 = getProxy(EducateProxy).GetEducateGroupList()

	table.sort(var_6_0, function(arg_7_0, arg_7_1)
		return arg_7_0.GetSortWeight() < arg_7_1.GetSortWeight())
	arg_6_0.toggleUIItemList.make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate:
			arg_6_0.UpdateToggle(arg_8_2, var_6_0[arg_8_1 + 1])

			if arg_8_1 == 0:
				arg_6_0.isInit = True

				triggerToggle(arg_8_2, True))
	arg_6_0.toggleUIItemList.align(#var_6_0)

	arg_6_0.isInit = False

def var_0_0.UpdateToggle(arg_9_0, arg_9_1, arg_9_2):
	setImageSprite(arg_9_1.Find("sel/Text"), GetSpriteFromAtlas("ui/EducateCharProfileUI_atlas", arg_9_2.GetSpriteName()), True)
	setImageSprite(arg_9_1.Find("Text"), GetSpriteFromAtlas("ui/EducateCharProfileUI_atlas", arg_9_2.GetSpriteName()), True)
	setActive(arg_9_1.Find("lock"), arg_9_2.IsLock())
	onToggle(arg_9_0, arg_9_1, function(arg_10_0)
		if arg_10_0:
			if not arg_9_0.isInit:
				arg_9_0.animation.Play("anim_educate_profile_change")

				arg_9_0.isInit = None

			local var_10_0 = arg_9_2.GetShowId()

			arg_9_0.ClearCurrentWord()
			arg_9_0.InitPainting(var_10_0)
			arg_9_0.InitWordList(var_10_0), SFX_PANEL)

def var_0_0.GetWordList(arg_11_0, arg_11_1):
	local var_11_0 = {}

	for iter_11_0, iter_11_1 in pairs(pg.character_voice_special.all):
		local var_11_1 = iter_11_1

		if string.find(iter_11_1, ShipWordHelper.WORD_TYPE_MAIN):
			local var_11_2 = string.gsub(iter_11_1, ShipWordHelper.WORD_TYPE_MAIN, "")

			var_11_1 = ShipWordHelper.WORD_TYPE_MAIN .. "_" .. var_11_2

		if EducateCharWordHelper.ExistWord(arg_11_1, var_11_1):
			table.insert(var_11_0, iter_11_1)

	return var_11_0

def var_0_0.InitWordList(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_0.GetWordList(arg_12_1)
	local var_12_1 = pg.secretary_special_ship[arg_12_1]

	arg_12_0.RemoveAllTimer()
	arg_12_0.wordUIItemList.make(function(arg_13_0, arg_13_1, arg_13_2)
		if arg_13_0 == UIItemList.EventUpdate:
			arg_12_0.UpdateWordCard(arg_13_2, arg_12_1, var_12_0[arg_13_1 + 1], arg_13_1))
	arg_12_0.wordUIItemList.align(#var_12_0)

def var_0_0.UpdateWordCard(arg_14_0, arg_14_1, arg_14_2, arg_14_3, arg_14_4):
	local var_14_0 = arg_14_1.Find("bg")
	local var_14_1 = pg.character_voice_special[arg_14_3]

	setText(var_14_0.Find("Text"), var_14_1.voice_name)

	local var_14_2 = -1

	onButton(arg_14_0, var_14_0, function()
		if arg_14_0.chatting:
			return

		local var_15_0, var_15_1, var_15_2, var_15_3 = EducateCharWordHelper.GetWordAndCV(arg_14_2, var_14_1.resource_key)

		seriesAsync({
			function(arg_16_0)
				arg_14_0.OnChatStart(var_14_0, var_15_2, arg_16_0),
			function(arg_17_0)
				arg_14_0.UpdateExpression(arg_14_2, var_14_1.resource_key)
				arg_14_0.PlayCV(var_15_3, var_15_0, function(arg_18_0)
					var_14_2 = arg_18_0

					arg_17_0()),
			function(arg_19_0)
				arg_14_0.StartCharAnimation(var_14_2, arg_19_0)
		}, function()
			arg_14_0.OnChatEnd()), SFX_PANEL)
	setActive(var_14_0, False)

	arg_14_0.timers[arg_14_4] = Timer.New(function()
		setActive(var_14_0, True)
		arg_14_1.GetComponent(typeof(Animation)).Play("anim_educate_profile_tpl"), math.max(1e-05, arg_14_4 * 0.066), 1)

	arg_14_0.timers[arg_14_4].Start()

def var_0_0.RemoveAllTimer(arg_22_0):
	for iter_22_0, iter_22_1 in pairs(arg_22_0.timers):
		iter_22_1.Stop()

		iter_22_1 = None

	arg_22_0.timers = {}

def var_0_0.OnChatStart(arg_23_0, arg_23_1, arg_23_2, arg_23_3):
	arg_23_0.chatting = True
	arg_23_0.chatTxt.text = arg_23_2

	triggerToggle(arg_23_1.Find("state"), True)

	arg_23_0.selectedCard = arg_23_1

	arg_23_3()

def var_0_0.UpdateExpression(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0 = EducateCharWordHelper.GetExpression(arg_24_1, arg_24_2)

	if var_24_0 and var_24_0 != "":
		ShipExpressionHelper.UpdateExpression(findTF(arg_24_0.paintingTr, "fitter").GetChild(0), arg_24_0.paintingName, var_24_0)
	else
		ShipExpressionHelper.UpdateExpression(findTF(arg_24_0.paintingTr, "fitter").GetChild(0), arg_24_0.paintingName, "")

def var_0_0.OnChatEnd(arg_25_0):
	arg_25_0.ClearCurrentWord()

def var_0_0.PlayCV(arg_26_0, arg_26_1, arg_26_2, arg_26_3):
	arg_26_0.cvLoader.Play(arg_26_1, arg_26_2, 0, arg_26_3)

def var_0_0.StartCharAnimation(arg_27_0, arg_27_1, arg_27_2):
	local var_27_0 = 0.3
	local var_27_1 = arg_27_1 > 0 and arg_27_1 or 3

	LeanTween.scale(rtf(arg_27_0.chatTf.gameObject), Vector3.New(1, 1, 1), var_27_0).setEase(LeanTweenType.easeOutBack).setOnComplete(System.Action(function()
		LeanTween.scale(rtf(arg_27_0.chatTf.gameObject), Vector3.New(0, 0, 1), var_27_0).setEase(LeanTweenType.easeInBack).setDelay(var_27_0 + var_27_1).setOnComplete(System.Action(arg_27_2))))

def var_0_0.InitPainting(arg_29_0, arg_29_1):
	arg_29_0.ReturnPainting()

	local var_29_0 = pg.secretary_special_ship[arg_29_1]

	setPaintingPrefab(arg_29_0.paintingTr, var_29_0.prefab, "tb3")

	arg_29_0.paintingName = var_29_0.prefab

def var_0_0.ReturnPainting(arg_30_0):
	if arg_30_0.paintingName:
		retPaintingPrefab(arg_30_0.paintingTr, arg_30_0.paintingName)

		arg_30_0.paintingName = None

def var_0_0.ClearCurrentWord(arg_31_0):
	arg_31_0.chatting = None

	LeanTween.cancel(arg_31_0.chatTf.gameObject)

	arg_31_0.chatTf.localScale = Vector3.zero

	arg_31_0.cvLoader.Stop()

	if not arg_31_0.selectedCard:
		return

	local var_31_0 = arg_31_0.selectedCard

	arg_31_0.selectedCard = None

	triggerToggle(var_31_0.Find("state"), False)

def var_0_0.onBackPressed(arg_32_0):
	var_0_0.super.onBackPressed(arg_32_0)

def var_0_0.willExit(arg_33_0):
	arg_33_0.ClearCurrentWord()
	arg_33_0.RemoveAllTimer()
	arg_33_0.ReturnPainting()

	if arg_33_0.cvLoader:
		arg_33_0.cvLoader.Dispose()

		arg_33_0.cvLoader = None

return var_0_0
