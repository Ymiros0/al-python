local var_0_0 = class("NewNavalTacticsBaseCard")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.event = arg_1_2
	arg_1_0._tf = arg_1_1
	arg_1_0._go = arg_1_1.gameObject

	arg_1_0.OnInit()

def var_0_0.emit(arg_2_0, ...):
	if arg_2_0.event:
		arg_2_0.event.emit(...)

def var_0_0.UpdatePosition(arg_3_0, arg_3_1):
	local var_3_0 = -493
	local var_3_1 = 0
	local var_3_2 = arg_3_0._tf.sizeDelta.x
	local var_3_3 = arg_3_0._tf.anchoredPosition3D
	local var_3_4 = var_3_0 + (arg_3_1 - 1) * (var_3_2 + var_3_1)

	arg_3_0._tf.anchoredPosition3D = Vector3(var_3_4, var_3_3.y, 0)

def var_0_0.Update(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0.index = arg_4_1

	arg_4_0.UpdatePosition(arg_4_1)
	arg_4_0.OnUpdate(arg_4_2)

def var_0_0.Enable(arg_5_0):
	setActive(arg_5_0._go, True)

def var_0_0.Disable(arg_6_0):
	setActive(arg_6_0._go, False)

def var_0_0.Dispose(arg_7_0):
	pg.DelegateInfo.Dispose(arg_7_0)
	Object.Destroy(arg_7_0._go)
	arg_7_0.OnDispose()

def var_0_0.Clone(arg_8_0):
	local var_8_0 = Object.Instantiate(arg_8_0._go, arg_8_0._tf.parent)

	assert(var_8_0)

	return _G[arg_8_0.__cname].New(var_8_0.transform, arg_8_0.event)

def var_0_0.OnInit(arg_9_0):
	return

def var_0_0.OnUpdate(arg_10_0, arg_10_1):
	return

def var_0_0.OnDispose(arg_11_0):
	return

return var_0_0
