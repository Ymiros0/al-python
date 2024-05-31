local var_0_0 = class("ShipGroup", import(".BaseVO"))

var_0_0.REQ_INTERVAL = 60

def var_0_0.GetGroupConfig(arg_1_0):
	local var_1_0 = checkExist(pg.ship_data_group.get_id_list_by_group_type[arg_1_0], {
		1
	})

	return var_1_0 and pg.ship_data_group[var_1_0] or None

def var_0_0.getDefaultShipConfig(arg_2_0):
	local var_2_0

	for iter_2_0 = 4, 1, -1:
		var_2_0 = pg.ship_data_statistics[tonumber(arg_2_0 .. iter_2_0)]

		if var_2_0:
			break

	return var_2_0

def var_0_0.getDefaultShipNameByGroupID(arg_3_0):
	return var_0_0.getDefaultShipConfig(arg_3_0).name

def var_0_0.IsBluePrintGroup(arg_4_0):
	return tobool(pg.ship_data_blueprint[arg_4_0])

def var_0_0.IsMetaGroup(arg_5_0):
	return tobool(pg.ship_strengthen_meta[arg_5_0])

def var_0_0.IsMotGroup(arg_6_0):
	return var_0_0.getDefaultShipConfig(arg_6_0).nationality == Nation.MOT

var_0_0.STATE_LOCK = 0
var_0_0.STATE_NOTGET = 1
var_0_0.STATE_UNLOCK = 2
var_0_0.ENABLE_SKIP_TO_CHAPTER = True

local var_0_1 = pg.ship_data_group

def var_0_0.getState(arg_7_0, arg_7_1, arg_7_2):
	if var_0_0.ENABLE_SKIP_TO_CHAPTER:
		if arg_7_2 and not arg_7_1:
			return var_0_0.STATE_NOTGET

		if var_0_1[arg_7_0]:
			local var_7_0 = var_0_1[arg_7_0]

			assert(var_7_0.hide, "hide can not be None in code " .. arg_7_0)

			if not var_7_0.hide:
				return var_0_0.STATE_LOCK

			if var_7_0.hide == 1:
				return var_0_0.STATE_LOCK
			elif var_7_0.hide != 0:
				assert(var_7_0.hide == 0 or var_7_0.hide == 1, "hide sign invalid in code " .. arg_7_0)

				return var_0_0.STATE_LOCK

		if arg_7_1:
			return var_0_0.STATE_UNLOCK
		else
			local var_7_1 = var_0_1[arg_7_0]

			if not var_7_1:
				return var_0_0.STATE_LOCK

			assert(var_7_1, "code can not be None" .. arg_7_0)

			local var_7_2 = var_7_1.redirect_id
			local var_7_3 = getProxy(ChapterProxy)
			local var_7_4

			if var_7_2 != 0:
				var_7_4 = var_7_3.getChapterById(var_7_2)

			if var_7_2 == 0 or var_7_4 and var_7_4.isClear():
				return var_0_0.STATE_NOTGET
			else
				return var_0_0.STATE_LOCK
	else
		return arg_7_1 and var_0_0.STATE_UNLOCK or var_0_0.STATE_LOCK

def var_0_0.Ctor(arg_8_0, arg_8_1):
	arg_8_0.id = arg_8_1.id
	arg_8_0.star = arg_8_1.star
	arg_8_0.hearts = arg_8_1.heart_count
	arg_8_0.iheart = (arg_8_1.heart_flag or 0) > 0
	arg_8_0.married = arg_8_1.marry_flag
	arg_8_0.maxIntimacy = arg_8_1.intimacy_max
	arg_8_0.maxLV = arg_8_1.lv_max
	arg_8_0.evaluation = None
	arg_8_0.equipCodes = None
	arg_8_0.lastReqStamp = 0
	arg_8_0.trans = False
	arg_8_0.remoulded = arg_8_1.remoulded

	local var_8_0 = var_0_0.getDefaultShipConfig(arg_8_0.id)

	assert(var_8_0, "can not find ship_data_statistics for group " .. arg_8_0.id)

	arg_8_0.shipConfig = setmetatable({}, {
		def __index:(arg_9_0, arg_9_1)
			return var_8_0[arg_9_1]
	})

	local var_8_1 = var_0_0.GetGroupConfig(arg_8_0.id)

	assert(var_8_1, "can not find ship_data_group for group " .. arg_8_0.id)

	arg_8_0.groupConfig = setmetatable({}, {
		def __index:(arg_10_0, arg_10_1)
			return var_8_1[arg_10_1]
	})

