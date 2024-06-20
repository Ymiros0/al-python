local var_0_0 = class("SpinePainting")
local var_0_1 = require("Mgr/Pool/PoolUtil")
local var_0_2 = {
	"aimudeng_4",
	"aimudeng_4M"
}
local var_0_3 = {
	"gaoxiong_6",
	"aimudeng_4M"
}

def var_0_0.GenerateData(arg_1_0):
	local var_1_0 = {
		def SetData:(arg_2_0, arg_2_1)
			arg_2_0.ship = arg_2_1.ship
			arg_2_0.parent = arg_2_1.parent
			arg_2_0.effectParent = arg_2_1.effectParent

			local var_2_0 = arg_2_0.GetShipSkinConfig()

			arg_2_0.pos = arg_2_1.position + BuildVector3(var_2_0.spine_offset[1])

			local var_2_1 = var_2_0.spine_offset[2][1]

			arg_2_0.scale = Vector3(var_2_1, var_2_1, var_2_1)

			if #var_2_0.special_effects > 0:
				arg_2_0.bgEffectName = var_2_0.special_effects[1]
				arg_2_0.bgEffectPos = arg_2_1.position + BuildVector3(var_2_0.special_effects[2])

				local var_2_2 = var_2_0.special_effects[3][1]

				arg_2_0.bgEffectScale = Vector3(var_2_2, var_2_2, var_2_2),
		def GetShipName:(arg_3_0)
			return arg_3_0.ship.getPainting(),
		def GetShipSkinConfig:(arg_4_0)
			return arg_4_0.ship.GetSkinConfig(),
		def isEmpty:(arg_5_0)
			return arg_5_0.ship == None,
		def Clear:(arg_6_0)
			arg_6_0.ship = None
			arg_6_0.parent = None
			arg_6_0.scale = None
			arg_6_0.pos = None
			arg_6_0.bgEffectName = None
			arg_6_0.bgEffectPos = None
			arg_6_0.bgEffectScale = None
			arg_6_0.effectParent = None
	}

	var_1_0.SetData(arg_1_0)

	return var_1_0

