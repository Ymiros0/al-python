ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleConfig
local var_0_4 = require("Mgr/Pool/PoolUtil")
local var_0_5 = singletonClass("BattleResourceManager")

var_0_0.Battle.BattleResourceManager = var_0_5
var_0_5.__name = "BattleResourceManager"

function var_0_5.Ctor(arg_1_0)
	arg_1_0.rotateScriptMap = setmetatable({}, {
		__mode = "kv"
	})
end

function var_0_5.Init(arg_2_0)
	arg_2_0._preloadList = {}
	arg_2_0._resCacheList = {}
	arg_2_0._allPool = {}
	arg_2_0._ob2Pool = {}

	local var_2_0 = GameObject()

	var_2_0:SetActive(false)

	var_2_0.name = "PoolRoot"
	var_2_0.transform.position = Vector3(-10000, -10000, 0)
	arg_2_0._poolRoot = var_2_0
	arg_2_0._bulletContainer = GameObject("BulletContainer")
	arg_2_0._battleCVList = {}
end

function var_0_5.Clear(arg_3_0)
	for iter_3_0, iter_3_1 in pairs(arg_3_0._allPool) do
		iter_3_1:Dispose()
	end

	for iter_3_2, iter_3_3 in pairs(arg_3_0._resCacheList) do
		if string.find(iter_3_2, "Char/") then
			var_0_5.ClearCharRes(iter_3_2, iter_3_3)
		elseif string.find(iter_3_2, "painting/") then
			var_0_5.ClearPaintingRes(iter_3_2, iter_3_3)
		else
			var_0_4.Destroy(iter_3_3)
		end
	end

	arg_3_0._resCacheList = {}
	arg_3_0._ob2Pool = {}
	arg_3_0._allPool = {}

	Object.Destroy(arg_3_0._poolRoot)

	arg_3_0._poolRoot = nil

	Object.Destroy(arg_3_0._bulletContainer)

	arg_3_0._bulletContainer = nil
	arg_3_0.rotateScriptMap = setmetatable({}, {
		__mode = "kv"
	})

	for iter_3_4, iter_3_5 in pairs(arg_3_0._battleCVList) do
		pg.CriMgr.UnloadCVBank(iter_3_5)
	end

	arg_3_0._battleCVList = {}

	var_0_0.Battle.BattleDataFunction.ClearConvertedBarrage()
end

function var_0_5.GetBulletPath(arg_4_0)
	return "Item/" .. arg_4_0
end

function var_0_5.GetOrbitPath(arg_5_0)
	return "orbit/" .. arg_5_0
end

function var_0_5.GetCharacterPath(arg_6_0)
	return "Char/" .. arg_6_0
end

function var_0_5.GetCharacterGoPath(arg_7_0)
	return "chargo/" .. arg_7_0
end

function var_0_5.GetAircraftIconPath(arg_8_0)
	return "AircraftIcon/" .. arg_8_0
end

function var_0_5.GetFXPath(arg_9_0)
	return "Effect/" .. arg_9_0
end

function var_0_5.GetPaintingPath(arg_10_0)
	return "painting/" .. arg_10_0
end

function var_0_5.GetHrzIcon(arg_11_0)
	return "herohrzicon/" .. arg_11_0
end

function var_0_5.GetSquareIcon(arg_12_0)
	return "squareicon/" .. arg_12_0
end

function var_0_5.GetQIcon(arg_13_0)
	return "qicon/" .. arg_13_0
end

function var_0_5.GetCommanderHrzIconPath(arg_14_0)
	return "commanderhrz/" .. arg_14_0
end

function var_0_5.GetShipTypeIconPath(arg_15_0)
	return "shiptype/" .. arg_15_0
end

function var_0_5.GetMapPath(arg_16_0)
	return "Map/" .. arg_16_0
end

function var_0_5.GetUIPath(arg_17_0)
	return "UI/" .. arg_17_0
end

function var_0_5.GetResName(arg_18_0)
	local var_18_0 = arg_18_0
	local var_18_1 = string.find(var_18_0, "%/")

	while var_18_1 do
		var_18_0 = string.sub(var_18_0, var_18_1 + 1)
		var_18_1 = string.find(var_18_0, "%/")
	end

	return var_18_0
end

function var_0_5.ClearCharRes(arg_19_0, arg_19_1)
	local var_19_0 = var_0_5.GetResName(arg_19_0)
	local var_19_1 = arg_19_1:GetComponent("SkeletonRenderer").skeletonDataAsset

	if not PoolMgr.GetInstance():IsSpineSkelCached(var_19_0) then
		UIUtil.ClearSharedMaterial(arg_19_1)
	end

	var_0_4.Destroy(arg_19_1)
end

function var_0_5.ClearPaintingRes(arg_20_0, arg_20_1)
	local var_20_0 = var_0_5.GetResName(arg_20_0)

	PoolMgr.GetInstance():ReturnPainting(var_20_0, arg_20_1)
end

function var_0_5.DestroyOb(arg_21_0, arg_21_1)
	local var_21_0 = arg_21_0._ob2Pool[arg_21_1]

	if var_21_0 then
		var_21_0:Recycle(arg_21_1)
	else
		var_0_4.Destroy(arg_21_1)
	end
end

function var_0_5.popPool(arg_22_0, arg_22_1, arg_22_2)
	local var_22_0 = arg_22_1:GetObject()

	if not arg_22_2 then
		var_22_0.transform.parent = nil
	end

	arg_22_0._ob2Pool[var_22_0] = arg_22_1

	return var_22_0
end

function var_0_5.InstCharacter(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = arg_23_0.GetCharacterPath(arg_23_1)
	local var_23_1 = arg_23_0._allPool[var_23_0]

	if var_23_1 then
		local var_23_2 = arg_23_0:popPool(var_23_1)

		arg_23_2(var_23_2)
	elseif arg_23_0._resCacheList[var_23_0] ~= nil then
		arg_23_0:InitPool(var_23_0, arg_23_0._resCacheList[var_23_0])

		var_23_1 = arg_23_0._allPool[var_23_0]

		local var_23_3 = arg_23_0:popPool(var_23_1)

		arg_23_2(var_23_3)
	else
		arg_23_0:LoadSpineAsset(arg_23_1, function(arg_24_0)
			if not arg_23_0._poolRoot then
				var_0_5.ClearCharRes(var_23_0, arg_24_0)

				return
			end

			assert(arg_24_0, "角色资源加载失败：" .. arg_23_1)

			local var_24_0 = SpineAnim.AnimChar(arg_23_1, arg_24_0)

			var_24_0:SetActive(false)
			arg_23_0:InitPool(var_23_0, var_24_0)

			var_23_1 = arg_23_0._allPool[var_23_0]

			local var_24_1 = arg_23_0:popPool(var_23_1)

			arg_23_2(var_24_1)
		end)
	end
end

function var_0_5.LoadSpineAsset(arg_25_0, arg_25_1, arg_25_2)
	local var_25_0 = arg_25_0.GetCharacterPath(arg_25_1)

	if not PoolMgr.GetInstance():IsSpineSkelCached(arg_25_1) then
		ResourceMgr.Inst:getAssetAsync(var_25_0, arg_25_1 .. "_SkeletonData", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_26_0)
			arg_25_2(arg_26_0)
		end), true, true)
	else
		PoolMgr.GetInstance():GetSpineSkel(arg_25_1, true, arg_25_2)
	end
