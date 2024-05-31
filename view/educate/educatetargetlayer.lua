﻿local var_0_0 = class("EducateTargetLayer", import(".base.EducateBaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "EducateTargetUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:initData()
	arg_2_0:findUI()
	arg_2_0:addListener()
end

function var_0_0.initData(arg_3_0)
	arg_3_0.taskProxy = getProxy(EducateProxy):GetTaskProxy()
	arg_3_0.targetId = arg_3_0.taskProxy:GetTargetId()
	arg_3_0.mainTaskVOs = arg_3_0.taskProxy:FilterByGroup(arg_3_0.taskProxy:GetMainTasksForShow())
	arg_3_0.otherTaskVOs = arg_3_0.taskProxy:FilterByGroup(arg_3_0.taskProxy:GetTargetTasksForShow())
	arg_3_0.canGetTargetAward = arg_3_0.taskProxy:CanGetTargetAward()
end

function var_0_0.findUI(arg_4_0)
	arg_4_0.anim = arg_4_0:findTF("anim_root"):GetComponent(typeof(Animation))
	arg_4_0.animEvent = arg_4_0:findTF("anim_root"):GetComponent(typeof(DftAniEvent))

	arg_4_0.animEvent:SetEndEvent(function()
		arg_4_0:emit(var_0_0.ON_CLOSE)
	end)

	arg_4_0.windowTF = arg_4_0:findTF("anim_root/window")
	arg_4_0.leftTF = arg_4_0:findTF("left/content", arg_4_0.windowTF)
	arg_4_0.leftEmptyTF = arg_4_0:findTF("left/empty", arg_4_0.windowTF)

	setText(arg_4_0:findTF("target_info/Text", arg_4_0.leftEmptyTF), i18n("child_target_set_empty"))

	arg_4_0.targetSetBtn = arg_4_0:findTF("target_info/target_set_btn", arg_4_0.leftEmptyTF)

	setText(arg_4_0:findTF("skip_title", arg_4_0.targetSetBtn), i18n("child_target_set_skip"))

	arg_4_0.targetInfoTF = arg_4_0:findTF("target_info", arg_4_0.leftTF)
	arg_4_0.iconTF = arg_4_0:findTF("icon", arg_4_0.targetInfoTF)
	arg_4_0.nameTF = arg_4_0:findTF("name_bg/name", arg_4_0.targetInfoTF)
	arg_4_0.unfinishTF = arg_4_0:findTF("unfinish", arg_4_0.targetInfoTF)
	arg_4_0.sliderTF = arg_4_0:findTF("progress", arg_4_0.unfinishTF)
	arg_4_0.progressWhiteTF = arg_4_0:findTF("white", arg_4_0.sliderTF)

	setActive(arg_4_0.progressWhiteTF, true)
	setText(arg_4_0:findTF("progress/title", arg_4_0.unfinishTF), i18n("child_target_progress"))

	arg_4_0.progressTextTF = arg_4_0:findTF("progress/title/Text", arg_4_0.unfinishTF)
	arg_4_0.targetAwardTF = arg_4_0:findTF("award", arg_4_0.unfinishTF)
	arg_4_0.finishTF = arg_4_0:findTF("finish", arg_4_0.targetInfoTF)

	setText(arg_4_0:findTF("Text", arg_4_0.finishTF), i18n("child_target_finish_tip"))
	setText(arg_4_0:findTF("time/title", arg_4_0.leftTF), i18n("child_target_time_title"))

	arg_4_0.timeTF = arg_4_0:findTF("time/Text", arg_4_0.leftTF)
	arg_4_0.taskContentTF = arg_4_0:findTF("task_scrollview/content", arg_4_0.windowTF)
	arg_4_0.mainTaskTF = arg_4_0:findTF("main_list", arg_4_0.taskContentTF)

	setText(arg_4_0:findTF("list/tpl/status/get/btn/Text", arg_4_0.mainTaskTF), i18n("word_take"))

	arg_4_0.mainTaskUIList = UIItemList.New(arg_4_0:findTF("list", arg_4_0.mainTaskTF), arg_4_0:findTF("list/tpl", arg_4_0.mainTaskTF))
	arg_4_0.mainTitleTF = arg_4_0:findTF("title/Text", arg_4_0.mainTaskTF)

	setText(arg_4_0.mainTitleTF, i18n("child_target_title1"))

	arg_4_0.mainProgressTF = arg_4_0:findTF("title/progress", arg_4_0.mainTaskTF)

	setActive(arg_4_0.mainProgressTF, false)

	arg_4_0.otherTaskTF = arg_4_0:findTF("other_list", arg_4_0.taskContentTF)

	setText(arg_4_0:findTF("list/tpl/status/get/btn/Text", arg_4_0.otherTaskTF), i18n("word_take"))

	arg_4_0.otherTaskUIList = UIItemList.New(arg_4_0:findTF("list", arg_4_0.otherTaskTF), arg_4_0:findTF("list/tpl", arg_4_0.otherTaskTF))
	arg_4_0.otherTitleTF = arg_4_0:findTF("title/Text", arg_4_0.otherTaskTF)

	setText(arg_4_0.otherTitleTF, i18n("child_target_title2"))
end

function var_0_0.addListener(arg_6_0)
	onButton(arg_6_0, arg_6_0:findTF("anim_root/close"), function()
		arg_6_0:_close()
	end, SFX_PANEL)
	onButton(arg_6_0, arg_6_0.targetSetBtn, function()
		function arg_6_0.onExit()
			getProxy(EducateProxy):MainAddLayer(Context.New({
				viewComponent = EducateTargetSetLayer,
				mediator = EducateTargetSetMediator
			}))
		end

		arg_6_0:_close()
	end, SFX_PANEL)
end

function var_0_0.didEnter(arg_10_0)
	pg.UIMgr.GetInstance():OverlayPanel(arg_10_0._tf, {
		groupName = arg_10_0:getGroupNameFromData(),
		weight = arg_10_0:getWeightFromData() + 1
	})
	arg_10_0:initLeft()
	arg_10_0.mainTaskUIList:make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate then
			arg_10_0:updateItem(arg_11_1, arg_11_2, "main")
		end
	end)
	arg_10_0.otherTaskUIList:make(function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate then
			arg_10_0:updateItem(arg_12_1, arg_12_2, "other")
		end
	end)
	arg_10_0:updateItems()
	EducateGuideSequence.CheckGuide(arg_10_0.__cname, function()
		return
	end)
end

function var_0_0.sumbitTask(arg_14_0, arg_14_1)
	arg_14_0:emit(EducateTargetMediator.ON_TASK_SUBMIT, arg_14_1)
end

function var_0_0.initLeft(arg_15_0)
	setActive(arg_15_0.leftTF, arg_15_0.targetId ~= 0)
	setActive(arg_15_0.leftEmptyTF, arg_15_0.targetId == 0)

	if arg_15_0.targetId ~= 0 then
		local var_15_0 = pg.child_target_set[arg_15_0.targetId]

		LoadImageSpriteAsync("educatetarget/" .. var_15_0.icon, arg_15_0.iconTF, true)
		setText(arg_15_0.nameTF, var_15_0.name)

		local var_15_1 = var_15_0.drop_display
		local var_15_2 = {
			type = var_15_1[1],
			id = var_15_1[2],
			number = var_15_1[3]
		}

		EducateHelper.UpdateDropShow(arg_15_0.targetAwardTF, var_15_2)
		onButton(arg_15_0, arg_15_0.targetAwardTF, function()
			if arg_15_0.canGetFinishAward then
				arg_15_0:emit(EducateTargetMediator.ON_GET_TARGET_AWARD)
			else
				arg_15_0:emit(var_0_0.EDUCATE_ON_ITEM, {
					drop = var_15_2
				})
			end
		end, SFX_PANEL)

		local var_15_3 = getProxy(EducateProxy):GetCharData():GetStageReaminWeek(var_15_0.stage)
		local var_15_4 = var_15_3 <= 1 and i18n("word_in_one_week") or var_15_3 .. i18n("word_week")

		setText(arg_15_0.timeTF, var_15_4)
	end

	arg_15_0:updataTarget()
end

function var_0_0.updataTarget(arg_17_0)
	local var_17_0, var_17_1 = getProxy(EducateProxy):GetTaskProxy():GetOtherTargetTaskProgress()
	local var_17_2 = var_17_0 / var_17_1

	if var_17_2 > 1 then
		var_17_2 = 1
	end

	if var_17_1 == 0 then
		var_17_2 = 1
	end

	setText(arg_17_0.progressTextTF, var_17_0 .. "/" .. var_17_1)

	if not arg_17_0.lastProgress or var_17_2 <= arg_17_0.lastProgress then
		setSlider(arg_17_0.sliderTF, 0, 1, var_17_2)

		arg_17_0.lastProgress = var_17_2
	else
		arg_17_0:playProgressAnim(var_17_2)

		arg_17_0.lastProgress = var_17_2
	end

	local var_17_3 = var_17_2 >= 1

	arg_17_0.canGetFinishAward = var_17_3 and arg_17_0.canGetTargetAward

	setActive(arg_17_0.unfinishTF, not var_17_3 or arg_17_0.canGetFinishAward)
	setActive(arg_17_0:findTF("receiveVX", arg_17_0.targetAwardTF), arg_17_0.canGetFinishAward)
	setActive(arg_17_0:findTF("tip", arg_17_0.unfinishTF), arg_17_0.canGetFinishAward)
	setActive(arg_17_0.finishTF, var_17_3 and not arg_17_0.canGetTargetAward)
end

function var_0_0.playProgressAnim(arg_18_0, arg_18_1)
	arg_18_0:cleanManagedTween()

	local var_18_0 = arg_18_0.sliderTF:GetComponent(typeof(Slider)).value
	local var_18_1 = arg_18_0.sliderTF.rect

	arg_18_0.progressWhiteTF.sizeDelta = Vector2(var_18_1.width * arg_18_1, var_18_1.height)

	arg_18_0.sliderTF:GetComponent(typeof(Animation)):Play("anim_educate_target_progress_add")
	arg_18_0:managedTween(LeanTween.delayedCall, function()
		arg_18_0:managedTween(LeanTween.value, nil, go(arg_18_0.sliderTF), var_18_0, arg_18_1, 0.264):setOnUpdate(System.Action_float(function(arg_20_0)
			setSlider(arg_18_0.sliderTF, 0, 1, arg_20_0)
		end)):setEase(LeanTweenType.easeInCubic)
	end, 0.132, nil)
end

function var_0_0.updateItems(arg_21_0)
	setActive(arg_21_0.mainTaskTF, #arg_21_0.mainTaskVOs > 0)
	arg_21_0.mainTaskUIList:align(#arg_21_0.mainTaskVOs)
	setActive(arg_21_0.otherTaskTF, #arg_21_0.otherTaskVOs > 0)
	arg_21_0.otherTaskUIList:align(#arg_21_0.otherTaskVOs)
end

function var_0_0.updateItem(arg_22_0, arg_22_1, arg_22_2, arg_22_3)
	local var_22_0 = arg_22_3 == "main" and arg_22_0.mainTaskVOs[arg_22_1 + 1] or arg_22_0.otherTaskVOs[arg_22_1 + 1]

	setText(arg_22_0:findTF("desc", arg_22_2), var_22_0:getConfig("name"))
	setText(arg_22_0:findTF("status/go/btn/Text", arg_22_2), var_22_0:GetProgress() .. "/" .. var_22_0:GetFinishNum())

	local var_22_1 = var_22_0:GetTaskStatus()

	setActive(arg_22_0:findTF("status/go", arg_22_2), var_22_1 == EducateTask.STATUS_UNFINISH)
	setActive(arg_22_0:findTF("status/get", arg_22_2), var_22_1 == EducateTask.STATUS_FINISH)
	setActive(arg_22_0:findTF("status/got", arg_22_2), var_22_1 == EducateTask.STATUS_RECEIVE)

	local var_22_2 = var_22_0:GetAwardShow()

	EducateHelper.UpdateDropShow(arg_22_0:findTF("award", arg_22_2), var_22_2)
	onButton(arg_22_0, arg_22_0:findTF("award", arg_22_2), function()
		arg_22_0:emit(var_0_0.EDUCATE_ON_ITEM, {
			drop = var_22_2
		})
	end)
	onButton(arg_22_0, arg_22_0:findTF("status/get", arg_22_2), function()
		if arg_22_0.isClick then
			return
		end

		arg_22_0.isClick = true

		local var_24_0 = var_22_0:IsMain() and "anim_educate_target_tpl_maingot" or "anim_educate_target_tpl_othergot"

		arg_22_2:GetComponent(typeof(Animation)):Play(var_24_0)
		onDelayTick(function()
			arg_22_0.isClick = nil

			arg_22_0:sumbitTask(var_22_0)
			var_22_0:SetRecieve()
		end, 0.5)
	end, SFX_PANEL)
end

function var_0_0.updateView(arg_26_0)
	arg_26_0:initData()
	arg_26_0:updateItems()
	arg_26_0:updataTarget()
end

function var_0_0._close(arg_27_0)
	if arg_27_0.isClick then
		return
	end

	arg_27_0.anim:Play("anim_educate_target_out")
end

function var_0_0.onBackPressed(arg_28_0)
	arg_28_0:_close()
end

function var_0_0.willExit(arg_29_0)
	arg_29_0.animEvent:SetEndEvent(nil)
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_29_0._tf)

	if arg_29_0.onExit then
		arg_29_0.onExit()
	elseif getProxy(EducateProxy):GetCurTime().month == 2 then
		getProxy(EducateProxy):CheckGuide("EducateScene")
	end
end

return var_0_0
