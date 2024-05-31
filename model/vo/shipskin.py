local var_0_0 = class("ShipSkin", import(".BaseVO"))

var_0_0.SKIN_TYPE_DEFAULT = -1
var_0_0.SKIN_TYPE_COMMON_FASHION = 0
var_0_0.SKIN_TYPE_PROPOSE = 1
var_0_0.SKIN_TYPE_REMAKE = 2
var_0_0.SKIN_TYPE_OLD = 3
var_0_0.SKIN_TYPE_NOT_HAVE_HIDE = 4
var_0_0.SKIN_TYPE_SHOW_IN_TIME = 5
var_0_0.WITH_LIVE2D = 1
var_0_0.WITH_BG = 2
var_0_0.WITH_EFFECT = 3
var_0_0.WITH_DYNAMIC_BG = 4
var_0_0.WITH_BGM = 5
var_0_0.WITH_SPINE = 6
var_0_0.WITH_SPINE_PLUS = 7

def var_0_0.Tag2Name(arg_1_0):
	if not var_0_0.Tag2NameTab:
		var_0_0.Tag2NameTab = {
			[var_0_0.WITH_BG] = "bg",
			[var_0_0.WITH_BGM] = "bgm",
			[var_0_0.WITH_DYNAMIC_BG] = "dtbg",
			[var_0_0.WITH_EFFECT] = "effect",
			[var_0_0.WITH_LIVE2D] = "live2d",
			[var_0_0.WITH_SPINE] = "spine",
			[var_0_0.WITH_SPINE_PLUS] = "spine_plus"
		}

	return var_0_0.Tag2NameTab[arg_1_0]

def var_0_0.GetShopTypeIdBySkinId(arg_2_0, arg_2_1):
	local var_2_0 = pg.ship_skin_template.get_id_list_by_shop_type_id

	if arg_2_1[arg_2_0]:
		return arg_2_1[arg_2_0]

	for iter_2_0, iter_2_1 in pairs(var_2_0):
		for iter_2_2, iter_2_3 in ipairs(iter_2_1):
			arg_2_1[iter_2_3] = iter_2_0

			if iter_2_3 == arg_2_0:
				return iter_2_0

local var_0_1 = pg.ship_skin_template.get_id_list_by_ship_group

def var_0_0.GetSkinByType(arg_3_0, arg_3_1):
	local var_3_0 = var_0_1[arg_3_0] or {}

	for iter_3_0, iter_3_1 in ipairs(var_3_0):
		local var_3_1 = pg.ship_skin_template[iter_3_1]

		if var_3_1.skin_type == arg_3_1:
			return var_3_1

def var_0_0.GetAllSkinByGroup(arg_4_0):
	local var_4_0 = {}
	local var_4_1 = var_0_1[arg_4_0] or {}

	for iter_4_0, iter_4_1 in ipairs(var_4_1):
		local var_4_2 = pg.ship_skin_template[iter_4_1]

		if var_4_2.no_showing != "1":
			table.insert(var_4_0, var_4_2)

	return var_4_0

def var_0_0.GetShareSkinsByGroupId(arg_5_0):
	local function var_5_0(arg_6_0)
		local var_6_0 = arg_6_0.getConfig("skin_type")

		return not (var_6_0 == var_0_0.SKIN_TYPE_DEFAULT or var_6_0 == var_0_0.SKIN_TYPE_REMAKE or var_6_0 == var_0_0.SKIN_TYPE_OLD)

	local var_5_1 = pg.ship_data_group.get_id_list_by_group_type[arg_5_0][1]
	local var_5_2 = pg.ship_data_group[var_5_1]

	if not var_5_2.share_group_id or #var_5_2.share_group_id <= 0:
		return {}

	local var_5_3 = {}

	for iter_5_0, iter_5_1 in ipairs(var_5_2.share_group_id):
		local var_5_4 = pg.ship_skin_template.get_id_list_by_ship_group[iter_5_1]

		for iter_5_2, iter_5_3 in ipairs(var_5_4):
			local var_5_5 = ShipSkin.New({
				id = iter_5_3
			})

			if var_5_0(var_5_5):
				table.insert(var_5_3, var_5_5)

	return var_5_3

def var_0_0.Ctor(arg_7_0, arg_7_1):
	arg_7_0.id = arg_7_1.id
	arg_7_0.configId = arg_7_1.id
	arg_7_0.endTime = arg_7_1.end_time or arg_7_1.time or 0
	arg_7_0.isNew = True

	local var_7_0 = arg_7_0.getConfig("ship_group")
	local var_7_1 = ShipGroup.getDefaultShipConfig(var_7_0)

	arg_7_0.shipName = var_7_1 and var_7_1.name or ""
	arg_7_0.skinName = arg_7_0.getConfig("name")

