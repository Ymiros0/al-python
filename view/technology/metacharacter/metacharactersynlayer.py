local var_0_0 = class("MetaCharacterSynLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "MetaCharacterSynUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initUITextTips()
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.updateShipImg()
	arg_3_0.updatePtPanel()
	arg_3_0.updateTaskList()
	arg_3_0.updateGetAwardBtn()
	arg_3_0.updateActTimePanel()
	arg_3_0.enablePartialBlur()

	if arg_3_0.contextData.isMainOpen:
		arg_3_0.contextData.isMainOpen = None

		arg_3_0.moveShipImg(True)

	arg_3_0.movePanel()
	arg_3_0.TryPlayGuide()

def var_0_0.willExit(arg_4_0):
	arg_4_0.moveShipImg(False)
	arg_4_0.disablePartialBlur()

def var_0_0.initUITextTips(arg_5_0):
	local var_5_0 = arg_5_0.findTF("PTPanel/TipText")

	setText(var_5_0, i18n("meta_cur_pt"))

	local var_5_1 = arg_5_0.findTF("TaskPanel/ActTimePanel/Tip")

	setText(var_5_1, i18n("meta_acttime_limit"))

def var_0_0.initData(arg_6_0):
	arg_6_0.curMetaShipID = arg_6_0.contextData.shipID
	arg_6_0.curShipVO = None
	arg_6_0.curMetaCharacterVO = None
	arg_6_0.curMetaProgressVO = None

	arg_6_0.updateData()

def var_0_0.updateData(arg_7_0):
	arg_7_0.curShipVO = getProxy(BayProxy).getShipById(arg_7_0.curMetaShipID)
	arg_7_0.curMetaCharacterVO = arg_7_0.curShipVO.getMetaCharacter()
	arg_7_0.curMetaProgressVO = getProxy(MetaCharacterProxy).getMetaProgressVOByID(arg_7_0.curMetaCharacterVO.id)

def var_0_0.findUI(arg_8_0):
	arg_8_0.shipImg = arg_8_0.findTF("ShipImg")
	arg_8_0.ptPanel = arg_8_0.findTF("PTPanel")
	arg_8_0.ptSynRateText = arg_8_0.findTF("ProgressText", arg_8_0.ptPanel)
	arg_8_0.ptNumText = arg_8_0.findTF("Count/NumText", arg_8_0.ptPanel)
	arg_8_0.ptIconLeft = arg_8_0.findTF("Icon", arg_8_0.ptPanel)
	arg_8_0.showWayBtn = arg_8_0.findTF("ShowWayBtn", arg_8_0.ptPanel)
	arg_8_0.taskPanel = arg_8_0.findTF("TaskPanel")
	arg_8_0.taskTplContainer = arg_8_0.findTF("Scroll/Viewport/Content", arg_8_0.taskPanel)
	arg_8_0.taskTpl = arg_8_0.findTF("TaskTpl", arg_8_0.taskPanel)
	arg_8_0.getAllBtn = arg_8_0.findTF("BtnGetAll", arg_8_0.taskPanel)
	arg_8_0.getAllBtnDisable = arg_8_0.findTF("BtnGetAllDisable", arg_8_0.taskPanel)
	arg_8_0.getNextBtn = arg_8_0.findTF("BtnGetMore", arg_8_0.taskPanel)
	arg_8_0.taskUIItemList = UIItemList.New(arg_8_0.taskTplContainer, arg_8_0.taskTpl)
	arg_8_0.sizeH = GetComponent(arg_8_0.taskTpl, "LayoutElement").preferredHeight
	arg_8_0.spaceH = GetComponent(arg_8_0.taskTplContainer, "VerticalLayoutGroup").spacing
	arg_8_0.topH = GetComponent(arg_8_0.taskTplContainer, "VerticalLayoutGroup").padding.top
	arg_8_0.scrollSC = GetComponent(arg_8_0.findTF("Scroll", arg_8_0.taskPanel), "ScrollRect")
	arg_8_0.actTimePanel = arg_8_0.findTF("TaskPanel/ActTimePanel")
	arg_8_0.actTimeText = arg_8_0.findTF("TaskPanel/ActTimePanel/Text")

def var_0_0.addListener(arg_9_0):
	onButton(arg_9_0, arg_9_0.getAllBtn, function()
		local var_10_0, var_10_1 = arg_9_0.getOneStepPTAwardLevelAndCount()

		pg.m02.sendNotification(GAME.GET_META_PT_AWARD, {
			groupID = arg_9_0.curMetaProgressVO.id,
			targetCount = var_10_1
		}), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.getAllBtnDisable, function()
		return)
	onButton(arg_9_0, arg_9_0.getNextBtn, function()
		pg.TipsMgr.GetInstance().ShowTips(i18n("meta_pt_notenough")))
	onButton(arg_9_0, arg_9_0.showWayBtn, function()
		local var_13_0 = {
			count = 0,
			type = DROP_TYPE_ITEM,
			id = arg_9_0.curMetaProgressVO.metaPtData.resId
		}

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_SINGLE_ITEM,
			drop = var_13_0
		}), SFX_PANEL)

