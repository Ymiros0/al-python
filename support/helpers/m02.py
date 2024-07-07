import re
from packages.luatable import table, pairs, Clone, ipairs, setmetatable

from lib import pg

def flog(arg_1_0, arg_1_1):
	if arg_1_0 and arg_1_1 and pg.ConnectionMgr.GetInstance().isConnected():
		pg.m02.sendNotification(GAME.SEND_CMD, table(
			cmd = "log",
			arg1 = arg_1_0,
			arg2 = arg_1_1
		))

def throttle(arg_2_0, arg_2_1, arg_2_2):
	var_2_3 = 0

	def var_2_4():
		var_2_3 = arg_2_2 and Time.unscaledTime or 0
		var_2_0 = None
		var_2_2 = arg_2_0(unpackEx(var_2_1))

		if not var_2_0:
			var_2_1 = None

	def _function(*args):
		var_4_0 = Time.unscaledTime

		if not var_2_3 and not arg_2_2:
			var_2_3 = var_4_0

		var_4_1 = arg_2_1 - (var_4_0 - var_2_3)

		var_2_1 = packEx(*args)

		if var_4_1 <= 0 or var_4_1 > arg_2_1:
			if var_2_0:
				var_2_0.Stop()

				var_2_0 = None

			var_2_3 = var_4_0
			var_2_2 = arg_2_0(unpackEx(var_2_1))

			if not var_2_0:
				var_2_1 = None
		elif not var_2_0 and arg_2_2:
			var_2_0 = Timer.New(var_2_4, var_4_1, 1)

			var_2_0.Start()

		return var_2_2

	return _function

def debounce(arg_5_0, arg_5_1, arg_5_2):
	var_5_2 = None
	def var_5_5():
		var_6_0 = Time.unscaledTime - var_5_2

		if var_6_0 < arg_5_1 and var_6_0 > 0:
			var_5_0 = Timer.New(var_5_5, arg_5_1 - var_6_0, 1)

			var_5_0.Start()
		else:
			var_5_0 = None

			if not arg_5_2:
				var_5_3 = arg_5_0(unpackEx(var_5_1))

				if not var_5_0:
					var_5_1 = None
			else:
				arg_5_2 = False

	def _function(*args):
		var_5_1 = packEx(*args)
		var_5_2 = Time.unscaledTime

		var_7_0 = arg_5_2 and not var_5_0

		if not var_5_0:
			var_5_0 = Timer.New(var_5_5, arg_5_1, 1)

			var_5_0.Start()

		if var_7_0:
			var_5_3 = arg_5_0(unpackEx(var_5_1))
			var_5_1 = None

		return var_5_3

	return _function

def createLog(arg_8_0, arg_8_1):
	if LOG and arg_8_1:
		return lambda *args: print(f"{arg_8_0}. ", *args)
	else:
		print(f"{arg_8_0}. log disabled")

		return lambda: None

def getProxy(arg_11_0):
	assert pg.m02, "game is not started"

	return pg.m02.retrieveProxy(arg_11_0.__cname)

def LoadAndInstantiateAsync(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4):
	arg_12_4 = defaultValue(arg_12_4, True)
	arg_12_3 = defaultValue(arg_12_3, True)
	arg_12_0, arg_12_1 = HXSet.autoHxShift(f"{arg_12_0}/", arg_12_1)

	def _function(arg_13_0):
		var_13_0 = Instantiate(arg_13_0)

		arg_12_2(var_13_0)

	ResourceMgr.Inst.getAssetAsync(f"{arg_12_0}{arg_12_1}", arg_12_1, UnityEngine.Events.UnityAction_UnityEngine_Object(_function), arg_12_3, arg_12_4)

def LoadAndInstantiateSync(arg_14_0, arg_14_1, arg_14_2, arg_14_3):
	arg_14_3 = defaultValue(arg_14_3, True)
	arg_14_2 = defaultValue(arg_14_2, True)
	arg_14_0, arg_14_1 = HXSet.autoHxShift(f"{arg_14_0}/", arg_14_1)

	var_14_0 = ResourceMgr.Inst.getAssetSync(f"{arg_14_0}{arg_14_1}", arg_14_1, arg_14_2, arg_14_3)

	return (Instantiate(var_14_0))

var_0_1 = table()

def LoadSprite(arg_15_0, arg_15_1):
	arg_15_0, arg_15_1 = HXSet.autoHxShiftPath(arg_15_0, arg_15_1)

	return ResourceMgr.Inst.getAssetSync(arg_15_0, arg_15_1 or "", typeof(Sprite), True, False)

def LoadSpriteAtlasAsync(arg_16_0, arg_16_1, arg_16_2):
	arg_16_0, arg_16_1 = HXSet.autoHxShiftPath(arg_16_0, arg_16_1)

	ResourceMgr.Inst.getAssetAsync(arg_16_0, arg_16_1 or "", typeof(Sprite), UnityEngine.Events.UnityAction_UnityEngine_Object(lambda arg_17_0: arg_16_2(arg_17_0)), True, False)

def LoadSpriteAsync(arg_18_0, arg_18_1):
	LoadSpriteAtlasAsync(arg_18_0, None, arg_18_1)

def LoadAny(arg_19_0, arg_19_1, arg_19_2):
	arg_19_0, arg_19_1 = HXSet.autoHxShiftPath(arg_19_0, arg_19_1)

	return ResourceMgr.Inst.getAssetSync(arg_19_0, arg_19_1, arg_19_2, True, False)

def LoadAnyAsync(arg_20_0, arg_20_1, arg_20_2, arg_20_3):
	arg_20_0, arg_20_1 = HXSet.autoHxShiftPath(arg_20_0, arg_20_1)

	return ResourceMgr.Inst.getAssetAsync(arg_20_0, arg_20_1, arg_20_2, arg_20_3, True, False)

def LoadImageSpriteAtlasAsync(arg_21_0, arg_21_1, arg_21_2, arg_21_3):
	var_21_0 = arg_21_2.GetComponent(typeof(Image))

	var_21_0.enabled = False
	var_0_1[var_21_0] = arg_21_0

	def _function(arg_22_0):
		if var_21_0 is not None and var_0_1[var_21_0] == arg_21_0:
			var_0_1[var_21_0] = None
			var_21_0.enabled = True
			var_21_0.sprite = arg_22_0

			if arg_21_3:
				var_21_0.SetNativeSize()

	LoadSpriteAtlasAsync(arg_21_0, arg_21_1, _function)

def LoadImageSpriteAsync(arg_23_0, arg_23_1, arg_23_2):
	LoadImageSpriteAtlasAsync(arg_23_0, None, arg_23_1, arg_23_2)

def GetSpriteFromAtlas(arg_24_0, arg_24_1):
	var_24_0 = None

	arg_24_0, arg_24_1 = HXSet.autoHxShiftPath(arg_24_0, arg_24_1)

	def _function(arg_25_0):
		var_24_0 = arg_25_0

	PoolMgr.GetInstance().GetSprite(arg_24_0, arg_24_1, False, _function)

	return var_24_0

def GetSpriteFromAtlasAsync(arg_26_0, arg_26_1, arg_26_2):
	arg_26_0, arg_26_1 = HXSet.autoHxShiftPath(arg_26_0, arg_26_1)

	PoolMgr.GetInstance().GetSprite(arg_26_0, arg_26_1, True, lambda arg_27_0: arg_26_2(arg_27_0))

def GetImageSpriteFromAtlasAsync(arg_28_0, arg_28_1, arg_28_2, arg_28_3):
	arg_28_0, arg_28_1 = HXSet.autoHxShiftPath(arg_28_0, arg_28_1)

	var_28_0 = arg_28_2.GetComponent(typeof(Image))

	var_28_0.enabled = False
	var_0_1[var_28_0] = f"{arg_28_0}{arg_28_1}"

	def _function(arg_29_0):
		if var_28_0 is not None and var_0_1[var_28_0] == f"{arg_28_0}{arg_28_1}":
			var_0_1[var_28_0] = None
			var_28_0.enabled = True
			var_28_0.sprite = arg_29_0

			if arg_28_3:
				var_28_0.SetNativeSize()

	GetSpriteFromAtlasAsync(arg_28_0, arg_28_1, _function)

def SetAction(arg_30_0, arg_30_1, arg_30_2):
	GetComponent(arg_30_0, "SkeletonGraphic").AnimationState.SetAnimation(0, arg_30_1, defaultValue(arg_30_2, True))

def SetActionCallback(arg_31_0, arg_31_1):
	GetOrAddComponent(arg_31_0, typeof(SpineAnimUI)).SetActionCallBack(arg_31_1)

def emojiText(arg_32_0, arg_32_1):
	var_32_0 = buildTempAB("emojis", False)
	var_32_1 = GetComponent(arg_32_0, "TextMesh")
	var_32_2 = GetComponent(arg_32_0, "MeshRenderer")
	var_32_3 = Shader.Find("UI/Unlit/Transparent")
	var_32_4 = var_32_2.materials
	var_32_5 = table(
		var_32_4[0]
	)
	var_32_6 = table()
	var_32_7 = 0
	def _function(arg_33_0):
		if not var_32_6[arg_33_0]:
			var_32_7 = var_32_7 + 1

			var_33_0 = Material.New(var_32_3)

			var_33_0.mainTexture = var_32_0.LoadAssetSync(f"emoji{arg_33_0}", False, False)

			table.insert(var_32_5, var_33_0)

			var_32_6[arg_33_0] = var_32_7

			var_33_1 = var_32_7

		return "<quad material={var_32_7} />"
	var_32_1.text = re.sub(r"#(\d+)#", _function(r"\1"), arg_32_1)
	var_32_2.materials = var_32_5

	ResourceMgr.Inst.ClearBundleRef("emojis", False, False)

def setPaintingImg(arg_34_0, arg_34_1):
	var_34_0 = LoadSprite("painting/{arg_34_1}") or LoadSprite("painting/unknown")

	setImageSprite(arg_34_0, var_34_0)
	resetAspectRatio(arg_34_0)

def setPaintingPrefab(arg_35_0, arg_35_1, arg_35_2, arg_35_3):
	var_35_0 = findTF(arg_35_0, "fitter")

	assert var_35_0, "请添加子物体fitter"
	removeAllChildren(var_35_0)

	var_35_1 = GetOrAddComponent(var_35_0, "PaintingScaler")

	var_35_1.FrameName = arg_35_2 or ""
	var_35_1.Tween = 1

	var_35_2 = arg_35_1

	if not arg_35_3 and checkABExist("painting/{arg_35_1}_n") and PlayerPrefs.GetInt("paint_hide_other_obj_{arg_35_1}", 0) != 0:
		arg_35_1 = f"{arg_35_1}_n"

	def _function(arg_36_0):
		setParent(arg_36_0, var_35_0, False)

		var_36_0 = findTF(arg_36_0, "Touch")

		if var_36_0 is not None:
			setActive(var_36_0, False)

		var_36_1 = findTF(arg_36_0, "hx")

		if var_36_1 is not None:
			setActive(var_36_1, HXSet.isHx())

		ShipExpressionHelper.SetExpression(var_35_0.GetChild(0), var_35_2)

	PoolMgr.GetInstance().GetPainting(arg_35_1, False, _function)

var_0_2 = table()

def setPaintingPrefabAsync(arg_37_0, arg_37_1, arg_37_2, arg_37_3, arg_37_4):
	var_37_0 = arg_37_1

	if checkABExist(f"painting/{arg_37_1}_n") and PlayerPrefs.GetInt(f"paint_hide_other_obj_{arg_37_1}", 0) != 0:
		arg_37_1 = f"{arg_37_1}_n"

	LoadPaintingPrefabAsync(arg_37_0, var_37_0, arg_37_1, arg_37_2, arg_37_3)

def LoadPaintingPrefabAsync(arg_38_0, arg_38_1, arg_38_2, arg_38_3, arg_38_4):
	var_38_0 = findTF(arg_38_0, "fitter")

	assert var_38_0, "请添加子物体fitter"
	removeAllChildren(var_38_0)

	var_38_1 = GetOrAddComponent(var_38_0, "PaintingScaler")

	var_38_1.FrameName = arg_38_3 or ""
	var_38_1.Tween = 1
	var_0_2[arg_38_0] = arg_38_2

	def _function(arg_39_0):
		if arg_38_0 is None or var_0_2[arg_38_0] != arg_38_2:
			PoolMgr.GetInstance().ReturnPainting(arg_38_2, arg_39_0)

			return
		else:
			setParent(arg_39_0, var_38_0, False)

			var_0_2[arg_38_0] = None

			ShipExpressionHelper.SetExpression(arg_39_0, arg_38_1)

		var_39_0 = findTF(arg_39_0, "Touch")

		if var_39_0 is not None:
			setActive(var_39_0, False)

		var_39_1 = findTF(arg_39_0, "Drag")

		if var_39_1 is not None:
			setActive(var_39_1, False)

		var_39_2 = findTF(arg_39_0, "hx")

		if var_39_2 is not None:
			setActive(var_39_2, HXSet.isHx())

		if arg_38_4:
			arg_38_4()

	PoolMgr.GetInstance().GetPainting(arg_38_2, True, function)

def retPaintingPrefab(arg_40_0, arg_40_1, arg_40_2):
	if arg_40_0 and arg_40_1:
		var_40_0 = findTF(arg_40_0, "fitter")

		if var_40_0 and var_40_0.childCount > 0:
			var_40_1 = var_40_0.GetChild(0)

			if var_40_1 is not None:
				var_40_2 = findTF(var_40_1, "Touch")

				def _function(arg_41_0):
						var_41_0 = arg_41_0.GetComponent(typeof(Button))

						if var_41_0 is not None:
							removeOnButton(arg_41_0)

				if var_40_2 is not None:
					eachChild(var_40_2, _function)

				if not arg_40_2:
					PoolMgr.GetInstance().ReturnPainting(string.gsub(var_40_1.name, "%(Clone%)", ""), var_40_1.gameObject)
				else:
					PoolMgr.GetInstance().ReturnPaintingWithPrefix(string.gsub(var_40_1.name, "%(Clone%)", ""), var_40_1.gameObject, arg_40_2)

		var_0_2[arg_40_0] = None

def numberFormat(arg_42_0, arg_42_1):
	var_42_0 = ""
	var_42_1 = tostring(arg_42_0)
	var_42_2 = string.len(var_42_1)

	if arg_42_1 == None:
		arg_42_1 = ","

	arg_42_1 = tostring(arg_42_1)

	for iter_42_0 in range(1, var_42_2):
		var_42_0 = f"{string.char(string.byte(var_42_1, var_42_2 + 1 - iter_42_0))}{var_42_0}"

		if iter_42_0 % 3 == 0 and var_42_2 - iter_42_0 != 0:
			var_42_0 = f"{arg_42_1}{var_42_0}"

	return var_42_0

def usMoneyFormat(arg_43_0, arg_43_1):
	var_43_0 = arg_43_0 % 100
	var_43_1 = math.floor(arg_43_0 / 100)

	if var_43_0 > 0:
		var_43_0 = var_43_0 > 10 and var_43_0 or f"0{var_43_0}"

		if var_43_1 < 1:
			return f"0.{var_43_0}"
		else:
			return f"{numberFormat(var_43_1, arg_43_1)}.{var_43_0}"
	else:
		return numberFormat(var_43_1, arg_43_1)

def checkPaintingPrefab(arg_44_0, arg_44_1, arg_44_2, arg_44_3, arg_44_4):
	var_44_0 = findTF(arg_44_0, "fitter")

	assert var_44_0, "请添加子物体fitter"
	removeAllChildren(var_44_0)

	var_44_1 = GetOrAddComponent(var_44_0, "PaintingScaler")

	var_44_1.FrameName = arg_44_2 or ""
	var_44_1.Tween = 1

	var_44_2 = arg_44_4 or "painting/"
	var_44_3 = arg_44_1

	if not arg_44_3 and checkABExist(f"{var_44_2}{arg_44_1}_n") and PlayerPrefs.GetInt(f"paint_hide_other_obj_{arg_44_1}", 0) != 0:
		arg_44_1 = f"{arg_44_1}_n"

	return var_44_0, arg_44_1, var_44_3

def onLoadedPaintingPrefab(arg_45_0):
	var_45_0 = arg_45_0.paintingTF
	var_45_1 = arg_45_0.fitterTF
	var_45_2 = arg_45_0.defaultPaintingName

	setParent(var_45_0, var_45_1, False)

	var_45_3 = findTF(var_45_0, "Touch")

	if var_45_3 is not None:
		setActive(var_45_3, False)

	var_45_4 = findTF(var_45_0, "hx")

	if var_45_4 is not None:
		setActive(var_45_4, HXSet.isHx())

	ShipExpressionHelper.SetExpression(var_45_1.GetChild(0), var_45_2)

def onLoadedPaintingPrefabAsync(arg_46_0):
	var_46_0 = arg_46_0.paintingTF
	var_46_1 = arg_46_0.fitterTF
	var_46_2 = arg_46_0.objectOrTransform
	var_46_3 = arg_46_0.paintingName
	var_46_4 = arg_46_0.defaultPaintingName
	var_46_5 = arg_46_0.callback

	if var_46_2 is None or var_0_2[var_46_2] != var_46_3:
		PoolMgr.GetInstance().ReturnPainting(var_46_3, var_46_0)

		return
	else:
		setParent(var_46_0, var_46_1, False)

		var_0_2[var_46_2] = None

		ShipExpressionHelper.SetExpression(var_46_0, var_46_4)

	var_46_6 = findTF(var_46_0, "Touch")

	if var_46_6 is not None:
		setActive(var_46_6, False)

	var_46_7 = findTF(var_46_0, "hx")

	if var_46_7 is not None:
		setActive(var_46_7, HXSet.isHx())

	if var_46_5:
		var_46_5()

def setCommanderPaintingPrefab(arg_47_0, arg_47_1, arg_47_2, arg_47_3):
	var_47_0, var_47_1, var_47_2 = checkPaintingPrefab(arg_47_0, arg_47_1, arg_47_2, arg_47_3)

	def _function(arg_48_0):
		var_48_0 = table(
			paintingTF = arg_48_0,
			fitterTF = var_47_0,
			defaultPaintingName = var_47_2
		)

		onLoadedPaintingPrefab(var_48_0), "commanderpainting/"

	PoolMgr.GetInstance().GetPaintingWithPrefix(var_47_1, False, _function)

