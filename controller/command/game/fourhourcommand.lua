local var_0_0 = class("FourHourCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0, var_1_1 = pcall(arg_1_0.mainHandler, arg_1_0)

	if not var_1_0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("four_hour_command_error"))
		error(var_1_1)
	end
end

function var_0_0.mainHandler(arg_2_0, arg_2_1)
	getProxy(TechnologyProxy):resetPursuingTimes()
	arg_2_0:sendNotification(GAME.FOUR_HOUR_OP_DONE)
end

return var_0_0
