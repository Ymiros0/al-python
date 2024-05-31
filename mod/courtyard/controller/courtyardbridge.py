local var_0_0 = class("CourtYardBridge")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.core = arg_1_1.core
	arg_1_0.isSetup = False
	arg_1_0.controller = arg_1_0.System2Controller(arg_1_1.system, arg_1_1)
	arg_1_0.view = CourtYardView.New(arg_1_1.name, arg_1_0.controller.GetStorey())

	if not arg_1_0.handle:
		arg_1_0.handle = UpdateBeat.CreateListener(arg_1_0.Update, arg_1_0)

	UpdateBeat.AddListener(arg_1_0.handle)

def var_0_0.SetUp(arg_2_0):
	if arg_2_0.controller:
		arg_2_0.isSetup = True

		arg_2_0.controller.SetUp()

def var_0_0.Update(arg_3_0):
	if not arg_3_0.isSetup and arg_3_0.view.IsInit():
		arg_3_0.SetUp()

	if arg_3_0.isSetup and arg_3_0.controller:
		arg_3_0.controller.Update()

def var_0_0.IsLoaed(arg_4_0):
	if not arg_4_0.controller:
		return False

	return arg_4_0.controller.IsLoaed()

def var_0_0.GetView(arg_5_0):
	return arg_5_0.view

def var_0_0.GetController(arg_6_0):
	return arg_6_0.controller

def var_0_0.Exit(arg_7_0):
	if arg_7_0.controller:
		arg_7_0.controller.Dispose()

		arg_7_0.controller = None

	if arg_7_0.view:
		arg_7_0.view.Dispose()

		arg_7_0.view = None

def var_0_0.SendNotification(arg_8_0, arg_8_1, arg_8_2):
	if arg_8_0.core:
		arg_8_0.core.sendNotification(arg_8_1, arg_8_2)

def var_0_0.Dispose(arg_9_0):
	if arg_9_0.handle:
		UpdateBeat.RemoveListener(arg_9_0.handle)

	arg_9_0.Exit()

def var_0_0.System2Controller(arg_10_0, arg_10_1, arg_10_2):
	if arg_10_1 == CourtYardConst.SYSTEM_FEAST:
		return CourtYardFeastController.New(arg_10_0, arg_10_2)
	else
		return CourtYardController.New(arg_10_0, arg_10_2)

return var_0_0
