local var_0_0 = class("ValentineQteGamePage")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._tf = arg_1_1

	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	arg_2_0.root = findTF(arg_2_0._tf, "root")
	arg_2_0.slideWay = findTF(arg_2_0._tf, "slideway")
	arg_2_0.slider = findTF(arg_2_0._tf, "slider")
	arg_2_0.goodArea = findTF(arg_2_0._tf, "good")
	arg_2_0.greatArea = findTF(arg_2_0._tf, "great")
	arg_2_0.perfectArea = findTF(arg_2_0._tf, "perfect")
	arg_2_0.scoreTxt = findTF(arg_2_0._tf, "score/Text").GetComponent(typeof(Text))
	arg_2_0.comboTxt = findTF(arg_2_0._tf, "score/combo").GetComponent(typeof(Text))
	arg_2_0.refrigerator = findTF(arg_2_0._tf, "bg/refrigerator").GetComponent(typeof(SpineAnimUI))
	arg_2_0.char = findTF(arg_2_0._tf, "bg/char").GetComponent(typeof(SpineAnimUI))
	arg_2_0.backBtn = findTF(arg_2_0._tf, "back")
	arg_2_0.puaseBtn = findTF(arg_2_0._tf, "pause")
	arg_2_0.timeTxt = findTF(arg_2_0._tf, "time/Text").GetComponent(typeof(Text))
	arg_2_0.lineTr = findTF(arg_2_0._tf, "slideway/line")

	setActive(arg_2_0.lineTr, False)

	arg_2_0.itemContainer = findTF(arg_2_0._tf, "items")
	arg_2_0.effectContainer = findTF(arg_2_0._tf, "effects")
	arg_2_0.finger = findTF(arg_2_0._tf, "finger")
	arg_2_0.gearTr = findTF(arg_2_0._tf, "gear").GetComponent(typeof(Image))
	arg_2_0.gearTrPos = arg_2_0.gearTr.transform.localPosition.y
	arg_2_0.gearSps = {
		[ValentineQteGameConst.OP_SCORE_GEAR_PERFECT] = GetSpriteFromAtlas("ui/valentineqtegame_atlas", "Perfect"),
		[ValentineQteGameConst.OP_SCORE_GEAR_GREAT] = GetSpriteFromAtlas("ui/valentineqtegame_atlas", "Great"),
		[ValentineQteGameConst.OP_SCORE_GEAR_GOOD] = GetSpriteFromAtlas("ui/valentineqtegame_atlas", "Good"),
		[ValentineQteGameConst.OP_SCORE_GEAR_MISS] = GetSpriteFromAtlas("ui/valentineqtegame_atlas", "Miss")
	}
	arg_2_0.msgBox = ValentineQteGameMsgBox.New(arg_2_0._tf.Find("msgbox"))
	arg_2_0.itemPoolMgr = ValentineQteGamePoolMgr.New(arg_2_0._tf.Find("root/item"), 2, 4)
	arg_2_0.resultWindow = ValentineQteGameResultWindow.New(arg_2_0._tf.Find("result_panel"))
	arg_2_0.countDownWindow = findTF(arg_2_0._tf, "countdown")
	arg_2_0.countDown1 = findTF(arg_2_0._tf, "countdown/1")
	arg_2_0.countDown2 = findTF(arg_2_0._tf, "countdown/2")
	arg_2_0.countDown3 = findTF(arg_2_0._tf, "countdown/3")
	arg_2_0.effectPools = {}

