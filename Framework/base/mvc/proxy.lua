ys = ys or {}

local var_0_0 = ys

var_0_0.MVC = var_0_0.MVC or {}
var_0_0.MVC.Proxy = singletonClass("MVC.Proxy")
var_0_0.MVC.Proxy.__name = "MVC.Proxy"

function var_0_0.MVC.Proxy.Ctor(arg_1_0)
	return
end

function var_0_0.MVC.Proxy.ActiveProxy(arg_2_0)
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_2_0)
end

function var_0_0.MVC.Proxy.DeactiveProxy(arg_3_0)
	var_0_0.EventDispatcher.DetachEventDispatcher(arg_3_0)
end
