from packages.luatable import table

import IndexConst

SortRarity = bit.lshift(1, 0)
SortLevel = bit.lshift(1, 1)
SortPower = bit.lshift(1, 2)
SortAchivedTime = bit.lshift(1, 3)
SortIntimacy = bit.lshift(1, 4)
SortEnergy = bit.lshift(1, 13)
SortProperty_Cannon = bit.lshift(1, 5)
SortProperty_Air = bit.lshift(1, 6)
SortProperty_Dodge = bit.lshift(1, 7)
SortProperty_AntiAircraft = bit.lshift(1, 8)
SortProperty_Torpedo = bit.lshift(1, 9)
SortProperty_Reload = bit.lshift(1, 10)
SortProperty_Durability = bit.lshift(1, 11)
SortProperty_Antisub = bit.lshift(1, 12)
SortPropertyIndexs = table(
	SortProperty_Cannon,
	SortProperty_Air,
	SortProperty_Dodge,
	SortProperty_AntiAircraft,
	SortProperty_Torpedo,
	SortProperty_Reload,
	SortProperty_Durability,
	SortProperty_Antisub
)
SortPropertyAll = IndexConst.BitAll(SortPropertyIndexs)

table.insert(SortPropertyIndexs, 1, SortPropertyAll)

SortIndexs = table(
	SortRarity,
	SortLevel,
	SortPower,
	SortAchivedTime,
	SortIntimacy,
	SortEnergy
)

def getSortFuncAndName(arg_1_0, arg_1_1):
	from view.ship.ShipIndexCfg import ShipIndexCfg
	for iter_1_0 in range(1, len(ShipIndexCfg.sort)):
		var_1_0 = bit.lshift(1, iter_1_0 - 1)

		if bit.band(var_1_0, arg_1_0) > 0:
			return underscore.map(ShipIndexCfg.sort[iter_1_0].sortFuncs, lambda arg_2_0: lambda arg_3_0: (arg_1_1 and -1 or 1) * arg_2_0(arg_3_0)), ShipIndexCfg.sort[iter_1_0].name

SortNames = table(
	"word_rarity",
	"word_lv",
	"word_synthesize_power",
	"word_achieved_item",
	"attribute_intimacy",
	"sort_energy"
)
SortPropertyNames = table(
	"sort_attribute",
	"word_attr_cannon",
	"word_attr_air",
	"word_attr_dodge",
	"word_attr_antiaircraft",
	"word_attr_torpedo",
	"word_attr_reload",
	"word_attr_durability",
	"word_attr_antisub"
)

def sortByCombatPower():
	return table(
		lambda arg_5_0: -arg_5_0.getShipCombatPower(),
		lambda arg_6_0: arg_6_0.configId
	)

def sortByField(arg_7_0):
	return table(
		lambda arg_8_0: -arg_8_0[arg_7_0],
		lambda arg_9_0: -arg_9_0.getRarity(),
		lambda arg_10_0: arg_10_0.configId
	)

def sortByProperty(arg_11_0):
	return table(
		lambda arg_12_0: -arg_12_0.getShipProperties()[arg_11_0],
		lambda arg_13_0: arg_13_0.configId
	)

def sortByCfg(arg_14_0):
	return table(
		lambda arg_15_0: -(arg_14_0 == "rarity" and arg_15_0.getRarity() or arg_15_0.getConfig(arg_14_0)),
		lambda arg_16_0: arg_16_0.configId
	)

def sortByIntimacy():
	return table(
		lambda arg_18_0: -arg_18_0.intimacy,
		lambda arg_19_0: arg_19_0.propose and 0 or 1,
		lambda arg_20_0: arg_20_0.configId,
		lambda arg_21_0: -arg_21_0.level
	)

def sortByEnergy():
	return table(
		lambda arg_23_0: -arg_23_0.getEnergy(),
		lambda arg_24_0: arg_24_0.configId
	)

TypeFront = bit.lshift(1, 0)
TypeBack = bit.lshift(1, 1)
TypeQuZhu = bit.lshift(1, 2)
TypeQingXun = bit.lshift(1, 3)
TypeZhongXun = bit.lshift(1, 4)
TypeZhanLie = bit.lshift(1, 5)
TypeHangMu = bit.lshift(1, 6)
TypeWeiXiu = bit.lshift(1, 7)
TypeQianTing = bit.lshift(1, 8)
TypeOther = bit.lshift(1, 9)
TypeIndexs = table(
	TypeFront,
	TypeBack,
	TypeQuZhu,
	TypeQingXun,
	TypeZhongXun,
	TypeZhanLie,
	TypeHangMu,
	TypeWeiXiu,
	TypeQianTing,
	TypeOther
)
TypeAll = IndexConst.BitAll(TypeIndexs)

table.insert(TypeIndexs, 1, TypeAll)

