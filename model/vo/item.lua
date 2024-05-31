local var_0_0 = class("Item", import(".BaseVO"))

var_0_0.REVERT_EQUIPMENT_ID = 15007
var_0_0.COMMANDER_QUICKLY_TOOL_ID = 20010
var_0_0.QUICK_TASK_PASS_TICKET_ID = 15013
var_0_0.DOA_SELECT_CHAR_ID = 70144
var_0_0.INVISIBLE_TYPE = {
	[0] = true,
	[9] = true
}
var_0_0.PUZZLA_TYPE = 0
var_0_0.EQUIPMENT_BOX_TYPE_5 = 5
var_0_0.LESSON_TYPE = 10
var_0_0.EQUIPMENT_SKIN_BOX = 11
var_0_0.BLUEPRINT_TYPE = 12
var_0_0.ASSIGNED_TYPE = 13
var_0_0.GOLD_BOX_TYPE = 14
var_0_0.OIL_BOX_TYPE = 15
var_0_0.EQUIPMENT_ASSIGNED_TYPE = 16
var_0_0.GIFT_BOX = 17
var_0_0.TEC_SPEEDUP_TYPE = 18
var_0_0.SPECIAL_OPERATION_TICKET = 19
var_0_0.GUILD_OPENABLE = 20
var_0_0.INVITATION_TYPE = 21
var_0_0.EXP_BOOK_TYPE = 22
var_0_0.LOVE_LETTER_TYPE = 23
var_0_0.SPWEAPON_MATERIAL_TYPE = 24
var_0_0.METALESSON_TYPE = 25
var_0_0.SKIN_ASSIGNED_TYPE = 26

function var_0_0.Ctor(arg_1_0, arg_1_1)
	assert(not arg_1_1.type or arg_1_1.type == DROP_TYPE_VITEM or arg_1_1.type == DROP_TYPE_ITEM)

	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.count = arg_1_1.count
	arg_1_0.name = arg_1_1.name
	arg_1_0.extra = arg_1_1.extra

	arg_1_0:InitConfig()
end

function var_0_0.CanOpen(arg_2_0)
	local var_2_0 = arg_2_0:getConfig("type")

	return var_2_0 == var_0_0.EQUIPMENT_BOX_TYPE_5 or var_2_0 == var_0_0.EQUIPMENT_SKIN_BOX or var_2_0 == var_0_0.GOLD_BOX_TYPE or var_2_0 == var_0_0.OIL_BOX_TYPE or var_2_0 == var_0_0.GIFT_BOX or var_2_0 == var_0_0.GUILD_OPENABLE
end

function var_0_0.IsShipExpType(arg_3_0)
	return arg_3_0:getConfig("type") == var_0_0.EXP_BOOK_TYPE
end

function var_0_0.getConfigData(arg_4_0)
	local var_4_0 = {
		pg.item_virtual_data_statistics,
		pg.item_data_statistics
	}
	local var_4_1

	if underscore.any(var_4_0, function(arg_5_0)
		return arg_5_0[arg_4_0] ~= nil
	end) then
		var_4_1 = setmetatable({}, {
			__index = function(arg_6_0, arg_6_1)
				for iter_6_0, iter_6_1 in ipairs(var_4_0) do
					if iter_6_1[arg_4_0] and iter_6_1[arg_4_0][arg_6_1] ~= nil then
						arg_6_0[arg_6_1] = iter_6_1[arg_4_0][arg_6_1]

						return arg_6_0[arg_6_1]
					end
				end
			end
		})
	end

	return var_4_1
end

function var_0_0.InitConfig(arg_7_0)
	arg_7_0.cfg = var_0_0.getConfigData(arg_7_0.configId)

	assert(arg_7_0.cfg, string.format("without item config from id_%d", arg_7_0.id))
end

function var_0_0.getConfigTable(arg_8_0)
	return arg_8_0.cfg
end

function var_0_0.CanInBag(arg_9_0)
	return tobool(pg.item_data_statistics[arg_9_0])
end

function var_0_0.couldSell(arg_10_0)
	return table.getCount(arg_10_0:getConfig("price")) > 0
end

function var_0_0.isEnough(arg_11_0, arg_11_1)
	return arg_11_1 <= arg_11_0.count
end

function var_0_0.consume(arg_12_0, arg_12_1)
	arg_12_0.count = arg_12_0.count - arg_12_1
end

function var_0_0.isDesignDrawing(arg_13_0)
	return arg_13_0:getConfig("type") == 9
end

function var_0_0.isVirtualItem(arg_14_0)
	return arg_14_0:getConfig("type") == 0
end

function var_0_0.isEquipmentSkinBox(arg_15_0)
	return arg_15_0:getConfig("type") == var_0_0.EQUIPMENT_SKIN_BOX
end

function var_0_0.isBluePrintType(arg_16_0)
	return arg_16_0:getConfig("type") == var_0_0.BLUEPRINT_TYPE
end

function var_0_0.isTecSpeedUpType(arg_17_0)
	return arg_17_0:getConfig("type") == var_0_0.TEC_SPEEDUP_TYPE
end

function var_0_0.IsMaxCnt(arg_18_0)
	return arg_18_0:getConfig("max_num") <= arg_18_0.count
end

function var_0_0.IsDoaSelectCharItem(arg_19_0)
	return arg_19_0.id == var_0_0.DOA_SELECT_CHAR_ID
end

function var_0_0.getConfig(arg_20_0, arg_20_1)
	if arg_20_1 == "display" then
		local var_20_0 = var_0_0.super.getConfig(arg_20_0, "combination_display")

		if var_20_0 and #var_20_0 > 0 then
			return arg_20_0:CombinationDisplay(var_20_0)
		end
	end

	return var_0_0.super.getConfig(arg_20_0, arg_20_1)
