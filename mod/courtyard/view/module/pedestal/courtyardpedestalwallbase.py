local var_0_0 = class("CourtYardPedestalWallBase", import(".CourtYardPedestalStructure"))

def var_0_0.GetAssetPath(arg_1_0):
	return "furniTrues/base/wall_" .. arg_1_0.level

def var_0_0.OnLoaded(arg_2_0, arg_2_1):
	arg_2_1.transform.SetAsFirstSibling()

return var_0_0
