local var_0_0 = class("MetaTacticsInfo")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	if arg_1_1:
		arg_1_0.shipID = arg_1_1.ship_id
		arg_1_0.curDayExp = arg_1_1.exp
		arg_1_0.curSkillID = arg_1_1.skill_id
		arg_1_0.skillExpInfoTable = {}

		for iter_1_0, iter_1_1 in ipairs(arg_1_1.skill_exp):
			local var_1_0 = iter_1_1.skill_id
			local var_1_1 = iter_1_1.exp

			arg_1_0.skillExpInfoTable[var_1_0] = var_1_1
	else
		arg_1_0.shipID = None
		arg_1_0.curDayExp = 0
		arg_1_0.curSkillID = None
		arg_1_0.skillExpInfoTable = {}

def var_0_0.updateExp(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_1.day_exp
	local var_2_1 = arg_2_1.skill_id
	local var_2_2 = arg_2_1.skill_exp

	arg_2_0.curDayExp = var_2_0
	arg_2_0.skillExpInfoTable[var_2_1] = var_2_2

def var_0_0.setNewExp(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.skillExpInfoTable[arg_3_1] = arg_3_2

	arg_3_0.printInfo()

def var_0_0.switchSkill(arg_4_0, arg_4_1):
	arg_4_0.curSkillID = arg_4_1

def var_0_0.unlockSkill(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0.skillExpInfoTable[arg_5_1] = 0

	if arg_5_2:
		arg_5_0.curSkillID = arg_5_1

def var_0_0.getSkillExp(arg_6_0, arg_6_1):
	return arg_6_0.skillExpInfoTable[arg_6_1] or 0

def var_0_0.isExpMaxPerDay(arg_7_0):
	return arg_7_0.curDayExp >= pg.gameset.meta_skill_exp_max.key_value

def var_0_0.isAnyLearning(arg_8_0):
	return arg_8_0.curSkillID and arg_8_0.curSkillID > 0

var_0_0.States = {
	LearnAble = 1,
	LearnFinished = 3,
	None = 0,
	Learning = 2
}

def var_0_0.getTacticsStateForShow(arg_9_0):
	local var_9_0 = arg_9_0.isAnyLearning()
	local var_9_1 = getProxy(BayProxy).getShipById(arg_9_0.shipID)
	local var_9_2 = var_9_1 and var_9_1.isAllMetaSkillLevelMax() or False

	if not var_9_0 and not var_9_2:
		return var_0_0.States.LearnAble
	elif var_9_0:
		if getProxy(BayProxy).getShipById(arg_9_0.shipID).isSkillLevelMax(arg_9_0.curSkillID):
			if not var_9_2:
				local var_9_3 = getProxy(BayProxy).getShipById(arg_9_0.shipID).getGroupId()

				if not MetaCharacterConst.isMetaTacticsRedTag(var_9_3):
					return var_0_0.States.LearnAble

			return var_0_0.States.LearnFinished
		else
			return var_0_0.States.Learning
	else
		return var_0_0.States.None

def var_0_0.printInfo(arg_10_0):
	return

return var_0_0
