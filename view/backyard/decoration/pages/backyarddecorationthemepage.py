local var_0_0 = class("BackYardDecorationThemePage", import(".BackYardDecorationBasePage"))

def var_0_0.getUIName(arg_1_0):
	return "BackYardDecorationThemePage"

def var_0_0.OnLoaded(arg_2_0):
	var_0_0.super.OnLoaded(arg_2_0)

	arg_2_0.msgbox = BackYardDecorationMsgBox.New(arg_2_0._parentTf.parent.parent.parent.parent.parent, arg_2_0.event, arg_2_0.contextData)
	arg_2_0.refreshList = {}

def var_0_0.OnDisplayList(arg_3_0):
	arg_3_0.InitList()

def var_0_0.InitList(arg_4_0):
	arg_4_0.displays = {}

	local var_4_0 = arg_4_0.dorm.GetPurchasedFurnitures()
	local var_4_1 = getProxy(DormProxy).GetSystemThemes()

	for iter_4_0, iter_4_1 in ipairs(var_4_1):
		if iter_4_1.IsPurchased(var_4_0):
			table.insert(arg_4_0.displays, iter_4_1)

	local var_4_2 = 0

	if arg_4_0.customTheme:
		for iter_4_2, iter_4_3 in pairs(arg_4_0.customTheme):
			var_4_2 = var_4_2 + 1

			table.insert(arg_4_0.displays, iter_4_3)

	if var_4_2 < BackYardConst.MAX_USER_THEME:
		table.insert(arg_4_0.displays, {
			id = "",
			isEmpty = True
		})

	arg_4_0.SortDisplays()

local function var_0_1(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_0.isEmpty and 1 or 0
	local var_5_1 = arg_5_1.isEmpty and 1 or 0

	if var_5_0 == var_5_1:
		local var_5_2 = arg_5_0.IsSystem() and 1 or 0
		local var_5_3 = arg_5_1.IsSystem() and 1 or 0

		if var_5_2 == var_5_3:
			if arg_5_0.order == arg_5_1.order:
				return arg_5_0.id > arg_5_1.id
			else
				return arg_5_0.order > arg_5_1.order
		else
			return var_5_2 < var_5_3
	else
		return var_5_1 < var_5_0

local function var_0_2(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_0.isEmpty and 1 or 0
	local var_6_1 = arg_6_1.isEmpty and 1 or 0

	if var_6_0 == var_6_1:
		local var_6_2 = arg_6_0.IsSystem() and 1 or 0
		local var_6_3 = arg_6_1.IsSystem() and 1 or 0

		if var_6_2 == var_6_3:
			if arg_6_0.order == arg_6_1.order:
				return arg_6_0.id < arg_6_1.id
			else
				return arg_6_0.order < arg_6_1.order
		else
			return var_6_3 < var_6_2
	else
		return var_6_1 < var_6_0

def var_0_0.SortDisplays(arg_7_0):
	table.sort(arg_7_0.displays, function(arg_8_0, arg_8_1)
		if arg_7_0.orderMode == BackYardDecorationFilterPanel.ORDER_MODE_ASC:
			return var_0_2(arg_8_0, arg_8_1)
		else
			return var_0_1(arg_8_0, arg_8_1))
	arg_7_0.SetTotalCount()

def var_0_0.OnOrderModeUpdated(arg_9_0):
	arg_9_0.SortDisplays()

def var_0_0.OnInitItem(arg_10_0, arg_10_1):
	local var_10_0 = BackYardDecorationThemeCard.New(arg_10_1)

	onButton(arg_10_0, var_10_0._tf, function()
		if var_10_0.HasMask():
			return

		arg_10_0.msgbox.ExecuteAction("Show", var_10_0.themeVO, True))
	onButton(arg_10_0, var_10_0.add, function()
		local var_12_0 = getProxy(DormProxy).GetTemplateNewID()

		arg_10_0.msgbox.ExecuteAction("Show", {
			id = var_12_0
		}, False))

	arg_10_0.cards[arg_10_1] = var_10_0

def var_0_0.OnUpdateItem(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = arg_13_0.cards[arg_13_2]

	if not var_13_0:
		arg_13_0.OnInitItem(arg_13_2)

		var_13_0 = arg_13_0.cards[arg_13_2]

	local var_13_1 = arg_13_0.lastDiaplys[arg_13_1 + 1]

	var_13_0.Update(var_13_1, False)

def var_0_0.OnThemeUpdated(arg_14_0):
	arg_14_0.currHouse = None

	arg_14_0.InitList()

def var_0_0.OnApplyThemeBefore(arg_15_0):
	arg_15_0.currHouse = None

	for iter_15_0, iter_15_1 in pairs(arg_15_0.cards):
		iter_15_1.Update(iter_15_1.themeVO, False)

	arg_15_0.temps = {}

def var_0_0.OnApplyThemeAfter(arg_16_0, arg_16_1):
	for iter_16_0, iter_16_1 in pairs(arg_16_0.cards):
		if iter_16_1.themeVO.id == arg_16_1:
			iter_16_1.Update(iter_16_1.themeVO, False)

def var_0_0.SetTotalCount(arg_17_0):
	if not arg_17_0.searchKey or arg_17_0.searchKey == "":
		arg_17_0.lastDiaplys = arg_17_0.displays
	else
		arg_17_0.lastDiaplys = {}

		for iter_17_0, iter_17_1 in ipairs(arg_17_0.displays):
			if iter_17_1.id == "" or iter_17_1.MatchSearchKey(arg_17_0.searchKey):
				table.insert(arg_17_0.lastDiaplys, iter_17_1)

	arg_17_0.scrollRect.SetTotalCount(#arg_17_0.lastDiaplys)

def var_0_0.OnSearchKeyChanged(arg_18_0):
	arg_18_0.SetTotalCount()

def var_0_0.OnDestroy(arg_19_0):
	arg_19_0.msgbox.Destroy()

	for iter_19_0, iter_19_1 in pairs(arg_19_0.cards or {}):
		iter_19_1.Dispose()

	arg_19_0.cards = None

def var_0_0.OnBackPressed(arg_20_0):
	if arg_20_0.GetLoaded() and arg_20_0.msgbox.GetLoaded() and arg_20_0.msgbox.isShowing():
		arg_20_0.msgbox.Hide()

		return True

	return False

return var_0_0
