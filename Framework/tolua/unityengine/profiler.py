local var_0_0 = LuaProfiler
local var_0_1 = jit and require("jit.vmdef")
local var_0_2 = {
	event = {
		[20] = "_xpcall.__call",
		[142] = "event.__call"
	},
	slot = {
		[11] = "slot.__call"
	},
	MainScene = {
		[250] = "MainScene.Update"
	}
}
local var_0_3 = {
	ipairs_aux = 1,
	["_xpcall.__call"] = 1,
	unknow = 1
}
local var_0_4 = {
	mark = 1,
	cache = 1
}
local var_0_5 = {}

def var_0_4.scan(arg_1_0, arg_1_1, arg_1_2):
	if arg_1_0.mark[arg_1_1]:
		return

	arg_1_0.mark[arg_1_1] = True

	for iter_1_0, iter_1_1 in pairs(arg_1_1):
		if type(iter_1_0) == "string":
			if type(iter_1_1) == "function":
				local var_1_0 = iter_1_0

				if arg_1_2:
					var_1_0 = arg_1_2 .. "." .. var_1_0

				if not var_0_3[var_1_0] and iter_1_0 != "__index" and iter_1_0 != "__newindex":
					arg_1_0.cache[iter_1_1] = {
						id = -1,
						name = var_1_0
					}
			elif type(iter_1_1) == "table" and not arg_1_0.mark[iter_1_1]:
				arg_1_0.scan(iter_1_1, iter_1_0)
		elif arg_1_2 and iter_1_0 == tolua.gettag or iter_1_0 == tolua.settag:
			arg_1_0.scan(iter_1_1, arg_1_2)

def var_0_4.scanlibs(arg_2_0):
	local var_2_0 = package.loaded

	arg_2_0.mark[var_2_0] = True

	for iter_2_0, iter_2_1 in pairs(var_2_0):
		if type(iter_2_0) == "string" and type(iter_2_1) == "table":
			arg_2_0.scan(iter_2_1, iter_2_0)

			local var_2_1 = getmetatable(iter_2_1)

			if var_2_1:
				arg_2_0.scan(var_2_1, iter_2_0)

local function var_0_6(arg_3_0)
	local var_3_0 = #var_0_5 + 1

	for iter_3_0, iter_3_1 in ipairs(var_0_5):
		if iter_3_1 == arg_3_0:
			var_3_0 = iter_3_0

	return var_3_0

local function var_0_7(arg_4_0)
	local var_4_0 = #var_0_5

	if var_4_0 > 0:
		local var_4_1 = debug.getinfo(5, "f")

		if var_4_1:
			local var_4_2 = var_4_1.func
			local var_4_3 = var_0_6(var_4_2)

			if var_4_0 < var_4_3:
				local var_4_4 = debug.getinfo(6, "f")

				if var_4_4:
					local var_4_5 = var_4_4.func

					var_4_3 = var_0_6(var_4_5) or var_4_3

			for iter_4_0 = var_4_3 + 1, var_4_0:
				table.remove(var_0_5)
				var_0_0.EndSample()

local function var_0_8(arg_5_0, arg_5_1, arg_5_2)
	var_0_7()
	table.insert(var_0_5, arg_5_1)

	if arg_5_2.id == -1:
		arg_5_2.name = arg_5_0
		arg_5_2.id = var_0_0.GetID(arg_5_0)

	var_0_0.BeginSample(arg_5_2.id)

local function var_0_9(arg_6_0, arg_6_1, arg_6_2)
	var_0_7()
	table.insert(var_0_5, arg_6_1)

	local var_6_0 = -1

	if arg_6_2.nick == None:
		arg_6_2.nick = {}

	local var_6_1 = arg_6_2.nick[arg_6_0]

	if not var_6_1:
		var_6_1 = var_0_0.GetID(arg_6_0)
		arg_6_2.nick[arg_6_0] = var_6_1

	var_0_0.BeginSample(var_6_1)

def profiler_hook(arg_7_0, arg_7_1):
	if arg_7_0 == "call":
		local var_7_0
		local var_7_1 = debug.getinfo(2, "f").func
		local var_7_2 = var_0_4.cache[var_7_1]

		if var_7_2:
			var_7_0 = var_7_2.name

		if var_0_3[var_7_0]:
			return

		if var_7_0 == "event.__call":
			local var_7_3 = debug.getinfo(2, "n")

			var_0_9(var_7_3.name or var_7_0, var_7_1, var_7_2)
		elif var_7_0:
			var_0_8(var_7_0, var_7_1, var_7_2)
		else
			local var_7_4 = debug.getinfo(2, "Sn")
			local var_7_5 = var_7_4.name
			local var_7_6 = var_7_4.linedefined

			if not var_7_2:
				var_7_2 = {
					id = -1,
					name = "unknow"
				}
				var_0_4.cache[var_7_1] = var_7_2

			if var_7_4.short_src == "[C]":
				if var_7_5 == "__index" or var_7_5 == "__newindex":
					return

				local var_7_7 = tostring(var_7_1).match("function. builtin#(%d+)")

				if not var_7_7:
					if var_7_5:
						local var_7_8 = var_7_5

						var_0_8(var_7_5, var_7_1, var_7_2)
					elif var_7_6 != -1:
						local var_7_9 = var_7_4.short_src .. var_7_6

						var_0_8(var_7_9, var_7_1, var_7_2)
				else
					local var_7_10 = var_0_1.ffnames[tonumber(var_7_7)]

					if not var_0_3[var_7_10]:
						var_0_8(var_7_10, var_7_1, var_7_2)
			elif var_7_6 != -1 or var_7_5:
				local var_7_11 = var_7_4.short_src

				var_7_5 = var_7_5 or var_7_6

				local var_7_12
				local var_7_13 = var_7_11.match("([^/\\]+)%.%w+$") or var_7_11.match("([^/\\]+)$")
				local var_7_14 = var_0_2[var_7_13]

				if var_7_14:
					var_7_13 = var_7_14[var_7_6]
				else
					var_7_13 = var_7_13 .. "." .. var_7_5

				var_7_13 = var_7_13 or var_7_11 .. "." .. var_7_5

				var_0_8(var_7_13, var_7_1, var_7_2)
			else
				var_0_8(var_7_0, var_7_1, var_7_2)
	elif arg_7_0 == "return":
		local var_7_15 = #var_0_5

		if var_7_15 == 0:
			return

		local var_7_16 = debug.getinfo(2, "f")

		if var_7_16.func == var_0_5[var_7_15]:
			table.remove(var_0_5)
			var_0_0.EndSample()
		else
			local var_7_17 = var_0_6(var_7_16.func)

			if var_7_15 < var_7_17:
				return

			for iter_7_0 = var_7_17, var_7_15:
				table.remove(var_0_5)
				var_0_0.EndSample()

def var_0_4.start(arg_8_0):
	arg_8_0.mark = {}
	arg_8_0.cache = {
		__mode = "k"
	}

	arg_8_0.scan(_G, None)
	arg_8_0.scanlibs()

	arg_8_0.mark = None

	debug.sethook(profiler_hook, "cr", 0)

def var_0_4.print(arg_9_0):
	for iter_9_0, iter_9_1 in pairs(arg_9_0.cache):
		print(iter_9_1.name)

def var_0_4.stop(arg_10_0):
	debug.sethook(None)

	arg_10_0.cache = None

return var_0_4
