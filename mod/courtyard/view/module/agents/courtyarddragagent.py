local var_0_0 = class("CourtYardDragAgent", import(".CourtYardAgent"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.rect = arg_1_2
	arg_1_0.trigger = GetOrAddComponent(arg_1_0._tf, "EventTriggerListener")
	arg_1_0.dragging = False

	arg_1_0.RegisterEvent()

def var_0_0.Enable(arg_2_0, arg_2_1):
	arg_2_0.trigger.enabled = arg_2_1

def var_0_0.RegisterEvent(arg_3_0):
	arg_3_0.trigger.AddBeginDragFunc(function(arg_4_0, arg_4_1)
		if not arg_3_0.CanDrag(arg_4_0):
			return

		arg_3_0.dragging = True

		arg_3_0.OnBeginDrag())
	arg_3_0.trigger.AddDragFunc(function(arg_5_0, arg_5_1)
		if arg_3_0.dragging and arg_3_0._go == arg_5_0:
			local var_5_0 = CourtYardCalcUtil.Screen2Local(arg_3_0.rect, arg_5_1.position)
			local var_5_1 = CourtYardCalcUtil.Local2Map(var_5_0)

			arg_3_0.OnDragging(var_5_1))
	arg_3_0.trigger.AddDragEndFunc(function(arg_6_0, arg_6_1)
		if arg_3_0.dragging and arg_6_0 == arg_3_0._go:
			arg_3_0.dragging = False

			local var_6_0 = CourtYardCalcUtil.Screen2Local(arg_3_0.rect, arg_6_1.position)
			local var_6_1 = CourtYardCalcUtil.Local2Map(var_6_0)

			arg_3_0.OnDragEnd(var_6_1))

def var_0_0.CanDrag(arg_7_0, arg_7_1):
	return Input.touchCount <= 1 and arg_7_0._go == arg_7_1

def var_0_0.UnRegisterEvent(arg_8_0):
	arg_8_0.dragging = False

	ClearEventTrigger(arg_8_0.trigger)

def var_0_0.Dispose(arg_9_0):
	var_0_0.super.Dispose(arg_9_0)
	arg_9_0.UnRegisterEvent()
	Object.Destroy(arg_9_0.trigger)

return var_0_0
