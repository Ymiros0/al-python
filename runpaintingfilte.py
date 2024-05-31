PaintingfilteConst = {}

local var_0_0 = PaintingfilteConst

def var_0_0.GetStandardTimeConfig(arg_1_0):
	local var_1_0 = {}

	local function var_1_1(arg_2_0)
		for iter_2_0, iter_2_1 in ipairs(arg_2_0):
			if type(iter_2_1) == "table" and #iter_2_1 == 2:
				table.insert(var_1_0, iter_2_1)

	local function var_1_2(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0):
			if type(iter_3_1) == "table" and type(iter_3_1[1]) == "string" and type(iter_3_1[2]) == "table":
				var_1_1(iter_3_1)

	if #arg_1_0 == 2 and type(arg_1_0[1][1]) == "string" and type(arg_1_0[2][1]) == "string":
		var_1_2(arg_1_0)
	else
		var_1_1(arg_1_0)

	return var_1_0

def var_0_0.IsTwoTimeCross(arg_4_0, arg_4_1):
	local var_4_0 = pg.TimeMgr.GetInstance()
	local var_4_1 = var_4_0.parseTimeFromConfig(arg_4_0[1])
	local var_4_2 = var_4_0.parseTimeFromConfig(arg_4_0[2])
	local var_4_3 = var_4_0.parseTimeFromConfig(arg_4_1[1])
	local var_4_4 = var_4_0.parseTimeFromConfig(arg_4_1[2])

	if var_4_2 <= var_4_3 or var_4_4 <= var_4_1:
		return False
	else
		return True

def var_0_0.IsActMatchTime(arg_5_0):
	local var_5_0 = pg.activity_template[arg_5_0]
	local var_5_1 = var_5_0.type
	local var_5_2 = var_5_0.time

	if type(var_5_2) == "string" and var_5_2 == "always":
		return True
	elif type(var_5_2) == "table":
		local var_5_3 = var_0_0.GetStandardTimeConfig(var_5_2)
		local var_5_4 = var_0_0.GetfilteTime()

		if var_0_0.IsTwoTimeCross(var_5_4, var_5_3):
			return True

def var_0_0.IsBuildActMatch(arg_6_0):
	if pg.activity_template[arg_6_0].type == 1 or pg.activity_template[arg_6_0].type == 85:
		return (var_0_0.IsActMatchTime(arg_6_0))
	else
		return False

def var_0_0.IsNormalShopMatch(arg_7_0):
	local var_7_0 = pg.shop_template[arg_7_0]
	local var_7_1 = var_7_0.genre
	local var_7_2 = var_7_0.time

	if var_7_1 == "skin_shop":
		if type(var_7_2) == "string" and var_7_2 == "always":
			return True
		elif type(var_7_2) == "table":
			local var_7_3 = var_0_0.GetStandardTimeConfig(var_7_2)
			local var_7_4 = var_0_0.GetfilteTime()

			if var_0_0.IsTwoTimeCross(var_7_4, var_7_3):
				return True

	return False

def var_0_0.IsActShopMatch(arg_8_0):
	local var_8_0 = pg.activity_shop_extra[arg_8_0]
	local var_8_1 = var_8_0.commodity_type
	local var_8_2 = var_8_0.time

	if var_8_1 == DROP_TYPE_SKIN:
		if type(var_8_2) == "string" and var_8_2 == "always":
			return True
		elif type(var_8_2) == "table":
			local var_8_3 = var_0_0.GetStandardTimeConfig(var_8_2)
			local var_8_4 = var_0_0.GetfilteTime()

			if var_0_0.IsTwoTimeCross(var_8_4, var_8_3):
				return True

	return False

def var_0_0.GetfilteTime():
	return pg.painting_filte_config.time

def var_0_0.GetConstPoolIndexList():
	return pg.painting_filte_config.pool_id_list

def var_0_0.IsPoolWeightConfigMatch(arg_11_0, arg_11_1):
	for iter_11_0, iter_11_1 in ipairs(arg_11_1):
		if arg_11_0[iter_11_1] > 0:
			return True

	return False

def var_0_0.GetBuildActIDList():
	local var_12_0 = {}

	for iter_12_0, iter_12_1 in ipairs(pg.activity_template.all):
		if var_0_0.IsBuildActMatch(iter_12_1):
			table.insert(var_12_0, iter_12_1)

	return var_12_0

def var_0_0.GetActPoolIndexList():
	local var_13_0 = {}
	local var_13_1 = var_0_0.GetBuildActIDList()

	for iter_13_0, iter_13_1 in ipairs(var_13_1):
		local var_13_2 = pg.activity_template[iter_13_1].config_id

		if not table.contains(var_13_0, var_13_2):
			table.insert(var_13_0, var_13_2)

	return var_13_0