def setCommanderPaintingPrefabAsync(arg_49_0, arg_49_1, arg_49_2, arg_49_3, arg_49_4):
	var_49_0, var_49_1, var_49_2 = checkPaintingPrefab(arg_49_0, arg_49_1, arg_49_2, arg_49_4)

	var_0_2[arg_49_0] = var_49_1

	def _function(arg_50_0):
		var_50_0 = table(
			paintingTF = arg_50_0,
			fitterTF = var_49_0,
			objectOrTransform = arg_49_0,
			paintingName = var_49_1,
			defaultPaintingName = var_49_2,
			callback = arg_49_3
		)

		onLoadedPaintingPrefabAsync(var_50_0), "commanderpainting/"

	PoolMgr.GetInstance().GetPaintingWithPrefix(var_49_1, True, _function)

def retCommanderPaintingPrefab(arg_51_0, arg_51_1):
	retPaintingPrefab(arg_51_0, arg_51_1, "commanderpainting/")

def setMetaPaintingPrefab(arg_52_0, arg_52_1, arg_52_2, arg_52_3):
	var_52_0, var_52_1, var_52_2 = checkPaintingPrefab(arg_52_0, arg_52_1, arg_52_2, arg_52_3)

	def _function(arg_53_0):
		var_53_0 = table(
			paintingTF = arg_53_0,
			fitterTF = var_52_0,
			defaultPaintingName = var_52_2
		)

		onLoadedPaintingPrefab(var_53_0), "metapainting/"

	PoolMgr.GetInstance().GetPaintingWithPrefix(var_52_1, False, _function)

def setMetaPaintingPrefabAsync(arg_54_0, arg_54_1, arg_54_2, arg_54_3, arg_54_4):
	var_54_0, var_54_1, var_54_2 = checkPaintingPrefab(arg_54_0, arg_54_1, arg_54_2, arg_54_4)

	var_0_2[arg_54_0] = var_54_1

	def _function(arg_55_0):
		var_55_0 = table(
			paintingTF = arg_55_0,
			fitterTF = var_54_0,
			objectOrTransform = arg_54_0,
			paintingName = var_54_1,
			defaultPaintingName = var_54_2,
			callback = arg_54_3
		)

		onLoadedPaintingPrefabAsync(var_55_0), "metapainting/"

	PoolMgr.GetInstance().GetPaintingWithPrefix(var_54_1, True, _function)

def retMetaPaintingPrefab(arg_56_0, arg_56_1):
	retPaintingPrefab(arg_56_0, arg_56_1, "metapainting/")

def setGuildPaintingPrefab(arg_57_0, arg_57_1, arg_57_2, arg_57_3):
	var_57_0, var_57_1, var_57_2 = checkPaintingPrefab(arg_57_0, arg_57_1, arg_57_2, arg_57_3)

	def _function(arg_58_0):
		var_58_0 = table(
			paintingTF = arg_58_0,
			fitterTF = var_57_0,
			defaultPaintingName = var_57_2
		)

		onLoadedPaintingPrefab(var_58_0), "guildpainting/"

	PoolMgr.GetInstance().GetPaintingWithPrefix(var_57_1, False, _function)

def setGuildPaintingPrefabAsync(arg_59_0, arg_59_1, arg_59_2, arg_59_3, arg_59_4):
	var_59_0, var_59_1, var_59_2 = checkPaintingPrefab(arg_59_0, arg_59_1, arg_59_2, arg_59_4)

	var_0_2[arg_59_0] = var_59_1

	def _function(arg_60_0):
		var_60_0 = table(
			paintingTF = arg_60_0,
			fitterTF = var_59_0,
			objectOrTransform = arg_59_0,
			paintingName = var_59_1,
			defaultPaintingName = var_59_2,
			callback = arg_59_3
		)

		onLoadedPaintingPrefabAsync(var_60_0), "guildpainting/"

	PoolMgr.GetInstance().GetPaintingWithPrefix(var_59_1, True, _function)

def retGuildPaintingPrefab(arg_61_0, arg_61_1):
	retPaintingPrefab(arg_61_0, arg_61_1, "guildpainting/")

def setShopPaintingPrefab(arg_62_0, arg_62_1, arg_62_2, arg_62_3):
	var_62_0, var_62_1, var_62_2 = checkPaintingPrefab(arg_62_0, arg_62_1, arg_62_2, arg_62_3)

	def _function(arg_63_0):
		var_63_0 = table(
			paintingTF = arg_63_0,
			fitterTF = var_62_0,
			defaultPaintingName = var_62_2
		)

		onLoadedPaintingPrefab(var_63_0), "shoppainting/"

	PoolMgr.GetInstance().GetPaintingWithPrefix(var_62_1, False, _function)

def retShopPaintingPrefab(arg_64_0, arg_64_1):
	retPaintingPrefab(arg_64_0, arg_64_1, "shoppainting/")

def setBuildPaintingPrefabAsync(arg_65_0, arg_65_1, arg_65_2, arg_65_3, arg_65_4):
	var_65_0, var_65_1, var_65_2 = checkPaintingPrefab(arg_65_0, arg_65_1, arg_65_2, arg_65_4)

	var_0_2[arg_65_0] = var_65_1

	def _function(arg_66_0):
		var_66_0 = table(
			paintingTF = arg_66_0,
			fitterTF = var_65_0,
			objectOrTransform = arg_65_0,
			paintingName = var_65_1,
			defaultPaintingName = var_65_2,
			callback = arg_65_3
		)

		onLoadedPaintingPrefabAsync(var_66_0), "buildpainting/"

	PoolMgr.GetInstance().GetPaintingWithPrefix(var_65_1, True, _function)

def retBuildPaintingPrefab(arg_67_0, arg_67_1):
	retPaintingPrefab(arg_67_0, arg_67_1, "buildpainting/")

def setColorCount(arg_68_0, arg_68_1, arg_68_2):
	setText(arg_68_0, string.format(arg_68_1 < arg_68_2 and f"<color={COLOR_RED}>d</color>/%d" or "%d/%d", arg_68_1, arg_68_2))

def setColorStr(arg_69_0, arg_69_1):
	return f"<color={arg_69_1}>{arg_69_0}</color>"

def setSizeStr(arg_70_0, arg_70_1):
	var_70_0, var_70_1 = string.gsub(arg_70_0, "[<]size=%d+[>]", f"<size={arg_70_1}>")

	if var_70_1 == 0:
		var_70_0 = "<size={arg_70_1}>{var_70_0}</size>"

	return var_70_0

def getBgm(arg_71_0):
	var_71_0 = pg.voice_bgm[arg_71_0]

	if pg.CriMgr.GetInstance().IsDefaultBGM():
		return var_71_0 and var_71_0.default_bgm or None
	elif var_71_0:
		var_71_1 = var_71_0.special_bgm
		var_71_2 = var_71_0.time

		if var_71_1 and type(var_71_1) == str and len(var_71_1) > 0 and var_71_2 and type(var_71_2) == table:
			var_71_3 = var_71_0.time
			var_71_4 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_71_3[1])
			var_71_5 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_71_3[2])
			var_71_6 = pg.TimeMgr.GetInstance().GetServerTime()

			if var_71_4 <= var_71_6 and var_71_6 <= var_71_5:
				return var_71_1
			else:
				return var_71_0.bgm
		else:
			return var_71_0 and var_71_0.bgm or None
	else:
		return None

def playStory(arg_72_0, arg_72_1):
	pg.NewStoryMgr.GetInstance().Play(arg_72_0, arg_72_1)

def errorMessage(arg_73_0):
	var_73_0 = ERROR_MESSAGE[arg_73_0]

	if var_73_0 == None:
		var_73_0 = f"{ERROR_MESSAGE[9999]}.{arg_73_0}"

	return var_73_0

def errorTip(arg_74_0, arg_74_1, *args):
	var_74_0 = pg.gametip[f"{arg_74_0}_error"]
	var_74_1

	if var_74_0:
		var_74_1 = var_74_0.tip
	else:
		var_74_1 = pg.gametip.common_error.tip

	var_74_2 = f"{arg_74_0}_error_{arg_74_1}"

	if pg.gametip[var_74_2]:
		var_74_3 = i18n(var_74_2, *args)

		return f"{var_74_1}{var_74_3}"
	else:
		var_74_4 = f"common_error_{arg_74_1}"

		if pg.gametip[var_74_4]:
			var_74_5 = i18n(var_74_4, *args)

			return f"{var_74_1}{var_74_5}"
		else:
			var_74_6 = errorMessage(arg_74_1)

			return f"{var_74_1}{arg_74_1}.{var_74_6}"

def colorNumber(arg_75_0, arg_75_1):
	var_75_0 = "@COLOR_SCOPE"
	var_75_1 = table()

	def _function(arg_76_0):
		table.insert(var_75_1, arg_76_0)

		return var_75_0

	arg_75_0 = string.gsub(arg_75_0, "<color=#%x+>", _function)
	arg_75_0 = string.gsub(arg_75_0, "%d+%.?%d*%%*", lambda arg_77_0: f"<color={arg_75_1}>{arg_77_0}</color>")

	if len(var_75_1) > 0:
		var_75_2 = 0

		def _function(arg_78_0):
			var_75_2 = var_75_2 + 1

			return var_75_1[var_75_2]

		return (string.gsub(arg_75_0, var_75_0, _function))
	else:
		return arg_75_0

def getBounds(arg_79_0):
	var_79_0 = LuaHelper.GetWorldCorners(rtf(arg_79_0))
	var_79_1 = Bounds.New(var_79_0[0], Vector3.zero)

	var_79_1.Encapsulate(var_79_0[2])

	return var_79_1

def var_0_3(arg_80_0, arg_80_1):
	arg_80_0.localScale = Vector3.one
	arg_80_0.anchorMin = Vector2.zero
	arg_80_0.anchorMax = Vector2.one
	arg_80_0.offsetMin = Vector2(arg_80_1[1], arg_80_1[2])
	arg_80_0.offsetMax = Vector2(-arg_80_1[3], -arg_80_1[4])

var_0_4 = table(
	frame4_0 = table(
		-8,
		-8.5,
		-8,
		-8
	),
	frame5_0 = table(
		-8,
		-8.5,
		-8,
		-8
	),
	frame4_1 = table(
		-8,
		-8.5,
		-8,
		-8
	),
	frame_design = table(
		-16.5,
		-2.5,
		-3.5,
		-16.5
	),
	frame_skin = table(
		-16.5,
		-2.5,
		-3.5,
		-16.5
	),
	frame_npc = table(
		-4,
		-4,
		-4,
		-4
	),
	frame_store = table(
		-17,
		-3,
		-3,
		-18
	),
	frame_prop = table(
		-11,
		-12,
		-14,
		-14
	),
	frame_prop_meta = table(
		-11,
		-12,
		-14,
		-14
	),
	other = table(
		-2.5,
		-4.5,
		-3,
		-4.5
	)
)

def setFrame(arg_81_0, arg_81_1, arg_81_2):
	arg_81_1 = tostring(arg_81_1)

	var_81_0, var_81_1 = unpack((string.split(arg_81_1, "_")))

	if var_81_1 or tonumber(var_81_0) > 5:
		arg_81_2 = arg_81_2 or f"frame{arg_81_1}"

	GetImageSpriteFromAtlasAsync("weaponframes", "frame", arg_81_0)

	var_81_2 = arg_81_2 and Color.white or Color.NewHex(ItemRarity.Rarity2FrameHexColor(var_81_0 and tonumber(var_81_0) or ItemRarity.Gray))

	setImageColor(arg_81_0, var_81_2)

	var_81_3 = findTF(arg_81_0, "specialFrame")

	if arg_81_2:
		if var_81_3:
			setActive(var_81_3, True)
		else:
			var_81_3 = cloneTplTo(arg_81_0, arg_81_0, "specialFrame")

			removeAllChildren(var_81_3)

		var_0_3(var_81_3, var_0_4[arg_81_2] or var_0_4.other)
		GetImageSpriteFromAtlasAsync("weaponframes", arg_81_2, var_81_3)
	elif var_81_3:
		setActive(var_81_3, False)

def setIconColorful(arg_82_0, arg_82_1, arg_82_2, arg_82_3):
	arg_82_3 = arg_82_3 or table({
		ItemRarity.SSR: table(
			name = "IconColorful",
			active = lambda arg_83_0, arg_83_1: not arg_83_1.noIconColorful and arg_83_0 == ItemRarity.SSR
		)
	})

	var_82_0 = findTF(arg_82_0, "icon_bg/frame")

	for iter_82_0, iter_82_1 in pairs(arg_82_3):
		var_82_1 = iter_82_1.name
		var_82_2 = iter_82_1.active(arg_82_1, arg_82_2)
		var_82_3 = var_82_0.Find(f"{var_82_1}(Clone)")

		if var_82_3:
			setActive(var_82_3, var_82_2)
		elif var_82_2:
			def _function(arg_84_0):
				if arg_82_0 is None or var_82_0.Find(f"{var_82_1}(Clone)"):
					Object.Destroy(arg_84_0)
				else:
					setParent(arg_84_0, var_82_0)
					setActive(arg_84_0, var_82_2)
			LoadAndInstantiateAsync("ui", string.lower(var_82_1), _function)

def setIconStars(arg_85_0, arg_85_1, arg_85_2):
	var_85_0 = findTF(arg_85_0, "icon_bg/startpl")
	var_85_1 = findTF(arg_85_0, "icon_bg/stars")

	if var_85_1 and var_85_0:
		setActive(var_85_1, False)
		setActive(var_85_0, False)

	if not var_85_1 or not arg_85_1:
		return

	for iter_85_0 in range(1, max(arg_85_2, var_85_1.childCount)):
		setActive(iter_85_0 > var_85_1.childCount and cloneTplTo(var_85_0, var_85_1) or var_85_1.GetChild(iter_85_0 - 1), iter_85_0 <= arg_85_2)

	setActive(var_85_1, True)

def var_0_5(arg_86_0, arg_86_1):
	var_86_0 = findTF(arg_86_0, "icon_bg/slv")

	if var_86_0 is not None:
		setActive(var_86_0, arg_86_1 > 0)
		setText(findTF(var_86_0, "Text"), arg_86_1)

def setIconName(arg_87_0, arg_87_1, arg_87_2):
	var_87_0 = findTF(arg_87_0, "name")

	if var_87_0 is not None:
		setText(var_87_0, arg_87_1)
		setTextAlpha(var_87_0, (arg_87_2.hideName or arg_87_2.anonymous) and 0 or 1)

def setIconCount(arg_88_0, arg_88_1):
	var_88_0 = findTF(arg_88_0, "icon_bg/count")

	if var_88_0 is not None:
		setText(var_88_0, arg_88_1 and (type(arg_88_1) != "number" or arg_88_1 > 0) and arg_88_1 or "")

def updateEquipment(arg_89_0, arg_89_1, arg_89_2):
	arg_89_2 = arg_89_2 or table()

	assert arg_89_1, "equipmentVo can not be None."

	var_89_0 = EquipmentRarity.Rarity2Print(arg_89_1.getConfig("rarity"))

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_89_0}", findTF(arg_89_0, "icon_bg"))
	setFrame(findTF(arg_89_0, "icon_bg/frame"), var_89_0)

	var_89_1 = findTF(arg_89_0, "icon_bg/icon")

	var_0_3(var_89_1, table(
		16,
		16,
		16,
		16
	))
	GetImageSpriteFromAtlasAsync(f"equips/{arg_89_1.getConfig("icon")}", "", var_89_1)
	setIconStars(arg_89_0, True, arg_89_1.getConfig("rarity"))
	var_0_5(arg_89_0, arg_89_1.getConfig("level") - 1)
	setIconName(arg_89_0, arg_89_1.getConfig("name"), arg_89_2)
	setIconCount(arg_89_0, arg_89_1.count)
	setIconColorful(arg_89_0, arg_89_1.getConfig("rarity") - 1, arg_89_2)

def updateItem(arg_90_0, arg_90_1, arg_90_2):
	arg_90_2 = arg_90_2 or table()

	var_90_0 = ItemRarity.Rarity2Print(arg_90_1.getConfig("rarity"))

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_90_0}", findTF(arg_90_0, "icon_bg"))

	var_90_1

	if arg_90_1.getConfig("type") == 9:
		var_90_1 = "frame_design"
	elif arg_90_2.frame:
		var_90_1 = arg_90_2.frame

	setFrame(findTF(arg_90_0, "icon_bg/frame"), var_90_0, var_90_1)

	var_90_2 = findTF(arg_90_0, "icon_bg/icon")
	var_90_3 = arg_90_1.icon or arg_90_1.getConfig("icon")

	if arg_90_1.getConfig("type") == Item.LOVE_LETTER_TYPE:
		assert arg_90_1.extra, "without extra data"

		var_90_3 = f"SquareIcon/{ShipGroup.getDefaultSkin(arg_90_1.extra).prefab}"

	GetImageSpriteFromAtlasAsync(var_90_3, "", var_90_2)
	setIconStars(arg_90_0, False)
	setIconName(arg_90_0, arg_90_1.getName(), arg_90_2)
	setIconColorful(arg_90_0, arg_90_1.getConfig("rarity"), arg_90_2)

def updateWorldItem(arg_91_0, arg_91_1, arg_91_2):
	arg_91_2 = arg_91_2 or table()

	var_91_0 = ItemRarity.Rarity2Print(arg_91_1.getConfig("rarity"))

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_91_0}", findTF(arg_91_0, "icon_bg"))
	setFrame(findTF(arg_91_0, "icon_bg/frame"), var_91_0)

	var_91_1 = findTF(arg_91_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(arg_91_1.icon or arg_91_1.getConfig("icon"), "", var_91_1)
	setIconStars(arg_91_0, False)
	setIconName(arg_91_0, arg_91_1.getConfig("name"), arg_91_2)
	setIconColorful(arg_91_0, arg_91_1.getConfig("rarity"), arg_91_2)

def updateWorldCollection(arg_92_0, arg_92_1, arg_92_2):
	arg_92_2 = arg_92_2 or table()

	assert arg_92_1.getConfigTable(), f"world_collection_file_template 和 world_collection_record_template 表中找不到配置. {arg_92_1.id}"

	var_92_0 = arg_92_1.getDropRarity()
	var_92_1 = ItemRarity.Rarity2Print(var_92_0)

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_92_1}", findTF(arg_92_0, "icon_bg"))
	setFrame(findTF(arg_92_0, "icon_bg/frame"), var_92_1)

	var_92_2 = findTF(arg_92_0, "icon_bg/icon")
	var_92_3 = WorldCollectionProxy.GetCollectionType(arg_92_1.id) == WorldCollectionProxy.WorldCollectionType.FILE and "shoucangguangdie" or "shoucangjiaojuan"

	GetImageSpriteFromAtlasAsync(f"props/{var_92_3}", "", var_92_2)
	setIconStars(arg_92_0, False)
	setIconName(arg_92_0, arg_92_1.getName(), arg_92_2)
	setIconColorful(arg_92_0, var_92_0, arg_92_2)

