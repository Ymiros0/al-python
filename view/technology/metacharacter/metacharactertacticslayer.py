local var_0_0 = class("MetaCharacterTacticsLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "MetaCharacterTacticsUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initUITextTips()
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.updateRedTag()
	arg_3_0.updateShipImg()
	arg_3_0.updateNamePanel()
	arg_3_0.updateChar()
	arg_3_0.updateSkillListPanel()
	arg_3_0.enablePartialBlur()

	if arg_3_0.contextData.isMainOpen:
		arg_3_0.contextData.isMainOpen = None

		arg_3_0.moveShipImg(True)

	arg_3_0.moveRightPanel()

def var_0_0.willExit(arg_4_0):
	arg_4_0.moveShipImg(False)
	arg_4_0.recycleChar()
	arg_4_0.disablePartialBlur()

def var_0_0.onBackPressed(arg_5_0):
	if isActive(arg_5_0.skillUnlockPanel):
		arg_5_0.closeUnlockSkillPanel()

		return
	else
		arg_5_0.emit(var_0_0.ON_BACK_PRESSED)

def var_0_0.initUITextTips(arg_6_0):
	local var_6_0 = arg_6_0.findTF("ExpPanel")
	local var_6_1 = arg_6_0.findTF("ExpEveryDay", var_6_0)

	setText(var_6_1, i18n("meta_exp_per_day"))

	local var_6_2 = arg_6_0.findTF("TaskPanel/StudySkillTip/TipText")

	setText(var_6_2, i18n("meta_skill_unlock"))

def var_0_0.initData(arg_7_0):
	arg_7_0.metaCharacterProxy = getProxy(MetaCharacterProxy)
	arg_7_0.bayProxy = getProxy(BayProxy)
	arg_7_0.shipPrefab = None
	arg_7_0.shipModel = None
	arg_7_0.curMetaShipID = arg_7_0.contextData.shipID
	arg_7_0.curShipVO = None
	arg_7_0.curMetaCharacterVO = None

	arg_7_0.updateData()

	arg_7_0.skillBtnList = {}
	arg_7_0.curUnlockSkillID = None
	arg_7_0.curUnlockMaterialID = None
	arg_7_0.curUnlockMaterialNeedCount = None

def var_0_0.updateData(arg_8_0):
	arg_8_0.curShipVO = arg_8_0.bayProxy.getShipById(arg_8_0.curMetaShipID)
	arg_8_0.curMetaCharacterVO = arg_8_0.curShipVO.getMetaCharacter()

def var_0_0.setTacticsData(arg_9_0, arg_9_1):
	arg_9_0.doubleExpValue = arg_9_1.doubleExp
	arg_9_0.normalExpValue = arg_9_1.normalExp
	arg_9_0.curSkillID = arg_9_1.curSkillID
	arg_9_0.switchCountLeft = arg_9_1.switchCount
	arg_9_0.taskInfoTable = arg_9_1.taskInfoTable
	arg_9_0.skillExpTable = arg_9_1.skillExpTable
	arg_9_1 = None

def var_0_0.switchTacticsSkillData(arg_10_0, arg_10_1, arg_10_2):
	arg_10_0.curSkillID = arg_10_1
	arg_10_0.switchCountLeft = arg_10_2

def var_0_0.levelupTacticsSkillData(arg_11_0, arg_11_1, arg_11_2):
	arg_11_0.skillExpTable[arg_11_1] = 0
	arg_11_0.switchCountLeft = arg_11_2

	arg_11_0.clearTaskInfo()

def var_0_0.updateSkillExp(arg_12_0, arg_12_1, arg_12_2):
	arg_12_0.skillExpTable[arg_12_1] = arg_12_2

def var_0_0.clearTaskInfo(arg_13_0, arg_13_1):
	arg_13_0.taskInfoTable[arg_13_1] = {}

def var_0_0.initUI(arg_14_0):
	arg_14_0.shipImg = arg_14_0.findTF("ShipImg")
	arg_14_0.nameTF = arg_14_0.findTF("NamePanel")
	arg_14_0.nameScrollText = arg_14_0.findTF("NameMask/NameText", arg_14_0.nameTF)
	arg_14_0.shipTypeImg = arg_14_0.findTF("TypeImg", arg_14_0.nameTF)
	arg_14_0.enNameText = arg_14_0.findTF("NameENText", arg_14_0.nameTF)

	local var_14_0 = arg_14_0.findTF("StarTpl", arg_14_0.nameTF)
	local var_14_1 = arg_14_0.findTF("StarContainer", arg_14_0.nameTF)

	arg_14_0.nameTFStarUIList = UIItemList.New(var_14_1, var_14_0)
	arg_14_0.expPanel = arg_14_0.findTF("ExpPanel")
	arg_14_0.expText = arg_14_0.findTF("ExpText", arg_14_0.expPanel)
	arg_14_0.expDoubleTag = arg_14_0.findTF("DoubleTag", arg_14_0.expText)
	arg_14_0.taskPanel = arg_14_0.findTF("TaskPanel")
	arg_14_0.qCharContainer = arg_14_0.findTF("QChar", arg_14_0.taskPanel)
	arg_14_0.taskTpl = arg_14_0.findTF("TaskTpl", arg_14_0.taskPanel)
	arg_14_0.taskScrollTF = arg_14_0.findTF("ScrollView", arg_14_0.taskPanel)
	arg_14_0.taskTplContainer = arg_14_0.findTF("ScrollView/Viewport/Content", arg_14_0.taskPanel)
	arg_14_0.taskScrollBar = arg_14_0.findTF("ScrollView/Scrollbar Vertical", arg_14_0.taskPanel)
	arg_14_0.taskUIItemList = UIItemList.New(arg_14_0.taskTplContainer, arg_14_0.taskTpl)
	arg_14_0.skillInfoPanel = arg_14_0.findTF("SkillInfo", arg_14_0.taskPanel)
	arg_14_0.curSkillIcon = arg_14_0.findTF("Skill/Icon", arg_14_0.skillInfoPanel)
	arg_14_0.curSkillNameScrollText = arg_14_0.findTF("NameMask/Name", arg_14_0.skillInfoPanel)
	arg_14_0.curSkillLevelText = arg_14_0.findTF("LevelInfo/CurLevel", arg_14_0.skillInfoPanel)
	arg_14_0.nextSkillLevelText = arg_14_0.findTF("LevelInfo/NextLevel", arg_14_0.skillInfoPanel)
	arg_14_0.curSkillDescText = arg_14_0.findTF("DescView/Viewport/SkillDesc", arg_14_0.skillInfoPanel)
	arg_14_0.curSkillProgressText = arg_14_0.findTF("ExpProgress/Text", arg_14_0.skillInfoPanel)
	arg_14_0.curSkillProgressSlider = arg_14_0.findTF("ExpSlider", arg_14_0.skillInfoPanel)
	arg_14_0.curSkillQuickBtn = arg_14_0.findTF("QuickBtn", arg_14_0.skillInfoPanel)
	arg_14_0.studySkillTip = arg_14_0.findTF("StudySkillTip", arg_14_0.taskPanel)
	arg_14_0.startSkillTip = arg_14_0.findTF("StartLearn", arg_14_0.taskPanel)
	arg_14_0.maxSkillTip = arg_14_0.findTF("SkillMax", arg_14_0.taskPanel)
	arg_14_0.studySkillBtn = arg_14_0.findTF("StartLearnBtn", arg_14_0.startSkillTip)
	arg_14_0.skillPanel = arg_14_0.findTF("SkillPanel")
	arg_14_0.skillTpl = arg_14_0.findTF("SkillTpl", arg_14_0.skillPanel)
	arg_14_0.skillContainer = arg_14_0.findTF("Skills/Content", arg_14_0.skillPanel)
	arg_14_0.skillUIItemList = UIItemList.New(arg_14_0.skillContainer, arg_14_0.skillTpl)
	arg_14_0.skillUnlockPanel = arg_14_0.findTF("SkillLearnBox")
	arg_14_0.skillUnlockPanelBG = arg_14_0.findTF("BG", arg_14_0.skillUnlockPanel)
	arg_14_0.skillUnlockPanelTipText = arg_14_0.findTF("Box/TipText", arg_14_0.skillUnlockPanel)
	arg_14_0.skillUnlockPanelCancelBtn = arg_14_0.findTF("Box/Btns/CancenBtn", arg_14_0.skillUnlockPanel)
	arg_14_0.skillUnlockPanelConfirmBtn = arg_14_0.findTF("Box/Btns/ConfirmBtn", arg_14_0.skillUnlockPanel)
	arg_14_0.materialTpl = arg_14_0.findTF("Box/Material", arg_14_0.skillUnlockPanel)
	arg_14_0.materialTplContainer = arg_14_0.findTF("Box/MaterialContainer", arg_14_0.skillUnlockPanel)
	arg_14_0.materialUIItemList = UIItemList.New(arg_14_0.materialTplContainer, arg_14_0.materialTpl)

def var_0_0.addListener(arg_15_0):
	onButton(arg_15_0, arg_15_0.skillUnlockPanelBG, function()
		arg_15_0.closeUnlockSkillPanel(), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.skillUnlockPanelCancelBtn, function()
		arg_15_0.closeUnlockSkillPanel(), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.skillUnlockPanelConfirmBtn, function()
		if not arg_15_0.curUnlockMaterialID:
			pg.TipsMgr.GetInstance().ShowTips(i18n("meta_unlock_skill_select"))

			return
		elif getProxy(BagProxy).getItemCountById(arg_15_0.curUnlockMaterialID) < arg_15_0.curUnlockMaterialNeedCount:
			pg.TipsMgr.GetInstance().ShowTips(i18n("word_materal_no_enough"))
		else
			local var_18_0 = 0
			local var_18_1 = 0
			local var_18_2 = arg_15_0.getMetaSkillTacticsConfigBySkillID(arg_15_0.curUnlockSkillID, 1).skill_unlock

			for iter_18_0, iter_18_1 in ipairs(var_18_2):
				if arg_15_0.curUnlockMaterialID == iter_18_1[2]:
					var_18_0 = iter_18_0
					var_18_1 = iter_18_1[3]

					break

			pg.m02.sendNotification(GAME.TACTICS_META_UNLOCK_SKILL, {
				shipID = arg_15_0.curMetaShipID,
				skillID = arg_15_0.curUnlockSkillID,
				materialIndex = var_18_0,
				materialInfo = {
					id = arg_15_0.curUnlockMaterialID,
					count = var_18_1
				}
			}), SFX_PANEL)

def var_0_0.updateRedTag(arg_19_0):
	arg_19_0.metaCharacterProxy.updateRedTag(arg_19_0.curMetaCharacterVO.id)

def var_0_0.updateShipImg(arg_20_0):
	local var_20_0, var_20_1 = MetaCharacterConst.GetMetaCharacterPaintPath(arg_20_0.curMetaCharacterVO.id, True)

	setImageSprite(arg_20_0.shipImg, LoadSprite(var_20_0, var_20_1), True)

	local var_20_2 = arg_20_0.curMetaCharacterVO.id
	local var_20_3 = MetaCharacterConst.UIConfig[var_20_2]

	setLocalPosition(arg_20_0.shipImg, {
		x = var_20_3[7],
		y = var_20_3[8]
	})
	setLocalScale(arg_20_0.shipImg, {
		x = var_20_3[3],
		y = var_20_3[4]
	})

def var_0_0.updateNamePanel(arg_21_0):
	local var_21_0 = arg_21_0.curShipVO
	local var_21_1 = arg_21_0.curMetaCharacterVO
	local var_21_2 = var_21_0.getName()

	setScrollText(arg_21_0.nameScrollText, var_21_2)

	local var_21_3 = var_21_0.getShipType()

	setImageSprite(arg_21_0.shipTypeImg, LoadSprite("shiptype", var_21_3))

	local var_21_4 = var_21_0.getConfig("english_name")

	setText(arg_21_0.enNameText, var_21_4)

	local var_21_5 = var_21_0.getMaxStar()
	local var_21_6 = var_21_0.getStar()

	arg_21_0.nameTFStarUIList.make(function(arg_22_0, arg_22_1, arg_22_2)
		if arg_22_0 == UIItemList.EventUpdate:
			local var_22_0 = arg_21_0.findTF("empty", arg_22_2)
			local var_22_1 = arg_21_0.findTF("on", arg_22_2)

			arg_22_1 = arg_22_1 + 1

			setActive(var_22_1, arg_22_1 <= var_21_6))
	arg_21_0.nameTFStarUIList.align(var_21_5)

def var_0_0.updateChar(arg_23_0):
	return

def var_0_0.recycleChar(arg_24_0):
	if arg_24_0.shipPrefab and arg_24_0.shipModel:
		PoolMgr.GetInstance().ReturnSpineChar(arg_24_0.shipPrefab, arg_24_0.shipModel)

		arg_24_0.shipPrefab = None
		arg_24_0.shipModel = None

def var_0_0.updateSkillListPanel(arg_25_0):
	local var_25_0 = arg_25_0.curShipVO
	local var_25_1 = arg_25_0.curMetaCharacterVO
	local var_25_2 = arg_25_0.getSkillIDListForShow(var_25_0.configId)

	arg_25_0.skillUIItemList.make(function(arg_26_0, arg_26_1, arg_26_2)
		if arg_26_0 == UIItemList.EventUpdate:
			local var_26_0 = var_25_2[arg_26_1 + 1]

			if var_26_0:
				arg_25_0.skillBtnList[var_26_0] = arg_26_2

				arg_25_0.updateSkillTF(arg_26_2, var_26_0))
	arg_25_0.skillUIItemList.align(#var_25_2)

def var_0_0.updateSkillTF(arg_27_0, arg_27_1, arg_27_2):
	local var_27_0 = arg_27_0.curShipVO
	local var_27_1 = arg_27_0.curMetaCharacterVO
	local var_27_2 = arg_27_0.findTF("Skill/Icon", arg_27_1)
	local var_27_3 = arg_27_0.findTF("Skill/Level", arg_27_1)
	local var_27_4 = arg_27_0.findTF("Skill/Mask/Name", arg_27_1)
	local var_27_5 = arg_27_0.findTF("Skill/Arrow", arg_27_1)
	local var_27_6 = arg_27_0.findTF("Lock", arg_27_1)
	local var_27_7 = arg_27_0.findTF("Learning", arg_27_1)
	local var_27_8 = getSkillConfig(arg_27_2)
	local var_27_9 = var_27_0.getMetaSkillLevelBySkillID(arg_27_2)

	setImageSprite(var_27_2, LoadSprite("skillicon/" .. var_27_8.icon))
	setScrollText(var_27_4, getSkillName(var_27_8.id))

	if var_27_9 > 0:
		setText(var_27_3, "LEVEL. " .. var_27_9)
		setActive(var_27_6, False)
		onButton(arg_27_0, arg_27_1, function()
			if not isActive(var_27_5):
				eachChild(arg_27_0.skillContainer, function(arg_29_0)
					local var_29_0 = arg_27_0.findTF("Skill/Arrow", arg_29_0)

					setActive(var_29_0, False))
				setActive(var_27_5, True)
				arg_27_0.updateTaskPanel(arg_27_2), SFX_PANEL)
	else
		setText(var_27_3, "LEVEL. ??")
		setActive(var_27_6, True)
		onButton(arg_27_0, arg_27_1, function()
			arg_27_0.openUnlockSkillPanel(arg_27_2), SFX_PANEL)

def var_0_0.updateSkillTFLearning(arg_31_0):
	local var_31_0 = arg_31_0.curShipVO

	for iter_31_0, iter_31_1 in pairs(arg_31_0.skillBtnList):
		local var_31_1 = arg_31_0.findTF("Learning", iter_31_1)
		local var_31_2 = var_31_0.isSkillLevelMax(iter_31_0)
		local var_31_3 = iter_31_0 == arg_31_0.curSkillID

		setActive(var_31_1, var_31_3 and not var_31_2)

def var_0_0.TryPlayGuide(arg_32_0):
	pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0025")

def var_0_0.updateExpPanel(arg_33_0):
	local var_33_0 = arg_33_0.isAllSkillLock()
	local var_33_1 = arg_33_0.isAllSkillMaxLevel()

	if var_33_0 or var_33_1:
		setActive(arg_33_0.expPanel, False)
	elif arg_33_0.curSkillID > 0:
		setActive(arg_33_0.expPanel, True)

		local var_33_2 = pg.gameset.meta_skill_exp_double.key_value
		local var_33_3 = pg.gameset.meta_skill_exp_max.key_value

		setText(arg_33_0.expText, arg_33_0.normalExpValue .. "/" .. var_33_3)
		setActive(arg_33_0.expDoubleTag, var_33_2 > arg_33_0.doubleExpValue)
	else
		setActive(arg_33_0.expPanel, False)

def var_0_0.updateSkillInfoPanel(arg_34_0, arg_34_1):
	local var_34_0 = arg_34_0.curShipVO
	local var_34_1 = getSkillConfig(arg_34_1)

	setImageSprite(arg_34_0.curSkillIcon, LoadSprite("skillicon/" .. var_34_1.icon))
	setScrollText(arg_34_0.curSkillNameScrollText, getSkillName(var_34_1.id))

	local var_34_2 = pg.skill_data_template[arg_34_1].max_level
	local var_34_3 = var_34_0.getMetaSkillLevelBySkillID(arg_34_1)
	local var_34_4 = var_34_2 <= var_34_3

	setText(arg_34_0.curSkillLevelText, var_34_3)

	local var_34_5 = math.min(var_34_3 + 1, var_34_2)

	setText(arg_34_0.nextSkillLevelText, var_34_5)
	setText(arg_34_0.curSkillDescText, getSkillDesc(arg_34_1, var_34_0.getMetaSkillLevelBySkillID(arg_34_1)))
	setActive(arg_34_0.curSkillQuickBtn, not var_34_4 and not LOCK_META_SKILL_QUICK)
	onButton(arg_34_0, arg_34_0.curSkillQuickBtn, function()
		arg_34_0.emit(MetaCharacterTacticsMediator.ON_QUICK, arg_34_0.curShipVO.id, arg_34_1), SFX_PANEL)

	local var_34_6 = arg_34_0.skillExpTable[arg_34_1] or 0

	if not var_34_4:
		local var_34_7 = arg_34_0.getMetaSkillTacticsConfigBySkillID(arg_34_1, var_34_3).need_exp

		setText(arg_34_0.curSkillProgressText, var_34_6 .. "/" .. var_34_7)
		setSlider(arg_34_0.curSkillProgressSlider, 0, var_34_7, var_34_6)

		if var_34_6 < var_34_7:
			-- block empty
	else
		setText(arg_34_0.curSkillProgressText, var_34_6 .. "/Max")
		setSlider(arg_34_0.curSkillProgressSlider, 0, 1, 1)

def var_0_0.updateTaskListPanel(arg_36_0, arg_36_1):
	local var_36_0 = arg_36_0.curShipVO.getMetaSkillLevelBySkillID(arg_36_1)
	local var_36_1 = arg_36_0.getMetaSkillTacticsConfigBySkillID(arg_36_1, var_36_0).skill_levelup_task
	local var_36_2 = arg_36_0.sortTaskConfig(arg_36_1, var_36_1)

	arg_36_0.taskUIItemList.make(function(arg_37_0, arg_37_1, arg_37_2)
		if arg_37_0 == UIItemList.EventUpdate:
			local var_37_0 = arg_36_0.findTF("Desc", arg_37_2)
			local var_37_1 = arg_36_0.findTF("AddExp", arg_37_2)
			local var_37_2 = arg_36_0.findTF("Text", arg_37_2)

			arg_37_1 = arg_37_1 + 1

			local var_37_3 = var_36_2[arg_37_1]
			local var_37_4 = var_37_3[1]
			local var_37_5 = arg_36_0.getTaskInfoBySkillAndTaskID(arg_36_1, var_37_4)
			local var_37_6 = var_37_5 and var_37_5.finishCount or 0
			local var_37_7 = var_37_3[3]

			setText(var_37_1, "+" .. var_37_7)

			local var_37_8 = var_37_3[2]

			if var_37_8 == 0:
				setText(var_37_2, var_37_6 .. "/∞")
			else
				setText(var_37_2, var_37_6 .. "/" .. var_37_8)

			setText(var_37_0, pg.task_meta_data_template[var_37_4].desc))
	arg_36_0.taskUIItemList.align(#var_36_2)

def var_0_0.updateTaskPanel(arg_38_0, arg_38_1):
	local var_38_0 = arg_38_0.curShipVO
	local var_38_1 = arg_38_0.curMetaCharacterVO

	if var_38_0.isSkillLevelMax(arg_38_1) == True:
		setActive(arg_38_0.studySkillTip, False)
		setActive(arg_38_0.startSkillTip, False)
		setActive(arg_38_0.maxSkillTip, True)
		setActive(arg_38_0.skillInfoPanel, True)
		setActive(arg_38_0.taskTplContainer, False)
		setActive(arg_38_0.taskScrollBar, False)
		arg_38_0.updateSkillInfoPanel(arg_38_1)
	elif arg_38_1 != arg_38_0.curSkillID:
		setActive(arg_38_0.studySkillTip, False)
		setActive(arg_38_0.startSkillTip, True)
		setActive(arg_38_0.maxSkillTip, False)
		setActive(arg_38_0.skillInfoPanel, True)
		setActive(arg_38_0.taskTplContainer, True)
		setActive(arg_38_0.taskScrollBar, True)
		arg_38_0.updateSkillInfoPanel(arg_38_1)
		arg_38_0.updateTaskListPanel(arg_38_1)
		onButton(arg_38_0, arg_38_0.studySkillBtn, function()
			if arg_38_0.switchCountLeft == 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("meta_switch_skill_disable"))
			else
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("meta_switch_skill_box_title", getSkillName(arg_38_1)),
					def onYes:()
						pg.m02.sendNotification(GAME.TACTICS_META_SWITCH_SKILL, {
							shipID = var_38_0.id,
							skillID = arg_38_1
						}),
					weight = LayerWeightConst.TOP_LAYER
				}), SFX_PANEL)
	else
		setActive(arg_38_0.studySkillTip, False)
		setActive(arg_38_0.startSkillTip, False)
		setActive(arg_38_0.maxSkillTip, False)
		setActive(arg_38_0.skillInfoPanel, True)
		setActive(arg_38_0.taskTplContainer, True)
		setActive(arg_38_0.taskScrollBar, True)
		arg_38_0.updateSkillInfoPanel(arg_38_1)
		arg_38_0.updateTaskListPanel(arg_38_1)

