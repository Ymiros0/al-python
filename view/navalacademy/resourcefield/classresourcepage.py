local var_0_0 = class("ClassResourcePage", import(".ResourcePage"))

def var_0_0.getUIName(arg_1_0):
	return "ClassResourcePage"

def var_0_0.OnUpgrade(arg_2_0):
	local var_2_0 = arg_2_0.resourceField.GetUpgradeType()

	arg_2_0.emit(ClassMediator.UPGRADE_FIELD, var_2_0)

return var_0_0
