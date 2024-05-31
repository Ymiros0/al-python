GCThread = singletonClass("GCThread")

local var_0_0 = GCThread

var_0_0.R1024 = 0.00097656

def var_0_0.Ctor(arg_1_0):
	arg_1_0.step = 1
	arg_1_0.gctick = 0
	arg_1_0.gccost = 0
	arg_1_0.running = False
	arg_1_0.gcHandle = UpdateBeat.CreateListener(arg_1_0.GCStep, arg_1_0)
	arg_1_0.checkHandle = UpdateBeat.CreateListener(arg_1_0.WatchStep, arg_1_0)

def var_0_0.GC(arg_2_0, arg_2_1):
	arg_2_0.needUnityGC = True

	arg_2_0.LuaGC(arg_2_1)

def var_0_0.LuaGC(arg_3_0, arg_3_1):
	if arg_3_1:
		collectgarbage("collect")
		arg_3_0.GCFinal()
	elif not arg_3_0.running:
		arg_3_0.running = True

		arg_3_0.CalcStep()

		arg_3_0.gctick = 0
		arg_3_0.gccost = 0

		UpdateBeat.AddListener(arg_3_0.gcHandle)

def var_0_0.GCFinal(arg_4_0):
	arg_4_0.running = False

	UpdateBeat.RemoveListener(arg_4_0.gcHandle)

	if arg_4_0.needUnityGC:
		arg_4_0.needUnityGC = False

		local var_4_0 = PoolMgr.GetInstance()
		local var_4_1 = var_4_0.SpriteMemUsage()
		local var_4_2 = 24

		originalPrint("cached sprite size. " .. math.ceil(var_4_1 * 10) / 10 .. "/" .. var_4_2 .. "MB")

		if var_4_2 < var_4_1:
			var_4_0.DestroyAllSprite()

		ResourceMgr.Inst.ResUnloadAsync()
		LuaHelper.UnityGC()

	if IsUnityEditor:
		print("lua mem. " .. collectgarbage("count") * var_0_0.R1024 .. "MB")

def var_0_0.GCStep(arg_5_0):
	local var_5_0 = os.clock()

	if not arg_5_0.running:
		-- block empty
	elif collectgarbage("step", arg_5_0.step):
		arg_5_0.GCFinal()
	else
		local var_5_1 = os.clock() * 1000 - var_5_0 * 1000

		arg_5_0.gccost = arg_5_0.gccost <= 0 and var_5_1 or arg_5_0.gccost
		arg_5_0.gccost = (arg_5_0.gccost + var_5_1) * 0.5
		arg_5_0.gctick = arg_5_0.gctick + 1

		if arg_5_0.gctick > 300 and arg_5_0.gctick % 30 == 0:
			arg_5_0.CalcStep()

def var_0_0.CalcStep(arg_6_0):
	arg_6_0.step = math.max(arg_6_0.gctick - 60, 30) / 30 * 500 * math.max(1 - math.max(arg_6_0.gccost - 3, 0) * 0.1, 0.1)

def var_0_0.StartWatch(arg_7_0, arg_7_1):
	originalPrint("overhead. start watch")

	local var_7_0 = collectgarbage("count") * var_0_0.R1024

	if arg_7_1 < var_7_0 + 12:
		arg_7_1 = var_7_0 + 12

	arg_7_0.watcher = Timer.New(function()
		if not arg_7_0.running:
			local var_8_0 = collectgarbage("count") * var_0_0.R1024

			if var_8_0 > arg_7_1:
				originalPrint("overhead. start gc " .. var_8_0 .. "MB")

				arg_7_0.running = True

				arg_7_0.CalcStep()

				arg_7_0.gctick = 0
				arg_7_0.gccost = 0

				UpdateBeat.AddListener(arg_7_0.checkHandle), 5, -1)

	arg_7_0.watcher.Start()

def var_0_0.StopWatch(arg_9_0):
	originalPrint("overhead. stop watch")

	if arg_9_0.watcher:
		arg_9_0.watcher.Stop()

		arg_9_0.watcher = None

def var_0_0.WatchStep(arg_10_0):
	local var_10_0 = os.clock()

	if collectgarbage("step", arg_10_0.step):
		originalPrint("overhead. gc complete")

		if IsUnityEditor:
			print("lua mem. " .. collectgarbage("count") * var_0_0.R1024 .. "MB")

		arg_10_0.running = False

		UpdateBeat.RemoveListener(arg_10_0.checkHandle)
	else
		local var_10_1 = os.clock() * 1000 - var_10_0 * 1000

		arg_10_0.gccost = arg_10_0.gccost <= 0 and var_10_1 or arg_10_0.gccost
		arg_10_0.gccost = (arg_10_0.gccost + var_10_1) * 0.5
		arg_10_0.gctick = arg_10_0.gctick + 1

		if arg_10_0.gctick > 300 and arg_10_0.gctick % 30 == 0:
			arg_10_0.CalcStep()

return var_0_0
