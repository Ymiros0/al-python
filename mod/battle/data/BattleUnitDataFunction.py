from luatable import pairs, ipairs, table, Clone

import ys
import BattleConst
import BattleConfig
import BattleAttr
import BattleDataFunction
from model.vo import Ship, Equipment
from model.const import TeamType, ShipType, AttributeType, EquipType
from view.helper import ShipWordHelper
from const import *
ship_data_statistics = pg.ship_data_statistics
ship_data_template = pg.ship_data_template
ship_skin_template = pg.ship_skin_template
enemy_data_statistics = pg.enemy_data_statistics
weapon_property = pg.weapon_property
formation_template = pg.formation_template
auto_pilot_template = pg.auto_pilot_template
aircraft_template = pg.aircraft_template
ship_skin_words = pg.ship_skin_words
equip_data_statistics = pg.equip_data_statistics
equip_data_template = pg.equip_data_template
spweapon_data_statistics = pg.spweapon_data_statistics
enemy_data_skill = pg.enemy_data_skill
ship_data_personality = pg.ship_data_personality
enemy_data_by_type = pg.enemy_data_by_type
ship_data_by_type = pg.ship_data_by_type
ship_level = pg.ship_level
skill_data_template = pg.skill_data_template
ship_data_trans = pg.ship_data_trans
battle_environment_behaviour_template = pg.battle_environment_behaviour_template
equip_skin_template = pg.equip_skin_template
activity_template = pg.activity_template
activity_event_worldboss = pg.activity_event_worldboss
world_joint_boss_template = pg.world_joint_boss_template
world_boss_level = pg.world_boss_level
guild_boss_event = pg.guild_boss_event
ship_strengthen_meta = pg.ship_strengthen_meta
map_data = pg.map_data
strategy_data_template = pg.strategy_data_template

def CreateBattleUnitData(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5, arg_1_6, arg_1_7, arg_1_8, arg_1_9, arg_1_10, arg_1_11):
	var_1_0
	var_1_1

	if arg_1_1 == BattleConst.UnitType.PLAYER_UNIT:
		var_1_0 = ys.Battle.BattlePlayerUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)

		var_1_1 = Ship.WEAPON_COUNT
	elif arg_1_1 == BattleConst.UnitType.SUB_UNIT:
		var_1_0 = ys.Battle.BattleSubUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)

		var_1_1 = Ship.WEAPON_COUNT
	elif arg_1_1 == BattleConst.UnitType.ENEMY_UNIT:
		var_1_0 = ys.Battle.BattleEnemyUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetOverrideLevel(arg_1_11)
	elif arg_1_1 == BattleConst.UnitType.MINION_UNIT:
		var_1_0 = ys.Battle.BattleMinionUnit.New(arg_1_0, arg_1_2)
	elif arg_1_1 == BattleConst.UnitType.BOSS_UNIT:
		var_1_0 = ys.Battle.BattleBossUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetOverrideLevel(arg_1_11)
	elif arg_1_1 == BattleConst.UnitType.CONST_UNIT:
		var_1_0 = ys.Battle.BattleConstPlayerUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)

		var_1_1 = Ship.WEAPON_COUNT
	elif arg_1_1 == BattleConst.UnitType.CARDPUZZLE_PLAYER_UNIT:
		var_1_0 = ys.Battle.BattleCardPuzzlePlayerUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)
	elif arg_1_1 == BattleConst.UnitType.SUPPORT_UNIT:
		var_1_0 = ys.Battle.BattleSupportUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)

	var_1_0.SetTemplate(arg_1_3, arg_1_6, arg_1_7)

	var_1_2 = table()

	if arg_1_1 == BattleConst.UnitType.ENEMY_UNIT or arg_1_1 == BattleConst.UnitType.MINION_UNIT or arg_1_1 == BattleConst.UnitType.BOSS_UNIT:
		for iter_1_0, iter_1_1 in ipairs(arg_1_5):
			var_1_2.append(table(
				equipment = table(
					weapon_id = table(
						iter_1_1.id
					)
				)
			))
	else:
		for iter_1_2, iter_1_3 in ipairs(arg_1_5):
			if not iter_1_3.id:
				var_1_2.append(table(
					equipment = False,
					torpedoAmmo = 0,
					skin = iter_1_3.skin
				))
			else:
				var_1_3 = iter_1_3.equipmentInfo and iter_1_3.equipmentInfo.getConfig("torpedo_ammo") or 0

				if not var_1_1 or iter_1_2 <= var_1_1 or BattleDataFunction.GetWeaponDataFromID(iter_1_3.id).weapon_id:
					var_1_4 = BattleDataFunction.GetWeaponDataFromID(iter_1_3.id)

					var_1_2.append(table(
						equipment = var_1_4,
						skin = iter_1_3.skin,
						torpedoAmmo = var_1_3
					))
				else:
					var_1_2.append(table(
						equipment = False,
						skin = iter_1_3.skin,
						torpedoAmmo = var_1_3
					))

	var_1_0.SetProficiencyList(arg_1_8)
	var_1_0.SetEquipment(var_1_2)

	return var_1_0

