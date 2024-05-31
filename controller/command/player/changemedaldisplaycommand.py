local var_0_0 = class("ChangeMedalDisplayCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().medalList
	local var_1_1 = getProxy(PlayerProxy)
	local var_1_2 = var_1_1.getData().displayTrophyList
	local var_1_3 = 0

	while var_1_3 < 5:
		if var_1_0[var_1_3] != var_1_2[var_1_3]:
			break

		if var_1_3 == 5:
			return

		var_1_3 = var_1_3 + 1

	local var_1_4 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0):
		table.insert(var_1_4, iter_1_1)

	pg.ConnectionMgr.GetInstance().Send(17401, {
		fixed_const = 1,
		medal_id = var_1_4
	}, 17402, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_1.updatePlayerMedalDisplay(var_1_0)
			pg.TipsMgr.GetInstance().ShowTips(i18n("change_display_medal_success"))
			arg_1_0.sendNotification(GAME.CHANGE_PLAYER_MEDAL_DISPLAY_DONE))

return var_0_0
