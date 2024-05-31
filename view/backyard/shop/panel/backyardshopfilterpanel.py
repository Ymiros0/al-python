local var_0_0 = class("BackYardShopFilterPanel", import("...Decoration.panles.BackYardDecorationFilterPanel"))

def var_0_0.SortForDecorate(arg_1_0, arg_1_1, arg_1_2):
	local var_1_0 = arg_1_2[1]
	local var_1_1 = arg_1_2[2]
	local var_1_2 = arg_1_2[3]

	local function var_1_3(arg_2_0)
		if arg_2_0.getConfig("new") == -1:
			return 0
		elif arg_2_0.canPurchaseByGem() and not arg_2_0.canPurchaseByDormMoeny():
			return 1
		elif arg_2_0.canPurchaseByGem() and arg_2_0.canPurchaseByDormMoeny():
			return 3
		elif arg_2_0.canPurchaseByDormMoeny():
			return 4
		else
			return 5

	local function var_1_4(arg_3_0)
		local var_3_0 = pg.furniture_shop_template[arg_3_0.configId].time

		if arg_3_0.getConfig("new") > 0:
			return 4
		elif var_3_0 != "always":
			return 3
		elif var_3_0 == "always":
			return 2
		else
			return 1

	function var_0_0.SortByDefault1(arg_4_0, arg_4_1)
		local var_4_0 = var_1_3(arg_4_0)
		local var_4_1 = var_1_3(arg_4_1)

		if var_4_0 == var_4_1:
			local var_4_2 = var_1_4(arg_4_0)
			local var_4_3 = var_1_4(arg_4_1)

			if var_4_2 == var_4_3:
				return arg_4_0.id < arg_4_1.id
			else
				return var_4_2 < var_4_3
		else
			return var_4_0 < var_4_1

	function var_0_0.SortByDefault2(arg_5_0, arg_5_1)
		local var_5_0 = var_1_3(arg_5_0)
		local var_5_1 = var_1_3(arg_5_1)

		if var_5_0 == var_5_1:
			local var_5_2 = var_1_4(arg_5_0)
			local var_5_3 = var_1_4(arg_5_1)

			if var_5_2 == var_5_3:
				return arg_5_0.id > arg_5_1.id
			else
				return var_5_3 < var_5_2
		else
			return var_5_0 < var_5_1

	local var_1_5 = arg_1_0.canPurchase() and 1 or 0
	local var_1_6 = arg_1_1.canPurchase() and 1 or 0

	if var_1_5 == var_1_6:
		if var_1_0 == var_0_0.SORT_MODE.BY_DEFAULT:
			return var_0_0["SortByDefault" .. var_1_2](arg_1_0, arg_1_1)
		elif var_1_0 == var_0_0.SORT_MODE.BY_FUNC:
			return var_0_0.SORT_BY_FUNC(arg_1_0, arg_1_1, var_1_1, var_1_2, function()
				return var_0_0["SortByDefault" .. var_1_2](arg_1_0, arg_1_1))
		elif var_1_0 == var_0_0.SORT_MODE.BY_CONFIG:
			return var_0_0.SORT_BY_CONFIG(arg_1_0, arg_1_1, var_1_1, var_1_2, function()
				return var_0_0["SortByDefault" .. var_1_2](arg_1_0, arg_1_1))
	else
		return var_1_6 < var_1_5

def var_0_0.sort(arg_8_0, arg_8_1):
	table.sort(arg_8_1, function(arg_9_0, arg_9_1)
		return var_0_0.SortForDecorate(arg_9_0, arg_9_1, {
			arg_8_0.sortData[1],
			arg_8_0.sortData[2],
			arg_8_0.orderMode
		}))

	arg_8_0.furnitures = arg_8_1

return var_0_0
