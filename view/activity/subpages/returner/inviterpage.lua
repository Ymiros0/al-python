﻿local var_0_0 = class("InviterPage")

var_0_0.REFRESH_TIME = 1800

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._event = arg_1_2
	arg_1_0._go = arg_1_1
	arg_1_0._tf = tf(arg_1_1)
	arg_1_0.ptTxt = arg_1_0._tf:Find("pt_panel/slider/Text"):GetComponent(typeof(Text))
	arg_1_0.phaseTotalTxt = arg_1_0._tf:Find("pt_panel/total_progress"):GetComponent(typeof(Text))
	arg_1_0.phaseTxt = arg_1_0._tf:Find("pt_panel/progress"):GetComponent(typeof(Text))
	arg_1_0.progress = arg_1_0._tf:Find("pt_panel/slider")
	arg_1_0.getBtn = arg_1_0._tf:Find("pt_panel/get")
	arg_1_0.awardTF = arg_1_0._tf:Find("pt_panel/item")
	arg_1_0.awardOverView = arg_1_0._tf:Find("pt_panel/award_overview")
	arg_1_0.bg = arg_1_0._tf:Find("bg"):GetComponent(typeof(Image))
	arg_1_0.returnerList = UIItemList.New(arg_1_0._tf:Find("returners/content"), arg_1_0._tf:Find("returners/content/tpl"))
	arg_1_0.help = arg_1_0._tf:Find("help")
	arg_1_0.pushBtn = arg_1_0._tf:Find("push_btn")
	arg_1_0.pushedBtn = arg_1_0._tf:Find("pushed_btn")
	arg_1_0.pushDisBtn = arg_1_0._tf:Find("push_btn_dis")
	arg_1_0.codeTxt = arg_1_0._tf:Find("code"):GetComponent(typeof(Text))
	arg_1_0.taskLockPanel = arg_1_0._tf:Find("task_lock_panel")
	arg_1_0.taskPanel = arg_1_0._tf:Find("task_panel")
	arg_1_0.taskItemTF = arg_1_0._tf:Find("task_panel/item")
	arg_1_0.taskProgress = arg_1_0._tf:Find("task_panel/progress")
	arg_1_0.taskDesc = arg_1_0._tf:Find("task_panel/desc")
	arg_1_0.taskGoBtn = arg_1_0._tf:Find("task_panel/go")
	arg_1_0.taskGotBtn = arg_1_0._tf:Find("task_panel/got")
	arg_1_0.taskGetBtn = arg_1_0._tf:Find("task_panel/get")
	arg_1_0.taskProgressTxt = arg_1_0._tf:Find("task_panel/p"):GetComponent(typeof(Text))

	arg_1_0:Init()
end

function var_0_0.Init(arg_2_0)
	onButton(arg_2_0, arg_2_0.getBtn, function()
		arg_2_0._event:emit(ActivityMediator.RETURN_AWARD_OP, {
			activity_id = arg_2_0.activity.id,
			cmd = ActivityConst.RETURN_AWARD_OP_GET_AWARD,
			arg1 = arg_2_0.nextTarget
		})
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.awardOverView, function()
		arg_2_0._event:emit(ActivityMediator.RETURN_AWARD_OP, {
			cmd = ActivityConst.RETURN_AWARD_OP_SHOW_AWARD_OVERVIEW,
			arg1 = {
				dropList = arg_2_0.config.drop_client,
				targets = arg_2_0.config.target,
				fetchList = arg_2_0.fetchList,
				count = arg_2_0.pt,
				resId = arg_2_0.config.pt
			}
		})
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.pushBtn, function()
		if arg_2_0.isPush then
			return
		end

		if not arg_2_0.returners or #arg_2_0.returners >= 3 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("returner_max_count"))

			return
		end

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("returner_push_tip"),
			onYes = function()
				arg_2_0._event:emit(ActivityMediator.RETURN_AWARD_OP, {
					activity_id = arg_2_0.activity.id,
					cmd = ActivityConst.RETURN_AWARD_OP_PUSH_UID,
					arg1 = arg_2_0.code
				})
			end
		})
	end, SFX_PANEL)
end