def var_0_0.TryPlayGuide(arg_14_0):
	pg.SystemGuideMgr.GetInstance().PlayByGuideId("NG0028")

def var_0_0.updateActTimePanel(arg_15_0):
	local var_15_0 = arg_15_0.curMetaProgressVO

	if type(var_15_0.timeConfig) == "string":
		setActive(arg_15_0.actTimePanel, False)
	elif type(var_15_0.timeConfig) == "table":
		local var_15_1 = pg.TimeMgr.GetInstance().parseTimeFromConfig(var_15_0.timeConfig[2])
		local var_15_2 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_15_3 = pg.TimeMgr.GetInstance().DiffDay(var_15_2, var_15_1)

		setText(arg_15_0.actTimeText, i18n("meta_pt_left", var_15_3))

def var_0_0.updateShipImg(arg_16_0):
	local var_16_0, var_16_1 = MetaCharacterConst.GetMetaCharacterPaintPath(arg_16_0.curMetaCharacterVO.id, True)

	setImageSprite(arg_16_0.shipImg, LoadSprite(var_16_0, var_16_1), True)

	local var_16_2 = arg_16_0.curMetaCharacterVO.id
	local var_16_3 = MetaCharacterConst.UIConfig[var_16_2]

	setLocalPosition(arg_16_0.shipImg, {
		x = var_16_3[9],
		y = var_16_3[10]
	})
	setLocalScale(arg_16_0.shipImg, {
		x = var_16_3[3],
		y = var_16_3[4]
	})

def var_0_0.updatePtPanel(arg_17_0):
	setImageSprite(arg_17_0.ptIconLeft, LoadSprite(arg_17_0.curMetaProgressVO.getPtIconPath()))

	local var_17_0 = arg_17_0.curMetaProgressVO.getSynRate()

	setText(arg_17_0.ptSynRateText, string.format("%d", var_17_0 * 100) .. "%")

	local var_17_1 = arg_17_0.curMetaProgressVO.metaPtData.GetResProgress()

	setText(arg_17_0.ptNumText, var_17_1)

def var_0_0.updateTaskList(arg_18_0):
	arg_18_0.taskUIItemList.make(function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 == UIItemList.EventUpdate:
			arg_19_1 = arg_19_1 + 1

			arg_18_0.updateTaskTpl(arg_19_2, arg_19_1))

	local var_18_0, var_18_1, var_18_2 = arg_18_0.curMetaProgressVO.metaPtData.GetLevelProgress()

	arg_18_0.taskUIItemList.align(var_18_1)

	local var_18_3 = arg_18_0.topH + (var_18_0 - 1) * (arg_18_0.sizeH + arg_18_0.spaceH)

	setLocalPosition(arg_18_0.taskTplContainer, {
		y = var_18_3
	})

def var_0_0.updateTaskTpl(arg_20_0, arg_20_1, arg_20_2):
	local var_20_0 = arg_20_0.findTF("Target/IndexText", arg_20_1)
	local var_20_1 = arg_20_0.findTF("PT/Count/NumText", arg_20_1)
	local var_20_2 = arg_20_0.findTF("PT/Icon", arg_20_1)
	local var_20_3 = arg_20_0.findTF("Info/AwardInfo/NameMask/NameText", arg_20_1)
	local var_20_4 = arg_20_0.findTF("Info/AwardInfo/SynProgressText", arg_20_1)
	local var_20_5 = arg_20_0.findTF("Info/AwardInfo/Award/Item", arg_20_1)
	local var_20_6 = arg_20_0.findTF("Info/AwardInfo/Award/Tag/Get", arg_20_1)
	local var_20_7 = arg_20_0.findTF("Info/AwardInfo/Award/Tag/Got", arg_20_1)
	local var_20_8 = arg_20_0.findTF("GotMask", arg_20_1)

	setText(var_20_0, arg_20_2)

	local var_20_9 = arg_20_0.curMetaProgressVO.metaPtData.targets[arg_20_2]

	setText(var_20_1, var_20_9)
	setImageSprite(var_20_2, LoadSprite(arg_20_0.curMetaProgressVO.getPtIconPath()))

	local var_20_10 = Drop.Create(arg_20_0.curMetaProgressVO.metaPtData.dropList[arg_20_2])

	updateDrop(var_20_5, var_20_10, {
		hideName = True
	})
	onButton(arg_20_0, arg_20_0.findTF("Info/AwardInfo/Award", arg_20_1), function()
		arg_20_0.emit(BaseUI.ON_DROP, var_20_10), SFX_PANEL)
	setText(var_20_3, shortenString(var_20_10.getConfig("name"), 6))

	local var_20_11 = arg_20_0.curMetaProgressVO.unlockPTNum

	setText(var_20_4, math.round(var_20_9 / var_20_11 * 100) .. "%")

	if arg_20_2 < arg_20_0.curMetaProgressVO.metaPtData.level + 1:
		setActive(var_20_7, True)
		setActive(var_20_6, False)
		setActive(var_20_8, True)
		setGray(arg_20_1, True, True)
	else
		if var_20_9 > arg_20_0.curMetaProgressVO.metaPtData.count:
			setActive(var_20_7, False)
			setActive(var_20_6, False)
		else
			setActive(var_20_7, False)
			setActive(var_20_6, True)

		setActive(var_20_8, False)
		setGray(arg_20_1, False, True)

