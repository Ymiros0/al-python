local var_0_0 = table.remove

return setmetatable({
	def flush:(arg_1_0)
		for iter_1_0 = #arg_1_0, 1, -1:
			arg_1_0[iter_1_0] = None,
	def get:(arg_2_0)
		return arg_2_0[#arg_2_0]
}, {
	def __call:(arg_3_0, arg_3_1)
		if arg_3_1:
			arg_3_0[#arg_3_0 + 1] = arg_3_1
		else
			return (assert(var_0_0(arg_3_0), "empty zone stack"))
})
