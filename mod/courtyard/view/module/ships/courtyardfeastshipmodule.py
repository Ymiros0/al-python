local var_0_0 = class("CourtYardFeastShipModule", import(".CourtYardShipModule"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.feastAttachments = arg_1_0._tf.Find("feastAttachments")
	arg_1_0.bubbles = {
		arg_1_0._tf.Find("feastAttachments/greet"),
		arg_1_0._tf.Find("feastAttachments/drink"),
		arg_1_0._tf.Find("feastAttachments/eat"),
		arg_1_0._tf.Find("feastAttachments/dance"),
		arg_1_0._tf.Find("feastAttachments/sleep")
	}
	arg_1_0.expressList = {
		arg_1_0._tf.Find("feastAttachments/express/1"),
		arg_1_0._tf.Find("feastAttachments/express/2"),
		arg_1_0._tf.Find("feastAttachments/express/3"),
		arg_1_0._tf.Find("feastAttachments/express/4")
	}
	arg_1_0.chatBubble = arg_1_0._tf.Find("feastAttachments/chat")
	arg_1_0.chatBubbleTxt = arg_1_0._tf.Find("feastAttachments/chat/Text").GetComponent(typeof(Text))
	arg_1_0.specialMark = arg_1_0._tf.Find("feastAttachments/specialmark")

	setActive(arg_1_0.chatBubble, False)
	setParent(arg_1_0.specialMark, arg_1_0._tf)
	arg_1_0.specialMark.SetAsFirstSibling()

	arg_1_0.specialMark.localScale = Vector3(2, 2, 1)

	arg_1_0.InitMark()

	arg_1_0.timers = {}

def var_0_0.InitMark(arg_2_0):
	setActive(arg_2_0.specialMark, arg_2_0.data.IsSpecial())
	arg_2_0.OnFeastBubbleChange(arg_2_0.data.bubble)

	arg_2_0.bubbles[1].GetComponent(typeof(Image)).raycastTarget = True

	onButton(arg_2_0, arg_2_0.bubbles[1], function()
		triggerButton(arg_2_0.clickTF), SFX_PANEL)

def var_0_0.AddListeners(arg_4_0):
	var_0_0.super.AddListeners(arg_4_0)
	arg_4_0.AddListener(CourtYardEvent.FEAST_SHIP_BUBBLE_CHANGE, arg_4_0.OnFeastBubbleChange)
	arg_4_0.AddListener(CourtYardEvent.FEAST_SHIP_CHAT_CHANGE, arg_4_0.OnFeastChatChange)
	arg_4_0.AddListener(CourtYardEvent.FEAST_SHIP_BUBBLE_INTERACTION, arg_4_0.OnFeastShipBubbleInterAction)
	arg_4_0.AddListener(CourtYardEvent.FEAST_SHIP_SHOW_EXPRESS, arg_4_0.OnFeastShipShowExpress)

def var_0_0.RemoveListeners(arg_5_0):
	var_0_0.super.RemoveListeners(arg_5_0)
	arg_5_0.RemoveListener(CourtYardEvent.FEAST_SHIP_BUBBLE_CHANGE, arg_5_0.OnFeastBubbleChange)
	arg_5_0.RemoveListener(CourtYardEvent.FEAST_SHIP_CHAT_CHANGE, arg_5_0.OnFeastChatChange)
	arg_5_0.RemoveListener(CourtYardEvent.FEAST_SHIP_BUBBLE_INTERACTION, arg_5_0.OnFeastShipBubbleInterAction)
	arg_5_0.RemoveListener(CourtYardEvent.FEAST_SHIP_SHOW_EXPRESS, arg_5_0.OnFeastShipShowExpress)

def var_0_0.OnFeastShipShowExpress(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0.expressList[arg_6_1]

	if var_6_0:
		arg_6_0.ClearChatAnimation()
		arg_6_0.PlayExpressAnim(var_6_0)

def var_0_0.PlayExpressAnim(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	arg_7_3 = defaultValue(arg_7_3, 0)
	arg_7_2 = defaultValue(arg_7_2, Vector3(1, 1, 1))

	LeanTween.scale(go(arg_7_1), arg_7_2, 0.5).setEase(LeanTweenType.easeOutBack).setDelay(arg_7_3).setOnComplete(System.Action(function()
		arg_7_0.PlayExpressAnim(arg_7_1, Vector3(0, 0, 0), 2)))

def var_0_0.ClearChatAnimation(arg_9_0):
	var_0_0.super.ClearChatAnimation(arg_9_0)

	for iter_9_0, iter_9_1 in ipairs(arg_9_0.expressList or {}):
		if LeanTween.isTweening(iter_9_1.gameObject):
			LeanTween.cancel(iter_9_1.gameObject)

		iter_9_1.localScale = Vector3.zero

def var_0_0.OnFeastBubbleChange(arg_10_0, arg_10_1):
	for iter_10_0, iter_10_1 in ipairs(arg_10_0.bubbles):
		setActive(iter_10_1, iter_10_0 == arg_10_1)

def var_0_0.OnFeastChatChange(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1 != ""

	setActive(arg_11_0.chatBubble, var_11_0)

	arg_11_0.chatBubbleTxt.text = arg_11_1

	arg_11_0.RemoveDisappearTimer()

	if var_11_0:
		arg_11_0.DisappearTimer()

local var_0_1 = {
	"AiXin",
	"XinXin",
	"XinXin",
	"YinFu",
	"Zzz"
}

def var_0_0.OnFeastShipBubbleInterAction(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_0.GetView().poolMgr
	local var_12_1 = var_0_1[arg_12_1] or var_0_1[1]
	local var_12_2 = var_12_0["Get" .. var_12_1 .. "Pool"](var_12_0).Dequeue()

	var_12_2.transform.SetParent(arg_12_0._tf, False)

	tf(var_12_2).localPosition = Vector3(0, 100, -100)
	tf(var_12_2).localScale = Vector3(3, 3, 3)

	local var_12_3 = #arg_12_0.timers + 1
	local var_12_4

	arg_12_0.cg.blocksRaycasts = False
	var_12_4 = Timer.New(function()
		var_12_4.Stop()
		table.remove(arg_12_0.timers, var_12_3)
		arg_12_0.Emit("ShipBubbleInterActionFinish", arg_12_0.data.id)

		arg_12_0.cg.blocksRaycasts = True, 0.01, 1)

	var_12_4.Start()
	table.insert(arg_12_0.timers, var_12_4)

def var_0_0.DisappearTimer(arg_14_0):
	arg_14_0.disappearTimer = Timer.New(function()
		setActive(arg_14_0.chatBubble, False), CourtYardConst.FEAST_CHAT_TIME, 1)

	arg_14_0.disappearTimer.Start()

def var_0_0.RemoveDisappearTimer(arg_16_0):
	if arg_16_0.disappearTimer:
		arg_16_0.disappearTimer.Stop()

		arg_16_0.disappearTimer = None

def var_0_0.OnStateChange(arg_17_0, arg_17_1, arg_17_2):
	var_0_0.super.OnStateChange(arg_17_0, arg_17_1, arg_17_2)

	local var_17_0 = False

	if arg_17_0.data.IsSpecial() and (arg_17_1 == CourtYardShip.STATE_IDLE or arg_17_1 == CourtYardShip.STATE_MOVE or arg_17_1 == CourtYardShip.STATE_MOVING_ZERO or arg_17_1 == CourtYardShip.STATE_MOVING_HALF or arg_17_1 == CourtYardShip.STATE_MOVING_ONE or arg_17_1 == CourtYardShip.STATE_TOUCH or arg_17_1 == CourtYardShip.STATE_GETAWARD):
		var_17_0 = True

	setActive(arg_17_0.specialMark, var_17_0)

	local var_17_1 = arg_17_1 == CourtYardShip.STATE_INTERACT

	arg_17_0.feastAttachments.localPosition = var_17_1 and Vector3(0, -85, 0) or Vector3.zero

def var_0_0.OnDestroy(arg_18_0):
	arg_18_0.cg.blocksRaycasts = True

	for iter_18_0, iter_18_1 in ipairs(arg_18_0.timers or {}):
		iter_18_1.Stop()

	arg_18_0.timers = None

	arg_18_0.RemoveDisappearTimer()

	if arg_18_0.feastAttachments:
		setParent(arg_18_0.specialMark, arg_18_0.feastAttachments)

		arg_18_0.specialMark.localScale = Vector3.one

		Object.Destroy(arg_18_0.feastAttachments.gameObject)

		arg_18_0.feastAttachments = None

	var_0_0.super.OnDestroy(arg_18_0)

return var_0_0
