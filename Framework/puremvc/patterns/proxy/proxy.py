from Framework.puremvc.patterns.observer.Notifier import Notifier

class Proxy(Notifier):
	def __init__(self, arg_1_1, arg_1_2):
		if arg_1_1 != None:
			self.setData(arg_1_1)

		self.proxyName = arg_1_2 or self.__cname or Proxy.NAME

	NAME = "Proxy"

	def getProxyName(arg_2_0):
		return arg_2_0.proxyName

	def setData(arg_3_0, arg_3_1):
		arg_3_0.data = arg_3_1

	def getData(arg_4_0):
		return arg_4_0.data

	def onRegister(arg_5_0):
		return

	def onRemove(arg_6_0):
		return
