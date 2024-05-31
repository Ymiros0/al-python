﻿FrameListener = class("FrameListener")

local var_0_0 = FrameListener

function var_0_0.Ctor(arg_1_0)
	arg_1_0.jobs = {}
end

function var_0_0.UnShift(arg_2_0, ...)
	local var_2_0 = {
		...
	}

	for iter_2_0 = #var_2_0, 1, -1 do
		table.insert(arg_2_0.jobs, 1, var_2_0[iter_2_0])
	end

	arg_2_0:TryStart()
end

function var_0_0.Push(arg_3_0, ...)
	local var_3_0 = {
		...
	}

	for iter_3_0 = 1, #var_3_0 do
		table.insert(arg_3_0.jobs, var_3_0[iter_3_0])
	end

	arg_3_0:TryStart()
end

function var_0_0.Remove(arg_4_0, arg_4_1)
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.jobs) do
		if iter_4_1 == arg_4_1 then
			table.remove(arg_4_0.jobs, iter_4_0)
			arg_4_0:TryStop()

			break
		end
	end
end

function var_0_0.TryStart(arg_5_0)
	if not arg_5_0.running and #arg_5_0.jobs > 0 then
		arg_5_0.running = true

		UpdateBeat:Add(arg_5_0.Update, arg_5_0)
	end
end

function var_0_0.TryStop(arg_6_0)
	if arg_6_0.running and #arg_6_0.jobs == 0 then
		UpdateBeat:Remove(arg_6_0.Update, arg_6_0)

		arg_6_0.running = false
	end
end

function var_0_0.Update(arg_7_0)
	if #arg_7_0.jobs == 0 then
		arg_7_0:TryStop()
	else
		table.remove(arg_7_0.jobs, 1)()
	end
end

return var_0_0
