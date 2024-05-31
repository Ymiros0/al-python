local var_0_0 = class("AttireAchievementPanel", import("...base.BaseSubView"))

local function var_0_1(arg_1_0)
	local var_1_0 = {}

	local function var_1_1(arg_2_0)
		arg_2_0._go = arg_1_0
		arg_2_0.info = findTF(arg_2_0._go, "info")
		arg_2_0.empty = findTF(arg_2_0._go, "empty")
		arg_2_0.icon = findTF(arg_2_0._go, "info/icon")
		arg_2_0.selected = findTF(arg_2_0._go, "info/selected")
		arg_2_0.nameTxt = findTF(arg_2_0._go, "info/label/Text")
		arg_2_0.tags = {
			findTF(arg_2_0._go, "info/tags/new"),
			findTF(arg_2_0._go, "info/tags/e")
		}
		arg_2_0.print5 = findTF(arg_2_0._go, "prints/line5")
		arg_2_0.print6 = findTF(arg_2_0._go, "prints/line6")

	function var_1_0.Update(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
		arg_3_0.trophy = arg_3_1

		if arg_3_0.trophy:
			LoadImageSpriteAsync("medal/" .. arg_3_1.getConfig("icon"), arg_3_0.icon, True)
			setText(arg_3_0.nameTxt, arg_3_1.getConfig("name"))
			setActive(arg_3_0.tags[1], arg_3_1.isNew())
			arg_3_0.UpdateSelected(arg_3_2)

		setActive(arg_3_0.print5, not arg_3_3)
		setActive(arg_3_0.print6, not arg_3_3)
		setActive(arg_3_0.info, arg_3_0.trophy)
		setActive(arg_3_0.empty, not arg_3_0.trophy)

	function var_1_0.UpdateSelected(arg_4_0, arg_4_1)
		setActive(arg_4_0.selected, arg_4_1)
		setActive(arg_4_0.tags[2], arg_4_1)

	var_1_1(var_1_0)

	return var_1_0

local function var_0_2(arg_5_0)
	local var_5_0 = {}

	local function var_5_1(arg_6_0)
		arg_6_0._tf = arg_5_0
		arg_6_0.uiList = UIItemList.New(arg_6_0._tf.Find("list"), arg_6_0._tf.Find("list/tpl"))

	function var_5_0.Update(arg_7_0, arg_7_1)
		arg_7_0.uiList.make(function(arg_8_0, arg_8_1, arg_8_2)
			if arg_8_0 == UIItemList.EventUpdate:
				local var_8_0 = arg_7_1[arg_8_1 + 1]
				local var_8_1 = Trophy.New({
					id = var_8_0
				})
				local var_8_2 = findTF(arg_8_2, "icon")

				LoadImageSpriteAsync("medal/s_" .. var_8_1.getConfig("icon"), var_8_2, True))
		arg_7_0.uiList.align(#arg_7_1)

	function var_5_0.Dispose(arg_9_0)
		return

	var_5_1(var_5_0)

	return var_5_0

def var_0_0.getUIName(arg_10_0):
	return "AttireAchievementUI"

def var_0_0.OnInit(arg_11_0):
	arg_11_0.listPanel = arg_11_0.findTF("list_panel")
	arg_11_0.scolrect = arg_11_0.findTF("scrollrect", arg_11_0.listPanel).GetComponent("LScrollRect")
	arg_11_0.totalCount = arg_11_0.findTF("total_count/Text").GetComponent(typeof(Text))
	arg_11_0.selectedTxt = arg_11_0.listPanel.Find("selected_bg/Text").GetComponent(typeof(Text))
	arg_11_0.toggle = arg_11_0.listPanel.Find("toggle")

	function arg_11_0.scolrect.onInitItem(arg_12_0)
		arg_11_0.OnInitItem(arg_12_0)

	function arg_11_0.scolrect.onUpdateItem(arg_13_0, arg_13_1)
		arg_11_0.OnUpdateItem(arg_13_0, arg_13_1)

	arg_11_0.confirmBtn = arg_11_0.findTF("list_panel/confirm")

	onButton(arg_11_0, arg_11_0.confirmBtn, function()
		if #arg_11_0.contextData.selectedMedalList == 0 and #arg_11_0.playerVO.displayTrophyList == 0:
			return

		if #arg_11_0.contextData.selectedMedalList == #arg_11_0.playerVO.displayTrophyList and _.all(arg_11_0.contextData.selectedMedalList, function(arg_15_0)
			return table.contains(arg_11_0.playerVO.displayTrophyList, arg_15_0)):
			return

		arg_11_0.event.emit(AttireMediator.ON_CHANGE_MEDAL_DISPLAY, arg_11_0.contextData.selectedMedalList), SFX_PANEL)

	arg_11_0.descPanel = var_0_2(arg_11_0.findTF("desc_panel"))
	arg_11_0.selectMaxLevel = True

	onToggle(arg_11_0, arg_11_0.toggle, function(arg_16_0)
		arg_11_0.selectMaxLevel = arg_16_0

		arg_11_0.Filter())

	arg_11_0.cards = {}
	arg_11_0.emptyPage = BaseEmptyListPage.New(arg_11_0.listPanel, arg_11_0.event)

def var_0_0.UpdateselectedTxt(arg_17_0):
	local var_17_0 = arg_17_0.contextData.selectedMedalList or {}

	arg_17_0.selectedTxt.text = #var_17_0 .. "/5"

def var_0_0.OnInitItem(arg_18_0, arg_18_1):
	local var_18_0 = var_0_1(arg_18_1)

	arg_18_0.cards[arg_18_1] = var_18_0

	onButton(arg_18_0, var_18_0._go, function()
		if not var_18_0.trophy:
			return

		local var_19_0 = arg_18_0.contextData.selectedMedalList or {}

		if #var_19_0 < 5 and not table.contains(var_19_0, var_18_0.trophy.id):
			table.insert(var_19_0, var_18_0.trophy.id)
			var_18_0.UpdateSelected(True)
		else
			for iter_19_0, iter_19_1 in ipairs(var_19_0):
				if iter_19_1 == var_18_0.trophy.id:
					table.remove(var_19_0, iter_19_0)
					var_18_0.UpdateSelected(False)

					break

		arg_18_0.contextData.selectedMedalList = var_19_0

		arg_18_0.descPanel.Update(arg_18_0.contextData.selectedMedalList)
		arg_18_0.UpdateselectedTxt(), SFX_PANEL)

def var_0_0.OnUpdateItem(arg_20_0, arg_20_1, arg_20_2):
	local var_20_0 = arg_20_0.cards[arg_20_2]

	if not var_20_0:
		arg_20_0.OnInitItem(arg_20_2)

		var_20_0 = arg_20_0.cards[arg_20_2]

	local var_20_1 = arg_20_0.displayVOs[arg_20_1 + 1]
	local var_20_2 = arg_20_1 < arg_20_0.scolrect.content.GetComponent(typeof(GridLayoutGroup)).constraintCount

	if var_20_1:
		local var_20_3 = table.contains(arg_20_0.contextData.selectedMedalList, var_20_1.id)

		var_20_0.Update(var_20_1, var_20_3, var_20_2)
	else
		var_20_0.Update(var_20_1, False, var_20_2)

def var_0_0.Update(arg_21_0, arg_21_1, arg_21_2):
	arg_21_0.playerVO = arg_21_2
	arg_21_0.trophys = arg_21_1.trophys
	arg_21_0.contextData.selectedMedalList = Clone(arg_21_0.playerVO.displayTrophyList) or {}

	arg_21_0.descPanel.Update(arg_21_0.contextData.selectedMedalList)
	arg_21_0.UpdateselectedTxt()
	arg_21_0.Filter()

	arg_21_0.totalCount.text = arg_21_0.getTotalCnt()

	local var_21_0 = arg_21_0.getTotalCnt()

	if var_21_0 <= 0:
		arg_21_0.emptyPage.ExecuteAction("ShowOrHide", True)
		arg_21_0.emptyPage.ExecuteAction("SetEmptyText", i18n("decoration_medal_placeholder"))
		arg_21_0.emptyPage.ExecuteAction("SetPosY", {
			x = 0,
			y = 22
		})
		setActive(arg_21_0.findTF("scrollrect", arg_21_0.listPanel), False)
	elif var_21_0 > 0 and arg_21_0.emptyPage.GetLoaded():
		arg_21_0.emptyPage.ExecuteAction("ShowOrHide", False)
		setActive(arg_21_0.findTF("scrollrect", arg_21_0.listPanel), True)

def var_0_0.getTotalCnt(arg_22_0):
	local var_22_0 = 0

	for iter_22_0, iter_22_1 in pairs(arg_22_0.trophys):
		if iter_22_1.isClaimed() and not iter_22_1.isHide():
			var_22_0 = var_22_0 + 1

	return var_22_0

def var_0_0.Filter(arg_23_0):
	arg_23_0.displayVOs = {}

	local function var_23_0(arg_24_0)
		local var_24_0 = arg_23_0.trophys[arg_24_0.getConfig("next")]

		return var_24_0 and var_24_0.isClaimed() and not var_24_0.isHide()

	for iter_23_0, iter_23_1 in pairs(arg_23_0.trophys):
		if iter_23_1.isClaimed() and not iter_23_1.isHide() and (not arg_23_0.selectMaxLevel or arg_23_0.selectMaxLevel and not var_23_0(iter_23_1)):
			table.insert(arg_23_0.displayVOs, iter_23_1)

	table.sort(arg_23_0.displayVOs, function(arg_25_0, arg_25_1)
		return arg_25_0.id < arg_25_1.id)

	local var_23_1 = arg_23_0.scolrect.content.GetComponent(typeof(GridLayoutGroup)).constraintCount
	local var_23_2 = var_23_1 - #arg_23_0.displayVOs % var_23_1

	if var_23_2 == var_23_1:
		var_23_2 = 0

	local var_23_3 = var_23_1 * arg_23_0.GetColumn()

	if var_23_3 > #arg_23_0.displayVOs:
		var_23_2 = var_23_3 - #arg_23_0.displayVOs

	for iter_23_2 = 1, var_23_2:
		table.insert(arg_23_0.displayVOs, False)

	arg_23_0.scolrect.SetTotalCount(#arg_23_0.displayVOs, -1)

def var_0_0.GetColumn(arg_26_0):
	return 2

def var_0_0.OnDestroy(arg_27_0):
	arg_27_0.descPanel.Dispose()

	if arg_27_0.emptyPage:
		arg_27_0.emptyPage.Destroy()

		arg_27_0.emptyPage = None

return var_0_0
