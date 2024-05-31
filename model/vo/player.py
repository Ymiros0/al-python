local var_0_0 = class("Player", import(".PlayerAttire"))
local var_0_1 = pg.player_resource
local var_0_2 = var_0_1.get_id_list_by_name
local var_0_3
local var_0_4

var_0_0.MAX_SHIP_BAG = 4000
var_0_0.MAX_EQUIP_BAG = 2000
var_0_0.MAX_COMMANDER_BAG = 200
var_0_0.ASSISTS_TYPE_SHAM = 0
var_0_0.ASSISTS_TYPE_GUILD = 1
var_0_0.CHANGE_NAME_KEY = 1

def id2res(arg_1_0):
	return var_0_1[arg_1_0].name

def res2id(arg_2_0):
	return var_0_1.get_id_list_by_name[arg_2_0][1]

def id2ItemId(arg_3_0):
	return var_0_1[arg_3_0].itemid

def itemId2Id(arg_4_0):
	assert(False)

def var_0_0.isMetaShipNeedToTrans(arg_5_0):
	local var_5_0 = MetaCharacterConst.GetMetaShipGroupIDByConfigID(arg_5_0)

	return getProxy(BayProxy).getMetaShipByGroupId(var_5_0) and True or False

def var_0_0.metaShip2Res(arg_6_0):
	local var_6_0 = MetaCharacterConst.GetMetaShipGroupIDByConfigID(arg_6_0)
	local var_6_1 = getProxy(BayProxy).getMetaShipByGroupId(var_6_0).getMetaCharacter().getSpecialMaterialInfoToMaxStar()
	local var_6_2 = var_6_1.itemID
	local var_6_3 = var_6_1.count <= getProxy(BagProxy).getItemCountById(var_6_2)
	local var_6_4

	if var_6_3:
		var_6_4 = pg.ship_transform[var_6_0].common_item
	else
		var_6_4 = pg.ship_transform[var_6_0].exclusive_item

	local var_6_5 = {}

	for iter_6_0, iter_6_1 in ipairs(var_6_4):
		local var_6_6 = {
			type = iter_6_1[1],
			id = iter_6_1[2],
			count = iter_6_1[3]
		}

		table.insert(var_6_5, var_6_6)

	return var_6_5

def var_0_0.getSkinTicket(arg_7_0):
	local var_7_0 = pg.gameset.skin_ticket.key_value

	return var_7_0 == 0 and 0 or arg_7_0.getResource(var_7_0)

