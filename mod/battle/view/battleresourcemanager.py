ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleConfig
local var_0_4 = require("Mgr/Pool/PoolUtil")
local var_0_5 = singletonClass("BattleResourceManager")

var_0_0.Battle.BattleResourceManager = var_0_5
var_0_5.__name = "BattleResourceManager"

def var_0_5.Ctor(arg_1_0):
	arg_1_0.rotateScriptMap = setmetatable({}, {
		__mode = "kv"
	})

def var_0_5.Init(arg_2_0):
	arg_2_0._preloadList = {}
	arg_2_0._resCacheList = {}
	arg_2_0._allPool = {}
	arg_2_0._ob2Pool = {}

	local var_2_0 = GameObject()

	var_2_0.SetActive(False)

	var_2_0.name = "PoolRoot"
	var_2_0.transform.position = Vector3(-10000, -10000, 0)
	arg_2_0._poolRoot = var_2_0
	arg_2_0._bulletContainer = GameObject("BulletContainer")
	arg_2_0._battleCVList = {}

def var_0_5.Clear(arg_3_0):
	for iter_3_0, iter_3_1 in pairs(arg_3_0._allPool):
		iter_3_1.Dispose()

	for iter_3_2, iter_3_3 in pairs(arg_3_0._resCacheList):
		if string.find(iter_3_2, "Char/"):
			var_0_5.ClearCharRes(iter_3_2, iter_3_3)
		elif string.find(iter_3_2, "painting/"):
			var_0_5.ClearPaintingRes(iter_3_2, iter_3_3)
		else
			var_0_4.Destroy(iter_3_3)

	arg_3_0._resCacheList = {}
	arg_3_0._ob2Pool = {}
	arg_3_0._allPool = {}

	Object.Destroy(arg_3_0._poolRoot)

	arg_3_0._poolRoot = None

	Object.Destroy(arg_3_0._bulletContainer)

	arg_3_0._bulletContainer = None
	arg_3_0.rotateScriptMap = setmetatable({}, {
		__mode = "kv"
	})

	for iter_3_4, iter_3_5 in pairs(arg_3_0._battleCVList):
		pg.CriMgr.UnloadCVBank(iter_3_5)

	arg_3_0._battleCVList = {}

	var_0_0.Battle.BattleDataFunction.ClearConvertedBarrage()

def var_0_5.GetBulletPath(arg_4_0):
	return "Item/" .. arg_4_0

def var_0_5.GetOrbitPath(arg_5_0):
	return "orbit/" .. arg_5_0

def var_0_5.GetCharacterPath(arg_6_0):
	return "Char/" .. arg_6_0

def var_0_5.GetCharacterGoPath(arg_7_0):
	return "chargo/" .. arg_7_0

def var_0_5.GetAircraftIconPath(arg_8_0):
	return "AircraftIcon/" .. arg_8_0

def var_0_5.GetFXPath(arg_9_0):
	return "Effect/" .. arg_9_0

def var_0_5.GetPaintingPath(arg_10_0):
	return "painting/" .. arg_10_0

def var_0_5.GetHrzIcon(arg_11_0):
	return "herohrzicon/" .. arg_11_0

def var_0_5.GetSquareIcon(arg_12_0):
	return "squareicon/" .. arg_12_0

def var_0_5.GetQIcon(arg_13_0):
	return "qicon/" .. arg_13_0

def var_0_5.GetCommanderHrzIconPath(arg_14_0):
	return "commanderhrz/" .. arg_14_0

def var_0_5.GetShipTypeIconPath(arg_15_0):
	return "shiptype/" .. arg_15_0

def var_0_5.GetMapPath(arg_16_0):
	return "Map/" .. arg_16_0

def var_0_5.GetUIPath(arg_17_0):
	return "UI/" .. arg_17_0

def var_0_5.GetResName(arg_18_0):
	local var_18_0 = arg_18_0
	local var_18_1 = string.find(var_18_0, "%/")

	while var_18_1:
		var_18_0 = string.sub(var_18_0, var_18_1 + 1)
		var_18_1 = string.find(var_18_0, "%/")

	return var_18_0

def var_0_5.ClearCharRes(arg_19_0, arg_19_1):
	local var_19_0 = var_0_5.GetResName(arg_19_0)
	local var_19_1 = arg_19_1.GetComponent("SkeletonRenderer").skeletonDataAsset

	if not PoolMgr.GetInstance().IsSpineSkelCached(var_19_0):
		UIUtil.ClearSharedMaterial(arg_19_1)

	var_0_4.Destroy(arg_19_1)

def var_0_5.ClearPaintingRes(arg_20_0, arg_20_1):
	local var_20_0 = var_0_5.GetResName(arg_20_0)

	PoolMgr.GetInstance().ReturnPainting(var_20_0, arg_20_1)

def var_0_5.DestroyOb(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_0._ob2Pool[arg_21_1]

	if var_21_0:
		var_21_0.Recycle(arg_21_1)
	else
		var_0_4.Destroy(arg_21_1)

def var_0_5.popPool(arg_22_0, arg_22_1, arg_22_2):
	local var_22_0 = arg_22_1.GetObject()

	if not arg_22_2:
		var_22_0.transform.parent = None

	arg_22_0._ob2Pool[var_22_0] = arg_22_1

	return var_22_0

def var_0_5.InstCharacter(arg_23_0, arg_23_1, arg_23_2):
	local var_23_0 = arg_23_0.GetCharacterPath(arg_23_1)
	local var_23_1 = arg_23_0._allPool[var_23_0]

	if var_23_1:
		local var_23_2 = arg_23_0.popPool(var_23_1)

		arg_23_2(var_23_2)
	elif arg_23_0._resCacheList[var_23_0] != None:
		arg_23_0.InitPool(var_23_0, arg_23_0._resCacheList[var_23_0])

		var_23_1 = arg_23_0._allPool[var_23_0]

		local var_23_3 = arg_23_0.popPool(var_23_1)

		arg_23_2(var_23_3)
	else
		arg_23_0.LoadSpineAsset(arg_23_1, function(arg_24_0)
			if not arg_23_0._poolRoot:
				var_0_5.ClearCharRes(var_23_0, arg_24_0)

				return

			assert(arg_24_0, "角色资源加载失败：" .. arg_23_1)

			local var_24_0 = SpineAnim.AnimChar(arg_23_1, arg_24_0)

			var_24_0.SetActive(False)
			arg_23_0.InitPool(var_23_0, var_24_0)

			var_23_1 = arg_23_0._allPool[var_23_0]

			local var_24_1 = arg_23_0.popPool(var_23_1)

			arg_23_2(var_24_1))

def var_0_5.LoadSpineAsset(arg_25_0, arg_25_1, arg_25_2):
	local var_25_0 = arg_25_0.GetCharacterPath(arg_25_1)

	if not PoolMgr.GetInstance().IsSpineSkelCached(arg_25_1):
		ResourceMgr.Inst.getAssetAsync(var_25_0, arg_25_1 .. "_SkeletonData", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_26_0)
			arg_25_2(arg_26_0)), True, True)
	else
		PoolMgr.GetInstance().GetSpineSkel(arg_25_1, True, arg_25_2)

