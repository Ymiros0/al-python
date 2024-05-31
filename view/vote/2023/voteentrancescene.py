local var_0_0 = class("VoteEntranceScene", import("view.base.BaseUI"))

var_0_0.MAIN_STAGE_CLOSE = 0
var_0_0.MAIN_STAGE_OPEN = 1
var_0_0.MAIN_STAGE_FINAL = 2
var_0_0.MAIN_STAGE_END = 3
var_0_0.SUB_STAGE_CLOSE = 0
var_0_0.SUB_STAGE_META = 1
var_0_0.SUB_STAGE_KID = 2
var_0_0.SUB_STAGE_SIREN = 3
var_0_0.EXCHANGE_STAGE_CLOSE = 0
var_0_0.EXCHANGE_STAGE_OPEN = 1
var_0_0.BILLBOARD_STAGE_NORMAL = 0
var_0_0.BILLBOARD_STAGE_FINAL = 1

def var_0_0.getUIName(arg_1_0):
	return "VoteEntranceUI"

def var_0_0.init(arg_2_0):
	arg_2_0.backBtn = arg_2_0.findTF("frame/back")
	arg_2_0.homeBtn = arg_2_0.findTF("frame/home")
	arg_2_0.helpBtn = arg_2_0.findTF("frame/help")
	arg_2_0.votesTr = arg_2_0.findTF("frame/votes")
	arg_2_0.votesTxt = arg_2_0.findTF("frame/votes/Text").GetComponent(typeof(Text))
	arg_2_0.scheduleTr = arg_2_0.findTF("frame/schedule")
	arg_2_0.scheduleTxt = arg_2_0.scheduleTr.Find("Text").GetComponent(typeof(Text))
	arg_2_0.scheduleImg = arg_2_0.scheduleTr.GetComponent(typeof(Image))
	arg_2_0.awardBtn = arg_2_0.findTF("frame/award")
	arg_2_0.mainTr = arg_2_0.findTF("bg/main").GetComponent(typeof(Image))
	arg_2_0.mainTip = arg_2_0.mainTr.gameObject.transform.Find("tip")
	arg_2_0.mainTitle = arg_2_0.mainTr.gameObject.transform.Find("title")
	arg_2_0.awardItem = arg_2_0.findTF("bg/main/item")
	arg_2_0.dropTr = arg_2_0.awardItem.Find("Award")
	arg_2_0.dropGetTr = arg_2_0.awardItem.Find("get")
	arg_2_0.dropGotTr = arg_2_0.awardItem.Find("got")
	arg_2_0.subTr = arg_2_0.findTF("bg/sub").GetComponent(typeof(Image))
	arg_2_0.subTip = arg_2_0.subTr.gameObject.transform.Find("tip")
	arg_2_0.subTitle = arg_2_0.subTr.gameObject.transform.Find("title")
	arg_2_0.exchangeTr = arg_2_0.findTF("bg/exchange").GetComponent(typeof(Image))
	arg_2_0.exchangeTip = arg_2_0.exchangeTr.gameObject.transform.Find("tip")
	arg_2_0.exchangeTitle = arg_2_0.exchangeTr.gameObject.transform.Find("title")
	arg_2_0.billboardTr = arg_2_0.findTF("bg/billboard").GetComponent(typeof(Image))
	arg_2_0.billboardTip = arg_2_0.billboardTr.gameObject.transform.Find("tip")
	arg_2_0.honorTr = arg_2_0.findTF("bg/honor").GetComponent(typeof(Image))
	arg_2_0.honorTip = arg_2_0.honorTr.gameObject.transform.Find("tip")
	arg_2_0.awardWindowPage = VoteAwardWindowPage.New(arg_2_0._tf, arg_2_0.event)

	VoteStoryUtil.Notify(VoteStoryUtil.ENTER_SCENE)

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.homeBtn, function()
		arg_3_0.emit(var_0_0.ON_HOME), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.vote_help_2023.tip
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.awardBtn, function()
		arg_3_0.awardWindowPage.ExecuteAction("Show"), SFX_PANEL)

	arg_3_0.voteActivity = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VOTE)

	arg_3_0.FlushAll()

