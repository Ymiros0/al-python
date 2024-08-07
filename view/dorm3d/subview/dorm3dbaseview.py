local var_0_0 = class("Dorm3dBaseView", import("view.base.BaseSubView"))

def var_0_0.SetApartment(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.apartment = arg_1_1

	local var_1_0 = "dorm3d_enter_count_" .. arg_1_0.apartment.configId

	PlayerPrefs.SetInt(var_1_0, PlayerPrefs.GetInt(var_1_0, 0) + 1)
	arg_1_0.UpdateFavorDisplay()
	arg_1_0.UpdateContactState()

def var_0_0.OnInit(arg_2_0):
	arg_2_0.uiContianer = arg_2_0._tf.Find("UI")

	local var_2_0 = arg_2_0.uiContianer.Find("base")

	onButton(arg_2_0, var_2_0.Find("btn_back"), function()
		arg_2_0.emit(BaseUI.ON_BACK), SFX_CANCEL)
	onButton(arg_2_0, var_2_0.Find("btn_back/help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("roll_gametip")
		}), SFX_PANEL)

	arg_2_0.rtFavorLevel = var_2_0.Find("top/favor_level")

	onButton(arg_2_0, arg_2_0.rtFavorLevel, function()
		arg_2_0.emit(Dorm3dSceneMediator.OPEN_LEVEL_LAYER), SFX_PANEL)
	onButton(arg_2_0, var_2_0.Find("bottom/btn_furniture"), function()
		local var_6_0, var_6_1 = arg_2_0.apartment.checkUnlockConfig(getDorm3dGameset("drom3d_furniture_unlock")[2])

		if not var_6_0:
			pg.TipsMgr.GetInstance().ShowTips(var_6_1)

			return

		arg_2_0.emit(Dorm3dSceneMediator.OPEN_FURNITURE_SELECT), SFX_PANEL)
	onButton(arg_2_0, var_2_0.Find("left/btn_photograph"), function()
		arg_2_0.emit(Dorm3dSceneMediator.OPEN_CAMERA_LAYER), SFX_PANEL)
	onButton(arg_2_0, var_2_0.Find("left/btn_collection"), function()
		local var_8_0, var_8_1 = arg_2_0.apartment.checkUnlockConfig(getDorm3dGameset("drom3d_recall_unlock")[2])

		if not var_8_0:
			pg.TipsMgr.GetInstance().ShowTips(var_8_1)

			return

		arg_2_0.emit(Dorm3dSceneMediator.OPEN_COLLECTION_LAYER), SFX_PANEL)

	local var_2_1 = arg_2_0.uiContianer.Find("touch")

	onButton(arg_2_0, var_2_1.Find("btn_back"), function()
		arg_2_0.ExitTouchMode(), SFX_CANCEL)
	onButton(arg_2_0, var_2_1.Find("btn_back/help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("roll_gametip")
		}), SFX_PANEL)

	arg_2_0.rtFavorUp = arg_2_0._tf.Find("Toast/favor_up")

	setActive(arg_2_0.rtFavorUp, False)

	arg_2_0.rtFavorUpDaily = arg_2_0._tf.Find("Toast/favor_up_daily")

	setActive(arg_2_0.rtFavorUpDaily, False)

	for iter_2_0, iter_2_1 in ipairs({
		arg_2_0.rtFavorUp,
		arg_2_0.rtFavorUpDaily
	}):
		iter_2_1.GetComponent("DftAniEvent").SetEndEvent(function(arg_11_0)
			setActive(iter_2_1, False))

	arg_2_0.rtLevelUpWindow = arg_2_0._tf.Find("LevelUpWindow")

	setActive(arg_2_0.rtLevelUpWindow, False)
	onButton(arg_2_0, arg_2_0.rtLevelUpWindow.Find("bg"), function()
		setActive(arg_2_0.rtLevelUpWindow, False)
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_2_0.rtLevelUpWindow, arg_2_0._tf)
		existCall(arg_2_0.levelUpCallback), SFX_PANEL)

	local var_2_2 = arg_2_0.uiContianer.Find("watch")

	onButton(arg_2_0, var_2_2.Find("btn_back"), function()
		arg_2_0.emit(Dorm3dScene.EXIT_WATCH_MODE))
	onButton(arg_2_0, var_2_2.Find("btn_back/help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("roll_gametip")
		}), SFX_PANEL)

	local var_2_3 = arg_2_0.uiContianer.Find("watch/Role")

	onButton(arg_2_0, var_2_3.Find("Talk"), function()
		local var_15_0 = arg_2_0.GetFurnitureTalk(arg_2_0.GetZoneName())

		if not var_15_0:
			pg.TipsMgr.GetInstance().ShowTips("without topic")

			return

		arg_2_0.DoTalk(var_15_0, True, function()
			arg_2_0.emit(Dorm3dSceneMediator.TRIGGER_FAVOR, arg_2_0.apartment.configId, Apartment.TRIGGER_TALK)), SFX_CONFIRM)
	setText(var_2_3.Find("Talk/Text"), i18n("dorm3d_talk"))
	onButton(arg_2_0, var_2_3.Find("Touch"), function()
		local var_17_0, var_17_1 = arg_2_0.apartment.checkUnlockConfig(getDorm3dGameset("drom3d_touch_dialogue")[2])

		if not var_17_0:
			pg.TipsMgr.GetInstance().ShowTips(var_17_1)

			return

		arg_2_0.EnterTouchMode(), SFX_CONFIRM)
	setText(var_2_3.Find("Touch/Text"), i18n("dorm3d_touch"))
	onButton(arg_2_0, var_2_3.Find("Gift"), function()
		local var_18_0, var_18_1 = arg_2_0.apartment.checkUnlockConfig(getDorm3dGameset("drom3d_gift_dialogue")[2])

		if not var_18_0:
			pg.TipsMgr.GetInstance().ShowTips(var_18_1)

			return

		arg_2_0.emit(Dorm3dSceneMediator.OPEN_GIFT_LAYER), SFX_CONFIRM)
	setText(var_2_3.Find("Gift/Text"), i18n("dorm3d_gift"))

	arg_2_0.rtFloatPage = arg_2_0._tf.Find("FloatPage")
	arg_2_0.tplFloat = arg_2_0.rtFloatPage.Find("tpl")

	setActive(arg_2_0.tplFloat, False)

	arg_2_0._joystick = arg_2_0._tf.Find("Stick")

	setActive(arg_2_0._joystick, True)

	arg_2_0._stickCom = arg_2_0._joystick.GetComponent(typeof(SlideController))

	arg_2_0._stickCom.SetStickFunc(function(arg_19_0)
		arg_2_0.emit(Dorm3dScene.ON_STICK_MOVE, arg_19_0))
	arg_2_0.SetUI("base")

	arg_2_0.cvLoader = ShipProfileCVLoader.New()

