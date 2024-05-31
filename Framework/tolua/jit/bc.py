local var_0_0 = require("jit")

assert(var_0_0.version_num == 20100, "LuaJIT core/library version mismatch")

local var_0_1 = require("jit.util")
local var_0_2 = require("jit.vmdef")
local var_0_3 = require("bit")
local var_0_4 = string.sub
local var_0_5 = string.gsub
local var_0_6 = string.format
local var_0_7 = string.byte
local var_0_8 = var_0_3.band
local var_0_9 = var_0_3.rshift
local var_0_10 = var_0_1.funcinfo
local var_0_11 = var_0_1.funcbc
local var_0_12 = var_0_1.funck
local var_0_13 = var_0_1.funcuvname
local var_0_14 = var_0_2.bcnames
local var_0_15 = io.stdout
local var_0_16 = io.stderr

local function var_0_17(arg_1_0)
	if arg_1_0 == "\n":
		return "\\n"
	elif arg_1_0 == "\r":
		return "\\r"
	elif arg_1_0 == "\t":
		return "\\t"
	else
		return var_0_6("\\%03d", var_0_7(arg_1_0))

local function var_0_18(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0, var_2_1 = var_0_11(arg_2_0, arg_2_1)

	if not var_2_0:
		return

	local var_2_2 = var_0_8(var_2_1, 7)
	local var_2_3 = var_0_8(var_2_1, 120)
	local var_2_4 = var_0_8(var_2_1, 1920)
	local var_2_5 = var_0_8(var_0_9(var_2_0, 8), 255)
	local var_2_6 = 6 * var_0_8(var_2_0, 255)
	local var_2_7 = var_0_4(var_0_14, var_2_6 + 1, var_2_6 + 6)
	local var_2_8 = var_0_6("%04d %s %-6s %3s ", arg_2_1, arg_2_2 or "  ", var_2_7, var_2_2 == 0 and "" or var_2_5)
	local var_2_9 = var_0_9(var_2_0, 16)

	if var_2_4 == 1664:
		return var_0_6("%s=> %04d\n", var_2_8, arg_2_1 + var_2_9 - 32767)

	if var_2_3 != 0:
		var_2_9 = var_0_8(var_2_9, 255)
	elif var_2_4 == 0:
		return var_2_8 .. "\n"

	local var_2_10

	if var_2_4 == 1280:
		var_2_10 = var_0_12(arg_2_0, -var_2_9 - 1)
		var_2_10 = var_0_6(#var_2_10 > 40 and "\"%.40s\"~" or "\"%s\"", var_0_5(var_2_10, "%c", var_0_17))
	elif var_2_4 == 1152:
		var_2_10 = var_0_12(arg_2_0, var_2_9)

		if var_2_7 == "TSETM ":
			var_2_10 = var_2_10 - 4503599627370496
	elif var_2_4 == 1536:
		local var_2_11 = var_0_10(var_0_12(arg_2_0, -var_2_9 - 1))

		if var_2_11.ffid:
			var_2_10 = var_0_2.ffnames[var_2_11.ffid]
		else
			var_2_10 = var_2_11.loc
	elif var_2_4 == 640:
		var_2_10 = var_0_13(arg_2_0, var_2_9)

	if var_2_2 == 5:
		local var_2_12 = var_0_13(arg_2_0, var_2_5)

		if var_2_10:
			var_2_10 = var_2_12 .. " ; " .. var_2_10
		else
			var_2_10 = var_2_12

	if var_2_3 != 0:
		local var_2_13 = var_0_9(var_2_0, 24)

		if var_2_10:
			return var_0_6("%s%3d %3d  ; %s\n", var_2_8, var_2_13, var_2_9, var_2_10)

		return var_0_6("%s%3d %3d\n", var_2_8, var_2_13, var_2_9)

	if var_2_10:
		return var_0_6("%s%3d      ; %s\n", var_2_8, var_2_9, var_2_10)

	if var_2_4 == 896 and var_2_9 > 32767:
		var_2_9 = var_2_9 - 65536

	return var_0_6("%s%3d\n", var_2_8, var_2_9)

local function var_0_19(arg_3_0)
	local var_3_0 = {}

	for iter_3_0 = 1, 1000000000:
		local var_3_1, var_3_2 = var_0_11(arg_3_0, iter_3_0)

		if not var_3_1:
			break

		if var_0_8(var_3_2, 1920) == 1664:
			var_3_0[iter_3_0 + var_0_9(var_3_1, 16) - 32767] = True

	return var_3_0

local function var_0_20(arg_4_0, arg_4_1, arg_4_2)
	arg_4_1 = arg_4_1 or var_0_15

	local var_4_0 = var_0_10(arg_4_0)

	if arg_4_2 and var_4_0.children:
		for iter_4_0 = -1, -1000000000, -1:
			local var_4_1 = var_0_12(arg_4_0, iter_4_0)

			if not var_4_1:
				break

			if type(var_4_1) == "proto":
				var_0_20(var_4_1, arg_4_1, True)

	arg_4_1.write(var_0_6("-- BYTECODE -- %s-%d\n", var_4_0.loc, var_4_0.lastlinedefined))

	local var_4_2 = var_0_19(arg_4_0)

	for iter_4_1 = 1, 1000000000:
		local var_4_3 = var_0_18(arg_4_0, iter_4_1, var_4_2[iter_4_1] and "=>")

		if not var_4_3:
			break

		arg_4_1.write(var_4_3)

	arg_4_1.write("\n")
	arg_4_1.flush()

local var_0_21
local var_0_22

local function var_0_23(arg_5_0)
	return var_0_20(arg_5_0, var_0_22)

local function var_0_24()
	if var_0_21:
		var_0_21 = False

		var_0_0.attach(var_0_23)

		if var_0_22 and var_0_22 != var_0_15 and var_0_22 != var_0_16:
			var_0_22.close()

		var_0_22 = None

local function var_0_25(arg_7_0)
	if var_0_21:
		var_0_24()

	arg_7_0 = arg_7_0 or os.getenv("LUAJIT_LISTFILE")

	if arg_7_0:
		var_0_22 = arg_7_0 == "-" and var_0_15 or assert(io.open(arg_7_0, "w"))
	else
		var_0_22 = var_0_16

	var_0_0.attach(var_0_23, "bc")

	var_0_21 = True

return {
	line = var_0_18,
	dump = var_0_20,
	targets = var_0_19,
	on = var_0_25,
	off = var_0_24,
	start = var_0_25
}
