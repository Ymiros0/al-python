local var_0_0 = class("GetStoreResCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.oil
	local var_1_2 = var_1_0.gold

	if var_1_1 == 0 and var_1_2 == 0 then
		return
	end

	local var_1_3 = GetItemsOverflowDic({
		Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = PlayerConst.ResOil,
			count = var_1_1
		}),
		Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = PlayerConst.ResGold,
			count = var_1_2
		})
	})
	local var_1_4, var_1_5 = CheckOverflow(var_1_3)

	if not var_1_4 then
		switch(var_1_5, {
			gold = function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_mail"))
			end,
			oil = function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_mail"))
			end,
			equip = function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("mail_takeAttachment_error_magazine_full"))
			end,
			ship = function()
				pg.TipsMgr.GetInstance():ShowTips(i18n("mail_takeAttachment_error_dockYrad_full"))
			end
		})

		return
	end

	pg.ConnectionMgr.GetInstance():Send(30012, {
		oil = var_1_1,
		gold = var_1_2
	}, 30013, function(arg_6_0)
		if arg_6_0.result == 0 then
			getProxy(PlayerProxy):UpdatePlayerRes({
				{
					id = PlayerConst.ResOil,
					count = var_1_1
				},
				{
					id = PlayerConst.ResStoreOil,
					count = -var_1_1
				},
				{
					id = PlayerConst.ResGold,
					count = var_1_2
				},
				{
					id = PlayerConst.ResStoreGold,
					count = -var_1_2
				}
			})
			arg_1_0:sendNotification(GAME.GET_STORE_RES_DONE)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_6_0.result))
		end
	end)
end

return var_0_0
