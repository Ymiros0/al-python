local var_0_0 = class("ChallengeMainScene", import("..base.BaseUI"))

var_0_0.BOSS_NUM = 5
var_0_0.FADE_TIME = 5

def var_0_0.getUIName(arg_1_0):
	return "ChallengeMainUI"

def var_0_0.init(arg_2_0):
	arg_2_0.findUI()
	arg_2_0.initData()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.updateGrade(arg_3_0.challengeInfo.getGradeList())
	arg_3_0.updateTimePanel()
	arg_3_0.updateSwitchModBtn()
	arg_3_0.updateAwardPanel()
	arg_3_0.updatePaintingList(arg_3_0.nameList, arg_3_0.showingIndex)
	arg_3_0.updateRoundText(arg_3_0.showingIndex)
	arg_3_0.updateSlider(arg_3_0.showingIndex)
	arg_3_0.updateFuncBtns()
	arg_3_0.showSLResetMsgBox()

	if arg_3_0.contextData.editFleet:
		arg_3_0.doOnFleetPanel()

		arg_3_0.contextData.editFleet = None

	arg_3_0.tryPlayGuide()

def var_0_0.willExit(arg_4_0):
	LeanTween.cancel(go(arg_4_0.modTipTF))

	if arg_4_0.timer:
		arg_4_0.timer.Stop()

	arg_4_0.destroyCommanderPanel()

def var_0_0.onBackPressed(arg_5_0):
	if isActive(arg_5_0.fleetSelect):
		arg_5_0.hideFleetEdit()
	else
		triggerButton(arg_5_0.backBtn)

def var_0_0.setFleet(arg_6_0, arg_6_1):
	arg_6_0.fleets = {}

	local function var_6_0(arg_7_0)
		arg_6_0.fleets[arg_7_0] = {
			arg_6_1[arg_7_0 + 1],
			[11] = arg_6_1[arg_7_0 + 11]
		}

	var_6_0(ChallengeProxy.MODE_CASUAL)
	var_6_0(ChallengeProxy.MODE_INFINITE)

