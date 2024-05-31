local var_0_0 = class("ApartmentGiveGiftCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.giftId
	local var_1_3 = var_1_0.count
	local var_1_4 = getProxy(ApartmentProxy)

	if var_1_3 > var_1_4.getGiftCount(var_1_2):
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_item_1"))

		return

	local var_1_5 = var_1_4.getApartment(var_1_1)

	pg.ConnectionMgr.GetInstance().Send(28009, {
		ship_group = var_1_1,
		gifts = {
			{
				gift_id = var_1_2,
				number = var_1_3
			}
		}
	}, 28010, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_4.addGiftGiveCount(var_1_2, var_1_3)
			var_1_4.changeGiftCount(var_1_2, -var_1_3)

			local var_2_0 = pg.dorm3d_gift[var_1_2].favor_trigger_id

			var_1_5 = var_1_4.getApartment(var_1_1)

			local var_2_1 = var_1_5.addFavor(var_2_0)

			var_1_4.updateApartment(var_1_5)
			arg_1_0.sendNotification(GAME.APARTMENT_TRIGGER_FAVOR_DONE, {
				triggerId = var_2_0,
				delta = var_2_1,
				apartment = var_1_5
			})
			arg_1_0.sendNotification(GAME.APARTMENT_GIVE_GIFT_DONE, var_1_2)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
