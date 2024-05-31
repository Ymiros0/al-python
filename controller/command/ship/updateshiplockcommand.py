local var_0_0 = class("UpdateShipLockCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.ship_id_list
	local var_1_2 = var_1_0.is_locked
	local var_1_3 = var_1_0.callback

	local function var_1_4()
		pg.ConnectionMgr.GetInstance().Send(12022, {
			ship_id_list = var_1_1,
			is_locked = var_1_2
		}, 12023, function(arg_3_0)
			if arg_3_0.result == 0:
				local var_3_0 = getProxy(BayProxy)
				local var_3_1

				if var_1_2 == Ship.LOCK_STATE_LOCK:
					var_3_1 = "ship_updateShipLock_ok_lock"
				elif var_1_2 == Ship.LOCK_STATE_UNLOCK:
					var_3_1 = "ship_updateShipLock_ok_unlock"

				for iter_3_0, iter_3_1 in ipairs(var_1_1):
					local var_3_2 = var_3_0.getShipById(iter_3_1)

					var_3_2.SetLockState(var_1_2)
					var_3_0.updateShip(var_3_2)
					arg_1_0.sendNotification(GAME.UPDATE_LOCK_DONE, var_3_2)
					pg.TipsMgr.GetInstance().ShowTips(i18n(var_3_1, var_3_2.getName()))

				if var_1_3:
					var_1_3()
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("ship_updateShipLock", arg_3_0.result)))

	if var_1_2 == Ship.LOCK_STATE_UNLOCK:
		local var_1_5 = pg.SecondaryPWDMgr

		var_1_5.LimitedOperation(var_1_5.UNLOCK_SHIP, var_1_0.ship_id_list, var_1_4)
	else
		var_1_4()

return var_0_0