end

function var_0_5.InstAirCharacter(arg_27_0, arg_27_1, arg_27_2)
	local var_27_0 = arg_27_0.GetCharacterGoPath(arg_27_1)
	local var_27_1 = arg_27_0._allPool[var_27_0]

	if var_27_1 then
		local var_27_2 = arg_27_0:popPool(var_27_1)

		arg_27_2(var_27_2)
	elseif arg_27_0._resCacheList[var_27_0] ~= nil then
		arg_27_0:InitPool(var_27_0, arg_27_0._resCacheList[var_27_0])

		var_27_1 = arg_27_0._allPool[var_27_0]

		local var_27_3 = arg_27_0:popPool(var_27_1)

		arg_27_2(var_27_3)
	else
		ResourceMgr.Inst:getAssetAsync(var_27_0, arg_27_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_28_0)
			if not arg_27_0._poolRoot then
				var_0_4.Destroy(arg_28_0)

				return
			else
				assert(arg_28_0, "飞机资源加载失败：" .. arg_27_1)
				arg_27_0:InitPool(var_27_0, arg_28_0)

				var_27_1 = arg_27_0._allPool[var_27_0]

				local var_28_0 = arg_27_0:popPool(var_27_1)

				arg_27_2(var_28_0)
			end
		end), true, true)
	end
end

function var_0_5.InstBullet(arg_29_0, arg_29_1, arg_29_2)
	local var_29_0 = arg_29_0.GetBulletPath(arg_29_1)
	local var_29_1 = arg_29_0._allPool[var_29_0]

	if var_29_1 then
		local var_29_2 = arg_29_0:popPool(var_29_1, true)

		if string.find(arg_29_1, "_trail") then
			local var_29_3 = var_29_2:GetComponentInChildren(typeof(UnityEngine.TrailRenderer))

			if var_29_3 then
				var_29_3:Clear()
			end
		end

		arg_29_2(var_29_2)

		return true
	elseif arg_29_0._resCacheList[var_29_0] ~= nil then
		arg_29_0:InitPool(var_29_0, arg_29_0._resCacheList[var_29_0])

		var_29_1 = arg_29_0._allPool[var_29_0]

		local var_29_4 = arg_29_0:popPool(var_29_1, true)

		if string.find(arg_29_1, "_trail") then
			local var_29_5 = var_29_4:GetComponentInChildren(typeof(UnityEngine.TrailRenderer))

			if var_29_5 then
				var_29_5:Clear()
			end
		end

		arg_29_2(var_29_4)

		return true
	else
		ResourceMgr.Inst:getAssetAsync(var_29_0, arg_29_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_30_0)
			if arg_29_0._poolRoot then
				var_0_4.Destroy(arg_30_0)

				return
			else
				assert(arg_30_0, "子弹资源加载失败：" .. arg_29_1)
				arg_29_0:InitPool(var_29_0, arg_30_0)

				var_29_1 = arg_29_0._allPool[var_29_0]

				local var_30_0 = arg_29_0:popPool(var_29_1, true)

				arg_29_2(var_30_0)
			end
		end), true, true)

		return false
	end
end

function var_0_5.InstFX(arg_31_0, arg_31_1, arg_31_2)
	local var_31_0 = arg_31_0.GetFXPath(arg_31_1)
	local var_31_1
	local var_31_2 = arg_31_0._allPool[var_31_0]

	if var_31_2 then
		var_31_1 = arg_31_0:popPool(var_31_2, arg_31_2)
	elseif arg_31_0._resCacheList[var_31_0] ~= nil then
		arg_31_0:InitPool(var_31_0, arg_31_0._resCacheList[var_31_0])

		local var_31_3 = arg_31_0._allPool[var_31_0]

		var_31_1 = arg_31_0:popPool(var_31_3, arg_31_2)
	else
		ResourceMgr.Inst:getAssetAsync(var_31_0, arg_31_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_32_0)
			if not arg_31_0._poolRoot then
				var_0_4.Destroy(arg_32_0)

				return
			else
				assert(arg_32_0, "特效资源加载失败：" .. arg_31_1)
				arg_31_0:InitPool(var_31_0, arg_32_0)
			end
		end), true, true)

		var_31_1 = GameObject(arg_31_1 .. "临时假obj")

		var_31_1:SetActive(false)

		arg_31_0._resCacheList[var_31_0] = var_31_1
	end

	return var_31_1
end

function var_0_5.InstOrbit(arg_33_0, arg_33_1)
	local var_33_0 = arg_33_0.GetOrbitPath(arg_33_1)
	local var_33_1
	local var_33_2 = arg_33_0._allPool[var_33_0]

	if var_33_2 then
		var_33_1 = arg_33_0:popPool(var_33_2)
	elseif arg_33_0._resCacheList[var_33_0] ~= nil then
		arg_33_0:InitPool(var_33_0, arg_33_0._resCacheList[var_33_0])

		local var_33_3 = arg_33_0._allPool[var_33_0]

		var_33_1 = arg_33_0:popPool(var_33_3)
	else
		ResourceMgr.Inst:getAssetAsync(var_33_0, arg_33_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_34_0)
			if not arg_33_0._poolRoot then
				var_0_4.Destroy(arg_34_0)

				return
			else
				assert(arg_34_0, "特效资源加载失败：" .. arg_33_1)
				arg_33_0:InitPool(var_33_0, arg_34_0)
			end
		end), true, true)

		var_33_1 = GameObject(arg_33_1 .. "临时假obj")

		var_33_1:SetActive(false)

		arg_33_0._resCacheList[var_33_0] = var_33_1
	end

	return var_33_1
end

function var_0_5.InstSkillPaintingUI(arg_35_0)
	local var_35_0 = arg_35_0._allPool["UI/SkillPainting"]
	local var_35_1 = var_35_0:GetObject()

	arg_35_0._ob2Pool[var_35_1] = var_35_0

	return var_35_1
end

function var_0_5.InstBossWarningUI(arg_36_0)
	local var_36_0 = arg_36_0._allPool["UI/MonsterAppearUI"]
	local var_36_1 = var_36_0:GetObject()

	arg_36_0._ob2Pool[var_36_1] = var_36_0

	return var_36_1
end

function var_0_5.InstGridmanSkillUI(arg_37_0)
	local var_37_0 = arg_37_0._allPool["UI/combatgridmanskillfloat"]
	local var_37_1 = var_37_0:GetObject()

	arg_37_0._ob2Pool[var_37_1] = var_37_0

	return var_37_1
end

