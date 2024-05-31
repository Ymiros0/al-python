ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleAttr
local var_0_4 = pg.ship_data_statistics
local var_0_5 = pg.ship_data_template
local var_0_6 = pg.ship_skin_template
local var_0_7 = pg.enemy_data_statistics
local var_0_8 = pg.weapon_property
local var_0_9 = pg.formation_template
local var_0_10 = pg.auto_pilot_template
local var_0_11 = pg.aircraft_template
local var_0_12 = pg.ship_skin_words
local var_0_13 = pg.equip_data_statistics
local var_0_14 = pg.equip_data_template
local var_0_15 = pg.spweapon_data_statistics
local var_0_16 = pg.enemy_data_skill
local var_0_17 = pg.ship_data_personality
local var_0_18 = pg.enemy_data_by_type
local var_0_19 = pg.ship_data_by_type
local var_0_20 = pg.ship_level
local var_0_21 = pg.skill_data_template
local var_0_22 = pg.ship_data_trans
local var_0_23 = pg.battle_environment_behaviour_template
local var_0_24 = pg.equip_skin_template
local var_0_25 = pg.activity_template
local var_0_26 = pg.activity_event_worldboss
local var_0_27 = pg.world_joint_boss_template
local var_0_28 = pg.world_boss_level
local var_0_29 = pg.guild_boss_event
local var_0_30 = pg.ship_strengthen_meta
local var_0_31 = pg.map_data
local var_0_32 = pg.strategy_data_template

var_0_0.Battle.BattleDataFunction = var_0_0.Battle.BattleDataFunction or {}

local var_0_33 = var_0_0.Battle.BattleDataFunction

def var_0_33.CreateBattleUnitData(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5, arg_1_6, arg_1_7, arg_1_8, arg_1_9, arg_1_10, arg_1_11):
	local var_1_0
	local var_1_1

	if arg_1_1 == var_0_1.UnitType.PLAYER_UNIT:
		var_1_0 = var_0_0.Battle.BattlePlayerUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)

		var_1_1 = Ship.WEAPON_COUNT
	elif arg_1_1 == var_0_1.UnitType.SUB_UNIT:
		var_1_0 = var_0_0.Battle.BattleSubUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)

		var_1_1 = Ship.WEAPON_COUNT
	elif arg_1_1 == var_0_1.UnitType.ENEMY_UNIT:
		var_1_0 = var_0_0.Battle.BattleEnemyUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetOverrideLevel(arg_1_11)
	elif arg_1_1 == var_0_1.UnitType.MINION_UNIT:
		var_1_0 = var_0_0.Battle.BattleMinionUnit.New(arg_1_0, arg_1_2)
	elif arg_1_1 == var_0_1.UnitType.BOSS_UNIT:
		var_1_0 = var_0_0.Battle.BattleBossUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetOverrideLevel(arg_1_11)
	elif arg_1_1 == var_0_1.UnitType.CONST_UNIT:
		var_1_0 = var_0_0.Battle.BattleConstPlayerUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)

		var_1_1 = Ship.WEAPON_COUNT
	elif arg_1_1 == var_0_1.UnitType.CARDPUZZLE_PLAYER_UNIT:
		var_1_0 = var_0_0.Battle.BattleCardPuzzlePlayerUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)
	elif arg_1_1 == var_0_1.UnitType.SUPPORT_UNIT:
		var_1_0 = var_0_0.Battle.BattleSupportUnit.New(arg_1_0, arg_1_2)

		var_1_0.SetSkinId(arg_1_4)
		var_1_0.SetWeaponInfo(arg_1_9, arg_1_10)

	var_1_0.SetTemplate(arg_1_3, arg_1_6, arg_1_7)

	local var_1_2 = {}

	if arg_1_1 == var_0_1.UnitType.ENEMY_UNIT or arg_1_1 == var_0_1.UnitType.MINION_UNIT or arg_1_1 == var_0_1.UnitType.BOSS_UNIT:
		for iter_1_0, iter_1_1 in ipairs(arg_1_5):
			var_1_2[#var_1_2 + 1] = {
				equipment = {
					weapon_id = {
						iter_1_1.id
					}
				}
			}
	else
		for iter_1_2, iter_1_3 in ipairs(arg_1_5):
			if not iter_1_3.id:
				var_1_2[#var_1_2 + 1] = {
					equipment = False,
					torpedoAmmo = 0,
					skin = iter_1_3.skin
				}
			else
				local var_1_3 = iter_1_3.equipmentInfo and iter_1_3.equipmentInfo.getConfig("torpedo_ammo") or 0

				if not var_1_1 or iter_1_2 <= var_1_1 or #var_0_33.GetWeaponDataFromID(iter_1_3.id).weapon_id:
					local var_1_4 = var_0_33.GetWeaponDataFromID(iter_1_3.id)

					var_1_2[#var_1_2 + 1] = {
						equipment = var_1_4,
						skin = iter_1_3.skin,
						torpedoAmmo = var_1_3
					}
				else
					var_1_2[#var_1_2 + 1] = {
						equipment = False,
						skin = iter_1_3.skin,
						torpedoAmmo = var_1_3
					}

	var_1_0.SetProficiencyList(arg_1_8)
	var_1_0.SetEquipment(var_1_2)

	return var_1_0

