local var_0_0 = class("StoryTimer")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.duration = arg_1_2
	arg_1_0.func = arg_1_1
	arg_1_0.loop = arg_1_3

def var_0_0.Start(arg_2_0):
	arg_2_0.passed = 0
	arg_2_0.running = True
	arg_2_0.paused = None

	if not arg_2_0.handle:
		arg_2_0.handle = UpdateBeat.CreateListener(arg_2_0.Update, arg_2_0)

	UpdateBeat.AddListener(arg_2_0.handle)

def var_0_0.Pause(arg_3_0):
	arg_3_0.paused = True

def var_0_0.Resume(arg_4_0):
	arg_4_0.paused = None

def var_0_0.Stop(arg_5_0):
	if not arg_5_0.running:
		return

	arg_5_0.running = False
	arg_5_0.paused = None
	arg_5_0.passed = 0

	if arg_5_0.handle:
		UpdateBeat.RemoveListener(arg_5_0.handle)

def var_0_0.Update(arg_6_0):
	if not arg_6_0.running or arg_6_0.paused:
		return

	arg_6_0.passed = arg_6_0.passed + Time.deltaTime

	if arg_6_0.passed >= arg_6_0.duration:
		arg_6_0.passed = 0

		arg_6_0.func()

		arg_6_0.loop = arg_6_0.loop - 1

	if arg_6_0.loop == 0:
		arg_6_0.Stop()

return var_0_0
