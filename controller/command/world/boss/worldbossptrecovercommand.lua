﻿local var_0_0 = class("WorldBossPtRecoverCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = nowWorld():GetBossProxy()

	if var_1_0:isMaxPt() then
		return
	end

	local var_1_1 = var_1_0:GetNextReconveTime()
	local var_1_2 = pg.TimeMgr.GetInstance():GetServerTime()
	local var_1_3 = var_1_0:GetRecoverPtTime()

	if var_1_1 <= var_1_2 then
		local var_1_4 = var_1_2 - var_1_1

		var_1_0:increasePt()

		if not var_1_0:isMaxPt() then
			while var_1_3 <= var_1_4 do
				var_1_0:increasePt()

				var_1_4 = var_1_4 - var_1_3
			end

			local var_1_5 = var_1_2 + (var_1_3 - var_1_4)

			var_1_0:updatePtTime(var_1_5)
		end
	end

	arg_1_0:sendNotification(GAME.WORLD_BOSS_PT_RECOVER_DONE)
end

return var_0_0
