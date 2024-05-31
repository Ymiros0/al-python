local var_0_0 = class("Ship", import(".BaseVO"))

var_0_0.ENERGY_MID = 40
var_0_0.ENERGY_LOW = 0
var_0_0.RECOVER_ENERGY_POINT = 2
var_0_0.INTIMACY_PROPOSE = 6
var_0_0.CONFIG_MAX_STAR = 6
var_0_0.BACKYARD_1F_ENERGY_ADDITION = 2
var_0_0.BACKYARD_2F_ENERGY_ADDITION = 3
var_0_0.PREFERENCE_TAG_NONE = 0
var_0_0.PREFERENCE_TAG_COMMON = 1

local var_0_1 = {
	vanguard = i18n("word_vanguard_fleet"),
	main = i18n("word_main_fleet")
}

var_0_0.CVBattleKey = {
	skill = "skill",
	link2 = "link2",
	lose = "lose",
	link5 = "link5",
	link3 = "link3",
	link6 = "link6",
	hp = "hp",
	link1 = "link1",
	link4 = "link4",
	warcry = "warcry",
	mvp = "mvp"
}
var_0_0.LOCK_STATE_UNLOCK = 0
var_0_0.LOCK_STATE_LOCK = 1
var_0_0.WEAPON_COUNT = 3
var_0_0.PREFAB_EQUIP = 4
var_0_0.MAX_SKILL_LEVEL = 10
var_0_0.ENERGY_RECOVER_TIME = 360
var_0_0.STATE_NORMAL = 1
var_0_0.STATE_REST = 2
var_0_0.STATE_CLASS = 3
var_0_0.STATE_COLLECT = 4
var_0_0.STATE_TRAIN = 5

local var_0_2 = 4
local var_0_3 = 100
local var_0_4 = 120
local var_0_5 = pg.ship_data_strengthen
local var_0_6 = pg.ship_level
local var_0_7 = pg.equip_skin_template
local var_0_8 = pg.ship_data_breakout

function nation2print(arg_1_0)
	return Nation.Nation2Print(arg_1_0)
end

function var_0_0.getRecoverEnergyPoint(arg_2_0)
	return arg_2_0.propose and 3 or 2
end

function shipType2name(arg_3_0)
	return ShipType.Type2Name(arg_3_0)
end

function shipType2print(arg_4_0)
	return ShipType.Type2Print(arg_4_0)
end

function shipType2Battleprint(arg_5_0)
	return ShipType.Type2BattlePrint(arg_5_0)
end

function skinId2bgPrint(arg_6_0)
	local var_6_0 = pg.ship_skin_template[arg_6_0].rarity_bg

	if var_6_0 and var_6_0 ~= "" then
		return var_6_0
	end
end

function var_0_0.rarity2bgPrint(arg_7_0)
	return shipRarity2bgPrint(arg_7_0:getRarity(), arg_7_0:isBluePrintShip(), arg_7_0:isMetaShip())
end

function var_0_0.rarity2bgPrintForGet(arg_8_0)
	return skinId2bgPrint(arg_8_0.skinId) or arg_8_0:rarity2bgPrint()
end

function var_0_0.getShipBgPrint(arg_9_0, arg_9_1)
	local var_9_0 = pg.ship_skin_template[arg_9_0.skinId]

	assert(var_9_0, "ship_skin_template not exist: " .. arg_9_0.skinId)

	local var_9_1

	if not arg_9_1 and var_9_0.bg_sp and var_9_0.bg_sp ~= "" and PlayerPrefs.GetInt("paint_hide_other_obj_" .. var_9_0.painting, 0) == 0 then
		var_9_1 = var_9_0.bg_sp
	end

	return var_9_1 and var_9_1 or var_9_0.bg and #var_9_0.bg > 0 and var_9_0.bg or arg_9_0:rarity2bgPrintForGet()
end

function var_0_0.getStar(arg_10_0)
	return arg_10_0:getConfig("star")
end

function var_0_0.getMaxStar(arg_11_0)
	return pg.ship_data_template[arg_11_0.configId].star_max
end

function var_0_0.getShipArmor(arg_12_0)
	return arg_12_0:getConfig("armor_type")
end

function var_0_0.getShipArmorName(arg_13_0)
	local var_13_0 = arg_13_0:getShipArmor()

	return ArmorType.Type2Name(var_13_0)
end

function var_0_0.getGroupId(arg_14_0)
	return pg.ship_data_template[arg_14_0.configId].group_type
end

function var_0_0.getGroupIdByConfigId(arg_15_0)
	return math.floor(arg_15_0 / 10)
end

function var_0_0.getShipWords(arg_16_0)
	local var_16_0 = pg.ship_skin_words[arg_16_0]

	if not var_16_0 then
		warning("找不到ship_skin_words: " .. arg_16_0)

		return
	end

	local var_16_1 = Clone(var_16_0)

	for iter_16_0, iter_16_1 in pairs(var_16_1) do
		if type(iter_16_1) == "string" then
			var_16_1[iter_16_0] = HXSet.hxLan(iter_16_1)
		end
	end

	local var_16_2 = pg.ship_skin_words_extra[arg_16_0]

	return var_16_1, var_16_2
end

function var_0_0.getMainwordsCount(arg_17_0)
	local var_17_0 = var_0_0.getShipWords(arg_17_0)

	if not var_17_0.main or var_17_0.main == "" then
		var_17_0 = var_0_0.getShipWords(var_0_0.getOriginalSkinId(arg_17_0))
	end

	return #string.split(var_17_0.main, "|")
end

function var_0_0.getWordsEx(arg_18_0, arg_18_1, arg_18_2, arg_18_3, arg_18_4, arg_18_5)
	local var_18_0 = arg_18_0 and arg_18_0[arg_18_1] or nil
	local var_18_1 = false

	if not var_18_0 or var_18_0 == "" then
		if arg_18_0 and arg_18_0.id == arg_18_4 then
			return
		end

		if not arg_18_5 then
			return
		end

		local var_18_2, var_18_3 = var_0_0.getShipWords(arg_18_4)

		if not var_18_3 then
			return
		end

		var_18_0 = var_18_3[arg_18_1]

		if not var_18_0 then
			return
		end

		var_18_1 = true
	end

	if type(var_18_0) == "string" then
		return
	end

	arg_18_3 = arg_18_3 or 0

	for iter_18_0, iter_18_1 in ipairs(var_18_0) do
		if arg_18_3 >= iter_18_1[1] then
			if arg_18_1 == "main" then
				return string.split(iter_18_1[2], "|")[arg_18_2], iter_18_1[1], var_18_1
			else
				return iter_18_1[2], iter_18_1[1], var_18_1
			end
		end
	end
end

