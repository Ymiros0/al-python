local var_0_0 = class("CourtYardFeastPedestalModule", import("..CourtYardBaseModule"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.storey = arg_1_0.data
	arg_1_0.scrollView = arg_1_0._tf.parent.Find("scroll_view")

def var_0_0.AddListeners(arg_2_0):
	arg_2_0.AddListener(CourtYardEvent.UPDATE_STOREY, arg_2_0.OnUpdate)

def var_0_0.RemoveListeners(arg_3_0):
	arg_3_0.RemoveListener(CourtYardEvent.UPDATE_STOREY, arg_3_0.OnUpdate)

def var_0_0.OnUpdate(arg_4_0, arg_4_1):
	arg_4_0.level = arg_4_1

	arg_4_0.InitScrollRect(arg_4_1)

def var_0_0.InitScrollRect(arg_5_0, arg_5_1):
	local var_5_0 = 1080 + (arg_5_1 - 1) * 150

	arg_5_0._tf.sizeDelta = Vector2(arg_5_0._tf.sizeDelta.x, var_5_0)

	scrollTo(arg_5_0.scrollView, 0.5, 0.5)

def var_0_0.OnDispose(arg_6_0):
	return

return var_0_0