def var_0_5.InstAirCharacter(arg_27_0, arg_27_1, arg_27_2):
	local var_27_0 = arg_27_0.GetCharacterGoPath(arg_27_1)
	local var_27_1 = arg_27_0._allPool[var_27_0]

	if var_27_1:
		local var_27_2 = arg_27_0.popPool(var_27_1)

		arg_27_2(var_27_2)
	elif arg_27_0._resCacheList[var_27_0] != None:
		arg_27_0.InitPool(var_27_0, arg_27_0._resCacheList[var_27_0])

		var_27_1 = arg_27_0._allPool[var_27_0]

		local var_27_3 = arg_27_0.popPool(var_27_1)

		arg_27_2(var_27_3)
	else
		ResourceMgr.Inst.getAssetAsync(var_27_0, arg_27_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_28_0)
			if not arg_27_0._poolRoot:
				var_0_4.Destroy(arg_28_0)

				return
			else
				assert(arg_28_0, "飞机资源加载失败：" .. arg_27_1)
				arg_27_0.InitPool(var_27_0, arg_28_0)

				var_27_1 = arg_27_0._allPool[var_27_0]

				local var_28_0 = arg_27_0.popPool(var_27_1)

				arg_27_2(var_28_0)), True, True)

def var_0_5.InstBullet(arg_29_0, arg_29_1, arg_29_2):
	local var_29_0 = arg_29_0.GetBulletPath(arg_29_1)
	local var_29_1 = arg_29_0._allPool[var_29_0]

	if var_29_1:
		local var_29_2 = arg_29_0.popPool(var_29_1, True)

		if string.find(arg_29_1, "_trail"):
			local var_29_3 = var_29_2.GetComponentInChildren(typeof(UnityEngine.TrailRenderer))

			if var_29_3:
				var_29_3.Clear()

		arg_29_2(var_29_2)

		return True
	elif arg_29_0._resCacheList[var_29_0] != None:
		arg_29_0.InitPool(var_29_0, arg_29_0._resCacheList[var_29_0])

		var_29_1 = arg_29_0._allPool[var_29_0]

		local var_29_4 = arg_29_0.popPool(var_29_1, True)

		if string.find(arg_29_1, "_trail"):
			local var_29_5 = var_29_4.GetComponentInChildren(typeof(UnityEngine.TrailRenderer))

			if var_29_5:
				var_29_5.Clear()

		arg_29_2(var_29_4)

		return True
	else
		ResourceMgr.Inst.getAssetAsync(var_29_0, arg_29_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_30_0)
			if arg_29_0._poolRoot:
				var_0_4.Destroy(arg_30_0)

				return
			else
				assert(arg_30_0, "子弹资源加载失败：" .. arg_29_1)
				arg_29_0.InitPool(var_29_0, arg_30_0)

				var_29_1 = arg_29_0._allPool[var_29_0]

				local var_30_0 = arg_29_0.popPool(var_29_1, True)

				arg_29_2(var_30_0)), True, True)

		return False

def var_0_5.InstFX(arg_31_0, arg_31_1, arg_31_2):
	local var_31_0 = arg_31_0.GetFXPath(arg_31_1)
	local var_31_1
	local var_31_2 = arg_31_0._allPool[var_31_0]

	if var_31_2:
		var_31_1 = arg_31_0.popPool(var_31_2, arg_31_2)
	elif arg_31_0._resCacheList[var_31_0] != None:
		arg_31_0.InitPool(var_31_0, arg_31_0._resCacheList[var_31_0])

		local var_31_3 = arg_31_0._allPool[var_31_0]

		var_31_1 = arg_31_0.popPool(var_31_3, arg_31_2)
	else
		ResourceMgr.Inst.getAssetAsync(var_31_0, arg_31_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_32_0)
			if not arg_31_0._poolRoot:
				var_0_4.Destroy(arg_32_0)

				return
			else
				assert(arg_32_0, "特效资源加载失败：" .. arg_31_1)
				arg_31_0.InitPool(var_31_0, arg_32_0)), True, True)

		var_31_1 = GameObject(arg_31_1 .. "临时假obj")

		var_31_1.SetActive(False)

		arg_31_0._resCacheList[var_31_0] = var_31_1

	return var_31_1

def var_0_5.InstOrbit(arg_33_0, arg_33_1):
	local var_33_0 = arg_33_0.GetOrbitPath(arg_33_1)
	local var_33_1
	local var_33_2 = arg_33_0._allPool[var_33_0]

	if var_33_2:
		var_33_1 = arg_33_0.popPool(var_33_2)
	elif arg_33_0._resCacheList[var_33_0] != None:
		arg_33_0.InitPool(var_33_0, arg_33_0._resCacheList[var_33_0])

		local var_33_3 = arg_33_0._allPool[var_33_0]

		var_33_1 = arg_33_0.popPool(var_33_3)
	else
		ResourceMgr.Inst.getAssetAsync(var_33_0, arg_33_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_34_0)
			if not arg_33_0._poolRoot:
				var_0_4.Destroy(arg_34_0)

				return
			else
				assert(arg_34_0, "特效资源加载失败：" .. arg_33_1)
				arg_33_0.InitPool(var_33_0, arg_34_0)), True, True)

		var_33_1 = GameObject(arg_33_1 .. "临时假obj")

		var_33_1.SetActive(False)

		arg_33_0._resCacheList[var_33_0] = var_33_1

	return var_33_1

def var_0_5.InstSkillPaintingUI(arg_35_0):
	local var_35_0 = arg_35_0._allPool["UI/SkillPainting"]
	local var_35_1 = var_35_0.GetObject()

	arg_35_0._ob2Pool[var_35_1] = var_35_0

	return var_35_1

def var_0_5.InstBossWarningUI(arg_36_0):
	local var_36_0 = arg_36_0._allPool["UI/MonsterAppearUI"]
	local var_36_1 = var_36_0.GetObject()

	arg_36_0._ob2Pool[var_36_1] = var_36_0

	return var_36_1

def var_0_5.InstGridmanSkillUI(arg_37_0):
	local var_37_0 = arg_37_0._allPool["UI/combatgridmanskillfloat"]
	local var_37_1 = var_37_0.GetObject()

	arg_37_0._ob2Pool[var_37_1] = var_37_0

	return var_37_1

def var_0_5.InstPainting(arg_38_0, arg_38_1):
	local var_38_0 = arg_38_0.GetPaintingPath(arg_38_1)
	local var_38_1
	local var_38_2 = arg_38_0._allPool[var_38_0]

	if var_38_2:
		var_38_1 = var_38_2.GetObject()
		arg_38_0._ob2Pool[var_38_1] = var_38_2
	elif arg_38_0._resCacheList[var_38_0] != None:
		var_38_1 = Object.Instantiate(arg_38_0._resCacheList[var_38_0])

		var_38_1.SetActive(True)

	return var_38_1

