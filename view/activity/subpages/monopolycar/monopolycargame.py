local var_0_0 = class("MonopolyCarGame")
local var_0_1 = 100
local var_0_2 = 50
local var_0_3 = "redcar"
local var_0_4 = {
	"gaoxiong_5",
	"aidang_5",
	"dafeng_5",
	"yuekegongjue_2",
	"weiershiqinwang_3",
	"xianghe_3",
	"ruihe_3",
	"ougen_5",
	"qiye_7"
}
local var_0_5 = 0.6
local var_0_6 = "B-stand"
local var_0_7 = "F-stand"
local var_0_8 = "B-walk"
local var_0_9 = "F-walk"
local var_0_10 = "typeMoveUp"
local var_0_11 = "typeMoveDown"
local var_0_12 = "typeMoveLeft"
local var_0_13 = "typeMoveRight"

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

	local var_2_0 = math.random(1, #var_0_4)

	arg_2_0.showSkinId = var_0_4[var_2_0]

def var_0_0.initUI(arg_3_0):
	arg_3_0.tplMapCell = findTF(arg_3_0._tf, "tplMapCell")
	arg_3_0.mapContainer = findTF(arg_3_0._tf, "mapContainer")
	arg_3_0.char = findTF(arg_3_0._tf, "mapContainer/char")
	arg_3_0.showChar = findTF(arg_3_0._tf, "showChar")

	setActive(arg_3_0.char, False)

	arg_3_0.btnStart = findTF(arg_3_0._tf, "btnStart")
	arg_3_0.btnHelp = findTF(arg_3_0._tf, "btnHelp")
	arg_3_0.btnRp = findTF(arg_3_0._tf, "btnRp")
	arg_3_0.commonAnim = findTF(arg_3_0.btnRp, "rpAni").GetComponent(typeof(Animator))
	arg_3_0.labelLeftCountTip = findTF(arg_3_0.btnStart, "labelLeftCountTip")

	setActive(arg_3_0.labelLeftCountTip, False)

	arg_3_0.labelLeftCount = findTF(arg_3_0.btnStart, "labelLeftCount")
	arg_3_0.labelDropShip = findTF(arg_3_0._tf, "labelDropShip")
	arg_3_0.labelLeftRpCount = findTF(arg_3_0._tf, "labelLeftRpCount")
	arg_3_0.rollStep = findTF(arg_3_0._tf, "step")

	setActive(arg_3_0.rollStep, False)

	arg_3_0.mcTouzi = findTF(arg_3_0._tf, "mcTouzi")
	arg_3_0.imgTouzi = findTF(arg_3_0._tf, "imgTouzi")

	setActive(arg_3_0.mcTouzi, False)
	arg_3_0.initMap()
	arg_3_0.initChar()

def var_0_0.initEvent(arg_4_0):
	onButton(arg_4_0._binder, arg_4_0.btnStart, function()
		if arg_4_0.inAnimatedFlag:
			return

		if arg_4_0.leftCount and arg_4_0.leftCount <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_count_noenough"))

			return

		arg_4_0.changeAnimeState(True)
		setActive(arg_4_0.btnStart, True)
		arg_4_0._event.emit(MonopolyCarPage.ON_START, arg_4_0.activity.id, function(arg_6_0)
			if arg_6_0 and arg_6_0 > 0:
				arg_4_0.showRollAnimated(arg_6_0)), SFX_PANEL)
	onButton(arg_4_0._binder, arg_4_0.btnHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_monopoly_car.tip
		}), SFX_PANEL)
	onButton(arg_4_0._binder, arg_4_0.showChar, function()
		arg_4_0._event.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.SKINSHOP), SFX_PANEL)
	onButton(arg_4_0._binder, arg_4_0.btnRp, function()
		if arg_4_0.leftAwardCnt > 0:
			arg_4_0._event.emit(MonopolyCarPage.ON_AWARD), SFX_PANEL)