function var_0_0.getWords(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4)
	local var_19_0, var_19_1 = var_0_0.getShipWords(arg_19_0)
	local var_19_2 = var_0_0.getOriginalSkinId(arg_19_0)
	local var_19_3 = math.fmod(arg_19_0, var_19_2)

	if not var_19_0 then
		var_19_0, var_19_1 = var_0_0.getShipWords(var_19_2)

		if not var_19_0 then
			return nil
		end
	end

	local var_19_4 = 0
	local var_19_5 = false
	local var_19_6 = var_19_0[arg_19_1]

	if not var_19_6 or var_19_6 == "" then
		var_19_5 = true

		if var_19_0.id == var_19_2 then
			return nil
		else
			var_19_0 = var_0_0.getShipWords(var_19_2)

			if not var_19_0 then
				return nil
			end

			var_19_6 = var_19_0[arg_19_1]

			if not var_19_6 or var_19_6 == "" then
				return nil
			end
		end
	end

	local var_19_7 = string.split(var_19_6, "|")
	local var_19_8 = arg_19_2 or math.random(#var_19_7)

	if arg_19_1 == "main" and var_19_7[var_19_8] == "nil" then
		var_19_5 = true
		var_19_0 = var_0_0.getShipWords(var_19_2)

		if not var_19_0 then
			return nil
		end

		local var_19_9 = var_19_0[arg_19_1]

		if not var_19_9 or var_19_9 == "" then
			return nil
		end

		var_19_7 = string.split(var_19_9, "|")
	end

	rstEx, cvEx, defaultCoverEx = var_0_0.getWordsEx(var_19_1, arg_19_1, var_19_8, arg_19_4, var_19_2, var_19_5)

	local var_19_10
	local var_19_11 = PlayerPrefs.GetInt("CV_LANGUAGE_" .. pg.ship_skin_template[arg_19_0].ship_group) == 2 and var_19_0.voice_key_2 or var_19_0.voice_key

	if var_19_11 == 0 then
		if not var_19_5 or rstEx and not defaultCoverEx then
			var_19_10 = var_0_0.getCVPath(var_19_2, arg_19_1, var_19_8, var_19_3)
		end
	elseif var_19_11 == -2 then
		-- block empty
	else
		var_19_10 = var_0_0.getCVPath(var_19_2, arg_19_1, var_19_8)
	end

	local var_19_12 = var_19_7[var_19_8]

	if var_19_12 and (arg_19_3 == nil and PLATFORM_CODE ~= PLATFORM_US or arg_19_3 == true) then
		var_19_12 = var_19_12:gsub("%s", " ")
	end

	if rstEx then
		var_19_10 = var_19_10 and var_19_10 .. "_ex" .. cvEx
	end

	return rstEx or var_19_12, var_19_10, cvEx
end

function var_0_0.getCVKeyID(arg_20_0)
	local var_20_0 = Ship.getShipWords(arg_20_0)

	if not var_20_0 then
		return -1
	end

	local var_20_1
	local var_20_2 = PlayerPrefs.GetInt("CV_LANGUAGE_" .. pg.ship_skin_template[arg_20_0].ship_group)
	local var_20_3 = var_20_2 == 2 and var_20_0.voice_key_2 >= 0 and var_20_0.voice_key_2 or var_20_0.voice_key

	if var_20_3 == 0 or var_20_3 == -2 then
		local var_20_4 = var_0_0.getOriginalSkinId(arg_20_0)
		local var_20_5 = var_0_0.getShipWords(var_20_4)

		var_20_3 = var_20_2 == 2 and var_20_5.voice_key_2 >= 0 and var_20_5.voice_key_2 or var_20_5.voice_key
	end

	return var_20_3
end

function var_0_0.getCVPath(arg_21_0, arg_21_1, arg_21_2, arg_21_3)
	arg_21_2 = arg_21_2 or 1

	local var_21_0 = Ship.getShipWords(arg_21_0)
	local var_21_1 = var_0_0.getOriginalSkinId(arg_21_0)

	if not var_21_0 then
		var_21_0 = var_0_0.getShipWords(var_21_1)

		if not var_21_0 then
			return
		end
	end

	local var_21_2 = PlayerPrefs.GetInt("CV_LANGUAGE_" .. arg_21_0 / 10)
	local var_21_3 = var_21_0[arg_21_1]

	if arg_21_1 == "main" then
		var_21_3 = string.split(var_21_3, "|")[arg_21_2]
		arg_21_1 = arg_21_1 .. arg_21_2
	end

	if arg_21_1 == "skill" or string.find(arg_21_1, "link") then
		if var_21_0.voice_key == 0 then
			var_21_0 = var_0_0.getShipWords(var_21_1)
		end
	elseif not var_21_3 or var_21_3 == "" or var_21_3 == "nil" then
		var_21_0 = var_0_0.getShipWords(var_21_1)
	end

	local var_21_4
	local var_21_5 = var_21_2 == 2 and var_21_0.voice_key_2 or var_21_0.voice_key

	if var_21_5 ~= -1 and pg.character_voice[arg_21_1] then
		var_21_4 = pg.character_voice[arg_21_1].resource_key

		if var_21_4 then
			var_21_4 = "event:/cv/" .. var_21_5 .. "/" .. var_21_4

			if arg_21_3 then
				var_21_4 = var_21_4 .. "_" .. arg_21_3
			end
		end
	end

	return var_21_4
end

function var_0_0.getCVCalibrate(arg_22_0, arg_22_1, arg_22_2)
	local var_22_0 = pg.ship_skin_template[arg_22_0]

	if not var_22_0 then
		return 0
	end

	if arg_22_1 == "main" then
		arg_22_1 = arg_22_1 .. "_" .. arg_22_2
	end

	return var_22_0.l2d_voice_calibrate[arg_22_1]
end

function var_0_0.getL2dSoundEffect(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = pg.ship_skin_template[arg_23_0]

	if not var_23_0 then
		return 0
	end

	if arg_23_1 == "main" then
		arg_23_1 = arg_23_1 .. "_" .. arg_23_2
	end

	return var_23_0.l2d_se[arg_23_1]
end

function var_0_0.getOriginalSkinId(arg_24_0)
	local var_24_0 = pg.ship_skin_template[arg_24_0].ship_group

	return ShipGroup.getDefaultSkin(var_24_0).id
end

function var_0_0.getTransformShipId(arg_25_0)
	local var_25_0 = pg.ship_data_template[arg_25_0].group_type
	local var_25_1 = pg.ship_data_trans[var_25_0]

	if var_25_1 then
		for iter_25_0, iter_25_1 in ipairs(var_25_1.transform_list) do
			for iter_25_2, iter_25_3 in ipairs(iter_25_1) do
				local var_25_2 = pg.transform_data_template[iter_25_3[2]]

				for iter_25_4, iter_25_5 in ipairs(var_25_2.ship_id) do
					if iter_25_5[1] == arg_25_0 then
						return iter_25_5[2]
					end
				end
			end
		end
	end
end

function var_0_0.getAircraftCount(arg_26_0)
	local var_26_0 = arg_26_0:getConfigTable().base_list
	local var_26_1 = arg_26_0:getConfigTable().default_equip_list
	local var_26_2 = {}

	for iter_26_0 = 1, 3 do
		local var_26_3 = arg_26_0:getEquip(iter_26_0) and arg_26_0:getEquip(iter_26_0).configId or var_26_1[iter_26_0]
		local var_26_4 = Equipment.getConfigData(var_26_3).type

		if table.contains(EquipType.AirDomainEquip, var_26_4) then
			var_26_2[var_26_4] = defaultValue(var_26_2[var_26_4], 0) + var_26_0[iter_26_0]
		end
	end

	return var_26_2
end

function var_0_0.getShipType(arg_27_0)
	return arg_27_0:getConfig("type")
end

function var_0_0.getEnergy(arg_28_0)
	return arg_28_0.energy
end

function var_0_0.getEnergeConfig(arg_29_0)
	local var_29_0 = pg.energy_template
	local var_29_1 = arg_29_0:getEnergy()

	for iter_29_0, iter_29_1 in pairs(var_29_0) do
		if type(iter_29_0) == "number" and var_29_1 >= iter_29_1.lower_bound and var_29_1 <= iter_29_1.upper_bound then
			return iter_29_1
		end
	end

	assert(false, "疲劳配置不存在：" .. arg_29_0.energy)
end

function var_0_0.getEnergyPrint(arg_30_0)
	local var_30_0 = arg_30_0:getEnergeConfig()

	return var_30_0.icon, var_30_0.desc
end

function var_0_0.getIntimacy(arg_31_0)
	return arg_31_0.intimacy
end

function var_0_0.getCVIntimacy(arg_32_0)
	return arg_32_0:getIntimacy() / 100 + (arg_32_0.propose and 1000 or 0)
end

function var_0_0.getIntimacyMax(arg_33_0)
	if arg_33_0.propose then
		return 200
	else
		return arg_33_0:GetNoProposeIntimacyMax()
	end
end

function var_0_0.GetNoProposeIntimacyMax(arg_34_0)
	return 100
end

function var_0_0.getIntimacyIcon(arg_35_0)
	local var_35_0 = pg.intimacy_template[arg_35_0:getIntimacyLevel()]
	local var_35_1 = ""

	if arg_35_0:isMetaShip() then
		var_35_1 = "_meta"
	elseif arg_35_0:IsXIdol() then
		var_35_1 = "_imas"
	end

	if not arg_35_0.propose and math.floor(arg_35_0:getIntimacy() / 100) >= arg_35_0:getIntimacyMax() then
		return var_35_0.icon .. var_35_1, "heart" .. var_35_1
	else
		return var_35_0.icon .. var_35_1
	end
end

function var_0_0.getIntimacyDetail(arg_36_0)
	return arg_36_0:getIntimacyMax(), math.floor(arg_36_0:getIntimacy() / 100)
end

function var_0_0.getIntimacyInfo(arg_37_0)
	local var_37_0 = pg.intimacy_template[arg_37_0:getIntimacyLevel()]

	return var_37_0.icon, var_37_0.desc
end

function var_0_0.getIntimacyLevel(arg_38_0)
	local var_38_0 = 0
	local var_38_1 = pg.intimacy_template

	for iter_38_0, iter_38_1 in pairs(var_38_1) do
		if type(iter_38_0) == "number" and arg_38_0:getIntimacy() >= iter_38_1.lower_bound and arg_38_0:getIntimacy() <= iter_38_1.upper_bound then
			var_38_0 = iter_38_0

			break
		end
	end

	if var_38_0 < arg_38_0.INTIMACY_PROPOSE and arg_38_0.propose then
		var_38_0 = arg_38_0.INTIMACY_PROPOSE
	end

	return var_38_0
end

function var_0_0.getBluePrint(arg_39_0)
	local var_39_0 = ShipBluePrint.New({
		id = arg_39_0.groupId
	})
	local var_39_1 = arg_39_0.strengthList[1] or {
		exp = 0,
		level = 0
	}

	var_39_0:updateInfo({
		blue_print_level = var_39_1.level,
		exp = var_39_1.exp
	})

	return var_39_0
end

function var_0_0.getBaseList(arg_40_0)
	if arg_40_0:isBluePrintShip() then
		local var_40_0 = arg_40_0:getBluePrint()

		assert(var_40_0, "blueprint can not be nil" .. arg_40_0.configId)

		return var_40_0:getBaseList(arg_40_0)
	else
		return arg_40_0:getConfig("base_list")
	end
end

function var_0_0.getPreLoadCount(arg_41_0)
	if arg_41_0:isBluePrintShip() then
		return arg_41_0:getBluePrint():getPreLoadCount(arg_41_0)
	else
		return arg_41_0:getConfig("preload_count")
	end
end

function var_0_0.getNation(arg_42_0)
	return arg_42_0:getConfig("nationality")
end

function var_0_0.getPaintingName(arg_43_0)
	local var_43_0 = pg.ship_data_statistics[arg_43_0].skin_id
	local var_43_1 = pg.ship_skin_template[var_43_0]

	assert(var_43_1, "ship_skin_template not exist: " .. arg_43_0 .. " " .. var_43_0)

	return var_43_1.painting
end

function var_0_0.getName(arg_44_0)
	if arg_44_0.propose and pg.PushNotificationMgr.GetInstance():isEnableShipName() then
		return arg_44_0.name
	end

	if arg_44_0:isRemoulded() then
		return pg.ship_skin_template[arg_44_0:getRemouldSkinId()].name
	end

	return pg.ship_data_statistics[arg_44_0.configId].name
end

function var_0_0.GetDefaultName(arg_45_0)
	if arg_45_0:isRemoulded() then
		return pg.ship_skin_template[arg_45_0:getRemouldSkinId()].name
	else
		return pg.ship_data_statistics[arg_45_0.configId].name
	end
end

function var_0_0.getShipName(arg_46_0)
	return pg.ship_data_statistics[arg_46_0].name
end

function var_0_0.getBreakOutLevel(arg_47_0)
	assert(arg_47_0, "必须存在配置id")
	assert(pg.ship_data_statistics[arg_47_0], "必须存在配置" .. arg_47_0)

	return pg.ship_data_statistics[arg_47_0].star
end

function var_0_0.Ctor(arg_48_0, arg_48_1)
	arg_48_0.id = arg_48_1.id
	arg_48_0.configId = arg_48_1.template_id or arg_48_1.configId
	arg_48_0.level = arg_48_1.level
	arg_48_0.exp = arg_48_1.exp
	arg_48_0.energy = arg_48_1.energy
	arg_48_0.lockState = arg_48_1.is_locked
	arg_48_0.intimacy = arg_48_1.intimacy
	arg_48_0.propose = arg_48_1.propose and arg_48_1.propose > 0
	arg_48_0.proposeTime = arg_48_1.propose

	if arg_48_0.intimacy and arg_48_0.intimacy > 10000 and not arg_48_0.propose then
		arg_48_0.intimacy = 10000
	end

	arg_48_0.renameTime = arg_48_1.change_name_timestamp

	if arg_48_1.name and arg_48_1.name ~= "" then
		arg_48_0.name = arg_48_1.name
	else
		assert(pg.ship_data_statistics[arg_48_0.configId], "必须存在配置" .. arg_48_0.configId)

		arg_48_0.name = pg.ship_data_statistics[arg_48_0.configId].name
	end

	arg_48_0.bluePrintFlag = arg_48_1.blue_print_flag or 0
	arg_48_0.strengthList = {}

	for iter_48_0, iter_48_1 in ipairs(arg_48_1.strength_list or {}) do
		if not arg_48_0:isBluePrintShip() then
			local var_48_0 = ShipModAttr.ID_TO_ATTR[iter_48_1.id]

			arg_48_0.strengthList[var_48_0] = iter_48_1.exp
		else
			table.insert(arg_48_0.strengthList, {
				level = iter_48_1.id,
				exp = iter_48_1.exp
			})
		end
	end

	local var_48_1 = arg_48_1.state or {}

	arg_48_0.state = var_48_1.state
	arg_48_0.state_info_1 = var_48_1.state_info_1
	arg_48_0.state_info_2 = var_48_1.state_info_2
	arg_48_0.state_info_3 = var_48_1.state_info_3
	arg_48_0.state_info_4 = var_48_1.state_info_4
	arg_48_0.equipmentSkins = {}
	arg_48_0.equipments = {}

	if arg_48_1.equip_info_list then
		for iter_48_2, iter_48_3 in ipairs(arg_48_1.equip_info_list or {}) do
			arg_48_0.equipments[iter_48_2] = iter_48_3.id > 0 and Equipment.New({
				count = 1,
				id = iter_48_3.id,
				config_id = iter_48_3.id,
				skinId = iter_48_3.skinId
			}) or false
			arg_48_0.equipmentSkins[iter_48_2] = iter_48_3.skinId > 0 and iter_48_3.skinId or 0

			arg_48_0:reletiveEquipSkin(iter_48_2)
		end
	end

	arg_48_0.spWeapon = nil

	if arg_48_1.spweapon then
		arg_48_0:UpdateSpWeapon(SpWeapon.CreateByNet(arg_48_1.spweapon))
	end

	arg_48_0.skills = {}

	for iter_48_4, iter_48_5 in ipairs(arg_48_1.skill_id_list or {}) do
		arg_48_0:updateSkill(iter_48_5)
	end

	arg_48_0.star = arg_48_0:getConfig("rarity")
	arg_48_0.transforms = {}

	for iter_48_6, iter_48_7 in ipairs(arg_48_1.transform_list or {}) do
		arg_48_0.transforms[iter_48_7.id] = {
			id = iter_48_7.id,
			level = iter_48_7.level
		}
	end

	arg_48_0.groupId = pg.ship_data_template[arg_48_0.configId].group_type
	arg_48_0.createTime = arg_48_1.create_time or 0

	local var_48_2 = getProxy(CollectionProxy)

	arg_48_0.virgin = var_48_2 and var_48_2.shipGroups[arg_48_0.groupId] == nil

	local var_48_3 = {
		pg.gameset.test_ship_config_1.key_value,
		pg.gameset.test_ship_config_2.key_value,
		pg.gameset.test_ship_config_3.key_value
	}
	local var_48_4 = table.indexof(var_48_3, arg_48_0.configId)

	if var_48_4 == 1 then
		arg_48_0.testShip = {
			2,
			3,
			4
		}
	elseif var_48_4 == 2 then
		arg_48_0.testShip = {
			5
		}
	elseif var_48_4 == 3 then
		arg_48_0.testShip = {
			6
		}
	else
		arg_48_0.testShip = nil
	end

	arg_48_0.maxIntimacy = pg.intimacy_template[#pg.intimacy_template.all].upper_bound

	if not HXSet.isHxSkin() then
		arg_48_0.skinId = arg_48_1.skin_id or 0
	else
		arg_48_0.skinId = 0
	end

	if arg_48_0.skinId == 0 then
		arg_48_0.skinId = arg_48_0:getConfig("skin_id")
	end

	if arg_48_1.name and arg_48_1.name ~= "" then
		arg_48_0.name = arg_48_1.name
	elseif arg_48_0:isRemoulded() then
		arg_48_0.name = pg.ship_skin_template[arg_48_0:getRemouldSkinId()].name
	else
		arg_48_0.name = pg.ship_data_statistics[arg_48_0.configId].name
	end

	arg_48_0.maxLevel = arg_48_1.max_level
	arg_48_0.proficiency = arg_48_1.proficiency or 0
	arg_48_0.preferenceTag = arg_48_1.common_flag
	arg_48_0.hpRant = 10000
	arg_48_0.strategies = {}
	arg_48_0.triggers = {}
	arg_48_0.commanderId = arg_48_1.commanderid or 0
	arg_48_0.activityNpc = arg_48_1.activity_npc or 0

	if var_0_0.isMetaShipByConfigID(arg_48_0.configId) then
		local var_48_5 = MetaCharacterConst.GetMetaShipGroupIDByConfigID(arg_48_0.configId)

		arg_48_0.metaCharacter = MetaCharacter.New({
			id = var_48_5,
			repair_attr_info = arg_48_1.meta_repair_list
		}, arg_48_0)
	end
end

function var_0_0.isMetaShipByConfigID(arg_49_0)
	local var_49_0 = pg.ship_meta_breakout.all
	local var_49_1 = var_49_0[1]
	local var_49_2 = false

	if var_49_1 <= arg_49_0 then
		for iter_49_0, iter_49_1 in ipairs(var_49_0) do
			if arg_49_0 == iter_49_1 then
				var_49_2 = true

				break
			end
		end
	end

	return var_49_2
end

function var_0_0.isMetaShip(arg_50_0)
	return arg_50_0.metaCharacter ~= nil
end

function var_0_0.getMetaCharacter(arg_51_0)
	return arg_51_0.metaCharacter
end

function var_0_0.unlockActivityNpc(arg_52_0, arg_52_1)
	arg_52_0.activityNpc = arg_52_1
end

function var_0_0.isActivityNpc(arg_53_0)
	return arg_53_0.activityNpc > 0
end

function var_0_0.getActiveEquipments(arg_54_0)
	local var_54_0 = Clone(arg_54_0.equipments)

	for iter_54_0 = #var_54_0, 1, -1 do
		local var_54_1 = var_54_0[iter_54_0]

		if var_54_1 then
			for iter_54_1 = 1, iter_54_0 - 1 do
				local var_54_2 = var_54_0[iter_54_1]

				if var_54_2 and var_54_1:getConfig("equip_limit") ~= 0 and var_54_2:getConfig("equip_limit") == var_54_1:getConfig("equip_limit") then
					var_54_0[iter_54_0] = false
				end
			end
		end
	end

	return var_54_0
end

function var_0_0.getAllEquipments(arg_55_0)
	return arg_55_0.equipments
end

function var_0_0.isBluePrintShip(arg_56_0)
	return arg_56_0.bluePrintFlag == 1
end

function var_0_0.updateSkinId(arg_57_0, arg_57_1)
	arg_57_0.skinId = arg_57_1
end

function var_0_0.updateName(arg_58_0)
	if arg_58_0.name ~= pg.ship_data_statistics[arg_58_0.configId].name then
		return
	end

	if arg_58_0:isRemoulded() then
		arg_58_0.name = pg.ship_skin_template[arg_58_0:getRemouldSkinId()].name
	else
		arg_58_0.name = pg.ship_data_statistics[arg_58_0.configId].name
	end
end

function var_0_0.isRemoulded(arg_59_0)
	if arg_59_0.remoulded then
		return true
	end

	local var_59_0 = pg.ship_data_trans[arg_59_0.groupId]

	if var_59_0 then
		for iter_59_0, iter_59_1 in ipairs(var_59_0.transform_list) do
			for iter_59_2, iter_59_3 in ipairs(iter_59_1) do
				local var_59_1 = pg.transform_data_template[iter_59_3[2]]

				if var_59_1.skin_id ~= 0 and arg_59_0.transforms[iter_59_3[2]] and arg_59_0.transforms[iter_59_3[2]].level == var_59_1.max_level then
					return true
				end
			end
		end
	end

	return false
end

function var_0_0.getRemouldSkinId(arg_60_0)
	local var_60_0 = ShipGroup.getModSkin(arg_60_0.groupId)

	if var_60_0 then
		return var_60_0.id
	end

	return nil
end

function var_0_0.hasEquipmentSkinInPos(arg_61_0, arg_61_1)
	local var_61_0 = arg_61_0.equipments[arg_61_1]

	return var_61_0 and var_61_0:hasSkin()
end

function var_0_0.getPrefab(arg_62_0)
	local var_62_0 = arg_62_0.skinId

	if arg_62_0:hasEquipmentSkinInPos(var_0_2) then
		local var_62_1 = arg_62_0:getEquip(var_0_2)
		local var_62_2 = var_0_7[var_62_1:getSkinId()].ship_skin_id

		var_62_0 = var_62_2 ~= 0 and var_62_2 or var_62_0
	end

	local var_62_3 = pg.ship_skin_template[var_62_0]

	assert(var_62_3, "ship_skin_template not exist: " .. arg_62_0.configId .. " " .. var_62_0)

	return var_62_3.prefab
end

function var_0_0.getAttachmentPrefab(arg_63_0)
	local var_63_0 = {}

	for iter_63_0, iter_63_1 in ipairs(arg_63_0.equipments) do
		if iter_63_1 and iter_63_1:hasSkinOrbit() then
			local var_63_1 = iter_63_1:getSkinId()

			var_63_0[var_63_1] = var_0_7[var_63_1]
		end
	end

	return var_63_0
end

function var_0_0.getPainting(arg_64_0)
	local var_64_0 = pg.ship_skin_template[arg_64_0.skinId]

	assert(var_64_0, "ship_skin_template not exist: " .. arg_64_0.configId .. " " .. arg_64_0.skinId)

	return var_64_0.painting
end

function var_0_0.GetSkinConfig(arg_65_0)
	local var_65_0 = pg.ship_skin_template[arg_65_0.skinId]

	assert(var_65_0, "ship_skin_template not exist: " .. arg_65_0.configId .. " " .. arg_65_0.skinId)

	return var_65_0
end

function var_0_0.getRemouldPainting(arg_66_0)
	local var_66_0 = pg.ship_skin_template[arg_66_0:getRemouldSkinId()]

	assert(var_66_0, "ship_skin_template not exist: " .. arg_66_0.configId .. " " .. arg_66_0.skinId)

	return var_66_0.painting
end

function var_0_0.updateStateInfo34(arg_67_0, arg_67_1, arg_67_2)
	arg_67_0.state_info_3 = arg_67_1
	arg_67_0.state_info_4 = arg_67_2
end

function var_0_0.hasStateInfo3Or4(arg_68_0)
	return arg_68_0.state_info_3 ~= 0 or arg_68_0.state_info_4 ~= 0
end

function var_0_0.isTestShip(arg_69_0)
	return arg_69_0.testShip
end

function var_0_0.canUseTestShip(arg_70_0, arg_70_1)
	assert(arg_70_0.testShip, "ship is not TestShip")

	return table.contains(arg_70_0.testShip, arg_70_1)
end

function var_0_0.updateEquip(arg_71_0, arg_71_1, arg_71_2)
	assert(arg_71_2 == nil or arg_71_2.count == 1)

	local var_71_0 = arg_71_0.equipments[arg_71_1]

	arg_71_0.equipments[arg_71_1] = arg_71_2 and Clone(arg_71_2) or false

	local function var_71_1(arg_72_0)
		arg_72_0 = CreateShell(arg_72_0)
		arg_72_0.shipId = arg_71_0.id
		arg_72_0.shipPos = arg_71_1

		return arg_72_0
	end

	if var_71_0 then
		getProxy(EquipmentProxy):OnShipEquipsRemove(var_71_0, arg_71_0.id, arg_71_1)
		var_71_0:setSkinId(0)
		pg.m02:sendNotification(BayProxy.SHIP_EQUIPMENT_REMOVED, var_71_1(var_71_0))
	end

	if arg_71_2 then
		getProxy(EquipmentProxy):OnShipEquipsAdd(arg_71_2, arg_71_0.id, arg_71_1)
		arg_71_0:reletiveEquipSkin(arg_71_1)
		pg.m02:sendNotification(BayProxy.SHIP_EQUIPMENT_ADDED, var_71_1(arg_71_2))
	end
end

function var_0_0.reletiveEquipSkin(arg_73_0, arg_73_1)
	if arg_73_0.equipments[arg_73_1] and arg_73_0.equipmentSkins[arg_73_1] ~= 0 then
		local var_73_0 = pg.equip_skin_template[arg_73_0.equipmentSkins[arg_73_1]].equip_type
		local var_73_1 = arg_73_0.equipments[arg_73_1]:getType()

		if table.contains(var_73_0, var_73_1) then
			arg_73_0.equipments[arg_73_1]:setSkinId(arg_73_0.equipmentSkins[arg_73_1])
		else
			arg_73_0.equipments[arg_73_1]:setSkinId(0)
		end
	elseif arg_73_0.equipments[arg_73_1] then
		arg_73_0.equipments[arg_73_1]:setSkinId(0)
	end
end

function var_0_0.updateEquipmentSkin(arg_74_0, arg_74_1, arg_74_2)
	if not arg_74_1 then
		return
	end

	if arg_74_2 and arg_74_2 > 0 then
		local var_74_0 = arg_74_0:getSkinTypes(arg_74_1)
		local var_74_1 = pg.equip_skin_template[arg_74_2].equip_type
		local var_74_2 = false

		for iter_74_0, iter_74_1 in ipairs(var_74_0) do
			for iter_74_2, iter_74_3 in ipairs(var_74_1) do
				if iter_74_1 == iter_74_3 then
					var_74_2 = true

					break
				end
			end
		end

		if not var_74_2 then
			assert(var_74_2, "部位" .. arg_74_1 .. " 无法穿戴皮肤 " .. arg_74_2)

			return
		end

		local var_74_3 = arg_74_0.equipments[arg_74_1] and arg_74_0.equipments[arg_74_1]:getType() or false

		arg_74_0.equipmentSkins[arg_74_1] = arg_74_2

		if var_74_3 and table.contains(var_74_1, var_74_3) then
			arg_74_0.equipments[arg_74_1]:setSkinId(arg_74_0.equipmentSkins[arg_74_1])
		elseif var_74_3 and not table.contains(var_74_1, var_74_3) then
			arg_74_0.equipments[arg_74_1]:setSkinId(0)
		end
	else
		arg_74_0.equipmentSkins[arg_74_1] = 0

		if arg_74_0.equipments[arg_74_1] then
			arg_74_0.equipments[arg_74_1]:setSkinId(0)
		end
	end
end

function var_0_0.getEquip(arg_75_0, arg_75_1)
	return Clone(arg_75_0.equipments[arg_75_1])
end

function var_0_0.getEquipSkins(arg_76_0)
	return Clone(arg_76_0.equipmentSkins)
end

function var_0_0.getEquipSkin(arg_77_0, arg_77_1)
	return arg_77_0.equipmentSkins[arg_77_1]
end

function var_0_0.getCanEquipSkin(arg_78_0, arg_78_1)
	local var_78_0 = arg_78_0:getSkinTypes(arg_78_1)

	if var_78_0 and #var_78_0 then
		for iter_78_0, iter_78_1 in ipairs(var_78_0) do
			if pg.equip_data_by_type[iter_78_1].equip_skin == 1 then
				return true
			end
		end
	end

	return false
end

function var_0_0.checkCanEquipSkin(arg_79_0, arg_79_1, arg_79_2)
	if not arg_79_1 or not arg_79_2 then
		return
	end

	local var_79_0 = arg_79_0:getSkinTypes(arg_79_1)
	local var_79_1 = pg.equip_skin_template[arg_79_2].equip_type

	for iter_79_0, iter_79_1 in ipairs(var_79_0) do
		if table.contains(var_79_1, iter_79_1) then
			return true
		end
	end

	return false
end

function var_0_0.getSkinTypes(arg_80_0, arg_80_1)
	return pg.ship_data_template[arg_80_0.configId]["equip_" .. arg_80_1] or {}
end

function var_0_0.updateState(arg_81_0, arg_81_1)
	arg_81_0.state = arg_81_1
end

function var_0_0.addSkillExp(arg_82_0, arg_82_1, arg_82_2)
	local var_82_0 = arg_82_0.skills[arg_82_1] or {
		exp = 0,
		level = 1,
		id = arg_82_1
	}
	local var_82_1 = var_82_0.level and var_82_0.level or 1
	local var_82_2 = pg.skill_need_exp.all[#pg.skill_need_exp.all]

	if var_82_1 == var_82_2 then
		return
	end

	local var_82_3 = var_82_0.exp and arg_82_2 + var_82_0.exp or 0 + arg_82_2

	while var_82_3 >= pg.skill_need_exp[var_82_1].exp do
		var_82_3 = var_82_3 - pg.skill_need_exp[var_82_1].exp
		var_82_1 = var_82_1 + 1

		if var_82_1 == var_82_2 then
			var_82_3 = 0

			break
		end
	end

	arg_82_0:updateSkill({
		id = var_82_0.id,
		level = var_82_1,
		exp = var_82_3
	})
end

function var_0_0.upSkillLevelForMeta(arg_83_0, arg_83_1)
	local var_83_0 = arg_83_0.skills[arg_83_1] or {
		exp = 0,
		level = 0,
		id = arg_83_1
	}
	local var_83_1 = arg_83_0:isSkillLevelMax(arg_83_1)
	local var_83_2 = var_83_0.level

	if not var_83_1 then
		var_83_2 = var_83_2 + 1
	end

	arg_83_0:updateSkill({
		exp = 0,
		id = var_83_0.id,
		level = var_83_2
	})
end

function var_0_0.getMetaSkillLevelBySkillID(arg_84_0, arg_84_1)
	return (arg_84_0.skills[arg_84_1] or {
		exp = 0,
		level = 0,
		id = arg_84_1
	}).level
end

function var_0_0.isSkillLevelMax(arg_85_0, arg_85_1)
	local var_85_0 = arg_85_0.skills[arg_85_1] or {
		exp = 0,
		level = 1,
		id = arg_85_1
	}

	return (var_85_0.level and var_85_0.level or 1) >= pg.skill_data_template[arg_85_1].max_level
end

function var_0_0.isAllMetaSkillLevelMax(arg_86_0)
	local var_86_0 = true
	local var_86_1 = MetaCharacterConst.getTacticsSkillIDListByShipConfigID(arg_86_0.configId)

	for iter_86_0, iter_86_1 in ipairs(var_86_1) do
		if not arg_86_0:isSkillLevelMax(iter_86_1) then
			var_86_0 = false

			break
		end
	end

	return var_86_0
end

function var_0_0.isAllMetaSkillLock(arg_87_0)
	local var_87_0 = MetaCharacterConst.getTacticsSkillIDListByShipConfigID(arg_87_0.configId)
	local var_87_1 = true

	for iter_87_0, iter_87_1 in ipairs(var_87_0) do
		if arg_87_0:getMetaSkillLevelBySkillID(iter_87_1) > 0 then
			var_87_1 = false

			break
		end
	end

	return var_87_1
end

function var_0_0.bindConfigTable(arg_88_0)
	return pg.ship_data_statistics
end

function var_0_0.isAvaiable(arg_89_0)
	return true
end

var_0_0.PROPERTIES = {
	AttributeType.Durability,
	AttributeType.Cannon,
	AttributeType.Torpedo,
	AttributeType.AntiAircraft,
	AttributeType.Air,
	AttributeType.Reload,
	AttributeType.Armor,
	AttributeType.Hit,
	AttributeType.Dodge,
	AttributeType.Speed,
	AttributeType.Luck,
	AttributeType.AntiSub
}
var_0_0.PROPERTIES_ENHANCEMENT = {
	AttributeType.Durability,
	AttributeType.Cannon,
	AttributeType.Torpedo,
	AttributeType.AntiAircraft,
	AttributeType.Air,
	AttributeType.Reload,
	AttributeType.Hit,
	AttributeType.Dodge,
	AttributeType.Speed,
	AttributeType.Luck,
	AttributeType.AntiSub
}
var_0_0.DIVE_PROPERTIES = {
	AttributeType.OxyMax,
	AttributeType.OxyCost,
	AttributeType.OxyRecovery,
	AttributeType.OxyRecoveryBench,
	AttributeType.OxyRecoverySurface,
	AttributeType.OxyAttackDuration,
	AttributeType.OxyRaidDistance
}
var_0_0.SONAR_PROPERTIES = {
	AttributeType.SonarRange
}

function var_0_0.intimacyAdditions(arg_90_0, arg_90_1)
	local var_90_0 = pg.intimacy_template[arg_90_0:getIntimacyLevel()].attr_bonus * 0.0001

	for iter_90_0, iter_90_1 in pairs(arg_90_1) do
		if iter_90_0 == AttributeType.Durability or iter_90_0 == AttributeType.Cannon or iter_90_0 == AttributeType.Torpedo or iter_90_0 == AttributeType.AntiAircraft or iter_90_0 == AttributeType.AntiSub or iter_90_0 == AttributeType.Air or iter_90_0 == AttributeType.Reload or iter_90_0 == AttributeType.Hit or iter_90_0 == AttributeType.Dodge then
			arg_90_1[iter_90_0] = arg_90_1[iter_90_0] * (var_90_0 + 1)
		end
	end
end

function var_0_0.getShipProperties(arg_91_0)
	local var_91_0 = arg_91_0:getBaseProperties()

	if arg_91_0:isBluePrintShip() then
		local var_91_1 = arg_91_0:getBluePrint()

		assert(var_91_1, "blueprint can not be nil" .. arg_91_0.configId)

		local var_91_2 = var_91_1:getTotalAdditions()

		for iter_91_0, iter_91_1 in pairs(var_91_2) do
			var_91_0[iter_91_0] = var_91_0[iter_91_0] + calcFloor(iter_91_1)
		end

		arg_91_0:intimacyAdditions(var_91_0)
	elseif arg_91_0:isMetaShip() then
		assert(arg_91_0.metaCharacter)

		for iter_91_2, iter_91_3 in pairs(var_91_0) do
			var_91_0[iter_91_2] = var_91_0[iter_91_2] + arg_91_0.metaCharacter:getAttrAddition(iter_91_2)
		end

		arg_91_0:intimacyAdditions(var_91_0)
	else
		local var_91_3 = pg.ship_data_template[arg_91_0.configId].strengthen_id
		local var_91_4 = var_0_5[var_91_3]

		for iter_91_4, iter_91_5 in pairs(arg_91_0.strengthList) do
			local var_91_5 = ShipModAttr.ATTR_TO_INDEX[iter_91_4]
			local var_91_6 = math.min(iter_91_5, var_91_4.durability[var_91_5] * var_91_4.level_exp[var_91_5])
			local var_91_7 = math.max(arg_91_0:getModExpRatio(iter_91_4), 1)

			var_91_0[iter_91_4] = var_91_0[iter_91_4] + calcFloor(var_91_6 / var_91_7)
		end

		arg_91_0:intimacyAdditions(var_91_0)

		for iter_91_6, iter_91_7 in pairs(arg_91_0.transforms) do
			local var_91_8 = pg.transform_data_template[iter_91_7.id].effect

			for iter_91_8 = 1, iter_91_7.level do
				local var_91_9 = var_91_8[iter_91_8] or {}

				for iter_91_9, iter_91_10 in pairs(var_91_0) do
					if var_91_9[iter_91_9] then
						var_91_0[iter_91_9] = var_91_0[iter_91_9] + var_91_9[iter_91_9]
					end
				end
			end
		end
	end

	return var_91_0
end

function var_0_0.getTechNationAddition(arg_92_0, arg_92_1)
	local var_92_0 = getProxy(TechnologyNationProxy)
	local var_92_1 = arg_92_0:getConfig("type")

	if var_92_1 == ShipType.DaoQuV or var_92_1 == ShipType.DaoQuM then
		var_92_1 = ShipType.QuZhu
	end

	return var_92_0:getShipAddition(var_92_1, arg_92_1)
end

function var_0_0.getTechNationMaxAddition(arg_93_0, arg_93_1)
	local var_93_0 = getProxy(TechnologyNationProxy)
	local var_93_1 = arg_93_0:getConfig("type")

	return var_93_0:getShipMaxAddition(var_93_1, arg_93_1)
end

function var_0_0.getEquipProficiencyByPos(arg_94_0, arg_94_1)
	return arg_94_0:getEquipProficiencyList()[arg_94_1]
end

function var_0_0.getEquipProficiencyList(arg_95_0)
	local var_95_0 = arg_95_0:getConfigTable()
	local var_95_1 = Clone(var_95_0.equipment_proficiency)

	if arg_95_0:isBluePrintShip() then
		local var_95_2 = arg_95_0:getBluePrint()

		assert(var_95_2, "blueprint can not be nil >>>" .. arg_95_0.groupId)

		var_95_1 = var_95_2:getEquipProficiencyList(arg_95_0)
	else
		for iter_95_0, iter_95_1 in ipairs(var_95_1) do
			local var_95_3 = 0

			for iter_95_2, iter_95_3 in pairs(arg_95_0.transforms) do
				local var_95_4 = pg.transform_data_template[iter_95_3.id].effect

				for iter_95_4 = 1, iter_95_3.level do
					local var_95_5 = var_95_4[iter_95_4] or {}

					if var_95_5["equipment_proficiency_" .. iter_95_0] then
						var_95_3 = var_95_3 + var_95_5["equipment_proficiency_" .. iter_95_0]
					end
				end
			end

			var_95_1[iter_95_0] = iter_95_1 + var_95_3
		end
	end

	return var_95_1
end

function var_0_0.getBaseProperties(arg_96_0)
	local var_96_0 = arg_96_0:getConfigTable()

	assert(var_96_0, "配置表没有这艘船" .. arg_96_0.configId)

	local var_96_1 = {}
	local var_96_2 = {}

	for iter_96_0, iter_96_1 in ipairs(var_0_0.PROPERTIES) do
		var_96_1[iter_96_1] = arg_96_0:getGrowthForAttr(iter_96_1)
		var_96_2[iter_96_1] = var_96_1[iter_96_1]
	end

	for iter_96_2, iter_96_3 in ipairs(arg_96_0:getConfig("lock")) do
		var_96_2[iter_96_3] = var_96_1[iter_96_3]
	end

	for iter_96_4, iter_96_5 in ipairs(var_0_0.DIVE_PROPERTIES) do
		var_96_2[iter_96_5] = var_96_0[iter_96_5]
	end

	for iter_96_6, iter_96_7 in ipairs(var_0_0.SONAR_PROPERTIES) do
		var_96_2[iter_96_7] = 0
	end

	return var_96_2
end

function var_0_0.getGrowthForAttr(arg_97_0, arg_97_1)
	local var_97_0 = arg_97_0:getConfigTable()
	local var_97_1 = table.indexof(var_0_0.PROPERTIES, arg_97_1)
	local var_97_2 = pg.gameset.extra_attr_level_limit.key_value
	local var_97_3 = var_97_0.attrs[var_97_1] + (arg_97_0.level - 1) * var_97_0.attrs_growth[var_97_1] / 1000

	if var_97_2 < arg_97_0.level then
		var_97_3 = var_97_3 + (arg_97_0.level - var_97_2) * var_97_0.attrs_growth_extra[var_97_1] / 1000
	end

	return var_97_3
end

function var_0_0.isMaxStar(arg_98_0)
	return arg_98_0:getStar() >= arg_98_0:getMaxStar()
end

function var_0_0.IsMaxStarByTmpID(arg_99_0)
	local var_99_0 = pg.ship_data_template[arg_99_0]

	return var_99_0.star >= var_99_0.star_max
end

function var_0_0.IsSpweaponUnlock(arg_100_0)
	if not arg_100_0:CanAccumulateExp() then
		return false, "spweapon_tip_locked"
	else
		return true
	end
end

function var_0_0.getModProperties(arg_101_0, arg_101_1)
	return arg_101_0.strengthList[arg_101_1] or 0
end

function var_0_0.addModAttrExp(arg_102_0, arg_102_1, arg_102_2)
	local var_102_0 = arg_102_0:getModAttrTopLimit(arg_102_1)

	if var_102_0 == 0 then
		return
	end

	local var_102_1 = arg_102_0:getModExpRatio(arg_102_1)
	local var_102_2 = arg_102_0:getModProperties(arg_102_1)

	if var_102_2 + arg_102_2 > var_102_0 * var_102_1 then
		arg_102_0.strengthList[arg_102_1] = var_102_0 * var_102_1
	else
		arg_102_0.strengthList[arg_102_1] = var_102_2 + arg_102_2
	end
end

function var_0_0.getNeedModExp(arg_103_0)
	local var_103_0 = {}

	for iter_103_0, iter_103_1 in pairs(ShipModAttr.ID_TO_ATTR) do
		local var_103_1 = arg_103_0:getModAttrTopLimit(iter_103_1)

		if var_103_1 == 0 then
			var_103_0[iter_103_1] = 0
		else
			var_103_0[iter_103_1] = var_103_1 * arg_103_0:getModExpRatio(iter_103_1) - arg_103_0:getModProperties(iter_103_1)
		end
	end

	return var_103_0
end

function var_0_0.attrVertify(arg_104_0)
	if not BayProxy.checkShiplevelVertify(arg_104_0) then
		return false
	end

	for iter_104_0, iter_104_1 in ipairs(arg_104_0.equipments) do
		if iter_104_1 and not iter_104_1:vertify() then
			return false
		end
	end

	return true
end

function var_0_0.getEquipmentProperties(arg_105_0)
	local var_105_0 = {}
	local var_105_1 = {}

	for iter_105_0, iter_105_1 in ipairs(var_0_0.PROPERTIES) do
		var_105_0[iter_105_1] = 0
	end

	for iter_105_2, iter_105_3 in ipairs(var_0_0.DIVE_PROPERTIES) do
		var_105_0[iter_105_3] = 0
	end

	for iter_105_4, iter_105_5 in ipairs(var_0_0.SONAR_PROPERTIES) do
		var_105_0[iter_105_5] = 0
	end

	for iter_105_6, iter_105_7 in ipairs(var_0_0.PROPERTIES_ENHANCEMENT) do
		var_105_1[iter_105_7] = 0
	end

	var_105_0[AttributeType.AirDominate] = 0
	var_105_0[AttributeType.AntiSiren] = 0

	local var_105_2 = arg_105_0:getActiveEquipments()

	for iter_105_8, iter_105_9 in ipairs(var_105_2) do
		if iter_105_9 then
			local var_105_3 = iter_105_9:GetAttributes()

			for iter_105_10, iter_105_11 in ipairs(var_105_3) do
				if iter_105_11 and var_105_0[iter_105_11.type] then
					var_105_0[iter_105_11.type] = var_105_0[iter_105_11.type] + iter_105_11.value
				end
			end

			local var_105_4 = iter_105_9:GetPropertyRate()

			for iter_105_12, iter_105_13 in pairs(var_105_4) do
				var_105_1[iter_105_12] = math.max(var_105_1[iter_105_12], iter_105_13)
			end

			local var_105_5 = iter_105_9:GetSonarProperty()

			if var_105_5 then
				for iter_105_14, iter_105_15 in pairs(var_105_5) do
					var_105_0[iter_105_14] = var_105_0[iter_105_14] + iter_105_15
				end
			end

			local var_105_6 = iter_105_9:GetAntiSirenPower()

			if var_105_6 then
				var_105_0[AttributeType.AntiSiren] = var_105_0[AttributeType.AntiSiren] + var_105_6 / 10000
			end
		end
	end

	;(function()
		local var_106_0 = arg_105_0:GetSpWeapon()

		if not var_106_0 then
			return
		end

		local var_106_1 = var_106_0:GetPropertiesInfo().attrs

		for iter_106_0, iter_106_1 in ipairs(var_106_1) do
			if iter_106_1 and var_105_0[iter_106_1.type] then
				var_105_0[iter_106_1.type] = var_105_0[iter_106_1.type] + iter_106_1.value
			end
		end
	end)()

	for iter_105_16, iter_105_17 in pairs(var_105_1) do
		var_105_1[iter_105_16] = iter_105_17 + 1
	end

	return var_105_0, var_105_1
end

function var_0_0.getSkillEffects(arg_107_0)
	local var_107_0 = arg_107_0:getShipSkillEffects()

	_.each(arg_107_0:getEquipmentSkillEffects(), function(arg_108_0)
		table.insert(var_107_0, arg_108_0)
	end)

	return var_107_0
end

function var_0_0.getShipSkillEffects(arg_109_0)
	local var_109_0 = {}
	local var_109_1 = arg_109_0:getSkillList()

	for iter_109_0, iter_109_1 in ipairs(var_109_1) do
		local var_109_2 = arg_109_0:RemapSkillId(iter_109_1)
		local var_109_3 = require("GameCfg.buff.buff_" .. var_109_2)

		arg_109_0:FilterActiveSkill(var_109_0, var_109_3, arg_109_0.skills[iter_109_1])
	end

	return var_109_0
end

function var_0_0.getEquipmentSkillEffects(arg_110_0)
	local var_110_0 = {}
	local var_110_1 = arg_110_0:getActiveEquipments()

	for iter_110_0, iter_110_1 in ipairs(var_110_1) do
		local var_110_2
		local var_110_3 = iter_110_1 and iter_110_1:getConfig("skill_id")[1]

		if var_110_3 then
			var_110_2 = require("GameCfg.buff.buff_" .. var_110_3)
		end

		arg_110_0:FilterActiveSkill(var_110_0, var_110_2)
	end

	;(function()
		local var_111_0 = arg_110_0:GetSpWeapon()
		local var_111_1 = var_111_0 and var_111_0:GetEffect() or 0
		local var_111_2

		if var_111_1 > 0 then
			var_111_2 = require("GameCfg.buff.buff_" .. var_111_1)
		end

		arg_110_0:FilterActiveSkill(var_110_0, var_111_2)
	end)()

	return var_110_0
end

function var_0_0.FilterActiveSkill(arg_112_0, arg_112_1, arg_112_2, arg_112_3)
	if not arg_112_2 or not arg_112_2.const_effect_list then
		return
	end

	for iter_112_0 = 1, #arg_112_2.const_effect_list do
		local var_112_0 = arg_112_2.const_effect_list[iter_112_0]
		local var_112_1 = var_112_0.trigger
		local var_112_2 = var_112_0.arg_list
		local var_112_3 = 1

		if arg_112_3 then
			var_112_3 = arg_112_3.level

			local var_112_4 = arg_112_2[var_112_3].const_effect_list

			if var_112_4 and var_112_4[iter_112_0] then
				var_112_1 = var_112_4[iter_112_0].trigger or var_112_1
				var_112_2 = var_112_4[iter_112_0].arg_list or var_112_2
			end
		end

		local var_112_5 = true

		for iter_112_1, iter_112_2 in pairs(var_112_1) do
			if arg_112_0.triggers[iter_112_1] ~= iter_112_2 then
				var_112_5 = false

				break
			end
		end

		if var_112_5 then
			table.insert(arg_112_1, {
				type = var_112_0.type,
				arg_list = var_112_2,
				level = var_112_3
			})
		end
	end
end

function var_0_0.getEquipmentGearScore(arg_113_0)
	local var_113_0 = 0
	local var_113_1 = arg_113_0:getActiveEquipments()

	for iter_113_0, iter_113_1 in ipairs(var_113_1) do
		if iter_113_1 then
			var_113_0 = var_113_0 + iter_113_1:GetGearScore()
		end
	end

	return var_113_0
end

function var_0_0.getProperties(arg_114_0, arg_114_1, arg_114_2, arg_114_3, arg_114_4)
	local var_114_0 = arg_114_1 or {}
	local var_114_1 = arg_114_0:getConfig("nationality")
	local var_114_2 = arg_114_0:getConfig("type")
	local var_114_3 = arg_114_0:getShipProperties()
	local var_114_4, var_114_5 = arg_114_0:getEquipmentProperties()
	local var_114_6
	local var_114_7
	local var_114_8

	if arg_114_3 and arg_114_0:getFlag("inWorld") then
		local var_114_9 = WorldConst.FetchWorldShip(arg_114_0.id)

		var_114_6, var_114_7 = var_114_9:GetShipBuffProperties()
		var_114_8 = var_114_9:GetShipPowerBuffProperties()
	end

	for iter_114_0, iter_114_1 in ipairs(var_0_0.PROPERTIES) do
		local var_114_10 = 0
		local var_114_11 = 0

		for iter_114_2, iter_114_3 in pairs(var_114_0) do
			var_114_10 = var_114_10 + iter_114_3:getAttrRatioAddition(iter_114_1, var_114_1, var_114_2) / 100
			var_114_11 = var_114_11 + iter_114_3:getAttrValueAddition(iter_114_1, var_114_1, var_114_2)
		end

		local var_114_12 = var_114_10 + (var_114_5[iter_114_1] or 1)
		local var_114_13 = var_114_7 and var_114_7[iter_114_1] or 1
		local var_114_14 = var_114_6 and var_114_6[iter_114_1] or 0

		if iter_114_1 == AttributeType.Speed then
			var_114_3[iter_114_1] = var_114_3[iter_114_1] * var_114_12 * var_114_13 + var_114_11 + var_114_4[iter_114_1] + var_114_14
		else
			var_114_3[iter_114_1] = calcFloor(calcFloor(var_114_3[iter_114_1]) * var_114_12 * var_114_13) + var_114_11 + var_114_4[iter_114_1] + var_114_14
		end
	end

	if not arg_114_2 and arg_114_0:isMaxStar() then
		for iter_114_4, iter_114_5 in pairs(var_114_3) do
			local var_114_15 = arg_114_4 and arg_114_0:getTechNationMaxAddition(iter_114_4) or arg_114_0:getTechNationAddition(iter_114_4)

			var_114_3[iter_114_4] = var_114_3[iter_114_4] + var_114_15
		end
	end

	for iter_114_6, iter_114_7 in ipairs(var_0_0.DIVE_PROPERTIES) do
		var_114_3[iter_114_7] = var_114_3[iter_114_7] + var_114_4[iter_114_7]
	end

	for iter_114_8, iter_114_9 in ipairs(var_0_0.SONAR_PROPERTIES) do
		var_114_3[iter_114_9] = var_114_3[iter_114_9] + var_114_4[iter_114_9]
	end

	if arg_114_3 then
		var_114_3[AttributeType.AntiSiren] = (var_114_3[AttributeType.AntiSiren] or 0) + var_114_4[AttributeType.AntiSiren]
	end

	if var_114_8 then
		for iter_114_10, iter_114_11 in pairs(var_114_8) do
			if var_114_3[iter_114_10] then
				if iter_114_10 == AttributeType.Speed then
					var_114_3[iter_114_10] = var_114_3[iter_114_10] * iter_114_11
				else
					var_114_3[iter_114_10] = math.floor(var_114_3[iter_114_10] * iter_114_11)
				end
			end
		end
	end

	return var_114_3
end

function var_0_0.getTransGearScore(arg_115_0)
	local var_115_0 = 0
	local var_115_1 = pg.transform_data_template

	for iter_115_0, iter_115_1 in pairs(arg_115_0.transforms) do
		for iter_115_2 = 1, iter_115_1.level do
			var_115_0 = var_115_0 + (var_115_1[iter_115_1.id].gear_score[iter_115_2] or 0)
		end
	end

	return var_115_0
end

function var_0_0.getShipCombatPower(arg_116_0, arg_116_1)
	local var_116_0 = arg_116_0:getProperties(arg_116_1, nil, nil, true)
	local var_116_1 = var_116_0[AttributeType.Durability] / 5 + var_116_0[AttributeType.Cannon] + var_116_0[AttributeType.Torpedo] + var_116_0[AttributeType.AntiAircraft] + var_116_0[AttributeType.Air] + var_116_0[AttributeType.AntiSub] + var_116_0[AttributeType.Reload] + var_116_0[AttributeType.Hit] * 2 + var_116_0[AttributeType.Dodge] * 2 + var_116_0[AttributeType.Speed] + arg_116_0:getEquipmentGearScore() + arg_116_0:getTransGearScore()

	return math.floor(var_116_1)
end

function var_0_0.cosumeEnergy(arg_117_0, arg_117_1)
	arg_117_0:setEnergy(math.max(arg_117_0:getEnergy() - arg_117_1, 0))
end

function var_0_0.addEnergy(arg_118_0, arg_118_1)
	arg_118_0:setEnergy(arg_118_0:getEnergy() + arg_118_1)
end

function var_0_0.setEnergy(arg_119_0, arg_119_1)
	arg_119_0.energy = arg_119_1
end

function var_0_0.setLikability(arg_120_0, arg_120_1)
	assert(arg_120_1 >= 0 and arg_120_1 <= arg_120_0.maxIntimacy, "intimacy value invaild" .. arg_120_1)
	arg_120_0:setIntimacy(arg_120_1)
end

function var_0_0.addLikability(arg_121_0, arg_121_1)
	local var_121_0 = Mathf.Clamp(arg_121_0:getIntimacy() + arg_121_1, 0, arg_121_0.maxIntimacy)

	arg_121_0:setIntimacy(var_121_0)
end

function var_0_0.setIntimacy(arg_122_0, arg_122_1)
	if arg_122_1 > 10000 and not arg_122_0.propose then
		arg_122_1 = 10000
	end

	arg_122_0.intimacy = arg_122_1

	if not arg_122_0:isActivityNpc() then
		getProxy(CollectionProxy).shipGroups[arg_122_0.groupId]:updateMaxIntimacy(arg_122_0:getIntimacy())
	end
end

function var_0_0.getLevelExpConfig(arg_123_0, arg_123_1)
	if arg_123_0:getConfig("rarity") == ShipRarity.SSR then
		local var_123_0 = Clone(getConfigFromLevel1(var_0_6, arg_123_1 or arg_123_0.level))

		var_123_0.exp = var_123_0.exp_ur
		var_123_0.exp_start = var_123_0.exp_ur_start
		var_123_0.exp_interval = var_123_0.exp_ur_interval
		var_123_0.exp_end = var_123_0.exp_ur_end

		return var_123_0
	else
		return getConfigFromLevel1(var_0_6, arg_123_1 or arg_123_0.level)
	end
end

function var_0_0.getExp(arg_124_0)
	local var_124_0 = arg_124_0:getMaxLevel()

	if arg_124_0.level == var_124_0 and LOCK_FULL_EXP then
		return 0
	end

	return arg_124_0.exp
end

function var_0_0.getProficiency(arg_125_0)
	return arg_125_0.proficiency
end

function var_0_0.addExp(arg_126_0, arg_126_1, arg_126_2)
	local var_126_0 = arg_126_0:getMaxLevel()

	if arg_126_0.level == var_126_0 then
		if arg_126_0.exp >= pg.gameset.exp_overflow_max.key_value then
			return
		end

		if LOCK_FULL_EXP or not arg_126_2 or not arg_126_0:CanAccumulateExp() then
			arg_126_1 = 0
		end
	end

	arg_126_0.exp = arg_126_0.exp + arg_126_1

	local var_126_1 = false

	while arg_126_0:canLevelUp() do
		arg_126_0.exp = arg_126_0.exp - arg_126_0:getLevelExpConfig().exp_interval
		arg_126_0.level = math.min(arg_126_0.level + 1, var_126_0)
		var_126_1 = true
	end

	if arg_126_0.level == var_126_0 then
		if arg_126_2 and arg_126_0:CanAccumulateExp() then
			arg_126_0.exp = math.min(arg_126_0.exp, pg.gameset.exp_overflow_max.key_value)
		elseif var_126_1 then
			arg_126_0.exp = 0
		end
	end
end

function var_0_0.getMaxLevel(arg_127_0)
	return arg_127_0.maxLevel
end

function var_0_0.canLevelUp(arg_128_0)
	local var_128_0 = arg_128_0:getLevelExpConfig(arg_128_0.level + 1)
	local var_128_1 = arg_128_0:getMaxLevel() <= arg_128_0.level

	return var_128_0 and arg_128_0:getLevelExpConfig().exp_interval <= arg_128_0.exp and not var_128_1
end

function var_0_0.getConfigMaxLevel(arg_129_0)
	return var_0_6.all[#var_0_6.all]
end

function var_0_0.isConfigMaxLevel(arg_130_0)
	return arg_130_0.level == arg_130_0:getConfigMaxLevel()
end

function var_0_0.updateMaxLevel(arg_131_0, arg_131_1)
	local var_131_0 = arg_131_0:getConfigMaxLevel()

	arg_131_0.maxLevel = math.max(math.min(var_131_0, arg_131_1), arg_131_0.maxLevel)
end

function var_0_0.getNextMaxLevel(arg_132_0)
	local var_132_0 = arg_132_0:getConfigMaxLevel()

	for iter_132_0 = arg_132_0:getMaxLevel() + 1, var_132_0 do
		if var_0_6[iter_132_0].level_limit == 1 then
			return iter_132_0
		end
	end
end

function var_0_0.canUpgrade(arg_133_0)
	if arg_133_0:isMetaShip() or arg_133_0:isBluePrintShip() then
		return false
	else
		local var_133_0 = var_0_8[arg_133_0.configId]

		assert(var_133_0, "不存在配置" .. arg_133_0.configId)

		return not arg_133_0:isMaxStar() and arg_133_0.level >= var_133_0.level
	end
end

function var_0_0.isReachNextMaxLevel(arg_134_0)
	return arg_134_0.level == arg_134_0:getMaxLevel() and arg_134_0:CanAccumulateExp() and arg_134_0:getNextMaxLevel() ~= nil
end

function var_0_0.isAwakening(arg_135_0)
	return arg_135_0:isReachNextMaxLevel() and arg_135_0.level < var_0_4
end

function var_0_0.isAwakening2(arg_136_0)
	return arg_136_0:isReachNextMaxLevel() and arg_136_0.level >= var_0_4
end

function var_0_0.notMaxLevelForFilter(arg_137_0)
	return arg_137_0.level ~= arg_137_0:getMaxLevel()
end

function var_0_0.getNextMaxLevelConsume(arg_138_0)
	local var_138_0 = arg_138_0:getMaxLevel()
	local var_138_1 = var_0_6[var_138_0]["need_item_rarity" .. arg_138_0:getConfig("rarity")]

	assert(var_138_1, "items  can not be nil")

	return _.map(var_138_1, function(arg_139_0)
		return {
			type = arg_139_0[1],
			id = arg_139_0[2],
			count = arg_139_0[3]
		}
	end)
end

function var_0_0.canUpgradeMaxLevel(arg_140_0)
	if not arg_140_0:isReachNextMaxLevel() then
		return false, i18n("upgrade_to_next_maxlevel_failed")
	else
		local var_140_0 = getProxy(PlayerProxy):getData()
		local var_140_1 = getProxy(BagProxy)
		local var_140_2 = arg_140_0:getNextMaxLevelConsume()

		for iter_140_0, iter_140_1 in pairs(var_140_2) do
			if iter_140_1.type == DROP_TYPE_RESOURCE then
				if var_140_0:getResById(iter_140_1.id) < iter_140_1.count then
					return false, i18n("common_no_resource")
				end
			elseif iter_140_1.type == DROP_TYPE_ITEM and var_140_1:getItemCountById(iter_140_1.id) < iter_140_1.count then
				return false, i18n("common_no_item_1")
			end
		end
	end

	return true
end

function var_0_0.CanAccumulateExp(arg_141_0)
	return pg.ship_data_template[arg_141_0.configId].can_get_proficency == 1
end

function var_0_0.getTotalExp(arg_142_0)
	return arg_142_0:getLevelExpConfig().exp_start + arg_142_0.exp
end

function var_0_0.getStartBattleExpend(arg_143_0)
	if table.contains(TeamType.SubShipType, arg_143_0:getShipType()) then
		return 0
	else
		return pg.ship_data_template[arg_143_0.configId].oil_at_start
	end
end

function var_0_0.getEndBattleExpend(arg_144_0)
	local var_144_0 = pg.ship_data_template[arg_144_0.configId]
	local var_144_1 = arg_144_0:getLevelExpConfig()

	return (math.floor(var_144_0.oil_at_end * var_144_1.fight_oil_ratio / 10000))
end

function var_0_0.getBattleTotalExpend(arg_145_0)
	return arg_145_0:getStartBattleExpend() + arg_145_0:getEndBattleExpend()
end

function var_0_0.getShipAmmo(arg_146_0)
	local var_146_0 = arg_146_0:getConfig(AttributeType.Ammo)

	for iter_146_0, iter_146_1 in pairs(arg_146_0:getAllSkills()) do
		local var_146_1 = tonumber(iter_146_0 .. string.format("%.2d", iter_146_1.level))
		local var_146_2 = pg.skill_benefit_template[var_146_1]

		if var_146_2 and arg_146_0:IsBenefitSkillActive(var_146_2) and (var_146_2.type == var_0_0.BENEFIT_EQUIP or var_146_2.type == var_0_0.BENEFIT_SKILL) then
			var_146_0 = var_146_0 + defaultValue(var_146_2.effect[1], 0)
		end
	end

	local var_146_3 = arg_146_0:getActiveEquipments()

	for iter_146_2, iter_146_3 in ipairs(var_146_3) do
		local var_146_4 = iter_146_3 and iter_146_3:getConfig("equip_parameters").ammo

		if var_146_4 then
			var_146_0 = var_146_0 + var_146_4
		end
	end

	return var_146_0
end

function var_0_0.getHuntingLv(arg_147_0)
	local var_147_0 = arg_147_0:getConfig("huntingrange_level")

	for iter_147_0, iter_147_1 in pairs(arg_147_0:getAllSkills()) do
		local var_147_1 = tonumber(iter_147_0 .. string.format("%.2d", iter_147_1.level))
		local var_147_2 = pg.skill_benefit_template[var_147_1]

		if var_147_2 and arg_147_0:IsBenefitSkillActive(var_147_2) and (var_147_2.type == var_0_0.BENEFIT_EQUIP or var_147_2.type == var_0_0.BENEFIT_SKILL) then
			var_147_0 = var_147_0 + defaultValue(var_147_2.effect[2], 0)
		end
	end

	local var_147_3 = arg_147_0:getActiveEquipments()

	for iter_147_2, iter_147_3 in ipairs(var_147_3) do
		local var_147_4 = iter_147_3 and iter_147_3:getConfig("equip_parameters").hunting_lv

		if var_147_4 then
			var_147_0 = var_147_0 + var_147_4
		end
	end

	return (math.min(var_147_0, arg_147_0:getMaxHuntingLv()))
end

function var_0_0.getMapAuras(arg_148_0)
	local var_148_0 = {}

	for iter_148_0, iter_148_1 in pairs(arg_148_0:getAllSkills()) do
		local var_148_1 = tonumber(iter_148_0 .. string.format("%.2d", iter_148_1.level))
		local var_148_2 = pg.skill_benefit_template[var_148_1]

		if var_148_2 and arg_148_0:IsBenefitSkillActive(var_148_2) and var_148_2.type == var_0_0.BENEFIT_MAP_AURA then
			local var_148_3 = {
				id = var_148_2.effect[1],
				level = iter_148_1.level
			}

			table.insert(var_148_0, var_148_3)
		end
	end

	return var_148_0
end

function var_0_0.getMapAids(arg_149_0)
	local var_149_0 = {}

	for iter_149_0, iter_149_1 in pairs(arg_149_0:getAllSkills()) do
		local var_149_1 = tonumber(iter_149_0 .. string.format("%.2d", iter_149_1.level))
		local var_149_2 = pg.skill_benefit_template[var_149_1]

		if var_149_2 and arg_149_0:IsBenefitSkillActive(var_149_2) and var_149_2.type == var_0_0.BENEFIT_AID then
			local var_149_3 = {
				id = var_149_2.effect[1],
				level = iter_149_1.level
			}

			table.insert(var_149_0, var_149_3)
		end
	end

	return var_149_0
end

var_0_0.BENEFIT_SKILL = 2
var_0_0.BENEFIT_EQUIP = 3
var_0_0.BENEFIT_MAP_AURA = 4
var_0_0.BENEFIT_AID = 5

function var_0_0.IsBenefitSkillActive(arg_150_0, arg_150_1)
	local var_150_0 = false

	if arg_150_1.type == var_0_0.BENEFIT_SKILL then
		if not arg_150_1.limit[1] or arg_150_1.limit[1] == arg_150_0.triggers.TeamNumbers then
			var_150_0 = true
		end
	elseif arg_150_1.type == var_0_0.BENEFIT_EQUIP then
		local var_150_1 = arg_150_1.limit
		local var_150_2 = arg_150_0:getAllEquipments()

		for iter_150_0, iter_150_1 in ipairs(var_150_2) do
			if iter_150_1 and table.contains(var_150_1, iter_150_1:getConfig("id")) then
				var_150_0 = true

				break
			end
		end
	elseif arg_150_1.type == var_0_0.BENEFIT_MAP_AURA then
		if arg_150_0.hpRant and arg_150_0.hpRant > 0 then
			return true
		end
	elseif arg_150_1.type == var_0_0.BENEFIT_AID and arg_150_0.hpRant and arg_150_0.hpRant > 0 then
		return true
	end

	return var_150_0
end

function var_0_0.getMaxHuntingLv(arg_151_0)
	return #arg_151_0:getConfig("hunting_range")
end

function var_0_0.getHuntingRange(arg_152_0, arg_152_1)
	local var_152_0 = arg_152_0:getConfig("hunting_range")
	local var_152_1 = Clone(var_152_0[1])
	local var_152_2 = arg_152_1 or arg_152_0:getHuntingLv()
	local var_152_3 = math.min(var_152_2, arg_152_0:getMaxHuntingLv())

	for iter_152_0 = 2, var_152_3 do
		_.each(var_152_0[iter_152_0], function(arg_153_0)
			table.insert(var_152_1, {
				arg_153_0[1],
				arg_153_0[2]
			})
		end)
	end

	return var_152_1
end

function var_0_0.getTriggerSkills(arg_154_0)
	local var_154_0 = {}
	local var_154_1 = arg_154_0:getSkillEffects()

	_.each(var_154_1, function(arg_155_0)
		if arg_155_0.type == "AddBuff" and arg_155_0.arg_list and arg_155_0.arg_list.buff_id then
			local var_155_0 = arg_155_0.arg_list.buff_id

			var_154_0[var_155_0] = {
				id = var_155_0,
				level = arg_155_0.level
			}
		end
	end)

	return var_154_0
end

function var_0_0.GetEquipmentSkills(arg_156_0)
	local var_156_0 = {}
	local var_156_1 = arg_156_0:getActiveEquipments()

	for iter_156_0, iter_156_1 in ipairs(var_156_1) do
		if iter_156_1 then
			local var_156_2 = iter_156_1:getConfig("skill_id")[1]

			if var_156_2 then
				var_156_0[var_156_2] = {
					level = 1,
					id = var_156_2
				}
			end
		end
	end

	;(function()
		local var_157_0 = arg_156_0:GetSpWeapon()
		local var_157_1 = var_157_0 and var_157_0:GetEffect() or 0

		if var_157_1 > 0 then
			var_156_0[var_157_1] = {
				level = 1,
				id = var_157_1
			}
		end
	end)()

	return var_156_0
end

function var_0_0.getAllSkills(arg_158_0)
	local var_158_0 = Clone(arg_158_0.skills)

	for iter_158_0, iter_158_1 in pairs(arg_158_0:GetEquipmentSkills()) do
		var_158_0[iter_158_0] = iter_158_1
	end

	for iter_158_2, iter_158_3 in pairs(arg_158_0:getTriggerSkills()) do
		var_158_0[iter_158_2] = iter_158_3
	end

	return var_158_0
end

function var_0_0.isSameKind(arg_159_0, arg_159_1)
	return pg.ship_data_template[arg_159_0.configId].group_type == pg.ship_data_template[arg_159_1.configId].group_type
end

function var_0_0.GetLockState(arg_160_0)
	return arg_160_0.lockState
end

function var_0_0.IsLocked(arg_161_0)
	return arg_161_0.lockState == var_0_0.LOCK_STATE_LOCK
end

function var_0_0.SetLockState(arg_162_0, arg_162_1)
	arg_162_0.lockState = arg_162_1
end

function var_0_0.GetPreferenceTag(arg_163_0)
	return arg_163_0.preferenceTag or 0
end

function var_0_0.IsPreferenceTag(arg_164_0)
	return arg_164_0:GetPreferenceTag() == var_0_0.PREFERENCE_TAG_COMMON
end

function var_0_0.SetPreferenceTag(arg_165_0, arg_165_1)
	arg_165_0.preferenceTag = arg_165_1
end

function var_0_0.calReturnRes(arg_166_0)
	local var_166_0 = pg.ship_data_by_type[arg_166_0:getShipType()]
	local var_166_1 = var_166_0.distory_resource_gold_ratio
	local var_166_2 = var_166_0.distory_resource_oil_ratio
	local var_166_3 = pg.ship_data_by_star[arg_166_0:getConfig("rarity")].destory_item

	return var_166_1, 0, var_166_3
end

function var_0_0.getRarity(arg_167_0)
	local var_167_0 = arg_167_0:getConfig("rarity")

	if arg_167_0:isRemoulded() then
		var_167_0 = var_167_0 + 1
	end

	return var_167_0
end

function var_0_0.getExchangePrice(arg_168_0)
	local var_168_0 = arg_168_0:getConfig("rarity")

	return pg.ship_data_by_star[var_168_0].exchange_price
end

function var_0_0.updateSkill(arg_169_0, arg_169_1)
	local var_169_0 = arg_169_1.skill_id or arg_169_1.id
	local var_169_1 = arg_169_1.skill_lv or arg_169_1.lv or arg_169_1.level
	local var_169_2 = arg_169_1.skill_exp or arg_169_1.exp

	arg_169_0.skills[var_169_0] = {
		id = var_169_0,
		level = var_169_1,
		exp = var_169_2
	}
end

function var_0_0.canEquipAtPos(arg_170_0, arg_170_1, arg_170_2)
	local var_170_0, var_170_1 = arg_170_0:isForbiddenAtPos(arg_170_1, arg_170_2)

	if var_170_0 then
		return false, var_170_1
	end

	for iter_170_0, iter_170_1 in ipairs(arg_170_0.equipments) do
		if iter_170_1 and iter_170_0 ~= arg_170_2 and iter_170_1:getConfig("equip_limit") ~= 0 and arg_170_1:getConfig("equip_limit") == iter_170_1:getConfig("equip_limit") then
			return false, i18n("ship_equip_same_group_equipment")
		end
	end

	return true
end

function var_0_0.isForbiddenAtPos(arg_171_0, arg_171_1, arg_171_2)
	local var_171_0 = pg.ship_data_template[arg_171_0.configId]

	assert(var_171_0, "can not find ship in ship_data_templtae: " .. arg_171_0.configId)

	local var_171_1 = var_171_0["equip_" .. arg_171_2]

	if not table.contains(var_171_1, arg_171_1:getConfig("type")) then
		return true, i18n("common_limit_equip")
	end

	if table.contains(arg_171_1:getConfig("ship_type_forbidden"), arg_171_0:getShipType()) then
		return true, i18n("common_limit_equip")
	end

	return false
end

function var_0_0.canEquipCommander(arg_172_0, arg_172_1)
	if arg_172_1:getShipType() ~= arg_172_0:getShipType() then
		return false, i18n("commander_type_unmatch")
	end

	return true
end

function var_0_0.upgrade(arg_173_0)
	local var_173_0 = pg.ship_data_transform[arg_173_0.configId]

	if var_173_0.trans_id and var_173_0.trans_id > 0 then
		arg_173_0.configId = var_173_0.trans_id
		arg_173_0.star = arg_173_0:getConfig("star")
	end
end

function var_0_0.getTeamType(arg_174_0)
	return TeamType.GetTeamFromShipType(arg_174_0:getShipType())
end

function var_0_0.getFleetName(arg_175_0)
	local var_175_0 = arg_175_0:getTeamType()

	return var_0_1[var_175_0]
end

function var_0_0.getMaxConfigId(arg_176_0)
	local var_176_0 = pg.ship_data_template
	local var_176_1

	for iter_176_0 = 4, 1, -1 do
		local var_176_2 = tonumber(arg_176_0.groupId .. iter_176_0)

		if var_176_0[var_176_2] then
			var_176_1 = var_176_2

			break
		end
	end

	return var_176_1
end

function var_0_0.getFlag(arg_177_0, arg_177_1, arg_177_2)
	return pg.ShipFlagMgr.GetInstance():GetShipFlag(arg_177_0.id, arg_177_1, arg_177_2)
end

function var_0_0.hasAnyFlag(arg_178_0, arg_178_1)
	return _.any(arg_178_1, function(arg_179_0)
		return arg_178_0:getFlag(arg_179_0)
	end)
end

function var_0_0.isBreakOut(arg_180_0)
	return arg_180_0.configId % 10 > 1
end

function var_0_0.fateSkillChange(arg_181_0, arg_181_1)
	if not arg_181_0.skillChangeList then
		arg_181_0.skillChangeList = arg_181_0:isBluePrintShip() and arg_181_0:getBluePrint():getChangeSkillList() or {}
	end

	for iter_181_0, iter_181_1 in ipairs(arg_181_0.skillChangeList) do
		if iter_181_1[1] == arg_181_1 and arg_181_0.skills[iter_181_1[2]] then
			return iter_181_1[2]
		end
	end

	return arg_181_1
end

function var_0_0.RemapSkillId(arg_182_0, arg_182_1)
	local var_182_0 = arg_182_0:GetSpWeapon()

	if var_182_0 then
		return var_182_0:RemapSkillId(arg_182_1)
	end

	return arg_182_1
end

function var_0_0.getSkillList(arg_183_0)
	local var_183_0 = pg.ship_data_template[arg_183_0.configId]
	local var_183_1 = Clone(var_183_0.buff_list_display)
	local var_183_2 = Clone(var_183_0.buff_list)
	local var_183_3 = pg.ship_data_trans[arg_183_0.groupId]
	local var_183_4 = 0

	if var_183_3 and var_183_3.skill_id ~= 0 then
		local var_183_5 = var_183_3.skill_id
		local var_183_6 = pg.transform_data_template[var_183_5]

		if arg_183_0.transforms[var_183_5] and var_183_6.skill_id ~= 0 then
			table.insert(var_183_2, var_183_6.skill_id)
		end
	end

	local var_183_7 = {}

	for iter_183_0, iter_183_1 in ipairs(var_183_1) do
		for iter_183_2, iter_183_3 in ipairs(var_183_2) do
			if iter_183_1 == iter_183_3 then
				table.insert(var_183_7, arg_183_0:fateSkillChange(iter_183_1))
			end
		end
	end

	return var_183_7
end

function var_0_0.getModAttrTopLimit(arg_184_0, arg_184_1)
	local var_184_0 = ShipModAttr.ATTR_TO_INDEX[arg_184_1]
	local var_184_1 = pg.ship_data_template[arg_184_0.configId].strengthen_id
	local var_184_2 = pg.ship_data_strengthen[var_184_1].durability[var_184_0]

	return calcFloor((3 + 7 * (math.min(arg_184_0.level, 100) / 100)) * var_184_2 * 0.1)
end

function var_0_0.leftModAdditionPoint(arg_185_0, arg_185_1)
	local var_185_0 = arg_185_0:getModProperties(arg_185_1)
	local var_185_1 = arg_185_0:getModExpRatio(arg_185_1)
	local var_185_2 = arg_185_0:getModAttrTopLimit(arg_185_1)
	local var_185_3 = calcFloor(var_185_0 / var_185_1)

	return math.max(0, var_185_2 - var_185_3)
end

function var_0_0.getModAttrBaseMax(arg_186_0, arg_186_1)
	if not table.contains(arg_186_0:getConfig("lock"), arg_186_1) then
		local var_186_0 = arg_186_0:leftModAdditionPoint(arg_186_1)
		local var_186_1 = arg_186_0:getShipProperties()

		return calcFloor(var_186_1[arg_186_1] + var_186_0)
	else
		return 0
	end
end

function var_0_0.getModExpRatio(arg_187_0, arg_187_1)
	if not table.contains(arg_187_0:getConfig("lock"), arg_187_1) then
		local var_187_0 = pg.ship_data_template[arg_187_0.configId].strengthen_id

		assert(pg.ship_data_strengthen[var_187_0], "ship_data_strengthen>>>>>>" .. var_187_0)

		return math.max(pg.ship_data_strengthen[var_187_0].level_exp[ShipModAttr.ATTR_TO_INDEX[arg_187_1]], 1)
	else
		return 1
	end
end

function var_0_0.inUnlockTip(arg_188_0)
	local var_188_0 = pg.gameset.tip_unlock_shipIds.description[0]

	return table.contains(var_188_0, arg_188_0)
end

function var_0_0.proposeSkinOwned(arg_189_0, arg_189_1)
	return arg_189_1 and arg_189_0.propose and arg_189_1.skin_type == ShipSkin.SKIN_TYPE_PROPOSE
end

function var_0_0.getProposeSkin(arg_190_0)
	return ShipSkin.GetSkinByType(arg_190_0.groupId, ShipSkin.SKIN_TYPE_PROPOSE)
end

function var_0_0.getDisplaySkillIds(arg_191_0)
	return _.map(pg.ship_data_template[arg_191_0.configId].buff_list_display, function(arg_192_0)
		return arg_191_0:fateSkillChange(arg_192_0)
	end)
end

function var_0_0.isFullSkillLevel(arg_193_0)
	local var_193_0 = pg.skill_data_template

	for iter_193_0, iter_193_1 in pairs(arg_193_0.skills) do
		if var_193_0[iter_193_1.id].max_level ~= iter_193_1.level then
			return false
		end
	end

	return true
end

function var_0_0.setEquipmentRecord(arg_194_0, arg_194_1, arg_194_2)
	local var_194_0 = "equipment_record" .. "_" .. arg_194_1 .. "_" .. arg_194_0.id

	PlayerPrefs.SetString(var_194_0, table.concat(_.flatten(arg_194_2), ":"))
	PlayerPrefs.Save()
end

function var_0_0.getEquipmentRecord(arg_195_0, arg_195_1)
	if not arg_195_0.equipmentRecords then
		local var_195_0 = "equipment_record" .. "_" .. arg_195_1 .. "_" .. arg_195_0.id
		local var_195_1 = string.split(PlayerPrefs.GetString(var_195_0) or "", ":")
		local var_195_2 = {}

		for iter_195_0 = 1, 3 do
			var_195_2[iter_195_0] = _.map(_.slice(var_195_1, 5 * iter_195_0 - 4, 5), function(arg_196_0)
				return tonumber(arg_196_0)
			end)
		end

		arg_195_0.equipmentRecords = var_195_2
	end

	return arg_195_0.equipmentRecords
end

function var_0_0.SetSpWeaponRecord(arg_197_0, arg_197_1, arg_197_2)
	local var_197_0 = "spweapon_record" .. "_" .. arg_197_1 .. "_" .. arg_197_0.id
	local var_197_1 = _.map({
		1,
		2,
		3
	}, function(arg_198_0)
		local var_198_0 = arg_197_2[arg_198_0]

		if var_198_0 then
			return (var_198_0:GetUID() or 0) .. "," .. var_198_0:GetConfigID()
		else
			return "0,0"
		end
	end)

	PlayerPrefs.SetString(var_197_0, table.concat(var_197_1, ":"))
	PlayerPrefs.Save()
end

function var_0_0.GetSpWeaponRecord(arg_199_0, arg_199_1)
	local var_199_0 = "spweapon_record" .. "_" .. arg_199_1 .. "_" .. arg_199_0.id

	return (_.map(string.split(PlayerPrefs.GetString(var_199_0, ""), ":"), function(arg_200_0)
		local var_200_0 = string.split(arg_200_0, ",")

		assert(var_200_0)

		local var_200_1 = tonumber(var_200_0[1])
		local var_200_2 = tonumber(var_200_0[2])

		if not var_200_2 or var_200_2 == 0 then
			return false
		end

		local var_200_3 = getProxy(EquipmentProxy):GetSpWeaponByUid(var_200_1) or _.detect(getProxy(BayProxy):GetSpWeaponsInShips(), function(arg_201_0)
			return arg_201_0:GetUID() == var_200_1
		end)

		var_200_3 = var_200_3 or SpWeapon.New({
			id = var_200_2
		})

		return var_200_3
	end))
end

function var_0_0.hasEquipEquipmentSkin(arg_202_0)
	for iter_202_0, iter_202_1 in ipairs(arg_202_0.equipments) do
		if iter_202_1 and iter_202_1:hasSkin() then
			return true
		end
	end

	return false
end

function var_0_0.hasCommander(arg_203_0)
	return arg_203_0.commanderId and arg_203_0.commanderId ~= 0
end

function var_0_0.getCommander(arg_204_0)
	return arg_204_0.commanderId
end

function var_0_0.setCommander(arg_205_0, arg_205_1)
	arg_205_0.commanderId = arg_205_1
end

function var_0_0.getSkillIndex(arg_206_0, arg_206_1)
	local var_206_0 = arg_206_0:getSkillList()

	for iter_206_0, iter_206_1 in ipairs(var_206_0) do
		if arg_206_1 == iter_206_1 then
			return iter_206_0
		end
	end
end

function var_0_0.getTactics(arg_207_0)
	return 1, "tactics_attack"
end

function var_0_0.IsBgmSkin(arg_208_0)
	local var_208_0 = arg_208_0:GetSkinConfig()

	return table.contains(var_208_0.tag, ShipSkin.WITH_BGM)
end

function var_0_0.GetSkinBgm(arg_209_0)
	if arg_209_0:IsBgmSkin() then
		return arg_209_0:GetSkinConfig().bgm
	end
end

function var_0_0.isIntensifyMax(arg_210_0)
	local var_210_0 = intProperties(arg_210_0:getShipProperties())

	if arg_210_0:isBluePrintShip() then
		return true
	end

	for iter_210_0, iter_210_1 in pairs(ShipModAttr.ID_TO_ATTR) do
		if arg_210_0:getModAttrBaseMax(iter_210_1) ~= var_210_0[iter_210_1] then
			return false
		end
	end

	return true
end

function var_0_0.isRemouldable(arg_211_0)
	return not arg_211_0:isTestShip() and not arg_211_0:isBluePrintShip() and pg.ship_data_trans[arg_211_0.groupId]
end

function var_0_0.isAllRemouldFinish(arg_212_0)
	local var_212_0 = pg.ship_data_trans[arg_212_0.groupId]

	assert(var_212_0, "this ship group without remould config:" .. arg_212_0.groupId)

	for iter_212_0, iter_212_1 in ipairs(var_212_0.transform_list) do
		for iter_212_2, iter_212_3 in ipairs(iter_212_1) do
			local var_212_1 = pg.transform_data_template[iter_212_3[2]]

			if #var_212_1.edit_trans > 0 then
				-- block empty
			elseif not arg_212_0.transforms[iter_212_3[2]] or arg_212_0.transforms[iter_212_3[2]].level < var_212_1.max_level then
				return false
			end
		end
	end

	return true
end

function var_0_0.isSpecialFilter(arg_213_0)
	local var_213_0 = pg.ship_data_statistics[arg_213_0.configId]

	assert(var_213_0, "this ship without statistics:" .. arg_213_0.configId)

	for iter_213_0, iter_213_1 in ipairs(var_213_0.tag_list) do
		if iter_213_1 == "special" then
			return true
		end
	end

	return false
end

function var_0_0.hasAvailiableSkin(arg_214_0)
	local var_214_0 = getProxy(ShipSkinProxy)
	local var_214_1 = var_214_0:GetAllSkinForShip(arg_214_0)
	local var_214_2 = var_214_0:getRawData()
	local var_214_3 = 0

	for iter_214_0, iter_214_1 in ipairs(var_214_1) do
		if arg_214_0:proposeSkinOwned(iter_214_1) or var_214_2[iter_214_1.id] then
			var_214_3 = var_214_3 + 1
		end
	end

	return var_214_3 > 0
end

function var_0_0.hasProposeSkin(arg_215_0)
	local var_215_0 = getProxy(ShipSkinProxy)
	local var_215_1 = var_215_0:GetAllSkinForShip(arg_215_0)

	for iter_215_0, iter_215_1 in ipairs(var_215_1) do
		if iter_215_1.skin_type == ShipSkin.SKIN_TYPE_PROPOSE then
			return true
		end
	end

	local var_215_2 = var_215_0:GetShareSkinsForShip(arg_215_0)

	for iter_215_2, iter_215_3 in ipairs(var_215_2) do
		if iter_215_3.skin_type == ShipSkin.SKIN_TYPE_PROPOSE then
			return true
		end
	end

	return false
end

function var_0_0.HasUniqueSpWeapon(arg_216_0)
	return tobool(pg.spweapon_data_statistics.get_id_list_by_unique[arg_216_0:getGroupId()])
end

function var_0_0.getAircraftReloadCD(arg_217_0)
	local var_217_0 = arg_217_0:getConfigTable().base_list
	local var_217_1 = arg_217_0:getConfigTable().default_equip_list
	local var_217_2 = 0
	local var_217_3 = 0

	for iter_217_0 = 1, 3 do
		local var_217_4 = arg_217_0:getEquip(iter_217_0)
		local var_217_5 = var_217_4 and var_217_4.configId or var_217_1[iter_217_0]
		local var_217_6 = Equipment.getConfigData(var_217_5).type

		if underscore.any(EquipType.AirEquipTypes, function(arg_218_0)
			return var_217_6 == arg_218_0
		end) then
			var_217_2 = var_217_2 + Equipment.GetEquipReloadStatic(var_217_5) * var_217_0[iter_217_0]
			var_217_3 = var_217_3 + var_217_0[iter_217_0]
		end
	end

	local var_217_7 = ys.Battle.BattleConfig.AIR_ASSIST_RELOAD_RATIO * pg.bfConsts.PERCENT

	return {
		name = i18n("equip_info_31"),
		type = AttributeType.CD,
		value = var_217_2 / var_217_3 * var_217_7
	}
end

function var_0_0.IsTagShip(arg_219_0, arg_219_1)
	local var_219_0 = arg_219_0:getConfig("tag_list")

	return table.contains(var_219_0, arg_219_1)
end

function var_0_0.setReMetaSpecialItemVO(arg_220_0, arg_220_1)
	arg_220_0.reMetaSpecialItemVO = arg_220_1
end

function var_0_0.getReMetaSpecialItemVO(arg_221_0, arg_221_1)
	return arg_221_0.reMetaSpecialItemVO
end

function var_0_0.getProposeType(arg_222_0)
	if arg_222_0:isMetaShip() then
		return "meta"
	elseif arg_222_0:IsXIdol() then
		return "imas"
	else
		return "default"
	end
end

function var_0_0.IsXIdol(arg_223_0)
	return arg_223_0:getNation() == Nation.IDOL_LINK
end

function var_0_0.getSpecificType(arg_224_0)
	return pg.ship_data_template[arg_224_0.configId].specific_type
end

function var_0_0.GetSpWeapon(arg_225_0)
	return arg_225_0.spWeapon
end

function var_0_0.UpdateSpWeapon(arg_226_0, arg_226_1)
	local var_226_0 = (arg_226_1 and arg_226_1:GetUID() or 0) == (arg_226_0.spWeapon and arg_226_0.spWeapon:GetUID() or 0)

	arg_226_0.spWeapon = arg_226_1

	if arg_226_1 then
		arg_226_1:SetShipId(arg_226_0.id)
	end

	if var_226_0 then
		pg.m02:sendNotification(EquipmentProxy.SPWEAPONS_UPDATED)
	end
end

function var_0_0.CanEquipSpWeapon(arg_227_0, arg_227_1)
	local var_227_0, var_227_1 = arg_227_0:IsSpWeaponForbidden(arg_227_1)

	if var_227_0 then
		return false, var_227_1
	end

	return true
end

function var_0_0.IsSpWeaponForbidden(arg_228_0, arg_228_1)
	local var_228_0 = arg_228_1:GetWearableShipTypes()
	local var_228_1 = arg_228_0:getShipType()

	if not table.contains(var_228_0, var_228_1) then
		return true, i18n("spweapon_tip_group_error")
	end

	local var_228_2 = arg_228_1:GetUniqueGroup()
	local var_228_3 = arg_228_0:getGroupId()

	if var_228_2 ~= 0 and var_228_2 ~= var_228_3 then
		return true, i18n("spweapon_tip_group_error")
	end

	return false
end

function var_0_0.GetMapStrikeAnim(arg_229_0)
	local var_229_0
	local var_229_1 = arg_229_0:getShipType()

	switch(TeamType.GetTeamFromShipType(var_229_1), {
		[TeamType.Main] = function()
			if ShipType.IsTypeQuZhu(var_229_1) then
				var_229_0 = "SubTorpedoUI"
			elseif ShipType.ContainInLimitBundle(ShipType.BundleAircraftCarrier, var_229_1) then
				var_229_0 = "AirStrikeUI"
			elseif ShipType.ContainInLimitBundle(ShipType.BundleBattleShip, var_229_1) then
				var_229_0 = "CannonUI"
			else
				var_229_0 = "CannonUI"
			end
		end,
		[TeamType.Vanguard] = function()
			if ShipType.IsTypeQuZhu(var_229_1) then
				var_229_0 = "SubTorpedoUI"
			end
		end,
		[TeamType.Submarine] = function()
			if arg_229_0:getNation() == Nation.MOT then
				var_229_0 = "CannonUI"
			else
				var_229_0 = "SubTorpedoUI"
			end
		end
	})

	return var_229_0
end

function var_0_0.IsDefaultSkin(arg_233_0)
	return arg_233_0.skinId == 0 or arg_233_0.skinId == arg_233_0:getConfig("skin_id")
end

function var_0_0.IsMatchKey(arg_234_0, arg_234_1)
	if not arg_234_1 or arg_234_1 == "" then
		return true
	end

	arg_234_1 = string.lower(string.gsub(arg_234_1, "%.", "%%."))

	return string.find(string.lower(arg_234_0:GetDefaultName()), arg_234_1)
end

function var_0_0.IsOwner(arg_235_0)
	return tobool(arg_235_0.id)
end

function var_0_0.GetUniqueId(arg_236_0)
	return arg_236_0.id
end

function var_0_0.ShowPropose(arg_237_0)
	if not arg_237_0.propose then
		return false
	else
		return not HXSet.isHxPropose() or arg_237_0:IsOwner() and arg_237_0:GetUniqueId() == getProxy(PlayerProxy):getRawData():GetProposeShipId()
	end
end

function var_0_0.GetColorName(arg_238_0, arg_238_1)
	arg_238_1 = arg_238_1 or arg_238_0:getName()

	if PlayerPrefs.GetInt("SHIP_NAME_COLOR", PLATFORM_CODE == PLATFORM_CH and 1 or 0) == 1 and arg_238_0.propose then
		return setColorStr(arg_238_1, "#FFAACEFF")
	else
		return arg_238_1
	end
end

local var_0_9 = {
	effect = {
		"duang_meta_jiehun",
		"duang_6_jiehun_tuzhi",
		"duang_6_jiehun",
		"duang_meta_%s",
		"duang_6"
	},
	frame = {
		"prop4_1",
		"prop%s",
		"prop"
	}
}

function var_0_0.GetFrameAndEffect(arg_239_0, arg_239_1)
	arg_239_1 = tobool(arg_239_1)

	local var_239_0
	local var_239_1

	if arg_239_0.propose then
		if arg_239_0:isMetaShip() then
			var_239_1 = string.format(var_0_9.effect[1])
			var_239_0 = string.format(var_0_9.frame[1])
		elseif arg_239_0:isBluePrintShip() then
			var_239_1 = string.format(var_0_9.effect[2])
			var_239_0 = string.format(var_0_9.frame[2], arg_239_0:rarity2bgPrint())
		else
			var_239_1 = string.format(var_0_9.effect[3])
			var_239_0 = string.format(var_0_9.frame[3])
		end

		if not arg_239_0:ShowPropose() then
			var_239_0 = nil
		end
	elseif arg_239_0:isMetaShip() then
		var_239_1 = string.format(var_0_9.effect[4], arg_239_0:rarity2bgPrint())
	elseif arg_239_0:getRarity() == ShipRarity.SSR then
		var_239_1 = string.format(var_0_9.effect[5])
	end

	if arg_239_1 then
		var_239_1 = var_239_1 and var_239_1 .. "_1"
	end

	return var_239_0, var_239_1
end

function var_0_0.GetRecordPosKey(arg_240_0)
	return arg_240_0.skinId
end

return var_0_0
