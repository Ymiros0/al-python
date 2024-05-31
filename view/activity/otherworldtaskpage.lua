﻿local var_0_0 = class("OtherWorldTaskPage")
local var_0_1 = 3
local var_0_2 = 1
local var_0_3 = "other_world_task_type_daily"
local var_0_4 = "other_world_task_type_main"
local var_0_5 = "other_world_task_type_repeat"
local var_0_6 = "other_world_task_get_all"
local var_0_7 = "other_world_task_go"
local var_0_8 = "other_world_task_got"
local var_0_9 = "other_world_task_get"
local var_0_10 = "other_world_task_tag_main"
local var_0_11 = "other_world_task_tag_daily"
local var_0_12 = "other_world_task_tag_all"

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4)
	arg_1_0.taskPage = arg_1_1
	arg_1_0.contextData = arg_1_2
	arg_1_0.taskItemTpl = findTF(arg_1_3, "taskItemTpl")
	arg_1_0.iconTpl = findTF(arg_1_3, "IconTpl")
	arg_1_0._event = arg_1_4

	setText(findTF(arg_1_0.taskItemTpl, "btnGo/text"), i18n(var_0_7))
	setText(findTF(arg_1_0.taskItemTpl, "btnGot/text"), i18n(var_0_8))
	setText(findTF(arg_1_0.taskItemTpl, "btnGet/text"), i18n(var_0_9))
	setText(findTF(arg_1_0.taskPage, "leftBtns/btnAll/text"), i18n(var_0_12))
	setText(findTF(arg_1_0.taskPage, "leftBtns/btnMain/text"), i18n(var_0_10))
	setText(findTF(arg_1_0.taskPage, "leftBtns/btnDaily/text"), i18n(var_0_11))
	setText(findTF(arg_1_0.taskPage, "leftBtns/btnAll/text_selected"), i18n(var_0_12))
	setText(findTF(arg_1_0.taskPage, "leftBtns/btnMain/text_selected"), i18n(var_0_10))
	setText(findTF(arg_1_0.taskPage, "leftBtns/btnDaily/text_selected"), i18n(var_0_11))
	setText(findTF(arg_1_0.taskPage, "btnGetAll/text"), i18n(var_0_6))
	setActive(arg_1_0.taskItemTpl, false)
	setActive(arg_1_0.iconTpl, false)

	arg_1_0.enterTaskId = nil
	arg_1_0.enterTaskIds = nil

	if arg_1_0.contextData.task_id then
		arg_1_0.enterTaskId = arg_1_0.contextData.task_id or nil
	elseif arg_1_0.contextData.task_ids then
		arg_1_0.enterTaskIds = arg_1_0.contextData.task_ids or nil
	end

	arg_1_0.activityId = ActivityConst.OTHER_WORLD_TASK_ID
	arg_1_0.hideTask = {}

	if pg.activity_template[arg_1_0.activityId] then
		arg_1_0.hideTask = pg.activity_template[arg_1_0.activityId].config_client.hide_task or {}
	end

	arg_1_0.btnGetAll = findTF(arg_1_0.taskPage, "btnGetAll")
	arg_1_0.taskTagPanel = findTF(arg_1_0.taskPage, "taskTagPanel")
	arg_1_0.taskListPanel = findTF(arg_1_0.taskPage, "taskListPanel")
	arg_1_0.scrollRect = findTF(arg_1_0.taskPage, "taskListPanel/Content"):GetComponent("LScrollRect")

	function arg_1_0.scrollRect.onUpdateItem(arg_2_0, arg_2_1)
		arg_1_0:onUpdateTaskItem(arg_2_0, arg_2_1)
	end

	arg_1_0.btnAll = findTF(arg_1_0.taskPage, "leftBtns/btnAll")
	arg_1_0.btnDaily = findTF(arg_1_0.taskPage, "leftBtns/btnDaily")
	arg_1_0.btnMain = findTF(arg_1_0.taskPage, "leftBtns/btnMain")

	onButton(arg_1_0._event, arg_1_0.btnAll, function()
		arg_1_0:clearTagBtn()
		setActive(findTF(arg_1_0.btnAll, "bg_selected"), true)
		setActive(findTF(arg_1_0.btnAll, "text_selected"), true)
		setActive(findTF(arg_1_0.btnAll, "text"), false)
		setImageColor(findTF(arg_1_0.btnAll, "bg"), Color.New(1, 0.9882352941176471, 0.9098039215686274, 1))
		arg_1_0:showTaskByType()
	end, SFX_CONFIRM)
	onButton(arg_1_0._event, arg_1_0.btnDaily, function()
		arg_1_0:clearTagBtn()
		setActive(findTF(arg_1_0.btnDaily, "bg_selected"), true)
		setActive(findTF(arg_1_0.btnDaily, "text_selected"), true)
		setActive(findTF(arg_1_0.btnDaily, "text"), false)
		setImageColor(findTF(arg_1_0.btnDaily, "bg"), Color.New(1, 0.9882352941176471, 0.9098039215686274, 1))
		arg_1_0:showTaskByType(var_0_1)
	end, SFX_CONFIRM)
	onButton(arg_1_0._event, arg_1_0.btnMain, function()
		arg_1_0:clearTagBtn()
		setActive(findTF(arg_1_0.btnMain, "bg_selected"), true)
		setActive(findTF(arg_1_0.btnMain, "text_selected"), true)
		setActive(findTF(arg_1_0.btnMain, "text"), false)
		setImageColor(findTF(arg_1_0.btnMain, "bg"), Color.New(1, 0.9882352941176471, 0.9098039215686274, 1))
		arg_1_0:showTaskByType(var_0_2)
	end, SFX_CONFIRM)
	onButton(arg_1_0._event, arg_1_0.btnGetAll, function()
		local var_6_0 = arg_1_0.getAllTasks

		arg_1_0._event:emit(OtherWorldTaskMediator.SUBMIT_TASK_ALL, {
			activityId = arg_1_0.activityId,
			ids = var_6_0
		})
	end, SFX_CONFIRM)

	arg_1_0.iconTfs = {}
	arg_1_0.awards = {}

	arg_1_0:updateTask()
	triggerButton(arg_1_0.btnAll, true)
