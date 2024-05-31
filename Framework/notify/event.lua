﻿local var_0_0 = require
local var_0_1 = setmetatable
local var_0_2 = string
local var_0_3 = error
local var_0_4 = unpack
local var_0_5 = var_0_0("Framework.notify.double-queue")
local var_0_6 = ":"
local var_0_7 = {}
local var_0_8 = {}
local var_0_9 = {
	__index = var_0_8
}

local function var_0_10()
	return {
		handlers = var_0_5.New(),
		pre_emits = var_0_5.New(),
		post_emits = var_0_5.New(),
		blocked_handlers = {},
		subevents = {}
	}
end

local function var_0_11(arg_2_0)
	local var_2_0 = {}

	for iter_2_0 in var_0_2.gmatch(arg_2_0, "[^" .. var_0_6 .. "]+") do
		var_2_0[#var_2_0 + 1] = iter_2_0
	end

	return var_2_0
end

local function var_0_12(arg_3_0, arg_3_1)
	local var_3_0 = var_0_11(arg_3_1)
	local var_3_1 = arg_3_0.events[var_3_0[1]] or var_0_10()

	arg_3_0.events[var_3_0[1]] = var_3_1

	for iter_3_0 = 2, #var_3_0 do
		local var_3_2 = var_3_1.subevents[var_3_0[iter_3_0]] or var_0_10()

		var_3_1.subevents[var_3_0[iter_3_0]] = var_3_2
		var_3_1 = var_3_2
	end

	return var_3_1
end

local function var_0_13(arg_4_0, arg_4_1)
	local var_4_0 = var_0_11(arg_4_1)
	local var_4_1 = arg_4_0.events[var_4_0[1]]

	if not var_4_1 then
		return true
	end

	for iter_4_0 = 2, #var_4_0 do
		local var_4_2 = var_4_1.subevents[var_4_0[iter_4_0]]

		if not var_4_2 then
			return true
		end

		var_4_1 = var_4_2
	end

	return false
end

local function var_0_14(arg_5_0, arg_5_1)
	local var_5_0 = var_0_11(arg_5_1)
	local var_5_1 = 2
	local var_5_2 = arg_5_0.events[var_5_0[1]]

	return function()
		if not var_5_2 then
			return
		end

		local var_6_0 = var_5_2

		if var_5_0[var_5_1] then
			var_5_2 = var_5_2.subevents[var_5_0[var_5_1]]
			var_5_1 = var_5_1 + 1
		else
			var_5_2 = nil
		end

		return var_6_0
	end
end

local function var_0_15(arg_7_0, arg_7_1)
	local var_7_0 = var_0_5.New()
	local var_7_1 = var_0_5.New()

	for iter_7_0 in var_0_14(arg_7_0, arg_7_1) do
		for iter_7_1 in iter_7_0.pre_emits:get_iterator() do
			iter_7_1(arg_7_1)
		end

		var_7_0:push_back(iter_7_0)
		var_7_1:push_front(iter_7_0)
	end

	return var_7_0, var_7_1
end

local function var_0_16(arg_8_0, arg_8_1)
	for iter_8_0 in arg_8_1:get_iterator() do
		for iter_8_1 in iter_8_0.post_emits:get_iterator() do
			iter_8_1(arg_8_0)
		end
	end
end

local function var_0_17(arg_9_0, arg_9_1)
	for iter_9_0 in arg_9_1.nodes:get_iterator() do
		for iter_9_1 in iter_9_0.handlers:get_iterator() do
			if arg_9_0.stopped then
				return
			end

			if iter_9_0.blocked_handlers[iter_9_1] == 0 then
				if arg_9_1.accumulator then
					arg_9_1.accumulator(iter_9_1(arg_9_1.event_name, unpackEx(arg_9_1.args)))
				else
					iter_9_1(arg_9_1.event_name, unpackEx(arg_9_1.args))
				end
			end
		end
	end
end

function var_0_7.New()
	return var_0_1({
		stopped = false,
		events = {}
	}, var_0_9)
end

function var_0_8.connect(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = var_0_12(arg_11_0, arg_11_1)

	var_11_0.handlers:push_back(arg_11_2)

	if not var_11_0.blocked_handlers[arg_11_2] then
		var_11_0.blocked_handlers[arg_11_2] = 0
	end
end

function var_0_8.disconnect(arg_12_0, arg_12_1, arg_12_2)
	if var_0_13(arg_12_0, arg_12_1) then
		return
	end

	local var_12_0 = var_0_12(arg_12_0, arg_12_1)

	var_12_0.handlers:remove(arg_12_2)

	var_12_0.blocked_handlers[arg_12_2] = nil
end

function var_0_8.chectConnect(arg_13_0, arg_13_1)
	return not var_0_13(arg_13_0, arg_13_1)
end

function var_0_8.block(arg_14_0, arg_14_1, arg_14_2)
	if var_0_13(arg_14_0, arg_14_1) then
		return
	end

	local var_14_0 = var_0_12(arg_14_0, arg_14_1)
	local var_14_1 = var_14_0.blocked_handlers[arg_14_2]

	if var_14_1 then
		var_14_0.blocked_handlers[arg_14_2] = var_14_1 + 1
	end
end

function var_0_8.unblock(arg_15_0, arg_15_1, arg_15_2)
	if var_0_13(arg_15_0, arg_15_1) then
		return
	end

	local var_15_0 = var_0_12(arg_15_0, arg_15_1)

	if var_15_0.blocked_handlers[arg_15_2] and var_15_0.blocked_handlers[arg_15_2] > 0 then
		var_15_0.blocked_handlers[arg_15_2] = var_15_0.blocked_handlers[arg_15_2] - 1
	end
end

function var_0_8.emit(arg_16_0, arg_16_1, ...)
	arg_16_0.stopped = false

	local var_16_0, var_16_1 = var_0_15(arg_16_0, arg_16_1)

	var_0_17(arg_16_0, {
		event_name = arg_16_1,
		nodes = var_16_0,
		args = packEx(...)
	})
	var_0_16(arg_16_1, var_16_1)
end

function var_0_8.emit_with_accumulator(arg_17_0, arg_17_1, arg_17_2, ...)
	arg_17_0.stopped = false

	local var_17_0, var_17_1 = var_0_15(arg_17_0, arg_17_1)

	var_0_17(arg_17_0, {
		event_name = arg_17_1,
		nodes = var_17_0,
		accumulator = arg_17_2,
		args = packEx(...)
	})
	var_0_16(arg_17_1, var_17_1)
end

function var_0_8.add_pre_emit(arg_18_0, arg_18_1, arg_18_2)
	var_0_12(arg_18_0, arg_18_1).pre_emits:push_back(arg_18_2)
end

function var_0_8.remove_pre_emit(arg_19_0, arg_19_1, arg_19_2)
	if var_0_13(arg_19_0, arg_19_1) then
		return
	end

	var_0_12(arg_19_0, arg_19_1).pre_emits:remove(arg_19_2)
end

function var_0_8.add_post_emit(arg_20_0, arg_20_1, arg_20_2)
	var_0_12(arg_20_0, arg_20_1).post_emits:push_front(arg_20_2)
end

function var_0_8.remove_post_emit(arg_21_0, arg_21_1, arg_21_2)
	if var_0_13(arg_21_0, arg_21_1) then
		return
	end

	var_0_12(arg_21_0, arg_21_1).post_emits:remove(arg_21_2)
end

function var_0_8.stop(arg_22_0)
	arg_22_0.stopped = true
end

function var_0_8.clear(arg_23_0, arg_23_1)
	if not arg_23_1 then
		arg_23_0.events = {}

		return
	end
end

local var_0_18 = var_0_7.New()

function var_0_7.get_global_event()
	return var_0_18
end

return var_0_7