def var_0_0.findUI(arg_8_0):
	arg_8_0.northTF = arg_8_0.findTF("ForNorth")
	arg_8_0.paintingListTF = arg_8_0.findTF("PaintingList")
	arg_8_0.backBtn = arg_8_0.findTF("top/back_button", arg_8_0.northTF)
	arg_8_0.gradeContainer = arg_8_0.findTF("GradeContainer", arg_8_0.northTF)
	arg_8_0.seasonBestPointText = arg_8_0.findTF("SeasonBestPoint/Text", arg_8_0.gradeContainer)
	arg_8_0.activityBestPointText = arg_8_0.findTF("ActivityBestPoint/Text", arg_8_0.gradeContainer)
	arg_8_0.seasonLevelNumText = arg_8_0.findTF("SeasonLevelNum/Text", arg_8_0.gradeContainer)
	arg_8_0.activityLevelNumText = arg_8_0.findTF("ActivityLevelNum/Text", arg_8_0.gradeContainer)
	arg_8_0.timeTipTF = arg_8_0.findTF("TimeTip", arg_8_0.northTF)
	arg_8_0.activityTimeText = arg_8_0.findTF("ActivityTimeText", arg_8_0.timeTipTF)
	arg_8_0.seasonDayText = arg_8_0.findTF("SeasonTipText/DayText", arg_8_0.timeTipTF)
	arg_8_0.seasonTimeText = arg_8_0.findTF("SeasonTimeText", arg_8_0.timeTipTF)
	arg_8_0.switchModTF = arg_8_0.findTF("SwitchMod", arg_8_0.northTF)
	arg_8_0.casualModBtn = arg_8_0.findTF("NormalBtn", arg_8_0.switchModTF)
	arg_8_0.infiniteModBtn = arg_8_0.findTF("EndlessBtn", arg_8_0.switchModTF)
	arg_8_0.casualModBtnBG = arg_8_0.findTF("BG", arg_8_0.casualModBtn)
	arg_8_0.infiniteModBtnBG = arg_8_0.findTF("BG", arg_8_0.infiniteModBtn)
	arg_8_0.casualModBtnSC = GetComponent(arg_8_0.casualModBtn, "Button")
	arg_8_0.infiniteModBtnSC = GetComponent(arg_8_0.infiniteModBtn, "Button")
	arg_8_0.functionBtnsTF = arg_8_0.findTF("FunctionBtns", arg_8_0.northTF)
	arg_8_0.rankBtn = arg_8_0.findTF("RankBtn", arg_8_0.functionBtnsTF)
	arg_8_0.startBtn = arg_8_0.findTF("StartBtn", arg_8_0.functionBtnsTF)
	arg_8_0.resetBtn = arg_8_0.findTF("ResetBtn", arg_8_0.functionBtnsTF)
	arg_8_0.startBtnBanned = arg_8_0.findTF("StartBtnBanned", arg_8_0.functionBtnsTF)
	arg_8_0.resetBtnBanned = arg_8_0.findTF("ResetBtnBanned", arg_8_0.functionBtnsTF)
	arg_8_0.awardTF = arg_8_0.findTF("Award", arg_8_0.northTF)
	arg_8_0.helpBtn = arg_8_0.findTF("HelpBtn", arg_8_0.awardTF)
	arg_8_0.getBtn = arg_8_0.findTF("GetBtn", arg_8_0.awardTF)
	arg_8_0.gotBtn = arg_8_0.findTF("GotBtn", arg_8_0.awardTF)
	arg_8_0.getBtnBanned = arg_8_0.findTF("GetBtnBanned", arg_8_0.awardTF)
	arg_8_0.itemTF = arg_8_0.findTF("ItemBG/item", arg_8_0.awardTF)
	arg_8_0.scoreText = arg_8_0.findTF("Score/ScoreText", arg_8_0.awardTF)
	arg_8_0.slider = arg_8_0.findTF("Slider", arg_8_0.northTF)
	arg_8_0.squareContainer = arg_8_0.findTF("SquareList", arg_8_0.slider)
	arg_8_0.squareTpl = arg_8_0.findTF("Squre", arg_8_0.slider)
	arg_8_0.squareList = UIItemList.New(arg_8_0.squareContainer, arg_8_0.squareTpl)
	arg_8_0.sliderSC = GetComponent(arg_8_0.slider, "Slider")
	arg_8_0.paintingContainer = arg_8_0.findTF("PaintingList")
	arg_8_0.scrollSC = GetComponent(arg_8_0.paintingContainer, "Slider")
	arg_8_0.material = arg_8_0.findTF("material").GetComponent(typeof(Image)).material
	arg_8_0.material1 = arg_8_0.findTF("material1").GetComponent(typeof(Image)).material
	arg_8_0.painting = arg_8_0.findTF("Painting", arg_8_0.paintingContainer)
	arg_8_0.paintingShadow1 = arg_8_0.findTF("PaintingShadow1", arg_8_0.painting)
	arg_8_0.paintingShadow2 = arg_8_0.findTF("PaintingShadow2", arg_8_0.painting)
	arg_8_0.bossInfoImg = arg_8_0.findTF("InfoImg", arg_8_0.painting)
	arg_8_0.roundNumText = arg_8_0.findTF("Round/NumText", arg_8_0.painting)
	arg_8_0.completeEffectTF = arg_8_0.findTF("TZ02", arg_8_0.painting)

	SetActive(arg_8_0.completeEffectTF, False)

	arg_8_0.card1TF = arg_8_0.findTF("Card1", arg_8_0.paintingContainer)
	arg_8_0.shipPaintImg_1 = arg_8_0.findTF("Mask/ShipPaint", arg_8_0.card1TF)
	arg_8_0.tag_1 = arg_8_0.findTF("Tag", arg_8_0.card1TF)
	arg_8_0.mask_1 = arg_8_0.findTF("Mask", arg_8_0.card1TF)
	arg_8_0.roundTF_1 = arg_8_0.findTF("Round", arg_8_0.card1TF)
	arg_8_0.roundText_1 = arg_8_0.findTF("Round/RoundText", arg_8_0.card1TF)
	arg_8_0.card2TF = arg_8_0.findTF("Card2", arg_8_0.paintingContainer)
	arg_8_0.shipPaintImg_2 = arg_8_0.findTF("Mask/ShipPaint", arg_8_0.card2TF)
	arg_8_0.tag_2 = arg_8_0.findTF("Tag", arg_8_0.card2TF)
	arg_8_0.mask_2 = arg_8_0.findTF("Mask", arg_8_0.card2TF)
	arg_8_0.roundTF_2 = arg_8_0.findTF("Round", arg_8_0.card2TF)
	arg_8_0.roundText_2 = arg_8_0.findTF("Round/RoundText", arg_8_0.card2TF)
	arg_8_0.modTipBtn = arg_8_0.findTF("ModTipBtn", arg_8_0.northTF)
	arg_8_0.modTipTF = arg_8_0.findTF("TipText", arg_8_0.northTF)
	arg_8_0.modTipText = arg_8_0.findTF("Text", arg_8_0.modTipTF)

	setActive(arg_8_0.modTipTF, False)

	arg_8_0.fleetSelect = arg_8_0.findTF("LevelFleetSelectView")
	arg_8_0.fleetEditPanel = ActivityFleetPanel.New(arg_8_0.fleetSelect.gameObject)

	function arg_8_0.fleetEditPanel.onCancel()
		arg_8_0.hideFleetEdit()

	function arg_8_0.fleetEditPanel.onCommit()
		arg_8_0.commitEdit()

	function arg_8_0.fleetEditPanel.onCombat()
		arg_8_0.commitEdit()
		arg_8_0.emit(ChallengeMainMediator.ON_PRECOMBAT, arg_8_0.curMode)

	function arg_8_0.fleetEditPanel.onLongPressShip(arg_12_0, arg_12_1)
		arg_8_0.openShipInfo(arg_12_0, arg_12_1)

	arg_8_0.buildCommanderPanel()

def var_0_0.tryPlayGuide(arg_13_0):
	pg.SystemGuideMgr.GetInstance().Play(arg_13_0)

def var_0_0.initData(arg_14_0):
	arg_14_0.challengeProxy = getProxy(ChallengeProxy)
	arg_14_0.challengeInfo = arg_14_0.challengeProxy.getChallengeInfo()
	arg_14_0.userChallengeInfoList = arg_14_0.challengeProxy.getUserChallengeInfoList()
	arg_14_0.timeOverTag = False

	arg_14_0.updateData()

	arg_14_0.openedCommanerSystem = True

