local var_0_0 = class("EventStartCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.shipIds
	local var_1_3 = getProxy(EventProxy)
	local var_1_4 = var_1_3.findInfoById(var_1_1)
	local var_1_5 = var_1_4.IsActivityType()

	if not var_1_5 and var_1_3.busyFleetNums >= var_1_3.maxFleetNums:
		pg.TipsMgr.GetInstance().ShowTips(i18n("event_fleet_busy"))

		return

	local var_1_6, var_1_7 = var_1_3.CanJoinEvent(var_1_4)

	if not var_1_6:
		if var_1_7:
			pg.TipsMgr.GetInstance().ShowTips(var_1_7)

		return

	local function var_1_8()
		if var_1_5:
			arg_1_0.sendNotification(GAME.ACT_COLLECTION_EVENT_OP, {
				arg2 = 0,
				cmd = ActivityConst.COLLETION_EVENT_OP_JOIN,
				arg1 = var_1_1,
				arg_list = var_1_2
			})
		else
			pg.ConnectionMgr.GetInstance().Send(13003, {
				id = var_1_1,
				ship_id_list = var_1_2
			}, 13004, function(arg_3_0)
				if arg_3_0.result == 0:
					var_0_0.OnStart(var_1_1)
				else
					pg.TipsMgr.GetInstance().ShowTips(errorTip("event_start_fail", arg_3_0.result)))

	local var_1_9 = var_1_4.getOilConsume()

	if var_1_9 > 0:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("event_oil_consume", var_1_9),
			onYes = var_1_8
		})
	else
		var_1_8()

def var_0_0.OnStart(arg_4_0):
	pg.TipsMgr.GetInstance().ShowTips(i18n("event_start_success"))

	local var_4_0 = getProxy(EventProxy).findInfoById(arg_4_0)
	local var_4_1 = getProxy(PlayerProxy)
	local var_4_2 = var_4_1.getData()

	var_4_0.finishTime = pg.TimeMgr.GetInstance().GetServerTime() + var_4_0.template.collect_time
	var_4_0.state = EventInfo.StateActive

	local var_4_3 = var_4_0.getOilConsume()

	var_4_2.consume({
		oil = var_4_3
	})
	var_4_1.updatePlayer(var_4_2)
	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inEvent")
	pg.m02.sendNotification(GAME.EVENT_LIST_UPDATE)

return var_0_0
