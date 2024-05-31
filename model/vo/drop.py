local var_0_0 = class("Drop", import(".BaseVO"))

def var_0_0.Create(arg_1_0):
	local var_1_0 = {}

	var_1_0.type, var_1_0.id, var_1_0.count = unpack(arg_1_0)

	return var_0_0.New(var_1_0)

def var_0_0.Change(arg_2_0):
	if not getmetatable(arg_2_0):
		setmetatable(arg_2_0, var_0_0)

		arg_2_0.class = var_0_0

		arg_2_0.InitConfig()
	else
		assert(instanceof(arg_2_0, var_0_0))

	return arg_2_0

def var_0_0.Ctor(arg_3_0, arg_3_1):
	assert(not getmetatable(arg_3_1), "drop data should not has metatable")

	for iter_3_0, iter_3_1 in pairs(arg_3_1):
		arg_3_0[iter_3_0] = iter_3_1

	arg_3_0.InitConfig()

def var_0_0.InitConfig(arg_4_0):
	if not var_0_0.inited:
		var_0_0.InitSwitch()

	arg_4_0.configId = arg_4_0.id
	arg_4_0.cfg = switch(arg_4_0.type, var_0_0.ConfigCase, var_0_0.ConfigDefault, arg_4_0)

def var_0_0.getConfigTable(arg_5_0):
	return arg_5_0.cfg

def var_0_0.getName(arg_6_0):
	return arg_6_0.name or arg_6_0.getConfig("name")

def var_0_0.getIcon(arg_7_0):
	return arg_7_0.getConfig("icon")

def var_0_0.getCount(arg_8_0):
	if arg_8_0.type == DROP_TYPE_OPERATION or arg_8_0.type == DROP_TYPE_LOVE_LETTER:
		return 1
	else
		return arg_8_0.count

def var_0_0.getOwnedCount(arg_9_0):
	return switch(arg_9_0.type, var_0_0.CountCase, var_0_0.CountDefault, arg_9_0)

def var_0_0.getSubClass(arg_10_0):
	return switch(arg_10_0.type, var_0_0.SubClassCase, var_0_0.SubClassDefault, arg_10_0)

def var_0_0.getDropRarity(arg_11_0):
	return switch(arg_11_0.type, var_0_0.RarityCase, var_0_0.RarityDefault, arg_11_0)

def var_0_0.DropTrans(arg_12_0, ...):
	return switch(arg_12_0.type, var_0_0.TransCase, var_0_0.TransDefault, arg_12_0, ...)

def var_0_0.AddItemOperation(arg_13_0):
	return switch(arg_13_0.type, var_0_0.AddItemCase, var_0_0.AddItemDefault, arg_13_0)

def var_0_0.MsgboxIntroSet(arg_14_0, ...):
	return switch(arg_14_0.type, var_0_0.MsgboxIntroCase, var_0_0.MsgboxIntroDefault, arg_14_0, ...)

def var_0_0.UpdateDropTpl(arg_15_0, ...):
	return switch(arg_15_0.type, var_0_0.UpdateDropCase, var_0_0.UpdateDropDefault, arg_15_0, ...)