def var_0_0.getName(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_0.shipConfig.name

	if arg_11_1 and arg_11_0.trans:
		local var_11_1 = arg_11_0.groupConfig.trans_skin

		var_11_0 = pg.ship_skin_template[var_11_1].name

	return var_11_0

def var_0_0.getNation(arg_12_0):
	return arg_12_0.shipConfig.nationality

def var_0_0.getRarity(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_0.shipConfig.rarity

	if arg_13_1 and arg_13_0.trans:
		var_13_0 = var_13_0 + 1

	return var_13_0

def var_0_0.getTeamType(arg_14_0):
	return TeamType.GetTeamFromShipType(arg_14_0.getShipType())

def var_0_0.getPainting(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_0.shipConfig.skin_id

	if arg_15_1 and arg_15_0.trans:
		var_15_0 = arg_15_0.groupConfig.trans_skin

	local var_15_1 = pg.ship_skin_template[var_15_0]

	assert(var_15_1, "ship_skin_template not exist. " .. var_15_0)

	return var_15_1.painting

def var_0_0.getShipType(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_0.shipConfig.type

	if arg_16_1 and arg_16_0.trans:
		local var_16_1 = Ship.getTransformShipId(arg_16_0.shipConfig.id)

		if var_16_1:
			var_16_0 = pg.ship_data_statistics[var_16_1].type

	return var_16_0

def var_0_0.getShipConfigId(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_0.shipConfig.id

	if arg_17_1 and arg_17_0.trans:
		local var_17_1 = Ship.getTransformShipId(arg_17_0.shipConfig.id)

		if var_17_1:
			var_17_0 = pg.ship_data_statistics[var_17_1].id

	return var_17_0

def var_0_0.getSkinList(arg_18_0):
	return ShipSkin.GetAllSkinByGroup(arg_18_0)

def var_0_0.getDisplayableSkinList(arg_19_0):
	local var_19_0 = {}

	local function var_19_1(arg_20_0)
		return arg_20_0.skin_type == ShipSkin.SKIN_TYPE_OLD or arg_20_0.skin_type == ShipSkin.SKIN_TYPE_NOT_HAVE_HIDE and not getProxy(ShipSkinProxy).hasSkin(arg_20_0.id)

	local function var_19_2(arg_21_0)
		return getProxy(ShipSkinProxy).InShowTime(arg_21_0)

	for iter_19_0, iter_19_1 in ipairs(pg.ship_skin_template.all):
		local var_19_3 = pg.ship_skin_template[iter_19_1]

		if var_19_3.ship_group == arg_19_0.id and var_19_3.no_showing != "1" and not var_19_1(var_19_3) and var_19_2(var_19_3.id):
			table.insert(var_19_0, var_19_3)

	return var_19_0

def var_0_0.getDefaultSkin(arg_22_0):
	return ShipSkin.GetSkinByType(arg_22_0, ShipSkin.SKIN_TYPE_DEFAULT)

def var_0_0.getProposeSkin(arg_23_0):
	return ShipSkin.GetSkinByType(arg_23_0, ShipSkin.SKIN_TYPE_PROPOSE)

def var_0_0.getModSkin(arg_24_0):
	local var_24_0 = pg.ship_data_trans[arg_24_0]

	if var_24_0:
		return pg.ship_skin_template[var_24_0.skin_id]

	return None

def var_0_0.GetSkin(arg_25_0, arg_25_1):
	if not arg_25_1:
		return var_0_0.getDefaultSkin(arg_25_0.id)
	else
		return var_0_0.getModSkin(arg_25_0.id)

def var_0_0.updateMaxIntimacy(arg_26_0, arg_26_1):
	arg_26_0.maxIntimacy = math.max(arg_26_1, arg_26_0.maxIntimacy)

def var_0_0.updateMarriedFlag(arg_27_0):
	arg_27_0.married = 1

def var_0_0.isBluePrintGroup(arg_28_0):
	return var_0_0.IsBluePrintGroup(arg_28_0.id)

def var_0_0.getBluePrintChangeSkillList(arg_29_0):
	assert(arg_29_0.isBluePrintGroup(), "ShipGroup " .. arg_29_0.id .. "isn't BluePrint")

	return pg.ship_data_blueprint[arg_29_0.id].change_skill

def var_0_0.GetNationTxt(arg_30_0):
	local var_30_0 = arg_30_0.shipConfig.nationality

	return Nation.Nation2facionName(var_30_0) .. "-" .. Nation.Nation2Name(var_30_0)

var_0_0.CONDITION_FORBIDDEN = -1
var_0_0.CONDITION_CLEAR = 0
var_0_0.CONDITION_INTIMACY = 1
var_0_0.CONDITION_MARRIED = 2

def var_0_0.VoiceReplayCodition(arg_31_0, arg_31_1):
	local var_31_0 = True
	local var_31_1 = ""

	if arg_31_0.isBluePrintGroup():
		local var_31_2 = getProxy(TechnologyProxy).getBluePrintById(arg_31_0.id)

		assert(var_31_2, "blueprint can not be None >>" .. arg_31_0.id)

		local var_31_3 = var_31_2.getUnlockVoices()

		if not table.contains(var_31_3, arg_31_1.key):
			local var_31_4 = var_31_2.getUnlockLevel(arg_31_1.key)

			if var_31_4 > 0:
				var_31_0 = False

				return var_31_0, i18n("ship_profile_voice_locked_design", var_31_4)

	if arg_31_0.isMetaGroup():
		local var_31_5 = getProxy(BayProxy).getMetaShipByGroupId(arg_31_0.id).getMetaCharacter()
		local var_31_6 = var_31_5.getUnlockedVoiceList()

		if not table.contains(var_31_6, arg_31_1.key):
			local var_31_7 = var_31_5.getUnlockVoiceRepairPercent(arg_31_1.key)

			if var_31_7 > 0:
				var_31_0 = False

				return var_31_0, i18n("ship_profile_voice_locked_meta", var_31_7)

	if arg_31_1.unlock_condition[1] == var_0_0.CONDITION_INTIMACY:
		if arg_31_0.maxIntimacy < arg_31_1.unlock_condition[2]:
			var_31_0 = False
			var_31_1 = i18n("ship_profile_voice_locked_intimacy", math.floor(arg_31_1.unlock_condition[2] / 100))
	elif arg_31_1.unlock_condition[1] == var_0_0.CONDITION_MARRIED and arg_31_0.married == 0:
		var_31_0 = False

		if arg_31_0.IsXIdol():
			var_31_1 = i18n("ship_profile_voice_locked_propose_imas")
		else
			var_31_1 = i18n("ship_profile_voice_locked_propose")

	return var_31_0, var_31_1

def var_0_0.GetMaxIntimacy(arg_32_0):
	return arg_32_0.maxIntimacy / 100 + (arg_32_0.married and arg_32_0.married * 1000 or 0)

def var_0_0.isSpecialFilter(arg_33_0):
	for iter_33_0, iter_33_1 in ipairs(arg_33_0.shipConfig.tag_list):
		if iter_33_1 == "special":
			return True

	return False

def var_0_0.getGroupId(arg_34_0):
	return arg_34_0.id

def var_0_0.isRemoulded(arg_35_0):
	return arg_35_0.remoulded

def var_0_0.isMetaGroup(arg_36_0):
	return var_0_0.IsMetaGroup(arg_36_0.id)

local var_0_2 = {
	feeling2 = True,
	feeling3 = True,
	feeling5 = True,
	feeling4 = True,
	propose = True,
	feeling1 = True
}

def var_0_0.getIntimacyName(arg_37_0, arg_37_1):
	if not var_0_2[arg_37_1]:
		return

	if arg_37_0.isMetaGroup():
		return i18n("meta_voice_name_" .. arg_37_1)
	elif arg_37_0.IsXIdol():
		return i18n("idolmaster_voice_name_" .. arg_37_1)

def var_0_0.getProposeType(arg_38_0):
	if arg_38_0.isMetaGroup():
		return "meta"
	elif arg_38_0.IsXIdol():
		return "imas"
	else
		return "default"

def var_0_0.IsXIdol(arg_39_0):
	return arg_39_0.getNation() == Nation.IDOL_LINK

def var_0_0.CanUseShareSkin(arg_40_0):
	return arg_40_0.groupConfig.share_group_id and #arg_40_0.groupConfig.share_group_id > 0

def var_0_0.rarity2bgPrint(arg_41_0, arg_41_1):
	return shipRarity2bgPrint(arg_41_0.getRarity(arg_41_1), arg_41_0.isBluePrintGroup(), arg_41_0.isMetaGroup())

def var_0_0.rarity2bgPrintForGet(arg_42_0, arg_42_1, arg_42_2):
	return skinId2bgPrint(arg_42_2 or arg_42_0.GetSkin(arg_42_1).id) or arg_42_0.rarity2bgPrint(arg_42_1)

def var_0_0.setEquipCodes(arg_43_0, arg_43_1):
	arg_43_0.equipCodes = arg_43_1

def var_0_0.getEquipCodes(arg_44_0):
	return arg_44_0.equipCodes

return var_0_0