def var_0_0.initNodeCanvas(arg_20_0, arg_20_1):
	arg_20_0.rtMainAI = arg_20_1

	local var_20_0 = pg.NodeCanvasMgr.GetInstance()

	var_20_0.SetOwner(arg_20_0.rtMainAI)

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.contextData.blackboard or {
		inTalking = False,
		inWatchMode = False
	}):
		arg_20_0.SetBlackboardValue(iter_20_0, iter_20_1)

	var_20_0.RegisterFunc("ClickCharacter", function(arg_21_0)
		if arg_20_0.uiState != "base":
			return

		if not arg_20_0.GetBlackboardValue("inWatchMode"):
			arg_20_0.OutOfLazy(function()
				arg_20_0.emit(Dorm3dScene.ENTER_WATCH_MODE)))
	var_20_0.RegisterFunc("MoveFurniture", function(arg_23_0)
		if arg_20_0.uiState != "base":
			return

		arg_20_0.OutOfLazy(function()
			arg_20_0.SetBlackboardValue("inMoving", True)
			arg_20_0.emit(Dorm3dScene.MOVE_PLAYER_TO_FURNITURE, arg_23_0.name, function()
				arg_20_0.SetBlackboardValue("inMoving", False))))
	var_20_0.RegisterFunc("ClickCharacterInWatch", function()
		arg_20_0.OutOfLazy(function()
			arg_20_0.emit(Dorm3dScene.WATCH_MODE_INTERACTIVE)))
	var_20_0.RegisterFunc("ClickContact", function(arg_28_0)
		arg_20_0.TriggerContact(arg_28_0))
	var_20_0.RegisterFunc("ShortWaitAction", function()
		arg_20_0.DoShortWait())
	var_20_0.RegisterFunc("LongWaitAction", function()
		arg_20_0.DoLongWait())

def var_0_0.BindEvent(arg_31_0):
	arg_31_0.bind(Dorm3dScene.ON_TOUCH_CHARACTER, function(arg_32_0, arg_32_1)
		if not arg_31_0.GetBlackboardValue("inTouching"):
			return

		arg_31_0.DoTouch(arg_32_1, 1))
	arg_31_0.bind(Dorm3dScene.ON_ROLEWATCH_CAMERA_MAX, function(arg_33_0, arg_33_1)
		if not arg_31_0.GetBlackboardValue("inTouching"):
			return

		arg_31_0.DoTouch(arg_33_1, 0))