def var_0_0.addListener(arg_15_0):
	onButton(arg_15_0, arg_15_0.backBtn, function()
		arg_15_0.emit(var_0_0.ON_BACK), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.challenge_help.tip
		}), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.rankBtn, function()
		arg_15_0.emit(ChallengeMainMediator.ON_OPEN_RANK), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.startBtn, function()
		local var_19_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CHALLENGE)

		if not var_19_0 or var_19_0.isEnd():
			pg.TipsMgr.GetInstance().ShowTips(i18n("challenge_end_tip"))
			triggerButton(arg_15_0.backBtn)

			return

		if arg_15_0.isCrossedSeason() == True:
			local var_19_1 = arg_15_0.challengeProxy.getCurMode()

			if not arg_15_0.curModeInfo:
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					hideNo = True,
					content = i18n("challenge_season_update"),
					def onYes:()
						arg_15_0.emit(ChallengeConst.RESET_DATA_EVENT, var_19_1),
					def onNo:()
						arg_15_0.emit(ChallengeConst.RESET_DATA_EVENT, var_19_1)
				})

				return
			else
				local var_19_2 = var_19_1 == ChallengeProxy.MODE_CASUAL and "challenge_season_update_casual_clear" or "challenge_season_update_infinite_clear"
				local var_19_3 = var_19_1 == ChallengeProxy.MODE_CASUAL and arg_15_0.curModeInfo.getScore() or arg_15_0.curModeInfo.getLevel()

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					hideNo = False,
					content = i18n(var_19_2, var_19_3),
					def onNo:()
						arg_15_0.emit(ChallengeConst.RESET_DATA_EVENT, var_19_1),
					def onYes:()
						arg_15_0.emit(ChallengeMainMediator.ON_PRECOMBAT, arg_15_0.curMode)
				})

				return

		if not arg_15_0.curModeInfo:
			arg_15_0.doOnFleetPanel()

			return

		arg_15_0.emit(ChallengeMainMediator.ON_PRECOMBAT, arg_15_0.curMode), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.resetBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = False,
			content = i18n("challenge_normal_reset"),
			def onYes:()
				arg_15_0.emit(ChallengeConst.RESET_DATA_EVENT, arg_15_0.challengeProxy.getCurMode())
		}), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.modTipBtn, function()
		arg_15_0.showTipText())

	local function var_15_0()
		if arg_15_0.showingIndex % ChallengeConst.BOSS_NUM == 1:
			return

		arg_15_0.showingIndex = arg_15_0.showingIndex - 1

		arg_15_0.updatePaintingList(arg_15_0.nameList, arg_15_0.showingIndex)
		arg_15_0.updateRoundText(arg_15_0.showingIndex)
		arg_15_0.updateSlider(arg_15_0.showingIndex)

	local function var_15_1()
		if arg_15_0.showingIndex % ChallengeConst.BOSS_NUM == 0:
			return

		arg_15_0.showingIndex = arg_15_0.showingIndex + 1

		arg_15_0.updatePaintingList(arg_15_0.nameList, arg_15_0.showingIndex)
		arg_15_0.updateRoundText(arg_15_0.showingIndex)
		arg_15_0.updateSlider(arg_15_0.showingIndex)

	addSlip(SLIP_TYPE_HRZ, arg_15_0.paintingContainer, var_15_0, var_15_1)

