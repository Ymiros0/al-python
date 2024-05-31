﻿local var_0_0 = class("LinerSignPage", import("view.base.BaseActivityPage"))

function var_0_0.OnInit(arg_1_0)
	arg_1_0.lockNamed = PLATFORM_CODE == PLATFORM_CH and LOCK_NAMED
	arg_1_0.bg = arg_1_0:findTF("AD")
	arg_1_0.signTF = arg_1_0:findTF("sign", arg_1_0.bg)
	arg_1_0.items = arg_1_0:findTF("items", arg_1_0.signTF)
	arg_1_0.uilist = UIItemList.New(arg_1_0.items, arg_1_0:findTF("tpl", arg_1_0.items))
	arg_1_0.signBtn = arg_1_0:findTF("get", arg_1_0.signTF)
	arg_1_0.signGreyBtn = arg_1_0:findTF("get_grey", arg_1_0.signTF)
	arg_1_0.countText = arg_1_0:findTF("count_bg/count", arg_1_0.signTF)
	arg_1_0.namedTF = arg_1_0:findTF("named", arg_1_0.bg)
	arg_1_0.nameInput = arg_1_0:findTF("input/nickname", arg_1_0.namedTF)
	arg_1_0.sureBtn = arg_1_0:findTF("sure", arg_1_0.namedTF)
	arg_1_0.linerTF = arg_1_0:findTF("liner", arg_1_0.bg)
	arg_1_0.linerInput = arg_1_0:findTF("name/input", arg_1_0.linerTF)
	arg_1_0.linerBtn = arg_1_0:findTF("go", arg_1_0.linerTF)

	setText(arg_1_0:findTF("lock/Text", arg_1_0.linerBtn), i18n("liner_sign_unlock_tip"))

	arg_1_0.nameInput:GetComponent(typeof(InputField)).interactable = not arg_1_0.lockNamed

	setActive(arg_1_0:findTF("input/pan", arg_1_0.namedTF), not arg_1_0.lockNamed)

	arg_1_0.linerInput:GetComponent(typeof(InputField)).interactable = not arg_1_0.lockNamed

	setActive(arg_1_0:findTF("name/edit", arg_1_0.linerTF), not arg_1_0.lockNamed)
end

function var_0_0.OnDataSetting(arg_2_0)
	arg_2_0.nday = 0
	arg_2_0.taskProxy = getProxy(TaskProxy)
	arg_2_0.taskGroup = underscore.flatten(arg_2_0.activity:getConfig("config_data"))
	arg_2_0.taskConfig = pg.task_data_template
	arg_2_0.preStory = arg_2_0.activity:getConfig("config_client").preStory

	return updateActivityTaskStatus(arg_2_0.activity)
end

