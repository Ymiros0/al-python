local var_0_0 = class("BackYardThemeTemplate", import(".BackYardBaseThemeTemplate"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.isFetched = arg_1_1.is_fetch
end

function var_0_0.GetType(arg_2_0)
	return BackYardConst.THEME_TEMPLATE_USAGE_TYPE_OTHER
end

function var_0_0.ShouldFetch(arg_3_0)
	return not arg_3_0.isFetched
end

function var_0_0.GetAllFurniture(arg_4_0)
	if not arg_4_0.furnitruesByIds then
		local var_4_0 = arg_4_0:GetRawPutList()

		arg_4_0.furnitruesByIds = arg_4_0:InitFurnitures({
			skipCheck = true,
			floor = 1,
			mapSize = arg_4_0:GetMapSize(),
			furniture_put_list = var_4_0
		})
	end

	return arg_4_0.furnitruesByIds
end

function var_0_0.GetMapSize(arg_5_0)
	return (Dorm.StaticGetMapSize(4))
end

function var_0_0.GetFurnitureCnt(arg_6_0)
	if not arg_6_0.furnitureCnts then
		arg_6_0.furnitureCnts = {}

		for iter_6_0, iter_6_1 in ipairs(arg_6_0:GetWarpFurnitures()) do
			if not arg_6_0.furnitureCnts[iter_6_1.configId] then
				arg_6_0.furnitureCnts[iter_6_1.configId] = 0
			end

			arg_6_0.furnitureCnts[iter_6_1.configId] = arg_6_0.furnitureCnts[iter_6_1.configId] + 1
		end
	end

	return arg_6_0.furnitureCnts
end

return var_0_0