def var_0_33.InitUnitSkill(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0.skills or {}

	for iter_2_0, iter_2_1 in pairs(var_2_0):
		local var_2_1 = var_0_0.Battle.BattleBuffUnit.New(iter_2_1.id, iter_2_1.level, arg_2_1)

		arg_2_1.AddBuff(var_2_1)

def var_0_33.GetEquipSkill(arg_3_0, arg_3_1):
	local var_3_0 = Ship.WEAPON_COUNT
	local var_3_1 = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0):
		local var_3_2 = iter_3_1.id

		if var_3_2:
			local var_3_3
			local var_3_4 = var_0_33.GetWeaponDataFromID(var_3_2)

			if var_3_4:
				for iter_3_2, iter_3_3 in ipairs(var_3_4.skill_id):
					iter_3_3 = arg_3_1 and var_0_33.SkillTranform(arg_3_1, iter_3_3) or iter_3_3

					table.insert(var_3_1, iter_3_3)

				for iter_3_4, iter_3_5 in ipairs(var_3_4.hidden_skill_id):
					iter_3_5 = arg_3_1 and var_0_33.SkillTranform(arg_3_1, iter_3_5) or iter_3_5

					table.insert(var_3_1, iter_3_5)

	return var_3_1

def var_0_33.AttachWeather(arg_4_0, arg_4_1):
	if table.contains(arg_4_1, var_0_1.WEATHER.NIGHT):
		local var_4_0 = arg_4_0.GetTemplate().type

		if arg_4_0.GetFleetVO():
			local var_4_1 = arg_4_0.GetFleetVO()

			if table.contains(TeamType.VanguardShipType, var_4_0):
				local var_4_2 = var_4_1.GetFleetBias()
				local var_4_3 = var_4_2.GetCrewCount() + 1

				var_4_2.ConfigMinRange(var_0_2.AIM_BIAS_MIN_RANGE_SCOUT[var_4_3])
				var_4_2.AppendCrew(arg_4_0)
			elif table.contains(TeamType.MainShipType, var_4_0):
				var_4_1.AttachCloak(arg_4_0)
			elif table.contains(TeamType.SubShipType, var_4_0):
				local var_4_4 = var_0_0.Battle.BattleUnitAimBiasComponent.New()

				var_4_4.ConfigRangeFormula(var_0_0.Battle.BattleFormulas.CalculateMaxAimBiasRangeSub, var_0_0.Battle.BattleFormulas.CalculateBiasDecay)
				var_4_4.ConfigMinRange(var_0_2.AIM_BIAS_MIN_RANGE_SUB)
				var_4_4.AppendCrew(arg_4_0)
				var_4_4.Active(var_4_4.STATE_ACTIVITING)
		elif arg_4_0.GetUnitType() == var_0_1.UnitType.ENEMY_UNIT or arg_4_0.GetUnitType() == var_0_1.UnitType.MINION_UNIT or arg_4_0.GetUnitType() == var_0_1.UnitType.BOSS_UNIT:
			local var_4_5 = var_0_0.Battle.BattleUnitAimBiasComponent.New()

			var_4_5.ConfigRangeFormula(var_0_0.Battle.BattleFormulas.CalculateMaxAimBiasRangeMonster, var_0_0.Battle.BattleFormulas.CalculateBiasDecayMonster)

			if table.contains(TeamType.SubShipType, var_4_0):
				var_4_5.ConfigMinRange(var_0_2.AIM_BIAS_MIN_RANGE_SUB)
			else
				var_4_5.ConfigMinRange(var_0_2.AIM_BIAS_MIN_RANGE_MONSTER)

			var_4_5.AppendCrew(arg_4_0)
			var_4_5.SetHostile()
			var_4_5.Active(var_4_5.STATE_SUMMON_SICKNESS)

