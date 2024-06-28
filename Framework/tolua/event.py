from luatable import setmetatable, table, ipairs

from Framework.tolua.unityengine.Time import Time
import xpcall
import pcall
import traceback #tolua.traceback? debug.traceback?
import packEx
import unpackEx
import jit
from Framework.tolua.list import ilist
def __call(arg_1_0, *args): #?????????????
	if jit:
		if arg_1_0.obj == None:
			return xpcall(arg_1_0.func, traceback, *args)
		else:
			return xpcall(arg_1_0.func, traceback, arg_1_0.obj, *args)
	else:
		var_1_0 = packEx(*args)

		if arg_1_0.obj == None:
			def var_1_1():
				arg_1_0.func(unpackEx(var_1_0))

			return xpcall(var_1_1, traceback)
		else:
			def var_1_2():
				arg_1_0.func(arg_1_0.obj, unpackEx(var_1_0))

			return xpcall(var_1_2, traceback),
def __eq(arg_4_0, arg_4_1):
	return arg_4_0.func == arg_4_1.func and arg_4_0.obj == arg_4_1.obj

var_0_9 = table(
	__call = __call,
	__eq = __eq
)

def var_0_10(arg_5_0, arg_5_1):
	return setmetatable(table(
		func = arg_5_0,
		obj = arg_5_1
	), var_0_9)


def __call(arg_6_0, *args):
	if arg_6_0.obj == None:
		return pcall(arg_6_0.func, *args)
	else:
		return pcall(arg_6_0.func, arg_6_0.obj, *args),
def __eq(arg_7_0, arg_7_1):
	return arg_7_0.func == arg_7_1.func and arg_7_0.obj == arg_7_1.obj

var_0_11 = table(
	__call = __call,
	__eq = __eq
)

def var_0_12(arg_8_0, arg_8_1):
	return setmetatable(table(
		func = arg_8_0,
		obj = arg_8_1
	), var_0_11)

var_0_13 = table()

var_0_13.__index = var_0_13

def Add(arg_9_0, arg_9_1, arg_9_2):
	assert arg_9_1

	if arg_9_0.keepSafe:
		arg_9_1 = var_0_10(arg_9_1, arg_9_2)
	else:
		arg_9_1 = var_0_12(arg_9_1, arg_9_2)

	if arg_9_0.lock:
		var_9_0 = table(
			_prev = 0,
			_next = 0,
			removed = True,
			value = arg_9_1
		)

		table.insert(arg_9_0.opList, lambda: arg_9_0.list.pushnode(var_9_0))

		return var_9_0
	else:
		return arg_9_0.list.push(arg_9_1)
var_0_13.Add = Add

def Remove(arg_11_0, arg_11_1, arg_11_2):
	for iter_11_0, iter_11_1 in ilist(arg_11_0.list):
		if iter_11_1.func == arg_11_1 and iter_11_1.obj == arg_11_2:
			if arg_11_0.lock:
				table.insert(arg_11_0.opList, lambda: arg_11_0.list.remove(iter_11_0))
			else:
				arg_11_0.list.remove(iter_11_0)

			break
var_0_13.Remove = Remove

def CreateListener(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_0.keepSafe:
		arg_13_1 = var_0_10(arg_13_1, arg_13_2)
	else:
		arg_13_1 = var_0_12(arg_13_1, arg_13_2)

	return table(
		_prev = 0,
		_next = 0,
		removed = True,
		value = arg_13_1
	)
var_0_13.CreateListener = CreateListener

def AddListener(arg_14_0, arg_14_1):
	assert arg_14_1

	if arg_14_0.lock:
		table.insert(arg_14_0.opList, lambda: arg_14_0.list.pushnode(arg_14_1))
	else:
		arg_14_0.list.pushnode(arg_14_1)
var_0_13.AddListener = AddListener

def RemoveListener(arg_16_0, arg_16_1):
	assert arg_16_1

	if arg_16_0.lock:
		table.insert(arg_16_0.opList, lambda: arg_16_0.list.remove(arg_16_1))
	else:
		arg_16_0.list.remove(arg_16_1)
var_0_13.RemoveListener = RemoveListener

def Count(arg_18_0):
	return arg_18_0.list.length
var_0_13.Count = Count

def Clear(arg_19_0):
	arg_19_0.list.clear()

	arg_19_0.opList = table()
	arg_19_0.lock = False
	arg_19_0.keepSafe = False
	arg_19_0.current = None
var_0_13.Clear = Clear

def Dump(arg_20_0):
	var_20_0 = 0

	for iter_20_0, iter_20_1 in ilist(arg_20_0.list):
		if iter_20_1.obj:
			print("update function.", iter_20_1.func, "object name.", iter_20_1.obj.name)
		else:
			print("update function. ", iter_20_1.func)

		var_20_0 = var_20_0 + 1

	print("all function is.", var_20_0)
var_0_13.Dump = Dump

def __call(arg_21_0, *args):
	var_21_0 = arg_21_0.list

	arg_21_0.lock = True

	for iter_21_0, iter_21_1 in ilist(var_21_0):
		arg_21_0.current = iter_21_0

		var_21_1, var_21_2 = iter_21_1(*args)

		if not var_21_1:
			var_21_0.remove(iter_21_0)

			arg_21_0.lock = False

			raise BaseException(var_21_2)

	var_21_3 = arg_21_0.opList

	arg_21_0.lock = False

	for iter_21_2, iter_21_3 in ipairs(var_21_3):
		iter_21_3()

		var_21_3[iter_21_2] = None
var_0_13.__call = __call

def event(arg_22_0, arg_22_1=False):

	return setmetatable(table(
		lock = False,
		name = arg_22_0,
		keepSafe = arg_22_1,
		opList = table(),
		list = list.new()
	), var_0_13)

UpdateBeat = event("Update", True)
LateUpdateBeat = event("LateUpdate", True)
FixedUpdateBeat = event("FixedUpdate", True)
CoUpdateBeat = event("CoUpdate")


def Update(arg_23_0, arg_23_1):
	Time.SetDeltaTime(arg_23_0, arg_23_1)
	UpdateBeat()

def LateUpdate():
	LateUpdateBeat()
	CoUpdateBeat()
	Time.SetFrameCount()

def FixedUpdate(arg_25_0):
	Time.SetFixedDelta(arg_25_0)
	FixedUpdateBeat()

def PrintEvents():
	UpdateBeat.Dump()
	FixedUpdateBeat.Dump()
