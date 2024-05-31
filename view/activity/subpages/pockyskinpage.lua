﻿local var_0_0 = class("PockySkinPage", import("view.base.BaseActivityPage"))

function var_0_0.GetCurrentDay()
	local var_1_0 = pg.TimeMgr.GetInstance():GetServerTime()

	return pg.TimeMgr.GetInstance():STimeDescS(var_1_0, "*t").yday
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0.bg = arg_2_0:findTF("AD")
	arg_2_0.leftStage = arg_2_0.bg:Find("left")
	arg_2_0.rightStage = arg_2_0.bg:Find("right")
	arg_2_0.taskDesc = arg_2_0.leftStage:Find("task")
	arg_2_0.signDesc = arg_2_0.leftStage:Find("signin")
	arg_2_0.spine = nil
	arg_2_0.spineLRQ = GetSpineRequestPackage.New("beierfasite_4", function(arg_3_0)
		SetParent(arg_3_0, arg_2_0.leftStage:Find("ship"))

		arg_2_0.spine = arg_3_0
		arg_2_0.spine.transform.localScale = Vector3.one

		arg_2_0:SetAction("stand")

		arg_2_0.spineLRQ = nil
	end):Start()

	local var_2_0 = getProxy(PlayerProxy):getRawData().id

	arg_2_0.startDay = PlayerPrefs.GetInt("PockySkinSignDay" .. (var_2_0 or "-1"), 0)
	arg_2_0.usmLRQ = nil
end

function var_0_0.OnDataSetting(arg_4_0)
	local var_4_0 = getProxy(ActivityProxy)
	local var_4_1 = arg_4_0.activity:getConfig("config_client").linkids
	local var_4_2 = false

	arg_4_0.ActSignIn = arg_4_0.activity
	arg_4_0.taskProxy = getProxy(TaskProxy)

	if arg_4_0.ActSignIn then
		arg_4_0.nday = 0
		arg_4_0.taskGroup = arg_4_0.ActSignIn:getConfig("config_data")
		var_4_2 = var_4_2 or updateActivityTaskStatus(arg_4_0.ActSignIn)
	end

	arg_4_0.ActPT = var_4_0:getActivityById(var_4_1[1])

	if arg_4_0.ActPT then
		if arg_4_0.ptData then
			arg_4_0.ptData:Update(arg_4_0.ActPT)
		else
			arg_4_0.ptData = ActivityPtData.New(arg_4_0.ActPT)
		end
	end

	arg_4_0.ActTaskList = var_4_0:getActivityById(var_4_1[2])

	if arg_4_0.ActTaskList then
		arg_4_0.nday2 = 0
		arg_4_0.taskGroup2 = arg_4_0.ActTaskList:getConfig("config_data")
		var_4_2 = var_4_2 or updateActivityTaskStatus(arg_4_0.ActTaskList)
	end

	arg_4_0.ActFinal = var_4_0:getActivityById(var_4_1[3])

	if arg_4_0.ActFinal then
		arg_4_0.nday3 = 0
		arg_4_0.taskGroup3 = arg_4_0.ActFinal:getConfig("config_data")
		var_4_2 = var_4_2 or updateActivityTaskStatus(arg_4_0.ActFinal)
	end

	return var_4_2
end

function var_0_0.OnFirstFlush(arg_5_0)
	onButton(arg_5_0, arg_5_0.rightStage:Find("display_btn"), function()
		arg_5_0:emit(ActivityMediator.SHOW_AWARD_WINDOW, PtAwardWindow, {
			type = arg_5_0.ptData.type,
			dropList = arg_5_0.ptData.dropList,
			targets = arg_5_0.ptData.targets,
			level = arg_5_0.ptData.level,
			count = arg_5_0.ptData.count,
			resId = arg_5_0.ptData.resId
		})
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.rightStage:Find("battle_btn"), function()
		arg_5_0:emit(ActivityMediator.SPECIAL_BATTLE_OPERA)
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.rightStage:Find("get_btn"), function()
		local var_8_0, var_8_1 = arg_5_0.ptData:GetResProgress()

		arg_5_0:emit(ActivityMediator.EVENT_PT_OPERATION, {
			cmd = 1,
			activity_id = arg_5_0.ptData:GetId(),
			arg1 = var_8_1
		})
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.bg:Find("help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.pocky_help.tip
		})
	end, SFX_PANEL)
end

function var_0_0.SetAction(arg_10_0, arg_10_1)
	if not arg_10_0.spine then
		return
	end

	local var_10_0 = arg_10_0.spine:GetComponent("SpineAnimUI")

	if var_10_0 then
		var_10_0:SetAction(arg_10_1, 0)
	end
