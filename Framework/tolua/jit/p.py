local var_0_0 = require("jit")

assert(var_0_0.version_num == 20100, "LuaJIT core/library version mismatch")

local var_0_1 = require("jit.profile")
local var_0_2 = require("jit.vmdef")
local var_0_3 = math
local var_0_4 = pairs
local var_0_5 = ipairs
local var_0_6 = tonumber
local var_0_7 = var_0_3.floor
local var_0_8 = table.sort
local var_0_9 = string.format
local var_0_10 = io.stdout
local var_0_11
local var_0_12
local var_0_13
local var_0_14
local var_0_15
local var_0_16
local var_0_17
local var_0_18
local var_0_19
local var_0_20
local var_0_21
local var_0_22
local var_0_23
local var_0_24 = {
	G = "Garbage Collector",
	C = "C code",
	N = "Compiled",
	J = "JIT Compiler",
	I = "Interpreted"
}

local function var_0_25(arg_1_0, arg_1_1, arg_1_2)
	var_0_23 = var_0_23 + arg_1_1

	local var_1_0
	local var_1_1
	local var_1_2

	if var_0_14:
		if var_0_14 == "v":
			var_1_2 = var_0_24[arg_1_2] or arg_1_2
		else
			var_1_2 = var_0_11.get() or "(none)"

	if var_0_18:
		var_1_0 = var_0_1.dumpstack(arg_1_0, var_0_18, var_0_19)
		var_1_0 = var_1_0.gsub("%[builtin#(%d+)%]", function(arg_2_0)
			return var_0_2.ffnames[var_0_6(arg_2_0)])

		if var_0_15 == 2:
			local var_1_3, var_1_4 = var_1_0.match("(.-) [<>] (.*)")

			if var_1_4:
				var_1_0, var_1_1 = var_1_3, var_1_4
		elif var_0_15 == 3:
			var_1_1 = var_0_1.dumpstack(arg_1_0, "l", 1)

	local var_1_5
	local var_1_6

	if var_0_15 == 1:
		if var_1_2:
			var_1_5 = var_1_2

			if var_1_0:
				var_1_6 = var_1_0
	elif var_1_0:
		var_1_5 = var_1_0

		if var_1_1:
			var_1_6 = var_1_1
		elif var_1_2:
			var_1_6 = var_1_2

	if var_1_5:
		local var_1_7 = var_0_21

		var_1_7[var_1_5] = (var_1_7[var_1_5] or 0) + arg_1_1

		if var_1_6:
			local var_1_8 = var_0_22
			local var_1_9 = var_1_8[var_1_5]

			if not var_1_9:
				var_1_9 = {}
				var_1_8[var_1_5] = var_1_9

			var_1_9[var_1_6] = (var_1_9[var_1_6] or 0) + arg_1_1

