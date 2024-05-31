ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffDeath = class("BattleBuffDeath", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffDeath.__name = "BattleBuffDeath"

local var_0_1 = var_0_0.Battle.BattleBuffDeath

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0._tempData.arg_list

	if var_2_0.time:
		arg_2_0._time = var_2_0.time + pg.TimeMgr.GetInstance().GetCombatTime()

	arg_2_0._maxX = var_2_0.maxX
	arg_2_0._minX = var_2_0.minX
	arg_2_0._maxY = var_2_0.maxY
	arg_2_0._minY = var_2_0.minY
	arg_2_0._countType = var_2_0.countType
	arg_2_0._instantkill = arg_2_0._tempData.arg_list.instant_kill

def var_0_1.onAttach(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if arg_3_0._instantkill:
		arg_3_0.DoDead(arg_3_1)

def var_0_1.onUpdate(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	local var_4_0 = arg_4_3.timeStamp

	if arg_4_0._time and var_4_0 > arg_4_0._time:
		arg_4_1.SetDeathReason(var_0_0.Battle.BattleConst.UnitDeathReason.DESTRUCT)
		arg_4_0.DoDead(arg_4_1)
	else
		local var_4_1 = arg_4_1.GetPosition()

		if arg_4_0._maxX and var_4_1.x >= arg_4_0._maxX:
			arg_4_1.SetDeathReason(var_0_0.Battle.BattleConst.UnitDeathReason.LEAVE)
			arg_4_0.DoDead(arg_4_1)
		elif arg_4_0._minX and var_4_1.x <= arg_4_0._minX:
			arg_4_1.SetDeathReason(var_0_0.Battle.BattleConst.UnitDeathReason.LEAVE)
			arg_4_0.DoDead(arg_4_1)
		elif arg_4_0._maxY and var_4_1.z >= arg_4_0._maxY:
			arg_4_1.SetDeathReason(var_0_0.Battle.BattleConst.UnitDeathReason.LEAVE)
			arg_4_0.DoDead(arg_4_1)
		elif arg_4_0._minY and var_4_1.z <= arg_4_0._minY:
			arg_4_1.SetDeathReason(var_0_0.Battle.BattleConst.UnitDeathReason.LEAVE)
			arg_4_0.DoDead(arg_4_1)

def var_0_1.onBattleBuffCount(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if arg_5_3.countType == arg_5_0._countType:
		arg_5_0.DoDead(arg_5_1)

def var_0_1.DoDead(arg_6_0, arg_6_1):
	arg_6_1.SetCurrentHP(0)
	arg_6_1.DeadAction()
