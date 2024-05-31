local var_0_0 = class("RemasterInfoRequestCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	pg.ConnectionMgr.GetInstance():Send(13505, {
		type = 0
	}, 13506, function(arg_2_0)
		local var_2_0 = getProxy(ChapterProxy).remasterInfo

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.remap_count_list) do
			if var_2_0[iter_2_1.chapter_id][iter_2_1.pos] then
				var_2_0[iter_2_1.chapter_id][iter_2_1.pos].count = iter_2_1.count
				var_2_0[iter_2_1.chapter_id][iter_2_1.pos].receive = iter_2_1.flag > 0
			end
		end

		arg_1_0:sendNotification(GAME.CHAPTER_REMASTER_INFO_REQUEST_DONE)
	end)
end

return var_0_0