def updateWorldBuff(arg_93_0, arg_93_1, arg_93_2):
	arg_93_2 = arg_93_2 or table()

	var_93_0 = pg.world_SLGbuff_data[arg_93_1]

	assert var_93_0, f"找不到大世界buff配置. {arg_93_1}"

	var_93_1 = ItemRarity.Rarity2Print(ItemRarity.Gray)

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_93_1}", findTF(arg_93_0, "icon_bg"))
	setFrame(findTF(arg_93_0, "icon_bg/frame"), var_93_1)

	var_93_2 = findTF(arg_93_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(f"world/buff/{var_93_0.icon}", "", var_93_2)

	var_93_3 = arg_93_0.Find("icon_bg/stars")

	if var_93_3 is not None:
		setActive(var_93_3, False)

	var_93_4 = findTF(arg_93_0, "name")

	if var_93_4 is not None:
		setText(var_93_4, var_93_0.name)

	var_93_5 = findTF(arg_93_0, "icon_bg/count")

	if var_93_5 is not None:
		SetActive(var_93_5, False)

def updateShip(arg_94_0, arg_94_1, arg_94_2):
	arg_94_2 = arg_94_2 or table()

	var_94_0 = arg_94_1.rarity2bgPrint()
	var_94_1 = arg_94_1.getPainting()

	if arg_94_2.anonymous:
		var_94_0 = "1"
		var_94_1 = "unknown"

	if arg_94_2.unknown_small:
		var_94_1 = "unknown_small"

	var_94_2 = findTF(arg_94_0, "icon_bg/new")

	if var_94_2:
		if arg_94_2.isSkin:
			setActive(var_94_2, not arg_94_2.isTimeLimit and arg_94_2.isNew)
		else:
			setActive(var_94_2, arg_94_1.virgin)

	var_94_3 = findTF(arg_94_0, "icon_bg/timelimit")

	if var_94_3:
		setActive(var_94_3, arg_94_2.isTimeLimit)

	var_94_4 = findTF(arg_94_0, "icon_bg")

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{(arg_94_2.isSkin and "_skin" or var_94_0)}", var_94_4)

	var_94_5 = findTF(arg_94_0, "icon_bg/frame")
	var_94_6

	if arg_94_1.isNpc:
		var_94_6 = "frame_npc"
	elif arg_94_1.ShowPropose():
		var_94_6 = "frame_prop"

		if arg_94_1.isMetaShip():
			var_94_6 = f"{var_94_6}_meta"
	elif arg_94_2.isSkin:
		var_94_6 = "frame_skin"

	setFrame(var_94_5, var_94_0, var_94_6)

	if arg_94_2.gray:
		setGray(var_94_4, True, True)

	var_94_7 = findTF(arg_94_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(f"{(arg_94_2.Q and "QIcon/" or "SquareIcon/")}{var_94_1}", "", var_94_7)

	var_94_8 = findTF(arg_94_0, "icon_bg/lv")

	if var_94_8:
		setActive(var_94_8, not arg_94_1.isNpc)

		if not arg_94_1.isNpc:
			var_94_9 = findTF(var_94_8, "Text")

			if var_94_9 and arg_94_1.level:
				setText(var_94_9, arg_94_1.level)

	var_94_10 = findTF(arg_94_0, "ship_type")

	if var_94_10:
		setActive(var_94_10, True)
		setImageSprite(var_94_10, GetSpriteFromAtlas("shiptype", shipType2print(arg_94_1.getShipType())))

	var_94_11 = var_94_4.Find("npc")

	if var_94_11 is not None:
		if var_94_2 and go(var_94_2).activeSelf:
			setActive(var_94_11, False)
		else:
			setActive(var_94_11, arg_94_1.isActivityNpc())

	var_94_12 = arg_94_0.Find("group_locked")

	if var_94_12:
		setActive(var_94_12, not arg_94_2.isSkin and not getProxy(CollectionProxy).getShipGroup(arg_94_1.groupId))

	setIconStars(arg_94_0, arg_94_2.initStar, arg_94_1.getStar())
	setIconName(arg_94_0, arg_94_2.isSkin and arg_94_1.GetSkinConfig().name or arg_94_1.getName(), arg_94_2)
	setIconColorful(arg_94_0, arg_94_2.isSkin and ItemRarity.Gold or arg_94_1.getRarity() - 1, arg_94_2)

def updateCommander(arg_95_0, arg_95_1, arg_95_2):
	arg_95_2 = arg_95_2 or table()

	var_95_0 = arg_95_1.getDropRarity()
	var_95_1 = ShipRarity.Rarity2Print(var_95_0)
	var_95_2 = arg_95_1.getConfig("painting")

	if arg_95_2.anonymous:
		var_95_1 = 1
		var_95_2 = "unknown"

	var_95_3 = findTF(arg_95_0, "icon_bg")

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{(arg_95_2.isSkin and "-skin" or var_95_1)}", var_95_3)

	var_95_4 = findTF(arg_95_0, "icon_bg/frame")

	setFrame(var_95_4, var_95_1)

	if arg_95_2.gray:
		setGray(var_95_3, True, True)

	var_95_5 = findTF(arg_95_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(f"CommanderIcon/{var_95_2}", "", var_95_5)
	setIconStars(arg_95_0, arg_95_2.initStar, 0)
	setIconName(arg_95_0, arg_95_1.getName(), arg_95_2)

def updateStrategy(arg_96_0, arg_96_1, arg_96_2):
	arg_96_2 = arg_96_2 or table()

	var_96_0 = ItemRarity.Rarity2Print(ItemRarity.Gray)

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_96_0}", findTF(arg_96_0, "icon_bg"))
	setFrame(findTF(arg_96_0, "icon_bg/frame"), var_96_0)

	var_96_1 = findTF(arg_96_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(f"{(arg_96_1.isWorldBuff and "world/buff/" or "strategyicon/")}{arg_96_1.getIcon()}", "", var_96_1)
	setIconStars(arg_96_0, False)
	setIconName(arg_96_0, arg_96_1.getName(), arg_96_2)
	setIconColorful(arg_96_0, ItemRarity.Gray, arg_96_2)

def updateFurniture(arg_97_0, arg_97_1, arg_97_2):
	arg_97_2 = arg_97_2 or table()

	var_97_0 = arg_97_1.getDropRarity()
	var_97_1 = ItemRarity.Rarity2Print(var_97_0)

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_97_1}", findTF(arg_97_0, "icon_bg"))
	setFrame(findTF(arg_97_0, "icon_bg/frame"), var_97_1)

	var_97_2 = findTF(arg_97_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(f"furnitureicon/{arg_97_1.getIcon()}", "", var_97_2)
	setIconStars(arg_97_0, False)
	setIconName(arg_97_0, arg_97_1.getName(), arg_97_2)
	setIconColorful(arg_97_0, var_97_0, arg_97_2)

def updateSpWeapon(arg_98_0, arg_98_1, arg_98_2):
	arg_98_2 = arg_98_2 or table()

	assert arg_98_1, "spWeaponVO can not be None."
	assert isa(arg_98_1, SpWeapon), "spWeaponVO is not Equipment."

	var_98_0 = ItemRarity.Rarity2Print(arg_98_1.GetRarity())

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_98_0}", findTF(arg_98_0, "icon_bg"))
	setFrame(findTF(arg_98_0, "icon_bg/frame"), var_98_0)

	var_98_1 = findTF(arg_98_0, "icon_bg/icon")

	var_0_3(var_98_1, table(
		16,
		16,
		16,
		16
	))
	GetImageSpriteFromAtlasAsync(arg_98_1.GetIconPath(), "", var_98_1)
	setIconStars(arg_98_0, True, arg_98_1.GetRarity())
	var_0_5(arg_98_0, arg_98_1.GetLevel() - 1)
	setIconName(arg_98_0, arg_98_1.GetName(), arg_98_2)
	setIconCount(arg_98_0, arg_98_1.count)
	setIconColorful(arg_98_0, arg_98_1.GetRarity(), arg_98_2)

def UpdateSpWeaponSlot(arg_99_0, arg_99_1, arg_99_2):
	var_99_0 = ItemRarity.Rarity2Print(arg_99_1.GetRarity())

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_99_0}", findTF(arg_99_0, "Icon/Mask/icon_bg"))

	var_99_1 = findTF(arg_99_0, "Icon/Mask/icon_bg/icon")

	arg_99_2 = arg_99_2 or table(
		16,
		16,
		16,
		16
	)

	var_0_3(var_99_1, arg_99_2)
	GetImageSpriteFromAtlasAsync(arg_99_1.GetIconPath(), "", var_99_1)

	var_99_2 = arg_99_1.GetLevel() - 1
	var_99_3 = findTF(arg_99_0, "Icon/LV")

	setActive(var_99_3, var_99_2 > 0)
	setText(findTF(var_99_3, "Text"), var_99_2)

def updateDorm3dFurniture(arg_100_0, arg_100_1, arg_100_2):
	arg_100_2 = arg_100_2 or table()

	var_100_0 = arg_100_1.getDropRarity()
	var_100_1 = ItemRarity.Rarity2Print(var_100_0)

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_100_1}", findTF(arg_100_0, "icon_bg"))
	setFrame(findTF(arg_100_0, "icon_bg/frame"), var_100_1)

	var_100_2 = findTF(arg_100_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(f"furnitureicon/{arg_100_1.getIcon()}", "", var_100_2)
	setIconStars(arg_100_0, False)
	setIconName(arg_100_0, arg_100_1.getName(), arg_100_2)
	setIconColorful(arg_100_0, var_100_0, arg_100_2)

def updateDorm3dGift(arg_101_0, arg_101_1, arg_101_2):
	arg_101_2 = arg_101_2 or table()

	var_101_0 = arg_101_1.getDropRarity()
	var_101_1 = ItemRarity.Rarity2Print(var_101_0) or ItemRarity.Gray

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_101_1}", arg_101_0.Find("icon_bg"))
	setFrame(arg_101_0.Find("icon_bg/frame"), var_101_1)

	var_101_2 = arg_101_0.Find("icon_bg/icon")

	GetImageSpriteFromAtlasAsync(f"furnitureicon/{arg_101_1.getIcon()}", "", var_101_2)
	setIconStars(arg_101_0, False)
	setIconName(arg_101_0, arg_101_1.getName(), arg_101_2)
	setIconColorful(arg_101_0, var_101_0, arg_101_2)

def updateDorm3dSkin(arg_102_0, arg_102_1, arg_102_2):
	arg_102_2 = arg_102_2 or table()

	var_102_0 = arg_102_1.getDropRarity()
	var_102_1 = ItemRarity.Rarity2Print(var_102_0) or ItemRarity.Gray

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_102_1}", arg_102_0.Find("icon_bg"))
	setFrame(arg_102_0.Find("icon_bg/frame"), var_102_1)

	var_102_2 = arg_102_0.Find("icon_bg/icon")

	setIconStars(arg_102_0, False)
	setIconName(arg_102_0, arg_102_1.getName(), arg_102_2)
	setIconColorful(arg_102_0, var_102_0, arg_102_2)

def updateDorm3dIcon(arg_103_0, arg_103_1):
	var_103_0 = arg_103_1.getConfig("rarity")

	GetImageSpriteFromAtlasAsync("weaponframes", f"dorm3d_{ItemRarity.Rarity2Print(var_103_0)}", arg_103_0)

	var_103_1 = arg_103_0.Find("icon")

	setText(arg_103_0.Find("count/Text"), f"x{arg_103_1.count}")
	setText(arg_103_0.Find("name/Text"), arg_103_1.getName())



def findCullAndClipWorldRect(arg_104_0):
	if len(arg_104_0) == 0:
		return False

	var_104_0 = arg_104_0[1].canvasRect

	for iter_104_0 in range(1, len(arg_104_0)):
		var_104_0 = rectIntersect(var_104_0, arg_104_0[iter_104_0].canvasRect)

	if var_104_0.width <= 0 or var_104_0.height <= 0:
		return False

	var_0_6 = var_0_6 or GameObject.Find("UICamera/Canvas").transform

	var_104_1 = var_0_6.TransformPoint(Vector3(var_104_0.x, var_104_0.y, 0))
	var_104_2 = var_0_6.TransformPoint(Vector3(var_104_0.x + var_104_0.width, var_104_0.y + var_104_0.height, 0))

	return True, Vector4(var_104_1.x, var_104_1.y, var_104_2.x, var_104_2.y)

def rectIntersect(arg_105_0, arg_105_1):
	var_105_0 = math.max(arg_105_0.x, arg_105_1.x)
	var_105_1 = math.min(arg_105_0.x + arg_105_0.width, arg_105_1.x + arg_105_1.width)
	var_105_2 = math.max(arg_105_0.y, arg_105_1.y)
	var_105_3 = math.min(arg_105_0.y + arg_105_0.height, arg_105_1.y + arg_105_1.height)

	if var_105_0 <= var_105_1 and var_105_2 <= var_105_3:
		return UnityEngine.Rect.New(var_105_0, var_105_2, var_105_1 - var_105_0, var_105_3 - var_105_2)

	return UnityEngine.Rect.New(0, 0, 0, 0)

def getDropInfo(arg_106_0):
	var_106_0 = table()

	for iter_106_0, iter_106_1 in ipairs(arg_106_0):
		var_106_1 = Drop.Create(iter_106_1)

		var_106_1.count = var_106_1.count or 1

		if var_106_1.type == DROP_TYPE_EMOJI:
			table.insert(var_106_0, var_106_1.getName())
		else:
			table.insert(var_106_0, f"{var_106_1.getName()}x{var_106_1.count}")

	return table.concat(var_106_0, "、")

def updateDrop(arg_107_0, arg_107_1, arg_107_2):
	Drop.Change(arg_107_1)

	arg_107_2 = arg_107_2 or table()

	var_107_0 = table(
		table(
			"icon_bg/slv"
		),
		table(
			"icon_bg/frame/specialFrame"
		),
		table(
			"ship_type",
			DROP_TYPE_SHIP
		),
		table(
			"icon_bg/new",
			DROP_TYPE_SHIP
		),
		table(
			"icon_bg/npc",
			DROP_TYPE_SHIP
		),
		table(
			"group_locked",
			DROP_TYPE_SHIP
		)
	)
	var_107_1

	for iter_107_0, iter_107_1 in ipairs(var_107_0):
		var_107_2 = arg_107_0.Find(iter_107_1[1])

		if arg_107_1.type != iter_107_1[2] and var_107_2 is not None:
			setActive(var_107_2, False)

	arg_107_0.Find("icon_bg/frame").GetComponent(typeof(Image)).enabled = True

	setIconColorful(arg_107_0, arg_107_1.getDropRarity(), arg_107_2, table({
		ItemRarity.Gold: table(
			name = "Item_duang5",
			active = lambda arg_108_0, arg_108_1: arg_108_1.fromAwardLayer and arg_108_0 >= ItemRarity.Gold
		)
	}))
	var_0_3(findTF(arg_107_0, "icon_bg/icon"), table(
		2,
		2,
		2,
		2
	))
	arg_107_1.UpdateDropTpl(arg_107_0, arg_107_2)
	setIconCount(arg_107_0, arg_107_2.count or arg_107_1.getCount())

def updateBuff(arg_109_0, arg_109_1, arg_109_2):
	arg_109_2 = arg_109_2 or table()

	var_109_0 = ItemRarity.Rarity2Print(ItemRarity.Gray)

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_109_0}", findTF(arg_109_0, "icon_bg"))

	var_109_1 = pg.benefit_buff_template[arg_109_1]

	setFrame(findTF(arg_109_0, "icon_bg/frame"), var_109_0)
	setText(findTF(arg_109_0, "icon_bg/count"), 1)

	var_109_2 = findTF(arg_109_0, "icon_bg/icon")
	var_109_3 = var_109_1.icon

	GetImageSpriteFromAtlasAsync(var_109_3, "", var_109_2)
	setIconStars(arg_109_0, False)
	setIconName(arg_109_0, var_109_1.name, arg_109_2)
	setIconColorful(arg_109_0, ItemRarity.Gold, arg_109_2)

def updateAttire(arg_110_0, arg_110_1, arg_110_2, arg_110_3):
	var_110_0 = 4

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_110_0}", findTF(arg_110_0, "icon_bg"))
	setFrame(findTF(arg_110_0, "icon_bg/frame"), var_110_0)

	var_110_1 = findTF(arg_110_0, "icon_bg/icon")
	var_110_2

	if arg_110_1 == AttireConst.TYPE_CHAT_FRAME:
		var_110_2 = "chat_frame"
	elif arg_110_1 == AttireConst.TYPE_ICON_FRAME:
		var_110_2 = "icon_frame"

	GetImageSpriteFromAtlasAsync(f"Props/{var_110_2}", "", var_110_1)
	setIconName(arg_110_0, arg_110_2.name, arg_110_3)

def updateEmoji(arg_111_0, arg_111_1, arg_111_2):
	var_111_0 = findTF(arg_111_0, "icon_bg/icon")
	var_111_1 = "icon_emoji"

	GetImageSpriteFromAtlasAsync(f"Props/{var_111_1}", "", var_111_0)

	var_111_2 = 4

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_111_2}", findTF(arg_111_0, "icon_bg"))
	setFrame(findTF(arg_111_0, "icon_bg/frame"), var_111_2)
	setIconName(arg_111_0, arg_111_1.name, arg_111_2)

def updateEquipmentSkin(arg_112_0, arg_112_1, arg_112_2):
	arg_112_2 = arg_112_2 or table()

	var_112_0 = EquipmentRarity.Rarity2Print(arg_112_1.rarity)

	GetImageSpriteFromAtlasAsync("weaponframes", f"bg{var_112_0}", findTF(arg_112_0, "icon_bg"))
	setFrame(findTF(arg_112_0, "icon_bg/frame"), var_112_0, "frame_skin")

	var_112_1 = findTF(arg_112_0, "icon_bg/icon")

	GetImageSpriteFromAtlasAsync(f"equips/{arg_112_1.icon}", "", var_112_1)
	setIconStars(arg_112_0, False)
	setIconName(arg_112_0, arg_112_1.name, arg_112_2)
	setIconCount(arg_112_0, arg_112_1.count)
	setIconColorful(arg_112_0, arg_112_1.rarity - 1, arg_112_2)

