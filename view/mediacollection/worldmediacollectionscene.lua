local var_0_0 = class("WorldMediaCollectionScene", require("view.base.BaseUI"))

var_0_0.PAGE_MEMORTY = 1
var_0_0.PAGE_FILE = 2
var_0_0.PAGE_RECORD = 3

function var_0_0.getUIName(arg_1_0)
	return "WorldMediaCollectionUI"
end

function var_0_0.getBGM(arg_2_0)
	local var_2_0 = arg_2_0.contextData.revertBgm

	arg_2_0.contextData.revertBgm = nil

	if var_2_0 then
		return var_2_0
	else
		return var_0_0.super.getBGM(arg_2_0)
	end
end

function var_0_0.init(arg_3_0)
	arg_3_0.top = arg_3_0._tf:Find("Top")
	arg_3_0.viewContainer = arg_3_0._tf:Find("Main")
	arg_3_0.subViews = {}
end

local var_0_1 = {
	import(".WorldMediaCollectionMemoryLayer"),
	import(".WorldMediaCollectionRecordLayer"),
	import(".WorldMediaCollectionFileLayer")
}

function var_0_0.GetCurrentPage(arg_4_0)
	return arg_4_0.contextData.page and arg_4_0.subViews[arg_4_0.contextData.page]
end

function var_0_0.didEnter(arg_5_0)
	pg.UIMgr.GetInstance():OverlayPanel(arg_5_0.top, {
		groupName = LayerWeightConst.GROUP_COLLECTION
	})
	onButton(arg_5_0, arg_5_0.top:Find("blur_panel/adapt/top/option"), function()
		arg_5_0:quickExitFunc()
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.top:Find("blur_panel/adapt/top/back_btn"), function()
		arg_5_0:Backward()
	end, SFX_UI_CANCEL)

	local var_5_0 = arg_5_0.contextData.page or var_0_0.PAGE_MEMORTY

	arg_5_0.contextData.page = nil

	arg_5_0:EnterPage(var_5_0)
	arg_5_0:UpdateView()
end

function var_0_0.EnterPage(arg_8_0, arg_8_1)
	local var_8_0 = arg_8_1 == arg_8_0.contextData.page
	local var_8_1 = arg_8_0.subViews[arg_8_1]

	if not var_8_1 then
		local var_8_2 = var_0_1[arg_8_1]

		if not var_8_2 then
			return
		end

		arg_8_0.contextData[var_8_2] = arg_8_0.contextData[var_8_2] or {}
		var_8_1 = var_8_2.New(arg_8_0, arg_8_0.viewContainer, arg_8_0.event, arg_8_0.contextData)

		var_8_1:Load()
	end

	if arg_8_0.contextData.page and arg_8_0.subViews[arg_8_0.contextData.page] and not var_8_0 then
		arg_8_0.subViews[arg_8_0.contextData.page].buffer:OnDeselected()
	end

	arg_8_0.contextData.page = arg_8_1
	arg_8_0.subViews[arg_8_1] = var_8_1

	if not var_8_0 then
		var_8_1.buffer:OnSelected()
	else
		var_8_1.buffer:OnReselected()
	end
end

function var_0_0.Backward(arg_9_0)
	local var_9_0 = arg_9_0.subViews[arg_9_0.contextData.page]
	local var_9_1 = var_9_0 and var_9_0:OnBackward()

	if var_9_1 then
		return var_9_1
	end

	arg_9_0:closeView()
end

function var_0_0.onBackPressed(arg_10_0)
	arg_10_0:Backward()
end

function var_0_0.Add2LayerContainer(arg_11_0, arg_11_1)
	setParent(arg_11_1, arg_11_0.viewContainer)
end

function var_0_0.Add2TopContainer(arg_12_0, arg_12_1)
	setParent(arg_12_1, arg_12_0.top)
end

function var_0_0.WorldRecordLock()
	local function var_13_0()
		local var_14_0 = getProxy(PlayerProxy):getRawData().level

		return pg.SystemOpenMgr.GetInstance():isOpenSystem(var_14_0, "WorldMediaCollectionRecordMediator")
	end

	return LOCK_WORLD_COLLECTION or not var_13_0()
end

function var_0_0.UpdateView(arg_15_0)
	local var_15_0 = arg_15_0.subViews[arg_15_0.contextData.page]

	if not var_15_0 then
		return
	end

	var_15_0.buffer:UpdateView()
end

function var_0_0.willExit(arg_16_0)
	local var_16_0 = arg_16_0:GetCurrentPage()

	if var_16_0 then
		var_16_0.buffer:Hide()
	end

	for iter_16_0, iter_16_1 in pairs(arg_16_0.subViews) do
		iter_16_1:Destroy()
	end

	table.clear(arg_16_0.subViews)
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_16_0.top, arg_16_0._tf)
end

return var_0_0
