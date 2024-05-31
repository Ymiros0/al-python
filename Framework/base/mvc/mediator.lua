ys = ys or {}

local var_0_0 = ys

var_0_0.MVC = var_0_0.MVC or {}
var_0_0.MVC.Mediator = class("MVC.Mediator")
var_0_0.MVC.Mediator.__name = "MVC.Mediator"

function var_0_0.MVC.Mediator.Ctor(arg_1_0)
	return
end

function var_0_0.MVC.Mediator.Initialize(arg_2_0)
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_2_0)
	var_0_0.EventListener.AttachEventListener(arg_2_0)
end

function var_0_0.MVC.Mediator.Update(arg_3_0)
	return
end

function var_0_0.MVC.Mediator.UpdatePause(arg_4_0)
	return
end

function var_0_0.MVC.Mediator.Dispose(arg_5_0)
	var_0_0.EventListener.DetachEventListener(arg_5_0)
	var_0_0.EventDispatcher.DetachEventDispatcher(arg_5_0)
end

function var_0_0.MVC.Mediator.GetState(arg_6_0)
	return arg_6_0._state
end
