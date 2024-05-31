local var_0_0 = class("CommanderQuicklyFinishBoxesCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.itemCnt
	local var_1_2 = var_1_0.finishCnt
	local var_1_3 = var_1_0.affectCnt

	pg.ConnectionMgr.GetInstance():Send(25037, {
		item_cnt = var_1_1,
		finish_cnt = var_1_2,
		affect_cnt = var_1_3
	}, 25038, function(arg_2_0)
		if arg_2_0.result == 0 then
			getProxy(BagProxy):removeItemById(Item.COMMANDER_QUICKLY_TOOL_ID, var_1_1)
			arg_1_0:sendNotification(GAME.COMMANDER_QUICKLY_FINISH_BOXES_DONE)
			arg_1_0:sendNotification(GAME.REFRESH_COMMANDER_BOXES)
		else
			arg_1_0:sendNotification(GAME.COMMANDER_QUICKLY_FINISH_BOXES_ERROR)
		end
	end)
end

return var_0_0
