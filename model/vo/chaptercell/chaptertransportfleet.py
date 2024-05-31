local var_0_0 = class("ChapterTransportFleet", import(".ChapterFleet"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.line = {
		row = arg_1_1.pos.row,
		column = arg_1_1.pos.column
	}
	arg_1_0.id = arg_1_2
	arg_1_0.configId = arg_1_1.item_id
	arg_1_0.restHp = arg_1_1.item_data
	arg_1_0.rotation = Quaternion.identity

	arg_1_0.updateShips({})

def var_0_0.bindConfigTable(arg_2_0):
	return pg.friendly_data_template

def var_0_0.getFleetType(arg_3_0):
	return FleetType.Transport

def var_0_0.getPrefab(arg_4_0):
	local var_4_0 = {
		{
			20,
			16
		},
		{
			15,
			11
		},
		{
			10,
			1
		},
		{
			0,
			0
		}
	}
	local var_4_1 = {
		"merchant",
		"merchant_1",
		"merchant_2",
		"merchant_d"
	}
	local var_4_2 = var_4_1[1]

	for iter_4_0, iter_4_1 in ipairs(var_4_0):
		if arg_4_0.getRestHp() >= iter_4_1[2] and arg_4_0.getRestHp() <= iter_4_1[1]:
			var_4_2 = var_4_1[iter_4_0]

			break

	return var_4_2

def var_0_0.getRestHp(arg_5_0):
	return arg_5_0.restHp

def var_0_0.setRestHp(arg_6_0, arg_6_1):
	arg_6_0.restHp = arg_6_1

def var_0_0.getTotalHp(arg_7_0):
	return arg_7_0.getConfig("hp")

def var_0_0.isValid(arg_8_0):
	return arg_8_0.restHp > 0

return var_0_0
