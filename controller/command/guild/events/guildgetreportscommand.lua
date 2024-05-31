local var_0_0 = class("GuildGetReportsCommand", import(".GuildEventBaseCommand"))

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().callback
	local var_1_1 = getProxy(GuildProxy)

	if not var_1_1:ShouldRequestReport() then
		local var_1_2 = var_1_1:GetReports()

		if var_1_0 then
			var_1_0(var_1_2)
		end

		return
	end

	local var_1_3 = getProxy(GuildProxy):GetMaxReportId()

	pg.ConnectionMgr.GetInstance():Send(61017, {
		index = var_1_3
	}, 61018, function(arg_2_0)
		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.reports) do
			local var_2_1

			if iter_2_1.event_type == GuildConst.REPORT_TYPE_BOSS then
				var_2_1 = GuildBossReport.New(iter_2_1)
			else
				var_2_1 = GuildReport.New(iter_2_1)
			end

			var_1_1:AddReport(var_2_1)
		end

		if var_1_0 then
			local var_2_2 = var_1_1:GetReports()

			var_1_0(var_2_2)
		end

		arg_1_0:sendNotification(GAME.GET_GUILD_REPORT_DONE)
	end)
end

return var_0_0
