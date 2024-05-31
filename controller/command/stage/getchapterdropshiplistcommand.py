local var_0_0 = class("GetChapterDropShipListCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.chapterId
	local var_1_2 = var_1_0.callback

	assert(var_1_1)

	local var_1_3 = getProxy(ChapterProxy)

	if not var_1_3.FectchDropShipListFlags:
		var_1_3.FectchDropShipListFlags = {}

	if not var_1_3.FectchDropShipListFlags[var_1_1]:
		pg.ConnectionMgr.GetInstance().Send(13109, {
			id = var_1_1
		}, 13110, function(arg_2_0)
			local var_2_0 = {}

			for iter_2_0, iter_2_1 in ipairs(arg_2_0.drop_ship_list):
				table.insert(var_2_0, iter_2_1)

			local var_2_1 = var_1_3.getChapterById(var_1_1)

			var_2_1.UpdateDropShipList(var_2_0)

			var_1_3.FectchDropShipListFlags[var_1_1] = True

			var_1_3.updateChapter(var_2_1)

			local var_2_2 = var_2_1.GetDropShipList()

			if var_1_2:
				var_1_2(var_2_2)

			arg_1_0.sendNotification(GAME.GET_CHAPTER_DROP_SHIP_LIST_DONE, {
				shipIds = var_2_2
			}))
	else
		local var_1_4 = var_1_3.getChapterById(var_1_1).GetDropShipList()

		if var_1_2:
			var_1_2(var_1_4)

		arg_1_0.sendNotification(GAME.GET_CHAPTER_DROP_SHIP_LIST_DONE, {
			shipIds = var_1_4
		})

return var_0_0
