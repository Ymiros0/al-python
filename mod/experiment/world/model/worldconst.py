from packages.alsupport import bit
from packages.luatable import table, pairs, ipairs
from packages.Vector3 import Vector3, Vector2, quaternion
from Framework.i18n import i18n
from Framework.tolua.tolua import Canvas, PlayerPrefs, Renderer
from lib import pg

from const import *
from Framework import underscore
from model.proxy.BayProxy import BayProxy
from model.proxy.SettingsProxy import SettingsProxy
from model.proxy.WorldProxy import WorldProxy
from packages.alsupport import typeof, defaultValue
from support.helpers.LuaSupport import warning
from WorldMapCell import WorldMapCell
from WorldBuff import WorldBuff
from support.helpers.M02 import getGameset, getProxy, nowWorld
from support.helpers.UnitySupport import seriesAsync

Quaternion = quaternion()

Debug = False

def Print(*args):
	if Debug:
		warning(*args)

def DebugPrintAttachmentCell(arg_2_0, arg_2_1):
	if not Debug:
		return

	warning(arg_2_0)

	for iter_2_0, iter_2_1 in pairs(arg_2_1):
		warning(iter_2_0, len(iter_2_1.attachmentList))

		for iter_2_2, iter_2_3 in ipairs(iter_2_1.attachmentList):
			warning(iter_2_3.DebugPrint())

DefaultAtlas = 1

def GetProgressAtlas(arg_3_0):
	return DefaultAtlas

MaxRow = 30
MaxColumn = 30
LineCross = 2
ActionIdle = "normal"
ActionMove = "move"
ActionDrag = "tuozhuai"
ActionYun = "yun"
ActionVanish = "vanish"
ActionAppear = "appear"
AutoFightLoopCountLimit = 25
EnemySize = table({
	1: 1,
	2: 2,
	3: 3,
	4: 1,
	5: 2,
	6: 3,
	7: 1,
	8: 2,
	9: 3,
	10: 1,
	11: 2,
	12: 3,
	13: 3,
	99: 99
})
ResourceID = 3002
SwitchPlainingItemId = 120
ReqName = table({
	1: "OpReqMoveFleet",
	2: "OpReqBox",
	8: "OpReqRound",
	9: "OpReqSub",
	10: "OpReqEvent",
	12: "OpReqDiscover",
	13: "OpReqTransport",
	14: "OpReqRetreat",
	18: "OpReqTask",
	20: "OpReqMaintenance",
	21: "OpReqVision",
	23: "OpReqRedeploy",
	25: "OpReqPressingMap",
	26: "OpReqJumpOut",
	27: "OpReqEnterPort",
	28: "OpReqCatSalvage",
	29: "OpReqSwitchFleet",
	99: "OpReqSkipBattle"
})

OpReqMoveFleet = 1
OpReqBox = 2
OpReqRound = 8
OpReqSub = 9
OpReqEvent = 10
OpReqDiscover = 12
OpReqTransport = 13
OpReqRetreat = 14
OpReqTask = 18
OpReqMaintenance = 20
OpReqVision = 21
OpReqRedeploy = 23
OpReqPressingMap = 25
OpReqJumpOut = 26
OpReqEnterPort = 27
OpReqCatSalvage = 28
OpReqSwitchFleet = 29
OpReqSkipBattle = 99
OpActionFleetMove = -100
OpActionAttachmentMove = -101
OpActionAttachmentAnim = -102
OpActionNextRound = -103
OpActionEventOp = -104
OpActionMoveStep = -105
OpActionUpdate = -106
OpActionFleetAnim = -107
OpActionEventEffect = -108
OpActionTaskGoto = -109
OpActionCameraMove = -110
OpActionTrapGravityAnim = -111
RoundPlayer = 0
RoundElse = 1
DirNone = 0
DirUp = 1
DirRight = 2
DirDown = 3
DirLeft = 4

def DirToLine(arg_4_0):
	if arg_4_0 == DirNone:
		return table(
			row = 0,
			column = 0
		)
	elif arg_4_0 == DirUp:
		return table(
			row = -1,
			column = 0
		)
	elif arg_4_0 == DirRight:
		return table(
			row = 0,
			column = 1
		)
	elif arg_4_0 == DirDown:
		return table(
			row = 1,
			column = 0
		)
	elif arg_4_0 == DirLeft:
		return table(
			row = 0,
			column = -1
		)
	else:
		assert False, f"without this dir {arg_4_0}"

