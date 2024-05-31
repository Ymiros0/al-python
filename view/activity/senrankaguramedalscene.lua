local var_0_0 = class("SenrankaguraMedalScene", import("..base.BaseUI"))
local var_0_1
local var_0_2
local var_0_3 = 4
local var_0_4 = "shan_luan_task_help"
local var_0_5 = "shan_luan_task_help"

function var_0_0.getUIName(arg_1_0)
	return "SenrankaguraMedalUI"
end

function var_0_0.GetTaskCountAble()
	local var_2_0 = ActivityConst.SENRANKAGURA_TASK_ID

	if not getProxy(ActivityProxy):getActivityById(var_2_0) then
		return false
	end

	local var_2_1 = pg.activity_template[var_2_0].config_client.player_task
	local var_2_2 = {}
	local var_2_3 = 0

	for iter_2_0, iter_2_1 in ipairs(var_2_1) do
		for iter_2_2, iter_2_3 in ipairs(iter_2_1) do
			table.insert(var_2_2, iter_2_3)
		end
	end

	local var_2_4

	local function var_2_5(arg_3_0)
		if not arg_3_0 then
			return true
		end

		local var_3_0 = getProxy(TaskProxy):getTaskById(arg_3_0)
		local var_3_1 = getProxy(TaskProxy):getFinishTaskById(arg_3_0)

		if not var_3_0 and not var_3_1 then
			return false
		end

		local var_3_2 = pg.task_data_template[arg_3_0].activity_client_config.before

		if var_3_0 and var_3_0:getTaskStatus() <= 0 then
			return false
		end

		return var_2_5(var_3_2)
	end

	for iter_2_4 = 1, #var_2_2 do
		local var_2_6 = var_2_2[iter_2_4]
		local var_2_7 = getProxy(TaskProxy):getTaskById(var_2_6)

		if var_2_7 then
			local var_2_8 = pg.task_data_template[var_2_6].activity_client_config.before

			if var_2_7:getTaskStatus() == 1 then
				local var_2_9 = pg.task_data_template[var_2_6].activity_client_config.before

				if not var_2_9 then
					var_2_3 = var_2_3 + 1
				elseif var_2_5(var_2_9) then
					var_2_3 = var_2_3 + 1
				end
			end
		end
	end

	return var_2_3 > 0, var_2_3
end

function var_0_0.init(arg_4_0)
	arg_4_0.activityId = ActivityConst.SENRANKAGURA_TASK_ID
	arg_4_0.taskActivity = getProxy(ActivityProxy):getActivityById(arg_4_0.activityId)
	arg_4_0.taskIds = pg.activity_template[arg_4_0.activityId].config_client.player_task
	arg_4_0.taskCount = 0
	arg_4_0.allTasksIds = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.taskIds) do
		arg_4_0.taskCount = arg_4_0.taskCount + #iter_4_1

		for iter_4_2, iter_4_3 in ipairs(iter_4_1) do
			table.insert(arg_4_0.allTasksIds, iter_4_3)
		end
	end

	arg_4_0.openTaskFlag = arg_4_0.contextData.task
	arg_4_0.buffs = pg.activity_template[arg_4_0.activityId].config_client.buff
	arg_4_0.ptId = pg.activity_template[arg_4_0.activityId].config_client.pt_id
	arg_4_0.ptName = pg.player_resource[arg_4_0.ptId].name
	arg_4_0.ptMaxNum = #arg_4_0.allTasksIds
	var_0_1 = #arg_4_0.taskIds
	var_0_2 = #arg_4_0.buffs
	arg_4_0.taskListDatas = {}

	for iter_4_4 = 1, #arg_4_0.taskIds do
		local var_4_0 = arg_4_0.taskIds[iter_4_4]
		local var_4_1 = {}

		for iter_4_5, iter_4_6 in ipairs(var_4_0) do
			arg_4_0:initTaskListIds(iter_4_6, var_4_1)
		end

		arg_4_0:sortListDatas(var_4_1)
		table.insert(arg_4_0.taskListDatas, var_4_1)
	end

	local var_4_2 = findTF(arg_4_0._tf, "ad")

	arg_4_0.btnDetail = findTF(var_4_2, "btnDetail")
	arg_4_0.btnBack = findTF(var_4_2, "frame/btnBack")
	arg_4_0.btnHelp = findTF(var_4_2, "frame/btnHelp")
	arg_4_0.btnHome = findTF(var_4_2, "frame/btnHome")
	arg_4_0.hxTf = findTF(var_4_2, "hx")

	setActive(arg_4_0.hxTf, PLATFORM_CODE == PLATFORM_CH)
	onButton(arg_4_0, arg_4_0.btnDetail, function()
		if arg_4_0:getMedalGetAble() then
			pg.m02:sendNotification(GAME.ACTIVITY_OPERATION, {
				cmd = 1,
				activity_id = ActivityConst.SENRANKAGURA_MEDAL_ID
			})
		elseif arg_4_0.taskActivity then
			arg_4_0:openDetailPane()
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("challenge_end_tip"))
		end
	end, SOUND_BACK)
	onButton(arg_4_0, arg_4_0.btnBack, function()
		arg_4_0:closeView()
	end, SOUND_BACK)
	onButton(arg_4_0, arg_4_0.btnHome, function()
		arg_4_0:emit(BaseUI.ON_HOME)
	end, SFX_CONFIRM)
	onButton(arg_4_0, arg_4_0.btnHelp, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[var_0_4].tip
		})
	end, SFX_CONFIRM)

	arg_4_0.btnPlayers = {}

	for iter_4_7 = 1, var_0_1 do
		local var_4_3 = iter_4_7
		local var_4_4 = findTF(var_4_2, "player/" .. iter_4_7)

		GetComponent(findTF(var_4_4, "img"), typeof(Image)).alphaHitTestMinimumThreshold = 0.5

		if arg_4_0.taskActivity then
			onButton(arg_4_0, var_4_4, function()
				arg_4_0:openTaskPanel(iter_4_7)
			end, SFX_CONFIRM)
		end

		setActive(findTF(var_4_4, "redTip"), false)
		table.insert(arg_4_0.btnPlayers, var_4_4)
	end

	local var_4_5 = findTF(arg_4_0._tf, "pop")

	arg_4_0.detailPanel = findTF(var_4_5, "detailPanel")

	setActive(arg_4_0.detailPanel, false)
	arg_4_0:initDetailPanel()

	arg_4_0.taskPanel = findTF(var_4_5, "taskPanel")

	setActive(arg_4_0.taskPanel, false)
	arg_4_0:initTaskPanel()

	arg_4_0.submitPanel = findTF(var_4_5, "submitPanel")

	setActive(arg_4_0.submitPanel, false)
	arg_4_0:initSubmitPanel()