def NoPosMsgBox(arg_113_0, arg_113_1, arg_113_2, arg_113_3):
	var_113_0
	var_113_1 = table()

	if arg_113_1:
		table.insert(var_113_1, table(
			text = "text_noPos_clear",
			atuoClose = True,
			onCallback = arg_113_1
		))

	if arg_113_2:
		table.insert(var_113_1, table(
			text = "text_noPos_buy",
			atuoClose = True,
			onCallback = arg_113_2
		))

	if arg_113_3:
		table.insert(var_113_1, table(
			text = "text_noPos_intensify",
			atuoClose = True,
			onCallback = arg_113_3
		))

	pg.MsgboxMgr.GetInstance().ShowMsgBox(table(
		hideYes = True,
		hideNo = True,
		content = arg_113_0,
		custom = var_113_1,
		weight = LayerWeightConst.TOP_LAYER
	))

def openDestroyEquip():
	if pg.m02.hasMediator(EquipmentMediator.__cname):
		var_114_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(EquipmentMediator)

		if var_114_0 and var_114_0.data.shipId:
			pg.m02.sendNotification(GAME.REMOVE_LAYERS, table(
				context = var_114_0
			))
		else:
			pg.m02.sendNotification(EquipmentMediator.BATCHDESTROY_MODE)

			return

	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.EQUIPSCENE, table(
		warp = StoreHouseConst.WARP_TO_WEAPON,
		mode = StoreHouseConst.DESTROY
	))

def OpenSpWeaponPage():
	if pg.m02.hasMediator(EquipmentMediator.__cname):
		var_115_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(EquipmentMediator)

		if var_115_0 and var_115_0.data.shipId:
			pg.m02.sendNotification(GAME.REMOVE_LAYERS, table(
				context = var_115_0
			))
		else:
			pg.m02.sendNotification(EquipmentMediator.SWITCH_TO_SPWEAPON_PAGE)

			return

	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.EQUIPSCENE, table(
		warp = StoreHouseConst.WARP_TO_WEAPON,
		mode = StoreHouseConst.SPWEAPON
	))

def openDockyardClear():
	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, table(
		blockLock = True,
		mode = DockyardScene.MODE_DESTROY,
		leftTopInfo = i18n("word_destroy"),
		selectedMax = getGameset("ship_select_limit")[1],
		onShip = ShipStatus.canDestroyShip,
		ignoredIds = pg.ShipFlagMgr.GetInstance().FilterShips(table(
			isActivityNpc = True
		))
	))

def openDockyardIntensify():
	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, table(
		mode = DockyardScene.MODE_OVERVIEW,
		onClick = lambda arg_118_0, arg_118_1: pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, table(
				page = 3,
				shipId = arg_118_0.id,
				shipVOs = arg_118_1
			))
	))

def GoShoppingMsgBox(arg_119_0, arg_119_1, arg_119_2):
	if arg_119_2:
		var_119_0 = ""

		for iter_119_0, iter_119_1 in ipairs(arg_119_2):
			var_119_1 = Item.getConfigData(iter_119_1[1])

			var_119_0 = f"{var_119_0}{i18n(iter_119_1[1] == 59001 and "text_noRes_info_tip" or "text_noRes_info_tip2", var_119_1.name, iter_119_1[2])}"

			if iter_119_0 < len(arg_119_2):
				var_119_0 = f"{var_119_0}{i18n("text_noRes_info_tip_link")}"

		if var_119_0 != "":
			arg_119_0 = f"{arg_119_0}\n{i18n("text_noRes_tip", var_119_0)}"

	pg.MsgboxMgr.GetInstance().ShowMsgBox(table(
		content = arg_119_0,
		weight = LayerWeightConst.SECOND_LAYER,
		onYes = lambda: gotoChargeScene(arg_119_1, arg_119_2)
	))

def shoppingBatch(arg_121_0, arg_121_1, arg_121_2, arg_121_3, arg_121_4):
	var_121_0 = pg.shop_template[arg_121_0]

	assert var_121_0, f"shop_template中找不到商品id：{arg_121_0}"

	var_121_1 = getProxy(PlayerProxy).getData()[id2res(var_121_0.resource_type)]
	var_121_2 = arg_121_1.price or var_121_0.resource_num
	var_121_3 = int(var_121_1 / var_121_2)

	var_121_3 = var_121_3 <= 0 and 1 or var_121_3
	var_121_3 = arg_121_2 != None and arg_121_2 < var_121_3 and arg_121_2 or var_121_3

	var_121_4 = True
	var_121_5 = 1

	if var_121_0 != None and arg_121_1.id:
		print(var_121_3 * var_121_0.num, "--", var_121_3)
		assert Item.getConfigData(arg_121_1.id), "item config should be existence"

		var_121_6 = Item.New(table(
			id = arg_121_1.id
		)).getConfig("name")

		def _numUpdate(arg_122_0, arg_122_1):
			var_121_5 = math.floor(arg_122_1 / var_121_0.num)

			var_122_0 = var_121_5 * var_121_2

			if var_122_0 > var_121_1:
				setText(arg_122_0, i18n(arg_121_3, var_122_0, arg_122_1, COLOR_RED, var_121_6))

				var_121_4 = False
			else:
				setText(arg_122_0, i18n(arg_121_3, var_122_0, arg_122_1, COLOR_GREEN, var_121_6))

				var_121_4 = True

		def _onYes():
			if var_121_4:
				pg.m02.sendNotification(GAME.SHOPPING, table(
					id = arg_121_0,
					count = var_121_5
				))
			elif arg_121_4:
				pg.TipsMgr.GetInstance().ShowTips(i18n(arg_121_4))
			else:
				pg.TipsMgr.GetInstance().ShowTips(i18n("main_playerInfoLayer_error_changeNameNoGem"))

		pg.MsgboxMgr.GetInstance().ShowMsgBox(table(
			needCounter = True,
			type = MSGBOX_TYPE_SINGLE_ITEM,
			drop = table(
				type = DROP_TYPE_ITEM,
				id = arg_121_1.id
			),
			addNum = var_121_0.num,
			maxNum = var_121_3 * var_121_0.num,
			defaultNum = var_121_0.num,
			numUpdate = _numUpdate,
			onYes = _onYes
		))

def gotoChargeScene(arg_124_0, arg_124_1):
	var_124_0 = getProxy(ContextProxy)
	var_124_1 = getProxy(ContextProxy).getCurrentContext()

	if instanceof(var_124_1.mediator, ChargeMediator):
		var_124_1.mediator.getViewComponent().switchSubViewByTogger(arg_124_0)
	else:
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.CHARGE, table(
			wrap = arg_124_0 or ChargeScene.TYPE_ITEM,
			noRes = arg_124_1
		))

def clearDrop(arg_125_0):
	var_125_0 = findTF(arg_125_0, "icon_bg")
	var_125_1 = findTF(arg_125_0, "icon_bg/frame")
	var_125_2 = findTF(arg_125_0, "icon_bg/icon")
	var_125_3 = findTF(arg_125_0, "icon_bg/icon/icon")

	clearImageSprite(var_125_0)
	clearImageSprite(var_125_1)
	clearImageSprite(var_125_2)

	if var_125_3:
		clearImageSprite(var_125_3)

var_0_7 = table(
	red = Color.New(1, 0.25, 0.25),
	blue = Color.New(0.11, 0.55, 0.64),
	yellow = Color.New(0.92, 0.52, 0)
)

def updateSkill(arg_126_0, arg_126_1, arg_126_2, arg_126_3):
	var_126_0 = findTF(arg_126_0, "skill")
	var_126_1 = findTF(arg_126_0, "lock")
	var_126_2 = findTF(arg_126_0, "unknown")

	if arg_126_1:
		setActive(var_126_0, True)
		setActive(var_126_2, False)
		setActive(var_126_1, not arg_126_2)
		LoadImageSpriteAsync(f"skillicon/{arg_126_1.icon}", findTF(var_126_0, "icon"))

		var_126_3 = arg_126_1.color or "blue"

		setText(findTF(var_126_0, "name"), shortenString(getSkillName(arg_126_1.id), arg_126_3 or 8))

		var_126_4 = findTF(var_126_0, "level")

		setText(var_126_4, f"LEVEL. {(arg_126_2 and arg_126_2.level or "??")}")
		setTextColor(var_126_4, var_0_7[var_126_3])
	else:
		setActive(var_126_0, False)
		setActive(var_126_2, True)
		setActive(var_126_1, False)

var_0_8 = True

def onBackButton(arg_127_0, arg_127_1, arg_127_2, arg_127_3):
	var_127_0 = GetOrAddComponent(arg_127_1, "UILongPressTrigger")

	assert arg_127_2, "callback should exist"

	var_127_0.longPressThreshold = defaultValue(arg_127_3, 1)

	def var_127_1(arg_128_0):
		def _function():
			if var_0_8:
				pg.CriMgr.GetInstance().PlaySoundEffect_V3(SOUND_BACK)

			var_129_0, var_129_1 = arg_127_2()

			if var_129_0:
				arg_128_0(var_129_1)

		return _function

	var_127_2 = var_127_0.onReleased

	pg.DelegateInfo.Add(arg_127_0, var_127_2)
	var_127_2.RemoveAllListeners()
	var_127_2.AddListener(var_127_1(lambda arg_130_0: arg_130_0.emit(BaseUI.ON_BACK)))

	var_127_3 = var_127_0.onLongPressed

	pg.DelegateInfo.Add(arg_127_0, var_127_3)
	var_127_3.RemoveAllListeners()
	var_127_3.AddListener(var_127_1(lambda arg_131_0: arg_131_0.emit(BaseUI.ON_HOME)))

def GetZeroTime():
	return pg.TimeMgr.GetInstance().GetNextTime(0, 0, 0)

def GetHalfHour():
	return pg.TimeMgr.GetInstance().GetNextTime(0, 0, 0, 1800)

def GetNextHour(arg_134_0):
	var_134_0 = pg.TimeMgr.GetInstance().GetServerTime()
	var_134_1, var_134_2 = pg.TimeMgr.GetInstance().parseTimeFrom(var_134_0)

	return var_134_1 * 86400 + (var_134_2 + arg_134_0) * 3600

def GetPerceptualSize(arg_135_0):
	def var_135_0(arg_136_0):
		if not arg_136_0:
			return 0, 1
		if arg_136_0 > 240:
			return 4, 1
		if arg_136_0 > 225:
			return 3, 1
		if arg_136_0 > 192:
			return 2, 1
		if arg_136_0 < 126:
			return 1, 0.5
		return 1, 1

	if type(arg_135_0) == "number":
		return var_135_0(arg_135_0)

	var_135_1 = 1
	var_135_2 = 0
	var_135_3 = 0
	var_135_4 = len(arg_135_0)

	while var_135_1 <= var_135_4:
		var_135_5 = string.byte(arg_135_0, var_135_1)
		var_135_6, var_135_7 = var_135_0(var_135_5)

		var_135_1 = var_135_1 + var_135_6
		var_135_2 = var_135_2 + var_135_7

	return var_135_2

def shortenString(arg_137_0, arg_137_1):
	var_137_0 = 1
	var_137_1 = 0
	var_137_2 = 0
	var_137_3 = len(arg_137_0)

	while var_137_0 <= var_137_3:
		var_137_4 = string.byte(arg_137_0, var_137_0)
		var_137_5, var_137_6 = GetPerceptualSize(var_137_4)

		var_137_0 = var_137_0 + var_137_5
		var_137_1 = var_137_1 + var_137_6

		if arg_137_1 <= math.ceil(var_137_1):
			var_137_2 = var_137_0

			break

	if var_137_2 == 0 or var_137_3 < var_137_2:
		return arg_137_0

	return string.sub(arg_137_0, 1, var_137_2 - 1) + ".."

def shouldShortenString(arg_138_0, arg_138_1):
	var_138_0 = 1
	var_138_1 = 0
	var_138_2 = 0
	var_138_3 = len(arg_138_0)

	while var_138_0 <= var_138_3:
		var_138_4 = string.byte(arg_138_0, var_138_0)
		var_138_5, var_138_6 = GetPerceptualSize(var_138_4)

		var_138_0 = var_138_0 + var_138_5
		var_138_1 = var_138_1 + var_138_6

		if arg_138_1 <= math.ceil(var_138_1):
			var_138_2 = var_138_0

			break

	if var_138_2 == 0 or var_138_3 < var_138_2:
		return False

	return True

def nameValidityCheck(arg_139_0, arg_139_1, arg_139_2, arg_139_3):
	var_139_0 = True
	var_139_1, var_139_2 = utf8_to_unicode(arg_139_0)
	var_139_3 = filterEgyUnicode(filterSpecChars(arg_139_0))
	var_139_4 = wordVer(arg_139_0)

	if not checkSpaceValid(arg_139_0):
		pg.TipsMgr.GetInstance().ShowTips(i18n(arg_139_3[1]))

		var_139_0 = False
	elif var_139_4 > 0 or var_139_3 != arg_139_0:
		pg.TipsMgr.GetInstance().ShowTips(i18n(arg_139_3[4]))

		var_139_0 = False
	elif var_139_2 < arg_139_1:
		pg.TipsMgr.GetInstance().ShowTips(i18n(arg_139_3[2]))

		var_139_0 = False
	elif arg_139_2 < var_139_2:
		pg.TipsMgr.GetInstance().ShowTips(i18n(arg_139_3[3]))

		var_139_0 = False

	return var_139_0

def checkSpaceValid(arg_140_0):
	if PLATFORM_CODE == PLATFORM_US:
		return True

	var_140_0 = string.gsub(arg_140_0, " ", "")

	return arg_140_0 == string.gsub(var_140_0, "　", "")

def filterSpecChars(arg_141_0):
	var_141_0 = table()
	var_141_1 = 0
	var_141_2 = 0
	var_141_3 = 0
	var_141_4 = 1

	while var_141_4 <= len(arg_141_0):
		var_141_5 = string.byte(arg_141_0, var_141_4)

		if not var_141_5:
			break

		if var_141_5 >= 48 and var_141_5 <= 57 or var_141_5 >= 65 and var_141_5 <= 90 or var_141_5 == 95 or var_141_5 >= 97 and var_141_5 <= 122:
			table.insert(var_141_0, string.char(var_141_5))
		elif var_141_5 >= 228 and var_141_5 <= 233:
			var_141_6 = string.byte(arg_141_0, var_141_4 + 1)
			var_141_7 = string.byte(arg_141_0, var_141_4 + 2)

			if var_141_6 and var_141_7 and var_141_6 >= 128 and var_141_6 <= 191 and var_141_7 >= 128 and var_141_7 <= 191:
				var_141_4 = var_141_4 + 2

				table.insert(var_141_0, string.char(var_141_5, var_141_6, var_141_7))

				var_141_1 = var_141_1 + 1
		elif var_141_5 == 45 or var_141_5 == 40 or var_141_5 == 41:
			table.insert(var_141_0, string.char(var_141_5))
		elif var_141_5 == 194:
			var_141_8 = string.byte(arg_141_0, var_141_4 + 1)

			if var_141_8 == 183:
				var_141_4 = var_141_4 + 1

				table.insert(var_141_0, string.char(var_141_5, var_141_8))

				var_141_1 = var_141_1 + 1
		elif var_141_5 == 239:
			var_141_9 = string.byte(arg_141_0, var_141_4 + 1)
			var_141_10 = string.byte(arg_141_0, var_141_4 + 2)

			if var_141_9 == 188 and (var_141_10 == 136 or var_141_10 == 137):
				var_141_4 = var_141_4 + 2

				table.insert(var_141_0, string.char(var_141_5, var_141_9, var_141_10))

				var_141_1 = var_141_1 + 1
		elif var_141_5 == 206 or var_141_5 == 207:
			var_141_11 = string.byte(arg_141_0, var_141_4 + 1)

			if var_141_5 == 206 and var_141_11 >= 177 or var_141_5 == 207 and var_141_11 <= 134:
				var_141_4 = var_141_4 + 1

				table.insert(var_141_0, string.char(var_141_5, var_141_11))

				var_141_1 = var_141_1 + 1
		elif var_141_5 == 227 and PLATFORM_CODE == PLATFORM_JP:
			var_141_12 = string.byte(arg_141_0, var_141_4 + 1)
			var_141_13 = string.byte(arg_141_0, var_141_4 + 2)

			if var_141_12 and var_141_13 and var_141_12 > 128 and var_141_12 <= 191 and var_141_13 >= 128 and var_141_13 <= 191:
				var_141_4 = var_141_4 + 2

				table.insert(var_141_0, string.char(var_141_5, var_141_12, var_141_13))

				var_141_2 = var_141_2 + 1
		elif var_141_5 >= 224 and PLATFORM_CODE == PLATFORM_KR:
			var_141_14 = string.byte(arg_141_0, var_141_4 + 1)
			var_141_15 = string.byte(arg_141_0, var_141_4 + 2)

			if var_141_14 and var_141_15 and var_141_14 >= 128 and var_141_14 <= 191 and var_141_15 >= 128 and var_141_15 <= 191:
				var_141_4 = var_141_4 + 2

				table.insert(var_141_0, string.char(var_141_5, var_141_14, var_141_15))

				var_141_3 = var_141_3 + 1
		elif PLATFORM_CODE == PLATFORM_US:
			if var_141_4 != 1 and var_141_5 == 32 and string.byte(arg_141_0, var_141_4 + 1) != 32:
				table.insert(var_141_0, string.char(var_141_5))

			if var_141_5 >= 192 and var_141_5 <= 223:
				var_141_16 = string.byte(arg_141_0, var_141_4 + 1)

				var_141_4 = var_141_4 + 1

				if var_141_5 == 194 and var_141_16 and var_141_16 >= 128:
					table.insert(var_141_0, string.char(var_141_5, var_141_16))
				elif var_141_5 == 195 and var_141_16 and var_141_16 <= 191:
					table.insert(var_141_0, string.char(var_141_5, var_141_16))

			if var_141_5 == 195:
				var_141_17 = string.byte(arg_141_0, var_141_4 + 1)

				if var_141_17 == 188:
					table.insert(var_141_0, string.char(var_141_5, var_141_17))

		var_141_4 = var_141_4 + 1

	return table.concat(var_141_0), var_141_1 + var_141_2 + var_141_3

def filterEgyUnicode(arg_142_0):
	arg_142_0 = string.gsub(arg_142_0, "\xF0\x93[\x80-\x8F][\x80-\xBF]", "")
	arg_142_0 = string.gsub(arg_142_0, "\xF0\x93\x90[\x80-\xAF]", "")

	return arg_142_0

