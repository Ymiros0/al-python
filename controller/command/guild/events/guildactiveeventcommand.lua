local var_0_0 = class("GuildActiveEventCommand", import(".GuildEventBaseCommand"))

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(GuildProxy)
	local var_1_2 = var_1_0.eventId

	if not arg_1_0:ExistEvent(var_1_2) then
		return
	end

	if not arg_1_0:NotExistActiveEvent() then
		return
	end

	if not arg_1_0:IsAnim() then
		return
	end

	local var_1_3 = var_1_1:getData()
	local var_1_4 = var_1_3:GetEventById(var_1_2)
	local var_1_5 = var_1_4:GetConsume()

	if not arg_1_0:CheckCapital(var_1_4, var_1_5) then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(61001, {
		chapter_id = var_1_2
	}, 61002, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_3:IncActiveEventCnt()
			var_1_3:consumeCapital(var_1_5)
			var_1_1:updateGuild(var_1_3)
			arg_1_0:sendNotification(GAME.GUILD_ACTIVE_EVENT_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