end

function var_0_0.didEnter(arg_10_0)
	arg_10_0:updateUI()

	if arg_10_0.taskActivity and arg_10_0.openTaskFlag then
		arg_10_0.openTaskFlag = false

		arg_10_0:openTaskPanel()
	end
end

function var_0_0.updateUI(arg_11_0)
	local var_11_0 = arg_11_0:getMedalGetAble()

	setActive(findTF(arg_11_0.btnDetail, "detail"), not var_11_0 and arg_11_0.taskActivity)
	setActive(findTF(arg_11_0.btnDetail, "get"), var_11_0)

	local var_11_1 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_MEDAL_ID)
	local var_11_2 = var_11_1.data2_list
	local var_11_3 = var_11_1:GetPicturePuzzleIds()

	for iter_11_0 = 1, #arg_11_0.btnPlayers do
		local var_11_4 = var_11_3[iter_11_0]
		local var_11_5 = arg_11_0.btnPlayers[iter_11_0]

		setActive(findTF(var_11_5, "medal/icon"), table.contains(var_11_2, var_11_4))
		setActive(findTF(var_11_5, "img/got"), table.contains(var_11_2, var_11_4))
	end

	local var_11_6 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_MEDAL_ID)
	local var_11_7 = var_11_6.data1_list
	local var_11_8 = var_11_6.data2_list
	local var_11_9 = false

	for iter_11_1 = 1, #var_11_7 do
		if not var_11_9 and not table.contains(var_11_8, var_11_7[iter_11_1]) then
			var_11_9 = true

			pg.m02:sendNotification(GAME.MEMORYBOOK_UNLOCK, {
				id = var_11_7[iter_11_1],
				actId = var_11_6.id
			})
		end
	end

	if arg_11_0.taskActivity then
		local var_11_10 = arg_11_0:getGetAbleTask()
		local var_11_11 = {}

		for iter_11_2 = 1, #arg_11_0.taskIds do
			local var_11_12 = iter_11_2

			for iter_11_3, iter_11_4 in ipairs(arg_11_0.taskIds[iter_11_2]) do
				if table.contains(var_11_10, iter_11_4) then
					if not var_11_11[var_11_12] then
						var_11_11[var_11_12] = 1
					else
						var_11_11[var_11_12] = var_11_11[var_11_12] + 1
					end
				end
			end
		end

		for iter_11_5 = 1, #arg_11_0.btnPlayers do
			setActive(findTF(arg_11_0.btnPlayers[iter_11_5], "redTip"), var_11_11[iter_11_5] ~= nil)
		end

		arg_11_0:updateDetailPanel()
		arg_11_0:updateTask()
	end
