local var_0_0 = class("CourtYardShipModule", import("..CourtYardPlaceableModule"))
local var_0_1 = 1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	var_0_1 = CourtYardConst.SHIP_SCALE

	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.role = arg_1_3

def var_0_0.OnInit(arg_2_0):
	var_0_0.super.OnInit(arg_2_0)
	pg.ViewUtils.SetLayer(arg_2_0._tf, Layer.UI)
	arg_2_0._tf.SetParent(arg_2_0.floor)

	arg_2_0.model = arg_2_0._tf.Find("model")
	arg_2_0.model.localPosition = Vector3(0, 25, 0)
	arg_2_0.shadow = arg_2_0._tf.Find("shadow")
	arg_2_0.shadow.localPosition = Vector3(0, 25, 0)

	arg_2_0.shadow.SetAsFirstSibling()

	arg_2_0.spineAnimUI = arg_2_0.role.model.GetComponent(typeof(SpineAnimUI))
	arg_2_0.clickTF = arg_2_0._tf.Find("click")
	arg_2_0.chatTF = arg_2_0._tf.Find("chat")
	arg_2_0.chatTF.localScale = Vector3.zero
	arg_2_0.additionTF = arg_2_0._tf.Find("addition")
	arg_2_0.additionTFs = {
		findTF(arg_2_0.additionTF, "money"),
		findTF(arg_2_0.additionTF, "intimacy"),
		findTF(arg_2_0.additionTF, "exp")
	}
	arg_2_0.additionTFPos = Vector3(0, 250, 0)
	arg_2_0.inimacyBubble = arg_2_0._tf.Find("intimacy")
	arg_2_0.moneyBubble = arg_2_0._tf.Find("money")
	arg_2_0.animator = CourtYardShipAnimatorAgent.New(arg_2_0)
	arg_2_0._tf.localScale = Vector3(var_0_1, var_0_1, 1)
	arg_2_0._tf.Find("grids").localScale = Vector3(1 / var_0_1, 1 / var_0_1, 1)

	arg_2_0.animator.SetState(arg_2_0.data.GetState())
	arg_2_0.UpdateBubble(arg_2_0.inimacyBubble, arg_2_0.data.inimacy)
	arg_2_0.UpdateBubble(arg_2_0.moneyBubble, arg_2_0.data.coin)
	arg_2_0.InitAttachment()
	setActive(arg_2_0.shadow, True)

def var_0_0.AdjustYForInteraction(arg_3_0):
	arg_3_0.model.localPosition = Vector3(0, 0, 0)

def var_0_0.ResetYForInteraction(arg_4_0):
	arg_4_0.model.localPosition = Vector3(0, 25, 0)

def var_0_0.GetSpine(arg_5_0):
	return arg_5_0.spineAnimUI.gameObject.transform

def var_0_0.AddListeners(arg_6_0):
	arg_6_0.AddListener(CourtYardEvent.SHIP_STATE_CHANGE, arg_6_0.OnStateChange)
	arg_6_0.AddListener(CourtYardEvent.SHIP_MOVE, arg_6_0.OnMove)
	arg_6_0.AddListener(CourtYardEvent.SHIP_POSITION_CHANGE, arg_6_0.OnUpdatePosition)
	arg_6_0.AddListener(CourtYardEvent.SHIP_GET_AWARD, arg_6_0.OnAddAward)
	arg_6_0.AddListener(CourtYardEvent.SHIP_INIMACY_CHANGE, arg_6_0.OnInimacyChange)
	arg_6_0.AddListener(CourtYardEvent.SHIP_COIN_CHANGE, arg_6_0.OnCoinChange)
	arg_6_0.AddListener(CourtYardEvent.SHIP_UPDATE_INTERACTION, arg_6_0.OnUpdateInteraction)
	arg_6_0.AddListener(CourtYardEvent.SHIP_WILL_INTERACTION, arg_6_0.WillInterAction)
	arg_6_0.AddListener(CourtYardEvent.SHIP_START_INTERACTION, arg_6_0.StartInterAction)
	arg_6_0.AddListener(CourtYardEvent.SHIP_STOP_INTERACTION, arg_6_0.StopInterAction)

def var_0_0.RemoveListeners(arg_7_0):
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_STATE_CHANGE, arg_7_0.OnStateChange)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_MOVE, arg_7_0.OnMove)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_POSITION_CHANGE, arg_7_0.OnUpdatePosition)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_GET_AWARD, arg_7_0.OnAddAward)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_INIMACY_CHANGE, arg_7_0.OnInimacyChange)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_COIN_CHANGE, arg_7_0.OnCoinChange)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_UPDATE_INTERACTION, arg_7_0.OnUpdateInteraction)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_WILL_INTERACTION, arg_7_0.WillInterAction)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_START_INTERACTION, arg_7_0.StartInterAction)
	arg_7_0.RemoveListener(CourtYardEvent.SHIP_STOP_INTERACTION, arg_7_0.StopInterAction)