TypeNames = table(
	"index_all",
	"index_fleetfront",
	"index_fleetrear",
	"index_shipType_quZhu",
	"index_shipType_qinXun",
	"index_shipType_zhongXun",
	"index_shipType_zhanLie",
	"index_shipType_hangMu",
	"index_shipType_weiXiu",
	"index_shipType_qianTing",
	"index_other"
)

def filterByType(arg_25_0, arg_25_1):
	if not arg_25_1 or arg_25_1 == TypeAll:
		return True

	for iter_25_0 in range(2, len(ShipIndexCfg.type)):
		var_25_0 = bit.lshift(1, iter_25_0 - 2)

		if bit.band(var_25_0, arg_25_1) > 0:
			var_25_1 = ShipIndexCfg.type[iter_25_0].types

			if iter_25_0 < 4:
				var_25_2 = ShipIndexCfg.type[iter_25_0].shipTypes

				if table.contains(var_25_1, arg_25_0.getShipType()):
					return True

				if table.contains(var_25_1, arg_25_0.getTeamType()):
					return True
			elif table.contains(var_25_1, arg_25_0.getShipType()):
				return True

	return False

CampUS = bit.lshift(1, 0)
CampEN = bit.lshift(1, 1)
CampJP = bit.lshift(1, 2)
CampDE = bit.lshift(1, 3)
CampCN = bit.lshift(1, 4)
CampITA = bit.lshift(1, 5)
CampSN = bit.lshift(1, 6)
CampFF = bit.lshift(1, 7)
CampMNF = bit.lshift(1, 8)
CampMETA = bit.lshift(1, 9)
CampMot = bit.lshift(1, 10)
CampOther = bit.lshift(1, 11)
CampIndexs = table(
	CampUS,
	CampEN,
	CampJP,
	CampDE,
	CampCN,
	CampITA,
	CampSN,
	CampFF,
	CampMNF,
	CampMETA,
	CampMot,
	CampOther
)
CampAll = IndexConst.BitAll(CampIndexs)

table.insert(CampIndexs, 1, CampAll)

CampNames = table(
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
	"word_shipNation_meta_index",
	"word_shipNation_mot",
	"word_shipNation_other"
)

def filterByCamp(arg_26_0, arg_26_1):
	if not arg_26_1 or arg_26_1 == CampAll:
		return True

	from view.ship.ShipIndexCfg import ShipIndexCfg
	for iter_26_0 in range(2, len(ShipIndexCfg.camp)):
		var_26_0 = bit.lshift(1, iter_26_0 - 2)

		if bit.band(var_26_0, arg_26_1) > 0:
			var_26_1 = ShipIndexCfg.camp[iter_26_0].types

			for iter_26_1, iter_26_2 in ipairs(var_26_1):
				if iter_26_2 == Nation.LINK:
					if arg_26_0.getNation() >= Nation.LINK:
						return True
				elif iter_26_2 == arg_26_0.getNation():
					return True

	return False

Rarity1 = bit.lshift(1, 0)
Rarity2 = bit.lshift(1, 1)
Rarity3 = bit.lshift(1, 2)
Rarity4 = bit.lshift(1, 3)
Rarity5 = bit.lshift(1, 4)
RarityIndexs = table(
	Rarity1,
	Rarity2,
	Rarity3,
	Rarity4,
	Rarity5
)
RarityAll = IndexConst.BitAll(RarityIndexs)

table.insert(RarityIndexs, 1, RarityAll)

RarityNames = table(
	"index_all",
	"index_rare2",
	"index_rare3",
	"index_rare4",
	"index_rare5",
	"index_rare6"
)

def filterByRarity(arg_27_0, arg_27_1):
	if not arg_27_1 or arg_27_1 == RarityAll:
		return True
	from view.ship.ShipIndexCfg import ShipIndexCfg
	for iter_27_0 in range(2, len(ShipIndexCfg.rarity)):
		var_27_0 = bit.lshift(1, iter_27_0 - 2)

		if bit.band(var_27_0, arg_27_1) > 0:
			var_27_1 = ShipIndexCfg.rarity[iter_27_0].types

			if table.contains(var_27_1, arg_27_0.getRarity()):
				return True

	return False

MetaRarityIndexs = table(
	RarityAll,
	Rarity3,
	Rarity4
)
MetaRarityNames = table(
	"index_all",
	"index_rare4",
	"index_rare5"
)
MetaExtraRepair = bit.lshift(1, 0)
MetaExtraTactics = bit.lshift(1, 1)
MetaExtraEnergy = bit.lshift(1, 2)
MetaExtraIndexs = table(
	MetaExtraRepair,
	MetaExtraTactics,
	MetaExtraEnergy
)
MetaExtraAll = IndexConst.BitAll(MetaExtraIndexs)

