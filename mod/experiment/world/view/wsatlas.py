local var_0_0 = class("WSAtlas", import("...BaseEntity"))

var_0_0.Fields = {
	transform = "userdata",
	atlas = "table",
	tfMapSelect = "userdata",
	tfCamera = "userdata",
	defaultSprite = "userdata",
	tfEntity = "userdata",
	cmPointer = "userdata",
	staticEntranceDic = "table",
	onClickColor = "function",
	tfSpriteScene = "userdata",
	addSprite = "userdata",
	tfMapScene = "userdata",
	tfActiveMark = "userdata",
	selectEntrance = "table"
}
var_0_0.Listeners = {
	onUpdateActiveEntrance = "OnUpdateActiveEntrance",
	onUpdatePressingAward = "OnUpdatePressingAward",
	onUpdateProgress = "OnUpdateProgress"
}
var_0_0.spriteBaseSize = Vector2(2048, 1347)

def var_0_0.Setup(arg_1_0):
	pg.DelegateInfo.New(arg_1_0)
	arg_1_0.Init()

def var_0_0.Dispose(arg_2_0):
	pg.DelegateInfo.Dispose(arg_2_0)
	arg_2_0.RemoveAtlasListener()
	arg_2_0.UpdateStaticMark()
	arg_2_0.ActiveSelect(arg_2_0.selectEntrance, False)

	if arg_2_0.tfActiveMark:
		arg_2_0.DestroyActiveMark()

	eachChild(arg_2_0.tfMapScene.Find("lock_layer"), function(arg_3_0)
		arg_2_0.RemoveExtraMarkPrefab(arg_3_0))
	arg_2_0.ReturnScene()
	arg_2_0.Clear()

def var_0_0.Init(arg_4_0):
	arg_4_0.staticEntranceDic = {}

def var_0_0.UpdateAtlas(arg_5_0, arg_5_1):
	if arg_5_0.atlas != arg_5_1:
		arg_5_0.RemoveAtlasListener()

		arg_5_0.atlas = arg_5_1

		arg_5_0.AddAtlasListener()
		arg_5_0.UpdateModelMask()
		arg_5_0.OnUpdateActiveEntrance(None, None, arg_5_0.atlas.GetActiveEntrance())
		arg_5_0.OnUpdatePressingAward()

def var_0_0.AddAtlasListener(arg_6_0):
	if arg_6_0.atlas:
		arg_6_0.atlas.AddListener(WorldAtlas.EventUpdateProgress, arg_6_0.onUpdateProgress)
		arg_6_0.atlas.AddListener(WorldAtlas.EventUpdateActiveEntrance, arg_6_0.onUpdateActiveEntrance)
		arg_6_0.atlas.AddListener(WorldAtlas.EventAddPressingEntrance, arg_6_0.onUpdatePressingAward)

def var_0_0.RemoveAtlasListener(arg_7_0):
	if arg_7_0.atlas:
		arg_7_0.atlas.RemoveListener(WorldAtlas.EventUpdateProgress, arg_7_0.onUpdateProgress)
		arg_7_0.atlas.RemoveListener(WorldAtlas.EventUpdateActiveEntrance, arg_7_0.onUpdateActiveEntrance)
		arg_7_0.atlas.RemoveListener(WorldAtlas.EventAddPressingEntrance, arg_7_0.onUpdatePressingAward)

def var_0_0.LoadScene(arg_8_0, arg_8_1):
	assert(False, "overwrite by subclass")

def var_0_0.ReturnScene(arg_9_0):
	assert(False, "overwrite by subclass")

def var_0_0.ShowOrHide(arg_10_0, arg_10_1):
	setActive(arg_10_0.transform, arg_10_1)

def var_0_0.GetMapScreenPos(arg_11_0, arg_11_1):
	return arg_11_0.cmPointer.GetMapScreenPos(arg_11_1)

def var_0_0.UpdateSelect(arg_12_0, arg_12_1):
	arg_12_0.ActiveSelect(arg_12_0.selectEntrance, False)
	arg_12_0.ActiveSelect(arg_12_1, True)

def var_0_0.ActiveSelect(arg_13_0, arg_13_1, arg_13_2):
	arg_13_0.selectEntrance = arg_13_2 and arg_13_1 or None

	if not arg_13_1 or arg_13_0.staticEntranceDic[arg_13_1.id]:
		return

	if arg_13_1.HasPort():
		-- block empty
	else
		setActive(arg_13_0.tfMapSelect.Find("A" .. arg_13_1.GetColormaskUniqueID() .. "_2"), arg_13_2)

def var_0_0.ActiveStatic(arg_14_0, arg_14_1, arg_14_2):
	arg_14_0.staticEntranceDic[arg_14_1.id] = arg_14_2

	if arg_14_1 == arg_14_0.selectEntrance:
		return

	if arg_14_1.HasPort():
		-- block empty
	else
		local var_14_0 = arg_14_0.tfMapSelect.Find("A" .. arg_14_1.GetColormaskUniqueID() .. "_2")

		LeanTween.cancel(go(var_14_0))

		local var_14_1 = var_14_0.GetComponent("SpriteRenderer").color

		var_14_1.a = arg_14_2 and 0 or 1
		var_14_0.GetComponent("SpriteRenderer").color = var_14_1

		if arg_14_2:
			setActive(var_14_0, True)
			LeanTween.alpha(go(var_14_0), 0.75, 1).setFrom(0).setLoopPingPong()
		else
			setActive(var_14_0, arg_14_0.selectEntrance == arg_14_1)

var_0_0.pressingMaskColor = Color.New(0.027450980392156862, 0.27450980392156865, 0.5490196078431373, 0.5019607843137255)
var_0_0.openMaskColor = Color.New(0, 0, 0, 0)
var_0_0.lockMaskColor = Color.New(0, 0, 0, 0.4)

