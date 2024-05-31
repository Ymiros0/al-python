local var_0_0 = singletonClass("PoolMgr")

pg = pg or {}
pg.PoolMgr = var_0_0
PoolMgr = var_0_0

local var_0_1 = require("Mgr/Pool/PoolPlural")
local var_0_2 = require("Mgr/Pool/PoolSingleton")
local var_0_3 = require("Mgr/Pool/PoolObjPack")
local var_0_4 = require("Mgr/Pool/PoolUtil")
local var_0_5 = ResourceMgr.Inst

def var_0_0.Ctor(arg_1_0):
	arg_1_0.root = GameObject.New("__Pool__").transform
	arg_1_0.pools_plural = {}
	arg_1_0.pools_pack = {}
	arg_1_0.callbacks = {}
	arg_1_0.pluralIndex = 0
	arg_1_0.singleIndex = 0
	arg_1_0.paintingCount = 0
	arg_1_0.commanderPaintingCount = 0
	arg_1_0.preloads = {
		shiptype = {
			"battle_hangmu",
			"battle_qingxun",
			"battle_quzhu",
			"battle_weixiu",
			"battle_zhanlie",
			"battle_zhongxun",
			"hangmu",
			"hangxun",
			"hangzhan",
			"leixun",
			"qingxun",
			"quzhu",
			"weixiu",
			"xunyang",
			"zhanlie",
			"zhongxun"
		},
		shipframe = {
			"1",
			"2",
			"3",
			"4",
			"4_0",
			"4_1",
			"5",
			"5_0",
			"5_1",
			"prop",
			"prop4_0",
			"prop4_1",
			"prop5_0"
		},
		shipframeb = {
			"b1",
			"b2",
			"b3",
			"b3_1",
			"b4",
			"b4_0",
			"b4_1",
			"b5",
			"b5_0",
			"b5_1",
			"ba",
			"bl",
			"bprop",
			"bprop4_0",
			"bprop4_1",
			"bprop5_0"
		},
		["shipyardicon/unknown"] = {
			""
		},
		skillframe = {
			"skill_red",
			"skill_blue",
			"skill_yellow"
		},
		weaponframes = {
			"bg1",
			"bg2",
			"bg3",
			"bg3_1",
			"bg4",
			"bg4_0",
			"bg4_1",
			"bg5",
			"bg5_0",
			"bg5_1",
			"bg7",
			"bg8",
			"bg9",
			"bg_skin",
			"frame",
			"frame3_1",
			"frame4_0",
			"frame4_1",
			"frame5_0",
			"frame8",
			"frame9",
			"frame_design",
			"frame_design_owned",
			"frame_npc",
			"frame_prop",
			"frame_prop_meta",
			"frame_skin"
		},
		energy = {
			"express_1",
			"express_2",
			"express_3",
			"express_4"
		},
		shipstatus = {},
		channel = {},
		["painting/mat"] = {}
	}
	arg_1_0.ui_tempCache = {}

def var_0_0.Init(arg_2_0, arg_2_1):
	print("initializing pool manager...")

	local var_2_0 = 0
	local var_2_1 = table.getCount(arg_2_0.preloads)

	local function var_2_2()
		var_2_0 = var_2_0 + 1

		if var_2_0 == var_2_1:
			arg_2_1()

	for iter_2_0, iter_2_1 in pairs(arg_2_0.preloads):
		if #iter_2_1 > 0:
			local var_2_3 = typeof(Sprite)
			local var_2_4 = False

			local function var_2_5(arg_4_0)
				return

			buildTempAB(iter_2_0, function(arg_5_0)
				for iter_5_0, iter_5_1 in ipairs(iter_2_1):
					local var_5_0 = arg_5_0.LoadAssetSync(iter_5_1, var_2_3, var_2_4, False)
					local var_5_1 = iter_2_0
					local var_5_2 = iter_5_1

					if arg_2_0.pools_pack[var_5_1] and arg_2_0.pools_pack[var_5_1].Get(var_5_2):
						var_2_5(arg_2_0.pools_pack[var_5_1].Get(var_5_2))
					else
						if not arg_2_0.pools_pack[var_5_1]:
							arg_2_0.pools_pack[var_5_1] = var_0_3.New(var_2_3)

						if not arg_2_0.pools_pack[var_5_1].Get(var_5_2):
							arg_2_0.pools_pack[var_5_1].Set(var_5_2, var_5_0)

						var_2_5(var_5_0)

				var_2_2())
		else
			buildTempAB(iter_2_0, function(arg_6_0)
				var_2_2())

