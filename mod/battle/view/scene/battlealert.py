ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleAlert = class("BattleAlert")
var_0_0.Battle.BattleAlert.__name = "BattleAlert"

def var_0_0.Battle.BattleAlert.Ctor(arg_1_0, arg_1_1):
	arg_1_0._alertGO = arg_1_1
	arg_1_0._alertTf = arg_1_1.transform
	arg_1_0._diskTf = arg_1_0._alertGO.transform.Find("Disk")

	arg_1_0.UpdateRate(0)
	arg_1_0._alertGO.SetActive(True)

def var_0_0.Battle.BattleAlert.SetPosition(arg_2_0, arg_2_1):
	arg_2_0._alertTf.localPosition = Vector3(arg_2_1.x, 0, arg_2_1.z)

def var_0_0.Battle.BattleAlert.Zoom(arg_3_0, arg_3_1):
	arg_3_0._alertTf.localScale = Vector3(arg_3_1 * 2, arg_3_1 * 2, 1)

def var_0_0.Battle.BattleAlert.UpdateRate(arg_4_0, arg_4_1):
	arg_4_0._diskTf.localScale = Vector3(arg_4_1, arg_4_1, 1)

def var_0_0.Battle.BattleAlert.Dispose(arg_5_0):
	Object.Destroy(arg_5_0._alertGO)
