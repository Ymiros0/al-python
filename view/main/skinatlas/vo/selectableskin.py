local var_0_0 = class("SelectableSkin")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.skinId = arg_1_1.id
	arg_1_0.isTimeLimit = arg_1_1.isTimeLimit
	arg_1_0.own = getProxy(ShipSkinProxy).hasSkin(arg_1_0.skinId)

def var_0_0.IsTimeLimit(arg_2_0):
	return arg_2_0.isTimeLimit

def var_0_0.OwnSkin(arg_3_0):
	return arg_3_0.own

def var_0_0.ToShipSkin(arg_4_0):
	return ShipSkin.New({
		id = arg_4_0.skinId
	})

def var_0_0.GetTimeLimitWeight(arg_5_0):
	return arg_5_0.IsTimeLimit() and 1 or 0

def var_0_0.GetOwnWeight(arg_6_0):
	return arg_6_0.OwnSkin() and 0 or 1

return var_0_0
