local var_0_0 = class("EquipCodeLikeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.groupId
	local var_1_2 = var_1_0.shareId
	local var_1_3 = getProxy(CollectionProxy)
	local var_1_4 = var_1_3.getShipGroup(var_1_1)
	local var_1_5 = underscore.detect(var_1_4.getEquipCodes(), function(arg_2_0)
		return arg_2_0.id == var_1_2)

	pg.ConnectionMgr.GetInstance().Send(17605, {
		shipgroup = var_1_1,
		shareid = var_1_2
	}, 17606, function(arg_3_0)
		if arg_3_0.result == 0:
			var_1_5.afterLike = True
			var_1_5.like = var_1_5.like + 1

			var_1_3.updateShipGroup(var_1_4)
			arg_1_0.sendNotification(GAME.EQUIP_CODE_LIKE_DONE, {
				like = True,
				shareId = var_1_2
			})
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_like_success"))
		elif arg_3_0.result == 7:
			var_1_5.afterLike = True

			var_1_3.updateShipGroup(var_1_4)
			arg_1_0.sendNotification(GAME.EQUIP_CODE_LIKE_DONE, {
				shareId = var_1_2
			})
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_like_limited"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_3_0.result)))

return var_0_0
