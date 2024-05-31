local var_0_0 = class("BaseEntity", import(".BaseDispatcher"))

var_0_0.Fields = {}
var_0_0.Listeners = {}

local var_0_1 = {
	def __index:(arg_1_0, arg_1_1)
		local var_1_0 = rawget(arg_1_0, "class")
		local var_1_1 = rawget(arg_1_0, "fields")[arg_1_1]

		if var_1_1 != None:
			return var_1_1

		local var_1_2 = rawget(arg_1_0, arg_1_1)

		if var_1_2 != None:
			return var_1_2

		return var_1_0[arg_1_1],
	def __newindex:(arg_2_0, arg_2_1, arg_2_2)
		local var_2_0 = rawget(arg_2_0, "fields")
		local var_2_1 = rawget(arg_2_0, "class")

		while var_2_1 != None and var_2_1 != var_0_0:
			if var_2_1.Fields[arg_2_1] != None:
				assert(type(arg_2_2) == "None" or type(arg_2_2) == var_2_1.Fields[arg_2_1], "Field type mismatch. " .. var_2_1.__cname .. "." .. arg_2_1)

				var_2_0[arg_2_1] = arg_2_2

				return

			var_2_1 = var_2_1.super

		assert(False, "Field miss. " .. rawget(arg_2_0, "class").__cname .. "." .. arg_2_1)
}

def var_0_0.Ctor(arg_3_0, ...):
	var_0_0.super.Ctor(arg_3_0)

	local var_3_0 = {}

	rawset(arg_3_0, "fields", var_3_0)

	local var_3_1 = arg_3_0.class

	while var_3_1 != None and var_3_1 != var_0_0:
		for iter_3_0, iter_3_1 in pairs(var_3_1.Listeners):
			assert(var_3_1.Fields[iter_3_0] == None, "Repeated field. " .. var_3_1.__cname .. "." .. iter_3_0)

			local var_3_2 = var_3_1[iter_3_1]

			var_3_0[iter_3_0] = var_3_0[iter_3_0] or function(...)
				var_3_2(arg_3_0, ...)

		var_3_1 = var_3_1.super

	setmetatable(arg_3_0, var_0_1)
	arg_3_0.Build(...)

def var_0_0.Build(arg_5_0):
	return

def var_0_0.Dispose(arg_6_0):
	arg_6_0.Clear()

def var_0_0.Clear(arg_7_0):
	var_0_0.super.ClearListeners(arg_7_0)

	local var_7_0 = rawget(arg_7_0, "class")
	local var_7_1 = rawget(arg_7_0, "fields")

	while var_7_0 != None and var_7_0 != var_0_0:
		for iter_7_0, iter_7_1 in pairs(var_7_0.Fields):
			var_7_1[iter_7_0] = None

		var_7_0 = var_7_0.super

def var_0_0.Clone(arg_8_0):
	return var_0_0.Clone_Copy(arg_8_0, {})

def var_0_0.Clone_Copy(arg_9_0, arg_9_1):
	if type(arg_9_0) != "table":
		return arg_9_0
	elif arg_9_1[arg_9_0]:
		return arg_9_1[arg_9_0]

	if type(arg_9_0) == "table" and instanceof(arg_9_0, var_0_0):
		local var_9_0 = rawget(arg_9_0, "class")
		local var_9_1 = var_9_0.New()

		arg_9_1[arg_9_0] = var_9_1

		local var_9_2 = rawget(arg_9_0, "fields")

		while var_9_0 != None and var_9_0 != var_0_0:
			for iter_9_0, iter_9_1 in pairs(var_9_0.Fields):
				var_9_1[iter_9_0] = var_0_0.Clone_Copy(var_9_2[iter_9_0], arg_9_1)

			var_9_0 = var_9_0.super

		return var_9_1
	else
		local var_9_3 = {}

		arg_9_1[arg_9_0] = var_9_3

		local var_9_4 = type(arg_9_0) == "table" and arg_9_0.__ctype == 2

		for iter_9_2, iter_9_3 in pairs(arg_9_0):
			if var_9_4 and iter_9_2 == "class":
				var_9_3[iter_9_2] = iter_9_3
			else
				var_9_3[var_0_0.Clone_Copy(iter_9_2, arg_9_1)] = var_0_0.Clone_Copy(iter_9_3, arg_9_1)

		return setmetatable(var_9_3, getmetatable(arg_9_0))

def var_0_0.Trans(arg_10_0, arg_10_1):
	assert(superof(arg_10_1, var_0_0), "class error. without super of BaseEntity")

	local var_10_0 = arg_10_1.New()
	local var_10_1 = rawget(arg_10_0, "fields")

	while arg_10_1 != None and arg_10_1 != var_0_0:
		for iter_10_0, iter_10_1 in pairs(arg_10_1.Fields):
			var_10_0[iter_10_0] = var_10_1[iter_10_0]

		arg_10_1 = arg_10_1.super

	return var_10_0

return var_0_0