def InitUnitSkill(arg_2_0, arg_2_1, arg_2_2):
	var_2_0 = arg_2_0.skills or table()

	for iter_2_0, iter_2_1 in pairs(var_2_0):
		var_2_1 = ys.Battle.BattleBuffUnit.New(iter_2_1.id, iter_2_1.level, arg_2_1)

		arg_2_1.AddBuff(var_2_1)

def GetEquipSkill(arg_3_0, arg_3_1):
	var_3_0 = Ship.WEAPON_COUNT
	var_3_1 = table()

	for iter_3_0, iter_3_1 in ipairs(arg_3_0):
		var_3_2 = iter_3_1.id

		if var_3_2:
			var_3_4 = BattleDataFunction.GetWeaponDataFromID(var_3_2)

			if var_3_4:
				for iter_3_2, iter_3_3 in ipairs(var_3_4.skill_id):
					iter_3_3 = arg_3_1 and BattleDataFunction.SkillTranform(arg_3_1, iter_3_3) or iter_3_3

					table.insert(var_3_1, iter_3_3)

				for iter_3_4, iter_3_5 in ipairs(var_3_4.hidden_skill_id):
					iter_3_5 = arg_3_1 and BattleDataFunction.SkillTranform(arg_3_1, iter_3_5) or iter_3_5

					table.insert(var_3_1, iter_3_5)

	return var_3_1

def AttachWeather(arg_4_0, arg_4_1):
	if table.contains(arg_4_1, BattleConst.WEATHER.NIGHT):
		var_4_0 = arg_4_0.GetTemplate().type

		if arg_4_0.GetFleetVO():
			var_4_1 = arg_4_0.GetFleetVO()

			if table.contains(TeamType.VanguardShipType, var_4_0):
				var_4_2 = var_4_1.GetFleetBias()
				var_4_3 = var_4_2.GetCrewCount() + 1

				var_4_2.ConfigMinRange(BattleConfig.AIM_BIAS_MIN_RANGE_SCOUT[var_4_3])
				var_4_2.AppendCrew(arg_4_0)
			elif table.contains(TeamType.MainShipType, var_4_0):
				var_4_1.AttachCloak(arg_4_0)
			elif table.contains(TeamType.SubShipType, var_4_0):
				var_4_4 = ys.Battle.BattleUnitAimBiasComponent.New()

				var_4_4.ConfigRangeFormula(ys.Battle.BattleFormulas.CalculateMaxAimBiasRangeSub, ys.Battle.BattleFormulas.CalculateBiasDecay)
				var_4_4.ConfigMinRange(BattleConfig.AIM_BIAS_MIN_RANGE_SUB)
				var_4_4.AppendCrew(arg_4_0)
				var_4_4.Active(var_4_4.STATE_ACTIVITING)
		elif arg_4_0.GetUnitType() == BattleConst.UnitType.ENEMY_UNIT or arg_4_0.GetUnitType() == BattleConst.UnitType.MINION_UNIT or arg_4_0.GetUnitType() == BattleConst.UnitType.BOSS_UNIT:
			var_4_5 = ys.Battle.BattleUnitAimBiasComponent.New()

			var_4_5.ConfigRangeFormula(ys.Battle.BattleFormulas.CalculateMaxAimBiasRangeMonster, ys.Battle.BattleFormulas.CalculateBiasDecayMonster)

			if table.contains(TeamType.SubShipType, var_4_0):
				var_4_5.ConfigMinRange(BattleConfig.AIM_BIAS_MIN_RANGE_SUB)
			else:
				var_4_5.ConfigMinRange(BattleConfig.AIM_BIAS_MIN_RANGE_MONSTER)

			var_4_5.AppendCrew(arg_4_0)
			var_4_5.SetHostile()
			var_4_5.Active(var_4_5.STATE_SUMMON_SICKNESS)

