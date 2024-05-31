﻿local var_0_0 = class("CommissionInfoEventItem", import(".CommissionInfoItem"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.lockTF = arg_1_0._tf:Find("lock")

	setActive(arg_1_0.lockTF, false)
	setText(arg_1_0.lockTF:Find("Text"), i18n("commission_label_unlock_event_tip"))
end

function var_0_0.CanOpen(arg_2_0)
	return getProxy(PlayerProxy):getData().level >= 12
end

function var_0_0.Init(arg_3_0)
	local var_3_0 = arg_3_0:CanOpen()

	setActive(arg_3_0.lockTF, not var_3_0)
	setGray(arg_3_0.toggle, not var_3_0, true)
	setActive(arg_3_0.foldFlag, var_3_0)
	setActive(arg_3_0.goBtn, var_3_0)

	arg_3_0.ptBonus = EventPtBonus.New(arg_3_0.toggle:Find("bonusPt"))

	var_0_0.super.Init(arg_3_0)
end

function var_0_0.GetList(arg_4_0)
	assert(arg_4_0.list, "why ???")
	table.sort(arg_4_0.list, function(arg_5_0, arg_5_1)
		return arg_5_0.state > arg_5_1.state
	end)

	return arg_4_0.list, 4
end

function var_0_0.OnFlush(arg_6_0)
	local var_6_0, var_6_1, var_6_2, var_6_3 = getProxy(EventProxy):GetEventListForCommossionInfo()

	arg_6_0.finishedCounter.text = var_6_1
	arg_6_0.ongoingCounter.text = var_6_2
	arg_6_0.leisureCounter.text = var_6_3

	setActive(arg_6_0.finishedCounterContainer, var_6_1 > 0)
	setActive(arg_6_0.ongoingCounterContainer, var_6_2 > 0)
	setActive(arg_6_0.leisureCounterContainer, var_6_3 > 0)
	setActive(arg_6_0.goBtn, var_6_1 == 0)
	setActive(arg_6_0.finishedBtn, var_6_1 > 0)

	arg_6_0.list = var_6_0
end

function var_0_0.UpdateList(arg_7_0)
	var_0_0.super.UpdateList(arg_7_0)
	arg_7_0:UpdateActList()
end

function var_0_0.UpdateActList(arg_8_0)
	local var_8_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_COLLECTION_EVENT)

	if var_8_0 and not var_8_0:isEnd() then
		local var_8_1 = getProxy(EventProxy):GetEventByActivityId(var_8_0.id)

		if var_8_1 then
			local var_8_2 = cloneTplTo(arg_8_0.uilist.item, arg_8_0.uilist.container)

			var_8_2:SetAsFirstSibling()
			arg_8_0:UpdateEventInfo(var_8_2, var_8_1)
			setActive(var_8_2:Find("unlock"), true)
			setActive(var_8_2:Find("lock"), false)
			arg_8_0:UpdateStyle(var_8_2, true)
		end
	end
end

function var_0_0.GetChapterByCount(arg_9_0, arg_9_1)
	local var_9_0 = pg.chapter_template

	for iter_9_0, iter_9_1 in pairs(var_9_0.all) do
		if var_9_0[iter_9_1].collection_team == arg_9_1 then
			return var_9_0[iter_9_1]
		end
	end
end

function var_0_0.UpdateListItem(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	local var_10_0 = arg_10_1 > getProxy(EventProxy).maxFleetNums

	if var_10_0 then
		local var_10_1 = arg_10_0:GetChapterByCount(arg_10_1)

		assert(var_10_1, arg_10_1)

		if getProxy(SettingsProxy):IsMellowStyle() then
			setText(arg_10_3:Find("lock/Text"), i18n("commission_open_tip", var_10_1.chapter_name))
		else
			setText(arg_10_3:Find("lock/Text"), i18n("commission_no_open") .. "\n" .. i18n("commission_open_tip", var_10_1.chapter_name))
		end
	else
		arg_10_0:UpdateEventInfo(arg_10_3, arg_10_2)
	end

	setActive(arg_10_3:Find("unlock"), not var_10_0)
	setActive(arg_10_3:Find("lock"), var_10_0)
	arg_10_0:UpdateStyle(arg_10_3, false, arg_10_2)
end

function var_0_0.UpdateEventInfo(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = arg_11_2 and arg_11_2.state or EventInfo.StateNone

	if var_11_0 == EventInfo.StateNone then
		setText(arg_11_1:Find("unlock/name_bg/Text"), i18n("commission_idle"))
		onButton(arg_11_0, arg_11_1:Find("unlock/leisure/go_btn"), function()
			arg_11_0:OnSkip()
		end, SFX_PANEL)
		onButton(arg_11_0, arg_11_1, function()
			triggerButton(arg_11_1:Find("unlock/leisure/go_btn"))
		end, SFX_PANEL)
	elseif var_11_0 == EventInfo.StateFinish then
		setText(arg_11_1:Find("unlock/name_bg/Text"), arg_11_2.template.title)
		onButton(arg_11_0, arg_11_1:Find("unlock/finished/finish_btn"), function()
			arg_11_0:emit(CommissionInfoMediator.FINISH_EVENT, arg_11_2)
		end, SFX_PANEL)
		onButton(arg_11_0, arg_11_1, function()
			triggerButton(arg_11_1:Find("unlock/finished/finish_btn"))
		end, SFX_PANEL)
	elseif var_11_0 == EventInfo.StateActive then
		setText(arg_11_1:Find("unlock/name_bg/Text"), arg_11_2.template.title)

		local var_11_1 = arg_11_1:Find("unlock/ongoging/time"):GetComponent(typeof(Text))

		arg_11_0:AddTimer(arg_11_2, var_11_1)
	end

	setActive(arg_11_1:Find("unlock/leisure"), var_11_0 == EventInfo.StateNone)
	setActive(arg_11_1:Find("unlock/ongoging"), var_11_0 == EventInfo.StateActive)
	setActive(arg_11_1:Find("unlock/finished"), var_11_0 == EventInfo.StateFinish)
end

function var_0_0.AddTimer(arg_16_0, arg_16_1, arg_16_2)
	arg_16_0:RemoveTimer(arg_16_1)

	local var_16_0 = arg_16_1.finishTime + 2

	arg_16_0.timers[arg_16_1.id] = Timer.New(function()
		local var_17_0 = var_16_0 - pg.TimeMgr.GetInstance():GetServerTime()

		if var_17_0 <= 0 then
			arg_16_0.timers[arg_16_1.id]:Stop()

			arg_16_0.timers[arg_16_1.id] = nil

			arg_16_0:OnFlush()
			arg_16_0:UpdateList()
		else
			arg_16_2.text = pg.TimeMgr.GetInstance():DescCDTime(var_17_0)
		end
	end, 1, -1)

	arg_16_0.timers[arg_16_1.id]:Start()
	arg_16_0.timers[arg_16_1.id].func()
end

function var_0_0.RemoveTimer(arg_18_0, arg_18_1)
	if arg_18_0.timers[arg_18_1.id] then
		arg_18_0.timers[arg_18_1.id]:Stop()

		arg_18_0.timers[arg_18_1.id] = nil
	end
end

function var_0_0.UpdateStyle(arg_19_0, arg_19_1, arg_19_2, arg_19_3)
	local var_19_0 = arg_19_3 and arg_19_3.state or EventInfo.StateNone
	local var_19_1 = "icon_1"
	local var_19_2 = "icon_4"
	local var_19_3 = "icon_3"

	if arg_19_2 then
		var_19_1, var_19_2, var_19_3 = "icon_5", "icon_6", "icon_6"
	end

	local function var_19_4(arg_20_0, arg_20_1)
		local var_20_0 = arg_19_1:Find(string.format("unlock/%s/icon", arg_20_0))
		local var_20_1 = GetSpriteFromAtlas("ui/commissioninfoui_atlas", arg_20_1)

		var_20_0.localScale = arg_19_2 and Vector3.one or Vector3(1.2, 1.2, 1.2)
		var_20_0:GetComponent(typeof(Image)).sprite = var_20_1

		var_20_0:GetComponent(typeof(Image)):SetNativeSize()
	end

	var_19_4("leisure", var_19_1)
	var_19_4("ongoging", var_19_2)
	var_19_4("finished", var_19_3)

	local var_19_5 = "event_ongoing"

	if arg_19_2 then
		var_19_5 = "event_bg_act"
	end

	if getProxy(SettingsProxy):IsMellowStyle() then
		var_19_5 = "frame_unlock"
		arg_19_1:Find("unlock/ongoging"):GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/CommissionInfoUI4Mellow_atlas", var_19_5)
		arg_19_1:Find("unlock/finished"):GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/CommissionInfoUI4Mellow_atlas", var_19_5)
	else
		arg_19_1:Find("unlock/ongoging"):GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/commissioninfoui_atlas", var_19_5)
		arg_19_1:Find("unlock/finished"):GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/commissioninfoui_atlas", var_19_5)
	end

	local var_19_6 = Color.New(0.996078431372549, 0.7568627450980392, 0.9725490196078431, 1)
	local var_19_7 = arg_19_2 and var_19_6 or Color.New(0.6039215686274509, 0.7843137254901961, 0.9607843137254902, 1)

	arg_19_1:Find("unlock/ongoging/print"):GetComponent(typeof(Image)).color = var_19_7
	arg_19_1:Find("unlock/finished/print"):GetComponent(typeof(Image)).color = var_19_7

	setActive(arg_19_1:Find("unlock/act"), var_19_0 == EventInfo.StateNone and arg_19_2)
end

function var_0_0.OnSkip(arg_21_0)
	arg_21_0:emit(CommissionInfoMediator.ON_ACTIVE_EVENT)
end

function var_0_0.OnFinishAll(arg_22_0)
	local var_22_0 = {}
	local var_22_1 = 0

	_.each(arg_22_0.list, function(arg_23_0)
		if arg_23_0.state == EventInfo.StateFinish then
			table.insert(var_22_0, function(arg_24_0)
				arg_22_0:emit(CommissionInfoMediator.FINISH_EVENT, arg_23_0, var_22_1, arg_24_0)
			end)
		end
	end)

	local var_22_2 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_COLLECTION_EVENT)

	if var_22_2 and not var_22_2:isEnd() then
		local var_22_3 = getProxy(EventProxy):GetEventByActivityId(var_22_2.id)

		if var_22_3 and var_22_3.state == EventInfo.StateFinish then
			table.insert(var_22_0, function(arg_25_0)
				arg_22_0:emit(CommissionInfoMediator.FINISH_EVENT, var_22_3, var_22_1, arg_25_0)
			end)
		end
	end

	var_22_1 = #var_22_0

	seriesAsync(var_22_0)
end

return var_0_0
