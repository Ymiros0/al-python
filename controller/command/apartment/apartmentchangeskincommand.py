local var_0_0 = class("ApartmentChangeSkinCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.skinId
	local var_1_3 = getProxy(ApartmentProxy)
	local var_1_4 = var_1_3.getApartment(var_1_1)

	if var_1_2 == var_1_4.getConfig("skin_model"):
		var_1_2 = 0

	if var_1_4.skinId == var_1_2:
		return

	pg.ConnectionMgr.GetInstance().Send(28013, {
		ship_group = var_1_1,
		skin = var_1_2
	}, 28014, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_4 = var_1_3.getApartment(var_1_1)
			var_1_4.skinId = var_1_2

			var_1_3.updateApartment(var_1_4)
			arg_1_0.sendNotification(GAME.APARTMENT_CHANGE_SKIN_DONE, var_1_4)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
