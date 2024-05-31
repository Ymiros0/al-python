local var_0_0 = class("InstagramNpcComment", import(".InstagramComment"))
local var_0_1 = pg.activity_ins_ship_group_template

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)

	arg_1_0.configId = arg_1_0.id

	local var_1_0 = arg_1_0.level + 1

	for iter_1_0, iter_1_1 in ipairs(arg_1_1.npc_reply):
		assert(arg_1_0.allReply[iter_1_1], iter_1_1)
		table.insert(arg_1_0.replyList, InstagramNpcComment.New(arg_1_0.allReply[iter_1_1], arg_1_2, var_1_0, arg_1_0))

	arg_1_0.config = var_0_1[arg_1_0.getConfig("ship_group")]

def var_0_0.bindConfigTable(arg_2_0):
	return pg.activity_ins_npc_template

def var_0_0.GetName(arg_3_0):
	return arg_3_0.config.name

def var_0_0.GetPainting(arg_4_0):
	return arg_4_0.config.sculpture

def var_0_0.GetType(arg_5_0):
	return Instagram.TYPE_NPC_COMMENT

return var_0_0
