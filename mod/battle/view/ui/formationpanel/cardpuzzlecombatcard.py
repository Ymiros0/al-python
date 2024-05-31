ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.CardPuzzleCombatCard = class("CardPuzzleCombatCard", CardPuzzleCardView)

local var_0_2 = var_0_0.Battle.CardPuzzleCombatCard

var_0_2.__name = "CardPuzzleCombatCard"
var_0_2.CARD_SCALE = Vector3(0.57, 0.57, 0)
var_0_2.DRAG_SCALE = Vector3(0.65, 0.65, 0)
var_0_2.DRAW_SCALE = Vector3(0.2, 0.2, 0)
var_0_2.SHUFFLE_SCALE = Vector3(0.1, 0.1, 0)
var_0_2.RECYLE_POS = Vector3(10000, 10000, 0)
var_0_2.STATE_LOCK = "STATE_LOCK"
var_0_2.STATE_FREE = "STATE_FREE"
var_0_2.STATE_DRAG = "STATE_DRAG"
var_0_2.STATE_LONG_PRESS = "STATE_LONG_PRESS"
var_0_2.BASE_LERP = 0.2

def var_0_2.Ctor(arg_1_0, arg_1_1):
	var_0_2.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._go = arg_1_1.gameObject
	arg_1_1.localScale = var_0_2.CARD_SCALE
	arg_1_0._moveLerp = 0.2
	arg_1_0._pos = Vector3.zero

def var_0_2.GetRarityBG(arg_2_0, arg_2_1):
	return "battle_card_bg_" .. arg_2_1

def var_0_2.GetCardCost(arg_3_0):
	return arg_3_0.data.GetTotalCost()

def var_0_2.UpdateView(arg_4_0):
	var_0_2.super.UpdateView(arg_4_0)

	arg_4_0._coolDown = arg_4_0._tf.Find("cooldown")
	arg_4_0._coolDownProgress = arg_4_0._coolDown.GetComponent(typeof(Image))
	arg_4_0._canvaGroup = arg_4_0._tf.GetComponent(typeof(CanvasGroup))
	arg_4_0._boostHint = arg_4_0._tf.Find("boost_hint")

	arg_4_0.UpdateTotalCost()
	arg_4_0.UpdateBoostHint()

def var_0_2.Update(arg_5_0):
	arg_5_0.updateCoolDown()
	arg_5_0.MoveToRefPos()

def var_0_2.ShowGray(arg_6_0, arg_6_1):
	setGray(arg_6_0._tf, arg_6_1, True)

def var_0_2.SetCardInfo(arg_7_0, arg_7_1):
	arg_7_0._cardInfo = arg_7_1

	arg_7_0.SetData(arg_7_0._cardInfo)

def var_0_2.GetCardInfo(arg_8_0):
	return arg_8_0._cardInfo

def var_0_2.DrawAnima(arg_9_0, arg_9_1):
	arg_9_0.drawAlphaAndScale()

	arg_9_0._tf.localPosition = arg_9_1

def var_0_2.GetUIPos(arg_10_0):
	return arg_10_0._tf.anchoredPosition

def var_0_2.SetSibling(arg_11_0, arg_11_1):
	arg_11_0._tf.SetSiblingIndex(arg_11_1)

def var_0_2.SetReferencePos(arg_12_0, arg_12_1):
	arg_12_0._refPos = arg_12_1

def var_0_2.SetMoveLerp(arg_13_0, arg_13_1):
	arg_13_0._moveLerp = arg_13_1 or var_0_2.BASE_LERP

def var_0_2.MoveToRefPos(arg_14_0):
	if arg_14_0._tf.localPosition.Equals(arg_14_0._refPos):
		if arg_14_0._moveToPointCallback:
			arg_14_0._moveToPointCallback()

			arg_14_0._moveToPointCallback = None

		return

	if arg_14_0._moveLerp == 1:
		arg_14_0._pos.Copy(arg_14_0._refPos)
	else
		local var_14_0 = arg_14_0._tf.localPosition
		local var_14_1 = Vector2.Lerp(var_14_0, arg_14_0._refPos, arg_14_0._moveLerp)

		arg_14_0._pos.Copy(var_14_1)

	arg_14_0._tf.localPosition = arg_14_0._pos

def var_0_2.SetToObjPoolRecylePos(arg_15_0):
	arg_15_0._tf.localPosition = var_0_2.RECYLE_POS

