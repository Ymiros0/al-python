local var_0_0 = class("BattleChallengeResultLayer", import(".BattleResultLayer"))

var_0_0.DURATION_WIN_FADE_IN = 0.5
var_0_0.DURATION_LOSE_FADE_IN = 1.5
var_0_0.DURATION_GRADE_LAST = 1.5
var_0_0.DURATION_MOVE = 0.7
var_0_0.DURATION_WIN_SCALE = 0.7
var_0_0.STATE_DEFEAT = "state_defeat"
var_0_0.STATE_CLEAR = "state_clear"
var_0_0.STATE_CONTINUE = "state_continue"
var_0_0.STATE_QUIT = "state_quit"

def var_0_0.getUIName(arg_1_0):
	return "BattleResultUI"

def var_0_0.setChallengeInfo(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.challenge = arg_2_1
	arg_2_0.challengeExpire = arg_2_2

def var_0_0.setShips(arg_3_0, arg_3_1):
	arg_3_0.shipVOs = arg_3_1

def var_0_0.isTotalClear(arg_4_0):
	return arg_4_0.challenge.getMode() == ChallengeProxy.MODE_CASUAL and arg_4_0.challenge.IsFinish() or arg_4_0.isFail()

def var_0_0.isFail(arg_5_0):
	return arg_5_0.contextData.score < ys.Battle.BattleConst.BattleScore.S

def var_0_0.init(arg_6_0):
	var_0_0.super.init(arg_6_0)

	arg_6_0._challengeBottomPanel = arg_6_0.findTF("challenge_confirm", arg_6_0._blurConatiner)

	setText(findTF(arg_6_0._challengeBottomPanel, "continue_btn/text"), i18n("battle_result_continue_battle"))
	setText(findTF(arg_6_0._challengeBottomPanel, "quit_btn/text"), i18n("battle_result_quit_battle"))
	setText(findTF(arg_6_0._challengeBottomPanel, "share_btn/text"), i18n("battle_result_share_battle"))

	arg_6_0._shareBtn = arg_6_0.findTF("share_btn", arg_6_0._challengeBottomPanel)
	arg_6_0._continueBtn = arg_6_0.findTF("continue_btn", arg_6_0._challengeBottomPanel)
	arg_6_0._quitBtn = arg_6_0.findTF("quit_btn", arg_6_0._challengeBottomPanel)
	arg_6_0._expire = arg_6_0.findTF("challenge_expire", arg_6_0._main)
	arg_6_0._expireTxt = arg_6_0.findTF("text", arg_6_0._expire)

def var_0_0.didEnter(arg_7_0):
	var_0_0.super.didEnter(arg_7_0)
	onButton(arg_7_0, arg_7_0._skipBtn, function()
		arg_7_0.skip(), SFX_CONFIRM)

def var_0_0.setStageName(arg_9_0):
	if arg_9_0.contextData.system and arg_9_0.contextData.system == SYSTEM_DUEL:
		setText(arg_9_0._levelText, arg_9_0.rivalVO.name)
	else
		local var_9_0 = arg_9_0.contextData.stageId
		local var_9_1 = pg.expedition_data_template[var_9_0]

	if arg_9_0.challenge.getMode() == ChallengeProxy.MODE_INFINITE:
		local var_9_2 = arg_9_0.contextData.stageId
		local var_9_3 = pg.expedition_data_template[var_9_2].name .. " - ROUND " .. arg_9_0.challenge.getLevel()

		setText(arg_9_0._levelText, var_9_3)
	else
		var_0_0.super.setStageName(arg_9_0)

def var_0_0.rankAnimaFinish(arg_10_0):
	local var_10_0 = arg_10_0.findTF("main/conditions")

	if arg_10_0.challenge.getMode() == ChallengeProxy.MODE_INFINITE:
		SetActive(var_10_0, False)

		arg_10_0._stateFlag = var_0_0.STATE_REPORTED
	else
		SetActive(var_10_0, True)
		arg_10_0.setCondition(i18n("challenge_combat_score", arg_10_0.challenge.getLastScore()), True)
		arg_10_0.setCondition(i18n("challenge_current_score", arg_10_0.challenge.getScore()), True)

		local var_10_1 = LeanTween.delayedCall(1, System.Action(function()
			arg_10_0._stateFlag = var_0_0.STATE_REPORTED

			SetActive(arg_10_0.findTF("jieuan01/tips", arg_10_0._bg), True)))

		table.insert(arg_10_0._delayLeanList, var_10_1.id)

		arg_10_0._stateFlag = var_0_0.STATE_REPORT

def var_0_0.displayDefeat(arg_12_0):
	local function var_12_0()
		arg_12_0.skip()

	if arg_12_0.isFail():
		arg_12_0._stateFlag = var_0_0.STATE_QUIT

		var_12_0()
	else
		arg_12_0.emit(BattleResultMediator.ON_CHALLENGE_DEFEAT_SCENE, {
			callback = var_12_0
		})

def var_0_0.showRightBottomPanel(arg_14_0):
	SetActive(arg_14_0._expire, arg_14_0.challengeExpire)
	setText(arg_14_0._expireTxt, i18n("challenge_expire_warn"))
	SetActive(arg_14_0._skipBtn, False)

	if not arg_14_0.isTotalClear():
		SetActive(arg_14_0.findTF("jieuan01/tips", arg_14_0._bg), False)

	SetActive(arg_14_0._challengeBottomPanel, True)

	if arg_14_0.isTotalClear():
		SetActive(arg_14_0._continueBtn, False)
		SetActive(arg_14_0._quitBtn, False)
		SetActive(arg_14_0._shareBtn, True)
		onButton(arg_14_0, arg_14_0._shareBtn, function()
			arg_14_0.emit(BattleResultMediator.ON_CHALLENGE_SHARE), SFX_CONFIRM)
		onButton(arg_14_0, arg_14_0._bg, function()
			arg_14_0.skip()

			arg_14_0._stateFlag = var_0_0.STATE_CLEAR)
	else
		SetActive(arg_14_0._continueBtn, True)
		SetActive(arg_14_0._quitBtn, True)
		SetActive(arg_14_0._shareBtn, False)
		onButton(arg_14_0, arg_14_0._continueBtn, function()
			arg_14_0.skip()

			arg_14_0._stateFlag = var_0_0.STATE_CONTINUE, SFX_CONFIRM)
		onButton(arg_14_0, arg_14_0._quitBtn, function()
			arg_14_0.skip()

			arg_14_0._stateFlag = var_0_0.STATE_QUIT, SFX_CONFIRM)

	arg_14_0._stateFlag = var_0_0.STATE_DEFEAT

def var_0_0.onBackPressed(arg_19_0):
	arg_19_0.skip()

def var_0_0.skip(arg_20_0):
	for iter_20_0, iter_20_1 in ipairs(arg_20_0._delayLeanList):
		LeanTween.cancel(iter_20_1)

	if arg_20_0._stateFlag == var_0_0.STATE_RANK_ANIMA:
		-- block empty
	elif arg_20_0._stateFlag == var_0_0.STATE_REPORT:
		local var_20_0 = arg_20_0._conditionContainer.childCount

		while var_20_0 > 0:
			SetActive(arg_20_0._conditionContainer.GetChild(var_20_0 - 1), True)

			var_20_0 = var_20_0 - 1

		SetActive(arg_20_0.findTF("jieuan01/tips", arg_20_0._bg), True)

		arg_20_0._stateFlag = var_0_0.STATE_REPORTED
	elif arg_20_0._stateFlag == var_0_0.STATE_REPORTED:
		arg_20_0.showRightBottomPanel()
	elif arg_20_0._stateFlag == var_0_0.STATE_DEFEAT:
		if arg_20_0.isTotalClear():
			arg_20_0.emit(BattleResultMediator.ON_BACK_TO_LEVEL_SCENE, {
				goToNext = False
			})
		else
			arg_20_0.displayDefeat()
	elif arg_20_0._stateFlag == var_0_0.STATE_CONTINUE:
		arg_20_0.emit(BattleResultMediator.ON_BACK_TO_LEVEL_SCENE, {
			goToNext = True
		})
	elif arg_20_0._stateFlag == var_0_0.STATE_QUIT or arg_20_0._stateFlag == var_0_0.STATE_CLEAR:
		arg_20_0.emit(BattleResultMediator.ON_BACK_TO_LEVEL_SCENE, {
			goToNext = False
		})

def var_0_0.willExit(arg_21_0):
	var_0_0.super.willExit(arg_21_0)
	LeanTween.cancel(go(arg_21_0._tf))
	pg.UIMgr.GetInstance().UnblurPanel(arg_21_0._tf)

return var_0_0
