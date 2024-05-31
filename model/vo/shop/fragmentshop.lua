﻿local var_0_0 = class("FragmentShop", import(".MonthlyShop"))

var_0_0.GoodsType = Goods.TYPE_FRAGMENT
var_0_0.type = ShopArgs.ShopFragment

function var_0_0.update(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	arg_1_0.id = arg_1_1
	arg_1_0.configId = arg_1_1

	local var_1_0 = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_2) do
		var_1_0[iter_1_1.shop_id] = iter_1_1.pay_count
	end

	for iter_1_2, iter_1_3 in ipairs(arg_1_3) do
		var_1_0[iter_1_3.shop_id] = iter_1_3.pay_count
	end

	table.clear(arg_1_0.goods)

	if arg_1_0.id and arg_1_0.id > 0 and arg_1_0:getConfigTable() then
		local function var_1_1(arg_2_0, arg_2_1)
			local var_2_0 = var_1_0[arg_2_0] or 0

			arg_1_0.goods[arg_2_0] = Goods.Create({
				shop_id = arg_2_0,
				buy_count = var_2_0
			}, arg_2_1)
		end

		for iter_1_4, iter_1_5 in ipairs(arg_1_0:getConfig("blueprint_shop_goods")) do
			var_1_1(iter_1_5, Goods.TYPE_FRAGMENT)
		end

		for iter_1_6, iter_1_7 in ipairs(arg_1_0:getConfig("blueprint_shop_limit_goods")) do
			var_1_1(iter_1_7, Goods.TYPE_FRAGMENT_NORMAL)
		end
	end
end

function var_0_0.Reset(arg_3_0, arg_3_1)
	local var_3_0 = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0:getConfig("blueprint_shop_limit_goods")) do
		local var_3_1 = arg_3_0.goods[iter_3_1]

		if var_3_1 then
			table.insert(var_3_0, {
				shop_id = iter_3_1,
				pay_count = var_3_1.buyCount
			})
		end
	end

	arg_3_0:update(arg_3_1, {}, var_3_0)
end

return var_0_0
