local var_0_0 = require("jit")

assert(var_0_0.version_num == 20100, "LuaJIT core/library version mismatch")

local var_0_1 = require("jit.util")
local var_0_2 = require("jit.vmdef")
local var_0_3 = var_0_1.funcinfo
local var_0_4 = var_0_1.traceinfo
local var_0_5 = type
local var_0_6 = string.format
local var_0_7 = io.stdout
local var_0_8 = io.stderr
local var_0_9
local var_0_10
local var_0_11
local var_0_12

local function var_0_13(arg_1_0, arg_1_1)
	local var_1_0 = var_0_3(arg_1_0, arg_1_1)

	if var_1_0.loc:
		return var_1_0.loc
	elif var_1_0.ffid:
		return var_0_2.ffnames[var_1_0.ffid]
	elif var_1_0.addr:
		return var_0_6("C.%x", var_1_0.addr)
	else
		return "(?)"

local function var_0_14(arg_2_0, arg_2_1)
	if var_0_5(arg_2_0) == "number":
		if var_0_5(arg_2_1) == "function":
			arg_2_1 = var_0_13(arg_2_1)

		arg_2_0 = var_0_6(var_0_2.traceerr[arg_2_0], arg_2_1)

	return arg_2_0

local function var_0_15(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5)
	if arg_3_0 == "start":
		var_0_11 = var_0_13(arg_3_2, arg_3_3)
		var_0_12 = arg_3_4 and "(" .. arg_3_4 .. "/" .. (arg_3_5 == -1 and "stitch" or arg_3_5) .. ") " or ""
	else
		if arg_3_0 == "abort":
			local var_3_0 = var_0_13(arg_3_2, arg_3_3)

			if var_3_0 != var_0_11:
				print(var_0_6("[TRACE --- %s%s -- %s at %s]\n", var_0_12, var_0_11, var_0_14(arg_3_4, arg_3_5), var_3_0))
			else
				print(var_0_6("[TRACE --- %s%s -- %s]\n", var_0_12, var_0_11, var_0_14(arg_3_4, arg_3_5)))
		elif arg_3_0 == "stop":
			local var_3_1 = var_0_4(arg_3_1)
			local var_3_2 = var_3_1.link
			local var_3_3 = var_3_1.linktype

			if var_3_3 == "interpreter":
				print(var_0_6("[TRACE %3s %s%s -- fallback to interpreter]\n", arg_3_1, var_0_12, var_0_11))
			elif var_3_3 == "stitch":
				print(var_0_6("[TRACE %3s %s%s %s %s]\n", arg_3_1, var_0_12, var_0_11, var_3_3, var_0_13(arg_3_2, arg_3_3)))
			elif var_3_2 == arg_3_1 or var_3_2 == 0:
				print(var_0_6("[TRACE %3s %s%s %s]\n", arg_3_1, var_0_12, var_0_11, var_3_3))
			elif var_3_3 == "root":
				print(var_0_6("[TRACE %3s %s%s -> %d]\n", arg_3_1, var_0_12, var_0_11, var_3_2))
			else
				print(var_0_6("[TRACE %3s %s%s -> %d %s]\n", arg_3_1, var_0_12, var_0_11, var_3_2, var_3_3))
		else
			print(var_0_6("[TRACE %s]\n", arg_3_0))

		var_0_10.flush()

local function var_0_16()
	if var_0_9:
		var_0_9 = False

		var_0_0.attach(var_0_15)

		if var_0_10 and var_0_10 != var_0_7 and var_0_10 != var_0_8:
			var_0_10.close()

		var_0_10 = None

local function var_0_17(arg_5_0)
	if var_0_9:
		var_0_16()

	arg_5_0 = arg_5_0 or os.getenv("LUAJIT_VERBOSEFILE")

	if arg_5_0:
		var_0_10 = arg_5_0 == "-" and var_0_7 or assert(io.open(arg_5_0, "w"))
	else
		var_0_10 = var_0_8

	var_0_0.attach(var_0_15, "trace")

	var_0_9 = True

return {
	on = var_0_17,
	off = var_0_16,
	start = var_0_17
}
