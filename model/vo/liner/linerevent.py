local var_0_0 = class("LinerEvent", import("model.vo.BaseVO"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1
	arg_1_0.configId = arg_1_0.id

def var_0_0.bindConfigTable(arg_2_0):
	return pg.activity_liner_event

def var_0_0.GetOptionName(arg_3_0):
	return HXSet.hxLan(arg_3_0.getConfig("option"))

def var_0_0.GetOptionDisplay(arg_4_0):
	local var_4_0 = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.getConfig("option_desc_display")):
		local var_4_1 = HXSet.hxLan(iter_4_1[1])

		table.insert(var_4_0, var_4_1)

	return var_4_0

def var_0_0.GetTitle(arg_5_0):
	return HXSet.hxLan(arg_5_0.getConfig("title"))

def var_0_0.GetLogDesc(arg_6_0):
	return HXSet.hxLan(arg_6_0.getConfig("option_desc"))

def var_0_0.GetReasoningDesc(arg_7_0):
	return HXSet.hxLan(arg_7_0.getConfig("option_desc_2"))

return var_0_0