def var_0_0.FlushAll(arg_8_0):
	arg_8_0.allPreheatStoriesPlayed = VoteStoryUtil.AllPreheatStoriesPlayed()

	arg_8_0.UpdateSchedule()
	arg_8_0.UpdateVotes()
	arg_8_0.UpdateMainEntrance()
	arg_8_0.UpdateSubEntrance()
	arg_8_0.UpdateExchangeEntrance()
	arg_8_0.UpdateBillboardEntrance()
	arg_8_0.UpdateHonorEntrance()

def var_0_0.UpdateSchedule(arg_9_0):
	if not arg_9_0.allPreheatStoriesPlayed:
		setActive(arg_9_0.scheduleTr, False)

		return

	local var_9_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup() or getProxy(VoteProxy).GetOpeningFunVoteGroup()

	setActive(arg_9_0.scheduleTr, var_9_0 != None)

	if var_9_0:
		arg_9_0.scheduleTxt.text = var_9_0.getConfig("name")

	local var_9_1 = "schedule_bg"

	if var_9_0 and var_9_0.isFinalsRace():
		var_9_1 = "schedule_bg_finals"
	elif var_9_0 and var_9_0.isResurrectionRace():
		var_9_1 = "schedule_bg_resurrection"
	elif var_9_0 and var_9_0.IsFunMetaRace():
		var_9_1 = "schedule_bg_meta"
	elif var_9_0 and var_9_0.IsFunSireRace():
		var_9_1 = "schedule_bg_sire"
	elif var_9_0 and var_9_0.IsFunKidRace():
		var_9_1 = "schedule_bg_kid"

	arg_9_0.scheduleImg.sprite = GetSpriteFromAtlas("ui/Vote2023MainUI_atlas", var_9_1)

def var_0_0.UpdateVotes(arg_10_0):
	if not arg_10_0.allPreheatStoriesPlayed:
		setActive(arg_10_0.votesTr, False)
		setActive(arg_10_0.awardBtn, False)

		return

	setActive(arg_10_0.awardBtn, not getProxy(VoteProxy).IsAllRaceEnd())

	local var_10_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup() or getProxy(VoteProxy).GetOpeningFunVoteGroup()

	setActive(arg_10_0.votesTr, var_10_0 != None)

	if var_10_0 and var_10_0.IsFunRace():
		arg_10_0.votesTxt.text = arg_10_0.GetSubVotes()
	else
		arg_10_0.votesTxt.text = arg_10_0.GetVotes()

def var_0_0.UpdateMainEntrance(arg_11_0):
	local var_11_0 = arg_11_0.GetMainStageState()
	local var_11_1 = GetSpriteFromAtlas("ui/Vote2023MainUI_atlas", "icon_main_" .. var_11_0)

	arg_11_0.mainTr.sprite = var_11_1

	onButton(arg_11_0, arg_11_0.mainTr.gameObject, function()
		local var_12_0 = arg_11_0.ShouldPlayMainStory()

		VoteStoryUtil.Notify(VoteStoryUtil.ENTER_MAIN_STAGE)

		if var_12_0:
			return

		if not arg_11_0.CheckPreheatStories():
			return

		arg_11_0.MarkMainRaceNonNew()

		if arg_11_0.ExistMainStageAward():
			arg_11_0.emit(VoteEntranceMediator.SUBMIT_TASK)

			return

		arg_11_0.emit(VoteEntranceMediator.ON_VOTE), SFX_PANEL)
	arg_11_0.UpdateMainAward()

	local var_11_2 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()
	local var_11_3 = var_11_2 and var_11_2.IsOpening() or arg_11_0.ExistMainStageAward() or arg_11_0.ShouldPlayMainStory()

	setGray(arg_11_0.mainTitle, not var_11_3, True)
	arg_11_0.UpdateMainStageTip()

def var_0_0.UpdateMainAward(arg_13_0):
	local var_13_0 = arg_13_0.GetMainStageState() == var_0_0.MAIN_STAGE_END
	local var_13_1 = False

	if var_13_0:
		local var_13_2 = getProxy(ActivityProxy).getActivityById(ActivityConst.VOTE_ENTRANCE_ACT_ID).getConfig("config_client")[2] or -1
		local var_13_3 = pg.task_data_template[var_13_2].award_display

		updateDrop(arg_13_0.dropTr, {
			type = var_13_3[1][1],
			id = var_13_3[1][2],
			count = var_13_3[1][3]
		})

		local var_13_4 = getProxy(TaskProxy).getTaskById(var_13_2) or getProxy(TaskProxy).getFinishTaskById(var_13_2)

		var_13_1 = var_13_4 and var_13_4.isFinish()

		setActive(arg_13_0.dropGetTr, var_13_4 and var_13_4.isFinish() and not var_13_4.isReceive())
		setActive(arg_13_0.dropGotTr, var_13_4 and var_13_4.isFinish() and var_13_4.isReceive())

	setActive(arg_13_0.awardItem, var_13_0 and var_13_1)

