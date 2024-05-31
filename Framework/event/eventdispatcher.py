ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("EventDispatcher")

var_0_0.EventDispatcher = var_0_1
var_0_1.__name = "EventDispatcher"
var_0_1.FUNC_NAME_REGISTER = "RegisterEventListener"
var_0_1.FUNC_NAME_UNREGISTER = "UnregisterEventListener"
var_0_1.FUNC_NAME_DISPATCH = "DispatchEvent"

def var_0_1.AttachEventDispatcher(arg_1_0):
	var_0_1.New(arg_1_0)

def var_0_1.DetachEventDispatcher(arg_2_0):
	if arg_2_0._dispatcher_ == None:
		return

	arg_2_0._dispatcher_._Destory_()

	arg_2_0._dispatcher_ = None

def var_0_1.Ctor(arg_3_0, arg_3_1):
	arg_3_0._target_ = arg_3_1

	arg_3_0._Init_()

def var_0_1._Init_(arg_4_0):
	arg_4_0._listenerMap_ = {}
	arg_4_0._target_[var_0_1.FUNC_NAME_REGISTER] = var_0_1._RegisterEventListener_
	arg_4_0._target_[var_0_1.FUNC_NAME_UNREGISTER] = var_0_1._UnregisterEventListener_
	arg_4_0._target_[var_0_1.FUNC_NAME_DISPATCH] = var_0_1._DispatchEvent_
	arg_4_0._target_._dispatcher_ = arg_4_0

def var_0_1._Destory_(arg_5_0):
	arg_5_0._listenerMap_ = None
	arg_5_0._target_ = None

def var_0_1._DispatchEvent_(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0._dispatcher_

	arg_6_1.Dispatcher = arg_6_1.Dispatcher or var_6_0._target_

	local var_6_1 = arg_6_1.ID
	local var_6_2 = var_6_0._listenerMap_[var_6_1]

	if var_6_2:
		for iter_6_0, iter_6_1 in ipairs(var_6_2):
			iter_6_1._Handle_(arg_6_1)

def var_0_1._RegisterEventListener_(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	local var_7_0 = arg_7_0._dispatcher_

	assert(arg_7_1._eventListener_ != None, "EventDispatcher ERROR" .. arg_7_1.__cname)

	if var_7_0._listenerMap_[arg_7_2] == None:
		var_7_0._listenerMap_[arg_7_2] = {}

	local var_7_1 = var_7_0._listenerMap_[arg_7_2]

	var_7_1[#var_7_1 + 1] = arg_7_1._eventListener_

	arg_7_1._eventListener_._AddRoute_(arg_7_2, arg_7_0, arg_7_3)

def var_0_1._UnregisterEventListener_(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = arg_8_0._dispatcher_

	arg_8_1 = arg_8_1._eventListener_

	if var_8_0._listenerMap_[arg_8_2] == None:
		return

	local var_8_1 = var_8_0._listenerMap_[arg_8_2]

	arg_8_1._RemoveRoute_(arg_8_2, arg_8_0)

	for iter_8_0, iter_8_1 in ipairs(var_8_1):
		if iter_8_1 == arg_8_1:
			local var_8_2 = iter_8_0

			for iter_8_2 = #var_8_1, 1, -1:
				var_8_1[iter_8_2] = None

			var_8_1[#var_8_1] = None

			break

	if #var_8_1 == 0:
		var_8_0._listenerMap_[arg_8_2] = None
