﻿local var_0_0 = class("IdolMedalCollectionView", import("view.base.BaseUI"))

var_0_0.FADE_OUT_TIME = 1
var_0_0.PAGE_NUM = 5
var_0_0.MEDAL_NUM_PER_PAGE = 3

function var_0_0.getUIName(arg_1_0)
	return "IdolMedalCollectionUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:initData()
	arg_2_0:findUI()
	arg_2_0:addListener()
end

function var_0_0.didEnter(arg_3_0)
	arg_3_0:checkAward()
	setText(arg_3_0.progressText, setColorStr(tostring(#arg_3_0.activeIDList), COLOR_RED) .. "/" .. #arg_3_0.allIDList)
	triggerToggle(arg_3_0.switchBtnList[1], true)
end

function var_0_0.willExit(arg_4_0)
	return
end

function var_0_0.initData(arg_5_0)
	arg_5_0.activityProxy = getProxy(ActivityProxy)
	arg_5_0.activityData = arg_5_0.activityProxy:getActivityById(ActivityConst.IDOL_MEDAL_COLLECTION)
	arg_5_0.allIDList = arg_5_0.activityData:GetPicturePuzzleIds()
	arg_5_0.pageIDList = {}

	for iter_5_0 = 1, var_0_0.PAGE_NUM do
		arg_5_0.pageIDList[iter_5_0] = {}

		for iter_5_1 = 1, var_0_0.MEDAL_NUM_PER_PAGE do
			arg_5_0.pageIDList[iter_5_0][iter_5_1] = arg_5_0.allIDList[(iter_5_0 - 1) * var_0_0.MEDAL_NUM_PER_PAGE + iter_5_1]
		end
	end

	arg_5_0.activatableIDList = arg_5_0.activityData.data1_list
	arg_5_0.activeIDList = arg_5_0.activityData.data2_list
	arg_5_0.curPage = nil
	arg_5_0.newMedalID = nil
end

function var_0_0.findUI(arg_6_0)
	arg_6_0.bg = arg_6_0:findTF("BG")

	local var_6_0 = arg_6_0:findTF("NotchAdapt")

	arg_6_0.backBtn = arg_6_0:findTF("BackBtn", var_6_0)
	arg_6_0.progressText = arg_6_0:findTF("ProgressImg/ProgressText", var_6_0)
	arg_6_0.helpBtn = arg_6_0:findTF("HelpBtn", var_6_0)

	local var_6_1 = arg_6_0:findTF("MedalContainer")

	arg_6_0.medalItemList = {}
	arg_6_0.medalItemList[1] = arg_6_0:findTF("Medal1", var_6_1)
	arg_6_0.medalItemList[2] = arg_6_0:findTF("Medal2", var_6_1)
	arg_6_0.medalItemList[3] = arg_6_0:findTF("Medal3", var_6_1)

	local var_6_2 = arg_6_0:findTF("SwitchBtnList", var_6_0)

	arg_6_0.switchBtnList = {}

	for iter_6_0 = 1, 5 do
		arg_6_0.switchBtnList[iter_6_0] = arg_6_0:findTF("Button" .. iter_6_0, var_6_2)
	end
end

function var_0_0.addListener(arg_7_0)
	onButton(arg_7_0, arg_7_0.backBtn, function()
		arg_7_0:closeView()
	end, SFX_CANCEL)
	onButton(arg_7_0, arg_7_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.music_collection.tip
		})
	end, SFX_PANEL)

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.switchBtnList) do
		onToggle(arg_7_0, iter_7_1, function(arg_10_0)
			if arg_10_0 == true then
				arg_7_0.curPage = iter_7_0

				arg_7_0:updateSwitchBtnTF()
				arg_7_0:updateMedalContainerView(iter_7_0)
			end
		end, SFX_PANEL)
	end

	addSlip(SLIP_TYPE_HRZ, arg_7_0.bg, function()
		if arg_7_0.curPage > 1 then
			triggerToggle(arg_7_0.switchBtnList[arg_7_0.curPage - 1], true)
		else
			return
		end
	end, function()
		if arg_7_0.curPage < var_0_0.PAGE_NUM then
			triggerToggle(arg_7_0.switchBtnList[arg_7_0.curPage + 1], true)
		else
			return
		end
	end)
end