def var_0_0.updateData(arg_29_0):
	arg_29_0.curMode = arg_29_0.challengeProxy.getCurMode()
	arg_29_0.curModeInfo = arg_29_0.userChallengeInfoList[arg_29_0.curMode]
	arg_29_0.timeOverTag = False

	if not arg_29_0.curModeInfo:
		arg_29_0.curLevel = 1
		arg_29_0.showingIndex = arg_29_0.curLevel

		if arg_29_0.curMode == ChallengeProxy.MODE_CASUAL:
			arg_29_0.dungeonIDList = arg_29_0.challengeInfo.getDungeonIDList()
		elif arg_29_0.curMode == ChallengeProxy.MODE_INFINITE:
			local var_29_0 = arg_29_0.challengeInfo.getSeasonID()
			local var_29_1 = arg_29_0.challengeInfo.getActivityIndex()

			arg_29_0.dungeonIDList = pg.activity_event_challenge[var_29_1].infinite_stage[var_29_0][1]
	else
		arg_29_0.curLevel = arg_29_0.curModeInfo.getLevel()
		arg_29_0.showingIndex = arg_29_0.curLevel
		arg_29_0.dungeonIDList = arg_29_0.curModeInfo.getDungeonIDList()

		print("self.dungeonIDList", tostring(arg_29_0.dungeonIDList))

	arg_29_0.nameList = {}

	print("创建nameList", tostring(arg_29_0.nameList), tostring(arg_29_0.dungeonIDList), tostring(#arg_29_0.dungeonIDList))

	arg_29_0.infoNameList = {}

	for iter_29_0, iter_29_1 in ipairs(arg_29_0.dungeonIDList):
		local var_29_2 = pg.expedition_challenge_template[iter_29_1].char_icon[1]

		arg_29_0.nameList[iter_29_0] = var_29_2

		print("self.nameList", tostring(var_29_2))

		local var_29_3 = pg.expedition_challenge_template[iter_29_1].name_p

		arg_29_0.infoNameList[iter_29_0] = var_29_3

	arg_29_0.nextNameList = {}

	if arg_29_0.curMode == ChallengeProxy.MODE_INFINITE:
		local var_29_4

		if arg_29_0.curModeInfo:
			var_29_4 = arg_29_0.curModeInfo.getNextInfiniteDungeonIDList()
		else
			local var_29_5 = arg_29_0.challengeInfo.getSeasonID()
			local var_29_6 = arg_29_0.challengeInfo.getActivityIndex()

			if pg.activity_event_challenge[var_29_6].infinite_stage[var_29_5][2]:
				var_29_4 = pg.activity_event_challenge[var_29_6].infinite_stage[var_29_5][2]
			else
				var_29_4 = pg.activity_event_challenge[var_29_6].infinite_stage[var_29_5][1]

		for iter_29_2, iter_29_3 in ipairs(var_29_4):
			local var_29_7 = pg.expedition_challenge_template[iter_29_3].char_icon[1]

			arg_29_0.nextNameList[iter_29_2 + ChallengeConst.BOSS_NUM] = var_29_7

def var_0_0.updatePaintingList(arg_30_0, arg_30_1, arg_30_2):
	local var_30_0 = arg_30_1 or arg_30_0.nameList
	local var_30_1 = arg_30_2 or arg_30_0.showingIndex
	local var_30_2 = arg_30_0.curLevel

	if var_30_1 > ChallengeConst.BOSS_NUM:
		var_30_1 = var_30_1 % ChallengeConst.BOSS_NUM == 0 and ChallengeConst.BOSS_NUM or var_30_1 % ChallengeConst.BOSS_NUM

	if arg_30_0.curMode == ChallengeProxy.MODE_INFINITE and var_30_2 > ChallengeConst.BOSS_NUM:
		var_30_2 = var_30_2 % ChallengeConst.BOSS_NUM == 0 and ChallengeConst.BOSS_NUM or var_30_2 % ChallengeConst.BOSS_NUM

	local function var_30_3(arg_31_0)
		arg_31_0.material.SetFloat("_LineGray", 0.3)
		arg_31_0.material.SetFloat("_TearDistance", 0)
		LeanTween.cancel(arg_31_0.gameObject)
		LeanTween.value(arg_31_0.gameObject, 0, 2, 2).setLoopClamp().setOnUpdate(System.Action_float(function(arg_32_0)
			if arg_32_0 >= 1.2:
				arg_31_0.material.SetFloat("_LineGray", 0.3)
			elif arg_32_0 >= 1.1:
				arg_31_0.material.SetFloat("_LineGray", 0.45)
			elif arg_32_0 >= 1.03:
				arg_31_0.material.SetFloat("_TearDistance", 0)
			elif arg_32_0 >= 1:
				arg_31_0.material.SetFloat("_TearDistance", 0.3)
			elif arg_32_0 >= 0.35:
				arg_31_0.material.SetFloat("_LineGray", 0.3)
			elif arg_32_0 >= 0.3:
				arg_31_0.material.SetFloat("_LineGray", 0.4)
			elif arg_32_0 >= 0.25:
				arg_31_0.material.SetFloat("_LineGray", 0.3)
			elif arg_32_0 >= 0.2:
				arg_31_0.material.SetFloat("_LineGray", 0.4)))

	setPaintingPrefabAsync(arg_30_0.painting, var_30_0[var_30_1], "chuanwu", function()
		local var_33_0 = arg_30_0.findTF("fitter", arg_30_0.painting).GetChild(0)

		if var_33_0:
			local var_33_1 = GetComponent(var_33_0, "MeshImage")
			local var_33_2 = var_30_2 - 1 - var_30_1 >= 0

			SetActive(arg_30_0.completeEffectTF, var_33_2)

			if var_33_2:
				var_33_1.material = arg_30_0.material1

				var_33_1.material.SetFloat("_LineDensity", 7)
				var_30_3(var_33_1)
			else
				var_33_1.material = arg_30_0.material

				var_33_1.material.SetFloat("_Range", 16)
				var_33_1.material.SetFloat("_Degree", 7))
	setPaintingPrefabAsync(arg_30_0.paintingShadow1, var_30_0[var_30_1], "chuanwu", function()
		local var_34_0 = arg_30_0.findTF("fitter", arg_30_0.paintingShadow1).GetChild(0)

		if var_34_0:
			var_34_0.GetComponent("Image").color = Color.New(0, 0, 0, 0.44))
	setPaintingPrefabAsync(arg_30_0.paintingShadow2, var_30_0[var_30_1], "chuanwu", function()
		local var_35_0 = arg_30_0.findTF("fitter", arg_30_0.paintingShadow2).GetChild(0)

		if var_35_0:
			var_35_0.GetComponent("Image").color = Color.New(1, 1, 1, 0.15))
	LoadSpriteAsync("ChallengeBossInfo/" .. arg_30_0.infoNameList[var_30_1], function(arg_36_0)
		setImageSprite(arg_30_0.bossInfoImg, arg_36_0, True))

	if var_0_0.BOSS_NUM - var_30_1 >= 2:
		setActive(arg_30_0.roundTF_1, True)
		setActive(arg_30_0.roundTF_2, True)
		setActive(arg_30_0.mask_1, True)
		setActive(arg_30_0.mask_2, True)
		LoadSpriteAsync("shipYardIcon/" .. var_30_0[var_30_1 + 1], function(arg_37_0)
			setImageSprite(arg_30_0.shipPaintImg_1, arg_37_0))
		LoadSpriteAsync("shipYardIcon/" .. var_30_0[var_30_1 + 2], function(arg_38_0)
			setImageSprite(arg_30_0.shipPaintImg_2, arg_38_0))
	elif var_0_0.BOSS_NUM - var_30_1 == 1:
		setActive(arg_30_0.roundTF_1, True)
		setActive(arg_30_0.roundTF_2, False)
		setActive(arg_30_0.mask_1, True)
		setActive(arg_30_0.mask_2, False)
		LoadSpriteAsync("shipYardIcon/" .. var_30_0[var_30_1 + 1], function(arg_39_0)
			setImageSprite(arg_30_0.shipPaintImg_1, arg_39_0))

		if arg_30_0.curMode == ChallengeProxy.MODE_INFINITE:
			LoadSpriteAsync("shipYardIcon/" .. arg_30_0.nextNameList[var_30_1 + 2], function(arg_40_0)
				setImageSprite(arg_30_0.shipPaintImg_2, arg_40_0)
				setActive(arg_30_0.mask_2, True)
				setActive(arg_30_0.roundTF_2, True))
	else
		setActive(arg_30_0.roundTF_1, False)
		setActive(arg_30_0.roundTF_2, False)
		setActive(arg_30_0.mask_1, False)
		setActive(arg_30_0.mask_2, False)

		if arg_30_0.curMode == ChallengeProxy.MODE_INFINITE:
			LoadSpriteAsync("shipYardIcon/" .. arg_30_0.nextNameList[var_30_1 + 1], function(arg_41_0)
				setImageSprite(arg_30_0.shipPaintImg_1, arg_41_0)
				setActive(arg_30_0.mask_1, True)
				setActive(arg_30_0.roundTF_1, True))
			LoadSpriteAsync("shipYardIcon/" .. arg_30_0.nextNameList[var_30_1 + 2], function(arg_42_0)
				setImageSprite(arg_30_0.shipPaintImg_2, arg_42_0)
				setActive(arg_30_0.mask_2, True)
				setActive(arg_30_0.roundTF_2, True))

	if var_30_2 - 1 - var_30_1 >= 2:
		setActive(arg_30_0.tag_1, True)
		setActive(arg_30_0.tag_2, True)
	elif var_30_2 - 1 - var_30_1 == 1:
		setActive(arg_30_0.tag_1, True)
		setActive(arg_30_0.tag_2, False)
	elif var_30_2 - 1 - var_30_1 <= 0:
		setActive(arg_30_0.tag_1, False)
		setActive(arg_30_0.tag_2, False)

def var_0_0.updateRoundText(arg_43_0, arg_43_1):
	local var_43_0 = arg_43_1 or arg_43_0.showingIndex

	if arg_43_0.curMode == ChallengeProxy.MODE_CASUAL and var_43_0 > ChallengeConst.BOSS_NUM:
		var_43_0 = var_43_0 % ChallengeConst.BOSS_NUM == 0 and ChallengeConst.BOSS_NUM or var_43_0 % ChallengeConst.BOSS_NUM

	setText(arg_43_0.roundNumText, string.format("%02d", var_43_0))
	setText(arg_43_0.roundText_1, "Round" .. var_43_0 + 1)
	setText(arg_43_0.roundText_2, "Round" .. var_43_0 + 2)

def var_0_0.updateSlider(arg_44_0, arg_44_1):
	local var_44_0 = arg_44_1 or arg_44_0.showingIndex
	local var_44_1 = arg_44_0.curLevel

	if var_44_0 > ChallengeConst.BOSS_NUM:
		var_44_0 = var_44_0 % ChallengeConst.BOSS_NUM == 0 and ChallengeConst.BOSS_NUM or var_44_0 % ChallengeConst.BOSS_NUM

	if arg_44_0.curMode == ChallengeProxy.MODE_INFINITE and var_44_1 > ChallengeConst.BOSS_NUM:
		var_44_1 = var_44_1 % ChallengeConst.BOSS_NUM == 0 and ChallengeConst.BOSS_NUM or var_44_1 % ChallengeConst.BOSS_NUM

	local var_44_2 = 1 / (ChallengeConst.BOSS_NUM - 1)
	local var_44_3 = (var_44_1 - 1) * var_44_2

	arg_44_0.sliderSC.value = var_44_3

	arg_44_0.squareList.make(function(arg_45_0, arg_45_1, arg_45_2)
		local var_45_0 = arg_44_0.findTF("UnFinished", arg_45_2)
		local var_45_1 = arg_44_0.findTF("Finished", arg_45_2)
		local var_45_2 = arg_44_0.findTF("Challengeing", arg_45_2)
		local var_45_3 = arg_44_0.findTF("Arrow", arg_45_2)

		local function var_45_4()
			setActive(var_45_1, True)
			setActive(var_45_0, False)
			setActive(var_45_2, False)

		local function var_45_5()
			setActive(var_45_1, False)
			setActive(var_45_0, True)
			setActive(var_45_2, False)

		local function var_45_6()
			setActive(var_45_1, False)
			setActive(var_45_0, False)
			setActive(var_45_2, True)

		if arg_45_0 == UIItemList.EventUpdate:
			if arg_45_1 + 1 < var_44_1:
				var_45_4()
			elif arg_45_1 + 1 == var_44_1:
				var_45_6()
			elif arg_45_1 + 1 > var_44_1:
				var_45_5()

			if arg_45_1 + 1 == var_44_0:
				setActive(var_45_3, True)
			else
				setActive(var_45_3, False))
	arg_44_0.squareList.align(ChallengeConst.BOSS_NUM)

def var_0_0.updateGrade(arg_49_0, arg_49_1):
	setText(arg_49_0.seasonBestPointText, arg_49_1.seasonMaxScore)
	setText(arg_49_0.activityBestPointText, arg_49_1.activityMaxScore)
	setText(arg_49_0.seasonLevelNumText, arg_49_1.seasonMaxLevel)
	setText(arg_49_0.activityLevelNumText, arg_49_1.activityMaxLevel)

def var_0_0.updateTimePanel(arg_50_0):
	local var_50_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CHALLENGE).stopTime
	local var_50_1 = pg.TimeMgr.GetInstance().STimeDescS(var_50_0, "%Y.%m.%d")

	setText(arg_50_0.activityTimeText, var_50_1)

	local var_50_2 = pg.TimeMgr.GetInstance()
	local var_50_3 = var_50_2.GetNextWeekTime(1, 0, 0, 0) - var_50_2.GetServerTime()
	local var_50_4, var_50_5, var_50_6, var_50_7 = var_50_2.parseTimeFrom(var_50_3)

	setText(arg_50_0.seasonDayText, var_50_4)
	setText(arg_50_0.seasonTimeText, string.format("%02d.%02d.%02d", var_50_5, var_50_6, var_50_7))

	if arg_50_0.timer:
		arg_50_0.timer.Stop()

	arg_50_0.timer = Timer.New(function()
		var_50_3 = var_50_3 - 1

		local var_51_0, var_51_1, var_51_2, var_51_3 = pg.TimeMgr.GetInstance().parseTimeFrom(var_50_3)

		setText(arg_50_0.seasonDayText, var_51_0)
		setText(arg_50_0.seasonTimeText, string.format("%02d.%02d.%02d", var_51_1, var_51_2, var_51_3))

		if var_50_3 <= 0:
			arg_50_0.timeOverTag = True

			arg_50_0.timer.Stop(), 1, -1)

	arg_50_0.timer.Start()

def var_0_0.updateSwitchModBtn(arg_52_0):
	if not arg_52_0.isFinishedCasualMode():
		setActive(arg_52_0.infiniteModBtn, False)
	else
		setActive(arg_52_0.infiniteModBtn, True)

	if arg_52_0.curMode == ChallengeProxy.MODE_CASUAL:
		setActive(arg_52_0.casualModBtnBG, True)
		setActive(arg_52_0.infiniteModBtnBG, False)
	else
		setActive(arg_52_0.casualModBtnBG, False)
		setActive(arg_52_0.infiniteModBtnBG, True)

	onButton(arg_52_0, arg_52_0.casualModBtn, function()
		if arg_52_0.curMode == ChallengeProxy.MODE_CASUAL:
			return

		local var_53_0 = arg_52_0.curModeInfo and arg_52_0.curModeInfo.getLevel() or 0

		local function var_53_1()
			arg_52_0.challengeProxy.setCurMode(ChallengeProxy.MODE_CASUAL)
			setActive(arg_52_0.casualModBtnBG, True)
			setActive(arg_52_0.infiniteModBtnBG, False)
			arg_52_0.updateData()
			arg_52_0.updatePaintingList(arg_52_0.nameList, arg_52_0.showingIndex)
			arg_52_0.updateRoundText(arg_52_0.showingIndex)
			arg_52_0.updateSlider(arg_52_0.showingIndex)
			arg_52_0.updateSwitchModBtn()
			arg_52_0.updateFuncBtns()
			arg_52_0.showTipText()

		if arg_52_0.isCrossedSeason():
			local var_53_2 = "challenge_season_update_infinite_switch"
			local var_53_3 = var_53_0

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = False,
				content = i18n(var_53_2, var_53_3),
				def onYes:()
					arg_52_0.emit(ChallengeConst.RESET_DATA_EVENT, ChallengeProxy.MODE_INFINITE),
				onNo = var_53_1
			})

			return

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = False,
			content = i18n("challenge_infinite_click_switch", var_53_0),
			onYes = var_53_1
		}), SFX_PANEL)
	onButton(arg_52_0, arg_52_0.infiniteModBtn, function()
		if arg_52_0.curMode == ChallengeProxy.MODE_INFINITE:
			return

		local var_56_0 = arg_52_0.curModeInfo and arg_52_0.curModeInfo.getScore() or arg_52_0.challengeInfo.getGradeList().seasonMaxScore

		local function var_56_1()
			arg_52_0.challengeProxy.setCurMode(ChallengeProxy.MODE_INFINITE)
			setActive(arg_52_0.casualModBtnBG, False)
			setActive(arg_52_0.infiniteModBtnBG, True)
			arg_52_0.updateData()
			arg_52_0.updatePaintingList(arg_52_0.nameList, arg_52_0.showingIndex)
			arg_52_0.updateRoundText(arg_52_0.showingIndex)
			arg_52_0.updateSlider(arg_52_0.showingIndex)
			arg_52_0.updateFuncBtns()
			arg_52_0.showTipText()

		if arg_52_0.isCrossedSeason():
			local var_56_2 = "challenge_season_update_casual_switch"
			local var_56_3 = var_56_0

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = False,
				content = i18n(var_56_2, var_56_3),
				def onYes:()
					arg_52_0.emit(ChallengeConst.RESET_DATA_EVENT, ChallengeProxy.MODE_CASUAL),
				onNo = var_56_1
			})

			return

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = False,
			content = i18n("challenge_casual_click_switch", var_56_0),
			onYes = var_56_1
		}), SFX_PANEL)

