ys = ys or {}

local ys_local = ys
local pg_local = pg

ys_local.MVC = ys_local.MVC or {}
ys_local.MVC.Facade = singletonClass("MVC.Facade")
ys_local.MVC.Facade.__name = "MVC.Facade"

function ys_local.MVC.Facade.Ctor(self)
	self:Initialize()
end

function ys_local.MVC.Facade.AddDataProxy(self, dataProxy)
	assert(dataProxy.__name ~= nil and type(dataProxy.__name) == "string", self.__name .. ".AddDataProxy: dataProxy.__name expected a string value")
	assert(self._proxyList[dataProxy.__name] == nil, self.__name .. ".AddDataProxy: same dataProxy exist")

	dataProxy._state = self

	dataProxy:ActiveProxy()

	self._proxyList[dataProxy.__name] = dataProxy

	return dataProxy
end

function ys_local.MVC.Facade.AddMediator(self, mediator)
	if mediator.__name == nil or type(mediator.__name) ~= "string" then
		assert(false, self.__name .. ".AddMediator: mediator.__name expected a string value")
	end

	assert(self._mediatorList[mediator.__name] == nil, self.__name .. ".AddMediator: same mediator exist")

	self._mediatorList[mediator.__name] = mediator
	mediator._state = self

	mediator:Initialize()

	return mediator
end

function ys_local.MVC.Facade.AddCommand(self, command)
	if command.__name == nil or type(command.__name) ~= "string" then
		assert(false, self.__name .. ".AddCommand: command.__name expected a string value")
	end

	assert(self._commandList[command.__name] == nil, self.__name .. ".AddCommand: same command exist")

	self._commandList[command.__name] = command
	command._state = self

	command:Initialize()

	return command
end

function ys_local.MVC.Facade.GetProxyByName(self, proxyName)
	assert(type(proxyName) == "string", self.__name .. ".GetProxyByName: expect a string value")

	return self._proxyList[proxyName]
end

function ys_local.MVC.Facade.GetMediatorByName(self, mediatorName)
	assert(type(mediatorName) == "string", self.__name .. ".GetMediatorByName: expect a string value")

	return self._mediatorList[mediatorName]
end

function ys_local.MVC.Facade.GetCommandByName(self, commandName)
	assert(type(commandName) == "string", self.__name .. ".GetCommandByName: expect a string value")

	return self._commandList[commandName]
end

function ys_local.MVC.Facade.RemoveMediator(self, mediatorName)
	if type(mediatorName) == "string" then
		mediatorName = self._mediatorList[mediatorName]
	end

	assert(mediatorName ~= nil, self.__name .. ".RemoveMediator: try to remove a nil mediator")
	mediatorName:Dispose()

	self._mediatorList[mediatorName.__name] = nil
end

function ys_local.MVC.Facade.RemoveCommand(self, commandName)
	if type(commandName) == "string" then
		commandName = self._commandList[commandName]
	end

	assert(commandName ~= nil, self.__name .. ".RemoveCommand: try to remove a nil command")
	commandName:Dispose()

	self._commandList[commandName.__name] = nil
end

function ys_local.MVC.Facade.RemoveProxy(self, proxyName)
	if type(proxyName) == "string" then
		proxyName = self._proxyList[proxyName]
	end

	assert(proxyName ~= nil, self.__name .. ".RemoveProxy: try to remove a nil proxy")
	proxyName:DeactiveProxy()

	self._proxyList[proxyName.__name] = nil
end

function ys_local.MVC.Facade.Initialize(self)
	self._proxyList = {}
	self._commandList = {}
	self._mediatorList = {}
end

function ys_local.MVC.Facade.Active(self)
	if not self._isPause then
		return
	end

	self._isPause = false

	pg_local.TimeMgr.GetInstance():ResumeBattleTimer()
end

function ys_local.MVC.Facade.Deactive(self)
	if self._isPause then
		return
	end

	self._isPause = true

	pg_local.TimeMgr.GetInstance():PauseBattleTimer()
end

function ys_local.MVC.Facade.ActiveEscape(self)
	self._escapeAITimer = pg_local.TimeMgr.GetInstance():AddTimer("escapeTimer", 0, ys_local.Battle.BattleConfig.viewInterval, function()
		self:escapeUpdate()
	end)
end

function ys_local.MVC.Facade.DeactiveEscape(self)
	pg_local.TimeMgr.GetInstance():RemoveTimer(self._escapeAITimer)
end

function ys_local.MVC.Facade.RemoveAllTimer(self)
	pg_local.TimeMgr.GetInstance():RemoveAllBattleTimer()

	self._calcTimer = nil
	self._AITimer = nil
end

function ys_local.MVC.Facade.ResetTimer(self)
	local var_18_0 = pg_local.TimeMgr.GetInstance()

	var_18_0:ResetCombatTime()
	var_18_0:RemoveBattleTimer(self._calcTimer)
	var_18_0:RemoveBattleTimer(self._AITimer)

	self._calcTimer = var_18_0:AddBattleTimer("calcTimer", -1, ys_local.Battle.BattleConfig.calcInterval, function()
		self:calcUpdate()
	end)
end

function ys_local.MVC.Facade.ActiveAutoComponentTimer(self)
	self._AITimer = pg_local.TimeMgr.GetInstance():AddBattleTimer("aiTimer", -1, ys_local.Battle.BattleConfig.AIInterval, function()
		self:aiUpdate()
	end)
end

function ys_local.MVC.Facade.calcUpdate(self)
	local time = pg_local.TimeMgr.GetInstance():GetCombatTime()

	for iter_22_0, iter_22_1 in pairs(self._proxyList) do
		iter_22_1:Update(time)
	end

	for iter_22_2, iter_22_3 in pairs(self._commandList) do
		iter_22_3:Update(time)
	end
end

function ys_local.MVC.Facade.aiUpdate(self)
	self:GetProxyByName(ys_local.Battle.BattleDataProxy.__name):UpdateAutoComponent(pg_local.TimeMgr.GetInstance():GetCombatTime())
end

function ys_local.MVC.Facade.escapeUpdate(self)
	local battleDataProxy = self:GetProxyByName(ys_local.Battle.BattleDataProxy.__name)
	local time = pg_local.TimeMgr.GetInstance():GetCombatTime()

	battleDataProxy:UpdateEscapeOnly(time)
	self:GetMediatorByName(ys_local.Battle.BattleSceneMediator.__name):UpdateEscapeOnly(time)
end