def var_0_0.updateMain(arg_41_0):
	local var_41_0 = arg_41_0.curShipVO
	local var_41_1 = arg_41_0.getSkillIDListForShow(var_41_0.configId)
	local var_41_2 = True
	local var_41_3 = 0
	local var_41_4, var_41_5 = arg_41_0.isAllSkillLock()

	setActive(arg_41_0.taskScrollTF, not var_41_4)

	if var_41_4:
		setActive(arg_41_0.expPanel, False)
		setActive(arg_41_0.skillInfoPanel, False)
		setActive(arg_41_0.taskTplContainer, False)
		setActive(arg_41_0.taskScrollBar, False)
		setActive(arg_41_0.studySkillTip, True)
		setActive(arg_41_0.startSkillTip, False)
		setActive(arg_41_0.maxSkillTip, False)
	elif arg_41_0.curUnlockSkillID:
		triggerButton(arg_41_0.skillBtnList[arg_41_0.curUnlockSkillID])
	elif arg_41_0.curSkillID > 0:
		triggerButton(arg_41_0.skillBtnList[arg_41_0.curSkillID])
	else
		triggerButton(arg_41_0.skillBtnList[var_41_5])

def var_0_0.tryLearnSkillAfterFirstUnlock(arg_42_0):
	local var_42_0 = arg_42_0.curUnlockSkillID
	local var_42_1 = 1

	arg_42_0.switchTacticsSkillData(var_42_0, var_42_1)
	arg_42_0.updateExpPanel()
	arg_42_0.updateTaskPanel(var_42_0)
	arg_42_0.updateSkillTFLearning()
	arg_42_0.TryPlayGuide()

