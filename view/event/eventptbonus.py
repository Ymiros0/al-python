local var_0_0 = class("EventPtBonus")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.tr = arg_1_1
	arg_1_0.resIcon = findTF(arg_1_0.tr, "Image").GetComponent(typeof(Image))
	arg_1_0.resName = findTF(arg_1_0.tr, "Text").GetComponent(typeof(Text))

	setActive(arg_1_0.tr, False)
	arg_1_0.Update()

def var_0_0.Update(arg_2_0):
	local var_2_0 = getProxy(ActivityProxy).getAliveActivityByType(ActivityConst.ACTIVITY_TYPE_EVENT)

	if var_2_0 and var_2_0.getConfig("config_client").shopActID:
		setActive(arg_2_0.tr, True)

return var_0_0
