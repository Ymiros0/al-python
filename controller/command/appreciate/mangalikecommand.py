local var_0_0 = class("MangaLikeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.mangaID
	local var_1_2 = var_1_0.action
	local var_1_3 = var_1_0.mangaCB
	local var_1_4 = getProxy(AppreciateProxy)

	print("17511 Send Manga ID", var_1_1)
	pg.ConnectionMgr.GetInstance().Send(17511, {
		id = var_1_1,
		action = var_1_2
	}, 17512, function(arg_2_0)
		if arg_2_0.result == 0:
			if var_1_2 == MangaConst.SET_MANGA_LIKE:
				var_1_4.addMangaIDToLikeList(var_1_1)
			else
				var_1_4.removeMangaIDFromLikeList(var_1_1)

			if var_1_3:
				var_1_3()

			arg_1_0.sendNotification(GAME.APPRECIATE_MANGA_LIKE_DONE, {
				mangaID = var_1_1,
				action = var_1_2
			})
		else
			pg.TipsMgr.GetInstance().ShowTips("17512 Manga Like Fail." .. tostring(arg_2_0.result)))

return var_0_0