def var_0_0.updateGetAwardBtn(arg_22_0):
	local var_22_0 = arg_22_0.curMetaProgressVO.metaPtData.CanGetAward()
	local var_22_1 = arg_22_0.curMetaProgressVO.metaPtData.CanGetNextAward()

	if var_22_0:
		setActive(arg_22_0.getAllBtn, True)
		setActive(arg_22_0.getAllBtnDisable, False)
		setActive(arg_22_0.getNextBtn, False)
	elif var_22_1:
		setActive(arg_22_0.getAllBtn, False)
		setActive(arg_22_0.getAllBtnDisable, False)
		setActive(arg_22_0.getNextBtn, True)
	else
		setActive(arg_22_0.getAllBtn, False)
		setActive(arg_22_0.getAllBtnDisable, True)
		setActive(arg_22_0.getNextBtn, False)

def var_0_0.moveShipImg(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_0.curMetaCharacterVO.id
	local var_23_1 = MetaCharacterConst.UIConfig[var_23_0]
	local var_23_2 = arg_23_1 and -2000 or var_23_1[9]
	local var_23_3 = arg_23_1 and var_23_1[9] or -2000

	arg_23_0.managedTween(LeanTween.moveX, None, rtf(arg_23_0.shipImg), var_23_3, 0.3).setFrom(var_23_2)

def var_0_0.movePanel(arg_24_0):
	local var_24_0 = 2000
	local var_24_1 = 500

	arg_24_0.managedTween(LeanTween.moveX, None, rtf(arg_24_0.taskPanel), var_24_1, 0.3).setFrom(var_24_0)

	local var_24_2 = -2000
	local var_24_3 = -516

	arg_24_0.managedTween(LeanTween.moveX, None, rtf(arg_24_0.ptPanel), var_24_3, 0.3).setFrom(var_24_2)

def var_0_0.enablePartialBlur(arg_25_0):
	if arg_25_0._tf:
		local var_25_0 = {}

		table.insert(var_25_0, arg_25_0.taskPanel)
		pg.UIMgr.GetInstance().OverlayPanelPB(arg_25_0._tf, {
			pbList = var_25_0,
			groupName = LayerWeightConst.GROUP_META,
			weight = LayerWeightConst.BASE_LAYER - 1
		})

def var_0_0.disablePartialBlur(arg_26_0):
	if arg_26_0._tf:
		pg.UIMgr.GetInstance().UnOverlayPanel(arg_26_0._tf)

def var_0_0.getOneStepPTAwardLevelAndCount(arg_27_0):
	local var_27_0 = arg_27_0.curMetaProgressVO
	local var_27_1 = var_27_0.metaPtData.GetResProgress()
	local var_27_2 = var_27_0.metaPtData.targets
	local var_27_3 = var_27_0.getStoryIndexList()
	local var_27_4 = var_27_0.unlockPTLevel
	local var_27_5 = 0

	for iter_27_0 = 1, #var_27_2:
		local var_27_6 = False
		local var_27_7 = False

		if var_27_1 >= var_27_2[iter_27_0]:
			var_27_6 = True

		local var_27_8 = var_27_3[iter_27_0]

		if var_27_8 == 0:
			var_27_7 = True
		elif pg.NewStoryMgr.GetInstance().IsPlayed(var_27_8):
			var_27_7 = True

		if var_27_6 and var_27_7:
			var_27_5 = iter_27_0
		else
			break

	print("calc max level", var_27_5, var_27_2[var_27_5])

	return var_27_5, var_27_2[var_27_5]

def var_0_0.goWorldFunc(arg_28_0):
	local var_28_0 = getProxy(ContextProxy).getContextByMediator(MetaCharacterMediator)
	local var_28_1 = pg.m02.retrieveMediator("MetaCharacterMediator")

	var_28_0.data.lastPageIndex = var_28_1.viewComponent.curPageIndex

	arg_28_0.closeView()
	arg_28_0.sendNotification(GAME.GO_SCENE, SCENE.WORLDBOSS)

return var_0_0
