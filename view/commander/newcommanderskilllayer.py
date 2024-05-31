local var_0_0 = class("NewCommanderSkillLayer", import(".CommanderSkillLayer"))

def var_0_0.getUIName(arg_1_0):
	return "NewCommanderSkillUI"

def var_0_0.didEnter(arg_2_0):
	var_0_0.super.didEnter(arg_2_0)

	arg_2_0.commonFlag = defaultValue(arg_2_0.contextData.commonFlag, True)

	local var_2_0 = arg_2_0.findTF("panel/bg/tags")

	onToggle(arg_2_0, var_2_0, function(arg_3_0)
		arg_2_0.commonFlag = arg_3_0

		arg_2_0.UpdateList(), SFX_PANEL)
	triggerToggle(var_2_0, arg_2_0.commonFlag)

def var_0_0.SetLocaliza(arg_4_0):
	return

def var_0_0.GetColor(arg_5_0, arg_5_1):
	return arg_5_1 and "#66472a" or "#a3a2a2"

return var_0_0