end

function var_0_0.getMedalGetAble(arg_12_0)
	local var_12_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_MEDAL_ID)
	local var_12_1 = var_12_0.data1_list
	local var_12_2 = var_12_0.data2_list
	local var_12_3 = var_12_0:GetPicturePuzzleIds()

	if #var_12_2 == #var_12_3 and var_12_0.data1 ~= 1 then
		return true
	end

	return false
end

function var_0_0.openDetailPane(arg_13_0)
	setActive(arg_13_0.detailPanel, true)
end

function var_0_0.initDetailPanel(arg_14_0)
	arg_14_0.detailSlider = findTF(arg_14_0.detailPanel, "ad/progressSlider")
	arg_14_0.detailClose = findTF(arg_14_0.detailPanel, "ad/btnClose")

	onButton(arg_14_0, findTF(arg_14_0.detailPanel, "ad/black"), function()
		setActive(arg_14_0.detailPanel, false)
	end, SOUND_BACK)
	onButton(arg_14_0, arg_14_0.detailClose, function()
		setActive(arg_14_0.detailPanel, false)
	end)

	arg_14_0.detailProgressTipContent = findTF(arg_14_0.detailPanel, "ad/progressDetail")
	arg_14_0.detailProgressTipTpl = findTF(arg_14_0.detailPanel, "ad/progressDetail/tipTpl")

	setActive(arg_14_0.detailProgressTipTpl, false)

	local var_14_0 = findTF(arg_14_0.detailPanel, "ad/progressDetail").sizeDelta.x

	arg_14_0.medalTfs = {}

	for iter_14_0 = 1, var_0_1 do
		table.insert(arg_14_0.medalTfs, findTF(arg_14_0.detailPanel, "ad/medals/" .. iter_14_0))
	end

	for iter_14_1 = 1, var_0_2 do
		local var_14_1 = arg_14_0.buffs[iter_14_1].pt[1]
		local var_14_2 = tf(instantiate(arg_14_0.detailProgressTipTpl))

		setImageSprite(findTF(var_14_2, "num"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "buff_" .. iter_14_1), true)
		setImageSprite(findTF(var_14_2, "count"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "buff_count_" .. iter_14_1), true)

		var_14_2.anchoredPosition = Vector3(var_14_1 / arg_14_0.ptMaxNum * var_14_0, 0, 0)

		SetParent(var_14_2, arg_14_0.detailProgressTipContent)
		SetActive(var_14_2, true)
	end

	arg_14_0.detailBuffTfs = {}

	for iter_14_2 = 1, var_0_3 do
		local var_14_3 = findTF(arg_14_0.detailPanel, "ad/buff/" .. iter_14_2)

		table.insert(arg_14_0.detailBuffTfs, var_14_3)
	end

	arg_14_0.detailProgressDesc = findTF(arg_14_0.detailPanel, "ad/progressDesc")
	arg_14_0.detailLevelDesc = findTF(arg_14_0.detailPanel, "ad/levelDesc")
end

function var_0_0.updateDetailPanel(arg_17_0)
	local var_17_0 = arg_17_0:getPtNum()
	local var_17_1 = arg_17_0:getBuildLv(var_17_0)
	local var_17_2

	if var_17_1 ~= 0 then
		var_17_2 = arg_17_0.buffs[var_17_1].benefit
	end

	for iter_17_0 = 1, var_0_3 do
		local var_17_3

		if var_17_2 then
			local var_17_4 = var_17_2[iter_17_0]

			var_17_3 = pg.benefit_buff_template[var_17_4].desc
		else
			var_17_3 = i18n("shan_luan_task_buff_default")
		end

		local var_17_5 = arg_17_0.detailBuffTfs[iter_17_0]

		setText(findTF(var_17_5, "desc"), var_17_3)
	end

	setSlider(arg_17_0.detailSlider, 0, arg_17_0.ptMaxNum, var_17_0)

	local var_17_6 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_MEDAL_ID)
	local var_17_7 = var_17_6.data1_list
	local var_17_8 = var_17_6.data2_list
	local var_17_9 = var_17_6:GetPicturePuzzleIds()

	for iter_17_1 = 1, #arg_17_0.medalTfs do
		local var_17_10 = arg_17_0.medalTfs[iter_17_1]
		local var_17_11 = var_17_9[iter_17_1]

		setActive(findTF(var_17_10, "icon"), table.contains(var_17_8, var_17_11))
	end

	setText(findTF(arg_17_0.detailProgressDesc, "desc"), i18n("shan_luan_task_progress_tip", arg_17_0:getTaskCompleteCount() .. "/" .. arg_17_0.taskCount))
	setText(findTF(arg_17_0.detailLevelDesc, "desc"), i18n("shan_luan_task_level_tip", "Lv." .. var_17_1))
