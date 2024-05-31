local var_0_0 = class("MonopolyGame")
local var_0_1 = pg.activity_event_monopoly_map
local var_0_2 = pg.activity_event_monopoly_event
local var_0_3 = 501041
local var_0_4 = 501041
local var_0_5 = 6
local var_0_6 = 5
local var_0_7 = {}

var_0_7.stateGold = "dafuweng_gold"
var_0_7.stateOil = "dafuweng_oil"
var_0_7.stateEvent = "dafuweng_event"
var_0_7.stateWalk = "dafuweng_walk"
var_0_7.stateStand = "dafuweng_stand"
var_0_7.stateJump = "dafuweng_jump"
var_0_7.stateRun = "dafuweng_run"
var_0_7.stateTouch = "dafuweng_touch"

local var_0_8

local function var_0_9()
	local var_1_0 = {
		def onActionUpdated:(arg_2_0, arg_2_1)
			return
	}

	var_1_0.currState = None

	function var_1_0.ChangeState(arg_3_0, arg_3_1, arg_3_2)
		arg_3_2 = arg_3_2 or function()
			return

		if arg_3_0.currState == arg_3_1:
			arg_3_2()

		arg_3_0.currState = arg_3_1

		arg_3_0.onActionUpdated(arg_3_1, arg_3_2)

	function var_1_0.IsStandState(arg_5_0)
		return arg_5_0.currState == var_0_7.stateStand

	return var_1_0

