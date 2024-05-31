ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleEvent
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = var_0_0.Battle.BattleConst
local var_0_4 = var_0_0.Battle.BattleConfig
local var_0_5 = var_0_0.Battle.BattleDataFunction
local var_0_6 = var_0_0.Battle.BattleAttr
local var_0_7 = var_0_0.Battle.BattleVariable
local var_0_8 = var_0_0.Battle.BattleTargetChoise
local var_0_9 = var_0_4.VAN_SONAR_PROPERTY
local var_0_10 = class("BattleFleetStaticSonar")

var_0_0.Battle.BattleFleetStaticSonar = var_0_10
var_0_10.__name = "BattleFleetStaticSonar"
var_0_10.STATE_DISABLE = "DISABLE"
var_0_10.STATE_READY = "READY"

def var_0_10.Ctor(arg_1_0, arg_1_1):
	arg_1_0.init()

	arg_1_0._fleetVO = arg_1_1

def var_0_10.GetCurrentState(arg_2_0):
	return arg_2_0._currentState

def var_0_10.Dispose(arg_3_0):
	arg_3_0._detectedList = None
	arg_3_0._crewUnitList = None
	arg_3_0._host = None

def var_0_10.init(arg_4_0):
	arg_4_0._crewUnitList = {}
	arg_4_0._detectedList = {}
	arg_4_0._skillDiameter = 0
	arg_4_0._radius = 0
	arg_4_0._diameter = 0

def var_0_10.AppendExtraSkillRange(arg_5_0, arg_5_1):
	arg_5_0._skillDiameter = arg_5_0._skillDiameter + arg_5_1

	if arg_5_0._radius != 0:
		arg_5_0._radius = arg_5_0._radius + arg_5_1 * 0.5

def var_0_10.AppendCrewUnit(arg_6_0, arg_6_1):
	arg_6_0._crewUnitList[arg_6_1.GetUniqueID()] = arg_6_1

	arg_6_0.flush()

def var_0_10.RemoveCrewUnit(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.GetUniqueID()

	if arg_7_0._crewUnitList[var_7_0]:
		arg_7_0._crewUnitList[var_7_0] = None

		arg_7_0.updateSonarState()

		if arg_7_0._currentState == var_0_10.STATE_DISABLE:
			arg_7_0.Undetect()

def var_0_10.SwitchHost(arg_8_0, arg_8_1):
	arg_8_0._host = arg_8_1

def var_0_10.GetRange(arg_9_0):
	return arg_9_0._diameter

def var_0_10.flush(arg_10_0):
	arg_10_0._diameter = 0

	local var_10_0, var_10_1, var_10_2 = arg_10_0.calcSonarRange()

	if var_10_0 != 0:
		arg_10_0._diameter = var_10_0 + var_10_2 + var_10_1
		arg_10_0._radius = arg_10_0._diameter * 0.5

	arg_10_0.updateSonarState()

def var_0_10.calcSonarRange(arg_11_0):
	local var_11_0 = 0
	local var_11_1 = 0
	local var_11_2 = 0

	for iter_11_0, iter_11_1 in pairs(arg_11_0._crewUnitList):
		local var_11_3, var_11_4, var_11_5 = arg_11_0.getSonarProperty(iter_11_1)

		if var_11_3 > 0:
			var_11_0 = math.max(var_11_3, var_11_0)

		var_11_1 = var_11_1 + var_11_4
		var_11_2 = var_11_2 + var_11_5

	local var_11_6 = var_0_4.MAIN_SONAR_PROPERTY
	local var_11_7 = var_11_2 / var_11_6.a
	local var_11_8 = Mathf.Clamp(var_11_7, var_11_6.minRange, var_11_6.maxRange)

	return var_11_0, var_11_8, var_11_1

def var_0_10.updateSonarState(arg_12_0):
	local var_12_0 = 0

	for iter_12_0, iter_12_1 in pairs(arg_12_0._crewUnitList):
		if arg_12_0.getSonarProperty(iter_12_1) > 0:
			var_12_0 = var_12_0 + 1

	if var_12_0 > 0:
		arg_12_0._currentState = var_0_10.STATE_READY
	else
		arg_12_0._currentState = var_0_10.STATE_DISABLE

	local var_12_1 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.SONAR_UPDATE)

	arg_12_0._fleetVO.DispatchEvent(var_12_1)

def var_0_10.getSonarProperty(arg_13_0):
	local var_13_0 = arg_13_0.GetTemplate().type
	local var_13_1 = var_0_9[var_13_0]
	local var_13_2 = 0

	if var_13_1:
		local var_13_3 = arg_13_0.GetAttrByName("baseAntiSubPower") / var_13_1.a - var_13_1.b

		var_13_2 = Mathf.Clamp(var_13_3, var_13_1.minRange, var_13_1.maxRange)

	local var_13_4 = arg_13_0.GetAttrByName("sonarRange")
	local var_13_5 = 0

	if table.contains(TeamType.MainShipType, var_13_0):
		var_13_5 = arg_13_0.GetAttrByName("baseAntiSubPower")

	return var_13_2, var_13_4, var_13_5

def var_0_10.Update(arg_14_0, arg_14_1):
	if arg_14_0._currentState != var_0_10.STATE_DISABLE:
		arg_14_0._fleetVO.DispatchSonarScan()
		arg_14_0.updateDetectedList()

def var_0_10.Undetect(arg_15_0):
	local var_15_0 = arg_15_0._detectedList

	for iter_15_0, iter_15_1 in ipairs(var_15_0):
		if iter_15_1.IsAlive():
			iter_15_1.Undetected()

	arg_15_0._detectedList = {}

def var_0_10.updateDetectedList(arg_16_0):
	local var_16_0 = var_0_8.LegalTarget(arg_16_0._host)
	local var_16_1 = var_0_8.TargetDiveState(arg_16_0._host, {
		diveState = var_0_3.OXY_STATE.DIVE
	}, var_16_0)
	local var_16_2 = arg_16_0.FilterRange(var_16_1)

	for iter_16_0, iter_16_1 in ipairs(var_16_1):
		local var_16_3 = table.contains(var_16_2, iter_16_1)
		local var_16_4 = table.contains(arg_16_0._detectedList, iter_16_1)

		if var_16_4:
			if not var_16_3:
				iter_16_1.Undetected()
		elif not var_16_4 and var_16_3:
			iter_16_1.Detected()

	arg_16_0._detectedList = var_16_2

def var_0_10.FilterTarget(arg_17_0):
	local var_17_0 = var_0_8.LegalTarget(arg_17_0._host)
	local var_17_1 = var_0_8.TargetDiveState(arg_17_0._host, {
		diveState = var_0_3.OXY_STATE.DIVE
	}, var_17_0)

	return (arg_17_0.FilterRange(var_17_1))

def var_0_10.FilterRange(arg_18_0, arg_18_1):
	local var_18_0 = {}

	for iter_18_0, iter_18_1 in ipairs(arg_18_1):
		if not arg_18_0.isOutOfRange(iter_18_1):
			table.insert(var_18_0, iter_18_1)

	return var_18_0

def var_0_10.isOutOfRange(arg_19_0, arg_19_1):
	return arg_19_0._host.GetDistance(arg_19_1) > arg_19_0._radius

def var_0_10.GetTotalRangeDetail(arg_20_0):
	local var_20_0, var_20_1, var_20_2 = arg_20_0.calcSonarRange()

	return var_20_0, var_20_1, var_20_2, arg_20_0._skillDiameter
