from packages.luatable import table, Clone, pairs, ipairs
from packages.alsupport import Mathf, math, defaultValue, calcFloor, tonumber, intProperties

from const import *
from Framework import underscore
from Framework.i18n import i18n
from Framework.levelExp import getConfigFromLevel1
from Framework.tolua.tolua import PlayerPrefs
from RunPaintingFilte import PLATFORM_US, PLATFORM_CH
from lib import pg

from main import PLATFORM_CODE
from mod.battle.BattleState import bfConsts
from mod.battle.data import BattleConfig
from mod.experiment.world.model import WorldConst
from model.const import Nation, ShipType, ArmorType, EquipType, ShipModAttr, AttributeType, ShipRarity, TeamType
from model.const.ShipRarity import shipRarity2bgPrint
from model.proxy.BagProxy import BagProxy
from model.proxy.BayProxy import BayProxy
from model.proxy.CollectionProxy import CollectionProxy #!
from model.proxy.EquipmentProxy import EquipmentProxy #!
from model.proxy.PlayerProxy import PlayerProxy #!
from model.proxy.ShipSkinProxy import ShipSkinProxy
from model.proxy.TechnologyNationProxy import TechnologyNationProxy #!
from model.vo.BaseVO import BaseVO
from model.vo.Equipment import Equipment #!
from model.vo.metacharacter.MetaCharacter import MetaCharacter #!
from model.vo.ShipBluePrint import ShipBluePrint #!
from model.vo.ShipGroup import ShipGroup
from model.vo.ShipSkin import ShipSkin
from model.vo.SpWeapon import SpWeapon #!
from support.helpers.M02 import getProxy, CreateShell, setColorStr
from support.utils.HXSet import HXSet
from view.technology.metacharacter import MetaCharacterConst

def nation2print(arg_1_0):
	return Nation.Nation2Print(arg_1_0)

def getRecoverEnergyPoint(arg_2_0):
	return arg_2_0.propose and 3 or 2

def shipType2name(arg_3_0):
	return ShipType.Type2Name(arg_3_0)

def shipType2print(arg_4_0):
	return ShipType.Type2Print(arg_4_0)

def shipType2Battleprint(arg_5_0):
	return ShipType.Type2BattlePrint(arg_5_0)

def skinId2bgPrint(arg_6_0):
	var_6_0 = pg.ship_skin_template[arg_6_0].rarity_bg

	if var_6_0 and var_6_0 != "":
		return var_6_0

pg.ship_data_strengthen = pg.ship_data_strengthen
var_0_6 = pg.ship_level
var_0_7 = pg.equip_skin_template
var_0_8 = pg.ship_data_breakout

