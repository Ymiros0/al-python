﻿local var_0_0 = class("LockCommanderCommande", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.commanderId
	local var_1_2 = var_1_0.flag
	local var_1_3 = getProxy(CommanderProxy)
	local var_1_4 = var_1_3:getCommanderById(var_1_1)

	if not var_1_4 or var_1_4:getLock() == var_1_2 then
		return
	end

	local function var_1_5()
		pg.ConnectionMgr.GetInstance():Send(25016, {
			commanderid = var_1_1,
			flag = var_1_2
		}, 25017, function(arg_3_0)
			if arg_3_0.result == 0 then
				var_1_4:setLock(var_1_2)
				var_1_3:updateCommander(var_1_4)
				arg_1_0:sendNotification(GAME.COMMANDER_LOCK_DONE, {
					commander = var_1_4,
					flag = var_1_2
				})
			else
				pg.TipsMgr.GetInstance():ShowTips(i18n("commander_lock_erro", arg_3_0.result))
			end
		end)
	end

	if var_1_2 == 0 then
		local var_1_6 = pg.SecondaryPWDMgr.GetInstance()

		var_1_6:LimitedOperation(var_1_6.UNLOCK_COMMANDER, var_1_1, var_1_5)
	else
		var_1_5()
	end
end

return var_0_0
