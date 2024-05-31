local var_0_0 = class("StoryPlayer", import("..animation.StoryAnimtion"))
local var_0_1 = 0
local var_0_2 = 1
local var_0_3 = 2
local var_0_4 = 3
local var_0_5 = 4
local var_0_6 = 5
local var_0_7 = 6
local var_0_8 = 7
local var_0_9 = 0
local var_0_10 = 1
local var_0_11 = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0)
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.animationPlayer = arg_1_0._tf.GetComponent(typeof(Animation))
	arg_1_0.front = arg_1_0.findTF("front")
	arg_1_0.actorTr = arg_1_0._tf.Find("actor")
	arg_1_0.frontTr = arg_1_0._tf.Find("front")
	arg_1_0.backPanel = arg_1_0.findTF("back")
	arg_1_0.goCG = GetOrAddComponent(arg_1_0._tf, typeof(CanvasGroup))
	arg_1_0.asidePanel = arg_1_0.findTF("front/aside_panel")
	arg_1_0.bgGlitch = arg_1_0.findTF("back/bg_glitch")
	arg_1_0.oldPhoto = arg_1_0.findTF("front/oldphoto").GetComponent(typeof(Image))
	arg_1_0.bgPanel = arg_1_0.findTF("back/bg")
	arg_1_0.bgPanelCg = arg_1_0.bgPanel.GetComponent(typeof(CanvasGroup))
	arg_1_0.bgImage = arg_1_0.findTF("image", arg_1_0.bgPanel).GetComponent(typeof(Image))
	arg_1_0.mainImg = arg_1_0._tf.GetComponent(typeof(Image))
	arg_1_0.castPanel = arg_1_0.findTF("front/cast_panel")
	arg_1_0.centerPanel = arg_1_0._tf.Find("center")
	arg_1_0.actorPanel = arg_1_0.findTF("actor")
	arg_1_0.dialoguePanel = arg_1_0.findTF("front/dialogue")
	arg_1_0.effectPanel = arg_1_0.findTF("front/effect")
	arg_1_0.movePanel = arg_1_0.findTF("front/move_layer")
	arg_1_0.curtain = arg_1_0.findTF("back/curtain")
	arg_1_0.curtainCg = arg_1_0.curtain.GetComponent(typeof(CanvasGroup))
	arg_1_0.flash = arg_1_0.findTF("front/flash")
	arg_1_0.flashImg = arg_1_0.flash.GetComponent(typeof(Image))
	arg_1_0.flashCg = arg_1_0.flash.GetComponent(typeof(CanvasGroup))
	arg_1_0.curtainF = arg_1_0.findTF("back/curtain_front")
	arg_1_0.curtainFCg = arg_1_0.curtainF.GetComponent(typeof(CanvasGroup))
	arg_1_0.locationTr = arg_1_0.findTF("front/location")
	arg_1_0.locationTxt = arg_1_0.findTF("front/location/Text").GetComponent(typeof(Text))
	arg_1_0.locationTrPos = arg_1_0.locationTr.localPosition
	arg_1_0.locationAnim = arg_1_0.locationTr.GetComponent(typeof(Animation))
	arg_1_0.locationAniEvent = arg_1_0.locationTr.GetComponent(typeof(DftAniEvent))
	arg_1_0.iconImage = arg_1_0.findTF("front/icon").GetComponent(typeof(Image))
	arg_1_0.dialogueWin = None
	arg_1_0.bgs = {}
	arg_1_0.branchCodeList = {}
	arg_1_0.stop = False
	arg_1_0.pause = False

def var_0_0.StoryStart(arg_2_0, arg_2_1):
	arg_2_0.branchCodeList = {}

	eachChild(arg_2_0.dialoguePanel, function(arg_3_0)
		setActive(arg_3_0, False))

	arg_2_0.dialogueWin = arg_2_0.dialoguePanel.Find(arg_2_1.GetDialogueStyleName())

	setActive(arg_2_0.dialogueWin, True)

	arg_2_0.optionLUIlist = UIItemList.New(arg_2_0.dialogueWin.Find("options_panel/options_l"), arg_2_0.dialogueWin.Find("options_panel/options_l/option_tpl"))
	arg_2_0.optionCUIlist = UIItemList.New(arg_2_0.dialogueWin.Find("options_panel/options_c"), arg_2_0.dialogueWin.Find("options_panel/options_c/option_tpl"))
	arg_2_0.optionsCg = arg_2_0.dialogueWin.Find("options_panel").GetComponent(typeof(CanvasGroup))

	arg_2_0.OnStart(arg_2_1)

