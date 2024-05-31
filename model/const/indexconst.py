local var_0_0 = class("IndexConst")

def var_0_0.Flags2Bits(arg_1_0):
	local var_1_0 = 0

	for iter_1_0, iter_1_1 in ipairs(arg_1_0):
		var_1_0 = bit.bor(var_1_0, bit.lshift(1, iter_1_1))

	return var_1_0

def var_0_0.FlagRange2Bits(arg_2_0, arg_2_1):
	local var_2_0 = 0

	for iter_2_0 = arg_2_0, arg_2_1:
		var_2_0 = bit.bor(var_2_0, bit.lshift(1, iter_2_0))

	return var_2_0

def var_0_0.ToggleBits(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	local var_3_0 = arg_3_0
	local var_3_1 = bit.lshift(1, arg_3_3)

	if arg_3_2:
		local var_3_2 = bit.lshift(1, arg_3_2)
		local var_3_3 = _.reduce(arg_3_1, 0, function(arg_4_0, arg_4_1)
			return arg_4_0 + (arg_4_1 != arg_3_2 and bit.lshift(1, arg_4_1) or 0))

		if var_3_1 == var_3_2:
			var_3_0 = var_3_2
		else
			if bit.band(var_3_0, var_3_2) > 0:
				var_3_0 = var_3_0 - var_3_2

			if bit.band(var_3_0, var_3_1) > 0:
				var_3_1 = -var_3_1

			var_3_0 = var_3_0 + var_3_1

			if var_3_0 == var_3_3 or var_3_0 == 0:
				var_3_0 = var_3_2
	else
		if bit.band(var_3_0, var_3_1) > 0:
			var_3_1 = -var_3_1

		var_3_0 = var_3_0 + var_3_1

	return var_3_0

def var_0_0.SingleToggleBits(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local var_5_0 = arg_5_0
	local var_5_1 = bit.lshift(1, arg_5_3)

	if var_5_0 == var_5_1:
		var_5_0 = bit.lshift(1, arg_5_2)
	else
		var_5_0 = var_5_1

	return var_5_0

def var_0_0.StrLShift(arg_6_0, arg_6_1):
	local var_6_0 = ""

	for iter_6_0 = 1, arg_6_1:
		arg_6_0 = arg_6_0 .. "0"

	return arg_6_0 .. var_6_0

def var_0_0.StrAnd(arg_7_0, arg_7_1):
	local var_7_0 = ""
	local var_7_1 = string.len(arg_7_0) > string.len(arg_7_1) and arg_7_0 or arg_7_1
	local var_7_2 = var_7_1 == arg_7_0 and arg_7_1 or arg_7_0
	local var_7_3 = string.len(var_7_1)
	local var_7_4 = string.len(var_7_2)

	for iter_7_0 = 1, var_7_4:
		if string.sub(var_7_2, iter_7_0, iter_7_0) == "1" and string.sub(var_7_1, var_7_3 - var_7_4 + iter_7_0, var_7_3 - var_7_4 + iter_7_0) == "1":
			var_7_0 = var_7_0 .. "1"
		else
			var_7_0 = var_7_0 .. "0"

	local var_7_5 = ""

	for iter_7_1 = 1, var_7_3 - var_7_4:
		var_7_5 = var_7_5 .. "0"

	return var_7_5 .. var_7_0

def var_0_0.StrOr(arg_8_0, arg_8_1):
	local var_8_0 = ""
	local var_8_1 = string.len(arg_8_0) > string.len(arg_8_1) and arg_8_0 or arg_8_1
	local var_8_2 = var_8_1 == arg_8_0 and arg_8_1 or arg_8_0
	local var_8_3 = string.len(var_8_1)
	local var_8_4 = string.len(var_8_2)

	for iter_8_0 = 1, var_8_4:
		if string.sub(var_8_2, iter_8_0, iter_8_0) == "1" or string.sub(var_8_1, var_8_3 - var_8_4 + iter_8_0, var_8_3 - var_8_4 + iter_8_0) == "1":
			var_8_0 = var_8_0 .. "1"
		else
			var_8_0 = var_8_0 .. "0"

	return string.sub(var_8_1, 1, var_8_3 - var_8_4) .. var_8_0

def var_0_0.Flags2Str(arg_9_0):
	local var_9_0 = ""

	for iter_9_0, iter_9_1 in ipairs(arg_9_0):
		var_9_0 = var_0_0.StrOr(var_9_0, var_0_0.StrLShift("1", iter_9_1))

	return var_9_0

def var_0_0.FlagRange2Str(arg_10_0, arg_10_1):
	local var_10_0 = ""

	for iter_10_0 = arg_10_0, arg_10_1:
		var_10_0 = var_0_0.StrOr(var_10_0, var_0_0.StrLShift("1", iter_10_0))

	return var_10_0

def var_0_0.ToggleStr(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	local var_11_0 = arg_11_0
	local var_11_1 = var_0_0.StrLShift("1", arg_11_3)

	if arg_11_2:
		local var_11_2 = var_0_0.StrLShift("1", arg_11_2)
		local var_11_3 = ""

		for iter_11_0, iter_11_1 in ipairs(arg_11_1):
			if iter_11_1 != arg_11_2:
				var_11_3 = var_0_0.StrOr(var_11_3, var_0_0.StrLShift("1", iter_11_1))

		if var_11_1 == var_11_2 or var_11_0 == var_11_3:
			var_11_0 = var_11_2
		else
			if string.find(var_0_0.StrAnd(var_11_0, var_11_2), "1") != None:
				var_11_0 = var_11_1
			else
				local var_11_4 = var_0_0.StrOr(var_11_0, var_11_1)
				local var_11_5 = string.len(var_11_4) - arg_11_3
				local var_11_6 = string.find(var_0_0.StrAnd(var_11_0, var_11_1), "1") != None and "0" or "1"

				var_11_0 = string.sub(var_11_4, 1, var_11_5 - 1) .. var_11_6 .. string.sub(var_11_4, var_11_5 + 1)

			if var_11_0 == var_11_3 or string.find(var_11_0, "1") == None:
				var_11_0 = var_11_2
	else
		local var_11_7 = var_0_0.StrOr(var_11_0, var_11_1)
		local var_11_8 = string.len(var_11_7) - arg_11_3
		local var_11_9 = string.find(var_0_0.StrAnd(var_11_0, var_11_1), "1") != None and "0" or "1"

		var_11_0 = string.sub(var_11_7, 1, var_11_8 - 1) .. var_11_9 .. string.sub(var_11_7, var_11_8 + 1)

	return var_11_0

def var_0_0.BitAll(arg_12_0):
	local var_12_0 = 0

	for iter_12_0, iter_12_1 in ipairs(arg_12_0):
		var_12_0 = bit.bor(iter_12_1, var_12_0)

	return var_12_0

var_0_0.EquipmentTypeSmallCannon = bit.lshift(1, 0)
var_0_0.EquipmentTypeMediumCannon = bit.lshift(1, 1)
var_0_0.EquipmentTypeBigCannon = bit.lshift(1, 2)
var_0_0.EquipmentTypeWarshipTorpedo = bit.lshift(1, 3)
var_0_0.EquipmentTypeSubmaraineTorpedo = bit.lshift(1, 4)
var_0_0.EquipmentTypeAntiAircraft = bit.lshift(1, 5)
var_0_0.EquipmentTypeFighter = bit.lshift(1, 6)
var_0_0.EquipmentTypeBomber = bit.lshift(1, 7)
var_0_0.EquipmentTypeTorpedoBomber = bit.lshift(1, 8)
var_0_0.EquipmentTypeEquip = bit.lshift(1, 9)
var_0_0.EquipmentTypeOther = bit.lshift(1, 10)
var_0_0.EquipmentTypeIndexs = {
	var_0_0.EquipmentTypeSmallCannon,
	var_0_0.EquipmentTypeMediumCannon,
	var_0_0.EquipmentTypeBigCannon,
	var_0_0.EquipmentTypeWarshipTorpedo,
	var_0_0.EquipmentTypeSubmaraineTorpedo,
	var_0_0.EquipmentTypeAntiAircraft,
	var_0_0.EquipmentTypeFighter,
	var_0_0.EquipmentTypeBomber,
	var_0_0.EquipmentTypeTorpedoBomber,
	var_0_0.EquipmentTypeEquip,
	var_0_0.EquipmentTypeOther
}
var_0_0.EquipmentTypeAll = var_0_0.BitAll(var_0_0.EquipmentTypeIndexs)

table.insert(var_0_0.EquipmentTypeIndexs, 1, var_0_0.EquipmentTypeAll)

def var_0_0.filterEquipByType(arg_13_0, arg_13_1):
	if not arg_13_1 or arg_13_1 == var_0_0.EquipmentTypeAll:
		return True

	for iter_13_0 = 2, #EquipmentSortCfg.index:
		local var_13_0 = bit.lshift(1, iter_13_0 - 2)

		if bit.band(var_13_0, arg_13_1) > 0:
			local var_13_1 = EquipmentSortCfg.index[iter_13_0].types

			if table.contains(var_13_1, arg_13_0.getConfig("type")):
				return True

	return False

var_0_0.EquipmentTypeNames = {
	"word_equipment_all",
	"word_equipment_small_cannon",
	"word_equipment_medium_cannon",
	"word_equipment_big_cannon",
	"word_equipment_warship_torpedo",
	"word_equipment_submarine_torpedo",
	"word_equipment_antiaircraft",
	"word_equipment_fighter",
	"word_equipment_bomber",
	"word_equipment_torpedo_bomber",
	"word_equipment_equip",
	"word_equipment_special"
}
var_0_0.EquipCampUS = bit.lshift(1, 0)
var_0_0.EquipCampEN = bit.lshift(1, 1)
var_0_0.EquipCampJP = bit.lshift(1, 2)
var_0_0.EquipCampDE = bit.lshift(1, 3)
var_0_0.EquipCampCN = bit.lshift(1, 4)
var_0_0.EquipCampITA = bit.lshift(1, 5)
var_0_0.EquipCampSN = bit.lshift(1, 6)
var_0_0.EquipCampFR = bit.lshift(1, 7)
var_0_0.EquipCampMNF = bit.lshift(1, 8)
var_0_0.EquipCampLINK = bit.lshift(1, 9)
var_0_0.EquipCampOther = bit.lshift(1, 10)
var_0_0.EquipCampIndexs = {
	var_0_0.EquipCampUS,
	var_0_0.EquipCampEN,
	var_0_0.EquipCampJP,
	var_0_0.EquipCampDE,
	var_0_0.EquipCampCN,
	var_0_0.EquipCampITA,
	var_0_0.EquipCampSN,
	var_0_0.EquipCampFR,
	var_0_0.EquipCampMNF,
	var_0_0.EquipCampLINK,
	var_0_0.EquipCampOther
}
var_0_0.EquipCampNames = {
	"word_shipNation_all",
	"word_shipNation_baiYing",
	"word_shipNation_huangJia",
	"word_shipNation_chongYing",
	"word_shipNation_tieXue",
	"word_shipNation_dongHuang",
	"word_shipNation_saDing",
	"word_shipNation_beiLian",
	"word_shipNation_ziyou",
	"word_shipNation_weixi",
	"word_shipNation_link",
	"word_shipNation_other"
}
var_0_0.EquipCampAll = var_0_0.BitAll(var_0_0.EquipCampIndexs)

table.insert(var_0_0.EquipCampIndexs, 1, var_0_0.EquipCampAll)

def var_0_0.filterEquipByCamp(arg_14_0, arg_14_1):
	if not arg_14_1 or arg_14_1 == var_0_0.EquipmentTypeAll:
		return True

	for iter_14_0 = 2, #EquipmentSortCfg.campIndex:
		local var_14_0 = bit.lshift(1, iter_14_0 - 2)

		if bit.band(var_14_0, arg_14_1) > 0:
			local var_14_1 = EquipmentSortCfg.campIndex[iter_14_0].types

			for iter_14_1, iter_14_2 in ipairs(var_14_1):
				if iter_14_2 == Nation.LINK:
					if arg_14_0.getNation() >= Nation.LINK:
						return True
				elif iter_14_2 == arg_14_0.getNation():
					return True

	return False

var_0_0.EquipProperty_Cannon = bit.lshift(1, 0)
var_0_0.EquipProperty_Air = bit.lshift(1, 1)
var_0_0.EquipProperty_Dodge = bit.lshift(1, 2)
var_0_0.EquipProperty_AntiAircraft = bit.lshift(1, 3)
var_0_0.EquipProperty_Torpedo = bit.lshift(1, 4)
var_0_0.EquipProperty_Reload = bit.lshift(1, 5)
var_0_0.EquipProperty_Durability = bit.lshift(1, 6)
var_0_0.EquipProperty_Antisub = bit.lshift(1, 7)
var_0_0.EquipProperty_Oxy = bit.lshift(1, 8)
var_0_0.EquipProperty_Speed = bit.lshift(1, 9)
var_0_0.EquipProperty_Hit = bit.lshift(1, 10)
var_0_0.EquipProperty_Luck = bit.lshift(1, 11)
var_0_0.EquipPropertyIndexs = {
	var_0_0.EquipProperty_Cannon,
	var_0_0.EquipProperty_Air,
	var_0_0.EquipProperty_Dodge,
	var_0_0.EquipProperty_AntiAircraft,
	var_0_0.EquipProperty_Torpedo,
	var_0_0.EquipProperty_Reload,
	var_0_0.EquipProperty_Durability,
	var_0_0.EquipProperty_Antisub,
	var_0_0.EquipProperty_Oxy,
	var_0_0.EquipProperty_Speed,
	var_0_0.EquipProperty_Hit,
	var_0_0.EquipProperty_Luck
}
var_0_0.EquipPropertyAll = var_0_0.BitAll(var_0_0.EquipPropertyIndexs)

table.insert(var_0_0.EquipPropertyIndexs, 1, var_0_0.EquipPropertyAll)

var_0_0.EquipPropertyNames = {
	"sort_attribute",
	"attribute_cannon",
	"attribute_air",
	"attribute_dodge",
	"attribute_antiaircraft",
	"attribute_torpedo",
	"attribute_reload",
	"attribute_durability",
	"attribute_antisub",
	"attribute_oxy_max",
	"attribute_speed",
	"attribute_hit",
	"attribute_luck"
}

def var_0_0.filterEquipByProperty(arg_15_0, arg_15_1):
	local var_15_0 = {}

	if arg_15_0.getConfig("attribute_1"):
		table.insert(var_15_0, arg_15_0.getConfig("attribute_1"))

	if arg_15_0.getConfig("attribute_2"):
		table.insert(var_15_0, arg_15_0.getConfig("attribute_2"))

	if arg_15_0.getConfig("attribute_3"):
		table.insert(var_15_0, arg_15_0.getConfig("attribute_3"))

	local var_15_1 = 0

	for iter_15_0, iter_15_1 in ipairs(arg_15_1):
		if not iter_15_1 or iter_15_1 == var_0_0.EquipPropertyAll:
			var_15_1 = var_15_1 + 1
		else
			for iter_15_2 = 2, #EquipmentSortCfg.propertyIndex:
				local var_15_2 = bit.lshift(1, iter_15_2 - 2)

				if bit.band(var_15_2, iter_15_1) > 0:
					local var_15_3 = EquipmentSortCfg.propertyIndex[iter_15_2].types

					for iter_15_3 = #var_15_0, 1, -1:
						local var_15_4 = var_15_0[iter_15_3]

						if table.contains(var_15_3, var_15_4):
							var_15_1 = var_15_1 + 1

							table.remove(var_15_0, iter_15_3)

							break

	return var_15_1 >= #arg_15_1

var_0_0.EquipAmmoChuanjia = bit.lshift(1, 0)
var_0_0.EquipAmmoGaobao = bit.lshift(1, 1)
var_0_0.EquipAmmoTongchangDan = bit.lshift(1, 2)
var_0_0.EquipAmmoQita = bit.lshift(1, 3)
var_0_0.EquipAmmoIndexs_1 = {
	var_0_0.EquipAmmoChuanjia,
	var_0_0.EquipAmmoGaobao,
	var_0_0.EquipAmmoTongchangDan,
	var_0_0.EquipAmmoQita
}
var_0_0.EquipAmmoAll_1 = var_0_0.BitAll(var_0_0.EquipAmmoIndexs_1)

table.insert(var_0_0.EquipAmmoIndexs_1, 1, var_0_0.EquipAmmoAll_1)

var_0_0.EquipAmmoIndexs_1_Names = {
	"attribute_ammo",
	"equip_ammo_type_1",
	"equip_ammo_type_2",
	"equip_ammo_type_3",
	"word_shipType_other"
}

def var_0_0.filterEquipAmmo1(arg_16_0, arg_16_1):
	if not arg_16_1 or arg_16_1 == var_0_0.EquipAmmoAll_1:
		return True

	for iter_16_0 = 2, #EquipmentSortCfg.ammoIndex1:
		local var_16_0 = bit.lshift(1, iter_16_0 - 2)

		if bit.band(var_16_0, arg_16_1) > 0:
			local var_16_1 = EquipmentSortCfg.ammoIndex1[iter_16_0].types

			if table.contains(var_16_1, arg_16_0.getConfig("ammo")):
				return True

	return False

var_0_0.EquipAmmoShengdao = bit.lshift(1, 0)
var_0_0.EquipAmmoTongchang = bit.lshift(1, 1)
var_0_0.EquipAmmoIndexs_2 = {
	var_0_0.EquipAmmoShengdao,
	var_0_0.EquipAmmoTongchang
}
var_0_0.EquipAmmoAll_2 = var_0_0.BitAll(var_0_0.EquipAmmoIndexs_2)

table.insert(var_0_0.EquipAmmoIndexs_2, 1, var_0_0.EquipAmmoAll_2)

var_0_0.EquipAmmoIndexs_2_Names = {
	"attribute_ammo",
	"equip_ammo_type_4",
	"equip_ammo_type_5"
}

def var_0_0.filterEquipAmmo2(arg_17_0, arg_17_1):
	if not arg_17_1 or arg_17_1 == var_0_0.EquipAmmoAll_2:
		return True

	for iter_17_0 = 2, #EquipmentSortCfg.ammoIndex2:
		local var_17_0 = bit.lshift(1, iter_17_0 - 2)

		if bit.band(var_17_0, arg_17_1) > 0:
			local var_17_1 = EquipmentSortCfg.ammoIndex2[iter_17_0].types

			if table.contains(var_17_1, arg_17_0.getConfig("ammo")):
				return True

	return False

var_0_0.EquipmentRarity1 = bit.lshift(1, 0)
var_0_0.EquipmentRarity2 = bit.lshift(1, 1)
var_0_0.EquipmentRarity3 = bit.lshift(1, 2)
var_0_0.EquipmentRarity4 = bit.lshift(1, 3)
var_0_0.EquipmentRarity5 = bit.lshift(1, 4)
var_0_0.EquipmentRarityIndexs = {
	var_0_0.EquipmentRarity1,
	var_0_0.EquipmentRarity2,
	var_0_0.EquipmentRarity3,
	var_0_0.EquipmentRarity4,
	var_0_0.EquipmentRarity5
}
var_0_0.EquipmentRarityAll = var_0_0.BitAll(var_0_0.EquipmentRarityIndexs)

table.insert(var_0_0.EquipmentRarityIndexs, 1, var_0_0.EquipmentRarityAll)

var_0_0.RarityNames = {
	"index_all",
	"index_rare2",
	"index_rare3",
	"index_rare4",
	"index_rare5",
	"index_rare6"
}

def var_0_0.filterEquipByRarity(arg_18_0, arg_18_1):
	if not arg_18_1 or arg_18_1 == var_0_0.EquipmentRarityAll:
		return True

	local var_18_0 = math.max(arg_18_0.getConfig("rarity") - 2, 0)
	local var_18_1 = bit.lshift(1, var_18_0)

	return bit.band(var_18_1, arg_18_1) > 0

var_0_0.EquipmentExtraNames = {
	"index_without_limit",
	"index_equip",
	"index_strengthen",
	"index_reform"
}
var_0_0.EquipmentExtraEquiping = bit.lshift(1, 0)
var_0_0.EquipmentExtraStrengthen = bit.lshift(1, 1)
var_0_0.EquipmentExtraTransform = bit.lshift(1, 2)
var_0_0.EquipmentExtraIndexs = {
	var_0_0.EquipmentExtraEquiping,
	var_0_0.EquipmentExtraStrengthen,
	var_0_0.EquipmentExtraTransform
}
var_0_0.EquipmentExtraNone = 0

table.insert(var_0_0.EquipmentExtraIndexs, 1, var_0_0.EquipmentExtraNone)

def var_0_0.filterEquipByExtra(arg_19_0, arg_19_1):
	arg_19_1 = arg_19_1 or 0

	if bit.band(arg_19_1, var_0_0.EquipmentExtraEquiping) > 0 and not arg_19_0.shipId:
		return False

	if bit.band(arg_19_1, var_0_0.EquipmentExtraStrengthen) > 0:
		local var_19_0 = pg.equip_data_template[arg_19_0.id]

		if not var_19_0 or not var_19_0.next or var_19_0.next == 0:
			return False

	if bit.band(arg_19_1, var_0_0.EquipmentExtraTransform) > 0:
		local var_19_1 = EquipmentProxy.EquipTransformTargetDict[Equipment.GetEquipRootStatic(arg_19_0.id)]

		if not var_19_1 or not var_19_1.targets:
			return False

	return True

var_0_0.DisplayEquipSkinSort = 6
var_0_0.DisplayEquipSkinIndex = 7
var_0_0.DisplayEquipSkinTheme = 8
var_0_0.EquipSkinSortType = 1
var_0_0.EquipSkinSortTypes = {
	var_0_0.EquipSkinSortType
}
var_0_0.EquipSkinSortNames = {
	i18n("word_equipskin_type")
}
var_0_0.EquipSkinIndexAll = 1
var_0_0.EquipSkinIndexCannon = 2
var_0_0.EquipSkinIndexTarpedo = 3
var_0_0.EquipSkinIndexAircraft = 4
var_0_0.EquipSkinIndexAux = 5
var_0_0.EquipSkinIndexTypes = {
	var_0_0.EquipSkinIndexAll,
	var_0_0.EquipSkinIndexCannon,
	var_0_0.EquipSkinIndexTarpedo,
	var_0_0.EquipSkinIndexAircraft,
	var_0_0.EquipSkinIndexAux
}
var_0_0.EquipSkinIndexNames = {
	i18n("word_equipskin_all"),
	i18n("word_equipskin_cannon"),
	i18n("word_equipskin_tarpedo"),
	i18n("word_equipskin_aircraft"),
	i18n("word_equipskin_aux")
}
var_0_0.EquipSkinThemeAll = 1
var_0_0.EquipSkinThemeEnd = None
var_0_0.EquipSkinThemeTypes = {
	var_0_0.EquipSkinThemeAll
}

for iter_0_0, iter_0_1 in ipairs(pg.equip_skin_theme_template.all):
	table.insert(var_0_0.EquipSkinThemeTypes, iter_0_0 + var_0_0.EquipSkinThemeAll)

	if iter_0_0 == #pg.equip_skin_theme_template.all:
		var_0_0.EquipSkinThemeEnd = iter_0_0 + var_0_0.EquipSkinThemeAll + 1

var_0_0.EquipSkinThemeNames = {
	i18n("word_equipskin_all")
}

for iter_0_2, iter_0_3 in ipairs(pg.equip_skin_theme_template.all):
	local var_0_1 = pg.equip_skin_theme_template[iter_0_3].name

	table.insert(var_0_0.EquipSkinThemeNames, var_0_1)

def var_0_0.filterEquipSkinByIndex(arg_20_0, arg_20_1):
	if not arg_20_1:
		return True

	if bit.band(arg_20_1, bit.lshift(1, var_0_0.EquipSkinIndexAll)) > 0:
		return True

	local var_20_0 = {}
	local var_20_1 = {
		1,
		2,
		3,
		4,
		5
	}

	for iter_20_0, iter_20_1 in ipairs(var_0_0.EquipSkinIndexTypes):
		if bit.band(arg_20_1, bit.lshift(1, iter_20_1)) > 0:
			local var_20_2 = var_20_1[iter_20_1]
			local var_20_3 = EquipmentSortCfg.skinIndex[var_20_2].types

			for iter_20_2, iter_20_3 in ipairs(var_20_3):
				table.insert(var_20_0, iter_20_3)

	local var_20_4 = pg.equip_skin_template

	if arg_20_0.count > 0 and arg_20_0.isSkin:
		local var_20_5 = var_20_4[arg_20_0.id].equip_type

		for iter_20_4, iter_20_5 in pairs(var_20_5):
			if table.contains(var_20_0, iter_20_5):
				return True

def var_0_0.filterEquipSkinByTheme(arg_21_0, arg_21_1):
	if not arg_21_1:
		return True

	if string.find(var_0_0.StrAnd(arg_21_1, var_0_0.StrLShift("1", var_0_0.EquipSkinThemeAll)), "1") != None:
		return True

	local var_21_0 = pg.equip_skin_template
	local var_21_1 = pg.equip_skin_theme_template

	if arg_21_0.count > 0 and arg_21_0.isSkin:
		local var_21_2 = arg_21_0.id
		local var_21_3 = var_21_0[var_21_2].themeid
		local var_21_4

		for iter_21_0, iter_21_1 in ipairs(var_0_0.EquipSkinThemeTypes):
			if string.find(var_0_0.StrAnd(arg_21_1, var_0_0.StrLShift("1", iter_21_0)), "1") != None:
				local var_21_5 = var_21_1[var_21_1[pg.equip_skin_theme_template.all[iter_21_1 - 1]].id].ids

				if table.contains(var_21_5, var_21_2):
					return True

var_0_0.SpWeaponTypeQvZhu = bit.lshift(1, 0)
var_0_0.SpWeaponTypeQingXvn = bit.lshift(1, 1)
var_0_0.SpWeaponTypeZhongXvn = bit.lshift(1, 2)
var_0_0.SpWeaponTypeZhanLie = bit.lshift(1, 3)
var_0_0.SpWeaponTypeHangMu = bit.lshift(1, 4)
var_0_0.SpWeaponTypeWeiXiu = bit.lshift(1, 5)
var_0_0.SpWeaponTypeQianTing = bit.lshift(1, 6)
var_0_0.SpWeaponTypeQiTa = bit.lshift(1, 7)
var_0_0.SpWeaponTypeIndexs = {
	var_0_0.SpWeaponTypeQvZhu,
	var_0_0.SpWeaponTypeQingXvn,
	var_0_0.SpWeaponTypeZhongXvn,
	var_0_0.SpWeaponTypeZhanLie,
	var_0_0.SpWeaponTypeHangMu,
	var_0_0.SpWeaponTypeWeiXiu,
	var_0_0.SpWeaponTypeQianTing,
	var_0_0.SpWeaponTypeQiTa
}
var_0_0.SpWeaponTypeAll = var_0_0.BitAll(var_0_0.SpWeaponTypeIndexs)

table.insert(var_0_0.SpWeaponTypeIndexs, 1, var_0_0.SpWeaponTypeAll)

def var_0_0.filterSpWeaponByType(arg_22_0, arg_22_1):
	if not arg_22_1 or arg_22_1 == var_0_0.SpWeaponTypeAll:
		return True

	local var_22_0 = arg_22_0.GetWearableShipTypes()

	for iter_22_0 = 0, #var_0_0.SpWeaponTypeIndexs - 2:
		local var_22_1 = bit.lshift(1, iter_22_0)

		if bit.band(var_22_1, arg_22_1) > 0:
			local var_22_2 = ShipIndexCfg.type[4 + iter_22_0].types

			if _.any(var_22_2, function(arg_23_0)
				return table.contains(var_22_0, arg_23_0)):
				return True

	return False

var_0_0.SpWeaponTypeNames = {
	"word_equipment_all",
	"spweapon_ui_index_shipType_quZhu",
	"spweapon_ui_index_shipType_qinXun",
	"spweapon_ui_index_shipType_zhongXun",
	"spweapon_ui_index_shipType_zhanLie",
	"spweapon_ui_index_shipType_hangMu",
	"spweapon_ui_index_shipType_weiXiu",
	"spweapon_ui_index_shipType_qianTing",
	"spweapon_ui_index_shipType_other"
}
var_0_0.SpWeaponRarityNames = {
	"index_all",
	"index_rare3",
	"index_rare4",
	"index_rare5"
}
var_0_0.SpWeaponRarity1 = bit.lshift(1, 0)
var_0_0.SpWeaponRarity2 = bit.lshift(1, 1)
var_0_0.SpWeaponRarity3 = bit.lshift(1, 2)
var_0_0.SpWeaponRarityIndexs = {
	var_0_0.SpWeaponRarity1,
	var_0_0.SpWeaponRarity2,
	var_0_0.SpWeaponRarity3
}
var_0_0.SpWeaponRarityAll = var_0_0.BitAll(var_0_0.SpWeaponRarityIndexs)

table.insert(var_0_0.SpWeaponRarityIndexs, 1, var_0_0.SpWeaponRarityAll)

def var_0_0.filterSpWeaponByRarity(arg_24_0, arg_24_1):
	if not arg_24_1 or arg_24_1 == var_0_0.SpWeaponRarityAll:
		return True

	local var_24_0 = math.max(arg_24_0.GetRarity() - 2, 0)
	local var_24_1 = bit.lshift(1, var_24_0)

	return bit.band(var_24_1, arg_24_1) > 0

var_0_0.LABEL_COUNT = 9
var_0_0.ECodeLabelNames = {}
var_0_0.ECodeLabelIndexs = {}

for iter_0_4 = 1, var_0_0.LABEL_COUNT:
	local var_0_2 = bit.lshift(1, iter_0_4 - 1)

	table.insert(var_0_0.ECodeLabelNames, "equip_share_label_" .. iter_0_4)
	table.insert(var_0_0.ECodeLabelIndexs, var_0_2)

local var_0_3 = var_0_0.BitAll(var_0_0.ECodeLabelIndexs)

table.insert(var_0_0.ECodeLabelNames, 1, "index_all")
table.insert(var_0_0.ECodeLabelIndexs, 1, var_0_3)

def var_0_0.filterEquipCodeByLable(arg_25_0, arg_25_1):
	if not arg_25_1 or arg_25_1 == var_0_3:
		return True

	for iter_25_0, iter_25_1 in ipairs(arg_25_0.GetLabels()):
		if bit.band(bit.lshift(1, iter_25_1 - 1), arg_25_1) > 0:
			return True

	return False

return var_0_0
