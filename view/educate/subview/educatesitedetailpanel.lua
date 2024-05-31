﻿local var_0_0 = class("EducateSiteDetailPanel", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "EducateSiteDetailUI"
end

function var_0_0.OnInit(arg_2_0)
	setActive(arg_2_0._tf, false)

	arg_2_0.anim = arg_2_0:findTF("anim_root"):GetComponent(typeof(Animation))
	arg_2_0.animEvent = arg_2_0:findTF("anim_root"):GetComponent(typeof(DftAniEvent))

	arg_2_0.animEvent:SetEndEvent(function()
		setActive(arg_2_0._tf, false)

		if arg_2_0.contextData.onExit then
			arg_2_0.contextData.onExit()
		end
	end)

	arg_2_0.windowTF = arg_2_0:findTF("anim_root/window")
	arg_2_0.closeBtn = arg_2_0:findTF("close_btn", arg_2_0.windowTF)
	arg_2_0.nameTF = arg_2_0:findTF("name_bg/name", arg_2_0.windowTF)
	arg_2_0.picTF = arg_2_0:findTF("pic", arg_2_0.windowTF)
	arg_2_0.descTF = arg_2_0:findTF("desc", arg_2_0.windowTF)
	arg_2_0.optionsTF = arg_2_0:findTF("options/content", arg_2_0.windowTF)
	arg_2_0.optionTpl = arg_2_0:findTF("option_tpl", arg_2_0.windowTF)

	setText(arg_2_0:findTF("limit/Text", arg_2_0.optionTpl), i18n("child_option_limit"))
	setText(arg_2_0:findTF("type_2/awards/polaroid/Text", arg_2_0.optionTpl), i18n("child_random_polaroid_drop"))
	setActive(arg_2_0.optionTpl, false)

	arg_2_0.optionUIList = UIItemList.New(arg_2_0.optionsTF, arg_2_0.optionTpl)
	arg_2_0.performTF = arg_2_0:findTF("anim_root/perform")
	arg_2_0.performName = arg_2_0:findTF("name", arg_2_0.performTF)

	arg_2_0:addListener()
	pg.UIMgr.GetInstance():OverlayPanel(arg_2_0._tf, {
		groupName = LayerWeightConst.GROUP_EDUCATE,
		weight = LayerWeightConst.BASE_LAYER - 2
	})
end

function var_0_0.addListener(arg_4_0)
	onButton(arg_4_0, arg_4_0:findTF("anim_root/bg"), function()
		arg_4_0:onClose()
	end, SFX_PANEL)
	onButton(arg_4_0, arg_4_0.closeBtn, function()
		arg_4_0:onClose()
	end, SFX_PANEL)
	arg_4_0.optionUIList:make(function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_0 == UIItemList.EventUpdate then
			arg_4_0:updateOptionItem(arg_7_1, arg_7_2)
		end
	end)

	arg_4_0.optionIds = {}
end

function var_0_0.checkSpecEvent(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = getProxy(EducateProxy):GetEventProxy():GetSiteSpecEvents(arg_8_1)

	if #var_8_0 > 0 then
		arg_8_0:emit(EducateMapMediator.ON_SPECIAL_EVENT_TRIGGER, {
			siteId = arg_8_1,
			id = var_8_0[1].id,
			callback = arg_8_2
		})
	else
		arg_8_2()
	end
end

function var_0_0.showSpecEvent(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4)
	local var_9_0 = pg.child_event_special[arg_9_2].performance
	local var_9_1 = EducateHelper.GetDialogueShowDrops(arg_9_3)
	local var_9_2 = EducateHelper.GetCommonShowDrops(arg_9_3)

	local function var_9_3()
		if #var_9_2 > 0 then
			arg_9_0:emit(EducateBaseUI.EDUCATE_ON_AWARD, {
				items = var_9_2,
				removeFunc = function()
					arg_9_0:checkSpecEvent(arg_9_1, arg_9_4)
				end
			})
		else
			arg_9_0:checkSpecEvent(arg_9_1, arg_9_4)
		end

		setActive(arg_9_0.performTF, false)
	end

	if #var_9_0 > 0 then
		setActive(arg_9_0.performTF, true)
		pg.PerformMgr.GetInstance():PlayGroup(var_9_0, var_9_3, var_9_1)
	elseif var_9_3 then
		var_9_3()
	end
end

function var_0_0.showSiteDetailById(arg_12_0, arg_12_1)
	if arg_12_0.siteId == arg_12_1 then
		return
	end

	arg_12_0.siteId = arg_12_1
	arg_12_0.config = pg.child_site[arg_12_0.siteId]

	arg_12_0:checkSpecEvent(arg_12_0.siteId, function()
		arg_12_0:showDetailPanel()
	end)
end

function var_0_0.addTaskProgress(arg_14_0)
	local var_14_0 = getProxy(EducateProxy):GetTaskProxy():GetSiteEnterAddTasks(arg_14_0.siteId)
	local var_14_1 = {}
	local var_14_2 = {}
	local var_14_3 = {}

	for iter_14_0, iter_14_1 in ipairs(var_14_0) do
		if iter_14_1:IsMind() then
			table.insert(var_14_1, {
				progress = 1,
				task_id = iter_14_1.id
			})
		end

		if iter_14_1:IsTarget() then
			table.insert(var_14_2, {
				progress = 1,
				task_id = iter_14_1.id
			})
		end

		if iter_14_1:IsMain() then
			table.insert(var_14_3, {
				progress = 1,
				task_id = iter_14_1.id
			})
		end
	end

	if #var_14_1 > 0 then
		arg_14_0:emit(EducateMapMediator.ON_ADD_TASK_PROGRESS, {
			system = EducateTask.SYSTEM_TYPE_MIND,
			progresses = var_14_1
		})
	end

	if #var_14_2 > 0 then
		arg_14_0:emit(EducateMapMediator.ON_ADD_TASK_PROGRESS, {
			system = EducateTask.SYSTEM_TYPE_TARGET,
			progresses = var_14_2
		})
	end

	if #var_14_3 > 0 then
		arg_14_0:emit(EducateMapMediator.ON_ADD_TASK_PROGRESS, {
			system = EducateTask.STSTEM_TYPE_MAIN,
			progresses = var_14_3
		})
	end
end

local function var_0_1(arg_15_0, arg_15_1, arg_15_2)
	if arg_15_1[2] == -1 then
		LoadImageSpriteAtlasAsync("ui/educatecommonui_atlas", "res_-1", findTF(arg_15_0, "Image"), true)
		setText(findTF(arg_15_0, "Text"), i18n("child_random_ops_drop"))
	else
		local var_15_0 = ""
		local var_15_1 = ""

		if arg_15_1[1] == EducateConst.DROP_TYPE_ATTR then
			var_15_0 = "attr_"
			var_15_1 = pg.child_attr[arg_15_1[2]].name
		elseif arg_15_1[1] == EducateConst.DROP_TYPE_RES then
			var_15_0 = "res_"
			var_15_1 = pg.child_resource[arg_15_1[2]].name
		end

		LoadImageSpriteAtlasAsync("ui/educatecommonui_atlas", var_15_0 .. arg_15_1[2], findTF(arg_15_0, "Image"), true)
		setText(findTF(arg_15_0, "Text"), var_15_1 .. "+" .. arg_15_1[3])
	end
end

local function var_0_2(arg_16_0, arg_16_1)
	local var_16_0 = ""

	if arg_16_1[1] == EducateConst.DROP_TYPE_ATTR then
		var_16_0 = "attr_"
	elseif arg_16_1[1] == EducateConst.DROP_TYPE_RES then
		var_16_0 = "res_"
	end

	LoadImageSpriteAtlasAsync("ui/educatecommonui_atlas", var_16_0 .. arg_16_1[2], findTF(arg_16_0, "Image"), true)
	setText(findTF(arg_16_0, "Text"), "-" .. arg_16_1[3])
end

function var_0_0.updateOptionItem(arg_17_0, arg_17_1, arg_17_2)
	GetOrAddComponent(arg_17_2, "CanvasGroup").alpha = 1
	arg_17_2.name = tostring(arg_17_1 + 1)

	local var_17_0 = arg_17_0.optionVOs[arg_17_1 + 1]

	setActive(arg_17_0:findTF("limit", arg_17_2), var_17_0:IsShowLimit())

	local var_17_1 = var_17_0:GetType()

	for iter_17_0 = 1, 3 do
		setActive(arg_17_0:findTF("type_" .. iter_17_0, arg_17_2), iter_17_0 == var_17_1)
	end

	local var_17_2 = arg_17_0:findTF("type_" .. var_17_1, arg_17_2)
	local var_17_3 = not var_17_0:IsCountLimit() and true or var_17_0:CanTrigger()

	setGray(arg_17_2, not var_17_3)
	switch(var_17_1, {
		[EducateSiteOption.TYPE_SHOP] = function()
			setText(arg_17_0:findTF("name/Text", var_17_2), var_17_0:getConfig("name"))
			onButton(arg_17_0, arg_17_2, function()
				arg_17_0:emit(EducateMapMediator.ON_OPEN_SHOP, var_17_0:GetLinkId())
			end, SFX_PANEL)
		end,
		[EducateSiteOption.TYPE_EVENT] = function()
			setText(arg_17_0:findTF("name", var_17_2), shortenString(var_17_0:getConfig("name") .. var_17_0:GetCntText(), 12))

			local var_20_0 = var_17_0:IsShowPolaroid()

			setActive(arg_17_0:findTF("awards/polaroid", var_17_2), var_20_0)

			local var_20_1 = var_20_0 and 2 or 3
			local var_20_2 = var_17_0:GetResults()
			local var_20_3 = UIItemList.New(arg_17_0:findTF("awards/normal", var_17_2), arg_17_0:findTF("awards/normal/tpl", var_17_2))

			var_20_3:make(function(arg_21_0, arg_21_1, arg_21_2)
				if arg_21_0 == UIItemList.EventUpdate then
					var_0_1(arg_21_2, var_20_2[arg_21_1 + 1])
				end
			end)

			local var_20_4 = var_20_1 < #var_20_2 and var_20_1 or #var_20_2

			var_20_3:align(var_20_4)

			local var_20_5 = var_17_0:GetCost()
			local var_20_6 = UIItemList.New(arg_17_0:findTF("costs", var_17_2), arg_17_0:findTF("costs/tpl", var_17_2))

			var_20_6:make(function(arg_22_0, arg_22_1, arg_22_2)
				if arg_22_0 == UIItemList.EventUpdate then
					var_0_2(arg_22_2, var_20_5[arg_22_1 + 1], "-")
				end
			end)
			var_20_6:align(#var_20_5)
			onButton(arg_17_0, arg_17_2, function()
				if not var_17_3 then
					return
				end

				arg_17_0:emit(EducateMapMediator.ON_MAP_SITE_OPERATE, {
					siteId = arg_17_0.siteId,
					optionVO = var_17_0
				})
			end, SFX_PANEL)
		end,
		[EducateSiteOption.TYPE_SITE] = function()
			setText(arg_17_0:findTF("name/Text", var_17_2), var_17_0:getConfig("name"))
			onButton(arg_17_0, arg_17_2, function()
				local var_25_0 = var_17_0:GetLinkId()

				assert(pg.child_site[var_25_0], "child_site不存在id:" .. var_25_0)
				table.insert(arg_17_0.siteQueue, var_25_0)
				arg_17_0:showSiteDetailById(var_25_0)
			end, SFX_PANEL)
		end
	})
end

function var_0_0.showDetailPanel(arg_26_0)
	arg_26_0:addTaskProgress()
	setActive(arg_26_0.windowTF, true)
	setText(arg_26_0.nameTF, arg_26_0.config.name)
	setText(arg_26_0.descTF, arg_26_0.config.desc)
	LoadImageSpriteAsync("educatesite/" .. arg_26_0.config.pic, arg_26_0.picTF, true)

	arg_26_0.optionVOs = getProxy(EducateProxy):GetOptionsBySiteId(arg_26_0.siteId)

	arg_26_0.optionUIList:align(#arg_26_0.optionVOs)
end

function var_0_0.showSitePerform(arg_27_0, arg_27_1, arg_27_2, arg_27_3, arg_27_4, arg_27_5)
	local var_27_0 = EducateHelper.GetDialogueShowDrops(arg_27_4)
	local var_27_1 = EducateHelper.GetDialogueShowDrops(arg_27_5)
	local var_27_2 = table.mergeArray(EducateHelper.GetCommonShowDrops(arg_27_4), EducateHelper.GetCommonShowDrops(arg_27_5))
	local var_27_3 = {}
	local var_27_4 = pg.child_site_option_branch[arg_27_2].performance
	local var_27_5 = pg.child_site_option[arg_27_1].name

	table.insert(var_27_3, function(arg_28_0)
		pg.PerformMgr.GetInstance():PlayGroupNoHide(var_27_4, arg_28_0, var_27_0, var_27_5)
	end)

	if arg_27_3 and #arg_27_3 > 0 then
		for iter_27_0, iter_27_1 in ipairs(arg_27_3) do
			local var_27_6 = pg.child_event[iter_27_1].performance

			table.insert(var_27_3, function(arg_29_0)
				pg.PerformMgr.GetInstance():PlayGroupNoHide(var_27_6, arg_29_0, var_27_1)
			end)
		end
	end

	setText(arg_27_0.performName, var_27_5)
	setActive(arg_27_0.performTF, true)
	pg.PerformMgr.GetInstance():Show()
	seriesAsync(var_27_3, function()
		setActive(arg_27_0.performTF, false)

		if #var_27_2 > 0 then
			arg_27_0:emit(EducateBaseUI.EDUCATE_ON_AWARD, {
				items = var_27_2
			})
		end

		pg.PerformMgr.GetInstance():Hide()
		arg_27_0:showDetailPanel()
	end)
end

function var_0_0.Hide(arg_31_0)
	arg_31_0.anim:Play("anim_educate_sitedatail_out")
end

function var_0_0.Show(arg_32_0, arg_32_1)
	if not arg_32_0:GetLoaded() then
		return
	end

	arg_32_0.siteId = arg_32_1
	arg_32_0.config = pg.child_site[arg_32_0.siteId]

	assert(arg_32_0.config, "child_site不存在id:" .. arg_32_0.siteId)
	setActive(arg_32_0._tf, true)
	setActive(arg_32_0.windowTF, false)

	arg_32_0.siteQueue = {
		arg_32_0.siteId
	}

	arg_32_0:checkSpecEvent(arg_32_0.siteId, function()
		arg_32_0:showDetailPanel()

		if arg_32_0.contextData.onEnter then
			arg_32_0.contextData.onEnter()
		end
	end)
	EducateTipHelper.ClearNewTip(EducateTipHelper.NEW_SITE, arg_32_0.siteId)
end

function var_0_0.onClose(arg_34_0)
	if #arg_34_0.siteQueue > 1 then
		table.remove(arg_34_0.siteQueue, #arg_34_0.siteQueue)
		arg_34_0:showSiteDetailById(arg_34_0.siteQueue[#arg_34_0.siteQueue])
	else
		arg_34_0:Hide()
	end
end

function var_0_0.OnDestroy(arg_35_0)
	arg_35_0.animEvent:SetEndEvent(nil)
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_35_0._tf)
end

return var_0_0
