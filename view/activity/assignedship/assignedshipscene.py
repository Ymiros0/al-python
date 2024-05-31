local var_0_0 = class("AssignedShipScene", import(".BaseAssignedShipScene"))

def var_0_0.getUIName(arg_1_0):
	return "AssignedShipUI"

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

	arg_2_0.scrollrect = arg_2_0.findTF("layer/select_panel")
	arg_2_0.rightBtn = arg_2_0.findTF("layer/right")
	arg_2_0.leftBtn = arg_2_0.findTF("layer/left")

def var_0_0.didEnter(arg_3_0):
	var_0_0.super.didEnter(arg_3_0)

	arg_3_0.isZero = True
	arg_3_0.isOne = False

	onScroll(arg_3_0, arg_3_0.scrollrect, function(arg_4_0)
		local var_4_0 = Mathf.Clamp01(arg_4_0.x)
		local var_4_1 = arg_3_0.isZero
		local var_4_2 = arg_3_0.isOne

		arg_3_0.isZero = var_4_0 - 0.0001 <= 0
		arg_3_0.isOne = var_4_0 + 0.0001 >= 1

		if var_4_1 != arg_3_0.isZero or var_4_2 != arg_3_0.isOne:
			arg_3_0.UpdateArr())
	arg_3_0.UpdateArr()

def var_0_0.UpdateArr(arg_5_0):
	setActive(arg_5_0.rightBtn, not arg_5_0.isZero)
	setActive(arg_5_0.leftBtn, not arg_5_0.isOne)

return var_0_0