def var_0_5.InstMap(arg_39_0, arg_39_1):
	local var_39_0 = arg_39_0.GetMapPath(arg_39_1)
	local var_39_1
	local var_39_2 = arg_39_0._allPool[var_39_0]

	if var_39_2:
		var_39_1 = var_39_2.GetObject()
		arg_39_0._ob2Pool[var_39_1] = var_39_2
	elif arg_39_0._resCacheList[var_39_0] != None:
		var_39_1 = Object.Instantiate(arg_39_0._resCacheList[var_39_0])
	else
		assert(False, "地图资源没有预加载：" .. arg_39_1)

	var_39_1.SetActive(True)

	return var_39_1

def var_0_5.InstCardPuzzleCard(arg_40_0):
	local var_40_0 = arg_40_0._allPool["UI/CardTowerCardCombat"]
	local var_40_1 = var_40_0.GetObject()

	arg_40_0._ob2Pool[var_40_1] = var_40_0

	return var_40_1

def var_0_5.GetCharacterIcon(arg_41_0, arg_41_1):
	return arg_41_0._resCacheList[var_0_5.GetHrzIcon(arg_41_1)]

def var_0_5.GetCharacterSquareIcon(arg_42_0, arg_42_1):
	return arg_42_0._resCacheList[var_0_5.GetSquareIcon(arg_42_1)]

def var_0_5.GetCharacterQIcon(arg_43_0, arg_43_1):
	return arg_43_0._resCacheList[var_0_5.GetQIcon(arg_43_1)]

def var_0_5.GetAircraftIcon(arg_44_0, arg_44_1):
	return arg_44_0._resCacheList[var_0_5.GetAircraftIconPath(arg_44_1)]

def var_0_5.GetShipTypeIcon(arg_45_0, arg_45_1):
	return arg_45_0._resCacheList[var_0_5.GetShipTypeIconPath(arg_45_1)]

def var_0_5.GetCommanderHrzIcon(arg_46_0, arg_46_1):
	return arg_46_0._resCacheList[var_0_5.GetCommanderHrzIconPath(arg_46_1)]

def var_0_5.GetShader(arg_47_0, arg_47_1):
	return (pg.ShaderMgr.GetInstance().GetShader(var_0_3.BATTLE_SHADER[arg_47_1]))

def var_0_5.AddPreloadResource(arg_48_0, arg_48_1):
	if type(arg_48_1) == "string":
		arg_48_0._preloadList[arg_48_1] = False
	elif type(arg_48_1) == "table":
		for iter_48_0, iter_48_1 in ipairs(arg_48_1):
			arg_48_0._preloadList[iter_48_1] = False

def var_0_5.AddPreloadCV(arg_49_0, arg_49_1):
	local var_49_0 = Ship.getCVKeyID(arg_49_1)

	if var_49_0 > 0:
		arg_49_0._battleCVList[var_49_0] = pg.CriMgr.GetBattleCVBankName(var_49_0)

def var_0_5.StartPreload(arg_50_0, arg_50_1, arg_50_2):
	local var_50_0 = 0
	local var_50_1 = 0

	for iter_50_0, iter_50_1 in pairs(arg_50_0._preloadList):
		var_50_1 = var_50_1 + 1

	for iter_50_2, iter_50_3 in pairs(arg_50_0._battleCVList):
		var_50_1 = var_50_1 + 1

	local function var_50_2()
		if not arg_50_0._poolRoot:
			return

		var_50_0 = var_50_0 + 1

		if var_50_0 > var_50_1:
			return

		if arg_50_2:
			arg_50_2(var_50_0)

		if var_50_0 == var_50_1:
			arg_50_0._preloadList = None

			arg_50_1()

	for iter_50_4, iter_50_5 in pairs(arg_50_0._battleCVList):
		pg.CriMgr.GetInstance().LoadBattleCV(iter_50_4, var_50_2)

	for iter_50_6, iter_50_7 in pairs(arg_50_0._preloadList):
		local var_50_3 = arg_50_0.GetResName(iter_50_6)

		if var_50_3 == "" or arg_50_0._resCacheList[iter_50_6] != None:
			var_50_2()
		elif string.find(iter_50_6, "herohrzicon/") or string.find(iter_50_6, "qicon/") or string.find(iter_50_6, "squareicon/") or string.find(iter_50_6, "commanderhrz/") or string.find(iter_50_6, "AircraftIcon/"):
			local var_50_4, var_50_5 = HXSet.autoHxShiftPath(iter_50_6, var_50_3)

			ResourceMgr.Inst.getAssetAsync(var_50_4, "", typeof(Sprite), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_52_0)
				if arg_52_0 == None:
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot:
						var_0_4.Destroy(arg_52_0)

						return

					if arg_50_0._resCacheList:
						arg_50_0._resCacheList[iter_50_6] = arg_52_0

				var_50_2()), True, True)
		elif string.find(iter_50_6, "shiptype/"):
			local var_50_6 = string.split(iter_50_6, "/")[2]

			ResourceMgr.Inst.getAssetAsync("shiptype", var_50_6, typeof(Sprite), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_53_0)
				if arg_53_0 == None:
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot:
						var_0_4.Destroy(arg_53_0)

						return

					if arg_50_0._resCacheList:
						arg_50_0._resCacheList[iter_50_6] = arg_53_0

				var_50_2()), True, True)
		elif string.find(iter_50_6, "painting/"):
			local var_50_7 = False

			if PlayerPrefs.GetInt(BATTLE_HIDE_BG, 1) > 0:
				var_50_7 = checkABExist("painting/" .. var_50_3 .. "_n")
			else
				var_50_7 = PlayerPrefs.GetInt("paint_hide_other_obj_" .. var_50_3, 0) != 0

			PoolMgr.GetInstance().GetPainting(var_50_3 .. (var_50_7 and "_n" or ""), True, function(arg_54_0)
				if arg_54_0 == None:
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot:
						var_0_5.ClearPaintingRes(iter_50_6, arg_54_0)

						return

					ShipExpressionHelper.SetExpression(arg_54_0, var_50_3)
					arg_54_0.SetActive(False)

					if arg_50_0._resCacheList:
						arg_50_0._resCacheList[iter_50_6] = arg_54_0

				var_50_2())
		elif string.find(iter_50_6, "Char/"):
			arg_50_0.LoadSpineAsset(var_50_3, function(arg_55_0)
				if arg_55_0 == None:
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					arg_55_0 = SpineAnim.AnimChar(var_50_3, arg_55_0)

					if not arg_50_0._poolRoot:
						var_0_5.ClearCharRes(iter_50_6, arg_55_0)

						return

					arg_55_0.SetActive(False)

					if arg_50_0._resCacheList:
						arg_50_0._resCacheList[iter_50_6] = arg_55_0

				arg_50_0.InitPool(iter_50_6, arg_55_0)
				var_50_2())
		elif string.find(iter_50_6, "UI/"):
			LoadAndInstantiateAsync("UI", var_50_3, function(arg_56_0)
				if arg_56_0 == None:
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot:
						var_0_4.Destroy(arg_56_0)

						return

					arg_56_0.SetActive(False)

					if arg_50_0._resCacheList:
						arg_50_0._resCacheList[iter_50_6] = arg_56_0

				arg_50_0.InitPool(iter_50_6, arg_56_0)
				var_50_2(), True, True)
		else
			ResourceMgr.Inst.getAssetAsync(iter_50_6, var_50_3, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_57_0)
				if arg_57_0 == None:
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot:
						var_0_4.Destroy(arg_57_0)

						return

					if arg_50_0._resCacheList:
						arg_50_0._resCacheList[iter_50_6] = arg_57_0

				arg_50_0.InitPool(iter_50_6, arg_57_0)
				var_50_2()), True, True)

	return var_50_1

