ys = ys or {}
ys.Story = ys.Story or {}
ys.Story.NodeData = class("NodeData")

local var_0_0 = ys.Story.NodeData

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._data = arg_1_1 or {}
	arg_1_0._allSeq = {
		arg_1_2
	}

def var_0_0.AddSeq(arg_2_0, arg_2_1):
	table.insert(arg_2_0._allSeq, arg_2_1)

def var_0_0.GetAllSeq(arg_3_0):
	return arg_3_0._allSeq