function var_0_5.InstPainting(arg_38_0, arg_38_1)
	local var_38_0 = arg_38_0.GetPaintingPath(arg_38_1)
	local var_38_1
	local var_38_2 = arg_38_0._allPool[var_38_0]

	if var_38_2 then
		var_38_1 = var_38_2:GetObject()
		arg_38_0._ob2Pool[var_38_1] = var_38_2
	elseif arg_38_0._resCacheList[var_38_0] ~= nil then
		var_38_1 = Object.Instantiate(arg_38_0._resCacheList[var_38_0])

		var_38_1:SetActive(true)
	end

	return var_38_1
end

function var_0_5.InstMap(arg_39_0, arg_39_1)
	local var_39_0 = arg_39_0.GetMapPath(arg_39_1)
	local var_39_1
	local var_39_2 = arg_39_0._allPool[var_39_0]

	if var_39_2 then
		var_39_1 = var_39_2:GetObject()
		arg_39_0._ob2Pool[var_39_1] = var_39_2
	elseif arg_39_0._resCacheList[var_39_0] ~= nil then
		var_39_1 = Object.Instantiate(arg_39_0._resCacheList[var_39_0])
	else
		assert(false, "地图资源没有预加载：" .. arg_39_1)
	end

	var_39_1:SetActive(true)

	return var_39_1
end

function var_0_5.InstCardPuzzleCard(arg_40_0)
	local var_40_0 = arg_40_0._allPool["UI/CardTowerCardCombat"]
	local var_40_1 = var_40_0:GetObject()

	arg_40_0._ob2Pool[var_40_1] = var_40_0

	return var_40_1
end

function var_0_5.GetCharacterIcon(arg_41_0, arg_41_1)
	return arg_41_0._resCacheList[var_0_5.GetHrzIcon(arg_41_1)]
end

function var_0_5.GetCharacterSquareIcon(arg_42_0, arg_42_1)
	return arg_42_0._resCacheList[var_0_5.GetSquareIcon(arg_42_1)]
end

function var_0_5.GetCharacterQIcon(arg_43_0, arg_43_1)
	return arg_43_0._resCacheList[var_0_5.GetQIcon(arg_43_1)]
end

function var_0_5.GetAircraftIcon(arg_44_0, arg_44_1)
	return arg_44_0._resCacheList[var_0_5.GetAircraftIconPath(arg_44_1)]
end

function var_0_5.GetShipTypeIcon(arg_45_0, arg_45_1)
	return arg_45_0._resCacheList[var_0_5.GetShipTypeIconPath(arg_45_1)]
end

function var_0_5.GetCommanderHrzIcon(arg_46_0, arg_46_1)
	return arg_46_0._resCacheList[var_0_5.GetCommanderHrzIconPath(arg_46_1)]
end

function var_0_5.GetShader(arg_47_0, arg_47_1)
	return (pg.ShaderMgr.GetInstance():GetShader(var_0_3.BATTLE_SHADER[arg_47_1]))
end

function var_0_5.AddPreloadResource(arg_48_0, arg_48_1)
	if type(arg_48_1) == "string" then
		arg_48_0._preloadList[arg_48_1] = false
	elseif type(arg_48_1) == "table" then
		for iter_48_0, iter_48_1 in ipairs(arg_48_1) do
			arg_48_0._preloadList[iter_48_1] = false
		end
	end
end

function var_0_5.AddPreloadCV(arg_49_0, arg_49_1)
	local var_49_0 = Ship.getCVKeyID(arg_49_1)

	if var_49_0 > 0 then
		arg_49_0._battleCVList[var_49_0] = pg.CriMgr.GetBattleCVBankName(var_49_0)
	end
end

function var_0_5.StartPreload(arg_50_0, arg_50_1, arg_50_2)
	local var_50_0 = 0
	local var_50_1 = 0

	for iter_50_0, iter_50_1 in pairs(arg_50_0._preloadList) do
		var_50_1 = var_50_1 + 1
	end

	for iter_50_2, iter_50_3 in pairs(arg_50_0._battleCVList) do
		var_50_1 = var_50_1 + 1
	end

	local function var_50_2()
		if not arg_50_0._poolRoot then
			return
		end

		var_50_0 = var_50_0 + 1

		if var_50_0 > var_50_1 then
			return
		end

		if arg_50_2 then
			arg_50_2(var_50_0)
		end

		if var_50_0 == var_50_1 then
			arg_50_0._preloadList = nil

			arg_50_1()
		end
	end

	for iter_50_4, iter_50_5 in pairs(arg_50_0._battleCVList) do
		pg.CriMgr.GetInstance():LoadBattleCV(iter_50_4, var_50_2)
	end

	for iter_50_6, iter_50_7 in pairs(arg_50_0._preloadList) do
		local var_50_3 = arg_50_0.GetResName(iter_50_6)

		if var_50_3 == "" or arg_50_0._resCacheList[iter_50_6] ~= nil then
			var_50_2()
		elseif string.find(iter_50_6, "herohrzicon/") or string.find(iter_50_6, "qicon/") or string.find(iter_50_6, "squareicon/") or string.find(iter_50_6, "commanderhrz/") or string.find(iter_50_6, "AircraftIcon/") then
			local var_50_4, var_50_5 = HXSet.autoHxShiftPath(iter_50_6, var_50_3)

			ResourceMgr.Inst:getAssetAsync(var_50_4, "", typeof(Sprite), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_52_0)
				if arg_52_0 == nil then
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot then
						var_0_4.Destroy(arg_52_0)

						return
					end

					if arg_50_0._resCacheList then
						arg_50_0._resCacheList[iter_50_6] = arg_52_0
					end
				end

				var_50_2()
			end), true, true)
		elseif string.find(iter_50_6, "shiptype/") then
			local var_50_6 = string.split(iter_50_6, "/")[2]

			ResourceMgr.Inst:getAssetAsync("shiptype", var_50_6, typeof(Sprite), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_53_0)
				if arg_53_0 == nil then
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot then
						var_0_4.Destroy(arg_53_0)

						return
					end

					if arg_50_0._resCacheList then
						arg_50_0._resCacheList[iter_50_6] = arg_53_0
					end
				end

				var_50_2()
			end), true, true)
		elseif string.find(iter_50_6, "painting/") then
			local var_50_7 = false

			if PlayerPrefs.GetInt(BATTLE_HIDE_BG, 1) > 0 then
				var_50_7 = checkABExist("painting/" .. var_50_3 .. "_n")
			else
				var_50_7 = PlayerPrefs.GetInt("paint_hide_other_obj_" .. var_50_3, 0) ~= 0
			end

			PoolMgr.GetInstance():GetPainting(var_50_3 .. (var_50_7 and "_n" or ""), true, function(arg_54_0)
				if arg_54_0 == nil then
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot then
						var_0_5.ClearPaintingRes(iter_50_6, arg_54_0)

						return
					end

					ShipExpressionHelper.SetExpression(arg_54_0, var_50_3)
					arg_54_0:SetActive(false)

					if arg_50_0._resCacheList then
						arg_50_0._resCacheList[iter_50_6] = arg_54_0
					end
				end

				var_50_2()
			end)
		elseif string.find(iter_50_6, "Char/") then
			arg_50_0:LoadSpineAsset(var_50_3, function(arg_55_0)
				if arg_55_0 == nil then
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					arg_55_0 = SpineAnim.AnimChar(var_50_3, arg_55_0)

					if not arg_50_0._poolRoot then
						var_0_5.ClearCharRes(iter_50_6, arg_55_0)

						return
					end

					arg_55_0:SetActive(false)

					if arg_50_0._resCacheList then
						arg_50_0._resCacheList[iter_50_6] = arg_55_0
					end
				end

				arg_50_0:InitPool(iter_50_6, arg_55_0)
				var_50_2()
			end)
		elseif string.find(iter_50_6, "UI/") then
			LoadAndInstantiateAsync("UI", var_50_3, function(arg_56_0)
				if arg_56_0 == nil then
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot then
						var_0_4.Destroy(arg_56_0)

						return
					end

					arg_56_0:SetActive(false)

					if arg_50_0._resCacheList then
						arg_50_0._resCacheList[iter_50_6] = arg_56_0
					end
				end

				arg_50_0:InitPool(iter_50_6, arg_56_0)
				var_50_2()
			end, true, true)
		else
			ResourceMgr.Inst:getAssetAsync(iter_50_6, var_50_3, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_57_0)
				if arg_57_0 == nil then
					originalPrint("资源预加载失败，检查以下目录：>>" .. iter_50_6 .. "<<")
				else
					if not arg_50_0._poolRoot then
						var_0_4.Destroy(arg_57_0)

						return
					end

					if arg_50_0._resCacheList then
						arg_50_0._resCacheList[iter_50_6] = arg_57_0
					end
				end

				arg_50_0:InitPool(iter_50_6, arg_57_0)
				var_50_2()
			end), true, true)
		end
	end

	return var_50_1
