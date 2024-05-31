local var_0_0 = class("RemasterAwardReceiveCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.chapterId
	local var_1_2 = var_1_0.pos
	local var_1_3 = getProxy(ChapterProxy)
	local var_1_4 = var_1_3.remasterInfo[var_1_1]

	if not var_1_4 or var_1_4.receive then
		return
	end

	pg.ConnectionMgr.GetInstance():Send(13507, {
		chapter_id = var_1_1,
		pos = var_1_2
	}, 13508, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_3:markRemasterPassReceive(var_1_1, var_1_2)

			local var_2_0 = PlayerConst.addTranDrop(arg_2_0.drop_list)

			arg_1_0:sendNotification(GAME.CHAPTER_REMASTER_AWARD_RECEIVE_DONE, var_2_0)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
