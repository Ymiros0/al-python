﻿local var_0_0 = class("LinerLogSchedulePage", import("view.base.BaseSubView"))

var_0_0.SHOW_TIME_LIST = {
	{
		3,
		8
	},
	{
		8,
		12
	},
	{
		12,
		14
	},
	{
		14,
		18
	},
	{
		18,
		20
	},
	{
		20,
		25
	},
	{
		25,
		27
	}
}

function var_0_0.getUIName(arg_1_0)
	return "LinerLogSchedulePage"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.togglesTF = arg_2_0:findTF("toggles")
	arg_2_0.contentTF = arg_2_0:findTF("content")
	arg_2_0.anim = arg_2_0.contentTF:GetComponent(typeof(Animation))
	arg_2_0.awardTF = arg_2_0:findTF("award/mask/IconTpl")
	arg_2_0.awardDesc = arg_2_0:findTF("award/Text")
	arg_2_0.goBtn = arg_2_0:findTF("award/go")
	arg_2_0.getBtn = arg_2_0:findTF("award/get")
	arg_2_0.gotTF = arg_2_0:findTF("award/got")
end

function var_0_0.OnInit(arg_3_0)
	arg_3_0:UpdateActivity()
	onButton(arg_3_0, arg_3_0.getBtn, function()
		arg_3_0:emit(LinerLogBookMediator.GET_SCHEDULE_AWARD, arg_3_0.activity.id, arg_3_0.curIdx, arg_3_0.groups[arg_3_0.curIdx]:GetDrop())
	end, SFX_CONFIRM)
	onButton(arg_3_0, arg_3_0.goBtn, function()
		arg_3_0:emit(LinerLogBookMediator.ON_CLOSE)
	end, SFX_CONFIRM)

	arg_3_0.groupIds = arg_3_0.activity:getConfig("config_data")[1]
	arg_3_0.groups = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0.groupIds) do
		arg_3_0.groups[iter_3_0] = LinerTimeGroup.New(iter_3_1)
	end

	arg_3_0.itemUIList = UIItemList.New(arg_3_0.contentTF, arg_3_0:findTF("tpl", arg_3_0.contentTF))

	arg_3_0.itemUIList:make(function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_0 == UIItemList.EventUpdate then
			arg_3_0:UpdateItem(arg_6_1, arg_6_2)
		end
	end)

	arg_3_0.toggleUIList = UIItemList.New(arg_3_0.togglesTF, arg_3_0:findTF("tpl", arg_3_0.togglesTF))

	arg_3_0.toggleUIList:make(function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_0 == UIItemList.EventInit then
			local var_7_0 = arg_7_1 + 1

			arg_7_2.name = var_7_0

			local var_7_1 = "DAY " .. string.format("%02d", var_7_0)

			setText(arg_7_2:Find("Text"), var_7_1)
			setText(arg_7_2:Find("selected/Text"), var_7_1)
			onToggle(arg_3_0, arg_7_2, function(arg_8_0)
				if arg_8_0 then
					if arg_3_0.curIdx and arg_3_0.curIdx == var_7_0 then
						return
					end

					arg_3_0.curIdx = var_7_0

					arg_3_0:FlushPage(true)
				end
			end, SFX_CONFIRM)
		elseif arg_7_0 == UIItemList.EventUpdate then
			local var_7_2 = tonumber(arg_7_2.name) > arg_3_0.curDay

			setActive(arg_7_2:Find("lock"), var_7_2)
			SetCompomentEnabled(arg_7_2, typeof(Toggle), not var_7_2)

			if var_7_2 then
				setActive(arg_7_2:Find("selected"), false)
				setActive(arg_7_2:Find("tip"), false)
			else
				setActive(arg_7_2:Find("tip"), var_0_0.IsTipWithGroupId(arg_3_0.activity, arg_3_0.groups[arg_7_1 + 1].id))
			end
		end
	end)
	arg_3_0.toggleUIList:align(#arg_3_0.groupIds)
	triggerToggle(arg_3_0:findTF(tostring(arg_3_0.curDay), arg_3_0.toggleUIList.container), true)
end

function var_0_0.UpdateActivity(arg_9_0, arg_9_1)
	arg_9_0.activity = arg_9_1 or getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_LINER)

	assert(arg_9_0.activity and not arg_9_0.activity:isEnd(), "not exist liner act, type: " .. ActivityConst.ACTIVITY_TYPE_LINER)

	arg_9_0.finishTimeIds = arg_9_0.activity:GetFinishTimeIds()
	arg_9_0.timeId2ExploredIds = arg_9_0.activity:GetTimeId2ExploredIds()
	arg_9_0.curDay = arg_9_0.activity:GetDayByIdx(arg_9_0.activity:GetCurIdx())
end

