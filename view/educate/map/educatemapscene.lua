﻿local var_0_0 = class("EducateMapScene", import("..base.EducateBaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "EducateMapUI"
end

function var_0_0.preload(arg_2_0, arg_2_1)
	if getProxy(EducateProxy):NeedRequestOptsData() then
		pg.m02:sendNotification(GAME.EDUCATE_REQUEST_OPTION, {
			callback = arg_2_1
		})
	else
		arg_2_1()
	end
end

function var_0_0.init(arg_3_0)
	arg_3_0:initData()
	arg_3_0:findUI()
	arg_3_0:addListener()
end

function var_0_0.initData(arg_4_0)
	arg_4_0.config = pg.child_site
	arg_4_0.siteIdList = getProxy(EducateProxy):GetShowSiteIds()
end

function var_0_0.findUI(arg_5_0)
	arg_5_0.topTF = arg_5_0:findTF("ui/top")
	arg_5_0.homeBtn = arg_5_0:findTF("ui/home_btn/home_btn")

	setText(arg_5_0:findTF("Text", arg_5_0.homeBtn), i18n("child_btn_home"))

	arg_5_0.mapTF = arg_5_0:findTF("map")
	arg_5_0.mapContent = arg_5_0:findTF("content", arg_5_0.mapTF)
	arg_5_0.mapSiteTpl = arg_5_0:findTF("site_tpl", arg_5_0.mapTF)

	setText(arg_5_0:findTF("limit/Text", arg_5_0.mapSiteTpl), i18n("child_option_limit"))
	setActive(arg_5_0.mapSiteTpl, false)

	arg_5_0.siteUIList = UIItemList.New(arg_5_0.mapContent, arg_5_0.mapSiteTpl)
	arg_5_0.datePanel = EducateDatePanel.New(arg_5_0:findTF("date", arg_5_0.topTF), arg_5_0.event)

	arg_5_0.datePanel:Load()

	arg_5_0.resPanel = EducateResPanel.New(arg_5_0:findTF("res", arg_5_0.topTF), arg_5_0.event, {
		showBg = true
	})

	arg_5_0.resPanel:Load()

	arg_5_0.topPanel = EducateTopPanel.New(arg_5_0:findTF("top_right", arg_5_0.topTF), arg_5_0.event)

	arg_5_0.topPanel:Load()

	arg_5_0.targetPanel = EducateTargetPanel.New(arg_5_0:findTF("ui/target"), arg_5_0.event)

	arg_5_0.targetPanel:Load()

	arg_5_0.archivePanel = EducateArchivePanel.New(arg_5_0:findTF("ui/archive_panel"), arg_5_0.event)

	arg_5_0.archivePanel:Load()

	arg_5_0.detailPanel = EducateSiteDetailPanel.New(arg_5_0:findTF("ui/detail_panel"), arg_5_0.event, {
		onEnter = function()
			arg_5_0:MoveTargetPanelLeft()
		end,
		onExit = function()
			arg_5_0:MoveTargetPanelRight()
		end
	})

	arg_5_0.detailPanel:Load()
end

function var_0_0.addListener(arg_8_0)
	onButton(arg_8_0, arg_8_0.homeBtn, function()
		arg_8_0:emit(EducateBaseUI.EDUCATE_CHANGE_SCENE, SCENE.EDUCATE)
	end, SFX_PANEL)
end

function var_0_0.didEnter(arg_10_0)
	pg.UIMgr.GetInstance():OverlayPanel(arg_10_0.topTF, {
		groupName = arg_10_0:getGroupNameFromData(),
		weight = arg_10_0:getWeightFromData()
	})
	arg_10_0.siteUIList:make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate then
			arg_10_0:updateSiteItem(arg_11_1, arg_11_2)
		end
	end)
	arg_10_0.siteUIList:align(#arg_10_0.siteIdList)
	arg_10_0:playAnim()
	arg_10_0:CheckTips(function()
		arg_10_0.siteUIList:align(#arg_10_0.siteIdList)
	end)
end

function var_0_0.playAnim(arg_13_0)
	arg_13_0.siteUIList:each(function(arg_14_0, arg_14_1)
		setActive(arg_14_1, false)
	end)

	local var_13_0 = {}

	table.insert(var_13_0, function(arg_15_0)
		arg_13_0:managedTween(LeanTween.delayedCall, function()
			arg_15_0()
		end, 0.165, nil)
	end)

	for iter_13_0 = 1, #arg_13_0.siteIdList do
		table.insert(var_13_0, function(arg_17_0)
			setActive(arg_13_0.siteUIList.container:GetChild(iter_13_0 - 1), true)
			arg_13_0:managedTween(LeanTween.delayedCall, function()
				arg_17_0()
			end, 0.033, nil)
		end)
	end

	seriesAsync(var_13_0, function()
		return
	end)
end

function var_0_0.CheckTips(arg_20_0, arg_20_1)
	local var_20_0 = {}
	local var_20_1 = EducateTipHelper.GetSiteUnlockTipIds()

	if #var_20_1 > 0 then
		arg_20_0:emit(var_0_0.EDUCATE_ON_UNLOCK_TIP, {
			type = EducateUnlockTipLayer.UNLOCK_TYPE_SITE,
			list = var_20_1,
			onExit = arg_20_1
		})
	end
end

function var_0_0.updateSiteItem(arg_21_0, arg_21_1, arg_21_2)
	local var_21_0 = arg_21_0.config[arg_21_0.siteIdList[arg_21_1 + 1]]

	arg_21_2.name = var_21_0.id

	LoadImageSpriteAsync("educatesite/" .. var_21_0.icon, arg_21_0:findTF("icon", arg_21_2), true)
	LoadImageSpriteAsync("educatesite/" .. var_21_0.name_pic, arg_21_0:findTF("name", arg_21_2), true)

	local var_21_1 = getProxy(EducateProxy):GetOptionsBySiteId(var_21_0.id)
	local var_21_2 = underscore.any(var_21_1, function(arg_22_0)
		return arg_22_0:IsShowLimit()
	end)

	setActive(arg_21_0:findTF("limit", arg_21_2), var_21_2)
	setActive(arg_21_0:findTF("new", arg_21_2), EducateTipHelper.IsShowNewTip(EducateTipHelper.NEW_SITE, var_21_0.id))
	setAnchoredPosition(arg_21_2, {
		x = var_21_0.coordinate[1],
		y = var_21_0.coordinate[2]
	})
	onButton(arg_21_0, arg_21_2, function()
		arg_21_0.detailPanel:Show(var_21_0.id)
	end, SFX_PANEL)
end

function var_0_0.clearNewTip(arg_24_0, arg_24_1)
	eachChild(arg_24_0.mapContent, function(arg_25_0)
		if tonumber(arg_25_0.name) == arg_24_1 then
			setActive(arg_24_0:findTF("new", arg_25_0), false)
		end
	end)
end

function var_0_0.updateRes(arg_26_0)
	arg_26_0.resPanel:Flush()
end

function var_0_0.updateAttrs(arg_27_0)
	arg_27_0.archivePanel:Flush()
end

function var_0_0.updateTime(arg_28_0)
	arg_28_0.siteUIList:align(#arg_28_0.siteIdList)
	arg_28_0.datePanel:Flush()
end

function var_0_0.updateTarget(arg_29_0)
	arg_29_0.targetPanel:Flush()
end

function var_0_0.updateTimeWeekDay(arg_30_0, arg_30_1)
	arg_30_0.datePanel:UpdateWeekDay(arg_30_1)
end

function var_0_0.MoveTargetPanelLeft(arg_31_0)
	arg_31_0.targetPanel:SetPosLeft()
end

function var_0_0.MoveTargetPanelRight(arg_32_0)
	arg_32_0.targetPanel:SetPosRight()
end

function var_0_0.ShowSpecEvent(arg_33_0, arg_33_1, arg_33_2, arg_33_3, arg_33_4)
	arg_33_0.detailPanel:showSpecEvent(arg_33_1, arg_33_2, arg_33_3, arg_33_4)
end

function var_0_0.ShowSitePerform(arg_34_0, arg_34_1, arg_34_2, arg_34_3, arg_34_4, arg_34_5)
	arg_34_0.detailPanel:showSitePerform(arg_34_1, arg_34_2, arg_34_3, arg_34_4, arg_34_5)
end

function var_0_0.onBackPressed(arg_35_0)
	if arg_35_0.detailPanel:isShowing() then
		arg_35_0.detailPanel:onClose()
	else
		arg_35_0:emit(var_0_0.ON_BACK_PRESSED)
	end
end

function var_0_0.willExit(arg_36_0)
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_36_0.topTF, arg_36_0:findTF("ui"))
	arg_36_0.datePanel:Destroy()

	arg_36_0.datePanel = nil

	arg_36_0.resPanel:Destroy()

	arg_36_0.resPanel = nil

	arg_36_0.topPanel:Destroy()

	arg_36_0.topPanel = nil

	arg_36_0.targetPanel:Destroy()

	arg_36_0.targetPanel = nil

	arg_36_0.archivePanel:Destroy()

	arg_36_0.archivePanel = nil

	arg_36_0.detailPanel:Destroy()

	arg_36_0.detailPanel = nil
end

return var_0_0