def var_0_0.showRollAnimated(arg_10_0, arg_10_1):
	local var_10_0 = findTF(arg_10_0.rollStep, "stepArrow")

	var_10_0.localEulerAngles = Vector3(0, 0, 0)
	findTF(arg_10_0.rollStep, "progress/bg").GetComponent(typeof(Image)).fillAmount = 0.1
	findTF(arg_10_0.rollStep, "select/bg").GetComponent(typeof(Image)).fillAmount = 0.1

	setText(findTF(arg_10_0.rollStep, "labelRoll"), "0")
	seriesAsync({
		function(arg_11_0)
			LeanTween.value(go(arg_10_0._tf), 1, 0, 0.2).setOnUpdate(System.Action_float(function(arg_12_0)
				arg_10_0.btnStart.GetComponent(typeof(CanvasGroup)).alpha = arg_12_0)).setOnComplete(System.Action(function()
				setActive(arg_10_0.btnStart, False)

				arg_10_0.btnStart.GetComponent(typeof(CanvasGroup)).alpha = 1

				arg_11_0())),
		function(arg_14_0)
			LeanTween.value(go(arg_10_0._tf), 0, 1, 0.2).setOnUpdate(System.Action_float(function(arg_15_0)
				arg_10_0.rollStep.GetComponent(typeof(CanvasGroup)).alpha = arg_15_0

				setActive(arg_10_0.rollStep, True))).setOnComplete(System.Action(function()
				arg_14_0())),
		function(arg_17_0)
			local var_17_0 = arg_10_1 / 6 * 0.62
			local var_17_1 = var_17_0 / arg_10_1
			local var_17_2 = -arg_10_1 * 31

			LeanTween.value(go(arg_10_0._tf), 0, 1, 0.7 + arg_10_1 / 5).setEase(LeanTweenType.easeOutCirc).setOnUpdate(System.Action_float(function(arg_18_0)
				findTF(arg_10_0.rollStep, "progress/bg").GetComponent(typeof(Image)).fillAmount = var_17_0 * arg_18_0 + 0.13
				findTF(arg_10_0.rollStep, "select/bg").GetComponent(typeof(Image)).fillAmount = var_17_1 * math.floor(arg_18_0 / (1 / arg_10_1)) + 0.17

				setText(findTF(arg_10_0.rollStep, "labelRoll"), math.floor(arg_18_0 / (1 / arg_10_1)))

				local var_18_0 = var_17_2 * arg_18_0 - 13

				var_10_0.localEulerAngles = Vector3(0, 0, var_18_0))).setOnComplete(System.Action(function()
				arg_17_0())),
		function(arg_20_0)
			LeanTween.value(go(arg_10_0._tf), 1, 0, 0.3).setOnComplete(System.Action(function()
				arg_20_0())),
		function(arg_22_0)
			LeanTween.value(go(arg_10_0._tf), 1, 0, 0.3).setOnUpdate(System.Action_float(function(arg_23_0)
				arg_10_0.rollStep.GetComponent(typeof(CanvasGroup)).alpha = arg_23_0)).setOnComplete(System.Action(function()
				setActive(arg_10_0.rollStep, False)

				arg_10_0.rollStep.GetComponent(typeof(CanvasGroup)).alpha = 1

				arg_22_0()))
	}, function()
		setActive(arg_10_0.mcTouzi, True)
		setActive(arg_10_0.mcTouzi, False)

		arg_10_0.useCount = arg_10_0.useCount + 1
		arg_10_0.step = arg_10_1

		if arg_10_0.step > 0:
			local var_25_0 = GetSpriteFromAtlas("ui/activityuipage/monopolycar_atlas", arg_10_0.step)

			setActive(arg_10_0.imgTouzi, True)

			arg_10_0.imgTouzi.GetComponent(typeof(Image)).sprite = var_25_0

		arg_10_0.updataUI()
		arg_10_0.checkCharActive())

def var_0_0.checkCountStory(arg_26_0, arg_26_1):
	local var_26_0 = arg_26_0.useCount
	local var_26_1 = arg_26_0.activity.getDataConfig("story") or {}
	local var_26_2 = _.detect(var_26_1, function(arg_27_0)
		return arg_27_0[1] == var_26_0)

	if var_26_2:
		pg.NewStoryMgr.GetInstance().Play(var_26_2[2], arg_26_1)
	else
		arg_26_1()

def var_0_0.changeAnimeState(arg_28_0, arg_28_1):
	if arg_28_1:
		arg_28_0.btnStart.GetComponent(typeof(Image)).raycastTarget = False
		arg_28_0.inAnimatedFlag = True

		arg_28_0._event.emit(ActivityMainScene.LOCK_ACT_MAIN, True)
	else
		arg_28_0.inAnimatedFlag = False
		arg_28_0.btnStart.GetComponent(typeof(Image)).raycastTarget = True

		setActive(arg_28_0.imgTouzi, False)
		arg_28_0._event.emit(ActivityMainScene.LOCK_ACT_MAIN, False)

	setActive(arg_28_0.btnStart, not arg_28_1)

