local var_0_0 = class("SnackView", import("..BaseMiniGameView"))

var_0_0.States_Before = 0
var_0_0.States_Memory = 1
var_0_0.States_Select = 2
var_0_0.States_Finished = 3
var_0_0.Ani_Close_2_Open = True
var_0_0.Ani_Open_2_Close = False
var_0_0.Bubble_Fade_Time = 0.5
var_0_0.Order_Num = 3
var_0_0.Snack_Num = 9

def var_0_0.getUIName(arg_1_0):
	return "Snack"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.initList()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.initTime()
	arg_3_0.updateSDModel()
	arg_3_0.setState(var_0_0.States_Before)

def var_0_0.OnGetAwardDone(arg_4_0, arg_4_1):
	if arg_4_1.cmd == MiniGameOPCommand.CMD_COMPLETE:
		local var_4_0 = arg_4_0.GetMGHubData()

		if var_4_0.ultimate == 0 and var_4_0.usedtime >= var_4_0.getConfig("reward_need"):
			pg.m02.sendNotification(GAME.SEND_MINI_GAME_OP, {
				hubid = var_4_0.id,
				cmd = MiniGameOPCommand.CMD_ULTIMATE,
				args1 = {}
			})
	elif arg_4_1.cmd == MiniGameOPCommand.CMD_ULTIMATE:
		-- block empty

def var_0_0.OnSendMiniGameOPDone(arg_5_0):
	arg_5_0.updateCount()

	local var_5_0 = (getProxy(MiniGameProxy).GetMiniGameData(MiniGameDataCreator.ShrineGameID).GetRuntimeData("count") or 0) + 1

	pg.m02.sendNotification(GAME.MODIFY_MINI_GAME_DATA, {
		id = MiniGameDataCreator.ShrineGameID,
		map = {
			count = var_5_0
		}
	})

def var_0_0.onBackPressed(arg_6_0):
	if arg_6_0.state == var_0_0.States_Before:
		arg_6_0.emit(var_0_0.ON_BACK_PRESSED)

		return

	if arg_6_0.timer:
		arg_6_0.timer.Stop()

	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		content = i18n("tips_summergame_exit"),
		def onYes:()
			arg_6_0.countTime = 0

			arg_6_0.timer.Start(),
		def onNo:()
			arg_6_0.timer.Start()
	})

def var_0_0.willExit(arg_9_0):
	if arg_9_0.timer:
		arg_9_0.timer.Stop()

	if arg_9_0.prefab and arg_9_0.model:
		PoolMgr.GetInstance().ReturnSpineChar(arg_9_0.prefab, arg_9_0.model)

		arg_9_0.prefab = None
		arg_9_0.model = None

def var_0_0.findUI(arg_10_0):
	local var_10_0 = arg_10_0.findTF("ForNotch")

	arg_10_0.backBtn = arg_10_0.findTF("BackBtn", var_10_0)
	arg_10_0.helpBtn = arg_10_0.findTF("HelpBtn", var_10_0)
	arg_10_0.countText = arg_10_0.findTF("Count/CountText", var_10_0)

	local var_10_1 = arg_10_0.findTF("GameContent")

	arg_10_0.startBtn = arg_10_0.findTF("StartBtn", var_10_1)

	local var_10_2 = arg_10_0.findTF("Tip", var_10_1)

	arg_10_0.considerTipTF = arg_10_0.findTF("ConsiderTip", var_10_2)
	arg_10_0.considerTimeText = arg_10_0.findTF("TimeText", arg_10_0.considerTipTF)
	arg_10_0.selectTipTF = arg_10_0.findTF("SelectTip", var_10_2)
	arg_10_0.selectTimeText = arg_10_0.findTF("TimeText", arg_10_0.selectTipTF)
	arg_10_0.selectedContainer = arg_10_0.findTF("SelectedContainer", var_10_1)
	arg_10_0.selectedTpl = arg_10_0.findTF("SelectedTpl", var_10_1)
	arg_10_0.selectedContainerCG = GetComponent(arg_10_0.selectedContainer, "CanvasGroup")
	arg_10_0.snackContainer = arg_10_0.findTF("SnackContainer", var_10_1)
	arg_10_0.animtor = GetComponent(arg_10_0.snackContainer, "Animator")
	arg_10_0.dftAniEvent = GetComponent(arg_10_0.snackContainer, "DftAniEvent")

	arg_10_0.dftAniEvent.SetEndEvent(function(arg_11_0)
		arg_10_0.setState(var_0_0.States_Select))

	arg_10_0.spineCharContainer = arg_10_0.findTF("SpineChar", var_10_1)