def shiftPanel(arg_143_0, arg_143_1, arg_143_2, arg_143_3, arg_143_4, arg_143_5, arg_143_6, arg_143_7, arg_143_8):
	arg_143_3 = arg_143_3 or 0.2

	if arg_143_5:
		LeanTween.cancel(go(arg_143_0))

	var_143_0 = rtf(arg_143_0)

	arg_143_1 = arg_143_1 or var_143_0.anchoredPosition.x
	arg_143_2 = arg_143_2 or var_143_0.anchoredPosition.y

	var_143_1 = LeanTween.move(var_143_0, Vector3(arg_143_1, arg_143_2, 0), arg_143_3)

	arg_143_7 = arg_143_7 or LeanTweenType.easeInOutSine

	var_143_1.setEase(arg_143_7)

	if arg_143_4:
		var_143_1.setDelay(arg_143_4)

	if arg_143_6:
		GetOrAddComponent(arg_143_0, "CanvasGroup").blocksRaycasts = False

	def _function():
		if arg_143_8:
			arg_143_8()

		if arg_143_6:
			GetOrAddComponent(arg_143_0, "CanvasGroup").blocksRaycasts = True

	var_143_1.setOnComplete(System.Action(_function))

	return var_143_1

def TweenValue(arg_145_0, arg_145_1, arg_145_2, arg_145_3, arg_145_4, arg_145_5, arg_145_6, arg_145_7):
	def _function(arg_146_0):
		if arg_145_5:
			arg_145_5(arg_146_0)
	def _function2():
		if arg_145_6:
			arg_145_6()
	var_145_0 = LeanTween.value(go(arg_145_0), arg_145_1, arg_145_2, arg_145_3).setOnUpdate(System.Action_float(_function)).setOnComplete(System.Action(_function2)).setDelay(arg_145_4 or 0)

	if arg_145_7 and arg_145_7 > 0:
		var_145_0.setRepeat(arg_145_7)

	return var_145_0

def rotateAni(arg_148_0, arg_148_1, arg_148_2):
	return LeanTween.rotate(rtf(arg_148_0), 360 * arg_148_1, arg_148_2).setLoopClamp()

def blinkAni(arg_149_0, arg_149_1, arg_149_2, arg_149_3):
	return LeanTween.alpha(rtf(arg_149_0), arg_149_3 or 0, arg_149_1).setEase(LeanTweenType.easeInOutSine).setLoopPingPong(arg_149_2 or 0)

def scaleAni(arg_150_0, arg_150_1, arg_150_2, arg_150_3):
	return LeanTween.scale(rtf(arg_150_0), arg_150_3 or 0, arg_150_1).setLoopPingPong(arg_150_2 or 0)

def floatAni(arg_151_0, arg_151_1, arg_151_2, arg_151_3):
	var_151_0 = arg_151_0.localPosition.y + arg_151_1

	return LeanTween.moveY(rtf(arg_151_0), var_151_0, arg_151_2).setLoopPingPong(arg_151_3 or 0)


def tostring(arg_152_0):
	if arg_152_0 == None:
		return "None"

	var_152_0 = str(arg_152_0)

	if var_152_0 == None:
		if type(arg_152_0) == table:
			return "table()"

		return " ~None"

	return var_152_0

def wordVer(arg_153_0, arg_153_1):
	if arg_153_0.match(arg_153_0, ChatConst.EmojiCodeMatch):
		return 0, arg_153_0

	arg_153_1 = arg_153_1 or table()

	var_153_0 = filterEgyUnicode(arg_153_0)

	if len(var_153_0) != len(arg_153_0):
		if arg_153_1.isReplace:
			arg_153_0 = var_153_0
		else:
			return 1

	var_153_1 = wordSplit(arg_153_0)
	var_153_2 = pg.word_template
	var_153_3 = pg.word_legal_template

	arg_153_1.isReplace = arg_153_1.isReplace or False
	arg_153_1.replaceWord = arg_153_1.replaceWord or "*"

	var_153_4 = len(var_153_1)
	var_153_5 = 1
	var_153_6 = ""
	var_153_7 = 0

	while var_153_5 <= var_153_4:
		var_153_8, var_153_9, var_153_10 = wordLegalMatch(var_153_1, var_153_3, var_153_5)

		if var_153_8:
			var_153_5 = var_153_9
			var_153_6 = f"{var_153_6}{var_153_10}"
		else:
			var_153_11, var_153_12, var_153_13 = wordVerMatch(var_153_1, var_153_2, arg_153_1, var_153_5, "", False, var_153_5, "")

			if var_153_11:
				var_153_5 = var_153_12
				var_153_7 = var_153_7 + 1

				if arg_153_1.isReplace:
					var_153_6 = f"{var_153_6}{var_153_13}"
			else:
				if arg_153_1.isReplace:
					var_153_6 = f"{var_153_6}{var_153_1[var_153_5]}"

				var_153_5 = var_153_5 + 1

	if arg_153_1.isReplace:
		return var_153_7, var_153_6
	else:
		return var_153_7

def wordLegalMatch(arg_154_0, arg_154_1, arg_154_2, arg_154_3, arg_154_4):
	if arg_154_2 > len(arg_154_0):
		return arg_154_3, arg_154_2, arg_154_4

	var_154_0 = arg_154_0[arg_154_2]
	var_154_1 = arg_154_1[var_154_0]

	arg_154_4 = arg_154_4 == None and "" or arg_154_4

	if var_154_1:
		if var_154_1.this:
			return wordLegalMatch(arg_154_0, var_154_1, arg_154_2 + 1, True, f"{arg_154_4}{var_154_0}")
		else:
			return wordLegalMatch(arg_154_0, var_154_1, arg_154_2 + 1, False, f"{arg_154_4}{var_154_0}")
	else:
		return arg_154_3, arg_154_2, arg_154_4

var_0_10 = string.byte("a")
var_0_11 = string.byte("z")
var_0_12 = string.byte("A")
var_0_13 = string.byte("Z")

def var_0_14(arg_155_0):
	if not arg_155_0:
		return arg_155_0

	var_155_0 = string.byte(arg_155_0)

	if var_155_0 > 128:
		return

	if var_155_0 >= var_0_10 and var_155_0 <= var_0_11:
		return string.char(var_155_0 - 32)
	elif var_155_0 >= var_0_12 and var_155_0 <= var_0_13:
		return string.char(var_155_0 + 32)
	else:
		return arg_155_0

def wordVerMatch(arg_156_0, arg_156_1, arg_156_2, arg_156_3, arg_156_4, arg_156_5, arg_156_6, arg_156_7):
	if arg_156_3 > len(arg_156_0):
		return arg_156_5, arg_156_6, arg_156_7

	var_156_0 = arg_156_0[arg_156_3]
	var_156_1 = arg_156_1[var_156_0]

	if var_156_1:
		var_156_2, var_156_3, var_156_4 = wordVerMatch(arg_156_0, var_156_1, arg_156_2, arg_156_3 + 1, arg_156_2.isReplace and f"{arg_156_4}{arg_156_2.replaceWord}" or arg_156_4, var_156_1.this or arg_156_5, var_156_1.this and arg_156_3 + 1 or arg_156_6, var_156_1.this and (arg_156_2.isReplace and f"{arg_156_4}{arg_156_2.replaceWord}" or arg_156_4) or arg_156_7)

		if var_156_2:
			return var_156_2, var_156_3, var_156_4

	var_156_5 = var_0_14(var_156_0)
	var_156_6 = arg_156_1[var_156_5]

	if var_156_5 != var_156_0 and var_156_6:
		var_156_7, var_156_8, var_156_9 = wordVerMatch(arg_156_0, var_156_6, arg_156_2, arg_156_3 + 1, arg_156_2.isReplace and f"{arg_156_4}{arg_156_2.replaceWord}" or arg_156_4, var_156_6.this or arg_156_5, var_156_6.this and arg_156_3 + 1 or arg_156_6, var_156_6.this and (arg_156_2.isReplace and f"{arg_156_4}{arg_156_2.replaceWord}" or arg_156_4) or arg_156_7)

		if var_156_7:
			return var_156_7, var_156_8, var_156_9

	return arg_156_5, arg_156_6, arg_156_7

def wordSplit(arg_157_0):
	var_157_0 = table()

	for iter_157_0 in arg_157_0.gmatch(arg_157_0, "[\x01-\x7F\xC2-\xF4][\x80-\xBF]*"):
		var_157_0.append(iter_157_0)

	return var_157_0

def contentWrap(arg_158_0, arg_158_1, arg_158_2):
	var_158_0 = LuaHelper.WrapContent(arg_158_0, arg_158_1, arg_158_2)

	return len(var_158_0) != len(arg_158_0), var_158_0

def cancelRich(arg_159_0):
	var_159_0

	for iter_159_0 in range(1, 20):
		var_159_1

		arg_159_0, var_159_1 = string.gsub(arg_159_0, "<([^>]*)>", "%1")

		if var_159_1 <= 0:
			break

	return arg_159_0

def getSkillConfig(arg_160_0):
	var_160_0 = require(f"GameCfg.buff.buff_{arg_160_0}")

	if not var_160_0:
		warning(f"找不到技能配置. {arg_160_0}")

		return

	var_160_1 = Clone(var_160_0)

	var_160_1.name = getSkillName(arg_160_0)
	var_160_1.desc = HXSet.hxLan(var_160_1.desc)
	var_160_1.desc_get = HXSet.hxLan(var_160_1.desc_get)

	underscore.each(var_160_1, lambda arg_161_0: setattr(arg_161_0, "desc", HXSet.hxLan(arg_161_0.desc)))

	return var_160_1

def getSkillName(arg_162_0):
	var_162_0 = pg.skill_data_template[arg_162_0] or pg.skill_data_display[arg_162_0]

	if var_162_0:
		return HXSet.hxLan(var_162_0.name)
	else:
		return ""

def getSkillDescGet(arg_163_0, arg_163_1):
	var_163_0 = arg_163_1 and pg.skill_world_display[arg_163_0] and setmetatable(table(), table(
		__index = lambda arg_164_0, arg_164_1: pg.skill_world_display[arg_163_0][arg_164_1] or pg.skill_data_template[arg_163_0][arg_164_1]
	)) or pg.skill_data_template[arg_163_0]

	if not var_163_0:
		return ""

	var_163_1 = var_163_0.desc_get != "" and var_163_0.desc_get or var_163_0.desc

	for iter_163_0, iter_163_1 in pairs(var_163_0.desc_get_add):
		var_163_2 = setColorStr(iter_163_1[1], COLOR_GREEN)

		if iter_163_1[2]:
			var_163_2 = f"{var_163_2}{specialGSub(i18n("word_skill_desc_get"), "$1", setColorStr(iter_163_1[2], COLOR_GREEN))}"

		var_163_1 = specialGSub(var_163_1, f"${iter_163_0}", var_163_2)

	return HXSet.hxLan(var_163_1)

def getSkillDescLearn(arg_165_0, arg_165_1, arg_165_2):
	var_165_0 = arg_165_2 and pg.skill_world_display[arg_165_0] and setmetatable(table(), table(
		__index = lambda arg_166_0, arg_166_1: pg.skill_world_display[arg_165_0][arg_166_1] or pg.skill_data_template[arg_165_0][arg_166_1]
	)) or pg.skill_data_template[arg_165_0]

	if not var_165_0:
		return ""

	var_165_1 = var_165_0.desc

	if not var_165_0.desc_add:
		return HXSet.hxLan(var_165_1)

	for iter_165_0, iter_165_1 in pairs(var_165_0.desc_add):
		var_165_2 = iter_165_1[arg_165_1][1]

		if iter_165_1[arg_165_1][2]:
			var_165_2 = f"{var_165_2}{specialGSub(i18n("word_skill_desc_learn"), "$1", iter_165_1[arg_165_1][2])}"

		var_165_1 = specialGSub(var_165_1, f"${iter_165_0}", setColorStr(var_165_2, COLOR_YELLOW))

	return HXSet.hxLan(var_165_1)

def getSkillDesc(arg_167_0, arg_167_1, arg_167_2):
	var_167_0 = arg_167_2 and pg.skill_world_display[arg_167_0] and setmetatable(table(), table(
		__index = lambda arg_168_0, arg_168_1: pg.skill_world_display[arg_167_0][arg_168_1] or pg.skill_data_template[arg_167_0][arg_168_1]
	)) or pg.skill_data_template[arg_167_0]

	if not var_167_0:
		return ""

	var_167_1 = var_167_0.desc

	if not var_167_0.desc_add:
		return HXSet.hxLan(var_167_1)

	for iter_167_0, iter_167_1 in pairs(var_167_0.desc_add):
		var_167_2 = setColorStr(iter_167_1[arg_167_1][1], COLOR_GREEN)

		var_167_1 = specialGSub(var_167_1, f"${iter_167_0}", var_167_2)

	return HXSet.hxLan(var_167_1)

def specialGSub(arg_169_0, arg_169_1, arg_169_2):
	arg_169_0 = string.gsub(arg_169_0, "<color=#", "<color=NNN")
	arg_169_0 = string.gsub(arg_169_0, "#", "")
	arg_169_2 = string.gsub(arg_169_2, "%%", "%%%%")
	arg_169_0 = string.gsub(arg_169_0, arg_169_1, arg_169_2)
	arg_169_0 = string.gsub(arg_169_0, "<color=NNN", "<color=#")

	return arg_169_0

def topAnimation(arg_170_0, arg_170_1, arg_170_2, arg_170_3, arg_170_4, arg_170_5):
	var_170_0 = table()

	arg_170_4 = arg_170_4 or 0.27

	var_170_1 = 0.05

	if arg_170_0:
		var_170_2 = arg_170_0.transform.localPosition.x

		setAnchoredPosition(arg_170_0, table(
			x = var_170_2 - 500
		))
		shiftPanel(arg_170_0, var_170_2, None, 0.05, arg_170_4, True, True)
		setActive(arg_170_0, True)

	setActive(arg_170_1, False)
	setActive(arg_170_2, False)
	setActive(arg_170_3, False)

	for iter_170_0 in range(1, 3):
		def _function():
			if arg_170_1:
				setActive(arg_170_1, not arg_170_1.gameObject.activeSelf)
		table.insert(var_170_0, LeanTween.delayedCall(arg_170_4 + 0.13 + var_170_1 * iter_170_0, System.Action(_function))).uniqueId
		def _function():
			if arg_170_2:
				setActive(arg_170_2, not go(arg_170_2).activeSelf)

			if arg_170_2:
				setActive(arg_170_3, not go(arg_170_3).activeSelf)
		table.insert(var_170_0, LeanTween.delayedCall(arg_170_4 + 0.02 + var_170_1 * iter_170_0, System.Action(_function)).uniqueId)

	if arg_170_5:
		table.insert(var_170_0, LeanTween.delayedCall(arg_170_4 + 0.13 + var_170_1 * 3 + 0.1, System.Action(lambda: arg_170_5())).uniqueId)

	return var_170_0

def cancelTweens(arg_174_0):
	assert arg_174_0, "must provide cancel targets, LeanTween.cancelAll is not allow"

	for iter_174_0, iter_174_1 in ipairs(arg_174_0):
		if iter_174_1:
			LeanTween.cancel(iter_174_1)

def getOfflineTimeStamp(arg_175_0):
	var_175_0 = pg.TimeMgr.GetInstance().GetServerTime() - arg_175_0
	var_175_1 = ""

	if var_175_0 <= 59:
		var_175_1 = i18n("just_now")
	elif var_175_0 <= 3599:
		var_175_1 = i18n("several_minutes_before", math.floor(var_175_0 / 60))
	elif var_175_0 <= 86399:
		var_175_1 = i18n("several_hours_before", math.floor(var_175_0 / 3600))
	else:
		var_175_1 = i18n("several_days_before", math.floor(var_175_0 / 86400))

	return var_175_1

def playMovie(arg_176_0, arg_176_1, arg_176_2):
	var_176_0 = GameObject.Find("OverlayCamera/Overlay/UITop/MoviePanel")

	if var_176_0 is not None:
		pg.UIMgr.GetInstance().LoadingOn()
		def _function(arg_177_0):
			pg.UIMgr.GetInstance().LoadingOff()

			var_177_0 = GCHandle.Alloc(arg_177_0, GCHandleType.Pinned)

			setActive(var_176_0, True)

			var_177_1 = var_176_0.AddComponent(typeof(CriManaMovieControllerForUI))

			var_177_1.player.SetData(arg_177_0, arg_177_0.Length)

			var_177_1.target = var_176_0.GetComponent(typeof(Image))
			var_177_1.loop = False
			var_177_1.additiveMode = False
			var_177_1.playOnStart = True

			var_177_2
			def _timerfunc():
				if var_177_1.player.status == CriMana.Player.Status.PlayEnd or var_177_1.player.status == CriMana.Player.Status.Stop or var_177_1.player.status == CriMana.Player.Status.Error:
					var_177_2.Stop()
					Object.Destroy(var_177_1)
					GCHandle.Free(var_177_0)
					setActive(var_176_0, False)

					if arg_176_1:
						arg_176_1(), 0.2, -1
			var_177_2 = Timer.New(_timerfunc)

			var_177_2.Start()
			removeOnButton(var_176_0)

			def _function():
					var_177_1.Stop()
					GetOrAddComponent(var_176_0, typeof(Button)).onClick.RemoveAllListeners(), SFX_CANCEL

			if arg_176_2:
				onButton(None, var_176_0, _function)
		WWWLoader.Inst.LoadStreamingAsset(arg_176_0, _function)
	elif arg_176_1:
		arg_176_1()

PaintCameraAdjustOn = False

def cameraPaintViewAdjust(arg_180_0):
	if PaintCameraAdjustOn != arg_180_0:
		var_180_0 = GameObject.Find("UICamera/Canvas").GetComponent(typeof(CanvasScaler))

		if arg_180_0:
			CameraMgr.instance.AutoAdapt = False

			CameraMgr.instance.Revert()

			var_180_0.screenMatchMode = CanvasScaler.ScreenMatchMode.MatchWidthOrHeight
			var_180_0.matchWidthOrHeight = 1
		else:
			CameraMgr.instance.AutoAdapt = True
			CameraMgr.instance.CurrentWidth = 1
			CameraMgr.instance.CurrentHeight = 1
			CameraMgr.instance.AspectRatio = 1.7777777777777777
			var_180_0.screenMatchMode = CanvasScaler.ScreenMatchMode.Expand

		PaintCameraAdjustOn = arg_180_0

def ManhattonDist(arg_181_0, arg_181_1):
	return math.abs(arg_181_0.row - arg_181_1.row) + math.abs(arg_181_0.column - arg_181_1.column)

def checkFirstHelpShow(arg_182_0):
	var_182_0 = getProxy(SettingsProxy)

	if not var_182_0.checkReadHelp(arg_182_0):
		pg.MsgboxMgr.GetInstance().ShowMsgBox(table(
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[arg_182_0].tip
		))
		var_182_0.recordReadHelp(arg_182_0)

preOrientation = None
preNotchFitterEnabled = False

def openPortrait(arg_183_0):
	enableNotch(arg_183_0, True)

	preOrientation = Input.deviceOrientation.ToString()

	originalPrint(f"Begining Orientation.{preOrientation}")

	Screen.autorotateToPortrait = True
	Screen.autorotateToPortraitUpsideDown = True

	cameraPaintViewAdjust(True)