def var_0_0.GetOptionContainer(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.GetOptionCnt()

	if arg_4_0.script.IsDialogueStyle2():
		setActive(arg_4_0.optionLUIlist.container, True)
		setActive(arg_4_0.optionCUIlist.container, False)

		return arg_4_0.optionLUIlist, True

	if var_4_0 <= 3:
		setActive(arg_4_0.optionLUIlist.container, False)
		setActive(arg_4_0.optionCUIlist.container, True)

		return arg_4_0.optionCUIlist, False
	else
		setActive(arg_4_0.optionLUIlist.container, True)
		setActive(arg_4_0.optionCUIlist.container, False)

		return arg_4_0.optionLUIlist, True

def var_0_0.Pause(arg_5_0):
	arg_5_0.pause = True

	arg_5_0.PauseAllAnimation()
	pg.ViewUtils.SetLayer(arg_5_0.effectPanel, Layer.UIHidden)

def var_0_0.Resume(arg_6_0):
	arg_6_0.pause = False

	arg_6_0.ResumeAllAnimation()
	pg.ViewUtils.SetLayer(arg_6_0.effectPanel, Layer.UI)

def var_0_0.Stop(arg_7_0):
	arg_7_0.stop = True

	arg_7_0.NextOneImmediately()

def var_0_0.Play(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	if not arg_8_1:
		arg_8_3()

		return

	if arg_8_1.GetNextScriptName() or arg_8_0.stop:
		arg_8_3()

		return

	local var_8_0 = arg_8_1.GetStepByIndex(arg_8_2)

	if not var_8_0:
		arg_8_3()

		return

	pg.NewStoryMgr.GetInstance().AddRecord(var_8_0)

	if var_8_0.ShouldJumpToNextScript():
		arg_8_1.SetNextScriptName(var_8_0.GetNextScriptName())
		arg_8_3()

		return

	local var_8_1 = arg_8_1.ShouldSkipAll()

	if var_8_1:
		arg_8_0.ClearEffects()

	local var_8_2 = False

	if var_8_1 and var_8_0.IsImport() and not pg.NewStoryMgr.GetInstance().IsReView():
		var_8_2 = True
	elif var_8_1:
		arg_8_3()

		return

	arg_8_0.script = arg_8_1
	arg_8_0.callback = arg_8_3
	arg_8_0.step = var_8_0
	arg_8_0.autoNext = arg_8_1.GetAutoPlayFlag()
	arg_8_0.stage = var_0_1

	local var_8_3 = arg_8_1.GetTriggerDelayTime()

	if arg_8_0.autoNext and var_8_0.IsImport() and not var_8_0.optionSelCode:
		arg_8_0.autoNext = None

	arg_8_0.SetTimeScale(1 - arg_8_1.GetPlaySpeed() * 0.1)

	local var_8_4 = arg_8_1.GetPrevStep(arg_8_2)

	seriesAsync({
		function(arg_9_0)
			if not arg_8_0.NextStage(var_0_2):
				return

			parallelAsync({
				function(arg_10_0)
					arg_8_0.Reset(var_8_0, var_8_4, arg_10_0)
					arg_8_0.UpdateBg(var_8_0)
					arg_8_0.PlayBgm(var_8_0),
				function(arg_11_0)
					arg_8_0.LoadEffects(var_8_0, arg_11_0),
				function(arg_12_0)
					arg_8_0.ApplyEffects(var_8_0, arg_12_0),
				function(arg_13_0)
					arg_8_0.flashin(var_8_0, arg_13_0)
			}, arg_9_0),
		function(arg_14_0)
			if var_8_2:
				arg_8_1.StopSkip()

			var_8_2 = False

			arg_14_0(),
		function(arg_15_0)
			if not arg_8_0.NextStage(var_0_3):
				return

			parallelAsync({
				function(arg_16_0)
					arg_8_0.OnInit(var_8_0, var_8_4, arg_16_0),
				function(arg_17_0)
					arg_8_0.PlaySoundEffect(var_8_0)
					arg_8_0.StartUIAnimations(var_8_0, arg_17_0),
				function(arg_18_0)
					arg_8_0.OnEnter(var_8_0, var_8_4, arg_18_0),
				function(arg_19_0)
					arg_8_0.StartMoveNode(var_8_0, arg_19_0),
				function(arg_20_0)
					arg_8_0.UpdateIcon(var_8_0, arg_20_0),
				function(arg_21_0)
					arg_8_0.SetLocation(var_8_0, arg_21_0),
				function(arg_22_0)
					arg_8_0.DispatcherEvent(var_8_0, arg_22_0)
			}, arg_15_0),
		function(arg_23_0)
			arg_8_0.ClearCheckDispatcher()

			if not arg_8_0.NextStage(var_0_4):
				return

			if not var_8_0.ShouldDelayEvent():
				arg_23_0()

				return

			arg_8_0.DelayCall(var_8_0.GetEventDelayTime(), arg_23_0),
		function(arg_24_0)
			if not arg_8_0.NextStage(var_0_5):
				return

			if arg_8_0.skipOption:
				arg_24_0()

				return

			if var_8_0.SkipEventForOption():
				arg_24_0()

				return

			if arg_8_0.ShouldAutoTrigger():
				arg_8_0.UnscaleDelayCall(var_8_3, arg_24_0)

				return

			arg_8_0.RegisetEvent(arg_24_0)
			arg_8_0.TriggerEventIfAuto(var_8_3),
		function(arg_25_0)
			if not arg_8_0.NextStage(var_0_6):
				return

			if not var_8_0.ExistOption():
				arg_25_0()

				return

			if arg_8_0.skipOption:
				arg_8_0.skipOption = False

				arg_25_0()

				return

			arg_8_0.InitBranches(arg_8_1, var_8_0, function(arg_26_0)
				arg_25_0(), function()
				arg_8_0.TriggerOptionIfAuto(var_8_3, var_8_0)),
		function(arg_28_0)
			if not arg_8_0.NextStage(var_0_7):
				return

			arg_8_0.autoNext = None

			local var_28_0 = arg_8_1.GetNextStep(arg_8_2)

			seriesAsync({
				function(arg_29_0)
					arg_8_0.ClearAnimation()
					arg_8_0.ClearApplyEffect()
					arg_8_0.OnWillExit(var_8_0, var_28_0, arg_29_0),
				function(arg_30_0)
					parallelAsync({
						function(arg_31_0)
							if not var_28_0:
								arg_31_0()

								return

							arg_8_0.Flashout(var_28_0, arg_31_0),
						function(arg_32_0)
							if var_28_0:
								arg_32_0()

								return

							arg_8_0.FadeOutStory(arg_8_0.script, arg_32_0)
					}, arg_30_0)
			}, arg_28_0),
		function(arg_33_0)
			if not arg_8_0.NextStage(var_0_8):
				return

			arg_8_0.OnWillClear(var_8_0)
			arg_8_0.Clear(arg_33_0)
	}, arg_8_3)

def var_0_0.NextStage(arg_34_0, arg_34_1):
	if arg_34_0.stage == arg_34_1 - 1:
		arg_34_0.stage = arg_34_1

		return True

	return False

def var_0_0.ApplyEffects(arg_35_0, arg_35_1, arg_35_2):
	if arg_35_1.ShouldShake():
		arg_35_0.ApplyShakeEffect(arg_35_1)

	arg_35_2()

def var_0_0.ApplyShakeEffect(arg_36_0, arg_36_1):
	if not arg_36_1.ShouldShake():
		return

	arg_36_0.animationPlayer.Play("anim_storyrecordUI_shake_loop")

	local var_36_0 = arg_36_1.GetShakeTime()

	arg_36_0.playingShakeAnim = True

	arg_36_0.DelayCall(var_36_0, function()
		arg_36_0.ClearShakeEffect())

def var_0_0.ClearShakeEffect(arg_38_0):
	if arg_38_0.playingShakeAnim:
		arg_38_0.animationPlayer.Play("anim_storyrecordUI_shake_reset")

		arg_38_0.playingShakeAnim = None

def var_0_0.ClearApplyEffect(arg_39_0):
	arg_39_0.ClearShakeEffect()

def var_0_0.DispatcherEvent(arg_40_0, arg_40_1, arg_40_2):
	if not arg_40_1.ExistDispatcher():
		arg_40_2()

		return

	local var_40_0 = arg_40_1.GetDispatcher()

	pg.NewStoryMgr.GetInstance().ClearStoryEvent()
	pg.m02.sendNotification(var_40_0.name, {
		data = var_40_0.data,
		callbackData = var_40_0.callbackData,
		flags = arg_40_0.branchCodeList[arg_40_1.GetId()] or {}
	})

	if arg_40_1.ShouldHideUI():
		setActive(arg_40_0._tf, False)

	if arg_40_1.IsRecallDispatcher():
		arg_40_0.CheckDispatcher(arg_40_1, arg_40_2)
	else
		arg_40_2()

def var_0_0.CheckDispatcher(arg_41_0, arg_41_1, arg_41_2):
	local var_41_0 = arg_41_1.GetDispatcherRecallName()

	arg_41_0.checkTimer = Timer.New(function()
		if pg.NewStoryMgr.GetInstance().CheckStoryEvent(var_41_0):
			local var_42_0 = pg.NewStoryMgr.GetInstance().GetStoryEventArg(var_41_0)

			if var_42_0 and var_42_0.optionIndex:
				arg_41_0.SetBranchCode(arg_41_0.script, arg_41_1, var_42_0.optionIndex)

				arg_41_0.skipOption = True

			if arg_41_1.ShouldHideUI():
				setActive(arg_41_0._tf, True)

			arg_41_0.ClearCheckDispatcher()
			arg_41_2(), 1, -1)

	arg_41_0.checkTimer.Start()
	arg_41_0.checkTimer.func()

def var_0_0.ClearCheckDispatcher(arg_43_0):
	if arg_43_0.checkTimer:
		arg_43_0.checkTimer.Stop()

		arg_43_0.checkTimer = None

def var_0_0.TriggerEventIfAuto(arg_44_0, arg_44_1):
	if not arg_44_0.ShouldAutoTrigger():
		return

	arg_44_0.UnscaleDelayCall(arg_44_1, function()
		if not arg_44_0.autoNext:
			setButtonEnabled(arg_44_0._go, True)

			return

		triggerButton(arg_44_0._go))

def var_0_0.TriggerOptionIfAuto(arg_46_0, arg_46_1, arg_46_2):
	if not arg_46_0.ShouldAutoTrigger():
		return

	if not arg_46_2 or not arg_46_2.ExistOption():
		return

	arg_46_0.UnscaleDelayCall(arg_46_1, function()
		if not arg_46_0.autoNext:
			return

		local var_47_0 = arg_46_2.GetOptionIndexByAutoSel()

		if var_47_0 != None:
			local var_47_1 = arg_46_0.GetOptionContainer(arg_46_2).container.GetChild(var_47_0 - 1)

			triggerButton(var_47_1))

def var_0_0.ShouldAutoTrigger(arg_48_0):
	if arg_48_0.pause or arg_48_0.stop:
		return False

	return arg_48_0.autoNext

def var_0_0.CanSkip(arg_49_0):
	return arg_49_0.step and not arg_49_0.step.IsImport()

def var_0_0.CancelAuto(arg_50_0):
	arg_50_0.autoNext = False

def var_0_0.NextOne(arg_51_0):
	arg_51_0.timeScale = 0.0001

	if arg_51_0.stage == var_0_1:
		arg_51_0.autoNext = True
	elif arg_51_0.stage == var_0_5:
		arg_51_0.autoNext = True

		arg_51_0.TriggerEventIfAuto(0)
	elif arg_51_0.stage == var_0_6:
		arg_51_0.TriggerOptionIfAuto(0, arg_51_0.step)

def var_0_0.NextOneImmediately(arg_52_0):
	local var_52_0 = arg_52_0.callback

	if var_52_0:
		arg_52_0.ClearAnimation()
		arg_52_0.Clear()
		var_52_0()

def var_0_0.SetLocation(arg_53_0, arg_53_1, arg_53_2):
	if not arg_53_1.ExistLocation():
		arg_53_0.locationAniEvent.SetEndEvent(None)
		arg_53_2()

		return

	setActive(arg_53_0.locationTr, True)

	local var_53_0 = arg_53_1.GetLocation()

	arg_53_0.locationTxt.text = var_53_0.text

	local function var_53_1()
		arg_53_0.DelayCall(var_53_0.time, function()
			arg_53_0.locationAnim.Play("anim_newstoryUI_iocation_out")

			arg_53_0.locationStatus = var_0_11)

	arg_53_0.locationAniEvent.SetEndEvent(function()
		if arg_53_0.locationStatus == var_0_10:
			var_53_1()
			arg_53_2()
		elif arg_53_0.locationStatus == var_0_11:
			setActive(arg_53_0.locationTr, False)

			arg_53_0.locationStatus = var_0_9)
	arg_53_0.locationAnim.Play("anim_newstoryUI_iocation_in")

	arg_53_0.locationStatus = var_0_10

def var_0_0.UpdateIcon(arg_57_0, arg_57_1, arg_57_2):
	if not arg_57_1.ExistIcon():
		setActive(arg_57_0.iconImage.gameObject, False)
		arg_57_2()

		return

	local var_57_0 = arg_57_1.GetIconData()

	arg_57_0.iconImage.sprite = LoadSprite(var_57_0.image)

	arg_57_0.iconImage.SetNativeSize()

	local var_57_1 = arg_57_0.iconImage.gameObject.transform

	if var_57_0.pos:
		var_57_1.localPosition = Vector3(var_57_0.pos[1], var_57_0.pos[2], 0)
	else
		var_57_1.localPosition = Vector3.one

	var_57_1.localScale = Vector3(var_57_0.scale or 1, var_57_0.scale or 1, 1)

	setActive(arg_57_0.iconImage.gameObject, True)
	arg_57_2()

def var_0_0.UpdateOptionTxt(arg_58_0, arg_58_1, arg_58_2, arg_58_3):
	local var_58_0 = arg_58_2.GetComponent(typeof(LayoutElement))
	local var_58_1 = arg_58_2.Find("content")

	if arg_58_1:
		local var_58_2 = GetPerceptualSize(arg_58_3)
		local var_58_3 = arg_58_2.Find("content_max")
		local var_58_4 = var_58_2 >= 17
		local var_58_5 = var_58_4 and var_58_3 or var_58_1

		setActive(var_58_1, not var_58_4)
		setActive(var_58_3, var_58_4)
		setText(var_58_5.Find("Text"), arg_58_3)

		var_58_0.preferredHeight = var_58_5.rect.height
	else
		setText(var_58_1.Find("Text"), arg_58_3)

		var_58_0.preferredHeight = var_58_1.rect.height

def var_0_0.InitBranches(arg_59_0, arg_59_1, arg_59_2, arg_59_3, arg_59_4):
	local var_59_0 = False
	local var_59_1 = arg_59_2.GetOptions()
	local var_59_2, var_59_3 = arg_59_0.GetOptionContainer(arg_59_2)
	local var_59_4 = arg_59_2.GetId()
	local var_59_5 = arg_59_0.branchCodeList[var_59_4] or {}
	local var_59_6 = GetOrAddComponent(var_59_2.container, typeof(CanvasGroup))

	var_59_6.blocksRaycasts = True
	arg_59_0.selectedBranchID = None

	var_59_2.make(function(arg_60_0, arg_60_1, arg_60_2)
		if arg_60_0 == UIItemList.EventUpdate:
			local var_60_0 = arg_60_2
			local var_60_1 = var_59_1[arg_60_1 + 1][1]
			local var_60_2 = var_59_1[arg_60_1 + 1][2]
			local var_60_3 = table.contains(var_59_5, var_60_2)

			onButton(arg_59_0, var_60_0, function()
				if arg_59_0.pause or arg_59_0.stop:
					return

				if not var_59_0:
					return

				arg_59_0.selectedBranchID = arg_60_1

				arg_59_0.SetBranchCode(arg_59_1, arg_59_2, var_60_2)

				local var_61_0 = arg_60_2.GetComponent(typeof(Animation))

				if var_61_0:
					var_59_6.blocksRaycasts = False

					var_61_0.Play("anim_storydialogue_optiontpl_confirm")
					arg_60_2.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
						setActive(arg_59_0.optionsCg.gameObject, False)

						var_59_6.blocksRaycasts = True

						arg_59_3(var_60_1))
				else
					setActive(arg_59_0.optionsCg.gameObject, False)
					arg_59_3(var_60_1)

				arg_59_0.HideBranchesWithoutSelected(arg_59_2), SFX_PANEL)
			setButtonEnabled(var_60_0, not var_60_3)

			GetOrAddComponent(arg_60_2, typeof(CanvasGroup)).alpha = var_60_3 and 0.5 or 1

			arg_59_0.UpdateOptionTxt(var_59_3, var_60_0, var_60_1))
	var_59_2.align(#var_59_1)
	arg_59_0.ShowBranches(arg_59_2, function()
		var_59_0 = True

		if arg_59_4:
			arg_59_4())

def var_0_0.SetBranchCode(arg_64_0, arg_64_1, arg_64_2, arg_64_3):
	arg_64_2.SetBranchCode(arg_64_3)
	arg_64_1.SetBranchCode(arg_64_3)

	local var_64_0 = arg_64_2.GetId()

	if not arg_64_0.branchCodeList[var_64_0]:
		arg_64_0.branchCodeList[var_64_0] = {}

	table.insert(arg_64_0.branchCodeList[var_64_0], arg_64_3)

def var_0_0.ShowBranches(arg_65_0, arg_65_1, arg_65_2):
	setActive(arg_65_0.optionsCg.gameObject, True)

	local var_65_0 = arg_65_0.GetOptionContainer(arg_65_1)

	for iter_65_0 = 0, var_65_0.container.childCount - 1:
		local var_65_1 = var_65_0.container.GetChild(iter_65_0).GetComponent(typeof(Animation))

		if var_65_1:
			var_65_1.Play("anim_storydialogue_optiontpl_in")

	arg_65_2()

def var_0_0.HideBranchesWithoutSelected(arg_66_0, arg_66_1):
	local var_66_0 = arg_66_0.GetOptionContainer(arg_66_1)

	for iter_66_0 = 0, var_66_0.container.childCount - 1:
		if iter_66_0 != arg_66_0.selectedBranchID:
			local var_66_1 = var_66_0.container.GetChild(iter_66_0).GetComponent(typeof(Animation))

			if var_66_1:
				var_66_1.Play("anim_storydialogue_optiontpl_unselected")

def var_0_0.StartMoveNode(arg_67_0, arg_67_1, arg_67_2):
	if not arg_67_1.ExistMovableNode():
		arg_67_2()

		return

	local var_67_0 = arg_67_1.GetMovableNode()
	local var_67_1 = {}
	local var_67_2 = {}

	for iter_67_0, iter_67_1 in pairs(var_67_0):
		table.insert(var_67_1, function(arg_68_0)
			arg_67_0.LoadMovableNode(iter_67_1, function(arg_69_0)
				var_67_2[iter_67_0] = arg_69_0

				arg_68_0()))

	parallelAsync(var_67_1, function()
		arg_67_0.MoveAllNode(arg_67_1, var_67_2, var_67_0)
		arg_67_2())

def var_0_0.MoveAllNode(arg_71_0, arg_71_1, arg_71_2, arg_71_3):
	local var_71_0 = {}

	for iter_71_0, iter_71_1 in pairs(arg_71_2):
		table.insert(var_71_0, function(arg_72_0)
			local var_72_0 = arg_71_3[iter_71_0]
			local var_72_1 = var_72_0.path
			local var_72_2 = var_72_0.time
			local var_72_3 = var_72_0.easeType
			local var_72_4 = var_72_0.delay

			arg_71_0.moveLocalPath(iter_71_1, var_72_1, var_72_2, var_72_4, var_72_3, arg_72_0))

	arg_71_0.moveTargets = arg_71_2

	parallelAsync(var_71_0, function()
		arg_71_0.ClearMoveNodes(arg_71_1))

local function var_0_12(arg_74_0, arg_74_1, arg_74_2, arg_74_3, arg_74_4)
	PoolMgr.GetInstance().GetSpineChar(arg_74_1, True, function(arg_75_0)
		arg_75_0.transform.SetParent(arg_74_0.movePanel)

		local var_75_0 = arg_74_2.scale

		arg_75_0.transform.localScale = Vector3(var_75_0, var_75_0, 0)
		arg_75_0.transform.localPosition = arg_74_3

		arg_75_0.GetComponent(typeof(SpineAnimUI)).SetAction(arg_74_2.action, 0)

		arg_75_0.name = arg_74_1

		if arg_74_4:
			arg_74_4(arg_75_0))

local function var_0_13(arg_76_0, arg_76_1, arg_76_2, arg_76_3)
	local var_76_0 = GameObject.New("movable")

	var_76_0.transform.SetParent(arg_76_0.movePanel)

	var_76_0.transform.localScale = Vector3.zero

	local var_76_1 = GetOrAddComponent(var_76_0, typeof(RectTransform))
	local var_76_2 = GetOrAddComponent(var_76_0, typeof(Image))

	LoadSpriteAsync(arg_76_1, function(arg_77_0)
		var_76_2.sprite = arg_77_0

		var_76_2.SetNativeSize()

		var_76_1.localScale = Vector3.one
		var_76_1.localPosition = arg_76_2

		arg_76_3(var_76_1.gameObject))

def var_0_0.LoadMovableNode(arg_78_0, arg_78_1, arg_78_2):
	local var_78_0 = arg_78_1.path[1] or Vector3.zero

	if arg_78_1.isSpine:
		var_0_12(arg_78_0, arg_78_1.name, arg_78_1.spineData, var_78_0, arg_78_2)
	else
		var_0_13(arg_78_0, arg_78_1.name, var_78_0, arg_78_2)

def var_0_0.ClearMoveNodes(arg_79_0, arg_79_1):
	if not arg_79_1.ExistMovableNode():
		return

	if arg_79_0.movePanel.childCount <= 0:
		return

	for iter_79_0, iter_79_1 in ipairs(arg_79_0.moveTargets or {}):
		if iter_79_1.GetComponent(typeof(SpineAnimUI)) != None:
			PoolMgr.GetInstance().ReturnSpineChar(iter_79_1.name, iter_79_1.gameObject)
		else
			Object.Destroy(iter_79_1.gameObject)

	arg_79_0.moveTargets = {}

def var_0_0.FadeOutStory(arg_80_0, arg_80_1, arg_80_2):
	if not arg_80_1.ShouldFadeout():
		arg_80_2()

		return

	local var_80_0 = arg_80_1.GetFadeoutTime()

	if not arg_80_1.ShouldWaitFadeout():
		arg_80_0.fadeTransform(arg_80_0._go, 1, 0.3, var_80_0, True)
		arg_80_2()
	else
		arg_80_0.fadeTransform(arg_80_0._go, 1, 0.3, var_80_0, True, arg_80_2)

def var_0_0.GetFadeColor(arg_81_0, arg_81_1):
	local var_81_0 = {}
	local var_81_1 = {}
	local var_81_2 = arg_81_1.GetComponentsInChildren(typeof(Image))

	for iter_81_0 = 0, var_81_2.Length - 1:
		local var_81_3 = var_81_2[iter_81_0]
		local var_81_4 = {
			name = "_Color",
			color = Color.white
		}

		if var_81_3.material.shader.name == "UI/GrayScale":
			var_81_4 = {
				name = "_GrayScale",
				color = Color.New(0.21176470588235294, 0.7137254901960784, 0.07058823529411765)
			}
		elif var_81_3.material.shader.name == "UI/Line_Add_Blue":
			var_81_4 = {
				name = "_GrayScale",
				color = Color.New(1, 1, 1, 0.5882352941176471)
			}

		table.insert(var_81_1, var_81_4)

		if var_81_3.material == var_81_3.defaultGraphicMaterial:
			var_81_3.material = Material.Instantiate(var_81_3.defaultGraphicMaterial)

		table.insert(var_81_0, var_81_3.material)

	return var_81_0, var_81_1

def var_0_0._SetFadeColor(arg_82_0, arg_82_1, arg_82_2, arg_82_3):
	for iter_82_0, iter_82_1 in ipairs(arg_82_1):
		if not IsNil(iter_82_1):
			iter_82_1.SetColor(arg_82_2[iter_82_0].name, arg_82_2[iter_82_0].color * Color.New(arg_82_3, arg_82_3, arg_82_3))

def var_0_0.SetFadeColor(arg_83_0, arg_83_1, arg_83_2):
	local var_83_0, var_83_1 = arg_83_0.GetFadeColor(arg_83_1)

	arg_83_0._SetFadeColor(var_83_0, var_83_1, arg_83_2)

def var_0_0._RevertFadeColor(arg_84_0, arg_84_1, arg_84_2):
	arg_84_0._SetFadeColor(arg_84_1, arg_84_2, 1)

def var_0_0.RevertFadeColor(arg_85_0, arg_85_1):
	local var_85_0, var_85_1 = arg_85_0.GetFadeColor(arg_85_1)

	arg_85_0._RevertFadeColor(var_85_0, var_85_1)

def var_0_0.fadeTransform(arg_86_0, arg_86_1, arg_86_2, arg_86_3, arg_86_4, arg_86_5, arg_86_6):
	if arg_86_4 <= 0:
		if arg_86_6:
			arg_86_6()

		return

	local var_86_0, var_86_1 = arg_86_0.GetFadeColor(arg_86_1)

	LeanTween.value(go(arg_86_1), arg_86_2, arg_86_3, arg_86_4).setOnUpdate(System.Action_float(function(arg_87_0)
		arg_86_0._SetFadeColor(var_86_0, var_86_1, arg_87_0))).setOnComplete(System.Action(function()
		if arg_86_5:
			arg_86_0._RevertFadeColor(var_86_0, var_86_1)

		if arg_86_6:
			arg_86_6()))

def var_0_0.setPaintingAlpha(arg_89_0, arg_89_1, arg_89_2):
	local var_89_0 = {}
	local var_89_1 = {}
	local var_89_2 = arg_89_1.GetComponentsInChildren(typeof(Image))

	for iter_89_0 = 0, var_89_2.Length - 1:
		local var_89_3 = var_89_2[iter_89_0]
		local var_89_4 = {
			name = "_Color",
			color = Color.white
		}

		if var_89_3.material.shader.name == "UI/GrayScale":
			var_89_4 = {
				name = "_GrayScale",
				color = Color.New(0.21176470588235294, 0.7137254901960784, 0.07058823529411765)
			}
		elif var_89_3.material.shader.name == "UI/Line_Add_Blue":
			var_89_4 = {
				name = "_GrayScale",
				color = Color.New(1, 1, 1, 0.5882352941176471)
			}

		table.insert(var_89_1, var_89_4)

		if var_89_3.material == var_89_3.defaultGraphicMaterial:
			var_89_3.material = Material.Instantiate(var_89_3.defaultGraphicMaterial)

		table.insert(var_89_0, var_89_3.material)

	for iter_89_1, iter_89_2 in ipairs(var_89_0):
		if not IsNil(iter_89_2):
			iter_89_2.SetColor(var_89_1[iter_89_1].name, var_89_1[iter_89_1].color * Color.New(arg_89_2, arg_89_2, arg_89_2))

def var_0_0.RegisetEvent(arg_90_0, arg_90_1):
	setButtonEnabled(arg_90_0._go, not arg_90_0.autoNext)
	onButton(arg_90_0, arg_90_0._go, function()
		if arg_90_0.pause or arg_90_0.stop:
			return

		removeOnButton(arg_90_0._go)
		arg_90_1(), SFX_PANEL)

def var_0_0.flashEffect(arg_92_0, arg_92_1, arg_92_2, arg_92_3, arg_92_4, arg_92_5, arg_92_6):
	arg_92_0.flashImg.color = arg_92_4 and Color(0, 0, 0) or Color(1, 1, 1)
	arg_92_0.flashCg.alpha = arg_92_1

	setActive(arg_92_0.flash, True)
	arg_92_0.TweenValueForcanvasGroup(arg_92_0.flashCg, arg_92_1, arg_92_2, arg_92_3, arg_92_5, arg_92_6)

def var_0_0.Flashout(arg_93_0, arg_93_1, arg_93_2):
	local var_93_0, var_93_1, var_93_2, var_93_3 = arg_93_1.GetFlashoutData()

	if not var_93_0:
		arg_93_2()

		return

	arg_93_0.flashEffect(var_93_0, var_93_1, var_93_2, var_93_3, 0, arg_93_2)

def var_0_0.flashin(arg_94_0, arg_94_1, arg_94_2):
	local var_94_0, var_94_1, var_94_2, var_94_3, var_94_4 = arg_94_1.GetFlashinData()

	if not var_94_0:
		arg_94_2()

		return

	arg_94_0.flashEffect(var_94_0, var_94_1, var_94_2, var_94_3, var_94_4, arg_94_2)

def var_0_0.UpdateBg(arg_95_0, arg_95_1):
	if arg_95_1.ShouldBgGlitchArt():
		arg_95_0.SetBgGlitchArt(arg_95_1)
	else
		local var_95_0 = arg_95_1.GetBgName()

		if var_95_0:
			setActive(arg_95_0.bgPanel, True)

			arg_95_0.bgPanelCg.alpha = 1

			local var_95_1 = arg_95_0.bgImage

			var_95_1.color = Color.New(1, 1, 1)
			var_95_1.sprite = arg_95_0.GetBg(var_95_0)

		local var_95_2 = arg_95_1.GetBgShadow()

		if var_95_2:
			local var_95_3 = arg_95_0.bgImage

			arg_95_0.TweenValue(var_95_3, var_95_2[1], var_95_2[2], var_95_2[3], 0, function(arg_96_0)
				var_95_3.color = Color.New(arg_96_0, arg_96_0, arg_96_0), None)

		if arg_95_1.IsBlackBg():
			setActive(arg_95_0.curtain, True)

			arg_95_0.curtainCg.alpha = 1

		local var_95_4, var_95_5 = arg_95_1.IsBlackFrontGround()

		if var_95_4:
			arg_95_0.curtainFCg.alpha = var_95_5

		setActive(arg_95_0.curtainF, var_95_4)

	arg_95_0.ApplyOldPhotoEffect(arg_95_1)
	arg_95_0.OnBgUpdate(arg_95_1)

	local var_95_6 = arg_95_1.GetBgColor()

	arg_95_0.curtain.GetComponent(typeof(Image)).color = var_95_6

def var_0_0.ApplyOldPhotoEffect(arg_97_0, arg_97_1):
	local var_97_0 = arg_97_1.OldPhotoEffect()
	local var_97_1 = var_97_0 != None

	setActive(arg_97_0.oldPhoto.gameObject, var_97_1)

	if var_97_1:
		if type(var_97_0) == "table":
			arg_97_0.oldPhoto.color = Color.New(var_97_0[1], var_97_0[2], var_97_0[3], var_97_0[4])
		else
			arg_97_0.oldPhoto.color = Color.New(0.62, 0.58, 0.14, 0.36)

def var_0_0.SetBgGlitchArt(arg_98_0, arg_98_1):
	setActive(arg_98_0.bgPanel, False)
	setActive(arg_98_0.bgGlitch, True)

def var_0_0.GetBg(arg_99_0, arg_99_1):
	if not arg_99_0.bgs[arg_99_1]:
		arg_99_0.bgs[arg_99_1] = LoadSprite("bg/" .. arg_99_1)

	return arg_99_0.bgs[arg_99_1]

def var_0_0.LoadEffects(arg_100_0, arg_100_1, arg_100_2):
	local var_100_0 = arg_100_1.GetEffects()

	if #var_100_0 <= 0:
		arg_100_2()

		return

	local var_100_1 = {}

	for iter_100_0, iter_100_1 in ipairs(var_100_0):
		local var_100_2 = iter_100_1.name
		local var_100_3 = iter_100_1.active
		local var_100_4 = iter_100_1.interlayer
		local var_100_5 = iter_100_1.center
		local var_100_6 = iter_100_1.adapt
		local var_100_7 = arg_100_0.effectPanel.Find(var_100_2) or arg_100_0.centerPanel.Find(var_100_2)

		if var_100_7:
			setActive(var_100_7, var_100_3)
			setParent(var_100_7, var_100_5 and arg_100_0.centerPanel or arg_100_0.effectPanel.transform)

			if var_100_4:
				arg_100_0.UpdateEffectInterLayer(var_100_2, var_100_7)

			if var_100_3 == False:
				arg_100_0.ClearEffectInterlayer(var_100_2)

			if var_100_6:
				arg_100_0.AdaptEffect(var_100_7)
		else
			local var_100_8 = ""

			if checkABExist("ui/" .. var_100_2):
				var_100_8 = "ui"
			elif checkABExist("effect/" .. var_100_2):
				var_100_8 = "effect"

			if var_100_8 and var_100_8 != "":
				table.insert(var_100_1, function(arg_101_0)
					LoadAndInstantiateAsync(var_100_8, var_100_2, function(arg_102_0)
						setParent(arg_102_0, var_100_5 and arg_100_0.centerPanel or arg_100_0.effectPanel.transform)

						arg_102_0.transform.localScale = Vector3.one

						setActive(arg_102_0, var_100_3)

						arg_102_0.name = var_100_2

						if var_100_4:
							arg_100_0.UpdateEffectInterLayer(var_100_2, arg_102_0)

						if var_100_3 == False:
							arg_100_0.ClearEffectInterlayer(var_100_2)

						if var_100_6:
							arg_100_0.AdaptEffect(arg_102_0)

						arg_101_0()))
			else
				originalPrint("not found effect", var_100_2)

	parallelAsync(var_100_1, arg_100_2)

def var_0_0.AdaptEffect(arg_103_0, arg_103_1):
	local var_103_0 = 1.7777777777777777
	local var_103_1 = pg.UIMgr.GetInstance().OverlayMain.parent.sizeDelta
	local var_103_2 = var_103_1.x / var_103_1.y
	local var_103_3 = 1

	if var_103_0 < var_103_2:
		var_103_3 = var_103_2 / var_103_0
	else
		var_103_3 = var_103_0 / var_103_2

	tf(arg_103_1).localScale = Vector3(var_103_3, var_103_3, var_103_3)

def var_0_0.UpdateEffectInterLayer(arg_104_0, arg_104_1, arg_104_2):
	local var_104_0 = arg_104_0._go.GetComponent(typeof(Canvas)).sortingOrder
	local var_104_1 = arg_104_2.GetComponentsInChildren(typeof("UnityEngine.ParticleSystemRenderer"))

	for iter_104_0 = 1, var_104_1.Length - 1:
		local var_104_2 = var_104_1[iter_104_0 - 1]
		local var_104_3 = ReflectionHelp.RefGetProperty(typeof("UnityEngine.ParticleSystemRenderer"), "sortingOrder", var_104_2)

		if var_104_0 < var_104_3:
			var_104_0 = var_104_3

	local var_104_4 = var_104_0 + 1
	local var_104_5 = GetOrAddComponent(arg_104_0.actorTr, typeof(Canvas))

	var_104_5.overrideSorting = True
	var_104_5.sortingOrder = var_104_4

	local var_104_6 = GetOrAddComponent(arg_104_0.frontTr, typeof(Canvas))

	var_104_6.overrideSorting = True
	var_104_6.sortingOrder = var_104_4 + 1
	arg_104_0.activeInterLayer = arg_104_1

	GetOrAddComponent(arg_104_0.frontTr, typeof(GraphicRaycaster))

def var_0_0.ClearEffectInterlayer(arg_105_0, arg_105_1):
	if arg_105_0.activeInterLayer == arg_105_1:
		local var_105_0 = arg_105_0.actorTr.GetComponent(typeof(Canvas))
		local var_105_1 = arg_105_0.frontTr.GetComponent(typeof(Canvas))
		local var_105_2 = arg_105_0.frontTr.GetComponent(typeof(GraphicRaycaster))

		if var_105_0:
			Object.Destroy(var_105_0)

		if var_105_2:
			Object.Destroy(var_105_2)

		if var_105_1:
			Object.Destroy(var_105_1)

		arg_105_0.activeInterLayer = None

def var_0_0.ClearEffects(arg_106_0):
	removeAllChildren(arg_106_0.effectPanel)
	removeAllChildren(arg_106_0.centerPanel)

	if arg_106_0.activeInterLayer != None:
		arg_106_0.ClearEffectInterlayer(arg_106_0.activeInterLayer)

def var_0_0.PlaySoundEffect(arg_107_0, arg_107_1):
	if arg_107_1.ShouldPlaySoundEffect():
		local var_107_0, var_107_1 = arg_107_1.GetSoundeffect()

		arg_107_0.DelayCall(var_107_1, function()
			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_107_0))

	if arg_107_1.ShouldPlayVoice():
		arg_107_0.PlayVoice(arg_107_1)
	elif arg_107_1.ShouldStopVoice():
		arg_107_0.StopVoice()

def var_0_0.StopVoice(arg_109_0):
	if arg_109_0.currentVoice:
		arg_109_0.currentVoice.Stop(True)

		arg_109_0.currentVoice = None

def var_0_0.PlayVoice(arg_110_0, arg_110_1):
	if arg_110_0.voiceDelayTimer:
		arg_110_0.voiceDelayTimer.Stop()

		arg_110_0.voiceDelayTimer = None

	arg_110_0.StopVoice()

	local var_110_0, var_110_1 = arg_110_1.GetVoice()
	local var_110_2

	var_110_2 = arg_110_0.CreateDelayTimer(var_110_1, function()
		if var_110_2:
			var_110_2.Stop()

		if arg_110_0.voiceDelayTimer:
			arg_110_0.voiceDelayTimer = None

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_110_0, function(arg_112_0)
			if arg_112_0:
				arg_110_0.currentVoice = arg_112_0.playback))
	arg_110_0.voiceDelayTimer = var_110_2