def var_0_0.TreeStart(arg_34_0):
	if arg_34_0.contextData.resumeCallback:
		arg_34_0.contextData.resumeCallback()

		arg_34_0.contextData.resumeCallback = None

	SetCompomentEnabled(arg_34_0.rtMainAI, "BehaviourTreeOwner", True)
	arg_34_0.EnterCheck()

def var_0_0.SetBlackboardValue(arg_35_0, arg_35_1, arg_35_2):
	arg_35_0.contextData.blackboard = arg_35_0.contextData.blackboard or {}
	arg_35_0.contextData.blackboard[arg_35_1] = arg_35_2

	pg.NodeCanvasMgr.GetInstance().SetBlackboradValue(arg_35_1, arg_35_2)

def var_0_0.GetBlackboardValue(arg_36_0, arg_36_1):
	arg_36_0.contextData.blackboard = arg_36_0.contextData.blackboard or {}

	return arg_36_0.contextData.blackboard[arg_36_1]

def var_0_0.SendNodeCanvasEvent(arg_37_0, arg_37_1, arg_37_2):
	pg.NodeCanvasMgr.GetInstance().SendEvent(arg_37_1, arg_37_2)

def var_0_0.EnableJoystick(arg_38_0, arg_38_1):
	setActive(arg_38_0._joystick, arg_38_1)

def var_0_0.SetInFurniture(arg_39_0, arg_39_1):
	arg_39_0.SetBlackboardValue("inFurniture", arg_39_1)

def var_0_0.SetLadyTransform(arg_40_0, arg_40_1):
	arg_40_0.SetBlackboardValue("ladyTransform", arg_40_1)

def var_0_0.SetUI(arg_41_0, arg_41_1):
	if arg_41_0.uiState == arg_41_1:
		return

	arg_41_0.uiState = arg_41_1

	eachChild(arg_41_0.uiContianer, function(arg_42_0)
		setActive(arg_42_0, arg_42_0.name == arg_41_1))

def var_0_0.EnterTouchMode(arg_43_0):
	if arg_43_0.GetBlackboardValue("inTouching"):
		return

	arg_43_0.touchConfig, arg_43_0.touchDic = arg_43_0.apartment.getTouchConfig(arg_43_0.GetZoneName())

	local var_43_0 = {}

	table.insert(var_43_0, function(arg_44_0)
		arg_43_0.SetBlackboardValue("inTouching", True)
		setCanvasGroupAlpha(arg_43_0.uiContianer, 0)
		arg_43_0.emit(Dorm3dScene.SHOW_BLOCK)
		arg_43_0.SetUI("touch")
		arg_44_0())
	table.insert(var_43_0, function(arg_45_0)
		arg_43_0.emit(Dorm3dScene.ENTER_FREELOOK_MODE, arg_45_0, arg_43_0.touchConfig))
	seriesAsync(var_43_0, function()
		arg_43_0.EnableJoystick(True)
		setCanvasGroupAlpha(arg_43_0.uiContianer, 1)
		arg_43_0.emit(Dorm3dScene.HIDE_BLOCK))

def var_0_0.ExitTouchMode(arg_47_0):
	if not arg_47_0.GetBlackboardValue("inTouching"):
		return

	local var_47_0 = {}

	table.insert(var_47_0, function(arg_48_0)
		setCanvasGroupAlpha(arg_47_0.uiContianer, 0)
		arg_47_0.EnableJoystick(False)
		arg_47_0.emit(Dorm3dScene.SHOW_BLOCK)
		arg_48_0())
	table.insert(var_47_0, function(arg_49_0)
		arg_47_0.emit(Dorm3dScene.EXIT_FREELOOK_MODE, arg_49_0, arg_47_0.touchConfig))
	seriesAsync(var_47_0, function()
		arg_47_0.SetBlackboardValue("inTouching", False)
		setCanvasGroupAlpha(arg_47_0.uiContianer, 1)
		arg_47_0.emit(Dorm3dScene.HIDE_BLOCK)
		arg_47_0.SetUI("watch")

		arg_47_0.touchConfig = None
		arg_47_0.touchDic = None)

