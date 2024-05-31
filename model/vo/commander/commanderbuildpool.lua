local var_0_0 = class("CommanderBuildPool", import("..BaseVO"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
end

function var_0_0.bindConfigTable(arg_2_0)
	return pg.commander_data_create_material
end

function var_0_0.getName(arg_3_0)
	local var_3_0 = arg_3_0:getConfig("use_item")
	local var_3_1 = Item.New({
		id = var_3_0
	})

	return arg_3_0:getConfig("name") or var_3_1:getConfig("name") or ""
end

function var_0_0.getConsume(arg_4_0)
	local var_4_0 = arg_4_0:getConfig("use_item")
	local var_4_1 = arg_4_0:getConfig("number_1")

	return {
		{
			2,
			var_4_0,
			var_4_1
		}
	}
end

function var_0_0.getConsumeDesc(arg_5_0)
	local var_5_0 = arg_5_0:getConfig("use_gold")
	local var_5_1 = arg_5_0:getConfig("use_item")
	local var_5_2 = arg_5_0:getConfig("number_1")
	local var_5_3 = Item.New({
		id = var_5_1
	})

	return i18n("commander_build_pool_tip", var_5_3:getConfig("name"), var_5_2)
end

function var_0_0.getPrint(arg_6_0)
	return Commander.rarity2Print(arg_6_0.id + 2)
end

function var_0_0.getItemCount(arg_7_0)
	local var_7_0 = arg_7_0:getConfig("use_item")

	return getProxy(BagProxy):getItemCountById(var_7_0)
end

function var_0_0.getRarity(arg_8_0)
	return arg_8_0.id
end

return var_0_0