def var_0_0.initMap(arg_29_0):
	local var_29_0 = MonopolyCarConst.map_dic

	arg_29_0.mapCells = {}

	for iter_29_0 = 1, #var_29_0:
		local var_29_1 = iter_29_0 - 1
		local var_29_2 = {
			x = -var_29_1 * var_0_1,
			y = -var_29_1 * var_0_2
		}
		local var_29_3 = var_29_0[iter_29_0]

		for iter_29_1 = 1, #var_29_3:
			local var_29_4 = iter_29_1 - 1
			local var_29_5 = var_29_3[iter_29_1]

			if var_29_5 > 0:
				local var_29_6 = cloneTplTo(arg_29_0.tplMapCell, arg_29_0.mapContainer, tostring(var_29_5))
				local var_29_7 = Vector2(var_0_1 * var_29_4 + var_29_2.x, -var_0_2 * var_29_4 + var_29_2.y)

				var_29_6.localPosition = var_29_7

				local var_29_8 = pg.activity_event_monopoly_map[var_29_5].icon
				local var_29_9 = GetSpriteFromAtlas("ui/activityuipage/monopolycar_atlas", var_29_8)

				findTF(var_29_6, "image").GetComponent(typeof(Image)).sprite = var_29_9

				findTF(var_29_6, "image").GetComponent(typeof(Image)).SetNativeSize()

				local var_29_10 = {
					col = var_29_4,
					row = var_29_1,
					mapId = var_29_5,
					tf = var_29_6,
					icon = var_29_8,
					position = var_29_7
				}

				table.insert(arg_29_0.mapCells, var_29_10)

	table.sort(arg_29_0.mapCells, function(arg_30_0, arg_30_1)
		return arg_30_0.mapId < arg_30_1.mapId)

def var_0_0.initChar(arg_31_0):
	PoolMgr.GetInstance().GetSpineChar(var_0_3, True, function(arg_32_0)
		arg_31_0.model = arg_32_0
		arg_31_0.model.transform.localScale = Vector3.one
		arg_31_0.model.transform.localPosition = Vector3.zero

		arg_31_0.model.transform.SetParent(arg_31_0.char, False)

		arg_31_0.anim = arg_31_0.model.GetComponent(typeof(SpineAnimUI))

		arg_31_0.checkCharActive()

		if arg_31_0.pos:
			arg_31_0.updataCharDirect(arg_31_0.pos, False))
	PoolMgr.GetInstance().GetSpineChar(arg_31_0.showSkinId, True, function(arg_33_0)
		arg_31_0.showModel = arg_33_0
		arg_31_0.showModel.transform.localScale = Vector3.one
		arg_31_0.showModel.transform.localPosition = Vector3.zero

		arg_31_0.showModel.transform.SetParent(arg_31_0.showChar, False)

		arg_31_0.showAnim = arg_31_0.showModel.GetComponent(typeof(SpineAnimUI))

		arg_31_0.showAnim.SetAction("stand", 0))

def var_0_0.updataCharDirect(arg_34_0, arg_34_1, arg_34_2):
	if arg_34_0.model:
		local var_34_0 = arg_34_0.mapCells[arg_34_1].position
		local var_34_1 = arg_34_1 + 1 > #arg_34_0.mapCells and 1 or arg_34_1 + 1
		local var_34_2 = arg_34_0.mapCells[var_34_1]
		local var_34_3, var_34_4 = arg_34_0.getMoveType(arg_34_0.mapCells[arg_34_1].mapId, arg_34_0.mapCells[var_34_1].mapId, arg_34_2)

		arg_34_0.char.localScale = Vector3(var_34_4, arg_34_0.char.localScale.y, arg_34_0.char.localScale.z)

		arg_34_0.anim.SetActionCallBack(None)
		arg_34_0.anim.SetAction(var_34_3, 0)