def var_0_0.UpdateMainStageTip(arg_14_0):
	setActive(arg_14_0.mainTip, arg_14_0.ShouldTipMainStage())

def var_0_0.UpdateSubEntrance(arg_15_0):
	local var_15_0 = arg_15_0.GetSubStageState()
	local var_15_1 = GetSpriteFromAtlas("ui/Vote2023MainUI_atlas", "icon_sub_" .. var_15_0)

	arg_15_0.subTr.sprite = var_15_1

	arg_15_0.UpdateSubStageTip()
	onButton(arg_15_0, arg_15_0.subTr.gameObject, function()
		local var_16_0 = arg_15_0.ShouldPlaySubStory()

		VoteStoryUtil.Notify(VoteStoryUtil.ENTER_SUB_STAGE)

		if var_16_0:
			return

		if not arg_15_0.CheckPreheatStories():
			return

		arg_15_0.MarkSubRaceNonNew()
		arg_15_0.emit(VoteEntranceMediator.ON_FUN_VOTE), SFX_PANEL)

	local var_15_2 = getProxy(VoteProxy).GetOpeningFunVoteGroup()
	local var_15_3 = var_15_2 and var_15_2.IsOpening() or arg_15_0.ShouldPlaySubStory()

	setGray(arg_15_0.subTitle, not var_15_3, True)

def var_0_0.UpdateSubStageTip(arg_17_0):
	setActive(arg_17_0.subTip, arg_17_0.ShouldTipSubStage())

def var_0_0.UpdateExchangeEntrance(arg_18_0):
	local var_18_0 = arg_18_0.GetExchangeState()
	local var_18_1 = GetSpriteFromAtlas("ui/Vote2023MainUI_atlas", "icon_exchange_" .. var_18_0)

	arg_18_0.exchangeTr.sprite = var_18_1

	arg_18_0.UpdateExchangeTip()
	onButton(arg_18_0, arg_18_0.exchangeTr.gameObject, function()
		local var_19_0 = arg_18_0.ShouldPlayExchangeStory()

		VoteStoryUtil.Notify(VoteStoryUtil.ENTER_EXCHANGE)

		if var_19_0:
			return

		if not arg_18_0.CheckPreheatStories():
			return

		if getProxy(PlayerProxy).getRawData().level < 25:
			pg.TipsMgr.GetInstance().ShowTips(i18n("vote_tip_level_limit"))

			return

		arg_18_0.emit(VoteEntranceMediator.ON_EXCHANGE), SFX_PANEL)

	local var_18_2 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()
	local var_18_3 = var_18_2 and var_18_2.IsOpening() or arg_18_0.ShouldPlayExchangeStory()

	setGray(arg_18_0.exchangeTitle, not var_18_3, True)

def var_0_0.UpdateExchangeTip(arg_20_0):
	setActive(arg_20_0.exchangeTip, arg_20_0.ShouldTipExchange())

def var_0_0.UpdateBillboardEntrance(arg_21_0):
	local var_21_0 = arg_21_0.GetBillboardState()
	local var_21_1 = GetSpriteFromAtlas("ui/Vote2023MainUI_atlas", "icon_billboard_" .. var_21_0)

	arg_21_0.billboardTr.sprite = var_21_1

	arg_21_0.UpdateBillboardTip()
	onButton(arg_21_0, arg_21_0.billboardTr.gameObject, function()
		local var_22_0 = arg_21_0.ShouldPlayBillboardStory()

		VoteStoryUtil.Notify(VoteStoryUtil.ENTER_SCHEDULE)

		if var_22_0:
			return

		if not arg_21_0.CheckPreheatStories():
			return

		arg_21_0.emit(VoteEntranceMediator.ON_SCHEDULE), SFX_PANEL)

def var_0_0.UpdateBillboardTip(arg_23_0):
	setActive(arg_23_0.billboardTip, arg_23_0.ShouldTipBillboard())

