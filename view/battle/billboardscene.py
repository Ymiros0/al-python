local var_0_0 = class("BillboardScene", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "BillboardUI"

def var_0_0.updateRankList(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	if not arg_2_0.rankVOs:
		arg_2_0.rankVOs = {}

	if not arg_2_0.playerRankVOs:
		arg_2_0.playerRankVOs = {}

	arg_2_0.rankVOs[arg_2_1] = arg_2_2

	if not arg_2_0.ptRanks:
		arg_2_0.ptRanks = {}

	if arg_2_1 == PowerRank.TYPE_PT:
		assert(arg_2_4)

		arg_2_0.ptRanks[arg_2_4] = arg_2_2
		arg_2_0.playerPTRankVOMap = arg_2_0.playerPTRankVOMap or {}
		arg_2_0.playerPTRankVOMap[arg_2_4] = arg_2_3

	arg_2_0.playerRankVOs[arg_2_1] = arg_2_3

def var_0_0.init(arg_3_0):
	arg_3_0.blurPanel = arg_3_0.findTF("blur_panel")
	arg_3_0.rankRect = arg_3_0.findTF("main/frame/ranks").GetComponent("LScrollRect")
	arg_3_0.playerRankTF = arg_3_0.findTF("main/frame/player_rank")

	setActive(arg_3_0.playerRankTF, False)

	arg_3_0.topPanel = arg_3_0.findTF("adapt/top", arg_3_0.blurPanel)
	arg_3_0.leftPanel = arg_3_0.findTF("adapt/left_length", arg_3_0.blurPanel)
	arg_3_0.mainPanel = arg_3_0.findTF("main")
	arg_3_0.extraChapterBg = arg_3_0.findTF("extra_chapter_bg")
	arg_3_0.toggleScrollRect = arg_3_0.findTF("frame/scroll_rect", arg_3_0.leftPanel)
	arg_3_0.toggleContainer = arg_3_0.findTF("frame/scroll_rect/tagRoot", arg_3_0.leftPanel)
	arg_3_0.listEmptyTF = arg_3_0.findTF("main/frame/empty")

	setActive(arg_3_0.listEmptyTF, False)

	arg_3_0.listEmptyTxt = arg_3_0.findTF("Text", arg_3_0.listEmptyTF)

	setText(arg_3_0.listEmptyTxt, i18n("list_empty_tip_billboardui"))

	arg_3_0.toggles = {
		arg_3_0.findTF("frame/scroll_rect/tagRoot/power", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/collection", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/pt", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/pledge", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/chanllenge", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/extra_chapter", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/boss_battle", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/guild", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/military", arg_3_0.leftPanel),
		arg_3_0.findTF("frame/scroll_rect/tagRoot/bossrush", arg_3_0.leftPanel)
	}
	arg_3_0.ptToggles = {}

	local var_3_0 = _.filter(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PT_RANK), function(arg_4_0)
		return not arg_4_0.isEnd() and tonumber(arg_4_0.getConfig("config_data")) > 0)

	if #var_3_0 > 1:
		local var_3_1 = arg_3_0.toggles[3]

		for iter_3_0, iter_3_1 in pairs(var_3_0):
			local var_3_2 = cloneTplTo(var_3_1, var_3_1.parent)

			arg_3_0.ptToggles[iter_3_1.id] = var_3_2

		arg_3_0.toggles[3] = None

	arg_3_0.updateToggles()

	arg_3_0.rankRect.decelerationRate = 0.07

	local var_3_3 = arg_3_0.contextData.page or PowerRank.TYPE_POWER

	if var_3_3 == PowerRank.TYPE_EXTRA_CHAPTER:
		setActive(arg_3_0.leftPanel, False)
		setAnchoredPosition(arg_3_0.mainPanel, Vector2(0, -35.5))

		local var_3_4 = GetSpriteFromAtlas("commonbg/bg_fengshan", "")

		setImageSprite(arg_3_0.extraChapterBg, var_3_4)

	setActive(arg_3_0.extraChapterBg, var_3_3 == PowerRank.TYPE_EXTRA_CHAPTER)

def var_0_0.updateToggles(arg_5_0):
	for iter_5_0, iter_5_1 in pairs(arg_5_0.toggles):
		local var_5_0

		if PowerRank.typeInfo[iter_5_0].act_type:
			var_5_0 = PowerRank.getActivityByRankType(iter_5_0)
		else
			var_5_0 = (iter_5_0 != PowerRank.TYPE_PLEDGE or False) and (iter_5_0 == PowerRank.TYPE_GUILD_BATTLE and True or True)

		setActive(iter_5_1, var_5_0)

	for iter_5_2, iter_5_3 in pairs(arg_5_0.ptToggles):
		local var_5_1 = getProxy(ActivityProxy).getActivityById(iter_5_2)

		setActive(iter_5_3, var_5_1 and not var_5_1.isEnd())

	setActive(arg_5_0.toggleContainer, True)
	Canvas.ForceUpdateCanvases()

	local var_5_2 = arg_5_0.toggleScrollRect.rect.height < arg_5_0.toggleContainer.rect.height

	arg_5_0.toggleContainer.GetComponent(typeof(ScrollRect)).enabled = var_5_2

def var_0_0.didEnter(arg_6_0):
	onButton(arg_6_0, arg_6_0.findTF("back_btn", arg_6_0.topPanel), function()
		arg_6_0.emit(var_0_0.ON_BACK), SFX_CANCEL)

	for iter_6_0, iter_6_1 in pairs(arg_6_0.toggles):
		onToggle(arg_6_0, iter_6_1, function(arg_8_0)
			if iter_6_0 == PowerRank.TYPE_GUILD_BATTLE:
				setActive(arg_6_0.mainPanel, not arg_8_0)
				arg_6_0.emit(BillboardMediator.ON_GUILD_RANK, arg_8_0)

				return

			if arg_8_0:
				local var_8_0 = checkExist(PowerRank.getActivityByRankType(iter_6_0), {
					"id"
				})

				arg_6_0.switchPage(iter_6_0, var_8_0), SFX_PANEL)

	for iter_6_2, iter_6_3 in pairs(arg_6_0.ptToggles):
		onToggle(arg_6_0, iter_6_3, function(arg_9_0)
			if arg_9_0:
				arg_6_0.switchPage(PowerRank.TYPE_PT, iter_6_2), SFX_PANEL)

	arg_6_0.cards = {}

	function arg_6_0.rankRect.onInitItem(arg_10_0)
		arg_6_0.onInintItem(arg_10_0)

	function arg_6_0.rankRect.onUpdateItem(arg_11_0, arg_11_1)
		arg_6_0.onUpdateItem(arg_11_0, arg_11_1, arg_6_0.curPagePTActID)

	function arg_6_0.rankRect.onReturnItem(arg_12_0, arg_12_1)
		arg_6_0.onReturnItem(arg_12_0, arg_12_1)

	arg_6_0.playerCard = RankCard.New(arg_6_0.playerRankTF, RankCard.TYPE_SELF)

	local var_6_0 = arg_6_0.contextData.page or PowerRank.TYPE_POWER

	triggerToggle(arg_6_0.toggles[var_6_0], True)

def var_0_0.onInintItem(arg_13_0, arg_13_1):
	local var_13_0 = RankCard.New(arg_13_1, RankCard.TYPE_OTHER)

	onButton(arg_13_0, var_13_0._tf, function()
		if var_13_0.rankVO.type == PowerRank.TYPE_MILITARY_RANK:
			arg_13_0.emit(BillboardMediator.OPEN_RIVAL_INFO, var_13_0.rankVO.id))

	arg_13_0.cards[arg_13_1] = var_13_0

def var_0_0.onUpdateItem(arg_15_0, arg_15_1, arg_15_2, arg_15_3):
	local var_15_0 = arg_15_0.cards[arg_15_2]

	if not var_15_0:
		arg_15_0.onInintItem(arg_15_2)

		var_15_0 = arg_15_0.cards[arg_15_2]

	local var_15_1 = arg_15_0.displayRankVOs[arg_15_1 + 1]

	var_15_0.update(var_15_1, arg_15_3)

def var_0_0.onReturnItem(arg_16_0, arg_16_1, arg_16_2):
	if arg_16_0.exited:
		return

	local var_16_0 = arg_16_0.cards[arg_16_2]

	if var_16_0:
		var_16_0.clear()

def var_0_0.filter(arg_17_0, arg_17_1, arg_17_2):
	if arg_17_1 != arg_17_0.page:
		return

	local var_17_0 = arg_17_0.page
	local var_17_1

	if PowerRank.TYPE_PT == arg_17_1:
		assert(arg_17_2)

		var_17_1 = arg_17_0.ptRanks[arg_17_2]
	else
		var_17_1 = arg_17_0.rankVOs[var_17_0]

	arg_17_0.displayRankVOs = {}

	for iter_17_0, iter_17_1 in ipairs(var_17_1):
		table.insert(arg_17_0.displayRankVOs, iter_17_1)

	arg_17_0.rankRect.SetTotalCount(#arg_17_0.displayRankVOs)
	setActive(arg_17_0.listEmptyTF, #arg_17_0.displayRankVOs <= 0)

	local var_17_2 = arg_17_0.playerRankVOs[arg_17_0.page]

	if PowerRank.TYPE_PT == arg_17_1:
		local var_17_3 = arg_17_0.playerPTRankVOMap[arg_17_2]

		arg_17_0.playerCard.update(var_17_3, arg_17_2)
	else
		arg_17_0.playerCard.update(var_17_2, arg_17_2)

def var_0_0.switchPage(arg_18_0, arg_18_1, arg_18_2):
	if arg_18_0.page == arg_18_1 and arg_18_1 != PowerRank.TYPE_PT:
		return

	if arg_18_1 == PowerRank.TYPE_PT:
		arg_18_0.curPagePTActID = arg_18_2
	else
		arg_18_0.curPagePTActID = None

	arg_18_0.page = arg_18_1

	local var_18_0

	if arg_18_0.page == PowerRank.TYPE_PT:
		assert(arg_18_2)

		var_18_0 = arg_18_0.ptRanks[arg_18_2]
	else
		var_18_0 = arg_18_0.rankVOs[arg_18_1]

	if not var_18_0:
		arg_18_0.rankRect.SetTotalCount(0)
		arg_18_0.playerCard.clear()
		arg_18_0.emit(BillboardMediator.FETCH_RANKS, arg_18_0.page, arg_18_2)
	else
		arg_18_0.filter(arg_18_0.page, arg_18_2)

	setActive(arg_18_0.findTF("tip", arg_18_0.topPanel), not table.contains(BillboardProxy.NONTIMER, arg_18_0.page))
	arg_18_0.updateScoreTitle(arg_18_0.page, arg_18_2)

def var_0_0.updateScoreTitle(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0 = arg_19_0.findTF("main/frame/title")
	local var_19_1 = PowerRank.getTitleWord(arg_19_1, arg_19_2)

	for iter_19_0 = 1, 4:
		setText(var_19_0.GetChild(iter_19_0 - 1), var_19_1[iter_19_0])

def var_0_0.willExit(arg_20_0):
	for iter_20_0, iter_20_1 in ipairs(arg_20_0.cards):
		iter_20_1.dispose()

	arg_20_0.playerCard.dispose()

	if arg_20_0.name:
		retPaintingPrefab(arg_20_0.paintingTF, arg_20_0.name)

return var_0_0
