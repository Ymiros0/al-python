from mgr.story.Include import *

class NewStoryMgr:

	colour1 = Color.New(1, 0.8705, 0.4196, 1)
	colour2 = Color.New(1, 1, 1, 1)



	var_0_10 = True

	def var_0_11(*args):
		if var_0_10 and IsUnityEditor:
			originalPrint(*args)

	var_0_12 = {
		"",
		"JP",
		"KR",
		"US",
		""
	}

	def var_0_13(arg_2_0):
		var_2_0 = var_0_12[PLATFORM_CODE]

		if arg_2_0 == "index":
			arg_2_0 = arg_2_0 .. var_2_0

		var_2_1

		if PLATFORM_CODE == PLATFORM_JP:
			var_2_1 = f"GameCfg.story{var_2_0}.{arg_2_0}"
		else:
			var_2_1 = f"GameCfg.story.{arg_2_0}"

		var_2_2, var_2_3 = pcall(function()
			return require(var_2_1))

		if not var_2_2:
			var_2_4 = True

			if UnGamePlayState:
				var_2_5 = f"GameCfg.dungeon.{arg_2_0}"

				if pcall(function()
					return require(var_2_5)):
					var_2_4 = False

			if var_2_4:
				errorMsg(f"不存在剧情ID对应的Lua.{arg_2_0)}"

		return var_2_2 and var_2_3

	def var_0_0.SetData(arg_5_0, arg_5_1):
		arg_5_0.playedList = {}

		for iter_5_0, iter_5_1 in ipairs(arg_5_1):
			var_5_0 = iter_5_1

			if iter_5_1 == 20008:
				var_5_0 = 1131

			if iter_5_1 == 20009:
				var_5_0 = 1132

			if iter_5_1 == 20010:
				var_5_0 = 1133

			if iter_5_1 == 20011:
				var_5_0 = 1134

			if iter_5_1 == 20012:
				var_5_0 = 1135

			if iter_5_1 == 20013:
				var_5_0 = 1136

			if iter_5_1 == 20014:
				var_5_0 = 1137

			arg_5_0.playedList[var_5_0] = True

	def var_0_0.SetPlayedFlag(arg_6_0, arg_6_1):
		var_0_11("Update story id", arg_6_1)

		arg_6_0.playedList[arg_6_1] = True

	def var_0_0.GetPlayedFlag(arg_7_0, arg_7_1):
		return arg_7_0.playedList[arg_7_1]

	def var_0_0.IsPlayed(arg_8_0, arg_8_1, arg_8_2):
		var_8_0, var_8_1 = arg_8_0.StoryName2StoryId(arg_8_1)
		var_8_2 = arg_8_0.GetPlayedFlag(var_8_0)
		var_8_3 = True

		if var_8_1 and not arg_8_2:
			var_8_3 = arg_8_0.GetPlayedFlag(var_8_1)

		return var_8_2 and var_8_3

	function var_0_14(arg_9_0)
		var_9_0 = {}

		for iter_9_0, iter_9_1 in pairs(arg_9_0):
			var_9_0[iter_9_1] = iter_9_0

		return var_9_0

	def var_0_0.StoryName2StoryId(arg_10_0, arg_10_1):
		if not var_0_0.indexs:
			var_0_0.indexs = var_0_14(var_0_13("index"))

		if not var_0_0.againIndexs:
			var_0_0.againIndexs = var_0_14(var_0_13("index_again"))

		return var_0_0.indexs[arg_10_1], var_0_0.againIndexs[arg_10_1]

	def var_0_0.StoryId2StoryName(arg_11_0, arg_11_1):
		if not var_0_0.indexIds:
			var_0_0.indexIds = var_0_13("index")

		if not var_0_0.againIndexIds:
			var_0_0.againIndexIds = var_0_13("index_again")

		return var_0_0.indexIds[arg_11_1], var_0_0.againIndexIds[arg_11_1]

	def var_0_0.StoryLinkNames(arg_12_0, arg_12_1):
		if not var_0_0.linkNames:
			var_0_0.linkNames = var_0_13("index_link")

		return var_0_0.linkNames[arg_12_1]

	def var_0_0._GetStoryPaintingsByName(arg_13_0, arg_13_1):
		return arg_13_1.GetUsingPaintingNames()

	def var_0_0.GetStoryPaintingsByName(arg_14_0, arg_14_1):
		var_14_0 = var_0_13(arg_14_1)

		if not var_14_0:
			var_0_11("not exist story file")

			return {}

		var_14_1 = Story.New(var_14_0, False)

		return arg_14_0._GetStoryPaintingsByName(var_14_1)

	def var_0_0.GetStoryPaintingsByNameList(arg_15_0, arg_15_1):
		var_15_0 = {}
		var_15_1 = {}

		for iter_15_0, iter_15_1 in ipairs(arg_15_1):
			for iter_15_2, iter_15_3 in ipairs(arg_15_0.GetStoryPaintingsByName(iter_15_1)):
				var_15_1[iter_15_3] = True

		for iter_15_4, iter_15_5 in pairs(var_15_1):
			table.insert(var_15_0, iter_15_4)

		return var_15_0

	def var_0_0.GetStoryPaintingsById(arg_16_0, arg_16_1):
		return arg_16_0.GetStoryPaintingsByIdList({
			arg_16_1
		})

	def var_0_0.GetStoryPaintingsByIdList(arg_17_0, arg_17_1):
		var_17_0 = _.map(arg_17_1, function(arg_18_0)
			return arg_17_0.StoryId2StoryName(arg_18_0))

		return arg_17_0.GetStoryPaintingsByNameList(var_17_0)

	def var_0_0.ShouldDownloadRes(arg_19_0, arg_19_1):
		var_19_0 = arg_19_0.GetStoryPaintingsByName(arg_19_1)

		return _.any(var_19_0, function(arg_20_0)
			return PaintingGroupConst.VerifyPaintingFileName(arg_20_0))

	def var_0_0.Init(arg_21_0, arg_21_1):
		arg_21_0.state = 1
		arg_21_0.playedList = {}
		arg_21_0.playQueue = {}

		PoolMgr.GetInstance().GetUI("NewStoryUI", True, function(arg_22_0)
			arg_21_0._go = arg_22_0
			arg_21_0._tf = tf(arg_21_0._go)
			arg_21_0.frontTr = findTF(arg_21_0._tf, "front")
			arg_21_0.UIOverlay = GameObject.Find("Overlay/UIOverlay")

			arg_21_0._go.transform.SetParent(arg_21_0.UIOverlay.transform, False)

			arg_21_0.skipBtn = findTF(arg_21_0._tf, "front/btns/btns/skip_button")
			arg_21_0.autoBtn = findTF(arg_21_0._tf, "front/btns/btns/auto_button")
			arg_21_0.autoBtnImg = findTF(arg_21_0._tf, "front/btns/btns/auto_button/sel").GetComponent(typeof(Image))
			arg_21_0.alphaImage = arg_21_0._tf.GetComponent(typeof(Image))
			arg_21_0.recordBtn = findTF(arg_21_0._tf, "front/btns/record")
			arg_21_0.dialogueContainer = findTF(arg_21_0._tf, "front/dialogue")
			arg_21_0.players = {
				AsideStoryPlayer.New(arg_22_0),
				DialogueStoryPlayer.New(arg_22_0),
				BgStoryPlayer.New(arg_22_0),
				CarouselPlayer.New(arg_22_0),
				VedioStoryPlayer.New(arg_22_0),
				CastStoryPlayer.New(arg_22_0)
			}
			arg_21_0.setSpeedPanel = StorySetSpeedPanel.New(arg_21_0._tf)
			arg_21_0.recordPanel = NewStoryRecordPanel.New()
			arg_21_0.recorder = StoryRecorder.New()

			setActive(arg_21_0._go, False)

			arg_21_0.state = 2

			if arg_21_1:
				arg_21_1())

	def var_0_0.Play(arg_23_0, arg_23_1, arg_23_2, arg_23_3, arg_23_4, arg_23_5, arg_23_6):
		table.insert(arg_23_0.playQueue, {
			arg_23_1,
			arg_23_2
		})

		if #arg_23_0.playQueue == 1:
			var_23_0

			function var_23_1()
				if #arg_23_0.playQueue == 0:
					return

				var_24_0 = arg_23_0.playQueue[1][1]
				var_24_1 = arg_23_0.playQueue[1][2]

				arg_23_0.SoloPlay(var_24_0, function(arg_25_0, arg_25_1)
					if var_24_1:
						var_24_1(arg_25_0, arg_25_1)

					table.remove(arg_23_0.playQueue, 1)
					var_23_1(), arg_23_3, arg_23_4, arg_23_5, arg_23_6)

			var_23_1()

	def var_0_0.Puase(arg_26_0):
		if arg_26_0.state != 3:
			var_0_11("state is not 'running'")

			return

		arg_26_0.state = 4

		for iter_26_0, iter_26_1 in ipairs(arg_26_0.players):
			iter_26_1.Pause()

	def var_0_0.Resume(arg_27_0):
		if arg_27_0.state != 4:
			var_0_11("state is not 'pause'")

			return

		arg_27_0.state = 3

		for iter_27_0, iter_27_1 in ipairs(arg_27_0.players):
			iter_27_1.Resume()

	def var_0_0.Stop(arg_28_0):
		if arg_28_0.state != 3:
			var_0_11("state is not 'running'")

			return

		arg_28_0.state = 5

		for iter_28_0, iter_28_1 in ipairs(arg_28_0.players):
			iter_28_1.Stop()

	def var_0_0.PlayForWorld(arg_29_0, arg_29_1, arg_29_2, arg_29_3, arg_29_4, arg_29_5, arg_29_6, arg_29_7):
		arg_29_0.optionSelCodes = arg_29_2 or {}
		arg_29_0.autoPlayFlag = arg_29_6

		arg_29_0.Play(arg_29_1, arg_29_3, arg_29_4, arg_29_5, arg_29_7, True)

	def var_0_0.ForceAutoPlay(arg_30_0, arg_30_1, arg_30_2, arg_30_3, arg_30_4):
		arg_30_0.autoPlayFlag = True

		function var_30_0(arg_31_0, arg_31_1)
			arg_30_2(arg_31_0, arg_31_1, arg_30_0.isAutoPlay)

		arg_30_0.Play(arg_30_1, var_30_0, arg_30_3, arg_30_4, True)

	def var_0_0.ForceManualPlay(arg_32_0, arg_32_1, arg_32_2, arg_32_3, arg_32_4):
		arg_32_0.banPlayFlag = True

		function var_32_0(arg_33_0, arg_33_1)
			arg_32_2(arg_33_0, arg_33_1, arg_32_0.isAutoPlay)

		arg_32_0.Play(arg_32_1, var_32_0, arg_32_3, arg_32_4, True)

	def var_0_0.SeriesPlay(arg_34_0, arg_34_1, arg_34_2, arg_34_3, arg_34_4, arg_34_5, arg_34_6):
		var_34_0 = {}

		for iter_34_0, iter_34_1 in ipairs(arg_34_1):
			table.insert(var_34_0, function(arg_35_0)
				arg_34_0.SoloPlay(iter_34_1, arg_35_0, arg_34_3, arg_34_4, arg_34_5, arg_34_6))

		seriesAsync(var_34_0, arg_34_2)

	def var_0_0.SoloPlay(arg_36_0, arg_36_1, arg_36_2, arg_36_3, arg_36_4, arg_36_5, arg_36_6):
		var_0_11("Play Story.", arg_36_1)

		var_36_0 = 1

		function var_36_1(arg_37_0, arg_37_1)
			var_36_0 = var_36_0 - 1

			if arg_36_2 and var_36_0 == 0:
				onNextTick(function()
					arg_36_2(arg_37_0, arg_37_1))

		var_36_2 = var_0_13(arg_36_1)

		if not var_36_2:
			var_36_1(False)
			var_0_11("not exist story file")

			return None

		if arg_36_0.IsReView():
			arg_36_3 = True

		arg_36_0.storyScript = Story.New(var_36_2, arg_36_3, arg_36_0.optionSelCodes, arg_36_5, arg_36_6)

		if not arg_36_0.CheckState():
			var_0_11("story state error")
			var_36_1(False)

			return None

		if not arg_36_0.storyScript.CanPlay():
			var_0_11("story cant be played")
			var_36_1(False)

			return None

		seriesAsync({
			function(arg_39_0)
				arg_36_0.CheckResDownload(arg_36_0.storyScript, arg_39_0),
			function(arg_40_0)
				originalPrint("start load story window*args")
				arg_36_0.CheckAndLoadDialogue(arg_36_0.storyScript, arg_40_0)
		}, function()
			originalPrint("enter story*args")
			arg_36_0.OnStart()

			var_41_0 = {}

			arg_36_0.currPlayer = None

			for iter_41_0, iter_41_1 in ipairs(arg_36_0.storyScript.steps):
				table.insert(var_41_0, function(arg_42_0)
					pg.m02.sendNotification(GAME.STORY_NEXT)

					var_42_0 = arg_36_0.players[iter_41_1.GetMode()]

					arg_36_0.currPlayer = var_42_0

					var_42_0.Play(arg_36_0.storyScript, iter_41_0, arg_42_0))

			seriesAsync(var_41_0, function()
				arg_36_0.OnEnd(var_36_1)))

	def var_0_0.CheckResDownload(arg_44_0, arg_44_1, arg_44_2):
		var_44_0 = arg_44_0._GetStoryPaintingsByName(arg_44_1)
		var_44_1 = table.concat(var_44_0, ",")

		originalPrint(f"start:wnload res {var_44_1}")

		var_44_2 = {}

		for iter_44_0, iter_44_1 in ipairs(var_44_0):
			PaintingGroupConst.AddPaintingNameWithFilteMap(var_44_2, iter_44_1)

		PaintingGroupConst.PaintingDownload({
			isShowBox = True,
			paintingNameList = var_44_2,
			finishFunc = arg_44_2
		})

	function var_0_15(arg_45_0, arg_45_1)
		ResourceMgr.Inst.getAssetAsync(f"ui/{arg_45_0}", arg_45_0, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_46_0)
			arg_45_1(arg_46_0)), True, True)

	def var_0_0.CheckAndLoadDialogue(arg_47_0, arg_47_1, arg_47_2):
		var_47_0 = arg_47_1.GetDialogueStyleName()

		if not arg_47_0.dialogueContainer.Find(var_47_0):
			var_0_15(f"NewStoryDialogue{var_47_0}", function(arg_48_0)
				Object.Instantiate(arg_48_0, arg_47_0.dialogueContainer).name = var_47_0

				arg_47_2())
		else
			arg_47_2()

	def var_0_0.CheckState(arg_49_0):
		if arg_49_0.state == 3 or arg_49_0.state == 1 or arg_49_0.state == 4:
			return False

		return True

	def var_0_0.RegistSkipBtn(arg_50_0):
		function var_50_0()
			arg_50_0.TrackingSkip()
			arg_50_0.storyScript.SkipAll()
			arg_50_0.currPlayer.NextOneImmediately()

		onButton(arg_50_0, arg_50_0.skipBtn, function()
			if arg_50_0.IsStopping() or arg_50_0.IsPausing():
				return

			if not arg_50_0.currPlayer.CanSkip():
				return

			if arg_50_0.IsReView() or arg_50_0.storyScript.IsPlayed() or not arg_50_0.storyScript.ShowSkipTip():
				var_50_0()

				return

			arg_50_0.Puase()

			arg_50_0.isOpenMsgbox = True

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				parent = rtf(arg_50_0._tf.Find("front")),
				content = i18n("story_skip_confirm"),
				def onYes:()
					arg_50_0.Resume()
					var_50_0(),
				def onNo:()
					arg_50_0.isOpenMsgbox = False

					arg_50_0.Resume(),
				weight = LayerWeightConst.TOP_LAYER
			}), SFX_PANEL)

	def var_0_0.RegistAutoBtn(arg_55_0):
		onButton(arg_55_0, arg_55_0.autoBtn, function()
			if arg_55_0.IsStopping() or arg_55_0.IsPausing():
				return

			if arg_55_0.storyScript.GetAutoPlayFlag():
				arg_55_0.storyScript.StopAutoPlay()
				arg_55_0.currPlayer.CancelAuto()
			else
				arg_55_0.storyScript.SetAutoPlay()
				arg_55_0.currPlayer.NextOne()

			if arg_55_0.storyScript:
				arg_55_0.UpdateAutoBtn(), SFX_PANEL)

		var_55_0 = arg_55_0.IsAutoPlay()

		if var_55_0:
			arg_55_0.storyScript.SetAutoPlay()
			arg_55_0.UpdateAutoBtn()

			arg_55_0.autoPlayFlag = False

		arg_55_0.banPlayFlag = False
		arg_55_0.isAutoPlay = var_55_0

	def var_0_0.RegistRecordBtn(arg_57_0):
		onButton(arg_57_0, arg_57_0.recordBtn, function()
			if arg_57_0.storyScript.GetAutoPlayFlag():
				return

			if not arg_57_0.recordPanel.CanOpen():
				return

			var_58_0 = "Show"

			arg_57_0.recordPanel[var_58_0](arg_57_0.recordPanel, arg_57_0.recorder), SFX_PANEL)

	def var_0_0.TriggerAutoBtn(arg_59_0):
		if not arg_59_0.IsRunning():
			return

		triggerButton(arg_59_0.autoBtn)

	def var_0_0.TriggerSkipBtn(arg_60_0):
		if not arg_60_0.IsRunning():
			return

		triggerButton(arg_60_0.skipBtn)

	def var_0_0.ForEscPress(arg_61_0):
		if arg_61_0.recordPanel.IsShowing():
			arg_61_0.recordPanel.Hide()
		else
			arg_61_0.TriggerSkipBtn()

	def var_0_0.UpdatePlaySpeed(arg_62_0, arg_62_1):
		if arg_62_0.IsRunning() and arg_62_0.storyScript:
			arg_62_0.storyScript.SetPlaySpeed(arg_62_1)

	def var_0_0.GetPlaySpeed(arg_63_0):
		if arg_63_0.IsRunning() and arg_63_0.storyScript:
			return arg_63_0.storyScript.GetPlaySpeed()

	def var_0_0.OnStart(arg_64_0):
		arg_64_0.recorder.Clear()
		removeOnButton(arg_64_0._go)
		removeOnButton(arg_64_0.skipBtn)
		removeOnButton(arg_64_0.autoBtn)
		removeOnButton(arg_64_0.recordBtn)

		arg_64_0.alphaImage.color = Color(0, 0, 0, arg_64_0.storyScript.GetStoryAlpha())

		setActive(arg_64_0.recordBtn, not arg_64_0.storyScript.ShouldHideRecord())
		arg_64_0.ClearStoryEventTriggerListener()

		var_64_0 = arg_64_0.storyScript.GetAllStepDispatcherRecallName()

		if #var_64_0 > 0:
			arg_64_0.storyEventTriggerListener = StoryEventTriggerListener.New(var_64_0)

		arg_64_0.state = 3

		arg_64_0.TrackingStart()
		pg.m02.sendNotification(GAME.STORY_BEGIN, arg_64_0.storyScript.GetName())
		pg.m02.sendNotification(GAME.STORY_UPDATE, {
			storyId = arg_64_0.storyScript.GetName()
		})
		pg.DelegateInfo.New(arg_64_0)

		for iter_64_0, iter_64_1 in ipairs(arg_64_0.players):
			iter_64_1.StoryStart(arg_64_0.storyScript)

		setActive(arg_64_0._go, True)
		arg_64_0._tf.SetAsLastSibling()
		setActive(arg_64_0.skipBtn, not arg_64_0.storyScript.ShouldHideSkip())
		setActive(arg_64_0.autoBtn, not arg_64_0.storyScript.ShouldHideAutoBtn())

		arg_64_0.bgmVolumeValue = pg.CriMgr.GetInstance().getBGMVolume()

		arg_64_0.RegistSkipBtn()
		arg_64_0.RegistAutoBtn()
		arg_64_0.RegistRecordBtn()

	def var_0_0.TrackingStart(arg_65_0):
		arg_65_0.trackFlag = False

		if not arg_65_0.storyScript:
			return

		var_65_0 = arg_65_0.StoryName2StoryId(arg_65_0.storyScript.GetName())

		if not arg_65_0.GetPlayedFlag(var_65_0):
			TrackConst.StoryStart(var_65_0)

			arg_65_0.trackFlag = True

	def var_0_0.TrackingSkip(arg_66_0):
		if not arg_66_0.trackFlag or not arg_66_0.storyScript:
			return

		var_66_0 = arg_66_0.StoryName2StoryId(arg_66_0.storyScript.GetName())

		TrackConst.StorySkip(var_66_0)

	def var_0_0.ClearStoryEvent(arg_67_0):
		if arg_67_0.storyEventTriggerListener:
			arg_67_0.storyEventTriggerListener.Clear()

	def var_0_0.CheckStoryEvent(arg_68_0, arg_68_1):
		if arg_68_0.storyEventTriggerListener:
			return arg_68_0.storyEventTriggerListener.ExistCache(arg_68_1)

		return False

	def var_0_0.GetStoryEventArg(arg_69_0, arg_69_1):
		if not arg_69_0.CheckStoryEvent(arg_69_1):
			return None

		if arg_69_0.storyEventTriggerListener and arg_69_0.storyEventTriggerListener.ExistArg(arg_69_1):
			return arg_69_0.storyEventTriggerListener.GetArg(arg_69_1)

		return None

	def var_0_0.UpdateAutoBtn(arg_70_0):
		var_70_0 = arg_70_0.storyScript.GetAutoPlayFlag()

		arg_70_0.ClearAutoBtn(var_70_0)

	def var_0_0.ClearAutoBtn(arg_71_0, arg_71_1):
		arg_71_0.autoBtnImg.color = arg_71_1 and colour1 or colour2
		arg_71_0.isAutoPlay = arg_71_1

		var_71_0 = arg_71_1 and "Show" or "Hide"

		arg_71_0.setSpeedPanel[var_71_0](arg_71_0.setSpeedPanel)

	def var_0_0.ClearStoryEventTriggerListener(arg_72_0):
		if arg_72_0.storyEventTriggerListener:
			arg_72_0.storyEventTriggerListener.Dispose()

			arg_72_0.storyEventTriggerListener = None

	def var_0_0.Clear(arg_73_0):
		arg_73_0.ClearStoryEventTriggerListener()
		arg_73_0.recorder.Clear()
		arg_73_0.recordPanel.Hide()

		arg_73_0.autoPlayFlag = False
		arg_73_0.banPlayFlag = False

		removeOnButton(arg_73_0._go)
		removeOnButton(arg_73_0.skipBtn)
		removeOnButton(arg_73_0.recordBtn)
		removeOnButton(arg_73_0.autoBtn)
		arg_73_0.ClearAutoBtn(False)

		if isActive(arg_73_0._go):
			pg.DelegateInfo.Dispose(arg_73_0)

		if arg_73_0.setSpeedPanel:
			arg_73_0.setSpeedPanel.Clear()

		setActive(arg_73_0.skipBtn, False)
		setActive(arg_73_0._go, False)

		for iter_73_0, iter_73_1 in ipairs(arg_73_0.players):
			iter_73_1.StoryEnd(arg_73_0.storyScript)

		arg_73_0.optionSelCodes = None

		pg.BgmMgr.GetInstance().ContinuePlay()
		pg.m02.sendNotification(GAME.STORY_END)

		if arg_73_0.isOpenMsgbox:
			pg.MsgboxMgr.GetInstance().hide()

		var_73_0 = pg.CriMgr.GetInstance().getBGMVolume()

		if arg_73_0.bgmVolumeValue and arg_73_0.bgmVolumeValue != var_73_0:
			pg.CriMgr.GetInstance().setBGMVolume(arg_73_0.bgmVolumeValue)

		arg_73_0.bgmVolumeValue = None

	def var_0_0.OnEnd(arg_74_0, arg_74_1):
		arg_74_0.Clear()

		if arg_74_0.state == 3 or arg_74_0.state == 5:
			arg_74_0.state = 6

			var_74_0 = arg_74_0.storyScript.GetNextScriptName()

			if var_74_0 and not arg_74_0.IsReView():
				arg_74_0.storyScript = None

				arg_74_0.Play(var_74_0, arg_74_1)
			else
				var_74_1 = arg_74_0.storyScript.GetBranchCode()

				arg_74_0.storyScript = None

				if arg_74_1:
					arg_74_1(True, var_74_1)
		else
			arg_74_0.state = 6

			var_74_2 = arg_74_0.storyScript.GetBranchCode()

			if arg_74_1:
				arg_74_1(True, var_74_2)

	def var_0_0.OnSceneEnter(arg_75_0, arg_75_1):
		if not arg_75_0.scenes:
			arg_75_0.scenes = {}

		arg_75_0.scenes[arg_75_1.view] = True

	def var_0_0.OnSceneExit(arg_76_0, arg_76_1):
		if not arg_76_0.scenes:
			return

		arg_76_0.scenes[arg_76_1.view] = None

	def var_0_0.IsReView(arg_77_0):
		var_77_0 = getProxy(ContextProxy).GetPrevContext(1)

		return arg_77_0.scenes[WorldMediaCollectionScene.__cname] == True or var_77_0 and var_77_0.mediator == WorldMediaCollectionMediator

	def var_0_0.IsRunning(arg_78_0):
		return arg_78_0.state == 3

	def var_0_0.IsStopping(arg_79_0):
		return arg_79_0.state == 5

	def var_0_0.IsPausing(arg_80_0):
		return arg_80_0.state == 4

	def var_0_0.IsAutoPlay(arg_81_0):
		if arg_81_0.banPlayFlag:
			return False

		return getProxy(SettingsProxy).GetStoryAutoPlayFlag() or arg_81_0.autoPlayFlag == True

	def var_0_0.GetRectSize(arg_82_0):
		return Vector2(arg_82_0._tf.rect.width, arg_82_0._tf.rect.height)

	def var_0_0.AddRecord(arg_83_0, arg_83_1):
		arg_83_0.recorder.Add(arg_83_1)

	def var_0_0.Quit(arg_84_0):
		arg_84_0.recorder.Dispose()
		arg_84_0.recordPanel.Dispose()
		arg_84_0.setSpeedPanel.Dispose()

		arg_84_0.state = 7
		arg_84_0.storyScript = None
		arg_84_0.playQueue = {}
		arg_84_0.playedList = {}
		arg_84_0.scenes = {}

	def var_0_0.Fix(arg_85_0):
		var_85_0 = getProxy(PlayerProxy).getRawData().GetRegisterTime()
		var_85_1 = pg.TimeMgr.GetInstance().parseTimeFromConfig({
			{
				2021,
				4,
				8
			},
			{
				9,
				0,
				0
			}
		})
		var_85_2 = {
			10020,
			10021,
			10022,
			10023,
			10024,
			10025,
			10026,
			10027
		}

		if var_85_0 <= var_85_1:
			_.each(var_85_2, function(arg_86_0)
				arg_85_0.playedList[arg_86_0] = True)

		var_85_3 = 5001
		var_85_4 = 5020
		var_85_5 = getProxy(TaskProxy)
		var_85_6 = 0

		for iter_85_0 = var_85_3, var_85_4, -1:
			if var_85_5.getFinishTaskById(iter_85_0) or var_85_5.getTaskById(iter_85_0):
				var_85_6 = iter_85_0

				break

		for iter_85_1 = var_85_6, var_85_4, -1:
			var_85_7 = pg.task_data_template[iter_85_1]

			if var_85_7:
				var_85_8 = var_85_7.story_id

				if var_85_8 and #var_85_8 > 0 and not arg_85_0.IsPlayed(var_85_8):
					arg_85_0.playedList[var_85_8] = True

		var_85_9 = getProxy(ActivityProxy).getActivityById(ActivityConst.JYHZ_ACTIVITY_ID)

		if var_85_9 and not var_85_9.isEnd():
			var_85_10 = _.flatten(var_85_9.getConfig("config_data"))
			var_85_11

			for iter_85_2 = #var_85_10, 1, -1:
				var_85_12 = pg.task_data_template[var_85_10[iter_85_2]].story_id

				if var_85_12 and #var_85_12 > 0:
					var_85_13 = arg_85_0.IsPlayed(var_85_12)

					if var_85_11:
						if not var_85_13:
							arg_85_0.playedList[var_85_12] = True
					elif var_85_13:
						var_85_11 = iter_85_2
