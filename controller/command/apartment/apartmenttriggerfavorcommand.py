local var_0_0 = class("ApartmentTriggerFavorCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.triggerId
	local var_1_3 = getProxy(ApartmentProxy)
	local var_1_4 = var_1_3.getApartment(var_1_1)

	if pg.dorm3d_favor_trigger[var_1_2].is_repeat > 0:
		if var_1_4.daily >= getDorm3dGameset("daily_exp_max")[1]:
			return
	elif var_1_4.triggerCountDic[var_1_2] > 0:
		return

	pg.ConnectionMgr.GetInstance().Send(28003, {
		ship_group = var_1_1,
		trigger_id = var_1_2
	}, 28004, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_4 = var_1_3.getApartment(var_1_1)

			local var_2_0 = var_1_4.addFavor(var_1_2)

			var_1_3.updateApartment(var_1_4)
			arg_1_0.sendNotification(GAME.APARTMENT_TRIGGER_FAVOR_DONE, {
				triggerId = var_1_2,
				delta = var_2_0,
				apartment = var_1_4
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
