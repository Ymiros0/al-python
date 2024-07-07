from Framework.i18n import i18n
from const import DROP_TYPE_ITEM, DROP_TYPE_VITEM
from Framework import underscore
from lib import pg
from model.const import ItemUsage
from model.proxy.ActivityProxy import ActivityProxy
from model.proxy.ShipSkinProxy import ShipSkinProxy
from model.vo.BaseVO import BaseVO
from model.vo.PlayerConst import PlayerConst
from model.vo.ShipSkin import ShipSkin
from packages.luatable import ipairs, setmetatable, table
from support.helpers.M02 import getProxy, switch
from drop import Drop
from Goods import Goods

class Item(BaseVO):

	REVERT_EQUIPMENT_ID = 15007
	COMMANDER_QUICKLY_TOOL_ID = 20010
	QUICK_TASK_PASS_TICKET_ID = 15013
	DOA_SELECT_CHAR_ID = 70144
	INVISIBLE_TYPE = table({
		0: True,
		9: True
	})
	PUZZLA_TYPE = 0
	EQUIPMENT_BOX_TYPE_5 = 5
	LESSON_TYPE = 10
	EQUIPMENT_SKIN_BOX = 11
	BLUEPRINT_TYPE = 12
	ASSIGNED_TYPE = 13
	GOLD_BOX_TYPE = 14
	OIL_BOX_TYPE = 15
	EQUIPMENT_ASSIGNED_TYPE = 16
	GIFT_BOX = 17
	TEC_SPEEDUP_TYPE = 18
	SPECIAL_OPERATION_TICKET = 19
	GUILD_OPENABLE = 20
	INVITATION_TYPE = 21
	EXP_BOOK_TYPE = 22
	LOVE_LETTER_TYPE = 23
	SPWEAPON_MATERIAL_TYPE = 24
	METALESSON_TYPE = 25
	SKIN_ASSIGNED_TYPE = 26

	def __init__(arg_1_0, arg_1_1):
		assert not arg_1_1.type or arg_1_1.type == DROP_TYPE_VITEM or arg_1_1.type == DROP_TYPE_ITEM

		arg_1_0.id = arg_1_1.id
		arg_1_0.configId = arg_1_0.id
		arg_1_0.count = arg_1_1.count
		arg_1_0.name = arg_1_1.name
		arg_1_0.extra = arg_1_1.extra

		arg_1_0.InitConfig()

	def CanOpen(arg_2_0):
		var_2_0 = arg_2_0.getConfig("type")

		return var_2_0 == Item.EQUIPMENT_BOX_TYPE_5 or var_2_0 == Item.EQUIPMENT_SKIN_BOX or var_2_0 == Item.GOLD_BOX_TYPE or var_2_0 == Item.OIL_BOX_TYPE or var_2_0 == Item.GIFT_BOX or var_2_0 == Item.GUILD_OPENABLE

	def IsShipExpType(arg_3_0):
		return arg_3_0.getConfig("type") == Item.EXP_BOOK_TYPE

	def getConfigData(arg_4_0):
		var_4_0 = table(
			pg.item_virtual_data_statistics,
			pg.item_data_statistics
		)
		var_4_1

		if underscore.any(var_4_0, lambda arg_5_0: arg_5_0[arg_4_0] != None):
			def _index (arg_6_0, arg_6_1):
					for iter_6_0, iter_6_1 in ipairs(var_4_0):
						if iter_6_1[arg_4_0] and iter_6_1[arg_4_0][arg_6_1] != None:
							arg_6_0[arg_6_1] = iter_6_1[arg_4_0][arg_6_1]

							return arg_6_0[arg_6_1]
			var_4_1 = setmetatable(table(), table(
				__index = _index
			))

		return var_4_1

	def InitConfig(arg_7_0):
		arg_7_0.cfg = Item.getConfigData(arg_7_0.configId)

		assert(arg_7_0.cfg, "without item config from id_%d" % arg_7_0.id)

	def getConfigTable(arg_8_0):
		return arg_8_0.cfg

	def CanInBag(arg_9_0):
		return bool(pg.item_data_statistics[arg_9_0])

	def couldSell(arg_10_0):
		return table.getCount(arg_10_0.getConfig("price")) > 0

	def isEnough(arg_11_0, arg_11_1):
		return arg_11_1 <= arg_11_0.count

	def consume(arg_12_0, arg_12_1):
		arg_12_0.count = arg_12_0.count - arg_12_1

	def isDesignDrawing(arg_13_0):
		return arg_13_0.getConfig("type") == 9

	def isVirtualItem(arg_14_0):
		return arg_14_0.getConfig("type") == 0

	def isEquipmentSkinBox(arg_15_0):
		return arg_15_0.getConfig("type") == Item.EQUIPMENT_SKIN_BOX

	def isBluePrintType(arg_16_0):
		return arg_16_0.getConfig("type") == Item.BLUEPRINT_TYPE

	def isTecSpeedUpType(arg_17_0):
		return arg_17_0.getConfig("type") == Item.TEC_SPEEDUP_TYPE

	def IsMaxCnt(arg_18_0):
		return arg_18_0.getConfig("max_num") <= arg_18_0.count

	def IsDoaSelectCharItem(arg_19_0):
		return arg_19_0.id == Item.DOA_SELECT_CHAR_ID

	def getConfig(arg_20_0, arg_20_1):
		if arg_20_1 == "display":
			var_20_0 = super().getConfig(arg_20_0, "combination_display")

			if var_20_0 and len(var_20_0) > 0:
				return arg_20_0.CombinationDisplay(var_20_0)

		return super().getConfig(arg_20_0, arg_20_1)

	def StaticCombinationDisplay(arg_21_0):
		def _function(arg_22_0):
			var_22_0 = "%0.1f" % arg_22_0[2] / 100
			var_22_1 = ShipSkin.New(table(
				id = arg_22_0[1]
			))
			var_22_2 = ""

			if var_22_1.IsLive2d():
				var_22_2 = "（<color=#92fc63>" + i18n("luckybag_skin_islive2d") + "</color>）"
			elif var_22_1.IsSpine():
				var_22_2 = "（<color=#92fc63>" + i18n("luckybag_skin_isani") + "</color>）"

			var_22_3 = i18n("random_skin_list_item_desc_label")
			var_22_4 = ""

			if var_22_1.ExistReward():
				var_22_4 = i18n("word_show_extra_reward_at_fudai_dialog", var_22_1.GetRewardListDesc())

			return f"\n（<color=#92fc63>{var_22_0}%%</color>）{var_22_1.shipName}{var_22_3}{var_22_1.skinName}{var_22_2}{var_22_4}"
		var_21_0 = underscore.map(arg_21_0, _function)
		var_21_1 = table.concat(var_21_0, ";")

		return i18n("skin_gift_desc", var_21_1)

	def CombinationDisplay(arg_23_0, arg_23_1):
		return Item.StaticCombinationDisplay(arg_23_1)

	def InTimeLimitSkinAssigned(arg_24_0):
		var_24_0 = Item.getConfigData(arg_24_0)

		if var_24_0.type != Item.SKIN_ASSIGNED_TYPE:
			return False

		var_24_1 = var_24_0.usage_arg[1]

		return getProxy(ActivityProxy).IsActivityNotEnd(var_24_1)

	def GetValidSkinList(arg_25_0):
		assert(arg_25_0.getConfig("type") == Item.SKIN_ASSIGNED_TYPE)

		var_25_0 = arg_25_0.getConfig("usage_arg")

		if Item.InTimeLimitSkinAssigned(arg_25_0.id):
			return table.mergeArray(var_25_0[2], var_25_0[3], True)
		else:
			return underscore.rest(var_25_0[3], 1)

	def IsAllSkinOwner(arg_26_0):
		assert(arg_26_0.getConfig("type") == Item.SKIN_ASSIGNED_TYPE)

		var_26_0 = getProxy(ShipSkinProxy)

		return underscore.all(arg_26_0.GetValidSkinList(), lambda arg_27_0: var_26_0.hasNonLimitSkin(arg_27_0))

	def GetOverflowCheckItems(arg_28_0, arg_28_1):
		arg_28_1 = arg_28_1 or 1

		var_28_0 = table()

		if arg_28_0.getConfig("usage") == ItemUsage.DROP_TEMPLATE:
			var_28_1, var_28_2, var_28_3 = arg_28_0.getConfig("usage_arg").values()

			if var_28_2 > 0:
				table.insert(var_28_0, table(
					type = Item.DROP_TYPE_RESOURCE,
					id = PlayerConst.ResGold,
					count = var_28_2 * arg_28_1
				))

			if var_28_3 > 0:
				table.insert(var_28_0, table(
					type = Item.DROP_TYPE_RESOURCE,
					id = PlayerConst.ResOil,
					count = var_28_3 * arg_28_1
				))

		switch(arg_28_0.getConfig("type"), table({
			Item.EQUIPMENT_BOX_TYPE_5: lambda: table.insert(var_28_0, table(
					type = Item.DROP_TYPE_EQUIP,
					id = Item.EQUIP_OCCUPATION_ID,
					count = arg_28_1
				)),
			Item.EQUIPMENT_ASSIGNED_TYPE: lambda: table.insert(var_28_0, table(
					type = Item.DROP_TYPE_EQUIP,
					id = Item.EQUIP_OCCUPATION_ID,
					count = arg_28_1
				))
		}))
		underscore.map(var_28_0, lambda arg_31_0: Drop.New(arg_31_0))

		return var_28_0

	def IsSkinShopDiscountType(arg_32_0):
		return arg_32_0.getConfig("usage") == ItemUsage.SKIN_SHOP_DISCOUNT

	def CanUseForShop(arg_33_0, arg_33_1):
		if arg_33_0.IsSkinShopDiscountType():
			var_33_0 = arg_33_0.getConfig("usage_arg")

			if not var_33_0 or type(var_33_0) != "table":
				return False

			var_33_1 = var_33_0[1] or table()

			return len(var_33_1) == 1 and var_33_1[1] == 0 or table.contains(var_33_1, arg_33_1)

		return False

	def GetConsumeForSkinShopDiscount(arg_34_0, arg_34_1):
		if arg_34_0.IsSkinShopDiscountType():
			var_34_0 = pg.item_data_statistics[arg_34_0.configId].usage_arg[2] or 0
			var_34_1 = Goods.Create(table(
				shop_id = arg_34_1
			), Goods.TYPE_SKIN)

			return max(0, var_34_1.GetPrice() - var_34_0), var_34_1.getConfig("resource_type")
		else:
			return 0

	def getName(arg_35_0):
		return arg_35_0.name or arg_35_0.getConfig("name")

	def getIcon(arg_36_0):
		return arg_36_0.getConfig("Icon")
	