local var_0_0 = class("CourtYardStoreyDragBtn")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tf = arg_1_1
	arg_1_0._go = arg_1_1.gameObject
	arg_1_0.agent = CourtYardDragAgent.New(arg_1_0, arg_1_2)

	arg_1_0.agent.Enable(False)

def var_0_0.Active(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.OnDragCallBack = arg_2_1
	arg_2_0.OnDragingCallBack = arg_2_2
	arg_2_0.OnDragEndCallBack = arg_2_3

	arg_2_0.agent.Enable(True)

def var_0_0.DeActive(arg_3_0):
	arg_3_0.OnDragCallBack = None
	arg_3_0.OnDragingCallBack = None
	arg_3_0.OnDragEndCallBack = None

	arg_3_0.agent.Enable(False)

def var_0_0.OnBeginDrag(arg_4_0):
	if arg_4_0.OnDragCallBack:
		arg_4_0.OnDragCallBack()

def var_0_0.OnDragging(arg_5_0, arg_5_1):
	if arg_5_0.OnDragingCallBack:
		arg_5_0.OnDragingCallBack(arg_5_1)

def var_0_0.OnDragEnd(arg_6_0, arg_6_1):
	if arg_6_0.OnDragEndCallBack:
		arg_6_0.OnDragEndCallBack(arg_6_1)

def var_0_0.Dispose(arg_7_0):
	arg_7_0.DeActive()
	arg_7_0.agent.Dispose()

return var_0_0