end

function var_0_0.getTaskCompleteCount(arg_18_0)
	local var_18_0 = 0
	local var_18_1 = arg_18_0:getActiveTask()

	for iter_18_0, iter_18_1 in ipairs(var_18_1) do
		if arg_18_0:getTask(iter_18_1):getTaskStatus() == 2 then
			var_18_0 = var_18_0 + 1
		else
			print()
		end
	end

	return var_18_0
end

function var_0_0.getPtNum(arg_19_0)
	local var_19_0 = 0

	if arg_19_0.ptId then
		var_19_0 = getProxy(PlayerProxy):getData()[arg_19_0.ptName] or 0
	else
		var_19_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2):GetBuildingLevelSum()
	end

	if var_19_0 > arg_19_0.ptMaxNum then
		var_19_0 = arg_19_0.ptMaxNum
	end

	return var_19_0
end

function var_0_0.getBuildLv(arg_20_0, arg_20_1)
	local var_20_0 = 0

	for iter_20_0 = #arg_20_0.buffs, 1, -1 do
		var_20_0 = arg_20_1 >= arg_20_0.buffs[iter_20_0].pt[1] and var_20_0 < iter_20_0 and iter_20_0 or var_20_0
	end

	return var_20_0
end

function var_0_0.initTaskListIds(arg_21_0, arg_21_1, arg_21_2)
	local var_21_0
	local var_21_1 = pg.task_data_template[arg_21_1].activity_client_config.before
	local var_21_2 = pg.task_data_template[arg_21_1].activity_client_config.special or false
	local var_21_3 = {
		id = arg_21_1,
		before = var_21_1,
		special = var_21_2
	}

	for iter_21_0, iter_21_1 in ipairs(arg_21_2) do
		for iter_21_2, iter_21_3 in ipairs(iter_21_1) do
			if iter_21_3.id == var_21_1 then
				table.insert(iter_21_1, var_21_3)

				return
			elseif iter_21_3.before == arg_21_1 then
				table.insert(iter_21_1, var_21_3)

				return
			end
		end
	end

	table.insert(arg_21_2, {
		var_21_3
	})
end