def var_0_0.initData(arg_12_0):
	arg_12_0.state = None
	arg_12_0.orderIDList = {}
	arg_12_0.selectedIDList = {}
	arg_12_0.snackIDList = {}
	arg_12_0.score = 0
	arg_12_0.packageData = {}
	arg_12_0.selectedTFList = {}
	arg_12_0.snackTFList = {}
	arg_12_0.selectedSnackTFList = {}

def var_0_0.initTime(arg_13_0):
	arg_13_0.orginMemoryTime = arg_13_0.GetMGData().getConfig("simple_config_data").memory_time
	arg_13_0.orginSelectTime = arg_13_0.GetMGData().getConfig("simple_config_data").select_time
	arg_13_0.countTime = None
	arg_13_0.leftTime = arg_13_0.orginSelectTime

def var_0_0.initTimer(arg_14_0, arg_14_1):
	if arg_14_0.state == var_0_0.States_Memory:
		arg_14_0.countTime = arg_14_0.orginMemoryTime
	elif arg_14_0.state == var_0_0.States_Select:
		arg_14_0.countTime = arg_14_0.leftTime

	arg_14_0.timer = Timer.New(arg_14_1, 1, -1)

	arg_14_0.timer.Start()

def var_0_0.initList(arg_15_0):
	for iter_15_0 = 1, var_0_0.Order_Num:
		local var_15_0 = arg_15_0.selectedContainer.GetChild(iter_15_0 - 1)

		arg_15_0.selectedTFList[iter_15_0] = var_15_0

	for iter_15_1 = 1, var_0_0.Snack_Num:
		local var_15_1 = arg_15_0.snackContainer.GetChild(iter_15_1 - 1)

		arg_15_0.snackTFList[iter_15_1] = var_15_1

def var_0_0.addListener(arg_16_0):
	onButton(arg_16_0, arg_16_0.backBtn, function()
		arg_16_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_16_0, arg_16_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_summer_food.tip
		}), SFX_PANEL)
	onButton(arg_16_0, arg_16_0.startBtn, function()
		arg_16_0.setState(var_0_0.States_Memory), SFX_PANEL)

	for iter_16_0 = 1, var_0_0.Snack_Num:
		local var_16_0 = arg_16_0.snackContainer.GetChild(iter_16_0 - 1)

		onButton(arg_16_0, var_16_0, function()
			local var_20_0 = arg_16_0.snackIDList[iter_16_0]
			local var_20_1 = arg_16_0.findTF("SelectedTag", var_16_0)

			if isActive(var_20_1) == True:
				table.removebyvalue(arg_16_0.selectedIDList, var_20_0)
				arg_16_0.updateSelectedList(arg_16_0.selectedIDList)

				arg_16_0.selectedSnackTFList[var_20_0] = None

				setActive(var_20_1, False)
				arg_16_0.updateSelectedOrderTag()
			else
				table.insert(arg_16_0.selectedIDList, var_20_0)
				arg_16_0.updateSelectedList(arg_16_0.selectedIDList)

				arg_16_0.selectedSnackTFList[var_20_0] = var_16_0

				setActive(var_20_1, True)
				arg_16_0.updateSelectedOrderTag()

				if #arg_16_0.selectedIDList == var_0_0.Order_Num:
					arg_16_0.timer.Stop()
					arg_16_0.setState(var_0_0.States_Finished), SFX_PANEL)

def var_0_0.updateSDModel(arg_21_0):
	local var_21_0 = getProxy(PlayerProxy).getData()
	local var_21_1 = getProxy(BayProxy).getShipById(var_21_0.character).getPrefab()

	pg.UIMgr.GetInstance().LoadingOn()
	PoolMgr.GetInstance().GetSpineChar(var_21_1, True, function(arg_22_0)
		pg.UIMgr.GetInstance().LoadingOff()

		arg_21_0.prefab = var_21_1
		arg_21_0.model = arg_22_0
		tf(arg_22_0).localScale = Vector3(1, 1, 1)

		arg_22_0.GetComponent("SpineAnimUI").SetAction("stand", 0)
		setParent(arg_22_0, arg_21_0.spineCharContainer))

