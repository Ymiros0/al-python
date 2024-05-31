ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.AIStepType
local var_0_2 = class("AutoPilot")

var_0_0.Battle.AutoPilot = var_0_2
var_0_2.__name = "AutoPilot"
var_0_2.PILOT_VALVE = 0.5

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._aiCfg = arg_1_2
	arg_1_0._target = arg_1_1

	arg_1_1._move.SetAutoMoveAI(arg_1_0, arg_1_1)
	arg_1_0.generateList()

	arg_1_0._currentStep = arg_1_0._stepList[arg_1_0._aiCfg.default]

	arg_1_0._currentStep.Active(arg_1_0._target)

def var_0_2.GetDirection(arg_2_0):
	local var_2_0 = arg_2_0._target.GetPosition()

	return (arg_2_0._currentStep.GetDirection(var_2_0))

def var_0_2.GetTarget(arg_3_0):
	return arg_3_0._target

def var_0_2.InputWeaponStateChange(arg_4_0):
	return

def var_0_2.SetHiveUnit(arg_5_0, arg_5_1):
	arg_5_0._hiveUnit = arg_5_1

def var_0_2.GetHiveUnit(arg_6_0):
	return arg_6_0._hiveUnit

def var_0_2.OnHiveUnitDead(arg_7_0):
	arg_7_0._target.OnMotherDead()

def var_0_2.NextStep(arg_8_0):
	local var_8_0 = arg_8_0._currentStep.GetToIndex()

	if arg_8_0._stepList[var_8_0] == None:
		var_8_0 = arg_8_0._aiCfg.default

	arg_8_0._currentStep = arg_8_0._stepList[var_8_0]

	arg_8_0._currentStep.Active(arg_8_0._target)

def var_0_2.generateList(arg_9_0):
	arg_9_0._stepList = {}

	for iter_9_0, iter_9_1 in ipairs(arg_9_0._aiCfg.list):
		local var_9_0
		local var_9_1 = iter_9_1.index
		local var_9_2 = iter_9_1.to
		local var_9_3 = iter_9_1.type
		local var_9_4 = iter_9_1.param

		if var_9_3 == var_0_1.STAY:
			var_9_0 = var_0_0.Battle.AutoPilotStay.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.MOVE_TO:
			var_9_0 = var_0_0.Battle.AutoPilotMoveTo.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.MOVE:
			var_9_0 = var_0_0.Battle.AutoPilotMove.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.MOVE_RELATIVE:
			var_9_0 = var_0_0.Battle.AutoPilotMoveRelative.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.BROWNIAN:
			var_9_0 = var_0_0.Battle.AutoPilotBrownian.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.CIRCLE:
			var_9_0 = var_0_0.Battle.AutoPilotCircle.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.RELATIVE_BROWNIAN:
			var_9_0 = var_0_0.Battle.AutoPilotRelativeBrownian.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.RELATIVE_FLEET_MOVE_TO:
			var_9_0 = var_0_0.Battle.AutoPilotRelativeFleetMoveTo.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.HIVE_STAY:
			var_9_0 = var_0_0.Battle.AutoPilotHiveRelativeStay.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.HIVE_CIRCLE:
			var_9_0 = var_0_0.Battle.AutoPilotHiveRelativeCircle.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.MINION_STAY:
			var_9_0 = var_0_0.Battle.AutoPilotMinionRelativeStay.New(var_9_1, arg_9_0)
		elif var_9_3 == var_0_1.MINION_CIRCLE:
			var_9_0 = var_0_0.Battle.AutoPilotMinionRelativeCircle.New(var_9_1, arg_9_0)

		var_9_0.SetParameter(var_9_4, var_9_2)

		arg_9_0._stepList[var_9_0.GetIndex()] = var_9_0