def var_0_0.GetShipConfigIDListByPoolList(arg_14_0):
	local var_14_0 = {}

	for iter_14_0, iter_14_1 in pairs(pg.ship_data_create):
		local var_14_1 = iter_14_1.weight_group

		if var_0_0.IsPoolWeightConfigMatch(var_14_1, arg_14_0) and not table.contains(var_14_0, iter_14_0):
			table.insert(var_14_0, iter_14_0)

	return var_14_0

def var_0_0.GetActID2MemoryMap():
	local var_15_0 = {}

	for iter_15_0, iter_15_1 in ipairs(pg.memory_group.all):
		local var_15_1 = pg.memory_group[iter_15_1]
		local var_15_2 = var_15_1.link_event
		local var_15_3 = var_15_1.memories

		if var_15_2 and var_15_2 > 0:
			if not var_15_0[var_15_2]:
				var_15_0[var_15_2] = {}

			for iter_15_2, iter_15_3 in ipairs(var_15_3):
				if not table.contains(var_15_0[var_15_2], iter_15_3):
					table.insert(var_15_0[var_15_2], iter_15_3)

	return var_15_0

def var_0_0.GetActPoolShipConfigIDList():
	local var_16_0 = var_0_0.GetActPoolIndexList()

	return var_0_0.GetShipConfigIDListByPoolList(var_16_0)

def var_0_0.GetConstPoolShipConfigIDList():
	local var_17_0 = var_0_0.GetConstPoolIndexList()

	return var_0_0.GetShipConfigIDListByPoolList(var_17_0)

def var_0_0.GetCreateExchangeShipConfigIDList():
	local var_18_0 = {}
	local var_18_1 = {
		10,
		11
	}

	for iter_18_0, iter_18_1 in ipairs(var_18_1):
		local var_18_2 = var_0_0.GetBuildActIDList()

		for iter_18_2, iter_18_3 in ipairs(var_18_2):
			if pg.ship_data_create_exchange[iter_18_3]:
				for iter_18_4, iter_18_5 in ipairs(pg.ship_data_create_exchange[iter_18_3].exchange_ship_id):
					if not table.contains(var_18_0, iter_18_5):
						table.insert(var_18_0, iter_18_5)

	return var_18_0

def var_0_0.GetNPCShipConfigIDList():
	local var_19_0 = {}
	local var_19_1 = pg.activity_const.ACT_NPC_SHIP_ID.act_id

	if var_19_1 and IsNumber(var_19_1) and var_0_0.IsActMatchTime(var_19_1):
		local var_19_2 = pg.activity_template[var_19_1].config_data[1]
		local var_19_3 = pg.task_data_template[var_19_2].award_display[1][2]

		table.insert(var_19_0, var_19_3)

	return var_19_0

