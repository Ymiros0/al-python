local var_0_0 = class("GetStoreResCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.oil
	local var_1_2 = var_1_0.gold

	if var_1_1 == 0 and var_1_2 == 0:
		return

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

	if not var_1_4:
		switch(var_1_5, {
			def gold:()
				pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_mail")),
			def oil:()
				pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_mail")),
			def equip:()
				pg.TipsMgr.GetInstance().ShowTips(i18n("mail_takeAttachment_error_magazine_full")),
			def ship:()
				pg.TipsMgr.GetInstance().ShowTips(i18n("mail_takeAttachment_error_dockYrad_full"))
		})

		return

	pg.ConnectionMgr.GetInstance().Send(30012, {
		oil = var_1_1,
		gold = var_1_2
	}, 30013, function(arg_6_0)
		if arg_6_0.result == 0:
			getProxy(PlayerProxy).UpdatePlayerRes({
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
			arg_1_0.sendNotification(GAME.GET_STORE_RES_DONE)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_6_0.result)))

return var_0_0
