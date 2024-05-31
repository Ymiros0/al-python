local var_0_0 = class("EventGiveUpCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().id

	if getProxy(EventProxy).findInfoById(var_1_0).IsActivityType():
		arg_1_0.sendNotification(GAME.ACT_COLLECTION_EVENT_OP, {
			arg2 = 0,
			cmd = ActivityConst.COLLETION_EVENT_OP_GIVE_UP,
			arg1 = var_1_0,
			arg_list = {}
		})
	else
		pg.ConnectionMgr.GetInstance().Send(13007, {
			id = var_1_0
		}, 13008, function(arg_2_0)
			if arg_2_0.result == 0:
				var_0_0.OnCancel(var_1_0)
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("event_giveup_fail", arg_2_0.result)))

def var_0_0.OnCancel(arg_3_0):
	pg.TipsMgr.GetInstance().ShowTips(i18n("event_giveup_success"))

	local var_3_0, var_3_1 = getProxy(EventProxy).findInfoById(arg_3_0)

	var_3_0.state = EventInfo.StateNone

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inEvent")
	pg.m02.sendNotification(GAME.EVENT_LIST_UPDATE)

return var_0_0