end

local var_0_6 = Vector3(0, 10000, 0)

function var_0_5.HideBullet(arg_58_0)
	arg_58_0.transform.position = var_0_6
end

function var_0_5.InitParticleSystemCB(arg_59_0)
	pg.EffectMgr.GetInstance():CommonEffectEvent(arg_59_0)
end

function var_0_5.InitPool(arg_60_0, arg_60_1, arg_60_2)
	local var_60_0 = arg_60_0._poolRoot.transform

	if string.find(arg_60_1, "Item/") then
		if arg_60_2:GetComponentInChildren(typeof(UnityEngine.TrailRenderer)) ~= nil or arg_60_2:GetComponentInChildren(typeof(ParticleSystem)) ~= nil then
			arg_60_0._allPool[arg_60_1] = pg.Pool.New(arg_60_0._bulletContainer.transform, arg_60_2, 15, 20, true, false):InitSize()
		else
			local var_60_1 = pg.Pool.New(arg_60_0._bulletContainer.transform, arg_60_2, 20, 20, true, true)

			var_60_1:SetRecycleFuncs(var_0_5.HideBullet)
			var_60_1:InitSize()

			arg_60_0._allPool[arg_60_1] = var_60_1
		end
	elseif string.find(arg_60_1, "Effect/") then
		if arg_60_2:GetComponent(typeof(UnityEngine.ParticleSystem)) then
			local var_60_2 = 5

			if string.find(arg_60_1, "smoke") and not string.find(arg_60_1, "smokeboom") then
				var_60_2 = 30
			elseif string.find(arg_60_1, "feijiyingzi") then
				var_60_2 = 1
			end

			local var_60_3 = pg.Pool.New(var_60_0, arg_60_2, var_60_2, 20, false, false)

			var_60_3:SetInitFuncs(var_0_5.InitParticleSystemCB)
			var_60_3:InitSize()

			arg_60_0._allPool[arg_60_1] = var_60_3
		else
			local var_60_4 = 8

			if string.find(arg_60_1, "AntiAirArea") or string.find(arg_60_1, "AntiSubArea") then
				var_60_4 = 1
			end

			GetOrAddComponent(arg_60_2, typeof(ParticleSystemEvent))

			local var_60_5 = pg.Pool.New(var_60_0, arg_60_2, var_60_4, 20, false, false)

			var_60_5:InitSize()

			arg_60_0._allPool[arg_60_1] = var_60_5
		end
	elseif string.find(arg_60_1, "Char/") then
		local var_60_6 = 1

		if string.find(arg_60_1, "danchuan") then
			var_60_6 = 3
		end

		local var_60_7 = pg.Pool.New(var_60_0, arg_60_2, var_60_6, 20, false, false):InitSize()

		var_60_7:SetRecycleFuncs(var_0_5.ResetSpineAction)

		arg_60_0._allPool[arg_60_1] = var_60_7
	elseif string.find(arg_60_1, "chargo/") then
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 3, 20, false, false):InitSize()
	elseif string.find(arg_60_1, "orbit/") then
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 2, 20, false, false):InitSize()
	elseif arg_60_1 == "UI/SkillPainting" then
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 1, 20, false, false):InitSize()
	elseif arg_60_1 == "UI/MonsterAppearUI" then
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 1, 20, false, false):InitSize()
	elseif arg_60_1 == "UI/CardTowerCardCombat" then
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 7, 20, false, false):InitSize()
	elseif arg_60_1 == "UI/combatgridmanskillfloat" then
		arg_60_0._allPool[arg_60_1] = pg.Pool.New(var_60_0, arg_60_2, 1, 20, false, false):InitSize()
	elseif arg_60_1 == "UI/CombatHPBar" then
		var_0_0.Battle.BattleHPBarManager.GetInstance():Init(arg_60_2, var_60_0)
	elseif arg_60_1 == "UI/CombatHPPop" then
		var_0_0.Battle.BattlePopNumManager.GetInstance():Init(arg_60_2, var_60_0)
	end
end

function var_0_5.GetRotateScript(arg_61_0, arg_61_1, arg_61_2)
	local var_61_0 = arg_61_0.rotateScriptMap

	if var_61_0[arg_61_1] then
		return var_61_0[arg_61_1]
	end

	local var_61_1 = GetOrAddComponent(arg_61_1, "BulletRotation")

	var_61_0[arg_61_1] = var_61_1

	return var_61_1
end

function var_0_5.GetCommonResource()
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
end

function var_0_5.GetDisplayCommonResource()
	return {
		var_0_5.GetFXPath(var_0_0.Battle.BattleCharacterFactory.MOVE_WAVE_FX_NAME),
		var_0_5.GetFXPath(var_0_0.Battle.BattleCharacterFactory.BOMB_FX_NAME),
		var_0_5.GetFXPath(var_0_0.Battle.BattleCharacterFactory.DANCHUAN_MOVE_WAVE_FX_NAME)
	}
end

