pg = pg or {}

local var_0_0 = singletonClass("NodeMgr")

pg.NodeMgr = var_0_0

def var_0_0.Ctor(arg_1_0):
	return

var_0_0.NodeBase = {}

def var_0_0.RigisterNode(arg_2_0, arg_2_1):
	var_0_0.NodeBase[arg_2_0] = arg_2_1

def var_0_0.Ctor(arg_3_0):
	return

local function var_0_1(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
	local var_4_0 = arg_4_0.NodeBase[arg_4_2[1]]

	if var_4_0 == None:
		assert(False, "配置的节点不存在，检查“没配置串并”、“拼写错误”或“没补include”~ ：" .. arg_4_2[1])

		return

	local var_4_1 = var_4_0.New(arg_4_1, arg_4_2)

	arg_4_3.Add(var_4_1)

local function var_0_2(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	assert(type(arg_5_2) == "table", "节点信息解析错误." .. tostring(arg_5_2))

	local var_5_0 = arg_5_2._parallel

	if var_5_0 == None:
		var_0_1(arg_5_0, arg_5_1, arg_5_2, arg_5_3)

		return

	if var_5_0 == True:
		local var_5_1 = var_0_0.NodeBase.Guide.New(arg_5_1)

		arg_5_3.Add(var_5_1)

		for iter_5_0, iter_5_1 in ipairs(arg_5_2):
			local var_5_2 = arg_5_3.Center.NewSeq(iter_5_0)

			arg_5_1.AddSeq(var_5_2)

			local var_5_3 = ys.Battle.NodeData.New(arg_5_1.GetUnit(), {}, var_5_2)

			var_5_1.AddFollow(var_5_2, var_5_3)
			var_0_2(arg_5_0, var_5_3, iter_5_1, var_5_2)
	else
		for iter_5_2, iter_5_3 in ipairs(arg_5_2):
			var_0_2(arg_5_0, arg_5_1, iter_5_3, arg_5_3)

def var_0_0.GenNode(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	var_0_2(arg_6_0, arg_6_1, arg_6_2, arg_6_3)

	for iter_6_0, iter_6_1 in ipairs(arg_6_1.GetAllSeq()):
		iter_6_1.Update()
