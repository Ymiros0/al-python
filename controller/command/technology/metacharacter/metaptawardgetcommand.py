local var_0_0 = class("MetaPTAwardGetCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(MetaCharacterProxy)
	local var_1_1 = arg_1_1.getBody()
	local var_1_2 = {
		group_id = var_1_1.groupID,
		target_pt = var_1_1.targetCount
	}

	print("34003 meta pt award send.", var_1_1.groupID, var_1_1.targetCount)
	pg.ConnectionMgr.GetInstance().Send(34003, var_1_2, 34004, function(arg_2_0)
		print("34004 meta pt award:ne.", arg_2_0.result)

		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)
			local var_2_1 = var_1_0.getMetaProgressVOByID(var_1_1.groupID)
			local var_2_2 = var_2_1.metaPtData.targets
			local var_2_3 = table.indexof(var_2_2, var_1_1.targetCount)

			var_2_1.updatePTLevel(var_2_3)
			arg_1_0.sendNotification(GAME.GET_META_PT_AWARD_DONE, {
				awards = var_2_0
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(34004 + " . " + arg_2_0.result))

return var_0_0
