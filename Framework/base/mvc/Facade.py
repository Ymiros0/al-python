from luatable import table

from mgr.TimeMgr import TimeMgr #!
from mod.battle.data.BattleDataProxy import BattleDataProxy
from mod.battle.data import BattleConfig
from mod.battle.view.BattleSceneMediator import BattleSceneMediator #!

class Facade:
	__name = "MVC.Facade"

	def __new__(cls):
		it = cls.__dict__.get("__it__")
		if it is not None:
			return it
		cls.__it__ = it = object.__new__(cls)
		return it
	
	def __init__(self):
		self.Initialize()

	def AddDataProxy(self, dataProxy):
		assert dataProxy.__name is not None and type(dataProxy.__name) == str, self.__name + ".AddDataProxy. dataProxy.__name expected a string value"
		assert self._proxyList[dataProxy.__name] == None, self.__name + ".AddDataProxy. same dataProxy exist"

		dataProxy._state = self

		dataProxy.ActiveProxy()

		self._proxyList[dataProxy.__name] = dataProxy

		return dataProxy

	def AddMediator(self, mediator):
		assert mediator.__name is not None and type(mediator.__name) == str, self.__name + ".AddMediator. mediator.__name expected a string value"

		assert self._mediatorList[mediator.__name] == None, self.__name + ".AddMediator. same mediator exist"

		self._mediatorList[mediator.__name] = mediator
		mediator._state = self

		mediator.Initialize()

		return mediator

	def AddCommand(self, command):
		assert command.__name is not None and type(command.__name) == str, self.__name + ".AddCommand. command.__name expected a string value"

		assert self._commandList[command.__name] == None, self.__name + ".AddCommand. same command exist"

		self._commandList[command.__name] = command
		command._state = self

		command.Initialize()

		return command

	def GetProxyByName(self, proxyName):
		assert type(proxyName) == str, self.__name + ".GetProxyByName. expect a string value"

		return self._proxyList[proxyName]

	def GetMediatorByName(self, mediatorName):
		assert type(mediatorName) == str, self.__name + ".GetMediatorByName. expect a string value"

		return self._mediatorList[mediatorName]

	def GetCommandByName(self, commandName):
		assert type(commandName) == str, self.__name + ".GetCommandByName. expect a string value"

		return self._commandList[commandName]

	def RemoveMediator(self, mediatorName):
		if type(mediatorName) == str:
			mediatorName = self._mediatorList[mediatorName]

		assert mediatorName != None, self.__name + ".RemoveMediator. try to remove a None mediator"
		mediatorName.Dispose()

		self._mediatorList[mediatorName.__name] = None

	def RemoveCommand(self, commandName):
		if type(commandName) == str:
			commandName = self._commandList[commandName]

		assert commandName != None, self.__name + ".RemoveCommand. try to remove a None command"
		commandName.Dispose()

		self._commandList[commandName.__name] = None

	def RemoveProxy(self, proxyName):
		if type(proxyName) == str:
			proxyName = self._proxyList[proxyName]

		assert proxyName != None, self.__name + ".RemoveProxy. try to remove a None proxy"
		proxyName.DeactiveProxy()

		self._proxyList[proxyName.__name] = None

	def Initialize(self):
		self._proxyList = table()
		self._commandList = table()
		self._mediatorList = table()

	def Active(self):
		if not self._isPause:
			return

		self._isPause = False

		TimeMgr.GetInstance().ResumeBattleTimer()

	def Deactive(self):
		if self._isPause:
			return

		self._isPause = True

		TimeMgr.GetInstance().PauseBattleTimer()

	def ActiveEscape(self):
		self._escapeAITimer = TimeMgr.GetInstance().AddTimer("escapeTimer", 0, BattleConfig.viewInterval, lambda: self.escapeUpdate())

	def DeactiveEscape(self):
		TimeMgr.GetInstance().RemoveTimer(self._escapeAITimer)

	def RemoveAllTimer(self):
		TimeMgr.GetInstance().RemoveAllBattleTimer()

		self._calcTimer = None
		self._AITimer = None

	def ResetTimer(self):
		timer = TimeMgr.GetInstance()

		timer.ResetCombatTime()
		timer.RemoveBattleTimer(self._calcTimer)
		timer.RemoveBattleTimer(self._AITimer)

		self._calcTimer = timer.AddBattleTimer("calcTimer", -1, BattleConfig.calcInterval, lambda: self.calcUpdate())

	def ActiveAutoComponentTimer(self):
		self._AITimer = TimeMgr.GetInstance().AddBattleTimer("aiTimer", -1, BattleConfig.AIInterval, lambda: self.aiUpdate())

	def calcUpdate(self):
		time = TimeMgr.GetInstance().GetCombatTime()

		for i in self._proxyList.values():
			i.Update(time)

		for i in self._commandList.values():
			i.Update(time)

	def aiUpdate(self):
		self.GetProxyByName(BattleDataProxy.__name).UpdateAutoComponent(TimeMgr.GetInstance().GetCombatTime())

	def escapeUpdate(self):
		battleDataProxy = self.GetProxyByName(BattleDataProxy.__name)
		time = TimeMgr.GetInstance().GetCombatTime()

		battleDataProxy.UpdateEscapeOnly(time)
		self.GetMediatorByName(BattleSceneMediator.__name).UpdateEscapeOnly(time)
