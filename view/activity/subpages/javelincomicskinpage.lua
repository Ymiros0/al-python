﻿local var_0_0 = class("JavelinComicSkinPage", import(".TemplatePage.SkinTemplatePage"))

var_0_0.FADE_OUT_TIME = 1

function var_0_0.OnFirstFlush(arg_1_0)
	arg_1_0:InitView()
	arg_1_0:RegisterEvent()
	var_0_0.super.OnFirstFlush(arg_1_0)
end

function var_0_0.InitView(arg_2_0)
	arg_2_0.animations = {}
	arg_2_0.puzzle = arg_2_0:findTF("Puzzle", arg_2_0.bg)
	arg_2_0.linkActId = arg_2_0:GetLinkId()
	arg_2_0.activityProxy = getProxy(ActivityProxy)
	arg_2_0.chargeIDList = Clone(arg_2_0.activityProxy:getActivityById(arg_2_0.linkActId).data1_list)
	arg_2_0.puzzleIDList = Clone(pg.activity_template[arg_2_0.linkActId].config_data)

	arg_2_0:CheckFinalAward()
end

function var_0_0.RegisterEvent(arg_3_0)
	arg_3_0.helpBtn = arg_3_0:findTF("HelpBtn", arg_3_0.bg)

	onButton(arg_3_0, arg_3_0.helpBtn, function()
		if pg.gametip.comic_help then
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = pg.gametip.comic_help.tip,
				weight = LayerWeightConst.TOP_LAYER
			})
		end
	end, SFX_PANEL)
end

function var_0_0.GetLinkId(arg_5_0)
	return pg.activity_const.JAVELIN_COMIC_PUZZLE_TASK.act_id
end

function var_0_0.OnUpdateFlush(arg_6_0)
	var_0_0.super.OnUpdateFlush(arg_6_0)

	arg_6_0.linkActivity = arg_6_0.activityProxy:getActivityById(arg_6_0.linkActId)

	local var_6_0 = true

	for iter_6_0 = 1, #arg_6_0.puzzleIDList do
		local var_6_1 = arg_6_0.puzzle:GetChild(iter_6_0 - 1)
		local var_6_2 = arg_6_0.puzzleIDList[iter_6_0]
		local var_6_3 = table.contains(arg_6_0.linkActivity.data1_list, var_6_2)

		arg_6_0:UpdatePuzzle(var_6_1, var_6_3, var_6_2)

		if not var_6_3 then
			var_6_0 = false
		end
	end

	arg_6_0:UpdateMainView(var_6_0)
end

function var_0_0.UpdatePuzzle(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
	if arg_7_2 and not table.contains(arg_7_0.chargeIDList, arg_7_3) then
		table.insert(arg_7_0.chargeIDList, arg_7_3)
		arg_7_0:DoPieceAnimation(arg_7_1, 0, 1, function()
			setActive(arg_7_1, arg_7_2)
			arg_7_0:CheckFinalAward()
		end)
	else
		setActive(arg_7_1, arg_7_2)
	end
end

function var_0_0.DoPieceAnimation(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4)
	if LeanTween.isTweening(arg_9_1) then
		LeanTween.cancel(go(arg_9_1), true)

		arg_9_0.animations[arg_9_1] = nil
	end

	arg_9_0.animations[arg_9_1] = true

	LeanTween.alpha(arg_9_1, arg_9_3, var_0_0.FADE_OUT_TIME):setFrom(arg_9_2):setOnComplete(System.Action(arg_9_4))
end

function var_0_0.UpdateMainView(arg_10_0, arg_10_1)
	local var_10_0

	if #arg_10_0.chargeIDList == #arg_10_0.taskGroup then
		var_10_0 = "<color=#00FF00><size=48>" .. #arg_10_0.chargeIDList .. "</size></color><color=#00B8FF><size=28>     " .. #arg_10_0.taskGroup .. "</size></color>"
	else
		var_10_0 = "<color=#E75198><size=48>" .. #arg_10_0.chargeIDList .. "</size></color><color=#00B8FF><size=28>     " .. #arg_10_0.taskGroup .. "</size></color>"
	end

	setText(arg_10_0.dayTF, var_10_0)
end

function var_0_0.OnDestroy(arg_11_0)
	var_0_0.super.OnDestroy(arg_11_0)

	for iter_11_0, iter_11_1 in pairs(arg_11_0.animations or {}) do
		if LeanTween.isTweening(iter_11_0.gameObject) then
			LeanTween.cancel(iter_11_0.gameObject)
		end
	end

	arg_11_0.animations = nil
end

function var_0_0.CheckFinalAward(arg_12_0)
	local var_12_0 = arg_12_0.activityProxy:getActivityById(arg_12_0.linkActId)

	if #var_12_0.data1_list == #arg_12_0.puzzleIDList then
		if var_12_0.data1 == 0 then
			arg_12_0:FetchFinalAward()
		else
			arg_12_0:OnFetchFinalAwardDone()
		end
	end
end

function var_0_0.FetchFinalAward(arg_13_0)
	arg_13_0:emit(ActivityMediator.EVENT_OPERATION, {
		cmd = 1,
		activity_id = arg_13_0.linkActId
	})
end

function var_0_0.OnFetchFinalAwardDone(arg_14_0)
	return
end

return var_0_0
