local var_0_0 = class("CommanderCatDockPage", import("view.base.BaseSubView"))

var_0_0.ON_SORT = "CommanderCatDockPage.ON_SORT"

def var_0_0.getUIName(arg_1_0):
	return "CommanderCatDockui"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.scrollRect = arg_2_0._tf.Find("frame").GetComponent("LScrollRect")
	arg_2_0.reserveBtn = arg_2_0._tf.Find("box/reserve_btn")
	arg_2_0.reserveTxt = arg_2_0.reserveBtn.Find("Text").GetComponent(typeof(Text))
	arg_2_0.reserveTip = arg_2_0.reserveBtn.Find("free")
	arg_2_0.homeBtn = arg_2_0._tf.Find("box/home")
	arg_2_0.homeTxt = arg_2_0.homeBtn.Find("Text").GetComponent(typeof(Text))
	arg_2_0.homeTip = arg_2_0.homeBtn.Find("tip")
	arg_2_0.boxesBtn = arg_2_0._tf.Find("box/boxes_btn")
	arg_2_0.boxesTxt = arg_2_0.boxesBtn.Find("Text").GetComponent(typeof(Text))
	arg_2_0.boxesTip = arg_2_0.boxesBtn.Find("tip")
	arg_2_0.capacityTxt = arg_2_0._tf.Find("box/capcity/Text").GetComponent(typeof(Text))
	arg_2_0.sortBtn = arg_2_0._tf.Find("top/sort_btn")
	arg_2_0.sortIdTxt = arg_2_0.sortBtn.Find("id")
	arg_2_0.sortLvTxt = arg_2_0.sortBtn.Find("Level")
	arg_2_0.sortRarityTxt = arg_2_0.sortBtn.Find("Rarity")
	arg_2_0.ascBtn = arg_2_0._tf.Find("top/asc_btn")
	arg_2_0.ascTr = arg_2_0.ascBtn.Find("asc")
	arg_2_0.descTr = arg_2_0.ascBtn.Find("desc")
	arg_2_0.selectedTr = arg_2_0._tf.Find("bottom")
	arg_2_0.btnsTr = arg_2_0._tf.Find("box")
	arg_2_0.selectedNumTxt = arg_2_0._tf.Find("bottom/value/Text").GetComponent(typeof(Text))
	arg_2_0.selectedBtn = arg_2_0._tf.Find("bottom/select_btn")
	arg_2_0.cancelBtn = arg_2_0._tf.Find("bottom/cancel_btn")
	arg_2_0.reservePanel = CommanderReservePage.New(arg_2_0._tf.parent, arg_2_0.event, arg_2_0.contextData)
	arg_2_0.boxesPanel = CommanderBoxesPage.New(arg_2_0._tf.parent, arg_2_0.event, arg_2_0.contextData)
	arg_2_0.indexPanel = CommanderIndexPage.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.catterySettlementPage = CatterySettlementPage.New(arg_2_0._tf, arg_2_0.event)

def var_0_0.RegisterEvent(arg_3_0):
	arg_3_0.bind(var_0_0.ON_SORT, function(arg_4_0)
		arg_3_0.OnSort())
	arg_3_0.bind(CommanderCatScene.EVENT_NEXT_ONE, function(arg_5_0, arg_5_1)
		arg_3_0.OnNextOn(arg_5_1, 1))
	arg_3_0.bind(CommanderCatScene.EVENT_PREV_ONE, function(arg_6_0, arg_6_1)
		arg_3_0.OnNextOn(arg_6_1, -1))
	arg_3_0.bind(CommanderCatScene.MSG_UPDATE, function(arg_7_0)
		arg_3_0.UpdateCommanders(True)
		arg_3_0.UpdateCapacity())
	arg_3_0.bind(CommanderCatScene.MSG_HOME_TIP, function(arg_8_0)
		arg_3_0.UpdateHome())
	arg_3_0.bind(CommanderCatScene.MSG_BUILD, function()
		arg_3_0.UpdateBoxes())
	arg_3_0.bind(CommanderCatScene.MSG_RESERVE_BOX, function()
		arg_3_0.UpdateReserve())
	arg_3_0.bind(CommanderCatScene.EVENT_FOLD, function(arg_11_0, arg_11_1)
		if arg_11_1:
			LeanTween.moveX(rtf(arg_3_0._tf), 1000, 0.5)
		else
			LeanTween.moveX(rtf(arg_3_0._tf), -423, 0.5))

