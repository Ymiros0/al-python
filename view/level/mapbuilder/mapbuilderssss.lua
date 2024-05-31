local var_0_0 = class("MapBuilderSSSS", import(".MapBuilderNormal"))
local var_0_1 = "ssss_buttons"

function var_0_0.preload(arg_1_0, arg_1_1)
	PoolMgr.GetInstance():GetUI(var_0_1, true, function(arg_2_0)
		arg_1_0.buttons = arg_2_0

		arg_1_1()
	end)
end

function var_0_0.GetType(arg_3_0)
	return MapBuilder.TYPESSSS
end

function var_0_0.OnInit(arg_4_0)
	var_0_0.super.OnInit(arg_4_0)

	arg_4_0.mainLayer = arg_4_0._parentTf:Find("main")
	arg_4_0.rightChapter = arg_4_0._parentTf:Find("main/right_chapter/event_btns/BottomList")
	arg_4_0.leftChapter = arg_4_0._parentTf:Find("main/left_chapter/buttons")
	arg_4_0.challengeBtn = tf(arg_4_0.buttons):Find("btn_challenge")
	arg_4_0.missionBtn = tf(arg_4_0.buttons):Find("btn_mission")

	onButton(arg_4_0, arg_4_0.challengeBtn, function()
		if arg_4_0:isfrozen() then
			return
		end

		arg_4_0:emit(LevelUIConst.SWITCH_CHALLENGE_MAP)
	end, SFX_PANEL)
	onButton(arg_4_0, arg_4_0.missionBtn, function()
		if arg_4_0:isfrozen() then
			return
		end

		arg_4_0:emit(LevelMediator2.ON_GO_TO_TASK_SCENE, {
			page = TaskScene.PAGE_TYPE_ACT
		})
	end, SFX_PANEL)
	setParent(arg_4_0.buttons, arg_4_0.mainLayer)
end

function var_0_0.ShowButtons(arg_7_0)
	var_0_0.super.ShowButtons(arg_7_0)
	setActive(arg_7_0.buttons, true)
	setParent(arg_7_0.challengeBtn, arg_7_0.leftChapter)
	arg_7_0.challengeBtn:SetSiblingIndex(5)
	setParent(arg_7_0.missionBtn, arg_7_0.rightChapter)
	arg_7_0.missionBtn:SetSiblingIndex(0)
end

function var_0_0.HideButtons(arg_8_0)
	setParent(arg_8_0.challengeBtn, arg_8_0.buttons)
	setParent(arg_8_0.missionBtn, arg_8_0.buttons)
	setActive(arg_8_0.buttons, false)
	var_0_0.super.HideButtons(arg_8_0)
end

local var_0_2 = {
	18993,
	18994,
	18995,
	18996,
	18997
}

function var_0_0.UpdateButtons(arg_9_0)
	var_0_0.super.UpdateButtons(arg_9_0)

	local var_9_0 = arg_9_0.data:getConfig("type")

	setActive(arg_9_0.sceneParent.actEliteBtn, false)
	setActive(arg_9_0.challengeBtn, var_9_0 ~= Map.ACTIVITY_HARD)
	setActive(arg_9_0.missionBtn, var_9_0 == Map.ACTIVITY_HARD)

	if var_9_0 == Map.ACTIVITY_HARD then
		local var_9_1 = _.any(var_0_2, function(arg_10_0)
			local var_10_0 = getProxy(TaskProxy):getTaskById(arg_10_0)

			return tobool(var_10_0)
		end)

		setActive(arg_9_0.missionBtn, var_9_1)

		if var_9_1 then
			setActive(arg_9_0.missionBtn:Find("Tip"), _.any(var_0_2, function(arg_11_0)
				local var_11_0 = getProxy(TaskProxy):getTaskById(arg_11_0)

				return var_11_0 and var_11_0:isFinish()
			end))
		end
	end
end

function var_0_0.OnDestroy(arg_12_0)
	PoolMgr.GetInstance():ReturnUI(var_0_1, arg_12_0.buttons)
	var_0_0.super.OnDestroy(arg_12_0)
end

return var_0_0
