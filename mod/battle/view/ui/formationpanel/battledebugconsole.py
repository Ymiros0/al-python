ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleDebugConsole = class("BattleDebugConsole")
var_0_0.Battle.BattleDebugConsole.__name = "BattleDebugConsole"

local var_0_3 = var_0_0.Battle.BattleDebugConsole

var_0_3.ProxyUpdateNormal = var_0_0.Battle.BattleDataProxy.Update
var_0_3.ProxyUpdateAutoComponentNormal = var_0_0.Battle.BattleDataProxy.UpdateAutoComponent
var_0_3.UPDATE_PLAYER_WEAPON = "updatePlayerWeapon"
var_0_3.UPDATE_MONSTER_WEAPON = "updateMonsterWeapon"
var_0_3.UPDATE_MONSTER_AI = "updateMonsterAI"

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._go = arg_1_1
	arg_1_0._state = arg_1_2
	arg_1_0._dataProxy = arg_1_0._state.GetProxyByName(var_0_0.Battle.BattleDataProxy.__name)

	arg_1_0.initComponent()

	if arg_1_0._dataProxy.GetInitData().battleType == SYSTEM_DEBUG or arg_1_0._dataProxy.GetInitData().battleType == SYSTEM_CARDPUZZLE:
		arg_1_0.initData()
		arg_1_0.initDebug()
	else
		SetActive(arg_1_0._debug, False)