def var_0_0.HasNewFlag(arg_8_0):
	return arg_8_0.isNew

def var_0_0.SetIsNew(arg_9_0, arg_9_1):
	arg_9_0.isNew = arg_9_1

def var_0_0.bindConfigTable(arg_10_0):
	return pg.ship_skin_template

def var_0_0.isExpireType(arg_11_0):
	return arg_11_0.endTime > 0

def var_0_0.getExpireTime(arg_12_0):
	return arg_12_0.endTime

def var_0_0.isExpired(arg_13_0):
	return pg.TimeMgr.GetInstance().GetServerTime() >= arg_13_0.endTime

def var_0_0.getRemainTime(arg_14_0):
	return arg_14_0.getExpireTime() - pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.getIcon(arg_15_0):
	return arg_15_0.getConfig("painting")

def var_0_0.InShowTime(arg_16_0):
	return getProxy(ShipSkinProxy).InShowTime(arg_16_0.id)

def var_0_0.IsDefault(arg_17_0):
	return arg_17_0.getConfig("skin_type") == var_0_0.SKIN_TYPE_DEFAULT

def var_0_0.IsType(arg_18_0, arg_18_1):
	return arg_18_0.getConfig("shop_type_id") == arg_18_1

def var_0_0.IsMatchKey(arg_19_0, arg_19_1):
	if not arg_19_1 or arg_19_1 == "":
		return True

	arg_19_1 = string.lower(string.gsub(arg_19_1, "%.", "%%."))
	arg_19_1 = string.lower(string.gsub(arg_19_1, "%-", "%%-"))

	return string.find(string.lower(arg_19_0.shipName), arg_19_1) or string.find(string.lower(arg_19_0.skinName), arg_19_1)

def var_0_0.ToShip(arg_20_0):
	local var_20_0 = arg_20_0.getConfig("ship_group")
	local var_20_1 = ShipGroup.getDefaultShipConfig(var_20_0)

	if var_20_1:
		return Ship.New({
			id = 1,
			intimacy = 10000,
			template_id = var_20_1.id,
			skin_id = arg_20_0.id
		})
	else
		return None

def var_0_0.GetDefaultShipConfig(arg_21_0):
	local var_21_0 = arg_21_0.getConfig("ship_group")

	return (ShipGroup.getDefaultShipConfig(var_21_0))

def var_0_0.IsLive2d(arg_22_0):
	if not arg_22_0.isLive2dTag:
		arg_22_0.isLive2dTag = table.contains(arg_22_0.getConfig("tag"), var_0_0.WITH_LIVE2D)

	return arg_22_0.isLive2dTag

def var_0_0.IsDbg(arg_23_0):
	if not arg_23_0.isDGBTag:
		arg_23_0.isDGBTag = table.contains(arg_23_0.getConfig("tag"), var_0_0.WITH_DYNAMIC_BG)

	return arg_23_0.isDGBTag

def var_0_0.IsBG(arg_24_0):
	if not arg_24_0.isBGTag:
		arg_24_0.isBGTag = table.contains(arg_24_0.getConfig("tag"), var_0_0.WITH_BG)

	return arg_24_0.isBGTag

def var_0_0.IsEffect(arg_25_0):
	if not arg_25_0.isEffectTag:
		arg_25_0.isEffectTag = table.contains(arg_25_0.getConfig("tag"), var_0_0.WITH_EFFECT)

	return arg_25_0.isEffectTag

def var_0_0.isBgm(arg_26_0):
	if not arg_26_0.isBgmTag:
		arg_26_0.isBgmTag = table.contains(arg_26_0.getConfig("tag"), var_0_0.WITH_BGM)

	return arg_26_0.isBgmTag

def var_0_0.IsSpine(arg_27_0):
	if not arg_27_0.isSpine:
		arg_27_0.isSpine = table.contains(arg_27_0.getConfig("tag"), var_0_0.WITH_SPINE)

	return arg_27_0.isSpine

def var_0_0.CantUse(arg_28_0):
	local var_28_0 = arg_28_0.IsTransSkin()
	local var_28_1 = arg_28_0.IsProposeSkin()
	local var_28_2 = arg_28_0.getConfig("ship_group")
	local var_28_3 = getProxy(BayProxy)._ExistGroupShip(var_28_2, var_28_0, var_28_1)
	local var_28_4 = getProxy(CollectionProxy).shipGroups[var_28_2] == None

	return not var_28_3 or var_28_4