function var_0_0._getLogDesc(arg_10_0, arg_10_1)
	local var_10_0 = arg_10_1[1]
	local var_10_1 = arg_10_1[2] - 1

	if var_10_0 >= 24 then
		var_10_0 = var_10_0 - 24
	end

	if var_10_1 >= 24 then
		var_10_1 = var_10_1 - 24
	end

	local var_10_2 = var_10_0 < 12 and "AM" or "PM"
	local var_10_3 = var_10_1 < 12 and "AM" or "PM"
	local var_10_4

	var_10_4, var_10_1 = var_10_0 > 12 and var_10_0 - 12 or var_10_0, var_10_1 > 12 and var_10_1 - 12 or var_10_1

	return string.format("%d:00 %s~%d:59 %s", var_10_4, var_10_2, var_10_1, var_10_3)
end

function var_0_0._getReallyTime(arg_11_0, arg_11_1)
	for iter_11_0, iter_11_1 in ipairs(arg_11_0.times) do
		local var_11_0 = iter_11_1:GetTime()[1]
		local var_11_1 = iter_11_1:GetTime()[2]

		if var_11_0 < 3 then
			var_11_0 = var_11_0 + 24
		end

		if var_11_1 <= 3 then
			var_11_1 = var_11_1 + 24
		end

		if var_11_0 <= arg_11_1[1] and var_11_1 >= arg_11_1[2] then
			return iter_11_1
		end
	end
end

function var_0_0.UpdateItem(arg_12_0, arg_12_1, arg_12_2)
	local var_12_0 = arg_12_1 + 1
	local var_12_1 = var_0_0.SHOW_TIME_LIST[var_12_0]

	setText(arg_12_0:findTF("time/Text", arg_12_2), arg_12_0:_getLogDesc(var_12_1))

	local var_12_2 = arg_12_0:_getReallyTime(var_12_1)
	local var_12_3 = table.contains(arg_12_0.finishTimeIds, var_12_2.id)
	local var_12_4 = arg_12_0:findTF("desc", arg_12_2)
	local var_12_5 = var_12_3 and var_12_2:GetAfterDesc(var_12_0) or var_12_2:GetBeforDesc(var_12_0)

	if var_12_3 and var_12_2:GetType() == LinerTime.TYPE.EXPLORE then
		local var_12_6 = underscore.map(arg_12_0.timeId2ExploredIds[var_12_2.id], function(arg_13_0)
			return pg.activity_liner_room[arg_13_0].name
		end)

		var_12_5 = string.gsub(var_12_5, "$1", table.concat(var_12_6, "、"))
	end

	setText(var_12_4, var_12_5)
	setActive(arg_12_0:findTF("time/finish", arg_12_2), var_12_3)
	setActive(var_12_4, arg_12_0.curIdx <= arg_12_0.curDay)
end

function var_0_0.FlushPage(arg_14_0)
	arg_14_0.anim:Play()
	arg_14_0.toggleUIList:align(#arg_14_0.groupIds)

	arg_14_0.times = arg_14_0.groups[arg_14_0.curIdx]:GetTimeList()

	table.sort(arg_14_0.times, CompareFuncs({
		function(arg_15_0)
			return arg_15_0.id
		end
	}))
	arg_14_0.itemUIList:align(#var_0_0.SHOW_TIME_LIST)

	local var_14_0 = arg_14_0.groups[arg_14_0.curIdx]:GetDrop()

	updateDrop(arg_14_0.awardTF, var_14_0)
	onButton(arg_14_0, arg_14_0.awardTF, function()
		arg_14_0:emit(BaseUI.ON_DROP, var_14_0)
	end, SFX_PANEL)

	local var_14_1 = arg_14_0.activity:IsGotTimeAward(arg_14_0.curIdx)
	local var_14_2 = arg_14_0.groups[arg_14_0.curIdx].id
	local var_14_3 = var_0_0.IsTipWithGroupId(arg_14_0.activity, var_14_2)

	setActive(arg_14_0.goBtn, not var_14_1 and not var_14_3)
	setActive(arg_14_0.gotTF, var_14_1)
	setActive(arg_14_0:findTF("mask", arg_14_0.awardTF), var_14_1)

	local var_14_4 = var_14_1 and i18n("liner_schedule_award_tip2", arg_14_0.curIdx) or i18n("liner_schedule_award_tip1")

	setText(arg_14_0.awardDesc, var_14_4)
	setActive(arg_14_0.getBtn, var_14_3)
	arg_14_0:Show()
end

function var_0_0.OnDestroy(arg_17_0)
	return
end

function var_0_0.IsTipWithGroupId(arg_18_0, arg_18_1)
	local var_18_0 = table.indexof(arg_18_0:GetTimeGroupIds(), arg_18_1)

	if arg_18_0:IsGotTimeAward(var_18_0) then
		return false
	end

	local var_18_1 = arg_18_0:GetFinishTimeIds()

	return underscore.all(pg.activity_liner_time_group[arg_18_1].ids, function(arg_19_0)
		return table.contains(var_18_1, arg_19_0)
	end)
end

function var_0_0.IsTip()
	local var_20_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_LINER)

	assert(var_20_0 and not var_20_0:isEnd(), "not exist liner act, type: " .. ActivityConst.ACTIVITY_TYPE_LINER)

	local var_20_1 = var_20_0:GetTimeGroupIds()

	return underscore.any(var_20_1, function(arg_21_0)
		return var_0_0.IsTipWithGroupId(var_20_0, arg_21_0)
	end)
end

return var_0_0
