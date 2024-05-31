local var_0_0 = class("WSMapItem", import("...BaseEntity"))

var_0_0.Fields = {
	cell = "table",
	transform = "userdata",
	rtArtifacts = "userdata",
	theme = "table"
}

def var_0_0.GetResName():
	return "world_cell_item"

def var_0_0.GetName(arg_2_0, arg_2_1):
	return "item_" .. arg_2_0 .. "_" .. arg_2_1

def var_0_0.Setup(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.cell = arg_3_1
	arg_3_0.theme = arg_3_2

	arg_3_0.Init()

def var_0_0.Dispose(arg_4_0):
	arg_4_0.Clear()

def var_0_0.Init(arg_5_0):
	local var_5_0 = arg_5_0.cell
	local var_5_1 = arg_5_0.transform

	var_5_1.name = var_0_0.GetName(var_5_0.row, var_5_0.column)
	var_5_1.anchoredPosition = arg_5_0.theme.GetLinePosition(var_5_0.row, var_5_0.column)
	var_5_1.sizeDelta = arg_5_0.theme.cellSize
	arg_5_0.rtArtifacts = var_5_1.Find("artifacts")
	arg_5_0.rtArtifacts.localEulerAngles = Vector3(-arg_5_0.theme.angle, 0, 0)

return var_0_0
