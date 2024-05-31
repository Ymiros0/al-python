local var_0_0 = class("Goods", import(".BaseVO"))

var_0_0.TYPE_SHOPSTREET = 1
var_0_0.TYPE_MILITARY = 2
var_0_0.TYPE_CHARGE = 3
var_0_0.TYPE_GIFT_PACKAGE = 4
var_0_0.TYPE_SKIN = 6
var_0_0.TYPE_ACTIVITY = 7
var_0_0.TYPE_ACTIVITY_EXTRA = 8
var_0_0.TYPE_GUILD = 9
var_0_0.TYPE_SHAM_BATTLE = 10
var_0_0.TYPE_ESCORT = 11
var_0_0.TYPE_FRAGMENT = 12
var_0_0.TYPE_WORLD = 13
var_0_0.TYPE_FRAGMENT_NORMAL = 14
var_0_0.TYPE_NEW_SERVER = 15
var_0_0.TYPE_MINI_GAME = 16
var_0_0.TYPE_QUOTA = 17
var_0_0.TYPE_WORLD_NSHOP = 18
var_0_0.GEM = 0
var_0_0.GIFT_BOX = 1
var_0_0.MONTH_CARD = 2
var_0_0.ITEM_BOX = 3
var_0_0.PASS_ITEM = 4
var_0_0.EQUIP_BAG_SIZE_ITEM = 59100
var_0_0.SHIP_BAG_SIZE_ITEM = 59101
var_0_0.COMMANDER_BAG_SIZE_ITEM = 59114
var_0_0.SPWEAPON_BAG_SIZE_ITEM = 59360
var_0_0.Tec_Ship_Gift_Type = 3
var_0_0.Tec_Ship_Gift_Arg = {
	High = 1,
	Up = 3,
	Show = 0,
	Normal = 2
}
var_0_0.CUR_PACKET_ID = 138

def var_0_0.Ctor(arg_1_0):
	assert(False, "does not call this function, use Create instead")

local var_0_1 = {
	[var_0_0.TYPE_CHARGE] = function(arg_2_0, arg_2_1)
		return ChargeCommodity.New(arg_2_0, arg_2_1),
	[var_0_0.TYPE_ACTIVITY] = function(arg_3_0, arg_3_1)
		return ActivityCommodity.New(arg_3_0, arg_3_1),
	[var_0_0.TYPE_SHAM_BATTLE] = function(arg_4_0, arg_4_1)
		return ActivityCommodity.New(arg_4_0, arg_4_1),
	[var_0_0.TYPE_FRAGMENT] = function(arg_5_0, arg_5_1)
		return ActivityCommodity.New(arg_5_0, arg_5_1),
	[var_0_0.TYPE_FRAGMENT_NORMAL] = function(arg_6_0, arg_6_1)
		return ActivityCommodity.New(arg_6_0, arg_6_1),
	[var_0_0.TYPE_ESCORT] = function(arg_7_0, arg_7_1)
		return ActivityCommodity.New(arg_7_0, arg_7_1),
	[var_0_0.TYPE_ACTIVITY_EXTRA] = function(arg_8_0, arg_8_1)
		return ActivityExtraCommodity.New(arg_8_0, arg_8_1),
	[var_0_0.TYPE_MINI_GAME] = function(arg_9_0, arg_9_1)
		return MiniGameGoods.New(arg_9_0, arg_9_1),
	[var_0_0.TYPE_QUOTA] = function(arg_10_0, arg_10_1)
		return QuotaCommodity.New(arg_10_0, arg_10_1),
	[var_0_0.TYPE_ESCORT] = function(arg_11_0, arg_11_1)
		return ActivityCommodity.New(arg_11_0, arg_11_1),
	[var_0_0.TYPE_WORLD_NSHOP] = function(arg_12_0, arg_12_1)
		return WorldNShopCommodity.New(arg_12_0, arg_12_1)
}

def var_0_0.Create(arg_13_0, arg_13_1):
	return switch(arg_13_1, var_0_1, function(arg_14_0, arg_14_1)
		return CommonCommodity.New(arg_14_0, arg_14_1), arg_13_0, arg_13_1)

def var_0_0.ExistFurniture(arg_15_0):
	return pg.shop_furniture_relation[arg_15_0] != None

def var_0_0.Id2FurnitureId(arg_16_0):
	return pg.shop_furniture_relation[arg_16_0].fur_id

def var_0_0.FurnitureId2Id(arg_17_0):
	local var_17_0 = pg.shop_furniture_relation.get_id_list_by_fur_id[arg_17_0]

	return var_17_0 and var_17_0[1]

def var_0_0.GetFurnitureConfig(arg_18_0):
	return pg.shop_furniture_relation[arg_18_0]

def var_0_0.Id2ShipSkinId(arg_19_0):
	return pg.shop_template[arg_19_0].effect_args[1]

return var_0_0