def var_0_0.Reset(arg_113_0, arg_113_1, arg_113_2, arg_113_3):
	setActive(arg_113_0.castPanel, False)
	setActive(arg_113_0.bgPanel, False)
	setActive(arg_113_0.dialoguePanel, False)
	setActive(arg_113_0.asidePanel, False)
	setActive(arg_113_0.curtain, False)
	setActive(arg_113_0.flash, False)
	setActive(arg_113_0.optionsCg.gameObject, False)
	setActive(arg_113_0.bgGlitch, False)
	setActive(arg_113_0.locationTr, False)

	arg_113_0.locationTr.localPosition = arg_113_0.locationTrPos
	arg_113_0.locationStatus = var_0_9
	arg_113_0.flashCg.alpha = 1
	arg_113_0.goCG.alpha = 1

	arg_113_0.animationPlayer.Stop()
	arg_113_0.OnReset(arg_113_1, arg_113_2, arg_113_3)

def var_0_0.Clear(arg_114_0, arg_114_1):
	if arg_114_0.step:
		arg_114_0.ClearMoveNodes(arg_114_0.step)

	arg_114_0.bgs = {}
	arg_114_0.skipOption = None
	arg_114_0.step = None
	arg_114_0.goCG.alpha = 1
	arg_114_0.callback = None
	arg_114_0.autoNext = None
	arg_114_0.script = None
	arg_114_0.bgImage.sprite = None

	arg_114_0.OnClear()

	if arg_114_1:
		arg_114_1()

	pg.DelegateInfo.New(arg_114_0)