end

function var_0_0.OnUpdateFlush(arg_11_0)
	arg_11_0:UpdateTaskList()
	arg_11_0:UpdatePTList()

	local var_11_0 = arg_11_0.startDay < arg_11_0.GetCurrentDay()
	local var_11_1 = "ui"
	local var_11_2 = var_11_0 and "juu_factory_rest" or "juu_factory"

	if arg_11_0.usmLRQ and arg_11_0.usmLRQ.name ~= var_11_2 then
		arg_11_0.usmLRQ:Stop()

		arg_11_0.usmLRQ = nil
	end

	if arg_11_0.usmName ~= var_11_2 then
		arg_11_0.usmLRQ = LoadPrefabRequestPackage.New(var_11_1 .. "/" .. var_11_2, var_11_2, function(arg_12_0)
			if not IsNil(arg_11_0.usm) then
				Destroy(arg_11_0.usm)
			end

			arg_11_0.usm = arg_12_0

			setParent(arg_12_0, arg_11_0.bg:Find("usm"))
		end):Start()
		arg_11_0.usmName = var_11_2
	end
end

function var_0_0.UpdateTaskList(arg_13_0)
	arg_13_0.nday = arg_13_0.ActSignIn.data3 or 0
	arg_13_0.nday2 = arg_13_0.ActTaskList.data3 or 0
	arg_13_0.nday3 = arg_13_0.ActFinal.data3 or 0

	local var_13_0 = arg_13_0.ActSignIn:getConfig("config_client").story

	if checkExist(var_13_0, {
		arg_13_0.nday
	}, {
		1
	}) then
		pg.NewStoryMgr.GetInstance():Play(var_13_0[arg_13_0.nday][1])
	end

	local var_13_1 = arg_13_0.leftStage:Find("go_btn")
	local var_13_2 = arg_13_0.leftStage:Find("get_btn")
	local var_13_3 = arg_13_0.leftStage:Find("sign_btn")
	local var_13_4 = arg_13_0.leftStage:Find("got_btn")
	local var_13_5 = arg_13_0.leftStage:Find("award")
	local var_13_6 = arg_13_0.leftStage:Find("slider")
	local var_13_7 = getProxy(TaskProxy)
	local var_13_8 = arg_13_0.taskGroup[arg_13_0.nday][1]
	local var_13_9 = arg_13_0.taskGroup2[arg_13_0.nday2][1]
	local var_13_10 = arg_13_0.taskGroup3[arg_13_0.nday3][1]
	local var_13_11 = var_13_7:getTaskVO(var_13_8)
	local var_13_12 = var_13_7:getTaskVO(var_13_9)
	local var_13_13 = var_13_7:getTaskVO(var_13_10)
	local var_13_14 = var_13_11:getTaskStatus()
	local var_13_15 = var_13_12:getTaskStatus()
	local var_13_16 = var_13_13:getTaskStatus()

	if not arg_13_0.startTaskid then
		arg_13_0.startTaskid = var_13_8
		arg_13_0.startStatus = var_13_14
	end

	local var_13_17 = false

	if arg_13_0.startTaskid ~= var_13_8 then
		arg_13_0.startTaskid = var_13_8
		arg_13_0.startStatus = var_13_14
		var_13_17 = true
	elseif arg_13_0.startStatus ~= var_13_14 then
		arg_13_0.startStatus = var_13_14
		var_13_17 = true
	end

	local var_13_18 = arg_13_0.GetCurrentDay()

	if var_13_17 and var_13_18 > arg_13_0.startDay then
		arg_13_0.startDay = var_13_18

		local var_13_19 = getProxy(PlayerProxy):getRawData().id

		PlayerPrefs.SetInt("PockySkinSignDay" .. (var_13_19 or "-1"), arg_13_0.startDay)
	end

	if var_13_16 == 2 then
		setActive(var_13_5, false)
		setActive(var_13_6, false)
		setActive(arg_13_0.taskDesc, false)
		setActive(arg_13_0.signDesc, true)
		setText(arg_13_0.signDesc:Find("title"), i18n("pocky_jiujiu"))
		setText(arg_13_0.signDesc:Find("desc"), i18n("pocky_jiujiu_desc"))
		setActive(var_13_1, false)
		setActive(var_13_3, true)
		setActive(var_13_2, false)
		setActive(var_13_4, false)
		onButton(arg_13_0, var_13_3, function()
			local var_14_0 = arg_13_0.GetCurrentDay()

			if var_14_0 > arg_13_0.startDay then
				arg_13_0.startDay = var_14_0

				local var_14_1 = getProxy(PlayerProxy):getRawData().id

				PlayerPrefs.SetInt("PockySkinSignDay" .. (var_14_1 or "-1"), arg_13_0.startDay)
				arg_13_0:OnUpdateFlush()
			end
		end, SFX_PANEL)
		removeOnButton(var_13_4)

		return
	end

	local var_13_20
	local var_13_21
	local var_13_22

	if arg_13_0.ptData.level >= #arg_13_0.ptData.targets and arg_13_0.nday >= #arg_13_0.taskGroup and var_13_14 == 2 and arg_13_0.nday2 >= #arg_13_0.taskGroup2 and var_13_15 == 2 then
		setActive(var_13_3, false)

		var_13_20 = var_13_2
		var_13_21 = var_13_13
	elseif arg_13_0.nday <= arg_13_0.nday2 and var_13_14 ~= 2 then
		setActive(var_13_2, false)

		var_13_20 = var_13_3
		var_13_21 = var_13_11
	else
		setActive(var_13_3, false)

		var_13_20 = var_13_2
		var_13_21 = var_13_12
	end

	local var_13_23 = var_13_21:getConfig("award_display")[1]
	local var_13_24 = {
		type = var_13_23[1],
		id = var_13_23[2],
		count = var_13_23[3]
	}

	setActive(var_13_5, true)
	updateDrop(var_13_5, var_13_24)
	onButton(arg_13_0, var_13_5, function()
		arg_13_0:emit(BaseUI.ON_DROP, var_13_24)
	end, SFX_PANEL)
	setActive(var_13_6, true)
	setActive(arg_13_0.taskDesc, true)
	setActive(arg_13_0.signDesc, false)

	local var_13_25 = var_13_21:getProgress()
	local var_13_26 = var_13_21:getConfig("target_num")

	setText(arg_13_0.taskDesc:Find("title"), var_13_21:getConfig("name"))
	setText(arg_13_0.taskDesc:Find("desc"), var_13_21:getConfig("desc"))
	setSlider(var_13_6, 0, var_13_26, var_13_25)

	local var_13_27 = var_13_21:getTaskStatus()

	setActive(var_13_1, var_13_27 == 0)
	setActive(var_13_20, var_13_27 == 1)
	setActive(var_13_4, var_13_27 == 2)
	onButton(arg_13_0, var_13_1, function()
		arg_13_0:emit(ActivityMediator.ON_TASK_GO, var_13_21)
	end, SFX_PANEL)
	onButton(arg_13_0, var_13_20, function()
		arg_13_0:emit(ActivityMediator.ON_TASK_SUBMIT, var_13_21)
	end, SFX_PANEL)
