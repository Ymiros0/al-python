local var_0_0 = class("CommanderLearnTalentCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.talentId
	local var_1_3 = var_1_0.replaceid or 0
	local var_1_4 = getProxy(CommanderProxy)
	local var_1_5 = var_1_4.getCommanderById(var_1_1)

	if not var_1_5:
		return

	local var_1_6 = var_1_5.getNotLearnedList()

	if not _.any(var_1_6, function(arg_2_0)
		return arg_2_0.id == var_1_2):
		pg.TipsMgr.GetInstance().ShowTips(i18n("commander_talent_not_exist"))

		return

	local var_1_7 = var_1_5.getTalents()

	if var_1_3 != 0 and not _.any(var_1_7, function(arg_3_0)
		return arg_3_0.id == var_1_3):
		pg.TipsMgr.GetInstance().ShowTips(i18n("commander_replace_talent_not_exist"))

		return

	local var_1_8 = CommanderTalent.New({
		id = var_1_2
	})
	local var_1_9 = var_1_8.getConfig("cost")
	local var_1_10 = getProxy(PlayerProxy)
	local var_1_11 = var_1_10.getData()

	if var_1_9 > var_1_11.gold:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	pg.ConnectionMgr.GetInstance().Send(25012, {
		commanderid = var_1_1,
		targetid = var_1_2,
		replaceid = var_1_3
	}, 25013, function(arg_4_0)
		if arg_4_0.result == 0:
			var_1_11.consume({
				gold = var_1_9
			})
			var_1_10.updatePlayer(var_1_11)

			local var_4_0 = var_1_5.getSameGroupTalent(var_1_8.groupId)

			if var_4_0:
				var_1_5.deleteTablent(var_4_0.id)

			if var_1_3 != 0:
				var_1_5.deleteTablent(var_1_3)

			var_1_5.addTalent(var_1_8)
			var_1_5.updatePt(var_1_5.pt + 1)
			var_1_5.updateNotLearnedList({})
			var_1_4.updateCommander(var_1_5)
			arg_1_0.sendNotification(GAME.COMMANDER_LEARN_TALENTS_DONE, {
				commander = var_1_5
			})
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_talent_learned", var_1_8.getConfig("name")))
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_talent_learn_erro", arg_4_0.result)))

return var_0_0
