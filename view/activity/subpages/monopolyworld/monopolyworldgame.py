local var_0_0 = class("MonopolyWorldGame")
local var_0_1 = 117
local var_0_2 = 60
local var_0_3 = {
	{
		0,
		4007,
		4008,
		4009,
		4010,
		0
	},
	{
		4005,
		4006,
		0,
		0,
		4011,
		4012
	},
	{
		4004,
		0,
		0,
		0,
		0,
		4013
	},
	{
		4003,
		4002,
		0,
		0,
		4015,
		4014
	},
	{
		0,
		4001,
		4018,
		4017,
		4016,
		0
	}
}
local var_0_4 = "mengya"
local var_0_5 = "monopoly_world_tip1"
local var_0_6 = "monopoly_world_tip2"
local var_0_7 = "monopoly_world_tip3"
local var_0_8 = 0.6
local var_0_9 = "dafuweng_gold"
local var_0_10 = "dafuweng_oil"
local var_0_11 = "dafuweng_event"
local var_0_12 = "dafuweng_walk"
local var_0_13 = "dafuweng_stand"
local var_0_14 = "dafuweng_walk"
local var_0_15 = "dafuweng_run"
local var_0_16 = "dafuweng_touch"
local var_0_17 = "cell gold"
local var_0_18 = "cell move"
local var_0_19 = "cell oil"
local var_0_20 = "cell event"
local var_0_21 = "cell item"
local var_0_22 = {
	{
		path_length = 1,
		name = "gulitemengya_1",
		cell_type = var_0_18
	},
	{
		path_length = 2,
		name = "gulitemengya_2",
		cell_type = var_0_18
	},
	{
		path_length = 3,
		name = "gulitemengya_3",
		cell_type = var_0_18
	},
	{
		name = "gulitemengya_daoju",
		cell_type = var_0_21
	},
	{
		name = "gulitemengya_jinbi",
		cell_type = var_0_17
	},
	{
		name = "gulitemengya_mingyun",
		cell_type = var_0_20
	},
	{
		name = "gulitemengya_shiyou",
		cell_type = var_0_19
	}
}
local var_0_23 = {
	84180,
	84181,
	84183,
	84179,
	84182
}
local var_0_24
local var_0_25

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._binder = arg_1_1
	arg_1_0._tf = arg_1_2
	arg_1_0._event = arg_1_3

	arg_1_0.initData()
	arg_1_0.initUI()
	arg_1_0.initEvent()

def var_0_0.initData(arg_2_0):
	arg_2_0.leftCount = 0
	arg_2_0.inAnimatedFlag = False
	arg_2_0.mapCells = {}

def var_0_0.initUI(arg_3_0):
	arg_3_0.tplMapCell = findTF(arg_3_0._tf, "tplMapCell")
	arg_3_0.gameTipUI1 = findTF(arg_3_0._tf, "btnStart/desc")

	setText(arg_3_0.gameTipUI1, i18n(var_0_5))

	arg_3_0.gameTipUI2 = findTF(arg_3_0._tf, "bg/desc")

	setText(arg_3_0.gameTipUI2, "")

	arg_3_0.mapContainer = findTF(arg_3_0._tf, "mapContainer")
	arg_3_0.char = findTF(arg_3_0._tf, "mapContainer/char")

	setActive(arg_3_0.char, False)

	arg_3_0.btnStart = findTF(arg_3_0._tf, "btnStart")
	arg_3_0.effectStart = findTF(arg_3_0.btnStart, "gulitemengya_pingmu")
	arg_3_0.btnHelp = findTF(arg_3_0._tf, "topRight/btnHelp")
	arg_3_0.labelLeftCount = findTF(arg_3_0.btnStart, "times")
	arg_3_0.btnBack = findTF(arg_3_0._tf, "leftTop/back")

	arg_3_0.initMap()
	arg_3_0.initChar()
	arg_3_0.initFurn()