local function var_0_26(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	local var_3_0 = {}
	local var_3_1 = 0

	for iter_3_0 in var_0_4(arg_3_0):
		var_3_1 = var_3_1 + 1
		var_3_0[var_3_1] = iter_3_0

	var_0_8(var_3_0, function(arg_4_0, arg_4_1)
		return arg_3_0[arg_4_0] > arg_3_0[arg_4_1])

	for iter_3_1 = 1, var_3_1:
		local var_3_2 = var_3_0[iter_3_1]
		local var_3_3 = arg_3_0[var_3_2]
		local var_3_4 = var_0_7(var_3_3 * 100 / arg_3_2 + 0.5)

		if var_3_4 < var_0_16:
			break

		if not var_0_17:
			var_0_12.write(var_0_9("%s%2d%%  %s\n", arg_3_3, var_3_4, var_3_2))
		elif var_0_17 == "r":
			var_0_12.write(var_0_9("%s%5d  %s\n", arg_3_3, var_3_3, var_3_2))
		else
			var_0_12.write(var_0_9("%s %d\n", var_3_2, var_3_3))

		if arg_3_1:
			local var_3_5 = arg_3_1[var_3_2]

			if var_3_5:
				var_0_26(var_3_5, None, var_3_3, (var_0_15 == 3 or var_0_15 == 1) and "  -- " or var_0_19 < 0 and "  -> " or "  <- ")

local function var_0_27(arg_5_0, arg_5_1)
	local var_5_0 = {}
	local var_5_1 = 0

	for iter_5_0, iter_5_1 in var_0_4(arg_5_0):
		local var_5_2 = var_0_7(iter_5_1 * 100 / arg_5_1 + 0.5)

		var_5_1 = var_0_3.max(var_5_1, iter_5_1)

		if var_5_2 >= var_0_16:
			local var_5_3, var_5_4 = iter_5_0.match("^(.*).(%d+)$")

			if not var_5_3:
				var_5_3 = iter_5_0
				var_5_4 = 0

			local var_5_5 = var_5_0[var_5_3]

			if not var_5_5:
				var_5_5 = {}
				var_5_0[var_5_3] = var_5_5
				var_5_0[#var_5_0 + 1] = var_5_3

			var_5_5[var_0_6(var_5_4)] = var_0_17 and iter_5_1 or var_5_2

	var_0_8(var_5_0)

	local var_5_6 = " %3d%% | %s\n"
	local var_5_7 = "      | %s\n"

	if var_0_17:
		local var_5_8 = var_0_3.max(5, var_0_3.ceil(var_0_3.log10(var_5_1)))

		var_5_6 = "%" .. var_5_8 .. "d | %s\n"
		var_5_7 = (" ").rep(var_5_8) .. " | %s\n"

	local var_5_9 = var_0_20

	for iter_5_2, iter_5_3 in var_0_5(var_5_0):
		local var_5_10 = iter_5_3.byte()

		if var_5_10 == 40 or var_5_10 == 91:
			var_0_12.write(var_0_9("\n====== %s ======\n[Cannot annotate non-file]\n", iter_5_3))

			break

		local var_5_11, var_5_12 = io.open(iter_5_3)

		if not var_5_11:
			var_0_12.write(var_0_9("====== ERROR. %s. %s\n", iter_5_3, var_5_12))

			break

		var_0_12.write(var_0_9("\n====== %s ======\n", iter_5_3))

		local var_5_13 = var_5_0[iter_5_3]
		local var_5_14 = 1
		local var_5_15 = False

		if var_5_9 != 0:
			for iter_5_4 = 1, var_5_9:
				if var_5_13[iter_5_4]:
					var_5_15 = True

					var_0_12.write("@@ 1 @@\n")

					break

		for iter_5_5 in var_5_11.lines():
			if iter_5_5.byte() == 27:
				var_0_12.write("[Cannot annotate bytecode file]\n")

				break

			local var_5_16 = var_5_13[var_5_14]

			if var_5_9 != 0:
				local var_5_17 = var_5_13[var_5_14 + var_5_9]

				if var_5_15:
					if var_5_17:
						var_5_15 = var_5_14 + var_5_9
					elif var_5_16:
						var_5_15 = var_5_14
					elif var_5_14 > var_5_15 + var_5_9:
						var_5_15 = False
				elif var_5_17:
					var_5_15 = var_5_14 + var_5_9

					var_0_12.write(var_0_9("@@ %d @@\n", var_5_14))

				if not var_5_15:
					goto label_5_0

			if var_5_16:
				var_0_12.write(var_0_9(var_5_6, var_5_16, iter_5_5))
			else
				var_0_12.write(var_0_9(var_5_7, iter_5_5))

			..label_5_0..

			var_5_14 = var_5_14 + 1

		var_5_11.close()

local function var_0_28()
	if var_0_13:
		var_0_1.stop()

		local var_6_0 = var_0_23

		if var_6_0 == 0:
			if var_0_17 != True:
				var_0_12.write("[No samples collected]\n")

			return

		if var_0_20:
			var_0_27(var_0_21, var_6_0)
		else
			var_0_26(var_0_21, var_0_22, var_6_0, "")

		var_0_21 = None
		var_0_22 = None
		var_0_13 = None

local function var_0_29(arg_7_0)
	local var_7_0 = ""

	arg_7_0 = arg_7_0.gsub("i%d*", function(arg_8_0)
		var_7_0 = arg_8_0

		return "")
	var_0_16 = 3
	arg_7_0 = arg_7_0.gsub("m(%d+)", function(arg_9_0)
		var_0_16 = var_0_6(arg_9_0)

		return "")
	var_0_19 = 1
	arg_7_0 = arg_7_0.gsub("%-?%d+", function(arg_10_0)
		var_0_19 = var_0_6(arg_10_0)

		return "")

	local var_7_1 = {}

	for iter_7_0 in arg_7_0.gmatch("."):
		var_7_1[iter_7_0] = iter_7_0

	var_0_14 = var_7_1.z or var_7_1.v

	if var_0_14 == "z":
		var_0_11 = require("jit.zone")

	local var_7_2 = var_7_1.l or var_7_1.f or var_7_1.F or var_0_14 and "" or "f"
	local var_7_3 = var_7_1.p or ""

	var_0_17 = var_7_1.r

	if var_7_1.s:
		var_0_15 = 2

		if var_0_19 == -1 or var_7_1["-"]:
			var_0_19 = -2
		elif var_0_19 == 1:
			var_0_19 = 2
	elif arg_7_0.find("[fF].*l"):
		var_7_2 = "l"
		var_0_15 = 3
	else
		var_0_15 = (var_7_2 == "" or arg_7_0.find("[zv].*[lfF]")) and 1 or 0

	var_0_20 = var_7_1.A and 0 or var_7_1.a and 3

	if var_0_20:
		var_7_2 = "l"
		var_0_18 = "pl"
		var_0_15 = 0
		var_0_19 = 1
	elif var_7_1.G and var_7_2 != "":
		var_0_18 = var_7_3 .. var_7_2 .. "Z;"
		var_0_19 = -100
		var_0_17 = True
		var_0_16 = 0
	elif var_7_2 == "":
		var_0_18 = False
	else
		local var_7_4 = var_0_15 == 3 and var_7_1.f or var_7_1.F or var_7_2

		var_0_18 = var_7_3 .. var_7_4 .. (var_0_19 >= 0 and "Z < " or "Z > ")

	var_0_21 = {}
	var_0_22 = {}
	var_0_23 = 0

	var_0_1.start(var_7_2.lower() .. var_7_0, var_0_25)

	var_0_13 = newproxy(True)
	getmetatable(var_0_13).__gc = var_0_28

local function var_0_30(arg_11_0, arg_11_1)
	arg_11_1 = arg_11_1 or os.getenv("LUAJIT_PROFILEFILE")

	if arg_11_1:
		var_0_12 = arg_11_1 == "-" and var_0_10 or assert(io.open(arg_11_1, "w"))
	else
		var_0_12 = var_0_10

	var_0_29(arg_11_0 or "f")

return {
	start = var_0_30,
	stop = var_0_28
}
