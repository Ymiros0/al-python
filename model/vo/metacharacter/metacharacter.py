local var_0_0 = class("MetaCharacter", import("..BaseVO"))

def var_0_0.bindConfigTable(arg_1_0):
	return pg.ship_strengthen_meta

def var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2):
	assert(arg_2_1.id)
	assert(arg_2_2)

	arg_2_0.id = arg_2_1.id
	arg_2_0.configId = arg_2_0.id
	arg_2_0.shipVO = arg_2_2
	arg_2_0.maxRepairExp = arg_2_0.getConfig("repair_total_exp")
	arg_2_0.attrs = {}

	for iter_2_0, iter_2_1 in ipairs(MetaCharacterConst.REPAIR_ATTRS):
		arg_2_0.attrs[iter_2_1] = MetaCharacterAttr.New({
			attr = iter_2_1,
			items = arg_2_0.getConfig("repair_" .. iter_2_1)
		})

	arg_2_0.effects = _.map(arg_2_0.getConfig("repair_effect"), function(arg_3_0)
		return MetaRepairEffect.New({
			id = arg_3_0[2],
			progress = arg_3_0[1]
		}))

	for iter_2_2, iter_2_3 in ipairs(arg_2_1.repair_attr_info or {}):
		for iter_2_4, iter_2_5 in pairs(arg_2_0.attrs):
			if iter_2_5.hasItemId(iter_2_3):
				local var_2_0 = iter_2_5.getLevelByItemId(iter_2_3)

				iter_2_5.updateCount(var_2_0)

def var_0_0.getBreakOutInfo(arg_4_0):
	assert(arg_4_0.shipVO)

	local var_4_0 = arg_4_0.shipVO

	if not arg_4_0.beakOutInfo or var_4_0.configId != arg_4_0.beakOutInfo.id:
		arg_4_0.beakOutInfo = MetaCharacterBreakout.New({
			id = var_4_0.configId
		})

	return arg_4_0.beakOutInfo

def var_0_0.getSpecialMaterialInfoToMaxStar(arg_5_0):
	local var_5_0 = arg_5_0.getBreakOutInfo()
	local var_5_1 = {
		count = 0,
		itemID = arg_5_0.beakOutInfo.getConfig("item1")
	}

	while True:
		if not var_5_0.hasNextInfo():
			return var_5_1
		else
			var_5_1.count = var_5_1.count + var_5_0.getConfig("item1_num")
			var_5_0 = var_5_0.getNextInfo()

def var_0_0.getCurRepairExp(arg_6_0):
	local var_6_0 = 0

	for iter_6_0, iter_6_1 in pairs(arg_6_0.attrs):
		var_6_0 = var_6_0 + iter_6_1.getRepairExp()

	return var_6_0

def var_0_0.getMaxRepairExp(arg_7_0):
	return arg_7_0.maxRepairExp

def var_0_0.getRepairRate(arg_8_0):
	return arg_8_0.getCurRepairExp() / arg_8_0.getMaxRepairExp()

def var_0_0.isMaxRepairExp(arg_9_0):
	return arg_9_0.getCurRepairExp() == arg_9_0.getMaxRepairExp()

def var_0_0.getAttrAddition(arg_10_0, arg_10_1):
	return arg_10_0.getRepairAddition(arg_10_1) + arg_10_0.getPercentageAddition(arg_10_1)

def var_0_0.getPercentageAddition(arg_11_0, arg_11_1):
	local var_11_0 = 0
	local var_11_1 = arg_11_0.getRepairRate() * 100

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.effects):
		if var_11_1 >= iter_11_1.progress:
			var_11_0 = var_11_0 + iter_11_1.getAttrAddition(arg_11_1)

	return var_11_0

def var_0_0.getRepairAddition(arg_12_0, arg_12_1):
	local var_12_0 = 0
	local var_12_1 = arg_12_0.attrs[arg_12_1]

	if var_12_1 and var_12_1.isLock():
		return 0

	if var_12_1:
		var_12_0 = var_12_0 + var_12_1.getAddition()

	return var_12_0

def var_0_0.getTotalMaxAddition(arg_13_0):
	local var_13_0 = {}

	for iter_13_0, iter_13_1 in pairs(arg_13_0.attrs):
		local var_13_1 = iter_13_1.attr
		local var_13_2 = 0

		if iter_13_1 and iter_13_1.isLock():
			var_13_2 = 0
		else
			local var_13_3 = Clone(iter_13_1)

			var_13_3.level = var_13_3.getItemCount() + 1
			var_13_2 = var_13_2 + var_13_3.getAddition()

		if var_13_0[var_13_1]:
			var_13_0[var_13_1] = var_13_0[var_13_1] + var_13_2
		else
			var_13_0[var_13_1] = var_13_2

	for iter_13_2, iter_13_3 in ipairs(arg_13_0.effects):
		local var_13_4 = iter_13_3.getAttrAdditionList()

		for iter_13_4, iter_13_5 in ipairs(var_13_4):
			local var_13_5 = iter_13_5[1]
			local var_13_6 = iter_13_5[2]

			if var_13_0[var_13_5]:
				var_13_0[var_13_5] = var_13_0[var_13_5] + var_13_6
			else
				var_13_0[var_13_5] = var_13_6

	return var_13_0

def var_0_0.getFinalAddition(arg_14_0, arg_14_1):
	assert(arg_14_1, "shipVO can not be None")

	local var_14_0 = arg_14_1.getBaseProperties()
	local var_14_1 = arg_14_0.getTotalMaxAddition()

	for iter_14_0, iter_14_1 in pairs(var_14_0):
		var_14_0[iter_14_0] = var_14_0[iter_14_0] + (var_14_1[iter_14_0] or 0)

	return var_14_0

def var_0_0.getAttrVO(arg_15_0, arg_15_1):
	return arg_15_0.attrs[arg_15_1]

def var_0_0.existAttr(arg_16_0, arg_16_1):
	return not arg_16_0.getAttrVO(arg_16_1).isLock()

def var_0_0.getEffects(arg_17_0):
	return arg_17_0.effects

def var_0_0.getUnlockedVoiceList(arg_18_0):
	local var_18_0 = arg_18_0.getEffects()
	local var_18_1 = arg_18_0.getRepairRate() * 100
	local var_18_2 = {}

	for iter_18_0, iter_18_1 in ipairs(var_18_0):
		if var_18_1 >= iter_18_1.progress and iter_18_1.words != "":
			for iter_18_2, iter_18_3 in ipairs(iter_18_1.words):
				table.insert(var_18_2, iter_18_3)

	return var_18_2

def var_0_0.getUnlockVoiceRepairPercent(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_0.getEffects()
	local var_19_1 = 0

	for iter_19_0, iter_19_1 in ipairs(var_19_0):
		if iter_19_1.words != "" and table.contains(iter_19_1.words, arg_19_1):
			var_19_1 = iter_19_1.progress

	return var_19_1

return var_0_0
