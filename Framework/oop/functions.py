def printf(arg_1_0, ...):
	print(string.format(tostring(arg_1_0), ...))

def AssureTable(arg_2_0):
	if type(arg_2_0) != "table":
		arg_2_0 = {}

	return arg_2_0

def checknumber(arg_3_0, arg_3_1):
	return tonumber(arg_3_0, arg_3_1) or 0

def math.round(arg_4_0):
	arg_4_0 = checknumber(arg_4_0)

	return math.floor(arg_4_0 + 0.5)

def checkint(arg_5_0):
	return math.round(checknumber(arg_5_0))

def handler(arg_6_0, arg_6_1):
	return function(...)
		return arg_6_1(arg_6_0, ...)

def handlerArg1(arg_8_0, arg_8_1, arg_8_2):
	return function(...)
		return arg_8_1(arg_8_0, arg_8_2, ...)

local var_0_0 = print
local var_0_1 = table.concat
local var_0_2 = table.insert
local var_0_3 = string.rep
local var_0_4 = type
local var_0_5 = pairs
local var_0_6 = tostring
local var_0_7 = next

def print_r(arg_10_0):
	local var_10_0 = {
		[arg_10_0] = "."
	}

	local function var_10_1(arg_11_0, arg_11_1, arg_11_2)
		local var_11_0 = {}

		for iter_11_0, iter_11_1 in var_0_5(arg_11_0):
			local var_11_1 = var_0_6(iter_11_0)

			if var_10_0[iter_11_1]:
				var_0_2(var_11_0, "+" .. var_11_1 .. " {" .. var_10_0[iter_11_1] .. "}")
			elif var_0_4(iter_11_1) == "table":
				local var_11_2 = arg_11_2 .. "." .. var_11_1

				var_10_0[iter_11_1] = var_11_2

				var_0_2(var_11_0, "+" .. var_11_1 .. var_10_1(iter_11_1, arg_11_1 .. (var_0_7(arg_11_0, iter_11_0) and "|" or " ") .. var_0_3(" ", #var_11_1), var_11_2))
			else
				var_0_2(var_11_0, "+" .. var_11_1 .. " [" .. var_0_6(iter_11_1) .. "]")

		return var_0_1(var_11_0, "\n" .. arg_11_1)

	var_0_0(var_10_1(arg_10_0, "", ""))
