local var_0_0 = class("StereoCellView", import("view.level.cell.LevelCellView"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0)

	arg_1_0.assetName = None
	arg_1_0.line = {
		row = arg_1_1,
		column = arg_1_2
	}
	arg_1_0.buffer = FuncBuffer.New()

def var_0_0.UpdateGO(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0.GetLoader().GetRequestPackage("main")

	if var_2_0 and var_2_0.name == arg_2_0.assetName:
		return

	arg_2_0.buffer.Clear()
	arg_2_0.buffer.SetNotifier(None)
	arg_2_0.GetLoader().GetPrefab(arg_2_1, arg_2_2, function(arg_3_0)
		arg_2_0.go = arg_3_0
		arg_2_0.tf = arg_2_0.go.transform

		arg_2_0.OnLoaded(arg_3_0)
		arg_2_0.buffer.SetNotifier(arg_2_0)
		arg_2_0.buffer.ExcuteAll()
		arg_2_0.OverrideCanvas()
		arg_2_0.ResetCanvasOrder(), "main")

def var_0_0.OnLoaded(arg_4_0, arg_4_1):
	return

return var_0_0
