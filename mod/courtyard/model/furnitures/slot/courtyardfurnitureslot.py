local var_0_0 = class("CourtYardFurnitureSlot", import(".CourtYardFurnitureBaseSlot"))

def var_0_0.OnInit(arg_1_0, arg_1_1):
	arg_1_0.actionName = arg_1_1[1]
	arg_1_0.offset = arg_1_1[2] and Vector3(arg_1_1[2][1], arg_1_1[2][2], 0) or Vector3.zero
	arg_1_0.scale = arg_1_1[3] and Vector3(arg_1_1[3][1], arg_1_1[3][2], 1) or Vector3.one
	arg_1_0.mask = arg_1_1[4]
	arg_1_0.bodyMask = arg_1_1[6] and {
		offset = arg_1_1[6][1] and Vector2(arg_1_1[6][1][1], arg_1_1[6][1][2]) or Vector3.zero,
		size = arg_1_1[6][2] and Vector2(arg_1_1[6][2][1], arg_1_1[6][2][2]) or Vector3.zero,
		img = arg_1_1[6][3]
	}

def var_0_0.GetMask(arg_2_0):
	if arg_2_0.mask == "":
		return None

	return arg_2_0.mask

def var_0_0.OnStart(arg_3_0):
	arg_3_0.user.UpdateInteraction({
		action = arg_3_0.actionName
	})

return var_0_0
