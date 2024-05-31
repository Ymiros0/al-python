local var_0_0 = class("MiniGameTemplateView", import("view.miniGame.BaseMiniGameView"))

var_0_0.canSelectStage = true

function var_0_0.getUIName(arg_1_0)
	return nil
end

function var_0_0.getGameController(arg_2_0)
	return nil
end

function var_0_0.getShowSide(arg_3_0)
	return true
end

function var_0_0.updateMainUI(arg_4_0)
	if arg_4_0:getShowSide() then
		local var_4_0 = arg_4_0:GetMGHubData()
		local var_4_1 = var_4_0:getConfig("reward_need")
		local var_4_2 = var_4_0.usedtime
		local var_4_3 = var_4_2 + var_4_0.count
		local var_4_4 = math.min(var_4_0.usedtime + 1, var_4_3)
		local var_4_5 = arg_4_0.itemList.container
		local var_4_6 = var_4_5.childCount

		for iter_4_0 = 1, var_4_6 do
			local var_4_7 = {}

			if iter_4_0 <= var_4_2 then
				var_4_7.finish = true
			elseif iter_4_0 <= var_4_3 then
				-- block empty
			else
				var_4_7.lock = true
			end

			local var_4_8 = var_4_5:GetChild(iter_4_0 - 1)

			setActive(var_4_8:Find("finish"), var_4_7.finish)
			setActive(var_4_8:Find("lock"), var_4_7.lock)
			setToggleEnabled(var_4_8, arg_4_0.canSelectStage and iter_4_0 <= var_4_4)
			triggerToggle(var_4_8, iter_4_0 == var_4_4)
		end

		local var_4_9 = var_4_5:GetChild(0).anchoredPosition.y - var_4_5:GetChild(var_4_4 - 1).anchoredPosition.y
		local var_4_10 = var_4_5.rect.height
		local var_4_11 = var_4_5:GetComponent(typeof(ScrollRect)).viewport.rect.height
		local var_4_12 = math.clamp(var_4_9, 0, var_4_10 - var_4_11) / (var_4_10 - var_4_11)

		scrollTo(var_4_5, nil, 1 - var_4_12)
	end

	arg_4_0:checkGet()
end

function var_0_0.checkGet(arg_5_0)
	local var_5_0 = arg_5_0:GetMGHubData()

	if var_5_0.ultimate == 0 then
		if var_5_0.usedtime < var_5_0:getConfig("reward_need") then
			return
		end

		pg.m02:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_5_0.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
	end
end

