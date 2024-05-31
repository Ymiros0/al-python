local var_0_0 = class("WorldStoryGroup")
local var_0_1 = pg.memory_group

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_1.id
	arg_1_0.config = var_0_1[arg_1_0.configId]

	assert(arg_1_0.config)

	arg_1_0.storyIds = arg_1_0.config.memories

def var_0_0.getStoryIds(arg_2_0):
	return arg_2_0.storyIds

return var_0_0