def var_0_0.Ctor(arg_8_0, arg_8_1):
	var_0_0.super.Ctor(arg_8_0, arg_8_1)

	local var_8_0 = arg_8_0.character

	arg_8_0.educateCharacter = arg_8_1.child_display or 0

	if var_8_0:
		if type(var_8_0) == "number":
			arg_8_0.character = var_8_0
			arg_8_0.characters = {
				var_8_0
			}
		else
			arg_8_0.character = var_8_0[1]
			arg_8_0.characters = var_8_0

	arg_8_0.id = arg_8_1.id
	arg_8_0.name = arg_8_1.name
	arg_8_0.level = arg_8_1.level or arg_8_1.lv
	arg_8_0.configId = arg_8_0.level
	arg_8_0.exp = arg_8_1.exp or 0
	arg_8_0.attackCount = arg_8_1.attack_count or 0
	arg_8_0.winCount = arg_8_1.win_count or 0
	arg_8_0.manifesto = arg_8_1.adv or arg_8_1.manifesto
	arg_8_0.shipBagMax = arg_8_1.ship_bag_max
	arg_8_0.equipBagMax = arg_8_1.equip_bag_max
	arg_8_0.buff_list = arg_8_1.buffList or {}
	arg_8_0.rank = arg_8_1.rank or arg_8_1.title or 0
	arg_8_0.pvp_attack_count = arg_8_1.pvp_attack_count or 0
	arg_8_0.pvp_win_count = arg_8_1.pvp_win_count or 0
	arg_8_0.collect_attack_count = arg_8_1.collect_attack_count or 0
	arg_8_0.guideIndex = arg_8_1.guide_index
	arg_8_0.buyOilCount = arg_8_1.buy_oil_count
	arg_8_0.chatRoomId = arg_8_1.chat_room_id or 1
	arg_8_0.score = arg_8_1.score or 0
	arg_8_0.guildWaitTime = arg_8_1.guild_wait_time or 0
	arg_8_0.commanderBagMax = arg_8_1.commander_bag_max
	arg_8_0.displayTrophyList = arg_8_1.medal_id or {}
	arg_8_0.banBackyardUploadTime = arg_8_1.theme_upload_not_allowed_time or 0
	arg_8_0.rmb = arg_8_1.rmb or 0
	arg_8_0.identityFlag = arg_8_1.gm_flag
	arg_8_0.mailStoreLevel = arg_8_1.mail_storeroom_lv

	local var_8_1 = getProxy(AppreciateProxy)

	if arg_8_1.appreciation:
		for iter_8_0, iter_8_1 in ipairs(arg_8_1.appreciation.gallerys or {}):
			var_8_1.addPicIDToUnlockList(iter_8_1)

		for iter_8_2, iter_8_3 in ipairs(arg_8_1.appreciation.musics or {}):
			var_8_1.addMusicIDToUnlockList(iter_8_3)

		for iter_8_4, iter_8_5 in ipairs(arg_8_1.appreciation.favor_gallerys or {}):
			var_8_1.addPicIDToLikeList(iter_8_5)

		for iter_8_6, iter_8_7 in ipairs(arg_8_1.appreciation.favor_musics or {}):
			var_8_1.addMusicIDToLikeList(iter_8_7)

		local var_8_2 = getProxy(AppreciateProxy)
		local var_8_3 = var_8_2.getResultForVer()

		if var_8_3:
			pg.ConnectionMgr.GetInstance().Send(15300, {
				type = 0,
				ver_str = var_8_3
			})
			var_8_2.clearVer()

	if arg_8_1.cartoon_read_mark:
		var_8_1.initMangaReadIDList(arg_8_1.cartoon_read_mark)

	if arg_8_1.cartoon_collect_mark:
		var_8_1.initMangaLikeIDList(arg_8_1.cartoon_collect_mark)

	arg_8_0.cdList = {}

	for iter_8_8, iter_8_9 in ipairs(arg_8_1.cd_list or {}):
		arg_8_0.cdList[iter_8_9.key] = iter_8_9.timestamp

	arg_8_0.commonFlagList = {}

	for iter_8_10, iter_8_11 in ipairs(arg_8_1.flag_list or {}):
		arg_8_0.commonFlagList[iter_8_11] = True

	arg_8_0.registerTime = arg_8_1.register_time
	arg_8_0.vipCards = {}

	for iter_8_12, iter_8_13 in ipairs(arg_8_1.card_list or {}):
		local var_8_4 = VipCard.New(iter_8_13)

		arg_8_0.vipCards[var_8_4.id] = var_8_4

	arg_8_0.updateResources(arg_8_1.resource_list)

	arg_8_0.maxRank = arg_8_1.max_rank or 0
	arg_8_0.shipCount = arg_8_1.ship_count or 0
	arg_8_0.chargeExp = arg_8_1.acc_pay_lv or 0
	arg_8_0.mingshiflag = 0
	arg_8_0.mingshiCount = 0
	arg_8_0.chatMsgBanTime = arg_8_1.chat_msg_ban_time or 0
	arg_8_0.randomShipMode = arg_8_1.random_ship_mode or 0
	arg_8_0.customRandomShips = {}

	for iter_8_14, iter_8_15 in ipairs(arg_8_1.random_ship_list or {}):
		table.insert(arg_8_0.customRandomShips, iter_8_15)

	arg_8_0.buildShipNotification = {}

	for iter_8_16, iter_8_17 in ipairs(arg_8_1.taking_ship_list or {}):
		table.insert(arg_8_0.buildShipNotification, {
			uid = iter_8_17.uid,
			new = iter_8_17.isnew == 1
		})

	arg_8_0.proposeShipId = arg_8_1.marry_ship
	arg_8_0.unlockCryptolaliaList = {}

	for iter_8_18, iter_8_19 in ipairs(arg_8_1.soundstory or {}):
		table.insert(arg_8_0.unlockCryptolaliaList, iter_8_19)

	arg_8_0.displayInfo = arg_8_1.display or {}
	arg_8_0.attireInfo = {}
	arg_8_0.attireInfo[AttireConst.TYPE_ICON_FRAME] = arg_8_0.iconFrame
	arg_8_0.attireInfo[AttireConst.TYPE_CHAT_FRAME] = arg_8_0.chatFrame

def var_0_0.updateAttireFrame(arg_9_0, arg_9_1, arg_9_2):
	arg_9_0.attireInfo[arg_9_1] = arg_9_2

def var_0_0.getAttireByType(arg_10_0, arg_10_1):
	return arg_10_0.attireInfo[arg_10_1]

