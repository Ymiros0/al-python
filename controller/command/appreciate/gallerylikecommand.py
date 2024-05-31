local var_0_0 = class("GalleryLikeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.picID
	local var_1_2 = var_1_0.isAdd
	local var_1_3 = var_1_0.likeCBFunc
	local var_1_4 = getProxy(AppreciateProxy)

	pg.ConnectionMgr.GetInstance().Send(17505, {
		id = var_1_1,
		action = var_1_2
	}, 17506, function(arg_2_0)
		if arg_2_0.result == 0:
			if var_1_2 == 0:
				var_1_4.addPicIDToLikeList(var_1_1)
			elif var_1_2 == 1:
				var_1_4.removePicIDFromLikeList(var_1_1)

			if var_1_3:
				var_1_3()
		else
			pg.TipsMgr.GetInstance().ShowTips("Like Fail" .. tostring(arg_2_0.result)))

return var_0_0
