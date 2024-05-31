local var_0_0 = class("BattleResultLayer", import("..base.BaseUI"))

var_0_0.DURATION_MOVE = 0.35
var_0_0.DURATION_WIN_SCALE = 0.4
var_0_0.CONDITIONS_FREQUENCE = 0.15
var_0_0.STATE_RANK_ANIMA = "rankAnima"
var_0_0.STATE_REPORT = "report"
var_0_0.STATE_REPORTED = "reported"
var_0_0.STATE_REWARD = "reward"
var_0_0.STATE_DISPLAY = "display"
var_0_0.STATE_DISPLAYED = "displayed"
var_0_0.STATE_SUB_DISPLAY = "subDisplay"
var_0_0.STATE_SUB_DISPLAYED = "subDisplayed"
var_0_0.ObjectiveList = {
	"battle_result_victory",
	"battle_result_undefeated",
	"battle_result_sink_limit",
	"battle_preCombatLayer_time_hold",
	"battle_result_time_limit",
	"battle_result_boss_destruct",
	"battle_preCombatLayer_damage_before_end",
	"battle_result_defeat_all_enemys"
}

def var_0_0.getUIName(arg_1_0):
	return "BattleResultUI"

def var_0_0.setRivalVO(arg_2_0, arg_2_1):
	arg_2_0.rivalVO = arg_2_1

