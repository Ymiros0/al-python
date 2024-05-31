﻿local var_0_0 = class("ReplaceRivalsCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = getProxy(MilitaryExerciseProxy)
	local var_1_1 = var_1_0:getSeasonInfo()
	local var_1_2 = var_1_1:getconsumeGem()

	if var_1_1:getFlashCount() > MAX_REPLACE_RIVAL_COUNT then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_refresh_count_insufficient"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(18003, {
		type = 0
	}, 18004, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.target_list) do
				local var_2_1 = Rival.New(iter_2_1)

				table.insert(var_2_0, var_2_1)
			end

			var_1_0:updateRivals(var_2_0)

			var_1_1 = var_1_0:getSeasonInfo()

			var_1_1:increaseFlashCount()
			var_1_0:updateSeasonInfo(var_1_1)
			arg_1_0:sendNotification(GAME.REPLACE_RIVALS_DONE, var_2_0)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
