
from Framework import underscore
from Framework.i18n import i18n
from lib import pg
from mod.experiment.BaseEntity import BaseEntity
from model.const import FleetType, TeamType
from packages.luatable import Clone, ipairs, table, pairs
from support.helpers.M02 import getProxy
from boss.WorldBossProxy import WorldBossProxy
from collection.WorldCollectionProxy import WorldCollectionProxy
from WorldAtlas import WorldAtlas
import WorldConst
from worldstaminamanager import WorldStaminaManager


def var_0_1():
	return table({
		TeamType.Main: table(),
		TeamType.Vanguard: table(),
		TeamType.Submarine: table(),
		'commanders': table()
	})

var_0_2 = table(
	treasure_flag = 1
)


class World(BaseEntity):
	Fields = table(
		colorDic = "table",
		stepCount = "number",
		cdTimeList = "table",
		type = "number",
		inventoryProxy = "table",
		staminaMgr = "table",
		taskProxy = "table",
		autoInfos = "table",
		roundIndex = "number",
		fleets = "table",
		expiredTime = "number",
		activateCount = "number",
		pressingAwardDic = "table",
		achievements = "table",
		submarineSupport = "boolean",
		collectionProxy = "table",
		goodDic = "table",
		achieveEntranceStar = "table",
		baseCmdIds = "table",
		resetAward = "table",
		gobalFlag = "table",
		forceLock = "boolean",
		resetLimitTip = "boolean",
		atlas = "table",
		worldBossProxy = "table",
		progress = "number",
		globalBuffDic = "table",
		lowestHP = "table",
		treasureCount = "number",
		defaultFleets = "table",
		realm = "number",
		isAutoSwitch = "boolean",
		isAutoFight = "boolean",
		baseShipIds = "table",
		activateTime = "number"
	)
	EventUpdateSubmarineSupport = "World.EventUpdateSubmarineSupport"
	EventSwitchMap = "World.EventSwitchMap"
	EventUpdateProgress = "World.EventUpdateProgress"
	EventUpdateShopGoods = "World.EventUpdateShopGoods"
	EventUpdateGlobalBuff = "World.EventUpdateGlobalBuff"
	EventAddPortShip = "World.EventAddPortShip"
	EventRemovePortShip = "World.EventRemovePortShip"
	EventAchieved = "World.EventAchieved"
	Listeners = table(
		onUpdateItem = "OnUpdateItem",
		onUpdateTask = "OnUpdateTask"
	)
	TypeBase = 0
	TypeFull = 1
	InheritNameList = table(
		staminaMgr = lambda: WorldStaminaManager(),
		collectionProxy = lambda: WorldCollectionProxy(),
		worldBossProxy = lambda: WorldBossProxy()
	)

	def __init__(arg_4_0, arg_4_1, arg_4_2):
		super().__init__(arg_4_0)

		arg_4_0.type = arg_4_1

		arg_4_0.InheritReset(arg_4_2)

	def Build(arg_5_0):
		arg_5_0.atlas = WorldAtlas(WorldConst.DefaultAtlas)
		arg_5_0.realm = 0
		arg_5_0.fleets = table()
		arg_5_0.defaultFleets = table()
		arg_5_0.activateTime = 0
		arg_5_0.expiredTime = 0
		arg_5_0.roundIndex = None
		arg_5_0.submarineSupport = None
		arg_5_0.achievements = table()
		arg_5_0.achieveEntranceStar = table()

		arg_5_0.InitWorldShopGoods()
		arg_5_0.InitWorldColorDictionary()

		arg_5_0.activateCount = 0
		arg_5_0.stepCount = 0
		arg_5_0.treasureCount = 0
		arg_5_0.progress = 0
		arg_5_0.cdTimeList = table()
		arg_5_0.globalBuffDic = table()
		arg_5_0.pressingAwardDic = table()
		arg_5_0.lowestHP = table()
		arg_5_0.gobalFlag = table()
		arg_5_0.isAutoFight = False

		arg_5_0.InitAutoInfos()

		arg_5_0.inventoryProxy = WorldInventoryProxy()

		arg_5_0.inventoryProxy.AddListener(WorldInventoryProxy.EventUpdateItem, arg_5_0.onUpdateItem)

		arg_5_0.taskProxy = WorldTaskProxy()

		arg_5_0.taskProxy.AddListener(WorldTaskProxy.EventUpdateTask, arg_5_0.onUpdateTask)

		arg_5_0.baseShipIds = table()
		arg_5_0.baseCmdIds = table()

	def Dispose(arg_6_0, arg_6_1):
		var_6_0 = arg_6_1 and table(
			realm = arg_6_0.realm,
			defaultFleets = arg_6_0.defaultFleets,
			achievements = arg_6_0.achievements,
			achieveEntranceStar = arg_6_0.achieveEntranceStar,
			activateCount = arg_6_0.activateCount,
			progress = arg_6_0.progress,
			staminaMgr = arg_6_0.staminaMgr,
			collectionProxy = arg_6_0.collectionProxy
		) or table()

		var_6_0.worldBossProxy = arg_6_0.worldBossProxy

		for iter_6_0 in pairs(InheritNameList):
			if not var_6_0[iter_6_0]:
				arg_6_0[iter_6_0].Dispose()

		arg_6_0.inventoryProxy.RemoveListener(WorldInventoryProxy.EventUpdateItem, arg_6_0.onUpdateItem)
		arg_6_0.inventoryProxy.Dispose()
		arg_6_0.taskProxy.RemoveListener(WorldTaskProxy.EventUpdateTask, arg_6_0.onUpdateTask)
		arg_6_0.taskProxy.Dispose()
		arg_6_0.atlas.Dispose()
		arg_6_0.Clear()

		return var_6_0

	def InheritReset(arg_7_0, arg_7_1):
		arg_7_1 = arg_7_1 or table()

		if arg_7_1.progress:
			arg_7_0.UpdateProgress(arg_7_1.progress)

			arg_7_1.progress = None

		for iter_7_0, iter_7_1 in pairs(arg_7_1):
			arg_7_0[iter_7_0] = iter_7_1

		for iter_7_2, iter_7_3 in pairs(InheritNameList):
			if not arg_7_1[iter_7_2]:
				arg_7_0[iter_7_2] = iter_7_3()

	def UsePortNShop(arg_8_0):
		return arg_8_0.IsReseted() and arg_8_0.activateTime >= WorldConst.GetNShopTimeStamp()

	def IsReseted(arg_9_0):
		return arg_9_0.activateCount > (arg_9_0.IsActivate() and 1 or 0)

	def IsActivate(arg_10_0):
		if arg_10_0.type == World.TypeBase:
			return #arg_10_0.baseShipIds > 0
		else:
			return bool(arg_10_0.GetActiveMap())

	def CheckResetProgress(arg_11_0):
		return pg.gameset.world_resetting_stage.key_value <= arg_11_0.progress

	def GetResetWaitingTime(arg_12_0):
		return arg_12_0.expiredTime - pg.TimeMgr.GetInstance().GetServerTime()

	def CheckReset(arg_13_0, arg_13_1):
		return arg_13_0.IsActivate() and (arg_13_1 or arg_13_0.CheckResetProgress()) and arg_13_0.GetResetWaitingTime() < 0

	def GetAtlas(arg_14_0):
		return arg_14_0.atlas

	def GetEntrance(arg_15_0, arg_15_1):
		return arg_15_0.atlas.GetEntrance(arg_15_1)

	def GetActiveEntrance(arg_16_0):
		return arg_16_0.atlas.GetActiveEntrance()

	def GetMap(arg_17_0, arg_17_1):
		return arg_17_0.atlas.GetMap(arg_17_1)

	def GetActiveMap(arg_18_0):
		return arg_18_0.atlas.GetActiveMap()

	def OnSwitchMap(arg_19_0):
		arg_19_0.ResetRound()

		if arg_19_0.submarineSupport:
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_submarine_5"))
			arg_19_0.ResetSubmarine()
			arg_19_0.UpdateSubmarineSupport(False)

		arg_19_0.DispatchEvent(EventSwitchMap)
		print(f"switch 2 map. {arg_19_0.GetActiveMap().id}, {arg_19_0.GetActiveMap().gid}")

	def GetRound(arg_20_0):
		return arg_20_0.roundIndex % 2

	def IncRound(arg_21_0):
		arg_21_0.roundIndex = arg_21_0.roundIndex + 1

	def ResetRound(arg_22_0):
		arg_22_0.roundIndex = 0

	def UpdateProgress(arg_23_0, arg_23_1):
		if arg_23_1 > arg_23_0.progress:
			var_23_0 = arg_23_0.progress

			arg_23_0.progress = arg_23_1

			arg_23_0.atlas.UpdateProgress(var_23_0, arg_23_1)
			arg_23_0.DispatchEvent(EventUpdateProgress)

	def GetProgress(arg_24_0):
		return arg_24_0.progress

	def SetRealm(arg_25_0, arg_25_1):
		if arg_25_0.realm != arg_25_1:
			arg_25_0.realm = arg_25_1

	def GetRealm(arg_26_0):
		return 1

	def CanCallSubmarineSupport(arg_27_0):
		return arg_27_0.GetSubmarineFleet()

	def IsSubmarineSupporting(arg_28_0):
		return arg_28_0.submarineSupport

	def UpdateSubmarineSupport(arg_29_0, arg_29_1):
		arg_29_0.submarineSupport = arg_29_1

		arg_29_0.DispatchEvent(EventUpdateSubmarineSupport)

	def GetSubAidFlag(arg_30_0):
		return arg_30_0.IsSubmarineSupporting() and arg_30_0.GetSubmarineFleet().GetAmmo() > 0

	def ResetSubmarine(arg_31_0):
		var_31_0 = arg_31_0.GetSubmarineFleet()

		if var_31_0:
			var_31_0.RepairSubmarine()

	def SetFleets(arg_32_0, arg_32_1):
		arg_32_0.fleets = arg_32_1

		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inWorld")

	def GetFleets(arg_33_0):
		return underscore.rest(arg_33_0.fleets, 1)

	def GetFleet(arg_34_0, arg_34_1):
		return arg_34_1 and underscore.detect(arg_34_0.fleets, lambda arg_35_0: arg_35_0.id == arg_34_1) or arg_34_0.GetActiveMap().GetFleet()

	def GetNormalFleets(arg_36_0):
		return underscore.filter(arg_36_0.fleets, lambda arg_37_0: arg_37_0.GetFleetType() == FleetType.Normal)

	def GetSubmarineFleet(arg_38_0):
		return underscore.detect(arg_38_0.fleets, lambda arg_39_0: arg_39_0.GetFleetType() == FleetType.Submarine)

	def GetShips(arg_40_0):
		var_40_0 = table()

		underscore.each(arg_40_0.GetFleets(), lambda arg_41_0: underscore.each(arg_41_0.GetShips(True), lambda arg_42_0: table.insert(var_40_0, arg_42_0)))

		return var_40_0

	def GetShipVOs(arg_43_0):
		if arg_43_0.type == World.TypeBase:
			return underscore.map(arg_43_0.baseShipIds, lambda arg_44_0: WorldConst.FetchShipVO(arg_44_0))
		else:
			return underscore.map(arg_43_0.GetShips(), lambda arg_45_0: WorldConst.FetchShipVO(arg_45_0.id))

	def GetShip(arg_46_0, arg_46_1):
		return underscore.detect(arg_46_0.GetShips(), lambda arg_47_0: arg_47_0.id == arg_46_1)

	def GetShipVO(arg_48_0, arg_48_1):
		var_48_0 = arg_48_0.GetShip(arg_48_1)

		return var_48_0 and WorldConst.FetchShipVO(var_48_0.id)

	def SetDefaultFleets(arg_49_0, arg_49_1):
		arg_49_0.defaultFleets = arg_49_1

	def GetDefaultFleets(arg_50_0):
		return underscore.rest(arg_50_0.defaultFleets, 1)

	def TransDefaultFleets(arg_51_0):
		arg_51_0.defaultFleets = underscore.map(arg_51_0.fleets, lambda arg_52_0: arg_52_0.Trans(WorldBaseFleet))

	def GetLevel(arg_53_0):
		return underscore(arg_53_0.GetFleets()).chain().map(lambda arg_54_0: arg_54_0.GetLevel()).max().value()

	def GetWorldPower(arg_55_0):
		var_55_0 = 0

		def _function(arg_56_0):
			var_55_0 = var_55_0 + arg_56_0.GetGearScoreSum()

		underscore.each(arg_55_0.fleets, _function)

		return int(var_55_0 * (1 + arg_55_0.GetWorldMapBuffAverageLevel() / pg.gameset.world_strength_correct.key_value))

	def GetWorldRank(arg_57_0):
		var_57_0 = 0
		var_57_1 = underscore.map(arg_57_0.GetNormalFleets(), lambda arg_58_0: arg_58_0.GetLevelCount() / 6)
		var_57_2 = pg.gameset.world_level_correct.description

		for iter_57_0, iter_57_1 in ipairs(var_57_1):
			var_57_0 = var_57_0 + iter_57_1 * var_57_2[iter_57_0]

		var_57_3 = arg_57_0.GetSubmarineFleet()

		if var_57_3:
			var_57_0 = var_57_0 + var_57_3.GetLevelCount() / 3 * var_57_2[5]

		var_57_4 = var_57_0 * arg_57_0.GetWorldMapBuffAverageLevel()
		var_57_5
		var_57_6 = pg.gameset.world_suggest_level.description

		for iter_57_2, iter_57_3 in ipairs(var_57_6):
			if var_57_4 < iter_57_3:
				break
			else:
				var_57_5 = iter_57_2

		return var_57_5

	def GetBossProxy(arg_59_0):
		return arg_59_0.worldBossProxy

	def GetTaskProxy(arg_60_0):
		return arg_60_0.taskProxy

	def GetInventoryProxy(arg_61_0):
		return arg_61_0.inventoryProxy

	def GetCollectionProxy(arg_62_0):
		return arg_62_0.collectionProxy

	def VerifyFormation(arg_63_0):
		var_63_0 = table()

		def _function(arg_64_0):
			var_63_0[arg_64_0.id] = (var_63_0[arg_64_0.id] or 0) + 1

			assert var_63_0[arg_64_0.id] <= 1, f"repeated ship id. {arg_64_0.id}"

		underscore.each(arg_63_0.GetShips(), _function)

	def CalcRepairCost(arg_65_0, arg_65_1):
		var_65_0 = WorldConst.FetchShipVO(arg_65_1.id).level - arg_65_0.GetLevel()

		if arg_65_1.IsBroken():
			var_65_1 = pg.gameset.world_port_service_2_interval.description

			return (underscore.detect(var_65_1, lambda arg_66_0: arg_66_0[1] >= var_65_0) or var_65_1[-1])[2] * pg.gameset.world_port_service_2_price.key_value
		elif not arg_65_1.IsHpFull():
			var_65_2 = pg.gameset.world_port_service_1_interval.description
			var_65_3 = pg.gameset.world_port_service_1_price.description

			return (underscore.detect(var_65_2, lambda arg_67_0: arg_67_0[1] >= var_65_0) or var_65_2[-1])[2] * (underscore.detect(var_65_3, lambda arg_68_0: arg_68_0[1] >= arg_65_1.hpRant) or var_65_3[-1])[2]

		return 0

	def GetMoveRange(arg_69_0, arg_69_1):
		var_69_0 = arg_69_0.GetActiveMap()

		if var_69_0.CanLongMove(arg_69_1):
			return var_69_0.GetLongMoveRange(arg_69_1)
		else:
			return var_69_0.GetMoveRange(arg_69_1)

	def IsRookie(arg_70_0):
		return arg_70_0.activateCount == 0 and arg_70_0.progress <= 0

	def EntranceToReplacementMapList(arg_71_0, arg_71_1):
		var_71_0 = table()

		for iter_71_0, iter_71_1 in ipairs(arg_71_1.config.stage_chapter):
			if arg_71_0.GetProgress() >= iter_71_1[1] and arg_71_0.GetProgress() <= iter_71_1[2]:
				table.insert(var_71_0, arg_71_0.GetMap(iter_71_1[3]))

		for iter_71_2, iter_71_3 in ipairs(arg_71_1.config.task_chapter):
			var_71_1 = arg_71_0.taskProxy.getTaskById(iter_71_3[1])

			if var_71_1 and var_71_1.isAlive():
				table.insert(var_71_0, arg_71_0.GetMap(iter_71_3[2]))

		if arg_71_1.becomeSairen:
			table.insert(var_71_0, arg_71_0.GetMap(arg_71_1.config.sairen_chapter[1]))

		for iter_71_4, iter_71_5 in ipairs(arg_71_1.config.teasure_chapter):
			if arg_71_0.inventoryProxy.GetItemCount(iter_71_5[1]) > 0:
				table.insert(var_71_0, arg_71_0.GetMap(iter_71_5[2]))

		var_71_2 = arg_71_1.GetBaseMap()

		if var_71_2.isPressing and len(arg_71_1.config.complete_chapter) > 0:
			table.insert(var_71_0, arg_71_0.GetMap(arg_71_1.config.complete_chapter[1]))

		table.insert(var_71_0, var_71_2)

		if arg_71_1.active and not underscore.any(var_71_0, lambda arg_72_0: arg_72_0.active):
			table.insert(var_71_0, arg_71_0.GetActiveMap())

		var_71_3 = table()

		def _function(arg_73_0):
			if var_71_3[arg_73_0.id]:
				return False
			else:
				var_71_3[arg_73_0.id] = True

				return True

		return (underscore.filter(var_71_0, _function))

	def ReplacementMapType(arg_74_0, arg_74_1):
		for iter_74_0, iter_74_1 in ipairs(arg_74_0.config.stage_chapter):
			if iter_74_1[3] == arg_74_1.id:
				return "stage_chapter", i18n("area_zhuxian")

		for iter_74_2, iter_74_3 in ipairs(arg_74_0.config.task_chapter):
			if iter_74_3[2] == arg_74_1.id:
				var_74_0 = pg.world_task_data[iter_74_3[1]].type

				if var_74_0 == 0:
					return "task_chapter", i18n("area_zhuxian")
				elif var_74_0 == 6:
					return "task_chapter", i18n("area_dangan")
				else:
					return "task_chapter", i18n("area_renwu")

		for iter_74_4, iter_74_5 in ipairs(arg_74_0.config.teasure_chapter):
			if iter_74_5[2] == arg_74_1.id:
				var_74_1 = pg.world_item_data_template[iter_74_5[1]].usage_arg[1] == 1

				return "teasure_chapter", var_74_1 and i18n("area_shenyuan") or i18n("area_yinmi")

		if arg_74_0.config.sairen_chapter[1] == arg_74_1.id:
			return "sairen_chapter", i18n("area_yaosai")

		if arg_74_0.config.complete_chapter[1] == arg_74_1.id:
			return "complete_chapter", i18n("area_anquan")

		if arg_74_0.GetBaseMapId() == arg_74_1.id:
			return "base_chapter", i18n("area_putong")

		return "test_chapter", i18n("area_unkown")

	def FindTreasureEntrance(arg_75_0, arg_75_1):
		return underscore.values(arg_75_0.atlas.GetTreasureDic(arg_75_1))[1]

	def TreasureMap2ItemId(arg_76_0, arg_76_1, arg_76_2):
		var_76_0 = arg_76_0.GetEntrance(arg_76_2)

		for iter_76_0, iter_76_1 in ipairs(var_76_0.config.teasure_chapter):
			if iter_76_1[2] == arg_76_1:
				return iter_76_1[1]

	def CheckFleetMovable(arg_77_0):
		var_77_0 = arg_77_0.GetActiveMap()
		var_77_1 = var_77_0.GetFleet()

		return arg_77_0.GetRound() == WorldConst.RoundPlayer and var_77_0.CheckFleetMovable(var_77_1) and not var_77_0.CheckInteractive()

	def SetAchieveSuccess(arg_78_0, arg_78_1, arg_78_2):
		arg_78_0.achieveEntranceStar[arg_78_1] = arg_78_0.achieveEntranceStar[arg_78_1] or table()
		arg_78_0.achieveEntranceStar[arg_78_1][arg_78_2] = True

	def GetMapAchieveStarDic(arg_79_0, arg_79_1):
		return arg_79_0.achieveEntranceStar[arg_79_1] or table()

	def GetAchievement(arg_80_0, arg_80_1):
		if not arg_80_0.achievements[arg_80_1]:
			arg_80_0.achievements[arg_80_1] = WorldAchievement.New()

			arg_80_0.achievements[arg_80_1].Setup(arg_80_1)

		return arg_80_0.achievements[arg_80_1]

	def GetAchievements(arg_81_0, arg_81_1):
		var_81_0 = table()

		underscore.each(arg_81_1.config.normal_target, lambda arg_82_0: table.insert(var_81_0, arg_81_0.GetAchievement(arg_82_0)))
		underscore.each(arg_81_1.config.cryptic_target, lambda arg_83_0: table.insert(var_81_0, arg_81_0.GetAchievement(arg_83_0)))

		return var_81_0

	def IsNormalAchievementAchieved(arg_84_0, arg_84_1):
		return arg_84_0.CountAchievements(arg_84_1) >= len(arg_84_1.config.normal_target)

	def AnyUnachievedAchievement(arg_85_0, arg_85_1):
		var_85_0 = arg_85_0.GetMapAchieveStarDic(arg_85_1.id)
		var_85_1 = underscore.detect(arg_85_1.GetAchievementAwards(), lambda arg_86_0: not var_85_0[arg_86_0.star])

		if var_85_1:
			var_85_2, var_85_3 = arg_85_0.CountAchievements(arg_85_1)

			return var_85_2 + var_85_3 >= var_85_1.star, var_85_1

	def GetFinishAchievements(arg_87_0, arg_87_1):
		arg_87_1 = arg_87_1 or arg_87_0.atlas.GetAchEntranceList()

		var_87_0 = table()
		var_87_1 = table()

		for iter_87_0, iter_87_1 in ipairs(arg_87_1):
			var_87_2, var_87_3 = arg_87_0.CountAchievements(iter_87_1)
			var_87_4 = arg_87_0.GetMapAchieveStarDic(iter_87_1.id)
			var_87_5 = table()

			for iter_87_2, iter_87_3 in ipairs(iter_87_1.GetAchievementAwards()):
				if not var_87_4[iter_87_3.star] and var_87_2 + var_87_3 >= iter_87_3.star:
					table.insert(var_87_5, iter_87_3.star)

			if len(var_87_5) > 0:
				table.insert(var_87_0, table(
					id = iter_87_1.id,
					star_list = var_87_5
				))
				table.insert(var_87_1, iter_87_1.id)

		return var_87_0, var_87_1

	def CountAchievements(arg_88_0, arg_88_1):
		var_88_0 = 0
		var_88_1 = 0
		var_88_2 = 0
		var_88_3 = arg_88_1 and table(
			arg_88_1
		) or arg_88_0.atlas.GetAchEntranceList()

		for iter_88_0, iter_88_1 in ipairs(var_88_3):
			for iter_88_2, iter_88_3 in ipairs(iter_88_1.config.normal_target):
				var_88_0 = var_88_0 + (arg_88_0.achievements[iter_88_3] and arg_88_0.achievements[iter_88_3].IsAchieved() and 1 or 0)

			for iter_88_4, iter_88_5 in ipairs(iter_88_1.config.cryptic_target):
				var_88_1 = var_88_1 + (arg_88_0.achievements[iter_88_5] and arg_88_0.achievements[iter_88_5].IsAchieved() and 1 or 0)

			var_88_2 = var_88_2 + len(iter_88_1.config.normal_target) + len(iter_88_1.config.cryptic_target)

		return var_88_0, var_88_1, var_88_2



	def BuildFormationIds(arg_90_0):
		var_90_0 = table({
			FleetType.Normal: table(),
			FleetType.Submarine: table()
		})
		var_90_1 = table({
			FleetType.Normal: 2,
			FleetType.Submarine: 0
		})
		var_90_2 = table({
			FleetType.Normal: 1,
			FleetType.Submarine: 1
		})

		for iter_90_0, iter_90_1 in ipairs(pg.world_stage_template):
			if arg_90_0.GetProgress() >= iter_90_1.stage_key:
				var_90_1[FleetType.Normal] = max(var_90_1[FleetType.Normal], iter_90_1.fleet_num)
			else:
				break

		if arg_90_0.IsSystemOpen(WorldConst.SystemSubmarine):
			var_90_1[FleetType.Submarine] = 1

		for iter_90_2, iter_90_3 in pairs(var_90_0):
			for iter_90_4 in range(1, var_90_1[iter_90_2]):
				table.insert(iter_90_3, var_0_1())

		for iter_90_5, iter_90_6 in ipairs(arg_90_0.IsActivate() and arg_90_0.GetFleets() or arg_90_0.GetDefaultFleets()):
			var_90_3 = iter_90_6.GetFleetType()
			var_90_4 = var_90_2[var_90_3]

			if var_90_4 <= var_90_1[var_90_3]:
				var_90_0[var_90_3][var_90_4] = iter_90_6.BuildFormationIds()
				var_90_2[var_90_3] = var_90_4 + 1

		var_90_5
		var_90_6 = arg_90_0.GetTaskProxy().getTasks()

		for iter_90_7, iter_90_8 in pairs(var_90_6):
			if iter_90_8.config.complete_condition == WorldConst.TaskTypeFleetExpansion and iter_90_8.isAlive():
				var_90_5 = iter_90_8.config.complete_parameter[1]

				break

		if var_90_5:
			for iter_90_9 in range(len(var_90_0[FleetType.Normal]) + 1, var_90_5):
				var_90_0[FleetType.Normal][iter_90_9] = var_0_1()

		var_90_7 = 0

		for iter_90_10, iter_90_11 in pairs(var_90_0):
			var_90_7 = var_90_7 + len(iter_90_11)

		return var_90_5 and WorldConst.FleetExpansion or WorldConst.FleetRedeploy, var_90_0, var_90_7

	def FormationIds2NetIds(arg_91_0, arg_91_1):
		var_91_0 = table()

		for iter_91_0, iter_91_1 in ipairs(table(
			FleetType.Normal,
			FleetType.Submarine
		)):
			for iter_91_2, iter_91_3 in ipairs(arg_91_1[iter_91_1]):
				var_91_1 = table()

				for iter_91_4, iter_91_5 in ipairs(table(
					TeamType.Main,
					TeamType.Vanguard,
					TeamType.Submarine
				)):
					for iter_91_6 in range(1, 4):
						if iter_91_3[iter_91_5][iter_91_6]:
							table.insert(var_91_1, iter_91_3[iter_91_5][iter_91_6])

				if len(var_91_1) > 0:
					table.insert(var_91_0, table(
						ship_id_list = var_91_1,
						commanders = Clone(iter_91_3.commanders)
					))

		return var_91_0

	def CompareRedeploy(arg_92_0, arg_92_1):
		var_92_0 = table(
			TeamType.Main,
			TeamType.Vanguard,
			TeamType.Submarine
		)
		var_92_1 = table()
		var_92_2 = 0

		for iter_92_0, iter_92_1 in pairs(arg_92_1):
			for iter_92_2, iter_92_3 in ipairs(iter_92_1):
				for iter_92_4, iter_92_5 in ipairs(var_92_0):
					for iter_92_6 in (1, 2, 3):
						var_92_3 = iter_92_3[iter_92_5][iter_92_6]

						if var_92_3 and not var_92_1[var_92_3]:
							var_92_1[var_92_3] = True
							var_92_2 = var_92_2 + 1

		var_92_4 = table()
		var_92_5 = 0

		for iter_92_7, iter_92_8 in ipairs(arg_92_0.GetFleets()):
			for iter_92_9, iter_92_10 in ipairs(var_92_0):
				var_92_6 = iter_92_8.GetTeamShips(iter_92_10, True)

				for iter_92_11, iter_92_12 in ipairs(var_92_6):
					if not var_92_4[iter_92_12.id]:
						var_92_4[iter_92_12.id] = True
						var_92_5 = var_92_5 + 1

		if var_92_5 != var_92_2:
			return True

		for iter_92_13, iter_92_14 in pairs(var_92_4):
			if not var_92_1[iter_92_13]:
				return True

		for iter_92_15, iter_92_16 in pairs(var_92_1):
			if not var_92_4[iter_92_15]:
				return True

		return False

	def IsSystemOpen(arg_93_0, arg_93_1):
		var_93_0 = arg_93_0.GetRealm()

		for iter_93_0, iter_93_1 in ipairs(pg.world_stage_template.all):
			var_93_1 = pg.world_stage_template[iter_93_1]

			if var_93_1.stage_ui[1] == arg_93_1 and (var_93_1.stage_ui[2] == 0 or var_93_1.stage_ui[2] == var_93_0):
				return arg_93_0.GetProgress() >= var_93_1.stage_key

		return True

	def CalcCDTimeCost(arg_94_0, arg_94_1, arg_94_2):
		var_94_0 = max(pg.TimeMgr.GetInstance().GetServerTime() - arg_94_1, 0)

		return int(arg_94_0[1] * max(arg_94_0[2] - var_94_0, 0) / arg_94_0[2] * max(10000 - arg_94_2, 0) / 10000)

	def GetReqCDTime(arg_95_0, arg_95_1):
		return arg_95_0.cdTimeList[arg_95_1] or 0

	def SetReqCDTime(arg_96_0, arg_96_1, arg_96_2):
		arg_96_0.cdTimeList[arg_96_1] = arg_96_2

	def InitWorldShopGoods(arg_97_0):
		arg_97_0.goodDic = table()

		for iter_97_0, iter_97_1 in ipairs(table(
			ShopArgs.WorldShop,
			ShopArgs.WorldCollection
		)):
			for iter_97_2, iter_97_3 in ipairs(pg.shop_template.get_id_list_by_genre[iter_97_1]):
				arg_97_0.goodDic[iter_97_3] = 0

	def UpdateWorldShopGoods(arg_98_0, arg_98_1):
		def _function(arg_99_0):
			assert arg_98_0.goodDic[arg_99_0.goods_id], f"without this good in id {arg_99_0.goods_id}"

			arg_98_0.goodDic[arg_99_0.goods_id] = arg_98_0.goodDic[arg_99_0.goods_id] + arg_99_0.count
		underscore.each(arg_98_1, _function)
		arg_98_0.DispatchEvent(EventUpdateShopGoods, arg_98_0.goodDic)

	def GetWorldShopGoodsDictionary(arg_100_0):
		return arg_100_0.goodDic

	def InitWorldColorDictionary(arg_101_0):
		arg_101_0.colorDic = table()

		def _function(arg_102_0):
			var_102_0 = pg.world_chapter_colormask[arg_102_0]
			var_102_1 = Color.New(var_102_0.color[1] / 255, var_102_0.color[2] / 255, var_102_0.color[3] / 255)

			arg_101_0.colorDic[var_102_1.ToHex()] = var_102_0.id

		underscore.each(pg.world_chapter_colormask.all, _function)

	def ColorToEntrance(arg_103_0, arg_103_1):
		return arg_103_0.colorDic[arg_103_1.ToHex()] and arg_103_0.GetEntrance(arg_103_0.colorDic[arg_103_1.ToHex()])

	def GetGlobalBuff(arg_104_0, arg_104_1):
		if not arg_104_0.globalBuffDic[arg_104_1]:
			var_104_0 = WorldBuff.New()

			var_104_0.Setup(table(
				floor = 0,
				id = arg_104_1
			))

			arg_104_0.globalBuffDic[arg_104_1] = var_104_0

		return arg_104_0.globalBuffDic[arg_104_1]

	def AddGlobalBuff(arg_105_0, arg_105_1, arg_105_2):
		assert arg_105_1 and arg_105_2
		arg_105_0.GetGlobalBuff(arg_105_1).AddFloor(arg_105_2)
		arg_105_0.DispatchEvent(EventUpdateGlobalBuff)

	def RemoveBuff(arg_106_0, arg_106_1, arg_106_2):
		assert arg_106_1

		var_106_0 = arg_106_0.GetGlobalBuff(arg_106_1)

		if arg_106_2:
			var_106_0.AddFloor(arg_106_2 * -1)
		else:
			arg_106_0.globalBuffDic[arg_106_1] = None

		arg_106_0.DispatchEvent(EventUpdateGlobalBuff)

	def GetWorldMapBuffLevel(arg_107_0):
		var_107_0 = pg.gameset.world_mapbuff_list.description

		return underscore.map(var_107_0, lambda arg_108_0: arg_107_0.GetGlobalBuff(arg_108_0).floor)

	def GetWorldMapBuffAverageLevel(arg_109_0):
		var_109_0 = arg_109_0.GetWorldMapBuffLevel()
		var_109_1 = 0

		def _function(arg_110_0):
			var_109_1 += arg_110_0

		underscore.each(var_109_0, _function)

		return var_109_1 / len(var_109_0)

	def GetWorldMapBuffs(arg_111_0):
		var_111_0 = pg.gameset.world_mapbuff_list.description

		return underscore.map(var_111_0, lambda arg_112_0: arg_111_0.GetGlobalBuff(arg_112_0))

	def GetWorldMapDifficultyBuffLevel(arg_113_0):
		var_113_0 = arg_113_0.GetActiveMap().config.difficulty

		return pg.gameset.world_difficult_value.description[var_113_0]

	def OnUpdateItem(arg_114_0, arg_114_1, arg_114_2, arg_114_3):
		if arg_114_3.getWorldItemType() == WorldItem.UsageWorldMap and arg_114_0.atlas:
			arg_114_0.atlas.UpdateTreasure(arg_114_3.id)

		arg_114_0.taskProxy.doUpdateTaskByItem(arg_114_3)

	def OnUpdateTask(arg_115_0, arg_115_1, arg_115_2, arg_115_3):
		if arg_115_0.atlas:
			arg_115_0.atlas.UpdateTask(arg_115_3)

	def GetPressingAward(arg_116_0, arg_116_1):
		return arg_116_0.pressingAwardDic[arg_116_1]

	def FlagMapPressingAward(arg_117_0, arg_117_1):
		var_117_0 = arg_117_0.GetPressingAward(arg_117_1)

		if var_117_0:
			var_117_0.flag = False

	def IsMapPressingAwardFlag(arg_118_0, arg_118_1):
		var_118_0 = arg_118_0.GetPressingAward(arg_118_1)

		return var_118_0 and var_118_0.flag == False

	def CheckAreaUnlock(arg_119_0, arg_119_1):
		return arg_119_0.progress >= pg.world_regions_data[arg_119_1].open_stage[1]

	def CheckTaskLockMap(arg_120_0):
		var_120_0 = arg_120_0.taskProxy.getTaskVOs()
		var_120_1 = arg_120_0.GetActiveMap().gid

		def _function(arg_121_0):
			var_121_0 = arg_121_0.config.task_target_map

			return arg_121_0.isAlive() and arg_121_0.IsLockMap() and underscore.any(var_121_0, lambda arg_122_0: arg_122_0 == var_120_1)

		return underscore.any(var_120_0, _function)

	def CheckResetAward(arg_123_0, arg_123_1):
		arg_123_0.resetAward = arg_123_1

		if getProxy(PlayerProxy).getData().getResource(WorldConst.ResourceID) == pg.gameset.world_resource_max.key_value:
			arg_123_0.resetLimitTip = True

	def ClearResetAward(arg_124_0):
		arg_124_0.resetAward = None
		arg_124_0.resetLimitTip = None

	def GetTargetMapPressingCount(arg_125_0, arg_125_1):
		var_125_0 = 0

		for iter_125_0, iter_125_1 in ipairs(arg_125_1):
			if arg_125_0.GetMap(iter_125_1).isPressing:
				var_125_0 = var_125_0 + 1

		return var_125_0

	def ClearAllFleetDefeatEnemies(arg_126_0):
		underscore.each(arg_126_0.GetFleets(), lambda arg_127_0: arg_127_0.ClearDefeatEnemies())

	def GetAreaEntranceIds(arg_128_0, arg_128_1):
		return arg_128_0.atlas.areaEntranceList[arg_128_1]

	def CalcOrderCost(arg_129_0, arg_129_1):
		var_129_0 = 0

		if arg_129_1 == WorldConst.OpReqRedeploy:
			return World.CalcCDTimeCost(pg.gameset.world_fleet_redeploy_cost.description, arg_129_0.GetReqCDTime(WorldConst.OpReqRedeploy), var_129_0)
		elif arg_129_1 == WorldConst.OpReqMaintenance:
			return pg.gameset.world_instruction_maintenance.description[1] * max(10000 - var_129_0, 0) / 10000
		elif arg_129_1 == WorldConst.OpReqSub:
			var_129_1 = arg_129_0.GetSubmarineFleet()

			def _function(arg_130_0):
				var_129_0 += arg_130_0.GetImportWorldShipVO().GetStaminaDiscount(WorldConst.OpReqSub)

			if var_129_1:
				underscore.each(var_129_1.GetShips(True), _function)

			return World.CalcCDTimeCost(pg.gameset.world_instruction_submarine.description, arg_129_0.GetReqCDTime(WorldConst.OpReqSub), var_129_0)
		elif arg_129_1 == WorldConst.OpReqVision:
			return World.CalcCDTimeCost(pg.gameset.world_instruction_detect.description, arg_129_0.GetReqCDTime(WorldConst.OpReqVision), var_129_0)
		else:
			assert False, f"op type error. {arg_129_1}"

	def GetDisplayPressingCount(arg_131_0):
		var_131_0 = 0

		for iter_131_0, iter_131_1 in ipairs(arg_131_0.atlas.pressingMapList):
			if arg_131_0.atlas.GetMap(iter_131_1).CheckMapPressingDisplay():
				var_131_0 = var_131_0 + 1

		return var_131_0

	def CheckCommanderInFleet(arg_132_0, arg_132_1):
		if arg_132_0.type == World.TypeBase:
			return underscore.any(arg_132_0.baseCmdIds, lambda arg_133_0: arg_133_0 == arg_132_1)
		else:
			for iter_132_0, iter_132_1 in ipairs(arg_132_0.fleets):
				if iter_132_1.HasCommander(arg_132_1):
					return True

			return False

	def CheckSkipBattle(arg_134_0):
		return getProxy(PlayerProxy).getRawData().CheckIdentityFlag() and world_skip_battle == 1

	def IsMapVisioned(arg_135_0, arg_135_1):
		var_135_0 = arg_135_0.GetActiveMap()

		if var_135_0.id == arg_135_1:
			var_135_1 = arg_135_0.GetActiveEntrance()
			var_135_2, var_135_3 = ReplacementMapType(var_135_1, var_135_0)

			if var_135_2 == "base_chapter" and var_135_0.isPressing:
				return True
			elif var_135_2 == "teasure_chapter" and var_135_3 == i18n("area_yinmi") and arg_135_0.GetGobalFlag("treasure_flag"):
				return True

		return arg_135_0.IsMapPressingAwardFlag(arg_135_1)

	def HasAutoFightDrops(arg_136_0):
		var_136_0 = arg_136_0.autoInfos

		return len(var_136_0.drops) > 0 or underscore.any(var_136_0.salvage, lambda arg_137_0: len(arg_137_0) > 0) or len(var_136_0.buffs) > 0 or len(var_136_0.message) > 0

	def AddAutoInfo(arg_138_0, arg_138_1, arg_138_2):
		if arg_138_1 == "drops":
			arg_138_0.autoInfos.drops = table.mergeArray(arg_138_0.autoInfos.drops, arg_138_2)
		elif arg_138_1 == "salvage":
			arg_138_0.autoInfos.salvage[arg_138_2.rarity] = table.mergeArray(arg_138_0.autoInfos.salvage[arg_138_2.rarity], arg_138_2.drops)
		elif arg_138_1 == "events":
			table.insert(arg_138_0.autoInfos.events, arg_138_2)
		elif arg_138_1 == "buffs":
			table.insert(arg_138_0.autoInfos.buffs, arg_138_2)
		elif arg_138_1 == "message":
			table.insert(arg_138_0.autoInfos.message, arg_138_2)
		else:
			assert False, f"type error.{arg_138_1}"

	def InitAutoInfos(arg_139_0):
		arg_139_0.autoInfos = table(
			drops = table(),
			salvage = table(
				table(),
				table(),
				table()
			),
			buffs = table(),
			message = table()
		)

	def TriggerAutoFight(arg_140_0, arg_140_1):
		arg_140_1 = arg_140_1 and arg_140_0.GetActiveMap().CanAutoFight()

		if bool(arg_140_1) != bool(arg_140_0.isAutoFight):
			arg_140_0.isAutoFight = arg_140_1

			pg.BrightnessMgr.GetInstance().SetScreenNeverSleep(arg_140_1)

			if arg_140_1:
				if not LOCK_BATTERY_SAVEMODE and PlayerPrefs.GetInt(AUTOFIGHT_BATTERY_SAVEMODE, 0) == 1 and pg.BrightnessMgr.GetInstance().IsPermissionGranted():
					pg.BrightnessMgr.GetInstance().EnterManualMode()

					if PlayerPrefs.GetInt(AUTOFIGHT_DOWN_FRAME, 0) == 1:
						getProxy(SettingsProxy).RecordFrameRate()

						Application.targetFrameRate = 30
			elif not LOCK_BATTERY_SAVEMODE:
				pg.BrightnessMgr.GetInstance().ExitManualMode()
				getProxy(SettingsProxy).RestoreFrameRate()

			pg.m02.sendNotification(GAME.WORLD_TRIGGER_AUTO_FIGHT)

		if not arg_140_1:
			arg_140_0.TriggerAutoSwitch(False)

	def TriggerAutoSwitch(arg_141_0, arg_141_1):
		if bool(arg_141_1) != bool(arg_141_0.isAutoSwitch):
			arg_141_0.isAutoSwitch = arg_141_1

			pg.m02.sendNotification(GAME.WORLD_TRIGGER_AUTO_SWITCH)

	def GetHistoryLowestHP(arg_142_0, arg_142_1):
		return arg_142_0.lowestHP[arg_142_1] or 10000

	def SetHistoryLowestHP(arg_143_0, arg_143_1, arg_143_2):
		arg_143_0.lowestHP[arg_143_1] = arg_143_2

	def SetGlobalFlag(arg_144_0, arg_144_1, arg_144_2):
		arg_144_0.gobalFlag[var_0_2[arg_144_1]] = arg_144_2

	def GetGobalFlag(arg_145_0, arg_145_1):
		return arg_145_0.gobalFlag[var_0_2[arg_145_1]]
