ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst

var_0_0.Battle.BattleWallData = class("BattleWallData")
var_0_0.Battle.BattleWallData.__name = "BattleWallData"

local var_0_2 = var_0_0.Battle.BattleWallData

var_0_2.CLD_OBJ_TYPE_BULLET = 1
var_0_2.CLD_OBJ_TYPE_SHIP = 2

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5):
	arg_1_0._id = arg_1_1
	arg_1_0._host = arg_1_2
	arg_1_0._cldFun = arg_1_3
	arg_1_0._cldBox = arg_1_4
	arg_1_0._cldOffset = arg_1_5

	arg_1_0.InitCldComponent()

def var_0_2.InitCldComponent(arg_2_0):
	local var_2_0 = arg_2_0._cldBox
	local var_2_1 = arg_2_0._cldOffset

	if var_2_0.range:
		arg_2_0._cldComponent = var_0_0.Battle.BattleColumnCldComponent.New(var_2_0.range, 5, var_2_1[1], var_2_1[3])
	else
		arg_2_0._cldComponent = var_0_0.Battle.BattleCubeCldComponent.New(var_2_0[1], var_2_0[2], var_2_0[3], var_2_1[1], var_2_1[3])

	local var_2_2 = {
		type = var_0_1.CldType.WALL,
		UID = arg_2_0.GetUniqueID(),
		func = arg_2_0.GetCldFunc()
	}

	arg_2_0._cldComponent.SetCldData(var_2_2)
	arg_2_0._cldComponent.SetActive(True)
	arg_2_0.SetCldObjType()

def var_0_2.IsActive(arg_3_0):
	return arg_3_0._host.IsWallActive()

def var_0_2.DeactiveCldBox(arg_4_0):
	arg_4_0._cldComponent.SetActive(False)

def var_0_2.GetCldBox(arg_5_0):
	return arg_5_0._cldComponent.GetCldBox(arg_5_0.GetPosition())

def var_0_2.GetCldData(arg_6_0):
	return arg_6_0._cldComponent.GetCldData()

def var_0_2.GetBoxSize(arg_7_0):
	return arg_7_0._cldComponent.GetCldBoxSize()

def var_0_2.GetHost(arg_8_0):
	return arg_8_0._host

def var_0_2.GetIFF(arg_9_0):
	return arg_9_0.GetHost().GetIFF()

def var_0_2.GetPosition(arg_10_0):
	return arg_10_0.GetHost().GetPosition()

def var_0_2.GetUniqueID(arg_11_0):
	return arg_11_0._id

def var_0_2.GetCldFunc(arg_12_0):
	return arg_12_0._cldFun

def var_0_2.SetCldObjType(arg_13_0, arg_13_1):
	arg_13_0._cldObjType = arg_13_1 or var_0_2.CLD_OBJ_TYPE_BULLET

def var_0_2.GetCldObjType(arg_14_0):
	return arg_14_0._cldObjType