local function var_0_10(arg_6_0)
	return {
		def onMove:(arg_7_0, arg_7_1)
			return,
		def onJump:(arg_8_0, arg_8_1)
			return,
		def onUpdatePos:(arg_9_0)
			return,
		ship = Ship.New({
			configId = arg_6_0,
			skin_id = var_0_4
		}),
		state = var_0_9(),
		def Move:(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
			arg_10_2 = arg_10_2 or function()
				return

			if #arg_10_1 == 0:
				arg_10_2()

				return

			local function var_10_0(arg_12_0)
				if arg_12_0:
					arg_10_0.state.ChangeState(var_0_7.stateWalk)
				else
					arg_10_0.state.ChangeState(var_0_7.stateRun)

				arg_10_0.onMove(arg_10_1, function()
					local var_13_0 = arg_10_0.GetAction(arg_10_1[#arg_10_1])

					if var_13_0:
						arg_10_0.state.ChangeState(var_13_0, function()
							arg_10_0.state.ChangeState(var_0_7.stateStand)
							arg_10_2())
					else
						arg_10_0.state.ChangeState(var_0_7.stateStand)
						arg_10_2())

			if #arg_10_1 <= 3 and not arg_10_3:
				arg_10_0.Jump(arg_10_1, arg_10_2)
			else
				var_10_0(arg_10_3),
		def Jump:(arg_15_0, arg_15_1, arg_15_2)
			arg_15_2 = arg_15_2 or function()
				return

			if #arg_15_1 == 0:
				arg_15_2()

				return

			local var_15_0 = {}

			for iter_15_0, iter_15_1 in pairs(arg_15_1):
				table.insert(var_15_0, function(arg_17_0)
					arg_15_0.state.ChangeState(var_0_7.stateJump)
					arg_15_0.onJump(iter_15_1, function()
						arg_15_0.state.ChangeState(var_0_7.stateStand)
						arg_17_0()))

			seriesAsync(var_15_0, function()
				local var_19_0 = arg_15_0.GetAction(arg_15_1[#arg_15_1])

				if var_19_0:
					arg_15_0.state.ChangeState(var_19_0, function()
						arg_15_0.state.ChangeState(var_0_7.stateStand)
						arg_15_2())
				else
					arg_15_0.state.ChangeState(var_0_7.stateStand)
					arg_15_2()),
		def Touch:(arg_21_0)
			if arg_21_0.state.IsStandState():
				arg_21_0.state.ChangeState(var_0_7.stateTouch, function()
					arg_21_0.state.ChangeState(var_0_7.stateStand)),
		def GetAction:(arg_23_0, arg_23_1)
			local var_23_0 = arg_23_1.config.icon

			if var_23_0 == "icon_1":
				return var_0_7.stateEvent
			elif var_23_0 == "icon_2":
				return var_0_7.stateGold
			elif var_23_0 == "icon_3":
				-- block empty
			elif var_23_0 == "icon_4":
				return var_0_7.stateEvent
			elif var_23_0 == "icon_5":
				return var_0_7.stateOil
			elif var_23_0 == "icon_6":
				return var_0_7.stateEvent,
		def InitPos:(arg_24_0, arg_24_1)
			arg_24_0.ChangePos(arg_24_1)
			arg_24_0.state.ChangeState(var_0_7.stateStand),
		def ChangePos:(arg_25_0, arg_25_1)
			assert(arg_25_1)
			arg_25_0.onUpdatePos(arg_25_1),
		def Dispose:(arg_26_0)
			arg_26_0.onMove = None
			arg_26_0.onUpdatePos = None
	}

local function var_0_11(arg_27_0)
	return {
		id = arg_27_0,
		config = var_0_2[arg_27_0],
		def ExistStory:(arg_28_0)
			return arg_28_0.config.story and arg_28_0.config.story != "0",
		def isEmpty:(arg_29_0)
			return arg_29_0.config.story == "0" and arg_29_0.config.drop == 0 and #arg_29_0.config.effect == 0,
		def Dispose:(arg_30_0)
			arg_30_0.config = None
	}

local function var_0_12(arg_31_0)
	local var_31_0 = {}

	var_31_0.row, var_31_0.column = arg_31_0.pos[1], arg_31_0.pos[2]
	var_31_0.index = arg_31_0.index
	var_31_0.id = arg_31_0.id
	var_31_0.flag = arg_31_0.flag

	assert(var_31_0.id)

	var_31_0.config = var_0_1[var_31_0.id]
	var_31_0.events = {}

	for iter_31_0, iter_31_1 in ipairs(var_0_2.all):
		if not table.contains(var_31_0.events, iter_31_1):
			table.insert(var_31_0.events, var_0_11(iter_31_1))

	function var_31_0.GetEvent(arg_32_0, arg_32_1)
		for iter_32_0, iter_32_1 in ipairs(arg_32_0.events):
			if iter_32_1.id == arg_32_1:
				return iter_32_1

	function var_31_0.SetNext(arg_33_0, arg_33_1)
		arg_33_0.next = arg_33_1

	function var_31_0.Dispose(arg_34_0)
		for iter_34_0, iter_34_1 in ipairs(arg_34_0.events):
			iter_34_1.Dispose()

	return var_31_0

local function var_0_13(arg_35_0, arg_35_1)
	local var_35_0 = {
		ROW = var_0_5,
		COLUMN = var_0_6 - 2,
		cellIds = arg_35_0,
		path = {}
	}

	var_35_0.char = None
	var_35_0.index = arg_35_1

	function var_35_0.onCreateCell(arg_36_0)
		return

	function var_35_0.onCreateChar(arg_37_0)
		return

	function var_35_0.Init(arg_38_0)
		local var_38_0 = 0

		for iter_38_0 = 0, var_35_0.ROW - 1:
			var_35_0.CeateCell({
				var_38_0,
				iter_38_0
			}, 0)

		local var_38_1 = var_35_0.ROW - 1

		for iter_38_1 = 1, var_35_0.COLUMN:
			var_35_0.CeateCell({
				iter_38_1,
				var_38_1
			}, #arg_38_0.path)

		local var_38_2 = var_35_0.COLUMN + 1

		for iter_38_2 = var_35_0.ROW - 1, 0, -1:
			var_35_0.CeateCell({
				var_38_2,
				iter_38_2
			}, #arg_38_0.path)

		local var_38_3 = 0
		local var_38_4 = #arg_38_0.path - 1

		for iter_38_3 = var_35_0.COLUMN, 1, -1:
			var_35_0.CeateCell({
				iter_38_3,
				var_38_3
			}, var_38_4)

		arg_38_0.CreateChar(var_0_3)

	function var_35_0.CreateChar(arg_39_0, arg_39_1)
		arg_39_0.char = var_0_10(arg_39_1)

		arg_39_0.onCreateChar(arg_39_0.char)

		local var_39_0 = arg_39_0.GetCell(arg_39_0.index)

		arg_39_0.char.InitPos(var_39_0)

	function var_35_0.CeateCell(arg_40_0, arg_40_1, arg_40_2)
		local var_40_0 = #arg_40_0.path
		local var_40_1 = var_0_12({
			pos = arg_40_1,
			index = var_40_0 + 1,
			id = arg_40_0.cellIds[var_40_0 + 1],
			flag = arg_40_2
		})

		if var_40_0 == 0:
			var_40_1.SetNext(var_40_1)
		else
			local var_40_2 = arg_40_0.path[var_40_0]
			local var_40_3 = arg_40_0.path[1]

			var_40_2.SetNext(var_40_1)
			var_40_1.SetNext(var_40_3)

		table.insert(arg_40_0.path, var_40_1)
		arg_40_0.onCreateCell(var_40_1)

	function var_35_0.GetPath(arg_41_0)
		return arg_41_0.path

	function var_35_0.GetChar(arg_42_0)
		return arg_42_0.char

	function var_35_0.GetPathCell(arg_43_0, arg_43_1)
		return _.map(arg_43_1, function(arg_44_0)
			return arg_43_0.path[arg_44_0])

	function var_35_0.UpdateCharPos(arg_45_0, arg_45_1, arg_45_2, arg_45_3)
		local var_45_0 = arg_45_0.GetPathCell(arg_45_1)

		arg_45_0.char.Move(var_45_0, arg_45_2, arg_45_3)

		arg_45_0.index = arg_45_1[#arg_45_1]

	function var_35_0.GetCell(arg_46_0, arg_46_1)
		return arg_46_0.path[arg_46_1]

	function var_35_0.GetPos(arg_47_0)
		return arg_47_0.index

	function var_35_0.Dispose(arg_48_0)
		for iter_48_0, iter_48_1 in ipairs(arg_48_0.path):
			iter_48_1.Dispose()

		arg_48_0.char.Dispose()

		arg_48_0.onCreateCell = None
		arg_48_0.onCreateChar = None

	return var_35_0

local function var_0_14(arg_49_0, arg_49_1)
	local var_49_0 = {
		_tf = arg_49_0,
		_img = arg_49_0.GetComponent(typeof(Image)),
		cell = arg_49_1,
		interval = Vector2(0, 0),
		startPos = Vector2(0, 0),
		offset = Vector2(arg_49_0.rect.width * 0.5 + 2.5, arg_49_0.rect.height * 0.5 - 2),
		def GetGenPos:(arg_50_0)
			local var_50_0 = arg_50_0.cell.column
			local var_50_1 = arg_50_0.cell.row
			local var_50_2 = arg_50_0.startPos.x + var_50_0 * arg_50_0.offset.x + var_50_1 * arg_50_0.offset.x
			local var_50_3 = arg_50_0.startPos.y + var_50_0 * arg_50_0.offset.y + var_50_1 * -arg_50_0.offset.y

			return Vector3(var_50_2, var_50_3, 0),
		def UpdateStyle:(arg_51_0)
			local var_51_0 = arg_51_0.cell
			local var_51_1 = GetSpriteFromAtlas("ui/activityuipage/monopolycar_atlas", var_51_0.config.icon)

			arg_51_0._img.sprite = var_51_1

			arg_51_0._img.SetNativeSize(),
		def Dispose:(arg_52_0)
			return
	}

	setAnchoredPosition(arg_49_0, var_49_0.GetGenPos())
	var_49_0._tf.SetSiblingIndex(arg_49_1.flag)

	return var_49_0

local function var_0_15(arg_53_0, arg_53_1)
	local var_53_0 = {
		_tf = arg_53_0
	}

	var_53_0.WalkSpeed = 1
	var_53_0.RunSpeed = 0.5
	var_53_0.jumpSpeed = 0.5
	var_53_0.char = arg_53_1

	local var_53_1 = arg_53_0.GetChild(0)

	tf(var_53_1).localScale = Vector3(0.5, 0.5, 0.5)
	var_53_0.SpineAnimUI = var_53_1.GetComponent("SpineAnimUI")

	local var_53_2 = GameObject("mouseChild")

	tf(var_53_2).SetParent(tf(var_53_1))

	tf(var_53_2).localPosition = Vector3.zero

	setParent(var_53_2, var_53_1)

	GetOrAddComponent(var_53_2, "Image").color = Color.New(0, 0, 0, 0)

	local var_53_3 = var_53_2.GetComponent(typeof(RectTransform))

	var_53_3.sizeDelta = Vector2(3, 3)
	var_53_3.pivot = Vector2(0.5, 0)
	var_53_3.anchoredPosition = Vector2(0, 0)

	onButton(None, var_53_2, function()
		var_53_0.char.Touch())

	function var_53_0.Action(arg_55_0, arg_55_1, arg_55_2, arg_55_3)
		local var_55_0 = {}

		_.each(arg_55_1, function(arg_56_0)
			table.insert(var_55_0, function(arg_57_0)
				arg_55_0.UpdateScale(arg_56_0)

				local var_57_0 = arg_56_0.GetGenPos()

				if arg_55_0._tf.localPosition == var_57_0:
					arg_57_0()
				else
					LeanTween.moveLocal(go(arg_55_0._tf), var_57_0, arg_55_3).setOnComplete(System.Action(function()
						arg_55_0.preCellTF = arg_56_0

						arg_57_0()))))
		seriesAsync(var_55_0, function()
			if arg_55_2:
				arg_55_2())

	function var_53_0.Move(arg_60_0, arg_60_1, arg_60_2)
		if #arg_60_1 > 3:
			arg_60_0.Action(arg_60_1, arg_60_2, arg_60_0.RunSpeed)
		else
			arg_60_0.Action(arg_60_1, arg_60_2, arg_60_0.WalkSpeed)

	function var_53_0.Jump(arg_61_0, arg_61_1, arg_61_2)
		arg_61_0.Action({
			arg_61_1
		}, function()
			arg_61_2()
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_STEP_MONOPOLY), arg_61_0.jumpSpeed)

	function var_53_0.UpdatePos(arg_63_0, arg_63_1)
		arg_63_0.preCellTF = arg_63_1

		local var_63_0 = arg_63_1.GetGenPos()

		arg_63_0._tf.localPosition = var_63_0

	function var_53_0.UpdateScale(arg_64_0, arg_64_1)
		local var_64_0 = 1

		arg_64_0.preCellTF = arg_64_0.preCellTF or arg_64_1

		if arg_64_1.cell.row > arg_64_0.preCellTF.cell.row or arg_64_1.cell.column > arg_64_0.preCellTF.cell.column:
			var_64_0 = 1
		elif arg_64_1.cell.row < arg_64_0.preCellTF.cell.row or arg_64_1.cell.column < arg_64_0.preCellTF.cell.column:
			var_64_0 = -1

		arg_64_0._tf.localScale = Vector3(var_64_0, 1, 1)

	function var_53_0.ChangeAction(arg_65_0, arg_65_1, arg_65_2)
		arg_65_0.SpineAnimUI.SetActionCallBack(None)
		arg_65_0.SpineAnimUI.SetAction(arg_65_1, 0)
		arg_65_0.SpineAnimUI.SetActionCallBack(function(arg_66_0)
			if arg_66_0 == "finish":
				arg_65_0.SpineAnimUI.SetActionCallBack(None)
				arg_65_2())

	function var_53_0.Dispose(arg_67_0)
		arg_67_0.SpineAnimUI.SetActionCallBack(None)

		arg_67_0.char.onMove = None

		if arg_67_0.timer:
			arg_67_0.timer.Stop()

			arg_67_0.timer = None

	return var_53_0

def var_0_0.SetUp(arg_68_0, arg_68_1, arg_68_2):
	arg_68_0.viewComponent = arg_68_1

	local var_68_0 = arg_68_0.viewComponent._tf

	pg.DelegateInfo.New(arg_68_0)

	arg_68_0._tf = var_68_0
	arg_68_0._go = go(var_68_0)
	arg_68_0.models = {}

	parallelAsync({
		function(arg_69_0)
			local var_69_0 = Ship.New({
				configId = var_0_3,
				skin_id = var_0_4
			})
			local var_69_1 = var_69_0.getPrefab()

			PoolMgr.GetInstance().GetSpineChar(var_69_1, True, function(arg_70_0)
				arg_68_0.models[var_69_0.configId] = arg_70_0

				arg_69_0()),
		function(arg_71_0)
			onNextTick(arg_71_0)
	}, function()
		arg_68_0.setActivity(arg_68_2)
		arg_68_0.init()
		arg_68_0.didEnter())

def var_0_0.setActivity(arg_73_0, arg_73_1):
	arg_73_0.activity = arg_73_1

	local var_73_0 = arg_73_0.activity.data1
	local var_73_1 = arg_73_0.activity.data1_list[1]

	arg_73_0.useCount = arg_73_0.activity.data1_list[2]

	local var_73_2 = arg_73_0.activity.data1_list[3] - 1
	local var_73_3 = arg_73_0.activity.data2_list[1]
	local var_73_4 = arg_73_0.activity.data2_list[2]
	local var_73_5 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_73_6 = math.ceil((var_73_5 - var_73_0) / 86400) * arg_73_0.activity.getDataConfig("daily_time")

	arg_73_0.pos = arg_73_0.activity.data2
	arg_73_0.step = arg_73_0.activity.data3
	arg_73_0.effectId = arg_73_0.activity.data4
	arg_73_0.totalCnt = var_73_6 + var_73_1
	arg_73_0.leftCount = arg_73_0.totalCnt - arg_73_0.useCount

	local var_73_7 = arg_73_1.getDataConfig("reward_time")

	arg_73_0.nextredPacketStep = var_73_7 - arg_73_0.useCount % var_73_7
	arg_73_0.advanceTotalCnt = #arg_73_1.getDataConfig("reward")
	arg_73_0.isAdvanceRp = arg_73_0.advanceTotalCnt - var_73_4 > 0
	arg_73_0.leftAwardCnt = var_73_3 - var_73_4
	arg_73_0.advanceRpCount = math.max(0, math.min(var_73_3, arg_73_0.advanceTotalCnt) - var_73_4)
	arg_73_0.commonRpCount = math.max(0, var_73_3 - arg_73_0.advanceTotalCnt) - math.max(0, var_73_4 - arg_73_0.advanceTotalCnt)
	arg_73_0.leftDropShipCnt = 10 - var_73_2

def var_0_0.NetActivity(arg_74_0, arg_74_1):
	arg_74_0.setActivity(arg_74_1)
	arg_74_0.updateLeftCount()
	arg_74_0.updateNextRedPacketStep()

def var_0_0.init(arg_75_0):
	arg_75_0.blockAllEvent(False)

	arg_75_0.bg = arg_75_0.findTF("AD")
	arg_75_0.mapCellTpl = arg_75_0.getTpl("mapCell", arg_75_0.bg)
	arg_75_0.mapContainer = arg_75_0.findTF("mapContainer", arg_75_0.bg)
	arg_75_0.charTpl = arg_75_0.getTpl("char", arg_75_0.bg)
	arg_75_0.startBtn = arg_75_0.findTF("start", arg_75_0.bg)
	arg_75_0.valueImg = arg_75_0.findTF("value", arg_75_0.bg).GetComponent(typeof(Image))
	arg_75_0.leftcountLabel = arg_75_0.findTF("leftcount", arg_75_0.bg).GetComponent(typeof(Text))
	arg_75_0.leftCountTF = arg_75_0.findTF("leftcount/Text", arg_75_0.bg).GetComponent(typeof(Text))
	arg_75_0.nextRedPacketStepTF = arg_75_0.findTF("nextRpStep/Text", arg_75_0.bg).GetComponent(typeof(Text))
	arg_75_0.commonRp = arg_75_0.findTF("rp", arg_75_0.bg)
	arg_75_0.commonAnim = arg_75_0.commonRp.GetComponent(typeof(Animator))
	arg_75_0.commonRpCnt = arg_75_0.findTF("rp_text/Text", arg_75_0.bg).GetComponent(typeof(Text))
	arg_75_0.dropShipTxt = arg_75_0.findTF("AD/drop_ship_text").GetComponent(typeof(Text))
	arg_75_0.helpBtn = arg_75_0.findTF("AD/help")
	arg_75_0.anim = arg_75_0.findTF("AD/anim")

	setActive(arg_75_0.anim, False)

	arg_75_0.leftcountLabel.text = i18n("monopoly_left_count")
	arg_75_0.advanceTag = arg_75_0.findTF("AD/rp/sp")
	arg_75_0.advanceLabel = arg_75_0.findTF("AD/rp_text/sp")
	arg_75_0.advancecLabel = arg_75_0.findTF("AD/rp_text/label")
	arg_75_0.advanceImage = arg_75_0.findTF("AD/rp_text/sp_img")
	arg_75_0.advanceTxt = arg_75_0.findTF("AD/rp_text/sp_img/Text").GetComponent(typeof(Text))

def var_0_0.updateNextRedPacketStep(arg_76_0):
	arg_76_0.nextRedPacketStepTF.text = arg_76_0.nextredPacketStep

def var_0_0.updateLeftCount(arg_77_0):
	arg_77_0.leftCountTF.text = arg_77_0.leftCount

	arg_77_0.commonAnim.SetInteger("count", arg_77_0.leftAwardCnt)

	arg_77_0.commonRpCnt.text = arg_77_0.commonRpCount

def var_0_0.updateValue(arg_78_0, arg_78_1):
	if arg_78_1 != 0:
		arg_78_0.valueImg.sprite = GetSpriteFromAtlas("ui/activityuipage/monopoly_atlas", arg_78_1)

		arg_78_0.valueImg.SetNativeSize()

	setActive(go(arg_78_0.valueImg), arg_78_1 != 0)

def var_0_0.didEnter(arg_79_0):
	setActive(arg_79_0.startBtn, arg_79_0.leftCount > 0)
	arg_79_0.updateLeftCount()
	arg_79_0.updateValue(0)
	arg_79_0.updateNextRedPacketStep()

	local var_79_0 = arg_79_0.activity.getDataConfig("map")

	arg_79_0.mapVO = var_0_13(var_79_0, arg_79_0.pos)

	arg_79_0.createMap(arg_79_0.mapVO)
	arg_79_0.mapVO.Init()
	arg_79_0.checkState()
	onButton(arg_79_0, arg_79_0.startBtn, function()
		if arg_79_0.block:
			return

		if arg_79_0.leftCount <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_count_noenough"))

			return

		arg_79_0.startAction(), SFX_PANEL)
	onButton(arg_79_0, arg_79_0.commonRp, function()
		if arg_79_0.leftAwardCnt > 0:
			arg_79_0.emit(MonopolyPage.ON_AWARD), SFX_PANEL)
	onButton(arg_79_0, arg_79_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_chunjie_monopoly.tip
		}), SFX_PANEL)

def var_0_0.blockAllEvent(arg_83_0, arg_83_1):
	arg_83_0.emit(ActivityMainScene.LOCK_ACT_MAIN, arg_83_1)

	arg_83_0.block = arg_83_1

def var_0_0.triggerEvent(arg_84_0, arg_84_1, arg_84_2, arg_84_3):
	local var_84_0 = arg_84_0.mapVO.GetCell(arg_84_1).GetEvent(arg_84_2)

	local function var_84_1(arg_85_0, arg_85_1)
		if arg_85_0 and arg_85_0.ExistStory():
			pg.NewStoryMgr.GetInstance().Play(arg_85_0.config.story, arg_85_1, True, True)
		else
			arg_85_1()

	local var_84_2 = {
		function(arg_86_0)
			var_84_1(var_84_0, arg_86_0),
		function(arg_87_0)
			local var_87_0

			local function var_87_1()
				if not var_84_0 or var_84_0.isEmpty():
					arg_87_0()

					return

				arg_84_0.emit(MonopolyPage.ON_TRIGGER, arg_84_0.activity.id, function(arg_89_0, arg_89_1)
					if not arg_89_0 or #arg_89_0 == 0:
						arg_87_0()

						return

					arg_84_0.mapVO.UpdateCharPos(arg_89_0, function()
						local var_90_0 = arg_89_0[#arg_89_0]

						var_84_0 = arg_84_0.mapVO.GetCell(var_90_0).GetEvent(arg_89_1)

						var_84_1(var_84_0, var_87_1), True))

			var_87_1()
	}

	seriesAsync(var_84_2, arg_84_3)

def var_0_0.checkState(arg_91_0):
	local var_91_0 = {}

	arg_91_0.blockAllEvent(True)

	local var_91_1 = arg_91_0.getStrory()

	if var_91_1:
		table.insert(var_91_0, function(arg_92_0)
			pg.NewStoryMgr.GetInstance().Play(var_91_1, arg_92_0))

	if arg_91_0.effectId != 0:
		table.insert(var_91_0, function(arg_93_0)
			local var_93_0 = arg_91_0.mapVO.GetPos()

			arg_91_0.triggerEvent(var_93_0, arg_91_0.effectId, arg_93_0))

	if arg_91_0.step != 0:
		table.insert(var_91_0, function(arg_94_0)
			arg_91_0.emit(MonopolyPage.ON_MOVE, arg_91_0.activity.id, function(arg_95_0, arg_95_1, arg_95_2)
				if not arg_95_1 or #arg_95_1 == 0:
					arg_94_0()

					return

				arg_91_0.mapVO.UpdateCharPos(arg_95_1, function()
					local var_96_0 = arg_95_1[#arg_95_1]

					arg_91_0.triggerEvent(var_96_0, arg_95_2, arg_94_0))))

	seriesAsync(var_91_0, function()
		arg_91_0.blockAllEvent(False))

def var_0_0.startAction(arg_98_0):
	local var_98_0 = arg_98_0.activity.id
	local var_98_1 = 0

	local function var_98_2(arg_99_0)
		if var_98_1 == 0:
			arg_99_0()

			return

		arg_98_0.emit(MonopolyPage.ON_MOVE, var_98_0, function(arg_100_0, arg_100_1, arg_100_2)
			if not arg_100_1 or #arg_100_1 == 0:
				arg_99_0()

				return

			var_98_1 = arg_100_0

			arg_98_0.mapVO.UpdateCharPos(arg_100_1, function()
				local var_101_0 = arg_100_1[#arg_100_1]

				arg_98_0.triggerEvent(var_101_0, arg_100_2, arg_99_0)))

	seriesAsync({
		function(arg_102_0)
			setActive(arg_98_0.startBtn, False)
			arg_98_0.blockAllEvent(True)
			arg_98_0.playerAnim(arg_102_0),
		function(arg_103_0)
			arg_98_0.emit(MonopolyPage.ON_START, var_98_0, function(arg_104_0)
				var_98_1 = arg_104_0

				arg_98_0.updateValue(arg_104_0)
				arg_103_0()),
		function(arg_105_0)
			var_98_2(arg_105_0),
		function(arg_106_0)
			var_98_2(arg_106_0),
		function(arg_107_0)
			local var_107_0 = arg_98_0.getStrory()

			if not var_107_0:
				arg_107_0()

				return

			pg.NewStoryMgr.GetInstance().Play(var_107_0, arg_107_0)
	}, function()
		arg_98_0.updateValue(0)
		arg_98_0.blockAllEvent(False)
		setActive(arg_98_0.startBtn, arg_98_0.leftCount > 0))

def var_0_0.getStrory(arg_109_0):
	local var_109_0 = arg_109_0.useCount
	local var_109_1 = arg_109_0.activity.getDataConfig("story") or {}
	local var_109_2 = _.detect(var_109_1, function(arg_110_0)
		return arg_110_0[1] == var_109_0)

	if var_109_2:
		return var_109_2[2]

	return None

def var_0_0.createMap(arg_111_0, arg_111_1):
	arg_111_0.cellTFs, arg_111_0.charCard = {}

	function arg_111_1.onCreateCell(arg_112_0)
		local var_112_0 = cloneTplTo(arg_111_0.mapCellTpl, arg_111_0.mapContainer)
		local var_112_1 = var_0_14(var_112_0, arg_112_0)

		var_112_1.UpdateStyle()

		arg_111_0.cellTFs[arg_112_0.index] = var_112_1

	function arg_111_1.onCreateChar(arg_113_0)
		local var_113_0 = cloneTplTo(arg_111_0.charTpl, arg_111_0.mapContainer)
		local var_113_1 = arg_111_0.models[arg_113_0.ship.configId]

		setParent(var_113_1, var_113_0)

		arg_111_0.charCard = var_0_15(var_113_0, arg_113_0)

		function arg_113_0.onMove(arg_114_0, arg_114_1)
			local var_114_0 = _.map(arg_114_0, function(arg_115_0)
				return arg_111_0.cellTFs[arg_115_0.index])

			arg_111_0.charCard.Move(var_114_0, arg_114_1)

		function arg_113_0.onUpdatePos(arg_116_0)
			local var_116_0 = arg_111_0.cellTFs[arg_116_0.index]

			arg_111_0.charCard.UpdatePos(var_116_0)

		function arg_113_0.state.onActionUpdated(arg_117_0, arg_117_1)
			arg_111_0.charCard.ChangeAction(arg_117_0, arg_117_1)

		function arg_113_0.onJump(arg_118_0, arg_118_1)
			local var_118_0 = arg_111_0.cellTFs[arg_118_0.index]

			arg_111_0.charCard.Jump(var_118_0, arg_118_1)

def var_0_0.playerAnim(arg_119_0, arg_119_1):
	setActive(arg_119_0.anim, True)

	if arg_119_0.timer:
		arg_119_0.timer.Stop()

	arg_119_0.timer = Timer.New(function()
		arg_119_1()
		setActive(arg_119_0.anim, False), 1.5, 1)

	arg_119_0.timer.Start()

def var_0_0.findTF(arg_121_0, arg_121_1, arg_121_2):
	assert(arg_121_0._tf, "transform should exist")

	return findTF(arg_121_2 or arg_121_0._tf, arg_121_1)

def var_0_0.getTpl(arg_122_0, arg_122_1, arg_122_2):
	local var_122_0 = arg_122_0.findTF(arg_122_1, arg_122_2)

	var_122_0.SetParent(arg_122_0._tf, False)
	SetActive(var_122_0, False)

	return var_122_0

def var_0_0.Destroy(arg_123_0):
	for iter_123_0, iter_123_1 in pairs(arg_123_0.cellTFs):
		iter_123_1.Dispose()

	arg_123_0.charCard.Dispose()
	arg_123_0.mapVO.Dispose()

	arg_123_0.cellTFs = None
	arg_123_0.charCard = None
	arg_123_0.mapVO = None

	if arg_123_0.timer:
		arg_123_0.timer.Stop()

		arg_123_0.timer = None

	pg.DelegateInfo.Dispose(arg_123_0)

def var_0_0.emit(arg_124_0, arg_124_1, arg_124_2, arg_124_3):
	arg_124_0.viewComponent.emit(arg_124_1, arg_124_2, arg_124_3)

return var_0_0
