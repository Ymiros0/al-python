pg = pg or {}

local var_0_0 = pg

var_0_0.MessageCache = class("MessageCache")
var_0_0.MessageCache.DEFAULT_QUEUE_LENGTH = 10000
var_0_0.MessageCache.CMD_KILL = "CMD_KILL"
var_0_0.MessageCache.CMD_PUSH = "CMD_PUSH"
var_0_0.MessageCache.CMD_POP = "CMD_POP"
var_0_0.MessageCache.CMD_FLUSH = "CMD_FLUSH"
var_0_0.MessageCache.OK = "OK"
var_0_0.MessageCache.QUEUE_FULL = "QUEUE_FULL"
var_0_0.MessageCache.EXCEPTION = "EXCEPTION"

local function var_0_1(...)
	return coroutine.yield(...)

local function var_0_2(arg_2_0, arg_2_1, arg_2_2)
	if arg_2_1 == var_0_0.MessageCache.CMD_PUSH:
		local var_2_0 = #arg_2_0.cacheQueue_ + (arg_2_0.curRQLen_ - arg_2_0.curRQPos_)

		if var_2_0 >= arg_2_0.cacheQueueLenLimit_:
			return var_0_2(arg_2_0, var_0_1(var_0_0.MessageCache.QUEUE_FULL, string.format("                    the cache limit length is set with %s, the coming message will be ignored.\n                ", arg_2_0.cacheQueueLenLimit_)))
		else
			table.insert(arg_2_0.cacheQueue_, arg_2_2)

			return var_0_2(arg_2_0, var_0_1(var_0_0.MessageCache.OK, var_2_0 + 1))
	elif arg_2_1 == var_0_0.MessageCache.CMD_POP:
		if arg_2_0.curRQPos_ < arg_2_0.curRQLen_:
			arg_2_0.curRQPos_ = arg_2_0.curRQPos_ + 1

			local var_2_1 = arg_2_0.retrieveQueue_[arg_2_0.curRQPos_]

			arg_2_0.retrieveQueue_[arg_2_0.curRQPos_] = None

			return var_0_2(arg_2_0, var_0_1(var_0_0.MessageCache.OK, var_2_1))
		else
			assert(arg_2_0.curRQPos_ >= arg_2_0.curRQLen_)

			if arg_2_0.cacheQueue_[1]:
				arg_2_0.cacheQueue_, arg_2_0.retrieveQueue_ = arg_2_0.retrieveQueue_, arg_2_0.cacheQueue_
				arg_2_0.curRQPos_ = 1
				arg_2_0.curRQLen_ = #arg_2_0.retrieveQueue_

				local var_2_2 = arg_2_0.retrieveQueue_[arg_2_0.curRQPos_]

				arg_2_0.retrieveQueue_[arg_2_0.curRQPos_] = None

				return var_0_2(arg_2_0, var_0_1(var_0_0.MessageCache.OK, var_2_2))
			else
				return var_0_2(arg_2_0, var_0_1(var_0_0.MessageCache.OK))
	elif arg_2_1 == var_0_0.MessageCache.CMD_KILL:
		local var_2_3 = arg_2_0.curRQPos_
		local var_2_4 = arg_2_0.curRQLen_
		local var_2_5 = 1

		while var_2_3 < var_2_4:
			table.insert(arg_2_0.cacheQueue_, var_2_5, arg_2_0.retrieveQueue_[var_2_3])

			arg_2_0.retrieveQueue_[var_2_3] = None
			var_2_5 = var_2_5 + 1
			var_2_3 = var_2_3 + 1

		arg_2_0.curRQPos_ = 0
		arg_2_0.curRQLen_ = 0

		return var_0_0.MessageCache.OK, arg_2_0.cacheQueue_
	elif arg_2_1 == var_0_0.MessageCache.CMD_FLUSH:
		local var_2_6 = arg_2_0.curRQPos_
		local var_2_7 = arg_2_0.curRQLen_
		local var_2_8 = 1

		while var_2_6 < var_2_7:
			table.insert(arg_2_0.cacheQueue_, var_2_8, arg_2_0.retrieveQueue_[var_2_6])

			arg_2_0.retrieveQueue_[var_2_6] = None
			var_2_8 = var_2_8 + 1
			var_2_6 = var_2_6 + 1

		arg_2_0.curRQPos_ = 0
		arg_2_0.curRQLen_ = 0

		local var_2_9 = arg_2_0.cacheQueue_

		arg_2_0.cacheQueue_ = {}

		return var_0_2(arg_2_0, var_0_1(var_0_0.MessageCache.OK, var_2_9))
	else
		return var_0_2(arg_2_0, var_0_1(var_0_0.MessageCache.EXCEPTION, string.format("unknown cmd type received %s", tostring(arg_2_1))))

