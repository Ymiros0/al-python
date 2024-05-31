local var_0_0 = class("WSBaseCommand")

local function var_0_1(arg_1_0, arg_1_1)
	return arg_1_0 != None and type(arg_1_0) == arg_1_1

local var_0_2 = {
	def __index:(arg_2_0, arg_2_1)
		local var_2_0 = rawget(arg_2_0, "class")

		if var_0_1(rawget(var_0_0, arg_2_1), "function"):
			return var_2_0[arg_2_1]
		elif var_0_1(rawget(var_2_0, arg_2_1), "function"):
			return function(arg_3_0, ...)
				arg_3_0.Op(arg_2_1, ...)
		else
			local var_2_1 = rawget(arg_2_0, arg_2_1)

			if var_2_1 == None:
				return var_2_0[arg_2_1]
			else
				return var_2_1
}

def var_0_0.Ctor(arg_4_0, arg_4_1):
	arg_4_0.index = arg_4_1
	arg_4_0.wsOps = {}

	setmetatable(arg_4_0, var_0_2)

def var_0_0.Dispose(arg_5_0):
	return

def var_0_0.Op(arg_6_0, arg_6_1, ...):
	assert(arg_6_1 and #arg_6_1 > 0)

	if #arg_6_0.wsOps > 0:
		WorldConst.Print("ignore operation. " .. arg_6_1 .. ", current operation. " .. arg_6_0.wsOps[#arg_6_0.wsOps])

		return

	WorldConst.Print(arg_6_0.index .. ": operation. " .. arg_6_1)
	table.insert(arg_6_0.wsOps, arg_6_1)
	arg_6_0.class[arg_6_1](arg_6_0, ...)

def var_0_0.OpDone(arg_7_0, arg_7_1, ...):
	assert(#arg_7_0.wsOps > 0, "current operation can not be None.")

	local var_7_0 = arg_7_0.wsOps[#arg_7_0.wsOps]

	if arg_7_1 != None and var_7_0 .. "Done" != arg_7_1:
		assert(False, "current operation " .. var_7_0 .. " mismatch with " .. arg_7_1)

		return

	WorldConst.Print(arg_7_0.index .. " operation:ne. " .. var_7_0)
	table.remove(arg_7_0.wsOps, #arg_7_0.wsOps)

	if arg_7_1:
		arg_7_0.class[arg_7_1](arg_7_0, ...)

def var_0_0.OpRaw(arg_8_0, arg_8_1, ...):
	local var_8_0 = setmetatable({
		def Op:(arg_9_0, arg_9_1, ...)
			arg_9_0.class[arg_9_1](arg_9_0, ...),
		def OpDone:(arg_10_0, arg_10_1, ...)
			if arg_10_1:
				arg_10_0[arg_10_1](arg_10_0, ...)
	}, {
		__index = arg_8_0,
		__newindex = arg_8_0
	})

	var_8_0[arg_8_1](var_8_0, ...)

def var_0_0.OpClear(arg_11_0):
	arg_11_0.wsOps = {}

return var_0_0