def var_0_0.setRank(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.player = arg_3_1
	arg_3_0.season = arg_3_2

	setText(arg_3_0._playerName, "<color=#FFFFFF>" .. arg_3_0.player.name .. "</color><size=32> / C O M M A N D E R</size>")

	local var_3_0 = SeasonInfo.getMilitaryRank(arg_3_2.score, arg_3_2.rank)
	local var_3_1, var_3_2 = SeasonInfo.getNextMilitaryRank(arg_3_2.score, arg_3_2.rank)

	setText(arg_3_0._playerLv, var_3_0.name)
	setText(arg_3_0._playerExpLabel, i18n("word_rankScore"))

	arg_3_0._playerExpProgress.GetComponent(typeof(Image)).fillAmount = arg_3_2.score / var_3_2

	setText(arg_3_0._playerBonusExp, "+0")

	arg_3_0.calcPlayerProgress = arg_3_0.calcPlayerRank

def var_0_0.setShips(arg_4_0, arg_4_1):
	arg_4_0.shipVOs = arg_4_1

def var_0_0.setPlayer(arg_5_0, arg_5_1):
	arg_5_0.player = arg_5_1

	setText(arg_5_0._playerName, "<color=#FFFFFF>" .. arg_5_0.player.name .. "</color><size=32> / C O M M A N D E R</size>")
	setText(arg_5_0._playerLv, "Lv." .. arg_5_0.player.level)

	local var_5_0 = getConfigFromLevel1(pg.user_level, arg_5_0.player.level)

	arg_5_0._playerExpProgress.GetComponent(typeof(Image)).fillAmount = arg_5_0.player.exp / var_5_0.exp_interval

	if arg_5_0.player.level == pg.user_level[#pg.user_level].level:
		arg_5_0._playerExpProgress.GetComponent(typeof(Image)).fillAmount = 1

	setText(arg_5_0._playerBonusExp, "+0")

	arg_5_0.calcPlayerProgress = arg_5_0.calcPlayerExp

	local var_5_1 = arg_5_0.contextData.extraBuffList

	for iter_5_0, iter_5_1 in ipairs(var_5_1):
		if pg.benefit_buff_template[iter_5_1].benefit_type == Chapter.OPERATION_BUFF_TYPE_EXP:
			setActive(arg_5_0._playerExpExtra, True)

def var_0_0.setExpBuff(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.expBuff = arg_6_1
	arg_6_0.shipBuff = arg_6_2

def var_0_0.init(arg_7_0):
	arg_7_0._grade = arg_7_0.findTF("grade")
	arg_7_0._levelText = arg_7_0.findTF("chapterName/Text22", arg_7_0._grade)
	arg_7_0.clearFX = arg_7_0.findTF("clear")
	arg_7_0._main = arg_7_0.findTF("main")
	arg_7_0._blurConatiner = arg_7_0.findTF("blur_container")
	arg_7_0._bg = arg_7_0.findTF("main/jiesuanbeijing")
	arg_7_0._painting = arg_7_0.findTF("painting", arg_7_0._blurConatiner)
	arg_7_0._failPainting = arg_7_0.findTF("fail", arg_7_0._painting)
	arg_7_0._chat = arg_7_0.findTF("chat", arg_7_0._painting)
	arg_7_0._leftPanel = arg_7_0.findTF("leftPanel", arg_7_0._main)
	arg_7_0._expResult = arg_7_0.findTF("expResult", arg_7_0._leftPanel)
	arg_7_0._expContainer = arg_7_0.findTF("expContainer", arg_7_0._expResult)
	arg_7_0._extpl = arg_7_0.getTpl("ShipCardTpl", arg_7_0._expContainer)
	arg_7_0._playerExp = arg_7_0.findTF("playerExp", arg_7_0._leftPanel)
	arg_7_0._playerName = arg_7_0.findTF("name_text", arg_7_0._playerExp)
	arg_7_0._playerLv = arg_7_0.findTF("lv_text", arg_7_0._playerExp)
	arg_7_0._playerExpLabel = arg_7_0.findTF("exp_label", arg_7_0._playerExp)
	arg_7_0._playerExpProgress = arg_7_0.findTF("exp_progress", arg_7_0._playerExp)
	arg_7_0._playerBonusExp = arg_7_0.findTF("exp_text", arg_7_0._playerExp)
	arg_7_0._playerExpExtra = arg_7_0.findTF("operation_bonus", arg_7_0._playerExp)
	arg_7_0._atkBG = arg_7_0.findTF("atkPanel", arg_7_0._blurConatiner)
	arg_7_0._atkPanel = arg_7_0.findTF("atkResult", arg_7_0._atkBG)
	arg_7_0._atkResult = arg_7_0.findTF("atkResult/result", arg_7_0._atkBG)
	arg_7_0._atkContainer = arg_7_0.findTF("Grid", arg_7_0._atkResult)
	arg_7_0._atkContainerNext = arg_7_0.findTF("Grid_next", arg_7_0._atkResult)
	arg_7_0._atkToggle = arg_7_0.findTF("switchAtk", arg_7_0._atkPanel)
	arg_7_0._atkTpl = arg_7_0.getTpl("resulttpl", arg_7_0._atkResult)
	arg_7_0._mvpFX = arg_7_0.findTF("mvpFX", arg_7_0._atkPanel)
	arg_7_0._rightBottomPanel = arg_7_0.findTF("rightBottomPanel", arg_7_0._blurConatiner)
	arg_7_0._confirmBtn = arg_7_0.findTF("confirmBtn", arg_7_0._rightBottomPanel)

	setText(arg_7_0._confirmBtn.Find("Text"), i18n("text_confirm"))

	arg_7_0._statisticsBtn = arg_7_0.findTF("statisticsBtn", arg_7_0._rightBottomPanel)
	arg_7_0._subExpResult = arg_7_0.findTF("subExpResult", arg_7_0._leftPanel)
	arg_7_0._subExpContainer = arg_7_0.findTF("expContainer", arg_7_0._subExpResult)
	arg_7_0._subToggle = arg_7_0.findTF("switchFleet", arg_7_0._leftPanel)

	setActive(arg_7_0._subToggle, False)

	arg_7_0._skipBtn = arg_7_0.findTF("skipLayer", arg_7_0._tf)
	arg_7_0.UIMain = pg.UIMgr.GetInstance().UIMain
	arg_7_0.overlay = pg.UIMgr.GetInstance().OverlayMain
	arg_7_0._conditions = arg_7_0.findTF("main/conditions")
	arg_7_0._conditionContainer = arg_7_0.findTF("bg16/list", arg_7_0._conditions)
	arg_7_0._conditionTpl = arg_7_0.findTF("bg16/conditionTpl", arg_7_0._conditions)
	arg_7_0._conditionSubTpl = arg_7_0.findTF("bg16/conditionSubTpl", arg_7_0._conditions)
	arg_7_0._conditionContributeTpl = arg_7_0.findTF("bg16/conditionContributeTpl", arg_7_0._conditions)
	arg_7_0._conditionBGNormal = arg_7_0.findTF("bg16/bg_normal", arg_7_0._conditions)
	arg_7_0._conditionBGContribute = arg_7_0.findTF("bg16/bg_contribute", arg_7_0._conditions)
	arg_7_0._cmdExp = arg_7_0.findTF("commanderExp", arg_7_0._leftPanel)
	arg_7_0._cmdContainer = arg_7_0.findTF("commander_container", arg_7_0._cmdExp)
	arg_7_0._cmdTpl = arg_7_0.findTF("commander_tpl", arg_7_0._cmdExp)

	arg_7_0.setGradeLabel()
	SetActive(arg_7_0._levelText, False)

	arg_7_0._delayLeanList = {}
	arg_7_0._ratioFitter = GetComponent(arg_7_0._tf, typeof(AspectRatioFitter))
	arg_7_0._ratioFitter.enabled = True
	arg_7_0._ratioFitter.aspectRatio = pg.CameraFixMgr.GetInstance().targetRatio
	arg_7_0.camEventId = pg.CameraFixMgr.GetInstance().bind(pg.CameraFixMgr.ASPECT_RATIO_UPDATE, function(arg_8_0, arg_8_1)
		arg_7_0._ratioFitter.aspectRatio = arg_8_1)

def var_0_0.customsLang(arg_9_0):
	setText(findTF(arg_9_0._confirmBtn, "Text"), i18n("battle_result_confirm"))
	setText(findTF(arg_9_0._bg, "jieuan01/tips/dianjijixu/bg20"), i18n("battle_result_continue"))
	setText(findTF(arg_9_0._atkTpl, "result/dmg_count_label"), i18n("battle_result_dmg"))
	setText(findTF(arg_9_0._atkTpl, "result/kill_count_label"), i18n("battle_result_kill_count"))
	setText(findTF(arg_9_0._subToggle, "on"), i18n("battle_result_toggle_on"))
	setText(findTF(arg_9_0._subToggle, "off"), i18n("battle_result_toggle_off"))
	setText(findTF(arg_9_0._conditions, "bg17"), i18n("battle_result_targets"))

def var_0_0.setGradeLabel(arg_10_0):
	local var_10_0 = {
		"d",
		"c",
		"b",
		"a",
		"s"
	}
	local var_10_1 = arg_10_0.findTF("grade/Xyz/bg13")
	local var_10_2 = arg_10_0.findTF("grade/Xyz/bg14")
	local var_10_3
	local var_10_4
	local var_10_5
	local var_10_6 = arg_10_0.contextData.score
	local var_10_7
	local var_10_8 = var_10_6 > 0

	setActive(arg_10_0.findTF("jieuan01/BG/bg_victory", arg_10_0._bg), var_10_8)
	setActive(arg_10_0.findTF("jieuan01/BG/bg_fail", arg_10_0._bg), not var_10_8)

	if var_10_8:
		var_10_5 = var_10_0[var_10_6 + 1]
		var_10_3 = "battlescore/battle_score_" .. var_10_5 .. "/letter_" .. var_10_5
		var_10_4 = "battlescore/battle_score_" .. var_10_5 .. "/label_" .. var_10_5
	else
		if arg_10_0.contextData.statistics._scoreMark == ys.Battle.BattleConst.DEAD_FLAG:
			var_10_5 = var_10_0[2]
			var_10_7 = "flag_destroy"
		else
			var_10_5 = var_10_0[1]

		var_10_3 = "battlescore/battle_score_" .. var_10_5 .. "/letter_" .. var_10_5
		var_10_4 = "battlescore/battle_score_" .. var_10_5 .. "/label_" .. (var_10_7 or var_10_5)

	LoadImageSpriteAsync(var_10_3, var_10_1, False)
	LoadImageSpriteAsync(var_10_4, var_10_2, False)

	local var_10_9 = arg_10_0.contextData.system

	if (var_10_9 == SYSTEM_SCENARIO or var_10_9 == SYSTEM_ROUTINE or var_10_9 == SYSTEM_SUB_ROUTINE or var_10_9 == SYSTEM_DUEL) and (var_10_5 == var_10_0[1] or var_10_5 == var_10_0[2]):
		arg_10_0.failTag = True

def var_0_0.displayerCommanders(arg_11_0, arg_11_1):
	arg_11_0.commanderExps = arg_11_0.contextData.commanderExps or {}

	local var_11_0 = getProxy(CommanderProxy)

	removeAllChildren(arg_11_0._cmdContainer)

	local var_11_1

	if arg_11_1:
		var_11_1 = arg_11_0.commanderExps.submarineCMD or {}
	else
		var_11_1 = arg_11_0.commanderExps.surfaceCMD or {}

	setActive(arg_11_0._cmdExp, True)

	for iter_11_0, iter_11_1 in ipairs(var_11_1):
		local var_11_2 = var_11_0.getCommanderById(iter_11_1.commander_id)
		local var_11_3 = cloneTplTo(arg_11_0._cmdTpl, arg_11_0._cmdContainer)

		GetImageSpriteFromAtlasAsync("commandericon/" .. var_11_2.getPainting(), "", var_11_3.Find("icon/mask/pic"))
		setText(var_11_3.Find("exp/name_text"), var_11_2.getName())
		setText(var_11_3.Find("exp/lv_text"), "Lv." .. var_11_2.level)
		setText(var_11_3.Find("exp/exp_text"), "+" .. iter_11_1.exp)

		local var_11_4
		local var_11_5 = var_11_2.isMaxLevel() and 1 or iter_11_1.curExp / var_11_2.getNextLevelExp()

		var_11_3.Find("exp/exp_progress").GetComponent(typeof(Image)).fillAmount = var_11_5

def var_0_0.didEnter(arg_12_0):
	arg_12_0.setStageName()
	arg_12_0.customsLang()

	arg_12_0._shipResultCardList, arg_12_0._subShipResultCardList = {}, {}

	local var_12_0 = rtf(arg_12_0._grade)

	arg_12_0._gradeUpperLeftPos = var_12_0.localPosition
	var_12_0.localPosition = Vector3(0, 25, 0)

	pg.UIMgr.GetInstance().BlurPanel(arg_12_0._tf, True, {
		lockGlobalBlur = True,
		groupName = LayerWeightConst.GROUP_COMBAT
	})

	if arg_12_0.contextData.system != SYSTEM_BOSS_RUSH and arg_12_0.contextData.system != SYSTEM_BOSS_RUSH_EX and arg_12_0.contextData.system != SYSTEM_ACT_BOSS and arg_12_0.contextData.system != SYSTEM_BOSS_SINGLE:
		ys.Battle.BattleCameraUtil.GetInstance().ActiveMainCemera(False)

	arg_12_0._grade.transform.localScale = Vector3(1.5, 1.5, 0)

	LeanTween.scale(arg_12_0._grade, Vector3(0.88, 0.88, 1), var_0_0.DURATION_WIN_SCALE).setOnComplete(System.Action(function()
		SetActive(arg_12_0._levelText, True)
		arg_12_0.rankAnimaFinish()))

	arg_12_0._tf.GetComponent(typeof(Image)).color = Color.New(0, 0, 0, 0.5)

	SetActive(arg_12_0._atkBG, False)
	onToggle(arg_12_0, arg_12_0._subToggle, function(arg_14_0)
		SetActive(arg_12_0._subExpResult, not arg_14_0)
		SetActive(arg_12_0._expResult, arg_14_0)
		setActive(arg_12_0.findTF("off", arg_12_0._subToggle), not arg_14_0)
		arg_12_0.displayerCommanders(not arg_14_0), SFX_PANEL)

	arg_12_0._stateFlag = var_0_0.STATE_RANK_ANIMA

	onButton(arg_12_0, arg_12_0._skipBtn, function()
		arg_12_0.skip(), SFX_CONFIRM)

def var_0_0.setStageName(arg_16_0):
	if arg_16_0.contextData.system and arg_16_0.contextData.system == SYSTEM_DUEL:
		if arg_16_0.rivalVO:
			setText(arg_16_0._levelText, arg_16_0.rivalVO.name)
		else
			setText(arg_16_0._levelText, "")
	else
		local var_16_0 = arg_16_0.contextData.stageId
		local var_16_1 = pg.expedition_data_template[var_16_0]

		setText(arg_16_0._levelText, var_16_1.name)

def var_0_0.rankAnimaFinish(arg_17_0):
	local var_17_0 = arg_17_0.findTF("main/conditions")

	SetActive(var_17_0, True)

	local var_17_1 = arg_17_0.contextData.stageId
	local var_17_2 = pg.expedition_data_template[var_17_1]

	local function var_17_3(arg_18_0)
		if type(arg_18_0) == "table":
			local var_18_0 = i18n(var_0_0.ObjectiveList[arg_18_0[1]], arg_18_0[2])

			arg_17_0.setCondition(var_18_0, var_0_0.objectiveCheck(arg_18_0[1], arg_17_0.contextData))

	var_17_3(var_17_2.objective_1)
	var_17_3(var_17_2.objective_2)
	var_17_3(var_17_2.objective_3)

	local var_17_4 = LeanTween.delayedCall(1, System.Action(function()
		arg_17_0._stateFlag = var_0_0.STATE_REPORTED

		SetActive(arg_17_0.findTF("jieuan01/tips", arg_17_0._bg), True)

		if arg_17_0.skipFlag:
			arg_17_0.skip()))

	table.insert(arg_17_0._delayLeanList, var_17_4.id)

	arg_17_0._stateFlag = var_0_0.STATE_REPORT

def var_0_0.objectiveCheck(arg_20_0, arg_20_1):
	if arg_20_0 == 1 or arg_20_0 == 4 or arg_20_0 == 8:
		return arg_20_1.score > 1
	elif arg_20_0 == 2 or arg_20_0 == 3:
		return not arg_20_1.statistics._deadUnit
	elif arg_20_0 == 6:
		return arg_20_1.statistics._boss_destruct < 1
	elif arg_20_0 == 5:
		return not arg_20_1.statistics._badTime
	elif arg_20_0 == 7:
		return True

def var_0_0.setCondition(arg_21_0, arg_21_1, arg_21_2):
	local var_21_0 = cloneTplTo(arg_21_0._conditionTpl, arg_21_0._conditionContainer)

	setActive(var_21_0, False)

	local var_21_1
	local var_21_2 = var_21_0.Find("text").GetComponent(typeof(Text))

	if arg_21_2 == None:
		var_21_1 = "resources/condition_check"
		var_21_2.text = setColorStr(arg_21_1, "#FFFFFFFF")
	elif arg_21_2 == True:
		var_21_1 = "resources/condition_done"
		var_21_2.text = setColorStr(arg_21_1, "#FFFFFFFF")
	else
		var_21_1 = "resources/condition_fail"
		var_21_2.text = setColorStr(arg_21_1, "#FFFFFF80")

	arg_21_0.setSpriteTo(var_21_1, var_21_0.Find("checkBox"), True)

	local var_21_3 = arg_21_0._conditionContainer.childCount - 1

	if var_21_3 > 0:
		local var_21_4 = LeanTween.delayedCall(var_0_0.CONDITIONS_FREQUENCE * var_21_3, System.Action(function()
			setActive(var_21_0, True)))

		table.insert(arg_21_0._delayLeanList, var_21_4.id)
	else
		setActive(var_21_0, True)

def var_0_0.showRewardInfo(arg_23_0):
	arg_23_0._stateFlag = var_0_0.STATE_REWARD

	if arg_23_0.contextData.system == SYSTEM_BOSS_RUSH or arg_23_0.contextData.system == SYSTEM_BOSS_RUSH_EX:
		arg_23_0.emit(BattleResultMediator.ON_BACK_TO_LEVEL_SCENE)

		return

	SetActive(arg_23_0.findTF("jieuan01/tips", arg_23_0._bg), False)
	setParent(arg_23_0._tf, arg_23_0.UIMain)

	local var_23_0

	local function var_23_1()
		if var_23_0 and coroutine.status(var_23_0) == "suspended":
			local var_24_0, var_24_1 = coroutine.resume(var_23_0)

			assert(var_24_0, var_24_1)

	var_23_0 = coroutine.create(function()
		local var_25_0 = arg_23_0.contextData.drops
		local var_25_1 = getProxy(ActivityProxy)
		local var_25_2 = var_25_1.getActivityById(ActivityConst.UTAWARERU_ACTIVITY_PT_ID)

		if var_25_2 and not var_25_2.isEnd():
			local var_25_3 = var_25_2.getConfig("config_client").pt_id
			local var_25_4 = _.detect(var_25_1.getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PT_RANK), function(arg_26_0)
				return arg_26_0.getConfig("config_id") == var_25_3).getData1()

			if var_25_4 >= 1500:
				local var_25_5 = var_25_4 - 1500
				local var_25_6 = _.detect(var_25_0, function(arg_27_0)
					return arg_27_0.type == DROP_TYPE_RESOURCE and arg_27_0.id == var_25_3)

				var_25_0 = _.filter(var_25_0, function(arg_28_0)
					return arg_28_0.type != DROP_TYPE_RESOURCE or arg_28_0.id != var_25_3)

				if var_25_6 and var_25_5 < var_25_6.count:
					var_25_6.count = var_25_6.count - var_25_5

					table.insert(var_25_0, var_25_6)

		local var_25_7 = {}

		for iter_25_0, iter_25_1 in ipairs(arg_23_0.contextData.drops):
			table.insert(var_25_7, iter_25_1)

		for iter_25_2, iter_25_3 in ipairs(arg_23_0.contextData.extraDrops):
			iter_25_3.riraty = True

			table.insert(var_25_7, iter_25_3)

		local var_25_8 = False
		local var_25_9 = arg_23_0.contextData.extraBuffList

		for iter_25_4, iter_25_5 in ipairs(var_25_9):
			if pg.benefit_buff_template[iter_25_5].benefit_type == Chapter.OPERATION_BUFF_TYPE_REWARD:
				var_25_8 = True

				break

		local var_25_10 = PlayerConst.BonusItemMarker(var_25_0)

		if table.getCount(var_25_10) > 0:
			local var_25_11 = arg_23_0.skipFlag
			local var_25_12 = False

			if arg_23_0.contextData.system == SYSTEM_SCENARIO:
				local var_25_13 = getProxy(ChapterProxy).getActiveChapter(True)

				if var_25_13:
					if var_25_13.isLoop():
						getProxy(ChapterProxy).AddExtendChapterDataArray(var_25_13.id, "TotalDrops", var_25_7)

						var_25_12 = getProxy(ChapterProxy).GetChapterAutoFlag(var_25_13.id) == 1

					var_25_13.writeDrops(var_25_7)
			elif arg_23_0.contextData.system == SYSTEM_ACT_BOSS:
				if getProxy(ContextProxy).getCurrentContext().getContextByMediator(ContinuousOperationMediator):
					getProxy(ChapterProxy).AddActBossRewards(var_25_7)
			elif arg_23_0.contextData.system == SYSTEM_BOSS_SINGLE and getProxy(ContextProxy).getCurrentContext().getContextByMediator(BossSingleContinuousOperationMediator):
				getProxy(ChapterProxy).AddBossSingleRewards(var_25_7)

			arg_23_0.emit(BaseUI.ON_AWARD, {
				items = var_25_7,
				extraBonus = var_25_8,
				removeFunc = var_23_1,
				closeOnCompleted = var_25_11
			})
			coroutine.yield()

			local var_25_14 = #_.filter(var_25_7, function(arg_29_0)
				return arg_29_0.type == DROP_TYPE_SHIP)
			local var_25_15 = getProxy(BayProxy).getNewShip(True)

			for iter_25_6 = math.max(1, #var_25_15 - var_25_14 + 1), #var_25_15:
				local var_25_16 = var_25_15[iter_25_6]

				if PlayerPrefs.GetInt(DISPLAY_SHIP_GET_EFFECT) == 1 or var_25_16.virgin or var_25_16.getRarity() >= ShipRarity.Purple:
					local var_25_17 = var_25_12 and not var_25_16.virgin and 3 or None

					arg_23_0.emit(BattleResultMediator.GET_NEW_SHIP, var_25_16, var_23_1, var_25_17)
					coroutine.yield()

		setParent(arg_23_0._tf, arg_23_0.overlay)
		arg_23_0.displayBG())

	var_23_1()

def var_0_0.displayBG(arg_30_0):
	local function var_30_0()
		arg_30_0.displayShips()
		arg_30_0.displayPlayerInfo()
		arg_30_0.displayerCommanders()
		arg_30_0.initMetaBtn()

		arg_30_0._stateFlag = var_0_0.STATE_DISPLAY

		if arg_30_0.skipFlag:
			arg_30_0.skip()

	local var_30_1 = rtf(arg_30_0._grade)

	LeanTween.moveX(rtf(arg_30_0._conditions), 1300, var_0_0.DURATION_MOVE)
	LeanTween.scale(arg_30_0._grade, Vector3(0.6, 0.6, 0), var_0_0.DURATION_MOVE)
	LeanTween.moveLocal(go(var_30_1), arg_30_0._gradeUpperLeftPos, var_0_0.DURATION_MOVE)
	setActive(arg_30_0.findTF("jieuan01/Bomb", arg_30_0._bg), False)
	onDelayTick(function()
		setLocalScale(arg_30_0._grade, Vector3(0.6, 0.6, 0))
		setAnchoredPosition(arg_30_0._grade, arg_30_0._gradeUpperLeftPos)
		var_30_0(), var_0_0.DURATION_MOVE)

def var_0_0.displayPlayerInfo(arg_33_0):
	local var_33_0 = arg_33_0.calcPlayerProgress()

	SetActive(arg_33_0._leftPanel, True)
	SetActive(arg_33_0._playerExp, True)

	arg_33_0._main.GetComponent("Animator").enabled = True

	local var_33_1 = LeanTween.moveX(rtf(arg_33_0._leftPanel), 0, 0.5).setOnComplete(System.Action(function()
		local var_34_0 = LeanTween.value(go(arg_33_0._tf), 0, var_33_0, 1).setOnUpdate(System.Action_float(function(arg_35_0)
			setText(arg_33_0._playerBonusExp, "+" .. math.floor(arg_35_0))))

		table.insert(arg_33_0._delayLeanList, var_34_0.id)))

	table.insert(arg_33_0._delayLeanList, var_33_1.id)

def var_0_0.calcPlayerExp(arg_36_0):
	local var_36_0 = arg_36_0.contextData.oldPlayer
	local var_36_1 = var_36_0.level
	local var_36_2 = arg_36_0.player.level
	local var_36_3 = arg_36_0.player.exp - var_36_0.exp

	while var_36_1 < var_36_2:
		var_36_3 = var_36_3 + pg.user_level[var_36_1].exp
		var_36_1 = var_36_1 + 1

	if var_36_1 == pg.user_level[#pg.user_level].level:
		var_36_3 = 0

	return var_36_3

def var_0_0.calcPlayerRank(arg_37_0):
	local var_37_0 = arg_37_0.contextData.oldRank
	local var_37_1 = var_37_0.score

	return arg_37_0.season.score - var_37_0.score

def var_0_0.displayShips(arg_38_0):
	local var_38_0 = {}
	local var_38_1 = arg_38_0.shipVOs

	for iter_38_0, iter_38_1 in ipairs(var_38_1):
		var_38_0[iter_38_1.id] = iter_38_1

	local var_38_2 = arg_38_0.contextData.statistics

	for iter_38_2, iter_38_3 in ipairs(var_38_1):
		if var_38_2[iter_38_3.id]:
			var_38_2[iter_38_3.id].vo = iter_38_3

	local var_38_3
	local var_38_4

	if var_38_2.mvpShipID == -1:
		var_38_4 = 0

		for iter_38_4, iter_38_5 in ipairs(arg_38_0.contextData.oldMainShips):
			var_38_4 = math.max(var_38_2[iter_38_5.id].output, var_38_4)
	elif var_38_2.mvpShipID and var_38_2.mvpShipID != 0:
		var_38_3 = var_38_2[var_38_2.mvpShipID]
		var_38_4 = var_38_3.output
	else
		var_38_4 = 0

	local var_38_5 = arg_38_0.contextData.oldMainShips

	arg_38_0._atkFuncs = {}

	local var_38_6
	local var_38_7

	SetActive(arg_38_0._atkToggle, #var_38_5 > 6)

	if #var_38_5 > 6:
		onToggle(arg_38_0, arg_38_0._atkToggle, function(arg_39_0)
			SetActive(arg_38_0._atkContainer, arg_39_0)
			SetActive(arg_38_0._atkContainerNext, not arg_39_0)

			if arg_39_0:
				arg_38_0.skipAtkAnima(arg_38_0._atkContainerNext)
			else
				arg_38_0.skipAtkAnima(arg_38_0._atkContainer), SFX_PANEL)

	local var_38_8 = {}
	local var_38_9 = {}

	for iter_38_6, iter_38_7 in ipairs(var_38_5):
		local var_38_10 = var_38_0[iter_38_7.id]

		if var_38_2[iter_38_7.id]:
			local var_38_11 = ys.Battle.BattleDataFunction.GetPlayerShipTmpDataFromID(iter_38_7.configId).type
			local var_38_12 = table.contains(TeamType.SubShipType, var_38_11)
			local var_38_13
			local var_38_14
			local var_38_15 = 0
			local var_38_16

			if iter_38_6 > 6:
				var_38_14 = arg_38_0._atkContainerNext
				var_38_16 = 7
			else
				var_38_14 = arg_38_0._atkContainer
				var_38_16 = 1

			local var_38_17 = cloneTplTo(arg_38_0._atkTpl, var_38_14)
			local var_38_18 = var_38_17.localPosition

			var_38_18.x = var_38_18.x + (iter_38_6 - var_38_16) * 74
			var_38_18.y = var_38_18.y + (iter_38_6 - var_38_16) * -124
			var_38_17.localPosition = var_38_18

			local var_38_19 = findTF(var_38_17, "result/stars")
			local var_38_20 = findTF(var_38_17, "result/stars/star_tpl")
			local var_38_21 = iter_38_7.getStar()
			local var_38_22 = iter_38_7.getMaxStar()

			while var_38_22 > 0:
				local var_38_23 = cloneTplTo(var_38_20, var_38_19)

				SetActive(var_38_23.Find("empty"), var_38_21 < var_38_22)
				SetActive(var_38_23.Find("star"), var_38_22 <= var_38_21)

				var_38_22 = var_38_22 - 1

			local var_38_24 = arg_38_0.findTF("result/mask/icon", var_38_17)
			local var_38_25 = arg_38_0.findTF("result/type", var_38_17)

			var_38_24.GetComponent(typeof(Image)).sprite = LoadSprite("herohrzicon/" .. iter_38_7.getPainting())

			local var_38_26 = var_38_2[iter_38_7.id].output / var_38_4
			local var_38_27 = GetSpriteFromAtlas("shiptype", shipType2print(iter_38_7.getShipType()))

			setImageSprite(var_38_25, var_38_27, True)
			arg_38_0.setAtkAnima(var_38_17, var_38_14, var_38_26, var_38_4, var_38_3 and iter_38_7.id == var_38_3.id, var_38_2[iter_38_7.id].output, var_38_2[iter_38_7.id].kill_count)

			local var_38_28
			local var_38_29 = False

			if var_38_3 and iter_38_7.id == var_38_3.id:
				var_38_29 = True
				arg_38_0.mvpShipVO = iter_38_7

				local var_38_30
				local var_38_31
				local var_38_32

				if arg_38_0.contextData.score > 1:
					local var_38_33, var_38_34

					var_38_33, var_38_32, var_38_34 = ShipWordHelper.GetWordAndCV(arg_38_0.mvpShipVO.skinId, ShipWordHelper.WORD_TYPE_MVP, None, None, arg_38_0.mvpShipVO.getCVIntimacy())
				else
					local var_38_35, var_38_36

					var_38_35, var_38_32, var_38_36 = ShipWordHelper.GetWordAndCV(arg_38_0.mvpShipVO.skinId, ShipWordHelper.WORD_TYPE_LOSE)

				if var_38_32:
					arg_38_0.stopVoice()
					pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_38_32, function(arg_40_0)
						arg_38_0._currentVoice = arg_40_0)

			if iter_38_7.id == var_38_2._flagShipID:
				arg_38_0.flagShipVO = iter_38_7

			local var_38_37
			local var_38_38 = arg_38_0.shipBuff and arg_38_0.shipBuff[iter_38_7.getGroupId()]

			if arg_38_0.expBuff or var_38_38:
				var_38_37 = arg_38_0.expBuff and arg_38_0.expBuff.getConfig("name") or var_38_38 and i18n("Word_Ship_Exp_Buff")

			local var_38_39

			if not var_38_12:
				local var_38_40 = cloneTplTo(arg_38_0._extpl, arg_38_0._expContainer)

				var_38_39 = BattleResultShipCard.New(var_38_40)

				table.insert(arg_38_0._shipResultCardList, var_38_39)

				if var_38_7:
					var_38_7.ConfigCallback(function()
						var_38_39.Play())
				else
					var_38_39.Play()

				var_38_7 = var_38_39
			else
				local var_38_41 = cloneTplTo(arg_38_0._extpl, arg_38_0._subExpContainer)

				var_38_39 = BattleResultShipCard.New(var_38_41)

				table.insert(arg_38_0._subShipResultCardList, var_38_39)

				if not var_38_6:
					arg_38_0._subFirstExpCard = var_38_39
				else
					var_38_6.ConfigCallback(function()
						var_38_39.Play())

				var_38_6 = var_38_39

			var_38_39.SetShipVO(iter_38_7, var_38_10, var_38_29, var_38_37)

	if var_38_7:
		var_38_7.ConfigCallback(function()
			arg_38_0._stateFlag = var_0_0.STATE_DISPLAYED

			if not arg_38_0._subFirstExpCard:
				arg_38_0.skip())

	if var_38_6:
		var_38_6.ConfigCallback(function()
			arg_38_0._stateFlag = var_0_0.STATE_SUB_DISPLAYED

			arg_38_0.skip())

def var_0_0.stopVoice(arg_45_0):
	if arg_45_0._currentVoice:
		arg_45_0._currentVoice.PlaybackStop()

		arg_45_0._currentVoice = None

def var_0_0.setAtkAnima(arg_46_0, arg_46_1, arg_46_2, arg_46_3, arg_46_4, arg_46_5, arg_46_6, arg_46_7):
	local var_46_0 = arg_46_0.findTF("result", arg_46_1)
	local var_46_1 = arg_46_0.findTF("result/atk", arg_46_1)
	local var_46_2 = arg_46_0.findTF("result/dmg_progress/progress_bar", arg_46_1)
	local var_46_3 = arg_46_0.findTF("result/killCount", arg_46_1)
	local var_46_4 = var_46_0.GetComponent(typeof(DftAniEvent))

	setText(var_46_1, 0)
	setText(var_46_3, 0)

	var_46_2.GetComponent(typeof(Image)).fillAmount = 0

	if arg_46_5:
		local var_46_5 = arg_46_0.findTF("result/mvpBG", arg_46_1)

		setParent(arg_46_0._mvpFX, var_46_5)

		arg_46_0._mvpFX.localPosition = Vector3(-368.5, 0, 0)

		setActive(var_46_5, True)
		setActive(arg_46_0.findTF("result/bg", arg_46_1), False)

	var_46_4.SetEndEvent(function(arg_47_0)
		if arg_46_5:
			setActive(arg_46_0._mvpFX, True)

		LeanTween.value(go(var_46_0), 0, arg_46_3, arg_46_3).setOnUpdate(System.Action_float(function(arg_48_0)
			var_46_2.GetComponent(typeof(Image)).fillAmount = arg_48_0))

		if arg_46_4 != 0:
			LeanTween.value(go(var_46_0), 0, arg_46_6, arg_46_3).setOnUpdate(System.Action_float(function(arg_49_0)
				setText(var_46_1, math.floor(arg_49_0))))
			LeanTween.value(go(var_46_0), 0, arg_46_7, arg_46_3).setOnUpdate(System.Action_float(function(arg_50_0)
				setText(var_46_3, math.floor(arg_50_0)))))

	if arg_46_2.childCount > 1:
		arg_46_0.findTF("result", arg_46_2.GetChild(arg_46_2.childCount - 2)).GetComponent(typeof(DftAniEvent)).SetTriggerEvent(function(arg_51_0)
			setActive(var_46_0, True))
	else
		setActive(var_46_0, True)

	local function var_46_6()
		var_46_2.GetComponent(typeof(Image)).fillAmount = arg_46_3

		setText(var_46_1, arg_46_6)
		setText(var_46_3, arg_46_7)

		var_46_0.localPosition = Vector3(280, 46, 0)
		var_46_0.GetComponent(typeof(Animator)).enabled = False

		setActive(var_46_0, True)
		setActive(arg_46_0._mvpFX, True)

	if arg_46_0._atkFuncs[arg_46_2] == None:
		arg_46_0._atkFuncs[arg_46_2] = {}

	table.insert(arg_46_0._atkFuncs[arg_46_2], var_46_6)

def var_0_0.skipAtkAnima(arg_53_0, arg_53_1):
	if arg_53_0._atkFuncs[arg_53_1]:
		for iter_53_0, iter_53_1 in ipairs(arg_53_0._atkFuncs[arg_53_1]):
			iter_53_1()

		arg_53_0._atkFuncs[arg_53_1] = None

def var_0_0.showPainting(arg_54_0):
	local var_54_0
	local var_54_1
	local var_54_2

	SetActive(arg_54_0._painting, True)

	if arg_54_0.contextData.score > 1:
		local var_54_3 = arg_54_0.mvpShipVO or arg_54_0.flagShipVO

		arg_54_0.paintingName = var_54_3.getPainting()

		local var_54_4 = var_54_3.getCVIntimacy()

		setPaintingPrefabAsync(arg_54_0._painting, arg_54_0.paintingName, "jiesuan", function()
			if findTF(arg_54_0._painting, "fitter").childCount > 0:
				ShipExpressionHelper.SetExpression(findTF(arg_54_0._painting, "fitter").GetChild(0), arg_54_0.paintingName, "win_mvp", var_54_4))

		local var_54_5, var_54_6

		var_54_5, var_54_6, var_54_1 = ShipWordHelper.GetWordAndCV(var_54_3.skinId, ShipWordHelper.WORD_TYPE_MVP, None, None, var_54_4)

		SetActive(arg_54_0._failPainting, False)
	else
		local var_54_7 = arg_54_0.contextData.oldMainShips
		local var_54_8 = var_54_7[math.random(#var_54_7)]
		local var_54_9, var_54_10

		var_54_9, var_54_10, var_54_1 = ShipWordHelper.GetWordAndCV(var_54_8.skinId, ShipWordHelper.WORD_TYPE_LOSE)

	setText(arg_54_0._chat.Find("Text"), var_54_1)

	local var_54_11 = arg_54_0._chat.Find("Text").GetComponent(typeof(Text))

	if #var_54_11.text > CHAT_POP_STR_LEN:
		var_54_11.alignment = TextAnchor.MiddleLeft
	else
		var_54_11.alignment = TextAnchor.MiddleCenter

	SetActive(arg_54_0._chat, True)

	arg_54_0._chat.transform.localScale = Vector3.New(0, 0, 0)

	LeanTween.cancel(go(arg_54_0._painting))
	LeanTween.moveX(rtf(arg_54_0._painting), 50, 0.25).setOnComplete(System.Action(function()
		LeanTween.scale(rtf(arg_54_0._chat.gameObject), Vector3.New(1, 1, 1), 0.3).setEase(LeanTweenType.easeOutBack).setOnComplete(System.Action(function()
			arg_54_0._statisticsBtn.GetComponent("Button").enabled = True
			arg_54_0._confirmBtn.GetComponent("Button").enabled = True
			arg_54_0._atkBG.GetComponent("Button").enabled = True))))

def var_0_0.hidePainting(arg_58_0):
	SetActive(arg_58_0._chat, False)

	arg_58_0._chat.transform.localScale = Vector3.New(0, 0, 0)

	LeanTween.cancel(go(arg_58_0._painting))
	LeanTween.scale(rtf(arg_58_0._chat.gameObject), Vector3.New(0, 0, 0), 0.1).setEase(LeanTweenType.easeOutBack)
	LeanTween.moveX(rtf(arg_58_0._painting), 720, 0.2).setOnComplete(System.Action(function()
		SetActive(arg_58_0._painting, False)))

def var_0_0.skip(arg_60_0):
	for iter_60_0, iter_60_1 in ipairs(arg_60_0._delayLeanList):
		LeanTween.cancel(iter_60_1)

	if arg_60_0._stateFlag == var_0_0.STATE_RANK_ANIMA:
		-- block empty
	elif arg_60_0._stateFlag == var_0_0.STATE_REPORT:
		local var_60_0 = arg_60_0._conditionContainer.childCount

		while var_60_0 > 0:
			SetActive(arg_60_0._conditionContainer.GetChild(var_60_0 - 1), True)

			var_60_0 = var_60_0 - 1

		SetActive(arg_60_0.findTF("jieuan01/tips", arg_60_0._bg), True)

		arg_60_0._stateFlag = var_0_0.STATE_REPORTED

		arg_60_0.skip()
	elif arg_60_0._stateFlag == var_0_0.STATE_REPORTED:
		arg_60_0.showRewardInfo()
	elif arg_60_0._stateFlag == var_0_0.STATE_REWARD:
		-- block empty
	elif arg_60_0._stateFlag == var_0_0.STATE_DISPLAY:
		for iter_60_2, iter_60_3 in ipairs(arg_60_0._shipResultCardList):
			iter_60_3.SkipAnimation()

		arg_60_0._stateFlag = var_0_0.STATE_DISPLAYED

		setText(arg_60_0._playerBonusExp, "+" .. arg_60_0.calcPlayerProgress())

		if not arg_60_0._subFirstExpCard:
			arg_60_0.playSubExEnter()
		elif arg_60_0.skipFlag:
			arg_60_0.skip()
	elif arg_60_0._stateFlag == var_0_0.STATE_DISPLAYED:
		setText(arg_60_0._playerBonusExp, "+" .. arg_60_0.calcPlayerProgress())
		arg_60_0.playSubExEnter()
	elif arg_60_0._stateFlag == var_0_0.STATE_SUB_DISPLAY:
		for iter_60_4, iter_60_5 in ipairs(arg_60_0._subShipResultCardList):
			iter_60_5.SkipAnimation()

		arg_60_0._stateFlag = var_0_0.STATE_SUB_DISPLAYED

		if arg_60_0.skipFlag:
			arg_60_0.skip()
	elif arg_60_0._stateFlag == var_0_0.STATE_SUB_DISPLAYED:
		arg_60_0.showRightBottomPanel()

def var_0_0.playSubExEnter(arg_61_0):
	arg_61_0._stateFlag = var_0_0.STATE_SUB_DISPLAY

	if arg_61_0._subFirstExpCard:
		triggerToggle(arg_61_0._subToggle, False)
		arg_61_0._subFirstExpCard.Play()
	else
		arg_61_0.showRightBottomPanel()

	if arg_61_0.skipFlag:
		arg_61_0.skip()

def var_0_0.showRightBottomPanel(arg_62_0):
	SetActive(arg_62_0._skipBtn, False)
	SetActive(arg_62_0._rightBottomPanel, True)
	SetActive(arg_62_0._subToggle, arg_62_0._subFirstExpCard != None)
	onButton(arg_62_0, arg_62_0._statisticsBtn, function()
		if arg_62_0._atkBG.gameObject.activeSelf:
			arg_62_0.closeStatistics()
		else
			arg_62_0.showStatistics(), SFX_PANEL)
	onButton(arg_62_0, arg_62_0._confirmBtn, function()
		if arg_62_0.failTag == True:
			arg_62_0.emit(BattleResultMediator.PRE_BATTLE_FAIL_EXIT)
			arg_62_0.emit(BattleResultMediator.OPEN_FAIL_TIP_LAYER)
		else
			arg_62_0.emit(BattleResultMediator.ON_BACK_TO_LEVEL_SCENE), SFX_CONFIRM)
	onButton(arg_62_0, arg_62_0._atkBG, function()
		arg_62_0.closeStatistics(), SFX_CANCEL)

	arg_62_0._stateFlag = None
	arg_62_0._subFirstExpCard = None

	if arg_62_0.skipFlag:
		triggerButton(arg_62_0._confirmBtn)

def var_0_0.showStatistics(arg_66_0):
	setActive(arg_66_0._leftPanel, False)
	arg_66_0.enabledStatisticsGizmos(False)
	SetActive(arg_66_0._atkBG, True)

	arg_66_0._atkBG.GetComponent("Button").enabled = False
	arg_66_0._confirmBtn.GetComponent("Button").enabled = False
	arg_66_0._statisticsBtn.GetComponent("Button").enabled = False

	arg_66_0.showPainting()
	LeanTween.moveX(rtf(arg_66_0._atkPanel), 0, 0.25).setOnComplete(System.Action(function()
		SetActive(arg_66_0._atkContainer, True)))

def var_0_0.closeStatistics(arg_68_0):
	setActive(arg_68_0._leftPanel, True)
	arg_68_0.skipAtkAnima(arg_68_0._atkContainerNext)
	arg_68_0.skipAtkAnima(arg_68_0._atkContainer)
	arg_68_0.enabledStatisticsGizmos(True)
	arg_68_0.hidePainting()

	arg_68_0._atkBG.GetComponent("Button").enabled = False

	LeanTween.cancel(arg_68_0._atkPanel.gameObject)
	LeanTween.moveX(rtf(arg_68_0._atkPanel), -700, 0.2).setOnComplete(System.Action(function()
		SetActive(arg_68_0._atkBG, False)))

def var_0_0.enabledStatisticsGizmos(arg_70_0, arg_70_1):
	setActive(arg_70_0.findTF("gizmos/xuxian_down", arg_70_0._main), arg_70_1)
	setActive(arg_70_0.findTF("gizmos/xuxian_middle", arg_70_0._main), arg_70_1)

def var_0_0.PlayAnimation(arg_71_0, arg_71_1, arg_71_2, arg_71_3, arg_71_4, arg_71_5, arg_71_6):
	LeanTween.value(arg_71_1.gameObject, arg_71_2, arg_71_3, arg_71_4).setDelay(arg_71_5).setOnUpdate(System.Action_float(function(arg_72_0)
		arg_71_6(arg_72_0)))

def var_0_0.SetSkipFlag(arg_73_0, arg_73_1):
	arg_73_0.skipFlag = arg_73_1

def var_0_0.initMetaBtn(arg_74_0):
	arg_74_0.metaBtn = arg_74_0.findTF("MetaBtn", arg_74_0._main)

	local var_74_0 = getProxy(MetaCharacterProxy).getLastMetaSkillExpInfoList()

	setActive(arg_74_0.metaBtn, var_74_0 and #var_74_0 > 0 or False)
	onButton(arg_74_0, arg_74_0.metaBtn, function()
		setActive(arg_74_0.metaBtn, False)

		if not arg_74_0.metaExpView:
			arg_74_0.metaExpView = BattleResultMetaExpView.New(arg_74_0._blurConatiner, arg_74_0.event, arg_74_0.contextData)

			arg_74_0.metaExpView.Reset()
			arg_74_0.metaExpView.Load()
			arg_74_0.metaExpView.setData(var_74_0, function()
				if arg_74_0.metaBtn:
					setActive(arg_74_0.metaBtn, True)

				arg_74_0.metaExpView = None)
			arg_74_0.metaExpView.ActionInvoke("Show")
			arg_74_0.metaExpView.ActionInvoke("openPanel"), SFX_PANEL)

def var_0_0.onBackPressed(arg_77_0):
	if arg_77_0.metaExpView:
		arg_77_0.metaExpView.closePanel()

		arg_77_0.metaExpView = None

		return

	if arg_77_0._stateFlag == var_0_0.STATE_RANK_ANIMA:
		-- block empty
	elif arg_77_0._stateFlag == var_0_0.STATE_REPORT:
		triggerButton(arg_77_0._bg)
	elif arg_77_0._stateFlag == var_0_0.STATE_REPORTED:
		triggerButton(arg_77_0._skipBtn)
	elif arg_77_0._stateFlag == var_0_0.STATE_DISPLAY:
		triggerButton(arg_77_0._skipBtn)
	else
		triggerButton(arg_77_0._confirmBtn)

def var_0_0.willExit(arg_78_0):
	for iter_78_0, iter_78_1 in ipairs(arg_78_0._shipResultCardList):
		iter_78_1.Dispose()

	for iter_78_2, iter_78_3 in ipairs(arg_78_0._subShipResultCardList):
		iter_78_3.Dispose()

	arg_78_0._atkFuncs = None

	LeanTween.cancel(go(arg_78_0._tf))

	if arg_78_0._atkBG.gameObject.activeSelf:
		pg.UIMgr.GetInstance().UnblurPanel(arg_78_0._blurConatiner, arg_78_0._tf)

	if arg_78_0.paintingName:
		retPaintingPrefab(arg_78_0._painting, arg_78_0.paintingName)

	if arg_78_0._rightTimer:
		arg_78_0._rightTimer.Stop()

	pg.UIMgr.GetInstance().UnblurPanel(arg_78_0._tf)
	arg_78_0.stopVoice()
	getProxy(MetaCharacterProxy).clearLastMetaSkillExpInfoList()

	if arg_78_0.metaExpView:
		arg_78_0.metaExpView.Destroy()

		arg_78_0.metaExpView = None

	pg.CameraFixMgr.GetInstance().disconnect(arg_78_0.camEventId)

return var_0_0
