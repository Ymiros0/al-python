local var_0_0 = class("ExtendBackYardAreaCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(DormProxy)
	local var_1_1 = var_1_0.getData()

	var_1_1.levelUp()
	var_1_0.updateDrom(var_1_1, BackYardConst.DORM_UPDATE_TYPE_LEVEL)
	arg_1_0.sendNotification(GAME.EXTEND_BACKYARD_AREA_DONE)
	pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_extendArea_ok"))

return var_0_0
