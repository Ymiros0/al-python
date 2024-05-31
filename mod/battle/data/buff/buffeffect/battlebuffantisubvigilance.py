ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffAntiSubVigilance", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAntiSubVigilance = var_0_1
var_0_1.__name = "BattleBuffAntiSubVigilance"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._vigilantRange = var_2_0.vigilanceRange
	arg_2_0._sonarRange = var_2_0.sonarRange
	arg_2_0._sonarFrequency = var_2_0.sonarFrequency

def var_0_1.onAttach(arg_3_0, arg_3_1):
	arg_3_0._vigilantUnit = arg_3_1
	arg_3_0._vigilantState = arg_3_1.InitAntiSubState(arg_3_0._sonarRange, arg_3_0._sonarFrequency)

	local var_3_0 = arg_3_0.getTargetList(arg_3_0._vigilantUnit, "TargetHarmNearest", {
		range = 200
	})

	arg_3_0._vigilantState.InitCheck(#var_3_0)

	arg_3_0._sonarCheckTimeStamp = pg.TimeMgr.GetInstance().GetCombatTime()

def var_0_1.onUpdate(arg_4_0):
	if #arg_4_0.getTargetList(arg_4_0._vigilantUnit, "TargetHarmNearest", {
		range = arg_4_0._vigilantRange
	}) > 0:
		arg_4_0._vigilantState.VigilantAreaEngage()

	local var_4_0 = #arg_4_0.getTargetList(arg_4_0._vigilantUnit, "TargetHarmNearest", {
		range = 200
	})
	local var_4_1 = #arg_4_0.getTargetList(arg_4_0._vigilantUnit, {
		"TargetAllFoe",
		"TargetHarmNearest",
		"TargetDiveState"
	}, {
		range = arg_4_0._sonarRange
	})

	arg_4_0._vigilantState.Update(var_4_0, var_4_1)

	local var_4_2 = pg.TimeMgr.GetInstance().GetCombatTime()

	if var_4_2 - arg_4_0._sonarCheckTimeStamp >= arg_4_0._sonarFrequency:
		arg_4_0._vigilantState.SonarDetect(var_4_1)

		arg_4_0._sonarCheckTimeStamp = var_4_2

def var_0_1.onAntiSubHateChain(arg_5_0):
	arg_5_0._vigilantState.HateChain()

def var_0_1.onFriendlyShipDying(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	arg_6_0._vigilantState.MineExplode()

def var_0_1.onSubmarinFreeDive(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	return

def var_0_1.onSubmarinFreeFloat(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	arg_8_0._vigilantState.SubmarineFloat()
