local var_0_0 = class("ChangePlayerIconCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.characterId
	local var_1_2 = var_1_0.characterId
	local var_1_3 = var_1_0.skinPage
	local var_1_4 = var_1_0.callback
	local var_1_5 = getProxy(PlayerProxy)
	local var_1_6 = var_1_5.getData()

	if type(var_1_1) == "number":
		if var_1_6.character == var_1_1:
			if var_1_3:
				pg.TipsMgr.GetInstance().ShowTips(i18n("change_skin_secretary_ship"))

			return
		else
			var_1_2 = {}

			for iter_1_0 = 1, #var_1_6.characters:
				var_1_2[iter_1_0] = var_1_6.characters[iter_1_0]

			for iter_1_1 = 1, #var_1_2:
				if var_1_2[iter_1_1] == var_1_1:
					var_1_2[1], var_1_2[iter_1_1] = var_1_2[iter_1_1], var_1_2[1]

			var_1_2[1] = var_1_1

	if #var_1_2 <= 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_error"))

		return

	pg.ConnectionMgr.GetInstance().Send(11011, {
		character = var_1_2
	}, 11012, function(arg_2_0)
		if arg_2_0.result == 0:
			var_0_0.UpdayePlayerCharas(var_1_6, var_1_2)
			var_1_5.updatePlayer(var_1_6)
			pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inAdmiral")

			if var_1_3:
				pg.TipsMgr.GetInstance().ShowTips(i18n("change_skin_secretary_ship"))
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("player_changePlayerIcon_ok"))

			arg_1_0.sendNotification(GAME.CHANGE_PLAYER_ICON_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("player_changePlayerIcon", arg_2_0.result))

		if var_1_4:
			var_1_4())

def var_0_0.UpdayePlayerCharas(arg_3_0, arg_3_1):
	local var_3_0 = getProxy(BayProxy).getShipById(arg_3_1[1])

	arg_3_0.character = arg_3_1[1]
	arg_3_0.characters = arg_3_1
	arg_3_0.icon = var_3_0.configId
	arg_3_0.skinId = var_3_0.skinId

return var_0_0