def var_0_0.DoTouch(arg_51_0, arg_51_1, arg_51_2):
	assert(arg_51_0.touchConfig and arg_51_0.touchDic)
	warning(arg_51_1, arg_51_2, arg_51_0.touchDic[arg_51_2][arg_51_1])

	local var_51_0 = pg.dorm3d_touch_trigger[arg_51_0.touchDic[arg_51_2][arg_51_1]]

	if not var_51_0:
		return

	local var_51_1 = {}

	if var_51_0.talk_id > 0:
		table.insert(var_51_1, function(arg_52_0)
			arg_51_0.DoTalk(var_51_0.talk_id, False, arg_52_0))
	elif var_51_0.action:
		table.insert(var_51_1, function(arg_53_0)
			arg_51_0.emit(Dorm3dScene.PLAY_SINGLE_ACTION, var_51_0.action, arg_53_0))

	seriesAsync(var_51_1, function()
		if var_51_0.favor_trigger_id > 0:
			arg_51_0.emit(Dorm3dSceneMediator.TRIGGER_FAVOR, arg_51_0.apartment.configId, Apartment.TRIGGER_TOUCH)

			local var_54_0 = 202200
			local var_54_1 = pg.ship_skin_words[var_54_0].voice_key
			local var_54_2 = {
				"get_1",
				"touch_1",
				"touch_1_1",
				"touch_1_2",
				"touch_2_2"
			}

			arg_51_0.cvIndex = arg_51_0.cvIndex or 0

			local var_54_3 = var_54_2[arg_51_0.cvIndex + 1]

			arg_51_0.cvIndex = (arg_51_0.cvIndex + 1) % #var_54_2

			local var_54_4 = "event./cv/" .. var_54_1 .. "/" .. var_54_3

			arg_51_0.cvLoader.PlaySound(var_54_4))

def var_0_0.DoTalk(arg_55_0, arg_55_1, arg_55_2, arg_55_3):
	if arg_55_0.GetBlackboardValue("inTalking"):
		return

	local var_55_0 = {}
	local var_55_1

	table.insert(var_55_0, function(arg_56_0)
		arg_55_0.emit(Dorm3dSceneMediator.DO_TALK, arg_55_1, function(arg_57_0)
			var_55_1 = arg_57_0

			arg_56_0()))

	local var_55_2 = pg.dorm3d_dialogue_group[arg_55_1]

	table.insert(var_55_0, function(arg_58_0)
		warning(arg_55_1)

		if var_55_2.type == 101:
			PlayerPrefs.SetInt("dorm3d_enter_count_" .. arg_55_0.apartment.configId, 0)

		arg_55_0.SetBlackboardValue("inTalking", True)
		setCanvasGroupAlpha(arg_55_0.uiContianer, 0)
		arg_55_0.emit(Dorm3dScene.SHOW_BLOCK)
		arg_58_0())

	if var_55_2.trigger_area and var_55_2.trigger_area != "":
		table.insert(var_55_0, function(arg_59_0)
			arg_55_0.emit(Dorm3dScene.MOVE_PLAYER_TO_FURNITURE, var_55_2.trigger_area, arg_59_0))

	if arg_55_2:
		table.insert(var_55_0, function(arg_60_0)
			arg_55_0.emit(Dorm3dScene.ON_DIALOGUE_BEGIN, arg_60_0))

	if var_55_2.standby_action and var_55_2.standby_action != "":
		table.insert(var_55_0, function(arg_61_0)
			arg_55_0.emit(Dorm3dScene.PLAY_SINGLE_ACTION, var_55_2.standby_action, arg_61_0))

	table.insert(var_55_0, function(arg_62_0)
		pg.NewStoryMgr.GetInstance().ForceManualPlay(var_55_2.story, arg_62_0, True))

	if var_55_2.finish_action and var_55_2.finish_action != "":
		table.insert(var_55_0, function(arg_63_0)
			arg_55_0.emit(Dorm3dScene.PLAY_SINGLE_ACTION, var_55_2.finish_action, arg_63_0))

	if arg_55_2:
		table.insert(var_55_0, function(arg_64_0)
			arg_55_0.emit(Dorm3dScene.ON_DIALOGUE_END, arg_64_0))

	table.insert(var_55_0, function(arg_65_0)
		if var_55_1 and #var_55_1 > 0:
			arg_55_0.emit(Dorm3dSceneMediator.OPEN_DROP_LAYER, var_55_1, arg_65_0)
		else
			arg_65_0())
	table.insert(var_55_0, function(arg_66_0)
		setCanvasGroupAlpha(arg_55_0.uiContianer, 1)
		arg_55_0.emit(Dorm3dScene.HIDE_BLOCK)
		arg_55_0.SetBlackboardValue("inTalking", False)
		arg_66_0())
	seriesAsync(var_55_0, arg_55_3)