def var_0_0.moveShipImg(arg_43_0, arg_43_1):
	local var_43_0 = arg_43_0.curMetaCharacterVO.id
	local var_43_1 = MetaCharacterConst.UIConfig[var_43_0]
	local var_43_2 = arg_43_1 and -2000 or var_43_1[7]
	local var_43_3 = arg_43_1 and var_43_1[7] or -2000

	arg_43_0.managedTween(LeanTween.moveX, None, rtf(arg_43_0.shipImg), var_43_3, 0.2).setFrom(var_43_2)

def var_0_0.moveRightPanel(arg_44_0):
	local var_44_0 = 2000
	local var_44_1 = 500

	arg_44_0.managedTween(LeanTween.moveX, None, rtf(arg_44_0.skillPanel), var_44_1, 0.2).setFrom(var_44_0)
	arg_44_0.managedTween(LeanTween.moveX, None, rtf(arg_44_0.taskPanel), var_44_1, 0.2).setFrom(var_44_0)

def var_0_0.openUnlockSkillPanel(arg_45_0, arg_45_1):
	local var_45_0 = arg_45_0.curShipVO
	local var_45_1 = arg_45_0.curMetaCharacterVO

	arg_45_0.curUnlockSkillID = arg_45_1

	local var_45_2 = ShipGroup.getDefaultShipNameByGroupID(var_45_1.id)
	local var_45_3 = getSkillName(arg_45_1)

	setText(arg_45_0.skillUnlockPanelTipText, i18n("meta_unlock_skill_tip", var_45_2, var_45_3))

	local var_45_4 = arg_45_0.getMetaSkillTacticsConfigBySkillID(arg_45_1, 1)
	local var_45_5 = var_45_4.skill_unlock
	local var_45_6 = {
		var_45_4.skill_unlock[1]
	}

	arg_45_0.materialUIItemList.make(function(arg_46_0, arg_46_1, arg_46_2)
		if arg_46_0 == UIItemList.EventUpdate:
			arg_46_1 = arg_46_1 + 1

			local var_46_0 = var_45_6[arg_46_1]
			local var_46_1 = arg_45_0.findTF("Item", arg_46_2)
			local var_46_2 = arg_45_0.findTF("SelectedTag", arg_46_2)
			local var_46_3 = arg_45_0.findTF("Count/Text", arg_46_2)
			local var_46_4 = {
				type = DROP_TYPE_ITEM,
				id = var_46_0[2],
				count = var_46_0[3]
			}

			updateDrop(var_46_1, var_46_4)
			setActive(var_46_2, False)

			local var_46_5 = var_46_0[2]
			local var_46_6 = var_46_0[3]
			local var_46_7 = getProxy(BagProxy).getItemCountById(var_46_5)
			local var_46_8 = var_46_7 < var_46_6 and setColorStr(var_46_7, COLOR_RED) or setColorStr(var_46_7, COLOR_GREEN)

			setText(var_46_3, var_46_8 .. "/" .. var_46_6)

			arg_45_0.curUnlockMaterialID = var_46_5
			arg_45_0.curUnlockMaterialNeedCount = var_46_6)
	arg_45_0.materialUIItemList.align(#var_45_6)
	setActive(arg_45_0.skillUnlockPanel, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_45_0.skillUnlockPanel, False, {
		weight = LayerWeightConst.TOP_LAYER
	})

def var_0_0.closeUnlockSkillPanel(arg_47_0):
	arg_47_0.curUnlockSkillID = None
	arg_47_0.curUnlockMaterialID = None
	arg_47_0.curUnlockMaterialNeedCount = None

	setActive(arg_47_0.skillUnlockPanel, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_47_0.skillUnlockPanel, arg_47_0._tf)

def var_0_0.enablePartialBlur(arg_48_0):
	if arg_48_0._tf:
		local var_48_0 = {}

		table.insert(var_48_0, arg_48_0.taskPanel)
		table.insert(var_48_0, arg_48_0.skillPanel)
		pg.UIMgr.GetInstance().OverlayPanelPB(arg_48_0._tf, {
			pbList = var_48_0,
			groupName = LayerWeightConst.GROUP_META,
			weight = LayerWeightConst.BASE_LAYER - 1
		})

def var_0_0.disablePartialBlur(arg_49_0):
	if arg_49_0._tf:
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_49_0._tf)