def var_0_2.MoveToDeck(arg_16_0, arg_16_1, arg_16_2):
	arg_16_0.shuffleBackAlphaAndScale()
	arg_16_0.SetMoveLerp(0.8)

	arg_16_0._refPos = arg_16_2
	arg_16_0._moveToPointCallback = arg_16_1

def var_0_2.GetState(arg_17_0):
	return arg_17_0._state

def var_0_2.ChangeState(arg_18_0, arg_18_1):
	arg_18_0._state = arg_18_1

def var_0_2.ConfigOP(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4, arg_19_5, arg_19_6):
	arg_19_0._dragDelegate = GetOrAddComponent(arg_19_0._go, "EventTriggerListener")

	arg_19_0._dragDelegate.AddPointUpFunc(function(arg_20_0, arg_20_1)
		arg_19_6())
	arg_19_0._dragDelegate.AddBeginDragFunc(function(arg_21_0, arg_21_1)
		arg_19_0.dragAlphaAndScale()
		arg_19_2(arg_19_0._cardInfo))
	arg_19_0._dragDelegate.AddDragFunc(function(arg_22_0, arg_22_1)
		arg_19_3(arg_22_1.position))
	arg_19_0._dragDelegate.AddDragEndFunc(function(arg_23_0, arg_23_1)
		arg_19_0.resetAll()
		arg_19_4())

	arg_19_0._longPressDelegate = GetOrAddComponent(arg_19_0._go, "UILongPressTrigger")
	arg_19_0._longPressDelegate.longPressThreshold = 0.5

	arg_19_0._longPressDelegate.onLongPressed.AddListener(function()
		arg_19_5())

def var_0_2.updateCoolDown(arg_25_0):
	if arg_25_0._cardInfo.GetCastRemainRate() > 0:
		setActive(arg_25_0._coolDown, True)

		arg_25_0._coolDownProgress.fillAmount = arg_25_0._cardInfo.GetCastRemainRate()
	else
		setActive(arg_25_0._coolDown, False)

def var_0_2.change2ScrPos(arg_26_0, arg_26_1):
	local var_26_0 = pg.UIMgr.GetInstance().overlayCameraComp

	return (LuaHelper.ScreenToLocal(arg_26_0, arg_26_1, var_26_0))

def var_0_2.UpdateDragPosition(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_0.change2ScrPos(arg_27_0._tf.parent, arg_27_1)

	arg_27_0.SetReferencePos(var_27_0)

def var_0_2.BlockRayCast(arg_28_0, arg_28_1):
	arg_28_0._canvaGroup.blocksRaycasts = arg_28_1

def var_0_2.UpdateTotalCost(arg_29_0):
	if arg_29_0._cardInfo:
		setText(arg_29_0.costTF, arg_29_0.data.GetTotalCost())

def var_0_2.UpdateBoostHint(arg_30_0):
	if arg_30_0._cardInfo:
		setActive(arg_30_0._boostHint, arg_30_0._cardInfo.IsBoost())

def var_0_2.dragAlphaAndScale(arg_31_0):
	LeanTween.cancel(arg_31_0._go)
	LeanTween.scale(arg_31_0._go, var_0_2.DRAG_SCALE, 0.1)
	LeanTween.alphaCanvas(arg_31_0._canvaGroup, 0.7, 0.1)

def var_0_2.drawAlphaAndScale(arg_32_0):
	LeanTween.cancel(arg_32_0._go)

	arg_32_0._tf.localScale = var_0_2.DRAW_SCALE
	arg_32_0._canvaGroup.alpha = 0.2

	LeanTween.scale(arg_32_0._go, var_0_2.CARD_SCALE, 0.2)
	LeanTween.alphaCanvas(arg_32_0._canvaGroup, 1, 0.2)

def var_0_2.shuffleBackAlphaAndScale(arg_33_0):
	arg_33_0.resetAll()
	LeanTween.scale(arg_33_0._go, var_0_2.SHUFFLE_SCALE, 0.2)
	LeanTween.alphaCanvas(arg_33_0._canvaGroup, 0, 0.2)

def var_0_2.resetAll(arg_34_0):
	LeanTween.cancel(arg_34_0._go)

	arg_34_0._tf.localScale = var_0_2.CARD_SCALE
	arg_34_0._canvaGroup.alpha = 1