end

function var_0_0.showTaskByType(arg_7_0, arg_7_1)
	arg_7_0.tagType = arg_7_1
	arg_7_0.showTasks = {}

	if arg_7_1 then
		for iter_7_0, iter_7_1 in ipairs(arg_7_0.allDisplayTask) do
			if iter_7_1:getConfig("priority_type") == arg_7_1 then
				table.insert(arg_7_0.showTasks, iter_7_1)
			end
		end
	else
		arg_7_0.showTasks = arg_7_0.allDisplayTask
	end

	if arg_7_0.enterTaskId and arg_7_0.enterTaskId > 0 then
		for iter_7_2 = 1, #arg_7_0.showTasks do
			if arg_7_0.showTasks[iter_7_2].id == arg_7_0.enterTaskId then
				arg_7_0.scrollIndex = iter_7_2
			end
		end
	end

	arg_7_0.scrollRect:SetTotalCount(#arg_7_0.showTasks, 0)

	if arg_7_0.scrollIndex ~= nil then
		local var_7_0 = arg_7_0.scrollRect:HeadIndexToValue(arg_7_0.scrollIndex - 1)

		arg_7_0.scrollRect:ScrollTo(var_7_0)
	end
end

function var_0_0.clearTagBtn(arg_8_0)
	setActive(findTF(arg_8_0.btnAll, "bg_selected"), false)
	setActive(findTF(arg_8_0.btnDaily, "bg_selected"), false)
	setActive(findTF(arg_8_0.btnMain, "bg_selected"), false)
	setActive(findTF(arg_8_0.btnMain, "text_selected"), false)
	setActive(findTF(arg_8_0.btnDaily, "text_selected"), false)
	setActive(findTF(arg_8_0.btnAll, "text_selected"), false)
	setActive(findTF(arg_8_0.btnMain, "text"), true)
	setActive(findTF(arg_8_0.btnDaily, "text"), true)
	setActive(findTF(arg_8_0.btnAll, "text"), true)
	setImageColor(findTF(arg_8_0.btnMain, "bg"), Color.New(0.7372549019607844, 0.6352941176470588, 0.5882352941176471, 1))
	setImageColor(findTF(arg_8_0.btnDaily, "bg"), Color.New(0.7372549019607844, 0.6352941176470588, 0.5882352941176471, 1))
	setImageColor(findTF(arg_8_0.btnAll, "bg"), Color.New(0.7372549019607844, 0.6352941176470588, 0.5882352941176471, 1))
end

function var_0_0.onUpdateTaskItem(arg_9_0, arg_9_1, arg_9_2)
	if arg_9_0.exitFlag then
		return
	end

	arg_9_1 = arg_9_1 + 1

	local var_9_0 = arg_9_0.showTasks[arg_9_1]
	local var_9_1 = var_9_0.id
	local var_9_2 = var_9_0:getProgress()
	local var_9_3 = var_9_0:getConfig("desc")
	local var_9_4 = var_9_0:getConfig("ryza_icon")
	local var_9_5 = var_9_0:isOver()
	local var_9_6 = var_9_0:isFinish()
	local var_9_7 = var_9_0:getTarget()
	local var_9_8 = var_9_0:isCircle()
	local var_9_9 = var_9_0:isDaily()
	local var_9_10 = var_9_0:isSubmit()
	local var_9_11 = var_9_0:getConfig("sub_type")
	local var_9_12 = var_9_0:getConfig("type")
	local var_9_13 = var_9_0:getConfig("priority_type")

	setScrollText(findTF(arg_9_2, "desc/text"), var_9_3)

	if PLATFORM_CODE ~= PLATFORM_CH then
		-- block empty
	end

	if not var_9_5 then
		setText(findTF(arg_9_2, "progressDesc/text"), setColorStr(var_9_2, "#51382E") .. " / " .. setColorStr(var_9_7, "#51382E"))
	else
		setText(findTF(arg_9_2, "progressDesc/text"), "--/--")
	end

	setSlider(findTF(arg_9_2, "progressBar"), 0, 1, var_9_5 and 1 or var_9_2 / var_9_7)

	local var_9_14 = pg.task_data_template[var_9_1].award_display
	local var_9_15 = findTF(arg_9_2, "awardDisplay/viewport/content")
	local var_9_16 = var_9_15.childCount

	if var_9_16 < #var_9_14 then
		local var_9_17 = #var_9_14 - var_9_16

		for iter_9_0 = 1, var_9_17 do
			local var_9_18 = tf(Instantiate(arg_9_0.iconTpl))

			setParent(var_9_18, var_9_15)
			setActive(var_9_18, true)
		end
	end

	for iter_9_1 = 1, var_9_15.childCount do
		local var_9_19 = var_9_15:GetChild(iter_9_1 - 1)

		if iter_9_1 <= #var_9_14 then
			local var_9_20 = var_9_14[iter_9_1]
			local var_9_21 = {
				type = var_9_20[1],
				id = var_9_20[2],
				count = var_9_20[3]
			}

			updateDrop(var_9_19, var_9_21)
			onButton(arg_9_0._event, var_9_19, function()
				arg_9_0._event:emit(BaseUI.ON_DROP, var_9_21)
			end, SFX_PANEL)
			setActive(var_9_19, true)
		else
			setActive(var_9_19, false)
		end
	end

	setActive(findTF(arg_9_2, "btnGo"), not var_9_5 and not var_9_6 and var_9_11 ~= 1006)
	setActive(findTF(arg_9_2, "btnGet"), not var_9_5 and var_9_6 and not var_9_10)
	setActive(findTF(arg_9_2, "btnGot"), var_9_6)
	setSlider(findTF(arg_9_2, "progressBar"), 0, 1, var_9_2 / var_9_7)

	local var_9_22

	if var_9_13 == var_0_1 then
		if var_9_12 == 16 and var_9_11 == 20 then
			var_9_22 = var_0_5
		else
			var_9_22 = var_0_3
		end
	else
		var_9_22 = var_0_4
	end

	setText(findTF(arg_9_2, "tag/text"), i18n(var_9_22))
	onButton(arg_9_0._event, findTF(arg_9_2, "btnGo"), function()
		arg_9_0._event:emit(OtherWorldTaskMediator.TASK_GO, {
			taskVO = var_9_0
		})
	end, SFX_CONFIRM)
	onButton(arg_9_0._event, findTF(arg_9_2, "btnGet"), function()
		local var_12_0 = var_9_0:getConfig("priority_type")
		local var_12_1 = var_9_0:getConfig("sub_type")

		arg_9_0._event:emit(OtherWorldTaskMediator.SUBMIT_TASK, {
			activityId = arg_9_0.activityId,
			id = var_9_0.id
		})
	end, SFX_CONFIRM)

	if arg_9_1 == 1 then
		arg_9_0.scrollIndex = nil
	end

	if arg_9_0.enterTaskId ~= nil and arg_9_0.enterTaskId > 0 then
		if var_9_1 == arg_9_0.enterTaskId then
			arg_9_0.enterTaskId = nil
			arg_9_0.scrollIndex = nil
		end
	elseif arg_9_0.enterTaskIds and #arg_9_0.enterTaskIds > 0 then
		for iter_9_2, iter_9_3 in ipairs(arg_9_0.enterTaskIds) do
			if var_9_1 == iter_9_3 then
				arg_9_0.enterTaskIds = nil
				arg_9_0.scrollIndex = nil
			end
		end
	end
end

function var_0_0.updateTask(arg_13_0, arg_13_1)
	arg_13_0.displayTask = {}
	arg_13_0.allDisplayTask = {}

	local var_13_0 = getProxy(ActivityTaskProxy):getTaskById(arg_13_0.activityId)

	arg_13_0.getAllTasks = {}

	for iter_13_0 = 1, #var_13_0 do
		local var_13_1 = var_13_0[iter_13_0]
		local var_13_2 = var_13_1.id

		if not table.contains(arg_13_0.hideTask, var_13_2) then
			local var_13_3 = var_13_1:getProgress()
			local var_13_4 = var_13_1:getTarget()
			local var_13_5 = var_13_1:getConfig("priority_type")

			if not arg_13_0.displayTask[var_13_5] then
				arg_13_0.displayTask[var_13_5] = {}
			end

			table.insert(arg_13_0.displayTask[var_13_5], var_13_1)
			table.insert(arg_13_0.allDisplayTask, var_13_1)

			if var_13_1:isFinish() and not var_13_1:isOver() then
				table.insert(arg_13_0.getAllTasks, var_13_2)
			end
		end
	end

	local var_13_6 = getProxy(ActivityProxy):getActivityById(arg_13_0.activityId)
	local var_13_7 = {}

	if var_13_6 then
		var_13_7 = var_13_6.data1_list
	end

	if var_13_7 and #var_13_7 > 0 then
		for iter_13_1 = 1, #var_13_7 do
			local var_13_8 = var_13_7[iter_13_1]
			local var_13_9 = ActivityTask.New(arg_13_0.activityId, {
				progress = 0,
				id = var_13_8
			})

			var_13_9:setOver()

			local var_13_10 = var_13_9:getConfig("ryza_type")

			if var_13_10 > 0 then
				if not arg_13_0.displayTask[var_13_10] then
					arg_13_0.displayTask[var_13_10] = {}
				end

				table.insert(arg_13_0.displayTask[var_13_10], var_13_9)
				table.insert(arg_13_0.allDisplayTask, var_13_9)
			end
		end
	end

	local function var_13_11(arg_14_0, arg_14_1)
		if arg_14_0:isOver() and not arg_14_1:isOver() then
			return false
		elseif not arg_14_0:isOver() and arg_14_1:isOver() then
			return true
		end

		if arg_14_0:isFinish() and not arg_14_1:isFinish() then
			return true
		elseif not arg_14_0:isFinish() and arg_14_1:isFinish() then
			return false
		end

		local var_14_0 = arg_14_0:getConfig("priority_type")
		local var_14_1 = arg_14_1:getConfig("priority_type")

		if var_14_0 == var_0_2 and var_14_1 == var_0_1 then
			return true
		elseif var_14_0 == var_0_1 and var_14_1 == var_0_2 then
			return false
		end

		if arg_14_0:isNew() and not arg_14_1:isNew() then
			return true
		elseif not arg_14_0:isNew() and arg_14_1:isNew() then
			return false
		end

		if arg_14_0.id > arg_14_1.id then
			return false
		elseif arg_14_0.id < arg_14_1.id then
			return true
		end
	end

	for iter_13_2, iter_13_3 in pairs(arg_13_0.displayTask) do
		table.sort(iter_13_3, var_13_11)
	end

	table.sort(arg_13_0.allDisplayTask, var_13_11)

	if arg_13_1 then
		arg_13_0:showTaskByType(arg_13_0.tagType)
	end

	if #arg_13_0.getAllTasks > 0 then
		setActive(arg_13_0.btnGetAll, true)
	else
		setActive(arg_13_0.btnGetAll, false)
	end
end

function var_0_0.setActive(arg_15_0, arg_15_1)
	setActive(arg_15_0.taskPage, arg_15_1)
end

function var_0_0.dispose(arg_16_0)
	arg_16_0.exitFlag = true

	for iter_16_0 = 1, #arg_16_0.allDisplayTask do
		local var_16_0 = arg_16_0.allDisplayTask[iter_16_0]

		if var_16_0:isNew() then
			var_16_0:changeNew()
		end
	end
end

return var_0_0