def var_0_0.InitSwitch():
	var_0_0.inited = True
	var_0_0.ConfigCase = {
		[DROP_TYPE_RESOURCE] = function(arg_17_0)
			local var_17_0 = Item.getConfigData(id2ItemId(arg_17_0.id))

			arg_17_0.desc = var_17_0.display

			return var_17_0,
		[DROP_TYPE_ITEM] = function(arg_18_0)
			local var_18_0 = Item.getConfigData(arg_18_0.id)

			arg_18_0.desc = var_18_0.display

			if var_18_0.type == Item.LOVE_LETTER_TYPE:
				arg_18_0.desc = string.gsub(arg_18_0.desc, "$1", ShipGroup.getDefaultShipNameByGroupID(arg_18_0.extra))

			return var_18_0,
		[DROP_TYPE_VITEM] = function(arg_19_0)
			local var_19_0 = Item.getConfigData(arg_19_0.id)

			arg_19_0.desc = var_19_0.display

			return var_19_0,
		[DROP_TYPE_LOVE_LETTER] = function(arg_20_0)
			local var_20_0 = Item.getConfigData(arg_20_0.id)

			arg_20_0.desc = string.gsub(var_20_0.display, "$1", ShipGroup.getDefaultShipNameByGroupID(arg_20_0.count))

			return var_20_0,
		[DROP_TYPE_EQUIP] = function(arg_21_0)
			local var_21_0 = Equipment.getConfigData(arg_21_0.id)

			arg_21_0.desc = var_21_0.descrip

			return var_21_0,
		[DROP_TYPE_SHIP] = function(arg_22_0)
			local var_22_0 = pg.ship_data_statistics[arg_22_0.id]
			local var_22_1, var_22_2, var_22_3 = ShipWordHelper.GetWordAndCV(var_22_0.skin_id, ShipWordHelper.WORD_TYPE_DROP)

			arg_22_0.desc = var_22_3 or i18n("ship_drop_desc_default")
			arg_22_0.ship = Ship.New({
				configId = arg_22_0.id,
				skin_id = arg_22_0.skinId,
				propose = arg_22_0.propose
			})
			arg_22_0.ship.remoulded = arg_22_0.remoulded
			arg_22_0.ship.virgin = arg_22_0.virgin

			return var_22_0,
		[DROP_TYPE_FURNITURE] = function(arg_23_0)
			local var_23_0 = pg.furniture_data_template[arg_23_0.id]

			arg_23_0.desc = var_23_0.describe

			return var_23_0,
		[DROP_TYPE_SKIN] = function(arg_24_0)
			local var_24_0 = pg.ship_skin_template[arg_24_0.id]
			local var_24_1, var_24_2, var_24_3 = ShipWordHelper.GetWordAndCV(arg_24_0.id, ShipWordHelper.WORD_TYPE_DROP)

			arg_24_0.desc = var_24_3

			return var_24_0,
		[DROP_TYPE_SKIN_TIMELIMIT] = function(arg_25_0)
			local var_25_0 = pg.ship_skin_template[arg_25_0.id]
			local var_25_1, var_25_2, var_25_3 = ShipWordHelper.GetWordAndCV(arg_25_0.id, ShipWordHelper.WORD_TYPE_DROP)

			arg_25_0.desc = var_25_3

			return var_25_0,
		[DROP_TYPE_EQUIPMENT_SKIN] = function(arg_26_0)
			local var_26_0 = pg.equip_skin_template[arg_26_0.id]

			arg_26_0.desc = var_26_0.desc

			return var_26_0,
		[DROP_TYPE_WORLD_ITEM] = function(arg_27_0)
			local var_27_0 = pg.world_item_data_template[arg_27_0.id]

			arg_27_0.desc = var_27_0.display

			return var_27_0,
		[DROP_TYPE_ICON_FRAME] = function(arg_28_0)
			return pg.item_data_frame[arg_28_0.id],
		[DROP_TYPE_CHAT_FRAME] = function(arg_29_0)
			return pg.item_data_chat[arg_29_0.id],
		[DROP_TYPE_SPWEAPON] = function(arg_30_0)
			local var_30_0 = pg.spweapon_data_statistics[arg_30_0.id]

			arg_30_0.desc = var_30_0.descrip

			return var_30_0,
		[DROP_TYPE_RYZA_DROP] = function(arg_31_0)
			local var_31_0 = pg.activity_ryza_item[arg_31_0.id]

			arg_31_0.item = AtelierMaterial.New({
				configId = arg_31_0.id
			})
			arg_31_0.desc = arg_31_0.item.GetDesc()

			return var_31_0,
		[DROP_TYPE_OPERATION] = function(arg_32_0)
			arg_32_0.ship = getProxy(BayProxy).getShipById(arg_32_0.count)

			local var_32_0 = pg.ship_data_statistics[arg_32_0.ship.configId]
			local var_32_1, var_32_2, var_32_3 = ShipWordHelper.GetWordAndCV(var_32_0.skin_id, ShipWordHelper.WORD_TYPE_DROP)

			arg_32_0.desc = var_32_3 or i18n("ship_drop_desc_default")

			return var_32_0,
		[DROP_TYPE_STRATEGY] = function(arg_33_0)
			return arg_33_0.isWorldBuff and pg.world_SLGbuff_data[arg_33_0.id] or pg.strategy_data_template[arg_33_0.id],
		[DROP_TYPE_EMOJI] = function(arg_34_0)
			local var_34_0 = pg.emoji_template[arg_34_0.id]

			arg_34_0.name = var_34_0.item_name
			arg_34_0.desc = var_34_0.item_desc

			return var_34_0,
		[DROP_TYPE_WORLD_COLLECTION] = function(arg_35_0)
			local var_35_0 = WorldCollectionProxy.GetCollectionTemplate(arg_35_0.id)

			arg_35_0.desc = var_35_0.name

			return var_35_0,
		[DROP_TYPE_META_PT] = function(arg_36_0)
			local var_36_0 = pg.ship_strengthen_meta[arg_36_0.id]
			local var_36_1 = Item.getConfigData(var_36_0.itemid)

			arg_36_0.desc = var_36_1.display

			return var_36_1,
		[DROP_TYPE_WORKBENCH_DROP] = function(arg_37_0)
			local var_37_0 = pg.activity_workbench_item[arg_37_0.id]

			arg_37_0.item = WorkBenchItem.New({
				configId = arg_37_0.id
			})
			arg_37_0.desc = arg_37_0.item.GetDesc()

			return var_37_0,
		[DROP_TYPE_BUFF] = function(arg_38_0)
			local var_38_0 = pg.benefit_buff_template[arg_38_0.id]

			arg_38_0.desc = var_38_0.desc

			return var_38_0,
		[DROP_TYPE_COMMANDER_CAT] = function(arg_39_0)
			local var_39_0 = pg.commander_data_template[arg_39_0.id]

			arg_39_0.desc = ""

			return var_39_0,
		[DROP_TYPE_TRANS_ITEM] = function(arg_40_0)
			return pg.drop_data_restore[arg_40_0.id],
		[DROP_TYPE_DORM3D_FURNITURE] = function(arg_41_0)
			local var_41_0 = pg.dorm3d_furniture_template[arg_41_0.id]

			arg_41_0.desc = var_41_0.desc

			return var_41_0,
		[DROP_TYPE_DORM3D_GIFT] = function(arg_42_0)
			local var_42_0 = pg.dorm3d_gift[arg_42_0.id]

			arg_42_0.desc = ""

			return var_42_0,
		[DROP_TYPE_DORM3D_SKIN] = function(arg_43_0)
			local var_43_0 = pg.dorm3d_resource[arg_43_0.id]

			arg_43_0.desc = ""

			return var_43_0
	}

	function var_0_0.ConfigDefault(arg_44_0)
		local var_44_0 = arg_44_0.type

		if var_44_0 > DROP_TYPE_USE_ACTIVITY_DROP:
			local var_44_1 = pg.activity_drop_type[var_44_0].relevance

			return var_44_1 and pg[var_44_1][arg_44_0.id]

	var_0_0.CountCase = {
		[DROP_TYPE_RESOURCE] = function(arg_45_0)
			return getProxy(PlayerProxy).getRawData().getResById(arg_45_0.id), True,
		[DROP_TYPE_ITEM] = function(arg_46_0)
			local var_46_0 = getProxy(BagProxy).getItemCountById(arg_46_0.id)

			if arg_46_0.getConfig("type") == Item.LOVE_LETTER_TYPE:
				return math.min(var_46_0, 1), True
			else
				return var_46_0, True,
		[DROP_TYPE_EQUIP] = function(arg_47_0)
			local var_47_0 = arg_47_0.getConfig("group")

			assert(pg.equip_data_template.get_id_list_by_group[var_47_0], "equip groupId not exist")

			local var_47_1 = pg.equip_data_template.get_id_list_by_group[var_47_0]

			return underscore.reduce(var_47_1, 0, function(arg_48_0, arg_48_1)
				local var_48_0 = getProxy(EquipmentProxy).getEquipmentById(arg_48_1)

				return arg_48_0 + (var_48_0 and var_48_0.count or 0) + getProxy(BayProxy).GetEquipCountInShips(arg_48_1)),
		[DROP_TYPE_SHIP] = function(arg_49_0)
			return getProxy(BayProxy).getConfigShipCount(arg_49_0.id),
		[DROP_TYPE_FURNITURE] = function(arg_50_0)
			return getProxy(DormProxy).getRawData().GetOwnFurnitureCount(arg_50_0.id),
		[DROP_TYPE_STRATEGY] = function(arg_51_0)
			return arg_51_0.count, tobool(arg_51_0.count),
		[DROP_TYPE_SKIN] = function(arg_52_0)
			return getProxy(ShipSkinProxy).getSkinCountById(arg_52_0.id),
		[DROP_TYPE_SKIN_TIMELIMIT] = function(arg_53_0)
			return getProxy(ShipSkinProxy).getSkinCountById(arg_53_0.id),
		[DROP_TYPE_VITEM] = function(arg_54_0)
			if arg_54_0.getConfig("virtual_type") == 22:
				local var_54_0 = getProxy(ActivityProxy).getActivityById(arg_54_0.getConfig("link_id"))

				return var_54_0 and var_54_0.data1 or 0, True,
		[DROP_TYPE_EQUIPMENT_SKIN] = function(arg_55_0)
			local var_55_0 = getProxy(EquipmentProxy).getEquipmnentSkinById(arg_55_0.id)

			return (var_55_0 and var_55_0.count or 0) + getProxy(BayProxy).GetEquipSkinCountInShips(arg_55_0.id),
		[DROP_TYPE_RYZA_DROP] = function(arg_56_0)
			local var_56_0 = getProxy(ActivityProxy).getActivityById(pg.activity_drop_type[arg_56_0.type].activity_id).GetItemById(arg_56_0.id)

			return var_56_0 and var_56_0.count or 0,
		[DROP_TYPE_ICON_FRAME] = function(arg_57_0)
			local var_57_0 = getProxy(AttireProxy).getAttireFrame(AttireConst.TYPE_ICON_FRAME, arg_57_0.id)

			return var_57_0 and (not var_57_0.expiredType() or not not var_57_0.isExpired()) and 1 or 0,
		[DROP_TYPE_CHAT_FRAME] = function(arg_58_0)
			local var_58_0 = getProxy(AttireProxy).getAttireFrame(AttireConst.TYPE_CHAT_FRAME, arg_58_0.id)

			return var_58_0 and (not var_58_0.expiredType() or not not var_58_0.isExpired()) and 1 or 0,
		[DROP_TYPE_WORLD_ITEM] = function(arg_59_0)
			local var_59_0 = nowWorld()

			if var_59_0.type != World.TypeFull:
				assert(False)

				return 0, False
			else
				return var_59_0.GetInventoryProxy().GetItemCount(arg_59_0.id), False,
		[DROP_TYPE_COMMANDER_CAT] = function(arg_60_0)
			return getProxy(CommanderProxy).GetSameConfigIdCommanderCount(arg_60_0.id)
	}

	function var_0_0.CountDefault(arg_61_0)
		local var_61_0 = arg_61_0.type

		if var_61_0 > DROP_TYPE_USE_ACTIVITY_DROP:
			return getProxy(ActivityProxy).getActivityById(pg.activity_drop_type[var_61_0].activity_id).getVitemNumber(arg_61_0.id)
		else
			return 0, False

	var_0_0.SubClassCase = {
		[DROP_TYPE_RESOURCE] = function(arg_62_0)
			return,
		[DROP_TYPE_ITEM] = function(arg_63_0)
			return Item.New(arg_63_0),
		[DROP_TYPE_VITEM] = function(arg_64_0)
			return Item.New(arg_64_0),
		[DROP_TYPE_EQUIP] = function(arg_65_0)
			return Equipment.New(arg_65_0),
		[DROP_TYPE_LOVE_LETTER] = function(arg_66_0)
			return Item.New({
				count = 1,
				id = arg_66_0.id,
				extra = arg_66_0.count
			}),
		[DROP_TYPE_WORLD_ITEM] = function(arg_67_0)
			return WorldItem.New(arg_67_0)
	}

	function var_0_0.SubClassDefault(arg_68_0)
		assert(False, string.format("drop type %d without subClass", arg_68_0.type))

	var_0_0.RarityCase = {
		[DROP_TYPE_RESOURCE] = function(arg_69_0)
			return arg_69_0.getConfig("rarity"),
		[DROP_TYPE_ITEM] = function(arg_70_0)
			return arg_70_0.getConfig("rarity"),
		[DROP_TYPE_EQUIP] = function(arg_71_0)
			return arg_71_0.getConfig("rarity") - 1,
		[DROP_TYPE_SHIP] = function(arg_72_0)
			return arg_72_0.getConfig("rarity") - 1,
		[DROP_TYPE_FURNITURE] = function(arg_73_0)
			return arg_73_0.getConfig("rarity"),
		[DROP_TYPE_SKIN] = function(arg_74_0)
			return ItemRarity.Gold,
		[DROP_TYPE_SKIN_TIMELIMIT] = function(arg_75_0)
			return ItemRarity.Gold,
		[DROP_TYPE_VITEM] = function(arg_76_0)
			return arg_76_0.getConfig("rarity"),
		[DROP_TYPE_WORLD_ITEM] = function(arg_77_0)
			return arg_77_0.getConfig("rarity"),
		[DROP_TYPE_BUFF] = function(arg_78_0)
			return ItemRarity.Purple,
		[DROP_TYPE_COMMANDER_CAT] = function(arg_79_0)
			return arg_79_0.getConfig("rarity") - 1,
		[DROP_TYPE_DORM3D_FURNITURE] = function(arg_80_0)
			return arg_80_0.getConfig("rarity"),
		[DROP_TYPE_DORM3D_SKIN] = function(arg_81_0)
			return ItemRarity.Gold,
		[DROP_TYPE_WORLD_COLLECTION] = function(arg_82_0)
			return ItemRarity.Gold
	}

	function var_0_0.RarityDefault(arg_83_0)
		return 1

	var_0_0.TransCase = {
		[DROP_TYPE_TRANS_ITEM] = function(arg_84_0)
			local var_84_0 = Drop.New({
				type = DROP_TYPE_RESOURCE,
				id = arg_84_0.getConfig("resource_type"),
				count = arg_84_0.getConfig("resource_num") * arg_84_0.count
			})
			local var_84_1 = Drop.New({
				type = arg_84_0.getConfig("target_type"),
				id = arg_84_0.getConfig("target_id")
			})

			var_84_0.name = string.format("%s(%s)", var_84_0.getName(), var_84_1.getName())

			return var_84_0,
		[DROP_TYPE_RESOURCE] = function(arg_85_0)
			for iter_85_0, iter_85_1 in ipairs(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PT_CRUSING)):
				if pg.battlepass_event_pt[iter_85_1.id].pt == arg_85_0.id:
					return None, arg_85_0

			return arg_85_0,
		[DROP_TYPE_OPERATION] = function(arg_86_0)
			if arg_86_0.id != 3:
				return None

			return arg_86_0,
		[DROP_TYPE_VITEM] = function(arg_87_0, arg_87_1, arg_87_2)
			assert(arg_87_0.getConfig("type") == 0, "item type error.must be virtual type from " .. arg_87_0.id)

			return switch(arg_87_0.getConfig("virtual_type"), {
				function()
					if arg_87_0.getConfig("link_id") == ActivityConst.LINLK_DUNHUANG_ACT:
						return None, arg_87_0

					return arg_87_0,
				[6] = function()
					local var_89_0 = arg_87_2.taskId
					local var_89_1 = getProxy(ActivityProxy)
					local var_89_2 = var_89_1.getActivityByType(ActivityConst.ACTIVITY_TYPE_REFLUX)

					if var_89_2:
						local var_89_3 = var_89_2.data1KeyValueList[1]

						var_89_3[var_89_0] = defaultValue(var_89_3[var_89_0], 0) + arg_87_0.count

						var_89_1.updateActivity(var_89_2)

					return None, arg_87_0,
				[13] = function()
					local var_90_0 = arg_87_0.getName()

					if not SkinCouponActivity.StaticExistActivity():
						pg.TipsMgr.GetInstance().ShowTips(i18n("coupon_timeout_tip", var_90_0))

						return None
					elif SkinCouponActivity.StaticOwnMaxCntSkinCoupon():
						pg.TipsMgr.GetInstance().ShowTips(i18n("coupon_repeat_tip", var_90_0))

						return None
					elif SkinCouponActivity.StaticOwnAllSkin():
						if arg_87_0.count > 1:
							pg.TipsMgr.GetInstance().ShowTips(i18n("coupon_repeat_tip", var_90_0))

						return SkinCouponActivity.StaticGetEquivalentRes(), None
					else
						return arg_87_0, None,
				[21] = function()
					return None, arg_87_0
			}, function()
				return arg_87_0),
		[DROP_TYPE_SHIP] = function(arg_93_0, arg_93_1)
			if Ship.isMetaShipByConfigID(arg_93_0.id) and Player.isMetaShipNeedToTrans(arg_93_0.id):
				local var_93_0 = table.indexof(arg_93_1, arg_93_0.id, 1)

				if var_93_0:
					table.remove(arg_93_1, var_93_0)
				else
					local var_93_1 = Player.metaShip2Res(arg_93_0.id)
					local var_93_2 = Drop.New(var_93_1[1])

					getProxy(BayProxy).addMetaTransItemMap(arg_93_0.id, var_93_2)

					return arg_93_0, var_93_2

			return arg_93_0,
		[DROP_TYPE_SKIN] = function(arg_94_0)
			arg_94_0.isNew = not getProxy(ShipSkinProxy).hasOldNonLimitSkin(arg_94_0.id)

			return arg_94_0
	}

	function var_0_0.TransDefault(arg_95_0)
		return arg_95_0

	var_0_0.AddItemCase = {
		[DROP_TYPE_RESOURCE] = function(arg_96_0)
			local var_96_0 = id2res(arg_96_0.id)

			assert(var_96_0, "res should be defined. " .. arg_96_0.id)

			local var_96_1 = getProxy(PlayerProxy)
			local var_96_2 = var_96_1.getData()

			var_96_2.addResources({
				[var_96_0] = arg_96_0.count
			})
			var_96_1.updatePlayer(var_96_2),
		[DROP_TYPE_ITEM] = function(arg_97_0)
			if arg_97_0.getConfig("type") == Item.EXP_BOOK_TYPE:
				local var_97_0 = getProxy(BagProxy).getItemCountById(arg_97_0.id)
				local var_97_1 = math.min(arg_97_0.getConfig("max_num") - var_97_0, arg_97_0.count)

				if var_97_1 > 0:
					getProxy(BagProxy).addItemById(arg_97_0.id, var_97_1)
			else
				getProxy(BagProxy).addItemById(arg_97_0.id, arg_97_0.count, arg_97_0.extra),
		[DROP_TYPE_LOVE_LETTER] = function(arg_98_0)
			local var_98_0 = arg_98_0.getSubClass()

			getProxy(BagProxy).addItemById(var_98_0.id, var_98_0.count, var_98_0.extra),
		[DROP_TYPE_EQUIP] = function(arg_99_0)
			getProxy(EquipmentProxy).addEquipmentById(arg_99_0.id, arg_99_0.count),
		[DROP_TYPE_SHIP] = function(arg_100_0)
			return,
		[DROP_TYPE_FURNITURE] = function(arg_101_0)
			local var_101_0 = getProxy(DormProxy)
			local var_101_1 = Furniture.New({
				id = arg_101_0.id,
				count = arg_101_0.count
			})

			if var_101_1.isRecordTime():
				var_101_1.date = pg.TimeMgr.GetInstance().GetServerTime()

			var_101_0.AddFurniture(var_101_1),
		[DROP_TYPE_SKIN] = function(arg_102_0)
			local var_102_0 = getProxy(ShipSkinProxy)
			local var_102_1 = ShipSkin.New({
				id = arg_102_0.id
			})

			var_102_0.addSkin(var_102_1),
		[DROP_TYPE_VITEM] = function(arg_103_0)
			arg_103_0 = arg_103_0.getSubClass()

			assert(arg_103_0.isVirtualItem(), "item type error(virtual item)>>" .. arg_103_0.id)
			switch(arg_103_0.getConfig("virtual_type"), {
				[0] = function()
					getProxy(ActivityProxy).addVitemById(arg_103_0.id, arg_103_0.count),
				function()
					local var_105_0 = getProxy(ActivityProxy)
					local var_105_1 = arg_103_0.getConfig("link_id")
					local var_105_2

					if var_105_1 > 0:
						var_105_2 = var_105_0.getActivityById(var_105_1)
					else
						var_105_2 = var_105_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_PUZZLA)

					if var_105_2 and not var_105_2.isEnd():
						if not table.contains(var_105_2.data1_list, arg_103_0.id):
							table.insert(var_105_2.data1_list, arg_103_0.id)

						var_105_0.updateActivity(var_105_2),
				function()
					local var_106_0 = getProxy(ActivityProxy)
					local var_106_1 = var_106_0.getActivitiesByType(ActivityConst.ACTIVITY_TYPE_VOTE)

					for iter_106_0, iter_106_1 in ipairs(var_106_1):
						iter_106_1.data1 = iter_106_1.data1 + arg_103_0.count

						local var_106_2 = iter_106_1.getConfig("config_id")
						local var_106_3 = pg.activity_vote[var_106_2]

						if var_106_3 and var_106_3.ticket_id_period == arg_103_0.id:
							iter_106_1.data3 = iter_106_1.data3 + arg_103_0.count

						var_106_0.updateActivity(iter_106_1)
						pg.ToastMgr.GetInstance().ShowToast(pg.ToastMgr.TYPE_VOTE, {
							ptId = arg_103_0.id,
							ptCount = arg_103_0.count
						}),
				[4] = function()
					local var_107_0 = getProxy(ColoringProxy).getColorItems()

					var_107_0[arg_103_0.id] = (var_107_0[arg_103_0.id] or 0) + arg_103_0.count,
				[6] = function()
					local var_108_0 = getProxy(ActivityProxy)
					local var_108_1 = var_108_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_REFLUX)

					if var_108_1:
						var_108_1.data3 = var_108_1.data3 + arg_103_0.count

						var_108_0.updateActivity(var_108_1),
				[7] = function()
					local var_109_0 = getProxy(ChapterProxy)

					var_109_0.updateRemasterTicketsNum(math.min(var_109_0.remasterTickets + arg_103_0.count, pg.gameset.reactivity_ticket_max.key_value)),
				[9] = function()
					local var_110_0 = getProxy(ActivityProxy)
					local var_110_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_MONOPOLY)

					if var_110_1:
						var_110_1.data1_list[1] = var_110_1.data1_list[1] + arg_103_0.count

						var_110_0.updateActivity(var_110_1),
				[10] = function()
					local var_111_0 = getProxy(ActivityProxy)
					local var_111_1 = var_111_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_INSTAGRAM)

					if var_111_1 and not var_111_1.isEnd():
						var_111_1.data1 = var_111_1.data1 + arg_103_0.count

						var_111_0.updateActivity(var_111_1)
						pg.m02.sendNotification(GAME.ACTIVITY_BE_UPDATED, {
							activity = var_111_1
						}),
				[11] = function()
					local var_112_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_RED_PACKETS)

					if var_112_0 and not var_112_0.isEnd():
						var_112_0.data1 = var_112_0.data1 + arg_103_0.count,
				[12] = function()
					local var_113_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF)

					if var_113_0 and not var_113_0.isEnd():
						var_113_0.data1KeyValueList[1][arg_103_0.id] = (var_113_0.data1KeyValueList[1][arg_103_0.id] or 0) + arg_103_0.count,
				[13] = function()
					SkinCouponActivity.AddSkinCoupon(arg_103_0.id),
				[14] = function()
					local var_115_0 = nowWorld().GetBossProxy()

					if WorldBossConst.WORLD_BOSS_ITEM_ID == arg_103_0.id:
						var_115_0.AddSummonPt(arg_103_0.count)
					elif WorldBossConst.WORLD_PAST_BOSS_ITEM_ID == arg_103_0.id:
						var_115_0.AddSummonPtOld(arg_103_0.count),
				[15] = function()
					local var_116_0 = getProxy(ActivityProxy)
					local var_116_1 = var_116_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_WORLDINPICTURE)

					if var_116_1 and not var_116_1.isEnd():
						local var_116_2 = pg.activity_event_grid[var_116_1.data1]

						if arg_103_0.id == var_116_2.ticket_item:
							var_116_1.data2 = var_116_1.data2 + arg_103_0.count
						elif arg_103_0.id == var_116_2.explore_item:
							var_116_1.data3 = var_116_1.data3 + arg_103_0.count

					var_116_0.updateActivity(var_116_1),
				[16] = function()
					local var_117_0 = getProxy(ActivityProxy)
					local var_117_1 = var_117_0.getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHAKE_BEADS)

					for iter_117_0, iter_117_1 in pairs(var_117_1):
						if iter_117_1 and not iter_117_1.isEnd() and arg_103_0.id == iter_117_1.getConfig("config_id"):
							iter_117_1.data1 = iter_117_1.data1 + arg_103_0.count

							var_117_0.updateActivity(iter_117_1),
				[20] = function()
					local var_118_0 = getProxy(BagProxy)
					local var_118_1 = pg.gameset.urpt_chapter_max.description
					local var_118_2 = var_118_1[1]
					local var_118_3 = var_118_1[2]
					local var_118_4 = var_118_0.GetLimitCntById(var_118_2)
					local var_118_5 = math.min(var_118_3 - var_118_4, arg_103_0.count)

					if var_118_5 > 0:
						var_118_0.addItemById(var_118_2, var_118_5)
						var_118_0.AddLimitCnt(var_118_2, var_118_5),
				[21] = function()
					local var_119_0 = getProxy(ActivityProxy)
					local var_119_1 = var_119_0.getActivityById(arg_103_0.getConfig("link_id"))

					if var_119_1 and not var_119_1.isEnd():
						var_119_1.data2 = 1

						var_119_0.updateActivity(var_119_1),
				[22] = function()
					local var_120_0 = getProxy(ActivityProxy)
					local var_120_1 = var_120_0.getActivityById(arg_103_0.getConfig("link_id"))

					if var_120_1 and not var_120_1.isEnd():
						var_120_1.data1 = var_120_1.data1 + arg_103_0.count

						var_120_0.updateActivity(var_120_1),
				[23] = function()
					local var_121_0 = (function()
						for iter_122_0, iter_122_1 in ipairs(pg.gameset.package_lv.description):
							if arg_103_0.id == iter_122_1[1]:
								return iter_122_1[2])()

					assert(var_121_0)

					local var_121_1 = getProxy(PlayerProxy)
					local var_121_2 = var_121_1.getData()

					var_121_2.addExpToLevel(var_121_0)
					var_121_1.updatePlayer(var_121_2),
				[24] = function()
					local var_123_0 = arg_103_0.getConfig("link_id")
					local var_123_1 = getProxy(ActivityProxy).getActivityById(var_123_0)

					if var_123_1 and not var_123_1.isEnd() and var_123_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_HOTSPRING:
						var_123_1.data2 = var_123_1.data2 + arg_103_0.count

						getProxy(ActivityProxy).updateActivity(var_123_1),
				[25] = function()
					local var_124_0 = getProxy(ActivityProxy)
					local var_124_1 = var_124_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_FIREWORK)

					if var_124_1 and not var_124_1.isEnd():
						var_124_1.data1 = var_124_1.data1 - 1

						if not table.contains(var_124_1.data1_list, arg_103_0.id):
							table.insert(var_124_1.data1_list, arg_103_0.id)

						var_124_0.updateActivity(var_124_1)

						local var_124_2 = arg_103_0.getConfig("link_id")

						if var_124_2 > 0:
							local var_124_3 = var_124_0.getActivityById(var_124_2)

							if var_124_3 and not var_124_3.isEnd():
								var_124_3.data1 = var_124_3.data1 + 1

								var_124_0.updateActivity(var_124_3),
				[99] = function()
					return,
				[100] = function()
					return
			}),
		[DROP_TYPE_EQUIPMENT_SKIN] = function(arg_127_0)
			getProxy(EquipmentProxy).addEquipmentSkin(arg_127_0.id, arg_127_0.count),
		[DROP_TYPE_OPERATION] = function(arg_128_0)
			local var_128_0 = getProxy(BayProxy)
			local var_128_1 = var_128_0.getShipById(arg_128_0.count)

			if var_128_1:
				var_128_1.unlockActivityNpc(0)
				var_128_0.updateShip(var_128_1)
				getProxy(CollectionProxy).flushCollection(var_128_1),
		[DROP_TYPE_WORLD_ITEM] = function(arg_129_0)
			nowWorld().GetInventoryProxy().AddItem(arg_129_0.id, arg_129_0.count),
		[DROP_TYPE_ICON_FRAME] = function(arg_130_0)
			local var_130_0 = getProxy(AttireProxy)
			local var_130_1 = pg.TimeMgr.GetInstance().GetServerTime()
			local var_130_2 = IconFrame.New({
				id = arg_130_0.id
			})
			local var_130_3 = var_130_1 + var_130_2.getConfig("time_second")

			var_130_2.updateData({
				isNew = True,_time = var_130_3
			})
			var_130_0.addAttireFrame(var_130_2)
			pg.ToastMgr.GetInstance().ShowToast(pg.ToastMgr.TYPE_ATTIRE, var_130_2),
		[DROP_TYPE_CHAT_FRAME] = function(arg_131_0)
			local var_131_0 = getProxy(AttireProxy)
			local var_131_1 = pg.TimeMgr.GetInstance().GetServerTime()
			local var_131_2 = ChatFrame.New({
				id = arg_131_0.id
			})
			local var_131_3 = var_131_1 + var_131_2.getConfig("time_second")

			var_131_2.updateData({
				isNew = True,_time = var_131_3
			})
			var_131_0.addAttireFrame(var_131_2)
			pg.ToastMgr.GetInstance().ShowToast(pg.ToastMgr.TYPE_ATTIRE, var_131_2),
		[DROP_TYPE_EMOJI] = function(arg_132_0)
			getProxy(EmojiProxy).addNewEmojiID(arg_132_0.id)
			pg.ToastMgr.GetInstance().ShowToast(pg.ToastMgr.TYPE_EMOJI, arg_132_0.getConfigTable()),
		[DROP_TYPE_WORLD_COLLECTION] = function(arg_133_0)
			nowWorld().GetCollectionProxy().Unlock(arg_133_0.id),
		[DROP_TYPE_META_PT] = function(arg_134_0)
			getProxy(MetaCharacterProxy).getMetaProgressVOByID(arg_134_0.id).addPT(arg_134_0.count),
		[DROP_TYPE_SKIN_TIMELIMIT] = function(arg_135_0)
			local var_135_0 = arg_135_0.id
			local var_135_1 = arg_135_0.count
			local var_135_2 = getProxy(ShipSkinProxy)
			local var_135_3 = var_135_2.getSkinById(var_135_0)

			if var_135_3 and var_135_3.isExpireType():
				local var_135_4 = var_135_1 + var_135_3.endTime
				local var_135_5 = ShipSkin.New({
					id = var_135_0,_time = var_135_4
				})

				var_135_2.addSkin(var_135_5)
			elif not var_135_3:
				local var_135_6 = var_135_1 + pg.TimeMgr.GetInstance().GetServerTime()
				local var_135_7 = ShipSkin.New({
					id = var_135_0,_time = var_135_6
				})

				var_135_2.addSkin(var_135_7),
		[DROP_TYPE_BUFF] = function(arg_136_0)
			local var_136_0 = arg_136_0.id
			local var_136_1 = pg.benefit_buff_template[var_136_0]

			assert(var_136_1 and var_136_1.act_id > 0, "should exist act id")

			local var_136_2 = getProxy(ActivityProxy).getActivityById(var_136_1.act_id)

			if var_136_2 and not var_136_2.isEnd():
				local var_136_3 = var_136_1.max_time
				local var_136_4 = pg.TimeMgr.GetInstance().GetServerTime() + var_136_3

				var_136_2.AddBuff(ActivityBuff.New(var_136_2.id, var_136_0, var_136_4))
				getProxy(ActivityProxy).updateActivity(var_136_2),
		[DROP_TYPE_COMMANDER_CAT] = function(arg_137_0)
			return,
		[DROP_TYPE_DORM3D_GIFT] = function(arg_138_0)
			getProxy(ApartmentProxy).changeGiftCount(arg_138_0.id, arg_138_0.count),
		[DROP_TYPE_DORM3D_SKIN] = function(arg_139_0)
			local var_139_0 = getProxy(ApartmentProxy)
			local var_139_1 = var_139_0.getApartment(arg_139_0.getConfig("ship_group"))

			var_139_1.addSkin(arg_139_0.id)
			var_139_0.updateApartment(var_139_1)
	}

	function var_0_0.AddItemDefault(arg_140_0)
		if arg_140_0.type > DROP_TYPE_USE_ACTIVITY_DROP:
			local var_140_0 = getProxy(ActivityProxy).getActivityById(pg.activity_drop_type[arg_140_0.type].activity_id)

			if arg_140_0.type == DROP_TYPE_RYZA_DROP:
				if var_140_0 and not var_140_0.isEnd():
					var_140_0.AddItem(AtelierMaterial.New({
						configId = arg_140_0.id,
						count = arg_140_0.count
					}))
					getProxy(ActivityProxy).updateActivity(var_140_0)
			elif var_140_0 and not var_140_0.isEnd():
				var_140_0.addVitemNumber(arg_140_0.id, arg_140_0.count)
				getProxy(ActivityProxy).updateActivity(var_140_0)
		else
			print("can not handle this type>>" .. arg_140_0.type)

	var_0_0.MsgboxIntroCase = {
		[DROP_TYPE_RESOURCE] = function(arg_141_0, arg_141_1, arg_141_2)
			setText(arg_141_2, arg_141_0.getConfig("display")),
		[DROP_TYPE_ITEM] = function(arg_142_0, arg_142_1, arg_142_2)
			local var_142_0 = arg_142_0.getConfig("display")

			if arg_142_0.getConfig("type") == Item.LOVE_LETTER_TYPE:
				var_142_0 = string.gsub(var_142_0, "$1", ShipGroup.getDefaultShipNameByGroupID(arg_142_0.extra))
			elif arg_142_0.getConfig("combination_display") != None:
				local var_142_1 = arg_142_0.getConfig("combination_display")

				if var_142_1 and #var_142_1 > 0:
					var_142_0 = Item.StaticCombinationDisplay(var_142_1)

			setText(arg_142_2, SwitchSpecialChar(var_142_0, True)),
		[DROP_TYPE_FURNITURE] = function(arg_143_0, arg_143_1, arg_143_2)
			setText(arg_143_2, arg_143_0.getConfig("describe")),
		[DROP_TYPE_SHIP] = function(arg_144_0, arg_144_1, arg_144_2)
			local var_144_0 = arg_144_0.getConfig("skin_id")
			local var_144_1, var_144_2, var_144_3 = ShipWordHelper.GetWordAndCV(var_144_0, ShipWordHelper.WORD_TYPE_DROP, None, PLATFORM_CODE != PLATFORM_US)

			setText(arg_144_2, var_144_3 or i18n("ship_drop_desc_default")),
		[DROP_TYPE_OPERATION] = function(arg_145_0, arg_145_1, arg_145_2)
			local var_145_0 = arg_145_0.getConfig("skin_id")
			local var_145_1, var_145_2, var_145_3 = ShipWordHelper.GetWordAndCV(var_145_0, ShipWordHelper.WORD_TYPE_DROP, None, PLATFORM_CODE != PLATFORM_US)

			setText(arg_145_2, var_145_3 or i18n("ship_drop_desc_default")),
		[DROP_TYPE_EQUIP] = function(arg_146_0, arg_146_1, arg_146_2)
			setText(arg_146_2, arg_146_1.name or arg_146_0.getConfig("name") or ""),
		[DROP_TYPE_STRATEGY] = function(arg_147_0, arg_147_1, arg_147_2)
			local var_147_0 = arg_147_0.getConfig("desc")

			for iter_147_0, iter_147_1 in ipairs({
				arg_147_0.count
			}):
				var_147_0 = string.gsub(var_147_0, "$" .. iter_147_0, iter_147_1)

			setText(arg_147_2, var_147_0),
		[DROP_TYPE_SKIN] = function(arg_148_0, arg_148_1, arg_148_2)
			setText(arg_148_2, arg_148_0.getConfig("desc")),
		[DROP_TYPE_SKIN_TIMELIMIT] = function(arg_149_0, arg_149_1, arg_149_2)
			setText(arg_149_2, arg_149_0.getConfig("desc")),
		[DROP_TYPE_EQUIPMENT_SKIN] = function(arg_150_0, arg_150_1, arg_150_2)
			local var_150_0 = arg_150_0.getConfig("desc")
			local var_150_1 = _.map(arg_150_0.getConfig("equip_type"), function(arg_151_0)
				return EquipType.Type2Name2(arg_151_0))

			setText(arg_150_2, var_150_0 .. "\n\n" .. i18n("word_fit") .. ". " .. table.concat(var_150_1, ",")),
		[DROP_TYPE_VITEM] = function(arg_152_0, arg_152_1, arg_152_2)
			setText(arg_152_2, arg_152_0.getConfig("display")),
		[DROP_TYPE_WORLD_ITEM] = function(arg_153_0, arg_153_1, arg_153_2)
			setText(arg_153_2, arg_153_0.getConfig("display")),
		[DROP_TYPE_WORLD_COLLECTION] = function(arg_154_0, arg_154_1, arg_154_2, arg_154_3)
			local var_154_0 = WorldCollectionProxy.GetCollectionType(arg_154_0.id) == WorldCollectionProxy.WorldCollectionType.FILE and "file" or "record"

			setText(arg_154_2, i18n("world_" .. var_154_0 .. "_desc", arg_154_0.getConfig("name")))
			setText(arg_154_3, i18n("world_" .. var_154_0 .. "_name", arg_154_0.getConfig("name"))),
		[DROP_TYPE_ICON_FRAME] = function(arg_155_0, arg_155_1, arg_155_2)
			setText(arg_155_2, arg_155_0.getConfig("desc")),
		[DROP_TYPE_CHAT_FRAME] = function(arg_156_0, arg_156_1, arg_156_2)
			setText(arg_156_2, arg_156_0.getConfig("desc")),
		[DROP_TYPE_EMOJI] = function(arg_157_0, arg_157_1, arg_157_2)
			setText(arg_157_2, arg_157_0.getConfig("item_desc")),
		[DROP_TYPE_LOVE_LETTER] = function(arg_158_0, arg_158_1, arg_158_2)
			local var_158_0 = string.gsub(arg_158_0.getConfig("display"), "$1", ShipGroup.getDefaultShipNameByGroupID(arg_158_0.count))

			setText(arg_158_2, SwitchSpecialChar(var_158_0, True)),
		[DROP_TYPE_META_PT] = function(arg_159_0, arg_159_1, arg_159_2)
			setText(arg_159_2, arg_159_0.getConfig("display")),
		[DROP_TYPE_BUFF] = function(arg_160_0, arg_160_1, arg_160_2)
			setText(arg_160_2, arg_160_0.getConfig("desc")),
		[DROP_TYPE_COMMANDER_CAT] = function(arg_161_0, arg_161_1, arg_161_2)
			setText(arg_161_2, "")
	}

	function var_0_0.MsgboxIntroDefault(arg_162_0, arg_162_1, arg_162_2)
		if arg_162_0.type > DROP_TYPE_USE_ACTIVITY_DROP:
			setText(arg_162_2, arg_162_0.getConfig("display"))
		else
			assert(False, "can not handle this type>>" .. arg_162_0.type)

	var_0_0.UpdateDropCase = {
		[DROP_TYPE_RESOURCE] = function(arg_163_0, arg_163_1, arg_163_2)
			if arg_163_0.id == PlayerConst.ResStoreGold or arg_163_0.id == PlayerConst.ResStoreOil:
				arg_163_2 = arg_163_2 or {}
				arg_163_2.frame = "frame_store"

			updateItem(arg_163_1, Item.New({
				id = id2ItemId(arg_163_0.id)
			}), arg_163_2),
		[DROP_TYPE_ITEM] = function(arg_164_0, arg_164_1, arg_164_2)
			updateItem(arg_164_1, arg_164_0.getSubClass(), arg_164_2),
		[DROP_TYPE_EQUIP] = function(arg_165_0, arg_165_1, arg_165_2)
			updateEquipment(arg_165_1, arg_165_0.getSubClass(), arg_165_2),
		[DROP_TYPE_SHIP] = function(arg_166_0, arg_166_1, arg_166_2)
			updateShip(arg_166_1, arg_166_0.ship, arg_166_2),
		[DROP_TYPE_OPERATION] = function(arg_167_0, arg_167_1, arg_167_2)
			updateShip(arg_167_1, arg_167_0.ship, arg_167_2),
		[DROP_TYPE_FURNITURE] = function(arg_168_0, arg_168_1, arg_168_2)
			updateFurniture(arg_168_1, arg_168_0, arg_168_2),
		[DROP_TYPE_STRATEGY] = function(arg_169_0, arg_169_1, arg_169_2)
			arg_169_2.isWorldBuff = arg_169_0.isWorldBuff

			updateStrategy(arg_169_1, arg_169_0, arg_169_2),
		[DROP_TYPE_SKIN] = function(arg_170_0, arg_170_1, arg_170_2)
			arg_170_2.isSkin = True
			arg_170_2.isNew = arg_170_0.isNew

			updateShip(arg_170_1, Ship.New({
				configId = tonumber(arg_170_0.getConfig("ship_group") .. "1"),
				skin_id = arg_170_0.id
			}), arg_170_2),
		[DROP_TYPE_EQUIPMENT_SKIN] = function(arg_171_0, arg_171_1, arg_171_2)
			local var_171_0 = setmetatable({
				count = arg_171_0.count
			}, {
				__index = arg_171_0.getConfigTable()
			})

			updateEquipmentSkin(arg_171_1, var_171_0, arg_171_2),
		[DROP_TYPE_VITEM] = function(arg_172_0, arg_172_1, arg_172_2)
			updateItem(arg_172_1, Item.New({
				id = arg_172_0.id
			}), arg_172_2),
		[DROP_TYPE_WORLD_ITEM] = function(arg_173_0, arg_173_1, arg_173_2)
			updateWorldItem(arg_173_1, WorldItem.New({
				id = arg_173_0.id
			}), arg_173_2),
		[DROP_TYPE_WORLD_COLLECTION] = function(arg_174_0, arg_174_1, arg_174_2)
			updateWorldCollection(arg_174_1, arg_174_0, arg_174_2),
		[DROP_TYPE_CHAT_FRAME] = function(arg_175_0, arg_175_1, arg_175_2)
			updateAttire(arg_175_1, AttireConst.TYPE_CHAT_FRAME, arg_175_0.getConfigTable(), arg_175_2),
		[DROP_TYPE_ICON_FRAME] = function(arg_176_0, arg_176_1, arg_176_2)
			updateAttire(arg_176_1, AttireConst.TYPE_ICON_FRAME, arg_176_0.getConfigTable(), arg_176_2),
		[DROP_TYPE_EMOJI] = function(arg_177_0, arg_177_1, arg_177_2)
			updateEmoji(arg_177_1, arg_177_0.getConfigTable(), arg_177_2),
		[DROP_TYPE_LOVE_LETTER] = function(arg_178_0, arg_178_1, arg_178_2)
			arg_178_2.count = 1

			updateItem(arg_178_1, arg_178_0.getSubClass(), arg_178_2),
		[DROP_TYPE_SPWEAPON] = function(arg_179_0, arg_179_1, arg_179_2)
			updateSpWeapon(arg_179_1, SpWeapon.New({
				id = arg_179_0.id
			}), arg_179_2),
		[DROP_TYPE_META_PT] = function(arg_180_0, arg_180_1, arg_180_2)
			updateItem(arg_180_1, Item.New({
				id = arg_180_0.getConfig("id")
			}), arg_180_2),
		[DROP_TYPE_SKIN_TIMELIMIT] = function(arg_181_0, arg_181_1, arg_181_2)
			arg_181_2.isSkin = True
			arg_181_2.isTimeLimit = True
			arg_181_2.count = 1

			updateShip(arg_181_1, Ship.New({
				configId = tonumber(arg_181_0.getConfig("ship_group") .. "1"),
				skin_id = arg_181_0.id
			}), arg_181_2),
		[DROP_TYPE_RYZA_DROP] = function(arg_182_0, arg_182_1, arg_182_2)
			AtelierMaterial.UpdateRyzaItem(arg_182_1, arg_182_0.item, arg_182_2),
		[DROP_TYPE_WORKBENCH_DROP] = function(arg_183_0, arg_183_1, arg_183_2)
			WorkBenchItem.UpdateDrop(arg_183_1, arg_183_0.item, arg_183_2),
		[DROP_TYPE_FEAST_DROP] = function(arg_184_0, arg_184_1, arg_184_2)
			WorkBenchItem.UpdateDrop(arg_184_1, WorkBenchItem.New({
				configId = arg_184_0.id,
				count = arg_184_0.count
			}), arg_184_2),
		[DROP_TYPE_BUFF] = function(arg_185_0, arg_185_1, arg_185_2)
			updateBuff(arg_185_1, arg_185_0.id, arg_185_2),
		[DROP_TYPE_COMMANDER_CAT] = function(arg_186_0, arg_186_1, arg_186_2)
			updateCommander(arg_186_1, arg_186_0, arg_186_2),
		[DROP_TYPE_DORM3D_FURNITURE] = function(arg_187_0, arg_187_1, arg_187_2)
			updateDorm3dFurniture(arg_187_1, arg_187_0, arg_187_2),
		[DROP_TYPE_DORM3D_GIFT] = function(arg_188_0, arg_188_1, arg_188_2)
			updateDorm3dGift(arg_188_1, arg_188_0, arg_188_2),
		[DROP_TYPE_DORM3D_SKIN] = function(arg_189_0, arg_189_1, arg_189_2)
			updateDorm3dSkin(arg_189_1, arg_189_0, arg_189_2)
	}

	function var_0_0.UpdateDropDefault(arg_190_0, arg_190_1, arg_190_2)
		warning(string.format("without dropType %d in updateDrop", arg_190_0.type))

return var_0_0
