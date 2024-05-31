local var_0_0 = class("TrophyClaimCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().trophyID
	local var_1_1 = getProxy(CollectionProxy)

	pg.ConnectionMgr.GetInstance().Send(17301, {
		id = var_1_0
	}, 17302, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = arg_2_0.timestamp

			var_1_1.updateTrophyClaim(var_1_0, var_2_0)

			local var_2_1 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.next):
				var_2_1[#var_2_1 + 1] = Trophy.New(iter_2_1)

			var_1_1.unlockNewTrophy(var_2_1)
			arg_1_0.sendNotification(GAME.TROPHY_CLAIM_DONE, {
				trophyID = var_1_0
			})
			var_1_1.updateTrophy())

return var_0_0