def var_0_0.SetUp(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	arg_3_0.onComplete = arg_3_1
	arg_3_0.onExist = arg_3_2
	arg_3_0.isClick = not arg_3_3

	arg_3_0.Show()

def var_0_0.Show(arg_4_0):
	arg_4_0.UpdateFinger()
	parallelAsync({
		function(arg_5_0)
			arg_4_0.CountDown(arg_5_0),
		function(arg_6_0)
			seriesAsync({
				function(arg_7_0)
					arg_4_0.LoadEffects(arg_7_0),
				function(arg_8_0)
					arg_4_0.InitGame(arg_8_0),
				function(arg_9_0)
					arg_4_0.Reset(arg_9_0)
			}, arg_6_0)
	}, function()
		arg_4_0.StartGame())

def var_0_0.CountDown(arg_11_0, arg_11_1):
	local function var_11_0(arg_12_0)
		setActive(arg_11_0.countDown1, arg_12_0 == 3)
		setActive(arg_11_0.countDown2, arg_12_0 == 2)
		setActive(arg_11_0.countDown3, arg_12_0 == 1)

	setActive(arg_11_0.countDownWindow, True)

	local var_11_1 = 1

	arg_11_0.countDownTimer = Timer.New(function()
		var_11_1 = var_11_1 + 1

		var_11_0(var_11_1)

		if var_11_1 == 4:
			setActive(arg_11_0.countDownWindow, False)
			arg_11_1(), 1, 3)

	arg_11_0.countDownTimer.Start()
	var_11_0(var_11_1)

def var_0_0.LoadEffects(arg_14_0, arg_14_1):
	parallelAsync({
		function(arg_15_0)
			LoadAndInstantiateAsync("ui", "chufang_Prefect", function(arg_16_0)
				SetParent(arg_16_0, arg_14_0.root)

				local var_16_0 = ValentineQteGamePoolMgr.New(arg_16_0, 1, 2)

				arg_14_0.effectPools[ValentineQteGameConst.OP_SCORE_GEAR_PERFECT] = var_16_0

				arg_15_0()),
		function(arg_17_0)
			LoadAndInstantiateAsync("ui", "chufang_Great", function(arg_18_0)
				SetParent(arg_18_0, arg_14_0.root)

				local var_18_0 = ValentineQteGamePoolMgr.New(arg_18_0, 1, 2)

				arg_14_0.effectPools[ValentineQteGameConst.OP_SCORE_GEAR_GREAT] = var_18_0

				arg_17_0()),
		function(arg_19_0)
			LoadAndInstantiateAsync("ui", "chufang_Good", function(arg_20_0)
				SetParent(arg_20_0, arg_14_0.root)

				local var_20_0 = ValentineQteGamePoolMgr.New(arg_20_0, 1, 2)

				arg_14_0.effectPools[ValentineQteGameConst.OP_SCORE_GEAR_GOOD] = var_20_0

				arg_19_0()),
		function(arg_21_0)
			LoadAndInstantiateAsync("ui", "chufang_Miss", function(arg_22_0)
				SetParent(arg_22_0, arg_14_0.root)

				local var_22_0 = ValentineQteGamePoolMgr.New(arg_22_0, 1, 2)

				arg_14_0.effectPools[ValentineQteGameConst.OP_SCORE_GEAR_MISS] = var_22_0

				arg_21_0()),
		function(arg_23_0)
			LoadAndInstantiateAsync("ui", "chufang_shiqu", function(arg_24_0)
				SetParent(arg_24_0, arg_14_0.root)

				local var_24_0 = ValentineQteGamePoolMgr.New(arg_24_0, 1, 2)

				arg_14_0.pickPool = var_24_0

				arg_23_0())
	}, arg_14_1)

def var_0_0.InitGame(arg_25_0, arg_25_1):
	arg_25_0.slideWay.sizeDelta = Vector2(ValentineQteGameConst.SLIDEWAY_WIDTH, arg_25_0.slideWay.sizeDelta.y)
	arg_25_0.slider.sizeDelta = Vector2(ValentineQteGameConst.SLIDER_WIDTH, arg_25_0.slider.sizeDelta.y)
	arg_25_0.goodArea.sizeDelta = Vector2(ValentineQteGameConst.GOOD_WIDTH, arg_25_0.goodArea.sizeDelta.y)
	arg_25_0.greatArea.sizeDelta = Vector2(ValentineQteGameConst.GREAT_WIDTH, arg_25_0.greatArea.sizeDelta.y)
	arg_25_0.perfectArea.sizeDelta = Vector2(ValentineQteGameConst.PERFECT_WIDTH, arg_25_0.perfectArea.sizeDelta.y)
	arg_25_0.scoreTxt.text = 0
	arg_25_0.comboTxt.text = 0
	arg_25_0.slideWay.localPosition = Vector3(0, arg_25_0.slideWay.localPosition.y, 0)
	arg_25_0.goodArea.localPosition = Vector3(0, arg_25_0.goodArea.localPosition.y, 0)
	arg_25_0.greatArea.localPosition = Vector3(0, arg_25_0.greatArea.localPosition.y, 0)
	arg_25_0.perfectArea.localPosition = Vector3(0, arg_25_0.perfectArea.localPosition.y, 0)

	local var_25_0 = arg_25_0.slider.sizeDelta.x * 0.5

	arg_25_0.missMinPosX, arg_25_0.missMaxPosX = arg_25_0.CalcGearArea(arg_25_0.slideWay, var_25_0)
	arg_25_0.goodMinPosX, arg_25_0.goodMaxPosX = arg_25_0.CalcGearArea(arg_25_0.goodArea, var_25_0)
	arg_25_0.greatMinPosX, arg_25_0.greatMaxPosX = arg_25_0.CalcGearArea(arg_25_0.greatArea, var_25_0)
	arg_25_0.prefectMinPosX, arg_25_0.prefectMaxPosX = arg_25_0.CalcGearArea(arg_25_0.perfectArea, var_25_0)
	arg_25_0.slider.localPosition = Vector3(arg_25_0.missMinPosX, arg_25_0.slideWay.localPosition.y, 0)
	arg_25_0.itemGenMinArea = Vector2(arg_25_0.missMinPosX - var_25_0 + 40, arg_25_0.goodMinPosX - var_25_0 - 40)
	arg_25_0.itemGenMaxArea = Vector2(arg_25_0.goodMaxPosX + var_25_0 + 40, arg_25_0.missMaxPosX + var_25_0 - 40)

	if ValentineQteGameConst.DEBUG:
		arg_25_0.InitDebugView()

	arg_25_1()

def var_0_0.Reset(arg_26_0, arg_26_1):
	arg_26_0.speedX = ValentineQteGameConst.INIT_SPEED
	arg_26_0.time = ValentineQteGameConst.GMAE_TIME
	arg_26_0.comboCnt = 0
	arg_26_0.score = 0
	arg_26_0.opCdTime = 0
	arg_26_0.elapseTimes = {}
	arg_26_0.accelerated = 0
	arg_26_0.items = {}
	arg_26_0.genItemTime = 0
	arg_26_0.gearShowTime = 0
	arg_26_0.timers = {}
	arg_26_0.startFlag = False
	arg_26_0.statistics = {
		Score = 0,
		Combo = 0,
		Great = 0,
		Perfect = 0,
		Good = 0,
		Miss = 0
	}

	arg_26_1()

def var_0_0.InitDebugView(arg_27_0):
	arg_27_0.CreateDebugLinePos("missMinPosX")
	arg_27_0.CreateDebugLinePos("missMaxPosX")
	arg_27_0.CreateDebugLinePos("goodMinPosX")
	arg_27_0.CreateDebugLinePos("goodMaxPosX")
	arg_27_0.CreateDebugLinePos("greatMinPosX")
	arg_27_0.CreateDebugLinePos("greatMaxPosX")
	arg_27_0.CreateDebugLinePos("prefectMinPosX")
	arg_27_0.CreateDebugLinePos("prefectMaxPosX")
	arg_27_0.CreateDebugArea("itemGenMinArea")
	arg_27_0.CreateDebugArea("itemGenMaxArea")

def var_0_0.CreateDebugArea(arg_28_0, arg_28_1):
	local var_28_0 = cloneTplTo(arg_28_0.lineTr, arg_28_0.lineTr.parent, arg_28_1 .. "01")

	var_28_0.localPosition = Vector3(arg_28_0[arg_28_1].x, var_28_0.localPosition.y, 0)

	setActive(var_28_0, True)

	local var_28_1 = cloneTplTo(arg_28_0.lineTr, arg_28_0.lineTr.parent, arg_28_1 .. "02")

	var_28_1.localPosition = Vector3(arg_28_0[arg_28_1].y, var_28_1.localPosition.y, 0)

	setActive(var_28_1, True)

def var_0_0.CreateDebugLinePos(arg_29_0, arg_29_1):
	local var_29_0 = cloneTplTo(arg_29_0.lineTr, arg_29_0.lineTr.parent, arg_29_1)

	var_29_0.localPosition = Vector3(arg_29_0[arg_29_1], var_29_0.localPosition.y, 0)

	setActive(var_29_0, True)

def var_0_0.CalcGearArea(arg_30_0, arg_30_1, arg_30_2):
	local var_30_0 = -arg_30_1.sizeDelta.x * 0.5 + arg_30_2
	local var_30_1 = arg_30_1.sizeDelta.x * 0.5 - arg_30_2

	return var_30_0, var_30_1

def var_0_0.StartGame(arg_31_0):
	arg_31_0.startFlag = True

	if not arg_31_0.handle:
		arg_31_0.handle = UpdateBeat.CreateListener(arg_31_0.UpdateGame, arg_31_0)

	UpdateBeat.AddListener(arg_31_0.handle)
	arg_31_0.char.SetAction("1", 0)
	onButton(arg_31_0, arg_31_0.puaseBtn, function()
		if not arg_31_0.puaseGameFlag:
			arg_31_0.PuaseGame()
			arg_31_0.msgBox.Show({
				noNo = True,
				content = ValentineQteGameMsgBox.PAUSE_TXT,
				def onYes:()
					arg_31_0.ResumeGame(),
				def onNo:()
					arg_31_0.ResumeGame()
			})
		else
			arg_31_0.ResumeGame(), SFX_PANEL)
	onButton(arg_31_0, arg_31_0.backBtn, function()
		arg_31_0.PuaseGame()
		arg_31_0.msgBox.Show({
			content = ValentineQteGameMsgBox.EXIT_TXT,
			def onYes:()
				arg_31_0.EndGame(True),
			def onNo:()
				arg_31_0.ResumeGame()
		}), SFX_PANEL)

	arg_31_0.dragDelegate = GetOrAddComponent(arg_31_0._tf, "EventTriggerListener")

	arg_31_0.dragDelegate.AddPointDownFunc(function()
		arg_31_0.isClick = True

		if arg_31_0.opCdTime <= 0 and not arg_31_0.puaseGameFlag:
			arg_31_0.Snap()

			arg_31_0.opCdTime = ValentineQteGameConst.OP_INTERVAL

		arg_31_0.UpdateFinger())

def var_0_0.UpdateFinger(arg_39_0):
	setActive(arg_39_0.finger, not arg_39_0.isClick)

def var_0_0.UpdateGame(arg_40_0):
	if arg_40_0.puaseGameFlag:
		return

	arg_40_0.HideGear()
	arg_40_0.CheckDisapperItems()
	arg_40_0.UpdateSlider()
	arg_40_0.UpdateSpeed()
	arg_40_0.UpdateTime()
	arg_40_0.UpdateOpCdTime()
	arg_40_0.CheckAndGenItem()
	arg_40_0.CheckInteraction()

def var_0_0.CheckInteraction(arg_41_0):
	local function var_41_0()
		return arg_41_0.time <= ValentineQteGameConst.OPEN_DOOR_TIME

	if not arg_41_0.isInteraction and var_41_0():
		arg_41_0.isInteraction = True

		arg_41_0.refrigerator.SetActionCallBack(function(arg_43_0)
			if arg_43_0 == "finish":
				arg_41_0.refrigerator.SetActionCallBack(None)
				arg_41_0.refrigerator.SetAction("3", 0))
		arg_41_0.refrigerator.SetAction("2", 0)

def var_0_0.HideGear(arg_44_0):
	if arg_44_0.gearShowTime <= 0:
		return

	if arg_44_0.gearShowTime - arg_44_0.time >= ValentineQteGameConst.GEAR_SHOW_TIME:
		arg_44_0.gearShowTime = 0

		setActive(arg_44_0.gearTr.gameObject, False)

def var_0_0.CheckDisapperItems(arg_45_0):
	for iter_45_0 = #arg_45_0.items, 1, -1:
		local var_45_0 = arg_45_0.items[iter_45_0]

		if var_45_0.ShouldDisapper(arg_45_0.time):
			var_45_0.Destroy()
			arg_45_0.itemPoolMgr.Enqueue(var_45_0._go)
			table.remove(arg_45_0.items, iter_45_0)

def var_0_0.CheckAndGenItem(arg_46_0):
	if #arg_46_0.items >= ValentineQteGameConst.MAX_ITEM_COUNT:
		return

	local var_46_0 = False

	if arg_46_0.genItemTime == 0 and arg_46_0.time <= ValentineQteGameConst.GMAE_TIME - ValentineQteGameConst.GEN_ITEM_FIRST_TIME or arg_46_0.genItemTime > 0 and arg_46_0.genItemTime - arg_46_0.time > ValentineQteGameConst.GEN_ITEM_INTERVAL:
		var_46_0 = True

	if var_46_0:
		arg_46_0.RandomItemPosition(0)

def var_0_0.IsVaildItemPos(arg_47_0, arg_47_1):
	local var_47_0 = arg_47_0.slider.sizeDelta.x + 80

	for iter_47_0, iter_47_1 in ipairs(arg_47_0.items):
		if not iter_47_1.IsSufficientLength(arg_47_1, var_47_0):
			return False

	return True

def var_0_0.RandomItemPosition(arg_48_0, arg_48_1):
	if arg_48_1 > 10:
		return

	local var_48_0 = math.random(1, 2) % 2 == 0 and arg_48_0.itemGenMinArea or arg_48_0.itemGenMaxArea
	local var_48_1 = math.random(var_48_0.x, var_48_0.y)

	if arg_48_0.IsVaildItemPos(var_48_1):
		arg_48_0.genItemTime = arg_48_0.time

		local var_48_2 = arg_48_0.itemPoolMgr.Dequeue()

		SetParent(var_48_2, arg_48_0.itemContainer)

		local var_48_3 = ValentineQteGameItem.New(var_48_2, Vector2(var_48_1, arg_48_0.slider.localPosition.y), arg_48_0.time)

		table.insert(arg_48_0.items, var_48_3)
	else
		arg_48_0.RandomItemPosition(arg_48_1 + 1)

def var_0_0.UpdateSlider(arg_49_0):
	local var_49_0 = arg_49_0.slider.localPosition

	if var_49_0.x == arg_49_0.missMinPosX or var_49_0.x == arg_49_0.missMaxPosX:
		arg_49_0.speedX = -arg_49_0.speedX

	local var_49_1 = math.clamp(var_49_0.x + arg_49_0.speedX * Time.deltaTime, arg_49_0.missMinPosX, arg_49_0.missMaxPosX)

	arg_49_0.slider.localPosition = Vector3(var_49_1, var_49_0.y, 0)

def var_0_0.UpdateTime(arg_50_0):
	arg_50_0.time = arg_50_0.time - Time.deltaTime

	if arg_50_0.time <= 0:
		arg_50_0.EndGame(True)

	arg_50_0.UpdateTimeText(arg_50_0.time)

def var_0_0.UpdateSpeed(arg_51_0):
	local var_51_0 = math.floor(math.ceil(ValentineQteGameConst.GMAE_TIME - arg_51_0.time) / 5)

	if var_51_0 > 0 and not arg_51_0.elapseTimes[var_51_0] and arg_51_0.accelerated + ValentineQteGameConst.INIT_SPEED < ValentineQteGameConst.MAX_SPEED:
		arg_51_0.elapseTimes[var_51_0] = True
		arg_51_0.accelerated = arg_51_0.accelerated + ValentineQteGameConst.SPEED_UP

		if arg_51_0.speedX < 0:
			arg_51_0.speedX = arg_51_0.speedX - arg_51_0.accelerated
		else
			arg_51_0.speedX = arg_51_0.speedX + arg_51_0.accelerated

def var_0_0.UpdateOpCdTime(arg_52_0):
	if arg_52_0.opCdTime > 0:
		arg_52_0.opCdTime = math.max(0, arg_52_0.opCdTime - Time.deltaTime)

def var_0_0.Snap(arg_53_0):
	local var_53_0 = arg_53_0.slider.localPosition.x
	local var_53_1 = arg_53_0.GetScoreGear(var_53_0)
	local var_53_2 = {}
	local var_53_3 = False

	if var_53_1 == ValentineQteGameConst.OP_SCORE_GEAR_GREAT:
		arg_53_0.comboCnt = arg_53_0.comboCnt + 1
		arg_53_0.statistics.Great = arg_53_0.statistics.Great + 1
	elif var_53_1 == ValentineQteGameConst.OP_SCORE_GEAR_PERFECT:
		arg_53_0.comboCnt = arg_53_0.comboCnt + 1
		arg_53_0.statistics.Perfect = arg_53_0.statistics.Perfect + 1
	elif arg_53_0.CanPickItem(var_53_0, var_53_2):
		arg_53_0.comboCnt = arg_53_0.comboCnt + 1
		var_53_1 = ValentineQteGameConst.OP_SCORE_GEAR_PERFECT
		arg_53_0.statistics.Perfect = arg_53_0.statistics.Perfect + 1

		arg_53_0.PickItems(var_53_2)

		var_53_3 = True
	elif var_53_1 == ValentineQteGameConst.OP_SCORE_GEAR_MISS:
		arg_53_0.comboCnt = 0
		arg_53_0.statistics.Miss = arg_53_0.statistics.Miss + 1
	elif var_53_1 == ValentineQteGameConst.OP_SCORE_GEAR_GOOD:
		arg_53_0.comboCnt = 0
		arg_53_0.statistics.Good = arg_53_0.statistics.Good + 1

	local var_53_4 = arg_53_0.GetScore(var_53_1, arg_53_0.comboCnt)

	arg_53_0.score = arg_53_0.score + var_53_4

	arg_53_0.UpdateScoreText(arg_53_0.score)
	arg_53_0.UpdateComboText(arg_53_0.comboCnt)

	if arg_53_0.comboCnt > arg_53_0.statistics.Combo:
		arg_53_0.statistics.Combo = arg_53_0.comboCnt

	arg_53_0.UpdateGear(var_53_1, var_53_3)

def var_0_0.UpdateGear(arg_54_0, arg_54_1, arg_54_2):
	if LeanTween.isTweening(arg_54_0.gearTr.gameObject):
		LeanTween.cancel(arg_54_0.gearTr.gameObject)

	arg_54_0.gearTr.sprite = arg_54_0.gearSps[arg_54_1]

	arg_54_0.gearTr.SetNativeSize()

	arg_54_0.gearShowTime = arg_54_0.time

	setActive(arg_54_0.gearTr.gameObject, True)

	if arg_54_2:
		setActive(arg_54_0.gearTr.gameObject, False)
		arg_54_0.GenEffect(ValentineQteGameConst.OP_SCORE_GEAR_GREAT)
		arg_54_0.PlaySound(ValentineQteGameConst.SOUND_PICK_ITEM)
	else
		arg_54_0.GenEffect(arg_54_1)
		arg_54_0.GearAnim()
		arg_54_0.PlaySound(ValentineQteGameConst.GEAR_SOUND[arg_54_1])

def var_0_0.PlaySound(arg_55_0, arg_55_1):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(arg_55_1)

def var_0_0.GearAnim(arg_56_0):
	arg_56_0.gearTr.gameObject.transform.localPosition = Vector3(arg_56_0.gearTr.gameObject.transform.localPosition.x, arg_56_0.gearTrPos, 0)

	LeanTween.value(arg_56_0.gearTr.gameObject, arg_56_0.gearTrPos, arg_56_0.gearTrPos + 50, 0.3).setOnUpdate(System.Action_float(function(arg_57_0)
		arg_56_0.gearTr.gameObject.transform.localPosition = Vector3(arg_56_0.gearTr.gameObject.transform.localPosition.x, arg_57_0, 0))).setOnComplete(System.Action(function()
		setActive(arg_56_0.gearTr.gameObject, False)))

def var_0_0.GenEffect(arg_59_0, arg_59_1):
	local var_59_0 = arg_59_0.effectPools[arg_59_1]
	local var_59_1 = var_59_0.Dequeue()

	SetParent(var_59_1, arg_59_0.effectContainer)

	var_59_1.transform.localPosition = Vector3(arg_59_0.slider.localPosition.x, arg_59_0.slider.localPosition.y, -100)

	local var_59_2 = Timer.New(function()
		var_59_0.Enqueue(var_59_1), 2, 1)

	var_59_2.Start()
	table.insert(arg_59_0.timers, var_59_2)

def var_0_0.CanPickItem(arg_61_0, arg_61_1, arg_61_2):
	for iter_61_0, iter_61_1 in ipairs(arg_61_0.items):
		if iter_61_1.IsOverlap(arg_61_0.slider):
			table.insert(arg_61_2, iter_61_1)

	return #arg_61_2 > 0

def var_0_0.PickItems(arg_62_0, arg_62_1):
	for iter_62_0, iter_62_1 in ipairs(arg_62_1):
		arg_62_0.PlayPickAnim(iter_62_1, function()
			iter_62_1.Destroy()
			arg_62_0.itemPoolMgr.Enqueue(iter_62_1._tf))
		table.removebyvalue(arg_62_0.items, iter_62_1)

def var_0_0.PlayPickAnim(arg_64_0, arg_64_1, arg_64_2):
	local var_64_0 = arg_64_1._tf.localPosition.y

	LeanTween.value(arg_64_1._go, var_64_0, var_64_0 + 70, 0.3).setOnUpdate(System.Action_float(function(arg_65_0)
		arg_64_1._tf.localPosition = Vector3(arg_64_1._tf.localPosition.x, arg_65_0, 0))).setOnComplete(System.Action(function()
		local var_66_0 = arg_64_0.pickPool.Dequeue()

		SetParent(var_66_0, arg_64_0.effectContainer)

		var_66_0.transform.localPosition = Vector3(arg_64_1._tf.localPosition.x, arg_64_1._tf.localPosition.y, -100)

		local var_66_1 = Timer.New(function()
			arg_64_0.pickPool.Enqueue(var_66_0), 2, 1)

		var_66_1.Start()
		table.insert(arg_64_0.timers, var_66_1)
		arg_64_2()))

def var_0_0.UpdateTimeText(arg_68_0, arg_68_1):
	local var_68_0 = math.ceil(arg_68_1)

	if var_68_0 <= 0:
		arg_68_0.timeTxt.text = "0"
	else
		arg_68_0.timeTxt.text = math.max(0, var_68_0)

def var_0_0.UpdateScoreText(arg_69_0, arg_69_1):
	arg_69_0.scoreTxt.text = arg_69_1

def var_0_0.UpdateComboText(arg_70_0, arg_70_1):
	arg_70_0.comboTxt.text = arg_70_1

def var_0_0.GetScoreGear(arg_71_0, arg_71_1):
	if arg_71_1 >= arg_71_0.prefectMinPosX and arg_71_1 <= arg_71_0.prefectMaxPosX:
		return ValentineQteGameConst.OP_SCORE_GEAR_PERFECT

	if arg_71_1 >= arg_71_0.greatMinPosX and arg_71_1 <= arg_71_0.greatMaxPosX:
		return ValentineQteGameConst.OP_SCORE_GEAR_GREAT

	if arg_71_1 >= arg_71_0.goodMinPosX and arg_71_1 <= arg_71_0.goodMaxPosX:
		return ValentineQteGameConst.OP_SCORE_GEAR_GOOD

	return ValentineQteGameConst.OP_SCORE_GEAR_MISS

def var_0_0.GetScore(arg_72_0, arg_72_1, arg_72_2):
	local var_72_0 = ValentineQteGameConst.OP_SCORE[arg_72_1]
	local var_72_1 = ValentineQteGameConst.BASE_OP_SCORE * var_72_0
	local var_72_2 = 0

	for iter_72_0, iter_72_1 in ipairs(ValentineQteGameConst.COMBO_EXTRA_SCORE_RATIO):
		local var_72_3 = iter_72_1[1]
		local var_72_4 = iter_72_1[2]
		local var_72_5 = iter_72_1[3]

		if var_72_3 <= arg_72_2 and arg_72_2 <= var_72_4:
			var_72_2 = var_72_5

			break

	return var_72_1 + ValentineQteGameConst.BASE_OP_SCORE * var_72_2 * 0.01

def var_0_0.PuaseGame(arg_73_0):
	arg_73_0.puaseGameFlag = True

	arg_73_0.char.Pause()

def var_0_0.ResumeGame(arg_74_0):
	arg_74_0.puaseGameFlag = False

	arg_74_0.char.Resume()

def var_0_0.EndGame(arg_75_0, arg_75_1):
	if arg_75_0.handle:
		UpdateBeat.RemoveListener(arg_75_0.handle)

	ClearEventTrigger(arg_75_0.dragDelegate)
	removeOnButton(arg_75_0.puaseBtn)

	if arg_75_1:
		arg_75_0.statistics.Score = arg_75_0.score

		arg_75_0.resultWindow.Show(arg_75_0.statistics, function()
			arg_75_0.Destroy())

	if arg_75_0.onComplete and arg_75_1:
		arg_75_0.onComplete()

	arg_75_0.onComplete = None

def var_0_0.ExitGame(arg_77_0):
	arg_77_0.EndGame(False)

	if arg_77_0.onExist:
		arg_77_0.onExist()

		arg_77_0.onExist = None

def var_0_0.onBackPressed(arg_78_0):
	if arg_78_0.startFlag and not arg_78_0.puaseGameFlag:
		triggerButton(arg_78_0.puaseBtn)

		return True

	if isActive(arg_78_0.msgBox._tf):
		triggerButton(arg_78_0.msgBox.cancelBtn)

		return True

	return False

def var_0_0.Destroy(arg_79_0):
	if arg_79_0.countDownTimer:
		arg_79_0.countDownTimer.Stop()

		arg_79_0.countDownTimer = None

	if LeanTween.isTweening(arg_79_0.gearTr.gameObject):
		LeanTween.cancel(arg_79_0.gearTr.gameObject)

	for iter_79_0, iter_79_1 in ipairs(arg_79_0.timers):
		iter_79_1.Stop()

	arg_79_0.timers = None

	for iter_79_2, iter_79_3 in pairs(arg_79_0.effectPools):
		iter_79_3.Destroy()

	arg_79_0.effectPools = None

	arg_79_0.refrigerator.SetActionCallBack(None)

	if arg_79_0.msgBox:
		arg_79_0.msgBox.Destroy()

		arg_79_0.msgBox = None

	if arg_79_0.resultWindow:
		arg_79_0.resultWindow.Destroy()

		arg_79_0.resultWindow = None

	arg_79_0.ExitGame()
	pg.DelegateInfo.Dispose(arg_79_0)

	if arg_79_0.itemPoolMgr:
		arg_79_0.itemPoolMgr.Destroy()

		arg_79_0.itemPoolMgr = None

	arg_79_0.gearSps = None

return var_0_0
