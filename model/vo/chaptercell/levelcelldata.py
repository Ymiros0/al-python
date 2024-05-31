local var_0_0 = class("LevelCellData", import("model.vo.BaseVO"))

def var_0_0.GetLine(arg_1_0):
	return {
		row = arg_1_0.row,
		column = arg_1_0.column
	}

def var_0_0.SetLine(arg_2_0, arg_2_1):
	arg_2_0.row = arg_2_1.row
	arg_2_0.column = arg_2_1.column

return var_0_0