def var_0_0.updateResetBtn(arg_59_0):
	if arg_59_0.userChallengeInfoList[arg_59_0.curMode]:
		setActive(arg_59_0.resetBtn, True)
		SetActive(arg_59_0.resetBtnBanned, False)
	else
		setActive(arg_59_0.resetBtn, False)
		SetActive(arg_59_0.resetBtnBanned, True)

def var_0_0.updateStartBtn(arg_60_0):
	local var_60_0 = arg_60_0.userChallengeInfoList[arg_60_0.curMode]

	if var_60_0:
		if arg_60_0.curMode == ChallengeProxy.MODE_CASUAL and var_60_0.getLevel() > ChallengeConst.BOSS_NUM:
			SetActive(arg_60_0.startBtn, False)
			SetActive(arg_60_0.startBtnBanned, True)
		else
			SetActive(arg_60_0.startBtn, True)
			SetActive(arg_60_0.startBtnBanned, False)
	else
		SetActive(arg_60_0.startBtn, True)
		SetActive(arg_60_0.startBtnBanned, False)

def var_0_0.updateFuncBtns(arg_61_0):
	arg_61_0.updateResetBtn()
	arg_61_0.updateStartBtn()

def var_0_0.updateAwardPanel(arg_62_0):
	local var_62_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CHALLENGE)
	local var_62_1 = pg.activity_template[var_62_0.id].config_data[1]
	local var_62_2 = pg.activity_template[var_62_1].config_data[1]
	local var_62_3 = getProxy(TaskProxy).getTaskById(var_62_2) or getProxy(TaskProxy).getFinishTaskById(var_62_2)
	local var_62_4 = var_62_3.getConfig("target_num")
	local var_62_5 = arg_62_0.challengeInfo.getGradeList().activityMaxScore

	setText(arg_62_0.scoreText, var_62_5 .. " / " .. var_62_4)

	local var_62_6 = var_62_3.getTaskStatus()

	if var_62_6 == 0:
		setActive(arg_62_0.getBtn, False)
		setActive(arg_62_0.getBtnBanned, True)
		setActive(arg_62_0.gotBtn, False)
	elif var_62_6 == 1:
		setActive(arg_62_0.getBtn, True)
		setActive(arg_62_0.getBtnBanned, False)
		setActive(arg_62_0.gotBtn, False)
	elif var_62_6 == 2:
		setActive(arg_62_0.getBtn, False)
		setActive(arg_62_0.getBtnBanned, False)
		setActive(arg_62_0.gotBtn, True)

	local var_62_7 = var_62_3.getConfig("award_display")[1]
	local var_62_8 = {
		type = var_62_7[1],
		id = var_62_7[2],
		count = var_62_7[3]
	}

	updateDrop(arg_62_0.itemTF, var_62_8)
	onButton(arg_62_0, arg_62_0.itemTF, function()
		arg_62_0.emit(BaseUI.ON_DROP, var_62_8), SFX_PANEL)
	onButton(arg_62_0, arg_62_0.getBtn, function()
		arg_62_0.emit(ChallengeConst.CLICK_GET_AWARD_BTN, var_62_3.id), SFX_PANEL)

	local var_62_9