def var_0_3.initDebug(arg_2_0):
	arg_2_0._randomEngage = arg_2_0._debug.Find("spawn_enemy")

	onButton(None, arg_2_0._randomEngage, function()
		local var_3_0 = math.random(#arg_2_0._monsterArray)

		arg_2_0.spawnEnemy(arg_2_0._monsterArray[var_3_0], 15, 25, 25, 65), SFX_PANEL)

	arg_2_0._summon = arg_2_0._debug.Find("summon_enemy")
	arg_2_0._summonID = arg_2_0._debug.Find("model_id").GetComponent("InputField")
	arg_2_0._minX = arg_2_0._debug.Find("x_min").GetComponent("InputField")
	arg_2_0._manX = arg_2_0._debug.Find("x_max").GetComponent("InputField")
	arg_2_0._minZ = arg_2_0._debug.Find("z_min").GetComponent("InputField")
	arg_2_0._manZ = arg_2_0._debug.Find("z_max").GetComponent("InputField")

	onButton(None, arg_2_0._summon, function()
		local var_4_0 = tonumber(arg_2_0._summonID.text)
		local var_4_1 = tonumber(arg_2_0._minX.text)
		local var_4_2 = tonumber(arg_2_0._manX.text)
		local var_4_3 = tonumber(arg_2_0._minZ.text)
		local var_4_4 = tonumber(arg_2_0._manZ.text)

		arg_2_0.spawnEnemy(var_4_0, var_4_1, var_4_2, var_4_3, var_4_4), SFX_PANEL)

	arg_2_0._killAllEnemy = arg_2_0._debug.Find("clear_enemy")

	onButton(None, arg_2_0._killAllEnemy, function()
		arg_2_0._dataProxy.KillAllEnemy(), SFX_PANEL)

	arg_2_0._summonStrike = arg_2_0._debug.Find("spawn_strike")
	arg_2_0._summonStrikeID = arg_2_0._debug.Find("air_model_id").GetComponent("InputField")
	arg_2_0._summonStrikeTotal = arg_2_0._debug.Find("total").GetComponent("InputField")
	arg_2_0._summonStrikeSingular = arg_2_0._debug.Find("once").GetComponent("InputField")
	arg_2_0._summonStrikeInterval = arg_2_0._debug.Find("interval").GetComponent("InputField")

	onButton(None, arg_2_0._summonStrike, function()
		local var_6_0 = tonumber(arg_2_0._summonStrikeID.text)
		local var_6_1 = tonumber(arg_2_0._summonStrikeTotal.text)
		local var_6_2 = tonumber(arg_2_0._summonStrikeSingular.text)
		local var_6_3 = tonumber(arg_2_0._summonStrikeInterval.text)

		arg_2_0.spawnStrike(var_6_0, var_6_1, var_6_2, var_6_3), SFX_PANEL)

	arg_2_0._killAllStrike = arg_2_0._debug.Find("clear_strike")

	onButton(None, arg_2_0._killAllStrike, function()
		arg_2_0._dataProxy.KillAllAirStrike(), SFX_PANEL)

	arg_2_0._blockCld = arg_2_0._debug.Find("all_cld")
	arg_2_0._blockPlayerWeapon = arg_2_0._debug.Find("player_weapon")
	arg_2_0._blockMonsterWeapon = arg_2_0._debug.Find("monster_weapon")
	arg_2_0._blockMonsterAI = arg_2_0._debug.Find("monster_motion")

	onToggle(None, arg_2_0._blockCld, function(arg_8_0)
		if arg_8_0:
			arg_2_0._dataProxy.Update = var_0_3.ProxyUpdateNormal
		else
			arg_2_0._dataProxy.Update = arg_2_0._dataProxy.__debug__BlockCldUpdate__, SFX_PANEL)
	onToggle(None, arg_2_0._blockPlayerWeapon, function(arg_9_0)
		if arg_9_0:
			arg_2_0._autoComponentFuncList.updatePlayerWeapon = arg_2_0._updatePlayerWeapon
		else
			arg_2_0._autoComponentFuncList.updatePlayerWeapon = None, SFX_PANEL)
	onToggle(None, arg_2_0._blockMonsterWeapon, function(arg_10_0)
		if arg_10_0:
			arg_2_0._autoComponentFuncList.updateMonsterWeapon = arg_2_0._updateMonsterWeapon
		else
			arg_2_0._autoComponentFuncList.updateMonsterWeapon = None, SFX_PANEL)
	onToggle(None, arg_2_0._blockMonsterAI, function(arg_11_0)
		if arg_11_0:
			arg_2_0._autoComponentFuncList.updateMonsterAI = arg_2_0._updateMonsterAI
		else
			arg_2_0._autoComponentFuncList.updateMonsterAI = None, SFX_PANEL)

	arg_2_0._setDungeonLevel = arg_2_0._debug.Find("dungeon_level")
	arg_2_0._dungeonLevel = arg_2_0._debug.Find("level_input").GetComponent("InputField")

	onButton(None, arg_2_0._setDungeonLevel, function()
		arg_2_0._dataProxy.SetDungeonLevel(tonumber(arg_2_0._dungeonLevel.text)), SFX_PANEL)

	arg_2_0._clsBullet = arg_2_0._debug.Find("cls_bullet")

	onButton(None, arg_2_0._clsBullet, function()
		arg_2_0._dataProxy.CLSBullet(var_0_2.FRIENDLY_CODE)
		arg_2_0._dataProxy.CLSBullet(var_0_2.FOE_CODE), SFX_PANEL)

def var_0_3.initData(arg_14_0):
	arg_14_0._fleetList = arg_14_0._dataProxy.GetFleetList()
	arg_14_0._freeShipList = arg_14_0._dataProxy.GetFreeShipList()
	arg_14_0._monsterArray = {}

	for iter_14_0, iter_14_1 in ipairs(pg.enemy_data_statistics.all):
		if type(iter_14_1) == "number" and iter_14_1 <= 10000000:
			table.insert(arg_14_0._monsterArray, iter_14_1)

	function arg_14_0._updatePlayerWeapon(arg_15_0)
		for iter_15_0, iter_15_1 in pairs(arg_14_0._fleetList):
			iter_15_1.UpdateAutoComponent(arg_15_0)

	function arg_14_0._updateMonsterWeapon(arg_16_0)
		for iter_16_0, iter_16_1 in pairs(arg_14_0._freeShipList):
			iter_16_1.UpdateWeapon(arg_16_0)

	function arg_14_0._updateMonsterAI(arg_17_0)
		for iter_17_0, iter_17_1 in pairs(arg_14_0._dataProxy._teamList):
			if iter_17_1.IsFatalDamage():
				arg_14_0._dataProxy.KillNPCTeam(iter_17_0)
			else
				iter_17_1.UpdateMotion()

	arg_14_0._autoComponentFuncList = {}
	arg_14_0._autoComponentFuncList.updatePlayerWeapon = arg_14_0._updatePlayerWeapon
	arg_14_0._autoComponentFuncList.updateMonsterWeapon = arg_14_0._updateMonsterWeapon
	arg_14_0._autoComponentFuncList.updateMonsterAI = arg_14_0._updateMonsterAI

	local function var_14_0(arg_18_0, arg_18_1)
		for iter_18_0, iter_18_1 in pairs(arg_14_0._autoComponentFuncList):
			iter_18_1(arg_18_1)

	arg_14_0._dataProxy.UpdateAutoComponent = var_14_0

def var_0_3.initComponent(arg_19_0):
	arg_19_0._base = arg_19_0._go.Find("bg")
	arg_19_0._common = arg_19_0._base.Find("common")
	arg_19_0._debug = arg_19_0._base.Find("debug")
	arg_19_0._exitBtn = arg_19_0._common.Find("close")

	onButton(None, arg_19_0._exitBtn, function()
		arg_19_0.SetActive(False), SFX_PANEL)

	arg_19_0._activeReference = arg_19_0._common.Find("reference_switch")

	onButton(None, arg_19_0._activeReference, function()
		arg_19_0.activeReference(), SFX_PANEL)

	arg_19_0._lockCommonDMG = arg_19_0._common.Find("common_damage")
	arg_19_0._lockS2MDMG = arg_19_0._common.Find("ship2main_damage")
	arg_19_0._lockA2MDMG = arg_19_0._common.Find("aircraft2main_damage")
	arg_19_0._lockCrushDMG = arg_19_0._common.Find("crush_damage")

	onToggle(None, arg_19_0._lockCommonDMG, function(arg_22_0)
		arg_19_0._dataProxy.SetupCalculateDamage(arg_22_0 and var_0_0.Battle.BattleFormulas.CalcDamageLock or None), SFX_PANEL)
	onToggle(None, arg_19_0._lockS2MDMG, function(arg_23_0)
		arg_19_0._dataProxy.SetupDamageKamikazeAir(arg_23_0 and var_0_0.Battle.BattleFormulas.CalcDamageLockA2M or None), SFX_PANEL)
	onToggle(None, arg_19_0._lockA2MDMG, function(arg_24_0)
		arg_19_0._dataProxy.SetupDamageKamikazeShip(arg_24_0 and var_0_0.Battle.BattleFormulas.CalcDamageLockS2M or None), SFX_PANEL)
	onToggle(None, arg_19_0._lockCrushDMG, function(arg_25_0)
		arg_19_0._dataProxy.SetupDamageCrush(arg_25_0 and var_0_0.Battle.BattleFormulas.CalcDamageLockCrush or None), SFX_PANEL)

	arg_19_0._triggerWave = arg_19_0._common.Find("wave_trigger")
	arg_19_0._waveIndex = arg_19_0._common.Find("wave_input").GetComponent("InputField")

	if arg_19_0._dataProxy.GetInitData().battleType != SYSTEM_SCENARIO and arg_19_0._dataProxy.GetInitData().battleType != SYSTEM_ROUTINE and arg_19_0._dataProxy.GetInitData().battleType != SYSTEM_ACT_BOSS:
		SetActive(arg_19_0._triggerWave, False)
		SetActive(arg_19_0._waveIndex, False)
	else
		onButton(None, arg_19_0._triggerWave, function()
			arg_19_0.forceTrigger(tonumber(arg_19_0._waveIndex.text)))

	arg_19_0._triggerWeather = arg_19_0._common.Find("weather_trigger")
	arg_19_0._weatherInput = arg_19_0._common.Find("weather_input").GetComponent("InputField")

	onButton(None, arg_19_0._triggerWeather, function()
		arg_19_0._dataProxy.AddWeather(tonumber(arg_19_0._weatherInput.text)))

	arg_19_0._antiSubDetailRange = arg_19_0._common.Find("anti_sub_detail")

	onButton(None, arg_19_0._antiSubDetailRange, function()
		arg_19_0._state.GetMediatorByName("BattleSceneMediator").InitDetailAntiSubArea())

	arg_19_0._instantReload = arg_19_0._common.Find("instant_reload")

	onButton(None, arg_19_0._instantReload, function()
		local var_29_0 = arg_19_0._dataProxy._fleetList[1]

		local function var_29_1(arg_30_0)
			local var_30_0 = arg_30_0.GetWeaponList()

			for iter_30_0, iter_30_1 in ipairs(var_30_0):
				iter_30_1.QuickCoolDown()

		var_29_1(var_29_0.GetChargeWeaponVO())
		var_29_1(var_29_0.GetTorpedoWeaponVO())
		var_29_1(var_29_0.GetAirAssistVO()))

	arg_19_0._white = arg_19_0._base.Find("white_button")

	onButton(None, arg_19_0._white, function()
		arg_19_0._dataProxy._fleetList[1]._scoutList[1].UpdateHP(-20, {}), SFX_PANEL)
	SetActive(arg_19_0._white, True)

def var_0_3.SetActive(arg_32_0, arg_32_1):
	SetActive(arg_32_0._go, arg_32_1)

def var_0_3.spawnEnemy(arg_33_0, arg_33_1, arg_33_2, arg_33_3, arg_33_4, arg_33_5):
	local var_33_0 = {
		monsterTemplateID = arg_33_1,
		corrdinate = {
			math.random(arg_33_2, arg_33_3),
			0,
			math.random(arg_33_4, arg_33_5)
		}
	}

	var_33_0.delay = 0
	var_33_0.moveCast = True
	var_33_0.score = 0
	var_33_0.buffList = {
		8001
	}

	arg_33_0._dataProxy.SpawnMonster(var_33_0, 1, var_0_1.UnitType.ENEMY_UNIT, var_0_2.FOE_CODE)

def var_0_3.spawnStrike(arg_34_0, arg_34_1, arg_34_2, arg_34_3, arg_34_4):
	local var_34_0 = {
		templateID = arg_34_1,
		weaponID = {},
		attr = {},
		totalNumber = arg_34_2,
		onceNumber = arg_34_3
	}

	var_34_0.formation = 10006
	var_34_0.delay = 0
	var_34_0.interval = 0.1
	var_34_0.score = 0

	arg_34_0._dataProxy.SpawnAirFighter(var_34_0)

def var_0_3.activeReference(arg_35_0):
	arg_35_0._state.ActiveReference()

	local var_35_0 = arg_35_0._state.GetMediatorByName(var_0_0.Battle.BattleReferenceBoxMediator.__name) or arg_35_0._state.AddMediator(var_0_0.Battle.BattleReferenceBoxMediator.New())

	pg.TipsMgr.GetInstance().ShowTips("┏━━━━━━━━━━━━━━━━━━━┓")
	pg.TipsMgr.GetInstance().ShowTips("┃ヽ(•̀ω•́ )ゝ战斗调试模块初始化成功！(ง •̀_•́)ง┃")
	pg.TipsMgr.GetInstance().ShowTips("┗━━━━━━━━━━━━━━━━━━━┛")

	arg_35_0._activeReference.transform.GetComponent("Button").enabled = False
	arg_35_0._activeReference.Find("text").GetComponent(typeof(Text)).text = "(ﾉ･ω･)ﾉﾞ"
	arg_35_0._referenceConsole = arg_35_0._common.Find("reference_btns")

	SetActive(arg_35_0._referenceConsole, True)

	arg_35_0._speedUp = arg_35_0._referenceConsole.Find("speed_up")
	arg_35_0._speedDown = arg_35_0._referenceConsole.Find("speed_down")
	arg_35_0._speedLevel = arg_35_0._referenceConsole.Find("speed")

	onButton(None, arg_35_0._speedUp, function()
		local var_36_0 = var_0_0.Battle.BattleConfig.BASIC_TIME_SCALE

		if var_36_0 < 1:
			var_0_0.Battle.BattleControllerCommand.removeSpeed(2)
		elif var_36_0 >= 1:
			var_0_0.Battle.BattleControllerCommand.addSpeed(2)

		arg_35_0._speedLevel.GetComponent(typeof(Text)).text = var_0_0.Battle.BattleConfig.BASIC_TIME_SCALE

		arg_35_0._state.ScaleTimer(), SFX_PANEL)
	onButton(None, arg_35_0._speedDown, function()
		local var_37_0 = var_0_0.Battle.BattleConfig.BASIC_TIME_SCALE

		if var_37_0 > 1:
			var_0_0.Battle.BattleControllerCommand.removeSpeed(0.5)
		elif var_37_0 <= 1:
			var_0_0.Battle.BattleControllerCommand.addSpeed(0.5)

		arg_35_0._speedLevel.GetComponent(typeof(Text)).text = var_0_0.Battle.BattleConfig.BASIC_TIME_SCALE

		arg_35_0._state.ScaleTimer(), SFX_PANEL)

	arg_35_0._shipBox = arg_35_0._referenceConsole.Find("ship_box")
	arg_35_0._bulletBox = arg_35_0._referenceConsole.Find("bullet_box")
	arg_35_0._pp = arg_35_0._referenceConsole.Find("property_panel")

	onToggle(None, arg_35_0._shipBox, function(arg_38_0)
		var_35_0.ActiveUnitBoxes(arg_38_0), SFX_PANEL)
	onToggle(None, arg_35_0._bulletBox, function(arg_39_0)
		var_35_0.ActiveBulletBoxes(arg_39_0), SFX_PANEL)
	onToggle(None, arg_35_0._pp, function(arg_40_0)
		var_35_0.ActiveUnitDetail(arg_40_0), SFX_PANEL)

def var_0_3.forceTrigger(arg_41_0, arg_41_1):
	local var_41_0 = arg_41_0._state.GetCommandByName("BattleSingleDungeonCommand")._waveUpdater._waveInfoList[arg_41_1]

	if var_41_0 == None:
		pg.TipsMgr.GetInstance().ShowTips("查无次波")
	elif var_41_0.GetState() != var_41_0.STATE_DEACTIVE:
		pg.TipsMgr.GetInstance().ShowTips("该触发器已经触发")
	else
		var_41_0.DoWave()
