﻿local var_0_0 = class("WorldBossArchivesStopAutoBattleCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.type
	local var_1_3 = nowWorld():GetBossProxy()
	local var_1_4 = var_1_3:GetSelfBoss()

	if not var_1_4 then
		return
	end

	local var_1_5 = var_1_4.hp
	local var_1_6 = var_1_3:GetHighestDamage()

	pg.ConnectionMgr.GetInstance():Send(34525, {
		boss_id = var_1_1
	}, 34526, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_3:ClearAutoBattle()

			local var_2_0 = arg_2_0.count or 0
			local var_2_1 = arg_2_0.damage or 0
			local var_2_2 = arg_2_0.oil or 0

			arg_1_0:sendNotification(GAME.WORLD_ARCHIVES_BOSS_STOP_AUTO_BATTLE_DONE, {
				cnt = var_2_0,
				damage = var_2_1,
				oil = var_2_2
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result)
		end
	end)
end

return var_0_0
