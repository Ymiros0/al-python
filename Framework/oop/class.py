def Clone_Copy(arg_1_0, arg_1_1):
	if type(arg_1_0) != "table":
		return arg_1_0
	elif arg_1_1[arg_1_0]:
		return arg_1_1[arg_1_0]

	local var_1_0 = {}

	arg_1_1[arg_1_0] = var_1_0

	local var_1_1 = type(arg_1_0) == "table" and arg_1_0.__ctype == 2

	for iter_1_0, iter_1_1 in pairs(arg_1_0):
		if var_1_1 and iter_1_0 == "class":
			var_1_0[iter_1_0] = iter_1_1
		else
			var_1_0[Clone_Copy(iter_1_0, arg_1_1)] = Clone_Copy(iter_1_1, arg_1_1)

	return setmetatable(var_1_0, getmetatable(arg_1_0))

def Clone(arg_2_0):
	return Clone_Copy(arg_2_0, {})

def class(arg_3_0, arg_3_1):
	local var_3_0 = type(arg_3_1)
	local var_3_1

	if var_3_0 != "function" and var_3_0 != "table":
		var_3_0 = None
		arg_3_1 = None

	if var_3_0 == "function" or arg_3_1 and arg_3_1.__ctype == 1:
		var_3_1 = {}

		if var_3_0 == "table":
			for iter_3_0, iter_3_1 in pairs(arg_3_1):
				var_3_1[iter_3_0] = iter_3_1

			var_3_1.__create = arg_3_1.__create
			var_3_1.super = arg_3_1
		else
			var_3_1.__create = arg_3_1

		function var_3_1.Ctor()
			return

		var_3_1.__cname = arg_3_0
		var_3_1.__ctype = 1

		function var_3_1.New(...)
			local var_5_0 = var_3_1.__create(...)

			for iter_5_0, iter_5_1 in pairs(var_3_1):
				var_5_0[iter_5_0] = iter_5_1

			var_5_0.class = var_3_1

			var_5_0.Ctor(...)

			return var_5_0
	else
		if arg_3_1:
			var_3_1 = setmetatable({}, arg_3_1)
			var_3_1.super = arg_3_1
		else
			var_3_1 = {
				def Ctor:()
					return
			}

		var_3_1.__cname = arg_3_0
		var_3_1.__ctype = 2
		var_3_1.__index = var_3_1

		function var_3_1.New(...)
			local var_7_0 = setmetatable({}, var_3_1)

			var_7_0.class = var_3_1

			var_7_0.Ctor(...)

			return var_7_0

	return var_3_1

def isa(arg_8_0, arg_8_1):
	local var_8_0 = getmetatable(arg_8_0)

	while var_8_0 != None:
		if var_8_0 == arg_8_1:
			return True
		else
			assert(var_8_0 != getmetatable(var_8_0), "Loop metatable")

			var_8_0 = getmetatable(var_8_0)

	return False

def instanceof(arg_9_0, arg_9_1):
	return superof(arg_9_0.class, arg_9_1)

def superof(arg_10_0, arg_10_1):
	while arg_10_0 != None:
		if arg_10_0 == arg_10_1:
			return True
		else
			arg_10_0 = arg_10_0.super

	return False

def singletonClass(arg_11_0, arg_11_1):
	local var_11_0 = class(arg_11_0, arg_11_1)

	var_11_0._new = var_11_0.New

	rawset(var_11_0, "_singletonInstance", None)

	function var_11_0.New()
		if not var_11_0._singletonInstance:
			return var_11_0.GetInstance()

		error("singleton class can not new. Please use " .. arg_11_0 .. ".GetInstance() to get it", 2)

	function var_11_0.GetInstance()
		if rawget(var_11_0, "_singletonInstance") == None:
			rawset(var_11_0, "_singletonInstance", var_11_0._new())

		return var_11_0._singletonInstance

	return var_11_0

def removeSingletonInstance(arg_14_0):
	if arg_14_0 and rawget(arg_14_0, "_singletonInstance"):
		rawset(arg_14_0, "_singletonInstance", None)

		return True

	return False

def tracebackex():
	local var_15_0 = ""
	local var_15_1 = 2
	local var_15_2 = var_15_0 .. "stack traceback.\n"

	while True:
		local var_15_3 = debug.getinfo(var_15_1, "Sln")

		if not var_15_3:
			break

		if var_15_3.what == "C":
			var_15_2 = var_15_2 .. tostring(var_15_1) .. "\tC function\n"
		else
			var_15_2 = var_15_2 .. string.format("\t[%s].%d in function `%s`\n", var_15_3.short_src, var_15_3.currentline, var_15_3.name or "")

		local var_15_4 = 1

		while True:
			local var_15_5, var_15_6 = debug.getlocal(var_15_1, var_15_4)

			if not var_15_5:
				break

			var_15_2 = var_15_2 .. "\t\t" .. var_15_5 .. " =\t" .. tostringex(var_15_6, 3) .. "\n"
			var_15_4 = var_15_4 + 1

		var_15_1 = var_15_1 + 1

	return var_15_2

def tostringex(arg_16_0, arg_16_1):
	if arg_16_1 == None:
		arg_16_1 = 0

	local var_16_0 = string.rep("\t", arg_16_1)
	local var_16_1 = ""

	if type(arg_16_0) == "table":
		if arg_16_1 > 5:
			return "\t{ ... }"

		local var_16_2 = ""

		for iter_16_0, iter_16_1 in pairs(arg_16_0):
			var_16_2 = var_16_2 .. "\n\t" .. var_16_0 .. tostring(iter_16_0) .. "."
			var_16_2 = var_16_2 .. tostringex(iter_16_1, arg_16_1 + 1)

		if var_16_2 == "":
			var_16_1 = var_16_1 .. var_16_0 .. "{ }\t(" .. tostring(arg_16_0) .. ")"
		else
			if arg_16_1 > 0:
				var_16_1 = var_16_1 .. "\t(" .. tostring(arg_16_0) .. ")\n"

			var_16_1 = var_16_1 .. var_16_0 .. "{" .. var_16_2 .. "\n" .. var_16_0 .. "}"
	else
		var_16_1 = var_16_1 .. var_16_0 .. tostring(arg_16_0) .. "\t(" .. type(arg_16_0) .. ")"

	return var_16_1

def DecorateClass(arg_17_0, arg_17_1):
	assert(arg_17_0, "Need a Base Class")

	local var_17_0 = setmetatable({}, {
		def __index:(arg_18_0, arg_18_1)
			return arg_17_0[arg_18_1] or arg_17_1[arg_18_1]
	})

	var_17_0.super = arg_17_0
	var_17_0.__cname = arg_17_0.__cname .. " feat." .. arg_17_1.__cname
	var_17_0.__ctype = 2
	var_17_0.__index = var_17_0

	function var_17_0.New(...)
		local var_19_0 = setmetatable({}, var_17_0)

		var_19_0.class = var_17_0

		var_19_0.Ctor(...)

		return var_19_0

	return var_17_0
