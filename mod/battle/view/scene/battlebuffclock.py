ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffClock = class("BattleBuffClock")
var_0_0.Battle.BattleBuffClock.__name = "BattleBuffClock"

local var_0_1 = var_0_0.Battle.BattleBuffClock

var_0_1.OFFSET = Vector3(1.8, 2.3, 0)
var_0_1.TYPE_INDEX = 3

def var_0_1.Ctor(arg_1_0, arg_1_1):
	arg_1_0._castClockTF = arg_1_1
	arg_1_0._castClockGO = arg_1_0._castClockTF.gameObject
	arg_1_0._bgList = arg_1_0._castClockTF.Find("bg")
	arg_1_0._danger = arg_1_0._castClockTF.Find("danger")
	arg_1_0._interrupt = arg_1_0._castClockTF.Find("interrupt")
	arg_1_0._casting = arg_1_0._castClockTF.Find("casting")
	arg_1_0._progressProtected = arg_1_0._castClockTF.Find("progress/protected")
	arg_1_0._progressInterrupt = arg_1_0._castClockTF.Find("progress/interrupt")
	arg_1_0._clockCG = arg_1_0._castClockTF.GetComponent(typeof(CanvasGroup))

def var_0_1.switchToIndex(arg_2_0, arg_2_1, arg_2_2):
	for iter_2_0 = 1, var_0_1.TYPE_INDEX:
		local var_2_0 = arg_2_1.Find(tostring(iter_2_0))

		SetActive(var_2_0, arg_2_2 == iter_2_0)

def var_0_1.IsActive(arg_3_0):
	return arg_3_0._buffEffect != None

def var_0_1.Casting(arg_4_0, arg_4_1):
	LeanTween.cancel(arg_4_0._castClockGO)

	arg_4_0._castClockTF.localScale = Vector3(0.1, 0.1, 1)

	local var_4_0 = arg_4_1.iconType

	arg_4_0.switchToIndex(arg_4_0._bgList, var_4_0)
	arg_4_0.switchToIndex(arg_4_0._danger, var_4_0)
	arg_4_0.switchToIndex(arg_4_0._interrupt, var_4_0)
	arg_4_0.switchToIndex(arg_4_0._casting, var_4_0)
	SetActive(arg_4_0._progressInterrupt, arg_4_1.interrupt)
	SetActive(arg_4_0._progressProtected, not arg_4_1.interrupt)

	arg_4_0._castProgress = arg_4_1.interrupt and arg_4_0._progressInterrupt.GetComponent(typeof(Image)) or arg_4_0._progressProtected.GetComponent(typeof(Image))

	SetActive(arg_4_0._castClockTF, True)
	SetActive(arg_4_0._casting, True)
	SetActive(arg_4_0._interrupt, False)
	LeanTween.scale(rtf(arg_4_0._castClockGO), Vector3.New(1, 1, 1), 0.1).setEase(LeanTweenType.easeInBack)
	LeanTween.rotate(rtf(arg_4_0._danger), 360, 5).setLoopClamp()

	arg_4_0._buffEffect = arg_4_1.buffEffect

def var_0_1.Interrupt(arg_5_0, arg_5_1):
	if arg_5_1.interrupt:
		SetActive(arg_5_0._casting, False)
		SetActive(arg_5_0._interrupt, True)

	LeanTween.cancel(go(arg_5_0._danger))

	for iter_5_0 = 1, 2:
		LeanTween.alphaCanvas(arg_5_0._clockCG, 0.3, 0.3).setFrom(1).setDelay(0.3 * (iter_5_0 - 1))
		LeanTween.alphaCanvas(arg_5_0._clockCG, 1, 0.3).setDelay(0.3 * iter_5_0)

	LeanTween.scale(rtf(arg_5_0._castClockGO), Vector3.New(0.1, 0.1, 1), 0.3).setEase(LeanTweenType.easeInBack).setDelay(1.25).setOnComplete(System.Action(function()
		arg_5_0._buffEffect = None

		SetActive(arg_5_0._castClockTF, False)))

def var_0_1.UpdateCastClockPosition(arg_7_0, arg_7_1):
	arg_7_0._castClockTF.position = arg_7_1 + var_0_1.OFFSET

def var_0_1.UpdateCastClock(arg_8_0):
	arg_8_0._castProgress.fillAmount = arg_8_0._buffEffect.GetCountProgress()

def var_0_1.Dispose(arg_9_0):
	arg_9_0._buffEffect = None

	Object.Destroy(arg_9_0._castClockGO)

	arg_9_0._castClockTF = None
	arg_9_0._castClockGO = None
	arg_9_0._castProgress = None
	arg_9_0._interrupt = None
	arg_9_0._casting = None
	arg_9_0._bgList = None
	arg_9_0._danger = None
	arg_9_0._progressInterrupt = None
	arg_9_0._progressProtected = None
