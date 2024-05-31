local var_0_0 = class("MetaCharacterTacticsSwitchCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.shipID
	local var_1_2 = var_1_0.skillID

	print("63307 switch skill", tostring(var_1_1), tostring(var_1_2))
	pg.ConnectionMgr.GetInstance().Send(63307, {
		ship_id = var_1_1,
		skill_id = var_1_2
	}, 63308, function(arg_2_0)
		if arg_2_0.result == 0:
			print("63308 switch success")
			getProxy(MetaCharacterProxy).switchMetaTacticsSkill(var_1_1, var_1_2)
			getProxy(MetaCharacterProxy).tryRemoveMetaSkillLevelMaxInfo(var_1_1, var_1_2)

			local var_2_0 = arg_2_0.switch_cnt

			arg_1_0.sendNotification(GAME.TACTICS_META_SWITCH_SKILL_DONE, {
				metaShipID = var_1_1,
				skillID = var_1_2,
				leftSwitchCount = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_2_0.result)))

return var_0_0