def var_0_0.GetSpineChar(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	local var_7_0 = ("char/" .. arg_7_1) .. arg_7_1

	local function var_7_1()
		local var_8_0 = arg_7_0.pools_plural[var_7_0]

		var_8_0.index = arg_7_0.pluralIndex
		arg_7_0.pluralIndex = arg_7_0.pluralIndex + 1

		local var_8_1 = var_8_0.Dequeue()

		var_8_1.SetActive(True)
		arg_7_3(var_8_1)

	if not arg_7_0.pools_plural[var_7_0]:
		arg_7_0.GetSpineSkel(arg_7_1, arg_7_2, function(arg_9_0)
			assert(arg_9_0 != None, "Spine角色不存在. " .. arg_7_1)

			if not arg_7_0.pools_plural[var_7_0]:
				arg_9_0 = SpineAnimUI.AnimChar(arg_7_1, arg_9_0)

				arg_9_0.SetActive(False)
				tf(arg_9_0).SetParent(arg_7_0.root, False)

				local var_9_0 = arg_9_0.GetComponent("SkeletonGraphic")

				var_9_0.material = var_9_0.skeletonDataAsset.atlasAssets[0].materials[0]
				arg_7_0.pools_plural[var_7_0] = var_0_1.New(arg_9_0, 1)

			var_7_1())
	else
		var_7_1()

def var_0_0.ReturnSpineChar(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = ("char/" .. arg_10_1) .. arg_10_1

	if IsNil(arg_10_2):
		Debugger.LogError(debug.traceback("empty go. " .. arg_10_1))
	elif arg_10_0.pools_plural[var_10_0]:
		if arg_10_2.GetComponent("SkeletonGraphic").allowMultipleCanvasRenderers:
			UIUtil.ClearChildren(arg_10_2, {
				"Renderer"
			})
		else
			UIUtil.ClearChildren(arg_10_2)

		setActiveViaLayer(arg_10_2.transform, True)
		arg_10_2.SetActive(False)
		arg_10_2.transform.SetParent(arg_10_0.root, False)

		arg_10_2.transform.localPosition = Vector3.New(0, 0, 0)
		arg_10_2.transform.localScale = Vector3.New(0.5, 0.5, 1)
		arg_10_2.transform.localRotation = Quaternion.identity

		arg_10_0.pools_plural[var_10_0].Enqueue(arg_10_2)
		arg_10_0.ExcessSpineChar()
	else
		var_0_4.Destroy(arg_10_2)

def var_0_0.ExcessSpineChar(arg_11_0):
	local var_11_0 = 0
	local var_11_1 = 6
	local var_11_2 = {}

	for iter_11_0, iter_11_1 in pairs(arg_11_0.pools_plural):
		if string.find(iter_11_0, "char/") == 1:
			table.insert(var_11_2, iter_11_0)

	if var_11_1 < #var_11_2:
		table.sort(var_11_2, function(arg_12_0, arg_12_1)
			return arg_11_0.pools_plural[arg_12_0].index > arg_11_0.pools_plural[arg_12_1].index)

		for iter_11_2 = var_11_1 + 1, #var_11_2:
			local var_11_3 = var_11_2[iter_11_2]

			arg_11_0.pools_plural[var_11_3].Clear()

			arg_11_0.pools_plural[var_11_3] = None

def var_0_0.GetSpineSkel(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	local var_13_0, var_13_1 = HXSet.autoHxShiftPath("char/" .. arg_13_1, arg_13_1)
	local var_13_2 = var_13_1 .. "_SkeletonData"

	arg_13_0.LoadAsset(var_13_0, var_13_2, arg_13_2, typeof(Object), function(arg_14_0)
		arg_13_3(arg_14_0), True)

def var_0_0.IsSpineSkelCached(arg_15_0, arg_15_1):
	local var_15_0 = ("char/" .. arg_15_1) .. arg_15_1

	return arg_15_0.pools_plural[var_15_0] != None

local var_0_6 = {
	"ResPanel",
	"WorldResPanel"
}
local var_0_7 = {
	"ResPanel",
	"WorldResPanel",
	"NewMainUI",
	"DockyardUI",
	"AwardInfoUI",
	"SkillInfoUI",
	"ItemInfoUI",
	"ShipDetailView",
	"LevelFleetSelectView",
	"ToastUI",
	"MsgBox",
	"TipPanel",
	"Loading",
	"WorldUI"
}
local var_0_8 = {}

def var_0_0.GetUI(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	local var_16_0 = "ui/" .. arg_16_1
	local var_16_1 = table.contains(var_0_6, arg_16_1) and 3 or 1
	local var_16_2 = table.contains(var_0_7, arg_16_1) or table.contains(var_0_8, arg_16_1)

	arg_16_0.FromPlural(var_16_0, arg_16_1, arg_16_2, var_16_1, function(arg_17_0)
		local function var_17_0()
			arg_16_3(arg_17_0)

		if table.indexof(var_0_8, arg_16_1):
			local var_17_1 = var_16_0 .. arg_16_1

			arg_16_0.pools_plural[var_17_1].prefab.GetComponent(typeof(UIArchiver)).Clear()
			arg_17_0.GetComponent(typeof(UIArchiver)).Load(var_17_0)
		else
			var_17_0(), var_16_2)

def var_0_0.BuildUIPlural(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0 = "ui/" .. arg_19_1
	local var_19_1 = var_19_0 .. arg_19_1

	if arg_19_0.pools_plural[var_19_1]:
		return

	local var_19_2 = table.contains(var_0_6, arg_19_1) and 3 or 1
	local var_19_3 = table.contains(var_0_7, arg_19_1) or table.contains(var_0_8, arg_19_1)

	arg_19_0.LoadAsset(var_19_0, arg_19_1, True, typeof(Object), function(arg_20_0)
		if arg_20_0 == None:
			Debugger.LogError("can not find asset. " .. var_19_0 .. " . " .. arg_19_1)

			return

		if not arg_19_0.pools_plural[var_19_1]:
			arg_19_0.pools_plural[var_19_1] = var_0_1.New(arg_20_0, var_19_2)

		existCall(arg_19_2), var_19_3)

def var_0_0.ReturnUI(arg_21_0, arg_21_1, arg_21_2):
	local var_21_0 = "ui/" .. arg_21_1
	local var_21_1 = var_21_0 .. arg_21_1

	if IsNil(arg_21_2):
		Debugger.LogError(debug.traceback("empty go. " .. arg_21_1))
	elif arg_21_0.pools_plural[var_21_1]:
		if table.indexof(var_0_6, arg_21_1):
			arg_21_2.transform.SetParent(arg_21_0.root, False)

		if table.indexof(var_0_7, arg_21_1) or arg_21_0.ui_tempCache[arg_21_1]:
			setActiveViaLayer(arg_21_2.transform, False)
			arg_21_0.pools_plural[var_21_1].Enqueue(arg_21_2)
		elif table.indexof(var_0_8, arg_21_1):
			setActiveViaLayer(arg_21_2.transform, False)
			arg_21_2.GetComponent(typeof(UIArchiver)).Clear()
			arg_21_0.pools_plural[var_21_1].Enqueue(arg_21_2)
		else
			arg_21_0.pools_plural[var_21_1].Enqueue(arg_21_2, True)

			if arg_21_0.pools_plural[var_21_1].AllReturned() and (not arg_21_0.callbacks[var_21_1] or #arg_21_0.callbacks[var_21_1] == 0):
				var_0_5.ClearBundleRef(var_21_0, True, True)
				arg_21_0.pools_plural[var_21_1].Clear()

				arg_21_0.pools_plural[var_21_1] = None
	else
		var_0_4.Destroy(arg_21_2)

def var_0_0.HasCacheUI(arg_22_0, arg_22_1):
	local var_22_0 = ("ui/" .. arg_22_1) .. arg_22_1

	return arg_22_0.pools_plural[var_22_0] != None

def var_0_0.PreloadUI(arg_23_0, arg_23_1, arg_23_2):
	local var_23_0 = {}
	local var_23_1 = ("ui/" .. arg_23_1) .. arg_23_1

	if not arg_23_0.pools_plural[var_23_1]:
		table.insert(var_23_0, function(arg_24_0)
			arg_23_0.GetUI(arg_23_1, True, function(arg_25_0)
				arg_23_0.pools_plural[var_23_1].Enqueue(arg_25_0)
				arg_24_0()))

	seriesAsync(var_23_0, arg_23_2)

def var_0_0.AddTempCache(arg_26_0, arg_26_1):
	arg_26_0.ui_tempCache[arg_26_1] = True

def var_0_0.DelTempCache(arg_27_0, arg_27_1):
	arg_27_0.ui_tempCache[arg_27_1] = None

def var_0_0.PreloadPainting(arg_28_0, arg_28_1, arg_28_2):
	local var_28_0 = {}
	local var_28_1 = ("painting/" .. arg_28_1) .. arg_28_1

	if not arg_28_0.pools_plural[var_28_1]:
		table.insert(var_28_0, function(arg_29_0)
			arg_28_0.GetPainting(arg_28_1, True, function(arg_30_0)
				arg_28_0.pools_plural[var_28_1].Enqueue(arg_30_0)
				arg_29_0()))

	seriesAsync(var_28_0, arg_28_2)

def var_0_0.GetPainting(arg_31_0, arg_31_1, arg_31_2, arg_31_3):
	local var_31_0 = "painting/" .. arg_31_1
	local var_31_1 = var_31_0 .. arg_31_1

	arg_31_0.FromPlural(var_31_0, arg_31_1, arg_31_2, 1, function(arg_32_0)
		arg_32_0.SetActive(True)

		if ShipExpressionHelper.DefaultFaceless(arg_31_1):
			setActive(tf(arg_32_0).Find("face"), True)

		arg_31_3(arg_32_0), True)

def var_0_0.ReturnPainting(arg_33_0, arg_33_1, arg_33_2):
	local var_33_0 = ("painting/" .. arg_33_1) .. arg_33_1

	if IsNil(arg_33_2):
		Debugger.LogError(debug.traceback("empty go. " .. arg_33_1))
	elif arg_33_0.pools_plural[var_33_0]:
		setActiveViaLayer(arg_33_2, True)

		local var_33_1 = tf(arg_33_2).Find("face")

		if var_33_1:
			setActive(var_33_1, False)

		arg_33_2.SetActive(False)
		arg_33_2.transform.SetParent(arg_33_0.root, False)
		arg_33_0.pools_plural[var_33_0].Enqueue(arg_33_2)
		arg_33_0.ExcessPainting()
	else
		var_0_4.Destroy(arg_33_2, True)

def var_0_0.ExcessPainting(arg_34_0):
	local var_34_0 = 0
	local var_34_1 = 4
	local var_34_2 = {}

	for iter_34_0, iter_34_1 in pairs(arg_34_0.pools_plural):
		local var_34_3 = string.find(iter_34_0, "painting/")

		if var_34_3 and var_34_3 >= 1:
			table.insert(var_34_2, iter_34_0)

	if var_34_1 < #var_34_2:
		table.sort(var_34_2, function(arg_35_0, arg_35_1)
			return arg_34_0.pools_plural[arg_35_0].index > arg_34_0.pools_plural[arg_35_1].index)

		for iter_34_2 = var_34_1 + 1, #var_34_2:
			local var_34_4 = var_34_2[iter_34_2]

			arg_34_0.pools_plural[var_34_4].Clear(True)

			arg_34_0.pools_plural[var_34_4] = None

		var_0_5.unloadUnusedAssetBundles()

		arg_34_0.paintingCount = arg_34_0.paintingCount + 1

		if arg_34_0.paintingCount > 10:
			arg_34_0.paintingCount = 0

			var_0_5.Inst.ResUnloadAsync()

def var_0_0.GetPaintingWithPrefix(arg_36_0, arg_36_1, arg_36_2, arg_36_3, arg_36_4):
	local var_36_0 = arg_36_4 .. arg_36_1
	local var_36_1 = var_36_0 .. arg_36_1

	arg_36_0.FromPlural(var_36_0, arg_36_1, arg_36_2, 1, function(arg_37_0)
		arg_37_0.SetActive(True)

		if ShipExpressionHelper.DefaultFaceless(arg_36_1):
			setActive(tf(arg_37_0).Find("face"), True)

		arg_36_3(arg_37_0), True)

def var_0_0.ReturnPaintingWithPrefix(arg_38_0, arg_38_1, arg_38_2, arg_38_3):
	local var_38_0 = (arg_38_3 .. arg_38_1) .. arg_38_1

	if IsNil(arg_38_2):
		Debugger.LogError(debug.traceback("empty go. " .. arg_38_1))
	elif arg_38_0.pools_plural[var_38_0]:
		setActiveViaLayer(arg_38_2, True)

		local var_38_1 = tf(arg_38_2).Find("face")

		if var_38_1:
			setActive(var_38_1, False)

		arg_38_2.SetActive(False)
		arg_38_2.transform.SetParent(arg_38_0.root, False)
		arg_38_0.pools_plural[var_38_0].Enqueue(arg_38_2)
		arg_38_0.ExcessPainting()
	else
		var_0_4.Destroy(arg_38_2, True)

def var_0_0.GetSprite(arg_39_0, arg_39_1, arg_39_2, arg_39_3, arg_39_4):
	arg_39_0.FromObjPack(arg_39_1, tostring(arg_39_2), arg_39_3, typeof(Sprite), function(arg_40_0)
		arg_39_4(arg_40_0))

def var_0_0.DecreasSprite(arg_41_0, arg_41_1, arg_41_2):
	local var_41_0 = arg_41_1
	local var_41_1 = typeof(Sprite)

	if arg_41_0.pools_pack[var_41_0] and arg_41_0.pools_pack[var_41_0].type == var_41_1:
		if arg_41_0.pools_pack[var_41_0].Remove(arg_41_2):
			var_0_5.ClearBundleRef(var_41_0, False, False)

		if arg_41_0.pools_pack[var_41_0].GetAmount() <= 0:
			arg_41_0.pools_pack[var_41_0].Clear()

			arg_41_0.pools_pack[var_41_0] = None

def var_0_0.DestroySprite(arg_42_0, arg_42_1):
	local var_42_0 = arg_42_1
	local var_42_1 = typeof(Sprite)

	if arg_42_0.pools_pack[var_42_0] and arg_42_0.pools_pack[var_42_0].type == var_42_1:
		local var_42_2 = arg_42_0.pools_pack[var_42_0].GetAmount()

		arg_42_0.pools_pack[var_42_0].Clear()

		arg_42_0.pools_pack[var_42_0] = None

		for iter_42_0 = 1, var_42_2:
			var_0_5.ClearBundleRef(var_42_0, False, False)

def var_0_0.DestroyAllSprite(arg_43_0):
	local var_43_0 = {}
	local var_43_1 = typeof(Sprite)

	for iter_43_0, iter_43_1 in pairs(arg_43_0.pools_pack):
		if iter_43_1.type == var_43_1 and not arg_43_0.preloads[iter_43_0]:
			var_43_0[iter_43_0] = iter_43_1

	for iter_43_2, iter_43_3 in pairs(var_43_0):
		local var_43_2 = arg_43_0.pools_pack[iter_43_2].GetAmount()

		arg_43_0.pools_pack[iter_43_2].Clear()

		arg_43_0.pools_pack[iter_43_2] = None

		for iter_43_4 = 1, var_43_2:
			var_0_5.ClearBundleRef(iter_43_2, False, False)

	var_0_5.unloadUnusedAssetBundles()

def var_0_0.DisplayPoolPacks(arg_44_0):
	local var_44_0 = ""

	for iter_44_0, iter_44_1 in pairs(arg_44_0.pools_pack):
		for iter_44_2, iter_44_3 in pairs(iter_44_1.items):
			if #var_44_0 > 0:
				var_44_0 = var_44_0 .. "\n"

			local var_44_1 = _.map({
				iter_44_0,
				"assetName.",
				iter_44_2,
				"type.",
				iter_44_1.type.FullName
			}, function(arg_45_0)
				return tostring(arg_45_0))

			var_44_0 = var_44_0 .. " " .. table.concat(var_44_1, " ")

	warning(var_44_0)

def var_0_0.SpriteMemUsage(arg_46_0):
	local var_46_0 = 0
	local var_46_1 = 9.5367431640625e-07
	local var_46_2 = typeof(Sprite)

	for iter_46_0, iter_46_1 in pairs(arg_46_0.pools_pack):
		if iter_46_1.type == var_46_2:
			local var_46_3 = {}

			for iter_46_2, iter_46_3 in pairs(iter_46_1.items):
				local var_46_4 = iter_46_3.texture
				local var_46_5 = var_46_4.name

				if not var_46_3[var_46_5]:
					local var_46_6 = 4
					local var_46_7 = var_46_4.format

					if var_46_7 == TextureFormat.RGB24:
						var_46_6 = 3
					elif var_46_7 == TextureFormat.ARGB4444 or var_46_7 == TextureFormat.RGBA4444:
						var_46_6 = 2
					elif var_46_7 == TextureFormat.DXT5 or var_46_7 == TextureFormat.ETC2_RGBA8:
						var_46_6 = 1
					elif var_46_7 == TextureFormat.PVRTC_RGB4 or var_46_7 == TextureFormat.PVRTC_RGBA4 or var_46_7 == TextureFormat.ETC_RGB4 or var_46_7 == TextureFormat.ETC2_RGB or var_46_7 == TextureFormat.DXT1:
						var_46_6 = 0.5

					var_46_0 = var_46_0 + var_46_4.width * var_46_4.height * var_46_6 * var_46_1
					var_46_3[var_46_5] = True

	return var_46_0

local var_0_9 = 64
local var_0_10 = {
	"chapter/",
	"emoji/",
	"world/"
}

def var_0_0.GetPrefab(arg_47_0, arg_47_1, arg_47_2, arg_47_3, arg_47_4, arg_47_5):
	local var_47_0 = arg_47_1 .. arg_47_2

	arg_47_0.FromPlural(arg_47_1, arg_47_2, arg_47_3, arg_47_5 or var_0_9, function(arg_48_0)
		if string.find(arg_47_1, "emoji/") == 1:
			local var_48_0 = arg_48_0.GetComponent(typeof(CriManaEffectUI))

			if var_48_0:
				var_48_0.Pause(False)

		arg_48_0.SetActive(True)
		tf(arg_48_0).SetParent(arg_47_0.root, False)
		arg_47_4(arg_48_0), True)

def var_0_0.ReturnPrefab(arg_49_0, arg_49_1, arg_49_2, arg_49_3, arg_49_4):
	local var_49_0 = arg_49_1 .. arg_49_2

	if IsNil(arg_49_3):
		Debugger.LogError(debug.traceback("empty go. " .. arg_49_2))
	elif arg_49_0.pools_plural[var_49_0]:
		if string.find(arg_49_1, "emoji/") == 1:
			local var_49_1 = arg_49_3.GetComponent(typeof(CriManaEffectUI))

			if var_49_1:
				var_49_1.Pause(True)

		arg_49_3.SetActive(False)
		arg_49_3.transform.SetParent(arg_49_0.root, False)
		arg_49_0.pools_plural[var_49_0].Enqueue(arg_49_3)

		if arg_49_4 and arg_49_0.pools_plural[var_49_0].balance <= 0 and (not arg_49_0.callbacks[var_49_0] or #arg_49_0.callbacks[var_49_0] == 0):
			arg_49_0.DestroyPrefab(arg_49_1, arg_49_2)
	else
		var_0_4.Destroy(arg_49_3)

def var_0_0.DestroyPrefab(arg_50_0, arg_50_1, arg_50_2):
	local var_50_0 = arg_50_1 .. arg_50_2

	if arg_50_0.pools_plural[var_50_0]:
		arg_50_0.pools_plural[var_50_0].Clear()

		arg_50_0.pools_plural[var_50_0] = None

		var_0_5.ClearBundleRef(arg_50_1, True, False)

def var_0_0.DestroyAllPrefab(arg_51_0):
	local var_51_0 = {}

	for iter_51_0, iter_51_1 in pairs(arg_51_0.pools_plural):
		if _.any(var_0_10, function(arg_52_0)
			return string.find(iter_51_0, arg_52_0) == 1):
			iter_51_1.Clear()
			var_0_5.ClearBundleRef(iter_51_0, True, False)
			table.insert(var_51_0, iter_51_0)

	_.each(var_51_0, function(arg_53_0)
		arg_51_0.pools_plural[arg_53_0] = None)

def var_0_0.DisplayPluralPools(arg_54_0):
	local var_54_0 = ""

	for iter_54_0, iter_54_1 in pairs(arg_54_0.pools_plural):
		if #var_54_0 > 0:
			var_54_0 = var_54_0 .. "\n"

		local var_54_1 = _.map({
			iter_54_0,
			"balance",
			iter_54_1.balance,
			"currentItmes",
			#iter_54_1.items
		}, function(arg_55_0)
			return tostring(arg_55_0))

		var_54_0 = var_54_0 .. " " .. table.concat(var_54_1, " ")

	warning(var_54_0)

def var_0_0.GetPluralStatus(arg_56_0, arg_56_1):
	if not arg_56_0.pools_plural[arg_56_1]:
		return "NIL"

	local var_56_0 = arg_56_0.pools_plural[arg_56_1]
	local var_56_1 = _.map({
		arg_56_1,
		"balance",
		var_56_0.balance,
		"currentItmes",
		#var_56_0.items
	}, tostring)

	return table.concat(var_56_1, " ")

def var_0_0.FromPlural(arg_57_0, arg_57_1, arg_57_2, arg_57_3, arg_57_4, arg_57_5, arg_57_6):
	local var_57_0 = arg_57_1 .. arg_57_2

	local function var_57_1()
		local var_58_0 = arg_57_0.pools_plural[var_57_0]

		var_58_0.index = arg_57_0.pluralIndex
		arg_57_0.pluralIndex = arg_57_0.pluralIndex + 1

		arg_57_5(var_58_0.Dequeue())

	if not arg_57_0.pools_plural[var_57_0]:
		arg_57_0.LoadAsset(arg_57_1, arg_57_2, arg_57_3, typeof(Object), function(arg_59_0)
			if arg_59_0 == None:
				Debugger.LogError("can not find asset. " .. arg_57_1 .. " . " .. arg_57_2)

				return

			if not arg_57_0.pools_plural[var_57_0]:
				arg_57_0.pools_plural[var_57_0] = var_0_1.New(arg_59_0, arg_57_4)

			var_57_1(), arg_57_6)
	else
		var_57_1()

def var_0_0.FromObjPack(arg_60_0, arg_60_1, arg_60_2, arg_60_3, arg_60_4, arg_60_5):
	local var_60_0 = arg_60_1

	if not arg_60_0.pools_pack[var_60_0] or not arg_60_0.pools_pack[var_60_0].Get(arg_60_2):
		arg_60_0.LoadAsset(arg_60_1, arg_60_2, arg_60_3, arg_60_4, function(arg_61_0)
			if not arg_60_0.pools_pack[var_60_0]:
				arg_60_0.pools_pack[var_60_0] = var_0_3.New(arg_60_4)

			if not arg_60_0.pools_pack[var_60_0].Get(arg_60_2):
				arg_60_0.pools_pack[var_60_0].Set(arg_60_2, arg_61_0)

			arg_60_5(arg_61_0), False)
	else
		arg_60_5(arg_60_0.pools_pack[var_60_0].Get(arg_60_2))

def var_0_0.LoadAsset(arg_62_0, arg_62_1, arg_62_2, arg_62_3, arg_62_4, arg_62_5, arg_62_6):
	arg_62_1, arg_62_2 = HXSet.autoHxShiftPath(arg_62_1, arg_62_2)

	local var_62_0 = arg_62_1 .. arg_62_2

	if arg_62_0.callbacks[var_62_0]:
		if not arg_62_3:
			errorMsg("Sync Loading after async operation")

		table.insert(arg_62_0.callbacks[var_62_0], arg_62_5)
	elif arg_62_3:
		arg_62_0.callbacks[var_62_0] = {
			arg_62_5
		}

		var_0_5.getAssetAsync(arg_62_1, arg_62_2, arg_62_4, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_63_0)
			if arg_62_0.callbacks[var_62_0]:
				local var_63_0 = arg_62_0.callbacks[var_62_0]

				arg_62_0.callbacks[var_62_0] = None

				while next(var_63_0):
					table.remove(var_63_0)(arg_63_0)), arg_62_6, False)
	else
		arg_62_5(var_0_5.getAssetSync(arg_62_1, arg_62_2, arg_62_4, arg_62_6, False))

def var_0_0.PrintPools(arg_64_0):
	local var_64_0 = ""

	for iter_64_0, iter_64_1 in pairs(arg_64_0.pools_plural):
		var_64_0 = var_64_0 .. "\n" .. iter_64_0

	warning(var_64_0)

def var_0_0.PrintObjPack(arg_65_0):
	local var_65_0 = ""

	for iter_65_0, iter_65_1 in pairs(arg_65_0.pools_pack):
		for iter_65_2, iter_65_3 in pairs(iter_65_1.items):
			var_65_0 = var_65_0 .. "\n" .. iter_65_0 .. " " .. iter_65_2

	warning(var_65_0)

return var_0_0
