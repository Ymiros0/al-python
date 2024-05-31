local var_0_0 = class("MusicUnlockCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.musicID
	local var_1_2 = var_1_0.unlockCBFunc
	local var_1_3 = getProxy(AppreciateProxy)
	local var_1_4 = getProxy(BagProxy)
	local var_1_5 = getProxy(PlayerProxy)
	local var_1_6 = var_1_5.getData()
	local var_1_7 = var_1_3.getMusicUnlockMaterialByID(var_1_1)

	for iter_1_0, iter_1_1 in pairs(var_1_7):
		if iter_1_1.type == DROP_TYPE_RESOURCE:
			if var_1_6.getResById(iter_1_1.id) < iter_1_1.count:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

				return
		elif iter_1_1.type == DROP_TYPE_ITEM and var_1_4.getItemCountById(iter_1_1.id) < iter_1_1.count:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_item_1"))

			return

	pg.ConnectionMgr.GetInstance().Send(17503, {
		id = var_1_1
	}, 17504, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_3.addMusicIDToUnlockList(var_1_1)

			local var_2_0 = var_1_3.getMusicUnlockMaterialByID(var_1_1)

			for iter_2_0, iter_2_1 in pairs(var_2_0):
				if iter_2_1.type == DROP_TYPE_RESOURCE:
					var_1_6.consume({
						[id2res(iter_2_1.id)] = iter_2_1.count
					})
					var_1_5.updatePlayer(var_1_6)
				elif iter_2_1.type == DROP_TYPE_ITEM:
					var_1_4.removeItemById(iter_2_1.id, iter_2_1.count)

			if var_1_2:
				var_1_2()
		else
			pg.TipsMgr.GetInstance().ShowTips("UnLock Fail, Code." .. tostring(arg_2_0.result)))

return var_0_0
