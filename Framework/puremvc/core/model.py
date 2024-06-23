from luatable import table

class Model:

	def __init__(arg_1_0, arg_1_1):
		if Model.instanceMap[arg_1_1]:
			raise BaseException(Model.MULTITON_MSG)

		arg_1_0.multitonKey = arg_1_1
		Model.instanceMap[arg_1_1] = arg_1_0
		arg_1_0.proxyMap = table()

		arg_1_0.initializeModel()

	def initializeModel(self):
		return

	def getInstance(instance_id):
		if instance_id == None:
			return None

		if Model.instanceMap[instance_id] == None:
			return Model(instance_id)
		else:
			return Model.instanceMap[instance_id]

	def registerProxy(self, proxy):
		proxy.initializeNotifier(self.multitonKey)

		self.proxyMap[proxy.getProxyName()] = proxy

		proxy.onRegister()

	def retrieveProxy(self, arg_5_1):
		return self.proxyMap[arg_5_1]

	def hasProxy(self, arg_6_1):
		return self.proxyMap[arg_6_1] != None

	def removeProxy(self, proxy_name):
		proxy = self.proxyMap[proxy_name]

		if proxy != None:
			self.proxyMap[proxy_name] = None

			proxy.onRemove()

		return proxy

	def removeModel(instance_id):
		Model.instanceMap[instance_id] = None

	instanceMap = table()
	MULTITON_MSG = "Model instance for this Multiton key already constructed!"

