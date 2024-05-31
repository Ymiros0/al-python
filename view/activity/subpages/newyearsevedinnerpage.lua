﻿local var_0_0 = class("NewYearsEveDinnerPage", import(".TemplatePage.SkinTemplatePage"))
local var_0_1 = 3
local var_0_2 = 2
local var_0_3 = Vector2(760, -144)
local var_0_4 = Vector2(370, -144)

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.roleTF = arg_1_0:findTF("mask/role_pos", arg_1_0.bg)
	arg_1_0.effectNode = arg_1_0:findTF("mofang_yanwu", arg_1_0.bg)
	arg_1_0.foodTF = arg_1_0:findTF("food", arg_1_0.bg)
	arg_1_0.dialogTF = arg_1_0:findTF("dialog", arg_1_0.bg)
	arg_1_0.rightPanel = arg_1_0:findTF("right_panel", arg_1_0.bg)
	arg_1_0.helpBtn = arg_1_0:findTF("help_btn", arg_1_0.rightPanel)
	arg_1_0.titleFoodTF = arg_1_0:findTF("menu_title/icon", arg_1_0.rightPanel)
	arg_1_0.cookBtn = arg_1_0:findTF("cook_btn", arg_1_0.rightPanel)
	arg_1_0.cookProgress = arg_1_0:findTF("progress", arg_1_0.cookBtn)
	arg_1_0.cookAwardTF = arg_1_0:findTF("award", arg_1_0.cookBtn)
end

function var_0_0.OnDataSetting(arg_2_0)
	arg_2_0.cookActID = arg_2_0.activity:getConfig("config_client").linkTaskPoolAct
	arg_2_0.cookCfg = pg.activity_template[arg_2_0.cookActID].config_client
	arg_2_0.cookTaskIds = pg.activity_template[arg_2_0.cookActID].config_data
	arg_2_0.totalCookCnt = #arg_2_0.cookTaskIds
	arg_2_0.playerId = getProxy(PlayerProxy):getData().id
	arg_2_0.randomSeed = arg_2_0:GetRandomById()

	var_0_0.super.OnDataSetting(arg_2_0)
end

function var_0_0.GetRandomById(arg_3_0)
	local var_3_0 = arg_3_0.playerId
	local var_3_1 = {}

	while #var_3_1 < 7 do
		local var_3_2 = var_3_0 % 10

		var_3_0 = math.floor(var_3_0 / 10)

		if var_3_0 == 0 then
			var_3_0 = arg_3_0.playerId
		end

		table.insert(var_3_1, var_3_2)
	end

	return var_3_1
end

function var_0_0.OnFirstFlush(arg_4_0)
	var_0_0.super.OnFirstFlush(arg_4_0)
	onButton(arg_4_0, arg_4_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.sevenday_nianye.tip
		})
	end, SFX_PANEL)
	onButton(arg_4_0, arg_4_0.cookBtn, function()
		if arg_4_0.isMoving then
			pg.TipsMgr.GetInstance():ShowTips(i18n("tip_nianye"))

			return
		end

		if arg_4_0.isEffectPlaying then
			return
		end

		local var_6_0 = arg_4_0.taskProxy:getTaskVO(arg_4_0.curTaskId)

		if var_6_0:getTaskStatus() == 1 then
			setActive(arg_4_0.effectNode, true)

			arg_4_0.isEffectPlaying = true

			arg_4_0:managedTween(LeanTween.delayedCall, function()
				arg_4_0:emit(ActivityMediator.ON_TASK_SUBMIT, var_6_0)
				setActive(arg_4_0.effectNode, false)

				arg_4_0.isEffectPlaying = false
			end, var_0_2, nil)
		end
	end, SFX_PANEL)
	setActive(arg_4_0:findTF("shine", arg_4_0.cookBtn), false)
end

function var_0_0.OnUpdateFlush(arg_8_0)
	var_0_0.super.OnUpdateFlush(arg_8_0)

	arg_8_0.cookAct = getProxy(ActivityProxy):getActivityById(arg_8_0.cookActID)

	assert(arg_8_0.cookAct and not arg_8_0.cookAct:isEnd(), "自选任务池活动(type86)已结束")
	arg_8_0:RefreshCookData()
	arg_8_0:UpdateCookData()
	arg_8_0:UpdateCookUI()
end

function var_0_0.RefreshCookData(arg_9_0)
	arg_9_0.usedCnt = arg_9_0.cookAct:getData1()

	local var_9_0 = pg.TimeMgr.GetInstance()

	arg_9_0.unlockCnt = (var_9_0:DiffDay(arg_9_0.cookAct:getStartTime(), var_9_0:GetServerTime()) + 1) * arg_9_0.cookAct:getConfig("config_id")
	arg_9_0.unlockCnt = math.min(arg_9_0.unlockCnt, arg_9_0.totalCookCnt)
	arg_9_0.remainCnt = arg_9_0.usedCnt >= arg_9_0.totalCookCnt and 0 or arg_9_0.unlockCnt - arg_9_0.usedCnt
end

