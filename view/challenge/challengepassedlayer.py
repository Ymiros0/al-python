local var_0_0 = class("ChallengePassedLayer", import("..base.BaseUI"))

var_0_0.BOSS_NUM = 5
var_0_0.GROW_TIME = 0.55

def var_0_0.getUIName(arg_1_0):
	return "ChallengePassedUI"

def var_0_0.init(arg_2_0):
	arg_2_0.findUI()
	arg_2_0.initData()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.tweenObjs = {}

	pg.UIMgr.GetInstance().OverlayPanel(arg_3_0._tf)
	arg_3_0.updatePainting(arg_3_0.paintingName, arg_3_0.paintingTF, arg_3_0.paintingShadow1, True)

	if arg_3_0.paintingNamemNext:
		arg_3_0.updatePainting(arg_3_0.paintingNamemNext, arg_3_0.paintingNextTF, arg_3_0.paintingNextShadow1)

	arg_3_0.updateSlider(arg_3_0.curIndex)
	arg_3_0.moveSlider(arg_3_0.curIndex)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.emit(var_0_0.ON_CLOSE))
	arg_3_0._tf.GetComponent("DftAniEvent").SetEndEvent(function(arg_5_0)
		arg_3_0.emit(var_0_0.ON_CLOSE))

def var_0_0.willExit(arg_6_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_6_0._tf)
	LeanTween.cancel(go(arg_6_0.slider))

	for iter_6_0, iter_6_1 in ipairs(arg_6_0.tweenObjs):
		LeanTween.cancel(iter_6_1)

	arg_6_0.tweenObjs = {}

def var_0_0.onBackPressed(arg_7_0):
	triggerButton(arg_7_0._tf)

def var_0_0.findUI(arg_8_0):
	arg_8_0.bg = arg_8_0.findTF("BG")
	arg_8_0.paintingTF = arg_8_0.findTF("Painting")
	arg_8_0.paintingShadow1 = arg_8_0.findTF("Painting/PaintingShadow1")
	arg_8_0.paintingNextTF = arg_8_0.findTF("PaintingNext")
	arg_8_0.paintingNextShadow1 = arg_8_0.findTF("PaintingNext/PaintingShadow1")
	arg_8_0.material1 = arg_8_0.findTF("material1").GetComponent(typeof(Image)).material
	arg_8_0.slider = arg_8_0.findTF("Slider")
	arg_8_0.squareContainer = arg_8_0.findTF("SquareList", arg_8_0.slider)
	arg_8_0.squareTpl = arg_8_0.findTF("Squre", arg_8_0.slider)
	arg_8_0.squareList = UIItemList.New(arg_8_0.squareContainer, arg_8_0.squareTpl)
	arg_8_0.sliderSC = GetComponent(arg_8_0.slider, "Slider")

def var_0_0.initData(arg_9_0):
	local var_9_0 = arg_9_0.contextData.mode
	local var_9_1 = getProxy(ChallengeProxy).getUserChallengeInfo(var_9_0)

	arg_9_0.curIndex = var_9_1.getLevel()

	local var_9_2 = arg_9_0.curIndex % ChallengeConst.BOSS_NUM

	if var_9_2 == 0:
		var_9_2 = ChallengeConst.BOSS_NUM

	local var_9_3 = var_9_1.getDungeonIDList()
	local var_9_4 = var_9_3[var_9_2]
	local var_9_5 = 0

	if var_9_0 == ChallengeProxy.MODE_CASUAL:
		if var_9_2 != ChallengeConst.BOSS_NUM:
			var_9_5 = var_9_3[var_9_2 + 1]
	elif var_9_2 == ChallengeConst.BOSS_NUM:
		var_9_5 = var_9_1.getNextInfiniteDungeonIDList()[1]
	else
		var_9_5 = var_9_3[var_9_2 + 1]

	arg_9_0.paintingName = pg.expedition_challenge_template[var_9_4].char_icon[1]

	if var_9_5 != 0:
		arg_9_0.paintingNamemNext = pg.expedition_challenge_template[var_9_5].char_icon[1]

def var_0_0.addListener(arg_10_0):
	onButton(arg_10_0, arg_10_0._tf, function()
		LeanTween.cancel(go(arg_10_0.slider))
		arg_10_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)