def var_0_0.showSLResetMsgBox(arg_65_0):
	local var_65_0 = False
	local var_65_1
	local var_65_2

	for iter_65_0, iter_65_1 in pairs(arg_65_0.userChallengeInfoList):
		if iter_65_1.getResetFlag() >= ChallengeConst.NEED_TO_RESET_SAVELOAD:
			var_65_0 = True
			var_65_1 = iter_65_1
			var_65_2 = iter_65_0

			break

	if var_65_0 == True:
		local var_65_3
		local var_65_4

		if var_65_2 == ChallengeProxy.MODE_CASUAL:
			var_65_3 = "challenge_casual_reset"
			var_65_4 = var_65_1.getScore()
		elif var_65_2 == ChallengeProxy.MODE_INFINITE:
			var_65_3 = "challenge_infinite_reset"
			var_65_4 = var_65_1.getLevel() - 1

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = i18n(var_65_3, var_65_4),
			def onYes:()
				arg_65_0.emit(ChallengeConst.RESET_DATA_EVENT, var_65_2),
			def onNo:()
				arg_65_0.emit(ChallengeConst.RESET_DATA_EVENT, var_65_2)
		})

def var_0_0.showTipText(arg_68_0):
	local var_68_0
	local var_68_1 = arg_68_0.curMode == ChallengeProxy.MODE_CASUAL and "challenge_normal_tip" or "challenge_unlimited_tip"

	setText(arg_68_0.modTipText, i18n(var_68_1))

	local var_68_2 = arg_68_0.modTipTF.GetComponent(typeof(DftAniEvent))

	if var_68_2:
		var_68_2.SetEndEvent(function(arg_69_0)
			setActive(arg_68_0.modTipText, False)
			setActive(arg_68_0.modTipTF, False))

	setActive(arg_68_0.modTipTF, True)
	setActive(arg_68_0.modTipText, True)

