local var_0_0 = class("CourtYardFollowerSlot", import(".CourtYardFurnitureBaseSlot"))

def var_0_0.OnInit(arg_1_0, arg_1_1):
	arg_1_0.name = arg_1_1[1][1]
	arg_1_0.defaultAction = arg_1_1[1][2]
	arg_1_0.skewValue = Vector3(arg_1_1[3][1][1], arg_1_1[3][1][2])
	arg_1_0.aciton = arg_1_1[3][2]

def var_0_0.GetSpineDefaultAction(arg_2_0):
	return arg_2_0.defaultAction

def var_0_0.Occupy(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if arg_3_0.IsEmpty():
		arg_3_0.owner = arg_3_2
		arg_3_0.user = arg_3_1
		arg_3_0.observer = arg_3_3

		arg_3_0.Use()
		arg_3_0.OnAwake()
		arg_3_3.StartInteraction(arg_3_0)
		arg_3_1.StartInteraction(arg_3_0)
		arg_3_2.StartInteraction(arg_3_0, True)
		arg_3_0.OnStart()

def var_0_0.OnAwake(arg_4_0):
	arg_4_0.ClearTimer()

def var_0_0.Clear(arg_5_0, arg_5_1):
	if arg_5_0.IsUsing():
		arg_5_0.Empty()
		arg_5_0.observer.WillClearInteraction(arg_5_0, arg_5_1)
		arg_5_0.user.ClearInteraction(arg_5_0, arg_5_1)
		arg_5_0.owner.ClearInteraction(arg_5_0, arg_5_1, True)
		arg_5_0.observer.ClearInteraction(arg_5_0, arg_5_1)

		arg_5_0.user = None
		arg_5_0.owner = None
		arg_5_0.observer = None

def var_0_0.OnStart(arg_6_0):
	arg_6_0.user.UpdateInteraction({
		action = arg_6_0.aciton,
		slot = arg_6_0
	})

def var_0_0.ClearTimer(arg_7_0):
	return

def var_0_0.OnStop(arg_8_0):
	arg_8_0.ClearTimer()

def var_0_0.OnEnd(arg_9_0):
	arg_9_0.ClearTimer()

def var_0_0.GetBodyMask(arg_10_0):
	return False

def var_0_0.GetUsingAnimator(arg_11_0):
	return False

def var_0_0.GetFollower(arg_12_0):
	return None

return var_0_0
