local var_0_0 = class("Equipment", import(".BaseVO"))

var_0_0.EQUIPMENT_STATE_LOCK = 1
var_0_0.EQUIPMENT_STATE_EMPTY = 0
var_0_0.EQUIPMENT_NORMAL = 1
var_0_0.EQUIPMENT_IMPORTANCE = 2

local var_0_1 = pg.equip_skin_template

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1.id
	arg_1_0.configId = arg_1_1.config_id or arg_1_0.id

	arg_1_0.InitConfig()

	arg_1_0.count = defaultValue(arg_1_1.count, 0)
	arg_1_0.new = defaultValue(arg_1_1.new, 0)
	arg_1_0.isSkin = defaultValue(arg_1_1.isSkin, False)
	arg_1_0.skinId = arg_1_1.skinId or 0

def var_0_0.getConfigData(arg_2_0):
	local var_2_0 = {
		pg.equip_data_statistics,
		pg.equip_data_template
	}
	local var_2_1

	if underscore.any(var_2_0, function(arg_3_0)
		return arg_3_0[arg_2_0] != None):
		var_2_1 = setmetatable({}, {
			def __index:(arg_4_0, arg_4_1)
				for iter_4_0, iter_4_1 in ipairs(var_2_0):
					if iter_4_1[arg_2_0] and iter_4_1[arg_2_0][arg_4_1] != None:
						arg_4_0[arg_4_1] = iter_4_1[arg_2_0][arg_4_1]

						return arg_4_0[arg_4_1]
		})

		local var_2_2 = var_2_1.weapon_id

		if var_2_2 and #var_2_2 > 0:
			local var_2_3 = pg.weapon_property[var_2_2[1]]

			var_2_1[AttributeType.CD] = var_2_3 and var_2_3.reload_max

	return var_2_1

def var_0_0.InitConfig(arg_5_0):
	arg_5_0.cfg = var_0_0.getConfigData(arg_5_0.configId)

	if not IsUnityEditor:
		arg_5_0.config = arg_5_0.cfg

	assert(arg_5_0.cfg, string.format("without equip config from id_%d", arg_5_0.id))

def var_0_0.getConfigTable(arg_6_0):
	return arg_6_0.cfg

def var_0_0.GetAttributes(arg_7_0):
	local var_7_0 = {}

	for iter_7_0 = 1, 3:
		local var_7_1 = arg_7_0.getConfig("attribute_" .. iter_7_0)
		local var_7_2 = arg_7_0.getConfig("value_" .. iter_7_0)

		var_7_0[iter_7_0] = var_7_1 != None and {
			type = var_7_1,
			value = string.match(var_7_2, "^[%d|\\.]+$") and tonumber(var_7_2) or var_7_2,
			auxBoost = arg_7_0.isDevice()
		} or False

	return var_7_0

def var_0_0.GetPropertyRate(arg_8_0):
	return arg_8_0.getConfig("property_rate")

def var_0_0.CanInBag(arg_9_0):
	return tobool(pg.equip_data_template[arg_9_0])

def var_0_0.vertify(arg_10_0):
	local var_10_0 = pg.equip_data_statistics[arg_10_0.configId]
	local var_10_1 = pg.equip_data_template[arg_10_0.configId]

	if arg_10_0.getConfig("value_1") != var_10_0.value_1 or arg_10_0.getConfig("value_2") != var_10_0.value_2:
		return False

	return True

