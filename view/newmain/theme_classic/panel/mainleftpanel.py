local var_0_0 = class("MainLeftPanel", import("...base.MainConcealablePanel"))

def var_0_0.GetBtns(arg_1_0):
	return {
		MainCommissionBtn.New(findTF(arg_1_0._tf, "commissionButton"), arg_1_0.event),
		MainHideBtn.New(findTF(arg_1_0._tf, "hideButton"), arg_1_0.event),
		MainCameraBtn.New(findTF(arg_1_0._tf, "cameraButton"), arg_1_0.event),
		MainWordBtn.New(findTF(arg_1_0._tf, "wordBtn"), arg_1_0.event),
		MainChangeSkinBtn.New(findTF(arg_1_0._tf, "changeBtn"), arg_1_0.event)
	}

def var_0_0.GetDirection(arg_2_0):
	return Vector2(-1, 0)

return var_0_0