local var_0_6 = Vector3(0, 10000, 0)

def var_0_5.HideBullet(arg_58_0):
	arg_58_0.transform.position = var_0_6

def var_0_5.InitParticleSystemCB(arg_59_0):
	pg.EffectMgr.GetInstance().CommonEffectEvent(arg_59_0)

def var_0_5.InitPool(arg_60_0, arg_60_1, arg_60_2):
	local var_60_0 = arg_60_0._poolRoot.transform

	if string.find(arg_60_1, "Item/"):
		if arg_60_2.GetComponentInChildren(typeof(UnityEngine.TrailRenderer)) != None or arg_60_2.GetComponentInChildren(typeof(ParticleSystem)) != None:
			arg_60_0._allPool[arg_60_1] = pg.Pool.New(arg_60_0._bulletContainer.transform, arg_60_2, 15, 20, True, False).InitSize()
		else
			local var_60_1 = pg.Pool.New(arg_60_0._bulletContainer.transform, arg_60_2, 20, 20, True, True)

			var_60_1.SetRecycleFuncs(var_0_5.HideBullet)
			var_60_1.InitSize()

			arg_60_0._allPool[arg_60_1] = var_60_1
	elif string.find(arg_60_1, "Effect/"):
		if arg_60_2.GetComponent(typeof(UnityEngine.ParticleSystem)):
			local var_60_2 = 5

			if string.find(arg_60_1, "smoke") and not string.find(arg_60_1, "smokeboom"):
				var_60_2 = 30
			elif string.find(arg_60_1, "feijiyingzi"):
				var_60_2 = 1

			local var_60_3 = pg.Pool.New(var_60_0, arg_60_2, var_60_2, 20, False, False)

			var_60_3.SetInitFuncs(var_0_5.InitParticleSystemCB)
			var_60_3.InitSize()

			arg_60_0._allPool[arg_60_1] = var_60_3
		else
			local var_60_4 = 8

			if string.find(arg_60_1, "AntiAirArea") or string.find(arg_60_1, "AntiSubArea"):
				var_60_4 = 1

			GetOrAddComponent(arg_60_2, typeof(ParticleSystemEvent))

			local var_60_5 = pg.Pool.New(var_60_0, arg_60_2, var_60_4, 20, False, False)

			var_60_5.InitSize()

			arg_60_0._allPool[arg_60_1] = var_60_5
	elif string.find(arg_60_1, "Char/"):
		local var_60_6 = 1

		if string.find(arg_60_1, "danchuan"):
			var_60_6 = 3

		local var_60_7 = pg.Pool.New(var_60_0, arg_60_2, var_60_6, 20, False, False).InitSize()

		var_60_7.SetRecycleFuncs(var_0_5.ResetSpineAction)

		arg_60_0._allPool[arg_60_1] = var_60_7
	elif string.find(arg_60_1, "chargo/"):
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 3, 20, False, False).InitSize()
	elif string.find(arg_60_1, "orbit/"):
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 2, 20, False, False).InitSize()
	elif arg_60_1 == "UI/SkillPainting":
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 1, 20, False, False).InitSize()
	elif arg_60_1 == "UI/MonsterAppearUI":
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 1, 20, False, False).InitSize()
	elif arg_60_1 == "UI/CardTowerCardCombat":
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 7, 20, False, False).InitSize()
	elif arg_60_1 == "UI/combatgridmanskillfloat":
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 1, 20, False, False).InitSize()
	elif arg_60_1 == "UI/CombatHPBar":
		var_0_0.Battle.BattleHPBarManager.GetInstance().Init(arg_60_2, var_60_0)
	elif arg_60_1 == "UI/CombatHPPop":
		var_0_0.Battle.BattlePopNumManager.GetInstance().Init(arg_60_2, var_60_0)

def var_0_5.GetRotateScript(arg_61_0, arg_61_1, arg_61_2):
	local var_61_0 = arg_61_0.rotateScriptMap

	if var_61_0[arg_61_1]:
		return var_61_0[arg_61_1]

	local var_61_1 = GetOrAddComponent(arg_61_1, "BulletRotation")

	var_61_0[arg_61_1] = var_61_1

	return var_61_1

def var_0_5.GetCommonResource():
	return {
		var_0_5.GetMapPath("visionLine"),
		var_0_5.GetMapPath("exposeLine"),
		var_0_5.GetFXPath(var_0_0.Battle.BattleCharacterFactory.MOVE_WAVE_FX_NAME),
		var_0_5.GetFXPath(var_0_0.Battle.BattleCharacterFactory.BOMB_FX_NAME),
		var_0_5.GetFXPath(var_0_0.Battle.BattleBossCharacterFactory.BOMB_FX_NAME),
		var_0_5.GetFXPath(var_0_0.Battle.BattleAircraftCharacterFactory.BOMB_FX_NAME),
		var_0_5.GetFXPath("AlertArea"),
		var_0_5.GetFXPath("TorAlert"),
		var_0_5.GetFXPath("SquareAlert"),
		var_0_5.GetFXPath("AntiAirArea"),
		var_0_5.GetFXPath("AntiSubArea"),
		var_0_5.GetFXPath("AimBiasArea"),
		var_0_5.GetFXPath("shock"),
		var_0_5.GetFXPath("qianting_chushui"),
		var_0_5.GetFXPath(var_0_3.PLAYER_SUB_BUBBLE_FX),
		var_0_5.GetFXPath("weaponrange"),
		var_0_5.GetUIPath("SkillPainting"),
		var_0_5.GetUIPath("MonsterAppearUI"),
		var_0_5.GetUIPath("CombatHPBar"),
		var_0_5.GetUIPath("CombatHPPop")
	}

