ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffHOT = class("BattleBuffHOT", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffHOT.__name = "BattleBuffHOT"

def var_0_0.Battle.BattleBuffHOT.Ctor(arg_1_0, arg_1_1):
	var_0_0.Battle.BattleBuffHOT.super.Ctor(arg_1_0, arg_1_1)

def var_0_0.Battle.BattleBuffHOT.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._number = arg_2_0._tempData.arg_list.number or 0
	arg_2_0._numberBase = arg_2_0._number
	arg_2_0._time = arg_2_0._tempData.arg_list.time or 0
	arg_2_0._nextEffectTime = pg.TimeMgr.GetInstance().GetCombatTime() + arg_2_0._time
	arg_2_0._maxHPRatio = arg_2_0._tempData.arg_list.maxHPRatio or 0
	arg_2_0._currentHPRatio = arg_2_0._tempData.arg_list.currentHPRatio or 0
	arg_2_0._incorruptible = arg_2_0._tempData.arg_list.incorrupt

def var_0_0.Battle.BattleBuffHOT.onStack(arg_3_0, arg_3_1, arg_3_2):
	return

def var_0_0.Battle.BattleBuffHOT.onUpdate(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	if arg_4_3.timeStamp >= arg_4_0._nextEffectTime:
		local var_4_0 = arg_4_0.CalcNumber(arg_4_1, arg_4_2)
		local var_4_1 = {
			isMiss = False,
			isCri = False,
			isHeal = True,
			incorrupt = arg_4_0._incorruptible
		}

		arg_4_1.UpdateHP(var_4_0, var_4_1)

		if arg_4_1.IsAlive():
			arg_4_0._nextEffectTime = arg_4_0._nextEffectTime + arg_4_0._time

def var_0_0.Battle.BattleBuffHOT.onRemove(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = arg_5_0.CalcNumber(arg_5_1, arg_5_2)
	local var_5_1 = {
		isMiss = False,
		isCri = False,
		isHeal = True,
		incorrupt = arg_5_0._incorruptible
	}

	arg_5_1.UpdateHP(var_5_0, var_5_1)

def var_0_0.Battle.BattleBuffHOT.CalcNumber(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0, var_6_1 = arg_6_1.GetHP()
	local var_6_2 = arg_6_1.GetAttrByName("healingRate")
	local var_6_3 = math.max(0, var_6_0 * arg_6_0._currentHPRatio + var_6_1 * arg_6_0._maxHPRatio + arg_6_0._number)

	return (math.floor(var_6_3 * arg_6_2._stack * var_6_2))
