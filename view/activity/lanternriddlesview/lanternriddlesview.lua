﻿local var_0_0 = class("LanternRiddlesView")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.controller = arg_1_1

	pg.DelegateInfo.New(arg_1_0)
end

function var_0_0.SetUI(arg_2_0, arg_2_1)
	arg_2_0._tf = arg_2_1
	arg_2_0.questioneTFs = {}

	for iter_2_0, iter_2_1 in ipairs(pg.activity_event_question.all) do
		local var_2_0 = arg_2_0:findTF("labels/label" .. iter_2_0)

		arg_2_0.questioneTFs[iter_2_1] = var_2_0
	end

	arg_2_0.mainPanel = arg_2_0:findTF("main")
	arg_2_0.day = arg_2_0:findTF("time/Text"):GetComponent(typeof(Text))
	arg_2_0:findTF("frame/time", arg_2_0.mainPanel):GetComponent(typeof(Text)).text = i18n("LanternRiddle_wait_time_tip")

	setActive(arg_2_0.mainPanel, false)
	onButton(arg_2_0, arg_2_0.mainPanel, function()
		arg_2_0:HideMainPanel()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0:findTF("back"), function()
		arg_2_0.controller:ExitGame()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0:findTF("back/help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.lanternRiddles_gametip.tip
		})
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0:findTF("option"), function()
		arg_2_0.controller:ExitGameAndGoHome()
	end, SFX_PANEL)
end

function var_0_0.UpdateDay(arg_7_0, arg_7_1)
	local var_7_0 = math.min(arg_7_1, 7)

	arg_7_0.day.text = var_7_0
end

function var_0_0.InitLanternRiddles(arg_8_0, arg_8_1)
	for iter_8_0, iter_8_1 in ipairs(arg_8_1) do
		local var_8_0 = arg_8_0.questioneTFs[iter_8_1.id]
		local var_8_1 = iter_8_1.isUnlock

		onButton(arg_8_0, var_8_0, function()
			if not var_8_1 then
				return
			end

			arg_8_0:ShowMainPanel(iter_8_1)
		end, SFX_PANEL)
		setActive(var_8_0:Find("finish"), iter_8_1.isFinish)

		if LeanTween.isTweening(go(var_8_0)) then
			LeanTween.cancel(go(var_8_0))
		end

		local var_8_2 = var_8_0:Find("image")

		if var_8_1 and not iter_8_1.isFinish then
			LeanTween.rotateZ(go(var_8_0), 10, 2):setLoopPingPong(0):setFrom(0)
		end

		setActive(var_8_2, var_8_1)
	end
end

function var_0_0.RefreshLanterRiddles(arg_10_0, arg_10_1)
	arg_10_0:InitLanternRiddles(arg_10_1)
end

function var_0_0.ShowMainPanel(arg_11_0, arg_11_1)
	pg.UIMgr.GetInstance():BlurPanel(arg_11_0.mainPanel)
	setActive(arg_11_0.mainPanel, true)
	setActive(arg_11_0:findTF("frame/label_game", arg_11_0.mainPanel), arg_11_1.type == 2)
	setActive(arg_11_0:findTF("frame/label_his", arg_11_0.mainPanel), arg_11_1.type == 1)
	setText(arg_11_0:findTF("frame/Text", arg_11_0.mainPanel), arg_11_1.text)
	arg_11_0:UpdateMainPanelTime()

	local var_11_0 = arg_11_1.answers
	local var_11_1 = arg_11_0:findTF("frame/answers", arg_11_0.mainPanel)
	local var_11_2 = arg_11_1.isFinish

	for iter_11_0 = 1, 4 do
		local var_11_3 = var_11_0[iter_11_0][1]
		local var_11_4 = var_11_0[iter_11_0][2]
		local var_11_5 = var_11_1:GetChild(iter_11_0 - 1)

		setText(var_11_5:Find("Text"), var_11_3)
		setActive(var_11_5:Find("right"), var_11_2 and iter_11_0 == arg_11_1.rightIndex)
		setActive(var_11_5:Find("false"), var_11_4)
		onButton(arg_11_0, var_11_5, function()
			if arg_11_1.isFinish then
				return
			end

			if var_11_4 then
				return
			end

			if pg.TimeMgr.GetInstance():GetServerTime() < arg_11_0.controller:GetLockTime() then
				pg.TipsMgr.GetInstance():ShowTips(i18n("lanternRiddles_wait_for_reanswer"))

				return
			end

			arg_11_0.controller:SelectAnswer(arg_11_1.id, iter_11_0)
		end, SFX_PANEL)
	end
