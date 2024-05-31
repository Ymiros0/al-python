local var_0_0 = class("MainWordView", import("...base.MainBaseView"))

var_0_0.START_ANIMATION = "MainWordView:ON_ANIMATION"
var_0_0.STOP_ANIMATION = "MainWordView:STOP_ANIMATION"
var_0_0.SET_CONTENT = "MainWordView:SET_CONTENT"

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.chatTf = arg_1_1
	arg_1_0.chatPos = arg_1_0.chatTf.anchoredPosition
	arg_1_0.chatTxt = arg_1_0.chatTf:Find("Text"):GetComponent(typeof(Text))
	arg_1_0.chatTextBg = arg_1_0.chatTf:Find("chatbgtop")
	arg_1_0.initChatBgH = arg_1_0.chatTextBg.sizeDelta.y
	arg_1_0.stopChatFlag = false

	arg_1_0:Register()
end

function var_0_0.Register(arg_2_0)
	arg_2_0:bind(var_0_0.START_ANIMATION, function(arg_3_0, arg_3_1, arg_3_2)
		arg_2_0:StartAnimation(arg_3_1, arg_3_2)
	end)
	arg_2_0:bind(var_0_0.STOP_ANIMATION, function(arg_4_0, arg_4_1, arg_4_2)
		arg_2_0:StopAnimation(arg_4_1, arg_4_2)
	end)
	arg_2_0:bind(var_0_0.SET_CONTENT, function(arg_5_0, arg_5_1, arg_5_2)
		arg_2_0:AdjustChatPosition(arg_5_1, arg_5_2)
	end)
	arg_2_0:bind(GAME.LOAD_LAYERS, function(arg_6_0, arg_6_1)
		local var_6_0 = arg_6_1.context

		if var_6_0.mediator == CommissionInfoMediator or var_6_0.mediator == NotificationMediator then
			arg_2_0:StopAnimation()

			arg_2_0.stopChatFlag = true
		end
	end)
	arg_2_0:bind(GAME.WILL_LOGOUT, function()
		arg_2_0.stopChatFlag = false
	end)
	arg_2_0:bind(GAME.REMOVE_LAYERS, function(arg_8_0, arg_8_1)
		local var_8_0 = arg_8_1.context

		if var_8_0.mediator == CommissionInfoMediator or var_8_0.mediator == NotificationMediator then
			arg_2_0.stopChatFlag = false
		end
	end)
end

function var_0_0.Fold(arg_9_0, arg_9_1, arg_9_2)
	LeanTween.cancel(go(arg_9_0.chatTf))

	if not arg_9_1 then
		arg_9_0.chatTf.anchoredPosition = arg_9_0.chatPos
	elseif arg_9_2 > 0 then
		local var_9_0 = arg_9_0.chatTf.anchoredPosition.x

		LeanTween.value(go(arg_9_0.chatTf), var_9_0, 0, arg_9_2):setOnUpdate(System.Action_float(function(arg_10_0)
			setAnchoredPosition(arg_9_0.chatTf, {
				x = arg_10_0
			})
		end)):setEase(LeanTweenType.easeInOutExpo)
	end

	arg_9_0.isFoldState = arg_9_1
end

function var_0_0.Refresh(arg_11_0)
	arg_11_0.stopChatFlag = false

	setActive(arg_11_0.chatTxt.gameObject, false)
	setActive(arg_11_0.chatTxt.gameObject, true)
end

function var_0_0.Disable(arg_12_0)
	arg_12_0.stopChatFlag = false

	arg_12_0:StopAnimation()
end

function var_0_0.StartAnimation(arg_13_0, arg_13_1, arg_13_2)
	if arg_13_0.stopChatFlag == true then
		return
	end

	if LeanTween.isTweening(arg_13_0.chatTf.gameObject) then
		LeanTween.cancel(arg_13_0.chatTf.gameObject)
	end

	local var_13_0 = getProxy(SettingsProxy):ShouldShipMainSceneWord() and 1 or 0

	LeanTween.scale(rtf(arg_13_0.chatTf.gameObject), Vector3.New(var_13_0, var_13_0, 1), arg_13_1):setEase(LeanTweenType.easeOutBack):setOnComplete(System.Action(function()
		LeanTween.scale(rtf(arg_13_0.chatTf.gameObject), Vector3.New(0, 0, 1), arg_13_1):setEase(LeanTweenType.easeInBack):setDelay(arg_13_1 + arg_13_2)
	end))
end

function var_0_0.StopAnimation(arg_15_0)
	if LeanTween.isTweening(arg_15_0.chatTf.gameObject) then
		LeanTween.cancel(arg_15_0.chatTf.gameObject)
	end

	arg_15_0.chatTf.localScale = Vector3.zero
end

function var_0_0.AdjustChatPosition(arg_16_0, arg_16_1, arg_16_2)
	local var_16_0 = arg_16_0.chatTxt

	if #var_16_0.text > CHAT_POP_STR_LEN then
		var_16_0.alignment = TextAnchor.MiddleLeft
	else
		var_16_0.alignment = TextAnchor.MiddleCenter
	end

	local var_16_1 = var_16_0.preferredHeight + 26

	if var_16_1 > arg_16_0.initChatBgH then
		arg_16_0.chatTextBg.sizeDelta = Vector2.New(arg_16_0.chatTextBg.sizeDelta.x, var_16_1)
	else
		arg_16_0.chatTextBg.sizeDelta = Vector2.New(arg_16_0.chatTextBg.sizeDelta.x, arg_16_0.initChatBgH)
	end

	if PLATFORM_CODE == PLATFORM_US then
		setTextEN(arg_16_0.chatTxt, arg_16_2)
	else
		setText(arg_16_0.chatTxt, SwitchSpecialChar(arg_16_2))
	end

	arg_16_0:RegisterBtn(arg_16_1)
end

function var_0_0.RegisterBtn(arg_17_0, arg_17_1)
	removeOnButton(arg_17_0.chatTf)
	onButton(arg_17_0, arg_17_0.chatTf, function()
		if arg_17_1 == "mission_complete" or arg_17_1 == "mission" then
			pg.m02:sendNotification(GAME.GO_SCENE, SCENE.TASK)
		elseif arg_17_1 == "collection" then
			pg.m02:sendNotification(GAME.GO_SCENE, SCENE.EVENT)
		elseif arg_17_1 == "event_complete" then
			pg.m02:sendNotification(GAME.GO_SCENE, SCENE.EVENT)
		end
	end)
end

function var_0_0.Dispose(arg_19_0)
	var_0_0.super.Dispose(arg_19_0)
	LeanTween.cancel(arg_19_0.chatTf.gameObject)
end

return var_0_0
