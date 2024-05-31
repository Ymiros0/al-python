ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = class("BattleDropsView")

var_0_0.Battle.BattleDropsView = var_0_2
var_0_2.__name = "BattleDropsView"
var_0_2.FLOAT_DURATION = 0.4

def var_0_2.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0._container = arg_1_2
	arg_1_0._containerTF = arg_1_0._container.transform

	arg_1_0.init()

def var_0_2.SetActive(arg_2_0, arg_2_1):
	setActive(arg_2_0._go, arg_2_1)

def var_0_2.AddCamera(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0._camera = arg_3_1
	arg_3_0._uiCamera = arg_3_2
	arg_3_0._cameraTF = arg_3_0._camera.transform

	local var_3_0 = arg_3_0._cameraTF.localPosition

	arg_3_0._cameraSrcX = var_3_0.x
	arg_3_0._cameraSrcZ = var_3_0.z
	arg_3_0._cameraXRotate = arg_3_0._cameraTF.localEulerAngles.x

def var_0_2.RefreshScaleRate(arg_4_0):
	local var_4_0 = UnityEngine.Screen.width
	local var_4_1 = UnityEngine.Screen.height
	local var_4_2 = arg_4_0._camera.ScreenToWorldPoint(Vector3(var_4_0, var_4_1, 0))

	arg_4_0._xScale = var_4_0 / var_4_2.x
	arg_4_0._yScale = var_4_1 / var_4_2.y

def var_0_2.Update(arg_5_0):
	if #arg_5_0._resourceList == #arg_5_0._resourcePool:
		return

	arg_5_0.updateContainerPosition()

def var_0_2.init(arg_6_0):
	arg_6_0._resourceIcon = arg_6_0._tf.Find("resourceIcon")
	arg_6_0._resourceText = arg_6_0._tf.Find("resourceText").GetComponent(typeof(Text))
	arg_6_0._resourceGO = arg_6_0._containerTF.Find("spin_gold")

	local var_6_0 = arg_6_0._tf.rect.width / 2
	local var_6_1 = arg_6_0._tf.rect.height / 2

	arg_6_0._resourceIconX = arg_6_0._resourceIcon.transform.anchoredPosition.x + var_6_0
	arg_6_0._resourceIconY = arg_6_0._resourceIcon.transform.anchoredPosition.y + var_6_1
	arg_6_0._itemPool = {}
	arg_6_0._resourcePool = {}
	arg_6_0._resourceList = {}
	arg_6_0._itemCount = 0
	arg_6_0._resourceCount = 0

	arg_6_0.updateCountText(arg_6_0._resourceText)

	arg_6_0._timerList = {}

	local var_6_2 = {}

	for iter_6_0 = 1, 5:
		table.insert(var_6_2, arg_6_0.pop(arg_6_0._resourcePool))

	for iter_6_1 = 1, 5:
		arg_6_0.push(var_6_2[iter_6_1], arg_6_0._resourcePool)

	local var_6_3

def var_0_2.pop(arg_7_0, arg_7_1):
	local var_7_0

	if #arg_7_1 == 0:
		if arg_7_1 == arg_7_0._resourcePool:
			var_7_0 = Object.Instantiate(arg_7_0._resourceGO, Vector3.zero, Quaternion.identity)
			arg_7_0._resourceList[#arg_7_0._resourceList + 1] = var_7_0

		var_7_0.transform.SetParent(arg_7_0._go, False)
	else
		var_7_0 = arg_7_1[#arg_7_1]
		arg_7_1[#arg_7_1] = None

	return var_7_0

def var_0_2.push(arg_8_0, arg_8_1, arg_8_2):
	arg_8_1.transform.localScale = Vector3(0.35, 0.35, 0.35)
	arg_8_1.GetComponent(typeof(Animator)).enabled = False

	SetActive(arg_8_1, False)

	arg_8_2[#arg_8_2 + 1] = arg_8_1

def var_0_2.updateCountText(arg_9_0, arg_9_1):
	local var_9_0

	if arg_9_1 == arg_9_0._resourceText:
		var_9_0 = arg_9_0._resourceCount

	if var_9_0 > 999:
		arg_9_1.text = string.format("%s%.1f%s", "x", var_9_0 / 1000, "k")
	else
		arg_9_1.text = string.format("%s%d", "x", var_9_0)

def var_0_2.ShowDrop(arg_10_0, arg_10_1):
	if #arg_10_0._resourceList == #arg_10_0._resourcePool:
		arg_10_0.updateContainerPosition()

	local var_10_0 = var_0_0.Battle.BattleVariable.CameraPosToUICamera(arg_10_1.scenePos.Clone())
	local var_10_1 = Vector3(var_10_0.x, var_10_0.y, 2)
	local var_10_2 = arg_10_1.drops.resourceCount
	local var_10_3, var_10_4 = math.modf(var_10_2 / var_0_1.RESOURCE_STEP)

	if var_10_4 > 0:
		arg_10_0.makeFloatAnima(var_10_1, arg_10_0._resourcePool, arg_10_0._resourceIconX, arg_10_0._resourceIconY, arg_10_0._resourceIcon, "_resourceCount", var_10_4 * var_0_1.RESOURCE_STEP, arg_10_0._resourceText, 0)

	while var_10_3 > 0:
		arg_10_0.makeFloatAnima(var_10_1, arg_10_0._resourcePool, arg_10_0._resourceIconX, arg_10_0._resourceIconY, arg_10_0._resourceIcon, "_resourceCount", var_0_1.RESOURCE_STEP, arg_10_0._resourceText, var_10_3)

		var_10_3 = var_10_3 - 1

def var_0_2.updateContainerPosition(arg_11_0):
	local var_11_0 = arg_11_0._cameraTF.localPosition

	arg_11_0._containerTF.localPosition = Vector3(arg_11_0._xScale * (arg_11_0._cameraSrcX - var_11_0.x), arg_11_0._yScale * (arg_11_0._cameraSrcZ - var_11_0.z), 0)

def var_0_2.makeFloatAnima(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4, arg_12_5, arg_12_6, arg_12_7, arg_12_8, arg_12_9):
	local var_12_0 = arg_12_0.pop(arg_12_2)
	local var_12_1 = var_12_0.transform

	SetActive(var_12_0, True)

	var_12_1.position = arg_12_1
	var_12_1.localPosition = var_12_1.localPosition - arg_12_0._containerTF.localPosition

	arg_12_0.Update()
	var_12_1.SetParent(arg_12_0._container, False)

	local var_12_2 = math.random() * 200 - 100
	local var_12_3 = math.random() * 200

	LeanTween.moveX(rtf(var_12_0), var_12_1.anchoredPosition.x + var_12_2, var_0_1.RESOURCE_STAY_DURATION + arg_12_9 * 0.05).setOnComplete(System.Action(function()
		LeanTween.scale(go(var_12_0), Vector3(0.2, 0.2, 1), var_0_2.FLOAT_DURATION)

		local var_13_0 = Vector3(arg_12_3 - var_12_1.position.x, arg_12_4 - var_12_1.position.y, 0)

		var_12_1.localPosition = var_12_1.localPosition + arg_12_0._containerTF.localPosition

		var_12_1.SetParent(arg_12_0._go, False)
		LeanTween.move(rtf(var_12_0), var_13_0, var_0_2.FLOAT_DURATION).setOnComplete(System.Action(function()
			arg_12_0.push(var_12_0, arg_12_2)

			arg_12_5.transform.localScale = Vector3(0.35, 0.35, 0.35)
			arg_12_0[arg_12_6] = arg_12_0[arg_12_6] + arg_12_7

			arg_12_0.updateCountText(arg_12_8)
			LeanTween.scale(go(arg_12_5), Vector3(0.5, 0.5, 0.5), 0.12).setEase(LeanTweenType.easeOutExpo).setOnComplete(System.Action(function()
				LeanTween.scale(go(arg_12_5), Vector3(0.35, 0.35, 0.35), 0.3)))))))

	local var_12_4 = var_12_3 / 200

	LeanTween.moveY(rtf(var_12_0), var_12_1.anchoredPosition.y + var_12_3, 0.5 * var_12_4).setOnComplete(System.Action(function()
		var_12_0.GetComponent("Animator").enabled = True

		LeanTween.moveY(rtf(var_12_0), var_12_1.anchoredPosition.y - var_12_3, 1.5 * var_12_4).setEase(LeanTweenType.easeOutBounce)))

def var_0_2.Dispose(arg_17_0):
	for iter_17_0, iter_17_1 in pairs(arg_17_0._timerList):
		if iter_17_1:
			pg.TimeMgr.GetInstance().RemoveBattleTimer(iter_17_0)

	for iter_17_2, iter_17_3 in ipairs(arg_17_0._resourceList):
		LeanTween.cancel(go(iter_17_3))

	arg_17_0._timerList = None
	arg_17_0._go = None
	arg_17_0._resourceIcon = None
	arg_17_0._resourceText = None
	arg_17_0._itemIcon = None
	arg_17_0._itemText = None
	arg_17_0._camera = None
	arg_17_0._uiCamera = None
