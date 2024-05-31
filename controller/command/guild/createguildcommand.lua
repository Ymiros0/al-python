local var_0_0 = class("CreateGuildCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0:getName()
	local var_1_2 = pg.gameset.create_guild_cost.key_value
	local var_1_3 = getProxy(PlayerProxy)
	local var_1_4 = var_1_3:getData()

	if var_1_2 > var_1_4:getTotalGem() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("guild_create_error_nomoney"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(60001, {
		faction = var_1_0:getFaction(),
		policy = var_1_0:getPolicy(),
		name = var_1_1,
		manifesto = var_1_0:getManifesto()
	}, 60002, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = Guild.New({
				base = var_1_0
			})

			var_2_0:setId(arg_2_0.id)

			local var_2_1 = getProxy(GuildProxy)
			local var_2_2 = GuildMember.New({
				online = 1,
				liveness = 0,
				id = var_1_4.id,
				name = var_1_4.name,
				lv = var_1_4.level,
				adv = var_1_4.manifesto,
				display = {
					icon = var_1_4.icon,
					character = var_1_4.character,
					icon_theme = var_1_4.iconTheme,
					transform_flag = var_1_4.transformFlag,
					skin = var_1_4.skinId,
					marry_flag = var_1_4.proposeTime
				},
				join_time = pg.TimeMgr.GetInstance():GetServerTime()
			})

			var_2_2:setDuty(GuildConst.DUTY_COMMANDER)
			var_2_0:addMember(var_2_2)

			local var_2_3 = pg.guildset.guild_tech_default.key_value

			var_2_0:StartTech(var_2_3)
			var_2_1:addGuild(var_2_0)
			var_1_4:consume({
				gem = var_1_2
			})
			var_1_3:updatePlayer(var_1_4)
			arg_1_0:sendNotification(GAME.HANDLE_GUILD_AND_PUBLIC_GUILD_TECH)
			arg_1_0:sendNotification(GAME.CREATE_GUILD_DONE)
			arg_1_0:sendNotification(GAME.GUILD_GET_USER_INFO)
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_create_sucess"))
		elseif arg_2_0.result == 2015 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_name_invaild"))
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("guild_create_error", arg_2_0.result))
		end
	end)
end

return var_0_0
