from luatable import table, setmetatable
from Framework.tolua.event import UpdateBeat, CoUpdateBeat #!
from Framework.tolua.unityengine.Time import Time #!

Timer = table(
	loop = 1,
	running = False,
	time = 0,
	duration = 1,
	scale = False
)


mt = table(
	__index = Timer
)

class Timer:
	loop = 1,
	running = False,
	time = 0,
	duration = 1,
	scale = False

	def New(func, duration, loop=1, scale=False):
		assert duration > 0, f"定时器间隔不能小于等于0！：table(arg_1_1)"

		scale = scale and True	
		loop = loop or 1
		return setmetatable(table(func = func, duration = duration, time = duration, loop = loop, scale = scale, running = False), mt)	

	def Start(arg_2_0):
		assert(arg_2_0.running == False, "对已经启动的定时器执行启动！")

		arg_2_0.running = True
		arg_2_0.paused = None

		if not arg_2_0.handle:
			arg_2_0.handle = UpdateBeat.CreateListener(arg_2_0.Update, arg_2_0)

		UpdateBeat.AddListener(arg_2_0.handle)

	def Reset(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
		arg_3_0.duration = arg_3_2 or arg_3_0.duration

		assert arg_3_0.duration > 0, f"定时器间隔不能小于等于0！：{arg_3_0.duration}"

		arg_3_0.loop = arg_3_3 or arg_3_0.loop
		arg_3_0.scale = arg_3_4 or arg_3_0.scale
		arg_3_0.func = arg_3_1 or arg_3_0.func
		arg_3_0.time = arg_3_2 or arg_3_0.time
		arg_3_0.running = False
		arg_3_0.paused = None

	def SetScale(arg_4_0, arg_4_1):
		arg_4_0.scale = arg_4_1

	def Stop(arg_5_0):
		if not arg_5_0.running:
			return

		arg_5_0.running = False
		arg_5_0.paused = None
		arg_5_0.time = 0

		if arg_5_0.handle:
			UpdateBeat.RemoveListener(arg_5_0.handle)

	def Pause(arg_6_0):
		arg_6_0.paused = True

	def Resume(arg_7_0):
		arg_7_0.paused = None

	def Update(arg_8_0):
		if not arg_8_0.running or arg_8_0.paused:
			return

		var_8_0 = arg_8_0.scale and Time.deltaTime or Time.unscaledDeltaTime

		arg_8_0.time = arg_8_0.time - var_8_0

		var_8_1 = 0

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

FrameTimer = table()

mt2 = table(
	__index = FrameTimer
	)

class FrameTimer:
	def New(arg_9_0, arg_9_1, arg_9_2):
		var_9_0 = Time.frameCount + arg_9_1

		arg_9_2 = arg_9_2 or 1

		return setmetatable(table(
			running = False,
			func = arg_9_0,
			loop = arg_9_2,
			duration = arg_9_1,
			count = var_9_0
		), mt2)

	def Reset(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
		arg_10_0.func = arg_10_1
		arg_10_0.duration = arg_10_2
		arg_10_0.loop = arg_10_3
		arg_10_0.count = Time.frameCount + arg_10_2

	def Start(arg_11_0):
		if not arg_11_0.handle:
			arg_11_0.handle = CoUpdateBeat.CreateListener(arg_11_0.Update, arg_11_0)

		CoUpdateBeat.AddListener(arg_11_0.handle)

		arg_11_0.running = True

	def Stop(arg_12_0):
		arg_12_0.running = False

		if arg_12_0.handle:
			CoUpdateBeat.RemoveListener(arg_12_0.handle)

	def Update(arg_13_0):
		if not arg_13_0.running:
			return

		if Time.frameCount >= arg_13_0.count:
			arg_13_0.func()

			if arg_13_0.loop > 0:
				arg_13_0.loop = arg_13_0.loop - 1

			if arg_13_0.loop == 0:
				arg_13_0.Stop()
			else:
				arg_13_0.count = Time.frameCount + arg_13_0.duration

CoTimer = table()


mt3 = table(
	__index = CoTimer
)

class CoTimer:
	def New(arg_14_0, arg_14_1, arg_14_2):
		arg_14_2 = arg_14_2 or 1

		return setmetatable(table(
			running = False,
			duration = arg_14_1,
			loop = arg_14_2,
			func = arg_14_0,
			time = arg_14_1
		), mt3)

	def Start(arg_15_0):
		if not arg_15_0.handle:
			arg_15_0.handle = CoUpdateBeat.CreateListener(arg_15_0.Update, arg_15_0)

		arg_15_0.running = True

		CoUpdateBeat.AddListener(arg_15_0.handle)

	def Reset(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
		arg_16_0.duration = arg_16_2
		arg_16_0.loop = arg_16_3 or 1
		arg_16_0.func = arg_16_1
		arg_16_0.time = arg_16_2

	def Stop(arg_17_0):
		arg_17_0.running = False

		if arg_17_0.handle:
			CoUpdateBeat.RemoveListener(arg_17_0.handle)

	def Update(arg_18_0):
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

		arg_18_0.time = arg_18_0.time - Time.deltaTime