def var_0_0.getMoveType(arg_35_0, arg_35_1, arg_35_2, arg_35_3):
	local var_35_0 = MonopolyCarConst.map_dic
	local var_35_1 = {}
	local var_35_2 = {}

	for iter_35_0 = 1, #var_35_0:
		local var_35_3 = var_35_0[iter_35_0]

		for iter_35_1 = 1, #var_35_3:
			local var_35_4 = var_35_3[iter_35_1]

			if var_35_4 == arg_35_1:
				var_35_1 = {
					x = iter_35_1,
					y = iter_35_0
				}

			if var_35_4 == arg_35_2:
				var_35_2 = {
					x = iter_35_1,
					y = iter_35_0
				}

	local var_35_5
	local var_35_6

	if var_35_2.y > var_35_1.y:
		var_35_5 = arg_35_3 and var_0_9 or var_0_7
		var_35_6 = var_0_5
	elif var_35_2.y < var_35_1.y:
		var_35_5 = arg_35_3 and var_0_8 or var_0_6
		var_35_6 = var_0_5
	elif var_35_2.x > var_35_1.x:
		var_35_5 = arg_35_3 and var_0_9 or var_0_7
		var_35_6 = -var_0_5
	elif var_35_2.x < var_35_1.x:
		var_35_5 = arg_35_3 and var_0_8 or var_0_6
		var_35_6 = -var_0_5

	return var_35_5, var_35_6

def var_0_0.checkCharActive(arg_36_0):
	if arg_36_0.anim:
		if arg_36_0.effectId and arg_36_0.effectId > 0:
			arg_36_0.changeAnimeState(True)
			arg_36_0.checkEffect(function()
				arg_36_0.changeAnimeState(False)
				arg_36_0.checkCharActive())
		elif arg_36_0.step and arg_36_0.step > 0:
			arg_36_0.changeAnimeState(True)
			arg_36_0.checkStep(function()
				arg_36_0.changeAnimeState(False)
				arg_36_0.checkCharActive())

def var_0_0.firstUpdata(arg_39_0, arg_39_1):
	arg_39_0.activityDataUpdata(arg_39_1)
	arg_39_0.updataUI()
	arg_39_0.updataChar()
	arg_39_0.checkCharActive()

def var_0_0.updataActivity(arg_40_0, arg_40_1):
	arg_40_0.activityDataUpdata(arg_40_1)
	arg_40_0.updataUI()

def var_0_0.activityDataUpdata(arg_41_0, arg_41_1):
	arg_41_0.activity = arg_41_1

	local var_41_0 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_41_1 = arg_41_0.activity.data1

	arg_41_0.totalCnt = math.ceil((var_41_0 - var_41_1) / 86400) * arg_41_0.activity.getDataConfig("daily_time") + arg_41_0.activity.data1_list[1]
	arg_41_0.useCount = arg_41_0.activity.data1_list[2]
	arg_41_0.leftCount = arg_41_0.totalCnt - arg_41_0.useCount
	arg_41_0.turnCnt = arg_41_0.activity.data1_list[3] - 1
	arg_41_0.leftDropShipCnt = 8 - arg_41_0.turnCnt

	local var_41_2 = arg_41_0.activity.data2_list[2]

	arg_41_0.advanceTotalCnt = #arg_41_1.getDataConfig("reward")
	arg_41_0.isAdvanceRp = arg_41_0.advanceTotalCnt - var_41_2 > 0

	local var_41_3 = arg_41_0.activity.data2_list[1]

	arg_41_0.leftAwardCnt = var_41_3 - var_41_2
	arg_41_0.advanceRpCount = math.max(0, math.min(var_41_3, arg_41_0.advanceTotalCnt) - var_41_2)
	arg_41_0.commonRpCount = math.max(0, var_41_3 - arg_41_0.advanceTotalCnt) - math.max(0, var_41_2 - arg_41_0.advanceTotalCnt)

	local var_41_4 = arg_41_1.getDataConfig("reward_time")

	arg_41_0.nextredPacketStep = var_41_4 - arg_41_0.useCount % var_41_4
	arg_41_0.pos = arg_41_0.activity.data2
	arg_41_0.step = arg_41_0.activity.data3
	arg_41_0.effectId = arg_41_0.activity.data4