DefaultMapOffset = Vector3(0, -1000, -1000)

def InFOVRange(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	arg_5_4 = arg_5_4 or GetFOVRadius()

	return (arg_5_0 - arg_5_2) * (arg_5_0 - arg_5_2) + (arg_5_1 - arg_5_3) * (arg_5_1 - arg_5_3) <= arg_5_4 * arg_5_4

def GetFOVRadius():
	return pg.gameset.world_move_initial_view.key_value

def IsRookieMap(arg_7_0):
	return underscore.any(pg.gameset.world_guide_map_list.description, lambda arg_8_0: arg_7_0 == arg_8_0)

def GetRealmRookieId(arg_9_0):
	assert arg_9_0 and arg_9_0 > 0

	return pg.gameset.world_default_entrance.description[arg_9_0]

def ParseConfigDir(arg_10_0, arg_10_1):
	if arg_10_0 == -1:
		return DirUp
	elif arg_10_0 == 1:
		return DirDown
	elif arg_10_1 == -1:
		return DirLeft
	elif arg_10_1 == 1:
		return DirRight

	assert False

def Pos2FogRes(arg_11_0, arg_11_1):
	arg_11_0 = arg_11_0 % 3
	arg_11_1 = arg_11_1 % 3

	return f"miwu0{arg_11_0 * 3 + arg_11_1 + 1}"

TerrainStreamRes = table(
	"yangliu_shang",
	"yangliu_you",
	"yangliu_xia",
	"yangliu_zuo"
)
TerrainWindRes = table(
	"longjuanfeng_shang",
	"longjuanfeng_you",
	"longjuanfeng_xia",
	"longjuanfeng_zuo"
)
TerrainPoisonRes = table(
	"poison01",
	"poison02"
)

def GetTerrainEffectRes(arg_12_0, arg_12_1, arg_12_2):
	if arg_12_0 == WorldMapCell.TerrainStream:
		var_12_0 = TerrainStreamRes[arg_12_1]

		return f"world/object/{var_12_0}", var_12_0
	elif arg_12_0 == WorldMapCell.TerrainWind:
		var_12_1 = TerrainWindRes[arg_12_1]

		return f"world/object/{var_12_1}", var_12_1
	elif arg_12_0 == WorldMapCell.TerrainIce:
		return "world/object/ice", "ice"
	elif arg_12_0 == WorldMapCell.TerrainPoison:
		var_12_2 = TerrainPoisonRes[arg_12_2]

		return f"world/object/{var_12_2}", var_12_2

	assert False

def GetWindEffect():
	return "world/object/longjuanfeng", "longjuanfeng"

def GetBuffEffect(arg_14_0):
	return f"ui/{arg_14_0}", arg_14_0

PoisonEffect = "san_low"

def ArrayEffectOrder(arg_15_0, arg_15_1):
	var_15_0 = table()
	var_15_1 = arg_15_0.GetComponentsInChildren(typeof(Renderer), True)

	for iter_15_0 in range(0, var_15_1.Length):
		table.insert(var_15_0, var_15_1[iter_15_0])

	var_15_2 = arg_15_0.GetComponentsInChildren(typeof(Canvas), True)

	for iter_15_1 in range(0, var_15_2.Length):
		table.insert(var_15_0, var_15_2[iter_15_1])

	for iter_15_2, iter_15_3 in ipairs(var_15_0):
		iter_15_3.sortingOrder = iter_15_3.sortingOrder + arg_15_1

Flag16Max = 65535
LOEffectA = 1
LOQuad = 1000
LOEffectB = 1001
LOItem = 2000
LOEffectC = 2001
LOCell = 3000
LOFleet = 3001
LOTop = 4000
WindScale = table(
	0.5,
	0.5,
	0.75,
	0.75,
	1
)

def GetWindScale(arg_16_0):
	var_16_0 = arg_16_0 and WindScale[arg_16_0] or 1

	return Vector3(var_16_0, var_16_0, var_16_0)

BaseMoveDuration = 0.35

def GetTerrainMoveStepDuration(arg_17_0):
	MoveStepDuration = MoveStepDuration or table({
		WorldMapCell.TerrainNone: BaseMoveDuration,
		WorldMapCell.TerrainWind: BaseMoveDuration / 2,
		WorldMapCell.TerrainStream: BaseMoveDuration / 2,
		WorldMapCell.TerrainIce: BaseMoveDuration / 2,
		WorldMapCell.TerrainFog: BaseMoveDuration,
		WorldMapCell.TerrainFire: BaseMoveDuration,
		WorldMapCell.TerrainPoison: BaseMoveDuration
	})

	return MoveStepDuration[arg_17_0]

UIEaseDuration = 0.5
UIEaseFasterDuration = 0.3
ModelSpine = 1
ModelPrefab = 2
ResBoxPrefab = "boxprefab/"
ResChapterPrefab = "chapter/"
DirType1 = 1
DirType2 = 2
DirType4 = 4

def CalcModelPosition(arg_18_0, arg_18_1):
	return Vector3((arg_18_0.config.area_pos[1] - arg_18_1.x / 2) / PIXEL_PER_UNIT, 0, (arg_18_0.config.area_pos[2] - arg_18_1.y / 2) / PIXEL_PER_UNIT)

BrokenBuffId = pg.gameset.world_death_buff.key_value
MoveLimitBuffId = pg.gameset.world_move_buff_desc.key_value
DamageBuffList = pg.gameset.world_buff_morale.description

def ExtendPropertiesRatesFromBuffList(arg_19_0, arg_19_1):
	for iter_19_0, iter_19_1 in ipairs(arg_19_1):
		assert iter_19_1._class == WorldBuff

		if iter_19_1.IsValid():
			for iter_19_2, iter_19_3 in ipairs(iter_19_1.config.buff_attr):
				assert iter_19_1.config.percent[iter_19_2] == 1

				arg_19_0[iter_19_3] = defaultValue(arg_19_0[iter_19_3], 1) * (10000 + iter_19_1.config.buff_effect[iter_19_2] * iter_19_1.GetFloor()) / 10000

def AppendPropertiesFromBuffList(arg_20_0, arg_20_1, arg_20_2):
	for iter_20_0, iter_20_1 in ipairs(arg_20_2):
		assert iter_20_1._class == WorldBuff

		if iter_20_1.IsValid():
			for iter_20_2, iter_20_3 in ipairs(iter_20_1.config.buff_attr):
				if iter_20_1.config.percent[iter_20_2] == 1:
					arg_20_1[iter_20_3] = defaultValue(arg_20_1[iter_20_3], 0) + iter_20_1.config.buff_effect[iter_20_2] * iter_20_1.GetFloor()
				else:
					arg_20_0[iter_20_3] = defaultValue(arg_20_0[iter_20_3], 0) + iter_20_1.config.buff_effect[iter_20_2] * iter_20_1.GetFloor()

	for iter_20_4, iter_20_5 in pairs(arg_20_1):
		arg_20_1[iter_20_4] = 1 + iter_20_5 / 10000

TaskTypeSubmitItem = 2
TaskTypeArrivePort = 6
TaskTypeFleetExpansion = 7
TaskTypePressingMap = 12
FleetRedeploy = 1
FleetExpansion = 2
QuadBlinkDuration = 1
QuadSpriteWhite = "cell_white"
TransportDisplayNormal = 0
TransportDisplayGuideEnable = 1
TransportDisplayGuideDanger = 2
TransportDisplayGuideForbid = 3

def CalcRelativeRectPos(arg_21_0, arg_21_1, arg_21_2, arg_21_3):
	var_21_0 = arg_21_2.x + arg_21_1.width / 2
	var_21_1 = arg_21_2.x + arg_21_2.width - arg_21_1.width / 2
	var_21_2 = arg_21_2.y + arg_21_1.height / 2
	var_21_3 = arg_21_2.y + arg_21_2.height - arg_21_1.height / 2

	def var_21_4(arg_22_0):
		return arg_22_0.x >= var_21_0 and arg_22_0.x <= var_21_1 and arg_22_0.y >= var_21_2 and arg_22_0.y <= var_21_3

	var_21_5 = 10
	var_21_6 = Quaternion.Euler(0, 0, var_21_5)

	for iter_21_0 in range(arg_21_3, 0, -50):
		var_21_7 = Vector3(iter_21_0, 0, 0)

		for iter_21_1 in range(360 / var_21_5, 1, -1):
			var_21_7 = var_21_6 * var_21_7

			if var_21_4(arg_21_0 + var_21_7):
				return arg_21_0 + var_21_7

	return underscore.min(table(
		Vector2(var_21_0, var_21_2),
		Vector2(var_21_0, var_21_3),
		Vector2(var_21_1, var_21_3),
		Vector2(var_21_1, var_21_2)
	), lambda arg_23_0: Vector2.Distance(arg_23_0, arg_21_0))

def GetMapIconState(arg_24_0):
	if arg_24_0 == 1:
		return "normal"
	elif arg_24_0 == 2:
		return "danger"
	elif arg_24_0 == 3:
		return "danger"
	else:
		assert False, "config error.{arg_24_0}"

def HasDangerConfirm(arg_25_0):
	if arg_25_0 == 1:
		return False
	elif arg_25_0 == 2:
		return False
	elif arg_25_0 == 3:
		return True
	else:
		assert False, f"config error.{arg_25_0}"

SystemCompass = 1
SystemMemo = 2
SystemInventory = 3
SystemWorldBoss = 4
SystemCollection = 5
SystemSubmarine = 6
SystemFleetDetail = 7
SystemWorldInfo = 8
SystemRedeploy = 9
SystemScanner = 10
SystemResource = 11
SystemOutMap = 12
SystemOrderRedeploy = SystemRedeploy
SystemOrderMaintenance = 13
SystemOrderFOV = 15
SystemOrderSubmarine = SystemSubmarine
SystemResetCountDown = 16
SystemResetExchange = 17
SystemResetShop = 18
SystemAutoFight_1 = 19
SystemAutoFight_2 = 20
SystemAutoSwitch = 21
SystemDailyTask = 22

def BuildHelpTips(arg_26_0):
	var_26_0 = i18n("world_stage_help")
	var_26_1 = pg.gameset.world_stage_help.description
	var_26_2 = 1

	for iter_26_0, iter_26_1 in ipairs(var_26_1):
		if arg_26_0 >= iter_26_1[1]:
			table.insert(var_26_0, var_26_2, table(
				icon = table(
					path = "",
					atlas = iter_26_1[2]
				)
			))

			var_26_2 = var_26_2 + 1

	return var_26_0

AnimRadar = "RadarEffectUI"

def FindStageTemplates(arg_27_0):
	var_27_0 = table()

	for iter_27_0, iter_27_1 in ipairs(pg.world_stage_template.all):
		var_27_1 = pg.world_stage_template[iter_27_1]

		if var_27_1.stage_key == arg_27_0:
			table.insert(var_27_0, var_27_1)

	return var_27_0

def GetRookieBattleLoseStory():
	return pg.gameset.world_story_special_2.description[1]

FOVMapSight = 1
FOVEventEffect = 2
GuideEnemyEnd = False

def IsWorldGuideEnemyId(arg_29_0):
	if GuideEnemyEnd:
		return False

	var_29_0 = pg.gameset.world_guide_enemy_id.description

	return table.contains(var_29_0, arg_29_0)

def WorldLevelCorrect(arg_30_0, arg_30_1):
	for iter_30_0, iter_30_1 in ipairs(pg.gameset.world_expedition_level.description):
		for iter_30_2, iter_30_3 in ipairs(iter_30_1[1]):
			if arg_30_1 == iter_30_3:
				arg_30_0 = arg_30_0 + iter_30_1[2]

	return max(arg_30_0, 1)

def GetAreaFocusPos(arg_31_0):
	var_31_0 = pg.world_regions_data[arg_31_0].regions_pos

	return Vector2(var_31_0[1], var_31_0[2])

def GetTransportBlockEvent():
	if not blockEventDic:
		blockEventDic = table()

		for iter_32_0, iter_32_1 in ipairs(pg.gameset.world_movelimit_event.description):
			blockEventDic[iter_32_1] = True

	return blockEventDic

def GetTransportStoryEvent():
	if not blockStoryDic:
		blockStoryDic = table()

		for iter_33_0, iter_33_1 in ipairs(pg.gameset.world_transfer_eventlist.description):
			blockStoryDic[iter_33_1] = True

	return blockStoryDic

def IsWorldHelpNew(arg_34_0, arg_34_1):
	if arg_34_1:
		PlayerPrefs.SetInt("world_help_progress", arg_34_0)
		PlayerPrefs.Save()

		return False
	else:
		var_34_0 = PlayerPrefs.HasKey("world_help_progress") and PlayerPrefs.GetInt("world_help_progress") or 0

		if var_34_0 < arg_34_0:
			for iter_34_0, iter_34_1 in ipairs(pg.world_help_data.all):
				var_34_1 = pg.world_help_data[iter_34_1]

				if arg_34_0 >= var_34_1.stage:
					if var_34_0 < var_34_1.stage:
						return True
					else:
						for iter_34_2, iter_34_3 in ipairs(var_34_1.stage_help):
							if var_34_0 < iter_34_3[1] and arg_34_0 >= iter_34_3[1]:
								return True

		return False

def ParsingBuffs(arg_35_0):
	var_35_0 = table()

	def _function(arg_36_0):
		var_36_0 = WorldBuff.New()

		var_36_0.Setup(table(
			id = arg_36_0.id,
			floor = arg_36_0.stack,
			round = arg_36_0.round,
			step = arg_36_0.step
		))

		var_35_0[var_36_0.id] = var_36_0

	underscore.each(arg_35_0, _function)

	return var_35_0

def CompareBuffs(arg_37_0, arg_37_1):
	var_37_0 = underscore.extend(table(), arg_37_0)
	var_37_1 = table()
	var_37_2 = underscore.extend(table(), arg_37_1)

	for iter_37_0, iter_37_1 in pairs(var_37_0):
		if var_37_2[iter_37_0]:
			var_37_1[iter_37_0] = var_37_0[iter_37_0]
			var_37_0[iter_37_0] = None
			var_37_2[iter_37_0] = None

	return table({
		"remove": var_37_0,
		"continue": var_37_1,
		"add": var_37_2
	})

def FetchWorldShip(arg_38_0):
	var_38_0 = nowWorld().GetShip(arg_38_0)

	assert var_38_0, f"world ship not exist. {arg_38_0}"

	return var_38_0

def FetchShipVO(arg_39_0):
	var_39_0 = getProxy(BayProxy).getShipById(arg_39_0)

	assert var_39_0, f"ship not exist. {arg_39_0}"

	return var_39_0

def FetchRawShipVO(arg_40_0):
	var_40_0 = getProxy(BayProxy).getRawData()[arg_40_0]

	assert var_40_0, f"ship not exist. {arg_40_0}"

	return var_40_0

def ReqWorldCheck(arg_41_0):
	from World import World
	var_41_0 = table()

	if nowWorld().type == World.TypeBase:
		def _function(arg_42_0):
			def _function(arg_43_0):
				var_43_0 = getProxy(WorldProxy)

				var_43_0.BuildWorld(World.TypeFull)
				var_43_0.NetFullUpdate(arg_43_0)
				arg_42_0()
			pg.ConnectionMgr.GetInstance().Send(33000, table(
				type = 0
			), 33001, _function)
		table.insert(var_41_0, _function)

	seriesAsync(var_41_0, arg_41_0)

def ReqWorldForServer():
	pg.ConnectionMgr.GetInstance().Send(33000, table(
		type = 1
	), 33001, lambda _: None)

ObstacleConfig = table(
	2,
	3,
	7,
	0,
	6,
	1,
	4,
	5
)
ObstacleType = table(
	"leave",
	"arrive",
	"pass"
)

def GetObstacleKey(arg_46_0):
	return bit.lshift(1, len(ObstacleType) - table.indexof(ObstacleType, arg_46_0))

def GetObstacleConfig(arg_47_0, arg_47_1):
	var_47_0 = GetObstacleKey(arg_47_1)

	return bit.band(ObstacleConfig[arg_47_0], var_47_0) > 0

def RangeCheck(arg_48_0, arg_48_1, arg_48_2):
	for iter_48_0 in range(arg_48_0.row - arg_48_1, arg_48_0.row + arg_48_1):
		for iter_48_1 in range(arg_48_0.column - arg_48_1, arg_48_0.column + arg_48_1):
			if InFOVRange(arg_48_0.row, arg_48_0.column, iter_48_0, iter_48_1, arg_48_1):
				arg_48_2(iter_48_0, iter_48_1)

def CheckWorldStorySkip(arg_49_0):
	return table.contains(pg.gameset.world_quickmode_skiplua.description, arg_49_0) and getProxy(SettingsProxy).GetWorldFlag("story_tips") and pg.NewStoryMgr.GetInstance().IsPlayed(arg_49_0)

def GetNShopTimeStamp():
	if not nShopTimestamp:
		var_50_0 = table()

		var_50_0.year, var_50_0.month, var_50_0.day = getGameset("world_newshop_date")[2]
		var_50_0.hour, var_50_0.min, var_50_0.sec = 0, 0, 0
		nShopTimestamp = pg.TimeMgr.GetInstance().Table2ServerTime(var_50_0)

	return nShopTimestamp