def var_0_0.StoryEnd(arg_115_0):
	setActive(arg_115_0.iconImage.gameObject, False)

	arg_115_0.iconImage.sprite = None
	arg_115_0.branchCodeList = {}
	arg_115_0.stop = False
	arg_115_0.pause = False

	if arg_115_0.voiceDelayTimer:
		arg_115_0.voiceDelayTimer.Stop()

		arg_115_0.voiceDelayTimer = None

	if arg_115_0.currentVoice:
		arg_115_0.currentVoice.Stop(True)

		arg_115_0.currentVoice = None

	arg_115_0.ClearEffects()
	arg_115_0.Clear()
	arg_115_0.OnEnd()

def var_0_0.PlayBgm(arg_116_0, arg_116_1):
	if arg_116_1.ShouldStopBgm():
		arg_116_0.StopBgm()

	if arg_116_1.ShoulePlayBgm():
		local var_116_0, var_116_1, var_116_2 = arg_116_1.GetBgmData()

		arg_116_0.DelayCall(var_116_1, function()
			arg_116_0.RevertBgmVolume()
			pg.BgmMgr.GetInstance().TempPlay(var_116_0))

		if var_116_2 and var_116_2 > 0:
			arg_116_0.defaultBgmVolume = pg.CriMgr.GetInstance().getBGMVolume()

			pg.CriMgr.GetInstance().setBGMVolume(var_116_2)

