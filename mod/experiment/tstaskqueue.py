local var_0_0 = class("TSTaskQueue")

var_0_0.MTPF = 0.03333333333333333

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.maxTimePerFrame = math.min(arg_1_1, var_0_0.MTPF)
	arg_1_0.taskPool = {}
	arg_1_0.taskQueue = {}
	arg_1_0.running = False
	arg_1_0.updateHandle = UpdateBeat.CreateListener(arg_1_0.Update, arg_1_0)

def var_0_0.Enqueue(arg_2_0, arg_2_1):
	assert(type(arg_2_1) == "function", "job should be a function")

	local var_2_0 = #arg_2_0.taskPool > 0 and table.remove(arg_2_0.taskPool, #arg_2_0.taskPool) or TSTask.New()

	var_2_0.SetJob(arg_2_1)
	table.insert(arg_2_0.taskQueue, var_2_0)

	if not arg_2_0.running:
		arg_2_0.running = True

		UpdateBeat.AddListener(arg_2_0.updateHandle)

def var_0_0.Update(arg_3_0):
	if not arg_3_0.running:
		return

	local var_3_0 = 0

	while var_3_0 < arg_3_0.maxTimePerFrame:
		if #arg_3_0.taskQueue == 0:
			UpdateBeat.RemoveListener(arg_3_0.updateHandle)

			arg_3_0.running = False

			return

		local var_3_1 = table.remove(arg_3_0.taskQueue, 1)

		var_3_0 = var_3_0 + var_3_1.Execute()

		var_3_1.Clear()
		table.insert(arg_3_0.taskPool, var_3_1)

def var_0_0.IsBusy(arg_4_0):
	return arg_4_0.running

def var_0_0.Clear(arg_5_0, arg_5_1):
	for iter_5_0 = #arg_5_0.taskQueue, 1, -1:
		local var_5_0 = arg_5_0.taskQueue[iter_5_0]

		if arg_5_1:
			var_5_0.Execute()

		var_5_0.Clear()
		table.insert(arg_5_0.taskPool, var_5_0)

	arg_5_0.taskQueue = {}

return var_0_0
