ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = class("BattleLastingAOEData", var_0_0.Battle.BattleAOEData)

var_0_0.Battle.BattleLastingAOEData = var_0_2
var_0_2.__name = "BattleLastingAOEData"

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5, arg_1_6):
	var_0_2.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_5)

	arg_1_0._exitCldFunc = arg_1_4

	if arg_1_6:
		arg_1_0.Settle = arg_1_0.frequentlySettle

	arg_1_0._handledList = {}

def var_0_2.Dispose(arg_2_0):
	for iter_2_0, iter_2_1 in pairs(arg_2_0._handledList):
		arg_2_0._exitCldFunc(iter_2_0)

		arg_2_0._handledList[iter_2_0] = None

	arg_2_0._exitCldFunc = None
	arg_2_0._handledList = None

	var_0_2.super.Dispose(arg_2_0)

def var_0_2.Settle(arg_3_0):
	local var_3_0 = {}
	local var_3_1 = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0._cldObjList):
		var_3_1[iter_3_1.UID] = True

		if not arg_3_0._handledList[iter_3_1]:
			var_3_0[#var_3_0 + 1] = iter_3_1
			arg_3_0._handledList[iter_3_1] = True

	arg_3_0.SortCldObjList(var_3_0)
	arg_3_0._cldComponent.GetCldData().func(var_3_0, obj)

	for iter_3_2, iter_3_3 in pairs(arg_3_0._handledList):
		if not var_3_1[iter_3_2.UID] or iter_3_2.ImmuneCLD == True:
			arg_3_0._exitCldFunc(iter_3_2)

			arg_3_0._handledList[iter_3_2] = None

def var_0_2.frequentlySettle(arg_4_0):
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._cldObjList):
		var_4_0[iter_4_1.UID] = True

		if not arg_4_0._handledList[iter_4_1]:
			arg_4_0._handledList[iter_4_1] = True

	for iter_4_2, iter_4_3 in pairs(arg_4_0._handledList):
		if not var_4_0[iter_4_2.UID]:
			arg_4_0._exitCldFunc(iter_4_2)

			arg_4_0._handledList[iter_4_2] = None

	arg_4_0.SortCldObjList(arg_4_0._cldObjList)
	arg_4_0._cldComponent.GetCldData().func(arg_4_0._cldObjList)

def var_0_2.ForceExit(arg_5_0, arg_5_1):
	local var_5_0

	for iter_5_0, iter_5_1 in pairs(arg_5_0._handledList):
		if iter_5_0.UID == arg_5_1:
			var_5_0 = iter_5_0

			break

	if var_5_0:
		arg_5_0._exitCldFunc(var_5_0)

		arg_5_0._handledList[var_5_0] = None
