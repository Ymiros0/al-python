local var_0_0 = class("WorldMediaCollectionScene", require("view.base.BaseUI"))

var_0_0.PAGE_MEMORTY = 1
var_0_0.PAGE_FILE = 2
var_0_0.PAGE_RECORD = 3

def var_0_0.getUIName(arg_1_0):
	return "WorldMediaCollectionUI"

def var_0_0.getBGM(arg_2_0):
	local var_2_0 = arg_2_0.contextData.revertBgm

	arg_2_0.contextData.revertBgm = None

	if var_2_0:
		return var_2_0
	else
		return var_0_0.super.getBGM(arg_2_0)

def var_0_0.init(arg_3_0):
	arg_3_0.top = arg_3_0._tf.Find("Top")
	arg_3_0.viewContainer = arg_3_0._tf.Find("Main")
	arg_3_0.subViews = {}

local var_0_1 = {
	import(".WorldMediaCollectionMemoryLayer"),
	import(".WorldMediaCollectionRecordLayer"),
	import(".WorldMediaCollectionFileLayer")
}

def var_0_0.GetCurrentPage(arg_4_0):
	return arg_4_0.contextData.page and arg_4_0.subViews[arg_4_0.contextData.page]

def var_0_0.didEnter(arg_5_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_5_0.top, {
		groupName = LayerWeightConst.GROUP_COLLECTION
	})
	onButton(arg_5_0, arg_5_0.top.Find("blur_panel/adapt/top/option"), function()
		arg_5_0.quickExitFunc(), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.top.Find("blur_panel/adapt/top/back_btn"), function()
		arg_5_0.Backward(), SFX_UI_CANCEL)

	local var_5_0 = arg_5_0.contextData.page or var_0_0.PAGE_MEMORTY

	arg_5_0.contextData.page = None

	arg_5_0.EnterPage(var_5_0)
	arg_5_0.UpdateView()

def var_0_0.EnterPage(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1 == arg_8_0.contextData.page
	local var_8_1 = arg_8_0.subViews[arg_8_1]

	if not var_8_1:
		local var_8_2 = var_0_1[arg_8_1]

		if not var_8_2:
			return

		arg_8_0.contextData[var_8_2] = arg_8_0.contextData[var_8_2] or {}
		var_8_1 = var_8_2.New(arg_8_0, arg_8_0.viewContainer, arg_8_0.event, arg_8_0.contextData)

		var_8_1.Load()

	if arg_8_0.contextData.page and arg_8_0.subViews[arg_8_0.contextData.page] and not var_8_0:
		arg_8_0.subViews[arg_8_0.contextData.page].buffer.OnDeselected()

	arg_8_0.contextData.page = arg_8_1
	arg_8_0.subViews[arg_8_1] = var_8_1

	if not var_8_0:
		var_8_1.buffer.OnSelected()
	else
		var_8_1.buffer.OnReselected()

def var_0_0.Backward(arg_9_0):
	local var_9_0 = arg_9_0.subViews[arg_9_0.contextData.page]
	local var_9_1 = var_9_0 and var_9_0.OnBackward()

	if var_9_1:
		return var_9_1

	arg_9_0.closeView()

def var_0_0.onBackPressed(arg_10_0):
	arg_10_0.Backward()

def var_0_0.Add2LayerContainer(arg_11_0, arg_11_1):
	setParent(arg_11_1, arg_11_0.viewContainer)

def var_0_0.Add2TopContainer(arg_12_0, arg_12_1):
	setParent(arg_12_1, arg_12_0.top)

def var_0_0.WorldRecordLock():
	local function var_13_0()
		local var_14_0 = getProxy(PlayerProxy).getRawData().level

		return pg.SystemOpenMgr.GetInstance().isOpenSystem(var_14_0, "WorldMediaCollectionRecordMediator")

	return LOCK_WORLD_COLLECTION or not var_13_0()

def var_0_0.UpdateView(arg_15_0):
	local var_15_0 = arg_15_0.subViews[arg_15_0.contextData.page]

	if not var_15_0:
		return

	var_15_0.buffer.UpdateView()

def var_0_0.willExit(arg_16_0):
	local var_16_0 = arg_16_0.GetCurrentPage()

	if var_16_0:
		var_16_0.buffer.Hide()

	for iter_16_0, iter_16_1 in pairs(arg_16_0.subViews):
		iter_16_1.Destroy()

	table.clear(arg_16_0.subViews)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_16_0.top, arg_16_0._tf)

return var_0_0
