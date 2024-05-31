local var_0_0 = class("AwardCampTecCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupID
	local var_1_2 = var_1_0.tecID
	local var_1_3 = {
		group_id = var_1_1,
		tech_id = var_1_2
	}

	print("64005 Get TecCamp Award", var_1_1, var_1_2)
	pg.ConnectionMgr.GetInstance().Send(64005, var_1_3, 64006, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.rewards)
			local var_2_1 = getProxy(TechnologyNationProxy)

			var_2_1.updateTecItemAward(var_1_1, var_1_2)
			arg_1_0.sendNotification(TechnologyConst.GOT_TEC_CAMP_AWARD, {
				awardList = var_2_0,
				groupID = var_1_1,
				tecID = var_1_2
			})
			var_2_1.refreshRedPoint()
			arg_1_0.sendNotification(TechnologyConst.UPDATE_REDPOINT_ON_TOP)
		else
			pg.TipsMgr.GetInstance().ShowTips("64005 Error Code." .. arg_2_0.result))

return var_0_0
