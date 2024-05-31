local var_0_0 = import(".MapBuilder")
local var_0_1 = class("MapBuilderNormal", var_0_0)

def var_0_1.Ctor(arg_1_0, ...):
	var_0_1.super.Ctor(arg_1_0, ...)

	arg_1_0.mapItemTimer = {}
	arg_1_0.chapterTFsById = {}
	arg_1_0.chaptersInBackAnimating = {}

def var_0_1.GetType(arg_2_0):
	return var_0_0.TYPENORMAL

def var_0_1.getUIName(arg_3_0):
	return "levels"

def var_0_1.Load(arg_4_0):
	if arg_4_0._state != var_0_1.STATES.NONE:
		return

	arg_4_0._state = var_0_1.STATES.LOADING

	pg.UIMgr.GetInstance().LoadingOn()
	seriesAsync({
		function(arg_5_0)
			arg_4_0.preload(arg_5_0),
		function(arg_6_0)
			local var_6_0 = arg_4_0.float.Find("levels").gameObject

			arg_4_0.Loaded(var_6_0)
			arg_4_0.Init()
	})

def var_0_1.Destroy(arg_7_0):
	if arg_7_0._state == var_0_1.STATES.DESTROY:
		return

	if not arg_7_0.GetLoaded():
		arg_7_0._state = var_0_1.STATES.DESTROY

		return

	arg_7_0.Hide()
	arg_7_0.OnDestroy()
	pg.DelegateInfo.Dispose(arg_7_0)

	arg_7_0._go = None

	arg_7_0.disposeEvent()
	arg_7_0.cleanManagedTween()

	arg_7_0._state = var_0_1.STATES.DESTROY

def var_0_1.OnInit(arg_8_0):
	arg_8_0.chapterTpl = arg_8_0._tf.Find("level_tpl")

	setActive(arg_8_0.chapterTpl, False)

	arg_8_0.storyTpl = arg_8_0._tf.Find("story_tpl")

	setActive(arg_8_0.storyTpl, False)

	arg_8_0.itemHolder = arg_8_0._tf.Find("items")
	arg_8_0.storyHolder = arg_8_0._tf.Find("stories")

def var_0_1.OnShow(arg_9_0):
	setActive(arg_9_0.sceneParent.mainLayer.Find("title_chapter_lines"), True)
	setActive(arg_9_0.sceneParent.topChapter.Find("title_chapter"), True)
	setActive(arg_9_0.sceneParent.topChapter.Find("type_chapter"), True)

def var_0_1.OnHide(arg_10_0):
	setActive(arg_10_0.sceneParent.mainLayer.Find("title_chapter_lines"), False)
	setActive(arg_10_0.sceneParent.topChapter.Find("title_chapter"), False)
	setActive(arg_10_0.sceneParent.topChapter.Find("type_chapter"), False)
	table.clear(arg_10_0.chaptersInBackAnimating)
	arg_10_0.StopMapItemTimers()

	for iter_10_0, iter_10_1 in pairs(arg_10_0.chapterTFsById):
		local var_10_0 = findTF(iter_10_1, "main/info/bk")

		LeanTween.cancel(rtf(var_10_0))

	var_0_1.super.OnHide(arg_10_0)

def var_0_1.OnDestroy(arg_11_0):
	arg_11_0.mapItemTimer = None

	var_0_1.super.OnDestroy(arg_11_0)