def var_0_0.doOnFleetPanel(arg_70_0):
	arg_70_0.fleetEditPanel.attach(arg_70_0)
	arg_70_0.fleetEditPanel.setFleets(arg_70_0.fleets[arg_70_0.curMode])
	arg_70_0.fleetEditPanel.set(1, 1)
	pg.UIMgr.GetInstance().BlurPanel(arg_70_0.fleetEditPanel._tf)

def var_0_0.isFinishedCasualMode(arg_71_0):
	local var_71_0 = False
	local var_71_1 = arg_71_0.userChallengeInfoList[ChallengeProxy.MODE_INFINITE]
	local var_71_2 = arg_71_0.userChallengeInfoList[ChallengeProxy.MODE_CASUAL]

	if var_71_1:
		var_71_0 = True
	elif not var_71_1:
		local var_71_3 = arg_71_0.challengeInfo.getGradeList().seasonMaxLevel

		if var_71_2:
			if var_71_2.getSeasonID() == arg_71_0.challengeInfo.getSeasonID():
				if var_71_3 >= ChallengeConst.BOSS_NUM:
					var_71_0 = True
				else
					var_71_0 = False
			else
				var_71_0 = False
		elif var_71_3 >= ChallengeConst.BOSS_NUM:
			var_71_0 = True
		elif not var_71_2:
			var_71_0 = False

	return var_71_0