def var_0_0.StopBgm(arg_118_0, arg_118_1):
	arg_118_0.RevertBgmVolume()
	pg.BgmMgr.GetInstance().StopPlay()

def var_0_0.RevertBgmVolume(arg_119_0):
	if arg_119_0.defaultBgmVolume:
		pg.CriMgr.GetInstance().setBGMVolume(arg_119_0.defaultBgmVolume)

		arg_119_0.defaultBgmVolume = None

def var_0_0.StartUIAnimations(arg_120_0, arg_120_1, arg_120_2):
	parallelAsync({
		function(arg_121_0)
			arg_120_0.StartBlinkAnimation(arg_120_1, arg_121_0),
		function(arg_122_0)
			arg_120_0.StartBlinkWithColorAnimation(arg_120_1, arg_122_0),
		function(arg_123_0)
			arg_120_0.OnStartUIAnimations(arg_120_1, arg_123_0)
	}, arg_120_2)

def var_0_0.StartBlinkAnimation(arg_124_0, arg_124_1, arg_124_2):
	if arg_124_1.ShouldBlink():
		local var_124_0 = arg_124_1.GetBlinkData()
		local var_124_1 = var_124_0.black
		local var_124_2 = var_124_0.number
		local var_124_3 = var_124_0.dur
		local var_124_4 = var_124_0.delay
		local var_124_5 = var_124_0.alpha[1]
		local var_124_6 = var_124_0.alpha[2]
		local var_124_7 = var_124_0.wait

		arg_124_0.flashImg.color = var_124_1 and Color(0, 0, 0) or Color(1, 1, 1)

		setActive(arg_124_0.flash, True)

		local var_124_8 = {}

		for iter_124_0 = 1, var_124_2:
			table.insert(var_124_8, function(arg_125_0)
				arg_124_0.TweenAlpha(arg_124_0.flash, var_124_5, var_124_6, var_124_3 / 2, 0, function()
					arg_124_0.TweenAlpha(arg_124_0.flash, var_124_6, var_124_5, var_124_3 / 2, var_124_7, arg_125_0)))

		seriesAsync(var_124_8, function()
			setActive(arg_124_0.flash, False))

	arg_124_2()

