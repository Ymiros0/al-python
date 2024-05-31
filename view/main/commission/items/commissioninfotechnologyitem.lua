﻿local var_0_0 = class("CommissionInfoTechnologyItem", import(".CommissionInfoItem"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.commingTF = arg_1_0._tf:Find("comming")
	arg_1_0.techFrame = arg_1_0._tf:Find("frame")
	arg_1_0.lockTF = arg_1_0._tf:Find("lock")

	setActive(arg_1_0.lockTF, false)
	setText(arg_1_0.lockTF:Find("Text"), i18n("commission_label_unlock_tech_tip"))
end

function var_0_0.CanOpen(arg_2_0)
	return getProxy(PlayerProxy):getData().level >= 30 and not LOCK_TECHNOLOGY
end

function var_0_0.Init(arg_3_0)
	if LOCK_TECHNOLOGY then
		setActive(arg_3_0._tf:Find("frame"), false)
		setActive(arg_3_0.lockTF, false)
		setActive(arg_3_0.commingTF, true)
	else
		setActive(arg_3_0._tf:Find("frame"), true)
		setActive(arg_3_0.lockTF, false)
		setActive(arg_3_0.commingTF, false)

		local var_3_0 = arg_3_0:CanOpen()

		setActive(arg_3_0.lockTF, not var_3_0)
		setGray(arg_3_0.toggle, not var_3_0, true)
		setActive(arg_3_0.foldFlag, false)
		setActive(arg_3_0.goBtn, var_3_0)
		var_0_0.super.Init(arg_3_0)
	end
end

function var_0_0.OnFlush(arg_4_0)
	local var_4_0 = getProxy(TechnologyProxy):getPlanningTechnologys()

	arg_4_0.list = {}

	local var_4_1 = {
		ongoing = 0,
		finished = 0,
		leisure = TechnologyConst.QUEUE_TOTAL_COUNT + 1
	}

	for iter_4_0, iter_4_1 in ipairs(var_4_0) do
		if iter_4_1:isCompleted() then
			var_4_1.leisure = var_4_1.leisure - 1
			var_4_1.finished = var_4_1.finished + 1
		elseif iter_4_1:isActivate() then
			var_4_1.leisure = var_4_1.leisure - 1
			var_4_1.ongoing = var_4_1.ongoing + 1
		end
	end

	eachChild(arg_4_0._tf:Find("frame/counter"), function(arg_5_0)
		setActive(arg_5_0, var_4_1[arg_5_0.name] > 0)
		setText(arg_5_0:Find("Text"), var_4_1[arg_5_0.name])
	end)
	setActive(arg_4_0.goBtn, var_4_1.finished == 0)
	setActive(arg_4_0.finishedBtn, var_4_1.finished > 0)
end

function var_0_0.UpdateListItem(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	local var_6_0 = arg_6_2
	local var_6_1 = pg.TimeMgr.GetInstance():GetServerTime()
	local var_6_2 = var_6_0:getConfig("time")
	local var_6_3 = var_6_0.time

	if var_6_3 == 0 then
		setText(arg_6_3:Find("unlock/desc/name_bg/Text"), i18n("commission_idle"))
		onButton(arg_6_0, arg_6_3:Find("unlock/leisure/go_btn"), function()
			arg_6_0:OnSkip()
		end, SFX_PANEL)
		onButton(arg_6_0, arg_6_3, function()
			arg_6_0:OnSkip()
		end, SFX_PANEL)
	elseif var_6_1 < var_6_3 - var_6_2 then
		arg_6_0:UpdateTechnology(arg_6_3, var_6_0)
		setText(arg_6_3:Find("unlock/ongoging/time"), pg.TimeMgr.GetInstance():DescCDTime(var_6_2))
	elseif var_6_1 < var_6_3 then
		arg_6_0:UpdateTechnology(arg_6_3, var_6_0)
		arg_6_0:AddTimer(var_6_0, arg_6_3)
	else
		arg_6_0:UpdateTechnology(arg_6_3, var_6_0)

		if var_6_0:finishCondition() then
			local var_6_4 = arg_6_3:Find("unlock/finished/finish_btn")

			onButton(arg_6_0, var_6_4, function()
				arg_6_0:emit(CommissionInfoMediator.ON_TECH_FINISHED, {
					id = var_6_0.id,
					pool_id = var_6_0.poolId
				})
			end, SFX_PANEL)
			onButton(arg_6_0, arg_6_3, function()
				triggerButton(var_6_4)
			end, SFX_PANEL)
		else
			setText(arg_6_3:Find("unlock/ongoging/time"), "00:00:00")
		end
	end

	setActive(arg_6_3:Find("unlock"), true)
	setActive(arg_6_3:Find("lock"), false)
	setActive(arg_6_3:Find("unlock/leisure"), not var_6_0:isActivate())
	setActive(arg_6_3:Find("unlock/ongoging"), var_6_0:isActivate() and not var_6_0:isCompleted())
	setActive(arg_6_3:Find("unlock/finished"), var_6_0:isCompleted())
	setActive(arg_6_3:Find("unlock/desc/task_bg"), var_6_0:isActivate() and var_6_0:getConfig("condition") > 0)
end

function var_0_0.AddTimer(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = arg_11_2:Find("unlock/ongoging/time"):GetComponent(typeof(Text))

	arg_11_0.timers[arg_11_1.id] = Timer.New(function()
		local var_12_0 = arg_11_1:getFinishTime() - pg.TimeMgr.GetInstance():GetServerTime()

		if var_12_0 > 0 then
			var_11_0.text = pg.TimeMgr.GetInstance():DescCDTime(var_12_0)
		else
			arg_11_0:RemoveTimer(arg_11_1)
			arg_11_0:OnFlush()
			arg_11_0:UpdateList()
		end
	end, 1, -1)

	arg_11_0.timers[arg_11_1.id]:Start()
	arg_11_0.timers[arg_11_1.id].func()
end

function var_0_0.RemoveTimer(arg_13_0, arg_13_1)
	if arg_13_0.timers[arg_13_1.id] then
		arg_13_0.timers[arg_13_1.id]:Stop()

		arg_13_0.timers[arg_13_1.id] = nil
	end
end

function var_0_0.UpdateTechnology(arg_14_0, arg_14_1, arg_14_2)
	setText(arg_14_1:Find("unlock/desc/name_bg/Text"), arg_14_2:getConfig("name"))

	local var_14_0 = arg_14_2:getConfig("condition")

	if var_14_0 > 0 then
		local var_14_1 = getProxy(TaskProxy):getTaskVO(var_14_0)
		local var_14_2 = var_14_1:getConfig("desc") .. "(" .. var_14_1:getProgress() .. "/" .. var_14_1:getConfig("target_num") .. ")"

		setText(arg_14_1:Find("unlock/desc/task_bg/Text"), shortenString(var_14_2, 10))
	end
end

function var_0_0.GetList(arg_15_0)
	local var_15_0 = getProxy(PlayerProxy):getRawData()
	local var_15_1 = pg.SystemOpenMgr.GetInstance():isOpenSystem(var_15_0.level, "TechnologyMediator")

	return arg_15_0.list, var_15_1 and TechnologyConst.QUEUE_TOTAL_COUNT + 1 or 0
end

function var_0_0.OnSkip(arg_16_0)
	arg_16_0:emit(CommissionInfoMediator.ON_ACTIVE_TECH)
end

function var_0_0.OnFinishAll(arg_17_0)
	local var_17_0 = getProxy(TechnologyProxy)

	if var_17_0.queue[1] and var_17_0.queue[1]:isCompleted() then
		arg_17_0:emit(CommissionInfoMediator.ON_TECH_QUEUE_FINISH)
	else
		local var_17_1 = var_17_0:getActivateTechnology()

		arg_17_0:emit(CommissionInfoMediator.ON_TECH_FINISHED, {
			id = var_17_1.id,
			pool_id = var_17_1.poolId
		})
	end
end

return var_0_0
