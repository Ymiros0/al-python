from Framework.puremvc.patterns.facade.Facade import Facade
class Notifier:
	def __new__(cls):
		return

	def sendNotification(self, arg_2_1, arg_2_2, arg_2_3):
		facade = self.getFacade()

		if facade != None:
			facade.sendNotification(arg_2_1, arg_2_2, arg_2_3)

	def initializeNotifier(self, key):
		self.multitonKey = key
		self.facade = self.getFacade()

	def getFacade(self):
		if self.multitonKey == None:
			raise ValueError(Notifier.MULTITON_MSG)

		return Facade.getInstance(self.multitonKey)

	MULTITON_MSG = "multitonKey for this Notifier not yet initialized!"