def var_0_0.OnNextOn(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = 0

	for iter_12_0, iter_12_1 in ipairs(arg_12_0.displays):
		if iter_12_1.id == arg_12_1:
			var_12_0 = iter_12_0

			break

	local var_12_1 = var_12_0 + arg_12_2

	if var_12_1 <= 0 or var_12_1 > #arg_12_0.displays:
		return

	local var_12_2 = False
	local var_12_3 = arg_12_0.displays[var_12_1]

	for iter_12_2, iter_12_3 in pairs(arg_12_0.cards):
		if iter_12_3.commanderVO and iter_12_3.commanderVO.id == var_12_3.id:
			var_12_2 = True

			triggerButton(iter_12_3.infoTF)

			break

	if not var_12_2:
		arg_12_0.emit(CommanderCatScene.EVENT_SELECTED, var_12_3)

def var_0_0.OnSort(arg_13_0):
	local var_13_0 = arg_13_0.sortData.asc

	arg_13_0.sortData = arg_13_0.indexPanel.data
	arg_13_0.sortData.asc = var_13_0

	arg_13_0.UpdateSortTxt()
	arg_13_0.UpdateCommanders(False)
	setActive(arg_13_0.ascTr, arg_13_0.sortData.asc)
	setActive(arg_13_0.descTr, not arg_13_0.sortData.asc)

def var_0_0.UpdateSortTxt(arg_14_0):
	setActive(arg_14_0.sortIdTxt, arg_14_0.sortData.sortData == "id")
	setActive(arg_14_0.sortLvTxt, arg_14_0.sortData.sortData == "Level")
	setActive(arg_14_0.sortRarityTxt, arg_14_0.sortData.sortData == "Rarity")

def var_0_0.OnInit(arg_15_0):
	arg_15_0.onCommander = arg_15_0.contextData.onCommander or function(arg_16_0, arg_16_1, arg_16_2, arg_16_3)
		return True
	arg_15_0.onSelected = arg_15_0.contextData.onSelected or function(arg_17_0, arg_17_1)
		arg_17_1()
	arg_15_0.onQuit = arg_15_0.contextData.onQuit or function(arg_18_0)
		return

	arg_15_0.RegisterEvent()

	arg_15_0.sortData = arg_15_0.contextData.sortData or {
		asc = False,
		sortData = "Level",
		nationData = {},
		rarityData = {}
	}

	function arg_15_0.scrollRect.onInitItem(arg_19_0)
		arg_15_0.OnInitItem(arg_19_0)

	function arg_15_0.scrollRect.onUpdateItem(arg_20_0, arg_20_1)
		arg_15_0.OnUpdateItem(arg_20_0, arg_20_1)

	onButton(arg_15_0, arg_15_0.reserveBtn, function()
		arg_15_0.reservePanel.ExecuteAction("Update"), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.boxesBtn, function()
		arg_15_0.boxesPanel.ExecuteAction("Update"), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.ascBtn, function()
		arg_15_0.sortData.asc = not arg_15_0.sortData.asc

		setActive(arg_15_0.ascTr, arg_15_0.sortData.asc)
		setActive(arg_15_0.descTr, not arg_15_0.sortData.asc)
		arg_15_0.UpdateCommanders(False), SFX_PANEL)
	setActive(arg_15_0.ascTr, arg_15_0.sortData.asc)
	setActive(arg_15_0.descTr, not arg_15_0.sortData.asc)
	onButton(arg_15_0, arg_15_0.sortBtn, function()
		arg_15_0.indexPanel.ExecuteAction("Show", arg_15_0.sortData), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.selectedBtn, function()
		local var_25_0 = arg_15_0.contextData.minCount or 1

		if var_25_0 > #arg_15_0.selectedList:
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_select_min_cnt", var_25_0))

			return

		arg_15_0.onSelected(arg_15_0.selectedList, function()
			arg_15_0.emit(CommanderCatScene.EVENT_BACK)), SFX_PANEL)
	onButton(arg_15_0, arg_15_0.cancelBtn, function()
		arg_15_0.emit(CommanderCatScene.EVENT_BACK), SFX_PANEL)

	if not LOCK_CATTERY:
		onButton(arg_15_0, arg_15_0.homeBtn, function()
			arg_15_0.emit(CommanderCatMediator.OPEN_HOME), SFX_PANEL)
	else
		setActive(arg_15_0.homeBtn, False)

	arg_15_0.Flush()

def var_0_0.Flush(arg_29_0):
	arg_29_0.cards = {}
	arg_29_0.selectedList = arg_29_0.contextData.selectedIds or {}
	arg_29_0.previewCommander = arg_29_0.contextData.activeCommander
	arg_29_0.previewCommanderId = arg_29_0.previewCommander and arg_29_0.previewCommander.id
	arg_29_0.selectedId = arg_29_0.previewCommanderId or arg_29_0.contextData.selectedId

	arg_29_0.UpdateCommanders(True)
	arg_29_0.UpdateBoxes()
	arg_29_0.UpdateReserve()
	arg_29_0.UpdateCapacity()
	arg_29_0.UpdateHome()
	arg_29_0.TryPlayStory()
	arg_29_0.DisplayCatterySettlement()
	arg_29_0.UpdateStyle()
	arg_29_0.UpdateSortTxt()

def var_0_0.Show(arg_30_0):
	setActive(arg_30_0._tf, True)
	CommanderCatUtil.SetActive(arg_30_0._tf, True)

def var_0_0.Hide(arg_31_0):
	CommanderCatUtil.SetActive(arg_31_0._tf, False)

def var_0_0.UpdateStyle(arg_32_0):
	setActive(arg_32_0.selectedTr, arg_32_0.contextData.mode == CommanderCatScene.MODE_SELECT)
	setActive(arg_32_0.btnsTr, arg_32_0.contextData.mode == CommanderCatScene.MODE_VIEW)

	if arg_32_0.contextData.mode == CommanderCatScene.MODE_SELECT:
		arg_32_0.UpdateSelectedTxt()

def var_0_0.TryPlayStory(arg_33_0):
	if arg_33_0.contextData.fromMain:
		pg.SystemGuideMgr.GetInstance().PlayCommander()

def var_0_0.DisplayCatterySettlement(arg_34_0):
	local var_34_0 = getProxy(CommanderProxy).GetCommanderHome()
	local var_34_1 = arg_34_0.contextData.fromMediatorName == NewMainMediator.__cname
	local var_34_2 = pg.NewStoryMgr.GetInstance().IsRunning() or pg.NewGuideMgr.GetInstance().IsBusy()

	if var_34_0 and var_34_0.ShouldSettleCattery() and var_34_1 and not var_34_2:
		local var_34_3 = Clone(var_34_0)

		arg_34_0.catterySettlementPage.ExecuteAction("Show", var_34_3)

	pg.m02.sendNotification(GAME.OPEN_OR_CLOSE_CATTERY, {
		open = True
	})

def var_0_0.UpdateHome(arg_35_0):
	local var_35_0 = getProxy(CommanderProxy)

	setActive(arg_35_0.homeTip, var_35_0.AnyCatteryExistOP() or var_35_0.AnyCatteryCanUse())

	local var_35_1 = var_35_0.GetCommanderHome()
	local var_35_2 = ""

	if var_35_1:
		var_35_2 = var_35_1.GetExistCommanderCattertCnt() .. "/" .. var_35_1.GetMaxCatteryCnt()

	arg_35_0.homeTxt.text = var_35_2

def var_0_0.UpdateCapacity(arg_36_0):
	local var_36_0 = getProxy(PlayerProxy).getRawData()
	local var_36_1 = table.getCount(getProxy(CommanderProxy).getRawData())

	arg_36_0.capacityTxt.text = var_36_1 .. "/" .. var_36_0.commanderBagMax

def var_0_0.UpdateReserve(arg_37_0):
	local var_37_0 = getProxy(CommanderProxy).getBoxUseCnt()

	arg_37_0.reserveTxt.text = CommanderConst.MAX_GETBOX_CNT - var_37_0 .. "/" .. CommanderConst.MAX_GETBOX_CNT

	setActive(arg_37_0.reserveTip, var_37_0 == 0)

def var_0_0.UpdateBoxes(arg_38_0):
	local var_38_0 = getProxy(CommanderProxy).getBoxes()
	local var_38_1 = _.select(var_38_0, function(arg_39_0)
		return arg_39_0.getState() == CommanderBox.STATE_FINISHED)

	arg_38_0.boxesTxt.text = #var_38_1 .. "/" .. #var_38_0

	setActive(arg_38_0.boxesTip, getProxy(CommanderProxy).ShouldTipBox())

def var_0_0.OnInitItem(arg_40_0, arg_40_1):
	local var_40_0 = arg_40_0.NewCard(arg_40_1)

	onButton(arg_40_0, var_40_0.infoTF, function()
		if not var_40_0.commanderVO:
			return

		if arg_40_0.contextData.mode == CommanderCatScene.MODE_SELECT:
			local var_41_0 = #arg_40_0.selectedList

			arg_40_0.OnCheckBefore(var_40_0.commanderVO)
			arg_40_0.Check(var_40_0.commanderVO)
			arg_40_0.OnCheckAfter(var_40_0.commanderVO, var_41_0 > #arg_40_0.selectedList)
		else
			arg_40_0.selectedList = {}

			for iter_41_0, iter_41_1 in pairs(arg_40_0.cards):
				iter_41_1.UpdateSelected(arg_40_0.selectedList)

			table.insert(arg_40_0.selectedList, var_40_0.commanderVO.id)
			var_40_0.UpdateSelected(arg_40_0.selectedList, not defaultValue(arg_40_0.sortData.displayCustomName, True))

			arg_40_0.selectedId = var_40_0.commanderVO.id

			arg_40_0.emit(CommanderCatScene.EVENT_SELECTED, var_40_0.commanderVO, True), SFX_PANEL)
	onButton(arg_40_0, var_40_0.quitTF, function()
		if not var_40_0.commanderVO:
			return

		if var_40_0.commanderVO.id == 0:
			arg_40_0.onQuit(function()
				arg_40_0.emit(CommanderCatScene.EVENT_BACK)), SFX_PANEL)

	arg_40_0.cards[arg_40_1] = var_40_0

def var_0_0.OnCheckBefore(arg_44_0, arg_44_1):
	if arg_44_0.previewCommander and arg_44_0.contextData.maxCount > 1:
		arg_44_0.emit(CommanderCatScene.EVENT_SELECTED, arg_44_0.previewCommander, True)
	else
		arg_44_0.emit(CommanderCatScene.EVENT_SELECTED, arg_44_1, True)

		if arg_44_0.previewCommander:
			arg_44_0.emit(CommanderCatScene.EVENT_PREVIEW_ADDITION, arg_44_0.previewCommander, True)
		else
			arg_44_0.emit(CommanderCatScene.EVENT_PREVIEW_ADDITION, arg_44_1, True)

def var_0_0.OnCheckAfter(arg_45_0, arg_45_1, arg_45_2):
	if arg_45_0.previewCommander and arg_45_0.contextData.maxCount > 1:
		arg_45_0.emit(CommanderCatScene.EVENT_PREVIEW_PLAY, arg_45_0.selectedList, arg_45_2)

def var_0_0.Check(arg_46_0, arg_46_1):
	local var_46_0 = arg_46_0.contextData.maxCount or table.getCount(arg_46_0.commanderList)

	if table.contains(arg_46_0.selectedList, arg_46_1.id) and var_46_0 == 1:
		arg_46_0.UpdateSelected()

		return
	elif table.contains(arg_46_0.selectedList, arg_46_1.id):
		local var_46_1 = table.indexof(arg_46_0.selectedList, arg_46_1.id)

		table.remove(arg_46_0.selectedList, var_46_1)
		arg_46_0.UpdateSelected()

		return

	local function var_46_2()
		for iter_47_0, iter_47_1 in ipairs(arg_46_0.selectedList):
			if iter_47_1 == arg_46_1.id:
				table.remove(arg_46_0.selectedList, iter_47_0)

				break

	local var_46_3, var_46_4 = arg_46_0.onCommander(arg_46_1, function()
		var_46_2()
		arg_46_0.UpdateSelected(), function()
		var_46_2()
		arg_46_0.UpdateCommanders(True)

		for iter_49_0, iter_49_1 in ipairs(arg_46_0.commanderList or {}):
			if iter_49_1.id == arg_46_1.id:
				arg_46_0.Check(iter_49_1)

		arg_46_0.UpdateSelected(), arg_46_0)

	if not var_46_3:
		if var_46_4:
			pg.TipsMgr.GetInstance().ShowTips(var_46_4)

		return

	if var_46_0 == 1:
		table.remove(arg_46_0.selectedList, #arg_46_0.selectedList)
	elif var_46_0 <= #arg_46_0.selectedList:
		pg.TipsMgr.GetInstance().ShowTips(i18n("commander_select_max"))
		arg_46_0.UpdateSelected()

		return

	table.insert(arg_46_0.selectedList, arg_46_1.id)
	arg_46_0.UpdateSelected()

def var_0_0.UpdateSelected(arg_50_0):
	for iter_50_0, iter_50_1 in pairs(arg_50_0.cards):
		iter_50_1.UpdateSelected(arg_50_0.selectedList)

	arg_50_0.UpdateSelectedTxt()

def var_0_0.UpdateSelectedTxt(arg_51_0):
	local var_51_0 = arg_51_0.contextData.maxCount or table.getCount(arg_51_0.commanderList)

	arg_51_0.selectedNumTxt.text = #arg_51_0.selectedList .. "/" .. var_51_0

def var_0_0.NewCard(arg_52_0, arg_52_1):
	if arg_52_0.contextData.mode == CommanderCatScene.MODE_VIEW or arg_52_0.contextData.maxCount == 1:
		return CommanderCatCard.New(arg_52_1, CommanderCatCard.MARK_TYPE_CIRCLE)
	else
		return CommanderCatCard.New(arg_52_1, CommanderCatCard.MARK_TYPE_TICK)

def var_0_0.OnUpdateItem(arg_53_0, arg_53_1, arg_53_2):
	local var_53_0 = arg_53_0.cards[arg_53_2]

	if not var_53_0:
		var_53_0 = arg_53_0.NewCard(arg_53_2)
		arg_53_0.cards[arg_53_2] = var_53_0

	local var_53_1 = arg_53_0.displays[arg_53_1 + 1]

	var_53_0.Update(var_53_1, arg_53_0.selectedList, not defaultValue(arg_53_0.sortData.displayCustomName, True))

	if var_53_1 and arg_53_0.selectedId and arg_53_0.selectedId == var_53_1.id and arg_53_0.shouldTrigger:
		arg_53_0.shouldTrigger = False

		triggerButton(var_53_0.infoTF)

local function var_0_1(arg_54_0, arg_54_1, arg_54_2)
	local var_54_0 = False
	local var_54_1 = False
	local var_54_2 = arg_54_0.getConfig("nationality")

	if table.getCount(arg_54_1) == 0 or arg_54_1[var_54_2] or arg_54_1[CommanderIndexPage.NATION_OTHER] and CommanderIndexPage.IsOtherNation(var_54_2):
		var_54_0 = True

	if table.getCount(arg_54_2) == 0 or arg_54_2[arg_54_0.getRarity()]:
		var_54_1 = True

	return var_54_0 and var_54_1

local function var_0_2(arg_55_0, arg_55_1, arg_55_2, arg_55_3, arg_55_4)
	local function var_55_0()
		if arg_55_3 == "id":
			return (arg_55_2 and {
				arg_55_0.id < arg_55_1.id
			} or {
				arg_55_0.id > arg_55_1.id
			})[1]
		else
			local var_56_0 = arg_55_0["get" .. arg_55_3](arg_55_0)
			local var_56_1 = arg_55_1["get" .. arg_55_3](arg_55_1)

			if var_56_0 == var_56_1:
				return (arg_55_2 and {
					arg_55_0.configId < arg_55_1.configId
				} or {
					arg_55_0.configId > arg_55_1.configId
				})[1]
			else
				return (arg_55_2 and {
					var_56_0 < var_56_1
				} or {
					var_56_1 < var_56_0
				})[1]

	local function var_55_1()
		local var_57_0 = arg_55_4 == arg_55_0.id and 1 or 0
		local var_57_1 = arg_55_4 == arg_55_1.id and 1 or 0

		if var_57_0 == var_57_1:
			return var_55_0()
		else
			return var_57_1 < var_57_0

	local var_55_2 = arg_55_0.inFleet and 1 or 0
	local var_55_3 = arg_55_1.inFleet and 1 or 0

	if var_55_2 == var_55_3:
		return var_55_1()
	else
		return var_55_3 < var_55_2

def var_0_0.UpdateCommanders(arg_58_0, arg_58_1):
	local var_58_0 = (arg_58_1 or not arg_58_0.commanderList) and CommanderCatUtil.GetCommanderList(arg_58_0.contextData) or arg_58_0.commanderList

	arg_58_0.shouldTrigger = True
	arg_58_0.displays = {}

	local var_58_1 = {}
	local var_58_2 = {}

	for iter_58_0, iter_58_1 in pairs(arg_58_0.sortData.nationData or {}):
		var_58_1[iter_58_1] = True

	for iter_58_2, iter_58_3 in ipairs(arg_58_0.sortData.rarityData or {}):
		var_58_2[iter_58_3] = True

	for iter_58_4, iter_58_5 in pairs(var_58_0):
		if var_0_1(iter_58_5, var_58_1, var_58_2):
			table.insert(arg_58_0.displays, iter_58_5)

	table.sort(arg_58_0.displays, function(arg_59_0, arg_59_1)
		return var_0_2(arg_59_0, arg_59_1, arg_58_0.sortData.asc, arg_58_0.sortData.sortData, arg_58_0.previewCommanderId))

	if not arg_58_0.selectedId and #arg_58_0.displays > 0:
		arg_58_0.selectedId = arg_58_0.displays[1].id
	elif #arg_58_0.displays > 0 and _.all(arg_58_0.displays, function(arg_60_0)
		return arg_60_0.id != arg_58_0.selectedId) and arg_58_0.previewCommander:
		arg_58_0.OnCheckBefore(arg_58_0.previewCommander)
		arg_58_0.OnCheckAfter(arg_58_0.previewCommander)

	if arg_58_0.previewCommanderId and arg_58_0.contextData.maxCount == 1:
		table.insert(arg_58_0.displays, 1, {
			id = 0
		})

	local var_58_3, var_58_4 = arg_58_0.FillList()

	arg_58_0.scrollRect.SetTotalCount(var_58_3, var_58_4)

	arg_58_0.commanderList = var_58_0

def var_0_0.FillList(arg_61_0):
	if arg_61_0.contextData.mode == CommanderCatScene.MODE_VIEW:
		local var_61_0 = #arg_61_0.displays % 4 > 0 and 4 - #arg_61_0.displays % 4 or 0
		local var_61_1 = #arg_61_0.displays + var_61_0
		local var_61_2

		if arg_61_0.selectedId:
			local var_61_3 = 0

			for iter_61_0, iter_61_1 in ipairs(arg_61_0.displays):
				if iter_61_1.id == arg_61_0.selectedId:
					var_61_3 = iter_61_0

					break

			var_61_2 = math.floor(var_61_3 / 4) / (#arg_61_0.displays / 4)

		return math.max(12, var_61_1), var_61_2 or arg_61_0.contextData.scrollValue or 0
	elif arg_61_0.contextData.mode == CommanderCatScene.MODE_SELECT:
		return #arg_61_0.displays, arg_61_0.contextData.scrollValue or 0

def var_0_0.CanBack(arg_62_0):
	if arg_62_0.boxesPanel and arg_62_0.boxesPanel.GetLoaded() and arg_62_0.boxesPanel.CanBack and not arg_62_0.boxesPanel.CanBack():
		return False

	if arg_62_0.reservePanel and arg_62_0.reservePanel.GetLoaded() and arg_62_0.reservePanel.isShowing():
		arg_62_0.reservePanel.Hide()

		return False

	if arg_62_0.boxesPanel and arg_62_0.boxesPanel.GetLoaded() and arg_62_0.boxesPanel.isShowing():
		arg_62_0.boxesPanel.Hide()

		return False

	if arg_62_0.indexPanel and arg_62_0.indexPanel.GetLoaded() and arg_62_0.indexPanel.isShowing():
		arg_62_0.indexPanel.Hide()

		return False

	return True

def var_0_0.OnDestroy(arg_63_0):
	for iter_63_0, iter_63_1 in pairs(arg_63_0.cards):
		iter_63_1.Dispose()

	if arg_63_0.reservePanel:
		arg_63_0.reservePanel.Destroy()

		arg_63_0.reservePanel = None

	if arg_63_0.boxesPanel:
		arg_63_0.boxesPanel.Destroy()

		arg_63_0.boxesPanel = None

	if arg_63_0.indexPanel:
		arg_63_0.indexPanel.Destroy()

		arg_63_0.indexPanel = None

	if arg_63_0.catterySettlementPage:
		arg_63_0.catterySettlementPage.Destroy()

		arg_63_0.catterySettlementPage = None

	arg_63_0.contextData.scrollValue = math.min(arg_63_0.scrollRect.value, 1)

return var_0_0