def var_0_0.DoTalkTouchOption(arg_67_0, arg_67_1, arg_67_2, arg_67_3):
	local var_67_0 = arg_67_0._tf.Find("ExtraScreen/TalkTouchOption")
	local var_67_1 = pg.NewStoryMgr.GetInstance()._tf

	setActive(var_67_0, True)

	if isActive(var_67_1):
		setParent(var_67_0, var_67_1)
	else
		pg.UIMgr.GetInstance().OverlayPanel(var_67_0, {
			weight = LayerWeightConst.SECOND_LAYER,
			groupName = LayerWeightConst.GROUP_DORM3D
		})

	local var_67_2
	local var_67_3 = var_67_0.Find("content")

	UIItemList.StaticAlign(var_67_3, var_67_3.Find("clickTpl"), #arg_67_1.options, function(arg_68_0, arg_68_1, arg_68_2)
		arg_68_1 = arg_68_1 + 1

		if arg_68_0 == UIItemList.EventUpdate:
			local var_68_0 = arg_67_1.options[arg_68_1]

			setAnchoredPosition(arg_68_2, NewPos(unpack(var_68_0.pos)))
			onButton(arg_67_0, arg_68_2, function()
				var_67_2(var_68_0.flag), SFX_CONFIRM)
			setActive(arg_68_2, not table.contains(arg_67_2, var_68_0.flag)))

	function var_67_2(arg_70_0)
		setActive(var_67_0, False)

		if isActive(var_67_1):
			setParent(var_67_0, arg_67_0._tf)
		else
			pg.UIMgr.GetInstance().UnOverlayPanel(var_67_0, arg_67_0._tf)

		arg_67_3(arg_70_0)

def var_0_0.DoTimelineOption(arg_71_0, arg_71_1, arg_71_2):
	local var_71_0 = arg_71_0._tf.Find("ExtraScreen/TimelineOption")
	local var_71_1 = pg.NewStoryMgr.GetInstance()._tf

	setActive(var_71_0, True)

	if isActive(var_71_1):
		setParent(var_71_0, var_71_1)
	else
		pg.UIMgr.GetInstance().OverlayPanel(var_71_0, {
			weight = LayerWeightConst.SECOND_LAYER,
			groupName = LayerWeightConst.GROUP_DORM3D
		})

	local var_71_2
	local var_71_3 = var_71_0.Find("content")

	UIItemList.StaticAlign(var_71_3, var_71_3.Find("clickTpl"), #arg_71_1, function(arg_72_0, arg_72_1, arg_72_2)
		arg_72_1 = arg_72_1 + 1

		if arg_72_0 == UIItemList.EventUpdate:
			local var_72_0 = arg_71_1[arg_72_1]

			setText(arg_72_2.Find("Text"), var_72_0.content)
			onButton(arg_71_0, arg_72_2, function()
				var_71_2(arg_72_1), SFX_CONFIRM))

	function var_71_2(arg_74_0)
		setActive(var_71_0, False)

		if isActive(var_71_1):
			setParent(var_71_0, arg_71_0._tf)
		else
			pg.UIMgr.GetInstance().UnOverlayPanel(var_71_0, arg_71_0._tf)

		arg_71_2(arg_74_0)

def var_0_0.DoTimelineTouch(arg_75_0, arg_75_1, arg_75_2):
	local var_75_0 = arg_75_0._tf.Find("ExtraScreen/TimelineTouch")
	local var_75_1 = pg.NewStoryMgr.GetInstance()._tf

	setActive(var_75_0, True)

	if isActive(var_75_1):
		setParent(var_75_0, var_75_1)
	else
		pg.UIMgr.GetInstance().OverlayPanel(var_75_0, {
			weight = LayerWeightConst.SECOND_LAYER,
			groupName = LayerWeightConst.GROUP_DORM3D
		})

	local var_75_2
	local var_75_3 = var_75_0.Find("content")

	UIItemList.StaticAlign(var_75_3, var_75_3.Find("clickTpl"), #arg_75_1, function(arg_76_0, arg_76_1, arg_76_2)
		arg_76_1 = arg_76_1 + 1

		if arg_76_0 == UIItemList.EventUpdate:
			local var_76_0 = arg_75_1[arg_76_1]

			setAnchoredPosition(arg_76_2, NewPos(unpack(var_76_0.pos)))
			onButton(arg_75_0, arg_76_2, function()
				var_75_2(arg_76_1), SFX_CONFIRM))

	function var_75_2(arg_78_0)
		setActive(var_75_0, False)

		if isActive(var_75_1):
			setParent(var_75_0, arg_75_0._tf)
		else
			pg.UIMgr.GetInstance().UnOverlayPanel(var_75_0, arg_75_0._tf)

		arg_75_2(arg_78_0)

