local var_0_0 = {}
local var_0_1 = System.Reflection.BindingFlags
local var_0_2 = bit.bor(var_0_1.Instance, var_0_1.Public, var_0_1.NonPublic, var_0_1.FlattenHierarchy, var_0_1.Static)

def var_0_0.RefCallStaticMethod(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	local var_1_0
	local var_1_1

	if arg_1_2:
		var_1_0 = tolua.gettypemethod(arg_1_0, arg_1_1, var_0_2, Type.DefaultBinder, arg_1_2, {})
		var_1_1 = var_1_0.Call(unpack(arg_1_3))
	else
		var_1_0 = tolua.gettypemethod(arg_1_0, arg_1_1, var_0_2)
		var_1_1 = var_1_0.Call()

	var_1_0.Destroy()

	return var_1_1

def var_0_0.RefCallMethod(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	local var_2_0
	local var_2_1

	if arg_2_3:
		var_2_0 = tolua.gettypemethod(arg_2_0, arg_2_1, var_0_2, Type.DefaultBinder, arg_2_3, {})
		var_2_1 = var_2_0.Call(arg_2_2, unpack(arg_2_4))
	else
		var_2_0 = tolua.gettypemethod(arg_2_0, arg_2_1, var_0_2)
		var_2_1 = var_2_0.Call(arg_2_2)

	var_2_0.Destroy()

	return var_2_1

def var_0_0.RefCallMethodEx(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	local var_3_0
	local var_3_1
	local var_3_2 = tolua.gettypemethod(arg_3_0, arg_3_1, arg_3_3)
	local var_3_3 = var_3_2.Call(arg_3_2, unpack(arg_3_4))

	var_3_2.Destroy()

	return var_3_3

def var_0_0.RefGetField(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = tolua.getfield(arg_4_0, arg_4_1, var_0_2)
	local var_4_1 = var_4_0.Get(arg_4_2)

	var_4_0.Destroy()

	return var_4_1

def var_0_0.RefSetField(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local var_5_0 = tolua.getfield(arg_5_0, arg_5_1, var_0_2)

	var_5_0.Set(arg_5_2, arg_5_3)
	var_5_0.Destroy()

def var_0_0.RefGetProperty(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = tolua.getproperty(arg_6_0, arg_6_1, var_0_2)
	local var_6_1 = var_6_0.Get(arg_6_2, null)

	var_6_0.Destroy()

	return var_6_1

def var_0_0.RefSetProperty(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	local var_7_0 = tolua.getproperty(arg_7_0, arg_7_1, var_0_2)

	var_7_0.Set(arg_7_2, arg_7_3, null)
	var_7_0.Destroy()

return var_0_0
