ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BossSkillAlert = class("BossSkillAlert")
var_0_0.Battle.BossSkillAlert.__name = "BossSkillAlert"

def var_0_0.Battle.BossSkillAlert.Ctor(arg_1_0, arg_1_1):
	arg_1_0._alertGO = arg_1_1
	arg_1_0._alertTF = arg_1_1.transform
	arg_1_0._alertTF.localPosition = Vector3.zero

	LeanTween.alpha(arg_1_1, 0.3, 0.1).setDelay(0.1).setLoopPingPong()

def var_0_0.Battle.BossSkillAlert.SetActive(arg_2_0, arg_2_1):
	arg_2_0._alertGO.SetActive(arg_2_1)

def var_0_0.Battle.BossSkillAlert.GetActive(arg_3_0):
	return arg_3_0._alertGO.activeSelf

def var_0_0.Battle.BossSkillAlert.SetScale(arg_4_0, arg_4_1):
	arg_4_0._alertTF.localScale = arg_4_1

def var_0_0.Battle.BossSkillAlert.SetExistTime(arg_5_0, arg_5_1):
	arg_5_0._timer = pg.TimeMgr.GetInstance().AddBattleTimer("BossSkillAlert", 0, arg_5_1, function()
		if arg_5_0._alertGO:
			arg_5_0.Dispose())

def var_0_0.Battle.BossSkillAlert.Dispose(arg_7_0):
	pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_7_0._timer)
	LeanTween.cancel(arg_7_0._alertGO)
	Object.Destroy(arg_7_0._alertGO)

	arg_7_0._alertGO = None
