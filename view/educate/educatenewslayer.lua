﻿local var_0_0 = class("EducateNewsLayer", import(".base.EducateBaseUI"))
local var_0_1 = {
	[EducateSpecialEvent.TAG_ING] = "5ACEFE",
	[EducateSpecialEvent.TAG_COMING] = "CB99FF",
	[EducateSpecialEvent.TAG_END] = "7C7E81"
}
local var_0_2 = {
	[EducateSpecialEvent.TAG_ING] = "393A3C",
	[EducateSpecialEvent.TAG_COMING] = "393A3C",
	[EducateSpecialEvent.TAG_END] = "7C7E81"
}

function var_0_0.getUIName(arg_1_0)
	return "EducateNewsUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:initData()
	arg_2_0:findUI()
	arg_2_0:addListener()
end

function var_0_0.initData(arg_3_0)
	arg_3_0.curTime = getProxy(EducateProxy):GetCurTime()
	arg_3_0.finishEvents = getProxy(EducateProxy):GetEventProxy():GetFinishSpecEventIds()
	arg_3_0.importEvents = {}
	arg_3_0.otherEvents = {}

	local var_3_0 = getProxy(EducateProxy):GetPersonalityId()

	for iter_3_0, iter_3_1 in ipairs(pg.child_event_special.all) do
		local var_3_1 = EducateSpecialEvent.New(iter_3_1)

		if var_3_1:IsShow() and var_3_1:InMonth(arg_3_0.curTime.month) and var_3_1:IsUnlockSite() and var_3_1:IsMatch(var_3_0) then
			if var_3_1:IsImport() then
				table.insert(arg_3_0.importEvents, var_3_1)
			elseif var_3_1:IsOther() then
				table.insert(arg_3_0.otherEvents, var_3_1)
			end
		end
	end
end

function var_0_0.findUI(arg_4_0)
	arg_4_0.anim = arg_4_0:findTF("anim_root"):GetComponent(typeof(Animation))
	arg_4_0.animEvent = arg_4_0:findTF("anim_root"):GetComponent(typeof(DftAniEvent))

	arg_4_0.animEvent:SetEndEvent(function()
		arg_4_0:emit(var_0_0.ON_CLOSE)
	end)

	arg_4_0.windowTF = arg_4_0:findTF("anim_root/window")
	arg_4_0.tplTF = arg_4_0:findTF("tpl", arg_4_0.windowTF)

	setActive(arg_4_0.tplTF, false)

	arg_4_0.importTF = arg_4_0:findTF("scrollview/view/content/import_news", arg_4_0.windowTF)
	arg_4_0.importUIList = UIItemList.New(arg_4_0:findTF("list", arg_4_0.importTF), arg_4_0.tplTF)

	setText(arg_4_0:findTF("title/Text", arg_4_0.importTF), i18n("child_news_import_title"))
	setText(arg_4_0:findTF("empty/Text", arg_4_0.importTF), i18n("child_news_import_empty"))

	arg_4_0.otherTF = arg_4_0:findTF("scrollview/view/content/other_news", arg_4_0.windowTF)
	arg_4_0.otherUIList = UIItemList.New(arg_4_0:findTF("list", arg_4_0.otherTF), arg_4_0.tplTF)

	setText(arg_4_0:findTF("title/Text", arg_4_0.otherTF), i18n("child_news_other_title"))
	setText(arg_4_0:findTF("empty/Text", arg_4_0.otherTF), i18n("child_news_other_empty"))
end

function var_0_0.addListener(arg_6_0)
	onButton(arg_6_0, arg_6_0:findTF("anim_root/bg"), function()
		arg_6_0:_close()
	end, SFX_PANEL)
end

function var_0_0.didEnter(arg_8_0)
	pg.UIMgr.GetInstance():OverlayPanel(arg_8_0._tf, {
		groupName = arg_8_0:getGroupNameFromData(),
		weight = arg_8_0:getWeightFromData() + 1
	})
	arg_8_0:initNewsList()
	arg_8_0:updateNewsList()
end

function var_0_0.initNewsList(arg_9_0)
	arg_9_0.importUIList:make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventUpdate then
			arg_9_0:updateEventItem(arg_10_1, arg_10_2, true)
		end
	end)
	arg_9_0.otherUIList:make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate then
			arg_9_0:updateEventItem(arg_11_1, arg_11_2, false)
		end
	end)
end

function var_0_0.updateEventItem(arg_12_0, arg_12_1, arg_12_2, arg_12_3)
	local var_12_0 = arg_12_3 and arg_12_0.importEvents[arg_12_1 + 1] or arg_12_0.otherEvents[arg_12_1 + 1]
	local var_12_1 = var_12_0:GetTag(arg_12_0.finishEvents, arg_12_0.curTime.week)
	local var_12_2 = EducateSpecialEvent.TAG2NAME[var_12_1]

	setImageColor(arg_12_0:findTF("block", arg_12_2), Color.NewHex(var_0_1[var_12_1]))
	setText(arg_12_0:findTF("name", arg_12_2), var_12_0:getConfig("main_desc"))
	setTextColor(arg_12_0:findTF("name", arg_12_2), Color.NewHex(var_0_2[var_12_1]))
	eachChild(arg_12_0:findTF("name/tags", arg_12_2), function(arg_13_0)
		setActive(arg_13_0, arg_13_0.name == var_12_2)
	end)
	setText(arg_12_0:findTF("time/Text", arg_12_2), var_12_0:GetTimeDesc())
end

function var_0_0.updateNewsList(arg_14_0)
	local var_14_0 = CompareFuncs({
		function(arg_15_0)
			return arg_15_0:GetTag(arg_14_0.finishEvents, arg_14_0.curTime.week)
		end,
		function(arg_16_0)
			return arg_16_0.id
		end
	})

	table.sort(arg_14_0.importEvents, var_14_0)
	table.sort(arg_14_0.otherEvents, var_14_0)
	setActive(arg_14_0:findTF("empty", arg_14_0.importTF), #arg_14_0.importEvents <= 0)
	setActive(arg_14_0:findTF("empty", arg_14_0.otherTF), #arg_14_0.otherEvents <= 0)
	arg_14_0.importUIList:align(#arg_14_0.importEvents)
	arg_14_0.otherUIList:align(#arg_14_0.otherEvents)
end

function var_0_0._close(arg_17_0)
	arg_17_0.anim:Play("anim_educate_newsUI_out")
end

function var_0_0.onBackPressed(arg_18_0)
	arg_18_0:_close()
end

function var_0_0.willExit(arg_19_0)
	arg_19_0.animEvent:SetEndEvent(nil)
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_19_0._tf)
end

return var_0_0
