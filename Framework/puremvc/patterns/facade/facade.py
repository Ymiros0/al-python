from luatable import table

from Framework.puremvc.core.Controller import Controller
from Framework.puremvc.core.Model import Model
from Framework.puremvc.core.View import View
from Framework.puremvc.patterns.observer.Notification import Notification

class Facade:
	def __init__(self, instance_id):
		if Facade.instanceMap[instance_id] != None:
			raise BaseException(Facade.MULTITON_MSG)

		self.initializeNotifier(instance_id)

		Facade.instanceMap[instance_id] = self

		self.initializeFacade()

	def initializeFacade(self):
		self.initializeModel()
		self.initializeController()
		self.initializeView()

	def getInstance(instance_id):
		if instance_id == None:
			return None

		if Facade.instanceMap[instance_id] == None:
			Facade.instanceMap[instance_id] = instance_id.New(instance_id)

		return Facade.instanceMap[instance_id]

	def initializeController(self):
		if self.controller != None:
			return

		self.controller = Controller.getInstance(self.multitonKey)

	def initializeModel(self):
		if self.model != None:
			return

		self.model = Model.getInstance(self.multitonKey)

	def initializeView(self):
		if self.view != None:
			return

		self.view = View.getInstance(self.multitonKey)

	def registerCommand(self, arg_7_1, arg_7_2):
		assert(arg_7_2)
		self.controller.registerCommand(arg_7_1, arg_7_2)

	def removeCommand(self, arg_8_1):
		self.controller.removeCommand(arg_8_1)

	def hasCommand(self, arg_9_1):
		return self.controller.hasCommand(arg_9_1)

	def registerProxy(self, arg_10_1):
		self.model.registerProxy(arg_10_1)

	def retrieveProxy(self, arg_11_1):
		return self.model.retrieveProxy(arg_11_1)

	def removeProxy(self, arg_12_1):
		var_12_0

		if self.model != None:
			var_12_0 = self.model.removeProxy(arg_12_1)

		return var_12_0

	def hasProxy(self, arg_13_1):
		return self.model.hasProxy(arg_13_1)

	def registerMediator(self, arg_14_1):
		if self.view != None:
			self.view.registerMediator(arg_14_1)

	def retrieveMediator(self, arg_15_1):
		return self.view.retrieveMediator(arg_15_1)

	def removeMediator(self, arg_16_1):
		var_16_0

		if self.view != None:
			var_16_0 = self.view.removeMediator(arg_16_1)

		return var_16_0

	def hasMediator(self, arg_17_1):
		return self.view.hasMediator(arg_17_1)

	def sendNotification(self, arg_18_1, arg_18_2, arg_18_3):
		self.notifyObservers(Notification.New(arg_18_1, arg_18_2, arg_18_3))

	def notifyObservers(self, arg_19_1):
		if self.view != None:
			self.view.notifyObservers(arg_19_1)

	def initializeNotifier(self, arg_20_1):
		self.multitonKey = arg_20_1

	def hasCore(instance_id):
		return Facade.instanceMap[instance_id] != None

	def removeCore(instance_id):
		if Facade.instanceMap[instance_id] == None:
			return

		Model.removeModel(instance_id)
		View.removeView(instance_id)
		Controller.removeController(instance_id)

		Facade.instanceMap[instance_id] = None

	instanceMap = table()
	MULTITON_MSG = "Facade instance for this Multiton instance_id already constructed!"