def var_0_5.GetDisplayCommonResource():
	return {
		var_0_5.GetFXPath(var_0_0.Battle.BattleCharacterFactory.MOVE_WAVE_FX_NAME),
		var_0_5.GetFXPath(var_0_0.Battle.BattleCharacterFactory.BOMB_FX_NAME),
		var_0_5.GetFXPath(var_0_0.Battle.BattleCharacterFactory.DANCHUAN_MOVE_WAVE_FX_NAME)
	}

def var_0_5.GetMapResource(arg_64_0):
	local var_64_0 = {}
	local var_64_1 = var_0_0.Battle.BattleMap

	for iter_64_0, iter_64_1 in ipairs(var_64_1.LAYERS):
		local var_64_2 = var_64_1.GetMapResNames(arg_64_0, iter_64_1)

		for iter_64_2, iter_64_3 in ipairs(var_64_2):
			var_64_0[#var_64_0 + 1] = var_0_5.GetMapPath(iter_64_3)

	return var_64_0

def var_0_5.GetBuffResource():
	local var_65_0 = {}
	local var_65_1 = require("buffFXPreloadList")

	for iter_65_0, iter_65_1 in ipairs(var_65_1):
		var_65_0[#var_65_0 + 1] = var_0_5.GetFXPath(iter_65_1)

	return var_65_0

def var_0_5.GetShipResource(arg_66_0, arg_66_1, arg_66_2):
	local var_66_0 = {}
	local var_66_1 = var_0_1.GetPlayerShipTmpDataFromID(arg_66_0)

	if arg_66_1 == None or arg_66_1 == 0:
		arg_66_1 = var_66_1.skin_id

	local var_66_2 = var_0_1.GetPlayerShipSkinDataFromID(arg_66_1)

	var_66_0[#var_66_0 + 1] = var_0_5.GetCharacterPath(var_66_2.prefab)
	var_66_0[#var_66_0 + 1] = var_0_5.GetHrzIcon(var_66_2.painting)
	var_66_0[#var_66_0 + 1] = var_0_5.GetQIcon(var_66_2.painting)
	var_66_0[#var_66_0 + 1] = var_0_5.GetSquareIcon(var_66_2.painting)

	if arg_66_2 and var_0_1.GetShipTypeTmp(var_66_1.type).team_type == TeamType.Main:
		var_66_0[#var_66_0 + 1] = var_0_5.GetPaintingPath(var_66_2.painting)

	return var_66_0

def var_0_5.GetEnemyResource(arg_67_0):
	local var_67_0 = {}
	local var_67_1 = arg_67_0.monsterTemplateID
	local var_67_2 = arg_67_0.bossData != None
	local var_67_3 = arg_67_0.buffList or {}
	local var_67_4 = arg_67_0.phase or {}
	local var_67_5 = var_0_1.GetMonsterTmpDataFromID(var_67_1)

	var_67_0[#var_67_0 + 1] = var_0_5.GetCharacterPath(var_67_5.prefab)
	var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(var_67_5.wave_fx)

	if var_67_5.fog_fx:
		var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(var_67_5.fog_fx)

	for iter_67_0, iter_67_1 in ipairs(var_67_5.appear_fx):
		var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(iter_67_1)

	for iter_67_2, iter_67_3 in ipairs(var_67_5.smoke):
		local var_67_6 = iter_67_3[2]

		for iter_67_4, iter_67_5 in ipairs(var_67_6):
			var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(iter_67_5[1])

	if arg_67_0.deadFX:
		var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(arg_67_0.deadFX)

	if type(var_67_5.bubble_fx) == "table":
		var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(var_67_5.bubble_fx[1])

	local function var_67_7(arg_68_0)
		local var_68_0 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(arg_68_0, 1)

		for iter_68_0, iter_68_1 in pairs(var_68_0.effect_list):
			local var_68_1 = iter_68_1.arg_list.skill_id

			if var_68_1:
				local var_68_2 = var_0_0.Battle.BattleDataFunction.GetSkillTemplate(var_68_1).painting

				if var_68_2 == 1:
					var_67_0[#var_67_0 + 1] = var_0_5.GetHrzIcon(var_67_5.icon)
				elif type(var_68_2) == "string":
					var_67_0[#var_67_0 + 1] = var_0_5.GetHrzIcon(var_68_2)

			local var_68_3 = iter_68_1.arg_list.buff_id

			if var_68_3:
				var_67_7(var_68_3)

	for iter_67_6, iter_67_7 in ipairs(var_67_3):
		var_67_7(iter_67_7)

	for iter_67_8, iter_67_9 in ipairs(var_67_4):
		if iter_67_9.addBuff:
			for iter_67_10, iter_67_11 in ipairs(iter_67_9.addBuff):
				var_67_7(iter_67_11)

	if var_67_2:
		var_67_0[#var_67_0 + 1] = var_0_5.GetSquareIcon(var_67_5.icon)

	return var_67_0

def var_0_5.GetWeaponResource(arg_69_0, arg_69_1):
	local var_69_0 = {}

	if arg_69_0 == -1:
		return var_69_0

	local var_69_1 = var_0_1.GetWeaponPropertyDataFromID(arg_69_0)

	if var_69_1.type == var_0_2.EquipmentType.MAIN_CANNON or var_69_1.type == var_0_2.EquipmentType.SUB_CANNON or var_69_1.type == var_0_2.EquipmentType.TORPEDO or var_69_1.type == var_0_2.EquipmentType.ANTI_AIR or var_69_1.type == var_0_2.EquipmentType.ANTI_SEA or var_69_1.type == var_0_2.EquipmentType.POINT_HIT_AND_LOCK or var_69_1.type == var_0_2.EquipmentType.MANUAL_METEOR or var_69_1.type == var_0_2.EquipmentType.BOMBER_PRE_CAST_ALERT or var_69_1.type == var_0_2.EquipmentType.DEPTH_CHARGE or var_69_1.type == var_0_2.EquipmentType.MANUAL_TORPEDO or var_69_1.type == var_0_2.EquipmentType.DISPOSABLE_TORPEDO or var_69_1.type == var_0_2.EquipmentType.MANUAL_AAMISSILE or var_69_1.type == var_0_2.EquipmentType.BEAM or var_69_1.type == var_0_2.EquipmentType.SPACE_LASER or var_69_1.type == var_0_2.EquipmentType.FLEET_RANGE_ANTI_AIR or var_69_1.type == var_0_2.EquipmentType.MANUAL_MISSILE or var_69_1.type == var_0_2.EquipmentType.AUTO_MISSILE or var_69_1.type == var_0_2.EquipmentType.MISSILE:
		for iter_69_0, iter_69_1 in ipairs(var_69_1.bullet_ID):
			local var_69_2 = var_0_5.GetBulletResource(iter_69_1, arg_69_1)

			for iter_69_2, iter_69_3 in ipairs(var_69_2):
				var_69_0[#var_69_0 + 1] = iter_69_3
	elif var_69_1.type == var_0_2.EquipmentType.INTERCEPT_AIRCRAFT or var_69_1.type == var_0_2.EquipmentType.STRIKE_AIRCRAFT:
		var_69_0 = var_0_5.GetAircraftResource(arg_69_0, None, arg_69_1)
	elif var_69_1.type == var_0_2.EquipmentType.PREVIEW_ARICRAFT:
		for iter_69_4, iter_69_5 in ipairs(var_69_1.bullet_ID):
			var_69_0 = var_0_5.GetAircraftResource(iter_69_5, None, arg_69_1)

	if var_69_1.type == var_0_2.EquipmentType.FLEET_RANGE_ANTI_AIR:
		local var_69_3 = var_0_5.GetBulletResource(var_0_3.AntiAirConfig.RangeBulletID)

		for iter_69_6, iter_69_7 in ipairs(var_69_3):
			var_69_0[#var_69_0 + 1] = iter_69_7

	local var_69_4

	if arg_69_1 and arg_69_1 != 0:
		var_69_4 = var_0_0.Battle.BattleDataFunction.GetEquipSkinDataFromID(arg_69_1)

	if var_69_4 and var_69_4.fire_fx_name != "":
		var_69_0[#var_69_0 + 1] = var_0_5.GetFXPath(var_69_4.fire_fx_name)
	else
		var_69_0[#var_69_0 + 1] = var_0_5.GetFXPath(var_69_1.fire_fx)

	if var_69_1.precast_param.fx:
		var_69_0[#var_69_0 + 1] = var_0_5.GetFXPath(var_69_1.precast_param.fx)

	if var_69_4:
		local var_69_5 = var_69_4.orbit_combat

		if var_69_5 != "":
			var_69_0[#var_69_0 + 1] = var_0_5.GetOrbitPath(var_69_5)

	return var_69_0

def var_0_5.GetEquipResource(arg_70_0, arg_70_1, arg_70_2):
	local var_70_0 = {}

	if arg_70_1 != 0:
		local var_70_1 = var_0_0.Battle.BattleDataFunction.GetEquipSkinDataFromID(arg_70_1)
		local var_70_2 = var_70_1.ship_skin_id

		if var_70_2 != 0:
			local var_70_3 = var_0_0.Battle.BattleDataFunction.GetPlayerShipSkinDataFromID(var_70_2)

			var_70_0[#var_70_0 + 1] = var_0_5.GetCharacterPath(var_70_3.prefab)

		local var_70_4 = var_70_1.orbit_combat

		if var_70_4 != "":
			var_70_0[#var_70_0 + 1] = var_0_5.GetOrbitPath(var_70_4)

	local var_70_5 = var_0_0.Battle.BattleDataFunction.GetWeaponDataFromID(arg_70_0)
	local var_70_6 = var_70_5.weapon_id

	for iter_70_0, iter_70_1 in ipairs(var_70_6):
		local var_70_7 = var_0_5.GetWeaponResource(iter_70_1)

		for iter_70_2, iter_70_3 in ipairs(var_70_7):
			var_70_0[#var_70_0 + 1] = iter_70_3

	local var_70_8 = var_70_5.skill_id

	for iter_70_4, iter_70_5 in ipairs(var_70_8):
		iter_70_5 = arg_70_2 and var_0_0.Battle.BattleDataFunction.SkillTranform(arg_70_2, iter_70_5) or iter_70_5

		local var_70_9 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_70_5, 1, {})

		for iter_70_6, iter_70_7 in ipairs(var_70_9):
			var_70_0[#var_70_0 + 1] = iter_70_7

	return var_70_0

def var_0_5.GetBulletResource(arg_71_0, arg_71_1):
	local var_71_0 = {}
	local var_71_1

	if arg_71_1 != None and arg_71_1 != 0:
		var_71_1 = var_0_1.GetEquipSkinDataFromID(arg_71_1)

	local var_71_2 = var_0_1.GetBulletTmpDataFromID(arg_71_0)
	local var_71_3

	if var_71_1:
		var_71_3 = var_71_1.bullet_name

		if var_71_1.mirror == 1:
			var_71_0[#var_71_0 + 1] = var_0_5.GetBulletPath(var_71_3 .. var_0_0.Battle.BattleBulletUnit.MIRROR_RES)
	else
		var_71_3 = var_71_2.modle_ID

	if var_71_2.type == var_0_2.BulletType.BEAM or var_71_2.type == var_0_2.BulletType.SPACE_LASER or var_71_2.type == var_0_2.BulletType.MISSILE or var_71_2.type == var_0_2.BulletType.ELECTRIC_ARC:
		var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_2.modle_ID)
	else
		var_71_0[#var_71_0 + 1] = var_0_5.GetBulletPath(var_71_3)

	if var_71_2.extra_param.mirror:
		var_71_0[#var_71_0 + 1] = var_0_5.GetBulletPath(var_71_3 .. var_0_0.Battle.BattleBulletUnit.MIRROR_RES)

	local var_71_4

	if var_71_1 and var_71_1.hit_fx_name != "":
		var_71_4 = var_71_1.hit_fx_name
	else
		var_71_4 = var_71_2.hit_fx

	var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_4)
	var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_2.miss_fx)
	var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_2.alert_fx)

	if var_71_2.extra_param.area_FX:
		var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_2.extra_param.area_FX)

	if var_71_2.extra_param.shrapnel:
		for iter_71_0, iter_71_1 in ipairs(var_71_2.extra_param.shrapnel):
			local var_71_5 = var_0_5.GetBulletResource(iter_71_1.bullet_ID)

			for iter_71_2, iter_71_3 in ipairs(var_71_5):
				var_71_0[#var_71_0 + 1] = iter_71_3

	for iter_71_4, iter_71_5 in ipairs(var_71_2.attach_buff):
		if iter_71_5.effect_id:
			var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(iter_71_5.effect_id)

		if iter_71_5.buff_id:
			local var_71_6 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_71_5.buff_id, 1, {})

			for iter_71_6, iter_71_7 in ipairs(var_71_6):
				var_71_0[#var_71_0 + 1] = iter_71_7

	return var_71_0

def var_0_5.GetAircraftResource(arg_72_0, arg_72_1, arg_72_2):
	local var_72_0 = {}

	arg_72_2 = arg_72_2 or 0

	local var_72_1 = var_0_1.GetAircraftTmpDataFromID(arg_72_0)
	local var_72_2
	local var_72_3
	local var_72_4
	local var_72_5

	if arg_72_2 != 0:
		local var_72_6, var_72_7, var_72_8

		var_72_2, var_72_6, var_72_7, var_72_8 = var_0_1.GetEquipSkin(arg_72_2)

		if var_72_6 != "":
			var_72_0[#var_72_0 + 1] = var_0_5.GetBulletPath(var_72_6)

		if var_72_7 != "":
			var_72_0[#var_72_0 + 1] = var_0_5.GetBulletPath(var_72_7)

		if var_72_8 != "":
			var_72_0[#var_72_0 + 1] = var_0_5.GetBulletPath(var_72_8)
	else
		var_72_2 = var_72_1.model_ID

	var_72_0[#var_72_0 + 1] = var_0_5.GetCharacterGoPath(var_72_2)
	var_72_0[#var_72_0 + 1] = var_0_5.GetAircraftIconPath(var_72_1.model_ID)

	local var_72_9 = arg_72_1 or var_72_1.weapon_ID

	if type(var_72_9) == "table":
		for iter_72_0, iter_72_1 in ipairs(var_72_9):
			local var_72_10 = var_0_5.GetWeaponResource(iter_72_1)

			for iter_72_2, iter_72_3 in ipairs(var_72_10):
				var_72_0[#var_72_0 + 1] = iter_72_3
	else
		local var_72_11 = var_0_5.GetWeaponResource(var_72_9)

		for iter_72_4, iter_72_5 in ipairs(var_72_11):
			var_72_0[#var_72_0 + 1] = iter_72_5

	return var_72_0

def var_0_5.GetCommanderResource(arg_73_0):
	local var_73_0 = {}
	local var_73_1 = arg_73_0[1]

	var_73_0[#var_73_0 + 1] = var_0_5.GetCommanderHrzIconPath(var_73_1.getPainting())

	local var_73_2 = var_73_1.getSkills()[1].getLevel()

	for iter_73_0, iter_73_1 in ipairs(arg_73_0[2]):
		local var_73_3 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_73_1, var_73_2, {})

		for iter_73_2, iter_73_3 in ipairs(var_73_3):
			var_73_0[#var_73_0 + 1] = iter_73_3

	return var_73_0

def var_0_5.GetStageResource(arg_74_0):
	local var_74_0 = var_0_0.Battle.BattleDataFunction.GetDungeonTmpDataByID(arg_74_0)
	local var_74_1 = {}
	local var_74_2 = {}

	for iter_74_0, iter_74_1 in ipairs(var_74_0.stages):
		for iter_74_2, iter_74_3 in ipairs(iter_74_1.waves):
			if iter_74_3.triggerType == var_0_0.Battle.BattleConst.WaveTriggerType.NORMAL:
				for iter_74_4, iter_74_5 in ipairs(iter_74_3.spawn):
					local var_74_3 = var_0_5.GetMonsterRes(iter_74_5)

					for iter_74_6, iter_74_7 in ipairs(var_74_3):
						table.insert(var_74_1, iter_74_7)

				if iter_74_3.reinforcement:
					for iter_74_8, iter_74_9 in ipairs(iter_74_3.reinforcement):
						local var_74_4 = var_0_5.GetMonsterRes(iter_74_9)

						for iter_74_10, iter_74_11 in ipairs(var_74_4):
							table.insert(var_74_1, iter_74_11)
			elif iter_74_3.triggerType == var_0_0.Battle.BattleConst.WaveTriggerType.AID:
				local var_74_5 = iter_74_3.triggerParams.vanguard_unitList
				local var_74_6 = iter_74_3.triggerParams.main_unitList
				local var_74_7 = iter_74_3.triggerParams.sub_unitList

				local function var_74_8(arg_75_0)
					local var_75_0 = var_0_5.GetAidUnitsRes(arg_75_0)

					for iter_75_0, iter_75_1 in ipairs(var_75_0):
						table.insert(var_74_1, iter_75_1)

					for iter_75_2, iter_75_3 in ipairs(arg_75_0):
						var_74_2[#var_74_2 + 1] = iter_75_3.skinId

				if var_74_5:
					var_74_8(var_74_5)

				if var_74_6:
					var_74_8(var_74_6)

				if var_74_7:
					var_74_8(var_74_7)
			elif iter_74_3.triggerType == var_0_0.Battle.BattleConst.WaveTriggerType.ENVIRONMENT:
				for iter_74_12, iter_74_13 in ipairs(iter_74_3.spawn):
					var_0_5.GetEnvironmentRes(var_74_1, iter_74_13)
			elif iter_74_3.triggerType == var_0_0.Battle.BattleConst.WaveTriggerType.CARD_PUZZLE:
				local var_74_9 = var_0_0.Battle.BattleDataFunction.GetCardRes(iter_74_3.triggerParams.card_id)

				for iter_74_14, iter_74_15 in ipairs(var_74_9):
					table.insert(var_74_1, iter_74_15)

			if iter_74_3.airFighter != None:
				for iter_74_16, iter_74_17 in pairs(iter_74_3.airFighter):
					local var_74_10 = var_0_5.GetAircraftResource(iter_74_17.templateID, iter_74_17.weaponID)

					for iter_74_18, iter_74_19 in ipairs(var_74_10):
						var_74_1[#var_74_1 + 1] = iter_74_19

	return var_74_1, var_74_2

def var_0_5.GetEnvironmentRes(arg_76_0, arg_76_1):
	table.insert(arg_76_0, arg_76_1.prefab and var_0_5.GetFXPath(arg_76_1.prefab))

	local var_76_0 = arg_76_1.behaviours
	local var_76_1 = var_0_0.Battle.BattleDataFunction.GetEnvironmentBehaviour(var_76_0).behaviour_list

	for iter_76_0, iter_76_1 in ipairs(var_76_1):
		local var_76_2 = iter_76_1.type

		if var_76_2 == var_0_0.Battle.BattleConst.EnviroumentBehaviour.BUFF:
			local var_76_3 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_76_1.buff_id, 1, {})

			for iter_76_2, iter_76_3 in ipairs(var_76_3):
				arg_76_0[#arg_76_0 + 1] = iter_76_3
		elif var_76_2 == var_0_0.Battle.BattleConst.EnviroumentBehaviour.SPAWN:
			local var_76_4 = iter_76_1.content and iter_76_1.content.alert and iter_76_1.content.alert.alert_fx

			table.insert(arg_76_0, var_76_4 and var_0_5.GetFXPath(var_76_4))

			local var_76_5 = iter_76_1.content and iter_76_1.content.child_prefab

			if var_76_5:
				var_0_5.GetEnvironmentRes(arg_76_0, var_76_5)
		elif var_76_2 == var_0_0.Battle.BattleConst.EnviroumentBehaviour.PLAY_FX:
			arg_76_0[#arg_76_0 + 1] = var_0_5.GetFXPath(iter_76_1.FX_ID)

def var_0_5.GetMonsterRes(arg_77_0):
	local var_77_0 = {}
	local var_77_1 = var_0_5.GetEnemyResource(arg_77_0)

	for iter_77_0, iter_77_1 in ipairs(var_77_1):
		var_77_0[#var_77_0 + 1] = iter_77_1

	local var_77_2 = var_0_0.Battle.BattleDataFunction.GetMonsterTmpDataFromID(arg_77_0.monsterTemplateID)
	local var_77_3 = Clone(var_77_2.equipment_list)
	local var_77_4 = var_77_2.buff_list
	local var_77_5 = Clone(arg_77_0.buffList) or {}

	if arg_77_0.phase:
		for iter_77_2, iter_77_3 in ipairs(arg_77_0.phase):
			if iter_77_3.addWeapon:
				for iter_77_4, iter_77_5 in ipairs(iter_77_3.addWeapon):
					var_77_3[#var_77_3 + 1] = iter_77_5

			if iter_77_3.addRandomWeapon:
				for iter_77_6, iter_77_7 in ipairs(iter_77_3.addRandomWeapon):
					for iter_77_8, iter_77_9 in ipairs(iter_77_7):
						var_77_3[#var_77_3 + 1] = iter_77_9

			if iter_77_3.addBuff:
				for iter_77_10, iter_77_11 in ipairs(iter_77_3.addBuff):
					var_77_5[#var_77_5 + 1] = iter_77_11

	for iter_77_12, iter_77_13 in ipairs(var_77_4):
		local var_77_6 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_77_13.ID, iter_77_13.LV, {})

		for iter_77_14, iter_77_15 in ipairs(var_77_6):
			var_77_0[#var_77_0 + 1] = iter_77_15

	for iter_77_16, iter_77_17 in ipairs(var_77_5):
		local var_77_7 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_77_17, 1, {})

		for iter_77_18, iter_77_19 in ipairs(var_77_7):
			var_77_0[#var_77_0 + 1] = iter_77_19

		local var_77_8 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(iter_77_17, 1)

		for iter_77_20, iter_77_21 in pairs(var_77_8.effect_list):
			local var_77_9 = iter_77_21.arg_list.skill_id

			if var_77_9 and var_0_0.Battle.BattleDataFunction.NeedSkillPainting(var_77_9):
				var_77_0[#var_77_0 + 1] = var_0_5.GetPaintingPath(var_0_1.GetMonsterTmpDataFromID(arg_77_0.monsterTemplateID).icon)

				break

	for iter_77_22, iter_77_23 in ipairs(var_77_3):
		local var_77_10 = var_0_5.GetWeaponResource(iter_77_23)

		for iter_77_24, iter_77_25 in ipairs(var_77_10):
			var_77_0[#var_77_0 + 1] = iter_77_25

	return var_77_0

def var_0_5.GetEquipSkinPreviewRes(arg_78_0):
	local var_78_0 = {}
	local var_78_1 = var_0_1.GetEquipSkinDataFromID(arg_78_0)

	for iter_78_0, iter_78_1 in ipairs(var_78_1.weapon_ids):
		local var_78_2 = var_0_5.GetWeaponResource(iter_78_1)

		for iter_78_2, iter_78_3 in ipairs(var_78_2):
			var_78_0[#var_78_0 + 1] = iter_78_3

	local function var_78_3(arg_79_0)
		if arg_79_0 != "":
			var_78_0[#var_78_0 + 1] = var_0_5.GetBulletPath(arg_79_0)

	local var_78_4, var_78_5, var_78_6, var_78_7, var_78_8, var_78_9 = var_0_1.GetEquipSkin(arg_78_0)

	if _.any(EquipType.AirProtoEquipTypes, function(arg_80_0)
		return table.contains(var_78_1.equip_type, arg_80_0)):
		var_78_0[#var_78_0 + 1] = var_0_5.GetCharacterGoPath(var_78_4)
	else
		var_78_0[#var_78_0 + 1] = var_0_5.GetBulletPath(var_78_4)

	var_78_3(var_78_5)
	var_78_3(var_78_6)
	var_78_3(var_78_7)

	if var_78_8 and var_78_8 != "":
		var_78_0[#var_78_0 + 1] = var_0_5.GetFXPath(var_78_8)

	if var_78_9 and var_78_9 != "":
		var_78_0[#var_78_0 + 1] = var_0_5.GetFXPath(var_78_9)

	return var_78_0

def var_0_5.GetEquipSkinBulletRes(arg_81_0):
	local var_81_0 = {}
	local var_81_1, var_81_2, var_81_3, var_81_4 = var_0_1.GetEquipSkin(arg_81_0)

	local function var_81_5(arg_82_0)
		if arg_82_0 != "":
			var_81_0[#var_81_0 + 1] = var_0_5.GetBulletPath(arg_82_0)

	local var_81_6 = var_0_1.GetEquipSkinDataFromID(arg_81_0)
	local var_81_7 = False

	for iter_81_0, iter_81_1 in ipairs(var_81_6.equip_type):
		if table.contains(EquipType.AircraftSkinType, iter_81_1):
			var_81_7 = True

	if var_81_7:
		if var_81_1 != "":
			var_81_0[#var_81_0 + 1] = var_0_5.GetCharacterGoPath(var_81_1)
	else
		var_81_5(var_81_1)

		if var_0_1.GetEquipSkinDataFromID(arg_81_0).mirror == 1:
			var_81_0[#var_81_0 + 1] = var_0_5.GetBulletPath(var_81_1 .. var_0_0.Battle.BattleBulletUnit.MIRROR_RES)

	var_81_5(var_81_2)
	var_81_5(var_81_3)
	var_81_5(var_81_4)

	return var_81_0

def var_0_5.GetAidUnitsRes(arg_83_0):
	local var_83_0 = {}

	for iter_83_0, iter_83_1 in ipairs(arg_83_0):
		local var_83_1 = var_0_5.GetShipResource(iter_83_1.tmpID, None, True)

		for iter_83_2, iter_83_3 in ipairs(iter_83_1.equipment):
			if iter_83_3 != 0:
				if iter_83_2 <= Ship.WEAPON_COUNT:
					local var_83_2 = var_0_1.GetWeaponDataFromID(iter_83_3).weapon_id

					for iter_83_4, iter_83_5 in ipairs(var_83_2):
						local var_83_3 = var_0_5.GetWeaponResource(iter_83_5)

						for iter_83_6, iter_83_7 in ipairs(var_83_3):
							table.insert(var_83_1, iter_83_7)
				else
					local var_83_4 = var_0_5.GetEquipResource(iter_83_3)

					for iter_83_8, iter_83_9 in ipairs(var_83_4):
						table.insert(var_83_1, iter_83_9)

		for iter_83_10, iter_83_11 in ipairs(var_83_1):
			table.insert(var_83_0, iter_83_11)

	return var_83_0

def var_0_5.GetSpWeaponResource(arg_84_0, arg_84_1):
	local var_84_0 = {}
	local var_84_1 = var_0_0.Battle.BattleDataFunction.GetSpWeaponDataFromID(arg_84_0).effect_id

	if var_84_1 != 0:
		var_84_1 = arg_84_1 and var_0_0.Battle.BattleDataFunction.SkillTranform(arg_84_1, var_84_1) or var_84_1

		local var_84_2 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(var_84_1, 1, {})

		for iter_84_0, iter_84_1 in ipairs(var_84_2):
			var_84_0[#var_84_0 + 1] = iter_84_1

	return var_84_0
