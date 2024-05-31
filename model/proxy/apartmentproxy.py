local var_0_0 = class("ApartmentProxy", import(".NetProxy"))

var_0_0.UPDATE_APARTMENT = "ApartmentProxy.UPDATE_APARTMENT"
var_0_0.UPDATE_GIFT_COUNT = "ApartmentProxy.UPDATE_GIFT_COUNT"

def var_0_0.register(arg_1_0):
	arg_1_0.data = {}
	arg_1_0.giftBag = setDefaultZeroMetatable({})
	arg_1_0.giftGiveCount = setDefaultZeroMetatable({})

def var_0_0.updateApartment(arg_2_0, arg_2_1):
	arg_2_0.data[arg_2_1.configId] = arg_2_1.clone()

	arg_2_0.sendNotification(var_0_0.UPDATE_APARTMENT, arg_2_1)

def var_0_0.getApartment(arg_3_0, arg_3_1):
	return arg_3_0.data[arg_3_1] and arg_3_0.data[arg_3_1].clone() or None

def var_0_0.getGiftCount(arg_4_0, arg_4_1):
	return arg_4_0.giftBag[arg_4_1]

def var_0_0.changeGiftCount(arg_5_0, arg_5_1, arg_5_2):
	assert(arg_5_2 != 0)

	arg_5_0.giftBag[arg_5_1] = arg_5_0.giftBag[arg_5_1] + arg_5_2

	arg_5_0.sendNotification(var_0_0.UPDATE_GIFT_COUNT, arg_5_1)

def var_0_0.addGiftGiveCount(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.giftGiveCount[arg_6_1] = arg_6_0.giftGiveCount[arg_6_1] + arg_6_2

def var_0_0.isGiveGiftDone(arg_7_0, arg_7_1):
	return arg_7_0.giftGiveCount[arg_7_1] > 0

def var_0_0.getGiftUnlockTalk(arg_8_0, arg_8_1, arg_8_2):
	for iter_8_0, iter_8_1 in ipairs(pg.dorm3d_dialogue_group.get_id_list_by_char_id[20220]):
		local var_8_0 = pg.dorm3d_dialogue_group[iter_8_1]

		if var_8_0.type == 401 and table.contains(var_8_0.trigger_config, arg_8_2):
			return iter_8_1

def var_0_0.GetTimeIndex(arg_9_0):
	local var_9_0 = 3

	for iter_9_0, iter_9_1 in ipairs({
		7,
		16,
		20
	}):
		if arg_9_0 < iter_9_1:
			break
		else
			var_9_0 = iter_9_0

	return var_9_0

return var_0_0
