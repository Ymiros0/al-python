ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.WaveTriggerType

var_0_0.Battle.BattleWaveInfo = class("BattleWaveInfo")
var_0_0.Battle.BattleWaveInfo.__name = "BattleWaveInfo"

local var_0_2 = var_0_0.Battle.BattleWaveInfo

var_0_2.LOGIC_AND = 0
var_0_2.LGOIC_OR = 1
var_0_2.STATE_DEACTIVE = "STATE_DEACTIVE"
var_0_2.STATE_ACTIVE = "STATE_ACTIVE"
var_0_2.STATE_PASS = "STATE_PASS"
var_0_2.STATE_FAIL = "STATE_FAIL"

def var_0_2.Ctor(arg_1_0):
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_1_0)

	arg_1_0._preWaves = {}
	arg_1_0._postWaves = {}
	arg_1_0._branchWaves = {}

def var_0_2.IsReady(arg_2_0):
	return arg_2_0.IsPreWavesFinished()

def var_0_2.IsFlagsPass(arg_3_0):
	if not arg_3_0._blockFlags or not next(arg_3_0._blockFlags):
		return True

	local var_3_0 = var_0_0.Battle.BattleDataProxy.GetInstance().GetWaveFlags()

	if not var_3_0 or not next(var_3_0):
		return False

	for iter_3_0, iter_3_1 in ipairs(arg_3_0._blockFlags):
		if not table.contains(var_3_0, iter_3_1):
			return False

	return True

def var_0_2.IsPreWavesFinished(arg_4_0):
	local var_4_0 = #arg_4_0._preWaves
	local var_4_1

	if #arg_4_0._preWaves == 0:
		var_4_1 = True
	elif arg_4_0._logicType == var_0_2.LOGIC_AND:
		var_4_1 = True

		for iter_4_0, iter_4_1 in ipairs(arg_4_0._preWaves):
			if not iter_4_1.IsFinish():
				var_4_1 = False

				break
	elif arg_4_0._logicType == var_0_2.LGOIC_OR:
		var_4_1 = False

		for iter_4_2, iter_4_3 in ipairs(arg_4_0._preWaves):
			if iter_4_3.IsFinish():
				var_4_1 = True

				break

	return var_4_1

def var_0_2.IsFinish(arg_5_0):
	return arg_5_0.GetState() == var_0_2.STATE_PASS or arg_5_0.GetState() == var_0_2.STATE_FAIL

def var_0_2.DoBranch(arg_6_0):
	for iter_6_0, iter_6_1 in ipairs(arg_6_0._branchWaves):
		local var_6_0 = arg_6_0._branchWaveIDs[iter_6_1.GetIndex()]

		if var_6_0 and iter_6_1.GetState() == var_0_2.STATE_PASS or not var_6_0 and iter_6_1.GetState() == var_0_2.STATE_FAIL:
			-- block empty
		else
			arg_6_0.doFail()

			return

	if not arg_6_0.IsFlagsPass():
		arg_6_0.doFail()

		return

	arg_6_0.DoWave()

def var_0_2.DoWave(arg_7_0):
	arg_7_0._state = var_0_2.STATE_ACTIVE

def var_0_2.AddMonster(arg_8_0):
	return

def var_0_2.RemoveMonster(arg_9_0):
	return

def var_0_2.SetWaveData(arg_10_0, arg_10_1):
	arg_10_0._index = arg_10_1.waveIndex
	arg_10_0._isKeyWave = arg_10_1.key
	arg_10_0._logicType = arg_10_1.conditionType or var_0_2.LOGIC_AND
	arg_10_0._param = arg_10_1.triggerParams or {}
	arg_10_0._preWaveIDs = arg_10_1.preWaves or {}
	arg_10_0._branchWaveIDs = arg_10_1.conditionWaves or {}
	arg_10_0._blockFlags = arg_10_1.blockFlags
	arg_10_0._type = arg_10_1.triggerType
	arg_10_0._state = var_0_2.STATE_DEACTIVE

def var_0_2.SetCallback(arg_11_0, arg_11_1, arg_11_2):
	arg_11_0._spawnFunc = arg_11_1
	arg_11_0._airFunc = arg_11_2

def var_0_2.AppendBranchWave(arg_12_0, arg_12_1):
	arg_12_0._branchWaves[#arg_12_0._branchWaves + 1] = arg_12_1

def var_0_2.AppendPreWave(arg_13_0, arg_13_1):
	arg_13_0._preWaves[#arg_13_0._preWaves + 1] = arg_13_1

def var_0_2.AppendPostWave(arg_14_0, arg_14_1):
	arg_14_0._postWaves[#arg_14_0._postWaves + 1] = arg_14_1

def var_0_2.IsKeyWave(arg_15_0):
	return arg_15_0._isKeyWave

def var_0_2.GetPostWaves(arg_16_0):
	return arg_16_0._postWaves

def var_0_2.GetIndex(arg_17_0):
	return arg_17_0._index

def var_0_2.GetType(arg_18_0):
	return arg_18_0._type

def var_0_2.GetState(arg_19_0):
	return arg_19_0._state

def var_0_2.GetPreWaveIDs(arg_20_0):
	return arg_20_0._preWaveIDs

def var_0_2.GetBranchWaveIDs(arg_21_0):
	return arg_21_0._branchWaveIDs

def var_0_2.Dispose(arg_22_0):
	var_0_0.EventDispatcher.DetachEventDispatcher(arg_22_0)

def var_0_2.doPass(arg_23_0):
	if not arg_23_0.IsFinish():
		arg_23_0._state = var_0_2.STATE_PASS

		arg_23_0.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleEvent.WAVE_FINISH, {}))

def var_0_2.doFail(arg_24_0):
	if not arg_24_0.IsFinish():
		arg_24_0._state = var_0_2.STATE_FAIL

		arg_24_0.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleEvent.WAVE_FINISH, {}))