def closePortrait(arg_184_0):
	enableNotch(arg_184_0, False)

	Screen.autorotateToPortrait = False
	Screen.autorotateToPortraitUpsideDown = False

	originalPrint(f"Closing Orientation.{preOrientation}")

	Screen.orientation = ScreenOrientation.LandscapeLeft

	var_184_0 = Timer.New(lambda: setattr(Screen, "orientation", ScreenOrientation.AutoRotation), 0.2, 1).Start()

	cameraPaintViewAdjust(False)

def enableNotch(arg_186_0, arg_186_1):
	if arg_186_0 == None:
		return

	var_186_0 = arg_186_0.GetComponent("NotchAdapt")
	var_186_1 = arg_186_0.GetComponent("AspectRatioFitter")

	var_186_0.enabled = arg_186_1

	if var_186_1:
		if arg_186_1:
			var_186_1.enabled = preNotchFitterEnabled
		else:
			preNotchFitterEnabled = var_186_1.enabled
			var_186_1.enabled = False

def comma_value(arg_187_0):
	var_187_0 = arg_187_0
	var_187_1 = 0
	var_187_2 = None
	while True:
		var_187_0, var_187_2 = string.gsub(var_187_0, "^(-?%d+)(%d%d%d)", "%1,%2")
		if var_187_2 == 0:
			break

	return var_187_0

var_0_15 = 0.2

def SwitchPanel(arg_188_0, arg_188_1, arg_188_2, arg_188_3, arg_188_4, arg_188_5):
	arg_188_3 = defaultValue(arg_188_3, var_0_15)

	if arg_188_5:
		LeanTween.cancel(go(arg_188_0))

	var_188_0 = Vector3.New(tf(arg_188_0).localPosition.x, tf(arg_188_0).localPosition.y, tf(arg_188_0).localPosition.z)

	if arg_188_1:
		var_188_0.x = arg_188_1

	if arg_188_2:
		var_188_0.y = arg_188_2

	var_188_1 = LeanTween.move(rtf(arg_188_0), var_188_0, arg_188_3).setEase(LeanTweenType.easeInOutSine)

	if arg_188_4:
		var_188_1.setDelay(arg_188_4)

	return var_188_1

def updateActivityTaskStatus(arg_189_0):
	var_189_0 = arg_189_0.getConfig("config_id")
	var_189_1, var_189_2 = getActivityTask(arg_189_0, True)

	if not var_189_2:
		pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, table(
			cmd = 1,
			activity_id = arg_189_0.id
		))

		return True

	return False

def updateCrusingActivityTask(arg_190_0):
	var_190_0 = getProxy(TaskProxy)
	var_190_1 = arg_190_0.getNDay()

	for iter_190_0, iter_190_1 in ipairs(arg_190_0.getConfig("config_data")):
		var_190_2 = pg.battlepass_task_group[iter_190_1]

		if var_190_1 >= var_190_2.time and underscore.any(underscore.flatten(var_190_2.task_group), lambda arg_191_0: var_190_0.getTaskVO(arg_191_0) == None):
			pg.m02.sendNotification(GAME.CRUSING_CMD, table(
				cmd = 1,
				activity_id = arg_190_0.id
			))

			return True

	return False

def setShipCardFrame(arg_192_0, arg_192_1, arg_192_2):
	arg_192_0.localScale = Vector3.one
	arg_192_0.anchorMin = Vector2.zero
	arg_192_0.anchorMax = Vector2.one

	var_192_0 = arg_192_2 or arg_192_1

	GetImageSpriteFromAtlasAsync("shipframe", var_192_0, arg_192_0)

	var_192_1 = pg.frame_resource[var_192_0]

	if var_192_1:
		var_192_2 = var_192_1.param

		arg_192_0.offsetMin = Vector2(var_192_2[1], var_192_2[2])
		arg_192_0.offsetMax = Vector2(var_192_2[3], var_192_2[4])
	else:
		arg_192_0.offsetMin = Vector2.zero
		arg_192_0.offsetMax = Vector2.zero

def setRectShipCardFrame(arg_193_0, arg_193_1, arg_193_2):
	arg_193_0.localScale = Vector3.one
	arg_193_0.anchorMin = Vector2.zero
	arg_193_0.anchorMax = Vector2.one

	setImageSprite(arg_193_0, GetSpriteFromAtlas("shipframeb", f"b{(arg_193_2 or arg_193_1)}"))

	var_193_0 = f"b{(arg_193_2 or arg_193_1)}"
	var_193_1 = pg.frame_resource[var_193_0]

	if var_193_1:
		var_193_2 = var_193_1.param

		arg_193_0.offsetMin = Vector2(var_193_2[1], var_193_2[2])
		arg_193_0.offsetMax = Vector2(var_193_2[3], var_193_2[4])
	else:
		arg_193_0.offsetMin = Vector2.zero
		arg_193_0.offsetMax = Vector2.zero

def setFrameEffect(arg_194_0, arg_194_1):
	if arg_194_1:
		var_194_0 = f"{arg_194_1}(Clone)"
		var_194_1 = False

		def _function(arg_195_0):
			setActive(arg_195_0, arg_195_0.name == var_194_0)

			var_194_1 = var_194_1 or arg_195_0.name == var_194_0

		eachChild(arg_194_0, _function)

		if not var_194_1:
			def _function(arg_196_0):
				if arg_194_0 is None or findTF(arg_194_0, var_194_0):
					Object.Destroy(arg_196_0)
				else:
					setParent(arg_196_0, arg_194_0)
					setActive(arg_196_0, True)
			LoadAndInstantiateAsync("effect", arg_194_1, _function)

	setActive(arg_194_0, arg_194_1)

def setProposeMarkIcon(arg_197_0, arg_197_1):
	var_197_0 = arg_197_0.Find("proposeShipCard(Clone)")
	var_197_1 = arg_197_1.propose and not arg_197_1.ShowPropose()

	if var_197_0:
		setActive(var_197_0, var_197_1)
	elif var_197_1:
		def _function(arg_198_0):
			if arg_197_0 is None or arg_197_0.Find("proposeShipCard(Clone)"):
				pg.PoolMgr.GetInstance().ReturnUI("proposeShipCard", arg_198_0)
			else:
				setParent(arg_198_0, arg_197_0, False)
		pg.PoolMgr.GetInstance().GetUI("proposeShipCard", True, _function)

def flushShipCard(arg_199_0, arg_199_1):
	var_199_0 = arg_199_1.rarity2bgPrint()
	var_199_1 = findTF(arg_199_0, "content/bg")

	GetImageSpriteFromAtlasAsync(f"bg/star_level_card_{var_199_0}", "", var_199_1)

	var_199_2 = findTF(arg_199_0, "content/ship_icon")
	var_199_3 = arg_199_1 and table(
		f"shipYardIcon/{arg_199_1.getPainting()}",
		arg_199_1.getPainting()
	) or table(
		"shipYardIcon/unknown",
		""
	)

	GetImageSpriteFromAtlasAsync(var_199_3[1], var_199_3[2], var_199_2)

	var_199_4 = arg_199_1.getShipType()
	var_199_5 = findTF(arg_199_0, "content/info/top/type")

	GetImageSpriteFromAtlasAsync("shiptype", shipType2print(var_199_4), var_199_5)
	setText(findTF(arg_199_0, "content/dockyard/lv/Text"), defaultValue(arg_199_1.level, 1))

	var_199_6 = arg_199_1.getStar()
	var_199_7 = arg_199_1.getMaxStar()
	var_199_8 = findTF(arg_199_0, "content/front/stars")

	setActive(var_199_8, True)

	var_199_9 = findTF(var_199_8, "star_tpl")
	var_199_10 = var_199_8.childCount

	for iter_199_0 in range(1, Ship.CONFIG_MAX_STAR):
		var_199_11 = var_199_10 < iter_199_0 and cloneTplTo(var_199_9, var_199_8) or var_199_8.GetChild(iter_199_0 - 1)

		setActive(var_199_11, iter_199_0 <= var_199_7)
		triggerToggle(var_199_11, iter_199_0 <= var_199_6)

	var_199_12 = findTF(arg_199_0, "content/front/frame")
	var_199_13, var_199_14 = arg_199_1.GetFrameAndEffect()

	setShipCardFrame(var_199_12, var_199_0, var_199_13)
	setFrameEffect(findTF(arg_199_0, "content/front/bg_other"), var_199_14)
	setProposeMarkIcon(arg_199_0.Find("content/dockyard/propose"), arg_199_1)

def TweenItemAlphaAndWhite(arg_200_0):
	LeanTween.cancel(arg_200_0)

	var_200_0 = GetOrAddComponent(arg_200_0, "CanvasGroup")

	var_200_0.alpha = 0

	LeanTween.alphaCanvas(var_200_0, 1, 0.2).setUseEstimatedTime(True)

	var_200_1 = findTF(arg_200_0.transform, "white_mask")

	if var_200_1:
		setActive(var_200_1, False)

def ClearTweenItemAlphaAndWhite(arg_201_0):
	LeanTween.cancel(arg_201_0)

	GetOrAddComponent(arg_201_0, "CanvasGroup").alpha = 0

def getGroupOwnSkins(arg_202_0):
	var_202_0 = table()
	var_202_1 = getProxy(ShipSkinProxy).getSkinList()
	var_202_2 = getProxy(CollectionProxy).getShipGroup(arg_202_0)

	if var_202_2:
		var_202_3 = ShipGroup.getSkinList(arg_202_0)

		for iter_202_0, iter_202_1 in ipairs(var_202_3):
			if iter_202_1.skin_type == ShipSkin.SKIN_TYPE_DEFAULT or table.contains(var_202_1, iter_202_1.id) or iter_202_1.skin_type == ShipSkin.SKIN_TYPE_REMAKE and var_202_2.trans or iter_202_1.skin_type == ShipSkin.SKIN_TYPE_PROPOSE and var_202_2.married == 1:
				var_202_0[iter_202_1.id] = True

	return var_202_0

def split(arg_203_0, arg_203_1):
	var_203_0 = table()

	if not arg_203_0:
		return None

	var_203_1 = len(arg_203_0)
	var_203_2 = 1

	while var_203_2 <= var_203_1:
		var_203_3 = string.find(arg_203_0, arg_203_1, var_203_2)

		if var_203_3 == None:
			table.insert(var_203_0, string.sub(arg_203_0, var_203_2, var_203_1))

			break

		table.insert(var_203_0, string.sub(arg_203_0, var_203_2, var_203_3 - 1))

		if var_203_3 == var_203_1:
			table.insert(var_203_0, "")

			break

		var_203_2 = var_203_3 + 1

	return var_203_0

def NumberToChinese(arg_204_0, arg_204_1):
	var_204_0 = ""
	var_204_1 = len(arg_204_0)

	for iter_204_0 in range(1, var_204_1):
		var_204_2 = string.sub(arg_204_0, iter_204_0, iter_204_0)

		if var_204_2 != "0" or var_204_2 == "0" and not arg_204_1:
			if arg_204_1:
				if var_204_1 >= 2:
					if iter_204_0 == 1:
						if var_204_2 == "1":
							var_204_0 = i18n(f"number_{10}")
						else:
							var_204_0 = f"{i18n(f"number_{var_204_2}")}{i18n("number_10")}"
					else:
						var_204_0 = f"{var_204_0}{i18n(f"number_{var_204_2}")}"
				else:
					var_204_0 = f"{var_204_0}{i18n(f"number_{var_204_2}")}"
			else:
				var_204_0 = f"{var_204_0}{i18n(f"number_{var_204_2}")}"

	return var_204_0

def getActivityTask(arg_205_0, arg_205_1):
	var_205_0 = getProxy(TaskProxy)
	var_205_1 = arg_205_0.getConfig("config_data")
	var_205_2 = arg_205_0.getNDay(arg_205_0.data1)
	var_205_3
	var_205_4
	var_205_5

	for iter_205_0 in (max(arg_205_0.data3, 1), min(var_205_2, len(var_205_1))):
		var_205_6 = _.flatten(table(
			var_205_1[iter_205_0]
		))

		for iter_205_1, iter_205_2 in ipairs(var_205_6):
			var_205_7 = var_205_0.getTaskById(iter_205_2)

			if var_205_7:
				return var_205_7.id, var_205_7

			if var_205_4:
				var_205_5 = var_205_0.getFinishTaskById(iter_205_2)

				if var_205_5:
					var_205_4 = var_205_5
				elif arg_205_1:
					return iter_205_2
				else:
					return var_205_4.id, var_205_4
			else:
				var_205_4 = var_205_0.getFinishTaskById(iter_205_2)
				var_205_5 = var_205_5 or iter_205_2

	if var_205_4:
		return var_205_4.id, var_205_4
	else:
		return var_205_5

def setImageFromImage(arg_206_0, arg_206_1, arg_206_2):
	var_206_0 = GetComponent(arg_206_0, "Image")

	var_206_0.sprite = GetComponent(arg_206_1, "Image").sprite

	if arg_206_2:
		var_206_0.SetNativeSize()

def skinTimeStamp(arg_207_0):
	var_207_0, var_207_1, var_207_2, var_207_3 = pg.TimeMgr.GetInstance().parseTimeFrom(arg_207_0)

	if var_207_0 >= 1:
		return i18n("limit_skin_time_day", var_207_0)
	elif var_207_0 <= 0 and var_207_1 > 0:
		return i18n("limit_skin_time_day_min", var_207_1, var_207_2)
	elif var_207_0 <= 0 and var_207_1 <= 0 and (var_207_2 > 0 or var_207_3 > 0):
		return i18n("limit_skin_time_min", math.max(var_207_2, 1))
	elif var_207_0 <= 0 and var_207_1 <= 0 and var_207_2 <= 0 and var_207_3 <= 0:
		return i18n("limit_skin_time_overtime")

def skinCommdityTimeStamp(arg_208_0):
	var_208_0 = pg.TimeMgr.GetInstance().GetServerTime()
	var_208_1 = max(arg_208_0 - var_208_0, 0)
	var_208_2 = floor(var_208_1 / 86400)

	if var_208_2 > 0:
		return f"{i18n("time_remaining_tip")}{var_208_2}{i18n("word_date")}"
	else:
		var_208_3 = int(var_208_1 / 3600)

		if var_208_3 > 0:
			return f"{i18n("time_remaining_tip")}{var_208_3}{i18n("word_hour")}"
		else:
			var_208_4 = int(var_208_1 / 60)

			if var_208_4 > 0:
				return f"{i18n("time_remaining_tip")}{var_208_4}{i18n("word_minute")}"
			else:
				return f"{i18n("time_remaining_tip")}{var_208_1}{i18n("word_second")}"

def InstagramTimeStamp(arg_209_0):
	var_209_0 = pg.TimeMgr.GetInstance().GetServerTime() - arg_209_0
	var_209_1 = var_209_0 / 86400

	if var_209_1 > 1:
		return i18n("ins_word_day", math.floor(var_209_1))
	else:
		var_209_2 = var_209_0 / 3600

		if var_209_2 > 1:
			return i18n("ins_word_hour", math.floor(var_209_2))
		else:
			var_209_3 = var_209_0 / 60

			if var_209_3 > 1:
				return i18n("ins_word_minu", math.floor(var_209_3))
			else:
				return i18n("ins_word_minu", 1)

def InstagramReplyTimeStamp(arg_210_0):
	var_210_0 = pg.TimeMgr.GetInstance().GetServerTime() - arg_210_0
	var_210_1 = var_210_0 / 86400

	if var_210_1 > 1:
		return i18n1(f"{int(var_210_1)}d")
	else:
		var_210_2 = var_210_0 / 3600

		if var_210_2 > 1:
			return i18n1(f"{int(var_210_2)}h")
		else:
			var_210_3 = var_210_0 / 60

			if var_210_3 > 1:
				return i18n1(f"{int(var_210_3)}min")
			else:
				return i18n1("1min")

def attireTimeStamp(arg_211_0):
	var_211_0, var_211_1, var_211_2, var_211_3 = pg.TimeMgr.GetInstance().parseTimeFrom(arg_211_0)

	if var_211_0 <= 0 and var_211_1 <= 0 and var_211_2 <= 0 and var_211_3 <= 0:
		return i18n("limit_skin_time_overtime")
	else:
		return i18n("attire_time_stamp", var_211_0, var_211_1, var_211_2)

def checkExist(arg_212_0, *args):
	var_212_0 = table(
		*args
	)

	for iter_212_0, iter_212_1 in ipairs(var_212_0):
		if arg_212_0 == None:
			break

		assert type(arg_212_0) == "table", "type error . intermediate target should be table"
		assert type(iter_212_1) == "table", "type error . param should be table"

		if type(arg_212_0[iter_212_1[1]]) == "function":
			arg_212_0 = arg_212_0[iter_212_1[1]](arg_212_0, unpack(iter_212_1[2] or table()))
		else:
			arg_212_0 = arg_212_0[iter_212_1[1]]

	return arg_212_0

def AcessWithinNull(arg_213_0, arg_213_1):
	if arg_213_0 == None:
		return

	assert type(arg_213_0) == "table"

	return arg_213_0[arg_213_1]

def showRepairMsgbox():
	def _function():
			if PathMgr.FileExists(f"{Application.persistentDataPath}/hashes.csv"):
				BundleWizard.Inst.GetGroupMgr("DEFAULT_RES").StartVerifyForLua()
			else:
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
	var_214_0 = table(
		text = i18n("msgbox_repair"),
		onCallback = _function
	)
	def _function():
			if PathMgr.FileExists(f"{Application.persistentDataPath}/hashes-live2d.csv"):
				BundleWizard.Inst.GetGroupMgr("L2D").StartVerifyForLua()
			else:
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
	var_214_1 = table(
		text = i18n("msgbox_repair_l2d"),
		onCallback = _function
	)
	def _function():
			if PathMgr.FileExists(f"{Application.persistentDataPath}/hashes-painting.csv"):
				BundleWizard.Inst.GetGroupMgr("PAINTING").StartVerifyForLua()
			else:
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_no_cache"))
	var_214_2 = table(
		text = i18n("msgbox_repair_painting"),
		onCallback = _function
	)

	pg.MsgboxMgr.GetInstance().ShowMsgBox(table(
		hideYes = True,
		hideNo = True,
		content = i18n("resource_verify_warn"),
		custom = table(
			var_214_2,
			var_214_1,
			var_214_0
		)
	))