def var_0_0.GetSkinIDFromNormalShopID(arg_20_0):
	local var_20_0 = pg.shop_template[arg_20_0].effect_args

	assert(#var_20_0 == 1, "shop_template的effect_args字段,元素个数大于1,ID.", arg_20_0)

	return var_20_0[1]

def var_0_0.GetNormalShopSkinIDList():
	local var_21_0 = {}

	for iter_21_0, iter_21_1 in ipairs(pg.shop_template.get_id_list_by_genre[ShopArgs.SkinShop]):
		if var_0_0.IsNormalShopMatch(iter_21_1):
			local var_21_1 = var_0_0.GetSkinIDFromNormalShopID(iter_21_1)

			if not table.contains(var_21_0, var_21_1):
				table.insert(var_21_0, var_21_1)

	warning("普通商店皮肤个数" .. #var_21_0)

	return var_21_0

def var_0_0.GetSkinIDFromActShopID(arg_22_0):
	return pg.activity_shop_extra[arg_22_0].commodity_id

def var_0_0.GetActShopSkinIDList():
	local var_23_0 = {}

	for iter_23_0, iter_23_1 in ipairs(pg.activity_shop_extra.get_id_list_by_commodity_type[DROP_TYPE_SKIN]):
		if var_0_0.IsActShopMatch(iter_23_1):
			local var_23_1 = var_0_0.GetSkinIDFromActShopID(iter_23_1)

			if not table.contains(var_23_0, var_23_1):
				table.insert(var_23_0, var_23_1)

	warning("活动商店皮肤个数" .. #var_23_0)

	return var_23_0

local function var_0_1(arg_24_0, arg_24_1)
	arg_24_1 = string.lower(arg_24_1)

	local var_24_0 = pg.painting_filte_map[arg_24_1].res_list

	for iter_24_0, iter_24_1 in ipairs(var_24_0):
		if not table.contains(arg_24_0, iter_24_1):
			table.insert(arg_24_0, iter_24_1)

local function var_0_2(arg_25_0, arg_25_1)
	local var_25_0 = ShipGroup.getDefaultSkin(arg_25_1).painting

	var_0_1(arg_25_0, var_25_0)

local function var_0_3(arg_26_0, arg_26_1)
	local var_26_0 = {
		configId = arg_26_1
	}
	local var_26_1 = Ship.getGroupId(var_26_0)

	var_0_2(arg_26_0, var_26_1)

local function var_0_4(arg_27_0, arg_27_1)
	local var_27_0 = pg.ship_skin_template[arg_27_1].painting

	var_0_1(arg_27_0, var_27_0)

def SpecialFilteForChange():
	local var_28_0 = {}

	local function var_28_1(arg_29_0)
		for iter_29_0, iter_29_1 in ipairs(arg_29_0):
			var_0_3(var_28_0, iter_29_1)

	local function var_28_2(arg_30_0)
		for iter_30_0, iter_30_1 in ipairs(arg_30_0):
			var_0_4(var_28_0, iter_30_1)

	if pg.painting_filte_config.current_act_pool == 1:
		local var_28_3 = PaintingfilteConst.GetActPoolShipConfigIDList()

		var_28_1(var_28_3)

	local var_28_4 = PaintingfilteConst.GetConstPoolShipConfigIDList()

	var_28_1(var_28_4)

	local var_28_5 = PaintingfilteConst.GetNPCShipConfigIDList()

	var_28_1(var_28_5)

	local var_28_6 = PaintingfilteConst.GetCreateExchangeShipConfigIDList()

	var_28_1(var_28_6)

	if pg.painting_filte_config.current_sale_skin == 1:
		local var_28_7 = PaintingfilteConst.GetNormalShopSkinIDList()

		warning("normalShopSkinIDList." .. #var_28_7)
		var_28_2(var_28_7)

		local var_28_8 = PaintingfilteConst.GetActShopSkinIDList()

		warning("actShopSkinIDList." .. #var_28_8)
		var_28_2(var_28_8)

	for iter_28_0, iter_28_1 in ipairs(pg.secretary_special_ship.all):
		local var_28_9 = pg.secretary_special_ship[iter_28_1].prefab

		var_0_1(var_28_0, var_28_9)

	return table.concat(var_28_0, ";")

def SpecialFilteForConst():
	local var_31_0 = {}

	local function var_31_1(arg_32_0)
		for iter_32_0, iter_32_1 in ipairs(arg_32_0):
			var_0_2(var_31_0, iter_32_1)

	local function var_31_2(arg_33_0)
		for iter_33_0, iter_33_1 in ipairs(arg_33_0):
			var_0_4(var_31_0, iter_33_1)

	local var_31_3 = pg.painting_filte_config.skin_id_list

	var_31_2(var_31_3)

	return table.concat(var_31_0, ";")

def SpecialFilterForWorldStory(arg_34_0):
	local var_34_0 = {}

	for iter_34_0 = arg_34_0.Length, 1, -1:
		table.insert(var_34_0, arg_34_0[iter_34_0 - 1])

	return pg.NewStoryMgr.GetInstance().GetStoryPaintingsByNameList(var_34_0)

def SpecialFilteForActStory():
	local var_35_0 = PaintingfilteConst.GetActID2MemoryMap()
	local var_35_1 = PaintingfilteConst.GetfilteTime()
	local var_35_2 = {}

	for iter_35_0, iter_35_1 in ipairs(pg.activity_template.all):
		if var_35_0[iter_35_1] and PaintingfilteConst.IsActMatchTime(iter_35_1):
			for iter_35_2, iter_35_3 in ipairs(var_35_0[iter_35_1]):
				table.insert(var_35_2, iter_35_3)

	local var_35_3 = {}

	for iter_35_4, iter_35_5 in ipairs(var_35_2):
		local var_35_4 = pg.memory_template[iter_35_5]

		table.insert(var_35_3, var_35_4.story)

	return pg.NewStoryMgr.GetInstance().GetStoryPaintingsByNameList(var_35_3)

PLATFORM_CH = 1
PLATFORM_JP = 2
PLATFORM_KR = 3
PLATFORM_US = 4
PLATFORM_CHT = 5

def SetPlatform(arg_36_0):
	if arg_36_0 == "zh":
		PLATFORM_CODE = PLATFORM_CH
	elif arg_36_0 == "jp":
		PLATFORM_CODE = PLATFORM_JP
	elif arg_36_0 == "us":
		PLATFORM_CODE = PLATFORM_US
	elif arg_36_0 == "tw":
		PLATFORM_CODE = PLATFORM_CHT
	elif arg_36_0 == "kr":
		PLATFORM_CODE = PLATFORM_KR
	else
		return False

	return True

UnGamePlayState = True
