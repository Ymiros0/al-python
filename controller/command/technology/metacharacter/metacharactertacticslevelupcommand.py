local var_0_0 = class("MetaCharacterTacticsLevelUpCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipID
	local var_1_2 = var_1_0.skillID

	print("63309 skill levelup", tostring(var_1_1), tostring(var_1_2))
	pg.ConnectionMgr.GetInstance().Send(63309, {
		ship_id = var_1_1,
		skill_id = var_1_2
	}, 63310, function(arg_2_0)
		if arg_2_0.result == 0:
			print("63310 skill levelup success")

			local var_2_0 = getProxy(BayProxy)
			local var_2_1 = var_2_0.getShipById(var_1_1)

			var_2_1.upSkillLevelForMeta(var_1_2)
			var_2_0.updateShip(var_2_1)

			local var_2_2 = arg_2_0.switch_cnt

			arg_1_0.sendNotification(GAME.TACTICS_META_LEVELUP_SKILL_DONE, {
				skillID = var_1_2,
				leftSwitchCount = var_2_2
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
