local var_0_0 = class("ExtendStoreCapacityCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().isDiamond
	local var_1_1 = ({
		getProxy(PlayerProxy).getRawData().GetExtendStoreCost()
	})[var_1_0 and 1 or 2]

	if not var_1_1:
		pg.TipsMgr.GetInstance().ShowTips("level max")

		return
	elif var_1_1.getOwnedCount() < var_1_1.count:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_x", var_1_1.getName()))

		return

	pg.ConnectionMgr.GetInstance().Send(30010, {
		arg = var_1_1.id
	}, 30011, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = getProxy(PlayerProxy).getData()

			var_2_0.consume({
				[id2res(var_1_1.id)] = var_1_1.count
			})

			var_2_0.mailStoreLevel = var_2_0.mailStoreLevel + 1

			getProxy(PlayerProxy).updatePlayer(var_2_0)
			arg_1_0.sendNotification(GAME.EXTEND_STORE_CAPACITY_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
