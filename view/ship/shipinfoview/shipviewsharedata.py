local var_0_0 = class("ShipViewShareData")

def var_0_0.Ctor(arg_1_0):
	arg_1_0.shipVO = None

def var_0_0.SetShipVO(arg_2_0, arg_2_1):
	arg_2_0.shipVO = arg_2_1

def var_0_0.SetPlayer(arg_3_0, arg_3_1):
	arg_3_0.player = arg_3_1

def var_0_0.HasFashion(arg_4_0):
	return getProxy(ShipSkinProxy).HasFashion(arg_4_0.shipVO)

def var_0_0.GetCurGroupSkinList(arg_5_0):
	return arg_5_0.GetGroupSkinList(arg_5_0.shipVO.groupId)

def var_0_0.GetGroupSkinList(arg_6_0, arg_6_1):
	return getProxy(ShipSkinProxy).GetAllSkinForShip(arg_6_0.shipVO)

return var_0_0
