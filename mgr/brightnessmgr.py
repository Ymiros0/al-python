pg = pg or {}

local var_0_0 = pg
local var_0_1 = singletonClass("BrightnessMgr")

var_0_0.BrightnessMgr = var_0_1
var_0_1.AutoIntoDarkModeTime = 10
var_0_1.DarkModeBrightness = 0.1
var_0_1.BrightnessMode = {
	AUTO_ANDROID = 1,
	MANUAL_ANDROID = 0,
	MANUAL_IOS = 2
}

def var_0_1.Init(arg_1_0, arg_1_1):
	GlobalClickEventMgr.Inst.AddPointerDownFunc(function()
		if not arg_1_0.manulStatus:
			return

		arg_1_0.AwakeForAWhile())

	arg_1_0.manulStatus = False
	arg_1_0.originalBrightnessValue = 0
	arg_1_0.originalBrightnessMode = 0
	arg_1_0.sleepTimeOutCounter = 0

	arg_1_1()

def var_0_1.AwakeForAWhile(arg_3_0):
	if not arg_3_0.IsPermissionGranted():
		arg_3_0.ExitManualMode()

		return

	BrightnessHelper.SetScreenBrightness(arg_3_0.originalBrightnessValue)
	arg_3_0.SetDelayTask()

def var_0_1.SetDelayTask(arg_4_0):
	arg_4_0.ClearTask()

	arg_4_0.task = Timer.New(function()
		BrightnessHelper.SetScreenBrightness(math.min(var_0_1.DarkModeBrightness, arg_4_0.originalBrightnessValue)), var_0_1.AutoIntoDarkModeTime)

	arg_4_0.task.Start()

def var_0_1.ClearTask(arg_6_0):
	if not arg_6_0.task:
		return

	arg_6_0.task.Stop()

	arg_6_0.task = None

def var_0_1.EnterManualMode(arg_7_0):
	if arg_7_0.manulStatus:
		return

	local var_7_0 = BrightnessHelper.GetValue()

	arg_7_0.originalBrightnessValue = var_7_0

	BrightnessHelper.SetScreenBrightness(math.min(var_0_1.DarkModeBrightness, var_7_0))

	arg_7_0.manulStatus = True

def var_0_1.ExitManualMode(arg_8_0):
	if not arg_8_0.manulStatus:
		return

	BrightnessHelper.SetScreenBrightness(arg_8_0.originalBrightnessValue)
	arg_8_0.ClearTask()

	arg_8_0.manulStatus = False

def var_0_1.IsPermissionGranted(arg_9_0):
	return BrightnessHelper.IsHavePermission()

def var_0_1.RequestPremission(arg_10_0, arg_10_1):
	BrightnessHelper.SetScreenBrightness(BrightnessHelper.GetValue())

	if arg_10_1:
		FrameTimer.New(function()
			arg_10_1(arg_10_0.IsPermissionGranted()), 2).Start()

def var_0_1.SetScreenNeverSleep(arg_12_0, arg_12_1):
	arg_12_1 = tobool(arg_12_1)

	if arg_12_1:
		if arg_12_0.sleepTimeOutCounter == 0:
			Screen.sleepTimeout = SleepTimeout.NeverSleep

		arg_12_0.sleepTimeOutCounter = arg_12_0.sleepTimeOutCounter + 1
	else
		arg_12_0.sleepTimeOutCounter = arg_12_0.sleepTimeOutCounter - 1

		assert(arg_12_0.sleepTimeOutCounter >= 0, "InCorrect Call of SetScreenNeverSleep")

		arg_12_0.sleepTimeOutCounter = math.max(0, arg_12_0.sleepTimeOutCounter)

		if arg_12_0.sleepTimeOutCounter == 0:
			Screen.sleepTimeout = SleepTimeout.SystemSetting