def var_0_33.AttachSmoke(arg_5_0):
	local var_5_0 = arg_5_0.GetUnitType()

	if var_5_0 == var_0_1.UnitType.ENEMY_UNIT or var_5_0 == var_0_1.UnitType.BOSS_UNIT:
		if arg_5_0.GetAimBias():
			local var_5_1 = arg_5_0.GetAimBias()
			local var_5_2 = var_5_1.GetCurrentState()

			if var_5_2 == var_5_1.STATE_SKILL_EXPOSE:
				var_5_1.SomkeExitResume()
			elif var_5_2 == var_5_1.STATE_ACTIVITING or var_5_2 == var_5_1.STATE_TOTAL_EXPOSE:
				var_5_1.SmokeRecover()
		else
			local var_5_3 = var_0_0.Battle.BattleUnitAimBiasComponent.New()

			var_5_3.ConfigRangeFormula(var_0_0.Battle.BattleFormulas.CalculateMaxAimBiasRangeMonster, var_0_0.Battle.BattleFormulas.CalculateBiasDecayMonsterInSmoke)

			if table.contains(TeamType.SubShipType, shipType):
				var_5_3.ConfigMinRange(var_0_2.AIM_BIAS_MIN_RANGE_SUB)
			else
				var_5_3.ConfigMinRange(var_0_2.AIM_BIAS_MIN_RANGE_MONSTER)

			var_5_3.AppendCrew(arg_5_0)
			var_5_3.SetHostile()
			var_5_3.Active(var_5_3.STATE_ACTIVITING)