function var_0_0.initTaskPanel(arg_22_0)
	local var_22_0 = findTF(arg_22_0.taskPanel, "ad/frame/btnBack")
	local var_22_1 = findTF(arg_22_0.taskPanel, "ad/frame/btnHelp")
	local var_22_2 = findTF(arg_22_0.taskPanel, "ad/frame/btnHome")

	onButton(arg_22_0, var_22_0, function()
		setActive(arg_22_0.taskPanel, false)
	end, SOUND_BACK)
	onButton(arg_22_0, var_22_2, function()
		arg_22_0:emit(BaseUI.ON_HOME)
	end, SFX_CONFIRM)
	onButton(arg_22_0, var_22_1, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[var_0_5].tip
		})
	end, SFX_CONFIRM)

	arg_22_0.taskTagTfs = {}

	local var_22_3 = findTF(arg_22_0.taskPanel, "ad/tag/content")
	local var_22_4 = findTF(arg_22_0.taskPanel, "ad/tag/content/tagTpl")

	setActive(var_22_4, false)

	for iter_22_0 = 1, var_0_1 do
		local var_22_5 = iter_22_0
		local var_22_6 = tf(instantiate(var_22_4))

		setImageSprite(findTF(var_22_6, "icon"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "player_icon_" .. iter_22_0), true)
		SetParent(var_22_6, var_22_3)
		setActive(var_22_6, true)
		table.insert(arg_22_0.taskTagTfs, var_22_6)
		onButton(arg_22_0, var_22_6, function()
			arg_22_0:taskSelectTag(var_22_5, true)
		end, SFX_CONFIRM)
	end

	arg_22_0.taskButtonTpl = findTF(arg_22_0.taskPanel, "ad/taskButtonTpl")
	arg_22_0.taskList = {}

	local var_22_7 = findTF(arg_22_0.taskPanel, "ad/task/content")

	arg_22_0.taskDragTf = findTF(arg_22_0.taskPanel, "ad/task/drag")

	local var_22_8 = findTF(arg_22_0.taskPanel, "ad/taskTpl")
	local var_22_9 = findTF(arg_22_0.taskPanel, "ad/taskButtonTpl")

	setActive(var_22_8, false)
	setActive(var_22_9, false)

	arg_22_0.taskGroups = {}

	for iter_22_1 = 1, var_0_1 do
		local var_22_10 = {}
		local var_22_11 = arg_22_0.taskListDatas[iter_22_1]

		for iter_22_2 = 1, #var_22_11 do
			local var_22_12 = tf(instantiate(var_22_8))

			setParent(var_22_12, var_22_7)
			setActive(var_22_12, true)

			local var_22_13 = var_22_11[iter_22_2]
			local var_22_14 = {}

			for iter_22_3, iter_22_4 in ipairs(var_22_13) do
				local var_22_15 = tf(instantiate(var_22_9))

				var_22_15.anchoredPosition = Vector2(iter_22_4.pos[1] * 325 + iter_22_4.pos[2] * 90, iter_22_4.pos[2] * 190)

				local var_22_16 = iter_22_4.special

				if var_22_16 then
					if iter_22_4.pos[2] ~= 0 then
						setImageSprite(findTF(var_22_15, "get"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "task_get_" .. 4), true)
						setImageSprite(findTF(var_22_15, "got"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "task_got_" .. 4), true)
					else
						setImageSprite(findTF(var_22_15, "get"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "task_get_" .. 2), true)
						setImageSprite(findTF(var_22_15, "got"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "task_got_" .. 2), true)
					end
				elseif not var_22_16 and iter_22_4.pos[2] ~= 0 then
					setImageSprite(findTF(var_22_15, "get"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "task_get_" .. 3), true)
					setImageSprite(findTF(var_22_15, "got"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "task_got_" .. 3), true)
				end

				setActive(var_22_15, true)
				SetParent(var_22_15, var_22_12)
				table.insert(var_22_14, {
					tf = var_22_15,
					data = iter_22_4
				})
				onButton(arg_22_0, var_22_15, function()
					arg_22_0:openSubmitPanel(iter_22_4)
				end, SFX_CONFIRM)
			end

			var_22_10.listTf = var_22_12
			var_22_10.taskDic = var_22_14
		end

		table.insert(arg_22_0.taskGroups, var_22_10)
	end

	arg_22_0.taskButtonTpl = findTF(arg_22_0.taskPanel, "ad/buttonTpl")
	arg_22_0.taskBtnGetAll = findTF(arg_22_0.taskPanel, "ad/btnGetAll")

	onButton(arg_22_0, arg_22_0.taskBtnGetAll, function()
		local var_28_0 = arg_22_0:getGetAbleTask()

		if var_28_0 and #var_28_0 > 0 then
			arg_22_0:emit(SenrankaguraMedalMediator.SUBMIT_TASK_ALL, var_28_0)
		end
	end, SFX_CONFIRM)
end

function var_0_0.updateTask(arg_29_0)
	for iter_29_0 = 1, #arg_29_0.taskGroups do
		local var_29_0 = arg_29_0.taskGroups[iter_29_0].taskDic

		for iter_29_1, iter_29_2 in ipairs(var_29_0) do
			local var_29_1 = iter_29_2.tf
			local var_29_2 = arg_29_0:getTask(iter_29_2.data.id)

			setActive(findTF(var_29_1, "lock"), false)
			setActive(findTF(var_29_1, "getAble"), false)
			setActive(findTF(var_29_1, "get"), false)
			setActive(findTF(var_29_1, "got"), false)

			if var_29_2 then
				if arg_29_0:checkTaskBeforeComplete(var_29_2:getConfig("activity_client_config").before) then
					if var_29_2:getTaskStatus() == 0 then
						setActive(findTF(var_29_1, "get"), true)
					elseif var_29_2:getTaskStatus() == 1 then
						setActive(findTF(var_29_1, "get"), true)
						setActive(findTF(var_29_1, "getAble"), true)
					elseif var_29_2:getTaskStatus() == 2 then
						setActive(findTF(var_29_1, "got"), true)
					end
				else
					setActive(findTF(var_29_1, "lock"), true)
					setActive(findTF(var_29_1, "get"), true)
				end
			else
				setActive(findTF(var_29_1, "lock"), true)
				setActive(findTF(var_29_1, "get"), true)
			end
		end
	end

	if #arg_29_0:getGetAbleTask() > 0 then
		setActive(arg_29_0.taskBtnGetAll, true)
	else
		setActive(arg_29_0.taskBtnGetAll, false)
	end

	for iter_29_3 = 1, #arg_29_0.taskGroups do
		local var_29_3 = arg_29_0.taskGroups[iter_29_3].taskDic
		local var_29_4 = arg_29_0.taskGroups[iter_29_3].listTf

		for iter_29_4, iter_29_5 in ipairs(var_29_3) do
			local var_29_5 = iter_29_5.data.pos
			local var_29_6 = iter_29_5.data.before
			local var_29_7 = iter_29_5.tf

			setActive(findTF(var_29_7, "line/back"), false)
			setActive(findTF(var_29_7, "line/bottom"), false)
			setActive(findTF(var_29_7, "line/top"), false)
			var_29_7:SetAsFirstSibling()

			if not var_29_6 then
				setActive(findTF(var_29_7, "line"), false)
			else
				local var_29_8 = arg_29_0:getTaskPos(var_29_6)
				local var_29_9 = arg_29_0:getTask(var_29_6)
				local var_29_10 = arg_29_0:checkTaskBeforeComplete(var_29_6) and Color.New(0.9921568627450981, 0.9647058823529412, 0.8666666666666667) or Color.New(0.48627450980392156, 0.35294117647058826, 0.2901960784313726)

				if var_29_8[1] < var_29_5[1] then
					setActive(findTF(var_29_7, "line/back"), true)
					setImageColor(findTF(var_29_7, "line/back"), var_29_10)
				elseif var_29_8[2] < var_29_5[2] then
					setActive(findTF(var_29_7, "line/bottom"), true)
					setImageColor(findTF(var_29_7, "line/bottom"), var_29_10)
				else
					setActive(findTF(var_29_7, "line/top"), true)
					setImageColor(findTF(var_29_7, "line/top"), var_29_10)
				end

				setActive(findTF(var_29_7, "line"), true)
			end
		end
	end