end

function var_0_0.UpdateMainPanelTime(arg_13_0)
	arg_13_0:RemoveTimer()

	local var_13_0 = pg.TimeMgr.GetInstance():GetServerTime() <= arg_13_0.controller:GetLockTime()

	setActive(arg_13_0:findTF("frame/time", arg_13_0.mainPanel), var_13_0)

	if var_13_0 then
		arg_13_0:AddTimer()
	end
end

function var_0_0.OnUpdateAnswer(arg_14_0, arg_14_1, arg_14_2, arg_14_3)
	local var_14_0 = arg_14_0:findTF("frame/answers", arg_14_0.mainPanel):GetChild(arg_14_2 - 1)

	setActive(var_14_0:Find("right"), arg_14_3)
	setActive(var_14_0:Find("false"), not arg_14_3)

	if not arg_14_3 then
		arg_14_0:UpdateMainPanelTime()
		pg.TipsMgr.GetInstance():ShowTips(i18n("lanternRiddles_answer_is_wrong"))
	else
		pg.TipsMgr.GetInstance():ShowTips(i18n("lanternRiddles_answer_is_right"))

		local var_14_1 = arg_14_0.questioneTFs[arg_14_1.id]

		setActive(var_14_1:Find("finish"), arg_14_1.isFinish)

		if LeanTween.isTweening(go(var_14_1)) then
			LeanTween.cancel(go(var_14_1))
		end
	end
end

function var_0_0.HideMainPanel(arg_15_0)
	arg_15_0:RemoveTimer()
	setActive(arg_15_0.mainPanel, false)
	pg.UIMgr.GetInstance():UnblurPanel(arg_15_0.mainPanel, arg_15_0._tf)
end

function var_0_0.AddTimer(arg_16_0)
	local var_16_0 = arg_16_0.controller:GetLockTime()
	local var_16_1 = arg_16_0:findTF("frame/time/Text", arg_16_0.mainPanel):GetComponent(typeof(Text))

	arg_16_0.timer = Timer.New(function()
		local var_17_0 = pg.TimeMgr.GetInstance():GetServerTime()
		local var_17_1 = var_16_0 - var_17_0

		if var_17_1 <= 0 then
			arg_16_0:RemoveTimer()
			setActive(arg_16_0:findTF("frame/time", arg_16_0.mainPanel), false)
		else
			var_16_1.text = pg.TimeMgr.GetInstance():DescCDTime(var_17_1)
		end
	end, 1, -1)

	arg_16_0.timer:Start()
	arg_16_0.timer.func()
end

function var_0_0.RemoveTimer(arg_18_0)
	if arg_18_0.timer then
		arg_18_0.timer:Stop()

		arg_18_0.timer = nil
	end
end

function var_0_0.Dispose(arg_19_0)
	arg_19_0:RemoveTimer()
	arg_19_0:HideMainPanel()
	pg.DelegateInfo.Dispose(arg_19_0)
end

function var_0_0.findTF(arg_20_0, arg_20_1, arg_20_2)
	assert(arg_20_0._tf, "transform should exist")

	return findTF(arg_20_2 or arg_20_0._tf, arg_20_1)
end

return var_0_0
