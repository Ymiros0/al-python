local var_0_0 = class("RedDotNode")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	assert(not IsNil(arg_1_1))

	arg_1_0.gameObject = arg_1_1
	arg_1_0.types = arg_1_2

def var_0_0.GetName(arg_2_0):
	return arg_2_0.gameObject.transform.parent.gameObject.name

def var_0_0.Init(arg_3_0):
	return

def var_0_0.RefreshSelf(arg_4_0):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.types):
		pg.RedDotMgr.GetInstance().NotifyAll(iter_4_1)

def var_0_0.GetTypes(arg_5_0):
	return arg_5_0.types

def var_0_0.SetData(arg_6_0, arg_6_1):
	if IsNil(arg_6_0.gameObject):
		return

	setActive(arg_6_0.gameObject, arg_6_1)

def var_0_0.Remove(arg_7_0):
	return

return var_0_0