def AttachSmoke(arg_5_0):
	var_5_0 = arg_5_0.GetUnitType()

	if var_5_0 == BattleConst.UnitType.ENEMY_UNIT or var_5_0 == BattleConst.UnitType.BOSS_UNIT:
		if arg_5_0.GetAimBias():
			var_5_1 = arg_5_0.GetAimBias()
			var_5_2 = var_5_1.GetCurrentState()

			if var_5_2 == var_5_1.STATE_SKILL_EXPOSE:
				var_5_1.SomkeExitResume()
			elif var_5_2 == var_5_1.STATE_ACTIVITING or var_5_2 == var_5_1.STATE_TOTAL_EXPOSE:
				var_5_1.SmokeRecover()
		else:
			var_5_3 = ys.Battle.BattleUnitAimBiasComponent.New()

			var_5_3.ConfigRangeFormula(ys.Battle.BattleFormulas.CalculateMaxAimBiasRangeMonster, ys.Battle.BattleFormulas.CalculateBiasDecayMonsterInSmoke)

			if table.contains(TeamType.SubShipType, shipType): #???
				var_5_3.ConfigMinRange(BattleConfig.AIM_BIAS_MIN_RANGE_SUB)
			else:
				var_5_3.ConfigMinRange(BattleConfig.AIM_BIAS_MIN_RANGE_MONSTER)

			var_5_3.AppendCrew(arg_5_0)
			var_5_3.SetHostile()
			var_5_3.Active(var_5_3.STATE_ACTIVITING)

def InitEquipSkill(arg_6_0, arg_6_1, arg_6_2):
	var_6_0 = GetEquipSkill(arg_6_0, arg_6_2)

	for iter_6_0, iter_6_1 in ipairs(var_6_0):
		var_6_1 = ys.Battle.BattleBuffUnit.New(iter_6_1, 1, arg_6_1)

		arg_6_1.AddBuff(var_6_1)

