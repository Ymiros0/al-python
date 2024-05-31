local var_0_0 = class("TechnologyTreeNationScene", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "TechnologyTreeCampUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.addListener()
	arg_3_0.updateTecItemList()
	arg_3_0.updateOneStepBtn()

def var_0_0.willExit(arg_4_0):
	for iter_4_0, iter_4_1 in pairs(arg_4_0.timerList):
		iter_4_1.Stop()

def var_0_0.initData(arg_5_0):
	arg_5_0.nationProxy = getProxy(TechnologyNationProxy)
	arg_5_0.nationToPoint = arg_5_0.nationProxy.getNationPointList()
	arg_5_0.tecList = arg_5_0.nationProxy.GetTecList()
	arg_5_0.panelList = {}
	arg_5_0.timerList = {}

def var_0_0.calculateCurBuff(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0

	if arg_6_1 == 0:
		return {}, {}, {}
	else
		var_6_0 = pg.fleet_tech_group[arg_6_2].techs[arg_6_1]

	local var_6_1 = pg.fleet_tech_template[var_6_0].add
	local var_6_2 = {}
	local var_6_3 = {}

	for iter_6_0, iter_6_1 in ipairs(var_6_1):
		local var_6_4 = iter_6_1[2]
		local var_6_5 = iter_6_1[3]
		local var_6_6 = iter_6_1[1]

		for iter_6_2, iter_6_3 in ipairs(var_6_6):
			if var_6_2[iter_6_3]:
				table.insert(var_6_2[iter_6_3], {
					attr = var_6_4,
					value = var_6_5
				})
			else
				var_6_2[iter_6_3] = {
					{
						attr = var_6_4,
						value = var_6_5
					}
				}
				var_6_3[#var_6_3 + 1] = iter_6_3

	local var_6_7 = {}
	local var_6_8 = {}

	for iter_6_4, iter_6_5 in pairs(var_6_2):
		if not var_6_7[iter_6_4]:
			var_6_7[iter_6_4] = {}
			var_6_8[iter_6_4] = {}

		for iter_6_6, iter_6_7 in ipairs(iter_6_5):
			local var_6_9 = iter_6_7.attr
			local var_6_10 = iter_6_7.value

			if not var_6_7[iter_6_4][var_6_9]:
				var_6_7[iter_6_4][var_6_9] = var_6_10
				var_6_8[iter_6_4][#var_6_8[iter_6_4] + 1] = var_6_9
			else
				var_6_7[iter_6_4][var_6_9] = var_6_7[iter_6_4][var_6_9] + var_6_10

	table.sort(var_6_3, function(arg_7_0, arg_7_1)
		return arg_7_0 < arg_7_1)

	for iter_6_8, iter_6_9 in pairs(var_6_8):
		table.sort(iter_6_9, function(arg_8_0, arg_8_1)
			return arg_8_0 < arg_8_1)

	return var_6_3, var_6_8, var_6_7

def var_0_0.findUI(arg_9_0):
	arg_9_0.scrollRect = arg_9_0.findTF("Scroll View")
	arg_9_0.tecItemContainer = arg_9_0.findTF("Scroll View/Viewport/Content")
	arg_9_0.scrollRectCom = GetComponent(arg_9_0.scrollRect, "ScrollRect")
	arg_9_0.tecItemTpl = arg_9_0.findTF("CampTecItem")
	arg_9_0.typeItemTpl = arg_9_0.findTF("TypeItem")
	arg_9_0.buffItemTpl = arg_9_0.findTF("BuffItem")
	arg_9_0.tecItemTplOriginWidth = arg_9_0.tecItemTpl.rect.width
	arg_9_0.oneStepBtn = arg_9_0.findTF("OneStepBtn")

	if not LOCK_TEC_NATION_AWARD:
		arg_9_0.awardTpl = Instantiate(GetComponent(arg_9_0._tf, "ItemList").prefabItem[0])

		setActive(arg_9_0.awardTpl, False)

		local var_9_0 = arg_9_0.awardTpl.AddComponent(typeof(LayoutElement))

		var_9_0.preferredWidth = 204
		var_9_0.preferredHeight = 206

		local var_9_1 = arg_9_0.findTF("CampTecItem/AwardPanel/FinishBtn/Text")

		setText(var_9_1, i18n("tec_nation_award_finish"))
	else
		setActive(arg_9_0.oneStepBtn, False)

def var_0_0.onBackPressed(arg_10_0):
	arg_10_0.emit(var_0_0.ON_BACK)

def var_0_0.closeMyself(arg_11_0):
	arg_11_0.emit(var_0_0.ON_CLOSE)

def var_0_0.addListener(arg_12_0):
	onButton(arg_12_0, arg_12_0.oneStepBtn, function()
		pg.m02.sendNotification(GAME.GET_CAMP_TEC_AWARD_ONESTEP), SFX_PANEL)

def var_0_0.updateTecItemList(arg_14_0):
	local var_14_0 = UIItemList.New(arg_14_0.tecItemContainer, arg_14_0.tecItemTpl)

	var_14_0.make(function(arg_15_0, arg_15_1, arg_15_2)
		if arg_15_0 == UIItemList.EventUpdate:
			local var_15_0 = arg_15_1 + 1

			arg_14_0.panelList[var_15_0] = arg_15_2

			arg_14_0.updateTecItem(var_15_0))
	var_14_0.align(#pg.fleet_tech_group.all)

def var_0_0.updateTecItem(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_0.panelList[arg_16_1]
	local var_16_1 = arg_16_0.findTF("AwardPanel", var_16_0)

	arg_16_0.updateTecLevelAward(var_16_1, arg_16_1)

	local var_16_2 = arg_16_0.findTF("BaseInfo", var_16_0)
	local var_16_3 = arg_16_0.findTF("BG/Title/Text", var_16_2)
	local var_16_4 = arg_16_0.findTF("BG/UpLevelColor", var_16_2)
	local var_16_5 = arg_16_0.findTF("NationBG", var_16_2)
	local var_16_6 = arg_16_0.findTF("Code", var_16_2)
	local var_16_7 = arg_16_0.findTF("NationTextImg", var_16_6)
	local var_16_8 = arg_16_0.findTF("UpLevelBG", var_16_2)
	local var_16_9 = arg_16_0.findTF("UpLevelBtn", var_16_8)
	local var_16_10 = arg_16_0.findTF("FinishBtn", var_16_8)
	local var_16_11 = arg_16_0.findTF("Uping", var_16_2)
	local var_16_12 = arg_16_0.findTF("Text", var_16_11)
	local var_16_13 = arg_16_0.findTF("EnglishTextImg", var_16_2)
	local var_16_14 = arg_16_0.findTF("ProgressBarBG/Progress", var_16_2)
	local var_16_15 = arg_16_0.findTF("CampLogo", var_16_2)
	local var_16_16 = arg_16_0.findTF("LevelText/Text", var_16_2)
	local var_16_17 = arg_16_0.findTF("PointTextBar", var_16_2)
	local var_16_18 = pg.fleet_tech_group[arg_16_1].name
	local var_16_19 = pg.fleet_tech_group[arg_16_1].nation[1]

	setImageSprite(var_16_5, GetSpriteFromAtlas("TecNation", "camptec_nation_bar_" .. var_16_19))
	setImageSprite(var_16_7, GetSpriteFromAtlas("TecNation", "camptec_nation_text_" .. var_16_19), True)
	setImageSprite(var_16_13, GetSpriteFromAtlas("TecNation", "camp_tec_english_" .. var_16_19), True)
	setImageSprite(var_16_15, GetSpriteFromAtlas("TecNation", "camptec_logo_" .. var_16_19))
	setText(var_16_3, var_16_18)

	local var_16_20
	local var_16_21
	local var_16_22 = not arg_16_0.tecList[arg_16_1] and 0 or table.indexof(pg.fleet_tech_group[arg_16_1].techs, arg_16_0.tecList[arg_16_1].completeID, 1) or 0
	local var_16_23 = arg_16_0.nationToPoint[var_16_19]
	local var_16_24

	if var_16_22 == 0:
		var_16_21 = pg.fleet_tech_group[arg_16_1].techs[1]
		var_16_24 = pg.fleet_tech_template[var_16_21].pt
	elif var_16_22 == #pg.fleet_tech_group[arg_16_1].techs:
		var_16_21 = pg.fleet_tech_group[arg_16_1].techs[var_16_22]
		var_16_24 = pg.fleet_tech_template[var_16_21].pt
	else
		var_16_21 = pg.fleet_tech_group[arg_16_1].techs[var_16_22 + 1]
		var_16_24 = pg.fleet_tech_template[var_16_21].pt

	BaseUI.setImageAmount(var_16_14, 0.1 + 0.8 * var_16_23 / var_16_24)
	setText(var_16_16, var_16_22)
	setText(var_16_17, var_16_23 .. "/" .. var_16_24)

	local function var_16_25(arg_17_0, arg_17_1, arg_17_2)
		setActive(var_16_6, arg_17_0)
		setActive(var_16_8, arg_17_1)
		setActive(var_16_4, arg_17_1)
		setActive(var_16_9, arg_17_1)
		setActive(var_16_11, arg_17_2)

	if not arg_16_0.tecList[arg_16_1]:
		if var_16_24 <= var_16_23:
			var_16_25(False, True, False)
		else
			var_16_25(True, False, False)
	elif var_16_22 == #pg.fleet_tech_group[arg_16_1].techs:
		var_16_25(True, False, False)
	elif arg_16_0.tecList[arg_16_1].studyID != 0:
		var_16_25(False, False, True)

		if arg_16_0.timerList[arg_16_1]:
			arg_16_0.timerList[arg_16_1].Stop()

		local var_16_26 = arg_16_0.nationProxy.getLeftTime()

		setText(var_16_12, pg.TimeMgr.GetInstance().DescCDTime(var_16_26))

		arg_16_0.timerList[arg_16_1] = Timer.New(function()
			var_16_26 = var_16_26 - 1

			setText(var_16_12, pg.TimeMgr.GetInstance().DescCDTime(var_16_26))

			if var_16_26 == 0:
				arg_16_0.timerList[arg_16_1].Stop(), 1, -1)

		arg_16_0.timerList[arg_16_1].Start()
	elif var_16_24 <= var_16_23:
		var_16_25(False, True, False)
	else
		var_16_25(True, False, False)

	onButton(arg_16_0, var_16_9, function()
		arg_16_0.emit(TechnologyConst.CLICK_UP_TEC_BTN, arg_16_1, var_16_21), SFX_PANEL)

	local var_16_27 = arg_16_0.findTF("Mask/DetailPanel", var_16_0)
	local var_16_28 = GetComponent(var_16_0, "LayoutElement")
	local var_16_29 = arg_16_0.findTF("Toggle", var_16_27)

	arg_16_0.updateDetailPanel(var_16_27, var_16_22, arg_16_1, var_16_19, False)
	onToggle(arg_16_0, arg_16_0.findTF("BG", var_16_2), function(arg_20_0)
		if arg_20_0:
			triggerToggle(var_16_29, False)
			LeanTween.value(go(var_16_0), arg_16_0.tecItemTplOriginWidth, arg_16_0.tecItemTplOriginWidth + var_16_27.rect.width, 0.25).setOnUpdate(System.Action_float(function(arg_21_0)
				var_16_28.preferredWidth = arg_21_0

				if arg_16_1 == #pg.fleet_tech_group.all:
					arg_16_0.scrollRectCom.horizontalNormalizedPosition = 1)).setOnComplete(System.Action(function()
				if arg_16_1 == #pg.fleet_tech_group.all:
					arg_16_0.scrollRectCom.horizontalNormalizedPosition = 1))
		else
			LeanTween.cancel(go(var_16_0))

			local var_20_0 = var_16_28.preferredWidth

			LeanTween.value(go(var_16_0), var_20_0, arg_16_0.tecItemTplOriginWidth, 0.25).setOnUpdate(System.Action_float(function(arg_23_0)
				var_16_28.preferredWidth = arg_23_0)))

def var_0_0.updateDetailPanel(arg_24_0, arg_24_1, arg_24_2, arg_24_3, arg_24_4, arg_24_5):
	local var_24_0 = arg_24_0.findTF("TypeItemContainer", arg_24_1)
	local var_24_1 = arg_24_0.findTF("BG/Logo", arg_24_1)

	setImageSprite(var_24_1, GetSpriteFromAtlas("TecNation", "camptec_logo_" .. arg_24_4))

	local var_24_2 = arg_24_0.findTF("Toggle", arg_24_1)

	if arg_24_2 == #pg.fleet_tech_group[arg_24_3].techs and arg_24_5 == False:
		setActive(var_24_2, False)

	local function var_24_3(arg_25_0, arg_25_1, arg_25_2)
		local var_25_0 = UIItemList.New(var_24_0, arg_24_0.typeItemTpl)
		local var_25_1

		if arg_25_0 == 0:
			var_25_0.align(0)

			return
		else
			var_25_1 = pg.fleet_tech_group[arg_25_1].techs[arg_25_0]

		local var_25_2
		local var_25_3
		local var_25_4
		local var_25_5 = Color.New(1, 0.9333333333333333, 0.19215686274509805)

		if arg_25_2:
			var_25_2, var_25_3, var_25_4 = arg_24_0.calculateCurBuff(arg_25_0 - 1, arg_25_1)

		local var_25_6 = pg.fleet_tech_template[var_25_1].add
		local var_25_7 = {}
		local var_25_8 = {}

		for iter_25_0, iter_25_1 in ipairs(var_25_6):
			local var_25_9 = iter_25_1[2]
			local var_25_10 = iter_25_1[3]
			local var_25_11 = ShipType.FilterOverQuZhuType(iter_25_1[1])

			for iter_25_2, iter_25_3 in ipairs(var_25_11):
				local var_25_12

				if arg_25_2:
					if not table.indexof(var_25_2, iter_25_3, 1):
						var_25_12 = {
							attr = var_25_9,
							value = var_25_10,
							attrColor = var_25_5,
							valueColor = var_25_5
						}
					elif not table.indexof(var_25_3[iter_25_3], var_25_9, 1):
						var_25_12 = {
							attr = var_25_9,
							value = var_25_10,
							attrColor = var_25_5,
							valueColor = var_25_5
						}
					elif var_25_10 != var_25_4[iter_25_3][var_25_9]:
						var_25_12 = {
							attr = var_25_9,
							value = var_25_10,
							valueColor = var_25_5
						}
					else
						var_25_12 = {
							attr = var_25_9,
							value = var_25_10
						}
				else
					var_25_12 = {
						attr = var_25_9,
						value = var_25_10
					}

				if var_25_7[iter_25_3]:
					table.insert(var_25_7[iter_25_3], var_25_12)
				else
					var_25_7[iter_25_3] = {
						var_25_12
					}
					var_25_8[#var_25_8 + 1] = iter_25_3

		var_25_0.make(function(arg_26_0, arg_26_1, arg_26_2)
			if arg_26_0 == UIItemList.EventUpdate:
				local var_26_0 = arg_24_0.findTF("TypeIcon", arg_26_2)
				local var_26_1 = arg_24_0.findTF("BuffItemContainer", arg_26_2)
				local var_26_2 = var_25_8[arg_26_1 + 1]

				setImageSprite(var_26_0, GetSpriteFromAtlas("ShipType", "buffitem_tec_" .. var_26_2))
				arg_24_0.upBuffList(arg_26_2, var_25_7[var_26_2]))
		var_25_0.align(#var_25_8)

	onToggle(arg_24_0, var_24_2, function(arg_27_0)
		if arg_27_0 == True:
			var_24_3(arg_24_2 + 1, arg_24_3, True)
		else
			var_24_3(arg_24_2, arg_24_3), SFX_PANEL)

	if arg_24_5 == False:
		triggerToggle(var_24_2, False)

def var_0_0.upBuffList(arg_28_0, arg_28_1, arg_28_2):
	local var_28_0 = arg_28_0.findTF("BuffItemContainer", arg_28_1)
	local var_28_1 = UIItemList.New(var_28_0, arg_28_0.buffItemTpl)

	var_28_1.make(function(arg_29_0, arg_29_1, arg_29_2)
		if arg_29_0 == UIItemList.EventUpdate:
			local var_29_0 = arg_28_0.findTF("AttrText", arg_29_2)
			local var_29_1 = arg_28_0.findTF("ValueText", arg_29_2)
			local var_29_2 = arg_28_2[arg_29_1 + 1].attr
			local var_29_3 = arg_28_2[arg_29_1 + 1].value
			local var_29_4 = arg_28_2[arg_29_1 + 1].attrColor
			local var_29_5 = arg_28_2[arg_29_1 + 1].valueColor

			setText(var_29_0, AttributeType.Type2Name(pg.attribute_info_by_type[var_29_2].name))
			setText(var_29_1, "+" .. var_29_3)

			if var_29_4:
				setTextColor(var_29_0, var_29_4)
			else
				setTextColor(var_29_0, Color.white)

			if var_29_5:
				setTextColor(var_29_1, var_29_5)
			else
				setTextColor(var_29_1, Color.green))
	var_28_1.align(#arg_28_2)

def var_0_0.updateTecLevelAward(arg_30_0, arg_30_1, arg_30_2):
	if LOCK_TEC_NATION_AWARD:
		setActive(arg_30_1, False)

		return

	local var_30_0 = arg_30_0.findTF("AwardItem")
	local var_30_1 = arg_30_0.findTF("ItemContainer", arg_30_1)
	local var_30_2 = UIItemList.New(var_30_1, arg_30_0.awardTpl)
	local var_30_3 = arg_30_0.findTF("Level", arg_30_1)
	local var_30_4 = arg_30_0.findTF("Level/Num", arg_30_1)
	local var_30_5 = arg_30_0.findTF("GetBtn", arg_30_1)
	local var_30_6 = arg_30_0.findTF("DisGetBtn", arg_30_1)
	local var_30_7 = arg_30_0.findTF("FinishBtn", arg_30_1)
	local var_30_8 = arg_30_0.nationProxy.GetTecItemByGroupID(arg_30_2)
	local var_30_9 = pg.fleet_tech_group[arg_30_2]
	local var_30_10 = var_30_8 and var_30_8.rewardedID or 0
	local var_30_11 = var_30_8 and var_30_8.completeID or 0
	local var_30_12 = table.indexof(var_30_9.techs, var_30_10, 1) or 0
	local var_30_13 = table.indexof(var_30_9.techs, var_30_11, 1) or 0
	local var_30_14 = var_30_12 + 1
	local var_30_15

	if var_30_12 < var_30_13:
		var_30_15 = var_30_9.techs[var_30_14]
	elif var_30_12 == var_30_13 and var_30_12 < #var_30_9.techs:
		var_30_15 = var_30_9.techs[var_30_14]

	if var_30_15:
		setActive(var_30_3, True)
		setActive(var_30_1, True)
		setActive(var_30_5, var_30_12 < var_30_13)
		setActive(var_30_6, var_30_12 == var_30_13)
		setActive(var_30_7, False)
		setText(var_30_4, var_30_14)

		local var_30_16 = pg.fleet_tech_template[var_30_15].level_award_display

		var_30_2.make(function(arg_31_0, arg_31_1, arg_31_2)
			if arg_31_0 == UIItemList.EventUpdate:
				arg_31_1 = arg_31_1 + 1

				local var_31_0 = var_30_16[arg_31_1]
				local var_31_1 = {
					type = var_31_0[1],
					id = var_31_0[2],
					count = var_31_0[3]
				}

				updateDrop(arg_31_2, var_31_1))
		var_30_2.align(#var_30_16)

		if var_30_12 < var_30_13:
			onButton(arg_30_0, var_30_5, function()
				pg.m02.sendNotification(GAME.GET_CAMP_TEC_AWARD, {
					groupID = arg_30_2,
					tecID = var_30_15
				}), SFX_PANEL)
	else
		setActive(var_30_3, False)
		setActive(var_30_1, False)
		setActive(var_30_5, False)
		setActive(var_30_6, False)
		setActive(var_30_7, True)

def var_0_0.updateOneStepBtn(arg_33_0):
	if LOCK_TEC_NATION_AWARD:
		setActive(arg_33_0.oneStepBtn, False)

		return

	setActive(arg_33_0.oneStepBtn, arg_33_0.nationProxy.isAnyTecCampCanGetAward())

def var_0_0.updateTecListData(arg_34_0):
	arg_34_0.tecList = getProxy(TechnologyNationProxy).GetTecList()

return var_0_0