def var_0_33.InitEquipSkill(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = var_0_33.GetEquipSkill(arg_6_0, arg_6_2)

	for iter_6_0, iter_6_1 in ipairs(var_6_0):
		local var_6_1 = var_0_0.Battle.BattleBuffUnit.New(iter_6_1, 1, arg_6_1)

		arg_6_1.AddBuff(var_6_1)

def var_0_33.InitCommanderSkill(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0 = arg_7_0 or {}

	local var_7_0 = var_0_0.Battle.BattleState.GetInstance().GetBattleType()

	for iter_7_0, iter_7_1 in pairs(arg_7_0):
		local var_7_1 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(iter_7_1.id, iter_7_1.level).limit
		local var_7_2 = False

		if var_7_1:
			for iter_7_2, iter_7_3 in ipairs(var_7_1):
				if var_7_0 == iter_7_3:
					var_7_2 = True

					break

		if not var_7_2:
			local var_7_3 = var_0_0.Battle.BattleBuffUnit.New(iter_7_1.id, iter_7_1.level, arg_7_1)

			var_7_3.SetCommander(iter_7_1.commander)
			arg_7_1.AddBuff(var_7_3)

def var_0_33.CreateWeaponUnit(arg_8_0, arg_8_1, arg_8_2, arg_8_3, arg_8_4):
	arg_8_3 = arg_8_3 or -1

	local var_8_0 = arg_8_1.GetUnitType()
	local var_8_1
	local var_8_2 = var_0_33.GetWeaponPropertyDataFromID(arg_8_0)

	assert(var_8_2 != None, "找不到武器配置：id = " .. arg_8_0)

	local var_8_3 = arg_8_4 or var_8_2.type

	if var_8_3 == var_0_1.EquipmentType.MAIN_CANNON:
		var_8_1 = var_0_0.Battle.BattleWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.SUB_CANNON:
		var_8_1 = var_0_0.Battle.BattleWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.TORPEDO:
		var_8_1 = var_0_0.Battle.BattleTorpedoUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.MANUAL_TORPEDO:
		var_8_1 = var_0_0.Battle.BattleManualTorpedoUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.ANTI_AIR:
		var_8_1 = var_0_0.Battle.BattleAntiAirUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.FLEET_ANTI_AIR or var_8_3 == var_0_1.EquipmentType.FLEET_RANGE_ANTI_AIR:
		var_8_1 = var_0_0.Battle.BattleWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.INTERCEPT_AIRCRAFT or var_8_3 == var_0_1.EquipmentType.STRIKE_AIRCRAFT:
		if var_8_0 == var_0_1.UnitType.SUPPORT_UNIT:
			var_8_1 = var_0_0.Battle.BattleSupportHiveUnit.New()
		else
			var_8_1 = var_0_0.Battle.BattleHiveUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.SPECIAL:
		var_8_1 = var_0_0.Battle.BattleSpecialWeapon.New()
	elif var_8_3 == var_0_1.EquipmentType.ANTI_SEA:
		var_8_1 = var_0_0.Battle.BattleDirectHitWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.HAMMER_HEAD:
		var_8_1 = var_0_0.Battle.BattleHammerHeadWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.BOMBER_PRE_CAST_ALERT:
		var_8_1 = var_0_0.Battle.BattleBombWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.POINT_HIT_AND_LOCK or var_8_3 == var_0_1.EquipmentType.MANUAL_MISSILE or var_8_3 == var_0_1.EquipmentType.MANUAL_METEOR:
		var_8_1 = var_0_0.Battle.BattlePointHitWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.BEAM:
		var_8_1 = var_0_0.Battle.BattleLaserUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.DEPTH_CHARGE:
		var_8_1 = var_0_0.Battle.BattleDepthChargeUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.REPEATER_ANTI_AIR:
		var_8_1 = var_0_0.Battle.BattleRepeaterAntiAirUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.DISPOSABLE_TORPEDO:
		var_8_1 = var_0_0.Battle.BattleDisposableTorpedoUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.SPACE_LASER:
		var_8_1 = var_0_0.Battle.BattleSpaceLaserWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.MISSILE:
		var_8_1 = var_0_0.Battle.BattleMissileWeaponUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.MANUAL_AAMISSILE:
		var_8_1 = var_0_0.Battle.BattleManualAAMissileUnit.New()
	elif var_8_3 == var_0_1.EquipmentType.AUTO_MISSILE:
		var_8_1 = var_0_0.Battle.BattleAutoMissileUnit.New()

	assert(var_8_1 != None, "创建武器失败，不存在该类型的武器：id = " .. arg_8_0)
	var_8_1.SetPotentialFactor(arg_8_2)
	var_8_1.SetEquipmentIndex(arg_8_3)
	var_8_1.SetTemplateData(var_8_2)
	var_8_1.SetHostData(arg_8_1)

	if var_8_0 == var_0_1.UnitType.PLAYER_UNIT:
		if var_8_2.auto_aftercast > 0:
			var_8_1.OverrideGCD(var_8_2.auto_aftercast)
	elif var_8_0 == var_0_1.UnitType.ENEMY_UNIT or var_0_1.UnitType.BOSS_UNIT:
		var_8_1.HostOnEnemy()

	if var_8_2.type == var_0_1.EquipmentType.INTERCEPT_AIRCRAFT or var_8_2.type == var_0_1.EquipmentType.STRIKE_AIRCRAFT:
		var_8_1.EnterCoolDown()

	return var_8_1

def var_0_33.CreateAircraftUnit(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	local var_9_0
	local var_9_1 = var_0_33.GetAircraftTmpDataFromID(arg_9_1)

	assert(var_9_1 != None, "找不到飞机配置：id = " .. arg_9_1)

	if type(var_9_1.funnel_behavior) == "table":
		if var_9_1.funnel_behavior.hover_range:
			var_9_0 = var_0_0.Battle.BattelUAVUnit.New(arg_9_0)
		elif var_9_1.funnel_behavior.AI:
			var_9_0 = var_0_0.Battle.BattlePatternFunnelUnit.New(arg_9_0)
		else
			var_9_0 = var_0_0.Battle.BattleFunnelUnit.New(arg_9_0)
	else
		var_9_0 = var_0_0.Battle.BattleAircraftUnit.New(arg_9_0)

	var_9_0.SetMotherUnit(arg_9_2)
	var_9_0.SetWeanponPotential(arg_9_3)
	var_9_0.SetTemplate(var_9_1)

	return var_9_0

def var_0_33.CreateAllInStrike(arg_10_0):
	local var_10_0 = arg_10_0.GetTemplateID()
	local var_10_1 = var_0_33.GetPlayerShipModelFromID(var_10_0)
	local var_10_2 = 0
	local var_10_3 = {}

	for iter_10_0, iter_10_1 in ipairs(var_10_1.airassist_time):
		local var_10_4 = var_0_0.Battle.BattleAllInStrike.New(iter_10_1)

		var_10_4.SetHost(arg_10_0)

		var_10_3[iter_10_0] = var_10_4

	return var_10_3

def var_0_33.ExpandAllinStrike(arg_11_0):
	local var_11_0 = arg_11_0.GetTemplateID()
	local var_11_1 = var_0_33.GetPlayerShipModelFromID(var_11_0).airassist_time

	if #var_11_1 > 0:
		local var_11_2 = var_11_1[#var_11_1]
		local var_11_3 = var_0_0.Battle.BattleAllInStrike.New(var_11_2)

		var_11_3.SetHost(arg_11_0)
		arg_11_0.GetFleetVO().GetAirAssistVO().AppendWeapon(var_11_3)
		var_11_3.OverHeat()
		arg_11_0.GetAirAssistQueue().AppendWeapon(var_11_3)

		local var_11_4 = arg_11_0.GetAirAssistList()

		var_11_4[#var_11_4 + 1] = var_11_3

def var_0_33.CreateAirFighterUnit(arg_12_0, arg_12_1):
	local var_12_0
	local var_12_1 = var_0_33.GetAircraftTmpDataFromID(arg_12_1.templateID)
	local var_12_2 = var_0_0.Battle.BattleAirFighterUnit.New(arg_12_0)

	var_12_2.SetWeaponTemplateID(arg_12_1.weaponID)
	var_12_2.SetBackwardWeaponID(arg_12_1.backwardWeaponID)
	var_12_2.SetTemplate(var_12_1)

	return var_12_2

def var_0_33.GetPlayerShipTmpDataFromID(arg_13_0):
	assert(var_0_4[arg_13_0] != None, ">>ship_data_statistics<< 找不到玩家船只配置：id = " .. arg_13_0)

	return Clone(var_0_4[arg_13_0])

def var_0_33.GetPlayerShipModelFromID(arg_14_0):
	assert(var_0_5[arg_14_0] != None, ">>ship_data_template<< 找不到玩家船只模组配置：id = " .. arg_14_0)

	return var_0_5[arg_14_0]

def var_0_33.GetPlayerShipSkinDataFromID(arg_15_0):
	assert(var_0_6[arg_15_0] != None, ">>ship_skin_template<< 找不到舰娘皮肤配置：id = " .. arg_15_0)

	return var_0_6[arg_15_0]

def var_0_33.GetShipTypeTmp(arg_16_0):
	assert(var_0_19[arg_16_0] != None, ">>ship_data_by_type<< 找不到舰船类型配置：id = " .. arg_16_0)

	return var_0_19[arg_16_0]

def var_0_33.GetMonsterTmpDataFromID(arg_17_0):
	assert(var_0_7[arg_17_0] != None, ">>enemy_data_statistics<< 找不到敌方船只配置：id = " .. arg_17_0)

	return var_0_7[arg_17_0]

def var_0_33.GetAircraftTmpDataFromID(arg_18_0):
	assert(var_0_11[arg_18_0] != None, ">>aircraft_template<< 找不到飞机配置：id = " .. arg_18_0)

	return var_0_11[arg_18_0]

def var_0_33.GetWeaponDataFromID(arg_19_0):
	if arg_19_0 != Equipment.EQUIPMENT_STATE_EMPTY and arg_19_0 != Equipment.EQUIPMENT_STATE_LOCK:
		assert(var_0_13[arg_19_0] != None, ">>equip_data_statistics<< 找不到武器类装备配置：id = " .. arg_19_0)

	return var_0_13[arg_19_0]

def var_0_33.GetEquipDataTemplate(arg_20_0):
	assert(var_0_14[arg_20_0] != None, ">>equip_data_template<< 找不到武器装备模板：id = " .. arg_20_0)

	return var_0_14[arg_20_0]

def var_0_33.GetSpWeaponDataFromID(arg_21_0):
	assert(var_0_15[arg_21_0] != None, ">>spweapon_data_statistics<< 找不到特殊兵装配置：id = " .. arg_21_0)

	return var_0_15[arg_21_0]

def var_0_33.GetWeaponPropertyDataFromID(arg_22_0):
	assert(var_0_8[arg_22_0] != None, ">>weapon_property<< 找不到武器行为配置：id = " .. arg_22_0)

	return var_0_8[arg_22_0]

def var_0_33.GetFormationTmpDataFromID(arg_23_0):
	assert(var_0_9[arg_23_0] != None, ">>formation_template<<找不到阵型配置：id = " .. arg_23_0)

	return var_0_9[arg_23_0]

def var_0_33.GetAITmpDataFromID(arg_24_0):
	assert(var_0_10[arg_24_0] != None, ">>auto_pilot_template<< 找不到移动ai配置：id = " .. arg_24_0)

	return var_0_10[arg_24_0]

def var_0_33.GetShipPersonality(arg_25_0):
	assert(var_0_17[arg_25_0] != None, ">>shipPersonality<< 找不到性格配置：id = " .. arg_25_0)

	return var_0_17[arg_25_0]

def var_0_33.GetEnemyTypeDataByType(arg_26_0):
	assert(var_0_18[arg_26_0] != None, ">>enemy_data_by_type<< 找不到怪物类型：type = " .. arg_26_0)

	return var_0_18[arg_26_0]

def var_0_33.GetArenaBuffByShipType(arg_27_0):
	return var_0_33.GetShipTypeTmp(arg_27_0).arena_buff

def var_0_33.GetPlayerUnitDurabilityExtraAddition(arg_28_0, arg_28_1):
	if arg_28_0 == SYSTEM_DUEL:
		assert(var_0_20[arg_28_1] != None, ">>ship_level<< 找不到等级配置：level = " .. arg_28_1)

		return var_0_20[arg_28_1].arena_durability_ratio, var_0_20[arg_28_1].arena_durability_add
	else
		return 1, 0

def var_0_33.GetSkillDataTemplate(arg_29_0):
	assert(var_0_21[arg_29_0] != None, ">>skill_data_template<< 找不到技能配置：id = " .. arg_29_0)

	return var_0_21[arg_29_0]

def var_0_33.GetShipTransformDataTemplate(arg_30_0):
	local var_30_0 = var_0_33.GetPlayerShipModelFromID(arg_30_0)

	return var_0_22[var_30_0.group_type]

def var_0_33.GetShipMetaFromDataTemplate(arg_31_0):
	local var_31_0 = var_0_33.GetPlayerShipModelFromID(arg_31_0)

	return var_0_30[var_31_0.group_type]

def var_0_33.GetEquipSkinDataFromID(arg_32_0):
	assert(var_0_24[arg_32_0] != None, ">>equip_skin_template<< 找不到装备皮肤配置：id = " .. arg_32_0)

	return var_0_24[arg_32_0]

def var_0_33.GetEquipSkin(arg_33_0):
	assert(var_0_24[arg_33_0] != None, ">>equip_skin_template<< 找不到装备皮肤配置：id = " .. arg_33_0)

	local var_33_0 = var_0_24[arg_33_0]

	return var_33_0.bullet_name, var_33_0.derivate_bullet, var_33_0.derivate_torpedo, var_33_0.derivate_boom, var_33_0.fire_fx_name, var_33_0.hit_fx_name

def var_0_33.GetEquipSkinSFX(arg_34_0):
	assert(var_0_24[arg_34_0] != None, ">>equip_skin_template<< 找不到装备皮肤配置：id = " .. arg_34_0)

	local var_34_0 = var_0_24[arg_34_0]

	return var_34_0.hit_sfx, var_34_0.miss_sfx

def var_0_33.GetSpecificGuildBossEnemyList(arg_35_0, arg_35_1):
	local var_35_0 = var_0_29[arg_35_0].expedition_id
	local var_35_1 = {}

	if var_35_0[1] == arg_35_1:
		var_35_1 = var_35_0[2]

	return var_35_1

def var_0_33.GetSpecificEnemyList(arg_36_0, arg_36_1):
	local var_36_0 = var_0_25[arg_36_0]
	local var_36_1 = var_0_26[var_36_0.config_id].ex_expedition_enemy
	local var_36_2

	for iter_36_0, iter_36_1 in ipairs(var_36_1):
		if iter_36_1[1] == arg_36_1:
			var_36_2 = iter_36_1[2]

			break

	return var_36_2

def var_0_33.GetMetaBossTemplate(arg_37_0):
	return var_0_27[arg_37_0]

def var_0_33.GetMetaBossLevelTemplate(arg_38_0, arg_38_1):
	local var_38_0 = var_0_33.GetMetaBossTemplate(arg_38_0).boss_level_id + (arg_38_1 - 1)

	return var_0_28[var_38_0]

def var_0_33.GetSpecificWorldJointEnemyList(arg_39_0, arg_39_1, arg_39_2):
	local var_39_0 = var_0_33.GetMetaBossLevelTemplate(arg_39_1, arg_39_2)

	return {
		var_39_0.enemy_id
	}

def var_0_33.IncreaseAttributes(arg_40_0, arg_40_1, arg_40_2):
	for iter_40_0, iter_40_1 in ipairs(arg_40_2):
		if iter_40_1[arg_40_1] != None and type(iter_40_1[arg_40_1]) == "number":
			arg_40_0 = arg_40_0 + iter_40_1[arg_40_1]

def var_0_33.CreateAirFighterWeaponUnit(arg_41_0, arg_41_1, arg_41_2, arg_41_3):
	local var_41_0
	local var_41_1 = var_0_33.GetWeaponPropertyDataFromID(arg_41_0)

	assert(var_41_1 != None, "找不到武器配置：id = " .. arg_41_0)

	if var_41_1.type == var_0_1.EquipmentType.MAIN_CANNON:
		var_41_0 = var_0_0.Battle.BattleWeaponUnit.New()
	elif var_41_1.type == var_0_1.EquipmentType.SUB_CANNON:
		var_41_0 = var_0_0.Battle.BattleWeaponUnit.New()
	elif var_41_1.type == var_0_1.EquipmentType.TORPEDO:
		var_41_0 = var_0_0.Battle.BattleTorpedoUnit.New()
	elif var_41_1.type == var_0_1.EquipmentType.ANTI_AIR:
		var_41_0 = var_0_0.Battle.BattleAntiAirUnit.New()
	elif var_41_1.type == var_0_1.EquipmentType.ANTI_SEA:
		var_41_0 = var_0_0.Battle.BattleDirectHitWeaponUnit.New()
	elif var_41_1.type == var_0_1.EquipmentType.HAMMER_HEAD:
		var_41_0 = var_0_0.Battle.BattleHammerHeadWeaponUnit.New()
	elif var_41_1.type == var_0_1.EquipmentType.BOMBER_PRE_CAST_ALERT:
		var_41_0 = var_0_0.Battle.BattleBombWeaponUnit.New()
	elif var_41_1.type == var_0_1.EquipmentType.DEPTH_CHARGE:
		var_41_0 = var_0_0.Battle.BattleDepthChargeUnit.New()

	assert(var_41_0 != None, "创建武器失败，不存在该类型的武器：id = " .. arg_41_0)
	var_41_0.SetPotentialFactor(arg_41_3)

	local var_41_2 = Clone(var_41_1)

	var_41_2.spawn_bound = "weapon"

	var_41_0.SetTemplateData(var_41_2)
	var_41_0.SetHostData(arg_41_1, arg_41_2)

	return var_41_0

def var_0_33.GetWords(arg_42_0, arg_42_1, arg_42_2):
	local var_42_0, var_42_1, var_42_2 = ShipWordHelper.GetWordAndCV(arg_42_0, arg_42_1, 1, True, arg_42_2)

	return var_42_2

def var_0_33.SkillTranform(arg_43_0, arg_43_1):
	local var_43_0 = var_0_33.GetSkillDataTemplate(arg_43_1).system_transform

	if var_43_0[arg_43_0] == None:
		return arg_43_1
	else
		return var_43_0[arg_43_0]

def var_0_33.GenerateHiddenBuff(arg_44_0):
	local var_44_0 = var_0_33.GetPlayerShipModelFromID(arg_44_0).hide_buff_list
	local var_44_1 = {}

	for iter_44_0, iter_44_1 in ipairs(var_44_0):
		local var_44_2 = {}

		var_44_2.level = 1
		var_44_2.id = iter_44_1
		var_44_1[iter_44_1] = var_44_2

	return var_44_1

def var_0_33.GetDivingFilter(arg_45_0):
	return var_0_31[arg_45_0].diving_filter

def var_0_33.GeneratePlayerSubmarinPhase(arg_46_0, arg_46_1, arg_46_2, arg_46_3, arg_46_4):
	local var_46_0 = arg_46_0 - arg_46_2

	return {
		{
			index = 0,
			switchType = 3,
			switchTo = 1,
			switchParam = var_46_0
		},
		{
			switchParam = 0,
			dive = "STATE_RAID",
			switchTo = 2,
			index = 1,
			switchType = 5
		},
		{
			index = 2,
			switchType = 1,
			switchTo = 3,
			dive = "STATE_FLOAT",
			switchParam = arg_46_4
		},
		{
			index = 3,
			switchType = 4,
			switchTo = 4,
			dive = "STATE_RETREAT",
			switchParam = arg_46_1
		},
		{
			index = 4,
			retreat = True
		}
	}

def var_0_33.GetEnvironmentBehaviour(arg_47_0):
	assert(var_0_23[arg_47_0] != None, ">>battle_environment_behaviour_template<< 找不到环境行为配置：id = " .. arg_47_0)

	return var_0_23[arg_47_0]

def var_0_33.AttachUltimateBonus(arg_48_0):
	local var_48_0 = arg_48_0.GetTemplateID()

	if not Ship.IsMaxStarByTmpID(var_48_0):
		return

	local var_48_1 = var_0_33.GetPlayerShipModelFromID(var_48_0).specific_type

	for iter_48_0, iter_48_1 in ipairs(var_48_1):
		if iter_48_1 == ShipType.SpecificTypeTable.gunner:
			var_0_3.SetCurrent(arg_48_0, "barrageCounterMod", var_0_1.UltimateBonus.GunnerCountMod)
		elif iter_48_1 == ShipType.SpecificTypeTable.torpedo:
			local var_48_2 = var_0_0.Battle.BattleBuffUnit.New(var_0_1.UltimateBonus.TorpedoBarrageBuff)

			arg_48_0.AddBuff(var_48_2)
		elif iter_48_1 == ShipType.SpecificTypeTable.auxiliary:
			var_0_33.AuxBoost(arg_48_0)

def var_0_33.AuxBoost(arg_49_0):
	local var_49_0 = arg_49_0.GetEquipment()

	for iter_49_0, iter_49_1 in ipairs(var_49_0):
		if iter_49_1 and iter_49_1.equipment and table.contains(EquipType.DeviceEquipTypes, iter_49_1.equipment.type):
			local var_49_1 = iter_49_1.equipment

			for iter_49_2 = 1, 3:
				local var_49_2 = "attribute_" .. iter_49_2

				if var_49_1[var_49_2]:
					local var_49_3 = var_49_1["value_" .. iter_49_2]
					local var_49_4 = AttributeType.ConvertBattleAttrName(var_49_1[var_49_2])
					local var_49_5 = var_0_3.GetBase(arg_49_0, var_49_4) + var_49_3 * var_0_1.UltimateBonus.AuxBoostValue

					var_0_3.SetCurrent(arg_49_0, var_49_4, var_49_5)
					var_0_3.SetBaseAttr(arg_49_0)

def var_0_33.GetSLGStrategyBuffByCombatBuffID(arg_50_0):
	for iter_50_0, iter_50_1 in pairs(var_0_32):
		if iter_50_1.buff_id == arg_50_0:
			return iter_50_1
