local var_0_0 = class("NavalTacticsSkillInfoLayer", import(".SkillInfoLayer"))

def var_0_0.showBase(arg_1_0):
	var_0_0.super.showBase(arg_1_0)
	setActive(arg_1_0.metaBtn, False)
	setActive(arg_1_0.upgradeBtn, False)

def var_0_0.showInfo(arg_2_0, arg_2_1):
	arg_2_0.isWorld = arg_2_1

	local var_2_0 = arg_2_0.contextData.skillId
	local var_2_1 = arg_2_0.contextData.skillOnShip
	local var_2_2 = var_2_1 and var_2_1.level or 1

	setText(arg_2_0.skillInfoLv, "Lv." .. var_2_2)
	setText(arg_2_0.skillInfoIntro, Student.getSkillDesc(var_2_0, var_2_2, arg_2_1))

return var_0_0
