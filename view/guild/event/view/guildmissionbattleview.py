local var_0_0 = class("GuildMissionBattleView")
local var_0_1 = Vector3(40, -3, 40)
local var_0_2 = 10
local var_0_3 = 1028
local var_0_4 = Vector3(80, -3, 40)

local function var_0_5(arg_1_0)
	local var_1_0 = {}
	local var_1_1 = {}

	for iter_1_0, iter_1_1 in ipairs(ys.Battle.BattleConst.FXContainerIndex):
		local var_1_2 = arg_1_0[iter_1_0]

		var_1_1[iter_1_0] = Vector3(var_1_2[1], var_1_2[2], var_1_2[3])

	var_1_0._FXOffset = var_1_1
	var_1_0._FXAttachPoint = GameObject()

	function var_1_0.GetFXOffsets(arg_2_0, arg_2_1)
		arg_2_1 = arg_2_1 or 1

		return arg_2_0._FXOffset[arg_2_1]

	function var_1_0.GetAttachPoint(arg_3_0)
		return arg_3_0._FXAttachPoint

	function var_1_0.GetGO(arg_4_0)
		return arg_4_0._go

	function var_1_0.SetGo(arg_5_0, arg_5_1)
		assert(arg_5_1)

		arg_5_0._go = arg_5_1

		local var_5_0 = arg_5_0._FXAttachPoint.transform

		var_5_0.SetParent(arg_5_1.transform, False)

		var_5_0.localPosition = Vector3.zero
		var_5_0.localEulerAngles = Vector3(330, 0, 0)

	function var_1_0.GetSpecificFXScale(arg_6_0)
		return {}

	return var_1_0

def var_0_0.Ctor(arg_7_0, arg_7_1):
	arg_7_0.rawImage = arg_7_1

	setActive(arg_7_0.rawImage, False)

	arg_7_0.seaCameraGO = GameObject.Find("BarrageCamera")
	arg_7_0.seaCameraGO.tag = "MainCamera"
	arg_7_0.seaCamera = arg_7_0.seaCameraGO.GetComponent(typeof(Camera))
	arg_7_0.seaCamera.targetTexture = arg_7_0.rawImage.texture
	arg_7_0.seaCamera.enabled = True
	arg_7_0.mainCameraGO = pg.UIMgr.GetInstance().GetMainCamera()

def var_0_0.configUI(arg_8_0, arg_8_1, arg_8_2):
	arg_8_0.nameTF = arg_8_2
	arg_8_0.healTF = arg_8_1

	setActive(arg_8_0.healTF, False)
	arg_8_0.healTF.GetComponent("DftAniEvent").SetEndEvent(function()
		setActive(arg_8_0.healTF, False)
		setText(arg_8_0.healTF.Find("text"), ""))

def var_0_0.load(arg_10_0, arg_10_1, arg_10_2):
	ys.Battle.BattleVariable.Init()

	local var_10_0 = ys.Battle.BattleResourceManager.GetInstance()

	var_10_0.Init()
	var_10_0.AddPreloadResource(var_10_0.GetMapResource(arg_10_1))

	local function var_10_1()
		pg.UIMgr.GetInstance().LoadingOff()

		arg_10_0.seaView = ys.Battle.BattleMap.New(arg_10_1)

		setActive(arg_10_0.rawImage, True)

		GameObject.Find("scenes").transform.position = Vector3(0, -26, 0)

		var_10_0.Clear()

		if arg_10_2:
			onNextTick(arg_10_2)

	var_10_0.StartPreload(var_10_1, None)
	pg.UIMgr.GetInstance().LoadingOn()