local function var_0_3(arg_3_0)
	local var_3_0 = {
		curRQLen_ = 0,
		curRQPos_ = 0,
		cacheQueue_ = {},
		retrieveQueue_ = {},
		cacheQueueLenLimit_ = arg_3_0 or var_0_0.MessageCache.DEFAULT_QUEUE_LENGTH
	}

	return var_0_2(var_3_0, var_0_1(var_0_0.MessageCache.OK))

def var_0_0.MessageCache.Ctor(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0._name = arg_4_1
	arg_4_0._thread = coroutine.create(var_0_3)

	local var_4_0, var_4_1 = coroutine.resume(arg_4_0._thread, arg_4_2)

	assert(var_4_1 == var_0_0.MessageCache.OK)

def var_0_0.MessageCache.Push(arg_5_0, ...):
	local var_5_0 = coroutine.status(arg_5_0._thread)

	if var_5_0 == "suspended":
		local var_5_1, var_5_2, var_5_3 = coroutine.resume(arg_5_0._thread, var_0_0.MessageCache.CMD_PUSH, {
			...
		})

		if var_5_1:
			return var_5_2, var_5_3
		else
			return var_0_0.MessageCache.EXCEPTION, var_5_2
	else
		return var_0_0.MessageCache.EXCEPTION, string.format("current thread status %s,\n            maybe the MessageCache.Destroy() is called before the Push operation.", var_5_0)

def var_0_0.MessageCache.Pop(arg_6_0):
	local var_6_0 = coroutine.status(arg_6_0._thread)

	if var_6_0 == "suspended":
		local var_6_1, var_6_2, var_6_3 = coroutine.resume(arg_6_0._thread, var_0_0.MessageCache.CMD_POP)

		if var_6_1:
			if var_6_2 == var_0_0.MessageCache.OK and var_6_3 != None:
				return var_6_2, unpack(var_6_3)
			else
				return var_6_2, var_6_3
		else
			return var_0_0.MessageCache.EXCEPTION, var_6_2
	else
		return var_0_0.MessageCache.EXCEPTION, string.format("current thread status %s,\n            maybe the MessageCache.Destroy() is called before the Pop operation.", var_6_0)

def var_0_0.MessageCache.Flush(arg_7_0):
	local var_7_0 = coroutine.status(arg_7_0._thread)

	if var_7_0 == "suspended":
		local var_7_1, var_7_2, var_7_3 = coroutine.resume(arg_7_0._thread, var_0_0.MessageCache.CMD_FLUSH)

		if var_7_1:
			return var_7_2, var_7_3
		else
			return var_0_0.MessageCache.EXCEPTION, var_7_2
	else
		return var_0_0.MessageCache.EXCEPTION, string.format("current thread status %s,\n            maybe the MessageCache.Destroy() is called before the Destroy operation.", var_7_0)

def var_0_0.MessageCache.Destroy(arg_8_0):
	local var_8_0 = coroutine.status(arg_8_0._thread)

	if var_8_0 == "suspended":
		local var_8_1, var_8_2, var_8_3 = coroutine.resume(arg_8_0._thread, var_0_0.MessageCache.CMD_KILL)

		if var_8_1:
			return var_8_2, var_8_3
		else
			return var_0_0.MessageCache.EXCEPTION, var_8_2
	else
		return var_0_0.MessageCache.EXCEPTION, string.format("current thread status %s,\n            maybe the MessageCache.Destroy() is called before the Destroy operation.", var_8_0)
