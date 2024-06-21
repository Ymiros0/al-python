from luatable import table, setmetatable
allist = table()

allist.__index = allist

def _(arg_1_0):
	var_1_0 = table(
		_next = 0,
		length = 0,
		_prev = 0
	)

	var_1_0._prev = var_1_0
	var_1_0._next = var_1_0

	return setmetatable(var_1_0, allist)
allist.new = _

def _(arg_2_0):
	arg_2_0._next = arg_2_0
	arg_2_0._prev = arg_2_0
	arg_2_0.length = 0
allist.Clear = _

def _(arg_3_0, arg_3_1):
	var_3_0 = table(
		_prev = 0,
		_next = 0,
		removed = False,
		value = arg_3_1
	)

	arg_3_0._prev._next = var_3_0
	var_3_0._next = arg_3_0
	var_3_0._prev = arg_3_0._prev
	arg_3_0._prev = var_3_0
	arg_3_0.length += 1

	return var_3_0
allist.push = _

def _(arg_4_0, arg_4_1):
	if not arg_4_1.removed:
		return

	arg_4_0._prev._next = arg_4_1
	arg_4_1._next = arg_4_0
	arg_4_1._prev = arg_4_0._prev
	arg_4_0._prev = arg_4_1
	arg_4_1.removed = False
	arg_4_0.length += 1
allist.pushnode = _

def _(arg_5_0):
	var_5_0 = arg_5_0._prev

	arg_5_0.remove(arg_5_0, var_5_0)

	return var_5_0.value
allist.Pop = _

def _(arg_6_0, arg_6_1):
	var_6_0 = table(
		_prev = 0,
		_next = 0,
		removed = False,
		value = arg_6_1
	)

	arg_6_0._next._prev = var_6_0
	var_6_0._prev = arg_6_0
	var_6_0._next = arg_6_0._next
	arg_6_0._next = var_6_0
	arg_6_0.length += 1

	return var_6_0
allist.unshift = _

def _(arg_7_0):
	var_7_0 = arg_7_0._next

	arg_7_0.remove(arg_7_0, var_7_0)

	return var_7_0.value
allist.shift = _

def _(arg_8_0, arg_8_1):
	if arg_8_1.removed:
		return

	var_8_0 = arg_8_1._prev
	var_8_1 = arg_8_1._next

	var_8_1._prev = var_8_0
	var_8_0._next = var_8_1
	arg_8_0.length = max(0, arg_8_0.length - 1)
	arg_8_1.removed = True
allist.remove = _

def _(arg_9_0, arg_9_1, arg_9_2):
	arg_9_2 = arg_9_2 or arg_9_0

	while True:
		if arg_9_1 == arg_9_2.value:
			return arg_9_2
		arg_9_2 = arg_9_2._next
		if arg_9_2 == arg_9_0:
			return
allist.Find = _

def _(arg_10_0, arg_10_1, arg_10_2):
	arg_10_2 = arg_10_2 or arg_10_0

	while True:
		if arg_10_1 == arg_10_2.value:
			return arg_10_2

		arg_10_2 = arg_10_2._prev
		if arg_10_2 == arg_10_0:
			return
allist.findlast = _

def _(arg_11_0, arg_11_1):
	var_11_0 = arg_11_1._next

	if var_11_0 != arg_11_0:
		return var_11_0, var_11_0.value

	return
allist.next = _

def _(arg_12_0, arg_12_1):
	var_12_0 = arg_12_1._prev

	if var_12_0 != arg_12_0:
		return var_12_0, var_12_0.value

	return
allist.prev = _

def _(arg_13_0, arg_13_1):
	var_13_0 = arg_13_0.find(arg_13_0, arg_13_1)

	if var_13_0:
		arg_13_0.remove(arg_13_0, var_13_0)
allist.erase = _

def _(arg_14_0, arg_14_1, arg_14_2):
	if not arg_14_2:
		return arg_14_0.push(arg_14_0, arg_14_1)

	var_14_0 = table(
		_prev = 0,
		_next = 0,
		removed = False,
		value = arg_14_1
	)

	if arg_14_2._next:
		arg_14_2._next._prev = var_14_0
		var_14_0._next = arg_14_2._next
	else:
		arg_14_0.last = var_14_0

	var_14_0._prev = arg_14_2
	arg_14_2._next = var_14_0
	arg_14_0.length += 1

	return var_14_0
allist.Insert = _

def _(arg_15_0):
	return arg_15_0._next.value
allist.head = _

def _(arg_16_0):
	return arg_16_0._prev.value
allist.tail = _

def _(arg_17_0):
	var_17_0 = allist.new(allist)

	for iter_17_0, iter_17_1 in allist.next, arg_17_0, arg_17_0:
		var_17_0.push(var_17_0, iter_17_1)

	return var_17_0
allist.clone = _

def ilist(arg_18_0):
	return allist.next, arg_18_0, arg_18_0

def rilist(arg_19_0):
	return allist.prev, arg_19_0, arg_19_0

setmetatable(allist, table(
	__call = allist.new
))