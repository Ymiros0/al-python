﻿local var_0_0 = class("GuildUpdateAssaultFleetCommand", import(".GuildEventBaseCommand"))

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.fleet
	local var_1_2 = var_1_0.callBack
	local var_1_3 = getProxy(GuildProxy)
	local var_1_4 = var_1_3:getData()
	local var_1_5 = var_1_4:GetActiveEvent()

	if var_1_5 then
		local var_1_6 = var_1_5:GetBossMission()

		if var_1_6 and var_1_6:IsActive() then
			pg.TipsMgr:GetInstance():ShowTips(i18n("guild_formation_erro_in_boss_battle"))

			return
		end
	end

	local var_1_7 = getProxy(PlayerProxy):getRawData().id
	local var_1_8 = var_1_4:getMemberById(var_1_7)
	local var_1_9 = var_1_8:GetExternalAssaultFleet()

	if not var_1_9 then
		return
	end

	if not var_1_1 then
		return
	end

	if not var_1_9:AnyShipChanged(var_1_1) then
		pg.TipsMgr.GetInstance():ShowTips(i18n("guild_must_edit_fleet"))

		return
	end

	local var_1_10 = {}
	local var_1_11 = var_1_1:GetShipList()

	for iter_1_0, iter_1_1 in pairs(var_1_11) do
		if var_1_9:PositionIsChanged(var_1_1, iter_1_0) then
			local var_1_12 = GuildAssaultFleet.GetRealId(iter_1_1.id)

			table.insert(var_1_10, {
				pos = iter_1_0,
				shipId = var_1_12
			})
		end
	end

	pg.ConnectionMgr.GetInstance():Send(61003, {
		shipIds = var_1_10
	}, 61004, function(arg_2_0)
		if arg_2_0.result == 0 then
			for iter_2_0, iter_2_1 in ipairs(var_1_10) do
				local var_2_0 = pg.TimeMgr.GetInstance():GetServerTime()

				var_1_3:UpdatePosCdTime(iter_2_1.pos, var_2_0)
			end

			var_1_8:UpdateAssaultFleet(var_1_1)
			var_1_8:UpdateExternalAssaultFleet(var_1_1)
			var_1_3:updateGuild(var_1_4)
			arg_1_0:sendNotification(GAME.GUILD_UPDATE_MY_ASSAULT_FLEET_DONE)
			pg.ShipFlagMgr:GetInstance():UpdateFlagShips("inGuildEvent")
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end

		if var_1_2 then
			var_1_2()
		end
	end)
end

return var_0_0
