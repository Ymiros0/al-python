ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBarrierBar = class("BattleBarrierBar")
var_0_0.Battle.BattleBarrierBar.__name = "BattleBarrierBar"

local var_0_1 = var_0_0.Battle.BattleBarrierBar

var_0_1.OFFSET = Vector3(1.8, 2.3, 0)

def var_0_1.Ctor(arg_1_0, arg_1_1):
	arg_1_0._barrierClockTF = arg_1_1
	arg_1_0._barrierClockGO = arg_1_0._barrierClockTF.gameObject
	arg_1_0._castProgress = arg_1_0._barrierClockTF.Find("shield_progress").GetComponent(typeof(Image))
	arg_1_0._danger = arg_1_0._barrierClockTF.Find("danger")
	arg_1_0._clockCG = arg_1_0._barrierClockTF.GetComponent(typeof(CanvasGroup))

def var_0_1.Shielding(arg_2_0, arg_2_1):
	arg_2_0._barrierClockTF.localScale = Vector3(0.1, 0.1, 1)

	SetActive(arg_2_0._barrierClockTF, True)
	LeanTween.scale(rtf(arg_2_0._barrierClockGO), Vector3.New(1, 1, 1), 0.1).setEase(LeanTweenType.easeInBack)

	arg_2_0._barrierFinishTime = pg.TimeMgr.GetInstance().GetCombatTime() + arg_2_1
	arg_2_0._barrierDuration = arg_2_1

	LeanTween.rotate(rtf(arg_2_0._danger), 360, 5).setLoopClamp()

def var_0_1.Interrupt(arg_3_0):
	LeanTween.cancel(go(arg_3_0._danger))
	LeanTween.scale(rtf(arg_3_0._barrierClockGO), Vector3.New(0.1, 0.1, 1), 0.3).setEase(LeanTweenType.easeInBack).setOnComplete(System.Action(function()
		SetActive(arg_3_0._barrierClockTF, False)))

def var_0_1.UpdateBarrierClockPosition(arg_5_0, arg_5_1):
	arg_5_0._barrierClockTF.position = arg_5_1 + var_0_1.OFFSET

def var_0_1.UpdateBarrierClockProgress(arg_6_0):
	local var_6_0 = pg.TimeMgr.GetInstance().GetCombatTime()

	arg_6_0._castProgress.fillAmount = (arg_6_0._barrierFinishTime - var_6_0) / arg_6_0._barrierDuration

def var_0_1.Dispose(arg_7_0):
	Object.Destroy(arg_7_0._barrierClockGO)

	arg_7_0._barrierClockTF = None
	arg_7_0._barrierClockGO = None
	arg_7_0._castProgress = None
