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

function var_0_1.Init(arg_1_0, arg_1_1)
	GlobalClickEventMgr.Inst:AddPointerDownFunc(function()
		if not arg_1_0.manulStatus then
			return
		end

		arg_1_0:AwakeForAWhile()
	end)

	arg_1_0.manulStatus = false
	arg_1_0.originalBrightnessValue = 0
	arg_1_0.originalBrightnessMode = 0
	arg_1_0.sleepTimeOutCounter = 0

	arg_1_1()
end

function var_0_1.AwakeForAWhile(arg_3_0)
	if not arg_3_0:IsPermissionGranted() then
		arg_3_0:ExitManualMode()

		return
	end

	BrightnessHelper.SetScreenBrightness(arg_3_0.originalBrightnessValue)
	arg_3_0:SetDelayTask()
end

function var_0_1.SetDelayTask(arg_4_0)
	arg_4_0:ClearTask()

	arg_4_0.task = Timer.New(function()
		BrightnessHelper.SetScreenBrightness(math.min(var_0_1.DarkModeBrightness, arg_4_0.originalBrightnessValue))
	end, var_0_1.AutoIntoDarkModeTime)

	arg_4_0.task:Start()
end

function var_0_1.ClearTask(arg_6_0)
	if not arg_6_0.task then
		return
	end

	arg_6_0.task:Stop()

	arg_6_0.task = nil
end

function var_0_1.EnterManualMode(arg_7_0)
	if arg_7_0.manulStatus then
		return
	end

	local var_7_0 = BrightnessHelper.GetValue()

	arg_7_0.originalBrightnessValue = var_7_0

	BrightnessHelper.SetScreenBrightness(math.min(var_0_1.DarkModeBrightness, var_7_0))

	arg_7_0.manulStatus = true
end

function var_0_1.ExitManualMode(arg_8_0)
	if not arg_8_0.manulStatus then
		return
	end

	BrightnessHelper.SetScreenBrightness(arg_8_0.originalBrightnessValue)
	arg_8_0:ClearTask()

	arg_8_0.manulStatus = false
end

function var_0_1.IsPermissionGranted(arg_9_0)
	return BrightnessHelper.IsHavePermission()
end

function var_0_1.RequestPremission(arg_10_0, arg_10_1)
	BrightnessHelper.SetScreenBrightness(BrightnessHelper.GetValue())

	if arg_10_1 then
		FrameTimer.New(function()
			arg_10_1(arg_10_0:IsPermissionGranted())
		end, 2):Start()
	end
end

function var_0_1.SetScreenNeverSleep(arg_12_0, arg_12_1)
	arg_12_1 = tobool(arg_12_1)

	if arg_12_1 then
		if arg_12_0.sleepTimeOutCounter == 0 then
			Screen.sleepTimeout = SleepTimeout.NeverSleep
		end

		arg_12_0.sleepTimeOutCounter = arg_12_0.sleepTimeOutCounter + 1
	else
		arg_12_0.sleepTimeOutCounter = arg_12_0.sleepTimeOutCounter - 1

		assert(arg_12_0.sleepTimeOutCounter >= 0, "InCorrect Call of SetScreenNeverSleep")

		arg_12_0.sleepTimeOutCounter = math.max(0, arg_12_0.sleepTimeOutCounter)

		if arg_12_0.sleepTimeOutCounter == 0 then
			Screen.sleepTimeout = SleepTimeout.SystemSetting
		end
	end
end