function var_0_0.UpdateCookData(arg_10_0)
	local var_10_0 = 0

	arg_10_0.receivedTasks = {}

	local var_10_1 = underscore.rest(arg_10_0.cookTaskIds, 1)

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.cookTaskIds) do
		local var_10_2 = arg_10_0.taskProxy:getTaskVO(iter_10_1)

		if var_10_2:isReceive() then
			table.insert(arg_10_0.receivedTasks, var_10_2)

			var_10_0 = var_10_0 + 1

			table.removebyvalue(var_10_1, iter_10_1)
		end
	end

	table.sort(arg_10_0.receivedTasks, function(arg_11_0, arg_11_1)
		return arg_11_0.submitTime < arg_11_1.submitTime
	end)

	arg_10_0.receivedTasks = underscore.map(arg_10_0.receivedTasks, function(arg_12_0)
		return arg_12_0.id
	end)

	if arg_10_0.usedCnt ~= var_10_0 then
		arg_10_0.usedCnt = var_10_0

		local var_10_3 = arg_10_0.cookAct

		var_10_3.data1 = arg_10_0.usedCnt

		getProxy(ActivityProxy):updateActivity(var_10_3)

		return
	end

	local var_10_4 = arg_10_0.remainCnt == 0 and arg_10_0.usedCnt or arg_10_0.usedCnt + 1

	if arg_10_0.remainCnt == 0 then
		arg_10_0.curTaskId = arg_10_0.receivedTasks[#arg_10_0.receivedTasks]
	else
		arg_10_0.curTaskId = var_10_1[arg_10_0.randomSeed[var_10_4] % #var_10_1 + 1]
	end
end

function var_0_0.UpdateCookUI(arg_13_0)
	local var_13_0 = arg_13_0.remainCnt == 0 and arg_13_0.usedCnt or arg_13_0.usedCnt + 1

	setText(arg_13_0.cookProgress, var_13_0 .. "/" .. arg_13_0.totalCookCnt)

	local var_13_1 = arg_13_0.taskProxy:getTaskVO(arg_13_0.curTaskId)
	local var_13_2 = var_13_1:getConfig("award_display")[1]
	local var_13_3 = {
		type = var_13_2[1],
		id = var_13_2[2],
		count = var_13_2[3]
	}

	updateDrop(arg_13_0.cookAwardTF, var_13_3)

	local var_13_4 = var_13_1:getTaskStatus() == 2

	setActive(arg_13_0:findTF("got", arg_13_0.cookAwardTF), var_13_4)
	setActive(arg_13_0:findTF("icon_bg/count", arg_13_0.cookAwardTF), var_13_4)
	setText(arg_13_0:findTF("Text", arg_13_0.dialogTF), i18n(arg_13_0.cookCfg[arg_13_0.curTaskId][3]))

	local var_13_5 = var_13_4 and arg_13_0.cookCfg[arg_13_0.curTaskId][2] .. "_2" or "unknown"

	GetImageSpriteFromAtlasAsync("ui/activityuipage/NewYearsEveDinnerPage_atlas", arg_13_0.cookCfg[arg_13_0.curTaskId][2], arg_13_0.foodTF, true)
	GetImageSpriteFromAtlasAsync("ui/activityuipage/NewYearsEveDinnerPage_atlas", var_13_5, arg_13_0.titleFoodTF, true)

	arg_13_0.prefabName = arg_13_0.cookCfg[arg_13_0.curTaskId][1]

	pg.UIMgr.GetInstance():LoadingOn()
	PoolMgr.GetInstance():GetSpineChar(arg_13_0.prefabName, true, function(arg_14_0)
		pg.UIMgr.GetInstance():LoadingOff()

		arg_13_0.modelTf = tf(arg_14_0)
		arg_13_0.modelTf.localPosition = Vector3(0, 0, 0)
		arg_13_0.modelTf.localScale = Vector3(1, 1, 1)

		arg_13_0:ClearRole()
		setParent(arg_13_0.modelTf, arg_13_0.roleTF)
		arg_13_0:PlayRoleAnim()
	end)
end

function var_0_0.ClearRole(arg_15_0)
	arg_15_0.isMoving = false

	if LeanTween.isTweening(arg_15_0.roleTF) then
		LeanTween.cancel(arg_15_0.roleTF)
	end

	removeAllChildren(arg_15_0.roleTF)
end

function var_0_0.PlayRoleAnim(arg_16_0)
	local var_16_0 = arg_16_0.taskProxy:getTaskVO(arg_16_0.curTaskId):getTaskStatus() == 2
	local var_16_1 = arg_16_0.modelTf:GetComponent("SpineAnimUI")

	setActive(arg_16_0.foodTF, false)
	setActive(arg_16_0.dialogTF, false)
	setActive(arg_16_0:findTF("shine", arg_16_0.cookBtn), false)

	if var_16_0 then
		setAnchoredPosition(arg_16_0.roleTF, var_0_4)
		var_16_1:SetAction("normal", 0)
		setActive(arg_16_0.foodTF, true)
		setActive(arg_16_0.dialogTF, true)
		setActive(arg_16_0:findTF("shine", arg_16_0.cookBtn), not var_16_0 and arg_16_0.remainCnt > 0)
	else
		var_16_1:SetAction("move", 0)

		arg_16_0.isMoving = true

		setAnchoredPosition(arg_16_0.roleTF, var_0_3)
		arg_16_0:managedTween(LeanTween.moveX, function()
			var_16_1:SetAction("normal", 0)

			arg_16_0.isMoving = false

			setActive(arg_16_0.foodTF, var_16_0)
			setActive(arg_16_0.dialogTF, var_16_0)
			setActive(arg_16_0:findTF("shine", arg_16_0.cookBtn), not var_16_0 and arg_16_0.remainCnt > 0)
		end, arg_16_0.roleTF, var_0_4.x, var_0_1):setEase(LeanTweenType.linear)
	end
end

function var_0_0.OnDestroy(arg_18_0)
	if arg_18_0.prefabName and arg_18_0.modelTf then
		PoolMgr.GetInstance():ReturnSpineChar(arg_18_0.prefabName, arg_18_0.modelTf.gameObject)

		arg_18_0.prefabName = nil
		arg_18_0.modelTf = nil
	end

	arg_18_0:cleanManagedTween()
end

return var_0_0