function var_0_0.OnFirstFlush(arg_3_0)
	arg_3_0.uilist:make(function(arg_4_0, arg_4_1, arg_4_2)
		if arg_4_0 == UIItemList.EventInit then
			local var_4_0 = arg_4_1 + 1
			local var_4_1 = arg_3_0.taskGroup[var_4_0]
			local var_4_2 = arg_3_0:findTF("item_mask/item", arg_4_2)
			local var_4_3 = Drop.Create(arg_3_0.taskConfig[var_4_1].award_display[1])

			updateDrop(var_4_2, var_4_3)
			onButton(arg_3_0, arg_4_2, function()
				arg_3_0:emit(BaseUI.ON_DROP, var_4_3)
			end, SFX_PANEL)
			GetImageSpriteFromAtlasAsync("ui/activityuipage/linersignpage_atlas", "D" .. var_4_0, arg_3_0:findTF("day", arg_4_2), true)
		elseif arg_4_0 == UIItemList.EventUpdate then
			local var_4_4 = arg_4_1 + 1
			local var_4_5 = arg_3_0.taskGroup[var_4_4]
			local var_4_6 = arg_3_0.taskProxy:getTaskById(var_4_5) or arg_3_0.taskProxy:getFinishTaskById(var_4_5)

			setActive(arg_3_0:findTF("cur", arg_4_2), var_4_4 == arg_3_0.nday)
			setActive(arg_3_0:findTF("got", arg_4_2), var_4_4 < arg_3_0.nday or var_4_6 and var_4_6:getTaskStatus() == 2)
		end
	end)
	onButton(arg_3_0, arg_3_0.signBtn, function()
		if not arg_3_0.remainCnt or arg_3_0.remainCnt <= 0 then
			return
		end

		seriesAsync({
			function(arg_7_0)
				local var_7_0 = arg_3_0.activity:getConfig("config_client").story

				if checkExist(var_7_0, {
					arg_3_0.nday
				}, {
					1
				}) then
					pg.NewStoryMgr.GetInstance():Play(var_7_0[arg_3_0.nday][1], arg_7_0)
				else
					arg_7_0()
				end
			end,
			function(arg_8_0)
				if arg_3_0.curTaskVO:getTaskStatus() == 1 then
					arg_3_0:emit(ActivityMediator.ON_TASK_SUBMIT, arg_3_0.curTaskVO, arg_8_0)
				else
					arg_8_0()
				end
			end
		})
	end, SFX_PANEL)
	setInputText(arg_3_0.nameInput, getProxy(PlayerProxy):getRawData():GetName())
	onButton(arg_3_0, arg_3_0.sureBtn, function()
		local var_9_0 = getInputText(arg_3_0.nameInput)

		if var_9_0 == "" then
			return
		end

		if not nameValidityCheck(var_9_0, 4, 14, {
			"spece_illegal_tip",
			"login_newPlayerScene_name_tooShort",
			"login_newPlayerScene_name_tooLong",
			"login_newPlayerScene_invalideName"
		}) then
			return
		end

		arg_3_0:emit(ActivityMediator.STORE_DATE, {
			actId = ActivityConst.LINER_NAMED_ID,
			strValue = var_9_0,
			callback = function()
				arg_3_0:OnUpdateFlush()
			end
		})
	end, SFX_PANEL)
	onInputEndEdit(arg_3_0, arg_3_0.linerInput, function(arg_11_0)
		if not arg_3_0:IsNamed() then
			return
		end

		if not nameValidityCheck(arg_11_0, 4, 14, {
			"spece_illegal_tip",
			"login_newPlayerScene_name_tooShort",
			"login_newPlayerScene_name_tooLong",
			"login_newPlayerScene_invalideName"
		}) then
			setInputText(arg_3_0.linerInput, arg_3_0.lastName)

			return
		else
			arg_3_0:emit(ActivityMediator.STORE_DATE, {
				actId = ActivityConst.LINER_NAMED_ID,
				strValue = arg_11_0,
				callback = function()
					pg.TipsMgr.GetInstance():ShowTips(i18n("liner_name_modify"))
					arg_3_0:OnUpdateFlush()
				end
			})
		end
	end)
	onButton(arg_3_0, arg_3_0.linerBtn, function()
		if arg_3_0:IsLockLiner() then
			return
		end

		seriesAsync({
			function(arg_14_0)
				if arg_3_0.preStory and arg_3_0.preStory ~= "" and not pg.NewStoryMgr.GetInstance():IsPlayed(arg_3_0.preStory) then
					pg.NewStoryMgr.GetInstance():Play(arg_3_0.preStory, arg_14_0)
				else
					arg_14_0()
				end
			end
		}, function()
			arg_3_0:emit(ActivityMediator.EVENT_GO_SCENE, SCENE.LINER)
		end)
	end, SFX_PANEL)
end

function var_0_0.OnUpdateFlush(arg_16_0)
	arg_16_0.nday = arg_16_0.activity.data3

	local var_16_0 = arg_16_0:IsFinishSign()

	setActive(arg_16_0.signTF, not var_16_0)
	setActive(arg_16_0.namedTF, var_16_0 and not arg_16_0:IsNamed())
	setActive(arg_16_0.linerTF, var_16_0 and arg_16_0:IsNamed())
	setActive(arg_16_0:findTF("lock", arg_16_0.linerBtn), arg_16_0:IsLockLiner())

	if not var_16_0 then
		local var_16_1 = arg_16_0.taskGroup[arg_16_0.nday]

		arg_16_0.curTaskVO = arg_16_0.taskProxy:getTaskById(var_16_1) or arg_16_0.taskProxy:getFinishTaskById(var_16_1)
		arg_16_0.remainCnt = math.min(arg_16_0.activity:getDayIndex(), #arg_16_0.taskGroup) - arg_16_0.nday

		if arg_16_0.curTaskVO:getTaskStatus() == 1 then
			arg_16_0.remainCnt = arg_16_0.remainCnt + 1
		end

		setActive(arg_16_0.signBtn, arg_16_0.remainCnt > 0)
		setActive(arg_16_0.signGreyBtn, arg_16_0.remainCnt <= 0)
		setText(arg_16_0.countText, i18n("liner_sign_cnt_tip") .. arg_16_0.remainCnt)
		arg_16_0.uilist:align(#arg_16_0.taskGroup)
	else
		arg_16_0.lastName = getProxy(ActivityProxy):getActivityById(ActivityConst.LINER_NAMED_ID):getStrData1()

		setInputText(arg_16_0.linerInput, arg_16_0.lastName)
	end
end

function var_0_0.IsFinishSign(arg_17_0)
	local var_17_0 = arg_17_0.taskGroup[#arg_17_0.taskGroup]
	local var_17_1 = arg_17_0.taskProxy:getTaskById(var_17_0) or arg_17_0.taskProxy:getFinishTaskById(var_17_0)

	return var_17_1 and var_17_1:getTaskStatus() == 2
end

function var_0_0.IsNamed(arg_18_0)
	local var_18_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.LINER_NAMED_ID)

	return var_18_0 and not var_18_0:isEnd() and var_18_0:getStrData1() ~= ""
end

function var_0_0.IsLockLiner(arg_19_0)
	local var_19_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.LINER_ID)

	return not var_19_0 or var_19_0:isEnd()
end

return var_0_0
