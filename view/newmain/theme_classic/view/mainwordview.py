local var_0_0 = class("MainWordView", import("...base.MainBaseView"))

var_0_0.START_ANIMATION = "MainWordView.ON_ANIMATION"
var_0_0.STOP_ANIMATION = "MainWordView.STOP_ANIMATION"
var_0_0.SET_CONTENT = "MainWordView.SET_CONTENT"

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.chatTf = arg_1_1
	arg_1_0.chatPos = arg_1_0.chatTf.anchoredPosition
	arg_1_0.chatTxt = arg_1_0.chatTf.Find("Text").GetComponent(typeof(Text))
	arg_1_0.chatTextBg = arg_1_0.chatTf.Find("chatbgtop")
	arg_1_0.initChatBgH = arg_1_0.chatTextBg.sizeDelta.y
	arg_1_0.stopChatFlag = False

	arg_1_0.Register()

def var_0_0.Register(arg_2_0):
	arg_2_0.bind(var_0_0.START_ANIMATION, function(arg_3_0, arg_3_1, arg_3_2)
		arg_2_0.StartAnimation(arg_3_1, arg_3_2))
	arg_2_0.bind(var_0_0.STOP_ANIMATION, function(arg_4_0, arg_4_1, arg_4_2)
		arg_2_0.StopAnimation(arg_4_1, arg_4_2))
	arg_2_0.bind(var_0_0.SET_CONTENT, function(arg_5_0, arg_5_1, arg_5_2)
		arg_2_0.AdjustChatPosition(arg_5_1, arg_5_2))
	arg_2_0.bind(GAME.LOAD_LAYERS, function(arg_6_0, arg_6_1)
		local var_6_0 = arg_6_1.context

		if var_6_0.mediator == CommissionInfoMediator or var_6_0.mediator == NotificationMediator:
			arg_2_0.StopAnimation()

			arg_2_0.stopChatFlag = True)
	arg_2_0.bind(GAME.WILL_LOGOUT, function()
		arg_2_0.stopChatFlag = False)
	arg_2_0.bind(GAME.REMOVE_LAYERS, function(arg_8_0, arg_8_1)
		local var_8_0 = arg_8_1.context

		if var_8_0.mediator == CommissionInfoMediator or var_8_0.mediator == NotificationMediator:
			arg_2_0.stopChatFlag = False)

def var_0_0.Fold(arg_9_0, arg_9_1, arg_9_2):
	LeanTween.cancel(go(arg_9_0.chatTf))

	if not arg_9_1:
		arg_9_0.chatTf.anchoredPosition = arg_9_0.chatPos
	elif arg_9_2 > 0:
		local var_9_0 = arg_9_0.chatTf.anchoredPosition.x

		LeanTween.value(go(arg_9_0.chatTf), var_9_0, 0, arg_9_2).setOnUpdate(System.Action_float(function(arg_10_0)
			setAnchoredPosition(arg_9_0.chatTf, {
				x = arg_10_0
			}))).setEase(LeanTweenType.easeInOutExpo)

	arg_9_0.isFoldState = arg_9_1

def var_0_0.Refresh(arg_11_0):
	arg_11_0.stopChatFlag = False

	setActive(arg_11_0.chatTxt.gameObject, False)
	setActive(arg_11_0.chatTxt.gameObject, True)

def var_0_0.Disable(arg_12_0):
	arg_12_0.stopChatFlag = False

	arg_12_0.StopAnimation()

def var_0_0.StartAnimation(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_0.stopChatFlag == True:
		return

	if LeanTween.isTweening(arg_13_0.chatTf.gameObject):
		LeanTween.cancel(arg_13_0.chatTf.gameObject)

	local var_13_0 = getProxy(SettingsProxy).ShouldShipMainSceneWord() and 1 or 0

	LeanTween.scale(rtf(arg_13_0.chatTf.gameObject), Vector3.New(var_13_0, var_13_0, 1), arg_13_1).setEase(LeanTweenType.easeOutBack).setOnComplete(System.Action(function()
		LeanTween.scale(rtf(arg_13_0.chatTf.gameObject), Vector3.New(0, 0, 1), arg_13_1).setEase(LeanTweenType.easeInBack).setDelay(arg_13_1 + arg_13_2)))

def var_0_0.StopAnimation(arg_15_0):
	if LeanTween.isTweening(arg_15_0.chatTf.gameObject):
		LeanTween.cancel(arg_15_0.chatTf.gameObject)

	arg_15_0.chatTf.localScale = Vector3.zero

def var_0_0.AdjustChatPosition(arg_16_0, arg_16_1, arg_16_2):
	local var_16_0 = arg_16_0.chatTxt

	if #var_16_0.text > CHAT_POP_STR_LEN:
		var_16_0.alignment = TextAnchor.MiddleLeft
	else
		var_16_0.alignment = TextAnchor.MiddleCenter

	local var_16_1 = var_16_0.preferredHeight + 26

	if var_16_1 > arg_16_0.initChatBgH:
		arg_16_0.chatTextBg.sizeDelta = Vector2.New(arg_16_0.chatTextBg.sizeDelta.x, var_16_1)
	else
		arg_16_0.chatTextBg.sizeDelta = Vector2.New(arg_16_0.chatTextBg.sizeDelta.x, arg_16_0.initChatBgH)

	if PLATFORM_CODE == PLATFORM_US:
		setTextEN(arg_16_0.chatTxt, arg_16_2)
	else
		setText(arg_16_0.chatTxt, SwitchSpecialChar(arg_16_2))

	arg_16_0.RegisterBtn(arg_16_1)

def var_0_0.RegisterBtn(arg_17_0, arg_17_1):
	removeOnButton(arg_17_0.chatTf)
	onButton(arg_17_0, arg_17_0.chatTf, function()
		if arg_17_1 == "mission_complete" or arg_17_1 == "mission":
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.TASK)
		elif arg_17_1 == "collection":
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.EVENT)
		elif arg_17_1 == "event_complete":
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.EVENT))

def var_0_0.Dispose(arg_19_0):
	var_0_0.super.Dispose(arg_19_0)
	LeanTween.cancel(arg_19_0.chatTf.gameObject)

return var_0_0
