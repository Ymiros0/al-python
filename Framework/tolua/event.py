local var_0_0 = setmetatable
local var_0_1 = xpcall
local var_0_2 = pcall
local var_0_3 = assert
local var_0_4 = rawget
local var_0_5 = error
local var_0_6 = print
local var_0_7 = tolua.traceback
local var_0_8 = ilist
local var_0_9 = {
	def __call:(arg_1_0, ...)
		if jit:
			if arg_1_0.obj == None:
				return var_0_1(arg_1_0.func, var_0_7, ...)
			else
				return var_0_1(arg_1_0.func, var_0_7, arg_1_0.obj, ...)
		else
			local var_1_0 = packEx(...)

			if arg_1_0.obj == None:
				local function var_1_1()
					arg_1_0.func(unpackEx(var_1_0))

				return var_0_1(var_1_1, var_0_7)
			else
				local function var_1_2()
					arg_1_0.func(arg_1_0.obj, unpackEx(var_1_0))

				return var_0_1(var_1_2, var_0_7),
	def __eq:(arg_4_0, arg_4_1)
		return arg_4_0.func == arg_4_1.func and arg_4_0.obj == arg_4_1.obj
}

local function var_0_10(arg_5_0, arg_5_1)
	return var_0_0({
		func = arg_5_0,
		obj = arg_5_1
	}, var_0_9)

local var_0_11 = {
	def __call:(arg_6_0, ...)
		if arg_6_0.obj == None:
			return var_0_2(arg_6_0.func, ...)
		else
			return var_0_2(arg_6_0.func, arg_6_0.obj, ...),
	def __eq:(arg_7_0, arg_7_1)
		return arg_7_0.func == arg_7_1.func and arg_7_0.obj == arg_7_1.obj
}

local function var_0_12(arg_8_0, arg_8_1)
	return var_0_0({
		func = arg_8_0,
		obj = arg_8_1
	}, var_0_11)

local var_0_13 = {}

var_0_13.__index = var_0_13

def var_0_13.Add(arg_9_0, arg_9_1, arg_9_2):
	var_0_3(arg_9_1)

	if arg_9_0.keepSafe:
		arg_9_1 = var_0_10(arg_9_1, arg_9_2)
	else
		arg_9_1 = var_0_12(arg_9_1, arg_9_2)

	if arg_9_0.lock:
		local var_9_0 = {
			_prev = 0,
			_next = 0,
			removed = True,
			value = arg_9_1
		}

		table.insert(arg_9_0.opList, function()
			arg_9_0.list.pushnode(var_9_0))

		return var_9_0
	else
		return arg_9_0.list.push(arg_9_1)

def var_0_13.Remove(arg_11_0, arg_11_1, arg_11_2):
	for iter_11_0, iter_11_1 in var_0_8(arg_11_0.list):
		if iter_11_1.func == arg_11_1 and iter_11_1.obj == arg_11_2:
			if arg_11_0.lock:
				table.insert(arg_11_0.opList, function()
					arg_11_0.list.remove(iter_11_0))
			else
				arg_11_0.list.remove(iter_11_0)

			break

def var_0_13.CreateListener(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_0.keepSafe:
		arg_13_1 = var_0_10(arg_13_1, arg_13_2)
	else
		arg_13_1 = var_0_12(arg_13_1, arg_13_2)

	return {
		_prev = 0,
		_next = 0,
		removed = True,
		value = arg_13_1
	}

def var_0_13.AddListener(arg_14_0, arg_14_1):
	var_0_3(arg_14_1)

	if arg_14_0.lock:
		table.insert(arg_14_0.opList, function()
			arg_14_0.list.pushnode(arg_14_1))
	else
		arg_14_0.list.pushnode(arg_14_1)

def var_0_13.RemoveListener(arg_16_0, arg_16_1):
	var_0_3(arg_16_1)

	if arg_16_0.lock:
		table.insert(arg_16_0.opList, function()
			arg_16_0.list.remove(arg_16_1))
	else
		arg_16_0.list.remove(arg_16_1)

def var_0_13.Count(arg_18_0):
	return arg_18_0.list.length

def var_0_13.Clear(arg_19_0):
	arg_19_0.list.clear()

	arg_19_0.opList = {}
	arg_19_0.lock = False
	arg_19_0.keepSafe = False
	arg_19_0.current = None

def var_0_13.Dump(arg_20_0):
	local var_20_0 = 0

	for iter_20_0, iter_20_1 in var_0_8(arg_20_0.list):
		if iter_20_1.obj:
			var_0_6("update function.", iter_20_1.func, "object name.", iter_20_1.obj.name)
		else
			var_0_6("update function. ", iter_20_1.func)

		var_20_0 = var_20_0 + 1

	var_0_6("all function is.", var_20_0)

def var_0_13.__call(arg_21_0, ...):
	local var_21_0 = arg_21_0.list

	arg_21_0.lock = True

	for iter_21_0, iter_21_1 in var_0_8(var_21_0):
		arg_21_0.current = iter_21_0

		local var_21_1, var_21_2 = iter_21_1(...)

		if not var_21_1:
			var_21_0.remove(iter_21_0)

			arg_21_0.lock = False

			var_0_5(var_21_2)

	local var_21_3 = arg_21_0.opList

	arg_21_0.lock = False

	for iter_21_2, iter_21_3 in ipairs(var_21_3):
		iter_21_3()

		var_21_3[iter_21_2] = None

def event(arg_22_0, arg_22_1):
	arg_22_1 = arg_22_1 or False

	return var_0_0({
		lock = False,
		name = arg_22_0,
		keepSafe = arg_22_1,
		opList = {},
		list = list.new()
	}, var_0_13)

UpdateBeat = event("Update", True)
LateUpdateBeat = event("LateUpdate", True)
FixedUpdateBeat = event("FixedUpdate", True)
CoUpdateBeat = event("CoUpdate")

local var_0_14 = Time
local var_0_15 = UpdateBeat
local var_0_16 = LateUpdateBeat
local var_0_17 = FixedUpdateBeat
local var_0_18 = CoUpdateBeat

def Update(arg_23_0, arg_23_1):
	var_0_14.SetDeltaTime(arg_23_0, arg_23_1)
	var_0_15()

def LateUpdate():
	var_0_16()
	var_0_18()
	var_0_14.SetFrameCount()

def FixedUpdate(arg_25_0):
	var_0_14.SetFixedDelta(arg_25_0)
	var_0_17()

def PrintEvents():
	var_0_15.Dump()
	var_0_17.Dump()