end

function var_0_0.checkTaskBeforeComplete(arg_30_0, arg_30_1)
	if not arg_30_1 then
		return true
	end

	local var_30_0 = arg_30_0:getTaskGroupData(arg_30_1).before
	local var_30_1 = arg_30_0:getTask(arg_30_1)

	if not var_30_1 then
		return true
	end

	if var_30_1:getTaskStatus() == 0 then
		return false
	end

	if var_30_1:getTaskStatus() >= 1 then
		return arg_30_0:checkTaskBeforeComplete(var_30_0)
	end

	return true
end

function var_0_0.getTaskGroupData(arg_31_0, arg_31_1)
	for iter_31_0 = 1, #arg_31_0.taskGroups do
		local var_31_0 = arg_31_0.taskGroups[iter_31_0].taskDic

		for iter_31_1, iter_31_2 in ipairs(var_31_0) do
			if iter_31_2.data.id == arg_31_1 then
				return iter_31_2.data
			end
		end
	end

	return nil
end

function var_0_0.getTaskPos(arg_32_0, arg_32_1)
	for iter_32_0 = 1, #arg_32_0.taskGroups do
		local var_32_0 = arg_32_0.taskGroups[iter_32_0].taskDic

		for iter_32_1, iter_32_2 in ipairs(var_32_0) do
			if iter_32_2.data.id == arg_32_1 then
				return iter_32_2.data.pos
			end
		end
	end

	return nil
end

function var_0_0.getTask(arg_33_0, arg_33_1)
	local var_33_0 = getProxy(TaskProxy)
	local var_33_1
	local var_33_2 = var_33_0:getTaskById(arg_33_1)

	if var_33_2 then
		return var_33_2
	end

	local var_33_3 = var_33_0:getFinishTaskById(arg_33_1)

	if var_33_3 then
		return var_33_3
	end

	return nil
end

function var_0_0.getGetAbleTask(arg_34_0)
	local var_34_0 = {}
	local var_34_1 = getProxy(TaskProxy)
	local var_34_2 = arg_34_0:getActiveTask()

	for iter_34_0 = 1, #var_34_2 do
		local var_34_3 = var_34_1:getTaskById(var_34_2[iter_34_0])

		if var_34_3 and var_34_3:getTaskStatus() == 1 then
			table.insert(var_34_0, var_34_3.id)
		end
	end

	return var_34_0
end

function var_0_0.getActiveTask(arg_35_0)
	local var_35_0 = {}

	for iter_35_0 = 1, #arg_35_0.taskGroups do
		local var_35_1 = arg_35_0.taskGroups[iter_35_0].taskDic

		for iter_35_1, iter_35_2 in ipairs(var_35_1) do
			if not iter_35_2.data.before then
				table.insert(var_35_0, iter_35_2.data.id)
			elseif arg_35_0:checkTaskBeforeComplete(iter_35_2.data.before) then
				table.insert(var_35_0, iter_35_2.data.id)
			end
		end
	end

	return var_35_0
end

