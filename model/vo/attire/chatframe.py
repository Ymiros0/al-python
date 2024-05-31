local var_0_0 = class("ChatFrame", import(".AttireFrame"))

def var_0_0.GetIcon(arg_1_0):
	return "ChatFrame/" .. arg_1_0

def var_0_0.getType(arg_2_0):
	return AttireConst.TYPE_CHAT_FRAME

def var_0_0.bindConfigTable(arg_3_0):
	return pg.item_data_chat

def var_0_0.getPrefabName(arg_4_0):
	if arg_4_0.getConfig("id") == 0:
		return arg_4_0.getConfig("id") .. "_self"
	else
		return arg_4_0.getConfig("id") .. "_self"

def var_0_0.getDropType(arg_5_0):
	return DROP_TYPE_CHAT_FRAME

def var_0_0.getIcon(arg_6_0):
	return var_0_0.GetIcon(arg_6_0.getPrefabName())

return var_0_0
