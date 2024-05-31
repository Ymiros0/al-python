ys = ys or {}

local var_0_0 = ys

var_0_0.Event = class("Event")
var_0_0.Event.__name = "Event"

def var_0_0.Event.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.ID = arg_1_1
	arg_1_0.Data = arg_1_2
	arg_1_0.Dispatcher = arg_1_3

return var_0_0.Event