def var_0_0.initFurn(arg_4_0):
	local var_4_0 = findTF(arg_4_0._tf, "bg/mask/event").GetComponent("HScrollSnap")

	arg_4_0.bannerCanvas = GetComponent(findTF(arg_4_0._tf, "bg/mask"), typeof(CanvasGroup))

	var_4_0.Init()

	local var_4_1 = findTF(var_4_0, "content")
	local var_4_2 = findTF(var_4_0, "item")
	local var_4_3 = findTF(arg_4_0._tf, "bg/dots")
	local var_4_4 = findTF(arg_4_0._tf, "bg/dot")

	setActive(var_4_2, False)
	setActive(var_4_4, False)

	arg_4_0.furnItems = {}

	for iter_4_0 = 0, #var_0_23 - 1:
		cloneTplTo(var_4_4, var_4_3)

		local var_4_5 = Instantiate(var_4_2)

		var_0_24 = pg.furniture_data_template[var_0_23[iter_4_0 + 1]]
		var_0_25 = var_0_24.icon

		GetImageSpriteFromAtlasAsync("ui/monopolyworldui_atlas", var_0_25, findTF(var_4_5, "img"), True)
		var_4_0.AddChild(var_4_5)
		setActive(var_4_5, True)
		table.insert(arg_4_0.furnItems, var_4_5)

	arg_4_0.bannerSnap = var_4_0
	arg_4_0.bannerContent = var_4_1
	arg_4_0.bannerDots = var_4_3
	arg_4_0.furnNames = {}

	for iter_4_1 = 1, #var_0_23:
		table.insert(arg_4_0.furnNames, findTF(arg_4_0._tf, "bg/furnName/img" .. iter_4_1))

	local function var_4_6()
		for iter_5_0 = 1, #var_0_23:
			if iter_5_0 == arg_4_0.bannerSnap.CurrentScreen() + 1:
				if not isActive(arg_4_0.furnNames[iter_5_0]):
					setActive(arg_4_0.furnNames[iter_5_0], True)
			elif isActive(arg_4_0.furnNames[iter_5_0]):
				setActive(arg_4_0.furnNames[iter_5_0], False)

	arg_4_0.funrTimer = Timer.New(var_4_6, 0.2, -1)

	arg_4_0.funrTimer.Start()
	var_4_6()

def var_0_0.initEvent(arg_6_0):
	onButton(arg_6_0._binder, arg_6_0.btnStart, function()
		if arg_6_0.inAnimatedFlag:
			return

		if arg_6_0.leftCount and arg_6_0.leftCount <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_count_noenough"))

			return

		arg_6_0.changeAnimeState(True)
		setActive(arg_6_0.btnStart, True)
		arg_6_0._event.emit(MonopolyWorldScene.ON_START, arg_6_0.activity.id, function(arg_8_0)
			if arg_8_0 and arg_8_0 > 0:
				arg_6_0.showRollAnimated(arg_8_0)), SFX_PANEL)
	onButton(arg_6_0._binder, arg_6_0.btnHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_monopoly_world.tip
		}), SFX_PANEL)
	onButton(arg_6_0._binder, arg_6_0.btnBack, function()
		if not arg_6_0.inAnimatedFlag:
			arg_6_0._event.emit(BaseUI.ON_BACK), SFX_PANEL)
	onButton(arg_6_0._binder, findTF(arg_6_0.char, "click"), function()
		if not arg_6_0.model or arg_6_0.inAnimatedFlag:
			return

		arg_6_0.changeCharAction(var_0_16, 1, function()
			arg_6_0.changeCharAction(var_0_13)), SFX_PANEL)

def var_0_0.showRollAnimated(arg_13_0, arg_13_1):
	seriesAsync({
		function(arg_14_0)
			setActive(arg_13_0.effectStart, True)
			GetComponent(findTF(arg_13_0.btnStart, "anim"), typeof(Animator)).Play("start", -1, 0)
			LeanTween.delayedCall(1, System.Action(function()
				for iter_15_0 = 1, 6:
					local var_15_0 = findTF(arg_13_0.btnStart, "num/" .. iter_15_0)

					if iter_15_0 != arg_13_1:
						setActive(var_15_0, False)
					else
						setActive(var_15_0, True)))
			LeanTween.delayedCall(2, System.Action(function()
				arg_14_0()))
	}, function()
		arg_13_0.useCount = arg_13_0.useCount + 1
		arg_13_0.leftCount = arg_13_0.leftCount - 1
		arg_13_0.step = arg_13_1

		arg_13_0.updataUI()
		arg_13_0.checkCharActive())

