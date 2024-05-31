ys = ys or {}

local ys_local = ys

ys_local.MVC = ys_local.MVC or {}
ys_local.MVC.Command = class("MVC.Command")
ys_local.MVC.Command.__name = "MVC.Command"

function ys_local.MVC.Command.Ctor(self)
	return
end

function ys_local.MVC.Command.Initialize(self)
	ys_local.EventDispatcher.AttachEventDispatcher(self)
	ys_local.EventListener.AttachEventListener(self)
end

function ys_local.MVC.Command.Update(self)
	return
end

function ys_local.MVC.Command.Dispose(self)
	ys_local.EventListener.DetachEventListener(self)
	ys_local.EventDispatcher.DetachEventDispatcher(self)
end

function ys_local.MVC.Command.GetState(self)
	return self._state
end
