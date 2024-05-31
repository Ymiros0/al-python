ys = ys or {}

ys_local = ys

class Proxy:
	__name = "MVC.Proxy"

	def __new__(cls):
		it = cls.__dict__.get("__it__")
		if it is not None:
			return it
		cls.__it__ = it = object.__new__(cls)
		return it

	def ActiveProxy(self):
		ys_local.EventDispatcher.AttachEventDispatcher(self)

	def DeactiveProxy(self):
		ys_local.EventDispatcher.DetachEventDispatcher(self)
