from luatable import table, pairs, ipairs, Clone
from Vector3 import Vector3
from alsupport import math

from Framework.tolua.tolua import PlayerPrefs #!
from Framework import underscore
from luaex import GodenFnger

from const import *
from Framework.base.mvc import proxy

from .. import BattleEvent
import BattleFormulas
import BattleConst
import BattleConfig
import BattleDataFunction
import BattleAttr
import BattleVariable
from data.buff import BattleBuffUnit
from .. import BattleCardPuzzleEvent
from model.const import ChapterConst, ShipType, TeamType
from Framework.event import Event
from mgr import TimeMgr
from mgr.sdk import SdkMgr
from support.helpers.UnitySupport import onDelayTick
from localConfig import BATTLE_ENEMY_AIMBIAS_RANGE
from data.vo import BattleCldSystem
from view.camera import BattleCameraUtil
from unit.unitstatemachine import UnitState
from vo import BattleFleetVO, BattleUnitPhaseSwitcher, BattleTeamVO
from buff.buffeffect import BattleBuffSetBattleUnitType
from bullet import BattleShrapnelBulletUnit
from aircraft import BattleAirFighterUnit
from sceneobj import BattleLastingAOEData, BattleShelterData, BattleAOEData, BattleWallData, BattleTriggerAOEData
from environment import BattleEnvironmentUnit


