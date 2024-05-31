local var_0_0 = class("ChapterChampionNormal", import(".LevelCellData"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.row = arg_1_1.pos.row
	arg_1_0.column = arg_1_1.pos.column
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.attachmentId = arg_1_0.id
	arg_1_0.attachment = arg_1_1.attachment
	arg_1_0.flag = arg_1_1.flag
	arg_1_0.data = arg_1_1.data

def var_0_0.bindConfigTable(arg_2_0):
	return pg.expedition_data_template

def var_0_0.getPrefab(arg_3_0):
	return arg_3_0.getConfig("icon")

def var_0_0.getFleetType(arg_4_0):
	return FleetType.Normal

def var_0_0.getPoolType(arg_5_0):
	return arg_5_0.getConfig("icon_type") == 1 and ChapterConst.TemplateEnemy or ChapterConst.TemplateChampion

def var_0_0.getScale(arg_6_0):
	return arg_6_0.getConfig("scale")

def var_0_0.inAlertRange(arg_7_0, arg_7_1, arg_7_2):
	return _.any(arg_7_0.getConfig("alert_range"), function(arg_8_0)
		return arg_8_0[1] + arg_7_0.row == arg_7_1 and arg_8_0[2] + arg_7_0.column == arg_7_2)

return var_0_0
