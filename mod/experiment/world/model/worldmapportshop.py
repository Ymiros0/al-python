local var_0_0 = class("WorldMapPortShop", import("...BaseEntity"))

var_0_0.Fields = {
	items = "table",
	expiredTime = "number"
}

def var_0_0.Setup(arg_1_0):
	return

def var_0_0.IsValid(arg_2_0):
	return arg_2_0.expiredTime >= pg.TimeMgr.GetInstance().GetServerTime()

return var_0_0
