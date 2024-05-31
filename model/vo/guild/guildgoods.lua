﻿local var_0_0 = class("GuildGoods", import("..BaseVO"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.configId = arg_1_1.id
	arg_1_0.count = arg_1_1.count
	arg_1_0.index = arg_1_1.index
	arg_1_0.id = arg_1_0.configId .. "_" .. arg_1_0.index
end

function var_0_0.UpdateCnt(arg_2_0, arg_2_1)
	arg_2_0.count = arg_2_0.count - arg_2_1
end

function var_0_0.bindConfigTable(arg_3_0)
	return pg.guild_store
end

function var_0_0.CanPurchase(arg_4_0)
	return arg_4_0.count > 0
end

function var_0_0.GetPrice(arg_5_0)
	return arg_5_0:getConfig("price")
end

function var_0_0.Selectable(arg_6_0)
	return arg_6_0:getConfig("goods_type") == 2
end

function var_0_0.GetFirstDropId(arg_7_0)
	return arg_7_0:getConfig("goods")
end

function var_0_0.GetMaxCnt(arg_8_0)
	return arg_8_0.count
end

function var_0_0.CanPurchaseCnt(arg_9_0, arg_9_1)
	return arg_9_1 <= arg_9_0.count
end

function var_0_0.GetLimit(arg_10_0)
	return arg_10_0:getConfig("goods_purchase_limit")
end

return var_0_0