function var_0_0.initPageUI(arg_6_0)
	arg_6_0.rtTitlePage = arg_6_0._tf:Find("TitlePage")

	local var_6_0 = arg_6_0.rtTitlePage:Find("main")

	onButton(arg_6_0, var_6_0:Find("btn_back"), function()
		arg_6_0:closeView()
	end, SFX_CANCEL)
	onButton(arg_6_0, var_6_0:Find("btn_help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip["2023spring_minigame_help"].tip
		})
	end, SFX_PANEL)

	local var_6_1 = arg_6_0:GetMGData():GetSimpleValue("story")

	onButton(arg_6_0, var_6_0:Find("btn_start"), function()
		local var_9_0 = {}
		local var_9_1 = checkExist(var_6_1, {
			arg_6_0.stageIndex
		}, {
			1
		})

		if var_9_1 then
			table.insert(var_9_0, function(arg_10_0)
				pg.NewStoryMgr.GetInstance():Play(var_9_1, arg_10_0)
			end)
		end

		seriesAsync(var_9_0, function()
			arg_6_0:openUI("countdown")
		end)
	end, SFX_PANEL)

	arg_6_0.stageIndex = 0

	if arg_6_0:getShowSide() then
		local var_6_2 = pg.mini_game[arg_6_0:GetMGData().id].simple_config_data.drop
		local var_6_3 = var_6_0:Find("side_panel/award/content")

		arg_6_0.itemList = UIItemList.New(var_6_3, var_6_3:GetChild(0))

		arg_6_0.itemList:make(function(arg_12_0, arg_12_1, arg_12_2)
			arg_12_1 = arg_12_1 + 1

			if arg_12_0 == UIItemList.EventUpdate then
				local var_12_0 = arg_12_2:Find("IconTpl")
				local var_12_1 = {}

				var_12_1.type, var_12_1.id, var_12_1.count = unpack(var_6_2[arg_12_1])

				updateDrop(var_12_0, var_12_1)
				onButton(arg_6_0, var_12_0, function()
					arg_6_0:emit(var_0_0.ON_DROP, var_12_1)
				end, SFX_PANEL)
				onToggle(arg_6_0, arg_12_2, function(arg_14_0)
					if arg_14_0 then
						arg_6_0.stageIndex = arg_12_1
					end
				end)
			end
		end)
		arg_6_0.itemList:align(#var_6_2)
	end

	arg_6_0.rtTitlePage:Find("countdown"):Find("bg/Image"):GetComponent(typeof(DftAniEvent)):SetEndEvent(function()
		arg_6_0:openUI()
		arg_6_0.gameController:StartGame()
	end)

	local var_6_4 = arg_6_0.rtTitlePage:Find("pause")

	onButton(arg_6_0, var_6_4:Find("window/btn_confirm"), function()
		arg_6_0:openUI()
		arg_6_0.gameController:ResumeGame()
	end, SFX_CONFIRM)

	local var_6_5 = arg_6_0.rtTitlePage:Find("exit")

	onButton(arg_6_0, var_6_5:Find("window/btn_cancel"), function()
		arg_6_0:openUI()
		arg_6_0.gameController:ResumeGame()
	end, SFX_CANCEL)
	onButton(arg_6_0, var_6_5:Find("window/btn_confirm"), function()
		arg_6_0:openUI()
		arg_6_0.gameController:EndGame()
	end, SFX_CONFIRM)

	local var_6_6 = arg_6_0.rtTitlePage:Find("result")

	onButton(arg_6_0, var_6_6:Find("window/btn_finish"), function()
		arg_6_0:openUI("main")
	end, SFX_CONFIRM)
end

function var_0_0.initControllerUI(arg_20_0)
	local var_20_0 = arg_20_0._tf:Find("Controller/top")

	onButton(arg_20_0, var_20_0:Find("btn_back"), function()
		arg_20_0:openUI("exit")
	end, SFX_PANEL)
	onButton(arg_20_0, var_20_0:Find("btn_pause"), function()
		arg_20_0:openUI("pause")
	end)
end

function var_0_0.SaveDataChange(arg_23_0, arg_23_1)
	arg_23_0:StoreDataToServer(arg_23_1)
end

function var_0_0.didEnter(arg_24_0)
	arg_24_0:initPageUI()
	arg_24_0:initControllerUI()

	arg_24_0.gameController = arg_24_0:getGameController().New(arg_24_0, arg_24_0._tf)

	arg_24_0:openUI("main")
end

function var_0_0.initOpenUISwich(arg_25_0)
	arg_25_0.openSwitchDic = {
		main = function()
			arg_25_0:updateMainUI()
		end,
		pause = function()
			arg_25_0.gameController:PauseGame()
		end,
		exit = function()
			arg_25_0.gameController:PauseGame()
		end,
		result = function()
			local var_29_0 = arg_25_0:GetMGData():GetRuntimeData("elements") or {}
			local var_29_1 = arg_25_0.gameController.point
			local var_29_2 = var_29_0[1] or 0
			local var_29_3 = arg_25_0.rtTitlePage:Find("result")

			setActive(var_29_3:Find("window/now/new"), var_29_2 < var_29_1)

			if var_29_2 <= var_29_1 then
				var_29_2 = var_29_1
				var_29_0[1] = var_29_1
			end

			arg_25_0:SaveDataChange(var_29_0)
			setText(var_29_3:Find("window/high/Text"), var_29_2)
			setText(var_29_3:Find("window/now/Text"), var_29_1)

			local var_29_4 = arg_25_0:GetMGHubData()

			if (not arg_25_0:getShowSide() or arg_25_0.stageIndex == var_29_4.usedtime + 1) and var_29_4.count > 0 then
				arg_25_0:SendSuccess(0)
			end
		end
	}
end

function var_0_0.openUI(arg_30_0, arg_30_1)
	if not arg_30_0.openSwitchDic then
		arg_30_0:initOpenUISwich()
	end

	if arg_30_0.status then
		setActive(arg_30_0.rtTitlePage:Find(arg_30_0.status), false)
	end

	if arg_30_1 then
		setActive(arg_30_0.rtTitlePage:Find(arg_30_1), true)
	end

	arg_30_0.status = arg_30_1

	switch(arg_30_1, arg_30_0.openSwitchDic)
end

function var_0_0.initBackPressSwitch(arg_31_0)
	arg_31_0.backPressSwitchDic = {
		main = function()
			var_0_0.super.onBackPressed(arg_31_0)
		end,
		countdown = function()
			return
		end,
		pause = function()
			arg_31_0:openUI()
			arg_31_0.gameController:ResumeGame()
		end,
		exit = function()
			arg_31_0:openUI()
			arg_31_0.gameController:ResumeGame()
		end,
		result = function()
			return
		end
	}
end

function var_0_0.onBackPressed(arg_37_0)
	if not arg_37_0.backPressSwitchDic then
		arg_37_0:initBackPressSwitch()
	end

	switch(arg_37_0.status, arg_37_0.backPressSwitchDic, function()
		assert(arg_37_0.gameController.isStart)
		arg_37_0:openUI("pause")
	end)
end

function var_0_0.willExit(arg_39_0)
	return
end

return var_0_0