class BattleDataProxy(proxy):
	def __new__(cls):
		it = cls.__dict__.get("__it__")
		if it is not None:
			return it
		cls.__it__ = it = super().__new__(cls)
		return it

	__name = "BattleDataProxy"

	def InitBattle(self, arg_2_1):
		self.Update = self.updateInit

		var_2_0 = arg_2_1.battleType
		var_2_1 = var_2_0 == SYSTEM_WORLD or var_2_0 == SYSTEM_WORLD_BOSS
		var_2_2 = SdkMgr.GetInstance().CheckPretest() and (PlayerPrefs.GetInt("stage_scratch") or 0) == 1

		self.SetupCalculateDamage(var_2_2 and GodenFnger or BattleFormulas.CreateContextCalculateDamage(var_2_1))
		self.SetupDamageKamikazeAir()
		self.SetupDamageKamikazeShip()
		self.SetupDamageCrush()
		BattleVariable.Init()
		self.InitData(arg_2_1)
		self.DispatchEvent(Event.New(BattleEvent.STAGE_DATA_INIT_FINISH))
		self._cameraUtil.Initialize()

		self._cameraTop, self._cameraBottom, self._cameraLeft, self._cameraRight = self._cameraUtil.SetMapData(self.GetTotalBounds())

		self.InitWeatherData()
		self.InitUserShipsData(self._battleInitData.MainUnitList, self._battleInitData.VanguardUnitList, BattleConfig.FRIENDLY_CODE, self._battleInitData.SubUnitList)
		self.InitUserSupportShipsData(BattleConfig.FRIENDLY_CODE, self._battleInitData.SupportUnitList)
		self.InitUserAidData()
		self.SetSubmarinAidData()
		self._cameraUtil.SetFocusFleet(self.GetFleetByIFF(BattleConfig.FRIENDLY_CODE))
		self.StatisticsInit(self._fleetList[BattleConfig.FRIENDLY_CODE].GetUnitList())
		self.SetFlagShipID(self.GetFleetByIFF(BattleConfig.FRIENDLY_CODE).GetFlagShip())
		self.DispatchEvent(Event.New(BattleEvent.COMMON_DATA_INIT_FINISH, table()))

	def OnCameraRatioUpdate(self):
		self._cameraTop, self._cameraBottom, self._cameraLeft, self._cameraRight = self._cameraUtil.SetMapData(self.GetTotalBounds())

		self._cameraUtil.setArrowPoint()

	def Start(arg_4_0):
		arg_4_0._startTimeStamp = TimeMgr.GetInstance().GetCombatTime()

	def TriggerBattleInitBuffs(self):
		for iter_5_0, iter_5_1 in pairs(self._fleetList):
			var_5_0 = iter_5_1.GetUnitList()

			iter_5_1.FleetBuffTrigger(BattleConst.BuffEffectType.ON_INIT_GAME)

	def TirggerBattleStartBuffs(self):
		for iter_6_0, iter_6_1 in pairs(self._fleetList):
			var_6_0 = iter_6_1.GetUnitList()
			var_6_1 = iter_6_1.GetScoutList()
			var_6_2 = var_6_1[1]
			var_6_3 = len(var_6_1) > 1 and var_6_1[len(var_6_1)-1] or None
			var_6_4 = len(var_6_1) == 3 and var_6_1[2] or None
			var_6_5 = iter_6_1.GetMainList()
			var_6_6 = var_6_5[1]
			var_6_7 = var_6_5[2]
			var_6_8 = var_6_5[3]

			for iter_6_2, iter_6_3 in ipairs(var_6_0):
				underscore.each(self._battleInitData.ChapterBuffIDs or table(), lambda arg_7_0: iter_6_3.AddBuff(BattleBuffUnit.New(arg_7_0)))
				underscore.each(self._battleInitData.GlobalBuffIDs or table(),  lambda arg_8_0: iter_6_3.AddBuff(BattleBuffUnit.New(int(arg_8_0))))

				if self._battleInitData.MapAuraSkills:
					for iter_6_4, iter_6_5 in ipairs(self._battleInitData.MapAuraSkills):
						var_6_9 = BattleBuffUnit.New(iter_6_5.id, iter_6_5.level)

						iter_6_3.AddBuff(var_6_9)

				if self._battleInitData.MapAidSkills:
					for iter_6_6, iter_6_7 in ipairs(self._battleInitData.MapAidSkills):
						var_6_10 = BattleBuffUnit.New(iter_6_7.id, iter_6_7.level)

						iter_6_3.AddBuff(var_6_10)

				if self._currentStageData.stageBuff:
					for iter_6_8, iter_6_9 in ipairs(self._currentStageData.stageBuff):
						var_6_11 = BattleBuffUnit.New(iter_6_9.id, iter_6_9.level)

						iter_6_3.AddBuff(var_6_11)

				iter_6_3.TriggerBuff(BattleConst.BuffEffectType.ON_START_GAME)

				if iter_6_3 == var_6_6:
					iter_6_3.TriggerBuff(BattleConst.BuffEffectType.ON_FLAG_SHIP)
				elif iter_6_3 == var_6_7:
					iter_6_3.TriggerBuff(BattleConst.BuffEffectType.ON_UPPER_CONSORT)
				elif iter_6_3 == var_6_8:
					iter_6_3.TriggerBuff(BattleConst.BuffEffectType.ON_LOWER_CONSORT)
				elif iter_6_3 == var_6_2:
					iter_6_3.TriggerBuff(BattleConst.BuffEffectType.ON_LEADER)
				elif iter_6_3 == var_6_4:
					iter_6_3.TriggerBuff(BattleConst.BuffEffectType.ON_CENTER)
				elif iter_6_3 == var_6_3:
					iter_6_3.TriggerBuff(BattleConst.BuffEffectType.ON_REAR)

			var_6_12 = iter_6_1.GetSupportUnitList()

			for iter_6_10, iter_6_11 in ipairs(var_6_12):
				def helper(arg_9_0):
					if BattleDataFunction.GetSLGStrategyBuffByCombatBuffID(arg_9_0).type == ChapterConst.AirDominanceStrategyBuffType:
						var_9_0 = BattleBuffUnit.New(arg_9_0)

						iter_6_11.AddBuff(var_9_0)
				underscore.each(self._battleInitData.ChapterBuffIDs or table(), helper)

	def InitAllFleetUnitsWeaponCD(self):
		for iter_10_0, iter_10_1 in pairs(self._fleetList):
			var_10_0 = iter_10_1.GetUnitList()

			for iter_10_2, iter_10_3 in ipairs(var_10_0):
				self.InitUnitWeaponCD(iter_10_3)

	def InitUnitWeaponCD(self):
		self.CheckWeaponInitial()

	def StartCardPuzzle(self):
		for iter_12_0, iter_12_1 in pairs(self._fleetList):
			iter_12_1.GetCardPuzzleComponent().Start()

	def PausePuzzleComponent(self):
		for iter_13_0, iter_13_1 in pairs(self._fleetList):
			var_13_0 = iter_13_1.GetCardPuzzleComponent()

			if var_13_0:
				var_13_0.BlockComponentByCard(True)

	def ResumePuzzleComponent(self):
		def helper():
			for iter_15_0, iter_15_1 in pairs(self._fleetList):
				var_15_0 = iter_15_1.GetCardPuzzleComponent()

				if var_15_0:
					var_15_0.BlockComponentByCard(False), 0.06
		onDelayTick(helper)

	def GetInitData(sefl):
		return sefl._battleInitData

	def GetDungeonData(self):
		return self._dungeonInfo

	def InitData(self, arg_18_1):
		self.FrameIndex = 1
		self._friendlyCode = 1
		self._foeCode = -1
		BattleConst.FRIENDLY_CODE = 1
		BattleConst.FOE_CODE = -1
		self._completelyRepress = False
		self._repressReduce = 1
		self._repressLevel = 0
		self._repressEnemyHpRant = 1
		self._friendlyShipList = table()
		self._foeShipList = table()
		self._friendlyAircraftList = table()
		self._foeAircraftList = table()
		self._minionShipList = table()
		self._spectreShipList = table()
		self._fleetList = table()
		self._freeShipList = table()
		self._teamList = table()
		self._waveSummonList = table()
		self._aidUnitList = table()
		self._unitList = table()
		self._unitCount = 0
		self._bulletList = table()
		self._bulletCount = 0
		self._aircraftList = table()
		self._aircraftCount = 0
		self._AOEList = table()
		self._AOECount = 0
		self._wallList = table()
		self._wallIndex = 0
		self._shelterList = table()
		self._shelterIndex = 0
		self._environmentList = table()
		self._environmentIndex = 0
		self._deadUnitList = table()
		self._enemySubmarineCount = 0
		self._airFighterList = table()
		self._currentStageIndex = 1
		self._battleInitData = arg_18_1
		self._expeditionID = arg_18_1.StageTmpId
		self._expeditionTmp = expedition_data_template[self._expeditionID] #use api

		self.SetDungeonLevel(arg_18_1.WorldLevel or self._expeditionTmp.level)

		self._dungeonID = self._expeditionTmp.dungeon_id
		self._dungeonInfo = BattleDataFunction.GetDungeonTmpDataByID(self._dungeonID)

		if arg_18_1.WorldMapId:
			self._mapId = arg_18_1.WorldMapId
		elif self._expeditionTmp.map_id:
			var_18_0 = self._expeditionTmp.map_id

			if len(var_18_0) == 1:
				self._mapId = var_18_0[1][1]
			else:
				var_18_1 = table()

				for iter_18_0, iter_18_1 in ipairs(var_18_0):
					var_18_2 = iter_18_1[2] * 100

					table.insert(var_18_1, table(
						rst = iter_18_1[1],
						weight = var_18_2
					))

				self._mapId = BattleFormulas.WeightRandom(var_18_1)

		self._weahter = arg_18_1.ChapterWeatherIDS or table()
		self._exposeSpeed = self._expeditionTmp.expose_speed
		self._airExpose = self._expeditionTmp.aircraft_expose[1]
		self._airExposeEX = self._expeditionTmp.aircraft_expose[2]
		self._shipExpose = self._expeditionTmp.ship_expose[1]
		self._shipExposeEX = self._expeditionTmp.ship_expose[2]
		self._commander = arg_18_1.CommanderList or table()
		self._subCommander = arg_18_1.SubCommanderList or table()
		self._commanderBuff = self.initCommanderBuff(self._commander)
		self._subCommanderBuff = self.initCommanderBuff(self._subCommander)

		if self._battleInitData.RepressInfo:
			var_18_3 = self._battleInitData.RepressInfo

			if self._battleInitData.battleType == SYSTEM_SCENARIO:
				if var_18_3.repressCount >= var_18_3.repressMax:
					self._completelyRepress = True

				self._repressReduce = BattleFormulas.ChapterRepressReduce(var_18_3.repressReduce)
				self._repressLevel = var_18_3.repressLevel
				self._repressEnemyHpRant = var_18_3.repressEnemyHpRant
			elif self._battleInitData.battleType == SYSTEM_WORLD or self._battleInitData.battleType == SYSTEM_WORLD_BOSS:
				self._repressEnemyHpRant = var_18_3.repressEnemyHpRant

		self._chapterWinningStreak = self._battleInitData.DefeatCount or 0
		self._waveFlags = table.shallowCopy(arg_18_1.StageWaveFlags) or table()

		self.InitStageData()

		self._cldSystem = BattleCldSystem.New(self)
		self._cameraUtil = BattleCameraUtil.GetInstance()

		self.initBGM()

	def initBGM(arg_19_0):
		arg_19_0._initBGMList = table()
		arg_19_0._otherBGMList = table()

		var_19_0 = table()
		var_19_1 = table()

		def var_19_2(arg_20_0):
			for iter_20_0, iter_20_1 in ipairs(arg_20_0):
				var_20_0 = table()

				if iter_20_1.skills:
					for iter_20_2, iter_20_3 in ipairs(iter_20_1.skills):
						table.insert(var_20_0, iter_20_3)

				if iter_20_1.equipment:
					var_20_1 = BattleDataFunction.GetEquipSkill(iter_20_1.equipment, arg_19_0._battleInitData.battleType)

					for iter_20_4, iter_20_5 in ipairs(var_20_1):
						var_20_0[iter_20_5] = table(
							level = 1,
							id = iter_20_5
						)

				var_20_2 = BattleDataFunction.GetSongList(var_20_0)

				for iter_20_6, iter_20_7 in pairs(var_20_2.initList):
					var_19_0[iter_20_6] = True

				for iter_20_8, iter_20_9 in pairs(var_20_2.otherList):
					var_19_1[iter_20_8] = True

		var_19_2(arg_19_0._battleInitData.MainUnitList)
		var_19_2(arg_19_0._battleInitData.VanguardUnitList)
		var_19_2(arg_19_0._battleInitData.SubUnitList)

		if arg_19_0._battleInitData.RivalMainUnitList:
			var_19_2(arg_19_0._battleInitData.RivalMainUnitList)

		if arg_19_0._battleInitData.RivalVanguardUnitList:
			var_19_2(arg_19_0._battleInitData.RivalVanguardUnitList)

		for iter_19_0, iter_19_1 in pairs(var_19_0):
			table.insert(arg_19_0._initBGMList, iter_19_0)

		for iter_19_2, iter_19_3 in pairs(var_19_1):
			table.insert(arg_19_0._otherBGMList, iter_19_2)

	def initCommanderBuff(arg_21_0):
		var_21_0 = table()

		for iter_21_0, iter_21_1 in ipairs(arg_21_0):
			var_21_1 = iter_21_1[1]
			var_21_2 = var_21_1.getSkills()[1].getLevel()

			for iter_21_2, iter_21_3 in ipairs(iter_21_1[2]):
				table.insert(var_21_0, table(
					id = iter_21_3,
					level = var_21_2,
					commander = var_21_1
				))

		return var_21_0

	def Clear(arg_22_0):
		for iter_22_0, iter_22_1 in pairs(arg_22_0._teamList):
			arg_22_0.KillNPCTeam(iter_22_1)

		arg_22_0._teamList = None

		for iter_22_2, iter_22_3 in pairs(arg_22_0._bulletList):
			arg_22_0.RemoveBulletUnit(iter_22_2)

		arg_22_0._bulletList = None

		for iter_22_4, iter_22_5 in pairs(arg_22_0._unitList):
			arg_22_0.KillUnit(iter_22_4)

		arg_22_0._unitList = None

		for iter_22_6, iter_22_7 in ipairs(arg_22_0._deadUnitList):
			iter_22_7.Dispose()

		arg_22_0._deadUnitList = None

		for iter_22_8, iter_22_9 in pairs(arg_22_0._aircraftList):
			arg_22_0.KillAircraft(iter_22_8)

		arg_22_0._aircraftList = None

		for iter_22_10, iter_22_11 in pairs(arg_22_0._fleetList):
			iter_22_11.Dispose()

			arg_22_0._fleetList[iter_22_10] = None

		arg_22_0._fleetList = None

		for iter_22_12, iter_22_13 in pairs(arg_22_0._aidUnitList):
			iter_22_13.Dispose()

		arg_22_0._aidUnitList = None

		for iter_22_14, iter_22_15 in pairs(arg_22_0._environmentList):
			arg_22_0.RemoveEnvironment(iter_22_15.GetUniqueID())

		arg_22_0._environmentList = None

		for iter_22_16, iter_22_17 in pairs(arg_22_0._AOEList):
			arg_22_0.RemoveAreaOfEffect(iter_22_16)

		arg_22_0._AOEList = None

		arg_22_0._cldSystem.Dispose()

		arg_22_0._cldSystem = None
		arg_22_0._dungeonInfo = None
		arg_22_0._flagShipUnit = None
		arg_22_0._friendlyShipList = None
		arg_22_0._foeShipList = None
		arg_22_0._spectreShipList = None
		arg_22_0._friendlyAircraftList = None
		arg_22_0._foeAircraftList = None
		arg_22_0._fleetList = None
		arg_22_0._freeShipList = None
		arg_22_0._countDown = None
		arg_22_0._lastUpdateTime = None
		arg_22_0._statistics = None
		arg_22_0._battleInitData = None
		arg_22_0._currentStageData = None

		arg_22_0.ClearFormulas()
		BattleDataFunction.ClearDungeonCfg(arg_22_0._dungeonID)

	def DeactiveProxy(arg_23_0):
		arg_23_0._state = None

		arg_23_0.Clear()
		BattleDataProxy.super.DeactiveProxy(arg_23_0)

	def InitUserShipsData(arg_24_0, arg_24_1, arg_24_2, arg_24_3, arg_24_4):
		for iter_24_0, iter_24_1 in ipairs(arg_24_2):
			var_24_0 = arg_24_0.SpawnVanguard(iter_24_1, arg_24_3)

		for iter_24_2, iter_24_3 in ipairs(arg_24_1):
			var_24_1 = arg_24_0.SpawnMain(iter_24_3, arg_24_3)

		var_24_2 = arg_24_0.GetFleetByIFF(arg_24_3)

		var_24_2.FleetUnitSpwanFinish()

		var_24_3 = arg_24_0._battleInitData.battleType

		if var_24_3 == SYSTEM_SUBMARINE_RUN or var_24_3 == SYSTEM_SUB_ROUTINE:
			for iter_24_4, iter_24_5 in ipairs(arg_24_4):
				arg_24_0.SpawnManualSub(iter_24_5, arg_24_3)

			var_24_2.ShiftManualSub()
		else:
			var_24_2.SetSubUnitData(arg_24_4)

		if arg_24_0._battleInitData.battleType == SYSTEM_DUEL:
			for iter_24_6, iter_24_7 in ipairs(var_24_2.GetCloakList()):
				iter_24_7.GetCloak().SetRecoverySpeed(0)

		arg_24_0.DispatchEvent(Event.New(BattleEvent.ADD_FLEET, table(
			fleetVO = var_24_2
		)))

	def InitUserSupportShipsData(arg_25_0, arg_25_1, arg_25_2):
		var_25_0 = arg_25_0.GetFleetByIFF(arg_25_1)

		for iter_25_0, iter_25_1 in ipairs(arg_25_2):
			var_25_1 = arg_25_0.SpawnSupportUnit(iter_25_1, arg_25_1)

	def InitUserAidData(arg_26_0):
		for iter_26_0, iter_26_1 in ipairs(arg_26_0._battleInitData.AidUnitList):
			var_26_0 = arg_26_0.GenerateUnitID()
			var_26_1 = iter_26_1.properties

			var_26_1.level = iter_26_1.level
			var_26_1.formationID = BattleConfig.FORMATION_ID
			var_26_1.id = iter_26_1.id

			BattleFormulas.AttrFixer(arg_26_0._battleInitData.battleType, var_26_1)

			var_26_2 = iter_26_1.proficiency or table(
				1,
				1,
				1
			)
			var_26_3 = BattleDataFunction.CreateBattleUnitData(var_26_0, BattleConst.UnitType.PLAYER_UNIT, BattleConfig.FRIENDLY_CODE, iter_26_1.tmpID, iter_26_1.skinId, iter_26_1.equipment, var_26_1, iter_26_1.baseProperties, var_26_2, iter_26_1.baseList, iter_26_1.preloasList)

			arg_26_0._aidUnitList[var_26_3.GetUniqueID()] = var_26_3

	def SetSubmarinAidData(arg_27_0):
		arg_27_0.GetFleetByIFF(BattleConfig.FRIENDLY_CODE).SetSubAidData(arg_27_0._battleInitData.TotalSubAmmo, arg_27_0._battleInitData.SubFlag)

	def AddWeather(arg_28_0, arg_28_1):
		table.insert(arg_28_0._weahter, arg_28_1)
		arg_28_0.InitWeatherData()

	def InitWeatherData(arg_29_0):
		for iter_29_0, iter_29_1 in ipairs(arg_29_0._weahter):
			if iter_29_1 == BattleConst.WEATHER.NIGHT:
				for iter_29_2, iter_29_3 in pairs(arg_29_0._fleetList):
					iter_29_3.AttachNightCloak()

				for iter_29_4, iter_29_5 in pairs(arg_29_0._unitList):
					BattleDataFunction.AttachWeather(iter_29_5, arg_29_0._weahter)

	def CelebrateVictory(arg_30_0, arg_30_1):
		var_30_0

		if arg_30_1 == arg_30_0.GetFoeCode():
			var_30_0 = arg_30_0._foeShipList
		else:
			var_30_0 = arg_30_0._friendlyShipList

		for iter_30_0, iter_30_1 in pairs(var_30_0):
			iter_30_1.StateChange(UnitState.STATE_VICTORY)

	def InitStageData(arg_31_0):
		arg_31_0._currentStageData = arg_31_0._dungeonInfo.stages[arg_31_0._currentStageIndex]
		arg_31_0._countDown = arg_31_0._currentStageData.timeCount

		var_31_0 = arg_31_0._currentStageData.totalArea

		arg_31_0._totalLeftBound = var_31_0[1]
		arg_31_0._totalRightBound = var_31_0[1] + var_31_0[3]
		arg_31_0._totalUpperBound = var_31_0[2] + var_31_0[4]
		arg_31_0._totalLowerBound = var_31_0[2]

		var_31_1 = arg_31_0._currentStageData.playerArea

		arg_31_0._leftZoneLeftBound = var_31_1[1]
		arg_31_0._leftZoneRightBound = var_31_1[1] + var_31_1[3]
		arg_31_0._leftZoneUpperBound = var_31_1[2] + var_31_1[4]
		arg_31_0._leftZoneLowerBound = var_31_1[2]
		arg_31_0._rightZoneLeftBound = arg_31_0._leftZoneRightBound
		arg_31_0._rightZoneRightBound = arg_31_0._totalRightBound
		arg_31_0._rightZoneUpperBound = arg_31_0._leftZoneUpperBound
		arg_31_0._rightZoneLowerBound = arg_31_0._leftZoneLowerBound
		arg_31_0._bulletUpperBound = arg_31_0._totalUpperBound + 3
		arg_31_0._bulletLowerBound = arg_31_0._totalLowerBound - 10
		arg_31_0._bulletLeftBound = arg_31_0._totalLeftBound - 10
		arg_31_0._bulletRightBound = arg_31_0._totalRightBound + 10
		arg_31_0._bulletUpperBoundVision = arg_31_0._totalUpperBound + BattleConfig.BULLET_UPPER_BOUND_VISION_OFFSET
		arg_31_0._bulletLowerBoundSplit = arg_31_0._bulletLowerBound + BattleConfig.BULLET_LOWER_BOUND_SPLIT_OFFSET
		arg_31_0._bulletLeftBoundSplit = arg_31_0._bulletLeftBound + BattleConfig.BULLET_LEFT_BOUND_SPLIT_OFFSET

		if arg_31_0._battleInitData.battleType == SYSTEM_DUEL:
			arg_31_0._leftFieldBound = arg_31_0._totalLeftBound
			arg_31_0._rightFieldBound = arg_31_0._totalRightBound
		else:
			var_31_2

			if arg_31_0._currentStageData.mainUnitPosition and arg_31_0._currentStageData.mainUnitPosition[BattleConfig.FRIENDLY_CODE]:
				var_31_2 = arg_31_0._currentStageData.mainUnitPosition[BattleConfig.FRIENDLY_CODE][1].x
			else:
				var_31_2 = BattleConfig.MAIN_UNIT_POS[BattleConfig.FRIENDLY_CODE][1].x

			arg_31_0._leftFieldBound = var_31_2 - 1
			arg_31_0._rightFieldBound = arg_31_0._totalRightBound + BattleConfig.FIELD_RIGHT_BOUND_BIAS

	def GetVanguardBornCoordinate(arg_32_0, arg_32_1):
		if arg_32_1 == BattleConfig.FRIENDLY_CODE:
			return arg_32_0._currentStageData.fleetCorrdinate
		elif arg_32_1 == BattleConfig.FOE_CODE:
			return arg_32_0._currentStageData.rivalCorrdinate

	def GetTotalBounds(arg_33_0):
		return arg_33_0._totalUpperBound, arg_33_0._totalLowerBound, arg_33_0._totalLeftBound, arg_33_0._totalRightBound

	def GetTotalRightBound(arg_34_0):
		return arg_34_0._totalRightBound

	def GetTotalLowerBound(arg_35_0):
		return arg_35_0._totalLowerBound

	def GetUnitBoundByIFF(arg_36_0, arg_36_1):
		if arg_36_1 == BattleConfig.FRIENDLY_CODE:
			return arg_36_0._leftZoneUpperBound, arg_36_0._leftZoneLowerBound, arg_36_0._leftZoneLeftBound, BattleConfig.MaxRight, BattleConfig.MaxLeft, arg_36_0._leftZoneRightBound
		elif arg_36_1 == BattleConfig.FOE_CODE:
			return arg_36_0._rightZoneUpperBound, arg_36_0._rightZoneLowerBound, arg_36_0._rightZoneLeftBound, arg_36_0._rightZoneRightBound, arg_36_0._rightZoneLeftBound, BattleConfig.MaxRight

	def GetFleetBoundByIFF(arg_37_0, arg_37_1):
		if arg_37_1 == BattleConfig.FRIENDLY_CODE:
			return arg_37_0._leftZoneUpperBound, arg_37_0._leftZoneLowerBound, arg_37_0._leftZoneLeftBound, arg_37_0._leftZoneRightBound
		elif arg_37_1 == BattleConfig.FOE_CODE:
			return arg_37_0._rightZoneUpperBound, arg_37_0._rightZoneLowerBound, arg_37_0._rightZoneLeftBound, arg_37_0._rightZoneRightBound

	def ShiftFleetBound(arg_38_0, arg_38_1, arg_38_2):
		arg_38_1.GetUnitBound().SwtichDuelAggressive()
		arg_38_1.SetAutobotBound(arg_38_0.GetFleetBoundByIFF(arg_38_2))
		arg_38_1.UpdateScoutUnitBound()

	def GetFieldBound(arg_39_0):
		if arg_39_0._battleInitData and arg_39_0._battleInitData.battleType == SYSTEM_DUEL:
			return arg_39_0.GetTotalBounds()
		else:
			return arg_39_0._totalUpperBound, arg_39_0._totalLowerBound, arg_39_0._leftFieldBound, arg_39_0._rightFieldBound

	def GetFleetByIFF(arg_40_0, arg_40_1):
		if arg_40_0._fleetList[arg_40_1] == None:
			var_40_0 = BattleFleetVO.New(arg_40_1)

			arg_40_0._fleetList[arg_40_1] = var_40_0

			var_40_0.SetAutobotBound(arg_40_0.GetFleetBoundByIFF(arg_40_1))
			var_40_0.SetTotalBound(arg_40_0.GetTotalBounds())
			var_40_0.SetUnitBound(arg_40_0._currentStageData.totalArea, arg_40_0._currentStageData.playerArea)
			var_40_0.SetExposeLine(arg_40_0._expeditionTmp.horizon_line[arg_40_1], arg_40_0._expeditionTmp.expose_line[arg_40_1])
			var_40_0.CalcSubmarineBaseLine(arg_40_0._battleInitData.battleType)

			if arg_40_0._battleInitData.battleType == SYSTEM_CARDPUZZLE:
				var_40_1 = var_40_0.AttachCardPuzzleComponent()
				var_40_2 = table(
					cardList = arg_40_0._battleInitData.CardPuzzleCardIDList,
					commonHP = arg_40_0._battleInitData.CardPuzzleCommonHPValue,
					relicList = arg_40_0._battleInitData.CardPuzzleRelicList
				)

				var_40_1.InitCardPuzzleData(var_40_2)
				var_40_1.CustomConfigID(arg_40_0._battleInitData.CardPuzzleCombatID)
				arg_40_0.DispatchEvent(Event.New(BattleCardPuzzleEvent.CARD_PUZZLE_INIT))

		return arg_40_0._fleetList[arg_40_1]

	def GetAidUnit(arg_41_0):
		return arg_41_0._aidUnitList

	def GetFleetList(arg_42_0):
		return arg_42_0._fleetList

	def GetEnemySubmarineCount(arg_43_0):
		return arg_43_0._enemySubmarineCount

	def GetCommander(arg_44_0):
		return arg_44_0._commander

	def GetCommanderBuff(arg_45_0):
		return arg_45_0._commanderBuff, arg_45_0._subCommanderBuff

	def GetStageInfo(arg_46_0):
		return arg_46_0._currentStageData

	def GetWinningStreak(arg_47_0):
		return arg_47_0._chapterWinningStreak

	def GetBGMList(arg_48_0, arg_48_1):
		if not arg_48_1:
			return arg_48_0._initBGMList
		else:
			return arg_48_0._otherBGMList

	def GetDungeonLevel(arg_49_0):
		return arg_49_0._dungeonLevel

	def SetDungeonLevel(arg_50_0, arg_50_1):
		arg_50_0._dungeonLevel = arg_50_1

	def IsCompletelyRepress(arg_51_0):
		return arg_51_0._completelyRepress

	def GetRepressReduce(arg_52_0):
		return arg_52_0._repressReduce

	def GetRepressLevel(arg_53_0):
		return arg_53_0._repressLevel

	def updateInit(arg_54_0, arg_54_1):
		arg_54_0.TriggerBattleInitBuffs()

		arg_54_0.checkCld = True

		arg_54_0.updateLoop(arg_54_1)

		arg_54_0.Update = arg_54_0.updateLoop

	def updateLoop(arg_55_0, arg_55_1):
		arg_55_0.FrameIndex = arg_55_0.FrameIndex + 1

		arg_55_0.updateDeadList()
		arg_55_0.UpdateCountDown(arg_55_1)
		arg_55_0.UpdateWeather(arg_55_1)

		for iter_55_0, iter_55_1 in pairs(arg_55_0._fleetList):
			iter_55_1.UpdateMotion()

		arg_55_0.checkCld = not arg_55_0.checkCld

		var_55_0 = table({
			BattleConfig.FRIENDLY_CODE: arg_55_0._totalLeftBound,
			BattleConfig.FOE_CODE: arg_55_0._totalRightBound
		})

		for iter_55_2, iter_55_3 in pairs(arg_55_0._unitList):
			if iter_55_3.IsSpectre():
				if iter_55_3.GetAttrByName(BattleBuffSetBattleUnitType.ATTR_KEY) <= BattleConfig.FUSION_ELEMENT_UNIT_TYPE:
					pass #block empty
				else:
					iter_55_3.Update(arg_55_1)
			else:
				if arg_55_0.checkCld:
					arg_55_0._cldSystem.UpdateShipCldTree(iter_55_3)

				if iter_55_3.IsAlive():
					iter_55_3.Update(arg_55_1)

				var_55_1 = iter_55_3.GetPosition().x
				var_55_2 = iter_55_3.GetIFF()

				if var_55_2 == BattleConfig.FRIENDLY_CODE:
					var_55_0[var_55_2] = max(var_55_0[var_55_2], var_55_1)
				elif var_55_2 == BattleConfig.FOE_CODE:
					var_55_0[var_55_2] = min(var_55_0[var_55_2], var_55_1)

		var_55_3 = arg_55_0._fleetList[BattleConfig.FRIENDLY_CODE]
		var_55_4 = var_55_3.GetFleetExposeLine()
		var_55_5 = var_55_3.GetFleetVisionLine()
		var_55_6 = var_55_0[BattleConfig.FOE_CODE]

		if var_55_4 and var_55_6 < var_55_4:
			var_55_3.CloakFatalExpose()
		elif var_55_6 < var_55_5:
			var_55_3.CloakInVision(arg_55_0._exposeSpeed)
		else:
			var_55_3.CloakOutVision()

		if arg_55_0._fleetList[BattleConfig.FOE_CODE]:
			var_55_7 = arg_55_0._fleetList[BattleConfig.FOE_CODE]
			var_55_8 = var_55_7.GetFleetExposeLine()
			var_55_9 = var_55_7.GetFleetVisionLine()
			var_55_10 = var_55_0[BattleConfig.FRIENDLY_CODE]

			if var_55_8 and var_55_8 < var_55_10:
				var_55_7.CloakFatalExpose()
			elif var_55_9 < var_55_10:
				var_55_7.CloakInVision(arg_55_0._exposeSpeed)
			else:
				var_55_7.CloakOutVision()

		for iter_55_4, iter_55_5 in pairs(arg_55_0._bulletList):
			var_55_11 = iter_55_5.GetSpeed()
			var_55_12 = iter_55_5.GetPosition()
			var_55_13 = iter_55_5.GetType()
			var_55_14 = iter_55_5.GetOutBound()

			if var_55_14 == BattleConst.BulletOutBound.SPLIT and var_55_13 == BattleConst.BulletType.SHRAPNEL and (var_55_12.x > arg_55_0._bulletRightBound and var_55_11.x > 0 or var_55_12.x < arg_55_0._bulletLeftBoundSplit and var_55_11.x < 0 or var_55_12.z > arg_55_0._bulletUpperBound and var_55_11.z > 0 or var_55_12.z < arg_55_0._bulletLowerBoundSplit and var_55_11.z < 0):
				if iter_55_5.GetExist():
					iter_55_5.OutRange()
				else:
					arg_55_0.RemoveBulletUnit(iter_55_5.GetUniqueID())
			elif var_55_14 == BattleConst.BulletOutBound.COMMON and (var_55_12.x > arg_55_0._bulletRightBound and var_55_11.x > 0 or var_55_12.z < arg_55_0._bulletLowerBound and var_55_11.z < 0):
				arg_55_0.RemoveBulletUnit(iter_55_5.GetUniqueID())
			elif var_55_12.x < arg_55_0._bulletLeftBound and var_55_11.x < 0 and var_55_13 != BattleConst.BulletType.BOMB:
				if var_55_14 == BattleConst.BulletOutBound.RANDOM:
					var_55_15 = arg_55_0._fleetList[BattleConfig.FRIENDLY_CODE].RandomMainVictim()

					if var_55_15:
						arg_55_0.HandleDamage(iter_55_5, var_55_15)

				arg_55_0.RemoveBulletUnit(iter_55_5.GetUniqueID())
			else:
				iter_55_5.Update(arg_55_1)

				var_55_16 = iter_55_5.GetCurrentState and iter_55_5.GetCurrentState() or None

				if var_55_16 == BattleShrapnelBulletUnit.STATE_FINAL_SPLIT:
					pass #block empty
				elif var_55_16 == BattleShrapnelBulletUnit.STATE_SPLIT and not iter_55_5.IsFragile():
					pass #block empty
				elif var_55_14 == BattleConst.BulletOutBound.COMMON and var_55_12.z > arg_55_0._bulletUpperBound and var_55_11.z > 0 or var_55_14 == BattleConst.BulletOutBound.VISION and var_55_12.z > arg_55_0._bulletUpperBoundVision and var_55_11.z > 0 or iter_55_5.IsOutRange(arg_55_1):
					if iter_55_5.GetExist():
						iter_55_5.OutRange()
					else:
						arg_55_0.RemoveBulletUnit(iter_55_5.GetUniqueID())
				elif arg_55_0.checkCld:
					arg_55_0._cldSystem.UpdateBulletCld(iter_55_5)

		for iter_55_6, iter_55_7 in pairs(arg_55_0._aircraftList):
			iter_55_7.Update(arg_55_1)

			var_55_17, var_55_18 = iter_55_7.GetIFF()

			if var_55_17 == BattleConfig.FRIENDLY_CODE:
				var_55_18 = arg_55_0._totalRightBound
			elif var_55_17 == BattleConfig.FOE_CODE:
				var_55_18 = arg_55_0._totalLeftBound

			if iter_55_7.GetPosition().x * var_55_17 > abs(var_55_18) and iter_55_7.GetSpeed().x * var_55_17 > 0:
				iter_55_7.OutBound()
			else:
				arg_55_0._cldSystem.UpdateAircraftCld(iter_55_7)

			if not iter_55_7.IsAlive():
				arg_55_0.KillAircraft(iter_55_7.GetUniqueID())

		for iter_55_8, iter_55_9 in pairs(arg_55_0._AOEList):
			arg_55_0._cldSystem.UpdateAOECld(iter_55_9)
			iter_55_9.Settle()

			if iter_55_9.GetActiveFlag() == False:
				iter_55_9.SettleFinale()
				arg_55_0.RemoveAreaOfEffect(iter_55_9.GetUniqueID())

		for iter_55_10, iter_55_11 in pairs(arg_55_0._environmentList):
			iter_55_11.Update()

			if iter_55_11.IsExpire(arg_55_1):
				arg_55_0.RemoveEnvironment(iter_55_11.GetUniqueID())

		if arg_55_0.checkCld:
			for iter_55_12, iter_55_13 in pairs(arg_55_0._shelterList):
				if not iter_55_13.IsWallActive():
					arg_55_0.RemoveShelter(iter_55_13.GetUniqueID())
				else:
					iter_55_13.Update(arg_55_1)

			for iter_55_14, iter_55_15 in pairs(arg_55_0._wallList):
				if iter_55_15.IsActive():
					arg_55_0._cldSystem.UpdateWallCld(iter_55_15)

		if arg_55_0._battleInitData.battleType != SYSTEM_DUEL:
			for iter_55_16, iter_55_17 in pairs(arg_55_0._foeShipList):
				if iter_55_17.GetPosition().x + iter_55_17.GetBoxSize().x < arg_55_0._leftZoneLeftBound:
					iter_55_17.SetDeathReason(BattleConst.UnitDeathReason.TOUCHDOWN)
					iter_55_17.DeadAction()
					arg_55_0.KillUnit(iter_55_17.GetUniqueID())
					arg_55_0.HandleShipMissDamage(iter_55_17, arg_55_0._fleetList[BattleConfig.FRIENDLY_CODE])

	def UpdateAutoComponent(arg_56_0, arg_56_1):
		for iter_56_0, iter_56_1 in pairs(arg_56_0._fleetList):
			iter_56_1.UpdateAutoComponent(arg_56_1)

		for iter_56_2, iter_56_3 in pairs(arg_56_0._teamList):
			if iter_56_3.IsFatalDamage():
				arg_56_0.KillNPCTeam(iter_56_2)
			else:
				iter_56_3.UpdateMotion()

		for iter_56_4, iter_56_5 in pairs(arg_56_0._freeShipList):
			iter_56_5.UpdateOxygen(arg_56_1)
			iter_56_5.UpdateWeapon(arg_56_1)
			iter_56_5.UpdatePhaseSwitcher()

	def UpdateWeather(arg_57_0, arg_57_1):
		for iter_57_0, iter_57_1 in ipairs(arg_57_0._weahter):
			if iter_57_1 == BattleConst.WEATHER.NIGHT:
				var_57_0 = table({
					BattleConfig.FRIENDLY_CODE: 0,
					BattleConfig.FOE_CODE: 0
				})
				var_57_1 = table({
					BattleConfig.FRIENDLY_CODE: 0,
					BattleConfig.FOE_CODE: 0
				})
				var_57_2 = table({
					BattleConfig.FRIENDLY_CODE: 0,
					BattleConfig.FOE_CODE: 0
				})

				for iter_57_2, iter_57_3 in pairs(arg_57_0._unitList):
					var_57_3 = iter_57_3.GetAimBias()

					if not var_57_3 or var_57_3.GetCurrentState() != var_57_3.STATE_SUMMON_SICKNESS:
						var_57_4 = iter_57_3.GetIFF()
						var_57_5 = var_57_1[var_57_4]
						var_57_6 = BattleAttr.GetCurrent(iter_57_3, "attackRating")
						var_57_7 = BattleAttr.GetCurrent(iter_57_3, "aimBiasExtraACC")

						var_57_1[var_57_4] = max(var_57_5, var_57_6)
						var_57_2[var_57_4] = var_57_2[var_57_4] + var_57_7

						if ShipType.ContainInLimitBundle(ShipType.BundleAntiSubmarine, iter_57_3.GetTemplate().type):
							var_57_0[var_57_4] = max(var_57_0[var_57_4], var_57_6)

				for iter_57_4, iter_57_5 in pairs(arg_57_0._fleetList):
					var_57_8 = iter_57_5.GetFleetBias()
					var_57_9 = iter_57_4 * -1

					var_57_8.SetDecayFactor(var_57_1[var_57_9], var_57_2[var_57_9])
					var_57_8.Update(arg_57_1)

					for iter_57_6, iter_57_7 in ipairs(iter_57_5.GetSubList()):
						var_57_10 = iter_57_7.GetAimBias()

						if var_57_10.GetDecayFactorType() == var_57_10.DIVING:
							var_57_10.SetDecayFactor(var_57_0[var_57_9], var_57_2[var_57_9])
						else:
							var_57_10.SetDecayFactor(var_57_1[var_57_9], var_57_2[var_57_9])

						var_57_10.Update(arg_57_1)

				for iter_57_8, iter_57_9 in pairs(arg_57_0._freeShipList):
					var_57_11 = iter_57_9.GetIFF() * -1
					var_57_12 = iter_57_9.GetAimBias()

					if var_57_12.GetDecayFactorType() == var_57_12.DIVING:
						var_57_12.SetDecayFactor(var_57_0[var_57_11], var_57_2[var_57_11])
					else:
						var_57_12.SetDecayFactor(var_57_1[var_57_11], var_57_2[var_57_11])

					var_57_12.Update(arg_57_1)

	def UpdateEscapeOnly(arg_58_0, arg_58_1):
		for iter_58_0, iter_58_1 in pairs(arg_58_0._foeShipList):
			iter_58_1.Update(arg_58_1)

	def UpdateCountDown(arg_59_0, arg_59_1):
		arg_59_0._lastUpdateTime = arg_59_0._lastUpdateTime or arg_59_1

		var_59_0 = arg_59_0._countDown - (arg_59_1 - arg_59_0._lastUpdateTime)

		if var_59_0 <= 0:
			var_59_0 = 0

		if int(arg_59_0._countDown - var_59_0) == 0 or var_59_0 == 0:
			arg_59_0.DispatchEvent(Event.New(BattleEvent.UPDATE_COUNT_DOWN, table()))

		arg_59_0._countDown = var_59_0
		arg_59_0._totalTime = arg_59_1 - arg_59_0._startTimeStamp
		arg_59_0._lastUpdateTime = arg_59_1

	def SpawnMonster(arg_60_0, arg_60_1, arg_60_2, arg_60_3, arg_60_4, arg_60_5):
		var_60_0 = arg_60_0.GenerateUnitID()
		var_60_1 = BattleDataFunction.GetMonsterTmpDataFromID(arg_60_1.monsterTemplateID)
		var_60_2 = table()

		for iter_60_0, iter_60_1 in ipairs(var_60_1.equipment_list):
			table.insert(var_60_2, table(
				id = iter_60_1
			))

		var_60_3 = var_60_1.random_equipment_list
		var_60_4 = var_60_1.random_nub

		for iter_60_2, iter_60_3 in ipairs(var_60_3):
			var_60_5 = var_60_4[iter_60_2]
			var_60_6 = Clone(iter_60_3)

			for iter_60_4 in range(1, var_60_5):
				var_60_7 = math.random(len(var_60_6))

				table.insert(var_60_2, table(
					id = var_60_6[var_60_7]
				))
				table.remove(var_60_6, var_60_7)

		var_60_8 = BattleDataFunction.CreateBattleUnitData(var_60_0, arg_60_3, arg_60_4, arg_60_1.monsterTemplateID, None, var_60_2, arg_60_1.extraInfo, None, None, None, None, arg_60_1.level)

		BattleAttr.MonsterAttrFixer(arg_60_0._battleInitData.battleType, var_60_8)

		var_60_9

		if arg_60_1.immuneHPInherit:
			var_60_9 = var_60_8.GetMaxHP()
		else:
			var_60_9 = math.ceil(var_60_8.GetMaxHP() * arg_60_0._repressEnemyHpRant)

		if var_60_9 <= 0:
			var_60_9 = 1

		var_60_8.SetCurrentHP(var_60_9)

		var_60_10 = BattleFormulas.RandomPos(arg_60_1.corrdinate)

		var_60_8.SetPosition(var_60_10)
		var_60_8.SetAI(arg_60_1.pilotAITemplateID or var_60_1.pilot_ai_template_id)
		arg_60_0.setShipUnitBound(var_60_8)

		if table.contains(TeamType.SubShipType, var_60_1.type):
			var_60_8.InitOxygen()
			arg_60_0.UpdateHostileSubmarine(True)

		BattleDataFunction.AttachWeather(var_60_8, arg_60_0._weahter)

		arg_60_0._freeShipList[var_60_0] = var_60_8
		arg_60_0._unitList[var_60_0] = var_60_8

		if var_60_8.IsSpectre():
			var_60_8.UpdateBlindInvisibleBySpectre()
		else:
			arg_60_0._cldSystem.InitShipCld(var_60_8)

		var_60_11 = arg_60_1.sickness or BattleConst.SUMMONING_SICKNESS_DURATION

		var_60_8.SummonSickness(var_60_11)
		var_60_8.SetMoveCast(arg_60_1.moveCast == True)

		if var_60_8.GetIFF() == BattleConfig.FRIENDLY_CODE:
			arg_60_0._friendlyShipList[var_60_0] = var_60_8
		else:
			if var_60_8.IsSpectre():
				arg_60_0._spectreShipList[var_60_0] = var_60_8
			else:
				arg_60_0._foeShipList[var_60_0] = var_60_8

			var_60_8.SetWaveIndex(arg_60_2)

		if arg_60_1.reinforce:
			var_60_8.Reinforce()

		if arg_60_1.reinforceDelay:
			var_60_8.SetReinforceCastTime(arg_60_1.reinforceDelay)

		if arg_60_1.team:
			arg_60_0.GetNPCTeam(arg_60_1.team).AppendUnit(var_60_8)

		if arg_60_1.phase:
			BattleUnitPhaseSwitcher.New(var_60_8).SetTemplateData(arg_60_1.phase)

		if arg_60_5:
			arg_60_5(var_60_8)

		var_60_12 = table(
			type = arg_60_3,
			unit = var_60_8,
			bossData = arg_60_1.bossData,
			extraInfo = arg_60_1.extraInfo
		)

		arg_60_0.DispatchEvent(Event.New(BattleEvent.ADD_UNIT, var_60_12))

		def var_60_13(arg_61_0):
			for iter_61_0, iter_61_1 in ipairs(arg_61_0):
				if type(iter_61_1) == "number":
					var_61_1 = iter_61_1
					var_61_2 = 1
				else:
					var_61_1 = iter_61_1.ID
					var_61_2 = iter_61_1.LV or 1

				var_61_3 = BattleBuffUnit.New(var_61_1, var_61_2, var_60_8)

				var_60_8.AddBuff(var_61_3)

		var_60_14 = var_60_8.GetTemplate().buff_list
		var_60_15 = arg_60_1.buffList or table()
		var_60_16 = arg_60_0._battleInitData.ExtraBuffList or table()
		var_60_17 = arg_60_0._battleInitData.AffixBuffList or table()

		var_60_13(var_60_14)
		var_60_13(var_60_16)
		var_60_13(var_60_15)

		if arg_60_1.affix:
			var_60_13(var_60_17)

		var_60_18 = arg_60_1.summonWaveIndex

		if var_60_18:
			arg_60_0._waveSummonList[var_60_18] = arg_60_0._waveSummonList[var_60_18] or table()
			arg_60_0._waveSummonList[var_60_18][var_60_8] = True

		var_60_8.CheckWeaponInitial()

		if arg_60_0._battleInitData.CMDArgs and var_60_8.GetTemplateID() == arg_60_0._battleInitData.CMDArgs:
			arg_60_0.InitSpecificEnemyStatistics(var_60_8)

		var_60_8.OverrideDeadFX(arg_60_1.deadFX)

		if BATTLE_ENEMY_AIMBIAS_RANGE and var_60_8.GetAimBias():
			arg_60_0.DispatchEvent(Event.New(BattleEvent.ADD_AIM_BIAS, table(
				aimBias = var_60_8.GetAimBias()
			)))

		return var_60_8

	def UpdateHostileSubmarine(arg_62_0, arg_62_1):
		if arg_62_1:
			arg_62_0._enemySubmarineCount = arg_62_0._enemySubmarineCount + 1
		else:
			arg_62_0._enemySubmarineCount = arg_62_0._enemySubmarineCount - 1

		arg_62_0.DispatchEvent(Event.New(BattleEvent.UPDATE_HOSTILE_SUBMARINE))

	def SpawnNPC(arg_63_0, arg_63_1, arg_63_2):
		var_63_0 = arg_63_0.GenerateUnitID()
		var_63_1 = BattleConst.UnitType.MINION_UNIT
		var_63_2 = BattleDataFunction.GetMonsterTmpDataFromID(arg_63_1.monsterTemplateID)
		var_63_3 = table()

		for iter_63_0, iter_63_1 in ipairs(var_63_2.equipment_list):
			table.insert(var_63_3, table(
				id = iter_63_1
			))

		var_63_4 = BattleDataFunction.CreateBattleUnitData(var_63_0, var_63_1, arg_63_2.GetIFF(), arg_63_1.monsterTemplateID, None, var_63_3, arg_63_1.extraInfo, None, None, None, None, arg_63_1.level)

		var_63_4.SetMaster(arg_63_2)
		var_63_4.InheritMasterAttr()

		var_63_5 = var_63_4.GetMaxHP()

		var_63_4.SetCurrentHP(var_63_5)

		var_63_6

		if arg_63_1.corrdinate:
			var_63_6 = BattleFormulas.RandomPos(arg_63_1.corrdinate)
		else:
			var_63_6 = Clone(arg_63_2.GetPosition())

		var_63_4.SetPosition(var_63_6)
		var_63_4.SetAI(arg_63_1.pilotAITemplateID or var_63_2.pilot_ai_template_id)
		arg_63_0.setShipUnitBound(var_63_4)

		if table.contains(TeamType.SubShipType, var_63_2.type):
			var_63_4.InitOxygen()

			if var_63_4.GetIFF() != BattleConfig.FRIENDLY_CODE:
				arg_63_0.UpdateHostileSubmarine(True)

		BattleDataFunction.AttachWeather(var_63_4, arg_63_0._weahter)

		arg_63_0._freeShipList[var_63_0] = var_63_4
		arg_63_0._unitList[var_63_0] = var_63_4

		arg_63_0._cldSystem.InitShipCld(var_63_4)
		var_63_4.SummonSickness(BattleConst.SUMMONING_SICKNESS_DURATION)
		var_63_4.SetMoveCast(arg_63_1.moveCast == True)

		arg_63_0._minionShipList[var_63_0] = var_63_4

		if arg_63_1.phase:
			BattleUnitPhaseSwitcher.New(var_63_4).SetTemplateData(arg_63_1.phase)

		var_63_7 = table(
			type = var_63_1,
			unit = var_63_4,
			bossData = arg_63_1.bossData,
			extraInfo = arg_63_1.extraInfo
		)

		arg_63_0.DispatchEvent(Event.New(BattleEvent.ADD_UNIT, var_63_7))

		def var_63_8(arg_64_0):
			for iter_64_0, iter_64_1 in ipairs(arg_64_0):
				if type(iter_64_1) == "number":
					var_64_1 = iter_64_1
					var_64_2 = 1
				else:
					var_64_1 = iter_64_1.ID
					var_64_2 = iter_64_1.LV or 1

				var_64_3 = BattleBuffUnit.New(var_64_1, var_64_2, var_63_4)

				var_63_4.AddBuff(var_64_3)

		var_63_9 = var_63_4.GetTemplate().buff_list
		var_63_10 = arg_63_1.buffList or table()

		var_63_8(var_63_9)
		var_63_8(var_63_10)
		var_63_4.CheckWeaponInitial()

		return var_63_4

	def EnemyEscape(arg_65_0):
		for iter_65_0, iter_65_1 in pairs(arg_65_0._foeShipList):
			if iter_65_1.ContainsLabelTag(BattleConfig.ESCAPE_EXPLO_TAG):
				iter_65_1.SetDeathReason(BattleConst.UnitDeathReason.CLS)
				iter_65_1.DeadAction()
			else:
				iter_65_1.RemoveAllAutoWeapon()
				iter_65_1.SetAI(BattleConfig.COUNT_DOWN_ESCAPE_AI_ID)

	def GetNPCTeam(arg_66_0, arg_66_1):
		if not arg_66_0._teamList[arg_66_1]:
			arg_66_0._teamList[arg_66_1] = BattleTeamVO.New(arg_66_1)

		return arg_66_0._teamList[arg_66_1]

	def KillNPCTeam(arg_67_0, arg_67_1):
		var_67_0 = arg_67_0._teamList[arg_67_1]

		if var_67_0:
			var_67_0.Dispose()

			arg_67_0._teamList[arg_67_1] = None

	def SpawnVanguard(arg_68_0, arg_68_1, arg_68_2):
		var_68_0 = arg_68_0.GetVanguardBornCoordinate(arg_68_2)
		var_68_1 = arg_68_0.generatePlayerUnit(arg_68_1, arg_68_2, Vector3(*var_68_0.values()), arg_68_0._commanderBuff)

		arg_68_0.GetFleetByIFF(arg_68_2).AppendPlayerUnit(var_68_1)
		arg_68_0.setShipUnitBound(var_68_1)
		BattleDataFunction.AttachWeather(var_68_1, arg_68_0._weahter)
		arg_68_0._cldSystem.InitShipCld(var_68_1)

		var_68_2 = table(
			type = BattleConst.UnitType.PLAYER_UNIT,
			unit = var_68_1
		)

		arg_68_0.DispatchEvent(Event.New(BattleEvent.ADD_UNIT, var_68_2))

		return var_68_1

	def SpawnMain(arg_69_0, arg_69_1, arg_69_2):
		var_69_0
		var_69_1 = arg_69_0.GetFleetByIFF(arg_69_2)
		var_69_2 = len(var_69_1.GetMainList())

		if arg_69_0._currentStageData.mainUnitPosition and arg_69_0._currentStageData.mainUnitPosition[arg_69_2]:
			var_69_0 = Clone(arg_69_0._currentStageData.mainUnitPosition[arg_69_2][var_69_2])
		else:
			var_69_0 = Clone(BattleConfig.MAIN_UNIT_POS[arg_69_2][var_69_2])

		var_69_3 = arg_69_0.generatePlayerUnit(arg_69_1, arg_69_2, var_69_0, arg_69_0._commanderBuff)

		var_69_3.SetBornPosition(var_69_0)
		var_69_3.SetMainFleetUnit()

		var_69_4 = var_69_0.x

		if var_69_4 < arg_69_0._totalLeftBound or var_69_4 > arg_69_0._totalRightBound:
			var_69_3.SetImmuneCommonBulletCLD()

		var_69_1.AppendPlayerUnit(var_69_3)
		arg_69_0.setShipUnitBound(var_69_3)
		BattleDataFunction.AttachWeather(var_69_3, arg_69_0._weahter)
		arg_69_0._cldSystem.InitShipCld(var_69_3)

		var_69_5 = table(
			type = BattleConst.UnitType.PLAYER_UNIT,
			unit = var_69_3
		)

		arg_69_0.DispatchEvent(Event.New(BattleEvent.ADD_UNIT, var_69_5))

		return var_69_3

	def SpawnSub(arg_70_0, arg_70_1, arg_70_2):
		var_70_0
		var_70_1 = arg_70_0.GetFleetByIFF(arg_70_2)
		var_70_2 = len(var_70_1.GetSubList())
		var_70_3 = BattleConfig.SUB_UNIT_OFFSET_X + (BattleDataFunction.GetPlayerShipTmpDataFromID(arg_70_1.tmpID).summon_offset or 0)

		if arg_70_2 == BattleConfig.FRIENDLY_CODE:
			var_70_0 = Vector3(var_70_3 + arg_70_0._totalLeftBound, 0, BattleConfig.SUB_UNIT_POS_Z[var_70_2])
		else:
			var_70_0 = Vector3(arg_70_0._totalRightBound - var_70_3, 0, BattleConfig.SUB_UNIT_POS_Z[var_70_2])

		var_70_4 = arg_70_0.generatePlayerUnit(arg_70_1, arg_70_2, var_70_0, arg_70_0._subCommanderBuff)

		var_70_1.AddSubMarine(var_70_4)
		arg_70_0.setShipUnitBound(var_70_4)
		BattleDataFunction.AttachWeather(var_70_4, arg_70_0._weahter)
		arg_70_0._cldSystem.InitShipCld(var_70_4)

		var_70_5 = table(
			type = BattleConst.UnitType.PLAYER_UNIT,
			unit = var_70_4
		)

		arg_70_0.DispatchEvent(Event.New(BattleEvent.ADD_UNIT, var_70_5))

		return var_70_4

	def SpawnManualSub(arg_71_0, arg_71_1, arg_71_2):
		var_71_0 = arg_71_0.GetVanguardBornCoordinate(arg_71_2)
		var_71_1 = arg_71_0.generatePlayerUnit(arg_71_1, arg_71_2, Vector3(*var_71_0.values()), arg_71_0._commanderBuff)

		arg_71_0.GetFleetByIFF(arg_71_2).AddManualSubmarine(var_71_1)
		arg_71_0.setShipUnitBound(var_71_1)
		arg_71_0._cldSystem.InitShipCld(var_71_1)

		var_71_2 = table(
			type = BattleConst.UnitType.SUB_UNIT,
			unit = var_71_1
		)

		arg_71_0.DispatchEvent(Event.New(BattleEvent.ADD_UNIT, var_71_2))

		return var_71_1

	def SpawnSupportUnit(arg_72_0, arg_72_1, arg_72_2):
		var_72_0 = arg_72_0.generateSupportPlayerUnit(arg_72_1, arg_72_2)

		arg_72_0.GetFleetByIFF(arg_72_2).AppendSupportUnit(var_72_0)

		return var_72_0

	def ShutdownPlayerUnit(arg_73_0, arg_73_1):
		var_73_0 = arg_73_0._unitList[arg_73_1]
		var_73_1 = var_73_0.GetIFF()
		var_73_2 = arg_73_0.GetFleetByIFF(var_73_1)

		var_73_2.RemovePlayerUnit(var_73_0)

		var_73_3 = table()

		if var_73_2.GetFleetAntiAirWeapon().GetRange() == 0:
			var_73_3.isShow = False

		arg_73_0.DispatchEvent(Event.New(BattleEvent.ANTI_AIR_AREA, var_73_3))

		var_73_4 = table(
			unit = var_73_0
		)

		arg_73_0.DispatchEvent(Event.New(BattleEvent.SHUT_DOWN_PLAYER, var_73_4))

	def updateDeadList(arg_74_0):
		var_74_0 = len(arg_74_0._deadUnitList)

		while var_74_0 > 0:
			var_74_0 = var_74_0 - 1
			arg_74_0._deadUnitList[var_74_0].Dispose()

			arg_74_0._deadUnitList[var_74_0] = None

	def KillUnit(arg_75_0, arg_75_1):
		var_75_0 = arg_75_0._unitList[arg_75_1]

		if var_75_0 == None:
			return

		var_75_1 = var_75_0.GetUnitType()

		arg_75_0._cldSystem.DeleteShipCld(var_75_0)
		var_75_0.Clear()

		arg_75_0._unitList[arg_75_1] = None

		if arg_75_0._freeShipList[arg_75_1]:
			arg_75_0._freeShipList[arg_75_1] = None

		var_75_2 = var_75_0.GetIFF()
		var_75_3 = var_75_0.GetDeathReason()

		if var_75_0.GetAimBias():
			var_75_4 = var_75_0.GetAimBias()

			var_75_4.RemoveCrew(var_75_0)

			if var_75_4.GetCurrentState() == var_75_4.STATE_EXPIRE:
				arg_75_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AIM_BIAS, table(
					aimBias = var_75_0.GetAimBias()
				)))

		if var_75_0.IsSpectre():
			arg_75_0._spectreShipList[arg_75_1] = None
		elif var_75_2 == BattleConfig.FOE_CODE:
			arg_75_0._foeShipList[arg_75_1] = None

			if var_75_1 == BattleConst.UnitType.ENEMY_UNIT or var_75_1 == BattleConst.UnitType.BOSS_UNIT:
				if var_75_0.GetTeam():
					var_75_0.GetTeam().RemoveUnit(var_75_0)

				var_75_5 = var_75_0.GetTemplate().type

				if table.contains(TeamType.SubShipType, var_75_5):
					arg_75_0.UpdateHostileSubmarine(False)

				var_75_6 = var_75_0.GetWaveIndex()

				if var_75_6 and arg_75_0._waveSummonList[var_75_6]:
					arg_75_0._waveSummonList[var_75_6][var_75_0] = None
		elif var_75_2 == BattleConfig.FRIENDLY_CODE:
			arg_75_0._friendlyShipList[arg_75_1] = None

		var_75_7 = table(
			UID = arg_75_1,
			type = var_75_1,
			deadReason = var_75_3,
			unit = var_75_0
		)

		arg_75_0.DispatchEvent(Event.New(BattleEvent.REMOVE_UNIT, var_75_7))
		table.insert(arg_75_0._deadUnitList, var_75_0)

	def KillAllEnemy(arg_76_0):
		for iter_76_0, iter_76_1 in pairs(arg_76_0._unitList):
			if iter_76_1.GetIFF() == BattleConfig.FOE_CODE and iter_76_1.IsAlive() and not iter_76_1.IsBoss():
				iter_76_1.DeadAction()

	def KillSubmarineByIFF(arg_77_0, arg_77_1):
		for iter_77_0, iter_77_1 in pairs(arg_77_0._unitList):
			if iter_77_1.GetIFF() == arg_77_1 and iter_77_1.IsAlive() and table.contains(TeamType.SubShipType, iter_77_1.GetTemplate().type) and not iter_77_1.IsBoss():
				iter_77_1.DeadAction()

	def KillAllAircraft(arg_78_0):
		for iter_78_0, iter_78_1 in pairs(arg_78_0._aircraftList):
			iter_78_1.Clear()

			var_78_0 = table(
				UID = iter_78_0
			)

			arg_78_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AIR_CRAFT, var_78_0))

			arg_78_0._aircraftList[iter_78_0] = None

	def KillWaveSummonMonster(arg_79_0, arg_79_1):
		var_79_0 = arg_79_0._waveSummonList[arg_79_1]

		if var_79_0:
			for iter_79_0, iter_79_1 in pairs(var_79_0):
				var_79_1 = iter_79_0.GetUniqueID()

				arg_79_0.KillUnit(var_79_1)

		arg_79_0._waveSummonList[arg_79_1] = None

	def IsThereBoss(arg_80_0):
		return arg_80_0.GetActiveBossCount() > 0

	def GetActiveBossCount(arg_81_0):
		var_81_0 = 0

		for iter_81_0, iter_81_1 in pairs(arg_81_0.GetUnitList()):
			if iter_81_1.IsBoss() and iter_81_1.IsAlive():
				var_81_0 = var_81_0 + 1

		return var_81_0

	def setShipUnitBound(arg_82_0, arg_82_1):
		var_82_0 = arg_82_1.GetIFF()

		if arg_82_1.GetFleetVO():
			arg_82_1.SetBound(arg_82_1.GetFleetVO().GetUnitBound().GetBound())
		else:
			arg_82_1.SetBound(arg_82_0.GetUnitBoundByIFF(var_82_0))

	def generatePlayerUnit(arg_83_0, arg_83_1, arg_83_2, arg_83_3, arg_83_4):
		var_83_0 = arg_83_0.GenerateUnitID()
		var_83_1 = arg_83_1.properties

		var_83_1.level = arg_83_1.level
		var_83_1.formationID = BattleConfig.FORMATION_ID
		var_83_1.id = arg_83_1.id

		BattleAttr.AttrFixer(arg_83_0._battleInitData.battleType, var_83_1)

		var_83_2 = arg_83_1.proficiency or table(
			1,
			1,
			1
		)
		var_83_3 = BattleConst.UnitType.PLAYER_UNIT
		var_83_4 = arg_83_0._battleInitData.battleType

		if var_83_4 == SYSTEM_SUBMARINE_RUN or var_83_4 == SYSTEM_SUB_ROUTINE:
			var_83_3 = BattleConst.UnitType.SUB_UNIT
		elif var_83_4 == SYSTEM_AIRFIGHT:
			var_83_3 = BattleConst.UnitType.CONST_UNIT
		elif var_83_4 == SYSTEM_CARDPUZZLE:
			var_83_3 = BattleConst.UnitType.CARDPUZZLE_PLAYER_UNIT

		var_83_5 = BattleDataFunction.CreateBattleUnitData(var_83_0, var_83_3, arg_83_2, arg_83_1.tmpID, arg_83_1.skinId, arg_83_1.equipment, var_83_1, arg_83_1.baseProperties, var_83_2, arg_83_1.baseList, arg_83_1.preloasList)

		BattleDataFunction.AttachUltimateBonus(var_83_5)
		var_83_5.InitCurrentHP(arg_83_1.initHPRate or 1)
		var_83_5.SetRarity(arg_83_1.rarity)
		var_83_5.SetIntimacy(arg_83_1.intimacy)
		var_83_5.SetShipName(arg_83_1.name)

		if arg_83_1.spWeapon:
			var_83_5.SetSpWeapon(arg_83_1.spWeapon)
			underscore.each(arg_83_1.spWeapon.GetLabel(), lambda arg_84_0: var_83_5.AddLabelTag(arg_84_0))

		arg_83_0._unitList[var_83_0] = var_83_5

		if var_83_5.GetIFF() == BattleConfig.FRIENDLY_CODE:
			arg_83_0._friendlyShipList[var_83_0] = var_83_5
		elif var_83_5.GetIFF() == BattleConfig.FOE_CODE:
			arg_83_0._foeShipList[var_83_0] = var_83_5

		if var_83_4 == SYSTEM_WORLD:
			var_83_6 = BattleFormulas.WorldMapRewardHealingRate(arg_83_0._battleInitData.EnemyMapRewards, arg_83_0._battleInitData.FleetMapRewards)

			BattleAttr.SetCurrent(var_83_5, "healingRate", var_83_6)

		var_83_5.SetPosition(arg_83_3)
		BattleDataFunction.InitUnitSkill(arg_83_1, var_83_5, var_83_4)
		BattleDataFunction.InitEquipSkill(arg_83_1.equipment, var_83_5, var_83_4)
		BattleDataFunction.InitCommanderSkill(arg_83_4, var_83_5, var_83_4)
		var_83_5.SetGearScore(arg_83_1.shipGS)

		if arg_83_1.deathMark:
			var_83_5.SetWorldDeathMark()

		return var_83_5

	def generateSupportPlayerUnit(arg_85_0, arg_85_1, arg_85_2):
		var_85_0 = arg_85_0.GenerateUnitID()
		var_85_1 = arg_85_1.properties

		var_85_1.level = arg_85_1.level
		var_85_1.formationID = BattleConfig.FORMATION_ID
		var_85_1.id = arg_85_1.id

		BattleAttr.AttrFixer(arg_85_0._battleInitData.battleType, var_85_1)

		var_85_2 = arg_85_1.proficiency or table(
			1,
			1,
			1
		)
		var_85_3 = BattleDataFunction.CreateBattleUnitData(var_85_0, BattleConst.UnitType.SUPPORT_UNIT, arg_85_2, arg_85_1.tmpID, arg_85_1.skinId, arg_85_1.equipment, var_85_1, arg_85_1.baseProperties, var_85_2, arg_85_1.baseList, arg_85_1.preloasList)

		var_85_3.InitCurrentHP(1)
		var_85_3.SetShipName(arg_85_1.name)

		arg_85_0._spectreShipList[var_85_0] = var_85_3

		var_85_3.SetPosition(Clone(BattleConfig.AirSupportUnitPos))

		return var_85_3

	def SwitchSpectreUnit(arg_86_0, arg_86_1):
		var_86_0 = arg_86_1.GetUniqueID()
		var_86_1 = arg_86_1.GetIFF() == BattleConfig.FRIENDLY_CODE and arg_86_0._friendlyShipList or arg_86_0._foeShipList

		if arg_86_1.IsSpectre():
			var_86_1[var_86_0] = None
			arg_86_0._spectreShipList[var_86_0] = arg_86_1

			for iter_86_0, iter_86_1 in pairs(arg_86_0._AOEList):
				iter_86_1.ForceExit(arg_86_1.GetUniqueID())

			arg_86_0._cldSystem.DeleteShipCld(arg_86_1)
		else:
			arg_86_0._spectreShipList[var_86_0] = None
			var_86_1[var_86_0] = arg_86_1

			arg_86_1.ActiveCldBox()
			arg_86_0._cldSystem.InitShipCld(arg_86_1)

	def GetUnitList(arg_87_0):
		return arg_87_0._unitList

	def GetFriendlyShipList(arg_88_0):
		return arg_88_0._friendlyShipList

	def GetFoeShipList(arg_89_0):
		return arg_89_0._foeShipList

	def GetFoeAircraftList(arg_90_0):
		return arg_90_0._foeAircraftList

	def GetFreeShipList(arg_91_0):
		return arg_91_0._freeShipList

	def GetSpectreShipList(arg_92_0):
		return arg_92_0._spectreShipList

	def GenerateUnitID(arg_93_0):
		arg_93_0._unitCount = arg_93_0._unitCount + 1

		return arg_93_0._unitCount

	def GetCountDown(arg_94_0):
		return arg_94_0._countDown

	def SpawnAirFighter(arg_95_0, arg_95_1):
		var_95_0 = len(arg_95_0._airFighterList)
		var_95_1 = BattleDataFunction.GetFormationTmpDataFromID(arg_95_1.formation).pos_offset
		var_95_2 = table(
			currentNumber = 0,
			templateID = arg_95_1.templateID,
			totalNumber = arg_95_1.totalNumber or 0,
			onceNumber = arg_95_1.onceNumber,
			timeDelay = arg_95_1.interval or 3,
			maxTotalNumber = arg_95_1.maxTotalNumber or 15
		)

		def var_95_3(arg_96_0):
			var_96_0 = var_95_2.currentNumber

			if var_96_0 < var_95_2.totalNumber:
				var_95_2.currentNumber = var_96_0 + 1

				var_96_1 = arg_95_0.CreateAirFighter(arg_95_1)

				var_96_1.SetFormationOffset(var_95_1[arg_96_0])
				var_96_1.SetFormationIndex(arg_96_0)
				def helper():
					var_95_2.totalNumber = var_95_2.totalNumber - 1
					var_95_2.currentNumber = var_95_2.currentNumber - 1

					arg_95_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AIR_FIGHTER_ICON, table(
						index = var_95_0
					)))
					arg_95_0.DispatchEvent(Event.New(BattleEvent.UPDATE_AIR_SUPPORT_LABEL, table()))
				var_96_1.SetDeadCallBack(helper)
				def helper():
					var_95_2.currentNumber -= 1
				var_96_1.SetLiveCallBack(helper)

		def var_95_4():
			var_99_0 = var_95_2.onceNumber

			if var_95_2.totalNumber > 0:
				for iter_99_0 in range(1, var_99_0):
					var_95_3(iter_99_0)
			else:
				TimeMgr.GetInstance().RemoveBattleTimer(var_95_2.timer)

				var_95_2.timer = None

		arg_95_0._airFighterList[var_95_0] = var_95_2

		arg_95_0.DispatchEvent(Event.New(BattleEvent.ADD_AIR_FIGHTER_ICON, table(
			index = var_95_0
		)))
		arg_95_0.DispatchEvent(Event.New(BattleEvent.UPDATE_AIR_SUPPORT_LABEL, table()))

		var_95_2.timer = TimeMgr.GetInstance().AddBattleTimer("striker", -1, arg_95_1.interval, var_95_4)

	def ClearAirFighterTimer(arg_100_0):
		for iter_100_0, iter_100_1 in ipairs(arg_100_0._airFighterList):
			TimeMgr.GetInstance().RemoveBattleTimer(iter_100_1.timer)

			iter_100_1.timer = None

		arg_100_0._airFighterList = table()

	def KillAllAirStrike(arg_101_0):
		for iter_101_0, iter_101_1 in pairs(arg_101_0._aircraftList):
			if iter_101_1.__name == BattleAirFighterUnit.__name:
				arg_101_0._cldSystem.DeleteAircraftCld(iter_101_1)

				iter_101_1._aliveState = False
				arg_101_0._aircraftList[iter_101_0] = None
				arg_101_0._foeAircraftList[iter_101_0] = None

				var_101_0 = table(
					UID = iter_101_0
				)

				arg_101_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AIR_CRAFT, var_101_0))

		var_101_1 = True

		for iter_101_2, iter_101_3 in pairs(arg_101_0._foeAircraftList):
			var_101_1 = False

			break

		if var_101_1:
			arg_101_0.DispatchEvent(Event.New(BattleEvent.ANTI_AIR_AREA, table(
				isShow = False
			)))

		for iter_101_4, iter_101_5 in ipairs(arg_101_0._airFighterList):
			iter_101_5.totalNumber = 0

			arg_101_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AIR_FIGHTER_ICON, table(
				index = iter_101_4
			)))
			TimeMgr.GetInstance().RemoveBattleTimer(iter_101_5.timer)

			iter_101_5.timer = None

		arg_101_0._airFighterList = table()

	def GetAirFighterInfo(arg_102_0, arg_102_1):
		return arg_102_0._airFighterList[arg_102_1]

	def GetAirFighterList(arg_103_0):
		return arg_103_0._airFighterList

	def CreateAircraft(arg_104_0, arg_104_1, arg_104_2, arg_104_3, arg_104_4):
		var_104_0 = arg_104_0.GenerateAircraftID()
		var_104_1 = BattleDataFunction.CreateAircraftUnit(var_104_0, arg_104_2, arg_104_1, arg_104_3)

		if arg_104_4:
			var_104_1.SetSkinID(arg_104_4)

		var_104_2

		if arg_104_1.GetIFF() == BattleConfig.FRIENDLY_CODE:
			pass #block empty
		else:
			var_104_2 = True

		arg_104_0.doCreateAirUnit(var_104_0, var_104_1, BattleConst.UnitType.AIRCRAFT_UNIT, var_104_2)

		return var_104_1

	def CreateAirFighter(arg_105_0, arg_105_1):
		var_105_0 = arg_105_0.GenerateAircraftID()
		var_105_1 = BattleDataFunction.CreateAirFighterUnit(var_105_0, arg_105_1)

		arg_105_0.doCreateAirUnit(var_105_0, var_105_1, BattleConst.UnitType.AIRFIGHTER_UNIT, True)

		return var_105_1

	def doCreateAirUnit(arg_106_0, arg_106_1, arg_106_2, arg_106_3, arg_106_4):
		arg_106_0._aircraftList[arg_106_1] = arg_106_2

		arg_106_0._cldSystem.InitAircraftCld(arg_106_2)
		arg_106_2.SetBound(arg_106_0._leftZoneUpperBound, arg_106_0._leftZoneLowerBound)
		arg_106_2.SetViewBoundData(arg_106_0._cameraTop, arg_106_0._cameraBottom, arg_106_0._cameraLeft, arg_106_0._cameraRight)
		arg_106_0.DispatchEvent(Event.New(BattleEvent.ADD_UNIT, table(
			unit = arg_106_2,
			type = arg_106_3
		)))

		arg_106_4 = arg_106_4 or False

		if arg_106_4:
			arg_106_0._foeAircraftList[arg_106_1] = arg_106_2

			arg_106_0.DispatchEvent(Event.New(BattleEvent.ANTI_AIR_AREA, table(
				isShow = True
			)))

	def KillAircraft(arg_107_0, arg_107_1):
		var_107_0 = arg_107_0._aircraftList[arg_107_1]

		if var_107_0 == None:
			return

		var_107_0.Clear()
		arg_107_0._cldSystem.DeleteAircraftCld(var_107_0)

		if var_107_0.IsUndefeated() and var_107_0.GetCurrentState() != var_107_0.STRIKE_STATE_RECYCLE:
			var_107_1 = var_107_0.GetIFF() * -1

			arg_107_0.HandleAircraftMissDamage(var_107_0, arg_107_0._fleetList[var_107_1])

		var_107_0._aliveState = False
		arg_107_0._aircraftList[arg_107_1] = None
		arg_107_0._foeAircraftList[arg_107_1] = None

		var_107_2 = True

		for iter_107_0, iter_107_1 in pairs(arg_107_0._foeAircraftList):
			var_107_2 = False

			break

		if var_107_2:
			arg_107_0.DispatchEvent(Event.New(BattleEvent.ANTI_AIR_AREA, table(
				isShow = False
			)))

		var_107_3 = table(
			UID = arg_107_1
		)

		arg_107_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AIR_CRAFT, var_107_3))

	def GetAircraftList(arg_108_0):
		return arg_108_0._aircraftList

	def GenerateAircraftID(arg_109_0):
		arg_109_0._aircraftCount = arg_109_0._aircraftCount + 1

		return arg_109_0._aircraftCount

	def CreateBulletUnit(arg_110_0, arg_110_1, arg_110_2, arg_110_3, arg_110_4):
		var_110_0 = arg_110_0.GenerateBulletID()
		var_110_1, var_110_2 = BattleDataFunction.CreateBattleBulletData(var_110_0, arg_110_1, arg_110_2, arg_110_3, arg_110_4)

		if var_110_2:
			arg_110_0._cldSystem.InitBulletCld(var_110_1)

		var_110_3, var_110_4 = arg_110_3.GetFixBulletRange()

		if var_110_3 or var_110_4:
			var_110_1.FixRange(var_110_3, var_110_4)

		arg_110_0._bulletList[var_110_0] = var_110_1

		return var_110_1

	def RemoveBulletUnit(arg_111_0, arg_111_1):
		var_111_0 = arg_111_0._bulletList[arg_111_1]

		if var_111_0 == None:
			return

		var_111_0.DamageUnitListWriteback()

		if var_111_0.GetIsCld():
			arg_111_0._cldSystem.DeleteBulletCld(var_111_0)

		arg_111_0._bulletList[arg_111_1] = None

		var_111_1 = table(
			UID = arg_111_1
		)

		arg_111_0.DispatchEvent(Event.New(BattleEvent.REMOVE_BULLET, var_111_1))
		var_111_0.Dispose()

	def GetBulletList(arg_112_0):
		return arg_112_0._bulletList

	def GenerateBulletID(arg_113_0):
		var_113_0 = arg_113_0._bulletCount + 1

		arg_113_0._bulletCount = var_113_0

		return var_113_0

	def CLSBullet(arg_114_0, arg_114_1, arg_114_2):
		var_114_0 = True

		if arg_114_0._battleInitData.battleType == SYSTEM_DUEL:
			var_114_0 = False

		if var_114_0:
			for iter_114_0, iter_114_1 in pairs(arg_114_0._bulletList):
				if iter_114_1.GetIFF() != arg_114_1 or not iter_114_1.GetExist() or iter_114_1.ImmuneCLS() or iter_114_1.ImmuneBombCLS() and arg_114_2:
					pass #block empty
				else:
					arg_114_0.RemoveBulletUnit(iter_114_0)

	def CLSAircraft(arg_115_0, arg_115_1):
		for iter_115_0, iter_115_1 in pairs(arg_115_0._aircraftList):
			if iter_115_1.GetIFF() == arg_115_1:
				iter_115_1.Clear()

				var_115_0 = table(
					UID = iter_115_0
				)

				arg_115_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AIR_CRAFT, var_115_0))

				arg_115_0._aircraftList[iter_115_0] = None

	def CLSMinion(arg_116_0):
		for iter_116_0, iter_116_1 in pairs(arg_116_0._unitList):
			if iter_116_1.GetIFF() == BattleConfig.FOE_CODE and iter_116_1.IsAlive() and not iter_116_1.IsBoss():
				iter_116_1.SetDeathReason(BattleConst.UnitDeathReason.CLS)
				iter_116_1.DeadAction()

	def SpawnColumnArea(arg_117_0, arg_117_1, arg_117_2, arg_117_3, arg_117_4, arg_117_5, arg_117_6, arg_117_7, arg_117_8):
		arg_117_7 = arg_117_7 or False

		var_117_0 = arg_117_0.GenerateAreaID()
		var_117_1 = BattleAOEData.New(var_117_0, arg_117_2, arg_117_6, arg_117_8)
		var_117_2 = Clone(arg_117_3)

		var_117_1.SetPosition(var_117_2)
		var_117_1.SetRange(arg_117_4)
		var_117_1.SetAreaType(BattleConst.AreaType.COLUMN)
		var_117_1.SetLifeTime(arg_117_5)
		var_117_1.SetFieldType(arg_117_1)
		var_117_1.SetOpponentAffected(not arg_117_7)
		arg_117_0.CreateAreaOfEffect(var_117_1)

		return var_117_1

	def SpawnCubeArea(arg_118_0, arg_118_1, arg_118_2, arg_118_3, arg_118_4, arg_118_5, arg_118_6, arg_118_7, arg_118_8, arg_118_9):
		arg_118_8 = arg_118_8 or False

		var_118_0 = arg_118_0.GenerateAreaID()
		var_118_1 = BattleAOEData.New(var_118_0, arg_118_2, arg_118_7, arg_118_9)
		var_118_2 = Clone(arg_118_3)

		var_118_1.SetPosition(var_118_2)
		var_118_1.SetWidth(arg_118_4)
		var_118_1.SetHeight(arg_118_5)
		var_118_1.SetAreaType(BattleConst.AreaType.CUBE)
		var_118_1.SetLifeTime(arg_118_6)
		var_118_1.SetFieldType(arg_118_1)
		var_118_1.SetOpponentAffected(not arg_118_8)
		arg_118_0.CreateAreaOfEffect(var_118_1)

		return var_118_1

	def SpawnLastingColumnArea(arg_119_0, arg_119_1, arg_119_2, arg_119_3, arg_119_4, arg_119_5, arg_119_6, arg_119_7, arg_119_8, arg_119_9, arg_119_10, arg_119_11):
		arg_119_8 = arg_119_8 or False

		var_119_0 = arg_119_0.GenerateAreaID()
		var_119_1 = BattleLastingAOEData.New(var_119_0, arg_119_2, arg_119_6, arg_119_7, arg_119_10, arg_119_11)
		var_119_2 = Clone(arg_119_3)

		var_119_1.SetPosition(var_119_2)
		var_119_1.SetRange(arg_119_4)
		var_119_1.SetAreaType(BattleConst.AreaType.COLUMN)
		var_119_1.SetLifeTime(arg_119_5)
		var_119_1.SetFieldType(arg_119_1)
		var_119_1.SetOpponentAffected(not arg_119_8)
		arg_119_0.CreateAreaOfEffect(var_119_1)

		if arg_119_9 and arg_119_9 != "":
			var_119_3 = table(
				area = var_119_1,
				FXID = arg_119_9
			)

			arg_119_0.DispatchEvent(Event.New(BattleEvent.ADD_AREA, var_119_3))

		return var_119_1

	def SpawnLastingCubeArea(arg_120_0, arg_120_1, arg_120_2, arg_120_3, arg_120_4, arg_120_5, arg_120_6, arg_120_7, arg_120_8, arg_120_9, arg_120_10, arg_120_11, arg_120_12):
		arg_120_9 = arg_120_9 or False

		var_120_0 = arg_120_0.GenerateAreaID()
		var_120_1 = BattleLastingAOEData.New(var_120_0, arg_120_2, arg_120_7, arg_120_8, arg_120_11, arg_120_12)
		var_120_2 = Clone(arg_120_3)

		var_120_1.SetPosition(var_120_2)
		var_120_1.SetWidth(arg_120_4)
		var_120_1.SetHeight(arg_120_5)
		var_120_1.SetAreaType(BattleConst.AreaType.CUBE)
		var_120_1.SetLifeTime(arg_120_6)
		var_120_1.SetFieldType(arg_120_1)
		var_120_1.SetOpponentAffected(not arg_120_9)
		arg_120_0.CreateAreaOfEffect(var_120_1)

		if arg_120_10 and arg_120_10 != "":
			var_120_3 = table(
				area = var_120_1,
				FXID = arg_120_10
			)

			arg_120_0.DispatchEvent(Event.New(BattleEvent.ADD_AREA, var_120_3))

		return var_120_1

	def SpawnTriggerColumnArea(arg_121_0, arg_121_1, arg_121_2, arg_121_3, arg_121_4, arg_121_5, arg_121_6, arg_121_7, arg_121_8):
		arg_121_6 = arg_121_6 or False

		var_121_0 = arg_121_0.GenerateAreaID()
		var_121_1 = BattleTriggerAOEData.New(var_121_0, arg_121_2, arg_121_8)
		var_121_2 = Clone(arg_121_3)

		var_121_1.SetPosition(var_121_2)
		var_121_1.SetRange(arg_121_4)
		var_121_1.SetAreaType(BattleConst.AreaType.COLUMN)
		var_121_1.SetLifeTime(arg_121_5)
		var_121_1.SetFieldType(arg_121_1)
		var_121_1.SetOpponentAffected(not arg_121_6)
		arg_121_0.CreateAreaOfEffect(var_121_1)

		if arg_121_7 and arg_121_7 != "":
			var_121_3 = table(
				area = var_121_1,
				FXID = arg_121_7
			)

			arg_121_0.DispatchEvent(Event.New(BattleEvent.ADD_AREA, var_121_3))

		return var_121_1

	def CreateAreaOfEffect(arg_122_0, arg_122_1):
		arg_122_0._AOEList[arg_122_1.GetUniqueID()] = arg_122_1

		arg_122_0._cldSystem.InitAOECld(arg_122_1)
		arg_122_1.StartTimer()

	def RemoveAreaOfEffect(arg_123_0, arg_123_1):
		var_123_0 = arg_123_0._AOEList[arg_123_1]

		if not var_123_0:
			return

		var_123_0.Dispose()

		arg_123_0._AOEList[arg_123_1] = None

		arg_123_0._cldSystem.DeleteAOECld(var_123_0)
		arg_123_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AREA, table(
			id = arg_123_1
		)))

	def GetAOEList(arg_124_0):
		return arg_124_0._AOEList

	def GenerateAreaID(arg_125_0):
		arg_125_0._AOECount = arg_125_0._AOECount + 1

		return arg_125_0._AOECount

	def SpawnWall(arg_126_0, arg_126_1, arg_126_2, arg_126_3, arg_126_4):
		var_126_0 = arg_126_0.GenerateWallID()
		var_126_1 = BattleWallData.New(var_126_0, arg_126_1, arg_126_2, arg_126_3, arg_126_4)

		arg_126_0._wallList[var_126_0] = var_126_1

		arg_126_0._cldSystem.InitWallCld(var_126_1)

		return var_126_1

	def RemoveWall(arg_127_0, arg_127_1):
		var_127_0 = arg_127_0._wallList[arg_127_1]

		arg_127_0._wallList[arg_127_1] = None

		arg_127_0._cldSystem.DeleteWallCld(var_127_0)

	def SpawnShelter(arg_128_0, arg_128_1, arg_128_2):
		var_128_0 = arg_128_0.GernerateShelterID()
		var_128_1 = BattleShelterData.New(var_128_0)

		arg_128_0._shelterList[var_128_0] = var_128_1

		return var_128_1

	def RemoveShelter(arg_129_0, arg_129_1):
		var_129_0 = arg_129_0._shelterList[arg_129_1]
		var_129_1 = table(
			uid = arg_129_1
		)

		arg_129_0.DispatchEvent(Event.New(BattleEvent.REMOVE_SHELTER, var_129_1))
		var_129_0.Deactive()

		arg_129_0._shelterList[arg_129_1] = None

	def GetWallList(arg_130_0):
		return arg_130_0._wallList

	def GenerateWallID(arg_131_0):
		arg_131_0._wallIndex = arg_131_0._wallIndex + 1

		return arg_131_0._wallIndex

	def GernerateShelterID(arg_132_0):
		arg_132_0._shelterIndex = arg_132_0._shelterIndex + 1

		return arg_132_0._shelterIndex

	def SpawnEnvironment(arg_133_0, arg_133_1):
		var_133_0 = arg_133_0.GernerateEnvironmentID()
		var_133_1 = BattleEnvironmentUnit.New(var_133_0, BattleConfig.FOE_CODE)

		var_133_1.SetTemplate(arg_133_1)

		var_133_2 = var_133_1.GetBehaviours()
		var_133_3 = Vector3(arg_133_1.coordinate[1], arg_133_1.coordinate[2], arg_133_1.coordinate[3])

		def var_133_4(arg_134_0):
			var_134_0 = table()

			for iter_134_0, iter_134_1 in ipairs(arg_134_0):
				if iter_134_1.Active:
					var_134_1 = arg_133_0._unitList[iter_134_1.UID]

					if not var_134_1.IsSpectre():
						table.insert(var_134_0, var_134_1)

			var_133_1.UpdateFrequentlyCollide(var_134_0)

		def var_133_5():
			return

		def var_133_6():
			return

		var_133_7 = arg_133_1.field_type or BattleConst.BulletField.SURFACE
		var_133_8 = arg_133_1.IFF or BattleConfig.FOE_CODE
		var_133_9 = 0
		var_133_10

		if len(arg_133_1.cld_data) == 1:
			var_133_11 = arg_133_1.cld_data[1]

			var_133_10 = arg_133_0.SpawnLastingColumnArea(var_133_7, var_133_8, var_133_3, var_133_11, var_133_9, var_133_4, var_133_5, False, arg_133_1.prefab, var_133_6, True)
		else:
			var_133_12 = arg_133_1.cld_data[1]
			var_133_13 = arg_133_1.cld_data[2]

			var_133_10 = arg_133_0.SpawnLastingCubeArea(var_133_7, var_133_8, var_133_3, var_133_12, var_133_13, var_133_9, var_133_4, var_133_5, False, arg_133_1.prefab, var_133_6, True)

		var_133_1.SetAOEData(var_133_10)

		arg_133_0._environmentList[var_133_0] = var_133_1

		return var_133_1

	def RemoveEnvironment(arg_137_0, arg_137_1):
		var_137_0 = arg_137_0._environmentList[arg_137_1]
		var_137_1 = var_137_0.GetAOEData()

		arg_137_0.RemoveAreaOfEffect(var_137_1.GetUniqueID())
		var_137_0.Dispose()

		arg_137_0._environmentList[arg_137_1] = None

	def DispatchWarning(arg_138_0, arg_138_1, arg_138_2):
		arg_138_0.DispatchEvent(Event.New(BattleEvent.UPDATE_ENVIRONMENT_WARNING, table(
			isActive = arg_138_1
		)))

	def GetEnvironmentList(arg_139_0):
		return arg_139_0._environmentList

	def GernerateEnvironmentID(arg_140_0):
		arg_140_0._environmentIndex = arg_140_0._environmentIndex + 1

		return arg_140_0._environmentIndex

	def SpawnEffect(arg_141_0, arg_141_1, arg_141_2, arg_141_3):
		arg_141_0.DispatchEvent(Event.New(BattleEvent.ADD_EFFECT, table(
			FXID = arg_141_1,
			position = arg_141_2,
			localScale = arg_141_3
		)))

	def SpawnUIFX(arg_142_0, arg_142_1, arg_142_2, arg_142_3, arg_142_4):
		arg_142_0.DispatchEvent(Event.New(BattleEvent.ADD_UI_FX, table(
			FXID = arg_142_1,
			position = arg_142_2,
			localScale = arg_142_3,
			orderDiff = arg_142_4
		)))

	def SpawnCameraFX(arg_143_0, arg_143_1, arg_143_2, arg_143_3, arg_143_4):
		arg_143_0.DispatchEvent(Event.New(BattleEvent.ADD_CAMERA_FX, table(
			FXID = arg_143_1,
			position = arg_143_2,
			localScale = arg_143_3,
			orderDiff = arg_143_4
		)))

	def GetFriendlyCode(arg_144_0):
		return arg_144_0._friendlyCode

	def GetFoeCode(arg_145_0):
		return arg_145_0._foeCode

	def GetOppoSideCode(arg_146_0):
		if arg_146_0 == BattleConfig.FRIENDLY_CODE:
			return BattleConfig.FOE_CODE
		elif arg_146_0 == BattleConfig.FOE_CODE:
			return BattleConfig.FRIENDLY_CODE

	def GetStatistics(arg_147_0):
		return arg_147_0._statistics

	def BlockManualCast(arg_148_0, arg_148_1):
		var_148_0 = arg_148_1 and 1 or -1

		for iter_148_0, iter_148_1 in pairs(arg_148_0._fleetList):
			iter_148_1.SetWeaponBlock(var_148_0)

	def JamManualCast(arg_149_0, arg_149_1):
		arg_149_0.DispatchEvent(Event.New(BattleEvent.JAMMING, table(
			jammingFlag = arg_149_1
		)))

	def SubmarineStrike(arg_150_0, arg_150_1):
		var_150_0 = arg_150_0.GetFleetByIFF(arg_150_1)
		var_150_1 = var_150_0.GetSubAidVO()

		if var_150_0.GetWeaponBlock() or var_150_1.GetCurrent() < 1:
			return

		var_150_2 = var_150_0.GetSubUnitData()

		for iter_150_0, iter_150_1 in ipairs(var_150_2):
			var_150_3 = arg_150_0.SpawnSub(iter_150_1, arg_150_1)

			arg_150_0.InitAidUnitStatistics(var_150_3)

		var_150_0.SubWarcry()

		var_150_4 = var_150_0.GetSubList()

		for iter_150_2, iter_150_3 in ipairs(var_150_4):
			if iter_150_2 == 1:
				iter_150_3.TriggerBuff(BattleConst.BuffEffectType.ON_SUB_LEADER)
			elif iter_150_2 == 2:
				iter_150_3.TriggerBuff(BattleConst.BuffEffectType.ON_UPPER_SUB_CONSORT)
			elif iter_150_2 == 3:
				iter_150_3.TriggerBuff(BattleConst.BuffEffectType.ON_LOWER_SUB_CONSORT)

			if iter_150_3.GetAimBias():
				arg_150_0.DispatchEvent(Event.New(BattleEvent.ADD_AIM_BIAS, table(
					aimBias = iter_150_3.GetAimBias()
				)))

		var_150_5 = var_150_4[1]

		var_150_1.Cast()

	def GetWaveFlags(arg_151_0):
		return arg_151_0._waveFlags

	def AddWaveFlag(arg_152_0, arg_152_1):
		if not arg_152_1:
			return

		var_152_0 = arg_152_0.GetWaveFlags()

		if table.contains(var_152_0, arg_152_1):
			return

		table.insert(var_152_0, arg_152_1)

	def RemoveFlag(arg_153_0, arg_153_1):
		if not arg_153_1:
			return

		var_153_0 = arg_153_0.GetWaveFlags()

		if not table.contains(var_153_0, arg_153_1):
			return

		table.removebyvalue(var_153_0, arg_153_1)

	def DispatchCustomWarning(arg_154_0, arg_154_1):
		arg_154_0.DispatchEvent(Event.New(BattleEvent.EDIT_CUSTOM_WARNING_LABEL, table(
			labelData = arg_154_1
		)))

	def DispatchGridmanSkill(arg_155_0, arg_155_1, arg_155_2):
		arg_155_0.DispatchEvent(Event.New(BattleEvent.GRIDMAN_SKILL_FLOAT, table(
			type = arg_155_1,
			IFF = arg_155_2
		)))

	def SpawnFusionUnit(arg_156_0, arg_156_1, arg_156_2, arg_156_3, arg_156_4):
		var_156_0 = Clone(arg_156_1.GetPosition())
		var_156_1 = arg_156_1.GetIFF()
		var_156_2 = arg_156_0.generatePlayerUnit(arg_156_2, var_156_1, var_156_0, arg_156_0._commanderBuff)

		BattleAttr.SetFusionAttrFromElement(var_156_2, arg_156_1, arg_156_3, arg_156_4)
		var_156_2.SetCurrentHP(var_156_2.GetMaxHP())
		arg_156_1.GetFleetVO().AppendPlayerUnit(var_156_2)
		arg_156_0.setShipUnitBound(var_156_2)
		BattleDataFunction.AttachWeather(var_156_2, arg_156_0._weahter)
		arg_156_0._cldSystem.InitShipCld(var_156_2)

		var_156_3 = table(
			type = BattleConst.UnitType.PLAYER_UNIT,
			unit = var_156_2
		)

		arg_156_0.DispatchEvent(Event.New(BattleEvent.ADD_UNIT, var_156_3))

		return var_156_2

	def DefusionUnit(arg_157_0, arg_157_1):
		var_157_0 = arg_157_1.GetIFF()
		var_157_1 = arg_157_0.GetFleetByIFF(var_157_0)

		var_157_1.RemovePlayerUnit(arg_157_1)

		var_157_2 = table()

		if var_157_1.GetFleetAntiAirWeapon().GetRange() == 0:
			var_157_2.isShow = False

		arg_157_0.DispatchEvent(Event.New(BattleEvent.ANTI_AIR_AREA, var_157_2))
		arg_157_1.SetDeathReason(BattleConst.UnitDeathReason.DEFUSION)
		arg_157_0.KillUnit(arg_157_1.GetUniqueID())

	def FreezeUnit(arg_158_0, arg_158_1):
		BattleAttr.SetCurrent(arg_158_1, BattleBuffSetBattleUnitType.ATTR_KEY, BattleConfig.FUSION_ELEMENT_UNIT_TYPE)
		arg_158_1.UpdateBlindInvisibleBySpectre()
		arg_158_0.SwitchSpectreUnit(arg_158_1)

		if arg_158_1.GetAimBias():
			var_158_0 = arg_158_1.GetAimBias()

			var_158_0.RemoveCrew(arg_158_1)

			if var_158_0.GetCurrentState() == var_158_0.STATE_EXPIRE:
				arg_158_0.DispatchEvent(Event.New(BattleEvent.REMOVE_AIM_BIAS, table(
					aimBias = arg_158_1.GetAimBias()
				)))

		arg_158_1.Freeze()

		var_158_1 = arg_158_1.GetFleetVO()

		if var_158_1:
			var_158_1.FreezeUnit(arg_158_1)

	def ActiveFreezeUnit(arg_159_0, arg_159_1):
		BattleAttr.SetCurrent(arg_159_1, BattleBuffSetBattleUnitType.ATTR_KEY, BattleConfig.PLAYER_DEFAULT)
		arg_159_1.UpdateBlindInvisibleBySpectre()
		arg_159_0.SwitchSpectreUnit(arg_159_1)
		BattleDataFunction.AttachWeather(arg_159_1, arg_159_0._weahter)
		arg_159_1.ActiveFreeze()

		var_159_0 = arg_159_1.GetFleetVO()

		if var_159_0:
			var_159_0.ActiveFreezeUnit(arg_159_1)