def var_0_0.InitAttachment(arg_8_0):
	onButton(arg_8_0, arg_8_0.clickTF, function()
		arg_8_0.Emit("TouchShip", arg_8_0.data.id)
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_BOAT_CLICK))
	onButton(arg_8_0, arg_8_0.inimacyBubble, function()
		arg_8_0.Emit("GetShipInimacy", arg_8_0.data.id), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.moneyBubble, function()
		arg_8_0.Emit("GetShipCoin", arg_8_0.data.id), SFX_PANEL)

def var_0_0.OnBeginDrag(arg_12_0):
	if not arg_12_0.GetView().GetCurrStorey().AllModulesAreCompletion():
		return

	arg_12_0.Emit("DragShip", arg_12_0.data.id)
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_BOAT_DRAG)

def var_0_0.OnDragging(arg_13_0, arg_13_1):
	arg_13_0.Emit("DragingShip", arg_13_0.data.id, arg_13_1)

def var_0_0.OnDragEnd(arg_14_0, arg_14_1):
	arg_14_0.Emit("DragShipEnd", arg_14_0.data.id, arg_14_1)

def var_0_0.OnUpdatePosition(arg_15_0, arg_15_1, arg_15_2):
	arg_15_0.UpdatePosition(arg_15_1, arg_15_2)

def var_0_0.OnStateChange(arg_16_0, arg_16_1, arg_16_2):
	if arg_16_1 != CourtYardShip.STATE_MOVING_ZERO and arg_16_1 != CourtYardShip.STATE_MOVING_HALF and arg_16_1 != CourtYardShip.STATE_MOVING_ONE:
		arg_16_0.ClearMove()

	arg_16_0.animator.SetState(arg_16_1)

	if arg_16_1 == CourtYardShip.STATE_TOUCH:
		arg_16_0.ClearChatAnimation()
		arg_16_0.PlayChatAnim()

def var_0_0.PlayChatAnim(arg_17_0, arg_17_1, arg_17_2, arg_17_3):
	arg_17_3 = defaultValue(arg_17_3, True)
	arg_17_2 = defaultValue(arg_17_2, 0)
	arg_17_1 = defaultValue(arg_17_1, Vector3(2, 2, 2))

	local var_17_0 = LeanTween.scale(go(arg_17_0.chatTF), arg_17_1, 0.5).setEase(LeanTweenType.easeOutBack).setDelay(arg_17_2)

	if not arg_17_3:
		return

	var_17_0.setOnComplete(System.Action(function()
		arg_17_0.PlayChatAnim(Vector3(0, 0, 0), 2, False)))

def var_0_0.ClearChatAnimation(arg_19_0):
	if LeanTween.isTweening(go(arg_19_0.chatTF)):
		LeanTween.cancel(go(arg_19_0.chatTF))

	arg_19_0.chatTF.localScale = Vector3.zero

