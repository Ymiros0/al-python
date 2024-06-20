from luatable import table

from Framework import i18n


Durability = "durability"
Cannon = "cannon"
Torpedo = "torpedo"
AntiAircraft = "antiaircraft"
AntiSub = "antisub"
Air = "air"
Reload = "reload"
ArmorType = "armor_type"
Armor = "armor"
Hit = "hit"
Speed = "speed"
Luck = "luck"
Dodge = "dodge"
Expend = "expend"
Intimacy = "intimacy"
AirDominate = "AirDominate"
Damage = "damage"
CD = "cd"
Healthy = "healthy"
Speciality = "speciality"
Range = "range"
Angle = "angle"
Scatter = "scatter"
Ammo = "ammo"
HuntingRange = "hunting_range"
AirDurability = "AirDurability"
AntiSiren = "anti_siren"
Corrected = "corrected"
OxyMax = "oxy_max"
OxyCost = "oxy_cost"
OxyRecovery = "oxy_recovery"
OxyRecoverySurface = "oxy_recovery_surface"
OxyRecoveryBench = "oxy_recovery_bench"
OxyAttackDuration = "attack_duration"
OxyRaidDistance = "raid_distance"
SonarRange = "sonarRange"
Tactics = "tactics"
WorldPower = "world_power"

def Type2Name(arg_1_0):
	return i18n("attribute_" + arg_1_0)

eliteConditionTip = table(
	cannon = "elite_condition_cannon",
	air = "elite_condition_air",
	dodge = "elite_condition_dodge",
	torpedo = "elite_condition_torpedo",
	durability = "elite_condition_durability",
	reload = "elite_condition_reload",
	fleet_totle_level = "elite_condition_fleet_totle_level",
	antiaircraft = "elite_condition_antiaircraft",
	antisub = "elite_condition_antisub",
	level = "elite_condition_level"
)

var_0_1 = {
	0: "common_compare_equal",
	1: "common_compare_larger",
	2: "common_compare_not_less_than",
	-1: "common_compare_smaller",
	-2: "common_compare_not_more_than"
}

def eliteConditionCompareTip(arg_2_0):
	return i18n(var_0_1[arg_2_0])

def EliteCondition2Name(arg_3_0, *args):
	return i18n(eliteConditionTip[arg_3_0], *args)

def EliteConditionCompare(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_0 == 0:
		return arg_4_1 == arg_4_2
	elif arg_4_0 == 1:
		return arg_4_2 < arg_4_1
	elif arg_4_0 == -1:
		return arg_4_1 < arg_4_2
	elif arg_4_0 == 2:
		return arg_4_2 <= arg_4_1
	elif arg_4_0 == -2:
		return arg_4_1 <= arg_4_2
	else:
		assert(False, "compare type error")

attrNameTable = table({
	Durability: "maxHP",
	Cannon: "cannonPower",
	Torpedo: "torpedoPower",
	AntiAircraft: "antiAirPower",
	AntiSub: "antiSubPower",
	Air: "airPower",
	Reload: "loadSpeed",
	Hit: "attackRating",
	Speed: "speed",
	Luck: "luck",
	Dodge: "dodgeRate",
	OxyMax: "oxyMax",
	OxyCost: "oxyCost",
	OxyRecovery: "oxyRecovery",
	OxyRecoveryBench: "oxyRecoveryBench",
	OxyRecoverySurface: "oxyRecoverySurface",
	OxyAttackDuration: "oxyAtkDuration",
	OxyRaidDistance: "raidDist"
})

def ConvertBattleAttrName(arg_5_0):
	if attrNameTable[arg_5_0]:
		return attrNameTable[arg_5_0]
	else:
		return arg_5_0

PrimalAttr = table(
	torpedoPower = True,
	loadSpeed = True,
	antiSubPower = True,
	antiAirPower = True,
	dodgeRate = True,
	airPower = True,
	attackRating = True,
	cannonPower = True,
	velocity = True
)

def IsPrimalBattleAttr(arg_6_0):
	return PrimalAttr[arg_6_0]