def var_0_0.getMetaSkillTacticsConfigBySkillID(arg_50_0, arg_50_1, arg_50_2):
	return MetaCharacterConst.getMetaSkillTacticsConfig(arg_50_1, arg_50_2)

def var_0_0.getTaskInfoBySkillAndTaskID(arg_51_0, arg_51_1, arg_51_2):
	local var_51_0 = arg_51_0.taskInfoTable[arg_51_1] or {}

	for iter_51_0, iter_51_1 in ipairs(var_51_0):
		if iter_51_1.taskID == arg_51_2:
			return iter_51_1

def var_0_0.isAllSkillLock(arg_52_0):
	local var_52_0 = arg_52_0.curShipVO
	local var_52_1 = arg_52_0.getSkillIDListForShow(var_52_0.configId)
	local var_52_2 = True
	local var_52_3 = 0

	for iter_52_0, iter_52_1 in ipairs(var_52_1):
		if var_52_0.getMetaSkillLevelBySkillID(iter_52_1) > 0:
			var_52_2 = False
			var_52_3 = iter_52_1

			break

	return var_52_2, var_52_3

def var_0_0.isAllSkillMaxLevel(arg_53_0):
	local var_53_0 = arg_53_0.curShipVO
	local var_53_1 = arg_53_0.getSkillIDListForShow(var_53_0.configId)
	local var_53_2 = True

	for iter_53_0, iter_53_1 in ipairs(var_53_1):
		if not var_53_0.isSkillLevelMax(iter_53_1):
			return False

