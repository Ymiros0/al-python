local var_0_0 = class("CardPairsCard")

var_0_0.CARD_STATE_BACK = 0
var_0_0.CARD_STATE_FRONT = 1
var_0_0.CARD_STATE_HIDE = 2
var_0_0.ANI_TIME = 0.5

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5, arg_1_6):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.cardTf = arg_1_1
	arg_1_0.pics = arg_1_2
	arg_1_0.img = findTF(arg_1_0.cardTf, "img")
	arg_1_0.back = findTF(arg_1_0.cardTf, "back")
	arg_1_0.front = findTF(arg_1_0.cardTf, "front")
	arg_1_0.clearSign = findTF(arg_1_0.cardTf, "gray")
	arg_1_0.outline = GetComponent(arg_1_0.front, typeof(Outline))

	arg_1_0.setOutline(False)

	arg_1_0.cardState = arg_1_0.CARD_STATE_BACK
	arg_1_0.canClick = True
	arg_1_0.enable = True
	arg_1_0.aniCallBack = arg_1_6
	arg_1_0.aniStartCallBak = arg_1_5

	arg_1_0.initCard(arg_1_3)
	onButton(arg_1_0, arg_1_0.cardTf, function()
		arg_1_4(arg_1_0))

def var_0_0.getCardIndex(arg_3_0):
	return arg_3_0.cardIndex

def var_0_0.setEnable(arg_4_0, arg_4_1):
	arg_4_0.enable = arg_4_1

def var_0_0.setClear(arg_5_0):
	setActive(arg_5_0.clearSign, True)
	arg_5_0.setOutline(False)

	arg_5_0.canClick = False

def var_0_0.setOutline(arg_6_0, arg_6_1):
	arg_6_0.outline.enabled = arg_6_1

def var_0_0.initCard(arg_7_0, arg_7_1):
	arg_7_0.cardIndex = arg_7_1

	arg_7_0.setSpriteTo(findTF(arg_7_0.pics, "pic" .. arg_7_1), arg_7_0.img, False)
	setActive(arg_7_0.clearSign, False)
	arg_7_0.showBack()

	arg_7_0.canClick = True

def var_0_0.showBack(arg_8_0):
	setActive(arg_8_0.back, True)
	setActive(arg_8_0.front, False)
	setActive(arg_8_0.img, False)

	arg_8_0.cardState = arg_8_0.CARD_STATE_BACK

	arg_8_0.setOutline(False)

def var_0_0.showFront(arg_9_0):
	setActive(arg_9_0.back, False)
	setActive(arg_9_0.front, True)
	setActive(arg_9_0.img, True)

	arg_9_0.cardState = arg_9_0.CARD_STATE_FRONT

def var_0_0.aniShowBack(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	arg_10_0.canClick = False

	if arg_10_1:
		arg_10_0.showBack()
	else
		arg_10_0.showFront()

	if not arg_10_2:
		arg_10_0.aniStartCallBak(arg_10_0, arg_10_1)

	arg_10_0.cardTf.localScale = Vector3(1, 1, 1)

	LeanTween.scale(go(arg_10_0.cardTf), Vector3(0, 1, 1), arg_10_0.ANI_TIME).setDelay(defaultValue(arg_10_3, 0)).setOnComplete(System.Action(function()
		if arg_10_1:
			arg_10_0.showFront()
		else
			arg_10_0.showBack()

		LeanTween.scale(go(arg_10_0.cardTf), Vector3(1, 1, 1), arg_10_0.ANI_TIME).setOnComplete(System.Action(function()
			arg_10_0.canClick = True

			if not arg_10_2:
				arg_10_0.aniCallBack(arg_10_0, arg_10_1)))))

def var_0_0.setSpriteTo(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	local var_13_0 = arg_13_2.GetComponent(typeof(Image))

	var_13_0.sprite = arg_13_1.GetComponent(typeof(Image)).sprite

	if arg_13_3:
		var_13_0.SetNativeSize()

def var_0_0.clear(arg_14_0):
	LeanTween.cancel(go(arg_14_0.cardTf))

def var_0_0.destroy(arg_15_0):
	pg.DelegateInfo.Dispose(arg_15_0)
	LeanTween.cancel(go(arg_15_0.cardTf))

return var_0_0
