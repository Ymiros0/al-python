local var_0_0 = require("cjson")

local function var_0_1(arg_1_0)
	local var_1_0 = 0
	local var_1_1 = 0

	for iter_1_0, iter_1_1 in pairs(arg_1_0):
		if type(iter_1_0) == "number":
			if var_1_0 < iter_1_0:
				var_1_0 = iter_1_0

			var_1_1 = var_1_1 + 1
		else
			return -1

	if var_1_0 > var_1_1 * 2:
		return -1

	return var_1_0

local var_0_2

local function var_0_3(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0
	local var_2_1
	local var_2_2

	if arg_2_1:
		var_2_0 = "\n" .. arg_2_1
		var_2_1 = var_2_0 .. "  "
		var_2_2 = arg_2_1 .. "  "
	else
		var_2_0, var_2_1, var_2_2 = " ", " ", False

	arg_2_2 = arg_2_2 + 1

	if arg_2_2 > 50:
		return "Cannot serialise any further. too many nested tables"

	local var_2_3 = var_0_1(arg_2_0)
	local var_2_4 = False
	local var_2_5 = {
		"{" .. var_2_1
	}

	if var_2_3 > 0:
		for iter_2_0 = 1, var_2_3:
			if var_2_4:
				table.insert(var_2_5, "," .. var_2_1)

			table.insert(var_2_5, var_0_2(arg_2_0[iter_2_0], var_2_2, arg_2_2))

			var_2_4 = True
	elif var_2_3 < 0:
		for iter_2_1, iter_2_2 in pairs(arg_2_0):
			if var_2_4:
				table.insert(var_2_5, "," .. var_2_1)

			table.insert(var_2_5, ("[%s] = %s").format(var_0_2(iter_2_1, var_2_2, arg_2_2), var_0_2(iter_2_2, var_2_2, arg_2_2)))

			var_2_4 = True

	table.insert(var_2_5, var_2_0 .. "}")

	return table.concat(var_2_5)

def var_0_2(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_1 == None:
		arg_3_1 = ""

	if arg_3_2 == None:
		arg_3_2 = 0

	if arg_3_0 == var_0_0.null:
		return "json.null"
	elif type(arg_3_0) == "string":
		return ("%q").format(arg_3_0)
	elif type(arg_3_0) == "None" or type(arg_3_0) == "number" or type(arg_3_0) == "boolean":
		return tostring(arg_3_0)
	elif type(arg_3_0) == "table":
		return var_0_3(arg_3_0, arg_3_1, arg_3_2)
	else
		return "\"<" .. type(arg_3_0) .. ">\""

local function var_0_4(arg_4_0)
	local var_4_0

	if arg_4_0 == None:
		var_4_0 = io.stdin
	else
		local var_4_1
		local var_4_2

		var_4_0, var_4_2 = io.open(arg_4_0, "rb")

		if var_4_0 == None:
			error(("Unable to read '%s'. %s").format(arg_4_0, var_4_2))

	local var_4_3 = var_4_0.read("*a")

	if arg_4_0 != None:
		var_4_0.close()

	if var_4_3 == None:
		error("Failed to read " .. arg_4_0)

	return var_4_3

local function var_0_5(arg_5_0, arg_5_1)
	local var_5_0

	if arg_5_0 == None:
		var_5_0 = io.stdout
	else
		local var_5_1
		local var_5_2

		var_5_0, var_5_2 = io.open(arg_5_0, "wb")

		if var_5_0 == None:
			error(("Unable to write '%s'. %s").format(arg_5_0, var_5_2))

	var_5_0.write(arg_5_1)

	if arg_5_0 != None:
		var_5_0.close()

local function var_0_6(arg_6_0, arg_6_1)
	local var_6_0 = type(arg_6_0)

	if var_6_0 != type(arg_6_1):
		return False

	if var_6_0 == "number" and arg_6_0 != arg_6_0 and arg_6_1 != arg_6_1:
		return True

	if var_6_0 != "table":
		return arg_6_0 == arg_6_1

	local var_6_1 = {}

	for iter_6_0, iter_6_1 in pairs(arg_6_0):
		var_6_1[iter_6_0] = True

	for iter_6_2, iter_6_3 in pairs(arg_6_1):
		if not var_6_1[iter_6_2]:
			return False

		if not var_0_6(arg_6_0[iter_6_2], arg_6_1[iter_6_2]):
			return False

		var_6_1[iter_6_2] = None

	for iter_6_4, iter_6_5 in pairs(var_6_1):
		return False

	return True

local var_0_7 = 0
local var_0_8 = 0

local function var_0_9()
	return var_0_7, var_0_8

local function var_0_10(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4)
	local function var_8_0(arg_9_0, arg_9_1, arg_9_2)
		local var_9_0 = {
			[True] = ".success",
			[False] = ".error"
		}

		if arg_9_1 != None:
			arg_9_0 = arg_9_0 .. var_9_0[arg_9_1]

		print(("[%s] %s").format(arg_9_0, var_0_2(arg_9_2, False)))

	local var_8_1 = {
		pcall(arg_8_1, unpack(arg_8_2))
	}
	local var_8_2 = table.remove(var_8_1, 1)
	local var_8_3 = False

	if var_8_2 == arg_8_3 and var_0_6(var_8_1, arg_8_4):
		var_8_3 = True
		var_0_7 = var_0_7 + 1

	var_0_8 = var_0_8 + 1

	local var_8_4 = {
		[True] = "PASS",
		[False] = "FAIL"
	}

	print(("==> Test [%d] %s. %s").format(var_0_8, arg_8_0, var_8_4[var_8_3]))
	var_8_0("Input", None, arg_8_2)

	if not var_8_3:
		var_8_0("Expected", arg_8_3, arg_8_4)

	var_8_0("Received", var_8_2, var_8_1)
	print()

	return var_8_3, var_8_1

local function var_0_11(arg_10_0)
	local function var_10_0(arg_11_0, arg_11_1, arg_11_2)
		if type(arg_11_0) == "string" and #arg_11_0 > 0:
			print("==> " .. arg_11_0)

		arg_11_1(unpack(arg_11_2 or {}))
		print()

	for iter_10_0, iter_10_1 in ipairs(arg_10_0):
		if iter_10_1[4] == None:
			var_10_0(unpack(iter_10_1))
		else
			var_0_10(unpack(iter_10_1))

local function var_0_12(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_1 or {}
	local var_12_1

	if _G.setfenv:
		var_12_1 = loadstring(arg_12_0)

		if var_12_1:
			setfenv(var_12_1, var_12_0)
	else
		var_12_1 = load(arg_12_0, None, None, var_12_0)

	if var_12_1 == None:
		error("Invalid syntax.")

	var_12_1()

	return var_12_0

return {
	serialise_value = var_0_2,
	file_load = var_0_4,
	file_save = var_0_5,
	compare_values = var_0_6,
	run_test_summary = var_0_9,
	run_test = var_0_10,
	run_test_group = var_0_11,
	run_script = var_0_12
}
