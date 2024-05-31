local var_0_0 = class("BackYardThemeTemplate", import(".BackYardBaseThemeTemplate"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.isFetched = arg_1_1.is_fetch

def var_0_0.GetType(arg_2_0):
	return BackYardConst.THEME_TEMPLATE_USAGE_TYPE_OTHER

def var_0_0.ShouldFetch(arg_3_0):
	return not arg_3_0.isFetched

def var_0_0.GetAllFurniture(arg_4_0):
	if not arg_4_0.furniTruesByIds:
		local var_4_0 = arg_4_0.GetRawPutList()

		arg_4_0.furniTruesByIds = arg_4_0.InitFurnitures({
			skipCheck = True,
			floor = 1,
			mapSize = arg_4_0.GetMapSize(),
			furniture_put_list = var_4_0
		})

	return arg_4_0.furniTruesByIds

def var_0_0.GetMapSize(arg_5_0):
	return (Dorm.StaticGetMapSize(4))

def var_0_0.GetFurnitureCnt(arg_6_0):
	if not arg_6_0.furnitureCnts:
		arg_6_0.furnitureCnts = {}

		for iter_6_0, iter_6_1 in ipairs(arg_6_0.GetWarpFurnitures()):
			if not arg_6_0.furnitureCnts[iter_6_1.configId]:
				arg_6_0.furnitureCnts[iter_6_1.configId] = 0

			arg_6_0.furnitureCnts[iter_6_1.configId] = arg_6_0.furnitureCnts[iter_6_1.configId] + 1

	return arg_6_0.furnitureCnts

return var_0_0