function var_0_0.Update(arg_7_0, arg_7_1)
	arg_7_0.activity = arg_7_1

	local var_7_0 = pg.TimeMgr.GetInstance():GetServerTime()

	if not ActivityMainScene.FetchReturnersTime or var_7_0 >= ActivityMainScene.FetchReturnersTime then
		ActivityMainScene.FetchReturnersTime = var_7_0 + var_0_0.REFRESH_TIME

		arg_7_0._event:emit(ActivityMediator.RETURN_AWARD_OP, {
			activity_id = arg_7_0.activity.id,
			cmd = ActivityConst.RETURN_AWARD_OP_GET_RETRUNERS
		})

		return
	end

	arg_7_0:UpdateData()
	arg_7_0:UpdateUI()
	arg_7_0:UpdateReturners()
end

function var_0_0.getTotalPt(arg_8_0, arg_8_1)
	local var_8_0 = 0

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.returners) do
		var_8_0 = var_8_0 + iter_8_1:getPt()
	end

	return var_8_0 + arg_8_1
end

function var_0_0.UpdateData(arg_9_0)
	local var_9_0 = arg_9_0.activity

	arg_9_0.isPush = var_9_0.data2_list[1] == 1
	arg_9_0.code = getProxy(PlayerProxy):getRawData().id
	arg_9_0.fetchList = var_9_0.data1_list
	arg_9_0.config = pg.activity_template_headhunting[var_9_0.id]
	arg_9_0.targets = arg_9_0.config.target
	arg_9_0.nextIndex = -1

	for iter_9_0 = 1, #arg_9_0.targets do
		local var_9_1 = arg_9_0.targets[iter_9_0]

		if not table.contains(arg_9_0.fetchList, var_9_1) then
			arg_9_0.nextIndex = iter_9_0

			break
		end
	end

	if arg_9_0.nextIndex == -1 then
		arg_9_0.fetchIndex = #arg_9_0.targets
		arg_9_0.nextIndex = #arg_9_0.targets
	else
		arg_9_0.fetchIndex = math.max(arg_9_0.nextIndex - 1, 0)
	end

	arg_9_0.drops = arg_9_0.config.drop_client
	arg_9_0.nextDrops = arg_9_0.config.drop_client[arg_9_0.nextIndex]
	arg_9_0.nextTarget = arg_9_0.targets[arg_9_0.nextIndex]
	arg_9_0.returners = var_9_0:getClientList()

	local var_9_2 = var_9_0.data3

	arg_9_0.pt = arg_9_0:getTotalPt(var_9_2)

	setActive(arg_9_0.pushBtn, not arg_9_0.isPush and #arg_9_0.returners < 3)
	setActive(arg_9_0.pushedBtn, arg_9_0.isPush)
	setActive(arg_9_0.pushDisBtn, not arg_9_0.isPush and #arg_9_0.returners >= 3)
end

function var_0_0.UpdateUI(arg_10_0)
	arg_10_0.codeTxt.text = arg_10_0.code
	arg_10_0.ptTxt.text = arg_10_0.pt .. "/" .. arg_10_0.nextTarget

	setActive(arg_10_0.getBtn, arg_10_0.fetchIndex ~= #arg_10_0.targets and arg_10_0.pt >= arg_10_0.nextTarget)

	arg_10_0.phaseTxt.text = arg_10_0.fetchIndex
	arg_10_0.phaseTotalTxt.text = #arg_10_0.targets

	setFillAmount(arg_10_0.progress, arg_10_0.pt / arg_10_0.nextTarget)

	local var_10_0 = arg_10_0.nextDrops

	updateDrop(arg_10_0.awardTF, {
		type = var_10_0[1],
		id = var_10_0[2],
		count = var_10_0[3]
	})

	local var_10_1 = pg.activity_template_headhunting[arg_10_0.activity.id].tasklist

	arg_10_0:UpdateTasks(var_10_1)
end

function var_0_0.getTask(arg_11_0, arg_11_1)
	local var_11_0 = getProxy(TaskProxy)

	return var_11_0:getTaskById(arg_11_1) or var_11_0:getFinishTaskById(arg_11_1)
end

function var_0_0.UpdateTasks(arg_12_0, arg_12_1)
	if arg_12_0.isPush then
		local var_12_0 = arg_12_0.activity
		local var_12_1 = var_12_0:getDayIndex()
		local var_12_2 = getProxy(TaskProxy)
		local var_12_3 = 0

		for iter_12_0 = #arg_12_1, 1, -1 do
			if arg_12_0:getTask(arg_12_1[iter_12_0]) then
				var_12_3 = iter_12_0

				break
			end
		end

		local var_12_4 = arg_12_0:getTask(arg_12_1[var_12_3])

		if (not var_12_4 or var_12_4:isReceive()) and var_12_3 < var_12_1 then
			if var_12_3 == #arg_12_1 and var_12_4 and var_12_4:isReceive() then
				arg_12_0:UpdateTaskTF(var_12_4)
			else
				arg_12_0._event:emit(ActivityMediator.RETURN_AWARD_OP, {
					activity_id = var_12_0.id,
					cmd = ActivityConst.RETURN_AWARD_OP_ACCEPT_TASK
				})
			end
		else
			assert(var_12_4)
			arg_12_0:UpdateTaskTF(var_12_4)
		end
	else
		setActive(arg_12_0.taskPanel, false)
		setActive(arg_12_0.taskLockPanel, true)
	end
end

function var_0_0.UpdateTaskTF(arg_13_0, arg_13_1)
	setActive(arg_13_0.taskLockPanel, false)
	setActive(arg_13_0.taskPanel, true)

	local var_13_0 = arg_13_1:isFinish()
	local var_13_1 = arg_13_1:isReceive()

	setActive(arg_13_0.taskGoBtn, arg_13_1 and not var_13_0)
	setActive(arg_13_0.taskGotBtn, arg_13_1 and var_13_1)
	setActive(arg_13_0.taskGetBtn, arg_13_1 and var_13_0 and not var_13_1)

	local var_13_2 = arg_13_1:getConfig("award_display")[1]

	updateDrop(arg_13_0.taskItemTF, {
		type = var_13_2[1],
		id = var_13_2[2],
		count = var_13_2[3]
	})
	setFillAmount(arg_13_0.taskProgress, arg_13_1:getProgress() / arg_13_1:getConfig("target_num"))
	setText(arg_13_0.taskDesc, arg_13_1:getConfig("desc"))

	arg_13_0.taskProgressTxt.text = arg_13_1:getProgress() .. "/" .. arg_13_1:getConfig("target_num")

	onButton(arg_13_0, arg_13_0.taskGoBtn, function()
		arg_13_0._event:emit(ActivityMediator.ON_TASK_GO, arg_13_1)
	end, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.taskGetBtn, function()
		arg_13_0._event:emit(ActivityMediator.ON_TASK_SUBMIT, arg_13_1)
	end, SFX_PANEL)
end

local function var_0_1(arg_16_0, arg_16_1)
	LoadSpriteAsync("qicon/" .. arg_16_1:getPainting(), function(arg_17_0)
		if not IsNil(arg_16_0) then
			arg_16_0:GetComponent(typeof(Image)).sprite = arg_17_0
		end
	end)
	UIItemList.New(arg_16_0:Find("starts"), arg_16_0:Find("starts/tpl")):align(arg_16_1:getStar())
end

function var_0_0.UpdateReturners(arg_18_0)
	local var_18_0 = arg_18_0.returners

	arg_18_0.returnerList:make(function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 == UIItemList.EventUpdate then
			local var_19_0 = var_18_0[arg_19_1 + 1]

			if var_19_0 then
				local var_19_1 = var_19_0:getIcon()
				local var_19_2 = Ship.New({
					configId = var_19_1
				})

				var_0_1(arg_19_2:Find("info/icon"), var_19_2)
				setText(arg_19_2:Find("info/name"), var_19_0:getName())
				setText(arg_19_2:Find("info/pt/Text"), var_19_0:getPt())
			end

			setActive(arg_19_2:Find("empty"), not var_19_0)
			setActive(arg_19_2:Find("info"), var_19_0)
		end
	end)
	arg_18_0.returnerList:align(2)
end

function var_0_0.Dispose(arg_20_0)
	pg.DelegateInfo.Dispose(arg_20_0)

	arg_20_0.bg.sprite = nil
end

return var_0_0