function var_0_0.taskSelectTag(arg_36_0, arg_36_1, arg_36_2)
	local var_36_0 = 0

	if arg_36_0.currentSelectIndex then
		var_36_0 = math.abs(arg_36_0.currentSelectIndex - arg_36_1)
	end

	arg_36_0.currentSelectIndex = arg_36_1
	arg_36_0.currentSelectTag = arg_36_0.taskTagTfs[arg_36_1]
	arg_36_0.currentTaskDatas = arg_36_0.taskListDatas[arg_36_1]

	for iter_36_0 = 1, #arg_36_0.taskTagTfs do
		local var_36_1 = arg_36_0.taskTagTfs[iter_36_0]

		setActive(findTF(var_36_1, "select"), arg_36_0.currentSelectTag == var_36_1)
	end

	arg_36_0.taskScrollRect = GetComponent(findTF(arg_36_0.taskPanel, "ad/task"), typeof(ScrollRect))

	local var_36_2 = var_0_1 - 1
	local var_36_3 = Vector2(arg_36_0.taskScrollRect.normalizedPosition.x, arg_36_0.taskScrollRect.normalizedPosition.y)

	if arg_36_2 then
		local var_36_4 = arg_36_0.taskScrollRect.normalizedPosition.y
		local var_36_5 = (var_36_2 - (arg_36_1 - 1)) / var_36_2

		if LeanTween.isTweening(go(arg_36_0._tf)) then
			LeanTween.cancel(go(arg_36_0._tf))
		end

		LeanTween.value(go(arg_36_0._tf), var_36_4, var_36_5, 0.3 + var_36_0 * 0.1):setOnUpdate(System.Action_float(function(arg_37_0)
			var_36_3.y = arg_37_0
			arg_36_0.taskScrollRect.normalizedPosition = var_36_3

			arg_36_0.taskScrollRect.onValueChanged:Invoke(var_36_3)
		end))
	else
		scrollTo(arg_36_0.taskScrollRect, 0, (var_36_2 - (arg_36_1 - 1)) / var_36_2)
	end
end

function var_0_0.openTaskPanel(arg_38_0, arg_38_1)
	arg_38_1 = arg_38_1 or 1

	arg_38_0:taskSelectTag(arg_38_1, false)
	setActive(arg_38_0.taskPanel, true)
end

function var_0_0.sortListDatas(arg_39_0, arg_39_1)
	local var_39_0

	local function var_39_1(arg_40_0)
		for iter_40_0, iter_40_1 in ipairs(var_39_0) do
			if iter_40_1[1] == arg_40_0[1] and iter_40_1[2] == arg_40_0[2] then
				return false
			end
		end

		return true
	end

	local function var_39_2(arg_41_0, arg_41_1)
		for iter_41_0, iter_41_1 in ipairs(arg_41_1) do
			if iter_41_1.id == arg_41_0 then
				return iter_41_1
			end
		end
	end

	for iter_39_0 = 1, #arg_39_1 do
		var_39_0 = {}

		local var_39_3 = arg_39_1[iter_39_0]
		local var_39_4

		for iter_39_1 = 1, #var_39_3 do
			local var_39_5
			local var_39_6 = var_39_3[iter_39_1]

			if not var_39_6.before then
				var_39_5 = {
					0,
					0
				}
			elseif var_39_6.before then
				local var_39_7 = var_39_2(var_39_6.before, var_39_3)

				assert(var_39_7, "找不到前置id.." .. var_39_6.before)

				local var_39_8 = var_39_7.pos
				local var_39_9 = {
					var_39_8[1] + 1,
					var_39_8[2]
				}

				for iter_39_2 = 1, 10 do
					if var_39_1(var_39_9) then
						break
					else
						if iter_39_2 == 1 then
							var_39_9[1] = var_39_9[1] - 1
						end

						if var_39_9[2] > 0 then
							var_39_9[2] = var_39_9[2] * -1
						else
							var_39_9[2] = math.abs(var_39_9[2]) + 1
						end

						if var_39_8[2] - var_39_9[2] > 1 then
							var_39_7.pos = {
								var_39_9[1],
								var_39_9[2]
							}
							var_39_9[1] = var_39_9[1] + 1
						end
					end

					assert(iter_39_2 ~= 10, "任务分支超过10个")
				end

				var_39_5 = var_39_9
			end

			var_39_6.pos = var_39_5

			table.insert(var_39_0, var_39_5)
		end
	end
end