def var_0_0.OwnShip(arg_29_0):
	local var_29_0 = arg_29_0.IsTransSkin()
	local var_29_1 = arg_29_0.IsProposeSkin()
	local var_29_2 = arg_29_0.getConfig("ship_group")

	return (getProxy(BayProxy)._ExistGroupShip(var_29_2, var_29_0, var_29_1))

def var_0_0.WithoutUse(arg_30_0):
	local var_30_0 = arg_30_0.getConfig("ship_group")
	local var_30_1 = getProxy(BayProxy).findShipsByGroup(var_30_0)
	local var_30_2 = _.all(var_30_1, function(arg_31_0)
		return arg_31_0.skinId != arg_30_0.id)

	return #var_30_1 > 0 and var_30_2

def var_0_0.ExistShip(arg_32_0):
	local var_32_0 = arg_32_0.getConfig("ship_group")

	return pg.ship_data_statistics[tonumber(var_32_0 .. 1)] != None

def var_0_0.IsTransSkin(arg_33_0):
	return arg_33_0.getConfig("skin_type") == var_0_0.SKIN_TYPE_REMAKE

def var_0_0.IsProposeSkin(arg_34_0):
	return arg_34_0.getConfig("skin_type") == var_0_0.SKIN_TYPE_PROPOSE

def var_0_0.CanShare(arg_35_0):
	local var_35_0 = getProxy(ShipSkinProxy).hasSkin(arg_35_0.configId)

	local function var_35_1()
		if var_35_0:
			return True

		return arg_35_0.InShowTime()

	local function var_35_2()
		local var_37_0 = arg_35_0.getConfig("ship_group")
		local var_37_1 = getProxy(BayProxy).getRawData()

		for iter_37_0, iter_37_1 in pairs(var_37_1):
			if iter_37_1.groupId == var_37_0 and iter_37_1.propose:
				return True

		return False

	local var_35_3 = arg_35_0.getConfig("skin_type")

	return not (var_35_3 == var_0_0.SKIN_TYPE_DEFAULT or var_35_3 == var_0_0.SKIN_TYPE_REMAKE or var_35_3 == var_0_0.SKIN_TYPE_OLD or var_35_3 == var_0_0.SKIN_TYPE_NOT_HAVE_HIDE and not var_35_0 or var_35_3 == var_0_0.SKIN_TYPE_SHOW_IN_TIME and not var_35_1())

def var_0_0.IsShareSkin(arg_38_0, arg_38_1):
	local var_38_0 = pg.ship_skin_template[arg_38_1]
	local var_38_1 = pg.ship_data_group
	local var_38_2 = var_38_1[var_38_1.get_id_list_by_group_type[arg_38_0.groupId][1]].share_group_id

	return table.contains(var_38_2, var_38_0.ship_group)

def var_0_0.CanUseShareSkinForShip(arg_39_0, arg_39_1):
	local var_39_0 = var_0_0.IsShareSkin(arg_39_0, arg_39_1)
	local var_39_1 = ShipSkin.New({
		id = arg_39_1
	})
	local var_39_2 = False
	local var_39_3 = var_39_1.CanShare()
	local var_39_4 = var_39_1.IsProposeSkin()

	if var_39_3 and var_39_4 and arg_39_0.propose:
		var_39_2 = True
	elif var_39_3 and not var_39_4:
		var_39_2 = math.floor(arg_39_0.getIntimacy() / 100) >= arg_39_0.GetNoProposeIntimacyMax()

	return var_39_0 and var_39_2

def var_0_0.ExistReward(arg_40_0):
	local var_40_0 = pg.ship_skin_reward[arg_40_0.configId]

	return var_40_0 != None and #var_40_0.reward > 0

def var_0_0.GetRewardList(arg_41_0):
	if not arg_41_0.ExistReward():
		return {}

	local var_41_0 = pg.ship_skin_reward[arg_41_0.configId]
	local var_41_1 = {}

	for iter_41_0, iter_41_1 in pairs(var_41_0.reward):
		table.insert(var_41_1, {
			type = iter_41_1[1],
			id = iter_41_1[2],
			count = iter_41_1[3]
		})

	return var_41_1

def var_0_0.GetRewardListDesc(arg_42_0):
	local var_42_0 = arg_42_0.GetRewardList()

	if #var_42_0 <= 0:
		return ""

	local var_42_1 = _.map(var_42_0, function(arg_43_0)
		return {
			arg_43_0.type,
			arg_43_0.id,
			arg_43_0.count
		})

	return getDropInfo(var_42_1)

return var_0_0
