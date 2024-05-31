﻿local var_0_0 = class("WorldOverviewLayer", import("..base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "WorldOverviewUI"
end

function var_0_0.preload(arg_2_0, arg_2_1)
	arg_2_0:LoadAtlasOverall(arg_2_1)
end

function var_0_0.init(arg_3_0)
	local var_3_0 = arg_3_0._tf

	arg_3_0.rtBg = var_3_0:Find("bg")

	onButton(arg_3_0, arg_3_0.rtBg, function()
		arg_3_0:closeView()
	end, SFX_CANCEL)
	setText(var_3_0:Find("tip/Text"), i18n("click_back_tip"))

	arg_3_0.rtTaskPanel = var_3_0:Find("panel/middle/info_panel/task_panel")

	setActive(arg_3_0.rtTaskPanel, false)
	setActive(arg_3_0.rtTaskPanel:Find("btn_next"), false)

	arg_3_0.entranceItemList = UIItemList.New(arg_3_0.rtTaskPanel:Find("entrance_list/target_list"), arg_3_0.rtTaskPanel:Find("entrance_list/target_tpl"))

	arg_3_0.entranceItemList:make(function(arg_5_0, arg_5_1, arg_5_2)
		arg_5_1 = arg_5_1 + 1

		if arg_5_0 == UIItemList.EventUpdate then
			if arg_3_0.entranceIds[arg_5_1] then
				local var_5_0 = nowWorld():GetEntrance(arg_3_0.entranceIds[arg_5_1])

				setActive(arg_5_2:Find("Image"), true)
				setText(arg_5_2:Find("Text"), i18n("world_task_view1") .. var_5_0:GetBaseMap():GetName())
			else
				setActive(arg_5_2:Find("Image"), true)
				setText(arg_5_2:Find("Text"), i18n("world_task_view1") .. i18n("world_task_view2"))
			end
		end
	end)

	arg_3_0.areaItemList = UIItemList.New(arg_3_0.rtTaskPanel:Find("entrance_list/target_list"), arg_3_0.rtTaskPanel:Find("entrance_list/target_tpl"))

	arg_3_0.areaItemList:make(function(arg_6_0, arg_6_1, arg_6_2)
		arg_6_1 = arg_6_1 + 1

		if arg_6_0 == UIItemList.EventUpdate then
			if arg_3_0.areaIds[arg_6_1] then
				setActive(arg_6_2:Find("Image"), true)
				setText(arg_6_2:Find("Text"), i18n("world_task_view1") .. pg.world_regions_data[arg_3_0.areaIds[arg_6_1]].name)
			else
				setActive(arg_6_2:Find("Image"), true)
				setText(arg_6_2:Find("Text"), i18n("world_task_view1") .. i18n("world_task_view2"))
			end
		end
	end)

	arg_3_0.rtAchievementPanel = var_3_0:Find("panel/middle/info_panel/achievement_panel")

	setActive(arg_3_0.rtAchievementPanel, false)

	arg_3_0.btnAchieve = arg_3_0.rtAchievementPanel:Find("btn_all")

	onButton(arg_3_0, arg_3_0.btnAchieve, function()
		local var_7_0, var_7_1 = nowWorld():GetFinishAchievements()

		if #var_7_0 == 0 then
			pg.TipsMgr.GetInstance():ShowTips("without any award")
		else
			arg_3_0:emit(WorldOverviewMediator.OnAchieveStar, var_7_0)
			arg_3_0:closeView()
		end
	end, SFX_CONFIRM)
	pg.UIMgr.GetInstance():BlurPanel(arg_3_0._tf, false, {
		blurLevelCamera = true,
		weight = LayerWeightConst.TOP_LAYER
	})
end

function var_0_0.didEnter(arg_8_0)
	local var_8_0 = arg_8_0.contextData.info

	arg_8_0.mode = var_8_0.mode

	if arg_8_0.mode == "Task" then
		arg_8_0.taskId = var_8_0.taskId

		arg_8_0:UpdateTaskPanel()
	elseif arg_8_0.mode == "Achievement" then
		arg_8_0:UpdateAchievementPanel()
	else
		arg_8_0.entranceIds = var_8_0.ids
	end

	arg_8_0._tf:GetComponent("DftAniEvent"):SetEndEvent(function(arg_9_0)
		local var_9_0 = {}

		_.each(arg_8_0.entranceIds, function(arg_10_0)
			var_9_0[arg_10_0] = true
		end)

		if #arg_8_0.entranceIds > 0 then
			arg_8_0.wsAtlasOverall:UpdateTargetEntrance(arg_8_0.entranceIds[1])
		end

		arg_8_0.wsAtlasOverall:UpdateStaticMark(var_9_0, arg_8_0:GetOverviewMark())
		arg_8_0:DisplayAtlasOverall()

		if arg_8_0.mode then
			setActive(arg_8_0["rt" .. arg_8_0.mode .. "Panel"], true)

			if arg_8_0.mode == "Task" then
				eachChild(arg_8_0.entranceItemList.container, function(arg_11_0)
					local var_11_0 = GetComponent(arg_11_0:Find("Text"), typeof(Typewriter))

					var_11_0:setSpeed(0.03)
					var_11_0:Play()
				end)

				local var_9_1 = arg_8_0.rtTaskPanel:Find("entrance_list/target_tpl")
				local var_9_2 = GetComponent(var_9_1:Find("Text"), typeof(Typewriter))

				var_9_2:setSpeed(0.03)
				var_9_2:Play()
			end
		end
	end)
end

function var_0_0.willExit(arg_12_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_12_0._tf, arg_12_0._parentTf)

	if arg_12_0.mode then
		setActive(arg_12_0["rt" .. arg_12_0.mode .. "Panel"], false)
	end

	arg_12_0:HideAtlasOverall()
	arg_12_0:DisposeAtlasOverall()
end

function var_0_0.GetOverviewMark(arg_13_0)
	if arg_13_0.mode == "Task" then
		if arg_13_0.isTaskArea then
			return {
				"overview_port"
			}
		else
			return {
				"overview_task_port",
				"overview_task"
			}
		end
	elseif arg_13_0.mode == "Achievement" then
		return {
			"overview_achievement",
			"overview_achievement"
		}
	else
		return {
			"overview_task_port",
			"overview_task"
		}
	end
end

function var_0_0.UpdateTaskPanel(arg_14_0)
	local var_14_0 = nowWorld()
	local var_14_1 = var_14_0:GetTaskProxy():getTaskById(arg_14_0.taskId)

	assert(var_14_1, "without this doing task: " .. arg_14_0.taskId)

	local var_14_2 = arg_14_0.rtTaskPanel:Find("task_info")

	GetImageSpriteFromAtlasAsync("ui/worldtaskfloatui_atlas", pg.WorldToastMgr.Type2PictrueName[var_14_1.config.type], var_14_2:Find("type"), true)
	setText(var_14_2:Find("name/Text"), var_14_1.config.name)

	local var_14_3 = var_14_1:GetFollowingAreaId()

	if var_14_3 then
		arg_14_0.isTaskArea = true
		arg_14_0.entranceIds = underscore.rest(var_14_0:GetAreaEntranceIds(var_14_3), 1)
		arg_14_0.areaIds = {
			var_14_3
		}

		arg_14_0.areaItemList:align(math.max(#arg_14_0.areaIds, 1))
	else
		arg_14_0.isTaskArea = false
		arg_14_0.entranceIds = {
			var_14_1:GetFollowingEntrance()
		}

		arg_14_0.entranceItemList:align(math.max(#arg_14_0.entranceIds, 1))
	end

	local var_14_4 = arg_14_0.rtTaskPanel:Find("entrance_list/target_tpl")
	local var_14_5 = var_14_0:GetActiveEntrance()

	setActive(var_14_4:Find("Image"), false)
	setText(var_14_4:Find("Text"), i18n("world_task_view2") .. var_14_5:GetBaseMap():GetName())
end

function var_0_0.UpdateAchievementPanel(arg_15_0)
	local var_15_0 = nowWorld()
	local var_15_1, var_15_2, var_15_3 = var_15_0:CountAchievements()

	setText(arg_15_0.rtAchievementPanel:Find("achievement_info/name/info/number"), var_15_1 + var_15_2 .. "/" .. var_15_3)

	local var_15_4, var_15_5 = var_15_0:GetFinishAchievements()
	local var_15_6 = 0

	for iter_15_0, iter_15_1 in ipairs(var_15_4) do
		var_15_6 = var_15_6 + #iter_15_1.star_list
	end

	local var_15_7 = arg_15_0.rtAchievementPanel:Find("word_list/target_tpl")

	setActive(var_15_7:Find("Image"), true)
	setText(var_15_7:Find("Text"), i18n("world_target_count", "  " .. setColorStr(tostring(var_15_6), COLOR_YELLOW) .. "  "))

	arg_15_0.entranceIds = var_15_5

	local var_15_8 = pg.gameset.world_target_obtain.key_value

	setActive(arg_15_0.btnAchieve, var_15_8 <= #var_15_4)
end

function var_0_0.DisplayAtlasOverall(arg_16_0)
	if arg_16_0.wsAtlasOverall then
		setActive(arg_16_0.wsAtlasOverall.tfEntity:Find("Plane"), false)
		arg_16_0.wsAtlasOverall:ShowOrHide(true)
	end
end

function var_0_0.HideAtlasOverall(arg_17_0)
	if arg_17_0.wsAtlasOverall then
		arg_17_0.wsAtlasOverall:ShowOrHide(false)
	end
end

function var_0_0.LoadAtlasOverall(arg_18_0, arg_18_1)
	local var_18_0 = {}

	if not arg_18_0.wsAtlasOverall then
		table.insert(var_18_0, function(arg_19_0)
			arg_18_0.wsAtlasOverall = WSAtlasOverall.New()

			arg_18_0.wsAtlasOverall:Setup()
			arg_18_0.wsAtlasOverall:LoadScene(function()
				arg_18_0.wsAtlasOverall:UpdateAtlas(nowWorld():GetAtlas())

				return arg_19_0()
			end)
		end)
	end

	seriesAsync(var_18_0, function()
		return existCall(arg_18_1)
	end)
end

function var_0_0.DisposeAtlasOverall(arg_22_0)
	if arg_22_0.wsAtlasOverall then
		arg_22_0.wsAtlasOverall:Dispose()

		arg_22_0.wsAtlasOverall = nil
	end
end

return var_0_0
