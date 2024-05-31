ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.TorAlert = class("TorAlert")
var_0_0.Battle.TorAlert.__name = "TorAlert"

def var_0_0.Battle.TorAlert.Ctor(arg_1_0, arg_1_1):
	arg_1_0._alertGO = arg_1_1
	arg_1_0._alertTF = arg_1_1.transform
	arg_1_0._alertTF.localScale = Vector3(20, 5, 1)

	LeanTween.scaleY(arg_1_1, 0, 0.5).setDelay(0.1)

def var_0_0.Battle.TorAlert.SetPosition(arg_2_0, arg_2_1, arg_2_2):
	pg.EffectMgr.GetInstance().PlayBattleEffect(arg_2_0._alertGO, arg_2_1)

	arg_2_0._alertTF.eulerAngles = Vector3(0, 180 - arg_2_2, 0)

def var_0_0.Battle.TorAlert.Dispose(arg_3_0):
	LeanTween.cancel(arg_3_0._alertGO)
	var_0_0.Battle.BattleResourceManager.GetInstance().DestroyOb(arg_3_0._alertGO)
