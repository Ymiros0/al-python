from luatable import table
from Vector3 import Vector3
import math

from model.const import ShipType
from const import SYSTEM_WORLD


calcFPS = 30
viewFPS = 30
AIFPS = 10
calcInterval = 1 / calcFPS
viewInterval = 1 / viewFPS
AIInterval = 1 / AIFPS
FRIENDLY_CODE = 1
FOE_CODE = -1
SHIELD_CENTER_CONST = 3.14
SHIELD_CENTER_CONST_2 = 2.0933333333333333
SHIELD_CENTER_CONST_4 = 4.1866666666666665
SHIELD_ROTATE_CONST = 30 / math.pi * 18
K1 = 6
K2 = 100
K3 = 3.14
AIR_ASSIST_RELOAD_RATIO = 220
RANDOM_DAMAGE_MIN = 0
RANDOM_DAMAGE_MAX = 2
BASIC_TIME_SCALE = 1
SPINE_SCALE = 2
BULLET_UPPER_BOUND_VISION_OFFSET = 30
BULLET_LEFT_BOUND_SPLIT_OFFSET = 8
BULLET_LOWER_BOUND_SPLIT_OFFSET = 8
CAMERA_INIT_POS = Vector3(0, 62, -10)
CAMERA_SIZE = 20
CAMERA_BASE_HEIGH = 8
CAMERA_GOLDEN_RATE = 0.618
AntiAirConfig = table()
AntiAirConfig.const_n = 10
AntiAirConfig.const_K = 1000
AntiAirConfig.const_N = 5
AntiAirConfig.const_A = 20
AntiAirConfig.const_B = 40
AntiAirConfig.Restore_Interval = 1
AntiAirConfig.Precast_duration = 0.25
AntiAirConfig.RangeBulletID = 2001
AntiAirConfig.RangeBarrageID = 1
AntiAirConfig.RangeAntiAirBone = "rangeantiaircraft"
AirSupportUnitPos = Vector3(-105, 0, 58)
AnitAirRepeaterConfig = table()
AnitAirRepeaterConfig.const_A = 32
AnitAirRepeaterConfig.const_B = 12
AnitAirRepeaterConfig.const_C = 220
AnitAirRepeaterConfig.upper_range = 35
AnitAirRepeaterConfig.lower_range = 15
ChargeWeaponConfig = table()
ChargeWeaponConfig.a1 = 0
ChargeWeaponConfig.K1 = 0
ChargeWeaponConfig.K2 = 1000
ChargeWeaponConfig.FIX_CD = 7
ChargeWeaponConfig.MEGA_FIX_CD = 3
ChargeWeaponConfig.GCD = 1
ChargeWeaponConfig.Enhance = 1.2
ChargeWeaponConfig.SIGHT_A = 0.35
ChargeWeaponConfig.SIGHT_B = -40
ChargeWeaponConfig.SIGHT_C = 38
TorpedoCFG = table()
TorpedoCFG.T = 10
TorpedoCFG.N = 1000
TorpedoCFG.GCD = 0.5
AirAssistCFG = table()
AirAssistCFG.GCD = 0.5
HammerCFG = table()
HammerCFG.PreventUpperBound = 0.8
BulletHeight = 1
HeightOffsetRate = 1.5
CharacterFeetHight = -0.5
BombDetonateHeight = 1.2
CameraSizeChangeSpeed = 0.04
AircraftHeight = 10
AirFighterOffsetZ = 3
AirFighterHeight = 10
CommonBone = table(
	rangeantiaircraft = table(
		table(
			1.5,
			1.1,
			0
		)
	)
)
MaxLeft = -10000
MaxRight = 10000
BornOffset = Vector3(0, 0, 0.1)
FORMATION_ID = 10001
CelebrateDuration = 3
EscapeDuration = 5
BulletMotionRate = 0.4
BulletSpeedConvertConst = 0.1
ShipSpeedConvertConst = 0.01
AircraftSpeedConvertConst = 0.01
PLAYER_WEAPON_GLOBAL_COOL_DOWN_DURATION = 0.5
PLAYER_DEFAULT = 0
SPECTRE_UNIT_TYPE = -99
VISIBLE_SPECTRE_UNIT_TYPE = -100
FUSION_ELEMENT_UNIT_TYPE = -10000
COUNT_DOWN_ESCAPE_AI_ID = 80006
ESCAPE_EXPLO_TAG = table(
	"unexit"
)
RESOURCE_STEP = 10
RESOURCE_STAY_DURATION = 2
CAST_CAM_ZOOM_SIZE = 14
CAST_CAM_ZOOM_IN_DURATION = 0.1
CAST_CAM_ZOOM_IN_DURATION_SKILL = 0.04
CAST_CAM_ZOOM_OUT_DURATION_CANNON = 0.1
CAST_CAM_ZOOM_OUT_EXTRA_DELAY_CANNON = 0.04
CAST_CAM_ZOOM_OUT_DELAY_CANNON = 0
CAST_CAM_ZOOM_OUT_DURATION_AIR = 0.1
CAST_CAM_ZOOM_OUT_EXTRA_DELAY_AIR = 0.03
CAST_CAM_ZOOM_OUT_DELAY_AIR = 0.05
AIR_ASSIST_SPEED_RATE = 2.8
CAST_CAM_ZOOM_OUT_DURATION_SKILL = 0.04
CAST_CAM_ZOOM_OUT_EXTRA_DELAY_SKILL = 0
CAST_CAM_ZOOM_OUT_DELAY_SKILL = 0
CALIBRATE_ACCELERATION = 1.2
CAST_CAM_OVERLOOK_SIZE = 24
CAST_CAM_OVERLOOK_REVERT_DURATION = 1.5
CAM_RESET_DURATION = 0.7
SPEED_FACTOR_FOCUS_CHARACTER = "focusCharacter"
FOCUS_MAP_RATE = 0.1
MAIN_UNIT_POS = table(
	FRIENDLY_CODE = table(
		Vector3(-105, 0, 58),
		Vector3(-105, 0, 78),
		Vector3(-105, 0, 38)
	),
	FOE_CODE = table(
		Vector3(15, 0, 58),
		Vector3(15, 0, 78),
		Vector3(15, 0, 38)
	)
)
FIELD_RIGHT_BOUND_BIAS = 0
SUB_UNIT_POS_Z = table(
	58,
	78,
	38
)
SUB_UNIT_OFFSET_X = -5
SUB_BENCH_POS = table(
	Vector3(-325, 0, 228),
	Vector3(-325, 0, 128)
)
SHIP_CLD_INTERVAL = 1
SHIP_CLD_BUFF = 8010
START_SPEED_CONST_A = 2.5
START_SPEED_CONST_B = 0.25
START_SPEED_CONST_C = 0.3
START_SPEED_CONST_D = 2.5
GRAVITY = -0.05
DUEL_MAIN_RAGE_BUFF = 6
DULE_BALANCE_BUFF = 19
SIMULATION_BALANCE_BUFF = 49
ARENA_LIST = table(
	80000,
	80001,
	80002,
	80003
)
SIMULATION_FREE_BUFF = 41
SIMULATION_ADVANTAGE_BUFF = 42
SIMULATION_ADVANTAGE_CANCEL_LIST = table(
	42,
	44,
	45
)
SIMULATION_DISADVANTAGE_BUFF = 43
SIMULATION_RIVAL_RAGE_TOTAL_COUNT = 30
CHALLENGE_INVINCIBLE_BUFF = 50
WARNING_HP_RATE = 0.7
WARNING_HP_RATE_MAIN = 0.3
SKILL_BUTTON_DEFAULT_PREFERENCE = table()
SKILL_BUTTON_DEFAULT_PREFERENCE[1] = table(
	x = 0.924,
	scale = 1,
	y = 0.135
)
SKILL_BUTTON_DEFAULT_PREFERENCE[2] = table(
	x = 0.81,
	scale = 1,
	y = 0.135
)
SKILL_BUTTON_DEFAULT_PREFERENCE[3] = table(
	x = 0.696,
	scale = 1,
	y = 0.135
)
SKILL_BUTTON_DEFAULT_PREFERENCE[4] = table(
	x = 0.58,
	scale = 1,
	y = 0.135
)
JOY_STICK_DEFAULT_PREFERENCE = table(
	x = 0.12,
	scale = 1,
	y = 0.183
)
AUTO_DEFAULT_PREFERENCE = table(
	x = 0.0625,
	scale = 1,
	y = 0.925
)
DOT_CONFIG = table()
DOT_CONFIG[1] = table(
	reduce = "igniteReduce",
	shorten = "igniteShorten",
	prolong = "igniteProlong",
	resist = "igniteResist",
	enhance = "igniteEnhance",
	hit = "ignite_accuracy"
)
DOT_CONFIG[2] = table(
	reduce = "floodingReduce",
	shorten = "floodingShorten",
	prolong = "floodingProlong",
	resist = "floodingResist",
	enhance = "floodingEnhance",
	hit = "flooding_accuracy"
)
DOT_CONFIG[10] = table()
DOT_CONFIG_DEFAULT = table(
	reduce = 0,
	shorten = 0,
	prolong = 0,
	resist = 0,
	enhance = 0,
	hit = 0
)
AMMO_DAMAGE_ENHANCE = table(
	"damageRatioByAmmoType_1",
	"damageRatioByAmmoType_2",
	"damageRatioByAmmoType_3",
	None,
	None,
	None,
	"damageRatioByAmmoType_7"
)
AMMO_DAMAGE_REDUCE = table(
	"damageReduceFromAmmoType_1",
	"damageReduceFromAmmoType_2",
	"damageReduceFromAmmoType_3",
	"damageReduceFromAmmoType_4",
	None,
	None,
	"damageReduceFromAmmoType_7"
)
DAMAGE_AMMO_TO_ARMOR_RATE_ENHANCE = table(
	"damageAmmoToArmorRateEnhance_1",
	"damageAmmoToArmorRateEnhance_2",
	"damageAmmoToArmorRateEnhance_3"
)
DAMAGE_TO_ARMOR_RATE_ENHANCE = table(
	"damageToArmorRateEnhance_1",
	"damageToArmorRateEnhance_2",
	"damageToArmorRateEnhance_3"
)
SHIP_TYPE_ACCURACY_ENHANCE = table({
	ShipType.QuZhu: "accuracyToShipType_1",
	ShipType.QingXun: "accuracyToShipType_2",
	ShipType.ZhongXun: "accuracyToShipType_3",
	ShipType.ZhanXun: "accuracyToShipType_4",
	ShipType.ZhanLie: "accuracyToShipType_5",
	ShipType.QingHang: "accuracyToShipType_6",
	ShipType.ZhengHang: "accuracyToShipType_7",
	ShipType.QianTing: "accuracyToShipType_8",
	ShipType.HangXun: "accuracyToShipType_9",
	ShipType.HangZhan: "accuracyToShipType_10",
	ShipType.LeiXun: "accuracyToShipType_11",
	ShipType.WeiXiu: "accuracyToShipType_12",
	ShipType.ZhongPao: "accuracyToShipType_13",
	ShipType.YuLeiTing: "accuracyToShipType_14",
	ShipType.JinBi: "accuracyToShipType_15",
	ShipType.ZiBao: "accuracyToShipType_16",
	ShipType.QianMu: "accuracyToShipType_17",
	ShipType.ChaoXun: "accuracyToShipType_18",
	ShipType.Yunshu: "accuracyToShipType_19",
	ShipType.DaoQuV: "accuracyToShipType_20",
	ShipType.DaoQuM: "accuracyToShipType_21",
	ShipType.FengFanS: "accuracyToShipType_22",
	ShipType.FengFanV: "accuracyToShipType_23",
	ShipType.FengFanM: "accuracyToShipType_24"
})
OXY_RAID_BASE_LINE_PVE = -20
OXY_RAID_BASE_LINE_PVP = -20
SUB_DEFAULT_STAY_AI = 10006
SUB_DEFAULT_ENGAGE_AI = 90001
SUB_DEFAULT_RETREAT_AI = 90002
SONAR_DURATION_K = 0.1
SONAR_INTERVAL_K = 0.1
VAN_SONAR_PROPERTY = table({
	ShipType.QuZhu: table(
		maxRange = 100,
		a = 2,
		minRange = 45,
		b = 32
	),
	ShipType.QingXun: table(
		maxRange = 80,
		a = 2.86,
		minRange = 30,
		b = 0
	),
	ShipType.DaoQuV: table(
		maxRange = 100,
		a = 2,
		minRange = 45,
		b = 32
	)
})
MAIN_SONAR_PROPERTY = table(
	maxRange = 15,
	a = 24,
	minRange = 0
)
SUB_EXPOSE_LASTING_DURATION = 0.5
SUB_FADE_IN_DURATION = 0.5
SUB_FADE_OUT_DURATION = 0.5
SUB_DIVE_IMMUNE_IGNITE_BUFF = 314
SUB_FLOAT_DISIMMUNE_IGNITE_BUFF = 315
PLAYER_SUB_BUBBLE_FX = "bubble"
PLAYER_SUB_BUBBLE_INIT = 200
PLAYER_SUB_BUBBLE_INTERVAL = 3
MONSTER_SUB_KAMIKAZE_DUAL_K = 50
MONSTER_SUB_KAMIKAZE_DUAL_P = 0.15
BATTLE_SHADER = table()
BATTLE_SHADER.SEMI_TRANSPARENT = "M02/Unlit_Colored_Semitransparent"
BATTLE_SHADER.GRID_TRANSPARENT = "M02/Skeleton Colored_Additive"
BATTLE_SHADER.COLORED_ALPHA = "M02/Unlit Colored_Alpha"
BATTLE_DODGEM_STAGES = table(
	1140101,
	1140102,
	1140103
)
BATTLE_DODGEM_PASS_SCORE = 10
SR_CONFIG = table()
SR_CONFIG.FLOAT_CD = 2
SR_CONFIG.DIVE_CD = 2
SR_CONFIG.BOOST_CD = 10
SR_CONFIG.SHIFT_CD = 5
SR_CONFIG.BOOST_SPEED = 2
SR_CONFIG.BOOST_DECAY = 0.2
SR_CONFIG.BOOST_DURATION = 12
SR_CONFIG.BOOST_DECAY_STAMP = 9
SR_CONFIG.BASE_POINT = 100
SR_CONFIG.POINT = 10
SR_CONFIG.DEAD_POINT = 15
SR_CONFIG.M = 2
CHALLENGE_ENHANCE = table()
CHALLENGE_ENHANCE.K = 1
CHALLENGE_ENHANCE.X = 3
CHALLENGE_ENHANCE.A = 2
CHALLENGE_ENHANCE.X1 = 5
CHALLENGE_ENHANCE.X2 = 5
CHALLENGE_ENHANCE.Y1 = 10
CHALLENGE_ENHANCE.Y2 = 5
LOADING_TIPS_LIMITED_SYSTEM = table(
	SYSTEM_WORLD
)
WORLD_ENEMY_ENHANCEMENT_CONST_B = 80
WORLD_ENEMY_ENHANCEMENT_CONST_C = 1.1
BULLET_DECREASE_DMG_FONT = table(
	4,
	0.9
)
CLOAK_EXPOSE_CONST = 50
CLOAK_EXPOSE_BASE_MIN = 100
CLOAK_EXPOSE_SKILL_MIN = 60
CLOAK_BASE_RESTORE_DELTA = -60
CLOAK_RECOVERY = 5
BASE_ARP = 0.1
CLOAK_STRIKE_ADDITIVE = 6
CLOAK_STRIKE_ADDITIVE_LIMIT = 60
CLOAK_BOMBARD_BASE_EXPOSE = 10
AIM_BIAS_FLEET_RANGE_MOD = 0.18
AIM_BIAS_SUB_RANGE_MOD = 0.18
AIM_BIAS_MONSTER_RANGE_MOD = 0.4
AIM_BIAS_DECAY_MOD = 0.01
AIM_BIAS_DECAY_MOD_MONSTER = 0.01
AIM_BIAS_DECAY_BASE = 0
AIM_BIAS_DECAY_SUB_CONST = 50
AIM_BIAS_DECAY_SMOKE = 1
AIM_BIAS_DECAY_SMOKE_NIGHT = 0.8
AIM_BIAS_SMOKE_RESTORE_DURATION = 3
AIM_BIAS_SMOKE_RECOVERY_RATE = 0.6
AIM_BIAS_DECAY_SPEED_MAX_SCOUT = 3
AIM_BIAS_DECAY_SPEED_MAX_MONSTER = 3
AIM_BIAS_DECAY_SPEED_MAX_SUB = 100
AIM_BIAS_MIN_RANGE_SCOUT = table(
	3,
	4,
	5,
	5
)
AIM_BIAS_MIN_RANGE_MONSTER = 4
AIM_BIAS_MIN_RANGE_SUB = 4
AIM_BIAS_MAX_RANGE_SCOUT = 25
AIM_BIAS_MAX_RANGE_MONSTER = 60
AIM_BIAS_MAX_RANGE_SUB = 25
AIM_BIAS_ENEMY_INIT_TIME = 1.5
FLEET_ATTR_CAP = table(
	shenpanzhijian = 6,
	yuanchou = 9,
	ReisalinAP = 99,
	Judgement = 12,
	huohun = 5
)
TARGET_SELECT_PRIORITY = table(
	C14_1 = 10,
	leastHP = 998,
	QEM_highlight = 99,
	C14_highlight = 11,
	farthest = 999,
	highlight = 99,
	xuzhang_hude = 1
)
EQUIPMENT_ACTIVE_LIMITED_BY_TYPE = table({
	31: table(
		21
	),
	32: table(
		20
	)
})
SWEET_DEATH_NATIONALITY = table(
	107
)
ALCHEMIST_AP_UI = table(
	109
)
ALCHEMIST_AP_NAME = "ReisalinAP"