def var_0_0.CalcWeanponCD(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_0 or 0
	local var_11_1 = arg_11_1 and arg_11_1.getProperties().reload or 100

	return string.format("%0.2f", ys.Battle.BattleFormulas.CalculateReloadTime(var_11_0, var_11_1))

local var_0_2 = {
	attribute_cd = "cd_normal",
	equip_info_34 = "equip_info_33"
}
local var_0_3

local function var_0_4(arg_12_0)
	if not var_0_3:
		var_0_3 = {}

		for iter_12_0, iter_12_1 in pairs(var_0_2):
			var_0_3[i18n(iter_12_0)] = i18n(iter_12_1)

	return var_0_3[arg_12_0]

def var_0_0.GetInfoTrans(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_0.name
	local var_13_1 = arg_13_0.value
	local var_13_2 = arg_13_0.auxBoost

	if arg_13_0.type == AttributeType.CD:
		var_13_1 = var_0_0.CalcWeanponCD(var_13_1, arg_13_1) .. "s" .. pg.equip_data_code.WAVE.text
	elif arg_13_0.type == AttributeType.AirDurability:
		local var_13_3 = arg_13_1 and arg_13_1.level or 100

		var_13_1 = math.floor(var_13_1[1] + var_13_1[2] * (var_13_3 - 1) / 1000)
	elif arg_13_0.type == AttributeType.AntiSiren:
		var_13_1 = math.floor(var_13_1 / 100)
		var_13_1 = (var_13_1 > 0 and "+" or var_13_1 < 0 and "-" or "") .. var_13_1 .. "%"

	var_13_0 = var_13_0 or AttributeType.Type2Name(arg_13_0.type)

	if not arg_13_1:
		var_13_0 = defaultValue(var_0_4(var_13_0), var_13_0)

	var_13_1 = var_13_1 or ""
	var_13_2 = var_13_2 and arg_13_1 and table.contains(arg_13_1.getSpecificType(), ShipType.SpecificTypeTable.auxiliary)

	return var_13_0, var_13_1, var_13_2

local function var_0_5(arg_14_0)
	local var_14_0 = pg.equip_data_code.WAVE.text

	if string.match(arg_14_0, var_14_0):
		arg_14_0 = string.gsub(arg_14_0, var_14_0, "")

	arg_14_0 = string.gsub(arg_14_0, " ", "")

	local var_14_1 = {
		string.match(arg_14_0, "~(%d+)")
	}

	if #var_14_1 > 0:
		arg_14_0 = string.gsub(arg_14_0, "~" .. var_14_1[1], "")

	local var_14_2 = {
		string.match(arg_14_0, "(%d+)x(%d+)")
	}

	while #var_14_2 > 0:
		local var_14_3 = var_14_2[1]
		local var_14_4 = var_14_2[2]

		arg_14_0 = string.gsub(arg_14_0, var_14_3 .. "x" .. var_14_4, var_14_3 * var_14_4, 1)
		var_14_2 = {
			string.match(arg_14_0, "(%d+)x(%d+)")
		}

	return tonumber(arg_14_0)

def var_0_0.AlignAttrs(arg_15_0, arg_15_1):
	for iter_15_0 = 1, #arg_15_0:
		if not arg_15_1[iter_15_0] or arg_15_0[iter_15_0].type != arg_15_1[iter_15_0].type:
			table.insert(arg_15_1, iter_15_0, Clone(arg_15_0[iter_15_0]))

			arg_15_1[iter_15_0].value = 0

			for iter_15_1 = iter_15_0 + 1, #arg_15_1:
				if arg_15_1[iter_15_0].type == arg_15_1[iter_15_1].type:
					arg_15_1[iter_15_0].value = arg_15_1[iter_15_1].value

					table.remove(arg_15_1, iter_15_1)

					break

	for iter_15_2 = #arg_15_0 + 1, #arg_15_1:
		table.insert(arg_15_0, Clone(arg_15_1[iter_15_2]))

		arg_15_0[iter_15_2].value = 0

def var_0_0.CompareInfo(arg_16_0, arg_16_1, arg_16_2):
	if arg_16_0.type == AttributeType.Damage:
		local var_16_0 = var_0_5(arg_16_0.value)

		arg_16_1.compare = var_0_5(arg_16_1.value) - var_16_0
	elif arg_16_0.type == AttributeType.CD:
		local var_16_1 = var_0_0.CalcWeanponCD(arg_16_0.value, arg_16_2)

		arg_16_1.compare = -(var_0_0.CalcWeanponCD(arg_16_1.value, arg_16_2) - var_16_1)
	else
		arg_16_1.compare = arg_16_1.value - arg_16_0.value

def var_0_0.InsertAttrsUpgrade(arg_17_0, arg_17_1, arg_17_2):
	var_0_0.AlignAttrs(arg_17_0, arg_17_1)

	for iter_17_0 = #arg_17_0, 1, -1:
		if arg_17_0[iter_17_0].value == arg_17_1[iter_17_0].value:
			if not arg_17_2:
				table.remove(arg_17_0, iter_17_0)
				table.remove(arg_17_1, iter_17_0)
		else
			arg_17_0[iter_17_0].nextValue = arg_17_1[iter_17_0].value

def var_0_0.InsertAttrsCompare(arg_18_0, arg_18_1, arg_18_2):
	var_0_0.AlignAttrs(arg_18_0, arg_18_1)

	for iter_18_0 = 1, #arg_18_0:
		var_0_0.CompareInfo(arg_18_0[iter_18_0], arg_18_1[iter_18_0], arg_18_2)

def var_0_0.GetPropertiesInfo(arg_19_0):
	local var_19_0 = {
		attrs = {}
	}

	if arg_19_0.getConfig(AttributeType.Damage):
		table.insert(var_19_0.attrs, {
			type = AttributeType.Damage,
			value = arg_19_0.getConfig(AttributeType.Damage)
		})

	if arg_19_0.getConfig(AttributeType.CD):
		local var_19_1 = {
			type = AttributeType.CD,
			value = arg_19_0.getConfig(AttributeType.CD)
		}

		table.insert(var_19_0.attrs, var_19_1)

		if arg_19_0.isAircraftExtend() and arg_19_0.getConfig("weapon_id"):
			var_19_1.sub = {}

			for iter_19_0, iter_19_1 in ipairs(arg_19_0.getConfig("weapon_id")):
				if pg.weapon_property[iter_19_1].type == 11:
					table.insert(var_19_1.sub, {
						name = i18n("equip_info_34"),
						type = AttributeType.CD,
						value = pg.weapon_property[iter_19_1].reload_max
					})

	for iter_19_2, iter_19_3 in ipairs(arg_19_0.GetAttributes()):
		if iter_19_3 and iter_19_3.type != AttributeType.OxyRaidDistance:
			table.insert(var_19_0.attrs, iter_19_3)

	if arg_19_0.GetAntiSirenPower():
		table.insert(var_19_0.attrs, {
			type = AttributeType.AntiSiren,
			value = arg_19_0.GetAntiSirenPower()
		})

	local var_19_2 = arg_19_0.GetSonarProperty()

	if var_19_2:
		table.insert(var_19_0.attrs, {
			type = AttributeType.SonarRange,
			value = var_19_2[AttributeType.SonarRange]
		})

	var_19_0.weapon = {
		lock_open = True,
		name = i18n(arg_19_0.isAircraftExtend() and "equip_info_24" or "equip_info_5"),
		sub = {}
	}

	for iter_19_4, iter_19_5 in ipairs(arg_19_0.getConfig("ammo_info")):
		table.insert(var_19_0.weapon.sub, arg_19_0.GetWeaponPageInfo(iter_19_5[1], iter_19_5[2]))

	var_19_0.equipInfo = {
		name = i18n("equip_info_14"),
		sub = {}
	}

	for iter_19_6, iter_19_7 in ipairs(arg_19_0.getConfig("equip_info")):
		table.insert(var_19_0.equipInfo.sub, arg_19_0.GetEquipAttrPageInfo(iter_19_7))

	var_19_0.part = {
		arg_19_0.getConfig("part_main"),
		arg_19_0.getConfig("part_sub")
	}
	var_19_0.equipmentType = arg_19_0.getConfig("type")

	return var_19_0

def var_0_0.GetWeaponPageInfo(arg_20_0, arg_20_1, arg_20_2):
	local var_20_0
	local var_20_1 = pg.equip_bullet_type[arg_20_1]
	local var_20_2 = var_20_1.exhibition_type == 2

	for iter_20_0, iter_20_1 in ipairs(var_20_1.exhibition_list):
		if not var_20_0:
			var_20_0 = arg_20_0.GetWeaponInfo(iter_20_1, arg_20_2, var_20_2)
			var_20_0.sub = {}
		else
			table.insert(var_20_0.sub, arg_20_0.GetWeaponInfo(iter_20_1, arg_20_2, var_20_2))

	return var_20_0

def var_0_0.GetWeaponInfo(arg_21_0, arg_21_1, arg_21_2, arg_21_3):
	local var_21_0 = arg_21_3 and pg.weapon_property[arg_21_2].bullet_ID[1] or arg_21_2

	return switch(arg_21_1, {
		function()
			return {
				name = i18n("equip_ammo_type_" .. arg_21_0.getConfig(AttributeType.Ammo))
			},
		function()
			return {
				name = pg.weapon_name[arg_21_2].name
			},
		function()
			return {
				type = AttributeType.Damage,
				value = pg.weapon_property[arg_21_2].damage
			},
		function()
			return {
				name = i18n("equip_info_6"),
				value = pg.bullet_template[var_21_0].velocity
			},
		function()
			return {
				name = i18n("equip_info_7"),
				value = pg.bullet_template[var_21_0].velocity
			},
		function()
			local var_27_0 = pg.bullet_template[var_21_0].damage_type

			return {
				name = i18n("equip_info_8"),
				value = var_27_0[1] * 100 .. "-" .. var_27_0[2] * 100 .. "-" .. var_27_0[3] * 100
			},
		function()
			return {
				name = i18n("equip_info_9"),
				value = pg.bullet_template[var_21_0].hit_type.range
			},
		function()
			return {
				name = i18n("equip_info_10"),
				value = pg.weapon_property[arg_21_2].range
			},
		function()
			return {
				name = i18n("equip_info_11"),
				value = pg.weapon_property[arg_21_2].angle
			},
		function()
			return {
				name = i18n("equip_info_12"),
				value = (pg.bullet_template[var_21_0].extra_param.randomOffsetX or "0") .. "*" .. (pg.bullet_template[var_21_0].extra_param.randomOffsetZ or "0")
			},
		function()
			return {
				name = i18n("equip_info_13"),
				value = arg_21_0.getConfig(AttributeType.Speciality)
			},
		function()
			return {
				type = AttributeType.CD,
				value = pg.weapon_property[arg_21_2].reload_max
			},
		function()
			return {
				name = i18n("attribute_max_distance_damage"),
				value = (1 - pg.bullet_template[var_21_0].hit_type.decay) * 100 .. "%"
			}
	})

local var_0_6 = {
	None,
	None,
	True,
	True,
	True,
	[13] = True
}

def var_0_0.GetEquipAttrPageInfo(arg_35_0, arg_35_1):
	local var_35_0
	local var_35_1

	if type(arg_35_1) == "table":
		var_35_0, var_35_1 = arg_35_1[1], arg_35_1[2]
	else
		var_35_0, var_35_1 = arg_35_1, arg_35_0.getConfig("weapon_id")[1]

	assert(tobool(var_0_6[var_35_0]) == (type(arg_35_1) == "table"), "equip attr sid type error from equip." .. arg_35_0.id)

	return arg_35_0.GetEquipAttrInfo(var_35_0, var_35_1)

def var_0_0.GetEquipAttrInfo(arg_36_0, arg_36_1, arg_36_2):
	return switch(arg_36_1, {
		function()
			local var_37_0 = pg.weapon_property[arg_36_2]

			return {
				name = i18n("equip_info_15"),
				value = var_37_0.min_range == 0 and var_37_0.range or var_37_0.min_range .. "-" .. var_37_0.range
			},
		function()
			return {
				name = i18n("equip_info_16"),
				value = pg.weapon_property[arg_36_2].angle
			},
		function()
			local var_39_0 = pg.bullet_template[arg_36_2]

			return {
				name = i18n("equip_info_17"),
				value = var_39_0.range - var_39_0.range_offset .. "-" .. var_39_0.range + var_39_0.range_offset
			},
		function()
			local var_40_0 = pg.barrage_template[arg_36_2]

			return {
				name = i18n("equip_info_18"),
				value = var_40_0.random_angle and var_40_0.angle or math.abs(var_40_0.delta_angle) * var_40_0.primal_repeat
			},
		function()
			return {
				name = i18n("attribute_scatter"),
				value = pg.bullet_template[arg_36_2].extra_param.randomOffsetX
			},
		function()
			return {
				name = i18n("equip_info_19"),
				value = Nation.Nation2Name(arg_36_0.getConfig("nationality"))
			},
		function()
			local var_43_0 = pg.aircraft_template[arg_36_0.id]

			return {
				name = i18n("equip_info_20"),
				value = var_43_0.speed
			},
		function()
			local var_44_0 = pg.aircraft_template[arg_36_0.id]

			return {
				name = i18n("equip_info_21"),
				type = AttributeType.AirDurability,
				value = {
					var_44_0.max_hp,
					var_44_0.hp_growth
				}
			},
		function()
			local var_45_0 = pg.aircraft_template[arg_36_0.id]

			return {
				name = i18n("equip_info_22"),
				value = var_45_0.dodge_limit
			},
		function()
			if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
				return {
					name = i18n("equip_info_28"),
					type = AttributeType.Corrected,
					value = EquipmentRarity.Rarity2CorrectedLevel(arg_36_0.getConfig("rarity"), arg_36_0.getConfig("level"))
				}
			else
				return {
					name = i18n("equip_info_28"),
					type = AttributeType.Corrected,
					value = pg.weapon_property[arg_36_2].corrected .. "%"
				},
		function()
			if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
				return None
			else
				local var_47_0 = {
					AttributeType.Cannon,
					AttributeType.Torpedo,
					AttributeType.AntiAircraft,
					AttributeType.Air,
					AttributeType.AntiSub
				}

				return {
					name = i18n("equip_info_29"),
					value = AttributeType.Type2Name(var_47_0[pg.weapon_property[arg_36_2].attack_attribute])
				},
		function()
			if PLATFORM_CODE == PLATFORM_JP or PLATFORM_CODE == PLATFORM_US:
				return None
			else
				return {
					name = i18n("equip_info_30"),
					value = pg.weapon_property[arg_36_2].attack_attribute_ratio .. "%"
				},
		function()
			local var_49_0 = pg.bullet_template[arg_36_2]

			return {
				name = i18n("equip_info_32"),
				value = math.abs(var_49_0.extra_param.aim_offset)
			}
	})

def var_0_0.GetGearScore(arg_50_0):
	local var_50_0 = arg_50_0.getConfig("rarity")
	local var_50_1 = arg_50_0.getConfig("level")

	assert(pg.equip_data_by_quality[var_50_0], "equip_data_by_quality not exist. " .. var_50_0)

	local var_50_2 = pg.equip_data_by_quality[var_50_0]

	return var_50_2.gear_score + var_50_1 * var_50_2.gear_score_addition

def var_0_0.GetSkill(arg_51_0):
	local var_51_0
	local var_51_1 = arg_51_0.getConfig("skill_id")[1]

	if var_51_1:
		var_51_0 = getSkillConfig(var_51_1)

	return var_51_0

def var_0_0.GetWeaponID(arg_52_0):
	return arg_52_0.getConfig("weapon_id")

def var_0_0.GetSonarProperty(arg_53_0):
	local var_53_0 = arg_53_0.getConfig("equip_parameters").range

	if var_53_0:
		return {
			[AttributeType.SonarRange] = var_53_0
		}
	else
		return None

def var_0_0.GetAntiSirenPower(arg_54_0):
	return arg_54_0.getConfig("anti_siren")

def var_0_0.canUpgrade(arg_55_0):
	return var_0_0.getConfigData(arg_55_0).next != 0

def var_0_0.hasPrevLevel(arg_56_0):
	return arg_56_0.getConfig("prev") != 0

def var_0_0.getRevertAwards(arg_57_0):
	local var_57_0 = {}
	local var_57_1 = 0
	local var_57_2 = arg_57_0

	while var_57_2.hasPrevLevel():
		var_57_2 = Equipment.New({
			id = var_57_2.getConfig("prev")
		})

		for iter_57_0, iter_57_1 in ipairs(var_57_2.getConfig("trans_use_item")):
			table.insert(var_57_0, Drop.New({
				type = DROP_TYPE_ITEM,
				id = iter_57_1[1],
				count = iter_57_1[2]
			}))

		var_57_1 = var_57_1 + var_57_2.getConfig("trans_use_gold")

	local var_57_3 = PlayerConst.MergeSameDrops(var_57_0)

	if var_57_1 > 0:
		table.insert(var_57_3, Drop.New({
			type = DROP_TYPE_RESOURCE,
			id = PlayerConst.ResGold,
			count = var_57_1
		}))

	return var_57_3

def var_0_0.canEquipSkin(arg_58_0):
	local var_58_0 = arg_58_0.getConfig("type")

	return pg.equip_data_by_type[var_58_0].equip_skin == 1

def var_0_0.getType(arg_59_0):
	return arg_59_0.getConfig("type")

def var_0_0.hasSkin(arg_60_0):
	return arg_60_0.skinId and arg_60_0.skinId != 0

def var_0_0.setSkinId(arg_61_0, arg_61_1):
	arg_61_0.skinId = arg_61_1

def var_0_0.getSkinId(arg_62_0):
	return arg_62_0.skinId

def var_0_0.hasSkinOrbit(arg_63_0):
	if not arg_63_0.hasSkin():
		return False

	return var_0_0.IsOrbitSkin(arg_63_0.skinId)

def var_0_0.IsOrbitSkin(arg_64_0):
	local var_64_0 = var_0_1[arg_64_0]

	if var_64_0.orbit_combat != "" or var_64_0.orbit_ui != "":
		return True
	else
		return False

def var_0_0.isImportance(arg_65_0):
	return arg_65_0.getConfig("important") == var_0_0.EQUIPMENT_IMPORTANCE

def var_0_0.isUnique(arg_66_0):
	return arg_66_0.getConfig("equip_limit") != 0

def var_0_0.isDevice(arg_67_0):
	local var_67_0 = arg_67_0.getConfig("type")

	return underscore.any(EquipType.DeviceEquipTypes, function(arg_68_0)
		return arg_68_0 == var_67_0)

def var_0_0.isAircraft(arg_69_0):
	local var_69_0 = arg_69_0.getConfig("type")

	return underscore.any(EquipType.AirEquipTypes, function(arg_70_0)
		return arg_70_0 == var_69_0)

def var_0_0.isAircraftExtend(arg_71_0):
	local var_71_0 = arg_71_0.getConfig("type")

	return underscore.any(EquipType.AirExtendEquipTypes, function(arg_72_0)
		return arg_72_0 == var_71_0)

def var_0_0.MigrateTo(arg_73_0, arg_73_1):
	assert(not arg_73_0.isSkin)

	return Equipment.New({
		id = arg_73_1,
		config_id = arg_73_1,
		count = arg_73_0.count
	})

def var_0_0.GetRootEquipment(arg_74_0):
	local var_74_0 = var_0_0.getConfigData(arg_74_0.configId)

	while var_74_0.prev > 0:
		var_74_0 = var_0_0.getConfigData(var_74_0.prev)

	local var_74_1 = arg_74_0.MigrateTo(var_74_0.id)

	var_74_1.count = 1

	return var_74_1

def var_0_0.getNation(arg_75_0):
	return arg_75_0.getConfig("nationality")

def var_0_0.GetEquipRootStatic(arg_76_0):
	local var_76_0 = var_0_0.getConfigData(arg_76_0)

	while var_76_0.prev > 0:
		var_76_0 = var_0_0.getConfigData(var_76_0.prev)

	return var_76_0.id

def var_0_0.GetRevertRewardsStatic(arg_77_0):
	local var_77_0 = {}
	local var_77_1 = var_0_0.getConfigData(arg_77_0)

	while var_77_1.prev > 0:
		var_77_1 = var_0_0.getConfigData(var_77_1.prev)

		for iter_77_0, iter_77_1 in ipairs(var_77_1.trans_use_item):
			var_77_0[iter_77_1[1]] = (var_77_0[iter_77_1[1]] or 0) + iter_77_1[2]

		var_77_0.gold = (var_77_0.gold or 0) + var_77_1.trans_use_gold

	return var_77_0

def var_0_0.GetEquipReloadStatic(arg_78_0):
	local var_78_0 = var_0_0.getConfigData(arg_78_0).weapon_id

	if var_78_0 and #var_78_0 > 0:
		local var_78_1 = pg.weapon_property[var_78_0[1]]

		if var_78_1:
			return var_78_1.reload_max

def var_0_0.GetEquipComposeCfgStatic(arg_79_0):
	local var_79_0 = pg.compose_data_template

	for iter_79_0, iter_79_1 in ipairs(var_79_0.all):
		local var_79_1 = var_79_0[iter_79_1]
		local var_79_2 = True

		for iter_79_2, iter_79_3 in pairs(arg_79_0):
			var_79_2 = var_79_2 and var_79_1[iter_79_2] == iter_79_3

		if var_79_2:
			return var_79_1

return var_0_0