def var_0_0.updateSelectedList(arg_23_0, arg_23_1):
	arg_23_1 = arg_23_1 or {}

	for iter_23_0 = 1, var_0_0.Order_Num:
		local var_23_0 = arg_23_0.selectedContainer.GetChild(iter_23_0 - 1)
		local var_23_1 = arg_23_0.findTF("Empty", var_23_0)
		local var_23_2 = arg_23_0.findTF("Full", var_23_0)
		local var_23_3 = arg_23_0.findTF("SnackImg", var_23_2)

		arg_23_0.selectedTFList[iter_23_0] = var_23_0

		local var_23_4 = arg_23_1[iter_23_0]

		setActive(var_23_2, var_23_4)
		setActive(var_23_1, not var_23_4)

		if var_23_4:
			setImageSprite(var_23_3, GetSpriteFromAtlas("ui/snackui_atlas", "snack_" .. var_23_4))

def var_0_0.updateSnackList(arg_24_0, arg_24_1):
	for iter_24_0 = 1, var_0_0.Snack_Num:
		local var_24_0 = arg_24_0.snackContainer.GetChild(iter_24_0 - 1)
		local var_24_1 = arg_24_0.findTF("SnackImg", var_24_0)
		local var_24_2 = arg_24_1[iter_24_0]

		setImageSprite(var_24_1, GetSpriteFromAtlas("ui/snackui_atlas", "snack_" .. var_24_2))

		local var_24_3 = arg_24_0.findTF("SelectedTag", var_24_0)

		setActive(var_24_3, False)

		arg_24_0.snackTFList[iter_24_0] = var_24_0
		iter_24_0 = iter_24_0 + 1

def var_0_0.updateCount(arg_25_0):
	setText(arg_25_0.countText, arg_25_0.GetMGHubData().count)

def var_0_0.updateSelectedOrderTag(arg_26_0, arg_26_1):
	for iter_26_0, iter_26_1 in pairs(arg_26_0.selectedSnackTFList):
		local var_26_0 = arg_26_0.findTF("SelectedTag", iter_26_1)

		if arg_26_1:
			setActive(var_26_0, False)
		else
			local var_26_1 = table.indexof(arg_26_0.selectedIDList, iter_26_0, 1)

			setImageSprite(var_26_0, GetSpriteFromAtlas("ui/snackui_atlas", "order_" .. var_26_1))

def var_0_0.updateSnackInteractable(arg_27_0, arg_27_1):
	for iter_27_0, iter_27_1 in ipairs(arg_27_0.snackTFList):
		setButtonEnabled(iter_27_1, arg_27_1)