def resourceVerify(arg_218_0, arg_218_1):
	if CSharpVersion > 35:
		BundleWizard.Inst.GetGroupMgr("DEFAULT_RES").StartVerifyForLua()

		return

	var_218_0 = f"{Application.persistentDataPath}/hashes.csv"
	var_218_1
	var_218_2 = PathMgr.ReadAllLines(var_218_0)
	var_218_3 = table()

	if arg_218_0:
		setActive(arg_218_0, True)
	else:
		pg.UIMgr.GetInstance().LoadingOn()

	def var_218_4():
		if arg_218_0:
			setActive(arg_218_0, False)
		else:
			pg.UIMgr.GetInstance().LoadingOff()

		print(var_218_1)

		def _function():
			VersionMgr.Inst.DeleteCacheFiles()
			Application.Quit()

		if var_218_1:
			pg.MsgboxMgr.GetInstance().ShowMsgBox(table(
				content = i18n("resource_verify_fail", ""),
				onYes = _function
			))
		else:
			pg.MsgboxMgr.GetInstance().ShowMsgBox(table(
				content = i18n("resource_verify_success")
			))

	var_218_5 = var_218_2.Length
	var_218_6

	def var_218_7(arg_221_0):
		if arg_221_0 < 0:
			var_218_4()

			return

		if arg_218_1:
			setSlider(arg_218_1, 0, var_218_5, var_218_5 - arg_221_0)

		var_221_0 = string.split(var_218_2[arg_221_0], ",")
		var_221_1 = var_221_0[1]
		var_221_2 = var_221_0[3]
		var_221_3 = PathMgr.getAssetBundle(var_221_1)

		if PathMgr.FileExists(var_221_3):
			var_221_4 = PathMgr.ReadAllBytes(PathMgr.getAssetBundle(var_221_1))

			if var_221_2 == HashUtil.CalcMD5(var_221_4):
				onNextTick(lambda: var_218_7(arg_221_0 - 1))

				return

		var_218_1 = var_221_1

		var_218_4()

	var_218_7(var_218_5 - 1)

def splitByWordEN(arg_223_0, arg_223_1):
	var_223_0 = string.split(arg_223_0, " ")
	var_223_1 = ""
	var_223_2 = ""
	var_223_3 = arg_223_1.GetComponent(typeof(RectTransform))
	var_223_4 = arg_223_1.GetComponent(typeof(Text))
	var_223_5 = var_223_3.rect.width

	for iter_223_0, iter_223_1 in ipairs(var_223_0):
		var_223_6 = var_223_2

		var_223_2 = var_223_2 == "" and iter_223_1 or f"{var_223_2} {iter_223_1}"

		setText(arg_223_1, var_223_2)

		if var_223_5 < var_223_4.preferredWidth:
			var_223_1 = var_223_1 == "" and var_223_6 or f"{var_223_1}\n{var_223_6}"
			var_223_2 = iter_223_1

		if iter_223_0 >= len(var_223_0):
			var_223_1 = var_223_1 == "" and var_223_2 or f"{var_223_1}\n{var_223_2}"

	return var_223_1

def checkBirthFormat(arg_224_0):
	if len(arg_224_0) != 8:
		return False

	var_224_0 = 0
	var_224_1 = len(arg_224_0)

	while var_224_0 < var_224_1:
		var_224_2 = string.byte(arg_224_0, var_224_0 + 1)

		if var_224_2 < 48 or var_224_2 > 57:
			return False

		var_224_0 = var_224_0 + 1

	return True

def isHalfBodyLive2D(arg_225_0):
	var_225_0 = table(
		"biaoqiang",
		"z23",
		"lafei",
		"lingbo",
		"mingshi",
		"xuefeng"
	)

	return _.any(var_225_0, lambda arg_226_0: arg_226_0 == arg_225_0)

def GetServerState(arg_227_0):
	var_227_0 = -1
	var_227_1 = 0
	var_227_2 = 1
	var_227_3 = 2
	var_227_4 = NetConst.GetServerStateUrl()

	if PLATFORM_CODE == PLATFORM_CH:
		var_227_4 = string.gsub(var_227_4, "https", "http")

	def _function(arg_228_0, arg_228_1):
		var_228_0 = True
		var_228_1 = False

		for iter_228_0 in string.gmatch(arg_228_1, "\"state\".%d"):
			if iter_228_0 != "\"state\".1":
				var_228_0 = False

			var_228_1 = True

		if not var_228_1:
			var_228_0 = False

		if arg_227_0 != None:
			arg_227_0(var_228_0 and var_227_2 or var_227_1)

	VersionMgr.Inst.WebRequest(var_227_4, _function)

def setScrollText(arg_229_0, arg_229_1):
	GetOrAddComponent(arg_229_0, "ScrollText").SetText(arg_229_1)

def changeToScrollText(arg_230_0, arg_230_1):
	var_230_0 = GetComponent(arg_230_0, typeof(Text))

	assert var_230_0, "without component<Text>"

	var_230_1 = arg_230_0.Find("subText")

	if not var_230_1:
		var_230_1 = cloneTplTo(arg_230_0, arg_230_0, "subText")

		eachChild(arg_230_0, lambda arg_231_0: setActive(arg_231_0, arg_231_0 == var_230_1))

		arg_230_0.GetComponent(typeof(Text)).enabled = False

	setScrollText(var_230_1, arg_230_1)

def var_0_20(arg_232_0, arg_232_1, arg_232_2):
	var_232_0 = arg_232_0.Find("base")
	var_232_1, var_232_2, var_232_3 = Equipment.GetInfoTrans(arg_232_1, arg_232_2)

	if arg_232_1.nextValue:
		var_232_4 = table(
			name = arg_232_1.name,
			type = arg_232_1.type,
			value = arg_232_1.nextValue
		)
		var_232_5, var_232_6 = Equipment.GetInfoTrans(var_232_4, arg_232_2)

		var_232_2 = f"{var_232_2}{setColorStr(f"   >   {var_232_6}", COLOR_GREEN)}"

	setText(var_232_0.Find("name"), var_232_1)

	if var_232_3:
		var_232_7 = f"<color=#afff72>(+{ys.Battle.BattleConst.UltimateBonus.AuxBoostValue * 100}%)</color>"

		setText(var_232_0.Find("value"), f"{var_232_2}{var_232_7}")
	else:
		setText(var_232_0.Find("value"), var_232_2)

	setActive(var_232_0.Find("value/up"), arg_232_1.compare and arg_232_1.compare > 0)
	setActive(var_232_0.Find("value/down"), arg_232_1.compare and arg_232_1.compare < 0)
	triggerToggle(var_232_0, arg_232_1.lock_open)

	if not arg_232_1.lock_open and arg_232_1.sub and len(arg_232_1.sub) > 0:
		GetComponent(var_232_0, typeof(Toggle)).enabled = True
	else:
		setActive(var_232_0.Find("name/close"), False)
		setActive(var_232_0.Find("name/open"), False)

		GetComponent(var_232_0, typeof(Toggle)).enabled = False

def var_0_21(arg_233_0, arg_233_1, arg_233_2, arg_233_3):
	var_0_20(arg_233_0, arg_233_2, arg_233_3)

	if not arg_233_2.sub or len(arg_233_2.sub) == 0:
		return

	var_0_18(arg_233_0.Find("subs"), arg_233_1, arg_233_2.sub, arg_233_3)

def var_0_18(arg_234_0, arg_234_1, arg_234_2, arg_234_3):
	removeAllChildren(arg_234_0)
	var_0_19(arg_234_0, arg_234_1, arg_234_2, arg_234_3)

def var_0_19(arg_235_0, arg_235_1, arg_235_2, arg_235_3):
	for iter_235_0, iter_235_1 in ipairs(arg_235_2):
		var_235_0 = cloneTplTo(arg_235_1, arg_235_0)

		var_0_21(var_235_0, arg_235_1, iter_235_1, arg_235_3)

def updateEquipInfo(arg_236_0, arg_236_1, arg_236_2, arg_236_3):
	var_236_0 = arg_236_0.Find("attr_tpl")

	var_0_18(arg_236_0.Find("attrs"), var_236_0, arg_236_1.attrs, arg_236_3)
	setActive(arg_236_0.Find("skill"), arg_236_2)

	if arg_236_2:
		var_0_21(arg_236_0.Find("skill/attr"), var_236_0, table(
			name = i18n("skill"),
			value = setColorStr(arg_236_2.name, "#FFDE00FF")
		), arg_236_3)
		setText(arg_236_0.Find("skill/value/Text"), getSkillDescGet(arg_236_2.id))

	setActive(arg_236_0.Find("weapon"), len(arg_236_1.weapon.sub) > 0)

	if len(arg_236_1.weapon.sub) > 0:
		var_0_18(arg_236_0.Find("weapon"), var_236_0, table(
			arg_236_1.weapon
		), arg_236_3)

	setActive(arg_236_0.Find("equip_info"), len(arg_236_1.equipInfo.sub) > 0)

	if len(arg_236_1.equipInfo.sub) > 0:
		var_0_18(arg_236_0.Find("equip_info"), var_236_0, table(
			arg_236_1.equipInfo
		), arg_236_3)

	var_0_21(arg_236_0.Find("part/attr"), var_236_0, table(
		name = i18n("equip_info_23")
	), arg_236_3)

	var_236_1 = arg_236_0.Find("part/value")
	var_236_2 = var_236_1.Find("label")
	var_236_3 = table()
	var_236_4 = table()

	if len(arg_236_1.part[1]) == 0 and len(arg_236_1.part[2]) == 0:
		setmetatable(var_236_3, table(
			__index = lambda arg_237_0, arg_237_1: True
		))
		setmetatable(var_236_4, table(
			__index = lambda arg_238_0, arg_238_1: True
		))
	else:
		for iter_236_0, iter_236_1 in ipairs(arg_236_1.part[1]):
			var_236_3[iter_236_1] = True

		for iter_236_2, iter_236_3 in ipairs(arg_236_1.part[2]):
			var_236_4[iter_236_3] = True

	var_236_5 = ShipType.MergeFengFanType(ShipType.FilterOverQuZhuType(ShipType.AllShipType), var_236_3, var_236_4)

	def _function(arg_239_0, arg_239_1, arg_239_2):
		arg_239_1 = arg_239_1 + 1

		if arg_239_0 == UIItemList.EventUpdate:
			var_239_0 = var_236_5[arg_239_1]

			GetImageSpriteFromAtlasAsync("shiptype", ShipType.Type2CNLabel(var_239_0), arg_239_2)
			setActive(arg_239_2.Find("main"), var_236_3[var_239_0] and not var_236_4[var_239_0])
			setActive(arg_239_2.Find("sub"), var_236_4[var_239_0] and not var_236_3[var_239_0])
			setImageAlpha(arg_239_2, not var_236_3[var_239_0] and not var_236_4[var_239_0] and 0.3 or 1)

	UIItemList.StaticAlign(var_236_1, var_236_2, len(var_236_5), _function)

def updateEquipUpgradeInfo(arg_240_0, arg_240_1, arg_240_2):
	var_240_0 = arg_240_0.Find("attr_tpl")

	var_0_18(arg_240_0.Find("attrs"), var_240_0, arg_240_1.attrs, arg_240_2)
	setActive(arg_240_0.Find("weapon"), len(arg_240_1.weapon.sub) > 0)

	if len(arg_240_1.weapon.sub) > 0:
		var_0_18(arg_240_0.Find("weapon"), var_240_0, table(
			arg_240_1.weapon
		), arg_240_2)

	setActive(arg_240_0.Find("equip_info"), len(arg_240_1.equipInfo.sub) > 0)

	if len(arg_240_1.equipInfo.sub) > 0:
		var_0_18(arg_240_0.Find("equip_info"), var_240_0, table(
			arg_240_1.equipInfo
		), arg_240_2)

def setCanvasOverrideSorting(arg_241_0, arg_241_1):
	var_241_0 = arg_241_0.parent

	arg_241_0.SetParent(pg.LayerWeightMgr.GetInstance().uiOrigin, False)

	if isActive(arg_241_0):
		GetOrAddComponent(arg_241_0, typeof(Canvas)).overrideSorting = arg_241_1
	else:
		setActive(arg_241_0, True)

		GetOrAddComponent(arg_241_0, typeof(Canvas)).overrideSorting = arg_241_1

		setActive(arg_241_0, False)

	arg_241_0.SetParent(var_241_0, False)

def createNewGameObject(arg_242_0, arg_242_1):
	var_242_0 = GameObject.New()

	if arg_242_0:
		var_242_0.name = "model"

	var_242_0.layer = arg_242_1 or Layer.UI

	return GetOrAddComponent(var_242_0, "RectTransform")

def CreateShell(arg_243_0):
	if type(arg_243_0) not in (table, userdata):
		return arg_243_0

	var_243_0 = setmetatable(table(
		__index = arg_243_0
	), arg_243_0)

	return setmetatable(table(), var_243_0)

def CameraFittingSettin(arg_244_0):
	var_244_0 = GetComponent(arg_244_0, typeof(Camera))
	var_244_1 = 1.7777777777777777
	var_244_2 = Screen.width / Screen.height

	if var_244_2 < var_244_1:
		var_244_3 = var_244_2 / var_244_1

		var_244_0.rect = UnityEngine.Rect.New(0, (1 - var_244_3) / 2, 1, var_244_3)

def SwitchSpecialChar(arg_245_0, arg_245_1):
	if PLATFORM_CODE != PLATFORM_US:
		arg_245_0 = arg_245_0.gsub(" ", " ")
		arg_245_0 = arg_245_0.gsub("\t", "    ")

	if not arg_245_1:
		arg_245_0 = arg_245_0.gsub("\n", " ")

	return arg_245_0

def AfterCheck(arg_246_0, arg_246_1):
	var_246_0 = table()

	for iter_246_0, iter_246_1 in ipairs(arg_246_0):
		var_246_0[iter_246_0] = iter_246_1[1]()

	arg_246_1()

	for iter_246_2, iter_246_3 in ipairs(arg_246_0):
		if var_246_0[iter_246_2] != iter_246_3[1]():
			iter_246_3[2]()

		var_246_0[iter_246_2] = iter_246_3[1]()

def CompareFuncs(arg_247_0, arg_247_1):
	var_247_0 = table()

	def var_247_1(arg_248_0, arg_248_1):
		var_247_0[arg_248_0] = var_247_0[arg_248_0] or table()
		var_247_0[arg_248_0][arg_248_1] = var_247_0[arg_248_0][arg_248_1] or arg_247_0[arg_248_0](arg_248_1)

		return var_247_0[arg_248_0][arg_248_1]

	def _function(arg_249_0, arg_249_1):
		var_249_0 = 1

		while var_249_0 <= len(arg_247_0):
			var_249_1 = var_247_1(var_249_0, arg_249_0)
			var_249_2 = var_247_1(var_249_0, arg_249_1)

			if var_249_1 == var_249_2:
				var_249_0 = var_249_0 + 1
			else:
				return var_249_1 < var_249_2

		return bool(arg_247_1)

	return _function

def DropResultIntegration(arg_250_0):
	var_250_0 = table()
	var_250_1 = 1

	while var_250_1 <= len(arg_250_0):
		var_250_2 = arg_250_0[var_250_1].type
		var_250_3 = arg_250_0[var_250_1].id

		var_250_0[var_250_2] = var_250_0[var_250_2] or table()

		if var_250_0[var_250_2][var_250_3]:
			var_250_4 = arg_250_0[var_250_0[var_250_2][var_250_3]]
			var_250_5 = table.remove(arg_250_0, var_250_1)

			var_250_4.count = var_250_4.count + var_250_5.count
		else:
			var_250_0[var_250_2][var_250_3] = var_250_1
			var_250_1 = var_250_1 + 1

	def _f1(arg_251_0):
			var_251_0 = arg_251_0.type
			var_251_1 = arg_251_0.id

			if var_251_0 == DROP_TYPE_SHIP:
				return 1
			elif var_251_0 == DROP_TYPE_RESOURCE:
				if var_251_1 == 1:
					return 2
				else:
					return 3
			elif var_251_0 == DROP_TYPE_ITEM:
				if var_251_1 == 59010:
					return 4
				elif var_251_1 == 59900:
					return 5
				else:
					var_251_2 = Item.getConfigData(var_251_1)
					var_251_3 = var_251_2 and var_251_2.type or 0

					if var_251_3 == 9:
						return 6
					elif var_251_3 == 5:
						return 7
					elif var_251_3 == 4:
						return 8
					elif var_251_3 == 7:
						return 9
			elif var_251_0 == DROP_TYPE_VITEM and var_251_1 == 59011:
				return 4

			return 100
	
	def _f2(arg_252_0):
			var_252_0

			if arg_252_0.type == DROP_TYPE_SHIP:
				var_252_0 = pg.ship_data_statistics[arg_252_0.id]
			elif arg_252_0.type == DROP_TYPE_ITEM:
				var_252_0 = Item.getConfigData(arg_252_0.id)

			return (var_252_0 and var_252_0.rarity or 0) * -1

	var_250_6 = table(
		_f1,
		_f2,
		lambda arg_253_0: arg_253_0.id
	)

	table.sort(arg_250_0, CompareFuncs(var_250_6))

def getLoginConfig():
	var_254_0 = pg.TimeMgr.GetInstance().GetServerTime()
	var_254_1 = 1

	for iter_254_0, iter_254_1 in ipairs(pg.login.all):
		if pg.login[iter_254_1].date != "stop":
			var_254_2, var_254_3 = parseTimeConfig(pg.login[iter_254_1].date)

			assert not var_254_3

			if pg.TimeMgr.GetInstance().inTime(var_254_2, var_254_0):
				var_254_1 = iter_254_1

				break

	var_254_4 = pg.login[var_254_1].login_static

	var_254_4 = var_254_4 != "" and var_254_4 or "login"

	var_254_5 = pg.login[var_254_1].login_cri
	var_254_6 = var_254_5 != "" and True or False
	var_254_7 = pg.login[var_254_1].op_play == 1 and True or False
	var_254_8 = pg.login[var_254_1].op_time

	if var_254_8 == "" or not pg.TimeMgr.GetInstance().inTime(var_254_8, var_254_0):
		var_254_7 = False

	var_254_9 = var_254_8 == "" and var_254_8 or table.concat(var_254_8[1][1])

	return var_254_6, var_254_6 and var_254_5 or var_254_4, pg.login[var_254_1].bgm, var_254_7, var_254_9