function var_0_0.openSubmitPanel(arg_42_0, arg_42_1)
	setActive(arg_42_0.submitPanel, true)

	local var_42_0 = arg_42_0.currentSelectIndex

	setImageSprite(findTF(arg_42_0.submitPanel, "icon/img"), GetSpriteFromAtlas("ui/senrankaguramedalui_atlas", "player_icon_" .. var_42_0), true)

	local var_42_1 = arg_42_0:getTask(arg_42_1.id)
	local var_42_2 = arg_42_0:checkTaskBeforeComplete(arg_42_1.before)

	if var_42_1 then
		arg_42_0.selectTask = var_42_1

		setText(findTF(arg_42_0.submitPanel, "taskDesc"), var_42_1:getConfig("desc"))
		setText(findTF(arg_42_0.submitPanel, "img/taskName"), var_42_1:getConfig("name"))

		local var_42_3 = var_42_1:getProgress()
		local var_42_4 = var_42_1:getConfig("target_num")

		setText(findTF(arg_42_0.submitPanel, "progress/taskProgress"), setColorStr(var_42_3, "#C2695B") .. "/" .. setColorStr(var_42_4, "#9D6B59"))

		local var_42_5 = var_42_1:getConfig("award_display")

		arg_42_0:setSubmitAward(var_42_5)
		setActive(arg_42_0.submitGo, var_42_1:getTaskStatus() == 0 or not var_42_2)
		setActive(arg_42_0.submitGet, var_42_1:getTaskStatus() == 1 and var_42_2)
		setActive(arg_42_0.submitGot, var_42_1:getTaskStatus() == 2)
	end
end

function var_0_0.initSubmitPanel(arg_43_0)
	arg_43_0.submitGet = findTF(arg_43_0.submitPanel, "get")
	arg_43_0.submitGot = findTF(arg_43_0.submitPanel, "got")
	arg_43_0.submitGo = findTF(arg_43_0.submitPanel, "go")
	arg_43_0.submitbtnBack = findTF(arg_43_0.submitPanel, "back")
	arg_43_0.submitDisplayContent = findTF(arg_43_0.submitPanel, "itemDisplay/viewport/content")
	arg_43_0.submitItemTpl = findTF(arg_43_0.submitPanel, "itemDisplay/viewport/content/item")

	setActive(arg_43_0.submitItemTpl, false)

	arg_43_0.submitItemDesc = findTF(arg_43_0.submitPanel, "itemDesc")
	arg_43_0.submitItems = {}

	onButton(arg_43_0, findTF(arg_43_0.submitPanel, "black"), function()
		setActive(arg_43_0.submitPanel, false)
	end, SOUND_BACK)
	onButton(arg_43_0, arg_43_0.submitbtnBack, function()
		setActive(arg_43_0.submitPanel, false)
	end, SOUND_BACK)
	onButton(arg_43_0, arg_43_0.submitGet, function()
		if arg_43_0.selectTask then
			arg_43_0:emit(SenrankaguraMedalMediator.SUBMIT_TASK, arg_43_0.selectTask.id)
		end

		setActive(arg_43_0.submitPanel, false)
	end, SOUND_BACK)
	onButton(arg_43_0, arg_43_0.submitGo, function()
		setActive(arg_43_0.submitPanel, false)

		if arg_43_0.selectTask then
			arg_43_0:emit(SenrankaguraMedalMediator.TASK_GO, arg_43_0.selectTask)
		end
	end, SOUND_BACK)
	setText(findTF(arg_43_0.submitPanel, "bg/txtDesc"), i18n("ryza_task_detail_content"))
	setText(findTF(arg_43_0.submitPanel, "bg/txtAward"), i18n("ryza_task_detail_award"))
end

function var_0_0.setSubmitAward(arg_48_0, arg_48_1)
	if #arg_48_0.submitItems < #arg_48_1 then
		for iter_48_0 = 1, #arg_48_1 - #arg_48_0.submitItems do
			local var_48_0 = tf(instantiate(arg_48_0.submitItemTpl))

			setParent(var_48_0, arg_48_0.submitDisplayContent)
			table.insert(arg_48_0.submitItems, var_48_0)
		end
	end

	for iter_48_1 = 1, #arg_48_0.submitItems do
		local var_48_1 = arg_48_0.submitItems[iter_48_1]

		if iter_48_1 <= #arg_48_1 then
			local var_48_2 = {
				type = arg_48_1[iter_48_1][1],
				id = arg_48_1[iter_48_1][2],
				count = arg_48_1[iter_48_1][3]
			}

			updateDrop(var_48_1, var_48_2)
			onButton(arg_48_0, var_48_1, function()
				arg_48_0:emit(BaseUI.ON_DROP, var_48_2)
			end, SFX_PANEL)
			setActive(var_48_1, true)
		else
			setActive(var_48_1, false)
		end
	end
end

function var_0_0.willExit(arg_50_0)
	if LeanTween.isTweening(go(arg_50_0._tf)) then
		LeanTween.cancel(go(arg_50_0._tf))
	end
end

return var_0_0