function var_0_5.GetMapResource(arg_64_0)
	local var_64_0 = {}
	local var_64_1 = var_0_0.Battle.BattleMap

	for iter_64_0, iter_64_1 in ipairs(var_64_1.LAYERS) do
		local var_64_2 = var_64_1.GetMapResNames(arg_64_0, iter_64_1)

		for iter_64_2, iter_64_3 in ipairs(var_64_2) do
			var_64_0[#var_64_0 + 1] = var_0_5.GetMapPath(iter_64_3)
		end
	end

	return var_64_0
end

function var_0_5.GetBuffResource()
	local var_65_0 = {}
	local var_65_1 = require("buffFXPreloadList")

	for iter_65_0, iter_65_1 in ipairs(var_65_1) do
		var_65_0[#var_65_0 + 1] = var_0_5.GetFXPath(iter_65_1)
	end

	return var_65_0
end

function var_0_5.GetShipResource(arg_66_0, arg_66_1, arg_66_2)
	local var_66_0 = {}
	local var_66_1 = var_0_1.GetPlayerShipTmpDataFromID(arg_66_0)

	if arg_66_1 == nil or arg_66_1 == 0 then
		arg_66_1 = var_66_1.skin_id
	end

	local var_66_2 = var_0_1.GetPlayerShipSkinDataFromID(arg_66_1)

	var_66_0[#var_66_0 + 1] = var_0_5.GetCharacterPath(var_66_2.prefab)
	var_66_0[#var_66_0 + 1] = var_0_5.GetHrzIcon(var_66_2.painting)
	var_66_0[#var_66_0 + 1] = var_0_5.GetQIcon(var_66_2.painting)
	var_66_0[#var_66_0 + 1] = var_0_5.GetSquareIcon(var_66_2.painting)

	if arg_66_2 and var_0_1.GetShipTypeTmp(var_66_1.type).team_type == TeamType.Main then
		var_66_0[#var_66_0 + 1] = var_0_5.GetPaintingPath(var_66_2.painting)
	end

	return var_66_0
end

function var_0_5.GetEnemyResource(arg_67_0)
	local var_67_0 = {}
	local var_67_1 = arg_67_0.monsterTemplateID
	local var_67_2 = arg_67_0.bossData ~= nil
	local var_67_3 = arg_67_0.buffList or {}
	local var_67_4 = arg_67_0.phase or {}
	local var_67_5 = var_0_1.GetMonsterTmpDataFromID(var_67_1)

	var_67_0[#var_67_0 + 1] = var_0_5.GetCharacterPath(var_67_5.prefab)
	var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(var_67_5.wave_fx)

	if var_67_5.fog_fx then
		var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(var_67_5.fog_fx)
	end

	for iter_67_0, iter_67_1 in ipairs(var_67_5.appear_fx) do
		var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(iter_67_1)
	end

	for iter_67_2, iter_67_3 in ipairs(var_67_5.smoke) do
		local var_67_6 = iter_67_3[2]

		for iter_67_4, iter_67_5 in ipairs(var_67_6) do
			var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(iter_67_5[1])
		end
	end

	if arg_67_0.deadFX then
		var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(arg_67_0.deadFX)
	end

	if type(var_67_5.bubble_fx) == "table" then
		var_67_0[#var_67_0 + 1] = var_0_5.GetFXPath(var_67_5.bubble_fx[1])
	end

	local function var_67_7(arg_68_0)
		local var_68_0 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(arg_68_0, 1)

		for iter_68_0, iter_68_1 in pairs(var_68_0.effect_list) do
			local var_68_1 = iter_68_1.arg_list.skill_id

			if var_68_1 then
				local var_68_2 = var_0_0.Battle.BattleDataFunction.GetSkillTemplate(var_68_1).painting

				if var_68_2 == 1 then
					var_67_0[#var_67_0 + 1] = var_0_5.GetHrzIcon(var_67_5.icon)
				elseif type(var_68_2) == "string" then
					var_67_0[#var_67_0 + 1] = var_0_5.GetHrzIcon(var_68_2)
				end
			end

			local var_68_3 = iter_68_1.arg_list.buff_id

			if var_68_3 then
				var_67_7(var_68_3)
			end
		end
	end

	for iter_67_6, iter_67_7 in ipairs(var_67_3) do
		var_67_7(iter_67_7)
	end

	for iter_67_8, iter_67_9 in ipairs(var_67_4) do
		if iter_67_9.addBuff then
			for iter_67_10, iter_67_11 in ipairs(iter_67_9.addBuff) do
				var_67_7(iter_67_11)
			end
		end
	end

	if var_67_2 then
		var_67_0[#var_67_0 + 1] = var_0_5.GetSquareIcon(var_67_5.icon)
	end

	return var_67_0
end

function var_0_5.GetWeaponResource(arg_69_0, arg_69_1)
	local var_69_0 = {}

	if arg_69_0 == -1 then
		return var_69_0
	end

	local var_69_1 = var_0_1.GetWeaponPropertyDataFromID(arg_69_0)

	if var_69_1.type == var_0_2.EquipmentType.MAIN_CANNON or var_69_1.type == var_0_2.EquipmentType.SUB_CANNON or var_69_1.type == var_0_2.EquipmentType.TORPEDO or var_69_1.type == var_0_2.EquipmentType.ANTI_AIR or var_69_1.type == var_0_2.EquipmentType.ANTI_SEA or var_69_1.type == var_0_2.EquipmentType.POINT_HIT_AND_LOCK or var_69_1.type == var_0_2.EquipmentType.MANUAL_METEOR or var_69_1.type == var_0_2.EquipmentType.BOMBER_PRE_CAST_ALERT or var_69_1.type == var_0_2.EquipmentType.DEPTH_CHARGE or var_69_1.type == var_0_2.EquipmentType.MANUAL_TORPEDO or var_69_1.type == var_0_2.EquipmentType.DISPOSABLE_TORPEDO or var_69_1.type == var_0_2.EquipmentType.MANUAL_AAMISSILE or var_69_1.type == var_0_2.EquipmentType.BEAM or var_69_1.type == var_0_2.EquipmentType.SPACE_LASER or var_69_1.type == var_0_2.EquipmentType.FLEET_RANGE_ANTI_AIR or var_69_1.type == var_0_2.EquipmentType.MANUAL_MISSILE or var_69_1.type == var_0_2.EquipmentType.AUTO_MISSILE or var_69_1.type == var_0_2.EquipmentType.MISSILE then
		for iter_69_0, iter_69_1 in ipairs(var_69_1.bullet_ID) do
			local var_69_2 = var_0_5.GetBulletResource(iter_69_1, arg_69_1)

			for iter_69_2, iter_69_3 in ipairs(var_69_2) do
				var_69_0[#var_69_0 + 1] = iter_69_3
			end
		end
	elseif var_69_1.type == var_0_2.EquipmentType.INTERCEPT_AIRCRAFT or var_69_1.type == var_0_2.EquipmentType.STRIKE_AIRCRAFT then
		var_69_0 = var_0_5.GetAircraftResource(arg_69_0, nil, arg_69_1)
	elseif var_69_1.type == var_0_2.EquipmentType.PREVIEW_ARICRAFT then
		for iter_69_4, iter_69_5 in ipairs(var_69_1.bullet_ID) do
			var_69_0 = var_0_5.GetAircraftResource(iter_69_5, nil, arg_69_1)
		end
	end

	if var_69_1.type == var_0_2.EquipmentType.FLEET_RANGE_ANTI_AIR then
		local var_69_3 = var_0_5.GetBulletResource(var_0_3.AntiAirConfig.RangeBulletID)

		for iter_69_6, iter_69_7 in ipairs(var_69_3) do
			var_69_0[#var_69_0 + 1] = iter_69_7
		end
	end

	local var_69_4

	if arg_69_1 and arg_69_1 ~= 0 then
		var_69_4 = var_0_0.Battle.BattleDataFunction.GetEquipSkinDataFromID(arg_69_1)
	end

	if var_69_4 and var_69_4.fire_fx_name ~= "" then
		var_69_0[#var_69_0 + 1] = var_0_5.GetFXPath(var_69_4.fire_fx_name)
	else
		var_69_0[#var_69_0 + 1] = var_0_5.GetFXPath(var_69_1.fire_fx)
	end

	if var_69_1.precast_param.fx then
		var_69_0[#var_69_0 + 1] = var_0_5.GetFXPath(var_69_1.precast_param.fx)
	end

	if var_69_4 then
		local var_69_5 = var_69_4.orbit_combat

		if var_69_5 ~= "" then
			var_69_0[#var_69_0 + 1] = var_0_5.GetOrbitPath(var_69_5)
		end
	end

	return var_69_0
end

function var_0_5.GetEquipResource(arg_70_0, arg_70_1, arg_70_2)
	local var_70_0 = {}

	if arg_70_1 ~= 0 then
		local var_70_1 = var_0_0.Battle.BattleDataFunction.GetEquipSkinDataFromID(arg_70_1)
		local var_70_2 = var_70_1.ship_skin_id

		if var_70_2 ~= 0 then
			local var_70_3 = var_0_0.Battle.BattleDataFunction.GetPlayerShipSkinDataFromID(var_70_2)

			var_70_0[#var_70_0 + 1] = var_0_5.GetCharacterPath(var_70_3.prefab)
		end

		local var_70_4 = var_70_1.orbit_combat

		if var_70_4 ~= "" then
			var_70_0[#var_70_0 + 1] = var_0_5.GetOrbitPath(var_70_4)
		end
	end

	local var_70_5 = var_0_0.Battle.BattleDataFunction.GetWeaponDataFromID(arg_70_0)
	local var_70_6 = var_70_5.weapon_id

	for iter_70_0, iter_70_1 in ipairs(var_70_6) do
		local var_70_7 = var_0_5.GetWeaponResource(iter_70_1)

		for iter_70_2, iter_70_3 in ipairs(var_70_7) do
			var_70_0[#var_70_0 + 1] = iter_70_3
		end
	end

	local var_70_8 = var_70_5.skill_id

	for iter_70_4, iter_70_5 in ipairs(var_70_8) do
		iter_70_5 = arg_70_2 and var_0_0.Battle.BattleDataFunction.SkillTranform(arg_70_2, iter_70_5) or iter_70_5

		local var_70_9 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_70_5, 1, {})

		for iter_70_6, iter_70_7 in ipairs(var_70_9) do
			var_70_0[#var_70_0 + 1] = iter_70_7
		end
	end

	return var_70_0
end

function var_0_5.GetBulletResource(arg_71_0, arg_71_1)
	local var_71_0 = {}
	local var_71_1

	if arg_71_1 ~= nil and arg_71_1 ~= 0 then
		var_71_1 = var_0_1.GetEquipSkinDataFromID(arg_71_1)
	end

	local var_71_2 = var_0_1.GetBulletTmpDataFromID(arg_71_0)
	local var_71_3

	if var_71_1 then
		var_71_3 = var_71_1.bullet_name

		if var_71_1.mirror == 1 then
			var_71_0[#var_71_0 + 1] = var_0_5.GetBulletPath(var_71_3 .. var_0_0.Battle.BattleBulletUnit.MIRROR_RES)
		end
	else
		var_71_3 = var_71_2.modle_ID
	end

	if var_71_2.type == var_0_2.BulletType.BEAM or var_71_2.type == var_0_2.BulletType.SPACE_LASER or var_71_2.type == var_0_2.BulletType.MISSILE or var_71_2.type == var_0_2.BulletType.ELECTRIC_ARC then
		var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_2.modle_ID)
	else
		var_71_0[#var_71_0 + 1] = var_0_5.GetBulletPath(var_71_3)
	end

	if var_71_2.extra_param.mirror then
		var_71_0[#var_71_0 + 1] = var_0_5.GetBulletPath(var_71_3 .. var_0_0.Battle.BattleBulletUnit.MIRROR_RES)
	end

	local var_71_4

	if var_71_1 and var_71_1.hit_fx_name ~= "" then
		var_71_4 = var_71_1.hit_fx_name
	else
		var_71_4 = var_71_2.hit_fx
	end

	var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_4)
	var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_2.miss_fx)
	var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_2.alert_fx)

	if var_71_2.extra_param.area_FX then
		var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(var_71_2.extra_param.area_FX)
	end

	if var_71_2.extra_param.shrapnel then
		for iter_71_0, iter_71_1 in ipairs(var_71_2.extra_param.shrapnel) do
			local var_71_5 = var_0_5.GetBulletResource(iter_71_1.bullet_ID)

			for iter_71_2, iter_71_3 in ipairs(var_71_5) do
				var_71_0[#var_71_0 + 1] = iter_71_3
			end
		end
	end

	for iter_71_4, iter_71_5 in ipairs(var_71_2.attach_buff) do
		if iter_71_5.effect_id then
			var_71_0[#var_71_0 + 1] = var_0_5.GetFXPath(iter_71_5.effect_id)
		end

		if iter_71_5.buff_id then
			local var_71_6 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_71_5.buff_id, 1, {})

			for iter_71_6, iter_71_7 in ipairs(var_71_6) do
				var_71_0[#var_71_0 + 1] = iter_71_7
			end
		end
	end

	return var_71_0
end

function var_0_5.GetAircraftResource(arg_72_0, arg_72_1, arg_72_2)
	local var_72_0 = {}

	arg_72_2 = arg_72_2 or 0

	local var_72_1 = var_0_1.GetAircraftTmpDataFromID(arg_72_0)
	local var_72_2
	local var_72_3
	local var_72_4
	local var_72_5

	if arg_72_2 ~= 0 then
		local var_72_6, var_72_7, var_72_8

		var_72_2, var_72_6, var_72_7, var_72_8 = var_0_1.GetEquipSkin(arg_72_2)

		if var_72_6 ~= "" then
			var_72_0[#var_72_0 + 1] = var_0_5.GetBulletPath(var_72_6)
		end

		if var_72_7 ~= "" then
			var_72_0[#var_72_0 + 1] = var_0_5.GetBulletPath(var_72_7)
		end

		if var_72_8 ~= "" then
			var_72_0[#var_72_0 + 1] = var_0_5.GetBulletPath(var_72_8)
		end
	else
		var_72_2 = var_72_1.model_ID
	end

	var_72_0[#var_72_0 + 1] = var_0_5.GetCharacterGoPath(var_72_2)
	var_72_0[#var_72_0 + 1] = var_0_5.GetAircraftIconPath(var_72_1.model_ID)

	local var_72_9 = arg_72_1 or var_72_1.weapon_ID

	if type(var_72_9) == "table" then
		for iter_72_0, iter_72_1 in ipairs(var_72_9) do
			local var_72_10 = var_0_5.GetWeaponResource(iter_72_1)

			for iter_72_2, iter_72_3 in ipairs(var_72_10) do
				var_72_0[#var_72_0 + 1] = iter_72_3
			end
		end
	else
		local var_72_11 = var_0_5.GetWeaponResource(var_72_9)

		for iter_72_4, iter_72_5 in ipairs(var_72_11) do
			var_72_0[#var_72_0 + 1] = iter_72_5
		end
	end

	return var_72_0
end

function var_0_5.GetCommanderResource(arg_73_0)
	local var_73_0 = {}
	local var_73_1 = arg_73_0[1]

	var_73_0[#var_73_0 + 1] = var_0_5.GetCommanderHrzIconPath(var_73_1:getPainting())

	local var_73_2 = var_73_1:getSkills()[1]:getLevel()

	for iter_73_0, iter_73_1 in ipairs(arg_73_0[2]) do
		local var_73_3 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_73_1, var_73_2, {})

		for iter_73_2, iter_73_3 in ipairs(var_73_3) do
			var_73_0[#var_73_0 + 1] = iter_73_3
		end
	end

	return var_73_0
end

function var_0_5.GetStageResource(arg_74_0)
	local var_74_0 = var_0_0.Battle.BattleDataFunction.GetDungeonTmpDataByID(arg_74_0)
	local var_74_1 = {}
	local var_74_2 = {}

	for iter_74_0, iter_74_1 in ipairs(var_74_0.stages) do
		for iter_74_2, iter_74_3 in ipairs(iter_74_1.waves) do
			if iter_74_3.triggerType == var_0_0.Battle.BattleConst.WaveTriggerType.NORMAL then
				for iter_74_4, iter_74_5 in ipairs(iter_74_3.spawn) do
					local var_74_3 = var_0_5.GetMonsterRes(iter_74_5)

					for iter_74_6, iter_74_7 in ipairs(var_74_3) do
						table.insert(var_74_1, iter_74_7)
					end
				end

				if iter_74_3.reinforcement then
					for iter_74_8, iter_74_9 in ipairs(iter_74_3.reinforcement) do
						local var_74_4 = var_0_5.GetMonsterRes(iter_74_9)

						for iter_74_10, iter_74_11 in ipairs(var_74_4) do
							table.insert(var_74_1, iter_74_11)
						end
					end
				end
			elseif iter_74_3.triggerType == var_0_0.Battle.BattleConst.WaveTriggerType.AID then
				local var_74_5 = iter_74_3.triggerParams.vanguard_unitList
				local var_74_6 = iter_74_3.triggerParams.main_unitList
				local var_74_7 = iter_74_3.triggerParams.sub_unitList

				local function var_74_8(arg_75_0)
					local var_75_0 = var_0_5.GetAidUnitsRes(arg_75_0)

					for iter_75_0, iter_75_1 in ipairs(var_75_0) do
						table.insert(var_74_1, iter_75_1)
					end

					for iter_75_2, iter_75_3 in ipairs(arg_75_0) do
						var_74_2[#var_74_2 + 1] = iter_75_3.skinId
					end
				end

				if var_74_5 then
					var_74_8(var_74_5)
				end

				if var_74_6 then
					var_74_8(var_74_6)
				end

				if var_74_7 then
					var_74_8(var_74_7)
				end
			elseif iter_74_3.triggerType == var_0_0.Battle.BattleConst.WaveTriggerType.ENVIRONMENT then
				for iter_74_12, iter_74_13 in ipairs(iter_74_3.spawn) do
					var_0_5.GetEnvironmentRes(var_74_1, iter_74_13)
				end
			elseif iter_74_3.triggerType == var_0_0.Battle.BattleConst.WaveTriggerType.CARD_PUZZLE then
				local var_74_9 = var_0_0.Battle.BattleDataFunction.GetCardRes(iter_74_3.triggerParams.card_id)

				for iter_74_14, iter_74_15 in ipairs(var_74_9) do
					table.insert(var_74_1, iter_74_15)
				end
			end

			if iter_74_3.airFighter ~= nil then
				for iter_74_16, iter_74_17 in pairs(iter_74_3.airFighter) do
					local var_74_10 = var_0_5.GetAircraftResource(iter_74_17.templateID, iter_74_17.weaponID)

					for iter_74_18, iter_74_19 in ipairs(var_74_10) do
						var_74_1[#var_74_1 + 1] = iter_74_19
					end
				end
			end
		end
	end

	return var_74_1, var_74_2
end

function var_0_5.GetEnvironmentRes(arg_76_0, arg_76_1)
	table.insert(arg_76_0, arg_76_1.prefab and var_0_5.GetFXPath(arg_76_1.prefab))

	local var_76_0 = arg_76_1.behaviours
	local var_76_1 = var_0_0.Battle.BattleDataFunction.GetEnvironmentBehaviour(var_76_0).behaviour_list

	for iter_76_0, iter_76_1 in ipairs(var_76_1) do
		local var_76_2 = iter_76_1.type

		if var_76_2 == var_0_0.Battle.BattleConst.EnviroumentBehaviour.BUFF then
			local var_76_3 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_76_1.buff_id, 1, {})

			for iter_76_2, iter_76_3 in ipairs(var_76_3) do
				arg_76_0[#arg_76_0 + 1] = iter_76_3
			end
		elseif var_76_2 == var_0_0.Battle.BattleConst.EnviroumentBehaviour.SPAWN then
			local var_76_4 = iter_76_1.content and iter_76_1.content.alert and iter_76_1.content.alert.alert_fx

			table.insert(arg_76_0, var_76_4 and var_0_5.GetFXPath(var_76_4))

			local var_76_5 = iter_76_1.content and iter_76_1.content.child_prefab

			if var_76_5 then
				var_0_5.GetEnvironmentRes(arg_76_0, var_76_5)
			end
		elseif var_76_2 == var_0_0.Battle.BattleConst.EnviroumentBehaviour.PLAY_FX then
			arg_76_0[#arg_76_0 + 1] = var_0_5.GetFXPath(iter_76_1.FX_ID)
		end
	end
end

function var_0_5.GetMonsterRes(arg_77_0)
	local var_77_0 = {}
	local var_77_1 = var_0_5.GetEnemyResource(arg_77_0)

	for iter_77_0, iter_77_1 in ipairs(var_77_1) do
		var_77_0[#var_77_0 + 1] = iter_77_1
	end

	local var_77_2 = var_0_0.Battle.BattleDataFunction.GetMonsterTmpDataFromID(arg_77_0.monsterTemplateID)
	local var_77_3 = Clone(var_77_2.equipment_list)
	local var_77_4 = var_77_2.buff_list
	local var_77_5 = Clone(arg_77_0.buffList) or {}

	if arg_77_0.phase then
		for iter_77_2, iter_77_3 in ipairs(arg_77_0.phase) do
			if iter_77_3.addWeapon then
				for iter_77_4, iter_77_5 in ipairs(iter_77_3.addWeapon) do
					var_77_3[#var_77_3 + 1] = iter_77_5
				end
			end

			if iter_77_3.addRandomWeapon then
				for iter_77_6, iter_77_7 in ipairs(iter_77_3.addRandomWeapon) do
					for iter_77_8, iter_77_9 in ipairs(iter_77_7) do
						var_77_3[#var_77_3 + 1] = iter_77_9
					end
				end
			end

			if iter_77_3.addBuff then
				for iter_77_10, iter_77_11 in ipairs(iter_77_3.addBuff) do
					var_77_5[#var_77_5 + 1] = iter_77_11
				end
			end
		end
	end

	for iter_77_12, iter_77_13 in ipairs(var_77_4) do
		local var_77_6 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_77_13.ID, iter_77_13.LV, {})

		for iter_77_14, iter_77_15 in ipairs(var_77_6) do
			var_77_0[#var_77_0 + 1] = iter_77_15
		end
	end

	for iter_77_16, iter_77_17 in ipairs(var_77_5) do
		local var_77_7 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(iter_77_17, 1, {})

		for iter_77_18, iter_77_19 in ipairs(var_77_7) do
			var_77_0[#var_77_0 + 1] = iter_77_19
		end

		local var_77_8 = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(iter_77_17, 1)

		for iter_77_20, iter_77_21 in pairs(var_77_8.effect_list) do
			local var_77_9 = iter_77_21.arg_list.skill_id

			if var_77_9 and var_0_0.Battle.BattleDataFunction.NeedSkillPainting(var_77_9) then
				var_77_0[#var_77_0 + 1] = var_0_5.GetPaintingPath(var_0_1.GetMonsterTmpDataFromID(arg_77_0.monsterTemplateID).icon)

				break
			end
		end
	end

	for iter_77_22, iter_77_23 in ipairs(var_77_3) do
		local var_77_10 = var_0_5.GetWeaponResource(iter_77_23)

		for iter_77_24, iter_77_25 in ipairs(var_77_10) do
			var_77_0[#var_77_0 + 1] = iter_77_25
		end
	end

	return var_77_0
end

function var_0_5.GetEquipSkinPreviewRes(arg_78_0)
	local var_78_0 = {}
	local var_78_1 = var_0_1.GetEquipSkinDataFromID(arg_78_0)

	for iter_78_0, iter_78_1 in ipairs(var_78_1.weapon_ids) do
		local var_78_2 = var_0_5.GetWeaponResource(iter_78_1)

		for iter_78_2, iter_78_3 in ipairs(var_78_2) do
			var_78_0[#var_78_0 + 1] = iter_78_3
		end
	end

	local function var_78_3(arg_79_0)
		if arg_79_0 ~= "" then
			var_78_0[#var_78_0 + 1] = var_0_5.GetBulletPath(arg_79_0)
		end
	end

	local var_78_4, var_78_5, var_78_6, var_78_7, var_78_8, var_78_9 = var_0_1.GetEquipSkin(arg_78_0)

	if _.any(EquipType.AirProtoEquipTypes, function(arg_80_0)
		return table.contains(var_78_1.equip_type, arg_80_0)
	end) then
		var_78_0[#var_78_0 + 1] = var_0_5.GetCharacterGoPath(var_78_4)
	else
		var_78_0[#var_78_0 + 1] = var_0_5.GetBulletPath(var_78_4)
	end

	var_78_3(var_78_5)
	var_78_3(var_78_6)
	var_78_3(var_78_7)

	if var_78_8 and var_78_8 ~= "" then
		var_78_0[#var_78_0 + 1] = var_0_5.GetFXPath(var_78_8)
	end

	if var_78_9 and var_78_9 ~= "" then
		var_78_0[#var_78_0 + 1] = var_0_5.GetFXPath(var_78_9)
	end

	return var_78_0
end

function var_0_5.GetEquipSkinBulletRes(arg_81_0)
	local var_81_0 = {}
	local var_81_1, var_81_2, var_81_3, var_81_4 = var_0_1.GetEquipSkin(arg_81_0)

	local function var_81_5(arg_82_0)
		if arg_82_0 ~= "" then
			var_81_0[#var_81_0 + 1] = var_0_5.GetBulletPath(arg_82_0)
		end
	end

	local var_81_6 = var_0_1.GetEquipSkinDataFromID(arg_81_0)
	local var_81_7 = false

	for iter_81_0, iter_81_1 in ipairs(var_81_6.equip_type) do
		if table.contains(EquipType.AircraftSkinType, iter_81_1) then
			var_81_7 = true
		end
	end

	if var_81_7 then
		if var_81_1 ~= "" then
			var_81_0[#var_81_0 + 1] = var_0_5.GetCharacterGoPath(var_81_1)
		end
	else
		var_81_5(var_81_1)

		if var_0_1.GetEquipSkinDataFromID(arg_81_0).mirror == 1 then
			var_81_0[#var_81_0 + 1] = var_0_5.GetBulletPath(var_81_1 .. var_0_0.Battle.BattleBulletUnit.MIRROR_RES)
		end
	end

	var_81_5(var_81_2)
	var_81_5(var_81_3)
	var_81_5(var_81_4)

	return var_81_0
end

function var_0_5.GetAidUnitsRes(arg_83_0)
	local var_83_0 = {}

	for iter_83_0, iter_83_1 in ipairs(arg_83_0) do
		local var_83_1 = var_0_5.GetShipResource(iter_83_1.tmpID, nil, true)

		for iter_83_2, iter_83_3 in ipairs(iter_83_1.equipment) do
			if iter_83_3 ~= 0 then
				if iter_83_2 <= Ship.WEAPON_COUNT then
					local var_83_2 = var_0_1.GetWeaponDataFromID(iter_83_3).weapon_id

					for iter_83_4, iter_83_5 in ipairs(var_83_2) do
						local var_83_3 = var_0_5.GetWeaponResource(iter_83_5)

						for iter_83_6, iter_83_7 in ipairs(var_83_3) do
							table.insert(var_83_1, iter_83_7)
						end
					end
				else
					local var_83_4 = var_0_5.GetEquipResource(iter_83_3)

					for iter_83_8, iter_83_9 in ipairs(var_83_4) do
						table.insert(var_83_1, iter_83_9)
					end
				end
			end
		end

		for iter_83_10, iter_83_11 in ipairs(var_83_1) do
			table.insert(var_83_0, iter_83_11)
		end
	end

	return var_83_0
end

function var_0_5.GetSpWeaponResource(arg_84_0, arg_84_1)
	local var_84_0 = {}
	local var_84_1 = var_0_0.Battle.BattleDataFunction.GetSpWeaponDataFromID(arg_84_0).effect_id

	if var_84_1 ~= 0 then
		var_84_1 = arg_84_1 and var_0_0.Battle.BattleDataFunction.SkillTranform(arg_84_1, var_84_1) or var_84_1

		local var_84_2 = var_0_0.Battle.BattleDataFunction.GetResFromBuff(var_84_1, 1, {})

		for iter_84_0, iter_84_1 in ipairs(var_84_2) do
			var_84_0[#var_84_0 + 1] = iter_84_1
		end
	end

	return var_84_0
end
