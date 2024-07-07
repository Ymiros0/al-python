from luatable import table, setmetatable
var_0_0 = table(
	funcs = table()
)

var_0_0.__index = var_0_0

def __call(arg_1_0, arg_1_1):
	return var_0_0.new(arg_1_1)

def new(arg_2_0, arg_2_1=None, arg_2_2=None):
	return setmetatable(table(
		_val = arg_2_1,
		chained = arg_2_2 or False
	), arg_2_0)

def iter(arg_3_0):
	if type(arg_3_0) == function:
		return arg_3_0

	for i in arg_3_0:
		yield(i)

def range(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_1 == None:
		arg_5_1 = arg_5_0
		arg_5_0 = 1

	arg_5_2 = arg_5_2 or 1

	var_5_0 = (i for i in range(arg_5_0, arg_5_1, arg_5_2))

	return new(var_5_0)

def identity(arg_7_0):
	return arg_7_0

def chain(arg_8_0):
	arg_8_0.chained = True

	return arg_8_0

def value(arg_9_0):
	return arg_9_0._val

funcs = table()
def each(arg_10_0, arg_10_1):
	for iter_10_0 in var_0_0.iter(arg_10_0):
		arg_10_1(iter_10_0)

	return arg_10_0
funcs.each = each

def map(arg_11_0, arg_11_1):
	var_11_0 = {}

	for iter_11_0 in var_0_0.iter(arg_11_0):
		var_11_0.append(arg_11_1(iter_11_0))


	return var_11_0
funcs.map = map

def reduce(arg_12_0, arg_12_1, arg_12_2):
	for iter_12_0 in var_0_0.iter(arg_12_0):
		arg_12_1 = arg_12_2(arg_12_1, iter_12_0)

	return arg_12_1
funcs.reduce = reduce

def var_0_0.funcs.detect(arg_13_0, arg_13_1):
	for iter_13_0 in var_0_0.iter(arg_13_0):
		if arg_13_1(iter_13_0):
			return iter_13_0

	return None

def var_0_0.funcs.select(arg_14_0, arg_14_1):
	local var_14_0 = {}

	for iter_14_0 in var_0_0.iter(arg_14_0):
		if arg_14_1(iter_14_0):
			var_14_0[#var_14_0 + 1] = iter_14_0

	return var_14_0

def var_0_0.funcs.reject(arg_15_0, arg_15_1):
	local var_15_0 = {}

	for iter_15_0 in var_0_0.iter(arg_15_0):
		if not arg_15_1(iter_15_0):
			var_15_0[#var_15_0 + 1] = iter_15_0

	return var_15_0

def var_0_0.funcs.all(arg_16_0, arg_16_1):
	arg_16_1 = arg_16_1 or var_0_0.identity

	for iter_16_0 in var_0_0.iter(arg_16_0):
		if not arg_16_1(iter_16_0):
			return False

	return True

def var_0_0.funcs.any(arg_17_0, arg_17_1):
	arg_17_1 = arg_17_1 or var_0_0.identity

	for iter_17_0 in var_0_0.iter(arg_17_0):
		if arg_17_1(iter_17_0):
			return True

	return False

def var_0_0.funcs.include(arg_18_0, arg_18_1):
	for iter_18_0 in var_0_0.iter(arg_18_0):
		if iter_18_0 == arg_18_1:
			return True

	return False

def var_0_0.funcs.invoke(arg_19_0, arg_19_1, ...):
	local var_19_0 = packEx(...)

	var_0_0.funcs.each(arg_19_0, function(arg_20_0)
		arg_20_0[arg_19_1](arg_20_0, unpackEx(var_19_0)))

	return arg_19_0

def var_0_0.funcs.pluck(arg_21_0, arg_21_1):
	return var_0_0.funcs.map(arg_21_0, function(arg_22_0)
		return arg_22_0[arg_21_1])

def var_0_0.funcs.min(arg_23_0, arg_23_1):
	arg_23_1 = arg_23_1 or var_0_0.identity

	return var_0_0.funcs.reduce(arg_23_0, {}, function(arg_24_0, arg_24_1)
		if arg_24_0.item == None:
			arg_24_0.item = arg_24_1
			arg_24_0.value = arg_23_1(arg_24_1)
		else
			local var_24_0 = arg_23_1(arg_24_1)

			if var_24_0 < arg_24_0.value:
				arg_24_0.item = arg_24_1
				arg_24_0.value = var_24_0

		return arg_24_0).item

def var_0_0.funcs.max(arg_25_0, arg_25_1):
	arg_25_1 = arg_25_1 or var_0_0.identity

	return var_0_0.funcs.reduce(arg_25_0, {}, function(arg_26_0, arg_26_1)
		if arg_26_0.item == None:
			arg_26_0.item = arg_26_1
			arg_26_0.value = arg_25_1(arg_26_1)
		else
			local var_26_0 = arg_25_1(arg_26_1)

			if var_26_0 > arg_26_0.value:
				arg_26_0.item = arg_26_1
				arg_26_0.value = var_26_0

		return arg_26_0).item

def var_0_0.funcs.to_array(arg_27_0):
	local var_27_0 = {}

	for iter_27_0 in var_0_0.iter(arg_27_0):
		var_27_0[#var_27_0 + 1] = iter_27_0

	return var_27_0

def var_0_0.funcs.reverse(arg_28_0):
	local var_28_0 = {}

	for iter_28_0 in var_0_0.iter(arg_28_0):
		table.insert(var_28_0, 1, iter_28_0)

	return var_28_0

def var_0_0.funcs.sort(arg_29_0, arg_29_1):
	local var_29_0 = arg_29_0

	if type(arg_29_0) == "function":
		var_29_0 = var_0_0.funcs.to_array(arg_29_0)

	table.sort(var_29_0, arg_29_1)

	return var_29_0

def var_0_0.funcs.first(arg_30_0, arg_30_1):
	if arg_30_1 == None:
		return arg_30_0[1]
	else
		local var_30_0 = {}

		arg_30_1 = math.min(arg_30_1, #arg_30_0)

		for iter_30_0 = 1, arg_30_1:
			var_30_0[iter_30_0] = arg_30_0[iter_30_0]

		return var_30_0

def var_0_0.funcs.rest(arg_31_0, arg_31_1):
	arg_31_1 = arg_31_1 or 2

	local var_31_0 = {}

	for iter_31_0 = arg_31_1, #arg_31_0:
		var_31_0[#var_31_0 + 1] = arg_31_0[iter_31_0]

	return var_31_0

def var_0_0.funcs.slice(arg_32_0, arg_32_1, arg_32_2):
	local var_32_0 = {}

	arg_32_1 = math.max(arg_32_1, 1)

	local var_32_1 = math.min(arg_32_1 + arg_32_2 - 1, #arg_32_0)

	for iter_32_0 = arg_32_1, var_32_1:
		var_32_0[#var_32_0 + 1] = arg_32_0[iter_32_0]

	return var_32_0

def var_0_0.funcs.unfold(arg_33_0, arg_33_1):
	if type(arg_33_0) == "table":
		for iter_33_0 in var_0_0.iter(arg_33_0):
			var_0_0.funcs.unfold(iter_33_0, arg_33_1)
	else
		arg_33_1(arg_33_0)

def var_0_0.funcs.flatten(arg_34_0):
	local var_34_0 = {}

	var_0_0.funcs.unfold(arg_34_0, function(arg_35_0)
		var_34_0[#var_34_0 + 1] = arg_35_0)

	return var_34_0

def var_0_0.funcs.push(arg_36_0, arg_36_1):
	table.insert(arg_36_0, arg_36_1)

	return arg_36_0

def var_0_0.funcs.pop(arg_37_0):
	return table.remove(arg_37_0)

def var_0_0.funcs.shift(arg_38_0):
	return table.remove(arg_38_0, 1)

def var_0_0.funcs.unshift(arg_39_0, arg_39_1):
	table.insert(arg_39_0, 1, arg_39_1)

	return arg_39_0

def var_0_0.funcs.join(arg_40_0, arg_40_1):
	return table.concat(arg_40_0, arg_40_1)

def var_0_0.funcs.keys(arg_41_0):
	local var_41_0 = {}

	for iter_41_0, iter_41_1 in pairs(arg_41_0):
		var_41_0[#var_41_0 + 1] = iter_41_0

	return var_41_0

def var_0_0.funcs.values(arg_42_0):
	local var_42_0 = {}

	for iter_42_0, iter_42_1 in pairs(arg_42_0):
		var_42_0[#var_42_0 + 1] = iter_42_1

	return var_42_0

def var_0_0.funcs.extend(arg_43_0, arg_43_1):
	for iter_43_0, iter_43_1 in pairs(arg_43_1):
		arg_43_0[iter_43_0] = iter_43_1

	return arg_43_0

def var_0_0.funcs.is_empty(arg_44_0):
	return next(arg_44_0) == None

def var_0_0.funcs.is_equal(arg_45_0, arg_45_1, arg_45_2):
	local var_45_0 = type(arg_45_0)

	if var_45_0 != type(arg_45_1):
		return False

	if var_45_0 != "table":
		return arg_45_0 == arg_45_1

	local var_45_1 = getmetatable(arg_45_0)

	if not arg_45_2 and var_45_1 and var_45_1.__eq:
		return arg_45_0 == arg_45_1

	local var_45_2 = var_0_0.funcs.is_equal

	for iter_45_0, iter_45_1 in pairs(arg_45_0):
		local var_45_3 = arg_45_1[iter_45_0]

		if var_45_3 == None or not var_45_2(iter_45_1, var_45_3, arg_45_2):
			return False

	for iter_45_2, iter_45_3 in pairs(arg_45_1):
		if arg_45_0[iter_45_2] == None:
			return False

	return True

def var_0_0.funcs.compose(...):
	local function var_46_0(arg_47_0, ...)
		if #arg_47_0 > 1:
			return arg_47_0[1](var_46_0(_.rest(arg_47_0), ...))
		else
			return arg_47_0[1](...)

	local var_46_1 = {
		...
	}

	return function(...)
		return var_46_0(var_46_1, ...)

def var_0_0.funcs.wrap(arg_49_0, arg_49_1):
	return function(...)
		return arg_49_1(arg_49_0, ...)

def var_0_0.funcs.curry(arg_51_0, arg_51_1):
	return function(...)
		return arg_51_0(arg_51_1, ...)

def var_0_0.functions():
	return var_0_0.keys(var_0_0.funcs)

var_0_0.methods = var_0_0.functions
var_0_0.funcs.for_each = var_0_0.funcs.each
var_0_0.funcs.collect = var_0_0.funcs.map
var_0_0.funcs.inject = var_0_0.funcs.reduce
var_0_0.funcs.foldl = var_0_0.funcs.reduce
var_0_0.funcs.filter = var_0_0.funcs.select
var_0_0.funcs.every = var_0_0.funcs.all
var_0_0.funcs.some = var_0_0.funcs.any
var_0_0.funcs.head = var_0_0.funcs.first
var_0_0.funcs.tail = var_0_0.funcs.rest
var_0_0.funcs.contains = var_0_0.funcs.include

;(function()
	local function var_54_0(arg_55_0)
		local var_55_0 = False

		if getmetatable(arg_55_0) == var_0_0:
			var_55_0 = arg_55_0.chained
			arg_55_0 = arg_55_0._val

		return arg_55_0, var_55_0

	local function var_54_1(arg_56_0, arg_56_1)
		if arg_56_1:
			arg_56_0 = var_0_0.new(arg_56_0, True)

		return arg_56_0

	for iter_54_0, iter_54_1 in pairs(var_0_0.funcs):
		var_0_0[iter_54_0] = function(arg_57_0, ...)
			local var_57_0, var_57_1 = var_54_0(arg_57_0)

			return var_54_1(iter_54_1(var_57_0, ...), var_57_1))()

return var_0_0.new()
