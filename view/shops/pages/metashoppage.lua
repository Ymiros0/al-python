local var_0_0 = class("MetaShopPage", import(".ActivityShopPage"))

function var_0_0.getUIName(arg_1_0)
	return "MetaShop"
end

function var_0_0.ResId2ItemId(arg_2_0, arg_2_1)
	return arg_2_1
end

function var_0_0.SetResIcon(arg_3_0)
	var_0_0.super.SetResIcon(arg_3_0, DROP_TYPE_ITEM)
end

function var_0_0.UpdateTip(arg_4_0)
	arg_4_0.time.text = i18n("meta_shop_tip")
end

function var_0_0.OnUpdatePlayer(arg_5_0)
	return
end

function var_0_0.OnUpdateItems(arg_6_0)
	local var_6_0 = arg_6_0.shop:GetResList()

	for iter_6_0, iter_6_1 in pairs(arg_6_0.resTrList) do
		local var_6_1 = iter_6_1[1]
		local var_6_2 = iter_6_1[2]
		local var_6_3 = iter_6_1[3]
		local var_6_4 = var_6_0[iter_6_0]

		setActive(var_6_1, var_6_4 ~= nil)

		if var_6_4 ~= nil then
			var_6_3.text = (arg_6_0.items[var_6_4] or Item.New({
				count = 0,
				id = var_6_4
			})).count
		end
	end
end

function var_0_0.OnPurchase(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0 = arg_7_0.shop.activityId

	arg_7_0:emit(NewShopsMediator.ON_META_SHOP, var_7_0, 1, arg_7_1.id, arg_7_2)
end

function var_0_0.GetPaintingName(arg_8_0)
	local var_8_0, var_8_1, var_8_2 = var_0_0.super.GetPaintingName(arg_8_0)
	local var_8_3

	if type(var_8_0) == "table" then
		var_8_3 = var_8_0[math.random(1, #var_8_0)]
	else
		var_8_3 = var_8_0
	end

	return var_8_3, var_8_1, var_8_2
end

return var_0_0
