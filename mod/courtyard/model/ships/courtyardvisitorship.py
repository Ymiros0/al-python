local var_0_0 = class("CourtYardVisitorShip", import(".CourtYardShip"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.name = arg_1_2.name
	arg_1_0.inimacy = 0
	arg_1_0.coin = 0

def var_0_0.GetName(arg_2_0):
	return arg_2_0.name

def var_0_0.GetShipType(arg_3_0):
	return CourtYardConst.SHIP_TYPE_OTHER

return var_0_0