table.insert(MetaExtraIndexs, 1, MetaExtraAll)

MetaExtraNames = table(
	"index_no_limit",
	"index_meta_repair",
	"index_meta_tactics",
	"index_meta_energy"
)
ExtraSkin = bit.lshift(1, 0)
ExtraRemould = bit.lshift(1, 1)
Extrastrengthen = bit.lshift(1, 2)
ExtraUpgrade = bit.lshift(1, 3)
ExtraNotMaxLv = bit.lshift(1, 4)
ExtraAwakening = bit.lshift(1, 5)
ExtraAwakening2 = bit.lshift(1, 6)
ExtraSpecial = bit.lshift(1, 7)
ExtraProposeSkin = bit.lshift(1, 8)

if not LOCK_SP_WEAPON:
	ExtraUniqueSpWeapon = bit.lshift(1, 9)
	DRESSED = bit.lshift(1, 10)
	ExtraMarry = bit.lshift(1, 11)
else:
	DRESSED = bit.lshift(1, 9)
	ExtraMarry = bit.lshift(1, 10)

ExtraIndexs = table(
	ExtraSkin,
	ExtraRemould,
	Extrastrengthen,
	ExtraUpgrade,
	ExtraNotMaxLv,
	ExtraAwakening,
	ExtraAwakening2,
	ExtraSpecial,
	ExtraProposeSkin
)

if not LOCK_SP_WEAPON:
	table.insert(ExtraIndexs, ExtraUniqueSpWeapon)

table.insert(ExtraIndexs, DRESSED)
table.insert(ExtraIndexs, ExtraMarry)

ExtraAll = IndexConst.BitAll(ExtraIndexs)

table.insert(ExtraIndexs, 1, ExtraAll)

ExtraNames = table(
	"index_no_limit",
	"index_skin",
	"index_reform_cw",
	"index_strengthen",
	"index_upgrade",
	"index_not_lvmax",
	"index_awakening",
	"index_awakening2",
	"index_special",
	"index_propose_skin"
)

if not LOCK_SP_WEAPON:
	ExtraNames[11] = "index_spweapon"

table.insert(ExtraNames, "index_dressed")
table.insert(ExtraNames, "index_marry")

def filterByExtra(arg_28_0, arg_28_1):
	if not arg_28_1 or arg_28_1 == ExtraAll:
		return True

	if arg_28_1 == ExtraSkin:
		return arg_28_0.hasAvailiableSkin()
	elif arg_28_1 == ExtraRemould:
		return arg_28_0.isRemouldable() and not arg_28_0.isAllRemouldFinish()
	elif arg_28_1 == Extrastrengthen:
		return not arg_28_0.isMetaShip() and not arg_28_0.isIntensifyMax()
	elif arg_28_1 == ExtraUpgrade:
		return arg_28_0.canUpgrade()
	elif arg_28_1 == ExtraNotMaxLv:
		return arg_28_0.notMaxLevelForFilter()
	elif arg_28_1 == ExtraAwakening:
		return arg_28_0.isAwakening()
	elif arg_28_1 == ExtraAwakening2:
		return arg_28_0.isAwakening2()
	elif arg_28_1 == ExtraSpecial:
		return arg_28_0.isSpecialFilter()
	elif arg_28_1 == ExtraProposeSkin:
		return arg_28_0.hasProposeSkin()
	elif arg_28_1 == ExtraUniqueSpWeapon:
		return arg_28_0.HasUniqueSpWeapon()
	elif arg_28_1 == DRESSED:
		return not arg_28_0.IsDefaultSkin() and arg_28_0.getRemouldSkinId() != arg_28_0.skinId
	elif arg_28_1 == ExtraMarry:
		return arg_28_0.propose

	return False

CollExtraSpecial = bit.lshift(1, 0)
CollExtraNotObtained = bit.lshift(1, 1)
CollExtraIndexs = table(
	CollExtraSpecial,
	CollExtraNotObtained
)
CollExtraAll = IndexConst.BitAll(CollExtraIndexs)

table.insert(CollExtraIndexs, 1, CollExtraAll)

CollExtraNames = table(
	"index_no_limit",
	"index_special",
	"index_not_obtained"
)

def filterByCollExtra(arg_29_0, arg_29_1):
	if not arg_29_1 or arg_29_1 == CollExtraAll:
		return True

	if arg_29_1 == CollExtraSpecial:
		return arg_29_0.isSpecialFilter()

	if arg_29_1 == CollExtraNotObtained:
		var_29_0 = arg_29_0.getGroupId()
		var_29_1 = arg_29_0.isRemoulded()
		var_29_2 = getProxy(CollectionProxy).getShipGroup(var_29_0)

		if ShipGroup.getState(var_29_0, var_29_2, var_29_1) != ShipGroup.STATE_UNLOCK:
			return True

	return False

