local var_0_0 = class("BaseVO")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	for iter_1_0, iter_1_1 in pairs(arg_1_1):
		arg_1_0[iter_1_0] = iter_1_1

def var_0_0.display(arg_2_0, arg_2_1, arg_2_2):
	if arg_2_1 == "loaded" or not arg_2_2:
		return

	local var_2_0 = arg_2_0.__cname .. " id. " .. tostring(arg_2_0.id) .. " " .. (arg_2_1 or ".")

	for iter_2_0, iter_2_1 in pairs(arg_2_0):
		if iter_2_0 != "class":
			local var_2_1 = type(iter_2_1)

			var_2_0 = var_2_0 .. "\n" .. iter_2_0 .. "." .. tostring(iter_2_1)

			if var_2_1 == "table":
				var_2_0 = var_2_0 .. " ["

				for iter_2_2, iter_2_3 in pairs(iter_2_1):
					var_2_0 = var_2_0 .. tostring(iter_2_3) .. ", "

				var_2_0 = var_2_0 .. "]"

	print(var_2_0)

def var_0_0.clone(arg_3_0):
	return Clone(arg_3_0)

def var_0_0.bindConfigTable(arg_4_0):
	return

def var_0_0.GetConfigID(arg_5_0):
	return arg_5_0.configId

def var_0_0.getConfigTable(arg_6_0):
	local var_6_0 = arg_6_0.bindConfigTable()

	assert(var_6_0, "should bindConfigTable() first. " .. arg_6_0.__cname)

	return var_6_0[arg_6_0.configId]

def var_0_0.getConfig(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.getConfigTable()

	assert(var_7_0 != None, "Config missed, type -" .. arg_7_0.__cname .. " configId. " .. tostring(arg_7_0.configId))

	return var_7_0[arg_7_1]

return var_0_0
