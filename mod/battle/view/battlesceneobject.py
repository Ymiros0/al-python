ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSceneObject")

var_0_0.Battle.BattleSceneObject = var_0_1
var_0_1.__name = "BattleSceneObject"

def var_0_1.Ctor(arg_1_0):
	return

def var_0_1.GetGO(arg_2_0):
	return arg_2_0._go

def var_0_1.GetTf(arg_3_0):
	return arg_3_0._tf

def var_0_1.SetGO(arg_4_0, arg_4_1):
	arg_4_0._go = arg_4_1
	arg_4_0._tf = arg_4_1.transform

def var_0_1.GetCldBoxSize(arg_5_0):
	assert(False, arg_5_0.__name .. ".GetCldBoxSize. this function should be override!!!")

def var_0_1.GetCldBox(arg_6_0):
	assert(False, arg_6_0.__name .. ".GetCldBox. this function should be override!!!")

def var_0_1.GetCldData(arg_7_0):
	assert(False, arg_7_0.__name .. ".GetCldData. this function should be override!!!")

def var_0_1.GetGOPosition(arg_8_0):
	return arg_8_0._tf.localPosition

def var_0_1.CameraOrthogonal(arg_9_0, arg_9_1):
	arg_9_0._tf.localRotation = arg_9_1.transform.localRotation

def var_0_1.Dispose(arg_10_0):
	arg_10_0._tf = None

	var_0_0.Battle.BattleResourceManager.GetInstance().DestroyOb(arg_10_0._go)

	arg_10_0._go = None