def var_0_0.UpdateHonorEntrance(arg_24_0):
	arg_24_0.UpdateHonorTip()
	onButton(arg_24_0, arg_24_0.honorTr.gameObject, function()
		local var_25_0 = arg_24_0.ShouldPlayHonorStory()

		VoteStoryUtil.Notify(VoteStoryUtil.ENTER_HALL)

		if var_25_0:
			return

		if not arg_24_0.CheckPreheatStories():
			return

		arg_24_0.emit(VoteEntranceMediator.GO_HALL), SFX_PANEL)

def var_0_0.UpdateHonorTip(arg_26_0):
	setActive(arg_26_0.honorTip, arg_26_0.ShouldTipHonor())

def var_0_0.onBackPressed(arg_27_0):
	if arg_27_0.awardWindowPage and arg_27_0.awardWindowPage.GetLoaded() and arg_27_0.awardWindowPage.isShowing():
		arg_27_0.awardWindowPage.Hide()

		return

	var_0_0.super.onBackPressed(arg_27_0)

def var_0_0.willExit(arg_28_0):
	if arg_28_0.awardWindowPage:
		arg_28_0.awardWindowPage.Destroy()

		arg_28_0.awardWindowPage = None

def var_0_0.ExistMainStageAward(arg_29_0):
	local var_29_0 = getProxy(TaskProxy)
	local var_29_1 = getProxy(ActivityProxy).getActivityById(ActivityConst.VOTE_ENTRANCE_ACT_ID)

	if not var_29_1 or var_29_1.isEnd():
		return False

	local var_29_2 = var_29_1.getConfig("config_client")[2] or -1
	local var_29_3 = var_29_0.getTaskById(var_29_2) or var_29_0.getFinishTaskById(var_29_2)

	return var_29_3 and var_29_3.isFinish() and not var_29_3.isReceive()

def var_0_0.GetMainStageState(arg_30_0):
	if not arg_30_0.allPreheatStoriesPlayed:
		return var_0_0.MAIN_STAGE_CLOSE

	local var_30_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()
	local var_30_1 = not var_30_0

	if getProxy(VoteProxy).IsAllRaceEnd():
		return var_0_0.MAIN_STAGE_END
	elif var_30_0:
		if var_30_0.isFinalsRace():
			return var_0_0.MAIN_STAGE_FINAL
		else
			return var_0_0.MAIN_STAGE_OPEN
	else
		return var_0_0.MAIN_STAGE_CLOSE

def var_0_0.ShouldTipMainStage(arg_31_0):
	if not arg_31_0.allPreheatStoriesPlayed:
		return arg_31_0.ShouldPlayMainStory()
	else
		return arg_31_0.GetVotes() > 0 or arg_31_0.IsNewMainRace() or arg_31_0.ShouldPlayMainStory() or isActive(arg_31_0.dropGetTr)

def var_0_0.ShouldPlayMainStory(arg_32_0):
	local var_32_0 = VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_MAIN_STAGE)

	return arg_32_0.voteActivity and not arg_32_0.voteActivity.isEnd() and not pg.NewStoryMgr.GetInstance().IsPlayed(var_32_0)

def var_0_0.IsNewMainRace(arg_33_0):
	local var_33_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()

	return getProxy(VoteProxy).IsNewRace(var_33_0)

def var_0_0.MarkMainRaceNonNew(arg_34_0):
	local var_34_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()

	getProxy(VoteProxy).MarkRaceNonNew(var_34_0)

def var_0_0.GetSubStageState(arg_35_0):
	if not arg_35_0.allPreheatStoriesPlayed:
		return var_0_0.SUB_STAGE_CLOSE

	local var_35_0 = getProxy(VoteProxy).GetOpeningFunVoteGroup()

	if var_35_0:
		if var_35_0.IsFunSireRace():
			return var_0_0.SUB_STAGE_SIREN
		elif var_35_0.IsFunMetaRace():
			return var_0_0.SUB_STAGE_META
		elif var_35_0.IsFunKidRace():
			return var_0_0.SUB_STAGE_KID
		else
			assert(False)
	else
		return var_0_0.SUB_STAGE_CLOSE

def var_0_0.ShouldTipSubStage(arg_36_0):
	if not arg_36_0.allPreheatStoriesPlayed:
		return arg_36_0.ShouldPlaySubStory()
	else
		return arg_36_0.GetSubVotes() > 0 or arg_36_0.IsNewSubRace() or arg_36_0.ShouldPlaySubStory()

