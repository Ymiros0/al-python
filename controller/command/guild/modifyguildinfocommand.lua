﻿local var_0_0 = class("ModifyGuildInfoCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(PlayerProxy)
	local var_1_2 = var_1_1:getData()
	local var_1_3 = pg.gameset.modify_guild_cost.key_value

	if type == 1 and var_1_3 > var_1_2:getTotalGem() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_rmb"))

		return
	end

	local function var_1_4()
		pg.ConnectionMgr.GetInstance():Send(60026, {
			type = var_1_0.type,
			int = var_1_0.int,
			str = var_1_0.string
		}, 60027, function(arg_3_0)
			if arg_3_0.result == 0 then
				if var_1_0.type == 1 then
					var_1_2:consume({
						gem = var_1_3
					})
					var_1_1:updatePlayer(var_1_2)
				end

				arg_1_0:sendNotification(GAME.MODIFY_GUILD_INFO_DONE)
				pg.TipsMgr.GetInstance():ShowTips(i18n("guild_info_update"))
			else
				pg.TipsMgr.GetInstance():ShowTips(errorTip("guild_modify_erro", arg_3_0.result))
			end
		end)
	end

	if var_1_0.type == 1 then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("guild_modify_info_tip", var_1_3),
			onYes = function()
				var_1_4()
			end
		})
	else
		var_1_4()
	end
end

return var_0_0
