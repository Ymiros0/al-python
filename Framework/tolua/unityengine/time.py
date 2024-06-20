from luatable import table, setmetatable

from tolua import UnityEngine
old_time = UnityEngine.Time
import time

meta = table(
	maximumDeltaTime = 0.3333333,
	frameCount = 1,
	time = 0,
	fixedDeltaTime = 0,
	unscaledTime = 0,
	deltaTime = 0,
	timeSinceLevelLoad = 0,
	realtimeSinceStartup = 0,
	unscaledDeltaTime = 0,
	timeScale = 1,
	fixedTime = 0
)
def fixedDeltaTime(arg_1_0):
	meta.fixedDeltaTime = arg_1_0
	old_time.fixedDeltaTime = arg_1_0
def maximumDeltaTime(arg_2_0):
	meta.maximumDeltaTime = arg_2_0
	old_time.maximumDeltaTime = arg_2_0
def timeScale(arg_3_0):
	meta.timeScale = arg_3_0
	old_time.timeScale = arg_3_0
def captureFramerate(arg_4_0):
	meta.captureFramerate = arg_4_0
	old_time.captureFramerate = arg_4_0
def timeSinceLevelLoad(arg_5_0):
	meta.timeSinceLevelLoad = arg_5_0
var_0_4 = table(
	fixedDeltaTime,
	maximumDeltaTime,
	timeScale,
	captureFramerate,
	timeSinceLevelLoad
)

def __index(arg_6_0, arg_6_1):
	var_6_0 = table.rawget(meta, arg_6_1)

	if var_6_0:
		return var_6_0

	return old_time.__index(old_time, arg_6_1)
meta.__index = __index

def __newindex(arg_7_0, arg_7_1, arg_7_2):
	var_7_0 = table.rawget(var_0_4, arg_7_1)

	if var_7_0:
		return var_7_0(arg_7_2)

	raise PermissionError("Property or indexer `UnityEngine.Time.%s' cannot be assigned to (it is read only)" % arg_7_1)
meta.__newindex = __newindex

Time = table() #Rewrite as class
var_0_6 = 1

def SetDeltaTime(arg_8_0, arg_8_1, arg_8_2):
	meta.deltaTime = arg_8_1
	meta.unscaledDeltaTime = arg_8_2
	var_0_6 -= 1

	if var_0_6 == 0 and old_time:
		meta.time = old_time.time
		meta.timeSinceLevelLoad = old_time.timeSinceLevelLoad
		meta.unscaledTime = old_time.unscaledTime
		meta.realtimeSinceStartup = old_time.realtimeSinceStartup
		meta.frameCount = old_time.frameCount
		var_0_6 = 1000000
	else:
		meta.time += arg_8_1
		meta.realtimeSinceStartup += arg_8_2
		meta.timeSinceLevelLoad += arg_8_1
		meta.unscaledTime += arg_8_2
Time.SetDeltaTime = SetDeltaTime

def SetFixedDelta(arg_9_0, arg_9_1):
	meta.deltaTime = arg_9_1
	meta.fixedDeltaTime = arg_9_1
	meta.fixedTime += arg_9_1
Time.SetFixedDelta = SetFixedDelta

def SetFrameCount(arg_10_0):
	meta.frameCount += 1
Time.SetFrameCount = SetFrameCount

def SetTimeScale(arg_11_0, arg_11_1):
	var_11_0 = meta.timeScale

	meta.timeScale = arg_11_1
	old_time.timeScale = arg_11_1

	return var_11_0
Time.SetTimeScale = SetTimeScale

def GetTimestamp(arg_12_0):
	return time.time()
Time.GetTimestamp = GetTimestamp



setmetatable(Time, meta)

if old_time != None:
	meta.maximumDeltaTime = old_time.maximumDeltaTime
	meta.timeScale = old_time.timeScale