def var_0_0.DoShortWait(arg_79_0):
	local var_79_0 = arg_79_0.apartment.getZone(arg_79_0.GetZoneName()).getConfig("special_action")
	local var_79_1 = var_79_0 != "" and var_79_0[math.random(#var_79_0)] or None

	if not var_79_1:
		return

	arg_79_0.emit(Dorm3dScene.PLAY_SINGLE_ACTION, var_79_1)

def var_0_0.DoLongWait(arg_80_0):
	local var_80_0 = arg_80_0.apartment.getZone(arg_80_0.GetZoneName())

	if arg_80_0.GetBlackboardValue("inWatchMode"):
		local var_80_1 = var_80_0.getConfig("special_talk")
		local var_80_2 = var_80_1 != "" and var_80_1[math.random(#var_80_1)] or None

		if not var_80_2:
			return

		arg_80_0.DoTalk(var_80_2)
	else
		assert(not arg_80_0.GetBlackboardValue("inLazy"))

		local var_80_3 = var_80_0.getConfig("lazy_action")

		if var_80_3 == "":
			return

		arg_80_0.SetBlackboardValue("inLazy", True)
		arg_80_0.emit(Dorm3dScene.PLAY_SINGLE_ACTION, var_80_3[1])

def var_0_0.OutOfLazy(arg_81_0, arg_81_1):
	local var_81_0 = {}

	if arg_81_0.GetBlackboardValue("inLazy"):
		local var_81_1 = arg_81_0.apartment.getZone(arg_81_0.GetZoneName())

		table.insert(var_81_0, function(arg_82_0)
			arg_81_0.emit(Dorm3dScene.SHOW_BLOCK)
			arg_81_0.emit(Dorm3dScene.PLAY_SINGLE_ACTION, var_81_1.getConfig("lazy_action")[2], function()
				arg_81_0.SetBlackboardValue("inLazy", False)
				arg_81_0.emit(Dorm3dScene.HIDE_BLOCK)
				arg_82_0()))

	arg_81_0.contextData.enterZone = None

	seriesAsync(var_81_0, arg_81_1)

def var_0_0.TriggerContact(arg_84_0, arg_84_1):
	arg_84_0.emit(Dorm3dSceneMediator.COLLECTION_ITEM, arg_84_0.apartment.configId, arg_84_0.contactDic[arg_84_1])

def var_0_0.UpdateContactState(arg_85_0):
	local var_85_0 = arg_85_0.apartment.getTriggerableCollectItems()

	arg_85_0.contactDic = {}

	for iter_85_0, iter_85_1 in ipairs(var_85_0):
		local var_85_1 = pg.dorm3d_collection_template[iter_85_1]

		arg_85_0.contactDic[var_85_1.model] = iter_85_1

	arg_85_0.emit(Dorm3dScene.ON_UPDATE_CONTACT_STSTE, arg_85_0.contactDic)

	if not arg_85_0.floatTimer:
		arg_85_0.floatTimer = Timer.New(function()
			arg_85_0.UpdateContactPosition(), 1 / (Application.targetFrameRate or 60), -1)

		arg_85_0.floatTimer.Start()

	if #var_85_0 > 0:
		arg_85_0.floatTimer.Resume()
	else
		arg_85_0.floatTimer.Pause()

	arg_85_0.UpdateContactPosition()

def var_0_0.UpdateContactPosition(arg_87_0):
	arg_87_0.emit(Dorm3dScene.ON_UPDATE_CONTACT_POSITION, arg_87_0.contactDic)

def var_0_0.UpdateFavorDisplay(arg_88_0):
	setText(arg_88_0.rtFavorLevel.Find("rank/Text"), arg_88_0.apartment.level)

	local var_88_0 = arg_88_0.apartment.favor
	local var_88_1 = arg_88_0.apartment.getNextExp()

	setText(arg_88_0.rtFavorLevel.Find("Text"), string.format("<color=#ff6698>%d</color>/%d", var_88_0, var_88_1))

def var_0_0.CheckFavorTrigger(arg_89_0):
	if arg_89_0.uiState != "base":
		return

	local var_89_0 = {}
	local var_89_1 = getProxy(CollectionProxy).getShipGroup(arg_89_0.apartment.configId)

	table.insert(var_89_0, function(arg_90_0)
		if arg_89_0.apartment.triggerCountDic[Apartment.TRIGGER_OWNER] == 0 and var_89_1:
			arg_89_0.emit(Dorm3dSceneMediator.TRIGGER_FAVOR, arg_89_0.apartment.configId, Apartment.TRIGGER_OWNER)
		else
			arg_90_0())
	table.insert(var_89_0, function(arg_91_0)
		if arg_89_0.apartment.triggerCountDic[Apartment.TRIGGER_PROPOSE] == 0 and var_89_1 and var_89_1.married > 0:
			arg_89_0.emit(Dorm3dSceneMediator.TRIGGER_FAVOR, arg_89_0.apartment.configId, Apartment.TRIGGER_PROPOSE)
		else
			arg_91_0())
	seriesAsync(var_89_0, function()
		arg_89_0.CheckLevelUp())

def var_0_0.CheckLevelUp(arg_93_0):
	if arg_93_0.apartment.favor >= arg_93_0.apartment.getNextExp():
		arg_93_0.emit(Dorm3dSceneMediator.FAVOR_LEVEL_UP, arg_93_0.apartment.configId)

def var_0_0.PopFavorTrigger(arg_94_0, arg_94_1, arg_94_2, arg_94_3):
	if pg.dorm3d_favor_trigger[arg_94_1].is_repeat > 0:
		local var_94_0 = arg_94_3.daily - arg_94_2
		local var_94_1 = arg_94_3.daily
		local var_94_2 = getDorm3dGameset("daily_exp_max")[1]

		setText(arg_94_0.rtFavorUpDaily.Find("info/Text"), i18n("xxx"))
		setText(arg_94_0.rtFavorUpDaily.Find("info/count"), string.format("<color=#ffffff>%d</color>/%d", var_94_1, var_94_2))
		setSlider(arg_94_0.rtFavorUpDaily.Find("slider/back"), 0, var_94_2, var_94_1)
		setSlider(arg_94_0.rtFavorUpDaily.Find("slider/front"), 0, var_94_2, var_94_0)
		setActive(arg_94_0.rtFavorUpDaily, True)
	else
		setText(arg_94_0.rtFavorUp.Find("Text"), string.format("once plus %d", arg_94_2))
		setActive(arg_94_0.rtFavorUp, True)

def var_0_0.PopFavorLevelUp(arg_95_0, arg_95_1, arg_95_2):
	eachChild(arg_95_0.rtLevelUpWindow.Find("panel/mark/level"), function(arg_96_0)
		setActive(arg_96_0, arg_96_0.name == tostring(arg_95_1.level)))
	setText(arg_95_0.rtLevelUpWindow.Find("panel/info/Text"), arg_95_1.getFavorConfig("levelup_trigger_mention"))
	setActive(arg_95_0.rtLevelUpWindow, True)
	pg.UIMgr.GetInstance().OverlayPanel(arg_95_0.rtLevelUpWindow, {
		weight = LayerWeightConst.SECOND_LAYER,
		groupName = LayerWeightConst.GROUP_DORM3D
	})

	function arg_95_0.levelUpCallback()
		arg_95_0.levelUpCallback = None

		existCall(arg_95_2)

def var_0_0.TalkingEventHandle(arg_98_0, arg_98_1):
	local var_98_0 = {}
	local var_98_1 = {}
	local var_98_2 = arg_98_1.data

	if var_98_2.op_list:
		for iter_98_0, iter_98_1 in ipairs(var_98_2.op_list):
			table.insert(var_98_0, function(arg_99_0)
				if iter_98_1.skip:
					arg_99_0()

					arg_99_0 = None

				switch(iter_98_1.type, {
					def action:()
						arg_98_0.emit(Dorm3dScene.PLAY_SINGLE_ACTION, iter_98_1.name, arg_99_0),
					def timeline:()
						arg_98_0.emit(Dorm3dScene.PLAY_TIMELINE, iter_98_1, function(arg_102_0)
							var_98_1.optionIndex = arg_102_0.optionIndex

							existCall(arg_99_0)),
					def clickOption:()
						arg_98_0.DoTalkTouchOption(iter_98_1, arg_98_1.flags, function(arg_104_0)
							var_98_1.optionIndex = arg_104_0

							existCall(arg_99_0)),
					def wait:()
						arg_98_0.LTs = arg_98_0.LTs or {}

						table.insert(arg_98_0.LTs, LeanTween.delayedCall(iter_98_1.time, System.Action(function()
							existCall(arg_99_0))).uniqueId)
				}, function()
					assert(False, "op type error.", iter_98_1.type)))

	seriesAsync(var_98_0, function()
		if arg_98_1.callbackData:
			arg_98_0.emit(Dorm3dSceneMediator.TALKING_EVENT_FINISH, arg_98_1.callbackData.name, var_98_1))

def var_0_0.GetFurnitureTalk(arg_109_0, arg_109_1):
	local var_109_0 = arg_109_0.apartment.getFurnitureTalking(arg_109_1)

	return var_109_0[math.random(#var_109_0)]

def var_0_0.EnterCheck(arg_110_0):
	local var_110_0 = {}

	if arg_110_0.contextData.hasEnterCheck:
		arg_110_0.CheckFavorTrigger()
	else
		arg_110_0.contextData.hasEnterCheck = True

		if arg_110_0.contextData.enterType == 1:
			local var_110_1 = arg_110_0.GetEnterTalk()

			if var_110_1:
				table.insert(var_110_0, function(arg_111_0)
					arg_110_0.DoTalk(var_110_1, False, arg_111_0))

			seriesAsync(var_110_0, function()
				arg_110_0.CheckFavorTrigger())
		elif arg_110_0.contextData.enterType == 2:
			local var_110_2 = arg_110_0.apartment.getZone(arg_110_0.contextData.enterZone).getConfig("lazy_action")

			if var_110_2 == "":
				return

			arg_110_0.SetBlackboardValue("inLazy", True)
			arg_110_0.emit(Dorm3dScene.SWITCH_ACTION, var_110_2[3])
		else
			assert(False)

def var_0_0.GetEnterTalk(arg_113_0):
	local var_113_0 = {}

	for iter_113_0, iter_113_1 in ipairs(arg_113_0.apartment.getEnterTalking()):
		local var_113_1 = pg.dorm3d_dialogue_group[iter_113_1]

		if var_113_1.type == 104 and not pg.NewStoryMgr.GetInstance().IsPlayed(var_113_1.story):
			return iter_113_1
		elif var_113_1.type == 105 and PlayerPrefs.GetString("DORM3D_DAILY_ENTER", "") != pg.TimeMgr.GetInstance().CurrentSTimeDesc("%Y/%m/%d"):
			PlayerPrefs.SetString("DORM3D_DAILY_ENTER", pg.TimeMgr.GetInstance().CurrentSTimeDesc("%Y/%m/%d"))

			return iter_113_1
		elif var_113_1.type == 1053 and not pg.NewStoryMgr.GetInstance().IsPlayed(var_113_1.story):
			local var_113_2 = getProxy(CollectionProxy).getShipGroup(arg_113_0.apartment.configId)

			if var_113_2 and var_113_2.married > 0:
				return iter_113_1
		elif var_113_1.type == 1052 and underscore.any(var_113_1.trigger_config, function(arg_114_0)
			return getProxy(ActivityProxy).IsActivityNotEnd(arg_114_0)):
			table.insert(var_113_0, iter_113_1)
		elif var_113_1.type == 1051 and PlayerPrefs.GetInt("dorm3d_enter_count_" .. arg_113_0.apartment.configId, 0) > var_113_1.trigger_config[2]:
			table.insert(var_113_0, iter_113_1)

	return var_113_0[math.random(#var_113_0)]

def var_0_0.EnterWatchMode(arg_115_0):
	arg_115_0.SetBlackboardValue("inWatchMode", True)
	arg_115_0.SetUI("watch")

def var_0_0.ExitWatchMode(arg_116_0):
	arg_116_0.SetBlackboardValue("inWatchMode", False)
	arg_116_0.SetUI("base")
	arg_116_0.CheckFavorTrigger()

def var_0_0.GetZoneName(arg_117_0):
	local var_117_0 = arg_117_0.GetBlackboardValue("inFurniture")

	return arg_117_0.contextData.enterZone or var_117_0 and var_117_0.name or "Default"

def var_0_0.TempHideUI(arg_118_0, arg_118_1):
	local var_118_0 = defaultValue(arg_118_0.hideCount, 0)

	arg_118_0.hideCount = var_118_0 + (arg_118_1 and 1 or -1)

	assert(arg_118_0.hideCount >= 0)

	if arg_118_0.hideCount * var_118_0 > 0:
		return

	local var_118_1 = arg_118_0.hideCount == 0 and arg_118_0.uiState or None

	eachChild(arg_118_0.uiContianer, function(arg_119_0)
		setActive(arg_119_0, arg_119_0.name == var_118_1))
	setActive(arg_118_0.rtFloatPage, arg_118_0.hideCount == 0)

def var_0_0.onBackPressed(arg_120_0):
	if isActive(arg_120_0.rtLevelUpWindow):
		triggerButton(arg_120_0.rtLevelUpWindow.Find("bg"))
	elif arg_120_0.uiState != "base":
		triggerButton(arg_120_0.uiContianer.Find(arg_120_0.uiState .. "/btn_back"))
	else
		return False

	return True

def var_0_0.OnDestroy(arg_121_0):
	arg_121_0.cvLoader.Dispose()

	if arg_121_0.floatTimer:
		arg_121_0.floatTimer.Stop()

	if arg_121_0.LTs:
		underscore.map(arg_121_0.LTs, function(arg_122_0)
			LeanTween.cancel(arg_122_0))

		arg_121_0.LTs = None

	arg_121_0.SetBlackboardValue("inLockLayer", None)

	arg_121_0.contextData.charFurnitureName = None

	SetCompomentEnabled(arg_121_0.rtMainAI, "BehaviourTreeOwner", False)
	pg.NodeCanvasMgr.GetInstance().Clear()

return var_0_0
