ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleEnvironmentWave = class("BattleEnvironmentWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleEnvironmentWave.__name = "BattleEnvironmentWave"

local var_0_1 = var_0_0.Battle.BattleEnvironmentWave

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0._spawnTimerList = {}
end

function var_0_1.SetWaveData(arg_2_0, arg_2_1)
	var_0_1.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._sapwnData = arg_2_1.spawn or {}
	arg_2_0._environWarning = arg_2_1.warning
end

function var_0_1.DoWave(arg_3_0)
	var_0_1.super.DoWave(arg_3_0)

	for iter_3_0, iter_3_1 in ipairs(arg_3_0._sapwnData) do
		if iter_3_1.delay and iter_3_1.delay > 0 then
			arg_3_0:spawnTimer(iter_3_1)
		else
			arg_3_0:doSpawn(iter_3_1)
		end
	end

	if arg_3_0._environWarning then
		var_0_0.Battle.BattleDataProxy.GetInstance():DispatchWarning(true)
	end
end

function var_0_1.doSpawn(arg_4_0, arg_4_1)
	local var_4_0 = var_0_0.Battle.BattleDataProxy.GetInstance():SpawnEnvironment(arg_4_1)

	local function var_4_1()
		arg_4_0:doPass()
	end

	var_4_0:ConfigCallback(var_4_1)
end

function var_0_1.doPass(arg_6_0)
	if arg_6_0._environWarning then
		var_0_0.Battle.BattleDataProxy.GetInstance():DispatchWarning(false)
	end
end

function var_0_1.spawnTimer(arg_7_0, arg_7_1)
	local var_7_0
	local var_7_1 = arg_7_1.delay

	local function var_7_2()
		arg_7_0:doSpawn(arg_7_1)
		pg.TimeMgr.GetInstance():RemoveBattleTimer(var_7_0)
	end

	var_7_0 = pg.TimeMgr.GetInstance():AddBattleTimer("", 1, var_7_1, var_7_2, true)
	arg_7_0._spawnTimerList[var_7_0] = true
end

function var_0_1.Dispose(arg_9_0)
	for iter_9_0, iter_9_1 in pairs(arg_9_0._spawnTimerList) do
		pg.TimeMgr.GetInstance():RemoveBattleTimer(iter_9_0)
	end

	arg_9_0._spawnTimerList = nil
end
