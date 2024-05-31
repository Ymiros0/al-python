local var_0_0 = class("SetTecAttrAdditionCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.sendList
	local var_1_2 = var_1_0.onSuccess
	local var_1_3 = {
		techset_list = var_1_1
	}

	print("64009 Set Attr Addition")

	if Application.isEditor:
		print_r(var_1_1)

	pg.ConnectionMgr.GetInstance().Send(64009, var_1_3, 64010, function(arg_2_0)
		if arg_2_0.result == 0:
			getProxy(TechnologyNationProxy).initSetableAttrAddition(var_1_1)
			arg_1_0.sendNotification(TechnologyConst.SET_TEC_ATTR_ADDITION_FINISH, {
				onSuccess = var_1_2
			})
			pg.TipsMgr.GetInstance().ShowTips(i18n("attrset_save_success"))
		else
			pg.TipsMgr.GetInstance().ShowTips("64009 Error Code." .. arg_2_0.result))

return var_0_0
