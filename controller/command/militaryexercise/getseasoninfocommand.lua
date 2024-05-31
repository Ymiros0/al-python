﻿local var_0_0 = class("GetSeasonInfoCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	pg.ConnectionMgr.GetInstance():Send(18001, {
		type = 0
	}, 18002, function(arg_2_0)
		local var_2_0 = SeasonInfo.New(arg_2_0)
		local var_2_1 = getProxy(MilitaryExerciseProxy)

		if var_2_1:getData() then
			var_2_1:updateSeasonInfo(var_2_0)
		else
			var_2_1:addSeasonInfo(var_2_0)
		end

		local var_2_2 = getProxy(PlayerProxy)
		local var_2_3 = var_2_2:getData()

		var_2_3:updateScoreAndRank(var_2_0.score, var_2_0.rank)
		var_2_2:updatePlayer(var_2_3)
		arg_1_0:sendNotification(GAME.GET_SEASON_INFO_DONE, var_2_0)
	end)
end

return var_0_0
