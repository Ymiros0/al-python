local var_0_0 = class("PlayerVitaeBaseCard")
local var_0_1 = 160
local var_0_2 = 25

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.event = arg_1_2

	pg.DelegateInfo.New(arg_1_0)
	arg_1_0.Init(arg_1_1)

def var_0_0.Init(arg_2_0, arg_2_1):
	arg_2_0._go = arg_2_1
	arg_2_0._tf = arg_2_1.transform
	arg_2_0.width = arg_2_0._tf.sizeDelta.x
	arg_2_0.mask = arg_2_0._tf.Find("mask")

	arg_2_0.OnInit()

def var_0_0.UpdatePosition(arg_3_0, arg_3_1):
	local var_3_0 = var_0_1 + (arg_3_0.width + var_0_2) * (arg_3_1 - 1)

	arg_3_0._tf.anchoredPosition3D = Vector3(var_3_0, 0, 0)

	arg_3_0._tf.SetSiblingIndex(arg_3_1 - 1)

def var_0_0.Update(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4, arg_4_5):
	arg_4_0.OnUpdate(arg_4_1, arg_4_2, arg_4_3, arg_4_4, arg_4_5)
	arg_4_0.UpdatePosition(arg_4_1)

def var_0_0.Enable(arg_5_0):
	setActive(arg_5_0._tf, True)

def var_0_0.Disable(arg_6_0):
	setActive(arg_6_0._tf, False)

def var_0_0.Clone(arg_7_0):
	local var_7_0 = cloneTplTo(arg_7_0._go, arg_7_0._go.parent)

	return _G[arg_7_0.__cname].New(var_7_0, arg_7_0.event)

def var_0_0.emit(arg_8_0, ...):
	if arg_8_0.event:
		arg_8_0.event.emit(...)

def var_0_0.Dispose(arg_9_0):
	pg.DelegateInfo.Dispose(arg_9_0)
	arg_9_0.OnDispose()

def var_0_0.OnInit(arg_10_0):
	return

def var_0_0.OnUpdate(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4, arg_11_5):
	return

def var_0_0.OnDispose(arg_12_0):
	return

return var_0_0