class Ship(BaseVO):

	ENERGY_MID = 40
	ENERGY_LOW = 0
	RECOVER_ENERGY_POINT = 2
	INTIMACY_PROPOSE = 6
	CONFIG_MAX_STAR = 6
	BACKYARD_1F_ENERGY_ADDITION = 2
	BACKYARD_2F_ENERGY_ADDITION = 3
	PREFERENCE_TAG_NONE = 0
	PREFERENCE_TAG_COMMON = 1

	var_0_1 = table(
		vanguard = i18n("word_vanguard_fleet"),
		main = i18n("word_main_fleet")
	)

	CVBattleKey = table(
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
	)
	LOCK_STATE_UNLOCK = 0
	LOCK_STATE_LOCK = 1
	WEAPON_COUNT = 3
	PREFAB_EQUIP = 4
	MAX_SKILL_LEVEL = 10
	ENERGY_RECOVER_TIME = 360
	STATE_NORMAL = 1
	STATE_REST = 2
	STATE_CLASS = 3
	STATE_COLLECT = 4
	STATE_TRAIN = 5

	def rarity2bgPrint(arg_7_0):
		return shipRarity2bgPrint(arg_7_0.getRarity(), arg_7_0.isBluePrintShip(), arg_7_0.isMetaShip())

	def rarity2bgPrintForGet(arg_8_0):
		return skinId2bgPrint(arg_8_0.skinId) or arg_8_0.rarity2bgPrint()

	def getShipBgPrint(arg_9_0, arg_9_1):
		var_9_0 = pg.ship_skin_template[arg_9_0.skinId]

		assert var_9_0, f"ship_skin_template not exist. {arg_9_0.skinId}"

		var_9_1 = None

		if not arg_9_1 and var_9_0.bg_sp and var_9_0.bg_sp != "" and PlayerPrefs.GetInt("paint_hide_other_obj_{var_9_0.painting}", 0) == 0:
			var_9_1 = var_9_0.bg_sp

		return var_9_1 and var_9_1 or var_9_0.bg and len(var_9_0.bg) > 0 and var_9_0.bg or arg_9_0.rarity2bgPrintForGet()

	def getStar(arg_10_0):
		return arg_10_0.getConfig("star")

	def getMaxStar(arg_11_0):
		return pg.ship_data_template[arg_11_0.configId].star_max

	def getShipArmor(arg_12_0):
		return arg_12_0.getConfig("armor_type")

	def getShipArmorName(arg_13_0):
		var_13_0 = arg_13_0.getShipArmor()

		return ArmorType.Type2Name(var_13_0)

	def getGroupId(arg_14_0):
		return pg.ship_data_template[arg_14_0.configId].group_type

	def getGroupIdByConfigId(arg_15_0):
		return int(arg_15_0 / 10)

	def getShipWords(arg_16_0):
		var_16_0 = pg.ship_skin_words[arg_16_0]

		if not var_16_0:
			print("找不到ship_skin_words. {arg_16_0}")

			return

		var_16_1 = Clone(var_16_0)

		for iter_16_0, iter_16_1 in pairs(var_16_1):
			if type(iter_16_1) == str:
				var_16_1[iter_16_0] = HXSet.hxLan(iter_16_1)

		var_16_2 = pg.ship_skin_words_extra[arg_16_0]

		return var_16_1, var_16_2

	def getMainwordsCount(arg_17_0):
		var_17_0 = Ship.getShipWords(arg_17_0)

		if not var_17_0.main or var_17_0.main == "":
			var_17_0 = Ship.getShipWords(Ship.getOriginalSkinId(arg_17_0))

		return len(var_17_0.main.split("|"))

	def getWordsEx(arg_18_0, arg_18_1, arg_18_2, arg_18_3, arg_18_4, arg_18_5):
		var_18_0 = arg_18_0 and arg_18_0[arg_18_1] or None
		var_18_1 = False

		if not var_18_0 or var_18_0 == "":
			if arg_18_0 and arg_18_0.id == arg_18_4:
				return

			if not arg_18_5:
				return

			var_18_2, var_18_3 = Ship.getShipWords(arg_18_4)

			if not var_18_3:
				return

			var_18_0 = var_18_3[arg_18_1]

			if not var_18_0:
				return

			var_18_1 = True

		if type(var_18_0) == str:
			return

		arg_18_3 = arg_18_3 or 0

		for iter_18_0, iter_18_1 in ipairs(var_18_0):
			if arg_18_3 >= iter_18_1[1]:
				if arg_18_1 == "main":
					return iter_18_1[2].split("|")[arg_18_2], iter_18_1[1], var_18_1
				else:
					return iter_18_1[2], iter_18_1[1], var_18_1

	def getWords(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4):
		var_19_0, var_19_1 = Ship.getShipWords(arg_19_0)
		var_19_2 = Ship.getOriginalSkinId(arg_19_0)
		var_19_3 = arg_19_0 % var_19_2

		if not var_19_0:
			var_19_0, var_19_1 = Ship.getShipWords(var_19_2)

			if not var_19_0:
				return None

		var_19_4 = 0
		var_19_5 = False
		var_19_6 = var_19_0[arg_19_1]

		if not var_19_6 or var_19_6 == "":
			var_19_5 = True

			if var_19_0.id == var_19_2:
				return None
			else:
				var_19_0 = Ship.getShipWords(var_19_2)

				if not var_19_0:
					return None

				var_19_6 = var_19_0[arg_19_1]

				if not var_19_6 or var_19_6 == "":
					return None

		var_19_7 = var_19_6.split("|")
		var_19_8 = arg_19_2 or math.random(len(var_19_7))

		if arg_19_1 == "main" and var_19_7[var_19_8] == "None":
			var_19_5 = True
			var_19_0 = Ship.getShipWords(var_19_2)

			if not var_19_0:
				return None

			var_19_9 = var_19_0[arg_19_1]

			if not var_19_9 or var_19_9 == "":
				return None

			var_19_7 = var_19_9.split("|")

		rstEx, cvEx, defaultCoverEx = Ship.getWordsEx(var_19_1, arg_19_1, var_19_8, arg_19_4, var_19_2, var_19_5)

		var_19_10
		var_19_11 = PlayerPrefs.GetInt(f"CV_LANGUAGE_{pg.ship_skin_template[arg_19_0].ship_group}") == 2 and var_19_0.voice_key_2 or var_19_0.voice_key

		if var_19_11 == 0:
			if not var_19_5 or rstEx and not defaultCoverEx:
				var_19_10 = Ship.getCVPath(var_19_2, arg_19_1, var_19_8, var_19_3)
		elif var_19_11 == -2:
			pass#-- block empty
		else:
			var_19_10 = Ship.getCVPath(var_19_2, arg_19_1, var_19_8)

		var_19_12 = var_19_7[var_19_8]

		if var_19_12 and (arg_19_3 == None and PLATFORM_CODE != PLATFORM_US or arg_19_3 == True):
			var_19_12 = var_19_12.gsub("%s", " ")

		if rstEx:
			var_19_10 = var_19_10 and f"{var_19_10}_ex{cvEx}"

		return rstEx or var_19_12, var_19_10, cvEx

	def getCVKeyID(arg_20_0):
		var_20_0 = Ship.getShipWords(arg_20_0)

		if not var_20_0:
			return -1

		var_20_2 = PlayerPrefs.GetInt(f"CV_LANGUAGE_{pg.ship_skin_template[arg_20_0].ship_group}")
		var_20_3 = var_20_2 == 2 and var_20_0.voice_key_2 >= 0 and var_20_0.voice_key_2 or var_20_0.voice_key

		if var_20_3 == 0 or var_20_3 == -2:
			var_20_4 = Ship.getOriginalSkinId(arg_20_0)
			var_20_5 = Ship.getShipWords(var_20_4)

			var_20_3 = var_20_2 == 2 and var_20_5.voice_key_2 >= 0 and var_20_5.voice_key_2 or var_20_5.voice_key

		return var_20_3

	def getCVPath(arg_21_0, arg_21_1, arg_21_2, arg_21_3):
		arg_21_2 = arg_21_2 or 1

		var_21_0 = Ship.getShipWords(arg_21_0)
		var_21_1 = Ship.getOriginalSkinId(arg_21_0)

		if not var_21_0:
			var_21_0 = Ship.getShipWords(var_21_1)

			if not var_21_0:
				return

		var_21_2 = PlayerPrefs.GetInt(f"CV_LANGUAGE_{arg_21_0 / 10}")
		var_21_3 = var_21_0[arg_21_1]

		if arg_21_1 == "main":
			var_21_3 = var_21_3.split("|")[arg_21_2]
			arg_21_1 = arg_21_1 + arg_21_2

		if arg_21_1 == "skill" or "link" in arg_21_1:
			if var_21_0.voice_key == 0:
				var_21_0 = Ship.getShipWords(var_21_1)
		elif not var_21_3 or var_21_3 == "" or var_21_3 == "None":
			var_21_0 = Ship.getShipWords(var_21_1)

		var_21_5 = var_21_2 == 2 and var_21_0.voice_key_2 or var_21_0.voice_key

		if var_21_5 != -1 and pg.character_voice[arg_21_1]:
			var_21_4 = pg.character_voice[arg_21_1].resource_key

			if var_21_4:
				var_21_4 = f"event./cv/{var_21_5}/{var_21_4}"

				if arg_21_3:
					var_21_4 = f"{var_21_4}_{arg_21_3}"

		return var_21_4

	def getCVCalibrate(arg_22_0, arg_22_1, arg_22_2):
		var_22_0 = pg.ship_skin_template[arg_22_0]

		if not var_22_0:
			return 0

		if arg_22_1 == "main":
			arg_22_1 = f"{arg_22_1}_{arg_22_2}"

		return var_22_0.l2d_voice_calibrate[arg_22_1]

	def getL2dSoundEffect(arg_23_0, arg_23_1, arg_23_2):
		var_23_0 = pg.ship_skin_template[arg_23_0]

		if not var_23_0:
			return 0

		if arg_23_1 == "main":
			arg_23_1 = f"{arg_23_1}_{arg_23_2}"

		return var_23_0.l2d_se[arg_23_1]

	def getOriginalSkinId(arg_24_0):
		var_24_0 = pg.ship_skin_template[arg_24_0].ship_group

		return ShipGroup.getDefaultSkin(var_24_0).id

	def getTransformShipId(arg_25_0):
		var_25_0 = pg.ship_data_template[arg_25_0].group_type
		var_25_1 = pg.ship_data_trans[var_25_0]

		if var_25_1:
			for iter_25_0, iter_25_1 in ipairs(var_25_1.transform_list):
				for iter_25_2, iter_25_3 in ipairs(iter_25_1):
					var_25_2 = pg.transform_data_template[iter_25_3[2]]

					for iter_25_4, iter_25_5 in ipairs(var_25_2.ship_id):
						if iter_25_5[1] == arg_25_0:
							return iter_25_5[2]

	def getAircraftCount(arg_26_0):
		var_26_0 = arg_26_0.getConfigTable().base_list
		var_26_1 = arg_26_0.getConfigTable().default_equip_list
		var_26_2 = table()

		for iter_26_0 in range(1, 4):
			var_26_3 = arg_26_0.getEquip(iter_26_0) and arg_26_0.getEquip(iter_26_0).configId or var_26_1[iter_26_0]
			var_26_4 = Equipment.getConfigData(var_26_3).type

			if table.contains(EquipType.AirDomainEquip, var_26_4):
				var_26_2[var_26_4] = defaultValue(var_26_2[var_26_4], 0) + var_26_0[iter_26_0]

		return var_26_2

	def getShipType(arg_27_0):
		return arg_27_0.getConfig("type")

	def getEnergy(arg_28_0):
		return arg_28_0.energy

	def getEnergeConfig(arg_29_0):
		var_29_0 = pg.energy_template
		var_29_1 = arg_29_0.getEnergy()

		for iter_29_0, iter_29_1 in pairs(var_29_0):
			if type(iter_29_0) == "number" and var_29_1 >= iter_29_1.lower_bound and var_29_1 <= iter_29_1.upper_bound:
				return iter_29_1

		assert False, f"疲劳配置不存在：{arg_29_0.energy}"

	def getEnergyPrint(arg_30_0):
		var_30_0 = arg_30_0.getEnergeConfig()

		return var_30_0.icon, var_30_0.desc

	def getIntimacy(arg_31_0):
		return arg_31_0.intimacy

	def getCVIntimacy(arg_32_0):
		return arg_32_0.getIntimacy() / 100 + (arg_32_0.propose and 1000 or 0)

	def getIntimacyMax(arg_33_0):
		if arg_33_0.propose:
			return 200
		else:
			return arg_33_0.GetNoProposeIntimacyMax()

	def GetNoProposeIntimacyMax(arg_34_0):
		return 100

	def getIntimacyIcon(arg_35_0):
		var_35_0 = pg.intimacy_template[arg_35_0.getIntimacyLevel()]
		var_35_1 = ""

		if arg_35_0.isMetaShip():
			var_35_1 = "_meta"
		elif arg_35_0.IsXIdol():
			var_35_1 = "_imas"

		if not arg_35_0.propose and math.floor(arg_35_0.getIntimacy() / 100) >= arg_35_0.getIntimacyMax():
			return f"{var_35_0.icon}{var_35_1}", f"heart{var_35_1}"
		else:
			return f"{var_35_0.icon}{var_35_1}"

	def getIntimacyDetail(arg_36_0):
		return arg_36_0.getIntimacyMax(), math.floor(arg_36_0.getIntimacy() / 100)

	def getIntimacyInfo(arg_37_0):
		var_37_0 = pg.intimacy_template[arg_37_0.getIntimacyLevel()]

		return var_37_0.icon, var_37_0.desc

	def getIntimacyLevel(arg_38_0):
		var_38_0 = 0
		var_38_1 = pg.intimacy_template

		for iter_38_0, iter_38_1 in pairs(var_38_1):
			if type(iter_38_0) == "number" and arg_38_0.getIntimacy() >= iter_38_1.lower_bound and arg_38_0.getIntimacy() <= iter_38_1.upper_bound:
				var_38_0 = iter_38_0

				break

		if var_38_0 < arg_38_0.INTIMACY_PROPOSE and arg_38_0.propose:
			var_38_0 = arg_38_0.INTIMACY_PROPOSE

		return var_38_0

	def getBluePrint(arg_39_0):
		var_39_0 = ShipBluePrint.New(table(
			id = arg_39_0.groupId
		))
		var_39_1 = arg_39_0.strengthList[1] or table(
			exp = 0,
			level = 0
		)

		var_39_0.updateInfo(table(
			blue_print_level = var_39_1.level,
			exp = var_39_1.exp
		))

		return var_39_0

	def getBaseList(arg_40_0):
		if arg_40_0.isBluePrintShip():
			var_40_0 = arg_40_0.getBluePrint()

			assert var_40_0, f"blueprint can not be None{arg_40_0.configId}"

			return var_40_0.getBaseList(arg_40_0)
		else:
			return arg_40_0.getConfig("base_list")

	def getPreLoadCount(arg_41_0):
		if arg_41_0.isBluePrintShip():
			return arg_41_0.getBluePrint().getPreLoadCount(arg_41_0)
		else:
			return arg_41_0.getConfig("preload_count")

	def getNation(arg_42_0):
		return arg_42_0.getConfig("nationality")

	def getPaintingName(arg_43_0):
		var_43_0 = pg.ship_data_statistics[arg_43_0].skin_id
		var_43_1 = pg.ship_skin_template[var_43_0]

		assert var_43_1, f"ship_skin_template not exist. {arg_43_0} {var_43_0}"

		return var_43_1.painting

	def getName(arg_44_0):
		if arg_44_0.propose and pg.PushNotificationMgr.GetInstance().isEnableShipName():
			return arg_44_0.name

		if arg_44_0.isRemoulded():
			return pg.ship_skin_template[arg_44_0.getRemouldSkinId()].name

		return pg.ship_data_statistics[arg_44_0.configId].name

	def GetDefaultName(arg_45_0):
		if arg_45_0.isRemoulded():
			return pg.ship_skin_template[arg_45_0.getRemouldSkinId()].name
		else:
			return pg.ship_data_statistics[arg_45_0.configId].name

	def getShipName(arg_46_0):
		return pg.ship_data_statistics[arg_46_0].name

	def getBreakOutLevel(arg_47_0):
		assert arg_47_0, "必须存在配置id"
		assert pg.ship_data_statistics[arg_47_0], f"必须存在配置{arg_47_0}"

		return pg.ship_data_statistics[arg_47_0].star

	def Ctor(arg_48_0, arg_48_1):
		arg_48_0.id = arg_48_1.id
		arg_48_0.configId = arg_48_1.template_id or arg_48_1.configId
		arg_48_0.level = arg_48_1.level
		arg_48_0.exp = arg_48_1.exp
		arg_48_0.energy = arg_48_1.energy
		arg_48_0.lockState = arg_48_1.is_locked
		arg_48_0.intimacy = arg_48_1.intimacy
		arg_48_0.propose = arg_48_1.propose and arg_48_1.propose > 0
		arg_48_0.proposeTime = arg_48_1.propose

		if arg_48_0.intimacy and arg_48_0.intimacy > 10000 and not arg_48_0.propose:
			arg_48_0.intimacy = 10000

		arg_48_0.renameTime = arg_48_1.change_name_timestamp

		if arg_48_1.name and arg_48_1.name != "":
			arg_48_0.name = arg_48_1.name
		else:
			assert pg.ship_data_statistics[arg_48_0.configId], f"必须存在配置{arg_48_0.configId}"

			arg_48_0.name = pg.ship_data_statistics[arg_48_0.configId].name

		arg_48_0.bluePrintFlag = arg_48_1.blue_print_flag or 0
		arg_48_0.strengthList = table()

		for iter_48_0, iter_48_1 in ipairs(arg_48_1.strength_list or table()):
			if not arg_48_0.isBluePrintShip():
				var_48_0 = ShipModAttr.ID_TO_ATTR[iter_48_1.id]

				arg_48_0.strengthList[var_48_0] = iter_48_1.exp
			else:
				table.insert(arg_48_0.strengthList, table(
					level = iter_48_1.id,
					exp = iter_48_1.exp
				))

		var_48_1 = arg_48_1.state or table()

		arg_48_0.state = var_48_1.state
		arg_48_0.state_info_1 = var_48_1.state_info_1
		arg_48_0.state_info_2 = var_48_1.state_info_2
		arg_48_0.state_info_3 = var_48_1.state_info_3
		arg_48_0.state_info_4 = var_48_1.state_info_4
		arg_48_0.equipmentSkins = table()
		arg_48_0.equipments = table()

		if arg_48_1.equip_info_list:
			for iter_48_2, iter_48_3 in ipairs(arg_48_1.equip_info_list or table()):
				arg_48_0.equipments[iter_48_2] = iter_48_3.id > 0 and Equipment.New(table(
					count = 1,
					id = iter_48_3.id,
					config_id = iter_48_3.id,
					skinId = iter_48_3.skinId
				)) or False
				arg_48_0.equipmentSkins[iter_48_2] = iter_48_3.skinId > 0 and iter_48_3.skinId or 0

				arg_48_0.reletiveEquipSkin(iter_48_2)

		arg_48_0.spWeapon = None

		if arg_48_1.spweapon:
			arg_48_0.UpdateSpWeapon(SpWeapon.CreateByNet(arg_48_1.spweapon))

		arg_48_0.skills = table()

		for iter_48_4, iter_48_5 in ipairs(arg_48_1.skill_id_list or table()):
			arg_48_0.updateSkill(iter_48_5)

		arg_48_0.star = arg_48_0.getConfig("rarity")
		arg_48_0.transforms = table()

		for iter_48_6, iter_48_7 in ipairs(arg_48_1.transform_list or table()):
			arg_48_0.transforms[iter_48_7.id] = table(
				id = iter_48_7.id,
				level = iter_48_7.level
			)

		arg_48_0.groupId = pg.ship_data_template[arg_48_0.configId].group_type
		arg_48_0.createTime = arg_48_1.create_time or 0

		var_48_2 = getProxy(CollectionProxy)

		arg_48_0.virgin = var_48_2 and var_48_2.shipGroups[arg_48_0.groupId] == None

		var_48_3 = table(
			pg.gameset.test_ship_config_1.key_value,
			pg.gameset.test_ship_config_2.key_value,
			pg.gameset.test_ship_config_3.key_value
		)
		var_48_4 = table.indexof(var_48_3, arg_48_0.configId)

		if var_48_4 == 1:
			arg_48_0.testShip = table(
				2,
				3,
				4
			)
		elif var_48_4 == 2:
			arg_48_0.testShip = table(
				5
			)
		elif var_48_4 == 3:
			arg_48_0.testShip = table(
				6
			)
		else:
			arg_48_0.testShip = None

		arg_48_0.maxIntimacy = pg.intimacy_template[len(pg.intimacy_template.all)].upper_bound

		if not HXSet.isHxSkin():
			arg_48_0.skinId = arg_48_1.skin_id or 0
		else:
			arg_48_0.skinId = 0

		if arg_48_0.skinId == 0:
			arg_48_0.skinId = arg_48_0.getConfig("skin_id")

		if arg_48_1.name and arg_48_1.name != "":
			arg_48_0.name = arg_48_1.name
		elif arg_48_0.isRemoulded():
			arg_48_0.name = pg.ship_skin_template[arg_48_0.getRemouldSkinId()].name
		else:
			arg_48_0.name = pg.ship_data_statistics[arg_48_0.configId].name

		arg_48_0.maxLevel = arg_48_1.max_level
		arg_48_0.proficiency = arg_48_1.proficiency or 0
		arg_48_0.preferenceTag = arg_48_1.common_flag
		arg_48_0.hpRant = 10000
		arg_48_0.strategies = table()
		arg_48_0.triggers = table()
		arg_48_0.commanderId = arg_48_1.commanderid or 0
		arg_48_0.activityNpc = arg_48_1.activity_npc or 0

		if Ship.isMetaShipByConfigID(arg_48_0.configId):
			var_48_5 = MetaCharacterConst.GetMetaShipGroupIDByConfigID(arg_48_0.configId)

			arg_48_0.metaCharacter = MetaCharacter.New(table(
				id = var_48_5,
				repair_attr_info = arg_48_1.meta_repair_list
			), arg_48_0)

	def isMetaShipByConfigID(arg_49_0):
		var_49_0 = pg.ship_meta_breakout.all
		var_49_1 = var_49_0[1]
		var_49_2 = False

		if var_49_1 <= arg_49_0:
			for iter_49_0, iter_49_1 in ipairs(var_49_0):
				if arg_49_0 == iter_49_1:
					var_49_2 = True

					break

		return var_49_2

	def isMetaShip(arg_50_0):
		return arg_50_0.metaCharacter != None

	def getMetaCharacter(arg_51_0):
		return arg_51_0.metaCharacter

	def unlockActivityNpc(arg_52_0, arg_52_1):
		arg_52_0.activityNpc = arg_52_1

	def isActivityNpc(arg_53_0):
		return arg_53_0.activityNpc > 0

	def getActiveEquipments(arg_54_0):
		var_54_0 = Clone(arg_54_0.equipments)

		for iter_54_0 in range(len(var_54_0), 1, -1):
			var_54_1 = var_54_0[iter_54_0]

			if var_54_1:
				for iter_54_1 in range(1, iter_54_0 - 1):
					var_54_2 = var_54_0[iter_54_1]

					if var_54_2 and var_54_1.getConfig("equip_limit") != 0 and var_54_2.getConfig("equip_limit") == var_54_1.getConfig("equip_limit"):
						var_54_0[iter_54_0] = False

		return var_54_0

	def getAllEquipments(arg_55_0):
		return arg_55_0.equipments

	def isBluePrintShip(arg_56_0):
		return arg_56_0.bluePrintFlag == 1

	def updateSkinId(arg_57_0, arg_57_1):
		arg_57_0.skinId = arg_57_1

	def updateName(arg_58_0):
		if arg_58_0.name != pg.ship_data_statistics[arg_58_0.configId].name:
			return

		if arg_58_0.isRemoulded():
			arg_58_0.name = pg.ship_skin_template[arg_58_0.getRemouldSkinId()].name
		else:
			arg_58_0.name = pg.ship_data_statistics[arg_58_0.configId].name

	def isRemoulded(arg_59_0):
		if arg_59_0.remoulded:
			return True

		var_59_0 = pg.ship_data_trans[arg_59_0.groupId]

		if var_59_0:
			for iter_59_0, iter_59_1 in ipairs(var_59_0.transform_list):
				for iter_59_2, iter_59_3 in ipairs(iter_59_1):
					var_59_1 = pg.transform_data_template[iter_59_3[2]]

					if var_59_1.skin_id != 0 and arg_59_0.transforms[iter_59_3[2]] and arg_59_0.transforms[iter_59_3[2]].level == var_59_1.max_level:
						return True

		return False

	def getRemouldSkinId(arg_60_0):
		var_60_0 = ShipGroup.getModSkin(arg_60_0.groupId)

		if var_60_0:
			return var_60_0.id

		return None

	def hasEquipmentSkinInPos(arg_61_0, arg_61_1):
		var_61_0 = arg_61_0.equipments[arg_61_1]

		return var_61_0 and var_61_0.hasSkin()

	def getPrefab(arg_62_0):
		var_62_0 = arg_62_0.skinId

		if arg_62_0.hasEquipmentSkinInPos(4):
			var_62_1 = arg_62_0.getEquip(4)
			var_62_2 = var_0_7[var_62_1.getSkinId()].ship_skin_id

			var_62_0 = var_62_2 != 0 and var_62_2 or var_62_0

		var_62_3 = pg.ship_skin_template[var_62_0]

		assert var_62_3, f"ship_skin_template not exist. {arg_62_0.configId} {var_62_0}"

		return var_62_3.prefab

	def getAttachmentPrefab(arg_63_0):
		var_63_0 = table()

		for iter_63_0, iter_63_1 in ipairs(arg_63_0.equipments):
			if iter_63_1 and iter_63_1.hasSkinOrbit():
				var_63_1 = iter_63_1.getSkinId()

				var_63_0[var_63_1] = var_0_7[var_63_1]

		return var_63_0

	def getPainting(arg_64_0):
		var_64_0 = pg.ship_skin_template[arg_64_0.skinId]

		assert var_64_0, f"ship_skin_template not exist. {arg_64_0.configId} {arg_64_0.skinId}"

		return var_64_0.painting

	def GetSkinConfig(arg_65_0):
		var_65_0 = pg.ship_skin_template[arg_65_0.skinId]

		assert var_65_0, f"ship_skin_template not exist. {arg_65_0.configId} {arg_65_0.skinId}"

		return var_65_0

	def getRemouldPainting(arg_66_0):
		var_66_0 = pg.ship_skin_template[arg_66_0.getRemouldSkinId()]

		assert var_66_0, f"ship_skin_template not exist. {arg_66_0.configId} {arg_66_0.skinId}"

		return var_66_0.painting

	def updateStateInfo34(arg_67_0, arg_67_1, arg_67_2):
		arg_67_0.state_info_3 = arg_67_1
		arg_67_0.state_info_4 = arg_67_2

	def hasStateInfo3Or4(arg_68_0):
		return arg_68_0.state_info_3 != 0 or arg_68_0.state_info_4 != 0

	def isTestShip(arg_69_0):
		return arg_69_0.testShip

	def canUseTestShip(arg_70_0, arg_70_1):
		assert arg_70_0.testShip, "ship is not TestShip"

		return table.contains(arg_70_0.testShip, arg_70_1)

	def updateEquip(arg_71_0, arg_71_1, arg_71_2):
		assert arg_71_2 == None or arg_71_2.count == 1

		var_71_0 = arg_71_0.equipments[arg_71_1]

		arg_71_0.equipments[arg_71_1] = arg_71_2 and Clone(arg_71_2) or False

		def var_71_1(arg_72_0):
			arg_72_0 = CreateShell(arg_72_0)
			arg_72_0.shipId = arg_71_0.id
			arg_72_0.shipPos = arg_71_1

			return arg_72_0

		if var_71_0:
			getProxy(EquipmentProxy).OnShipEquipsRemove(var_71_0, arg_71_0.id, arg_71_1)
			var_71_0.setSkinId(0)
			pg.m02.sendNotification(BayProxy.SHIP_EQUIPMENT_REMOVED, var_71_1(var_71_0))

		if arg_71_2:
			getProxy(EquipmentProxy).OnShipEquipsAdd(arg_71_2, arg_71_0.id, arg_71_1)
			arg_71_0.reletiveEquipSkin(arg_71_1)
			pg.m02.sendNotification(BayProxy.SHIP_EQUIPMENT_ADDED, var_71_1(arg_71_2))

	def reletiveEquipSkin(arg_73_0, arg_73_1):
		if arg_73_0.equipments[arg_73_1] and arg_73_0.equipmentSkins[arg_73_1] != 0:
			var_73_0 = pg.equip_skin_template[arg_73_0.equipmentSkins[arg_73_1]].equip_type
			var_73_1 = arg_73_0.equipments[arg_73_1].getType()

			if table.contains(var_73_0, var_73_1):
				arg_73_0.equipments[arg_73_1].setSkinId(arg_73_0.equipmentSkins[arg_73_1])
			else:
				arg_73_0.equipments[arg_73_1].setSkinId(0)
		elif arg_73_0.equipments[arg_73_1]:
			arg_73_0.equipments[arg_73_1].setSkinId(0)

	def updateEquipmentSkin(arg_74_0, arg_74_1, arg_74_2):
		if not arg_74_1:
			return

		if arg_74_2 and arg_74_2 > 0:
			var_74_0 = arg_74_0.getSkinTypes(arg_74_1)
			var_74_1 = pg.equip_skin_template[arg_74_2].equip_type
			var_74_2 = False

			for iter_74_0, iter_74_1 in ipairs(var_74_0):
				for iter_74_2, iter_74_3 in ipairs(var_74_1):
					if iter_74_1 == iter_74_3:
						var_74_2 = True

						break

			if not var_74_2:
				assert var_74_2, f"部位{arg_74_1} 无法穿戴皮肤 {arg_74_2}"

				return

			var_74_3 = arg_74_0.equipments[arg_74_1] and arg_74_0.equipments[arg_74_1].getType() or False

			arg_74_0.equipmentSkins[arg_74_1] = arg_74_2

			if var_74_3 and table.contains(var_74_1, var_74_3):
				arg_74_0.equipments[arg_74_1].setSkinId(arg_74_0.equipmentSkins[arg_74_1])
			elif var_74_3 and not table.contains(var_74_1, var_74_3):
				arg_74_0.equipments[arg_74_1].setSkinId(0)
		else:
			arg_74_0.equipmentSkins[arg_74_1] = 0

			if arg_74_0.equipments[arg_74_1]:
				arg_74_0.equipments[arg_74_1].setSkinId(0)

	def getEquip(arg_75_0, arg_75_1):
		return Clone(arg_75_0.equipments[arg_75_1])

	def getEquipSkins(arg_76_0):
		return Clone(arg_76_0.equipmentSkins)

	def getEquipSkin(arg_77_0, arg_77_1):
		return arg_77_0.equipmentSkins[arg_77_1]

	def getCanEquipSkin(arg_78_0, arg_78_1):
		var_78_0 = arg_78_0.getSkinTypes(arg_78_1)

		if var_78_0 and len(var_78_0):
			for iter_78_0, iter_78_1 in ipairs(var_78_0):
				if pg.equip_data_by_type[iter_78_1].equip_skin == 1:
					return True

		return False

	def checkCanEquipSkin(arg_79_0, arg_79_1, arg_79_2):
		if not arg_79_1 or not arg_79_2:
			return

		var_79_0 = arg_79_0.getSkinTypes(arg_79_1)
		var_79_1 = pg.equip_skin_template[arg_79_2].equip_type

		for iter_79_0, iter_79_1 in ipairs(var_79_0):
			if table.contains(var_79_1, iter_79_1):
				return True

		return False

	def getSkinTypes(arg_80_0, arg_80_1):
		return pg.ship_data_template[arg_80_0.configId][f"equip_{arg_80_1}"] or {}

	def updateState(arg_81_0, arg_81_1):
		arg_81_0.state = arg_81_1

	def addSkillExp(arg_82_0, arg_82_1, arg_82_2):
		var_82_0 = arg_82_0.skills[arg_82_1] or table(
			exp = 0,
			level = 1,
			id = arg_82_1
		)
		var_82_1 = var_82_0.level and var_82_0.level or 1
		var_82_2 = pg.skill_need_exp.all[-1]

		if var_82_1 == var_82_2:
			return

		var_82_3 = var_82_0.exp and arg_82_2 + var_82_0.exp or 0 + arg_82_2

		while var_82_3 >= pg.skill_need_exp[var_82_1].exp:
			var_82_3 = var_82_3 - pg.skill_need_exp[var_82_1].exp
			var_82_1 = var_82_1 + 1

			if var_82_1 == var_82_2:
				var_82_3 = 0

				break

		arg_82_0.updateSkill(table(
			id = var_82_0.id,
			level = var_82_1,
			exp = var_82_3
		))

	def upSkillLevelForMeta(arg_83_0, arg_83_1):
		var_83_0 = arg_83_0.skills[arg_83_1] or table(
			exp = 0,
			level = 0,
			id = arg_83_1
		)
		var_83_1 = arg_83_0.isSkillLevelMax(arg_83_1)
		var_83_2 = var_83_0.level

		if not var_83_1:
			var_83_2 = var_83_2 + 1

		arg_83_0.updateSkill(table(
			exp = 0,
			id = var_83_0.id,
			level = var_83_2
		))

	def getMetaSkillLevelBySkillID(arg_84_0, arg_84_1):
		return (arg_84_0.skills[arg_84_1] or table(
			exp = 0,
			level = 0,
			id = arg_84_1
		)).level

	def isSkillLevelMax(arg_85_0, arg_85_1):
		var_85_0 = arg_85_0.skills[arg_85_1] or table(
			exp = 0,
			level = 1,
			id = arg_85_1
		)

		return (var_85_0.level and var_85_0.level or 1) >= pg.skill_data_template[arg_85_1].max_level

	def isAllMetaSkillLevelMax(arg_86_0):
		var_86_0 = True
		var_86_1 = MetaCharacterConst.getTacticsSkillIDListByShipConfigID(arg_86_0.configId)

		for iter_86_0, iter_86_1 in ipairs(var_86_1):
			if not arg_86_0.isSkillLevelMax(iter_86_1):
				var_86_0 = False

				break

		return var_86_0

	def isAllMetaSkillLock(arg_87_0):
		var_87_0 = MetaCharacterConst.getTacticsSkillIDListByShipConfigID(arg_87_0.configId)
		var_87_1 = True

		for iter_87_0, iter_87_1 in ipairs(var_87_0):
			if arg_87_0.getMetaSkillLevelBySkillID(iter_87_1) > 0:
				var_87_1 = False

				break

		return var_87_1

	def bindConfigTable(arg_88_0):
		return pg.ship_data_statistics

	def isAvaiable(arg_89_0):
		return True

	PROPERTIES = table(
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
	)
	PROPERTIES_ENHANCEMENT = table(
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
	)
	DIVE_PROPERTIES = table(
		AttributeType.OxyMax,
		AttributeType.OxyCost,
		AttributeType.OxyRecovery,
		AttributeType.OxyRecoveryBench,
		AttributeType.OxyRecoverySurface,
		AttributeType.OxyAttackDuration,
		AttributeType.OxyRaidDistance
	)
	SONAR_PROPERTIES = table(
		AttributeType.SonarRange
	)

	def intimacyAdditions(arg_90_0, arg_90_1):
		var_90_0 = pg.intimacy_template[arg_90_0.getIntimacyLevel()].attr_bonus * 0.0001

		for iter_90_0, iter_90_1 in pairs(arg_90_1):
			if iter_90_0 == AttributeType.Durability or iter_90_0 == AttributeType.Cannon or iter_90_0 == AttributeType.Torpedo or iter_90_0 == AttributeType.AntiAircraft or iter_90_0 == AttributeType.AntiSub or iter_90_0 == AttributeType.Air or iter_90_0 == AttributeType.Reload or iter_90_0 == AttributeType.Hit or iter_90_0 == AttributeType.Dodge:
				arg_90_1[iter_90_0] = arg_90_1[iter_90_0] * (var_90_0 + 1)

	def getShipProperties(arg_91_0):
		var_91_0 = arg_91_0.getBaseProperties()

		if arg_91_0.isBluePrintShip():
			var_91_1 = arg_91_0.getBluePrint()

			assert var_91_1, f"blueprint can not be None{arg_91_0.configId}"

			var_91_2 = var_91_1.getTotalAdditions()

			for iter_91_0, iter_91_1 in pairs(var_91_2):
				var_91_0[iter_91_0] = var_91_0[iter_91_0] + calcFloor(iter_91_1)

			arg_91_0.intimacyAdditions(var_91_0)
		elif arg_91_0.isMetaShip():
			assert arg_91_0.metaCharacter

			for iter_91_2, iter_91_3 in pairs(var_91_0):
				var_91_0[iter_91_2] = var_91_0[iter_91_2] + arg_91_0.metaCharacter.getAttrAddition(iter_91_2)

			arg_91_0.intimacyAdditions(var_91_0)
		else:
			var_91_3 = pg.ship_data_template[arg_91_0.configId].strengthen_id
			var_91_4 = pg.ship_data_strengthen[var_91_3]

			for iter_91_4, iter_91_5 in pairs(arg_91_0.strengthList):
				var_91_5 = ShipModAttr.ATTR_TO_INDEX[iter_91_4]
				var_91_6 = math.min(iter_91_5, var_91_4.durability[var_91_5] * var_91_4.level_exp[var_91_5])
				var_91_7 = math.max(arg_91_0.getModExpRatio(iter_91_4), 1)

				var_91_0[iter_91_4] = var_91_0[iter_91_4] + calcFloor(var_91_6 / var_91_7)

			arg_91_0.intimacyAdditions(var_91_0)

			for iter_91_6, iter_91_7 in pairs(arg_91_0.transforms):
				var_91_8 = pg.transform_data_template[iter_91_7.id].effect

				for iter_91_8 in range(1, iter_91_7.level):
					var_91_9 = var_91_8[iter_91_8] or table()

					for iter_91_9, iter_91_10 in pairs(var_91_0):
						if var_91_9[iter_91_9]:
							var_91_0[iter_91_9] = var_91_0[iter_91_9] + var_91_9[iter_91_9]

		return var_91_0

	def getTechNationAddition(arg_92_0, arg_92_1):
		var_92_0 = getProxy(TechnologyNationProxy)
		var_92_1 = arg_92_0.getConfig("type")

		if var_92_1 == ShipType.DaoQuV or var_92_1 == ShipType.DaoQuM:
			var_92_1 = ShipType.QuZhu

		return var_92_0.getShipAddition(var_92_1, arg_92_1)

	def getTechNationMaxAddition(arg_93_0, arg_93_1):
		var_93_0 = getProxy(TechnologyNationProxy)
		var_93_1 = arg_93_0.getConfig("type")

		return var_93_0.getShipMaxAddition(var_93_1, arg_93_1)

	def getEquipProficiencyByPos(arg_94_0, arg_94_1):
		return arg_94_0.getEquipProficiencyList()[arg_94_1]

	def getEquipProficiencyList(arg_95_0):
		var_95_0 = arg_95_0.getConfigTable()
		var_95_1 = Clone(var_95_0.equipment_proficiency)

		if arg_95_0.isBluePrintShip():
			var_95_2 = arg_95_0.getBluePrint()

			assert var_95_2, f"blueprint can not be None >>>{arg_95_0.groupId}"

			var_95_1 = var_95_2.getEquipProficiencyList(arg_95_0)
		else:
			for iter_95_0, iter_95_1 in ipairs(var_95_1):
				var_95_3 = 0

				for iter_95_2, iter_95_3 in pairs(arg_95_0.transforms):
					var_95_4 = pg.transform_data_template[iter_95_3.id].effect

					for iter_95_4 in range( 1, iter_95_3.level):
						var_95_5 = var_95_4[iter_95_4] or table()

						if var_95_5[f"equipment_proficiency_{iter_95_0}"]:
							var_95_3 = var_95_3 + var_95_5[f"equipment_proficiency_{iter_95_0}"]

				var_95_1[iter_95_0] = iter_95_1 + var_95_3

		return var_95_1

	def getBaseProperties(arg_96_0):
		var_96_0 = arg_96_0.getConfigTable()

		assert var_96_0, f"配置表没有这艘船{arg_96_0.configId}"

		var_96_1 = table()
		var_96_2 = table()

		for iter_96_0, iter_96_1 in ipairs(Ship.PROPERTIES):
			var_96_1[iter_96_1] = arg_96_0.getGrowthForAttr(iter_96_1)
			var_96_2[iter_96_1] = var_96_1[iter_96_1]

		for iter_96_2, iter_96_3 in ipairs(arg_96_0.getConfig("lock")):
			var_96_2[iter_96_3] = var_96_1[iter_96_3]

		for iter_96_4, iter_96_5 in ipairs(Ship.DIVE_PROPERTIES):
			var_96_2[iter_96_5] = var_96_0[iter_96_5]

		for iter_96_6, iter_96_7 in ipairs(Ship.SONAR_PROPERTIES):
			var_96_2[iter_96_7] = 0

		return var_96_2

	def getGrowthForAttr(arg_97_0, arg_97_1):
		var_97_0 = arg_97_0.getConfigTable()
		var_97_1 = table.indexof(Ship.PROPERTIES, arg_97_1)
		var_97_2 = pg.gameset.extra_attr_level_limit.key_value
		var_97_3 = var_97_0.attrs[var_97_1] + (arg_97_0.level - 1) * var_97_0.attrs_growth[var_97_1] / 1000

		if var_97_2 < arg_97_0.level:
			var_97_3 = var_97_3 + (arg_97_0.level - var_97_2) * var_97_0.attrs_growth_extra[var_97_1] / 1000

		return var_97_3

	def isMaxStar(arg_98_0):
		return arg_98_0.getStar() >= arg_98_0.getMaxStar()

	def IsMaxStarByTmpID(arg_99_0):
		var_99_0 = pg.ship_data_template[arg_99_0]

		return var_99_0.star >= var_99_0.star_max

	def IsSpweaponUnlock(arg_100_0):
		if not arg_100_0.CanAccumulateExp():
			return False, "spweapon_tip_locked"
		else:
			return True

	def getModProperties(arg_101_0, arg_101_1):
		return arg_101_0.strengthList[arg_101_1] or 0

	def addModAttrExp(arg_102_0, arg_102_1, arg_102_2):
		var_102_0 = arg_102_0.getModAttrTopLimit(arg_102_1)

		if var_102_0 == 0:
			return

		var_102_1 = arg_102_0.getModExpRatio(arg_102_1)
		var_102_2 = arg_102_0.getModProperties(arg_102_1)

		if var_102_2 + arg_102_2 > var_102_0 * var_102_1:
			arg_102_0.strengthList[arg_102_1] = var_102_0 * var_102_1
		else:
			arg_102_0.strengthList[arg_102_1] = var_102_2 + arg_102_2

	def getNeedModExp(arg_103_0):
		var_103_0 = table()

		for iter_103_0, iter_103_1 in pairs(ShipModAttr.ID_TO_ATTR):
			var_103_1 = arg_103_0.getModAttrTopLimit(iter_103_1)

			if var_103_1 == 0:
				var_103_0[iter_103_1] = 0
			else:
				var_103_0[iter_103_1] = var_103_1 * arg_103_0.getModExpRatio(iter_103_1) - arg_103_0.getModProperties(iter_103_1)

		return var_103_0

	def attrVertify(arg_104_0):
		if not BayProxy.checkShiplevelVertify(arg_104_0):
			return False

		for iter_104_0, iter_104_1 in ipairs(arg_104_0.equipments):
			if iter_104_1 and not iter_104_1.vertify():
				return False

		return True

	def getEquipmentProperties(arg_105_0):
		var_105_0 = table()
		var_105_1 = table()

		for iter_105_0, iter_105_1 in ipairs(Ship.PROPERTIES):
			var_105_0[iter_105_1] = 0

		for iter_105_2, iter_105_3 in ipairs(Ship.DIVE_PROPERTIES):
			var_105_0[iter_105_3] = 0

		for iter_105_4, iter_105_5 in ipairs(Ship.SONAR_PROPERTIES):
			var_105_0[iter_105_5] = 0

		for iter_105_6, iter_105_7 in ipairs(Ship.PROPERTIES_ENHANCEMENT):
			var_105_1[iter_105_7] = 0

		var_105_0[AttributeType.AirDominate] = 0
		var_105_0[AttributeType.AntiSiren] = 0

		var_105_2 = arg_105_0.getActiveEquipments()

		for iter_105_8, iter_105_9 in ipairs(var_105_2):
			if iter_105_9:
				var_105_3 = iter_105_9.GetAttributes()

				for iter_105_10, iter_105_11 in ipairs(var_105_3):
					if iter_105_11 and var_105_0[iter_105_11.type]:
						var_105_0[iter_105_11.type] = var_105_0[iter_105_11.type] + iter_105_11.value

				var_105_4 = iter_105_9.GetPropertyRate()

				for iter_105_12, iter_105_13 in pairs(var_105_4):
					var_105_1[iter_105_12] = math.max(var_105_1[iter_105_12], iter_105_13)

				var_105_5 = iter_105_9.GetSonarProperty()

				if var_105_5:
					for iter_105_14, iter_105_15 in pairs(var_105_5):
						var_105_0[iter_105_14] = var_105_0[iter_105_14] + iter_105_15

				var_105_6 = iter_105_9.GetAntiSirenPower()

				if var_105_6:
					var_105_0[AttributeType.AntiSiren] = var_105_0[AttributeType.AntiSiren] + var_105_6 / 10000

		def _():
			var_106_0 = arg_105_0.GetSpWeapon()

			if not var_106_0:
				return

			var_106_1 = var_106_0.GetPropertiesInfo().attrs

			for iter_106_0, iter_106_1 in ipairs(var_106_1):
				if iter_106_1 and var_105_0[iter_106_1.type]:
					var_105_0[iter_106_1.type] = var_105_0[iter_106_1.type] + iter_106_1.value
		_()

		for iter_105_16, iter_105_17 in pairs(var_105_1):
			var_105_1[iter_105_16] = iter_105_17 + 1

		return var_105_0, var_105_1

	def getSkillEffects(arg_107_0):
		var_107_0 = arg_107_0.getShipSkillEffects()

		underscore.each(arg_107_0.getEquipmentSkillEffects(), lambda arg_108_0: table.insert(var_107_0, arg_108_0))

		return var_107_0

	def getShipSkillEffects(arg_109_0):
		var_109_0 = table()
		var_109_1 = arg_109_0.getSkillList()

		for iter_109_0, iter_109_1 in ipairs(var_109_1):
			var_109_2 = arg_109_0.RemapSkillId(iter_109_1)
			var_109_3 = pg.loader.load_buff(var_109_2)

			arg_109_0.FilterActiveSkill(var_109_0, var_109_3, arg_109_0.skills[iter_109_1])

		return var_109_0

	def getEquipmentSkillEffects(arg_110_0):
		var_110_0 = table()
		var_110_1 = arg_110_0.getActiveEquipments()

		for iter_110_0, iter_110_1 in ipairs(var_110_1):
			var_110_2
			var_110_3 = iter_110_1 and iter_110_1.getConfig("skill_id")[1]

			if var_110_3:
				var_110_2 = pg.loader.load_buff(var_110_3)

			arg_110_0.FilterActiveSkill(var_110_0, var_110_2)

		var_111_0 = arg_110_0.GetSpWeapon()
		var_111_1 = var_111_0 and var_111_0.GetEffect() or 0
		var_111_2

		if var_111_1 > 0:
			var_111_2 = pg.loader.load_buff(var_111_1)

		arg_110_0.FilterActiveSkill(var_110_0, var_111_2)

		return var_110_0

	def FilterActiveSkill(arg_112_0, arg_112_1, arg_112_2, arg_112_3):
		if not arg_112_2 or not arg_112_2.const_effect_list:
			return

		for iter_112_0 in range(1, len(arg_112_2.const_effect_list)):
			var_112_0 = arg_112_2.const_effect_list[iter_112_0]
			var_112_1 = var_112_0.trigger
			var_112_2 = var_112_0.arg_list
			var_112_3 = 1

			if arg_112_3:
				var_112_3 = arg_112_3.level

				var_112_4 = arg_112_2[var_112_3].const_effect_list

				if var_112_4 and var_112_4[iter_112_0]:
					var_112_1 = var_112_4[iter_112_0].trigger or var_112_1
					var_112_2 = var_112_4[iter_112_0].arg_list or var_112_2

			var_112_5 = True

			for iter_112_1, iter_112_2 in pairs(var_112_1):
				if arg_112_0.triggers[iter_112_1] != iter_112_2:
					var_112_5 = False

					break

			if var_112_5:
				table.insert(arg_112_1, table(
					type = var_112_0.type,
					arg_list = var_112_2,
					level = var_112_3
				))

	def getEquipmentGearScore(arg_113_0):
		var_113_0 = 0
		var_113_1 = arg_113_0.getActiveEquipments()

		for iter_113_0, iter_113_1 in ipairs(var_113_1):
			if iter_113_1:
				var_113_0 = var_113_0 + iter_113_1.GetGearScore()

		return var_113_0

	def getProperties(arg_114_0, arg_114_1, arg_114_2, arg_114_3, arg_114_4):
		var_114_0 = arg_114_1 or table()
		var_114_1 = arg_114_0.getConfig("nationality")
		var_114_2 = arg_114_0.getConfig("type")
		var_114_3 = arg_114_0.getShipProperties()
		var_114_4, var_114_5 = arg_114_0.getEquipmentProperties()
		var_114_6
		var_114_7
		var_114_8

		if arg_114_3 and arg_114_0.getFlag("inWorld"):
			var_114_9 = WorldConst.FetchWorldShip(arg_114_0.id)

			var_114_6, var_114_7 = var_114_9.GetShipBuffProperties()
			var_114_8 = var_114_9.GetShipPowerBuffProperties()

		for iter_114_0, iter_114_1 in ipairs(Ship.PROPERTIES):
			var_114_10 = 0
			var_114_11 = 0

			for iter_114_2, iter_114_3 in pairs(var_114_0):
				var_114_10 = var_114_10 + iter_114_3.getAttrRatioAddition(iter_114_1, var_114_1, var_114_2) / 100
				var_114_11 = var_114_11 + iter_114_3.getAttrValueAddition(iter_114_1, var_114_1, var_114_2)

			var_114_12 = var_114_10 + (var_114_5[iter_114_1] or 1)
			var_114_13 = var_114_7 and var_114_7[iter_114_1] or 1
			var_114_14 = var_114_6 and var_114_6[iter_114_1] or 0

			if iter_114_1 == AttributeType.Speed:
				var_114_3[iter_114_1] = var_114_3[iter_114_1] * var_114_12 * var_114_13 + var_114_11 + var_114_4[iter_114_1] + var_114_14
			else:
				var_114_3[iter_114_1] = calcFloor(calcFloor(var_114_3[iter_114_1]) * var_114_12 * var_114_13) + var_114_11 + var_114_4[iter_114_1] + var_114_14

		if not arg_114_2 and arg_114_0.isMaxStar():
			for iter_114_4, iter_114_5 in pairs(var_114_3):
				var_114_15 = arg_114_4 and arg_114_0.getTechNationMaxAddition(iter_114_4) or arg_114_0.getTechNationAddition(iter_114_4)

				var_114_3[iter_114_4] = var_114_3[iter_114_4] + var_114_15

		for iter_114_6, iter_114_7 in ipairs(Ship.DIVE_PROPERTIES):
			var_114_3[iter_114_7] = var_114_3[iter_114_7] + var_114_4[iter_114_7]

		for iter_114_8, iter_114_9 in ipairs(Ship.SONAR_PROPERTIES):
			var_114_3[iter_114_9] = var_114_3[iter_114_9] + var_114_4[iter_114_9]

		if arg_114_3:
			var_114_3[AttributeType.AntiSiren] = (var_114_3[AttributeType.AntiSiren] or 0) + var_114_4[AttributeType.AntiSiren]

		if var_114_8:
			for iter_114_10, iter_114_11 in pairs(var_114_8):
				if var_114_3[iter_114_10]:
					if iter_114_10 == AttributeType.Speed:
						var_114_3[iter_114_10] = var_114_3[iter_114_10] * iter_114_11
					else:
						var_114_3[iter_114_10] = math.floor(var_114_3[iter_114_10] * iter_114_11)

		return var_114_3

	def getTransGearScore(arg_115_0):
		var_115_0 = 0
		var_115_1 = pg.transform_data_template

		for iter_115_0, iter_115_1 in pairs(arg_115_0.transforms):
			for iter_115_2 in range(1, iter_115_1.level):
				var_115_0 = var_115_0 + (var_115_1[iter_115_1.id].gear_score[iter_115_2] or 0)

		return var_115_0

	def getShipCombatPower(arg_116_0, arg_116_1):
		var_116_0 = arg_116_0.getProperties(arg_116_1, None, None, True)
		var_116_1 = var_116_0[AttributeType.Durability] / 5 + var_116_0[AttributeType.Cannon] + var_116_0[AttributeType.Torpedo] + var_116_0[AttributeType.AntiAircraft] + var_116_0[AttributeType.Air] + var_116_0[AttributeType.AntiSub] + var_116_0[AttributeType.Reload] + var_116_0[AttributeType.Hit] * 2 + var_116_0[AttributeType.Dodge] * 2 + var_116_0[AttributeType.Speed] + arg_116_0.getEquipmentGearScore() + arg_116_0.getTransGearScore()

		return math.floor(var_116_1)

	def cosumeEnergy(arg_117_0, arg_117_1):
		arg_117_0.setEnergy(math.max(arg_117_0.getEnergy() - arg_117_1, 0))

	def addEnergy(arg_118_0, arg_118_1):
		arg_118_0.setEnergy(arg_118_0.getEnergy() + arg_118_1)

	def setEnergy(arg_119_0, arg_119_1):
		arg_119_0.energy = arg_119_1

	def setLikability(arg_120_0, arg_120_1):
		assert arg_120_1 >= 0 and arg_120_1 <= arg_120_0.maxIntimacy, f"intimacy value invaild{arg_120_1}"
		arg_120_0.setIntimacy(arg_120_1)

	def addLikability(arg_121_0, arg_121_1):
		var_121_0 = Mathf.Clamp(arg_121_0.getIntimacy() + arg_121_1, 0, arg_121_0.maxIntimacy)

		arg_121_0.setIntimacy(var_121_0)

	def setIntimacy(arg_122_0, arg_122_1):
		if arg_122_1 > 10000 and not arg_122_0.propose:
			arg_122_1 = 10000

		arg_122_0.intimacy = arg_122_1

		if not arg_122_0.isActivityNpc():
			getProxy(CollectionProxy).shipGroups[arg_122_0.groupId].updateMaxIntimacy(arg_122_0.getIntimacy())

	def getLevelExpConfig(arg_123_0, arg_123_1):
		if arg_123_0.getConfig("rarity") == ShipRarity.SSR:
			var_123_0 = Clone(getConfigFromLevel1(var_0_6, arg_123_1 or arg_123_0.level))

			var_123_0.exp = var_123_0.exp_ur
			var_123_0.exp_start = var_123_0.exp_ur_start
			var_123_0.exp_interval = var_123_0.exp_ur_interval
			var_123_0.exp_end = var_123_0.exp_ur_end

			return var_123_0
		else:
			return getConfigFromLevel1(var_0_6, arg_123_1 or arg_123_0.level)

	def getExp(arg_124_0):
		var_124_0 = arg_124_0.getMaxLevel()

		if arg_124_0.level == var_124_0 and LOCK_FULL_EXP:
			return 0

		return arg_124_0.exp

	def getProficiency(arg_125_0):
		return arg_125_0.proficiency

	def addExp(arg_126_0, arg_126_1, arg_126_2):
		var_126_0 = arg_126_0.getMaxLevel()

		if arg_126_0.level == var_126_0:
			if arg_126_0.exp >= pg.gameset.exp_overflow_max.key_value:
				return

			if LOCK_FULL_EXP or not arg_126_2 or not arg_126_0.CanAccumulateExp():
				arg_126_1 = 0

		arg_126_0.exp = arg_126_0.exp + arg_126_1

		var_126_1 = False

		while arg_126_0.canLevelUp():
			arg_126_0.exp = arg_126_0.exp - arg_126_0.getLevelExpConfig().exp_interval
			arg_126_0.level = math.min(arg_126_0.level + 1, var_126_0)
			var_126_1 = True

		if arg_126_0.level == var_126_0:
			if arg_126_2 and arg_126_0.CanAccumulateExp():
				arg_126_0.exp = math.min(arg_126_0.exp, pg.gameset.exp_overflow_max.key_value)
			elif var_126_1:
				arg_126_0.exp = 0

	def getMaxLevel(arg_127_0):
		return arg_127_0.maxLevel

	def canLevelUp(arg_128_0):
		var_128_0 = arg_128_0.getLevelExpConfig(arg_128_0.level + 1)
		var_128_1 = arg_128_0.getMaxLevel() <= arg_128_0.level

		return var_128_0 and arg_128_0.getLevelExpConfig().exp_interval <= arg_128_0.exp and not var_128_1

	def getConfigMaxLevel(arg_129_0):
		return var_0_6.all[-1]

	def isConfigMaxLevel(arg_130_0):
		return arg_130_0.level == arg_130_0.getConfigMaxLevel()

	def updateMaxLevel(arg_131_0, arg_131_1):
		var_131_0 = arg_131_0.getConfigMaxLevel()

		arg_131_0.maxLevel = math.max(math.min(var_131_0, arg_131_1), arg_131_0.maxLevel)

	def getNextMaxLevel(arg_132_0):
		var_132_0 = arg_132_0.getConfigMaxLevel()

		for iter_132_0 in range(arg_132_0.getMaxLevel() + 1, var_132_0):
			if var_0_6[iter_132_0].level_limit == 1:
				return iter_132_0

	def canUpgrade(arg_133_0):
		if arg_133_0.isMetaShip() or arg_133_0.isBluePrintShip():
			return False
		else:
			var_133_0 = var_0_8[arg_133_0.configId]

			assert var_133_0, f"不存在配置{arg_133_0.configId}"

			return not arg_133_0.isMaxStar() and arg_133_0.level >= var_133_0.level

	def isReachNextMaxLevel(arg_134_0):
		return arg_134_0.level == arg_134_0.getMaxLevel() and arg_134_0.C
	def notMaxLevelForFilter(arg_137_0):
		return arg_137_0.level != arg_137_0.getMaxLevel()

	def getNextMaxLevelConsume(arg_138_0):
		var_138_0 = arg_138_0.getMaxLevel()
		var_138_1 = var_0_6[var_138_0][f"need_item_rarity{arg_138_0.getConfig}"("rarity")]

		assert var_138_1, "items  can not be None"

		return underscore.map(var_138_1, lambda arg_139_0: table(
				type = arg_139_0[1],
				id = arg_139_0[2],
				count = arg_139_0[3]
			))

	def canUpgradeMaxLevel(arg_140_0):
		if not arg_140_0.isReachNextMaxLevel():
			return False, i18n("upgrade_to_next_maxlevel_failed")
		else:
			var_140_0 = getProxy(PlayerProxy).getData()
			var_140_1 = getProxy(BagProxy)
			var_140_2 = arg_140_0.getNextMaxLevelConsume()

			for iter_140_0, iter_140_1 in pairs(var_140_2):
				if iter_140_1.type == DROP_TYPE_RESOURCE:
					if var_140_0.getResById(iter_140_1.id) < iter_140_1.count:
						return False, i18n("common_no_resource")
				elif iter_140_1.type == DROP_TYPE_ITEM and var_140_1.getItemCountById(iter_140_1.id) < iter_140_1.count:
					return False, i18n("common_no_item_1")

		return True

	def CanAccumulateExp(arg_141_0):
		return pg.ship_data_template[arg_141_0.configId].can_get_proficency == 1

	def getTotalExp(arg_142_0):
		return arg_142_0.getLevelExpConfig().exp_start + arg_142_0.exp

	def getStartBattleExpend(arg_143_0):
		if table.contains(TeamType.SubShipType, arg_143_0.getShipType()):
			return 0
		else:
			return pg.ship_data_template[arg_143_0.configId].oil_at_start

	def getEndBattleExpend(arg_144_0):
		var_144_0 = pg.ship_data_template[arg_144_0.configId]
		var_144_1 = arg_144_0.getLevelExpConfig()

		return (math.floor(var_144_0.oil_at_end * var_144_1.fight_oil_ratio / 10000))

	def getBattleTotalExpend(arg_145_0):
		return arg_145_0.getStartBattleExpend() + arg_145_0.getEndBattleExpend()

	def getShipAmmo(arg_146_0):
		var_146_0 = arg_146_0.getConfig(AttributeType.Ammo)

		for iter_146_0, iter_146_1 in pairs(arg_146_0.getAllSkills()):
			var_146_1 = tonumber(f"{iter_146_0}{iter_146_1.level:02d}")
			var_146_2 = pg.skill_benefit_template[var_146_1]

			if var_146_2 and arg_146_0.IsBenefitSkillActive(var_146_2) and (var_146_2.type == Ship.BENEFIT_EQUIP or var_146_2.type == Ship.BENEFIT_SKILL):
				var_146_0 = var_146_0 + defaultValue(var_146_2.effect[1], 0)

		var_146_3 = arg_146_0.getActiveEquipments()

		for iter_146_2, iter_146_3 in ipairs(var_146_3):
			var_146_4 = iter_146_3 and iter_146_3.getConfig("equip_parameters").ammo

			if var_146_4:
				var_146_0 = var_146_0 + var_146_4

		return var_146_0

	def getHuntingLv(arg_147_0):
		var_147_0 = arg_147_0.getConfig("huntingrange_level")

		for iter_147_0, iter_147_1 in pairs(arg_147_0.getAllSkills()):
			var_147_1 = tonumber(f"{iter_147_0}{iter_147_1.level:02d}")
			var_147_2 = pg.skill_benefit_template[var_147_1]

			if var_147_2 and arg_147_0.IsBenefitSkillActive(var_147_2) and (var_147_2.type == Ship.BENEFIT_EQUIP or var_147_2.type == Ship.BENEFIT_SKILL):
				var_147_0 = var_147_0 + defaultValue(var_147_2.effect[2], 0)

		var_147_3 = arg_147_0.getActiveEquipments()

		for iter_147_2, iter_147_3 in ipairs(var_147_3):
			var_147_4 = iter_147_3 and iter_147_3.getConfig("equip_parameters").hunting_lv

			if var_147_4:
				var_147_0 = var_147_0 + var_147_4

		return (math.min(var_147_0, arg_147_0.getMaxHuntingLv()))

	def getMapAuras(arg_148_0):
		var_148_0 = table()

		for iter_148_0, iter_148_1 in pairs(arg_148_0.getAllSkills()):
			var_148_1 = tonumber(f"{iter_148_0}{iter_148_1.level:02d}")
			var_148_2 = pg.skill_benefit_template[var_148_1]

			if var_148_2 and arg_148_0.IsBenefitSkillActive(var_148_2) and var_148_2.type == Ship.BENEFIT_MAP_AURA:
				var_148_3 = table(
					id = var_148_2.effect[1],
					level = iter_148_1.level
				)

				table.insert(var_148_0, var_148_3)

		return var_148_0

	def getMapAids(arg_149_0):
		var_149_0 = table()

		for iter_149_0, iter_149_1 in pairs(arg_149_0.getAllSkills()):
			var_149_1 = tonumber(f"{iter_149_0}{iter_149_1.level:02d}")
			var_149_2 = pg.skill_benefit_template[var_149_1]

			if var_149_2 and arg_149_0.IsBenefitSkillActive(var_149_2) and var_149_2.type == Ship.BENEFIT_AID:
				var_149_3 = table(
					id = var_149_2.effect[1],
					level = iter_149_1.level
				)

				table.insert(var_149_0, var_149_3)

		return var_149_0

	BENEFIT_SKILL = 2
	BENEFIT_EQUIP = 3
	BENEFIT_MAP_AURA = 4
	BENEFIT_AID = 5

	def IsBenefitSkillActive(arg_150_0, arg_150_1):
		var_150_0 = False

		if arg_150_1.type == Ship.BENEFIT_SKILL:
			if not arg_150_1.limit[1] or arg_150_1.limit[1] == arg_150_0.triggers.TeamNumbers:
				var_150_0 = True
		elif arg_150_1.type == Ship.BENEFIT_EQUIP:
			var_150_1 = arg_150_1.limit
			var_150_2 = arg_150_0.getAllEquipments()

			for iter_150_0, iter_150_1 in ipairs(var_150_2):
				if iter_150_1 and table.contains(var_150_1, iter_150_1.getConfig("id")):
					var_150_0 = True

					break
		elif arg_150_1.type == Ship.BENEFIT_MAP_AURA:
			if arg_150_0.hpRant and arg_150_0.hpRant > 0:
				return True
		elif arg_150_1.type == Ship.BENEFIT_AID and arg_150_0.hpRant and arg_150_0.hpRant > 0:
			return True

		return var_150_0

	def getMaxHuntingLv(arg_151_0):
		return #arg_151_0.getConfig("hunting_range")

	def getHuntingRange(arg_152_0, arg_152_1):
		var_152_0 = arg_152_0.getConfig("hunting_range")
		var_152_1 = Clone(var_152_0[1])
		var_152_2 = arg_152_1 or arg_152_0.getHuntingLv()
		var_152_3 = math.min(var_152_2, arg_152_0.getMaxHuntingLv())

		for iter_152_0 in range(1, var_152_3):
			underscore.each(var_152_0[iter_152_0], lambda arg_153_0: table.insert(var_152_1, table(
					arg_153_0[1],
					arg_153_0[2]
				)))

		return var_152_1

	def getTriggerSkills(arg_154_0):
		var_154_0 = table()
		var_154_1 = arg_154_0.getSkillEffects()

		def _function(arg_155_0):
			if arg_155_0.type == "AddBuff" and arg_155_0.arg_list and arg_155_0.arg_list.buff_id:
				var_155_0 = arg_155_0.arg_list.buff_id

				var_154_0[var_155_0] = table(
					id = var_155_0,
					level = arg_155_0.level
				)

		underscore.each(var_154_1, _function)

		return var_154_0

	def GetEquipmentSkills(arg_156_0):
		var_156_0 = table()
		var_156_1 = arg_156_0.getActiveEquipments()

		for iter_156_0, iter_156_1 in ipairs(var_156_1):
			if iter_156_1:
				var_156_2 = iter_156_1.getConfig("skill_id")[1]

				if var_156_2:
					var_156_0[var_156_2] = table(
						level = 1,
						id = var_156_2
					)

		var_157_0 = arg_156_0.GetSpWeapon()
		var_157_1 = var_157_0 and var_157_0.GetEffect() or 0

		if var_157_1 > 0:
			var_156_0[var_157_1] = table(
				level = 1,
				id = var_157_1
			)

		return var_156_0

	def getAllSkills(arg_158_0):
		var_158_0 = Clone(arg_158_0.skills)

		for iter_158_0, iter_158_1 in pairs(arg_158_0.GetEquipmentSkills()):
			var_158_0[iter_158_0] = iter_158_1

		for iter_158_2, iter_158_3 in pairs(arg_158_0.getTriggerSkills()):
			var_158_0[iter_158_2] = iter_158_3

		return var_158_0

	def isSameKind(arg_159_0, arg_159_1):
		return pg.ship_data_template[arg_159_0.configId].group_type == pg.ship_data_template[arg_159_1.configId].group_type

	def GetLockState(arg_160_0):
		return arg_160_0.lockState

	def IsLocked(arg_161_0):
		return arg_161_0.lockState == Ship.LOCK_STATE_LOCK

	def SetLockState(arg_162_0, arg_162_1):
		arg_162_0.lockState = arg_162_1

	def GetPreferenceTag(arg_163_0):
		return arg_163_0.preferenceTag or 0

	def IsPreferenceTag(arg_164_0):
		return arg_164_0.GetPreferenceTag() == Ship.PREFERENCE_TAG_COMMON

	def SetPreferenceTag(arg_165_0, arg_165_1):
		arg_165_0.preferenceTag = arg_165_1

	def calReturnRes(arg_166_0):
		var_166_0 = pg.ship_data_by_type[arg_166_0.getShipType()]
		var_166_1 = var_166_0.distory_resource_gold_ratio
		var_166_2 = var_166_0.distory_resource_oil_ratio
		var_166_3 = pg.ship_data_by_star[arg_166_0.getConfig("rarity")].destory_item

		return var_166_1, 0, var_166_3

	def getRarity(arg_167_0):
		var_167_0 = arg_167_0.getConfig("rarity")

		if arg_167_0.isRemoulded():
			var_167_0 = var_167_0 + 1

		return var_167_0

	def getExchangePrice(arg_168_0):
		var_168_0 = arg_168_0.getConfig("rarity")

		return pg.ship_data_by_star[var_168_0].exchange_price

	def updateSkill(arg_169_0, arg_169_1):
		var_169_0 = arg_169_1.skill_id or arg_169_1.id
		var_169_1 = arg_169_1.skill_lv or arg_169_1.lv or arg_169_1.level
		var_169_2 = arg_169_1.skill_exp or arg_169_1.exp

		arg_169_0.skills[var_169_0] = table(
			id = var_169_0,
			level = var_169_1,
			exp = var_169_2
		)

	def canEquipAtPos(arg_170_0, arg_170_1, arg_170_2):
		var_170_0, var_170_1 = arg_170_0.isForbiddenAtPos(arg_170_1, arg_170_2)

		if var_170_0:
			return False, var_170_1

		for iter_170_0, iter_170_1 in ipairs(arg_170_0.equipments):
			if iter_170_1 and iter_170_0 != arg_170_2 and iter_170_1.getConfig("equip_limit") != 0 and arg_170_1.getConfig("equip_limit") == iter_170_1.getConfig("equip_limit"):
				return False, i18n("ship_equip_same_group_equipment")

		return True

	def isForbiddenAtPos(arg_171_0, arg_171_1, arg_171_2):
		var_171_0 = pg.ship_data_template[arg_171_0.configId]

		assert var_171_0, f"can not find ship in ship_data_templtae. {arg_171_0.configId}"

		var_171_1 = var_171_0[f"equip_{arg_171_2}"]

		if not table.contains(var_171_1, arg_171_1.getConfig("type")):
			return True, i18n("common_limit_equip")

		if table.contains(arg_171_1.getConfig("ship_type_forbidden"), arg_171_0.getShipType()):
			return True, i18n("common_limit_equip")

		return False

	def canEquipCommander(arg_172_0, arg_172_1):
		if arg_172_1.getShipType() != arg_172_0.getShipType():
			return False, i18n("commander_type_unmatch")

		return True

	def upgrade(arg_173_0):
		var_173_0 = pg.ship_data_transform[arg_173_0.configId]

		if var_173_0.trans_id and var_173_0.trans_id > 0:
			arg_173_0.configId = var_173_0.trans_id
			arg_173_0.star = arg_173_0.getConfig("star")

	def getTeamType(arg_174_0):
		return TeamType.GetTeamFromShipType(arg_174_0.getShipType())

	def getFleetName(arg_175_0):
		var_175_0 = arg_175_0.getTeamType()

		return Ship.var_0_1[var_175_0]

	def getMaxConfigId(arg_176_0):
		var_176_0 = pg.ship_data_template
		var_176_1

		for iter_176_0 in range(4, 1, -1):
			var_176_2 = tonumber(f"{arg_176_0.groupId}{iter_176_0}")

			if var_176_0[var_176_2]:
				var_176_1 = var_176_2

				break

		return var_176_1

	def getFlag(arg_177_0, arg_177_1, arg_177_2):
		return pg.ShipFlagMgr.GetInstance().GetShipFlag(arg_177_0.id, arg_177_1, arg_177_2)

	def hasAnyFlag(arg_178_0, arg_178_1):
		return underscore.any(arg_178_1, lambda arg_179_0: arg_178_0.getFlag(arg_179_0))

	def isBreakOut(arg_180_0):
		return arg_180_0.configId % 10 > 1

	def fateSkillChange(arg_181_0, arg_181_1):
		if not arg_181_0.skillChangeList:
			arg_181_0.skillChangeList = arg_181_0.isBluePrintShip() and arg_181_0.getBluePrint().getChangeSkillList() or table()

		for iter_181_0, iter_181_1 in ipairs(arg_181_0.skillChangeList):
			if iter_181_1[1] == arg_181_1 and arg_181_0.skills[iter_181_1[2]]:
				return iter_181_1[2]

		return arg_181_1

	def RemapSkillId(arg_182_0, arg_182_1):
		var_182_0 = arg_182_0.GetSpWeapon()

		if var_182_0:
			return var_182_0.RemapSkillId(arg_182_1)

		return arg_182_1

	def getSkillList(arg_183_0):
		var_183_0 = pg.ship_data_template[arg_183_0.configId]
		var_183_1 = Clone(var_183_0.buff_list_display)
		var_183_2 = Clone(var_183_0.buff_list)
		var_183_3 = pg.ship_data_trans[arg_183_0.groupId]
		var_183_4 = 0

		if var_183_3 and var_183_3.skill_id != 0:
			var_183_5 = var_183_3.skill_id
			var_183_6 = pg.transform_data_template[var_183_5]

			if arg_183_0.transforms[var_183_5] and var_183_6.skill_id != 0:
				table.insert(var_183_2, var_183_6.skill_id)

		var_183_7 = table()

		for iter_183_0, iter_183_1 in ipairs(var_183_1):
			for iter_183_2, iter_183_3 in ipairs(var_183_2):
				if iter_183_1 == iter_183_3:
					table.insert(var_183_7, arg_183_0.fateSkillChange(iter_183_1))

		return var_183_7

	def getModAttrTopLimit(arg_184_0, arg_184_1):
		var_184_0 = ShipModAttr.ATTR_TO_INDEX[arg_184_1]
		var_184_1 = pg.ship_data_template[arg_184_0.configId].strengthen_id
		var_184_2 = pg.ship_data_strengthen[var_184_1].durability[var_184_0]

		return calcFloor((3 + 7 * (math.min(arg_184_0.level, 100) / 100)) * var_184_2 * 0.1)

	def leftModAdditionPoint(arg_185_0, arg_185_1):
		var_185_0 = arg_185_0.getModProperties(arg_185_1)
		var_185_1 = arg_185_0.getModExpRatio(arg_185_1)
		var_185_2 = arg_185_0.getModAttrTopLimit(arg_185_1)
		var_185_3 = calcFloor(var_185_0 / var_185_1)

		return math.max(0, var_185_2 - var_185_3)

	def getModAttrBaseMax(arg_186_0, arg_186_1):
		if not table.contains(arg_186_0.getConfig("lock"), arg_186_1):
			var_186_0 = arg_186_0.leftModAdditionPoint(arg_186_1)
			var_186_1 = arg_186_0.getShipProperties()

			return calcFloor(var_186_1[arg_186_1] + var_186_0)
		else:
			return 0

	def getModExpRatio(arg_187_0, arg_187_1):
		if not table.contains(arg_187_0.getConfig("lock"), arg_187_1):
			var_187_0 = pg.ship_data_template[arg_187_0.configId].strengthen_id

			assert pg.ship_data_strengthen[var_187_0], f"ship_data_strengthen>>>>>>{var_187_0}"

			return math.max(pg.ship_data_strengthen[var_187_0].level_exp[ShipModAttr.ATTR_TO_INDEX[arg_187_1]], 1)
		else:
			return 1

	def inUnlockTip(arg_188_0):
		var_188_0 = pg.gameset.tip_unlock_shipIds.description[0]

		return table.contains(var_188_0, arg_188_0)

	def proposeSkinOwned(arg_189_0, arg_189_1):
		return arg_189_1 and arg_189_0.propose and arg_189_1.skin_type == ShipSkin.SKIN_TYPE_PROPOSE

	def getProposeSkin(arg_190_0):
		return ShipSkin.GetSkinByType(arg_190_0.groupId, ShipSkin.SKIN_TYPE_PROPOSE)

	def getDisplaySkillIds(arg_191_0):
		return underscore.map(pg.ship_data_template[arg_191_0.configId].buff_list_display, lambda arg_192_0: arg_191_0.fateSkillChange(arg_192_0))

	def isFullSkillLevel(arg_193_0):
		var_193_0 = pg.skill_data_template

		for iter_193_0, iter_193_1 in pairs(arg_193_0.skills):
			if var_193_0[iter_193_1.id].max_level != iter_193_1.level:
				return False

		return True

	def setEquipmentRecord(arg_194_0, arg_194_1, arg_194_2):
		var_194_0 = f"equipment_record_{arg_194_1}_{arg_194_0.id}"

		PlayerPrefs.SetString(var_194_0, table.concat(underscore.flatten(arg_194_2), "."))
		PlayerPrefs.Save()

	def getEquipmentRecord(arg_195_0, arg_195_1):
		if not arg_195_0.equipmentRecords:
			var_195_0 = f"equipment_record_{arg_195_1}_{arg_195_0.id}"
			var_195_1 = PlayerPrefs.GetString(var_195_0) or "".split(".")
			var_195_2 = table()

			for iter_195_0 in range(1, 4):
				var_195_2[iter_195_0] = underscore.map(underscore.slice(var_195_1, 5 * iter_195_0 - 4, 5), lambda arg_196_0: tonumber(arg_196_0))

			arg_195_0.equipmentRecords = var_195_2

		return arg_195_0.equipmentRecords

	def SetSpWeaponRecord(arg_197_0, arg_197_1, arg_197_2):
		def _func(arg_198_0):
			var_198_0 = arg_197_2[arg_198_0]

			if var_198_0:
				return f"{(var_198_0.GetUID() or 0)},{var_198_0.GetConfigID}()"
			else:
				return "0,0"
		var_197_0 = f"spweapon_record_{arg_197_1}_{arg_197_0.id}"
		var_197_1 = underscore.map(table(
			1,
			2,
			3
		), _func)

		PlayerPrefs.SetString(var_197_0, table.concat(var_197_1, "."))
		PlayerPrefs.Save()

	def GetSpWeaponRecord(arg_199_0, arg_199_1):
		var_199_0 = f"spweapon_record_{arg_199_1}_{arg_199_0.id}"

		def _function(arg_200_0):
			var_200_0 = arg_200_0.split(",")

			assert var_200_0

			var_200_1 = tonumber(var_200_0[1])
			var_200_2 = tonumber(var_200_0[2])

			if not var_200_2 or var_200_2 == 0:
				return False

			var_200_3 = getProxy(EquipmentProxy).GetSpWeaponByUid(var_200_1) or underscore.detect(getProxy(BayProxy).GetSpWeaponsInShips(), lambda arg_201_0: arg_201_0.GetUID() == var_200_1)

			var_200_3 = var_200_3 or SpWeapon.New(table(
				id = var_200_2
			))

			return var_200_3

		return (underscore.map(PlayerPrefs.GetString(var_199_0, "").split("."), _function))

	def hasEquipEquipmentSkin(arg_202_0):
		for iter_202_0, iter_202_1 in ipairs(arg_202_0.equipments):
			if iter_202_1 and iter_202_1.hasSkin():
				return True

		return False

	def hasCommander(arg_203_0):
		return arg_203_0.commanderId and arg_203_0.commanderId != 0

	def getCommander(arg_204_0):
		return arg_204_0.commanderId

	def setCommander(arg_205_0, arg_205_1):
		arg_205_0.commanderId = arg_205_1

	def getSkillIndex(arg_206_0, arg_206_1):
		var_206_0 = arg_206_0.getSkillList()

		for iter_206_0, iter_206_1 in ipairs(var_206_0):
			if arg_206_1 == iter_206_1:
				return iter_206_0

	def getTactics(arg_207_0):
		return 1, "tactics_attack"

	def IsBgmSkin(arg_208_0):
		var_208_0 = arg_208_0.GetSkinConfig()

		return table.contains(var_208_0.tag, ShipSkin.WITH_BGM)

	def GetSkinBgm(arg_209_0):
		if arg_209_0.IsBgmSkin():
			return arg_209_0.GetSkinConfig().bgm

	def isIntensifyMax(arg_210_0):
		var_210_0 = intProperties(arg_210_0.getShipProperties())

		if arg_210_0.isBluePrintShip():
			return True

		for iter_210_0, iter_210_1 in pairs(ShipModAttr.ID_TO_ATTR):
			if arg_210_0.getModAttrBaseMax(iter_210_1) != var_210_0[iter_210_1]:
				return False

		return True

	def isRemouldable(arg_211_0):
		return not arg_211_0.isTestShip() and not arg_211_0.isBluePrintShip() and pg.ship_data_trans[arg_211_0.groupId]

	def isAllRemouldFinish(arg_212_0):
		var_212_0 = pg.ship_data_trans[arg_212_0.groupId]

		assert var_212_0, f"this ship group without remould config.{arg_212_0.groupId}"

		for iter_212_0, iter_212_1 in ipairs(var_212_0.transform_list):
			for iter_212_2, iter_212_3 in ipairs(iter_212_1):
				var_212_1 = pg.transform_data_template[iter_212_3[2]]

				if len(var_212_1.edit_trans) > 0:
					pass#-- block empty
				elif not arg_212_0.transforms[iter_212_3[2]] or arg_212_0.transforms[iter_212_3[2]].level < var_212_1.max_level:
					return False

		return True

	def isSpecialFilter(arg_213_0):
		var_213_0 = pg.ship_data_statistics[arg_213_0.configId]

		assert var_213_0, f"this ship without statistics.{arg_213_0.configId}"

		for iter_213_0, iter_213_1 in ipairs(var_213_0.tag_list):
			if iter_213_1 == "special":
				return True

		return False

	def hasAvailiableSkin(arg_214_0):
		var_214_0 = getProxy(ShipSkinProxy)
		var_214_1 = var_214_0.GetAllSkinForShip(arg_214_0)
		var_214_2 = var_214_0.getRawData()
		var_214_3 = 0

		for iter_214_0, iter_214_1 in ipairs(var_214_1):
			if arg_214_0.proposeSkinOwned(iter_214_1) or var_214_2[iter_214_1.id]:
				var_214_3 = var_214_3 + 1

		return var_214_3 > 0

	def hasProposeSkin(arg_215_0):
		var_215_0 = getProxy(ShipSkinProxy)
		var_215_1 = var_215_0.GetAllSkinForShip(arg_215_0)

		for iter_215_0, iter_215_1 in ipairs(var_215_1):
			if iter_215_1.skin_type == ShipSkin.SKIN_TYPE_PROPOSE:
				return True

		var_215_2 = var_215_0.GetShareSkinsForShip(arg_215_0)

		for iter_215_2, iter_215_3 in ipairs(var_215_2):
			if iter_215_3.skin_type == ShipSkin.SKIN_TYPE_PROPOSE:
				return True

		return False

	def HasUniqueSpWeapon(arg_216_0):
		return bool(pg.spweapon_data_statistics.get_id_list_by_unique[arg_216_0.getGroupId()])

	def getAircraftReloadCD(arg_217_0):
		var_217_0 = arg_217_0.getConfigTable().base_list
		var_217_1 = arg_217_0.getConfigTable().default_equip_list
		var_217_2 = 0
		var_217_3 = 0

		for iter_217_0 in range(1, 4):
			var_217_4 = arg_217_0.getEquip(iter_217_0)
			var_217_5 = var_217_4 and var_217_4.configId or var_217_1[iter_217_0]
			var_217_6 = Equipment.getConfigData(var_217_5).type

			if underscore.any(EquipType.AirEquipTypes, lambda arg_218_0: var_217_6 == arg_218_0):
				var_217_2 = var_217_2 + Equipment.GetEquipReloadStatic(var_217_5) * var_217_0[iter_217_0]
				var_217_3 = var_217_3 + var_217_0[iter_217_0]

		var_217_7 = BattleConfig.AIR_ASSIST_RELOAD_RATIO * bfConsts.PERCENT

		return table(
			name = i18n("equip_info_31"),
			type = AttributeType.CD,
			value = var_217_2 / var_217_3 * var_217_7
		)

	def IsTagShip(arg_219_0, arg_219_1):
		var_219_0 = arg_219_0.getConfig("tag_list")

		return table.contains(var_219_0, arg_219_1)

	def setReMetaSpecialItemVO(arg_220_0, arg_220_1):
		arg_220_0.reMetaSpecialItemVO = arg_220_1

	def getReMetaSpecialItemVO(arg_221_0, arg_221_1):
		return arg_221_0.reMetaSpecialItemVO

	def getProposeType(arg_222_0):
		if arg_222_0.isMetaShip():
			return "meta"
		elif arg_222_0.IsXIdol():
			return "imas"
		else:
			return "default"

	def IsXIdol(arg_223_0):
		return arg_223_0.getNation() == Nation.IDOL_LINK

	def getSpecificType(arg_224_0):
		return pg.ship_data_template[arg_224_0.configId].specific_type

	def GetSpWeapon(arg_225_0):
		return arg_225_0.spWeapon

	def UpdateSpWeapon(arg_226_0, arg_226_1):
		var_226_0 = (arg_226_1 and arg_226_1.GetUID() or 0) == (arg_226_0.spWeapon and arg_226_0.spWeapon.GetUID() or 0)

		arg_226_0.spWeapon = arg_226_1

		if arg_226_1:
			arg_226_1.SetShipId(arg_226_0.id)

		if var_226_0:
			pg.m02.sendNotification(EquipmentProxy.SPWEAPONS_UPDATED)

	def CanEquipSpWeapon(arg_227_0, arg_227_1):
		var_227_0, var_227_1 = arg_227_0.IsSpWeaponForbidden(arg_227_1)

		if var_227_0:
			return False, var_227_1

		return True

	def IsSpWeaponForbidden(arg_228_0, arg_228_1):
		var_228_0 = arg_228_1.GetWearableShipTypes()
		var_228_1 = arg_228_0.getShipType()

		if not table.contains(var_228_0, var_228_1):
			return True, i18n("spweapon_tip_group_error")

		var_228_2 = arg_228_1.GetUniqueGroup()
		var_228_3 = arg_228_0.getGroupId()

		if var_228_2 != 0 and var_228_2 != var_228_3:
			return True, i18n("spweapon_tip_group_error")

		return False

	def GetMapStrikeAnim(arg_229_0):
		var_229_1 = arg_229_0.getShipType()

		TT = TeamType.GetTeamFromShipType(var_229_1)
		if TT == TeamType.Main:
				if ShipType.IsTypeQuZhu(var_229_1):
					return "SubTorpedoUI"
				if ShipType.ContainInLimitBundle(ShipType.BundleAircraftCarrier, var_229_1):
					return "AirStrikeUI"
				if ShipType.ContainInLimitBundle(ShipType.BundleBattleShip, var_229_1):
					return "CannonUI"
				return "CannonUI",
		if TT == TeamType.Vanguard:
				if ShipType.IsTypeQuZhu(var_229_1):
					return "SubTorpedoUI",
		if TT == TeamType.Submarine:
				if arg_229_0.getNation() == Nation.MOT:
					return "CannonUI"
				return "SubTorpedoUI"

		return None

	def IsDefaultSkin(arg_233_0):
		return arg_233_0.skinId == 0 or arg_233_0.skinId == arg_233_0.getConfig("skin_id")

	def IsMatchKey(arg_234_0, arg_234_1):
		if not arg_234_1 or arg_234_1 == "":
			return True

		arg_234_1 = arg_234_1.replace("%.", "%%.").lower()

		return arg_234_0.GetDefaultName().lower().index(arg_234_1)

	def IsOwner(arg_235_0):
		return bool(arg_235_0.id)

	def GetUniqueId(arg_236_0):
		return arg_236_0.id

	def ShowPropose(arg_237_0):
		if not arg_237_0.propose:
			return False
		else:
			return not HXSet.isHxPropose() or arg_237_0.IsOwner() and arg_237_0.GetUniqueId() == getProxy(PlayerProxy).getRawData().GetProposeShipId()

	def GetColorName(arg_238_0, arg_238_1):
		arg_238_1 = arg_238_1 or arg_238_0.getName()

		if PlayerPrefs.GetInt("SHIP_NAME_COLOR", PLATFORM_CODE == PLATFORM_CH and 1 or 0) == 1 and arg_238_0.propose:
			return setColorStr(arg_238_1, "#FFAACEFF")
		else:
			return arg_238_1

	var_0_9 = table(
		effect = table(
			"duang_meta_jiehun",
			"duang_6_jiehun_tuzhi",
			"duang_6_jiehun",
			"duang_meta_%s",
			"duang_6"
		),
		frame = table(
			"prop4_1",
			"prop%s",
			"prop"
		)
	)

	def GetFrameAndEffect(arg_239_0, arg_239_1):
		arg_239_1 = bool(arg_239_1)

		var_239_0
		var_239_1

		if arg_239_0.propose:
			if arg_239_0.isMetaShip():
				var_239_1 = Ship.Ship.var_0_9.effect[0]
				var_239_0 = Ship.var_0_9.frame[0]
			elif arg_239_0.isBluePrintShip():
				var_239_1 = Ship.var_0_9.effect[1]
				var_239_0 = Ship.var_0_9.frame[1] % arg_239_0.rarity2bgPrint()
			else:
				var_239_1 = Ship.var_0_9.effect[2]
				var_239_0 = Ship.var_0_9.frame[2]

			if not arg_239_0.ShowPropose():
				var_239_0 = None
		elif arg_239_0.isMetaShip():
			var_239_1 = Ship.var_0_9.effect[4] % arg_239_0.rarity2bgPrint()
		elif arg_239_0.getRarity() == ShipRarity.SSR:
			var_239_1 = Ship.var_0_9.effect[4]

		if arg_239_1:
			var_239_1 = var_239_1 and f"{var_239_1}_1"

		return var_239_0, var_239_1

	def GetRecordPosKey(arg_240_0):
		return arg_240_0.skinId