def var_0_0.StartBlinkWithColorAnimation(arg_128_0, arg_128_1, arg_128_2):
	if arg_128_1.ShouldBlinkWithColor():
		local var_128_0 = arg_128_1.GetBlinkWithColorData()
		local var_128_1 = var_128_0.color
		local var_128_2 = var_128_0.alpha

		arg_128_0.flashImg.color = Color(var_128_1[1], var_128_1[2], var_128_1[3], var_128_1[4])

		setActive(arg_128_0.flash, True)

		local var_128_3 = {}

		for iter_128_0, iter_128_1 in ipairs(var_128_2):
			local var_128_4 = iter_128_1[1]
			local var_128_5 = iter_128_1[2]
			local var_128_6 = iter_128_1[3]
			local var_128_7 = iter_128_1[4]

			table.insert(var_128_3, function(arg_129_0)
				arg_128_0.TweenValue(arg_128_0.flash, var_128_4, var_128_5, var_128_6, var_128_7, function(arg_130_0)
					arg_128_0.flashCg.alpha = arg_130_0, arg_129_0))

		parallelAsync(var_128_3, function()
			setActive(arg_128_0.flash, False))

	arg_128_2()

def var_0_0.findTF(arg_132_0, arg_132_1, arg_132_2):
	assert(arg_132_0._tf, "transform should exist")

	return findTF(arg_132_2 or arg_132_0._tf, arg_132_1)

def var_0_0.OnStart(arg_133_0, arg_133_1):
	return

def var_0_0.OnReset(arg_134_0, arg_134_1, arg_134_2, arg_134_3):
	arg_134_3()

def var_0_0.OnBgUpdate(arg_135_0, arg_135_1):
	return

def var_0_0.OnInit(arg_136_0, arg_136_1, arg_136_2, arg_136_3):
	if arg_136_3:
		arg_136_3()

def var_0_0.OnStartUIAnimations(arg_137_0, arg_137_1, arg_137_2):
	if arg_137_2:
		arg_137_2()

def var_0_0.OnEnter(arg_138_0, arg_138_1, arg_138_2, arg_138_3):
	if arg_138_3:
		arg_138_3()

def var_0_0.OnWillExit(arg_139_0, arg_139_1, arg_139_2, arg_139_3):
	arg_139_3()

def var_0_0.OnWillClear(arg_140_0, arg_140_1):
	return

def var_0_0.OnClear(arg_141_0):
	return

def var_0_0.OnEnd(arg_142_0):
	return

return var_0_0
