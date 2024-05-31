local var_0_0 = class("SVRealmPanel", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "SVRealmPanel"

def var_0_0.OnLoaded(arg_2_0):
	return

def var_0_0.OnInit(arg_3_0):
	local var_3_0 = arg_3_0._tf.Find("panel")

	arg_3_0.btnBLHX = var_3_0.Find("blhx")
	arg_3_0.btnCSZZ = var_3_0.Find("cszz")

	setActive(arg_3_0.btnBLHX, True)
	setActive(arg_3_0.btnCSZZ, True)
	onButton(arg_3_0, arg_3_0.btnBLHX, function()
		arg_3_0.PlayAnim(arg_3_0.btnBLHX, function()
			arg_3_0.Hide()
			arg_3_0.onConfirm(1)), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.btnCSZZ, function()
		arg_3_0.PlayAnim(arg_3_0.btnCSZZ, function()
			arg_3_0.Hide()
			arg_3_0.onConfirm(2)))

def var_0_0.OnDestroy(arg_8_0):
	return

def var_0_0.Show(arg_9_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_9_0._tf)
	setActive(arg_9_0._tf, True)

def var_0_0.Hide(arg_10_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_10_0._tf, arg_10_0._parentTf)
	setActive(arg_10_0._tf, False)

def var_0_0.Setup(arg_11_0, arg_11_1):
	arg_11_0.onConfirm = arg_11_1

def var_0_0.PlayAnim(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = arg_12_1.Find("bg")

	setActive(var_12_0, True)
	LeanTween.value(go(var_12_0), 1, 1.2, 0.2).setOnUpdate(System.Action_float(function(arg_13_0)
		var_12_0.localScale = Vector3(arg_13_0, arg_13_0, 1))).setOnComplete(System.Action(function()
		setActive(var_12_0, False)

		var_12_0.localScale = Vector3(1, 1, 1)

		arg_12_2()))
	LeanTween.value(go(var_12_0), 1, 0.7, 0.2)

return var_0_0
