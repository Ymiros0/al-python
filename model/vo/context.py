local var_0_0 = class("Context")

var_0_0.TRANS_TYPE = {
	CROSS = 1,
	ONE_BY_ONE = 2
}

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_1 = arg_1_1 or {}
	arg_1_0.mediator = arg_1_1.mediator
	arg_1_0.viewComponent = arg_1_1.viewComponent
	arg_1_0.scene = arg_1_1.scene
	arg_1_0.onRemoved = arg_1_1.onRemoved
	arg_1_0.cleanStack = defaultValue(arg_1_1.cleanStack, False)
	arg_1_0.data = arg_1_1.data or {}
	arg_1_0.parent = arg_1_1.parent
	arg_1_0.children = {}
	arg_1_0.transType = defaultValue(arg_1_1.transType, var_0_0.TRANS_TYPE.CROSS)

def var_0_0.extendData(arg_2_0, arg_2_1):
	if arg_2_1 == None:
		return

	assert(type(arg_2_1) == "table", "data object should be a table")

	for iter_2_0, iter_2_1 in pairs(arg_2_1):
		arg_2_0.data[iter_2_0] = iter_2_1

def var_0_0.addChild(arg_3_0, arg_3_1):
	assert(isa(arg_3_1, Context), "should be an instance of Context")
	assert(arg_3_1.parent == None, "context already has parent")

	arg_3_1.parent = arg_3_0

	table.insert(arg_3_0.children, arg_3_1)

def var_0_0.addChilds(arg_4_0, arg_4_1):
	_.each(arg_4_1, function(arg_5_0)
		arg_4_0.addChild(arg_5_0))

def var_0_0.hasChild(arg_6_0):
	return arg_6_0.children and #arg_6_0.children > 0

def var_0_0.removeChild(arg_7_0, arg_7_1):
	assert(isa(arg_7_1, Context), "should be an instance of Context")

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.children):
		if iter_7_1 == arg_7_1:
			return table.remove(arg_7_0.children, iter_7_0)

	return None

def var_0_0.retriveLastChild(arg_8_0):
	for iter_8_0 = #arg_8_0.children, 1, -1:
		if not arg_8_0.children[iter_8_0].data.isSubView:
			return arg_8_0.children[iter_8_0].retriveLastChild()

	return arg_8_0

def var_0_0.GetHierarchy(arg_9_0):
	local var_9_0 = {
		arg_9_0
	}
	local var_9_1 = {}

	while #var_9_0 > 0:
		local var_9_2 = table.remove(var_9_0, 1)

		for iter_9_0, iter_9_1 in ipairs(var_9_2.children):
			table.insert(var_9_0, iter_9_1)

		table.insert(var_9_1, var_9_2)

	return var_9_1

def var_0_0.getContextByMediator(arg_10_0, arg_10_1):
	local function var_10_0(arg_11_0, arg_11_1)
		if arg_11_0.mediator == arg_11_1:
			return arg_11_0

		for iter_11_0, iter_11_1 in ipairs(arg_11_0.children):
			local var_11_0 = var_10_0(iter_11_1, arg_11_1)

			if var_11_0 != None:
				return var_11_0

		return None

	return var_10_0(arg_10_0, arg_10_1)

def var_0_0.onContextRemoved(arg_12_0):
	return arg_12_0.onRemoved and arg_12_0.onRemoved()

return var_0_0
