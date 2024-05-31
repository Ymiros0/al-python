ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleEvent
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = class("BattleSkillProjectShelter", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillProjectShelter = var_0_3
var_0_3.__name = "BattleSkillProjectShelter"

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_3.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._duration = arg_1_0._tempData.arg_list.duration
	arg_1_0._offset = arg_1_0._tempData.arg_list.offset
	arg_1_0._fxID = arg_1_0._tempData.arg_list.effect
	arg_1_0._box = arg_1_0._tempData.arg_list.box
	arg_1_0._count = arg_1_0._tempData.arg_list.count

def var_0_3.DoDataEffect(arg_2_0, arg_2_1):
	local var_2_0 = var_0_0.Battle.BattleDataProxy.GetInstance()
	local var_2_1 = var_2_0.SpawnShelter(arg_2_0._box, arg_2_0._duration)
	local var_2_2 = arg_2_1.GetIFF()

	if var_2_2 == var_0_2.FOE_CODE:
		arg_2_0._offset[1] = arg_2_0._offset[1] * -1

	local var_2_3 = arg_2_1.GetPosition() + BuildVector3(arg_2_0._offset)

	var_2_1.SetIFF(var_2_2)
	var_2_1.SetArgs(arg_2_0._count, arg_2_0._duration, arg_2_0._box, var_2_3, arg_2_0._fxID)
	var_2_1.SetStartTimeStamp(pg.TimeMgr.GetInstance().GetCombatTime())

	local var_2_4 = {
		shelter = var_2_1
	}

	var_2_0.DispatchEvent(var_0_0.Event.New(var_0_1.ADD_SHELTER, var_2_4))

def var_0_3.DataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.DoDataEffect(arg_3_1)
