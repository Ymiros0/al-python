local var_0_0 = class("GuideUIDuplicator")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.caches = {}
	arg_1_0.root = arg_1_1

def var_0_0.Duplicate(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = Object.Instantiate(arg_2_1, arg_2_0.root).transform

	setActive(var_2_0, True)
	arg_2_0.InitDuplication(var_2_0, arg_2_1, arg_2_2)

	if arg_2_2:
		arg_2_0.UpdateSettings(var_2_0, arg_2_1, arg_2_2)

	table.insert(arg_2_0.caches, var_2_0)

	return var_2_0

local function var_0_1(arg_3_0)
	return arg_3_0.GetComponent(typeof(Button)) != None or arg_3_0.GetComponent(typeof(Toggle)) != None or arg_3_0.GetComponent(typeof(EventTriggerListener)) != None

local function var_0_2(arg_4_0)
	local var_4_0 = arg_4_0.GetComponent(typeof(Button))
	local var_4_1 = arg_4_0.GetComponentsInChildren(typeof(Button))

	for iter_4_0 = 1, var_4_1.Length:
		local var_4_2 = var_4_1[iter_4_0 - 1]

		if var_4_0 != var_4_2:
			var_4_2.enabled = False

	local var_4_3 = arg_4_0.GetComponent(typeof(Toggle))
	local var_4_4 = arg_4_0.GetComponentsInChildren(typeof(Toggle))

	for iter_4_1 = 1, var_4_4.Length:
		local var_4_5 = var_4_4[iter_4_1 - 1]

		if var_4_3 != var_4_5:
			var_4_5.enabled = False

	if var_4_3:
		setToggleEnabled(arg_4_0, True)

local function var_0_3(arg_5_0)
	if LeanTween.isTweening(arg_5_0.gameObject):
		LeanTween.cancel(arg_5_0.gameObject)

	eachChild(arg_5_0, function(arg_6_0)
		if LeanTween.isTweening(arg_6_0.gameObject):
			LeanTween.cancel(arg_6_0.gameObject))

def var_0_0.InitDuplication(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	local var_7_0 = arg_7_1.GetComponent(typeof(CanvasGroup))

	if var_7_0:
		var_7_0.alpha = 1

	local var_7_1 = arg_7_1.GetComponentInChildren(typeof(UnityEngine.UI.Graphic))

	if arg_7_1.GetComponentInChildren(typeof(Canvas)) or var_7_1 == None:
		GetOrAddComponent(arg_7_1, typeof(Image)).color = Color.New(1, 1, 1, 0)

	if var_7_1 and var_7_1.raycastTarget == False:
		var_7_1.raycastTarget = True

	local var_7_2 = arg_7_1.GetComponent(typeof(Animator))

	if var_7_2:
		var_7_2.enabled = False

	if var_0_1(arg_7_1) or arg_7_3.clearChildEvent:
		var_0_2(arg_7_1)

	var_0_3(arg_7_1)

	if not arg_7_3.keepScrollTxt:
		local var_7_3 = arg_7_1.GetComponentsInChildren(typeof(ScrollText))

		for iter_7_0 = 1, var_7_3.Length:
			local var_7_4 = var_7_3[iter_7_0 - 1]

			setActive(var_7_4.gameObject, False)

	if arg_7_1.GetComponent(typeof(Canvas)) and arg_7_1.GetComponent(typeof(GraphicRaycaster)) == None:
		GetOrAddComponent(arg_7_1, typeof(GraphicRaycaster))

	arg_7_1.sizeDelta = arg_7_2.sizeDelta

def var_0_0.UpdateSettings(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	if arg_8_3.customPosition:
		arg_8_0.SetCustomPosition(arg_8_1, arg_8_2, arg_8_3)
	else
		arg_8_0.Syn(arg_8_1, arg_8_2, arg_8_3)

	if arg_8_3.clearAllEvent:
		GetOrAddComponent(arg_8_1, typeof(CanvasGroup)).blocksRaycasts = False

def var_0_0.SetCustomPosition(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	if arg_9_3.pos:
		arg_9_1.localPosition = Vector3(arg_9_3.pos.x, arg_9_3.pos.y, arg_9_3.pos.z or 0)
	elif arg_9_3.isLevelPoint:
		local var_9_0 = pg.UIMgr.GetInstance().levelCameraComp
		local var_9_1 = arg_9_2.transform.parent.TransformPoint(arg_9_2.transform.localPosition)
		local var_9_2 = var_9_0.WorldToScreenPoint(var_9_1)
		local var_9_3 = pg.UIMgr.GetInstance().overlayCameraComp

		arg_9_1.localPosition = LuaHelper.ScreenToLocal(arg_9_0.root, var_9_2, var_9_3)
	else
		arg_9_1.position = arg_9_2.transform.position
		arg_9_1.localPosition = Vector3(arg_9_1.localPosition.x, arg_9_1.localPosition.y, 0)

	local var_9_4 = arg_9_3.scale or 1

	arg_9_1.localScale = Vector3(var_9_4, var_9_4, var_9_4)
	arg_9_1.eulerAngles = arg_9_3.eulerAngles and Vector3(arg_9_3.eulerAngles[1], arg_9_3.eulerAngles[2], arg_9_3.eulerAngles[3]) or Vector3(0, 0, 0)

local function var_0_4(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	local var_10_0 = arg_10_0.root.InverseTransformPoint(arg_10_2.transform.position)

	arg_10_1.localPosition = Vector3(var_10_0.x, var_10_0.y, 0)

	local var_10_1 = arg_10_2.transform.localScale

	arg_10_1.localScale = Vector3(var_10_1.x, var_10_1.y, var_10_1.z)

local function var_0_5(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0
	local var_11_1
	local var_11_2 = arg_11_2.image.isChild and arg_11_1.Find(arg_11_2.image.source) or GameObject.Find(arg_11_2.image.source)

	if arg_11_2.image.isRelative:
		var_11_1 = arg_11_2.image.target == "" and arg_11_0 or arg_11_0.Find(arg_11_2.image.target)
	else
		var_11_1 = GameObject.Find(arg_11_2.image.target)

	if IsNil(var_11_2) or IsNil(var_11_1):
		return

	local var_11_3 = var_11_2.GetComponent(typeof(Image))
	local var_11_4 = var_11_1.GetComponent(typeof(Image))

	if not var_11_3 or not var_11_4:
		return

	local var_11_5 = var_11_3.sprite
	local var_11_6 = var_11_4.sprite

	if var_11_5 and var_11_6 and var_11_5 != var_11_6:
		var_11_4.enabled = var_11_3.enabled

		setImageSprite(var_11_1, var_11_5)

def var_0_0.Syn(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	arg_12_0.RemoveTimer()

	arg_12_0.timer = Timer.New(function()
		var_0_4(arg_12_0, arg_12_1, arg_12_2, arg_12_3)

		if arg_12_3.image:
			var_0_5(arg_12_1, arg_12_2, arg_12_3), 0.01, -1)

	arg_12_0.timer.Start()
	arg_12_0.timer.func()

def var_0_0.RemoveTimer(arg_14_0):
	if arg_14_0.timer:
		arg_14_0.timer.Stop()

		arg_14_0.timer = None

def var_0_0.Clear(arg_15_0):
	if arg_15_0.caches and #arg_15_0.caches > 0:
		for iter_15_0, iter_15_1 in ipairs(arg_15_0.caches):
			Object.Destroy(iter_15_1.gameObject)

		arg_15_0.caches = {}

	arg_15_0.RemoveTimer()

return var_0_0
