local var_0_0 = class("CourtYardStoreyPreviewModule", import(".CourtYardStoreyModule"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.bgmAgent.Clear()

def var_0_0.EnableZoom(arg_2_0, arg_2_1):
	arg_2_0.zoomAgent.enabled = False

return var_0_0