def var_0_0.onStateChange(arg_28_0):
	if arg_28_0.state == var_0_0.States_Before:
		setActive(arg_28_0.selectedContainer, False)
		setActive(arg_28_0.startBtn, True)
		setActive(arg_28_0.considerTipTF, False)
		setActive(arg_28_0.selectTipTF, False)
		arg_28_0.updateCount()
		arg_28_0.updateSnackInteractable(False)
	elif arg_28_0.state == var_0_0.States_Memory:
		setActive(arg_28_0.selectedContainer, True)
		setActive(arg_28_0.startBtn, False)

		arg_28_0.orderIDList = arg_28_0.randFetch(3, 9)

		arg_28_0.updateSelectedList(arg_28_0.orderIDList)

		arg_28_0.snackIDList = arg_28_0.randFetch(9, 9)

		arg_28_0.updateSnackList(arg_28_0.snackIDList)
		arg_28_0.updateSnackInteractable(False)

		local function var_28_0()
			arg_28_0.countTime = arg_28_0.countTime - 1

			setText(arg_28_0.considerTimeText, arg_28_0.countTime)

			if arg_28_0.countTime == 0:
				arg_28_0.timer.Stop()
				arg_28_0.animtor.SetBool("AniSwitch", var_0_0.Ani_Close_2_Open)

		LeanTween.value(go(arg_28_0.selectedContainer), 0, 1, var_0_0.Bubble_Fade_Time).setOnUpdate(System.Action_float(function(arg_30_0)
			arg_28_0.selectedContainerCG.alpha = arg_30_0)).setOnComplete(System.Action(function()
			setActive(arg_28_0.considerTipTF, True)
			setActive(arg_28_0.selectTipTF, False)
			arg_28_0.initTimer(var_28_0)
			setText(arg_28_0.considerTimeText, arg_28_0.countTime)))
	elif arg_28_0.state == var_0_0.States_Select:
		setActive(arg_28_0.considerTipTF, False)
		setActive(arg_28_0.selectTipTF, True)
		arg_28_0.updateSelectedList()
		arg_28_0.updateSnackInteractable(True)

		local function var_28_1()
			arg_28_0.countTime = arg_28_0.countTime - 1

			setText(arg_28_0.selectTimeText, arg_28_0.countTime)

			if arg_28_0.countTime == 0:
				arg_28_0.timer.Stop()
				arg_28_0.setState(var_0_0.States_Finished)

		arg_28_0.initTimer(var_28_1)
		setText(arg_28_0.selectTimeText, arg_28_0.countTime)
	elif arg_28_0.state == var_0_0.States_Finished:
		arg_28_0.updateSnackInteractable(False)
		LeanTween.value(go(arg_28_0.selectedContainer), 1, 0, var_0_0.Bubble_Fade_Time).setOnUpdate(System.Action_float(function(arg_33_0)
			arg_28_0.selectedContainerCG.alpha = arg_33_0)).setOnComplete(System.Action(function()
			arg_28_0.openResultView()))

def var_0_0.openResultView(arg_35_0):
	arg_35_0.packageData = {
		orderIDList = arg_35_0.orderIDList,
		selectedIDList = arg_35_0.selectedIDList,
		countTime = arg_35_0.countTime,
		score = arg_35_0.score,
		correctNumToEXValue = arg_35_0.GetMGData().getConfig("simple_config_data").correct_value,
		scoreLevel = arg_35_0.GetMGData().getConfig("simple_config_data").score_level,
		def onSubmit:(arg_36_0)
			if arg_35_0.GetMGHubData().count > 0:
				arg_35_0.SendSuccess(arg_36_0)

			arg_35_0.score = 0
			arg_35_0.countTime = None
			arg_35_0.leftTime = arg_35_0.orginSelectTime
			arg_35_0.orderIDList = {}
			arg_35_0.selectedIDList = {}
			arg_35_0.snackIDList = {}

			arg_35_0.updateSelectedOrderTag(True)

			arg_35_0.selectedSnackTFList = {}

			arg_35_0.animtor.SetBool("AniSwitch", var_0_0.Ani_Open_2_Close)
			arg_35_0.setState(var_0_0.States_Before),
		def onContinue:()
			arg_35_0.score = arg_35_0.packageData.score
			arg_35_0.leftTime = arg_35_0.packageData.countTime
			arg_35_0.orderIDList = {}
			arg_35_0.selectedIDList = {}
			arg_35_0.snackIDList = {}
			arg_35_0.selectedSnackTFList = {}

			arg_35_0.animtor.SetBool("AniSwitch", var_0_0.Ani_Open_2_Close)
			arg_35_0.setState(var_0_0.States_Memory)
	}
	arg_35_0.snackResultView = SnackResultView.New(arg_35_0._tf, arg_35_0.event, arg_35_0.packageData)

	arg_35_0.snackResultView.Reset()
	arg_35_0.snackResultView.Load()

def var_0_0.randFetch(arg_38_0, arg_38_1, arg_38_2):
	local var_38_0 = {}
	local var_38_1 = {}

	for iter_38_0 = 1, arg_38_1:
		local var_38_2 = math.random(iter_38_0, arg_38_2)
		local var_38_3 = var_38_1[var_38_2] or var_38_2

		var_38_1[var_38_2] = var_38_1[iter_38_0] or iter_38_0
		var_38_1[iter_38_0] = var_38_3

		table.insert(var_38_0, var_38_3)

	return var_38_0

def var_0_0.setState(arg_39_0, arg_39_1):
	if arg_39_0.state == arg_39_1:
		return

	arg_39_0.state = arg_39_1

	arg_39_0.onStateChange()

return var_0_0