def InitCommanderSkill(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0 = arg_7_0 or table()

	var_7_0 = ys.Battle.BattleState.GetInstance().GetBattleType()

	for iter_7_0, iter_7_1 in pairs(arg_7_0):
		var_7_1 = ys.Battle.BattleDataFunction.GetBuffTemplate(iter_7_1.id, iter_7_1.level).limit
		var_7_2 = False

		if var_7_1:
			for iter_7_2, iter_7_3 in ipairs(var_7_1):
				if var_7_0 == iter_7_3:
					var_7_2 = True

					break

		if not var_7_2:
			var_7_3 = ys.Battle.BattleBuffUnit.New(iter_7_1.id, iter_7_1.level, arg_7_1)

			var_7_3.SetCommander(iter_7_1.commander)
			arg_7_1.AddBuff(var_7_3)

def CreateWeaponUnit(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4):
	arg_8_3 = arg_8_3 or -1

	var_8_0 = arg_8_1.GetUnitType()
	var_8_1
	var_8_2 = BattleDataFunction.GetWeaponPropertyDataFromID(arg_8_0)

	assert var_8_2 != None, "找不到武器配置：id = " + arg_8_0

	var_8_3 = arg_8_4 or var_8_2.type

	if var_8_3 == BattleConst.EquipmentType.MAIN_CANNON:
		var_8_1 = ys.Battle.BattleWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.SUB_CANNON:
		var_8_1 = ys.Battle.BattleWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.TORPEDO:
		var_8_1 = ys.Battle.BattleTorpedoUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.MANUAL_TORPEDO:
		var_8_1 = ys.Battle.BattleManualTorpedoUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.ANTI_AIR:
		var_8_1 = ys.Battle.BattleAntiAirUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.FLEET_ANTI_AIR or var_8_3 == BattleConst.EquipmentType.FLEET_RANGE_ANTI_AIR:
		var_8_1 = ys.Battle.BattleWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.INTERCEPT_AIRCRAFT or var_8_3 == BattleConst.EquipmentType.STRIKE_AIRCRAFT:
		if var_8_0 == BattleConst.UnitType.SUPPORT_UNIT:
			var_8_1 = ys.Battle.BattleSupportHiveUnit.New()
		else:
			var_8_1 = ys.Battle.BattleHiveUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.SPECIAL:
		var_8_1 = ys.Battle.BattleSpecialWeapon.New()
	elif var_8_3 == BattleConst.EquipmentType.ANTI_SEA:
		var_8_1 = ys.Battle.BattleDirectHitWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.HAMMER_HEAD:
		var_8_1 = ys.Battle.BattleHammerHeadWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.BOMBER_PRE_CAST_ALERT:
		var_8_1 = ys.Battle.BattleBombWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.POINT_HIT_AND_LOCK or var_8_3 == BattleConst.EquipmentType.MANUAL_MISSILE or var_8_3 == BattleConst.EquipmentType.MANUAL_METEOR:
		var_8_1 = ys.Battle.BattlePointHitWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.BEAM:
		var_8_1 = ys.Battle.BattleLaserUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.DEPTH_CHARGE:
		var_8_1 = ys.Battle.BattleDepthChargeUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.REPEATER_ANTI_AIR:
		var_8_1 = ys.Battle.BattleRepeaterAntiAirUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.DISPOSABLE_TORPEDO:
		var_8_1 = ys.Battle.BattleDisposableTorpedoUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.SPACE_LASER:
		var_8_1 = ys.Battle.BattleSpaceLaserWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.MISSILE:
		var_8_1 = ys.Battle.BattleMissileWeaponUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.MANUAL_AAMISSILE:
		var_8_1 = ys.Battle.BattleManualAAMissileUnit.New()
	elif var_8_3 == BattleConst.EquipmentType.AUTO_MISSILE:
		var_8_1 = ys.Battle.BattleAutoMissileUnit.New()

	assert var_8_1 != None, "创建武器失败，不存在该类型的武器：id = " + arg_8_0
	var_8_1.SetPotentialFactor(arg_8_2)
	var_8_1.SetEquipmentIndex(arg_8_3)
	var_8_1.SetTemplateData(var_8_2)
	var_8_1.SetHostData(arg_8_1)

	if var_8_0 == BattleConst.UnitType.PLAYER_UNIT:
		if var_8_2.auto_aftercast > 0:
			var_8_1.OverrideGCD(var_8_2.auto_aftercast)
	elif var_8_0 == BattleConst.UnitType.ENEMY_UNIT or BattleConst.UnitType.BOSS_UNIT:
		var_8_1.HostOnEnemy()

	if var_8_2.type == BattleConst.EquipmentType.INTERCEPT_AIRCRAFT or var_8_2.type == BattleConst.EquipmentType.STRIKE_AIRCRAFT:
		var_8_1.EnterCoolDown()

	return var_8_1

def CreateAircraftUnit(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	var_9_0
	var_9_1 = BattleDataFunction.GetAircraftTmpDataFromID(arg_9_1)

	assert var_9_1 != None, "找不到飞机配置：id = " + arg_9_1

	if type(var_9_1.funnel_behavior) == "table":
		if var_9_1.funnel_behavior.hover_range:
			var_9_0 = ys.Battle.BattelUAVUnit.New(arg_9_0)
		elif var_9_1.funnel_behavior.AI:
			var_9_0 = ys.Battle.BattlePatternFunnelUnit.New(arg_9_0)
		else:
			var_9_0 = ys.Battle.BattleFunnelUnit.New(arg_9_0)
	else:
		var_9_0 = ys.Battle.BattleAircraftUnit.New(arg_9_0)

	var_9_0.SetMotherUnit(arg_9_2)
	var_9_0.SetWeanponPotential(arg_9_3)
	var_9_0.SetTemplate(var_9_1)

	return var_9_0

def CreateAllInStrike(arg_10_0):
	var_10_0 = arg_10_0.GetTemplateID()
	var_10_1 = BattleDataFunction.GetPlayerShipModelFromID(var_10_0)
	var_10_2 = 0
	var_10_3 = table()

	for iter_10_0, iter_10_1 in ipairs(var_10_1.airassist_time):
		var_10_4 = ys.Battle.BattleAllInStrike.New(iter_10_1)

		var_10_4.SetHost(arg_10_0)

		var_10_3[iter_10_0] = var_10_4

	return var_10_3

def ExpandAllinStrike(arg_11_0):
	var_11_0 = arg_11_0.GetTemplateID()
	var_11_1 = BattleDataFunction.GetPlayerShipModelFromID(var_11_0).airassist_time

	if var_11_1:
		var_11_2 = var_11_1[len(var_11_1)]
		var_11_3 = ys.Battle.BattleAllInStrike.New(var_11_2)

		var_11_3.SetHost(arg_11_0)
		arg_11_0.GetFleetVO().GetAirAssistVO().AppendWeapon(var_11_3)
		var_11_3.OverHeat()
		arg_11_0.GetAirAssistQueue().AppendWeapon(var_11_3)

		var_11_4 = arg_11_0.GetAirAssistList()

		var_11_4.append(var_11_3)

def CreateAirFighterUnit(arg_12_0, arg_12_1):
	var_12_1 = GetAircraftTmpDataFromID(arg_12_1.templateID)
	var_12_2 = ys.Battle.BattleAirFighterUnit.New(arg_12_0)

	var_12_2.SetWeaponTemplateID(arg_12_1.weaponID)
	var_12_2.SetBackwardWeaponID(arg_12_1.backwardWeaponID)
	var_12_2.SetTemplate(var_12_1)

	return var_12_2

def GetPlayerShipTmpDataFromID(arg_13_0):
	assert ship_data_statistics[arg_13_0] != None, ">>ship_data_statistics<< 找不到玩家船只配置：id = " + arg_13_0

	return Clone(ship_data_statistics[arg_13_0])

def GetPlayerShipModelFromID(arg_14_0):
	assert ship_data_template[arg_14_0] != None, ">>ship_data_template<< 找不到玩家船只模组配置：id = " + arg_14_0

	return ship_data_template[arg_14_0]

def GetPlayerShipSkinDataFromID(arg_15_0):
	assert ship_skin_template[arg_15_0] != None, ">>ship_skin_template<< 找不到舰娘皮肤配置：id = " + arg_15_0

	return ship_skin_template[arg_15_0]

def GetShipTypeTmp(arg_16_0):
	assert ship_data_by_type[arg_16_0] != None, ">>ship_data_by_type<< 找不到舰船类型配置：id = " + arg_16_0

	return ship_data_by_type[arg_16_0]

def GetMonsterTmpDataFromID(arg_17_0):
	assert enemy_data_statistics[arg_17_0] != None, ">>enemy_data_statistics<< 找不到敌方船只配置：id = " + arg_17_0

	return enemy_data_statistics[arg_17_0]

def GetAircraftTmpDataFromID(arg_18_0):
	assert aircraft_template[arg_18_0] != None, ">>aircraft_template<< 找不到飞机配置：id = " + arg_18_0

	return aircraft_template[arg_18_0]

def GetWeaponDataFromID(arg_19_0):
	if arg_19_0 != Equipment.EQUIPMENT_STATE_EMPTY and arg_19_0 != Equipment.EQUIPMENT_STATE_LOCK:
		assert equip_data_statistics[arg_19_0] != None, ">>equip_data_statistics<< 找不到武器类装备配置：id = " + arg_19_0

	return equip_data_statistics[arg_19_0]

def GetEquipDataTemplate(arg_20_0):
	assert equip_data_template[arg_20_0] != None, ">>equip_data_template<< 找不到武器装备模板：id = " + arg_20_0

	return equip_data_template[arg_20_0]

def GetSpWeaponDataFromID(arg_21_0):
	assert spweapon_data_statistics[arg_21_0] != None, ">>spweapon_data_statistics<< 找不到特殊兵装配置：id = " + arg_21_0

	return spweapon_data_statistics[arg_21_0]

def GetWeaponPropertyDataFromID(arg_22_0):
	assert weapon_property[arg_22_0] != None, ">>weapon_property<< 找不到武器行为配置：id = " + arg_22_0

	return weapon_property[arg_22_0]

def GetFormationTmpDataFromID(arg_23_0):
	assert formation_template[arg_23_0] != None, ">>formation_template<<找不到阵型配置：id = " + arg_23_0

	return formation_template[arg_23_0]

def GetAITmpDataFromID(arg_24_0):
	assert auto_pilot_template[arg_24_0] != None, ">>auto_pilot_template<< 找不到移动ai配置：id = " + arg_24_0

	return auto_pilot_template[arg_24_0]

def GetShipPersonality(arg_25_0):
	assert ship_data_personality[arg_25_0] != None, ">>shipPersonality<< 找不到性格配置：id = " + arg_25_0

	return ship_data_personality[arg_25_0]

def GetEnemyTypeDataByType(arg_26_0):
	assert enemy_data_by_type[arg_26_0] != None, ">>enemy_data_by_type<< 找不到怪物类型：type = " + arg_26_0

	return enemy_data_by_type[arg_26_0]

def GetArenaBuffByShipType(arg_27_0):
	return GetShipTypeTmp(arg_27_0).arena_buff

def GetPlayerUnitDurabilityExtraAddition(arg_28_0, arg_28_1):
	if arg_28_0 == SYSTEM_DUEL:
		assert ship_level[arg_28_1] != None, ">>ship_level<< 找不到等级配置：level = " + arg_28_1

		return ship_level[arg_28_1].arena_durability_ratio, ship_level[arg_28_1].arena_durability_add
	else:
		return 1, 0

def GetSkillDataTemplate(arg_29_0):
	assert skill_data_template[arg_29_0] != None, ">>skill_data_template<< 找不到技能配置：id = " + arg_29_0

	return skill_data_template[arg_29_0]

def GetShipTransformDataTemplate(arg_30_0):
	var_30_0 = GetPlayerShipModelFromID(arg_30_0)

	return ship_data_trans[var_30_0.group_type]

def GetShipMetaFromDataTemplate(arg_31_0):
	var_31_0 = GetPlayerShipModelFromID(arg_31_0)

	return ship_strengthen_meta[var_31_0.group_type]

def GetEquipSkinDataFromID(arg_32_0):
	assert equip_skin_template[arg_32_0] != None, ">>equip_skin_template<< 找不到装备皮肤配置：id = " + arg_32_0

	return equip_skin_template[arg_32_0]

def GetEquipSkin(arg_33_0):
	assert equip_skin_template[arg_33_0] != None, ">>equip_skin_template<< 找不到装备皮肤配置：id = " + arg_33_0

	var_33_0 = equip_skin_template[arg_33_0]

	return var_33_0.bullet_name, var_33_0.derivate_bullet, var_33_0.derivate_torpedo, var_33_0.derivate_boom, var_33_0.fire_fx_name, var_33_0.hit_fx_name

def GetEquipSkinSFX(arg_34_0):
	assert equip_skin_template[arg_34_0] != None, ">>equip_skin_template<< 找不到装备皮肤配置：id = " + arg_34_0

	var_34_0 = equip_skin_template[arg_34_0]

	return var_34_0.hit_sfx, var_34_0.miss_sfx

def GetSpecificGuildBossEnemyList(arg_35_0, arg_35_1):
	var_35_0 = guild_boss_event[arg_35_0].expedition_id
	var_35_1 = table()

	if var_35_0[1] == arg_35_1:
		var_35_1 = var_35_0[2]

	return var_35_1

def GetSpecificEnemyList(arg_36_0, arg_36_1):
	var_36_0 = activity_template[arg_36_0]
	var_36_1 = activity_event_worldboss[var_36_0.config_id].ex_expedition_enemy
	var_36_2

	for iter_36_0, iter_36_1 in ipairs(var_36_1):
		if iter_36_1[1] == arg_36_1:
			var_36_2 = iter_36_1[2]

			break

	return var_36_2

def GetMetaBossTemplate(arg_37_0):
	return world_joint_boss_template[arg_37_0]

def GetMetaBossLevelTemplate(arg_38_0, arg_38_1):
	var_38_0 = GetMetaBossTemplate(arg_38_0).boss_level_id + (arg_38_1 - 1)

	return world_boss_level[var_38_0]

def GetSpecificWorldJointEnemyList(arg_39_0, arg_39_1, arg_39_2):
	var_39_0 = GetMetaBossLevelTemplate(arg_39_1, arg_39_2)

	return table(
		var_39_0.enemy_id
	)

def IncreaseAttributes(arg_40_0, arg_40_1, arg_40_2):
	for iter_40_0, iter_40_1 in ipairs(arg_40_2):
		if iter_40_1[arg_40_1] != None and type(iter_40_1[arg_40_1]) == "number":
			arg_40_0 = arg_40_0 + iter_40_1[arg_40_1]

def CreateAirFighterWeaponUnit(arg_41_0, arg_41_1, arg_41_2, arg_41_3):
	var_41_0
	var_41_1 = GetWeaponPropertyDataFromID(arg_41_0)

	assert var_41_1 != None, "找不到武器配置：id = " + arg_41_0

	if var_41_1.type == BattleConst.EquipmentType.MAIN_CANNON:
		var_41_0 = ys.Battle.BattleWeaponUnit.New()
	elif var_41_1.type == BattleConst.EquipmentType.SUB_CANNON:
		var_41_0 = ys.Battle.BattleWeaponUnit.New()
	elif var_41_1.type == BattleConst.EquipmentType.TORPEDO:
		var_41_0 = ys.Battle.BattleTorpedoUnit.New()
	elif var_41_1.type == BattleConst.EquipmentType.ANTI_AIR:
		var_41_0 = ys.Battle.BattleAntiAirUnit.New()
	elif var_41_1.type == BattleConst.EquipmentType.ANTI_SEA:
		var_41_0 = ys.Battle.BattleDirectHitWeaponUnit.New()
	elif var_41_1.type == BattleConst.EquipmentType.HAMMER_HEAD:
		var_41_0 = ys.Battle.BattleHammerHeadWeaponUnit.New()
	elif var_41_1.type == BattleConst.EquipmentType.BOMBER_PRE_CAST_ALERT:
		var_41_0 = ys.Battle.BattleBombWeaponUnit.New()
	elif var_41_1.type == BattleConst.EquipmentType.DEPTH_CHARGE:
		var_41_0 = ys.Battle.BattleDepthChargeUnit.New()

	assert var_41_0 != None, "创建武器失败，不存在该类型的武器：id = " + arg_41_0
	var_41_0.SetPotentialFactor(arg_41_3)

	var_41_2 = Clone(var_41_1)

	var_41_2.spawn_bound = "weapon"

	var_41_0.SetTemplateData(var_41_2)
	var_41_0.SetHostData(arg_41_1, arg_41_2)

	return var_41_0

def GetWords(arg_42_0, arg_42_1, arg_42_2):
	var_42_0, var_42_1, var_42_2 = ShipWordHelper.GetWordAndCV(arg_42_0, arg_42_1, 1, True, arg_42_2)

	return var_42_2

def SkillTranform(arg_43_0, arg_43_1):
	var_43_0 = GetSkillDataTemplate(arg_43_1).system_transform

	if var_43_0[arg_43_0] == None:
		return arg_43_1
	else:
		return var_43_0[arg_43_0]

def GenerateHiddenBuff(arg_44_0):
	var_44_0 = GetPlayerShipModelFromID(arg_44_0).hide_buff_list
	var_44_1 = table()

	for iter_44_0, iter_44_1 in ipairs(var_44_0):
		var_44_2 = table()

		var_44_2.level = 1
		var_44_2.id = iter_44_1
		var_44_1[iter_44_1] = var_44_2

	return var_44_1

def GetDivingFilter(arg_45_0):
	return map_data[arg_45_0].diving_filter

def GeneratePlayerSubmarinPhase(arg_46_0, arg_46_1, arg_46_2, arg_46_3, arg_46_4):
	var_46_0 = arg_46_0 - arg_46_2

	return table(
		table(
			index = 0,
			switchType = 3,
			switchTo = 1,
			switchParam = var_46_0
		),
		table(
			switchParam = 0,
			dive = "STATE_RAID",
			switchTo = 2,
			index = 1,
			switchType = 5
		),
		table(
			index = 2,
			switchType = 1,
			switchTo = 3,
			dive = "STATE_FLOAT",
			switchParam = arg_46_4
		),
		table(
			index = 3,
			switchType = 4,
			switchTo = 4,
			dive = "STATE_RETREAT",
			switchParam = arg_46_1
		),
		table(
			index = 4,
			retreat = True
		)
	)

def GetEnvironmentBehaviour(arg_47_0):
	assert battle_environment_behaviour_template[arg_47_0] != None, ">>battle_environment_behaviour_template<< 找不到环境行为配置：id = " + arg_47_0

	return battle_environment_behaviour_template[arg_47_0]

def AttachUltimateBonus(arg_48_0):
	var_48_0 = arg_48_0.GetTemplateID()

	if not Ship.IsMaxStarByTmpID(var_48_0):
		return

	var_48_1 = GetPlayerShipModelFromID(var_48_0).specific_type

	for iter_48_0, iter_48_1 in ipairs(var_48_1):
		if iter_48_1 == ShipType.SpecificTypeTable.gunner:
			BattleAttr.SetCurrent(arg_48_0, "barrageCounterMod", BattleConst.UltimateBonus.GunnerCountMod)
		elif iter_48_1 == ShipType.SpecificTypeTable.torpedo:
			var_48_2 = ys.Battle.BattleBuffUnit.New(BattleConst.UltimateBonus.TorpedoBarrageBuff)

			arg_48_0.AddBuff(var_48_2)
		elif iter_48_1 == ShipType.SpecificTypeTable.auxiliary:
			AuxBoost(arg_48_0)

def AuxBoost(arg_49_0):
	var_49_0 = arg_49_0.GetEquipment()

	for iter_49_0, iter_49_1 in ipairs(var_49_0):
		if iter_49_1 and iter_49_1.equipment and table.contains(EquipType.DeviceEquipTypes, iter_49_1.equipment.type):
			var_49_1 = iter_49_1.equipment

			for iter_49_2 in range(1, 4):
				var_49_2 = "attribute_" + iter_49_2

				if var_49_1[var_49_2]:
					var_49_3 = var_49_1["value_" + iter_49_2]
					var_49_4 = AttributeType.ConvertBattleAttrName(var_49_1[var_49_2])
					var_49_5 = BattleAttr.GetBase(arg_49_0, var_49_4) + var_49_3 * BattleConst.UltimateBonus.AuxBoostValue

					BattleAttr.SetCurrent(arg_49_0, var_49_4, var_49_5)
					BattleAttr.SetBaseAttr(arg_49_0)

def GetSLGStrategyBuffByCombatBuffID(arg_50_0):
	for iter_50_0, iter_50_1 in pairs(strategy_data_template):
		if iter_50_1.buff_id == arg_50_0:
			return iter_50_1