def var_0_0.LoadShip(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4):
	if not arg_12_1:
		arg_12_4()

		return

	if arg_12_0.shipVO:
		arg_12_4()

		return

	arg_12_0.unitList = {}
	arg_12_0.bulletUnitList = {}
	arg_12_0.shipVO = arg_12_1
	arg_12_0.equipSkinId = 0
	arg_12_0.weaponIds = arg_12_2

	ys.Battle.BattleFXPool.GetInstance().Init()

	arg_12_0._cldSystem = ys.Battle.BattleCldSystem.New(arg_12_0)

	local var_12_0 = ys.Battle.BattleResourceManager.GetInstance()

	var_12_0.Init()
	var_12_0.AddPreloadResource(var_12_0.GetDisplayCommonResource())

	if arg_12_0.equipSkinId > 0:
		var_12_0.AddPreloadResource(var_12_0.GetEquipSkinPreviewRes(arg_12_0.equipSkinId))

	local var_12_1 = pg.enemy_data_statistics[var_0_2]

	var_12_0.AddPreloadResource(var_12_0.GetCharacterPath(var_12_1.prefab), False)

	local var_12_2 = pg.enemy_data_statistics[var_0_3]

	var_12_0.AddPreloadResource(var_12_0.GetCharacterPath(var_12_2.prefab), False)
	var_12_0.AddPreloadResource(var_12_0.GetShipResource(arg_12_1.configId, arg_12_1.skinId), False)

	if arg_12_1.getShipType() != ShipType.WeiXiu:
		for iter_12_0, iter_12_1 in ipairs(arg_12_2):
			if iter_12_1 != 0:
				local var_12_3 = ys.Battle.BattleDataFunction.GetWeaponDataFromID(iter_12_1).weapon_id

				for iter_12_2, iter_12_3 in ipairs(var_12_3):
					var_12_0.AddPreloadResource(var_12_0.GetWeaponResource(iter_12_3))

	local function var_12_4()
		local function var_13_0(arg_14_0)
			arg_12_0.seaCharacter = arg_14_0

			local var_14_0 = arg_12_1.getConfig("scale") / 50

			arg_14_0.transform.localScale = Vector3(var_14_0 - 0.4, var_14_0, var_14_0)
			arg_14_0.transform.localPosition = arg_12_0.GetCharacterOffset()
			arg_14_0.transform.localEulerAngles = Vector3(30, 0, 0)
			arg_12_0.seaAnimator = arg_14_0.transform.GetComponent("SpineAnim")
			arg_12_0.characterAction = ys.Battle.BattleConst.ActionName.MOVE

			arg_12_0.seaAnimator.SetAction(arg_12_0.characterAction, 0, True)

			local var_14_1 = cloneTplTo(arg_12_0.nameTF, arg_14_0)

			var_14_1.localPosition = Vector3(0, -0.35, -1)

			setText(var_14_1.Find("Text"), arg_12_3)

			local var_14_2 = pg.ship_skin_template[arg_12_1.skinId]
			local var_14_3 = var_0_5(var_14_2.fx_container)

			var_14_3.SetGo(arg_14_0)

			local var_14_4 = ys.Battle.BattleFXPool.GetInstance()
			local var_14_5 = var_14_4.GetCharacterFX("movewave", var_14_3)

			pg.EffectMgr.GetInstance().PlayBattleEffect(var_14_5, Vector3(0, 0, 0), True)

			arg_12_0.seaFXPool = var_14_4

			if arg_12_1.getShipType() != ShipType.WeiXiu:
				arg_12_0.boneList = {}

				local var_14_6 = pg.ship_skin_template[arg_12_1.skinId]

				for iter_14_0, iter_14_1 in pairs(var_14_6.bound_bone):
					local var_14_7 = {}

					for iter_14_2, iter_14_3 in ipairs(iter_14_1):
						if type(iter_14_3) == "table":
							var_14_7[#var_14_7 + 1] = Vector3(iter_14_3[1], iter_14_3[2], iter_14_3[3])
						else
							var_14_7[#var_14_7 + 1] = Vector3.zero

					arg_12_0.boneList[iter_14_0] = var_14_7[1]

			LeanTween.value(arg_14_0, -20, 0, 2).setOnUpdate(System.Action_float(function(arg_15_0)
				arg_14_0.transform.position = Vector3(arg_15_0, arg_14_0.transform.position.y, arg_14_0.transform.position.z)))

		seriesAsync({
			function(arg_16_0)
				var_12_0.InstCharacter(arg_12_1.getPrefab(), function(arg_17_0)
					var_13_0(arg_17_0)
					arg_16_0()),
			function(arg_18_0)
				arg_12_0.CreateMonster(arg_18_0),
			function(arg_19_0)
				arg_12_0.CreateItemBox(arg_19_0)
		}, function()
			arg_12_0.loaded = True

			pg.TimeMgr.GetInstance().ResumeBattleTimer()

			if arg_12_1.getShipType() != ShipType.WeiXiu:
				arg_12_0.onWeaponUpdate()
				arg_12_0.SeaUpdate()

			if arg_12_4:
				arg_12_4())

	var_12_0.StartPreload(var_12_4, None)

def var_0_0.StartMoveOtherShips(arg_21_0, arg_21_1):
	local function var_21_0(arg_22_0, arg_22_1)
		local var_22_0 = arg_22_0.transform.localPosition
		local var_22_1 = math.random(5, 8)
		local var_22_2 = math.random(0, 5)

		LeanTween.value(arg_22_0, var_22_0.x, 80, var_22_1).setOnUpdate(System.Action_float(function(arg_23_0)
			arg_22_0.transform.localPosition = Vector3(arg_23_0, var_22_0.y, var_22_0.z))).setOnComplete(System.Action(arg_22_1)).setDelay(var_22_2)

	local var_21_1 = {}

	for iter_21_0, iter_21_1 in ipairs(arg_21_0.otherShipGos):
		table.insert(var_21_1, function(arg_24_0)
			var_21_0(iter_21_1, arg_24_0))

	parallelAsync(var_21_1, arg_21_1)

def var_0_0.PlayOtherShipAnim(arg_25_0, arg_25_1, arg_25_2):
	if not arg_25_0.loaded:
		return

	arg_25_0.otherShipGos = {}

	local var_25_0 = ys.Battle.BattleResourceManager.GetInstance()

	var_25_0.Init()
	var_25_0.AddPreloadResource(var_25_0.GetDisplayCommonResource())

	local function var_25_1(arg_26_0, arg_26_1, arg_26_2)
		local var_26_0 = pg.ship_data_statistics[arg_26_0.id].scale / 50

		arg_26_2.transform.localScale = Vector3(var_26_0 - 0.4, var_26_0, var_26_0)
		arg_26_2.transform.localPosition = Vector3(-20, 0, arg_26_1)
		arg_26_2.transform.localEulerAngles = Vector3(30, 0, 0)

		arg_26_2.transform.GetComponent("SpineAnim").SetAction(ys.Battle.BattleConst.ActionName.MOVE, 0, True)

		local var_26_1 = cloneTplTo(arg_25_0.nameTF, arg_26_2)

		var_26_1.localPosition = Vector3(0, -0.35, -1)

		setText(var_26_1.Find("Text"), arg_26_0.name)

		local var_26_2 = pg.ship_skin_template[arg_26_0.skin]
		local var_26_3 = var_0_5(var_26_2.fx_container)

		var_26_3.SetGo(arg_26_2)

		local var_26_4 = ys.Battle.BattleFXPool.GetInstance().GetCharacterFX("movewave", var_26_3)

		pg.EffectMgr.GetInstance().PlayBattleEffect(var_26_4, Vector3(0, 0, 0), True)
		table.insert(arg_25_0.otherShipGos, arg_26_2)

	local var_25_2 = {}
	local var_25_3 = {
		math.random(43, 48),
		math.random(49, 53)
	}

	for iter_25_0, iter_25_1 in ipairs(arg_25_1):
		var_25_0.AddPreloadResource(var_25_0.GetShipResource(iter_25_1.id, iter_25_1.skin), False)
		table.insert(var_25_2, function(arg_27_0)
			local var_27_0 = pg.ship_skin_template[iter_25_1.skin]

			assert(var_27_0, iter_25_1.skin)
			var_25_0.InstCharacter(var_27_0.prefab, function(arg_28_0)
				var_25_1(iter_25_1, var_25_3[iter_25_0], arg_28_0)
				arg_27_0()))

	local function var_25_4()
		for iter_29_0, iter_29_1 in ipairs(arg_25_0.otherShipGos):
			Destroy(iter_29_1)

		arg_25_0.otherShipGos = None

		arg_25_2()

	local function var_25_5()
		seriesAsync(var_25_2, function()
			arg_25_0.StartMoveOtherShips(var_25_4))

	var_25_0.StartPreload(var_25_5, None)

def var_0_0.PlayAttackAnim(arg_32_0):
	arg_32_0.isFinish = None

	local function var_32_0()
		if not arg_32_0.animTimer:
			return

		arg_32_0.animTimer.Stop()

		arg_32_0.animTimer = None

	local function var_32_1(arg_34_0)
		var_32_0()
		arg_32_0.seaEmenyAnimator.SetAction("move", 0, True)

		local var_34_0

		var_34_0.localPosition, var_34_0 = var_0_1 + Vector3(40, 0, 0), arg_32_0.seaEmeny.transform

		setActive(arg_32_0.seaEmeny, True)

		arg_32_0.animTimer = Timer.New(function()
			var_34_0.localPosition = Vector3.Lerp(var_34_0.localPosition, var_0_1, Time.deltaTime * 3)

			if Vector3.Distance(var_0_1, var_34_0.localPosition) <= 1:
				arg_34_0(), 0.033, -1)

		arg_32_0.animTimer.Start()

	local function var_32_2(arg_36_0)
		var_32_0()

		if arg_32_0.shipVO.getShipType() != ShipType.WeiXiu:
			arg_32_0.SeaFire()

		arg_32_0.animTimer = Timer.New(arg_36_0, 3, 1)

		arg_32_0.animTimer.Start()

	local function var_32_3(arg_37_0)
		var_32_0()

		if not arg_32_0.isFinish:
			arg_32_0.HandleBulletHit(None, arg_32_0.unitList[1])

		arg_32_0.seaAnimator.SetActionCallBack(function(arg_38_0)
			if arg_38_0 == "finish":
				arg_32_0.seaAnimator.SetAction("move", 0, True)
				arg_32_0.seaAnimator.SetActionCallBack(None)
				arg_37_0())
		arg_32_0.seaAnimator.SetAction("victory", 0, True)

	seriesAsync({
		var_32_1,
		var_32_2,
		var_32_3
	})

def var_0_0.PlayItemAnim(arg_39_0):
	local function var_39_0()
		if not arg_39_0.animTimer:
			return

		arg_39_0.animTimer.Stop()

		arg_39_0.animTimer = None

	var_39_0()

	local function var_39_1(arg_41_0)
		arg_39_0.seaItemBoxAnimator.SetAction("move", 0, True)
		setActive(arg_39_0.seaItemBox, True)

		local var_41_0 = arg_39_0.seaItemBox.transform

		var_41_0.localPosition = var_0_4
		arg_39_0.animTimer = Timer.New(function()
			var_41_0.localPosition = Vector3.Lerp(var_41_0.localPosition, var_0_1, Time.deltaTime * 3)

			if Vector3.Distance(var_0_1, var_41_0.localPosition) <= 1:
				arg_41_0(), 0.033, -1)

		arg_39_0.animTimer.Start()

	local function var_39_2(arg_43_0)
		var_39_0()
		arg_39_0.seaAnimator.SetActionCallBack(function(arg_44_0)
			if arg_44_0 == "finish":
				arg_39_0.seaAnimator.SetAction("move", 0, True)
				arg_39_0.seaAnimator.SetActionCallBack(None)
				arg_43_0())
		arg_39_0.seaAnimator.SetAction("victory", 0, True)

	seriesAsync({
		var_39_1,
		var_39_2
	})

def var_0_0.CreateMonster(arg_45_0, arg_45_1):
	local var_45_0 = 1
	local var_45_1 = ys.Battle.BattleDataFunction.CreateBattleUnitData(var_45_0, ys.Battle.BattleConst.UnitType.ENEMY_UNIT, -1, var_0_2, None, {}, None, None, False, 1, 1, None, None, 1)

	var_45_1.SetPosition(var_0_1)
	var_45_1.ActiveCldBox()
	arg_45_0._cldSystem.InitShipCld(var_45_1)

	local var_45_2 = var_0_5(var_45_1.GetTemplate().fx_container)

	ys.Battle.BattleResourceManager.GetInstance().InstCharacter(var_45_1.GetTemplate().prefab, function(arg_46_0)
		var_45_2.SetGo(arg_46_0)

		local var_46_0 = var_45_1.GetTemplate().scale / 50

		arg_46_0.transform.localScale = Vector3(var_46_0, var_46_0, var_46_0)
		arg_46_0.transform.localPosition = var_0_1
		arg_46_0.transform.localEulerAngles = Vector3(30, 0, 0)

		local var_46_1 = var_45_1.GetTemplate().wave_fx
		local var_46_2 = ys.Battle.BattleFXPool.GetInstance().GetCharacterFX(var_46_1, var_45_2)

		pg.EffectMgr.GetInstance().PlayBattleEffect(var_46_2, Vector3(0, 0, 0), True)

		arg_45_0.seaEmeny = arg_46_0
		arg_45_0.seaEmenyAnimator = arg_46_0.transform.GetComponent("SpineAnim")

		setActive(arg_46_0, False)
		arg_45_1())

	arg_45_0.unitList[var_45_0] = var_45_1

def var_0_0.CreateItemBox(arg_47_0, arg_47_1):
	local var_47_0 = pg.enemy_data_statistics[var_0_3]

	ys.Battle.BattleResourceManager.GetInstance().InstCharacter(var_47_0.prefab, function(arg_48_0)
		local var_48_0 = var_47_0.scale / 50

		arg_48_0.transform.localScale = Vector3(var_48_0, var_48_0, var_48_0)
		arg_48_0.transform.localPosition = var_0_4
		arg_48_0.transform.localEulerAngles = Vector3(30, 0, 0)
		arg_47_0.seaItemBox = arg_48_0
		arg_47_0.seaItemBoxAnimator = arg_48_0.transform.GetComponent("SpineAnim")

		setActive(arg_48_0, False)
		arg_47_1())

def var_0_0.playShipAnims(arg_49_0):
	if arg_49_0.loaded and arg_49_0.seaAnimator:
		local var_49_0 = {
			"attack",
			"victory",
			"dead"
		}

		local function var_49_1(arg_50_0)
			if arg_49_0.seaAnimator:
				arg_49_0.seaAnimator.SetActionCallBack(None)

			arg_49_0.seaAnimator.SetAction(var_49_0[arg_50_0], 0, False)
			arg_49_0.seaAnimator.SetActionCallBack(function(arg_51_0)
				if arg_51_0 == "finish":
					arg_49_0.seaAnimator.SetActionCallBack(None)
					arg_49_0.seaAnimator.SetAction("stand", 0, False))

		if arg_49_0.palyAnimTimer:
			arg_49_0.palyAnimTimer.Stop()

			arg_49_0.palyAnimTimer = None

		arg_49_0.palyAnimTimer = Timer.New(function()
			var_49_1(math.random(1, #var_49_0)), 5, -1)

		arg_49_0.palyAnimTimer.Start()
		arg_49_0.palyAnimTimer.func()

def var_0_0.onWeaponUpdate(arg_53_0):
	if arg_53_0.loaded and arg_53_0.weaponIds:
		if arg_53_0.seaAnimator:
			arg_53_0.seaAnimator.SetActionCallBack(None)

		local function var_53_0()
			for iter_54_0, iter_54_1 in pairs(arg_53_0.weaponList or {}):
				for iter_54_2, iter_54_3 in pairs(iter_54_1.emitterList or {}):
					iter_54_3.Destroy()

			for iter_54_4, iter_54_5 in ipairs(arg_53_0.bulletList or {}):
				Object.Destroy(iter_54_5._go)

			for iter_54_6, iter_54_7 in pairs(arg_53_0.aircraftList or {}):
				Object.Destroy(iter_54_7.obj)

			arg_53_0.bulletList = {}
			arg_53_0.aircraftList = {}

		if #arg_53_0.weaponIds == 0 and arg_53_0.playRandomAnims:
			if arg_53_0._fireTimer:
				arg_53_0._fireTimer.Stop()

			if arg_53_0._delayTimer:
				arg_53_0._delayTimer.Stop()

			if arg_53_0.shipVO.getShipType() != ShipType.WeiXiu:
				var_53_0()
			elif arg_53_0.buffTimer:
				pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_53_0.buffTimer)

				arg_53_0.buffTimer = None

			arg_53_0.playShipAnims()
		elif arg_53_0.shipVO.getShipType() != ShipType.WeiXiu:
			var_53_0()
			arg_53_0.MakeWeapon(arg_53_0.weaponIds)
		else
			local var_53_1 = arg_53_0.weaponIds[1]

			if var_53_1:
				local var_53_2 = Equipment.getConfigData(var_53_1).skill_id[1]

				arg_53_0.MakeBuff(var_53_2)

def var_0_0.SeaFire(arg_55_0):
	local var_55_0 = 1
	local var_55_1

	local function var_55_2()
		local var_56_0 = arg_55_0.weaponList[var_55_0]

		if var_56_0:
			local function var_56_1()
				local var_57_0 = 1
				local var_57_1 = 0

				for iter_57_0, iter_57_1 in ipairs(var_56_0.emitterList):
					iter_57_1.Ready()

				for iter_57_2, iter_57_3 in ipairs(var_56_0.emitterList):
					iter_57_3.Fire(None, var_57_0, var_57_1)

				var_55_0 = var_55_0 + 1

			if var_56_0.tmpData.action_index != "":
				arg_55_0.characterAction = var_56_0.tmpData.action_index

				arg_55_0.seaAnimator.SetAction(arg_55_0.characterAction, 0, False)
				arg_55_0.seaAnimator.SetActionCallBack(function(arg_58_0)
					if arg_58_0 == "action":
						var_56_1())
			else
				var_56_1()

			if var_56_0.tmpData.type == ys.Battle.BattleConst.EquipmentType.PREVIEW_ARICRAFT:
				arg_55_0.timer = Timer.New(var_55_2, 1.5, 1)

				arg_55_0.timer.Start()
		elif arg_55_0.characterAction != ys.Battle.BattleConst.ActionName.MOVE:
			arg_55_0.characterAction = ys.Battle.BattleConst.ActionName.MOVE

			arg_55_0.seaAnimator.SetAction(arg_55_0.characterAction, 0, True)

			var_55_0 = 1

	var_55_2()

def var_0_0.MakeBuff(arg_59_0, arg_59_1):
	local var_59_0 = getSkillConfig(arg_59_1)
	local var_59_1 = var_59_0.effect_list[1].arg_list.skill_id
	local var_59_2 = var_59_0.effect_list[1].arg_list.time
	local var_59_3 = require("GameCfg.skill.skill_" .. var_59_1)

	if arg_59_0.buffTimer:
		pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_59_0.buffTimer)

		arg_59_0.buffTimer = None

	arg_59_0.buffTimer = pg.TimeMgr.GetInstance().AddBattleTimer("buffTimer", -1, var_59_2, function()
		setActive(arg_59_0.healTF, True)
		setText(arg_59_0.healTF.Find("text"), var_59_3.effect_list[1].arg_list.number))

def var_0_0.MakeWeapon(arg_61_0, arg_61_1):
	arg_61_0.weaponList = {}
	arg_61_0.bulletList = {}
	arg_61_0.aircraftList = {}

	local var_61_0 = 0
	local var_61_1 = ys.Battle.BattleConst

	for iter_61_0, iter_61_1 in ipairs(arg_61_1):
		local var_61_2 = Equipment.getConfigData(iter_61_1).weapon_id

		for iter_61_2, iter_61_3 in ipairs(var_61_2):
			if iter_61_3 <= 0:
				break

			var_61_0 = var_61_0 + 1

			local var_61_3 = ys.Battle.BattleDataFunction.GetWeaponPropertyDataFromID(iter_61_3)

			if var_61_3.type == var_61_1.EquipmentType.MAIN_CANNON or var_61_3.type == var_61_1.EquipmentType.SUB_CANNON or var_61_3.type == var_61_1.EquipmentType.TORPEDO or var_61_3.type == var_61_1.EquipmentType.MANUAL_TORPEDO or var_61_3.type == var_61_1.EquipmentType.POINT_HIT_AND_LOCK:
				if type(var_61_3.barrage_ID) == "table":
					arg_61_0.weaponList[var_61_0] = {
						tmpData = var_61_3,
						emitterList = {}
					}

					for iter_61_4, iter_61_5 in ipairs(var_61_3.barrage_ID):
						local var_61_4 = arg_61_0.createEmitterCannon(iter_61_5, var_61_3.bullet_ID[iter_61_4], var_61_3.spawn_bound)

						arg_61_0.weaponList[var_61_0].emitterList[iter_61_4] = var_61_4
			elif var_61_3.type == var_61_1.EquipmentType.PREVIEW_ARICRAFT and type(var_61_3.barrage_ID) == "table":
				arg_61_0.weaponList[var_61_0] = {
					tmpData = var_61_3,
					emitterList = {}
				}

				for iter_61_6, iter_61_7 in ipairs(var_61_3.barrage_ID):
					local var_61_5 = arg_61_0.createEmitterAir(iter_61_7, var_61_3.bullet_ID[iter_61_6], var_61_3.spawn_bound)

					arg_61_0.weaponList[var_61_0].emitterList[iter_61_6] = var_61_5

def var_0_0.createEmitterCannon(arg_62_0, arg_62_1, arg_62_2, arg_62_3):
	local function var_62_0(arg_63_0, arg_63_1, arg_63_2, arg_63_3, arg_63_4)
		local var_63_0 = ys.Battle.BattlePlayerUnit.New(1, ys.Battle.BattleConfig.FRIENDLY_CODE)
		local var_63_1 = {
			speed = 0
		}

		var_63_0.SetSkinId(arg_62_0.shipVO.skinId)
		var_63_0.SetTemplate(arg_62_0.shipVO.configId, var_63_1)

		local var_63_2
		local var_63_3 = arg_62_0.GetCharacterOffset()
		local var_63_4, var_63_5 = ys.Battle.BattleDataFunction.CreateBattleBulletData(arg_62_2, arg_62_2, var_63_0, var_63_2, var_63_3 + Vector3(40, 0, 0))

		if var_63_5:
			arg_62_0._cldSystem.InitBulletCld(var_63_4)

		var_63_4.SetOffsetPriority(arg_63_3)
		var_63_4.SetShiftInfo(arg_63_0, arg_63_1)
		var_63_4.SetRotateInfo(None, 0, arg_63_2)

		if arg_62_0.equipSkinId > 0:
			local var_63_6 = pg.equip_skin_template[arg_62_0.equipSkinId]
			local var_63_7, var_63_8, var_63_9, var_63_10 = ys.Battle.BattleDataFunction.GetEquipSkin(arg_62_0.equipSkinId)
			local var_63_11 = var_63_4.GetType()
			local var_63_12 = ys.Battle.BattleConst.BulletType
			local var_63_13

			if var_63_11 == var_63_12.CANNON or var_63_11 == var_63_12.BOMB:
				local var_63_14 = {
					EquipType.CannonQuZhu,
					EquipType.CannonQingXun,
					EquipType.CannonZhongXun,
					EquipType.CannonZhanlie,
					EquipType.CannonZhongXun2
				}

				if _.any(var_63_14, function(arg_64_0)
					return table.contains(var_63_6.equip_type, arg_64_0)):
					var_63_4.SetModleID(var_63_7)
				elif var_63_8 and #var_63_8 > 0:
					var_63_4.SetModleID(var_63_8)
				elif var_63_10 and #var_63_10 > 0:
					var_63_4.SetModleID(var_63_10)
			elif var_63_11 == var_63_12.TORPEDO:
				if table.contains(var_63_6.equip_type, EquipType.Torpedo):
					var_63_4.SetModleID(var_63_7)
				elif var_63_9 and #var_63_9 > 0:
					var_63_4.SetModleID(var_63_9)

		local var_63_15 = var_63_4.GetType()
		local var_63_16 = ys.Battle.BattleConst.BulletType
		local var_63_17

		if var_63_15 == var_63_16.CANNON:
			var_63_17 = ys.Battle.BattleCannonBullet.New()
		elif var_63_15 == var_63_16.BOMB:
			var_63_17 = ys.Battle.BattleBombBullet.New()
		elif var_63_15 == var_63_16.TORPEDO:
			var_63_17 = ys.Battle.BattleTorpedoBullet.New()
		else
			var_63_17 = ys.Battle.BattleBullet.New()

		var_63_17.SetBulletData(var_63_4)
		table.insert(arg_62_0.bulletUnitList, var_63_4)

		local function var_63_18(arg_65_0)
			var_63_17.SetGO(arg_65_0)
			var_63_17.AddRotateScript()

			if tf(arg_65_0).parent:
				tf(arg_65_0).parent = None

			local var_65_0 = arg_62_0.boneList[arg_62_3] or Vector3.zero
			local var_65_1 = arg_62_0.GetCharacterOffset()

			var_63_17.SetSpawn(var_65_1 + var_65_0)

			if arg_62_0.bulletList:
				table.insert(arg_62_0.bulletList, var_63_17)

		ys.Battle.BattleResourceManager.GetInstance().InstBullet(var_63_17.GetModleID(), function(arg_66_0)
			var_63_18(arg_66_0))

	local function var_62_1()
		return

	local var_62_2 = "BattleBulletEmitter"

	return (ys.Battle[var_62_2].New(var_62_0, var_62_1, arg_62_1))

def var_0_0.createEmitterAir(arg_68_0, arg_68_1, arg_68_2, arg_68_3):
	local function var_68_0(arg_69_0, arg_69_1, arg_69_2, arg_69_3, arg_69_4)
		local var_69_0 = {
			id = arg_68_2
		}
		local var_69_1 = pg.aircraft_template[arg_68_2]

		var_69_0.tmpData = var_69_1

		local var_69_2 = math.deg2Rad * arg_69_2
		local var_69_3 = Vector3(math.cos(var_69_2), 0, math.sin(var_69_2))

		local function var_69_4(arg_70_0)
			local var_70_0 = arg_68_0.GetCharacterOffset()
			local var_70_1 = var_70_0 + Vector3(var_69_1.position_offset[1] + arg_69_0, var_69_1.position_offset[2], var_69_1.position_offset[3] + arg_69_1)

			arg_70_0.transform.localPosition = var_70_1
			arg_70_0.transform.localScale = Vector3(0.1, 0.1, 0.1)
			var_69_0.obj = arg_70_0
			var_69_0.tf = arg_70_0.transform
			var_69_0.pos = var_70_1
			var_69_0.baseVelocity = ys.Battle.BattleFormulas.ConvertAircraftSpeed(var_69_0.tmpData.speed)
			var_69_0.speed = var_69_3 * var_69_0.baseVelocity
			var_69_0.speedZ = (math.random() - 0.5) * 0.5
			var_69_0.targetZ = var_70_0.z

			if arg_68_0.aircraftList:
				table.insert(arg_68_0.aircraftList, var_69_0)

		local var_69_5 = var_69_1.model_ID

		if arg_68_0.equipSkinId > 0:
			local var_69_6 = pg.equip_skin_template[arg_68_0.equipSkinId]
			local var_69_7 = {
				EquipType.FighterAircraft,
				EquipType.TorpedoAircraft,
				EquipType.BomberAircraft
			}

			if table.contains(var_69_6.equip_type, var_69_7[var_69_1.type]):
				var_69_5 = ys.Battle.BattleDataFunction.GetEquipSkin(arg_68_0.equipSkinId)

		ys.Battle.BattleResourceManager.GetInstance().InstAirCharacter(var_69_5, function(arg_71_0)
			var_69_4(arg_71_0))

	local function var_68_1()
		return

	local var_68_2 = "BattleBulletEmitter"

	return (ys.Battle[var_68_2].New(var_68_0, var_68_1, arg_68_1))

def var_0_0.RemoveBullet(arg_73_0, arg_73_1, arg_73_2):
	table.remove(arg_73_0.bulletUnitList, arg_73_1)

	local var_73_0 = arg_73_0.bulletList[arg_73_1]

	Object.Destroy(var_73_0._go)
	table.remove(arg_73_0.bulletList, arg_73_1)

	if arg_73_2:
		local var_73_1 = var_73_0.GetMissFXID()

		if var_73_1 and var_73_1 != "":
			local var_73_2, var_73_3 = arg_73_0.seaFXPool.GetFX(var_73_1)

			pg.EffectMgr.GetInstance().PlayBattleEffect(var_73_2, var_73_0.GetPosition() + var_73_3, True)

def var_0_0.SeaUpdate(arg_74_0):
	if not arg_74_0.bulletList:
		return

	local var_74_0 = 0
	local var_74_1 = -20
	local var_74_2 = 60
	local var_74_3 = 0
	local var_74_4 = 60
	local var_74_5 = ys.Battle.BattleConfig
	local var_74_6 = ys.Battle.BattleConst

	local function var_74_7()
		for iter_75_0 = #arg_74_0.bulletUnitList, 1, -1:
			local var_75_0 = arg_74_0.bulletUnitList[iter_75_0]

			arg_74_0._cldSystem.UpdateBulletCld(var_75_0)

		for iter_75_1 = #arg_74_0.bulletList, 1, -1:
			local var_75_1 = arg_74_0.bulletList[iter_75_1]
			local var_75_2 = var_75_1._bulletData.GetSpeed()()
			local var_75_3 = var_75_1.GetPosition()

			if var_75_3.x > var_74_2 and var_75_2.x > 0 or var_75_3.z < var_74_3 and var_75_2.z < 0:
				arg_74_0.RemoveBullet(iter_75_1, False)
			elif var_75_3.x < var_74_1 and var_75_2.x < 0 and var_75_1.GetType() != var_74_6.BulletType.BOMB:
				arg_74_0.RemoveBullet(iter_75_1, False)
			else
				local var_75_4 = pg.TimeMgr.GetInstance().GetCombatTime()

				var_75_1._bulletData.Update(var_75_4)
				var_75_1.Update(var_74_0)

				if var_75_3.z > var_74_4 and var_75_2.z > 0 or var_75_1._bulletData.IsOutRange(var_74_0):
					arg_74_0.RemoveBullet(iter_75_1, True)

		for iter_75_2, iter_75_3 in ipairs(arg_74_0.aircraftList):
			local var_75_5 = iter_75_3.pos + iter_75_3.speed

			if var_75_5.y < var_74_5.AircraftHeight + 5:
				iter_75_3.speed.y = math.max(0.4, 1 - var_75_5.y / var_74_5.AircraftHeight)

				local var_75_6 = math.min(1, var_75_5.y / var_74_5.AircraftHeight)

				iter_75_3.tf.localScale = Vector3(var_75_6, var_75_6, var_75_6)

			iter_75_3.speed.z = iter_75_3.baseVelocity * iter_75_3.speedZ

			local var_75_7 = iter_75_3.targetZ - var_75_5.z

			if var_75_7 > iter_75_3.baseVelocity:
				iter_75_3.speed.z = iter_75_3.baseVelocity * 0.5
			elif var_75_7 < -iter_75_3.baseVelocity:
				iter_75_3.speed.z = -iter_75_3.baseVelocity * 0.5
			else
				local var_75_8 = arg_74_0.GetCharacterOffset()

				iter_75_3.targetZ = var_75_8.z + var_75_8.z * (math.random() - 0.5) * 0.6

			if var_75_5.x > var_74_2 or var_75_5.x < var_74_1:
				Object.Destroy(iter_75_3.obj)
				table.remove(arg_74_0.aircraftList, iter_75_2)
			else
				iter_75_3.tf.localPosition = var_75_5
				iter_75_3.pos = var_75_5

		var_74_0 = var_74_0 + 1

	pg.TimeMgr.GetInstance().AddBattleTimer("barrageUpdateTimer", -1, 0.033, var_74_7)

def var_0_0.GetCharacterOffset(arg_76_0):
	return Vector3(0, -3, 40)

def var_0_0.GetTotalBounds(arg_77_0):
	local var_77_0 = {
		-70,
		20,
		90,
		70
	}
	local var_77_1 = var_77_0[1]
	local var_77_2 = var_77_0[1] + var_77_0[3]
	local var_77_3 = var_77_0[2] + var_77_0[4]
	local var_77_4 = var_77_0[2]

	return var_77_3, var_77_4, var_77_1, var_77_2

def var_0_0.HandleShipCrashDecelerate(arg_78_0):
	return

def var_0_0.HandleShipCrashDecelerate(arg_79_0):
	return

def var_0_0.HandleShipCrashDamageList(arg_80_0):
	return

def var_0_0.HandleBulletHit(arg_81_0, arg_81_1, arg_81_2):
	for iter_81_0 = #arg_81_0.bulletUnitList, 1, -1:
		if arg_81_0.bulletUnitList[iter_81_0] == arg_81_1:
			arg_81_0.RemoveBullet(iter_81_0, True)

	if not arg_81_0.isFinish:
		arg_81_0.isFinish = True

		setActive(arg_81_0.seaEmeny, False)

		local var_81_0, var_81_1 = ys.Battle.BattleFXPool.GetInstance().GetFX("Bomb")

		pg.EffectMgr.GetInstance().PlayBattleEffect(var_81_0, var_81_1.Add(arg_81_2.GetPosition()), True)

def var_0_0.HandleWallHitByBullet(arg_82_0):
	return

def var_0_0.GetUnitList(arg_83_0):
	return arg_83_0.unitList

def var_0_0.GetAircraftList(arg_84_0):
	return {}

def var_0_0.GetBulletList(arg_85_0):
	return arg_85_0.bulletUnitList

def var_0_0.GetAOEList(arg_86_0):
	return {}

def var_0_0.GetFriendlyCode(arg_87_0):
	return 1

def var_0_0.GetFoeCode(arg_88_0):
	return -1

def var_0_0.clear(arg_89_0):
	if arg_89_0.animTimer:
		arg_89_0.animTimer.Stop()

		arg_89_0.animTimer = None

	if arg_89_0._cldSystem:
		arg_89_0._cldSystem.Dispose()

	if arg_89_0.timer:
		arg_89_0.timer.Stop()

		arg_89_0.timer = None

	pg.TimeMgr.GetInstance().RemoveAllBattleTimer()

	if arg_89_0.seaCharacter:
		Destroy(arg_89_0.seaCharacter)

		arg_89_0.seaCharacter = None

	if arg_89_0.otherShipGos:
		for iter_89_0, iter_89_1 in ipairs(arg_89_0.otherShipGos):
			Destroy(iter_89_1)

		arg_89_0.otherShipGos = None

	if arg_89_0.aircraftList:
		for iter_89_2, iter_89_3 in ipairs(arg_89_0.aircraftList):
			Destroy(iter_89_3.obj)

		arg_89_0.aircraftList = None

	if arg_89_0.seaView:
		arg_89_0.seaView.Dispose()

		arg_89_0.seaView = None

	if arg_89_0.weaponList:
		for iter_89_4, iter_89_5 in ipairs(arg_89_0.weaponList):
			for iter_89_6, iter_89_7 in ipairs(iter_89_5.emitterList):
				iter_89_7.Destroy()

		arg_89_0.weaponList = None

	if arg_89_0.bulletList:
		for iter_89_8, iter_89_9 in ipairs(arg_89_0.bulletList):
			Destroy(iter_89_9._go)

		arg_89_0.bulletList = None

	if arg_89_0.seaFXPool:
		arg_89_0.seaFXPool.Clear()

		arg_89_0.seaFXPool = None

	if arg_89_0.seaEmeny:
		Destroy(arg_89_0.seaEmeny)

		arg_89_0.seaEmeny = None

	if arg_89_0.seaItemBox:
		Destroy(arg_89_0.seaItemBox)

		arg_89_0.seaItemBox = None

	if arg_89_0.seaFXContainersPool:
		arg_89_0.seaFXContainersPool.Clear()

		arg_89_0.seaFXContainersPool = None

	ys.Battle.BattleResourceManager.GetInstance().Clear()

	arg_89_0.seaCameraGO.tag = "Untagged"
	arg_89_0.seaCameraGO = None
	arg_89_0.seaCamera = None

	arg_89_0.mainCameraGO.SetActive(True)

	arg_89_0.mainCameraGO = None
	arg_89_0.loaded = False

	if arg_89_0.palyAnimTimer:
		arg_89_0.palyAnimTimer.Stop()

		arg_89_0.palyAnimTimer = None

return var_0_0