def var_0_1.StartTimer(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	if not arg_12_0.mapItemTimer[arg_12_1]:
		arg_12_0.mapItemTimer[arg_12_1] = Timer.New(arg_12_2, arg_12_3)
	else
		arg_12_0.mapItemTimer[arg_12_1].Reset(arg_12_2, arg_12_3)

	arg_12_0.mapItemTimer[arg_12_1].Start()

def var_0_1.StopMapItemTimers(arg_13_0):
	for iter_13_0, iter_13_1 in pairs(arg_13_0.mapItemTimer):
		iter_13_1.Stop()

	table.clear(arg_13_0.mapItemTimer)

def var_0_1.Update(arg_14_0, arg_14_1):
	arg_14_0.float.pivot = Vector2(0.5, 0.5)
	arg_14_0.float.anchoredPosition = Vector2(0, 0)

	local var_14_0 = string.split(arg_14_1.getConfig("name"), "||")

	setText(arg_14_0.sceneParent.chapterName, var_14_0[1])

	local var_14_1 = arg_14_1.getMapTitleNumber()

	arg_14_0.sceneParent.loader.GetSpriteQuiet("chapterno", "chapter" .. var_14_1, arg_14_0.sceneParent.chapterNoTitle, True)
	var_0_1.super.Update(arg_14_0, arg_14_1)

def var_0_1.UpdateButtons(arg_15_0):
	arg_15_0.sceneParent.updateDifficultyBtns()
	arg_15_0.sceneParent.updateActivityBtns()

def var_0_1.UpdateMapItems(arg_16_0):
	if not arg_16_0.isShowing():
		return

	var_0_1.super.UpdateMapItems(arg_16_0)
	arg_16_0.StopMapItemTimers()

	local var_16_0 = arg_16_0.data
	local var_16_1 = var_16_0.GetChapterInProgress()

	if var_16_1 and isa(var_16_1, ChapterStoryGroup):
		setActive(arg_16_0.itemHolder, False)
		setActive(arg_16_0.storyHolder, True)
		arg_16_0.UpdateStoryGroup()

		return

	setActive(arg_16_0.itemHolder, True)
	setActive(arg_16_0.storyHolder, False)

	local var_16_2 = getProxy(ChapterProxy)
	local var_16_3 = {}

	for iter_16_0, iter_16_1 in pairs(var_16_0.getChapters()):
		if (iter_16_1.isUnlock() or iter_16_1.activeAlways()) and (not iter_16_1.ifNeedHide() or var_16_2.GetJustClearChapters(iter_16_1.id)):
			table.insert(var_16_3, iter_16_1)

	table.clear(arg_16_0.chapterTFsById)
	UIItemList.StaticAlign(arg_16_0.itemHolder, arg_16_0.chapterTpl, #var_16_3, function(arg_17_0, arg_17_1, arg_17_2)
		if arg_17_0 == UIItemList.EventUpdate:
			local var_17_0 = var_16_3[arg_17_1 + 1]

			arg_16_0.UpdateMapItem(arg_17_2, var_17_0)

			arg_17_2.name = "Chapter_" .. var_17_0.id
			arg_16_0.chapterTFsById[var_17_0.id] = arg_17_2)

	local var_16_4 = {}

	for iter_16_2, iter_16_3 in pairs(var_16_3):
		local var_16_5 = iter_16_3.getConfigTable()

		var_16_4[var_16_5.pos_x] = var_16_4[var_16_5.pos_x] or {}

		local var_16_6 = var_16_4[var_16_5.pos_x]

		var_16_6[var_16_5.pos_y] = var_16_6[var_16_5.pos_y] or {}

		local var_16_7 = var_16_6[var_16_5.pos_y]

		table.insert(var_16_7, iter_16_3)

	for iter_16_4, iter_16_5 in pairs(var_16_4):
		for iter_16_6, iter_16_7 in pairs(iter_16_5):
			local var_16_8 = {}

			seriesAsync({
				function(arg_18_0)
					local var_18_0 = 0

					for iter_18_0, iter_18_1 in pairs(iter_16_7):
						if iter_18_1.ifNeedHide() and var_16_2.GetJustClearChapters(iter_18_1.id) and arg_16_0.chapterTFsById[iter_18_1.id]:
							var_18_0 = var_18_0 + 1

							local var_18_1 = arg_16_0.chapterTFsById[iter_18_1.id]

							setActive(var_18_1, True)
							arg_16_0.PlayChapterItemAnimationBackward(var_18_1, iter_18_1, function()
								var_18_0 = var_18_0 - 1

								setActive(var_18_1, False)
								var_16_2.RecordJustClearChapters(iter_18_1.id, None)

								if var_18_0 <= 0:
									arg_18_0())

							var_16_8[iter_18_1.id] = True
						elif arg_16_0.chapterTFsById[iter_18_1.id]:
							setActive(arg_16_0.chapterTFsById[iter_18_1.id], False)

					if var_18_0 <= 0:
						arg_18_0(),
				function(arg_20_0)
					local var_20_0 = 0

					for iter_20_0, iter_20_1 in pairs(iter_16_7):
						if not var_16_8[iter_20_1.id]:
							var_20_0 = var_20_0 + 1

							setActive(arg_16_0.chapterTFsById[iter_20_1.id], True)
							arg_16_0.PlayChapterItemAnimation(arg_16_0.chapterTFsById[iter_20_1.id], iter_20_1, function()
								var_20_0 = var_20_0 - 1

								if var_20_0 <= 0:
									arg_20_0())
			})

def var_0_1.UpdateMapItem(arg_22_0, arg_22_1, arg_22_2):
	local var_22_0 = arg_22_2.getConfigTable()

	setAnchoredPosition(arg_22_1, {
		x = arg_22_0.mapWidth * var_22_0.pos_x,
		y = arg_22_0.mapHeight * var_22_0.pos_y
	})

	local var_22_1 = findTF(arg_22_1, "main")

	setActive(var_22_1, True)

	local var_22_2 = findTF(var_22_1, "circle/fordark")
	local var_22_3 = findTF(var_22_1, "info/bk/fordark")

	setActive(var_22_2, var_22_0.icon_outline == 1)
	setActive(var_22_3, var_22_0.icon_outline == 1)

	local var_22_4 = findTF(var_22_1, "circle/clear_flag")
	local var_22_5 = findTF(var_22_1, "circle/progress")
	local var_22_6 = findTF(var_22_1, "circle/progress_text")
	local var_22_7 = findTF(var_22_1, "circle/stars")
	local var_22_8 = string.split(var_22_0.name, "|")

	setText(findTF(var_22_1, "info/bk/title_form/title_index"), var_22_0.chapter_name .. "  ")
	setText(findTF(var_22_1, "info/bk/title_form/title"), var_22_8[1])
	setText(findTF(var_22_1, "info/bk/title_form/title_en"), var_22_8[2] or "")
	setFillAmount(var_22_5, arg_22_2.progress / 100)
	setText(var_22_6, string.format("%d%%", arg_22_2.progress))
	setActive(var_22_7, arg_22_2.existAchieve())

	if arg_22_2.existAchieve():
		for iter_22_0, iter_22_1 in ipairs(arg_22_2.achieves):
			local var_22_9 = ChapterConst.IsAchieved(iter_22_1)
			local var_22_10 = var_22_7.Find("star" .. iter_22_0 .. "/light")

			setActive(var_22_10, var_22_9)

	local var_22_11 = not arg_22_2.active and arg_22_2.isClear()

	setActive(var_22_4, var_22_11)
	setActive(var_22_6, not var_22_11)
	arg_22_0.DeleteTween("fighting" .. arg_22_2.id)

	local var_22_12 = findTF(var_22_1, "circle/fighting")

	setText(findTF(var_22_12, "Text"), i18n("tag_level_fighting"))

	local var_22_13 = findTF(var_22_1, "circle/oni")

	setText(findTF(var_22_13, "Text"), i18n("tag_level_oni"))

	local var_22_14 = findTF(var_22_1, "circle/narrative")

	setText(findTF(var_22_14, "Text"), i18n("tag_level_narrative"))
	setActive(var_22_12, False)
	setActive(var_22_13, False)
	setActive(var_22_14, False)

	local var_22_15
	local var_22_16

	if arg_22_2.getConfig("chapter_tag") == 1:
		var_22_15 = var_22_14

	if arg_22_2.active:
		var_22_15 = arg_22_2.existOni() and var_22_13 or var_22_12

	if var_22_15:
		setActive(var_22_15, True)

		local var_22_17 = GetOrAddComponent(var_22_15, "CanvasGroup")

		var_22_17.alpha = 1

		arg_22_0.RecordTween("fighting" .. arg_22_2.id, LeanTween.alphaCanvas(var_22_17, 0, 0.5).setFrom(1).setEase(LeanTweenType.easeInOutSine).setLoopPingPong().uniqueId)

	local var_22_18 = findTF(var_22_1, "triesLimit")

	setActive(var_22_18, False)

	if arg_22_2.isTriesLimit():
		local var_22_19 = arg_22_2.getConfig("count")
		local var_22_20 = var_22_19 - arg_22_2.getTodayDefeatCount() .. "/" .. var_22_19

		setText(var_22_18.Find("label"), i18n("levelScene_chapter_count_tip"))
		setText(var_22_18.Find("Text"), setColorStr(var_22_20, var_22_19 <= arg_22_2.getTodayDefeatCount() and COLOR_RED or COLOR_GREEN))

		local var_22_21 = getProxy(ChapterProxy).IsActivitySPChapterActive() and SettingsProxy.IsShowActivityMapSPTip()

		setActive(var_22_18.Find("TipRect"), var_22_21)

	local var_22_22 = arg_22_2.GetDailyBonusQuota()
	local var_22_23 = findTF(var_22_1, "mark")

	setActive(var_22_23.Find("bonus"), var_22_22)
	setActive(var_22_23, var_22_22)

	if var_22_22:
		local var_22_24 = var_22_23.GetComponent(typeof(CanvasGroup))
		local var_22_25 = arg_22_0.sceneParent.contextData.map.getConfig("type") == Map.ACTIVITY_HARD and "bonus_us_hard" or "bonus_us"

		arg_22_0.sceneParent.loader.GetSprite("ui/levelmainscene_atlas", var_22_25, var_22_23.Find("bonus"))
		LeanTween.cancel(go(var_22_23), True)

		local var_22_26 = var_22_23.anchoredPosition.y

		var_22_24.alpha = 0

		LeanTween.value(go(var_22_23), 0, 1, 0.2).setOnUpdate(System.Action_float(function(arg_23_0)
			var_22_24.alpha = arg_23_0

			local var_23_0 = var_22_23.anchoredPosition

			var_23_0.y = var_22_26 * arg_23_0
			var_22_23.anchoredPosition = var_23_0)).setOnComplete(System.Action(function()
			var_22_24.alpha = 1

			local var_24_0 = var_22_23.anchoredPosition

			var_24_0.y = var_22_26
			var_22_23.anchoredPosition = var_24_0)).setEase(LeanTweenType.easeOutSine).setDelay(0.7)

	local var_22_27 = arg_22_2.id

	onButton(arg_22_0.sceneParent, var_22_1, function()
		if arg_22_0.InvokeParent("isfrozen"):
			return

		if arg_22_0.chaptersInBackAnimating[var_22_27]:
			return

		local var_25_0 = getProxy(ChapterProxy).getChapterById(var_22_27)

		if not var_25_0.isUnlock():
			local var_25_1 = var_25_0.getPrevChapterName()

			pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_tracking_error_pre", var_25_1))

			return

		local var_25_2 = var_25_0.getConfig("unlocklevel")

		if var_25_2 > arg_22_0.sceneParent.player.level:
			pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_chapter_level_limit", var_25_2))

			return

		local var_25_3 = getProxy(ChapterProxy).getActiveChapter(True)

		if var_25_3 and var_25_3.id != var_22_27:
			arg_22_0.InvokeParent("emit", LevelMediator2.ON_STRATEGYING_CHAPTER)

			return

		if var_25_0.active:
			arg_22_0.InvokeParent("switchToChapter", var_25_0)
		else
			if arg_22_0.sceneParent.contextData.map.getConfig("type") == Map.ACT_EXTRA and var_25_0.getPlayType() == ChapterConst.TypeRange:
				SettingsProxy.SetActivityMapSPTip()
				arg_22_0.UpdateChapterTF(var_22_27)

			local var_25_4 = arg_22_1.localPosition

			arg_22_0.InvokeParent("displayChapterPanel", var_25_0, Vector3(var_25_4.x - 10, var_25_4.y + 150)), SFX_UI_WEIGHANCHOR_SELECT)

def var_0_1.PlayChapterItemAnimation(arg_26_0, arg_26_1, arg_26_2, arg_26_3):
	local var_26_0 = findTF(arg_26_1, "main")
	local var_26_1 = var_26_0.Find("info")
	local var_26_2 = findTF(var_26_0, "circle")
	local var_26_3 = findTF(var_26_0, "info/bk")

	LeanTween.cancel(go(var_26_2))

	var_26_2.localScale = Vector3.zero

	local var_26_4 = LeanTween.scale(var_26_2, Vector3.one, 0.3).setDelay(0.3)

	arg_26_0.RecordTween(var_26_4.uniqueId)
	LeanTween.cancel(go(var_26_3))
	setAnchoredPosition(var_26_3, {
		x = -1 * var_26_1.rect.width
	})
	shiftPanel(var_26_3, 0, None, 0.4, 0.4, True, True, None, function()
		if arg_26_2.isTriesLimit():
			setActive(findTF(var_26_0, "triesLimit"), True)

		if arg_26_3:
			arg_26_3())

def var_0_1.PlayChapterItemAnimationBackward(arg_28_0, arg_28_1, arg_28_2, arg_28_3):
	local var_28_0 = findTF(arg_28_1, "main")
	local var_28_1 = var_28_0.Find("info")
	local var_28_2 = findTF(var_28_0, "circle")
	local var_28_3 = findTF(var_28_0, "info/bk")

	LeanTween.cancel(go(var_28_2))

	var_28_2.localScale = Vector3.one

	local var_28_4 = LeanTween.scale(go(var_28_2), Vector3.zero, 0.3).setDelay(0.3)

	arg_28_0.RecordTween(var_28_4.uniqueId)

	arg_28_0.chaptersInBackAnimating[arg_28_2.id] = True

	LeanTween.cancel(go(var_28_3))
	setAnchoredPosition(var_28_3, {
		x = 0
	})
	shiftPanel(var_28_3, -1 * var_28_1.rect.width, None, 0.4, 0.4, True, True, None, function()
		arg_28_0.chaptersInBackAnimating[arg_28_2.id] = None

		if arg_28_3:
			arg_28_3())

	if arg_28_2.isTriesLimit():
		setActive(findTF(var_28_0, "triesLimit"), False)

def var_0_1.UpdateChapterTF(arg_30_0, arg_30_1):
	local var_30_0 = arg_30_0.chapterTFsById[arg_30_1]

	if var_30_0:
		local var_30_1 = getProxy(ChapterProxy).getChapterById(arg_30_1)

		arg_30_0.UpdateMapItem(var_30_0, var_30_1)
		arg_30_0.PlayChapterItemAnimation(var_30_0, var_30_1)

def var_0_1.AddChapterTF(arg_31_0, arg_31_1):
	local var_31_0 = arg_31_0.data

	if arg_31_0.chapterTFsById[arg_31_1]:
		arg_31_0.UpdateChapterTF(arg_31_1)
	elif _.contains(var_31_0.GetChapterList(), function(arg_32_0)
		if arg_32_0 != arg_31_1:
			return False

		local var_32_0 = getProxy(ChapterProxy).getChapterById(arg_31_1, True)

		return (var_32_0.isUnlock() or var_32_0.activeAlways()) and not var_32_0.ifNeedHide()):
		local var_31_1 = getProxy(ChapterProxy).getChapterById(arg_31_1, True)
		local var_31_2 = cloneTplTo(arg_31_0.chapterTpl, arg_31_0.itemHolder, "Chapter_" .. var_31_1.id)

		arg_31_0.UpdateMapItem(var_31_2, var_31_1)

		arg_31_0.chapterTFsById[var_31_1.id] = var_31_2

		arg_31_0.PlayChapterItemAnimation(var_31_2)

def var_0_1.TryOpenChapter(arg_33_0, arg_33_1):
	local var_33_0 = arg_33_0.chapterTFsById[arg_33_1]

	if var_33_0:
		local var_33_1 = var_33_0.Find("main")

		triggerButton(var_33_1)

def var_0_1.UpdateStoryGroup(arg_34_0):
	local var_34_0 = arg_34_0.data.GetChapterInProgress().GetChapterStories()

	UIItemList.StaticAlign(arg_34_0.storyHolder, arg_34_0.storyTpl, #var_34_0, function(arg_35_0, arg_35_1, arg_35_2)
		if arg_35_0 != UIItemList.EventUpdate:
			return

		local var_35_0 = var_34_0[arg_35_1 + 1]

		arg_34_0.UpdateMapStory(arg_35_2, var_35_0)

		arg_35_2.name = "Chapter_" .. var_35_0.GetName())

def var_0_1.UpdateMapStory(arg_36_0, arg_36_1, arg_36_2):
	local var_36_0 = arg_36_2.GetPosition()

	setAnchoredPosition(arg_36_1, {
		x = arg_36_0.mapWidth * var_36_0[1],
		y = arg_36_0.mapHeight * var_36_0[2]
	})
	setText(arg_36_1.Find("Name"), arg_36_2.GetName())

	local var_36_1, var_36_2 = arg_36_2.GetIcon()

	arg_36_0.sceneParent.loader.GetSpriteQuiet(var_36_1, var_36_2, arg_36_1.Find("Icon"), True)

	local var_36_3 = arg_36_2.GetStoryName()

	onButton(arg_36_0, arg_36_1, function()
		pg.NewStoryMgr.GetInstance().Play(var_36_3, function()
			arg_36_0.sceneParent.RefreshMapBG()
			arg_36_0.UpdateMapItems()), SFX_PANEL)
	setActive(arg_36_1, not pg.NewStoryMgr.GetInstance().IsPlayed(var_36_3))

return var_0_1