def var_0_0.updateTacticsRedTag(arg_54_0):
	local var_54_0 = arg_54_0.curShipVO
	local var_54_1 = var_54_0.getMetaCharacter()
	local var_54_2 = arg_54_0.getSkillIDListForShow(var_54_0.configId)
	local var_54_3 = False

	for iter_54_0, iter_54_1 in ipairs(var_54_2):
		local var_54_4 = var_54_0.getMetaSkillLevelBySkillID(iter_54_1)
		local var_54_5 = var_54_0.isSkillLevelMax(iter_54_1)

		if var_54_4 > 0 and not var_54_5 and arg_54_0.getMetaSkillTacticsConfigBySkillID(iter_54_1, var_54_4).need_exp <= (arg_54_0.skillExpTable and arg_54_0.skillExpTable[iter_54_1] or 0):
			local var_54_6 = True

			break

def var_0_0.sortTaskConfig(arg_55_0, arg_55_1, arg_55_2):
	local var_55_0 = Clone(arg_55_2)

	table.sort(var_55_0, function(arg_56_0, arg_56_1)
		local var_56_0 = arg_56_0[1]
		local var_56_1 = arg_56_1[1]
		local var_56_2 = arg_56_0[2]
		local var_56_3 = arg_56_1[2]
		local var_56_4 = arg_55_0.getTaskInfoBySkillAndTaskID(arg_55_1, var_56_0)
		local var_56_5 = arg_55_0.getTaskInfoBySkillAndTaskID(arg_55_1, var_56_1)
		local var_56_6 = var_56_4 and var_56_4.finishCount or 0
		local var_56_7 = var_56_5 and var_56_5.finishCount or 0
		local var_56_8 = var_56_2 > 0 and var_56_6 <= var_56_2
		local var_56_9 = var_56_3 > 0 and var_56_7 <= var_56_3

		if var_56_2 == 0 and var_56_3 == 0:
			return var_56_0 < var_56_1
		elif var_56_2 == 0:
			return True
		elif var_56_3 == 0:
			return False
		elif var_56_8 == True and var_56_9 == True:
			return var_56_0 < var_56_1
		elif var_56_8 == True:
			return False
		elif var_56_9 == True:
			return True
		else
			return var_56_0 < var_56_1)

	return var_55_0

def var_0_0.getSkillIDListForShow(arg_57_0, arg_57_1):
	return MetaCharacterConst.getTacticsSkillIDListByShipConfigID(arg_57_1)

return var_0_0