def var_0_0.OnUpdateInteraction(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_1.action

	arg_20_0.animator.PlayInteractioAnim(var_20_0)

def var_0_0.OnAnimtionFinish(arg_21_0, arg_21_1):
	arg_21_0.Emit("ShipAnimtionFinish", arg_21_0.data.id, arg_21_1)

def var_0_0.OnMove(arg_22_0, arg_22_1, arg_22_2):
	arg_22_0.ClearMove()

	local var_22_0 = arg_22_0.data.GetPosition()
	local var_22_1 = CourtYardCalcUtil.Map2Local(arg_22_1)
	local var_22_2 = arg_22_0.data.GetMoveTime()
	local var_22_3 = arg_22_1.x < var_22_0.x and arg_22_1.y == var_22_0.y or arg_22_1.x == var_22_0.x and arg_22_1.y > var_22_0.y

	arg_22_0.model.transform.localScale = Vector3(var_22_3 and -1 or 1, 1, 1)

	local var_22_4 = Vector3(var_22_1.x, var_22_1.y, 0) + arg_22_2
	local var_22_5 = CourtYardCalcUtil.TrPosition2LocalPos(arg_22_0.GetParentTF(), arg_22_0._tf.parent, var_22_4)

	LeanTween.moveLocal(arg_22_0._go, var_22_5, var_22_2)

	for iter_22_0 = 1, arg_22_0.interactionTF.childCount:
		local var_22_6 = arg_22_0.interactionTF.GetChild(iter_22_0 - 1)

		var_22_6.localScale = Vector3(math.abs(var_22_6.localScale.x), var_22_6.localScale.y, var_22_6.localScale.z)

	arg_22_0.interactionTF.localScale = arg_22_0.model.transform.localScale

def var_0_0.OnAddAward(arg_23_0, arg_23_1, arg_23_2):
	if arg_23_2 == 3 and arg_23_1 <= 0:
		return

	for iter_23_0, iter_23_1 in pairs(arg_23_0.additionTFs):
		setActive(iter_23_1, arg_23_2 == iter_23_0)

	local var_23_0 = arg_23_0.additionTFs[arg_23_2]

	if arg_23_2 != 1:
		arg_23_1 = ""

	setText(var_23_0.Find("Text"), arg_23_1 or "")

	if arg_23_2 == 2 and arg_23_0.GetView().poolMgr.GetHeartPool():
		local var_23_1 = arg_23_0.GetView().poolMgr.GetHeartPool().Dequeue()

		var_23_1.transform.SetParent(arg_23_0._tf, False)

		tf(var_23_1).localPosition = Vector3(0, 200, -100)
		tf(var_23_1).localScale = Vector3(100, 100, 100)

	local var_23_2 = 1 / var_0_1

	if CourtYardCalcUtil.GetTransformSign(arg_23_0._tf, arg_23_0.rect) < 0:
		arg_23_0.additionTF.localScale = Vector3(-var_23_2, var_23_2, var_23_2)

	LeanTween.cancel(arg_23_0.additionTF.gameObject)

	arg_23_0.additionTF.transform.localPosition = arg_23_0.additionTFPos

	LeanTween.moveY(rtf(arg_23_0.additionTF), arg_23_0.additionTFPos.y + 110, 1.2).setOnComplete(System.Action(function()
		arg_23_0.additionTF.localScale = Vector3(var_23_2, var_23_2, var_23_2)

		setActive(var_23_0, False)))

def var_0_0.UpdateBubble(arg_25_0, arg_25_1, arg_25_2):
	setActive(arg_25_1, arg_25_2 != 0)

	if LeanTween.isTweening(arg_25_1.gameObject):
		LeanTween.cancel(arg_25_1.gameObject)

	if arg_25_2 != 0:
		arg_25_1.localScale = Vector3(2, 2, 0)

	if arg_25_2 != 0:
		floatAni(arg_25_1, 20, 1)

def var_0_0.OnInimacyChange(arg_26_0, arg_26_1):
	arg_26_0.UpdateBubble(arg_26_0.inimacyBubble, arg_26_1)

def var_0_0.OnCoinChange(arg_27_0, arg_27_1):
	arg_27_0.UpdateBubble(arg_27_0.moneyBubble, arg_27_1)

def var_0_0.ClearMove(arg_28_0):
	LeanTween.cancel(arg_28_0._go)

def var_0_0.WillInterAction(arg_29_0, arg_29_1):
	return

def var_0_0.StartInterAction(arg_30_0, arg_30_1):
	setActive(arg_30_0.shadow, False)

	local var_30_0 = arg_30_1.GetOffset()

	setAnchoredPosition(arg_30_0._tf, var_30_0)

	local var_30_1 = arg_30_1.GetOwner().GetNormalDirection()
	local var_30_2 = arg_30_1.GetScale()

	arg_30_0.model.localScale = Vector3(var_30_1 * var_30_2.x, var_30_2.y, var_30_2.z)

	arg_30_0.AdjustYForInteraction()

def var_0_0.StopInterAction(arg_31_0):
	setActive(arg_31_0.shadow, True)
	arg_31_0.ResetTransform()
	arg_31_0.ResetYForInteraction()

def var_0_0.ResetTransform(arg_32_0):
	arg_32_0._tf.localScale = Vector3(var_0_1, var_0_1, 1)
	arg_32_0._tf.localEulerAngles = Vector3.zero

def var_0_0.HideAttachment(arg_33_0, arg_33_1):
	if arg_33_0.role:
		arg_33_0.role.SetVisible(not arg_33_1)

def var_0_0.OnDispose(arg_34_0):
	var_0_0.super.OnDispose(arg_34_0)
	arg_34_0.ClearChatAnimation()
	arg_34_0.ResetTransform()

	if arg_34_0.animator:
		arg_34_0.animator.Dispose()

		arg_34_0.animator = None

	if arg_34_0.spineAnimUI:
		arg_34_0.spineAnimUI.SetActionCallBack(None)

		arg_34_0.spineAnimUI = None

	arg_34_0.ClearMove()

	if arg_34_0.role:
		arg_34_0.role.Dispose()

		arg_34_0.role = None

def var_0_0.OnDestroy(arg_35_0):
	arg_35_0.GetView().poolMgr.GetShipPool().Enqueue(arg_35_0._go)

return var_0_0
