from luatable import table

from View import View
from Framework.puremvc.patterns.observer.Observer import Observer
class Controller:
	def Ctor(self, arg_1_1):
		if self.instanceMap[arg_1_1] != None:
			raise BaseException(Controller.MULTITON_MSG)

		self.multitonKey = arg_1_1
		Controller.instanceMap[self.multitonKey] = self
		self.commandMap = table()

		self.initializeController()

	def initializeController(self):
		self.view = View.getInstance(self.multitonKey)

	def getInstance(self, instance_id):
		if instance_id == None:
			return None

		if Controller.instanceMap[instance_id] == None:
			return Controller(instance_id)
		else:
			return Controller.instanceMap[instance_id]

	def executeCommand(self, command):
		var_4_0 = self.commandMap[command.getName()]

		if var_4_0 == None:
			return

		var_4_1 = var_4_0()

		var_4_1.initializeNotifier(self.multitonKey)
		var_4_1.execute(command)

	def registerCommand(self, arg_5_1, arg_5_2):
		if self.commandMap[arg_5_1] == None:
			self.view.registerObserver(arg_5_1, Observer(self.executeCommand, self))

		self.commandMap[arg_5_1] = arg_5_2

	def hasCommand(self, arg_6_1):
		return self.commandMap[arg_6_1] != None

	def removeCommand(self, arg_7_1):
		if self.hasCommand(arg_7_1):
			self.view.removeObserver(arg_7_1, self)

			self.commandMap[arg_7_1] = None

	def removeController(self,instance_id):
		Controller.instanceMap[instance_id] = None

	instanceMap = table()
	MULTITON_MSG = "controller key for this Multiton key already constructed"