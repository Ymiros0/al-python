﻿local var_0_0 = class("MusicUnlockCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.musicID
	local var_1_2 = var_1_0.unlockCBFunc
	local var_1_3 = getProxy(AppreciateProxy)
	local var_1_4 = getProxy(BagProxy)
	local var_1_5 = getProxy(PlayerProxy)
	local var_1_6 = var_1_5:getData()
	local var_1_7 = var_1_3:getMusicUnlockMaterialByID(var_1_1)

	for iter_1_0, iter_1_1 in pairs(var_1_7) do
		if iter_1_1.type == DROP_TYPE_RESOURCE then
			if var_1_6:getResById(iter_1_1.id) < iter_1_1.count then
				pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_resource"))

				return
			end
		elseif iter_1_1.type == DROP_TYPE_ITEM and var_1_4:getItemCountById(iter_1_1.id) < iter_1_1.count then
			pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_item_1"))

			return
		end
	end

	pg.ConnectionMgr.GetInstance():Send(17503, {
		id = var_1_1
	}, 17504, function(arg_2_0)
		if arg_2_0.result == 0 then
			var_1_3:addMusicIDToUnlockList(var_1_1)

			local var_2_0 = var_1_3:getMusicUnlockMaterialByID(var_1_1)

			for iter_2_0, iter_2_1 in pairs(var_2_0) do
				if iter_2_1.type == DROP_TYPE_RESOURCE then
					var_1_6:consume({
						[id2res(iter_2_1.id)] = iter_2_1.count
					})
					var_1_5:updatePlayer(var_1_6)
				elseif iter_2_1.type == DROP_TYPE_ITEM then
					var_1_4:removeItemById(iter_2_1.id, iter_2_1.count)
				end
			end

			if var_1_2 then
				var_1_2()
			end
		else
			pg.TipsMgr.GetInstance():ShowTips("UnLock Fail, Code:" .. tostring(arg_2_0.result))
		end
	end)
end

return var_0_0
