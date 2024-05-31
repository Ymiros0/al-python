﻿local var_0_0 = class("GuildApplyCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.content or ""

	if wordVer(var_1_2) > 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("friend_msg_forbid"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(60005, {
		id = var_1_1,
		content = var_1_2
	}, 60006, function(arg_2_0)
		if arg_2_0.result == 0 then
			arg_1_0:sendNotification(GAME.GUILD_APPLY_DONE)
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_apply_sucess"))
		elseif arg_2_0.result == 4 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_join_cd"))
		elseif arg_2_0.result == 6 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_apply_full"))
		elseif arg_2_0.result == 4305 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_tip_grand_fleet_is_frozen"))
		elseif arg_2_0.result == 4306 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("guild_member_full"))
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("guild_apply_erro", arg_2_0.result))
		end
	end)
end

return var_0_0