def setIntimacyIcon(arg_255_0, arg_255_1, arg_255_2):
	var_255_0 = table()
	var_255_1

	if arg_255_0.childCount > 0:
		var_255_1 = arg_255_0.GetChild(0)
	else:
		var_255_1 = LoadAndInstantiateSync("template", "intimacytpl").transform

		setParent(var_255_1, arg_255_0)

	setImageAlpha(var_255_1, arg_255_2 and 0 or 1)
	eachChild(var_255_1, lambda arg_256_0: setActive(arg_256_0, False))

	if arg_255_2:
		var_255_2 = var_255_1.Find(f"{arg_255_2}(Clone)")

		if not var_255_2:
			var_255_2 = LoadAndInstantiateSync("ui", arg_255_2)

			setParent(var_255_2, var_255_1)

		setActive(var_255_2, True)
	elif arg_255_1:
		setImageSprite(var_255_1, GetSpriteFromAtlas("energy", arg_255_1), True)
	else:
		assert False, "param error"

	return var_255_1

var_0_22

def nowWorld():
	var_0_22 = var_0_22 or getProxy(WorldProxy)

	return var_0_22 and var_0_22.world

def removeWorld():
	var_0_22.world.Dispose()

	var_0_22.world = None
	var_0_22 = None

def switch(arg_259_0, arg_259_1, arg_259_2, *args):
	if arg_259_1[arg_259_0]:
		return arg_259_1[arg_259_0](*args)
	elif arg_259_2:
		return arg_259_2(*args)

def parseTimeConfig(arg_260_0):
	if type(arg_260_0[1]) == table:
		return arg_260_0[2], arg_260_0[1]
	return arg_260_0

var_0_23 = table(
	__add = lambda arg_261_0, arg_261_1: NewPos(arg_261_0.x + arg_261_1.x, arg_261_0.y + arg_261_1.y),
	__sub = lambda arg_262_0, arg_262_1: NewPos(arg_262_0.x - arg_262_1.x, arg_262_0.y - arg_262_1.y),
	__mul = lambda arg_263_0, arg_263_1: NewPos(arg_263_0.x * arg_263_1, arg_263_0.y * arg_263_1) if type(arg_263_1) == "number" else NewPos(arg_263_0.x * arg_263_1.x, arg_263_0.y * arg_263_1.y),
	__eq = lambda arg_264_0, arg_264_1: arg_264_0.x == arg_264_1.x and arg_264_0.y == arg_264_1.y,
	__tostring = lambda arg_265_0: f"{arg_265_0.x_arg_265_0.y}"
)

def NewPos(arg_266_0, arg_266_1):
	assert arg_266_0 and arg_266_1

	var_266_0 = setmetatable(table(
		x = arg_266_0,
		y = arg_266_1
	), var_0_23)

	var_266_0.SqrMagnitude = lambda arg_267_0: arg_267_0.x * arg_267_0.x + arg_267_0.y * arg_267_0.y

	def _Normalize(arg_268_0):
		var_268_0 = arg_268_0.SqrMagnitude()

		if var_268_0 > 1e-05:
			return arg_268_0 * (1 / math.sqrt(var_268_0))
		return NewPos(0, 0)
	var_266_0.Normalize = _Normalize

	return var_266_0

var_0_24 = None

def Timekeeping():
	warning(Time.realtimeSinceStartup - (var_0_24 or Time.realtimeSinceStartup), Time.realtimeSinceStartup)

	var_0_24 = Time.realtimeSinceStartup

def GetRomanDigit(arg_270_0):
	return (string.char(226, 133, 160 + (arg_270_0 - 1)))

def quickPlayAnimator(arg_271_0, arg_271_1):
	arg_271_0.GetComponent(typeof(Animator)).Play(arg_271_1, -1, 0)

def getSurveyUrl(arg_272_0):
	var_272_0 = pg.survey_data_template[arg_272_0]
	var_272_1

	if not IsUnityEditor:
		if PLATFORM_CODE == PLATFORM_CH:
			var_272_2 = getProxy(UserProxy).GetCacheGatewayInServerLogined()

			if var_272_2 == PLATFORM_ANDROID:
				if LuaHelper.GetCHPackageType() == PACKAGE_TYPE_BILI:
					var_272_1 = var_272_0.main_url
				else:
					var_272_1 = var_272_0.uo_url
			elif var_272_2 == PLATFORM_IPHONEPLAYER:
				var_272_1 = var_272_0.ios_url
		elif PLATFORM_CODE == PLATFORM_US or PLATFORM_CODE == PLATFORM_JP:
			var_272_1 = var_272_0.main_url
	else:
		var_272_1 = var_272_0.main_url

	var_272_3 = getProxy(PlayerProxy).getRawData().id
	var_272_4 = getProxy(UserProxy).getRawData().arg2 or ""
	var_272_5
	var_272_6 = PLATFORM == PLATFORM_ANDROID and 1 or PLATFORM == PLATFORM_IPHONEPLAYER and 2 or 3
	var_272_7 = getProxy(UserProxy).getRawData()
	var_272_8 = getProxy(ServerProxy).getRawData()[var_272_7 and var_272_7.server or 0]
	var_272_9 = var_272_8 and var_272_8.id or ""
	var_272_10 = getProxy(PlayerProxy).getRawData().level
	var_272_11 = f"{var_272_3}_{arg_272_0}"
	var_272_12 = var_272_1
	var_272_13 = table(
		var_272_3,
		var_272_4,
		var_272_6,
		var_272_9,
		var_272_10,
		var_272_11
	)

	if var_272_12:
		for iter_272_0, iter_272_1 in ipairs(var_272_13):
			var_272_12 = string.gsub(var_272_12, f"${iter_272_0}", tostring(iter_272_1))

	warning(var_272_12)

	return var_272_12

def GetMoneySymbol():
	if PLATFORM_CH == PLATFORM_CODE:
		return "￥"
	elif PLATFORM_JP == PLATFORM_CODE:
		return "￥"
	elif PLATFORM_KR == PLATFORM_CODE:
		return "₩"
	elif PLATFORM_US == PLATFORM_CODE:
		return "$"
	elif PLATFORM_CHT == PLATFORM_CODE:
		return "TWD"

	return ""

def FilterVarchar(arg_274_0):
	assert type(arg_274_0) == "string" or type(arg_274_0) == "table"

	if arg_274_0 == "":
		return None

	return arg_274_0

def getGameset(arg_275_0):
	var_275_0 = pg.gameset[arg_275_0]

	assert var_275_0

	return table(
		var_275_0.key_value,
		var_275_0.description
	)

def getDorm3dGameset(arg_276_0):
	var_276_0 = pg.dorm3d_set[arg_276_0]

	assert var_276_0

	return table(
		var_276_0.key_value_int,
		var_276_0.key_value_varchar
	)

def GetItemsOverflowDic(arg_277_0):
	arg_277_0 = arg_277_0 or table()

	var_277_0 = table({
		DROP_TYPE_ITEM: table(),
		DROP_TYPE_RESOURCE: table(),
		DROP_TYPE_EQUIP: 0,
		DROP_TYPE_SHIP: 0,
		DROP_TYPE_WORLD_ITEM: 0
	})

	while len(arg_277_0) > 0:
		var_277_1 = table.remove(arg_277_0)

		typ = var_277_1.type
		if typ == DROP_TYPE_ITEM:
			if var_277_1.getConfig("open_directly") == 1:
				for iter_278_0, iter_278_1 in ipairs(var_277_1.getConfig("display_icon")):
					var_278_0 = Drop.Create(iter_278_1)

					var_278_0.count = var_278_0.count * var_277_1.count

					table.insert(arg_277_0, var_278_0)
			elif var_277_1.getSubClass().IsShipExpType():
				var_277_0[typ][var_277_1.id] = defaultValue(var_277_0[typ][var_277_1.id], 0) + var_277_1.count,
		elif typ == DROP_TYPE_RESOURCE:
			var_277_0[typ][var_277_1.id] = defaultValue(var_277_0[typ][var_277_1.id], 0) + var_277_1.count,
		elif typ == DROP_TYPE_EQUIP:
			var_277_0[typ] = var_277_0[typ] + var_277_1.count,
		elif typ == DROP_TYPE_SHIP:
			var_277_0[typ] = var_277_0[typ] + var_277_1.count,
		elif typ == DROP_TYPE_WORLD_ITEM:
			var_277_0[typ] = var_277_0[typ] + var_277_1.count

	return var_277_0

def CheckOverflow(arg_283_0, arg_283_1):
	var_283_0 = table()
	var_283_1 = arg_283_0[DROP_TYPE_RESOURCE][PlayerConst.ResGold] or 0
	var_283_2 = arg_283_0[DROP_TYPE_RESOURCE][PlayerConst.ResOil] or 0
	var_283_3 = arg_283_0[DROP_TYPE_EQUIP]
	var_283_4 = arg_283_0[DROP_TYPE_SHIP]
	var_283_5 = getProxy(PlayerProxy).getRawData()
	var_283_6 = False

	if arg_283_1:
		var_283_7 = var_283_5.OverStore(PlayerConst.ResStoreGold, var_283_1)
		var_283_8 = var_283_5.OverStore(PlayerConst.ResStoreOil, var_283_2)

		if var_283_7 > 0 or var_283_8 > 0:
			var_283_0.isStoreOverflow = table(
				var_283_7,
				var_283_8
			)
	else:
		if var_283_1 > 0 and var_283_5.GoldMax(var_283_1):
			return False, "gold"

		if var_283_2 > 0 and var_283_5.OilMax(var_283_2):
			return False, "oil"

	var_283_0.isExpBookOverflow = table()

	for iter_283_0, iter_283_1 in pairs(arg_283_0[DROP_TYPE_ITEM]):
		var_283_9 = Item.getConfigData(iter_283_0)

		if getProxy(BagProxy).getItemCountById(iter_283_0) + iter_283_1 > var_283_9.max_num:
			table.insert(var_283_0.isExpBookOverflow, iter_283_0)

	var_283_10 = getProxy(EquipmentProxy).getCapacity()

	if var_283_3 > 0 and var_283_3 + var_283_10 > var_283_5.getMaxEquipmentBag():
		return False, "equip"

	var_283_11 = getProxy(BayProxy).getShipCount()

	if var_283_4 > 0 and var_283_4 + var_283_11 > var_283_5.getMaxShipBag():
		return False, "ship"

	return True, var_283_0

def CheckShipExpOverflow(arg_284_0):
	var_284_0 = getProxy(BagProxy)

	for iter_284_0, iter_284_1 in pairs(arg_284_0[DROP_TYPE_ITEM]):
		if var_284_0.getItemCountById(iter_284_0) + iter_284_1 > Item.getConfigData(iter_284_0).max_num:
			return False

	return True

var_0_25 = table({
	17: "item_type17_tip2",
	"tech": "techpackage_item_use_confirm",
	16: "item_type16_tip2",
	11: "equip_skin_detail_tip",
	13: "item_type13_tip2"
})

def RegisterDetailButton(arg_285_0, arg_285_1, arg_285_2):
	Drop.Change(arg_285_2)
	typ = arg_285_2.type
	if typ == DROP_TYPE_ITEM:
		if arg_285_2.getConfig("type") == Item.SKIN_ASSIGNED_TYPE:
			var_286_0 = Item.getConfigData(arg_285_2.id).usage_arg
			var_286_1 = var_286_0[3]

			if Item.InTimeLimitSkinAssigned(arg_285_2.id):
				var_286_1 = table.mergeArray(var_286_0[2], var_286_1, True)

			var_286_2 = table()

			for iter_286_0, iter_286_1 in ipairs(var_286_0[2]):
				var_286_2[iter_286_1] = True

			def _function():
				arg_285_0.closeView()
				pg.m02.sendNotification(GAME.LOAD_LAYERS, table(
					parentContext = getProxy(ContextProxy).getCurrentContext(),
					context = Context.New(table(
						viewComponent = SelectSkinLayer,
						mediator = SkinAtlasMediator,
						data = table(
							mode = SelectSkinLayer.MODE_VIEW,
							itemId = arg_285_2.id,
							selectableSkinList = underscore.map(var_286_1, lambda arg_288_0: SelectableSkin.New(table(
									id = arg_288_0,
									isTimeLimit = var_286_2[arg_288_0] or False
								)))
						)
					))
				)), SFX_PANEL

			onButton(arg_285_0, arg_285_1, _function)
			setActive(arg_285_1, True)
		else:
			var_286_3 = getProxy(TechnologyProxy).getItemCanUnlockBluePrint(arg_285_2.id) and "tech" or arg_285_2.getConfig("type")

			if var_0_25[var_286_3]:
				var_286_4 = table(
					item2Row = True,
					content = i18n(var_0_25[var_286_3]),
					itemList = underscore.map(arg_285_2.getConfig("display_icon"), lambda arg_289_0: Drop.Create(arg_289_0))
				)

				if var_286_3 == 11:
					onButton(arg_285_0, arg_285_1, lambda: arg_285_0.emit(BaseUI.ON_DROP_LIST_OWN, var_286_4), SFX_PANEL)
				else:
					onButton(arg_285_0, arg_285_1, lambda: arg_285_0.emit(BaseUI.ON_DROP_LIST, var_286_4), SFX_PANEL)

			setActive(arg_285_1, tobool(var_0_25[var_286_3])),
	elif typ == DROP_TYPE_EQUIP:
		onButton(arg_285_0, arg_285_1, lambda: arg_285_0.emit(BaseUI.ON_DROP, arg_285_2), SFX_PANEL)
		setActive(arg_285_1, True),
	elif typ == DROP_TYPE_SPWEAPON:
		onButton(arg_285_0, arg_285_1, lambda: arg_285_0.emit(BaseUI.ON_DROP, arg_285_2), SFX_PANEL)
		setActive(arg_285_1, True)
	else:
		setActive(arg_285_1, False)

def UpdateOwnDisplay(arg_297_0, arg_297_1):
	var_297_0, var_297_1 = arg_297_1.getOwnedCount()

	setActive(arg_297_0, var_297_1 and var_297_0 > 0)

	if var_297_1 and var_297_0 > 0:
		setText(arg_297_0.Find("label"), i18n("word_own1"))
		setText(arg_297_0.Find("Text"), var_297_0)

def Damp(arg_298_0, arg_298_1, arg_298_2):
	arg_298_1 = Mathf.Max(1, arg_298_1)

	var_298_0 = Mathf.Epsilon

	if arg_298_1 < var_298_0 or var_298_0 > Mathf.Abs(arg_298_0):
		return arg_298_0

	if arg_298_2 < var_298_0:
		return 0

	var_298_1 = -4.605170186

	return arg_298_0 * (1 - Mathf.Exp(var_298_1 * arg_298_2 / arg_298_1))

def checkCullResume(arg_299_0):
	if not ReflectionHelp.RefCallMethodEx(typeof("UnityEngine.CanvasRenderer"), "GetMaterial", GetComponent(arg_299_0, "CanvasRenderer"), table(
		typeof("System.Int32")
	), table(
		0
	)):
		var_299_0 = arg_299_0.GetComponentsInChildren(typeof(MeshImage))

		for iter_299_0 in range(1, var_299_0.Length):
			var_299_0[iter_299_0 - 1].SetVerticesDirty()

		return False

	return True

def parseEquipCode(arg_300_0):
	var_300_0 = table()

	if arg_300_0 and arg_300_0 != "":
		var_300_1 = base64.dec(arg_300_0)

		var_300_0 = string.split(var_300_1, "/")
		var_300_0[5], var_300_0[6] = unpack(string.split(var_300_0[5], "\\"))

		if len(var_300_0) < 6 or arg_300_0 != base64.enc(table.concat(table(
			table.concat(underscore.first(var_300_0, 5), "/"),
			var_300_0[6]
		), "\\")):
			pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_illegal"))

			var_300_0 = table()

	for iter_300_0 in range(1, 6):
		var_300_0[iter_300_0] = var_300_0[iter_300_0] and tonumber(var_300_0[iter_300_0], 32) or 0

	return var_300_0

def buildEquipCode(arg_301_0):
	var_301_0 = underscore.map(arg_301_0.getAllEquipments(), lambda arg_302_0: ConversionBase(32, arg_302_0 and arg_302_0.id or 0))
	var_301_1 = table(
		table.concat(var_301_0, "/"),
		ConversionBase(32, checkExist(arg_301_0.GetSpWeapon(), table(
			"id"
		)) or 0)
	)

	return base64.enc(table.concat(var_301_1, "\\"))

def setDirectorSpeed(arg_303_0, arg_303_1):
	GetComponent(arg_303_0, "TimelineSpeed").SetTimelineSpeed(arg_303_1)

def envFunc(arg_304_0, arg_304_1):
	assert not getmetatable(arg_304_1), "table has error metatable"
	setfenv(arg_304_0, setmetatable(arg_304_1, table(
		__index = _G
	)))
	arg_304_0()
	setfenv(arg_304_0, _G)

	return setmetatable(arg_304_1, None)

def setDefaultZeroMetatable(arg_305_0):
	def _function(arg_306_0, arg_306_1):
			if rawget(arg_306_0, arg_306_1) == None:
				arg_306_0[arg_306_1] = 0

			return arg_306_0[arg_306_1]
	return setmetatable(arg_305_0, table(
		__index = _function
	))

if EDITOR_TOOL:
	var_0_26 = table(
		__index = table(
			LoadAssetSync = lambda arg_307_0, *args: ResourceMgr.Inst.getAssetSync(arg_307_0.path, *args),
			GetAllAssetNames = lambda arg_308_0, *args: ReflectionHelp.RefCallMethod(typeof(ResourceMgr), "GetAssetBundleAllAssetNames", ResourceMgr.Inst, table(
					typeof("System.String")
				), table(
					arg_308_0.path
				))
		)
	)

	def buildTempAB(arg_309_0, arg_309_1):
		var_309_0 = setmetatable(table(
			path = arg_309_0
		), var_0_26)

		if arg_309_1:
			onNextTick(lambda: arg_309_1(var_309_0))

		return var_309_0

	def checkABExist(arg_311_0):
		return PathMgr.FileExists(PathMgr.getAssetBundle(arg_311_0)) or ResourceMgr.Inst.AssetExist(arg_311_0)
else:
	var_0_27 = table(
		__index = table(
			LoadAssetSync = lambda arg_312_0, *args: ResourceMgr.Inst.LoadAssetSync(arg_312_0.ab, *args),
			GetAllAssetNames = lambda arg_313_0, *args: arg_313_0.ab.GetAllAssetNames(*args)
		)
	)

	def buildTempAB(arg_314_0, arg_314_1):
		var_314_0 = setmetatable(table(
			path = arg_314_0
		), var_0_27)

		if arg_314_1:
			def _f(arg_315_0):
				var_314_0.ab = arg_315_0

				arg_314_1(var_314_0)
			ResourceMgr.Inst.loadAssetBundleAsync(arg_314_0, _f)
		else:
			var_314_0.ab = ResourceMgr.Inst.loadAssetBundleSync(arg_314_0)

		return var_314_0

	def checkABExist(arg_316_0):
		return PathMgr.FileExists(PathMgr.getAssetBundle(arg_316_0))
