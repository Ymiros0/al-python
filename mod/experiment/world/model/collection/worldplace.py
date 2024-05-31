local var_0_0 = class("WorldPlace")
local var_0_1 = {
	i18n1("碧蓝"),
	i18n1("铁血"),
	i18n1("塞壬")
}
local var_0_2 = pg.world_collection_place_template

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.number = arg_1_1.number or 0
	arg_1_0.unlock = False
	arg_1_0.config = var_0_2[arg_1_0.configId]

	assert(arg_1_0.config)

def var_0_0.setUnlock(arg_2_0, arg_2_1):
	arg_2_0.unlock = arg_2_1

def var_0_0.isUnlock(arg_3_0):
	return arg_3_0.unlock

def var_0_0.getNumber(arg_4_0):
	return arg_4_0.number

def var_0_0.getDesc(arg_5_0):
	if arg_5_0.isUnlock():
		return arg_5_0.config.description_known
	else
		return arg_5_0.config.description_unknown

def var_0_0.getCamp(arg_6_0):
	return var_0_1[tonumber(arg_6_0.config.type)]

def var_0_0.getName(arg_7_0):
	if arg_7_0.isUnlock():
		return arg_7_0.config.name
	else
		return arg_7_0.config.name_unknown

def var_0_0.getIconPath(arg_8_0):
	if arg_8_0.isUnlock():
		return "shipYardIcon/abeikelongbi"
	else
		return "shipYardIcon/unknown"

def var_0_0.getFullViewImg(arg_9_0):
	return "levelmap/map_1"

return var_0_0
