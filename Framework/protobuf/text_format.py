local var_0_0 = string
local var_0_1 = math
local var_0_2 = print
local var_0_3 = getmetatable
local var_0_4 = table
local var_0_5 = ipairs
local var_0_6 = tostring
local var_0_7 = require("descriptor")

module("text_format")

def format(arg_1_0):
	local var_1_0 = var_0_0.len(arg_1_0)

	for iter_1_0 = 1, var_1_0, 16:
		local var_1_1 = ""

		for iter_1_1 = iter_1_0, var_0_1.min(iter_1_0 + 16 - 1, var_1_0):
			var_1_1 = var_0_0.format("%s  %02x", var_1_1, var_0_0.byte(arg_1_0, iter_1_1))

		var_0_2(var_1_1)

local var_0_8 = var_0_7.FieldDescriptor

def msg_format_indent(arg_2_0, arg_2_1, arg_2_2):
	for iter_2_0, iter_2_1 in arg_2_1.ListFields():
		local function var_2_0(arg_3_0)
			local var_3_0 = iter_2_0.name

			arg_2_0(var_0_0.rep(" ", arg_2_2))

			if iter_2_0.type == var_0_8.TYPE_MESSAGE:
				if var_0_3(arg_2_1)._extensions_by_name[iter_2_0.full_name]:
					arg_2_0("[" .. var_3_0 .. "] {\n")
				else
					arg_2_0(var_3_0 .. " {\n")

				msg_format_indent(arg_2_0, arg_3_0, arg_2_2 + 4)
				arg_2_0(var_0_0.rep(" ", arg_2_2))
				arg_2_0("}\n")
			else
				arg_2_0(var_0_0.format("%s. %s\n", var_3_0, var_0_6(arg_3_0)))

		if iter_2_0.label == var_0_8.LABEL_REPEATED:
			for iter_2_2, iter_2_3 in var_0_5(iter_2_1):
				var_2_0(iter_2_3)
		else
			var_2_0(iter_2_1)

def msg_format(arg_4_0):
	local var_4_0 = {}

	local function var_4_1(arg_5_0)
		var_4_0[#var_4_0 + 1] = arg_5_0

	msg_format_indent(var_4_1, arg_4_0, 0)

	return var_0_4.concat(var_4_0)
