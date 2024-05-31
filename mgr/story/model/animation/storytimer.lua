﻿local var_0_0 = class("StoryTimer")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	arg_1_0.duration = arg_1_2
	arg_1_0.func = arg_1_1
	arg_1_0.loop = arg_1_3
end

function var_0_0.Start(arg_2_0)
	arg_2_0.passed = 0
	arg_2_0.running = true
	arg_2_0.paused = nil

	if not arg_2_0.handle then
		arg_2_0.handle = UpdateBeat:CreateListener(arg_2_0.Update, arg_2_0)
	end

	UpdateBeat:AddListener(arg_2_0.handle)
end

function var_0_0.Pause(arg_3_0)
	arg_3_0.paused = true
end

function var_0_0.Resume(arg_4_0)
	arg_4_0.paused = nil
end

function var_0_0.Stop(arg_5_0)
	if not arg_5_0.running then
		return
	end

	arg_5_0.running = false
	arg_5_0.paused = nil
	arg_5_0.passed = 0

	if arg_5_0.handle then
		UpdateBeat:RemoveListener(arg_5_0.handle)
	end
end

function var_0_0.Update(arg_6_0)
	if not arg_6_0.running or arg_6_0.paused then
		return
	end

	arg_6_0.passed = arg_6_0.passed + Time.deltaTime

	if arg_6_0.passed >= arg_6_0.duration then
		arg_6_0.passed = 0

		arg_6_0.func()

		arg_6_0.loop = arg_6_0.loop - 1
	end

	if arg_6_0.loop == 0 then
		arg_6_0:Stop()
	end
end

return var_0_0
