﻿local var_0_0 = setmetatable
local var_0_1 = UpdateBeat
local var_0_2 = CoUpdateBeat
local var_0_3 = Time

Timer = {
	loop = 1,
	running = false,
	time = 0,
	duration = 1,
	scale = false
}

local var_0_4 = Timer
local var_0_5 = {
	__index = var_0_4
}

function var_0_4.New(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	assert(arg_1_1 > 0, "定时器间隔不能小于等于0！：" .. arg_1_1)

	arg_1_3 = arg_1_3 or false
	arg_1_2 = arg_1_2 or 1

	return var_0_0({
		running = false,
		func = arg_1_0,
		duration = arg_1_1,
		time = arg_1_1,
		loop = arg_1_2,
		scale = arg_1_3
	}, var_0_5)
end

function var_0_4.Start(arg_2_0)
	assert(arg_2_0.running == false, "对已经启动的定时器执行启动！")

	arg_2_0.running = true
	arg_2_0.paused = nil

	if not arg_2_0.handle then
		arg_2_0.handle = var_0_1:CreateListener(arg_2_0.Update, arg_2_0)
	end

	var_0_1:AddListener(arg_2_0.handle)
end

function var_0_4.Reset(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4)
	arg_3_0.duration = arg_3_2 or arg_3_0.duration

	assert(arg_3_0.duration > 0, "定时器间隔不能小于等于0！：" .. arg_3_0.duration)

	arg_3_0.loop = arg_3_3 or arg_3_0.loop
	arg_3_0.scale = arg_3_4 or arg_3_0.scale
	arg_3_0.func = arg_3_1 or arg_3_0.func
	arg_3_0.time = arg_3_2 or arg_3_0.time
	arg_3_0.running = false
	arg_3_0.paused = nil
end

function var_0_4.SetScale(arg_4_0, arg_4_1)
	arg_4_0.scale = arg_4_1
end

function var_0_4.Stop(arg_5_0)
	if not arg_5_0.running then
		return
	end

	arg_5_0.running = false
	arg_5_0.paused = nil
	arg_5_0.time = 0

	if arg_5_0.handle then
		var_0_1:RemoveListener(arg_5_0.handle)
	end
end

function var_0_4.Pause(arg_6_0)
	arg_6_0.paused = true
end

function var_0_4.Resume(arg_7_0)
	arg_7_0.paused = nil
end

function var_0_4.Update(arg_8_0)
	if not arg_8_0.running or arg_8_0.paused then
		return
	end

	local var_8_0 = arg_8_0.scale and var_0_3.deltaTime or var_0_3.unscaledDeltaTime

	arg_8_0.time = arg_8_0.time - var_8_0

	local var_8_1 = 0

	while arg_8_0.time <= 0 and var_8_1 < 6 do
		var_8_1 = var_8_1 + 1

		arg_8_0.func(arg_8_0)

		if arg_8_0.loop > 0 then
			arg_8_0.loop = arg_8_0.loop - 1
			arg_8_0.time = arg_8_0.time + arg_8_0.duration
		end

		if arg_8_0.loop == 0 then
			arg_8_0:Stop()

			return
		elseif arg_8_0.loop < 0 then
			arg_8_0.time = arg_8_0.time + arg_8_0.duration
		end
	end
end

FrameTimer = {}

local var_0_6 = FrameTimer
local var_0_7 = {
	__index = var_0_6
}

function var_0_6.New(arg_9_0, arg_9_1, arg_9_2)
	local var_9_0 = var_0_3.frameCount + arg_9_1

	arg_9_2 = arg_9_2 or 1

	return var_0_0({
		running = false,
		func = arg_9_0,
		loop = arg_9_2,
		duration = arg_9_1,
		count = var_9_0
	}, var_0_7)
end

function var_0_6.Reset(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	arg_10_0.func = arg_10_1
	arg_10_0.duration = arg_10_2
	arg_10_0.loop = arg_10_3
	arg_10_0.count = var_0_3.frameCount + arg_10_2
end

function var_0_6.Start(arg_11_0)
	if not arg_11_0.handle then
		arg_11_0.handle = var_0_2:CreateListener(arg_11_0.Update, arg_11_0)
	end

	var_0_2:AddListener(arg_11_0.handle)

	arg_11_0.running = true
end

function var_0_6.Stop(arg_12_0)
	arg_12_0.running = false

	if arg_12_0.handle then
		var_0_2:RemoveListener(arg_12_0.handle)
	end
end

function var_0_6.Update(arg_13_0)
	if not arg_13_0.running then
		return
	end

	if var_0_3.frameCount >= arg_13_0.count then
		arg_13_0.func()

		if arg_13_0.loop > 0 then
			arg_13_0.loop = arg_13_0.loop - 1
		end

		if arg_13_0.loop == 0 then
			arg_13_0:Stop()
		else
			arg_13_0.count = var_0_3.frameCount + arg_13_0.duration
		end
	end
end

CoTimer = {}

local var_0_8 = CoTimer
local var_0_9 = {
	__index = var_0_8
}

function var_0_8.New(arg_14_0, arg_14_1, arg_14_2)
	arg_14_2 = arg_14_2 or 1

	return var_0_0({
		running = false,
		duration = arg_14_1,
		loop = arg_14_2,
		func = arg_14_0,
		time = arg_14_1
	}, var_0_9)
end

function var_0_8.Start(arg_15_0)
	if not arg_15_0.handle then
		arg_15_0.handle = var_0_2:CreateListener(arg_15_0.Update, arg_15_0)
	end

	arg_15_0.running = true

	var_0_2:AddListener(arg_15_0.handle)
end

function var_0_8.Reset(arg_16_0, arg_16_1, arg_16_2, arg_16_3)
	arg_16_0.duration = arg_16_2
	arg_16_0.loop = arg_16_3 or 1
	arg_16_0.func = arg_16_1
	arg_16_0.time = arg_16_2
end

function var_0_8.Stop(arg_17_0)
	arg_17_0.running = false

	if arg_17_0.handle then
		var_0_2:RemoveListener(arg_17_0.handle)
	end
end

function var_0_8.Update(arg_18_0)
	if not arg_18_0.running then
		return
	end

	if arg_18_0.time <= 0 then
		arg_18_0.func()

		if arg_18_0.loop > 0 then
			arg_18_0.loop = arg_18_0.loop - 1
			arg_18_0.time = arg_18_0.time + arg_18_0.duration
		end

		if arg_18_0.loop == 0 then
			arg_18_0:Stop()
		elseif arg_18_0.loop < 0 then
			arg_18_0.time = arg_18_0.time + arg_18_0.duration
		end
	end

	arg_18_0.time = arg_18_0.time - var_0_3.deltaTime
end