def var_0_0.checkStep(arg_42_0, arg_42_1):
	if arg_42_0.step > 0:
		arg_42_0._event.emit(MonopolyCarPage.ON_MOVE, arg_42_0.activity.id, function(arg_43_0, arg_43_1, arg_43_2)
			arg_42_0.step = arg_43_0
			arg_42_0.pos = arg_43_1[#arg_43_1]
			arg_42_0.effectId = arg_43_2

			seriesAsync({
				function(arg_44_0)
					local var_44_0

					arg_42_0.moveCharWithPaths(arg_43_1, var_44_0, arg_44_0),
				function(arg_45_0)
					arg_42_0.checkEffect(arg_45_0)
			}, function()
				if arg_42_1:
					arg_42_1()))
	elif arg_42_1:
		arg_42_1()

def var_0_0.updataUI(arg_47_0):
	setText(arg_47_0.labelLeftRpCount, "" .. arg_47_0.leftAwardCnt)
	arg_47_0.commonAnim.SetInteger("count", arg_47_0.leftAwardCnt)
	setText(arg_47_0.labelDropShip, "" .. arg_47_0.turnCnt + 1)
	setText(arg_47_0.labelLeftCountTip, i18n("monopoly_left_count"))
	setText(arg_47_0.labelLeftCount, arg_47_0.leftCount)

def var_0_0.updataChar(arg_48_0):
	local var_48_0 = arg_48_0.mapCells[arg_48_0.pos]

	arg_48_0.char.localPosition = var_48_0.position

	if not isActive(arg_48_0.char):
		SetActive(arg_48_0.char, True)
		arg_48_0.char.SetAsLastSibling()

	if arg_48_0.model:
		arg_48_0.updataCharDirect(arg_48_0.pos, False)

def var_0_0.checkEffect(arg_49_0, arg_49_1):
	if arg_49_0.effectId > 0:
		local var_49_0 = arg_49_0.mapCells[arg_49_0.pos]
		local var_49_1 = pg.activity_event_monopoly_event[arg_49_0.effectId].story

		seriesAsync({
			function(arg_50_0)
				if var_49_1 and tonumber(var_49_1) != 0:
					pg.NewStoryMgr.GetInstance().Play(var_49_1, arg_50_0, True, True)
				else
					arg_50_0(),
			function(arg_51_0)
				arg_49_0.triggerEfeect(arg_51_0),
			function(arg_52_0)
				arg_49_0.checkCountStory(arg_52_0)
		}, arg_49_1)
	elif arg_49_1:
		arg_49_1()

def var_0_0.triggerEfeect(arg_53_0, arg_53_1):
	arg_53_0._event.emit(MonopolyCarPage.ON_TRIGGER, arg_53_0.activity.id, function(arg_54_0, arg_54_1)
		if arg_54_0 and #arg_54_0 >= 0:
			arg_53_0.effectId = arg_54_1
			arg_53_0.pos = arg_54_0[#arg_54_0]

			seriesAsync({
				function(arg_55_0)
					arg_53_0.moveCharWithPaths(arg_54_0, None, arg_55_0)
			}, function()
				arg_53_1()))

def var_0_0.moveCarWithPaths(arg_57_0, arg_57_1, arg_57_2, arg_57_3):
	if not arg_57_1 or #arg_57_1 <= 0:
		if arg_57_3:
			arg_57_3()

		return

	local var_57_0 = {}
	local var_57_1 = arg_57_0.char.localPosition
	local var_57_2 = {}
	local var_57_3 = {}

	for iter_57_0 = 1, #arg_57_1:
		if arg_57_0.checkPathTurn(arg_57_1[iter_57_0]):
			table.insert(var_57_2, arg_57_0.mapCells[arg_57_1[iter_57_0]].position)
			table.insert(var_57_3, arg_57_1[iter_57_0])
		elif iter_57_0 == #arg_57_1:
			table.insert(var_57_2, arg_57_0.mapCells[arg_57_1[iter_57_0]].position)
			table.insert(var_57_3, arg_57_1[iter_57_0])

	arg_57_0.speedX = 0
	arg_57_0.speedY = 0
	arg_57_0.baseSpeed = 6
	arg_57_0.baseASpeed = 0.1

	if not arg_57_0.timer:
		arg_57_0.timer = Timer.New(function()
			arg_57_0.toMoveCar(), 0.016666666666666666, -1)

		arg_57_0.timer.Start()

	for iter_57_1 = 1, #var_57_2:
		table.insert(var_57_0, function(arg_59_0)
			arg_57_0.moveComplete = arg_59_0
			arg_57_0.stopOnEnd = False
			arg_57_0.targetPosition = var_57_2[iter_57_1]
			arg_57_0.targetPosIndex = var_57_3[iter_57_1]
			arg_57_0.moveX = arg_57_0.targetPosition.x - arg_57_0.char.localPosition.x
			arg_57_0.moveY = arg_57_0.targetPosition.y - arg_57_0.char.localPosition.y
			arg_57_0.baseSpeedX = arg_57_0.baseSpeed * (arg_57_0.moveX / math.abs(arg_57_0.moveX))
			arg_57_0.baseASpeedX = arg_57_0.baseASpeed * (arg_57_0.moveX / math.abs(arg_57_0.moveX))
			arg_57_0.baseSpeedY = math.abs(arg_57_0.baseSpeedX) / (math.abs(arg_57_0.moveX) / arg_57_0.moveY)
			arg_57_0.baseASpeedY = math.abs(arg_57_0.baseASpeedX) / (math.abs(arg_57_0.moveX) / arg_57_0.moveY)

			if iter_57_1 == 1:
				arg_57_0.speedX = 0
				arg_57_0.speedY = 0
			else
				arg_57_0.speedX = arg_57_0.baseSpeedX
				arg_57_0.speedY = arg_57_0.baseSpeedY)

	table.insert(var_57_0, function(arg_60_0)
		arg_57_0.moveComplete = None

		arg_57_0.updataCharDirect(arg_57_1[#arg_57_1], False)
		arg_60_0())
	table.insert(var_57_0, function(arg_61_0)
		LeanTween.value(go(arg_57_0._tf), 1, 0, 0.1).setOnComplete(System.Action(function()
			arg_61_0())))
	seriesAsync(var_57_0, arg_57_3)

def var_0_0.toMoveCar(arg_63_0):
	if not arg_63_0.targetPosition:
		return

	local var_63_0 = math.abs(arg_63_0.targetPosition.x - arg_63_0.char.localPosition.x)
	local var_63_1 = math.abs(arg_63_0.targetPosition.y - arg_63_0.char.localPosition.y)

	if var_63_0 <= 6.5 and var_63_1 <= 6.5:
		arg_63_0.targetPosition = None

		if arg_63_0.moveComplete:
			arg_63_0.updataCharDirect(arg_63_0.targetPosIndex, True)
			arg_63_0.moveComplete()

	arg_63_0.speedX = math.abs(arg_63_0.speedX + arg_63_0.baseASpeedX) > math.abs(arg_63_0.baseSpeedX) and arg_63_0.baseSpeedX or arg_63_0.speedX + arg_63_0.baseASpeedX
	arg_63_0.speedY = math.abs(arg_63_0.speedY + arg_63_0.baseASpeedY) > math.abs(arg_63_0.baseSpeedY) and arg_63_0.baseSpeedY or arg_63_0.speedY + arg_63_0.baseASpeedY

	local var_63_2 = arg_63_0.char.localPosition

	arg_63_0.char.localPosition = Vector3(var_63_2.x + arg_63_0.speedX, var_63_2.y + arg_63_0.speedY, 0)

def var_0_0.checkPathTurn(arg_64_0, arg_64_1):
	local var_64_0 = arg_64_1 + 1 > #arg_64_0.mapCells and 1 or arg_64_1 + 1
	local var_64_1 = arg_64_1 - 1 < 1 and #arg_64_0.mapCells or arg_64_1 - 1

	if arg_64_0.mapCells[var_64_0].col == arg_64_0.mapCells[var_64_1].col or arg_64_0.mapCells[var_64_0].row == arg_64_0.mapCells[var_64_1].row:
		return False

	return True

def var_0_0.moveCharWithPaths(arg_65_0, arg_65_1, arg_65_2, arg_65_3):
	arg_65_0.moveCarWithPaths(arg_65_1, arg_65_2, arg_65_3)

	do return end

	if not arg_65_1 or #arg_65_1 <= 0:
		if arg_65_3:
			arg_65_3()

		return

	local var_65_0 = {}
	local var_65_1 = arg_65_1[1] - 1 < 1 and #arg_65_0.mapCells or arg_65_1[1] - 1

	for iter_65_0 = 1, #arg_65_1:
		local var_65_2 = arg_65_0.mapCells[arg_65_1[iter_65_0]]

		table.insert(var_65_0, function(arg_66_0)
			arg_65_0.updataCharDirect(var_65_1, True)

			var_65_1 = arg_65_1[iter_65_0]

			local var_66_0 = 0.35

			LeanTween.moveLocal(go(arg_65_0.char), var_65_2.tf.localPosition, var_66_0).setEase(LeanTweenType.linear).setOnComplete(System.Action(function()
				arg_66_0())))

		if iter_65_0 == #arg_65_1:
			table.insert(var_65_0, function(arg_68_0)
				arg_65_0.updataCharDirect(arg_65_1[iter_65_0], False)
				arg_68_0())

	seriesAsync(var_65_0, arg_65_3)

def var_0_0.dispose(arg_69_0):
	PoolMgr.GetInstance().ReturnSpineChar(var_0_3, arg_69_0.model)
	PoolMgr.GetInstance().ReturnSpineChar(arg_69_0.showSkinId, arg_69_0.showModel)

return var_0_0
