from luatable import table, pairs

from Framework.puremvc.patterns.observer.Observer import Observer

class View:
	def __init__(self, instance_id):
		if View.instanceMap[instance_id] != None:
			raise BaseException(View.MULTITON_MSG)

		self.multitonKey = instance_id
		View.instanceMap[self.multitonKey] = self
		self.mediatorMap = table()
		self.observerMap = table()

		self.initializeView()

	def initializeView(arg_2_0):
		return

	def getInstance(instance_id):
		if instance_id == None:
			return None

		if View.instanceMap[instance_id] == None:
			return View(instance_id)
		else:
			return View.instanceMap[instance_id]

	def registerObserver(self, arg_4_1, arg_4_2):
		if self.observerMap[arg_4_1] != None:
			table.insert(self.observerMap[arg_4_1], arg_4_2)
		else:
			if arg_4_1 == None:
				print("debug.traceback()") #????

			self.observerMap[arg_4_1] = {
				arg_4_2
			}

	def notifyObservers(self, arg_5_1):
		var_5_0 = self.observerMap[arg_5_1.getName()]

		if var_5_0 != None:
			var_5_1 = table.shallowCopy(var_5_0)

			for iter_5_0, iter_5_1 in pairs(var_5_1):
				if table.contains(var_5_0, iter_5_1):
					iter_5_1.notifyObserver(arg_5_1)


	def removeObserver(self, arg_6_1, arg_6_2):
		var_6_0 = self.observerMap[arg_6_1]

		for iter_6_0, iter_6_1 in pairs(var_6_0):
			if iter_6_1.compareNotifyContext(arg_6_2):
				table.remove(var_6_0, iter_6_0)

				break

		if len(var_6_0) == 0:
			self.observerMap[arg_6_1] = None

	def registerMediator(self, arg_7_1):
		if self.mediatorMap[arg_7_1.getMediatorName()] != None:
			return

		arg_7_1.initializeNotifier(self.multitonKey)

		self.mediatorMap[arg_7_1.getMediatorName()] = arg_7_1

		var_7_0 = arg_7_1.listNotificationInterests()

		if len(var_7_0) > 0:
			var_7_1 = Observer(arg_7_1.handleNotification, arg_7_1)

			for iter_7_0, iter_7_1 in pairs(var_7_0):
				self.registerObserver(iter_7_1, var_7_1)

		arg_7_1.onRegister()

	def retrieveMediator(self, arg_8_1):
		return self.mediatorMap[arg_8_1]

	def removeMediator(self, arg_9_1):
		var_9_0 = self.mediatorMap[arg_9_1]

		if var_9_0 != None:
			var_9_1 = var_9_0.listNotificationInterests()

			for iter_9_0, iter_9_1 in pairs(var_9_1):
				self.removeObserver(iter_9_1, var_9_0)

			self.mediatorMap[arg_9_1] = None

			var_9_0.onRemove()

		return var_9_0

	def hasMediator(self, arg_10_1):
		return self.mediatorMap[arg_10_1] != None

	def removeView(instance_id):
		View.instanceMap[instance_id] = None

	instanceMap = table()
	MULTITON_MSG = "View instance for this Multiton key already constructed!"

	