end

function var_0_0.StaticCombinationDisplay(arg_21_0)
	local var_21_0 = _.map(arg_21_0, function(arg_22_0)
		local var_22_0 = string.format("%0.1f", arg_22_0[2] / 100)
		local var_22_1 = ShipSkin.New({
			id = arg_22_0[1]
		})
		local var_22_2 = ""

		if var_22_1:IsLive2d() then
			var_22_2 = "（<color=#92fc63>" .. i18n("luckybag_skin_islive2d") .. "</color>）"
		elseif var_22_1:IsSpine() then
			var_22_2 = "（<color=#92fc63>" .. i18n("luckybag_skin_isani") .. "</color>）"
		end

		local var_22_3 = i18n("random_skin_list_item_desc_label")
		local var_22_4 = ""

		if var_22_1:ExistReward() then
			var_22_4 = i18n("word_show_extra_reward_at_fudai_dialog", var_22_1:GetRewardListDesc())
		end

		return "\n（<color=#92fc63>" .. var_22_0 .. "%%</color>）" .. var_22_1.shipName .. var_22_3 .. var_22_1.skinName .. var_22_2 .. var_22_4
	end)
	local var_21_1 = table.concat(var_21_0, ";")

	return i18n("skin_gift_desc", var_21_1)
end

function var_0_0.CombinationDisplay(arg_23_0, arg_23_1)
	return var_0_0.StaticCombinationDisplay(arg_23_1)
end

function var_0_0.InTimeLimitSkinAssigned(arg_24_0)
	local var_24_0 = var_0_0.getConfigData(arg_24_0)

	if var_24_0.type ~= var_0_0.SKIN_ASSIGNED_TYPE then
		return false
	end

	local var_24_1 = var_24_0.usage_arg[1]

	return getProxy(ActivityProxy):IsActivityNotEnd(var_24_1)
end

function var_0_0.GetValidSkinList(arg_25_0)
	assert(arg_25_0:getConfig("type") == var_0_0.SKIN_ASSIGNED_TYPE)

	local var_25_0 = arg_25_0:getConfig("usage_arg")

	if Item.InTimeLimitSkinAssigned(arg_25_0.id) then
		return table.mergeArray(var_25_0[2], var_25_0[3], true)
	else
		return underscore.rest(var_25_0[3], 1)
	end
end

function var_0_0.IsAllSkinOwner(arg_26_0)
	assert(arg_26_0:getConfig("type") == var_0_0.SKIN_ASSIGNED_TYPE)

	local var_26_0 = getProxy(ShipSkinProxy)

	return underscore.all(arg_26_0:GetValidSkinList(), function(arg_27_0)
		return var_26_0:hasNonLimitSkin(arg_27_0)
	end)
end

function var_0_0.GetOverflowCheckItems(arg_28_0, arg_28_1)
	arg_28_1 = arg_28_1 or 1

	local var_28_0 = {}

	if arg_28_0:getConfig("usage") == ItemUsage.DROP_TEMPLATE then
		local var_28_1, var_28_2, var_28_3 = unpack(arg_28_0:getConfig("usage_arg"))

		if var_28_2 > 0 then
			table.insert(var_28_0, {
				type = DROP_TYPE_RESOURCE,
				id = PlayerConst.ResGold,
				count = var_28_2 * arg_28_1
			})
		end

		if var_28_3 > 0 then
			table.insert(var_28_0, {
				type = DROP_TYPE_RESOURCE,
				id = PlayerConst.ResOil,
				count = var_28_3 * arg_28_1
			})
		end
	end

	switch(arg_28_0:getConfig("type"), {
		[Item.EQUIPMENT_BOX_TYPE_5] = function()
			table.insert(var_28_0, {
				type = DROP_TYPE_EQUIP,
				id = EQUIP_OCCUPATION_ID,
				count = arg_28_1
			})
		end,
		[Item.EQUIPMENT_ASSIGNED_TYPE] = function()
			table.insert(var_28_0, {
				type = DROP_TYPE_EQUIP,
				id = EQUIP_OCCUPATION_ID,
				count = arg_28_1
			})
		end
	})
	underscore.map(var_28_0, function(arg_31_0)
		return Drop.New(arg_31_0)
	end)

	return var_28_0
end

function var_0_0.IsSkinShopDiscountType(arg_32_0)
	return arg_32_0:getConfig("usage") == ItemUsage.SKIN_SHOP_DISCOUNT
end

function var_0_0.CanUseForShop(arg_33_0, arg_33_1)
	if arg_33_0:IsSkinShopDiscountType() then
		local var_33_0 = arg_33_0:getConfig("usage_arg")

		if not var_33_0 or type(var_33_0) ~= "table" then
			return false
		end

		local var_33_1 = var_33_0[1] or {}

		return #var_33_1 == 1 and var_33_1[1] == 0 or table.contains(var_33_1, arg_33_1)
	end

	return false
end

function var_0_0.GetConsumeForSkinShopDiscount(arg_34_0, arg_34_1)
	if arg_34_0:IsSkinShopDiscountType() then
		local var_34_0 = pg.item_data_statistics[arg_34_0.configId].usage_arg[2] or 0
		local var_34_1 = Goods.Create({
			shop_id = arg_34_1
		}, Goods.TYPE_SKIN)

		return math.max(0, var_34_1:GetPrice() - var_34_0), var_34_1:getConfig("resource_type")
	else
		return 0
	end
end

function var_0_0.getName(arg_35_0)
	return arg_35_0.name or arg_35_0:getConfig("name")
end

function var_0_0.getIcon(arg_36_0)
	return arg_36_0:getConfig("Icon")
end

return var_0_0
