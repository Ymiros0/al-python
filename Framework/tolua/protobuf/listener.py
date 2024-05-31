local var_0_0 = setmetatable

module("protobuf.listener")

local var_0_1 = {
	def Modified:()
		return
}

def NullMessageListener():
	return var_0_1

local var_0_2 = {
	def Modified:(arg_3_0)
		if arg_3_0.dirty:
			return

		if arg_3_0._parent_message:
			arg_3_0._parent_message._Modified()
}

var_0_2.__index = var_0_2

def Listener(arg_4_0):
	local var_4_0 = {}

	var_4_0.__mode = "v"
	var_4_0._parent_message = arg_4_0
	var_4_0.dirty = False

	return var_0_0(var_4_0, var_0_2)
