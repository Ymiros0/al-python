ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleSkillCLS", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillCLS = var_0_1
var_0_1.__name = "BattleSkillCLS"
var_0_1.TYPE_BULLET = 1
var_0_1.TYPE_AIRCRAFT = 2
var_0_1.TYPE_MINION = 3

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._clsTypeList = arg_1_0._tempData.arg_list.typeList or {}

def var_0_1.DoDataEffect(arg_2_0, arg_2_1):
	arg_2_0.doCls(arg_2_1)

def var_0_1.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.doCls(arg_3_1)

def var_0_1.doCls(arg_4_0, arg_4_1):
	local var_4_0 = var_0_0.Battle.BattleDataProxy.GetInstance()
	local var_4_1 = arg_4_1.GetIFF() * -1

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._clsTypeList):
		if iter_4_1 == var_0_1.TYPE_BULLET:
			var_4_0.CLSBullet(var_4_1)
		elif iter_4_1 == var_0_1.TYPE_AIRCRAFT:
			var_4_0.CLSAircraft(var_4_1)
		elif iter_4_1 == var_0_1.TYPE_MINION:
			var_4_0.CLSMinion()
