import ys

ys_local = ys

ys_local.MVC = ys_local.MVC or {}
class Mediator:
	__name = "MVC.Mediator"

	def __init__(self):
		return

	def Initialize(self):
		ys_local.EventDispatcher.AttachEventDispatcher(self)
		ys_local.EventListener.AttachEventListener(self)

	def Update(self):
		return

	def UpdatePause(self):
		return

	def Dispose(self):
		ys_local.EventListener.DetachEventListener(self)
		ys_local.EventDispatcher.DetachEventDispatcher(self)

	def GetState(self):
		return self._state

ys_local.MVC.Mediator = Mediator