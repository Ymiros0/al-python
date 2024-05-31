ys = ys or {}

local var_0_0 = ys

var_0_0.EventListener = class("EventListener")
var_0_0.EventListener.__name = "EventListener"

def var_0_0.EventListener.AttachEventListener(arg_1_0):
	var_0_0.EventListener.New(arg_1_0)

def var_0_0.EventListener.DetachEventListener(arg_2_0):
	if arg_2_0._eventListener_ == None:
		return

	arg_2_0._eventListener_._Destory_()

	arg_2_0._eventListener_ = None

def var_0_0.EventListener.Ctor(arg_3_0, arg_3_1):
	arg_3_0._target_ = arg_3_1
	arg_3_0._target_._eventListener_ = arg_3_0
	arg_3_0._routeMap_ = {}

def var_0_0.EventListener._Destory_(arg_4_0):
	arg_4_0._routeMap_ = None
	arg_4_0._target_ = None

def var_0_0.EventListener._AddRoute_(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if arg_5_0._routeMap_[arg_5_1] == None:
		arg_5_0._routeMap_[arg_5_1] = {}

	arg_5_0._routeMap_[arg_5_1][arg_5_2] = arg_5_3

def var_0_0.EventListener._RemoveRoute_(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0._routeMap_[arg_6_1][arg_6_2] = None

def var_0_0.EventListener._Handle_(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0._target_

	arg_7_0._routeMap_[arg_7_1.ID][arg_7_1.Dispatcher](var_7_0, arg_7_1)
