local var_0_0 = class("GuildSearchCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	if not var_1_0 or var_1_0 == "":
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_should_input_keyword"))

		return

	var_1_0 = var_1_0 and string.gsub(var_1_0, "^%s*(.-)%s*$", "%1")

	local var_1_1
	local var_1_2 = tonumber(var_1_0) and 0 or 1

	pg.ConnectionMgr.GetInstance().Send(60028, {
		type = var_1_2,
		keyword = var_1_0
	}, 60029, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.guild):
				local var_2_1 = Guild.New(iter_2_1)

				var_2_1.SetMaxMemberCntAddition(iter_2_1.tech_seat)

				local var_2_2 = GuildMember.New(iter_2_1.leader)

				var_2_2.setDuty(GuildConst.DUTY_COMMANDER)
				var_2_1.addMember(var_2_2)
				table.insert(var_2_0, var_2_1)

			arg_1_0.sendNotification(GAME.GUILD_SEARCH_DONE, var_2_0)
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_search_sucess"))
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_no_exist")))

return var_0_0