def var_0_0.getRandomSecretary(arg_11_0):
	return arg_11_0.characters[math.random(#arg_11_0.characters)]

def var_0_0.canModifyName(arg_12_0):
	local var_12_0 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_12_1 = pg.gameset.player_name_change_lv_limit.key_value

	if var_12_1 > arg_12_0.level:
		return False, i18n("player_name_change_time_lv_tip", var_12_1)

	local var_12_2 = arg_12_0.getModifyNameTimestamp()

	if var_12_0 < var_12_2:
		local var_12_3, var_12_4, var_12_5, var_12_6 = pg.TimeMgr.GetInstance().parseTimeFrom(var_12_2 - var_12_0)
		local var_12_7

		if var_12_3 == 0:
			if var_12_4 == 0:
				var_12_7 = math.max(var_12_5, 1) .. i18n("word_minute")
			else
				var_12_7 = var_12_4 .. i18n("word_hour")
		else
			var_12_7 = var_12_3 .. i18n("word_date")

		return False, i18n("player_name_change_time_limit_tip", var_12_7)

	return True

def var_0_0.getModifyNameComsume(arg_13_0):
	return pg.gameset.player_name_change_cost.description

def var_0_0.getModifyNameTimestamp(arg_14_0):
	return arg_14_0.cdList[var_0_0.CHANGE_NAME_KEY] or 0

def var_0_0.updateModifyNameColdTime(arg_15_0, arg_15_1):
	arg_15_0.cdList[var_0_0.CHANGE_NAME_KEY] = arg_15_1

def var_0_0.getMaxGold(arg_16_0):
	return pg.gameset.max_gold.key_value

def var_0_0.getMaxOil(arg_17_0):
	return pg.gameset.max_oil.key_value

def var_0_0.getLevelMaxGold(arg_18_0):
	local var_18_0 = arg_18_0.getConfig("max_gold")
	local var_18_1 = getProxy(GuildProxy).GetAdditionGuild()

	return var_18_1 and var_18_0 + var_18_1.getMaxGoldAddition() or var_18_0

def var_0_0.getLevelMaxOil(arg_19_0):
	local var_19_0 = arg_19_0.getConfig("max_oil")
	local var_19_1 = getProxy(GuildProxy).GetAdditionGuild()

	return var_19_1 and var_19_0 + var_19_1.getMaxOilAddition() or var_19_0

def var_0_0.getResource(arg_20_0, arg_20_1):
	return arg_20_0[id2res(arg_20_1)] or 0

def var_0_0.updateResources(arg_21_0, arg_21_1):
	for iter_21_0, iter_21_1 in pairs(var_0_2):
		assert(#iter_21_1 == 1, "Multiple ID have the same name . " .. iter_21_0)

		local var_21_0 = iter_21_1[1]

		if iter_21_0 == "gem":
			arg_21_0.chargeGem = 0
		elif iter_21_0 == "freeGem":
			arg_21_0.awardGem = 0
		else
			arg_21_0[iter_21_0] = 0

	for iter_21_2, iter_21_3 in ipairs(arg_21_1 or {}):
		local var_21_1 = id2res(iter_21_3.type)

		assert(var_21_1, "resource type erro>>>>>" .. iter_21_3.type)

		if var_21_1 == "gem":
			arg_21_0.chargeGem = iter_21_3.num
		elif var_21_1 == "freeGem":
			arg_21_0.awardGem = iter_21_3.num
		else
			arg_21_0[var_21_1] = iter_21_3.num

def var_0_0.getPainting(arg_22_0):
	local var_22_0 = pg.ship_skin_template[arg_22_0.skinId]

	return var_22_0 and var_22_0.painting or "unknown"

def var_0_0.inGuildCDTime(arg_23_0):
	return arg_23_0.guildWaitTime > 0 and arg_23_0.guildWaitTime > pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.setGuildWaitTime(arg_24_0, arg_24_1):
	arg_24_0.guildWaitTime = arg_24_1

def var_0_0.getChargeLevel(arg_25_0):
	local var_25_0 = pg.pay_level_award
	local var_25_1 = var_25_0.all[1]
	local var_25_2 = var_25_0.all[#var_25_0.all]

	for iter_25_0, iter_25_1 in ipairs(var_25_0.all):
		if arg_25_0.chargeExp >= var_25_0[iter_25_1].exp:
			var_25_1 = math.min(iter_25_1 + 1, var_25_2)

	return var_25_1

def var_0_0.getCardById(arg_26_0, arg_26_1):
	return Clone(arg_26_0.vipCards[arg_26_1])

def var_0_0.addVipCard(arg_27_0, arg_27_1):
	arg_27_0.vipCards[arg_27_1.id] = arg_27_1

def var_0_0.addShipBagCount(arg_28_0, arg_28_1):
	arg_28_0.shipBagMax = arg_28_0.shipBagMax + arg_28_1

def var_0_0.addEquipmentBagCount(arg_29_0, arg_29_1):
	arg_29_0.equipBagMax = arg_29_0.equipBagMax + arg_29_1

def var_0_0.bindConfigTable(arg_30_0):
	return pg.user_level

def var_0_0.updateScoreAndRank(arg_31_0, arg_31_1, arg_31_2):
	arg_31_0.score = arg_31_1
	arg_31_0.rank = arg_31_2

def var_0_0.increasePvpCount(arg_32_0):
	arg_32_0.pvp_attack_count = arg_32_0.pvp_attack_count + 1

def var_0_0.increasePvpWinCount(arg_33_0):
	arg_33_0.pvp_win_count = arg_33_0.pvp_win_count + 1

def var_0_0.isEnough(arg_34_0, arg_34_1):
	for iter_34_0, iter_34_1 in pairs(arg_34_1):
		if arg_34_0[iter_34_0] == None or iter_34_1 > arg_34_0[iter_34_0]:
			return False, iter_34_0

	return True

def var_0_0.increaseBuyOilCount(arg_35_0):
	arg_35_0.buyOilCount = arg_35_0.buyOilCount + 1

def var_0_0.changeChatRoom(arg_36_0, arg_36_1):
	arg_36_0.chatRoomId = arg_36_1

def var_0_0.increaseAttackCount(arg_37_0):
	arg_37_0.attackCount = arg_37_0.attackCount + 1

def var_0_0.increaseAttackWinCount(arg_38_0):
	arg_38_0.winCount = arg_38_0.winCount + 1

def var_0_0.increaseShipCount(arg_39_0, arg_39_1):
	arg_39_0.shipCount = arg_39_0.shipCount + (arg_39_1 and arg_39_1 or 1)

def var_0_0.isFull(arg_40_0):
	for iter_40_0, iter_40_1 in pairs(var_0_2):
		local var_40_0 = pg.user_level["max_" .. iter_40_0]

		if var_40_0 and var_40_0 > arg_40_0[iter_40_0]:
			return False

	return True

def var_0_0.getMaxEquipmentBag(arg_41_0):
	local var_41_0 = arg_41_0.equipBagMax
	local var_41_1 = 0
	local var_41_2 = getProxy(GuildProxy).GetAdditionGuild()

	if var_41_2:
		var_41_1 = var_41_2.getEquipmentBagAddition()

	return var_41_1 + var_41_0

def var_0_0.getMaxShipBag(arg_42_0):
	local var_42_0 = arg_42_0.shipBagMax
	local var_42_1 = 0
	local var_42_2 = getProxy(GuildProxy).GetAdditionGuild()

	if var_42_2:
		var_42_1 = var_42_2.getShipBagAddition()

	return var_42_1 + var_42_0

def var_0_0.getMaxEquipmentBagExcludeGuild(arg_43_0):
	return arg_43_0.equipBagMax

def var_0_0.getMaxShipBagExcludeGuild(arg_44_0):
	return arg_44_0.shipBagMax

def var_0_0.__index(arg_45_0, arg_45_1):
	if arg_45_1 == "gem":
		return arg_45_0.getChargeGem()
	elif arg_45_1 == "freeGem":
		return arg_45_0.getTotalGem()
	elif arg_45_1 == "equipBagMax":
		return arg_45_0.getMaxEquipmentBag()
	elif arg_45_1 == "shipBagMax":
		return arg_45_0.getMaxShipBag()

	local var_45_0 = rawget(arg_45_0, arg_45_1) or var_0_0[arg_45_1]

	var_45_0 = var_45_0 or var_0_0.super[arg_45_1]

	return var_45_0

def var_0_0.__newindex(arg_46_0, arg_46_1, arg_46_2):
	assert(arg_46_1 != "gem" and arg_46_1 != "freeGem", "Do not set gem directly.")
	rawset(arg_46_0, arg_46_1, arg_46_2)

def var_0_0.getFreeGem(arg_47_0):
	return arg_47_0.awardGem

def var_0_0.getChargeGem(arg_48_0):
	return arg_48_0.chargeGem

def var_0_0.getTotalGem(arg_49_0):
	return arg_49_0.getFreeGem() + arg_49_0.getChargeGem()

def var_0_0.getResById(arg_50_0, arg_50_1):
	if arg_50_1 == 4:
		return arg_50_0.getTotalGem()
	else
		return arg_50_0[id2res(arg_50_1)]

def var_0_0.consume(arg_51_0, arg_51_1):
	local var_51_0 = (arg_51_1.freeGem or 0) + (arg_51_1.gem or 0)

	arg_51_1.freeGem = None
	arg_51_1.gem = None

	if var_51_0 > 0:
		local var_51_1 = arg_51_0.getFreeGem()
		local var_51_2 = math.min(var_51_0, var_51_1)

		arg_51_0.awardGem = var_51_1 - var_51_2
		arg_51_0.chargeGem = arg_51_0.chargeGem - (var_51_0 - var_51_2)

	for iter_51_0, iter_51_1 in pairs(arg_51_1):
		arg_51_0[iter_51_0] = arg_51_0[iter_51_0] - iter_51_1

def var_0_0.addResources(arg_52_0, arg_52_1):
	for iter_52_0, iter_52_1 in pairs(arg_52_1):
		if iter_52_0 == "gold":
			local var_52_0 = arg_52_0.getMaxGold()

			arg_52_0[iter_52_0] = math.min(arg_52_0[iter_52_0] + iter_52_1, var_52_0)
		elif iter_52_0 == "oil":
			local var_52_1 = arg_52_0.getMaxOil()

			arg_52_0[iter_52_0] = math.min(arg_52_0[iter_52_0] + iter_52_1, var_52_1)
		elif iter_52_0 == "gem":
			arg_52_0.chargeGem = arg_52_0.getChargeGem() + iter_52_1
		elif iter_52_0 == "freeGem":
			arg_52_0.awardGem = arg_52_0.getFreeGem() + iter_52_1
		elif iter_52_0 == id2res(WorldConst.ResourceID):
			local var_52_2 = pg.gameset.world_resource_max.key_value

			arg_52_0[iter_52_0] = math.min(arg_52_0[iter_52_0] + iter_52_1, var_52_2)
		elif iter_52_0 == "gameticket":
			local var_52_3 = pg.gameset.game_room_remax.key_value

			arg_52_0[iter_52_0] = math.min(arg_52_0[iter_52_0] + iter_52_1, var_52_3)
		else
			arg_52_0[iter_52_0] = arg_52_0[iter_52_0] + iter_52_1

def var_0_0.resetBuyOilCount(arg_53_0):
	arg_53_0.buyOilCount = 0

def var_0_0.addExp(arg_54_0, arg_54_1):
	assert(arg_54_1 >= 0, "exp should greater than zero")

	arg_54_0.exp = arg_54_0.exp + arg_54_1

	while arg_54_0.canLevelUp():
		arg_54_0.exp = arg_54_0.exp - arg_54_0.getLevelExpConfig().exp_interval
		arg_54_0.level = arg_54_0.level + 1

		pg.TrackerMgr.GetInstance().Tracking(TRACKING_USER_LEVELUP, arg_54_0.level)

		if arg_54_0.level == 30:
			pg.TrackerMgr.GetInstance().Tracking(TRACKING_USER_LEVEL_THIRTY)
		elif arg_54_0.level == 40:
			pg.TrackerMgr.GetInstance().Tracking(TRACKING_USER_LEVEL_FORTY)

def var_0_0.addExpToLevel(arg_55_0, arg_55_1):
	local var_55_0 = getConfigFromLevel1(pg.user_level, arg_55_1)
	local var_55_1 = arg_55_0.getLevelExpConfig()

	if var_55_1.exp_start + arg_55_0.exp >= var_55_0.exp_start:
		print("EXP Overflow, Return")

		return

	arg_55_0.addExp(var_55_0.exp_start - var_55_1.exp_start - arg_55_0.exp)

def var_0_0.GetBuffs(arg_56_0):
	return arg_56_0.buff_list

def var_0_0.getLevelExpConfig(arg_57_0):
	return getConfigFromLevel1(pg.user_level, arg_57_0.level)

def var_0_0.getMaxLevel(arg_58_0):
	return pg.user_level.all[#pg.user_level.all]

def var_0_0.getTotalExp(arg_59_0):
	return arg_59_0.getLevelExpConfig().exp_start + arg_59_0.exp

def var_0_0.canLevelUp(arg_60_0):
	local var_60_0 = getConfigFromLevel1(pg.user_level, arg_60_0.level + 1)
	local var_60_1 = arg_60_0.getLevelExpConfig()

	return var_60_0 and var_60_1 != var_60_0 and var_60_1.exp_interval <= arg_60_0.exp

def var_0_0.isSelf(arg_61_0):
	return getProxy(PlayerProxy).isSelf(arg_61_0.id)

def var_0_0.isFriend(arg_62_0):
	return getProxy(FriendProxy).isFriend(arg_62_0.id)

def var_0_0.OilMax(arg_63_0, arg_63_1):
	arg_63_1 = arg_63_1 or 0

	return pg.gameset.max_oil.key_value < arg_63_0.oil + arg_63_1

def var_0_0.GoldMax(arg_64_0, arg_64_1):
	arg_64_1 = arg_64_1 or 0

	return pg.gameset.max_gold.key_value < arg_64_0.gold + arg_64_1

def var_0_0.ResLack(arg_65_0, arg_65_1, arg_65_2):
	local var_65_0 = pg.gameset["max_" .. arg_65_1].key_value

	if var_65_0 < arg_65_0[arg_65_1]:
		return 0
	else
		return math.min(arg_65_2, var_65_0 - arg_65_0[arg_65_1])

def var_0_0.OverStore(arg_66_0, arg_66_1, arg_66_2):
	arg_66_2 = arg_66_2 or 0

	local var_66_0 = id2res(arg_66_1)
	local var_66_1 = pg.mail_storeroom[arg_66_0.mailStoreLevel]
	local var_66_2 = switch(arg_66_1, {
		[PlayerConst.ResStoreGold] = function()
			return var_66_1.gold_store,
		[PlayerConst.ResStoreOil] = function()
			return var_66_1.oil_store
	})

	return arg_66_0[var_66_0] + arg_66_2 - var_66_2

def var_0_0.UpdateCommonFlag(arg_69_0, arg_69_1):
	arg_69_0.commonFlagList[arg_69_1] = True

def var_0_0.GetCommonFlag(arg_70_0, arg_70_1):
	return arg_70_0.commonFlagList[arg_70_1]

def var_0_0.CancelCommonFlag(arg_71_0, arg_71_1):
	arg_71_0.commonFlagList[arg_71_1] = False

def var_0_0.SetCommonFlag(arg_72_0, arg_72_1, arg_72_2):
	arg_72_0.commonFlagList[arg_72_1] = arg_72_2

def var_0_0.updateCommanderBagMax(arg_73_0, arg_73_1):
	arg_73_0.commanderBagMax = arg_73_0.commanderBagMax + arg_73_1

def var_0_0.GetDaysFromRegister(arg_74_0):
	local var_74_0 = pg.TimeMgr.GetInstance().GetServerTime()

	return pg.TimeMgr.GetInstance().DiffDay(arg_74_0.registerTime, var_74_0)

def var_0_0.CanUploadBackYardThemeTemplate(arg_75_0):
	return pg.TimeMgr.GetInstance().GetServerTime() >= arg_75_0.banBackyardUploadTime

def var_0_0.GetBanUploadBackYardThemeTemplateTime(arg_76_0):
	return pg.TimeMgr.GetInstance().STimeDescC(arg_76_0.banBackyardUploadTime or 0)

def var_0_0.CheckIdentityFlag(arg_77_0):
	return arg_77_0.identityFlag == 1

def var_0_0.GetRegisterTime(arg_78_0):
	return arg_78_0.registerTime

def var_0_0.GetFlagShip(arg_79_0):
	local var_79_0 = getProxy(SettingsProxy)
	local var_79_1 = var_79_0.getCurrentSecretaryIndex()
	local var_79_2

	if var_79_0.IsOpenRandomFlagShip():
		var_79_2 = arg_79_0.GetRandomFlagShip(var_79_1)
	else
		var_79_2 = arg_79_0.GetNativeFlagShip(var_79_1)

	return var_79_2

local function var_0_5(arg_80_0)
	local var_80_0 = {}
	local var_80_1 = {}
	local var_80_2 = getProxy(SettingsProxy).GetFlagShipDisplayMode()
	local var_80_3 = getProxy(PlayerProxy).getRawData().ExistEducateChar()

	if var_80_2 == FlAG_SHIP_DISPLAY_ONLY_EDUCATECHAR and not var_80_3:
		var_80_2 = FlAG_SHIP_DISPLAY_ALL

		getProxy(SettingsProxy).SetFlagShipDisplayMode(var_80_2)

	if var_80_2 != FlAG_SHIP_DISPLAY_ONLY_EDUCATECHAR:
		local var_80_4 = getProxy(BayProxy)

		for iter_80_0, iter_80_1 in ipairs(arg_80_0):
			var_80_0[iter_80_0] = defaultValue(var_80_4.RawGetShipById(iter_80_1), False)

			table.insert(var_80_1, iter_80_0)

	if var_80_3 and var_80_2 != FlAG_SHIP_DISPLAY_ONLY_SHIP:
		table.insert(var_80_1, PlayerVitaeShipsPage.EDUCATE_CHAR_SLOT_ID)

		local var_80_5 = getProxy(PlayerProxy).getRawData().GetEducateCharacter()
		local var_80_6 = VirtualEducateCharShip.New(var_80_5)

		var_80_0[PlayerVitaeShipsPage.EDUCATE_CHAR_SLOT_ID] = var_80_6

	return var_80_0, var_80_1

def var_0_0.GetNativeFlagShip(arg_81_0, arg_81_1):
	local var_81_0, var_81_1 = var_0_5(arg_81_0.characters)
	local var_81_2 = getProxy(SettingsProxy)

	if getProxy(PlayerProxy).getFlag("battle"):
		local var_81_3 = math.random(#var_81_1)

		arg_81_1 = var_81_1[var_81_3]

		var_81_2.setCurrentSecretaryIndex(var_81_3)

	local var_81_4 = var_81_0[arg_81_1]

	if not var_81_4:
		local var_81_5 = PlayerVitaeShipsPage.GetSlotIndexList()
		local var_81_6 = table.indexof(var_81_5, arg_81_1)

		if var_81_6 and var_81_6 > 0:
			for iter_81_0 = var_81_6 + 1, #var_81_5:
				arg_81_1 = var_81_5[iter_81_0]
				var_81_4 = var_81_0[arg_81_1]

				if var_81_4:
					var_81_2.setCurrentSecretaryIndex(iter_81_0)

					break

	if not var_81_4:
		arg_81_1 = 1

		var_81_2.setCurrentSecretaryIndex(arg_81_1)

		var_81_4 = var_81_0[arg_81_1]

	return var_81_4

def var_0_0.GetRandomFlagShip(arg_82_0, arg_82_1):
	local var_82_0 = getProxy(SettingsProxy)
	local var_82_1 = var_82_0.GetRandomFlagShipList()
	local var_82_2, var_82_3 = var_0_5(var_82_1)

	if getProxy(PlayerProxy).getFlag("battle"):
		local var_82_4 = math.random(#var_82_3)

		arg_82_1 = var_82_3[var_82_4]

		var_82_0.setCurrentSecretaryIndex(var_82_4)

	local var_82_5 = var_82_2[arg_82_1]

	if not var_82_5:
		local var_82_6 = PlayerVitaeShipsPage.GetSlotIndexList()
		local var_82_7 = table.indexof(var_82_6, arg_82_1)

		if var_82_7 and var_82_7 > 0:
			for iter_82_0 = var_82_7 + 1, #var_82_6:
				arg_82_1 = var_82_6[iter_82_0]
				var_82_5 = var_82_2[arg_82_1]

				if var_82_5:
					var_82_0.setCurrentSecretaryIndex(iter_82_0)

					break

	if not var_82_5:
		local var_82_8 = {}

		for iter_82_1, iter_82_2 in pairs(var_82_2):
			if iter_82_2:
				table.insert(var_82_8, iter_82_1)

		if #var_82_8 > 0:
			arg_82_1 = var_82_8[math.random(1, #var_82_8)]
			var_82_5 = var_82_2[arg_82_1]

			local var_82_9 = table.indexof(var_82_3, arg_82_1)

			if var_82_9:
				var_82_0.setCurrentSecretaryIndex(var_82_9)

	if not var_82_5:
		arg_82_1 = 1

		var_82_0.setCurrentSecretaryIndex(arg_82_1)

		var_82_5 = var_82_2[arg_82_1]

	return var_82_5

def var_0_0.GetNextFlagShip(arg_83_0):
	getProxy(SettingsProxy).rotateCurrentSecretaryIndex()

	return arg_83_0.GetFlagShip()

def var_0_0.IsOpenShipEvaluationImpeach(arg_84_0):
	return not LOCK_IMPEACH and arg_84_0.level >= pg.gameset.report_level_limit.key_value

def var_0_0.ShouldCheckCustomName(arg_85_0):
	return arg_85_0.GetCommonFlag(REVERT_CUSTOM_NAME)

def var_0_0.WhetherServerModifiesName(arg_86_0):
	return arg_86_0.GetCommonFlag(ILLEGALITY_PLAYER_NAME)

def var_0_0.GetManifesto(arg_87_0):
	return arg_87_0.manifesto or ""

def var_0_0.GetName(arg_88_0):
	return arg_88_0.name

def var_0_0.GetRandomFlagShipMode(arg_89_0):
	if arg_89_0.randomShipMode <= 0:
		if arg_89_0.GetCommonFlag(RANDOM_FLAG_SHIP_MODE):
			arg_89_0.randomShipMode = SettingsRandomFlagShipAndSkinPanel.SHIP_LOCKED
		else
			arg_89_0.randomShipMode = SettingsRandomFlagShipAndSkinPanel.SHIP_FREQUENTLYUSED

	return arg_89_0.randomShipMode

def var_0_0.UpdateRandomFlagShipMode(arg_90_0, arg_90_1):
	arg_90_0.randomShipMode = arg_90_1

def var_0_0.GetCustomRandomShipList(arg_91_0):
	local var_91_0 = {}

	for iter_91_0, iter_91_1 in ipairs(arg_91_0.customRandomShips):
		table.insert(var_91_0, iter_91_1)

	return var_91_0

def var_0_0.UpdateCustomRandomShipList(arg_92_0, arg_92_1):
	arg_92_0.customRandomShips = arg_92_1

def var_0_0.SetProposeShipId(arg_93_0, arg_93_1):
	arg_93_0.proposeShipId = arg_93_1

def var_0_0.GetProposeShipId(arg_94_0):
	return arg_94_0.proposeShipId

def var_0_0.GetCryptolaliaList(arg_95_0):
	local var_95_0 = {}
	local var_95_1 = {}
	local var_95_2 = arg_95_0.unlockCryptolaliaList

	for iter_95_0, iter_95_1 in ipairs(var_95_2):
		var_95_1[iter_95_1] = True

	for iter_95_2, iter_95_3 in ipairs(pg.soundstory_template.all):
		local var_95_3 = Cryptolalia.New({
			id = iter_95_3
		})

		if var_95_1[iter_95_3]:
			var_95_3.Unlock()

		table.insert(var_95_0, var_95_3)

	return var_95_0

def var_0_0.UnlockCryptolalia(arg_96_0, arg_96_1):
	if not table.contains(arg_96_0.unlockCryptolaliaList):
		table.insert(arg_96_0.unlockCryptolaliaList, arg_96_1)

def var_0_0.ExistCryptolalia(arg_97_0, arg_97_1):
	local var_97_0 = arg_97_0.GetCryptolaliaList()

	for iter_97_0, iter_97_1 in ipairs(var_97_0):
		if (iter_97_1.InTime() or not iter_97_1.IsLock()) and iter_97_1.IsSameGroup(arg_97_1):
			return True

	return False

def var_0_0.ExistEducateChar(arg_98_0):
	return arg_98_0.educateCharacter > 0

def var_0_0.GetEducateCharacter(arg_99_0):
	return arg_99_0.educateCharacter

def var_0_0.SetEducateCharacter(arg_100_0, arg_100_1):
	arg_100_0.educateCharacter = arg_100_1

def var_0_0.CanGetResource(arg_101_0, arg_101_1):
	local var_101_0 = id2res(arg_101_1)
	local var_101_1

	if arg_101_1 == 1:
		var_101_1 = arg_101_0.getLevelMaxGold()
	elif arg_101_1 == 2:
		var_101_1 = arg_101_0.getLevelMaxOil()
	else
		assert(False)

	if var_101_1 <= arg_101_0[var_101_0]:
		return False

	return True

def var_0_0.GetExtendStoreCost(arg_102_0):
	local var_102_0 = pg.mail_storeroom[arg_102_0.mailStoreLevel]
	local var_102_1 = {}

	if var_102_0.upgrade_gem > 0:
		var_102_1.diamond = Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = PlayerConst.ResDiamond,
			count = var_102_0.upgrade_gem
		})

	if var_102_0.upgrade_gold > 0:
		var_102_1.gold = Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = PlayerConst.ResGold,
			count = var_102_0.upgrade_gold
		})

	return var_102_1.diamond, var_102_1.gold

def var_0_0.IsStoreLevelMax(arg_103_0):
	return not pg.mail_storeroom[arg_103_0.mailStoreLevel + 1]

return var_0_0