def var_0_0.ShouldPlaySubStory(arg_37_0):
	local var_37_0 = VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_SUB_STAGE)

	return arg_37_0.voteActivity and not arg_37_0.voteActivity.isEnd() and not pg.NewStoryMgr.GetInstance().IsPlayed(var_37_0)

def var_0_0.IsNewSubRace(arg_38_0):
	local var_38_0 = getProxy(VoteProxy).GetOpeningFunVoteGroup()

	return getProxy(VoteProxy).IsNewRace(var_38_0)

def var_0_0.MarkSubRaceNonNew(arg_39_0):
	local var_39_0 = getProxy(VoteProxy).GetOpeningFunVoteGroup()

	getProxy(VoteProxy).MarkRaceNonNew(var_39_0)

def var_0_0.GetExchangeState(arg_40_0):
	if not arg_40_0.allPreheatStoriesPlayed:
		return var_0_0.EXCHANGE_STAGE_CLOSE

	if getProxy(VoteProxy).GetOpeningNonFunVoteGroup():
		return var_0_0.EXCHANGE_STAGE_OPEN
	else
		return var_0_0.EXCHANGE_STAGE_CLOSE

def var_0_0.ShouldTipExchange(arg_41_0):
	return arg_41_0.ShouldPlayExchangeStory()

def var_0_0.ShouldPlayExchangeStory(arg_42_0):
	local var_42_0 = VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_EXCHANGE)

	return arg_42_0.voteActivity and not arg_42_0.voteActivity.isEnd() and not pg.NewStoryMgr.GetInstance().IsPlayed(var_42_0)

def var_0_0.GetBillboardState(arg_43_0):
	if not arg_43_0.allPreheatStoriesPlayed:
		return var_0_0.BILLBOARD_STAGE_NORMAL

	local var_43_0 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()

	if var_43_0 and var_43_0.isFinalsRace():
		return var_0_0.BILLBOARD_STAGE_FINAL
	else
		return var_0_0.BILLBOARD_STAGE_NORMAL

def var_0_0.ShouldTipBillboard(arg_44_0):
	return arg_44_0.ShouldPlayBillboardStory()

def var_0_0.ShouldPlayBillboardStory(arg_45_0):
	local var_45_0 = VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_SCHEDULE)

	return arg_45_0.voteActivity and not arg_45_0.voteActivity.isEnd() and not pg.NewStoryMgr.GetInstance().IsPlayed(var_45_0)

def var_0_0.ShouldTipHonor(arg_46_0):
	if not arg_46_0.allPreheatStoriesPlayed:
		return arg_46_0.ShouldPlayHonorStory()
	else
		return getProxy(VoteProxy).ExistPastVoteAward() or arg_46_0.ShouldPlayHonorStory()

def var_0_0.ShouldPlayHonorStory(arg_47_0):
	local var_47_0 = VoteStoryUtil.GetStoryNameByType(VoteStoryUtil.ENTER_HALL)

	return arg_47_0.voteActivity and not arg_47_0.voteActivity.isEnd() and not pg.NewStoryMgr.GetInstance().IsPlayed(var_47_0)

def var_0_0.GetVotes(arg_48_0):
	local var_48_0 = arg_48_0.GetMainStageState()

	if var_48_0 == var_0_0.MAIN_STAGE_OPEN or var_48_0 == var_0_0.MAIN_STAGE_FINAL:
		local var_48_1 = getProxy(VoteProxy).GetOpeningNonFunVoteGroup()

		return var_48_1 and getProxy(VoteProxy).GetVotesByConfigId(var_48_1.configId) or 0

	return 0

def var_0_0.GetSubVotes(arg_49_0):
	if var_0_0.SUB_STAGE_CLOSE != arg_49_0.GetSubStageState():
		local var_49_0 = getProxy(VoteProxy).GetOpeningFunVoteGroup()

		return var_49_0 and getProxy(VoteProxy).GetVotesByConfigId(var_49_0.configId) or 0
	else
		return 0

def var_0_0.CheckPreheatStories(arg_50_0):
	if not arg_50_0.allPreheatStoriesPlayed:
		pg.NewGuideMgr.GetInstance().Play("NG0043")

		return False

	return True

return var_0_0