local function var_0_4(arg_7_0, arg_7_1)
	arg_7_0._go = arg_7_1
	arg_7_0._tf = tf(arg_7_1)

	UIUtil.SetLayerRecursively(arg_7_0._go, LayerMask.NameToLayer("UI"))
	arg_7_0._tf.SetParent(arg_7_0._spinePaintingData.parent, True)

	arg_7_0._tf.localScale = arg_7_0._spinePaintingData.scale
	arg_7_0._tf.localPosition = arg_7_0._spinePaintingData.pos
	arg_7_0.spineAnimList = {}

	local var_7_0 = arg_7_0._tf.GetComponent(typeof(ItemList)).prefabItem

	for iter_7_0 = 0, var_7_0.Length - 1:
		arg_7_0.spineAnimList[#arg_7_0.spineAnimList + 1] = GetOrAddComponent(var_7_0[iter_7_0], "SpineAnimUI")

	local var_7_1 = #arg_7_0.spineAnimList

	assert(var_7_1 > 0, "动态立绘至少要保证有一个spine动画，请检查" .. arg_7_0._spinePaintingData.GetShipName())

	if var_7_1 == 1:
		arg_7_0.mainSpineAnim = arg_7_0.spineAnimList[1]
	else
		arg_7_0.mainSpineAnim = arg_7_0.spineAnimList[#arg_7_0.spineAnimList]

	arg_7_0._skeletonGraphic = arg_7_0.mainSpineAnim.GetComponent("SkeletonGraphic")
	arg_7_0.idleName = arg_7_0.getNormalName()

	arg_7_0.checkActionShow()

def var_0_0.getNormalName(arg_8_0):
	return "normal"

local function var_0_5(arg_9_0, arg_9_1)
	arg_9_0._bgEffectGo = arg_9_1
	arg_9_0._bgEffectTf = tf(arg_9_1)

	UIUtil.SetLayerRecursively(arg_9_0._bgEffectGo, LayerMask.NameToLayer("UI"))
	arg_9_0._bgEffectTf.SetParent(arg_9_0._spinePaintingData.effectParent, True)

	arg_9_0._bgEffectTf.localScale = arg_9_0._spinePaintingData.bgEffectScale
	arg_9_0._bgEffectTf.localPosition = arg_9_0._spinePaintingData.bgEffectPos

def var_0_0.Ctor(arg_10_0, arg_10_1, arg_10_2):
	arg_10_0._spinePaintingData = arg_10_1
	arg_10_0._loader = AutoLoader.New()

	parallelAsync({
		function(arg_11_0)
			local var_11_0 = arg_10_0._spinePaintingData.GetShipName()
			local var_11_1, var_11_2 = HXSet.autoHxShift("spinepainting/", var_11_0)
			local var_11_3 = var_11_1 .. var_11_2

			arg_10_0._loader.LoadPrefab(var_11_3, None, function(arg_12_0)
				var_0_4(arg_10_0, arg_12_0)
				arg_11_0(), var_11_3),
		function(arg_13_0)
			local var_13_0 = arg_10_0._spinePaintingData.bgEffectName

			if var_13_0 != None:
				local var_13_1 = "ui/" .. var_13_0

				arg_10_0._loader.LoadPrefab(var_13_1, var_13_0, function(arg_14_0)
					var_0_5(arg_10_0, arg_14_0)
					arg_13_0(), var_13_1)
			else
				arg_13_0()
	}, function()
		setActive(arg_10_0._spinePaintingData.parent, True)
		setActive(arg_10_0._spinePaintingData.effectParent, True)

		if arg_10_2:
			arg_10_2(arg_10_0))

def var_0_0.SetVisible(arg_16_0, arg_16_1):
	setActive(arg_16_0._spinePaintingData.effectParent, arg_16_1)
	setActiveViaLayer(arg_16_0._spinePaintingData.effectParent, arg_16_1)

	if not arg_16_1:
		arg_16_0.mainSpineAnim.SetActionCallBack(None)

		arg_16_0.inAction = False

		if LeanTween.isTweening(go(arg_16_0._tf)):
			LeanTween.cancel(go(arg_16_0._tf))

		if arg_16_0._baseShader:
			arg_16_0._skeletonGraphic.material.shader = arg_16_0._baseShader
			arg_16_0._baseShader = None

	arg_16_0.checkActionShow()

def var_0_0.checkActionShow(arg_17_0):
	local var_17_0 = tostring(arg_17_0.mainSpineAnim.name) .. "_" .. tostring(arg_17_0._spinePaintingData.ship.id)
	local var_17_1 = PlayerPrefs.GetString(var_17_0)

	if var_17_1 and #var_17_1 > 0:
		if PlayerPrefs.GetInt(LIVE2D_STATUS_SAVE, 1) == 1 and arg_17_0.idleName != var_17_1:
			arg_17_0.idleName = var_17_1

			arg_17_0.SetAction(var_17_1, 0)
		elif PlayerPrefs.GetInt(LIVE2D_STATUS_SAVE, 1) != 1 and arg_17_0.idleName != arg_17_0.getNormalName():
			arg_17_0.idleName = arg_17_0.getNormalName()

			arg_17_0.SetAction(arg_17_0.idleName, 0)

def var_0_0.DoSpecialTouch(arg_18_0):
	if not arg_18_0.inAction:
		arg_18_0.inAction = True

		arg_18_0.SetActionWithCallback("special", 0, function()
			arg_18_0.SetAction(arg_18_0.getNormalName(), 0)

			arg_18_0.inAction = False)

def var_0_0.DoDragClick(arg_20_0):
	return

def var_0_0.DoDragTouch(arg_21_0):
	local var_21_0 = False

	for iter_21_0, iter_21_1 in ipairs(var_0_3):
		var_21_0 = var_21_0 or string.find(arg_21_0.mainSpineAnim.name, iter_21_1) == 1

	if var_21_0 and not arg_21_0.inAction:
		arg_21_0.inAction = True

		if not arg_21_0.idleName or arg_21_0.idleName != "ex":
			arg_21_0.idleName = "ex"

			if string.find(arg_21_0.mainSpineAnim.name, "aimudeng_4"):
				arg_21_0._baseMaterial = arg_21_0._skeletonGraphic.material

				arg_21_0.getSpineMaterial("SkeletonGraphicDefaultRGBSplit", function(arg_22_0)
					arg_21_0._skeletonGraphic.material = arg_22_0

					LeanTween.delayedCall(go(arg_21_0._tf), 0.5, System.Action(function()
						arg_21_0._skeletonGraphic.material = arg_21_0._baseMaterial

						arg_21_0.changeSpecialIdle(arg_21_0.idleName))))
			else
				arg_21_0.SetActionWithFinishCallback("drag", 0, function()
					arg_21_0.changeSpecialIdle(arg_21_0.idleName))
		elif arg_21_0.idleName == "ex":
			arg_21_0.idleName = "normal"

			if string.find(arg_21_0.mainSpineAnim.name, "aimudeng_4"):
				arg_21_0._baseMaterial = arg_21_0._skeletonGraphic.material

				arg_21_0.getSpineMaterial("SkeletonGraphicDefaultRGBSplit", function(arg_25_0)
					arg_21_0._skeletonGraphic.material = arg_25_0

					LeanTween.delayedCall(go(arg_21_0._tf), 0.5, System.Action(function()
						arg_21_0._skeletonGraphic.material = arg_21_0._baseMaterial

						arg_21_0.changeSpecialIdle(arg_21_0.idleName))))
			else
				arg_21_0.SetActionWithFinishCallback("drag_ex", 0, function()
					arg_21_0.changeSpecialIdle(arg_21_0.idleName))

def var_0_0.getSpineMaterial(arg_28_0, arg_28_1, arg_28_2):
	if not arg_28_0._materialDic:
		arg_28_0._materialDic = {}

	if arg_28_0._materialDic[arg_28_1]:
		arg_28_2(arg_28_0._materialDic[arg_28_1])

	PoolMgr.GetInstance().LoadAsset("spinematerials", arg_28_1, False, typeof(Material), function(arg_29_0)
		arg_28_0._materialDic[arg_28_1] = arg_29_0

		arg_28_2(arg_28_0._materialDic[arg_28_1]), False)

def var_0_0.changeSpecialIdle(arg_30_0, arg_30_1):
	arg_30_0.SetAction(arg_30_1, 0)

	local var_30_0 = tostring(arg_30_0.mainSpineAnim.name) .. "_" .. tostring(arg_30_0._spinePaintingData.ship.id)

	PlayerPrefs.SetString(var_30_0, arg_30_1)

	arg_30_0.inAction = False

def var_0_0.SetAction(arg_31_0, arg_31_1, arg_31_2):
	if arg_31_2 == 1:
		if arg_31_0.inAction:
			return

		local var_31_0, var_31_1 = arg_31_0.getMultipFaceData()
		local var_31_2 = tonumber(arg_31_1)

		if var_31_2 and var_31_0:
			arg_31_1 = tostring(var_31_2 + var_31_1)

	if arg_31_1 == arg_31_0.getNormalName() and arg_31_0.idleName != None:
		arg_31_1 = arg_31_0.idleName

	for iter_31_0, iter_31_1 in ipairs(arg_31_0.spineAnimList):
		iter_31_1.SetAction(arg_31_1, arg_31_2)

def var_0_0.SetActionWithCallback(arg_32_0, arg_32_1, arg_32_2, arg_32_3):
	arg_32_0.SetAction(arg_32_1, arg_32_2)

	if arg_32_0.mainSpineAnim:
		arg_32_0.mainSpineAnim.SetActionCallBack(function(arg_33_0)
			arg_32_0.mainSpineAnim.SetActionCallBack(None)

			if arg_33_0 == "finish" and arg_32_3:
				arg_32_3())
		arg_32_0.mainSpineAnim.SetAction(arg_32_1, 0)

def var_0_0.SetActionWithFinishCallback(arg_34_0, arg_34_1, arg_34_2, arg_34_3):
	arg_34_0.SetAction(arg_34_1, arg_34_2)

	if arg_34_0.mainSpineAnim:
		arg_34_0.mainSpineAnim.SetActionCallBack(function(arg_35_0)
			if arg_35_0 == "finish" and arg_34_3:
				arg_34_0.mainSpineAnim.SetActionCallBack(None)
				arg_34_3())
		arg_34_0.mainSpineAnim.SetAction(arg_34_1, 0)

def var_0_0.SetEmptyAction(arg_36_0, arg_36_1):
	arg_36_0.SetVisible(True)

	for iter_36_0, iter_36_1 in ipairs(arg_36_0.spineAnimList):
		local var_36_0 = iter_36_1.GetAnimationState()

		if var_36_0:
			var_36_0.SetEmptyAnimation(arg_36_1, 0)
			GetComponent(iter_36_1.transform, "SkeletonGraphic").Update(Time.deltaTime)

def var_0_0.getMultipFaceData(arg_37_0):
	if table.contains(var_0_2, arg_37_0.mainSpineAnim.name) and arg_37_0.idleName == "ex":
		return True, 5

def var_0_0.Dispose(arg_38_0):
	arg_38_0._materialDic = {}

	if arg_38_0._spinePaintingData:
		arg_38_0._spinePaintingData.Clear()

	arg_38_0._loader.Clear()

	if arg_38_0._go != None:
		var_0_1.Destroy(arg_38_0._go)

	if arg_38_0._bgEffectGo != None:
		var_0_1.Destroy(arg_38_0._bgEffectGo)

	arg_38_0._go = None
	arg_38_0._tf = None
	arg_38_0._bgEffectGo = None
	arg_38_0._bgEffectTf = None

	if arg_38_0.spineAnim:
		arg_38_0.spineAnim.SetActionCallBack(None)

return var_0_0