def var_0_0.updatePainting(arg_12_0, arg_12_1, arg_12_2, arg_12_3, arg_12_4):
	local function var_12_0(arg_13_0)
		arg_13_0.material.SetFloat("_LineGray", 0.3)
		arg_13_0.material.SetFloat("_TearDistance", 0)
		LeanTween.cancel(arg_13_0.gameObject)
		table.insert(arg_12_0.tweenObjs, arg_13_0.gameObject)
		LeanTween.value(arg_13_0.gameObject, 0, 2, 2).setLoopClamp().setOnUpdate(System.Action_float(function(arg_14_0)
			if arg_14_0 >= 1.2:
				arg_13_0.material.SetFloat("_LineGray", 0.3)
			elif arg_14_0 >= 1.1:
				arg_13_0.material.SetFloat("_LineGray", 0.45)
			elif arg_14_0 >= 1.03:
				arg_13_0.material.SetFloat("_TearDistance", 0)
			elif arg_14_0 >= 1:
				arg_13_0.material.SetFloat("_TearDistance", 0.3)
			elif arg_14_0 >= 0.35:
				arg_13_0.material.SetFloat("_LineGray", 0.3)
			elif arg_14_0 >= 0.3:
				arg_13_0.material.SetFloat("_LineGray", 0.4)
			elif arg_14_0 >= 0.25:
				arg_13_0.material.SetFloat("_LineGray", 0.3)
			elif arg_14_0 >= 0.2:
				arg_13_0.material.SetFloat("_LineGray", 0.4)))

	setPaintingPrefab(arg_12_2, arg_12_1, "chuanwu")

	local var_12_1 = arg_12_0.findTF("fitter", arg_12_2).GetChild(0)

	if var_12_1:
		local var_12_2 = GetComponent(var_12_1, "MeshImage")

		if arg_12_4:
			var_12_2.material = arg_12_0.material1

			var_12_2.material.SetFloat("_LineDensity", 7)
			var_12_0(var_12_2)

	setPaintingPrefabAsync(arg_12_3, arg_12_1, "chuanwu")

	local var_12_3 = arg_12_0.findTF("fitter", arg_12_3).GetChild(0)

	if var_12_3:
		var_12_3.GetComponent("Image").color = Color.New(1, 1, 1, 0.15)

	arg_12_3.localScale = Vector3(2.2, 2.2, 1)

def var_0_0.updateSlider(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_1 or arg_15_0.curIndex

	if var_15_0 > ChallengeConst.BOSS_NUM:
		var_15_0 = var_15_0 % ChallengeConst.BOSS_NUM == 0 and ChallengeConst.BOSS_NUM or var_15_0 % ChallengeConst.BOSS_NUM

	local var_15_1 = 1 / (ChallengeConst.BOSS_NUM - 1)
	local var_15_2 = (var_15_0 - 1) * var_15_1

	arg_15_0.sliderSC.value = var_15_2

	arg_15_0.squareList.make(function(arg_16_0, arg_16_1, arg_16_2)
		local var_16_0 = arg_15_0.findTF("UnFinished", arg_16_2)
		local var_16_1 = arg_15_0.findTF("Finished", arg_16_2)
		local var_16_2 = arg_15_0.findTF("Challengeing", arg_16_2)
		local var_16_3 = arg_15_0.findTF("Arrow", arg_16_2)

		local function var_16_4()
			setActive(var_16_1, True)
			setActive(var_16_0, False)
			setActive(var_16_2, False)

		local function var_16_5()
			setActive(var_16_1, False)
			setActive(var_16_0, True)
			setActive(var_16_2, False)

		local function var_16_6()
			setActive(var_16_1, False)
			setActive(var_16_0, False)
			setActive(var_16_2, True)

		if arg_16_0 == UIItemList.EventUpdate:
			if arg_16_1 + 1 < var_15_0:
				setActive(var_16_3, False)
				var_16_4()
			elif arg_16_1 + 1 == var_15_0:
				setActive(var_16_3, True)
				var_16_6()
			elif arg_16_1 + 1 > var_15_0:
				setActive(var_16_3, False)
				var_16_5())
	arg_15_0.squareList.align(ChallengeConst.BOSS_NUM)

def var_0_0.moveSlider(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_1 or arg_20_0.curIndex

	if var_20_0 > ChallengeConst.BOSS_NUM:
		var_20_0 = var_20_0 % ChallengeConst.BOSS_NUM == 0 and ChallengeConst.BOSS_NUM or var_20_0 % ChallengeConst.BOSS_NUM

	local var_20_1 = 1 / (ChallengeConst.BOSS_NUM - 1)
	local var_20_2 = (var_20_0 - 1) * var_20_1
	local var_20_3 = var_20_0 * var_20_1

	LeanTween.value(go(arg_20_0.slider), var_20_2, var_20_3, var_0_0.GROW_TIME).setDelay(1.4).setOnUpdate(System.Action_float(function(arg_21_0)
		arg_20_0.sliderSC.value = arg_21_0)).setOnComplete(System.Action(function()
		arg_20_0.updateSlider(var_20_0 + 1)))

return var_0_0
