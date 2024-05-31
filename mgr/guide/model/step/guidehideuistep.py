local var_0_0 = class("GuideHideUIStep", import(".GuideStep"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.nodes = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.hideui):
		table.insert(arg_1_0.nodes, {
			path = iter_1_1.path,
			delay = iter_1_1.delay or 0,
			pathIndex = iter_1_1.pathIndex or -1,
			hideFlag = iter_1_1.ishide
		})

def var_0_0.GetType(arg_2_0):
	return GuideStep.TYPE_HIDEUI

def var_0_0.GetHideNodes(arg_3_0):
	return arg_3_0.nodes

return var_0_0