def var_0_0.isCrossedSeason(arg_72_0):
	local var_72_0 = False

	if arg_72_0.timeOverTag == True:
		var_72_0 = True
	elif arg_72_0.curModeInfo:
		if arg_72_0.curModeInfo.getSeasonID() != arg_72_0.challengeInfo.getSeasonID():
			var_72_0 = True
	else
		var_72_0 = False

	return var_72_0

def var_0_0.commitEdit(arg_73_0):
	arg_73_0.emit(ChallengeMainMediator.ON_COMMIT_FLEET)

def var_0_0.openShipInfo(arg_74_0, arg_74_1, arg_74_2):
	arg_74_0.emit(ChallengeMainMediator.ON_FLEET_SHIPINFO, {
		shipId = arg_74_1,
		shipVOs = arg_74_2
	})

def var_0_0.hideFleetEdit(arg_75_0):
	setActive(arg_75_0.fleetSelect, False)
	arg_75_0.closeCommanderPanel()
	pg.UIMgr.GetInstance().UnblurPanel(arg_75_0.fleetSelect, arg_75_0._tf)
	setParent(arg_75_0.fleetSelect, arg_75_0._tf, False)

def var_0_0.updateEditPanel(arg_76_0):
	arg_76_0.fleetEditPanel.setFleets(arg_76_0.fleets[arg_76_0.curMode])
	arg_76_0.fleetEditPanel.updateFleets()

def var_0_0.setCommanderPrefabs(arg_77_0, arg_77_1):
	arg_77_0.commanderPrefabs = arg_77_1

def var_0_0.openCommanderPanel(arg_78_0, arg_78_1, arg_78_2):
	local var_78_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CHALLENGE).id

	arg_78_0.levelCMDFormationView.setCallback(function(arg_79_0)
		if arg_79_0.type == LevelUIConst.COMMANDER_OP_SHOW_SKILL:
			arg_78_0.emit(ChallengeMainMediator.ON_COMMANDER_SKILL, arg_79_0.skill)
		elif arg_79_0.type == LevelUIConst.COMMANDER_OP_ADD:
			arg_78_0.contextData.eliteCommanderSelected = {
				fleetIndex = arg_78_2,
				cmdPos = arg_79_0.pos,
				mode = arg_78_0.curMode
			}

			arg_78_0.emit(ChallengeMainMediator.ON_SELECT_ELITE_COMMANDER, arg_78_2, arg_79_0.pos)
			arg_78_0.closeCommanderPanel()
			arg_78_0.hideFleetEdit()
		else
			arg_78_0.emit(ChallengeMainMediator.COMMANDER_FORMATION_OP, {
				FleetType = LevelUIConst.FLEET_TYPE_ACTIVITY,
				data = arg_79_0,
				fleetId = arg_78_1.id,
				actId = var_78_0
			}))
	arg_78_0.levelCMDFormationView.Load()
	arg_78_0.levelCMDFormationView.ActionInvoke("update", arg_78_1, arg_78_0.commanderPrefabs)
	arg_78_0.levelCMDFormationView.ActionInvoke("Show")

def var_0_0.closeCommanderPanel(arg_80_0):
	if arg_80_0.levelCMDFormationView.isShowing():
		arg_80_0.levelCMDFormationView.ActionInvoke("Hide")

def var_0_0.updateCommanderFleet(arg_81_0, arg_81_1):
	if arg_81_0.levelCMDFormationView.isShowing():
		arg_81_0.levelCMDFormationView.ActionInvoke("updateFleet", arg_81_1)

def var_0_0.updateCommanderPrefab(arg_82_0):
	if arg_82_0.levelCMDFormationView.isShowing():
		arg_82_0.levelCMDFormationView.ActionInvoke("updatePrefabs", arg_82_0.commanderPrefabs)

def var_0_0.buildCommanderPanel(arg_83_0):
	arg_83_0.levelCMDFormationView = LevelCMDFormationView.New(arg_83_0.fleetSelect, arg_83_0.event, arg_83_0.contextData)

def var_0_0.destroyCommanderPanel(arg_84_0):
	arg_84_0.levelCMDFormationView.Destroy()

	arg_84_0.levelCMDFormationView = None

return var_0_0