def var_0_0.UpdateModelMask(arg_15_0):
	for iter_15_0, iter_15_1 in pairs(arg_15_0.atlas.entranceDic):
		arg_15_0.UpdateEntranceMask(iter_15_1)

def var_0_0.UpdateEntranceMask(arg_16_0, arg_16_1):
	if arg_16_1.HasPort():
		-- block empty
	else
		local var_16_0 = arg_16_0.tfMapScene.Find("lock_layer/A" .. arg_16_1.GetColormaskUniqueID()).GetComponent("SpriteRenderer")

		if arg_16_1.IsPressing():
			var_16_0.color = var_0_0.pressingMaskColor
			var_16_0.material = arg_16_0.addSprite
		elif arg_16_0.atlas.transportDic[arg_16_1.id] and arg_16_1.IsOpen():
			var_16_0.color = var_0_0.openMaskColor
			var_16_0.material = arg_16_0.defaultSprite
		else
			var_16_0.color = var_0_0.lockMaskColor
			var_16_0.material = arg_16_0.defaultSprite

def var_0_0.SetSairenMarkActive(arg_17_0, arg_17_1, arg_17_2):
	arg_17_0.DoUpdatExtraMark(arg_17_1, "dsj_srgr", arg_17_2, function(arg_18_0)
		if arg_17_2:
			arg_18_0.GetComponent("SpriteRenderer").sprite = arg_17_1.GetComponent("SpriteRenderer").sprite)

def var_0_0.OnUpdateProgress(arg_19_0, arg_19_1, arg_19_2, arg_19_3):
	for iter_19_0 in pairs(arg_19_3):
		local var_19_0 = arg_19_0.atlas.GetEntrance(iter_19_0)

		arg_19_0.UpdateEntranceMask(var_19_0)

	arg_19_0.UpdateCenterEffectDisplay()

def var_0_0.BuildActiveMark(arg_20_0):
	arg_20_0.tfActiveMark = tf(GameObject.New())
	arg_20_0.tfActiveMark.gameObject.layer = Layer.UI
	arg_20_0.tfActiveMark.name = "active_mark"

	arg_20_0.tfActiveMark.SetParent(arg_20_0.tfSpriteScene, False)
	setActive(arg_20_0.tfActiveMark, False)

def var_0_0.DestroyActiveMark(arg_21_0):
	arg_21_0.RemoveExtraMarkPrefab(arg_21_0.tfActiveMark)
	Destroy(arg_21_0.tfActiveMark)

def var_0_0.LoadExtraMarkPrefab(arg_22_0, arg_22_1, arg_22_2, arg_22_3):
	local var_22_0 = PoolMgr.GetInstance()

	var_22_0.GetPrefab("world/mark/" .. arg_22_2, arg_22_2, True, function(arg_23_0)
		if IsNil(arg_22_1):
			var_22_0.ReturnPrefab("world/mark/" .. arg_22_2, arg_22_2, arg_23_0, True)
		else
			arg_23_0.name = arg_22_2

			tf(arg_23_0).SetParent(arg_22_1, False)
			setActive(arg_23_0, True)
			existCall(arg_22_3, tf(arg_23_0)))

def var_0_0.RemoveExtraMarkPrefab(arg_24_0, arg_24_1):
	local var_24_0 = PoolMgr.GetInstance()

	eachChild(arg_24_1, function(arg_25_0)
		var_24_0.ReturnPrefab("world/mark/" .. arg_25_0.name, arg_25_0.name, go(arg_25_0), True))

def var_0_0.DoUpdatExtraMark(arg_26_0, arg_26_1, arg_26_2, arg_26_3, arg_26_4):
	local var_26_0 = arg_26_1.Find(arg_26_2)

	if var_26_0:
		setActive(var_26_0, arg_26_3)
		existCall(arg_26_4, var_26_0)
	elif arg_26_3:
		arg_26_0.LoadExtraMarkPrefab(arg_26_1, arg_26_2, arg_26_4)

def var_0_0.OnUpdateActiveEntrance(arg_27_0, arg_27_1, arg_27_2, arg_27_3):
	if arg_27_3:
		arg_27_0.tfActiveMark.localPosition = WorldConst.CalcModelPosition(arg_27_3, arg_27_0.spriteBaseSize)

	setActive(arg_27_0.tfActiveMark, arg_27_3)

def var_0_0.UpdateStaticMark(arg_28_0, arg_28_1):
	for iter_28_0, iter_28_1 in pairs(arg_28_0.staticEntranceDic):
		arg_28_0.ActiveStatic(arg_28_0.atlas.GetEntrance(iter_28_0), False)

	for iter_28_2, iter_28_3 in pairs(arg_28_1 or {}):
		if iter_28_3:
			arg_28_0.ActiveStatic(arg_28_0.atlas.GetEntrance(iter_28_2), True)

def var_0_0.OnUpdatePressingAward(arg_29_0, arg_29_1, arg_29_2, arg_29_3):
	arg_29_3 = arg_29_3 or arg_29_0.atlas.transportDic

	for iter_29_0, iter_29_1 in pairs(arg_29_3):
		if iter_29_1:
			arg_29_0.UpdateEntranceMask(arg_29_0.atlas.GetEntrance(iter_29_0))

def var_0_0.UpdateCenterEffectDisplay(arg_30_0):
	local var_30_0 = nowWorld().CheckAreaUnlock(5)

	setActive(arg_30_0.tfEntity.Find("decolation_layer/DSJ_xuanwo"), not var_30_0)
	setActive(arg_30_0.tfEntity.Find("decolation_layer/DSJ_xuanwo_jianhua"), var_30_0)

return var_0_0
