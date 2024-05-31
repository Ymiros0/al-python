local var_0_0 = class("AddFoodCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.count
	local var_1_3 = Item.getConfigData(var_1_1)
	local var_1_4 = getProxy(DormProxy)
	local var_1_5 = var_1_4.getData()
	local var_1_6 = var_1_5.getConfig("capacity") + var_1_5.dorm_food_max

	if var_1_6 < var_1_5.food + var_1_3.usage_arg[1] * var_1_2:
		var_1_5.food = var_1_6
	else
		var_1_5.food = var_1_5.food + var_1_3.usage_arg[1] * var_1_2

	if var_1_5.next_timestamp == 0:
		var_1_5.restNextTime()

	var_1_4.updateDrom(var_1_5, BackYardConst.DORM_UPDATE_TYPE_USEFOOD)
	arg_1_0.sendNotification(GAME.ADD_FOOD_DONE, {
		id = var_1_1
	})

return var_0_0