def var_0_0.checkCountStory(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_0.useCount
	local var_18_1 = arg_18_0.activity.getDataConfig("story") or {}
	local var_18_2 = _.detect(var_18_1, function(arg_19_0)
		return arg_19_0[1] == var_18_0)

	if var_18_2:
		pg.NewStoryMgr.GetInstance().Play(var_18_2[2], arg_18_1)
	else
		arg_18_1()

def var_0_0.changeAnimeState(arg_20_0, arg_20_1):
	if arg_20_1:
		arg_20_0.btnStart.GetComponent(typeof(Image)).raycastTarget = False
		arg_20_0.inAnimatedFlag = True

		arg_20_0._event.emit(ActivityMainScene.LOCK_ACT_MAIN, True)
	else
		arg_20_0.inAnimatedFlag = False
		arg_20_0.btnStart.GetComponent(typeof(Image)).raycastTarget = True

		arg_20_0._event.emit(ActivityMainScene.LOCK_ACT_MAIN, False)

def var_0_0.initMap(arg_21_0):
	local var_21_0 = var_0_3

	arg_21_0.mapCells = {}

	for iter_21_0 = 1, #var_21_0:
		local var_21_1 = iter_21_0 - 1
		local var_21_2 = {
			x = -var_21_1 * var_0_1,
			y = -var_21_1 * var_0_2
		}
		local var_21_3 = var_21_0[iter_21_0]

		for iter_21_1 = 1, #var_21_3:
			local var_21_4 = iter_21_1 - 1
			local var_21_5 = var_21_3[iter_21_1]

			if var_21_5 > 0:
				local var_21_6 = cloneTplTo(arg_21_0.tplMapCell, arg_21_0.mapContainer, tostring(var_21_5))
				local var_21_7 = Vector2(var_0_1 * var_21_4 + var_21_2.x, -var_0_2 * var_21_4 + var_21_2.y)

				var_21_6.localPosition = var_21_7

				local var_21_8 = pg.activity_event_monopoly_map[var_21_5].icon
				local var_21_9 = GetSpriteFromAtlas("ui/monopolyworldui_atlas", var_21_8)

				findTF(var_21_6, "image").GetComponent(typeof(Image)).sprite = var_21_9

				findTF(var_21_6, "image").GetComponent(typeof(Image)).SetNativeSize()

				local var_21_10 = {
					col = var_21_4,
					row = var_21_1,
					mapId = var_21_5,
					tf = var_21_6,
					icon = var_21_8,
					position = var_21_7
				}

				table.insert(arg_21_0.mapCells, var_21_10)

	table.sort(arg_21_0.mapCells, function(arg_22_0, arg_22_1)
		return arg_22_0.mapId < arg_22_1.mapId)

def var_0_0.initChar(arg_23_0):
	PoolMgr.GetInstance().GetSpineChar(var_0_4, True, function(arg_24_0)
		arg_23_0.model = arg_24_0
		arg_23_0.model.transform.localScale = Vector3.one
		arg_23_0.model.transform.localPosition = Vector3.zero

		arg_23_0.model.transform.SetParent(arg_23_0.char, False)

		arg_23_0.anim = arg_23_0.model.GetComponent(typeof(SpineAnimUI))

		arg_23_0.changeCharAction(var_0_13, 0, None)
		arg_23_0.checkCharActive()

		if arg_23_0.pos:
			arg_23_0.updataCharDirect(arg_23_0.pos, False))

def var_0_0.updataCharDirect(arg_25_0, arg_25_1, arg_25_2):
	if arg_25_0.model:
		local var_25_0 = arg_25_0.mapCells[arg_25_1].position
		local var_25_1 = arg_25_1 + 1 > #arg_25_0.mapCells and 1 or arg_25_1 + 1
		local var_25_2 = arg_25_0.mapCells[var_25_1]
		local var_25_3 = arg_25_0.getMoveType(arg_25_0.mapCells[arg_25_1].mapId, arg_25_0.mapCells[var_25_1].mapId, arg_25_2) or arg_25_0.char.localScale.x

		arg_25_0.char.localScale = Vector3(var_25_3, arg_25_0.char.localScale.y, arg_25_0.char.localScale.z)

def var_0_0.getMoveType(arg_26_0, arg_26_1, arg_26_2, arg_26_3):
	local var_26_0 = var_0_3
	local var_26_1 = {}
	local var_26_2 = {}

	for iter_26_0 = 1, #var_26_0:
		local var_26_3 = var_26_0[iter_26_0]

		for iter_26_1 = 1, #var_26_3:
			local var_26_4 = var_26_3[iter_26_1]

			if var_26_4 == arg_26_1:
				var_26_1 = {
					x = iter_26_1,
					y = iter_26_0
				}

			if var_26_4 == arg_26_2:
				var_26_2 = {
					x = iter_26_1,
					y = iter_26_0
				}

	local var_26_5

	if var_26_2.y > var_26_1.y:
		var_26_5 = -var_0_8
	elif var_26_2.y < var_26_1.y:
		var_26_5 = var_0_8
	elif var_26_2.x > var_26_1.x:
		var_26_5 = var_0_8
	elif var_26_2.x < var_26_1.x:
		var_26_5 = -var_0_8

	return var_26_5

def var_0_0.checkCharActive(arg_27_0):
	if arg_27_0.anim:
		if arg_27_0.effectId and arg_27_0.effectId > 0:
			arg_27_0.changeAnimeState(True)
			arg_27_0.checkEffect(function()
				arg_27_0.changeAnimeState(False)
				arg_27_0.checkCharActive())
		elif arg_27_0.step and arg_27_0.step > 0:
			arg_27_0.changeAnimeState(True)
			arg_27_0.checkStep(function()
				arg_27_0.changeAnimeState(False)
				arg_27_0.checkCharActive())
		elif arg_27_0.activity:
			arg_27_0.activity = getProxy(ActivityProxy).getActivityById(arg_27_0.activity.id)

			arg_27_0.updataActivity(arg_27_0.activity)

def var_0_0.firstUpdata(arg_30_0, arg_30_1):
	arg_30_0.activityDataUpdata(arg_30_1)
	arg_30_0.updataUI()
	arg_30_0.updataChar()
	arg_30_0.checkCharActive()

def var_0_0.updataActivity(arg_31_0, arg_31_1):
	arg_31_0.activityDataUpdata(arg_31_1)
	arg_31_0.updataUI()

def var_0_0.activityDataUpdata(arg_32_0, arg_32_1):
	arg_32_0.activity = arg_32_1

	local var_32_0 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_32_1 = arg_32_0.activity.data1

	arg_32_0.totalCnt = math.ceil((var_32_0 - var_32_1) / 86400) * arg_32_0.activity.getDataConfig("daily_time") + arg_32_0.activity.data1_list[1]
	arg_32_0.useCount = arg_32_0.activity.data1_list[2]
	arg_32_0.leftCount = arg_32_0.totalCnt - arg_32_0.useCount

	if arg_32_0.turnCnt and arg_32_0.turnCnt != arg_32_0.activity.data1_list[3] - 1:
		arg_32_0.autoShowScreen = None

	arg_32_0.turnCnt = arg_32_0.activity.data1_list[3] - 1
	arg_32_0.leftDropShipCnt = 8 - arg_32_0.turnCnt

	local var_32_2 = arg_32_0.activity.data2_list[2]

	arg_32_0.advanceTotalCnt = #arg_32_1.getDataConfig("reward")
	arg_32_0.isAdvanceRp = arg_32_0.advanceTotalCnt - var_32_2 > 0

	local var_32_3 = arg_32_0.activity.data2_list[1]

	arg_32_0.leftAwardCnt = var_32_3 - var_32_2
	arg_32_0.advanceRpCount = math.max(0, math.min(var_32_3, arg_32_0.advanceTotalCnt) - var_32_2)
	arg_32_0.commonRpCount = math.max(0, var_32_3 - arg_32_0.advanceTotalCnt) - math.max(0, var_32_2 - arg_32_0.advanceTotalCnt)

	local var_32_4 = arg_32_1.getDataConfig("reward_time")

	arg_32_0.nextredPacketStep = var_32_4 - arg_32_0.useCount % var_32_4
	arg_32_0.pos = arg_32_0.activity.data2
	arg_32_0.lastPos = arg_32_0.pos
	arg_32_0.step = arg_32_0.activity.data3
	arg_32_0.effectId = arg_32_0.activity.data4

def var_0_0.checkStep(arg_33_0, arg_33_1):
	if arg_33_0.step > 0:
		arg_33_0._event.emit(MonopolyWorldScene.ON_MOVE, arg_33_0.activity.id, function(arg_34_0, arg_34_1, arg_34_2)
			arg_33_0.step = arg_34_0
			arg_33_0.lastPos = arg_33_0.pos
			arg_33_0.pos = arg_34_1[#arg_34_1]
			arg_33_0.effectId = arg_34_2

			seriesAsync({
				function(arg_35_0)
					local var_35_0 = #arg_34_1 > 3 and var_0_15 or var_0_14

					arg_33_0.moveCharWithPaths(arg_34_1, var_35_0, arg_35_0),
				function(arg_36_0)
					if arg_34_1 and #arg_34_1 > 0 and arg_33_0.pos == 1:
						arg_33_0.turnCnt = arg_33_0.turnCnt + 1

						setText(findTF(arg_33_0._tf, "topRight/times"), tostring(arg_33_0.turnCnt))
						arg_33_0.changeBg()

					if isActive(arg_33_0.effectStart):
						setActive(arg_33_0.effectStart, False)
						setActive(arg_33_0.effectStart, True)
						LeanTween.delayedCall(1, System.Action(function()
							for iter_37_0 = 1, 6:
								local var_37_0 = findTF(arg_33_0.btnStart, "num/" .. iter_37_0)

								setActive(var_37_0, False)))
						LeanTween.delayedCall(2, System.Action(function()
							setActive(arg_33_0.effectStart, False)))

					arg_33_0.checkEffect(arg_36_0)
			}, function()
				if arg_33_1:
					arg_33_1()))
	else
		if arg_33_0.pos == 1:
			arg_33_0.turnCnt = arg_33_0.turnCnt + 1

			arg_33_0.changeBg()

		if arg_33_1:
			arg_33_1()

def var_0_0.updataUI(arg_40_0):
	setText(arg_40_0.labelLeftCount, arg_40_0.leftCount)

	local var_40_0 = arg_40_0.activity.getDataConfig("daily_time")

	var_0_25 = var_0_24.icon

	if arg_40_0.turnCnt and arg_40_0.turnCnt < #var_0_23:
		var_0_24 = pg.furniture_data_template[var_0_23[arg_40_0.turnCnt + 1]]

		setText(arg_40_0.gameTipUI2, i18n(var_0_6, var_40_0, 1))
	else
		setText(arg_40_0.gameTipUI2, i18n(var_0_7, var_40_0))

	if arg_40_0.leftCount and arg_40_0.leftCount > 0:
		setActive(findTF(arg_40_0.btnStart, "img3"), True)
		setActive(findTF(arg_40_0.btnStart, "img4"), False)
	else
		setActive(findTF(arg_40_0.btnStart, "img3"), False)
		setActive(findTF(arg_40_0.btnStart, "img4"), True)

	setText(findTF(arg_40_0._tf, "topRight/times"), tostring(arg_40_0.turnCnt))

	for iter_40_0 = 1, #arg_40_0.furnItems:
		if iter_40_0 <= arg_40_0.turnCnt:
			setActive(findTF(arg_40_0.furnItems[iter_40_0], "got"), True)
		else
			setActive(findTF(arg_40_0.furnItems[iter_40_0], "got"), False)

	if arg_40_0.bannerSnap.StartingScreen == 0 and not arg_40_0.bannerInit:
		if arg_40_0.turnCnt < #var_0_23:
			arg_40_0.bannerSnap.StartingScreen = arg_40_0.turnCnt % 5 + 1
			arg_40_0.bannerInit = True
		else
			arg_40_0.bannerSnap.autoSnap = 5
	elif arg_40_0.bannerSnap.CurrentScreen() != arg_40_0.turnCnt and arg_40_0.turnCnt < #var_0_23:
		local var_40_1 = arg_40_0.turnCnt % 5 - arg_40_0.bannerSnap.CurrentScreen()

		for iter_40_1 = 1, math.abs(var_40_1):
			if math.sign(var_40_1) > 0:
				arg_40_0.bannerSnap.NextScreen(True)
			else
				arg_40_0.bannerSnap.PreviousScreen(True)

	if arg_40_0.turnCnt >= #var_0_23:
		if arg_40_0.bannerCanvas.blocksRaycasts != True:
			arg_40_0.bannerCanvas.blocksRaycasts = True

		if not isActive(findTF(arg_40_0._tf, "bg/dots")):
			arg_40_0.bannerSnap.NextScreen(True)
			setActive(findTF(arg_40_0._tf, "bg/dots"), True)
	else
		if arg_40_0.bannerCanvas.blocksRaycasts == True:
			arg_40_0.bannerCanvas.blocksRaycasts = False

		if isActive(findTF(arg_40_0._tf, "bg/dots")):
			setActive(findTF(arg_40_0._tf, "bg/dots"), False)

	arg_40_0.changeBg()

def var_0_0.updataChar(arg_41_0):
	local var_41_0 = arg_41_0.mapCells[arg_41_0.pos]

	arg_41_0.char.localPosition = var_41_0.position

	if not isActive(arg_41_0.char):
		SetActive(arg_41_0.char, True)
		arg_41_0.char.SetAsLastSibling()

	if arg_41_0.model:
		arg_41_0.updataCharDirect(arg_41_0.pos, False)

def var_0_0.getEffectTf(arg_42_0, arg_42_1, arg_42_2):
	for iter_42_0 = 1, #var_0_22:
		local var_42_0 = var_0_22[iter_42_0]

		if var_42_0.cell_type == arg_42_1:
			local var_42_1 = var_42_0.name

			if not arg_42_2:
				return findTF(arg_42_0._tf, "mapContainer/effect/" .. var_42_1)
			elif arg_42_2 == var_42_0.path_length:
				return findTF(arg_42_0._tf, "mapContainer/effect/" .. var_42_1)

	return None

def var_0_0.checkEffect(arg_43_0, arg_43_1):
	if arg_43_0.effectId > 0:
		local var_43_0 = arg_43_0.mapCells[arg_43_0.pos]
		local var_43_1, var_43_2 = arg_43_0.getActionName(var_43_0.icon)
		local var_43_3 = pg.activity_event_monopoly_event[arg_43_0.effectId].story

		seriesAsync({
			function(arg_44_0)
				if var_43_1:
					arg_43_0.changeCharAction(var_43_1, 1, function()
						arg_43_0.changeCharAction(var_0_13, 0, None)
						arg_44_0())

				if var_43_2:
					local var_44_0 = arg_43_0.getEffectTf(var_43_2)

					if var_44_0:
						var_44_0.anchoredPosition = Vector2(var_43_0.position.x, var_43_0.position.y)

						setActive(var_44_0, False)
						setActive(var_44_0, True)

				if not var_43_1 and not var_43_2:
					arg_44_0()
				elif not var_43_1 and var_43_2:
					LeanTween.delayedCall(1, System.Action(function()
						arg_44_0())),
			function(arg_47_0)
				if var_43_3 and tonumber(var_43_3) != 0:
					pg.NewStoryMgr.GetInstance().Play(var_43_3, arg_47_0, True, True)
				else
					arg_47_0(),
			function(arg_48_0)
				arg_43_0.triggerEfeect(arg_48_0),
			function(arg_49_0)
				arg_43_0.checkCountStory(arg_49_0),
			function(arg_50_0)
				if arg_43_0.pos == 1:
					arg_43_0.changeBg()

				arg_50_0()
		}, arg_43_1)
	elif arg_43_1:
		arg_43_1()

def var_0_0.triggerEfeect(arg_51_0, arg_51_1):
	arg_51_0._event.emit(MonopolyWorldScene.ON_TRIGGER, arg_51_0.activity.id, function(arg_52_0, arg_52_1)
		if arg_52_0 and #arg_52_0 >= 0:
			arg_51_0.effectId = arg_52_1
			arg_51_0.lastPos = arg_51_0.pos
			arg_51_0.pos = arg_52_0[#arg_52_0]

			if #arg_52_0 > 0:
				print()

			local var_52_0 = arg_51_0.getEffectTf(var_0_18, #arg_52_0)

			seriesAsync({
				function(arg_53_0)
					if var_52_0:
						setActive(var_52_0, False)
						setActive(var_52_0, True)

						var_52_0.anchoredPosition = arg_51_0.mapCells[arg_51_0.lastPos].position

						LeanTween.delayedCall(1, System.Action(function()
							arg_53_0()))
					else
						arg_53_0(),
				function(arg_55_0)
					arg_51_0.moveCharWithPaths(arg_52_0, var_0_12, arg_55_0)
			}, function()
				if var_52_0:
					-- block empty

				arg_51_1()))

def var_0_0.changeBg(arg_57_0):
	local var_57_0 = arg_57_0.turnCnt and arg_57_0.turnCnt % 5 + 1 or 1

	for iter_57_0 = 1, 5:
		local var_57_1 = findTF(arg_57_0._tf, "bg/img" .. iter_57_0)
		local var_57_2 = GetComponent(var_57_1, typeof(Image)).color.a

		if iter_57_0 == var_57_0:
			if var_57_2 != 1:
				LeanTween.alpha(var_57_1, 1, 0.5)
		elif var_57_2 != 0:
			LeanTween.alpha(var_57_1, 0, 0.5)

def var_0_0.toMoveCar(arg_58_0):
	if not arg_58_0.targetPosition:
		return

	local var_58_0 = math.abs(arg_58_0.targetPosition.x - arg_58_0.char.localPosition.x)
	local var_58_1 = math.abs(arg_58_0.targetPosition.y - arg_58_0.char.localPosition.y)

	if var_58_0 <= 6.5 and var_58_1 <= 6.5:
		arg_58_0.targetPosition = None

		if arg_58_0.moveComplete:
			arg_58_0.updataCharDirect(arg_58_0.targetPosIndex, True)
			arg_58_0.moveComplete()

	arg_58_0.speedX = math.abs(arg_58_0.speedX + arg_58_0.baseASpeedX) > math.abs(arg_58_0.baseSpeedX) and arg_58_0.baseSpeedX or arg_58_0.speedX + arg_58_0.baseASpeedX
	arg_58_0.speedY = math.abs(arg_58_0.speedY + arg_58_0.baseASpeedY) > math.abs(arg_58_0.baseSpeedY) and arg_58_0.baseSpeedY or arg_58_0.speedY + arg_58_0.baseASpeedY

	local var_58_2 = arg_58_0.char.localPosition

	arg_58_0.char.localPosition = Vector3(var_58_2.x + arg_58_0.speedX, var_58_2.y + arg_58_0.speedY, 0)

def var_0_0.checkPathTurn(arg_59_0, arg_59_1):
	local var_59_0 = arg_59_1 + 1 > #arg_59_0.mapCells and 1 or arg_59_1 + 1
	local var_59_1 = arg_59_1 - 1 < 1 and #arg_59_0.mapCells or arg_59_1 - 1

	if arg_59_0.mapCells[var_59_0].col == arg_59_0.mapCells[var_59_1].col or arg_59_0.mapCells[var_59_0].row == arg_59_0.mapCells[var_59_1].row:
		return False

	return True

def var_0_0.moveCharWithPaths(arg_60_0, arg_60_1, arg_60_2, arg_60_3):
	if not arg_60_1 or #arg_60_1 <= 0:
		if arg_60_3:
			arg_60_3()

		return

	local var_60_0 = {}
	local var_60_1 = arg_60_1[1] - 1 < 1 and #arg_60_0.mapCells or arg_60_1[1] - 1

	for iter_60_0 = 1, #arg_60_1:
		local var_60_2 = arg_60_0.mapCells[arg_60_1[iter_60_0]]

		table.insert(var_60_0, function(arg_61_0)
			arg_60_0.changeCharAction(arg_60_2, 0, None)
			arg_60_0.updataCharDirect(var_60_1, True)

			var_60_1 = arg_60_1[iter_60_0]

			local var_61_0
			local var_61_1 = arg_60_2 == var_0_12 and 0.9 or arg_60_2 == var_0_14 and 0.9 or 0.5

			LeanTween.moveLocal(go(arg_60_0.char), var_60_2.tf.localPosition, var_61_1).setEase(LeanTweenType.linear).setOnComplete(System.Action(function()
				if arg_60_2 == var_0_14:
					LeanTween.delayedCall(0.05, System.Action(function()
						arg_61_0()))
				else
					arg_61_0())))

		if iter_60_0 == #arg_60_1:
			table.insert(var_60_0, function(arg_64_0)
				arg_60_0.changeCharAction(var_0_13, 0, None)
				arg_60_0.updataCharDirect(arg_60_1[iter_60_0], False)
				arg_64_0())

	seriesAsync(var_60_0, arg_60_3)

def var_0_0.changeCharAction(arg_65_0, arg_65_1, arg_65_2, arg_65_3):
	if arg_65_0.actionName == arg_65_1 and arg_65_0.actionName != var_0_14:
		return

	arg_65_0.actionName = arg_65_1

	arg_65_0.anim.SetActionCallBack(None)
	arg_65_0.anim.SetAction(arg_65_1, 0)
	arg_65_0.anim.SetActionCallBack(function(arg_66_0)
		if arg_66_0 == "finish":
			if arg_65_2 == 1:
				arg_65_0.anim.SetActionCallBack(None)
				arg_65_0.anim.SetAction(var_0_13, 0)

			if arg_65_3:
				arg_65_3())

	if arg_65_2 != 1 and arg_65_3:
		arg_65_3()

def var_0_0.getActionName(arg_67_0, arg_67_1):
	if arg_67_1 == "icon_1":
		return var_0_11, var_0_21
	elif arg_67_1 == "icon_2":
		return var_0_9, var_0_17
	elif arg_67_1 == "icon_3":
		return var_0_11, var_0_20
	elif arg_67_1 == "icon_4":
		return var_0_11, var_0_21
	elif arg_67_1 == "icon_5":
		return var_0_10, var_0_19
	elif arg_67_1 == "icon_6":
		return None, None

def var_0_0.dispose(arg_68_0):
	if arg_68_0.skinCardName and arg_68_0.showModel:
		PoolMgr.GetInstance().ReturnSpineChar(arg_68_0.skinCardName, arg_68_0.showModel)

	if arg_68_0.funrTimer:
		arg_68_0.funrTimer.Stop()

		arg_68_0.funrTimer = None

	for iter_68_0 = 1, 5:
		local var_68_0 = findTF(arg_68_0._tf, "bg/img" .. iter_68_0)

		if LeanTween.isTweening(var_68_0):
			LeanTween.cancel(var_68_0)

return var_0_0
