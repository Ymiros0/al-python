local var_0_0 = class("CommanderTalent", import("..BaseVO"))
local var_0_1 = pg.commander_ability_group

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.groupId = arg_1_0.getConfig("group_id")

	assert(var_0_1[arg_1_0.groupId])

	arg_1_0.list = var_0_1[arg_1_0.groupId].ability_list

def var_0_0.reset(arg_2_0):
	arg_2_0.id = arg_2_0.list[1]
	arg_2_0.configId = arg_2_0.id

def var_0_0.setOrigin(arg_3_0, arg_3_1):
	arg_3_0.origin = arg_3_1

def var_0_0.isOrigin(arg_4_0):
	return arg_4_0.origin

def var_0_0.getTalentList(arg_5_0):
	return arg_5_0.list

def var_0_0.bindConfigTable(arg_6_0):
	return pg.commander_ability_template

def var_0_0.getConsume(arg_7_0):
	local var_7_0 = 0
	local var_7_1 = table.indexof(arg_7_0.list, arg_7_0.id)

	if arg_7_0.origin:
		var_7_0 = var_7_1 - table.indexof(arg_7_0.list, arg_7_0.origin.id)
	else
		var_7_0 = var_7_1

	return var_7_0

def var_0_0.getAttrsAddition(arg_8_0):
	local var_8_0 = {}
	local var_8_1 = {}

	for iter_8_0, iter_8_1 in ipairs(CommanderConst.PROPERTIES):
		for iter_8_2, iter_8_3 in ipairs(arg_8_0.getConfig("add")):
			if CommanderConst.TALENT_ADDITION_NUMBER == iter_8_3[1]:
				if iter_8_3[4] == iter_8_0:
					var_8_0[iter_8_1] = {
						value = iter_8_3[5],
						nation = iter_8_3[2],
						shiptype = iter_8_3[3]
					}
			elif CommanderConst.TALENT_ADDITION_RATIO == iter_8_3[1] and iter_8_3[4] == iter_8_0:
				var_8_1[iter_8_1] = {
					value = iter_8_3[5],
					nation = iter_8_3[2],
					shiptype = iter_8_3[3]
				}

	return var_8_0, var_8_1

def var_0_0.getBuffsAddition(arg_9_0):
	local var_9_0 = {}

	for iter_9_0, iter_9_1 in ipairs(arg_9_0.getConfig("add")):
		if CommanderConst.TALENT_ADDITION_BUFF == iter_9_1[1]:
			table.insert(var_9_0, iter_9_1[4])

	return var_9_0

def var_0_0.getDestoryExpValue(arg_10_0):
	local var_10_0 = 0
	local var_10_1 = arg_10_0.getConfig("add")

	for iter_10_0, iter_10_1 in ipairs(var_10_1):
		if iter_10_1[1] == CommanderConst.TALENT_ADDITION_NUMBER and iter_10_1[4] == CommanderConst.DESTROY_ATTR_ID:
			var_10_0 = var_10_0 + iter_10_1[5]

	return var_10_0

def var_0_0.getDestoryExpRetio(arg_11_0):
	local var_11_0 = 0
	local var_11_1 = arg_11_0.getConfig("add")

	for iter_11_0, iter_11_1 in ipairs(var_11_1):
		if iter_11_1[1] == CommanderConst.TALENT_ADDITION_RATIO and iter_11_1[4] == CommanderConst.DESTROY_ATTR_ID:
			var_11_0 = var_11_0 + iter_11_1[5]

	return var_11_0

def var_0_0.getDesc(arg_12_0):
	local var_12_0 = {}
	local var_12_1 = arg_12_0.getConfig("add_desc")

	for iter_12_0, iter_12_1 in ipairs(var_12_1):
		local var_12_2 = iter_12_1[1]

		if var_12_0[var_12_2]:
			var_12_0[var_12_2].value = var_12_0[var_12_2].value + iter_12_1[2]
		else
			var_12_0[var_12_2] = {
				value = iter_12_1[2],
				type = iter_12_1[3] and CommanderConst.TALENT_ADDITION_RATIO or CommanderConst.TALENT_ADDITION_NUMBER
			}

	return var_12_0

return var_0_0
