local var_0_0 = class("WSMapEffect", import(".WSMapTransform"))

var_0_0.Fields = {
	resPath = "string",
	resName = "string"
}

def var_0_0.Dispose(arg_1_0):
	arg_1_0.Unload()
	var_0_0.super.Dispose(arg_1_0)

def var_0_0.Setup(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.resPath = arg_2_1
	arg_2_0.resName = arg_2_2

def var_0_0.Load(arg_3_0, arg_3_1):
	arg_3_0.LoadModel(WorldConst.ModelPrefab, arg_3_0.resPath, arg_3_0.resName, True, function()
		setParent(arg_3_0.model, arg_3_0.transform, False)

		return existCall(arg_3_1))

def var_0_0.Unload(arg_5_0):
	arg_5_0.UnloadModel()

return var_0_0