function var_0_0.updateMedalContainerView(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_0.pageIDList[arg_13_1]

	for iter_13_0, iter_13_1 in ipairs(var_13_0) do
		arg_13_0:updateMedalView(var_13_0, iter_13_1)
	end
end

function var_0_0.updateMedalView(arg_14_0, arg_14_1, arg_14_2)
	local var_14_0 = table.indexof(arg_14_1, arg_14_2, 1)
	local var_14_1 = table.contains(arg_14_0.activeIDList, arg_14_2)
	local var_14_2 = table.contains(arg_14_0.activatableIDList, arg_14_2) and not var_14_1
	local var_14_3 = not var_14_1 and not var_14_2
	local var_14_4 = arg_14_0.medalItemList[var_14_0]
	local var_14_5 = arg_14_0:findTF("Active", var_14_4)
	local var_14_6 = arg_14_0:findTF("Activable", var_14_4)
	local var_14_7 = arg_14_0:findTF("DisActive", var_14_4)

	setActive(var_14_5, var_14_1)
	setActive(var_14_6, var_14_2)
	setActive(var_14_7, var_14_3)

	if var_14_5 then
		setImageSprite(var_14_5, GetSpriteFromAtlas("ui/musicfestivalmedalcollectionui_atlas", tostring(arg_14_2)))
	end

	if var_14_2 then
		onButton(arg_14_0, var_14_6, function()
			pg.m02:sendNotification(GAME.MEMORYBOOK_UNLOCK, {
				id = arg_14_2,
				actId = ActivityConst.IDOL_MEDAL_COLLECTION
			})
		end, SFX_PANEL)
	end

	if var_14_3 then
		local var_14_8 = table.indexof(arg_14_0.allIDList, arg_14_2, 1)
		local var_14_9 = arg_14_0.activityData:getConfig("config_client").unlock_desc[var_14_8]

		setText(var_14_7, var_14_9)
	end
end

function var_0_0.updateSwitchBtnTF(arg_16_0)
	for iter_16_0, iter_16_1 in ipairs(arg_16_0.switchBtnList) do
		local var_16_0 = arg_16_0:findTF("Tip", iter_16_1)
		local var_16_1 = arg_16_0:findTF("Text", var_16_0)
		local var_16_2 = arg_16_0:caculateActivatable(iter_16_0)

		if var_16_2 == 0 or iter_16_0 == arg_16_0.curPage then
			setActive(var_16_0, false)
		end

		if var_16_2 > 0 and iter_16_0 ~= arg_16_0.curPage then
			setActive(var_16_0, true)
			setText(var_16_1, var_16_2)
		end
	end
end

function var_0_0.updateAfterSubmit(arg_17_0, arg_17_1)
	arg_17_0.activityProxy = getProxy(ActivityProxy)
	arg_17_0.activityData = arg_17_0.activityProxy:getActivityById(ActivityConst.IDOL_MEDAL_COLLECTION)
	arg_17_0.activatableIDList = arg_17_0.activityData.data1_list
	arg_17_0.activeIDList = arg_17_0.activityData.data2_list
	arg_17_0.newMedalID = arg_17_1

	triggerToggle(arg_17_0.switchBtnList[arg_17_0.curPage], true)
	setText(arg_17_0.progressText, setColorStr(tostring(#arg_17_0.activeIDList), COLOR_RED) .. "/" .. #arg_17_0.allIDList)
	arg_17_0:checkAward()
end

function var_0_0.UpdateActivity(arg_18_0)
	return
end

function var_0_0.caculateActivatable(arg_19_0, arg_19_1)
	local var_19_0 = arg_19_0.pageIDList[arg_19_1]
	local var_19_1 = 0

	for iter_19_0, iter_19_1 in ipairs(var_19_0) do
		local var_19_2 = table.contains(arg_19_0.activeIDList, iter_19_1)
		local var_19_3 = table.contains(arg_19_0.activatableIDList, iter_19_1)

		if not var_19_2 and var_19_3 then
			var_19_1 = var_19_1 + 1
		end
	end

	return var_19_1
end

function var_0_0.checkAward(arg_20_0)
	if #arg_20_0.activeIDList == #arg_20_0.allIDList and arg_20_0.activityData.data1 ~= 1 then
		pg.m02:sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = ActivityConst.IDOL_MEDAL_COLLECTION
		})
	end
end

return var_0_0
