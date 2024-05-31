local var_0_0 = setmetatable
local var_0_1 = UpdateBeat
local var_0_2 = CoUpdateBeat
local var_0_3 = Time

Timer = {
	loop = 1,
	running = False,
	time = 0,
	duration = 1,
	scale = False
}

local var_0_4 = Timer
local var_0_5 = {
	__index = var_0_4
}

def var_0_4.New(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	assert(arg_1_1 > 0, "定时器间隔不能小于等于0！：" .. arg_1_1)

	arg_1_3 = arg_1_3 or False
	arg_1_2 = arg_1_2 or 1

	return var_0_0({
		running = False,
		func = arg_1_0,
		duration = arg_1_1,
		time = arg_1_1,
		loop = arg_1_2,
		scale = arg_1_3
	}, var_0_5)

def var_0_4.Start(arg_2_0):
	assert(arg_2_0.running == False, "对已经启动的定时器执行启动！")

	arg_2_0.running = True
	arg_2_0.paused = None

	if not arg_2_0.handle:
		arg_2_0.handle = var_0_1.CreateListener(arg_2_0.Update, arg_2_0)

	var_0_1.AddListener(arg_2_0.handle)

def var_0_4.Reset(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	arg_3_0.duration = arg_3_2 or arg_3_0.duration

	assert(arg_3_0.duration > 0, "定时器间隔不能小于等于0！：" .. arg_3_0.duration)

	arg_3_0.loop = arg_3_3 or arg_3_0.loop
	arg_3_0.scale = arg_3_4 or arg_3_0.scale
	arg_3_0.func = arg_3_1 or arg_3_0.func
	arg_3_0.time = arg_3_2 or arg_3_0.time
	arg_3_0.running = False
	arg_3_0.paused = None

def var_0_4.SetScale(arg_4_0, arg_4_1):
	arg_4_0.scale = arg_4_1

def var_0_4.Stop(arg_5_0):
	if not arg_5_0.running:
		return

	arg_5_0.running = False
	arg_5_0.paused = None
	arg_5_0.time = 0

	if arg_5_0.handle:
		var_0_1.RemoveListener(arg_5_0.handle)

def var_0_4.Pause(arg_6_0):
	arg_6_0.paused = True

def var_0_4.Resume(arg_7_0):
	arg_7_0.paused = None

def var_0_4.Update(arg_8_0):
	if not arg_8_0.running or arg_8_0.paused:
		return

	local var_8_0 = arg_8_0.scale and var_0_3.deltaTime or var_0_3.unscaledDeltaTime

	arg_8_0.time = arg_8_0.time - var_8_0

	local var_8_1 = 0

	while arg_8_0.time <= 0 and var_8_1 < 6:
		var_8_1 = var_8_1 + 1

		arg_8_0.func(arg_8_0)

		if arg_8_0.loop > 0:
			arg_8_0.loop = arg_8_0.loop - 1
			arg_8_0.time = arg_8_0.time + arg_8_0.duration

		if arg_8_0.loop == 0:
			arg_8_0.Stop()

			return
		elif arg_8_0.loop < 0:
			arg_8_0.time = arg_8_0.time + arg_8_0.duration

FrameTimer = {}

local var_0_6 = FrameTimer
local var_0_7 = {
	__index = var_0_6
}

def var_0_6.New(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = var_0_3.frameCount + arg_9_1

	arg_9_2 = arg_9_2 or 1

	return var_0_0({
		running = False,
		func = arg_9_0,
		loop = arg_9_2,
		duration = arg_9_1,
		count = var_9_0
	}, var_0_7)

def var_0_6.Reset(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	arg_10_0.func = arg_10_1
	arg_10_0.duration = arg_10_2
	arg_10_0.loop = arg_10_3
	arg_10_0.count = var_0_3.frameCount + arg_10_2

def var_0_6.Start(arg_11_0):
	if not arg_11_0.handle:
		arg_11_0.handle = var_0_2.CreateListener(arg_11_0.Update, arg_11_0)

	var_0_2.AddListener(arg_11_0.handle)

	arg_11_0.running = True

def var_0_6.Stop(arg_12_0):
	arg_12_0.running = False

	if arg_12_0.handle:
		var_0_2.RemoveListener(arg_12_0.handle)

def var_0_6.Update(arg_13_0):
	if not arg_13_0.running:
		return

	if var_0_3.frameCount >= arg_13_0.count:
		arg_13_0.func()

		if arg_13_0.loop > 0:
			arg_13_0.loop = arg_13_0.loop - 1

		if arg_13_0.loop == 0:
			arg_13_0.Stop()
		else
			arg_13_0.count = var_0_3.frameCount + arg_13_0.duration

CoTimer = {}

local var_0_8 = CoTimer
local var_0_9 = {
	__index = var_0_8
}

def var_0_8.New(arg_14_0, arg_14_1, arg_14_2):
	arg_14_2 = arg_14_2 or 1

	return var_0_0({
		running = False,
		duration = arg_14_1,
		loop = arg_14_2,
		func = arg_14_0,
		time = arg_14_1
	}, var_0_9)

def var_0_8.Start(arg_15_0):
	if not arg_15_0.handle:
		arg_15_0.handle = var_0_2.CreateListener(arg_15_0.Update, arg_15_0)

	arg_15_0.running = True

	var_0_2.AddListener(arg_15_0.handle)

def var_0_8.Reset(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	arg_16_0.duration = arg_16_2
	arg_16_0.loop = arg_16_3 or 1
	arg_16_0.func = arg_16_1
	arg_16_0.time = arg_16_2

def var_0_8.Stop(arg_17_0):
	arg_17_0.running = False

	if arg_17_0.handle:
		var_0_2.RemoveListener(arg_17_0.handle)

def var_0_8.Update(arg_18_0):
	if not arg_18_0.running:
		return

	if arg_18_0.time <= 0:
		arg_18_0.func()

		if arg_18_0.loop > 0:
			arg_18_0.loop = arg_18_0.loop - 1
			arg_18_0.time = arg_18_0.time + arg_18_0.duration

		if arg_18_0.loop == 0:
			arg_18_0.Stop()
		elif arg_18_0.loop < 0:
			arg_18_0.time = arg_18_0.time + arg_18_0.duration

	arg_18_0.time = arg_18_0.time - var_0_3.deltaTime