end

function var_0_0.UpdatePTList(arg_18_0)
	if not arg_18_0.ptData then
		return
	end

	local var_18_0 = arg_18_0.ptData:getTargetLevel()
	local var_18_1 = arg_18_0.ActPT:getConfig("config_client").story

	if checkExist(var_18_1, {
		var_18_0
	}, {
		1
	}) then
		pg.NewStoryMgr.GetInstance():Play(var_18_1[var_18_0][1])
	end

	local var_18_2, var_18_3 = arg_18_0.ptData:GetResProgress()
	local var_18_4 = arg_18_0.ptData:GetTotalResRequire()
	local var_18_5 = arg_18_0.rightStage:Find("slider")

	setSlider(var_18_5, 0, 1, math.min(var_18_2, var_18_3) / var_18_4)

	local var_18_6 = arg_18_0.ptData:GetUnlockedMaxResRequire()
	local var_18_7 = arg_18_0.rightStage:Find("slider_total")

	setSlider(var_18_7, 0, 1, var_18_6 / var_18_4)

	local var_18_8 = arg_18_0.ptData:CanGetAward()
	local var_18_9 = arg_18_0.ptData:CanGetNextAward()
	local var_18_10 = arg_18_0.ptData:CanGetMorePt()

	setActive(arg_18_0.rightStage:Find("battle_btn"), var_18_10 and not var_18_8 and var_18_9)
	setActive(arg_18_0.rightStage:Find("get_btn"), var_18_8)
	setActive(arg_18_0.rightStage:Find("got_btn"), not var_18_9)
end

function var_0_0.OnDestroy(arg_19_0)
	if arg_19_0.spineLRQ then
		arg_19_0.spineLRQ:Stop()

		arg_19_0.spineLRQ = nil
	end

	if arg_19_0.spine then
		arg_19_0.spine.transform.localScale = Vector3.one

		pg.PoolMgr.GetInstance():ReturnSpineChar("beierfasite_4", arg_19_0.spine)

		arg_19_0.spine = nil
	end
end

return var_0_0
