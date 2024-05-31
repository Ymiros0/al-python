local var_0_0 = class("NenjuuMiniGameView", import("view.miniGame.BaseMiniGameView"))

function var_0_0.getUIName(arg_1_0)
	return "NenjuuMiniGameUI"
end

function var_0_0.openUI(arg_2_0, arg_2_1)
	if arg_2_0.status then
		setActive(arg_2_0.rtTitlePage:Find(arg_2_0.status), false)
	end

	if arg_2_1 then
		setActive(arg_2_0.rtTitlePage:Find(arg_2_1), true)
	end

	arg_2_0.status = arg_2_1

	switch(arg_2_1, {
		main = function()
			arg_2_0:updateMainUI()
		end,
		pause = function()
			arg_2_0.gameController:PauseGame()
		end,
		exit = function()
			arg_2_0.gameController:PauseGame()
		end,
		result = function()
			local var_6_0 = NenjuuGameConfig.ParsingElements(arg_2_0:GetMGData():GetRuntimeData("elements") or {})
			local var_6_1 = arg_2_0.gameController.point
			local var_6_2 = var_6_0.high
			local var_6_3 = arg_2_0.rtTitlePage:Find("result")

			setActive(var_6_3:Find("window/now/new"), var_6_2 < var_6_1)

			if var_6_2 <= var_6_1 then
				var_6_2 = var_6_1
				var_6_0.high = var_6_1
			end

			var_6_0.count = var_6_0.count + var_6_1

			arg_2_0:SaveDataChange(var_6_0)
			setText(var_6_3:Find("window/high/Text"), var_6_2)
			setText(var_6_3:Find("window/now/Text"), var_6_1)

			local var_6_4 = arg_2_0:GetMGHubData()

			if arg_2_0.stageIndex == var_6_4.usedtime + 1 and var_6_4.count > 0 then
				arg_2_0:SendSuccess(0)
			end
		end
	})
end

function var_0_0.updateMainUI(arg_7_0)
	local var_7_0 = arg_7_0:GetMGHubData()
	local var_7_1 = var_7_0:getConfig("reward_need")
	local var_7_2 = var_7_0.usedtime
	local var_7_3 = var_7_2 + var_7_0.count
	local var_7_4 = math.min(var_7_0.usedtime + 1, var_7_3)
	local var_7_5 = arg_7_0.itemList.container
	local var_7_6 = var_7_5.childCount

	for iter_7_0 = 1, var_7_6 do
		local var_7_7 = {}

		if iter_7_0 <= var_7_2 then
			var_7_7.finish = true
		elseif iter_7_0 <= var_7_3 then
			-- block empty
		else
			var_7_7.lock = true
		end

		local var_7_8 = var_7_5:GetChild(iter_7_0 - 1)

		setActive(var_7_8:Find("finish"), var_7_7.finish)
		setActive(var_7_8:Find("lock"), var_7_7.lock)
		setToggleEnabled(var_7_8, iter_7_0 <= var_7_4)
		triggerToggle(var_7_8, iter_7_0 == var_7_4)
	end

	local var_7_9 = var_7_5:GetChild(0).anchoredPosition.y - var_7_5:GetChild(var_7_4 - 1).anchoredPosition.y
	local var_7_10 = var_7_5.rect.height
	local var_7_11 = var_7_5:GetComponent(typeof(ScrollRect)).viewport.rect.height
	local var_7_12 = math.clamp(var_7_9, 0, var_7_10 - var_7_11) / (var_7_10 - var_7_11)

	scrollTo(var_7_5, nil, 1 - var_7_12)
	arg_7_0:checkGet()
end

function var_0_0.checkGet(arg_8_0)
	local var_8_0 = arg_8_0:GetMGHubData()

	if var_8_0.ultimate == 0 then
		if var_8_0.usedtime < var_8_0:getConfig("reward_need") then
			return
		end

		pg.m02:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_8_0.id,
			cmd = MiniGameOPCommand.CMD_ULTIMATE,
			args1 = {}
		})
	end
end

function var_0_0.initPageUI(arg_9_0)
	arg_9_0.rtTitlePage = arg_9_0._tf:Find("TitlePage")

	local var_9_0 = arg_9_0.rtTitlePage:Find("main")

	onButton(arg_9_0, var_9_0:Find("btn_back"), function()
		arg_9_0:closeView()
	end, SFX_CANCEL)
	onButton(arg_9_0, var_9_0:Find("btn_help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip["2023spring_minigame_help"].tip
		})
	end, SFX_PANEL)
	onButton(arg_9_0, var_9_0:Find("btn_opreation"), function()
		setActive(arg_9_0.rtLevel:Find("Opreation"), true)
		arg_9_0:UpdateOpreationPage(1)
	end, SFX_PANEL)

	local var_9_1 = arg_9_0:GetMGData():GetSimpleValue("story")

	onButton(arg_9_0, var_9_0:Find("btn_start"), function()
		local var_13_0 = {}
		local var_13_1 = checkExist(var_9_1, {
			arg_9_0.stageIndex
		}, {
			1
		})

		if var_13_1 then
			table.insert(var_13_0, function(arg_14_0)
				pg.NewStoryMgr.GetInstance():Play(var_13_1, arg_14_0)
			end)
		end

		seriesAsync(var_13_0, function()
			arg_9_0:openReadyPage()
		end)
	end, SFX_PANEL)

	arg_9_0.stageIndex = 0

	local var_9_2 = pg.mini_game[arg_9_0:GetMGData().id].simple_config_data.drop
	local var_9_3 = var_9_0:Find("side_panel/award/content")

	arg_9_0.itemList = UIItemList.New(var_9_3, var_9_3:GetChild(0))

	arg_9_0.itemList:make(function(arg_16_0, arg_16_1, arg_16_2)
		arg_16_1 = arg_16_1 + 1

		if arg_16_0 == UIItemList.EventUpdate then
			local var_16_0 = arg_16_2:Find("IconTpl")
			local var_16_1 = {}

			var_16_1.type, var_16_1.id, var_16_1.count = unpack(var_9_2[arg_16_1])

			updateDrop(var_16_0, var_16_1)
			onButton(arg_9_0, var_16_0, function()
				arg_9_0:emit(var_0_0.ON_DROP, var_16_1)
			end, SFX_PANEL)
			onToggle(arg_9_0, arg_16_2, function(arg_18_0)
				if arg_18_0 then
					arg_9_0.stageIndex = arg_16_1
				end
			end)
		end
	end)
	arg_9_0.itemList:align(#var_9_2)
	arg_9_0.rtTitlePage:Find("countdown"):Find("bg/Image"):GetComponent(typeof(DftAniEvent)):SetEndEvent(function()
		arg_9_0:openUI()
		arg_9_0.gameController:StartGame()
	end)

	local var_9_4 = arg_9_0.rtTitlePage:Find("pause")

	onButton(arg_9_0, var_9_4:Find("window/btn_confirm"), function()
		arg_9_0:openUI()
		arg_9_0.gameController:ResumeGame()
	end, SFX_CONFIRM)

	local var_9_5 = arg_9_0.rtTitlePage:Find("exit")

	onButton(arg_9_0, var_9_5:Find("window/btn_cancel"), function()
		arg_9_0:openUI()
		arg_9_0.gameController:ResumeGame()
	end, SFX_CANCEL)
	onButton(arg_9_0, var_9_5:Find("window/btn_confirm"), function()
		arg_9_0:openUI()
		arg_9_0.gameController:EndGame()
	end, SFX_CONFIRM)

	local var_9_6 = arg_9_0.rtTitlePage:Find("result")

	onButton(arg_9_0, var_9_6:Find("window/btn_finish"), function()
		arg_9_0:openUI("main")
	end, SFX_CONFIRM)
end

function var_0_0.initLeveUI(arg_24_0)
	arg_24_0.rtLevel = arg_24_0._tf:Find("LevelPage")

	local var_24_0 = arg_24_0.rtLevel:Find("Opreation")

	onButton(arg_24_0, var_24_0:Find("btn_back"), function()
		setActive(var_24_0, false)
	end, SFX_CANCEL)
end

local var_0_1 = {
	bomb = {
		"2023spring_minigame_item_firecracker"
	},
	lantern = {
		"2023spring_minigame_item_lantern"
	},
	ice = {
		"2023spring_minigame_skill_icewall",
		"2023spring_minigame_skill_icewall_up"
	},
	flash = {
		"2023spring_minigame_skill_flash",
		"2023spring_minigame_skill_flash_up"
	},
	rush = {
		"2023spring_minigame_skill_sprint",
		"2023spring_minigame_skill_sprint_up"
	},
	blessing = {
		"2023spring_minigame_bless_speed",
		"2023spring_minigame_bless_speed_up"
	},
	decoy = {
		"2023spring_minigame_bless_substitute",
		"2023spring_minigame_bless_substitute_up"
	}
}

function var_0_0.UpdateOpreationPage(arg_26_0, arg_26_1)
	local var_26_0 = arg_26_0.rtLevel:Find("Opreation")
	local var_26_1 = NenjuuGameConfig.ParsingElements(arg_26_0:GetMGData():GetRuntimeData("elements") or {})

	setText(var_26_0:Find("point/Text"), var_26_1.count)

	local var_26_2 = {
		{
			"bomb",
			"lantern"
		},
		{
			"ice",
			"flash",
			"rush"
		},
		{
			"blessing",
			"decoy"
		}
	}
	local var_26_3
	local var_26_4 = var_26_0:Find("main/view/content")
	local var_26_5 = UIItemList.New(var_26_4, var_26_4:Find("tpl"))

	var_26_5:make(function(arg_27_0, arg_27_1, arg_27_2)
		arg_27_1 = arg_27_1 + 1

		if arg_27_0 == UIItemList.EventUpdate then
			local var_27_0 = var_26_3[arg_27_1]

			setActive(arg_27_2:Find("empty"), not var_27_0)
			setActive(arg_27_2:Find("info"), var_27_0)

			if var_27_0 then
				local var_27_1 = arg_27_2:Find("info")

				eachChild(var_27_1:Find("icon"), function(arg_28_0)
					setActive(arg_28_0, arg_28_0.name == var_27_0)
				end)

				local var_27_2 = string.split(i18n(var_0_1[var_27_0][1]), "|")

				setText(var_27_1:Find("name/Text"), var_27_2[1])
				setText(var_27_1:Find("desc"), var_27_2[2])
				setActive(var_27_1:Find("level"), var_0_1[var_27_0][2])

				if var_0_1[var_27_0][2] then
					local var_27_3 = string.split(i18n(var_0_1[var_27_0][2]), "|")

					for iter_27_0 = 1, 3 do
						local var_27_4 = var_27_1:Find("level/" .. iter_27_0)

						setActive(var_27_4, var_27_3[iter_27_0])

						if var_27_3[iter_27_0] then
							setTextColor(var_27_4:Find("Text"), Color.NewHex(iter_27_0 > var_26_1.level[var_27_0] and "8D90AFFF" or "535885FF"))
							changeToScrollText(var_27_4:Find("info"), setColorStr(var_27_3[iter_27_0], iter_27_0 > var_26_1.level[var_27_0] and "#8D90AFFF" or "#535885FF"))
						end
					end
				end

				eachChild(var_27_1:Find("status"), function(arg_29_0)
					setActive(arg_29_0, false)
				end)
				onButton(arg_26_0, var_27_1:Find("status/btn_equip"), function()
					var_26_1.item = var_27_0

					arg_26_0:SaveDataChange(var_26_1)
					arg_26_0:UpdateOpreationPage(arg_26_1)
				end, SFX_CONFIRM)
				onButton(arg_26_0, var_27_1:Find("status/btn_unlock"), function()
					var_26_1.count = var_26_1.count - NenjuuGameConfig.SKILL_LEVEL_CONFIG[var_27_0].cost[var_26_1.level[var_27_0] + 1]
					var_26_1.level[var_27_0] = var_26_1.level[var_27_0] + 1

					if var_26_1.level[var_27_0] > 1 then
						pg.TipsMgr.GetInstance():ShowTips(i18n("2023spring_minigame_tip7", var_27_2[1]))
					else
						pg.TipsMgr.GetInstance():ShowTips(i18n("2023spring_minigame_tip6", var_27_2[1]))
					end

					arg_26_0:SaveDataChange(var_26_1)
					arg_26_0:UpdateOpreationPage(arg_26_1)
				end, SFX_CONFIRM)

				if var_26_1.level[var_27_0] < #NenjuuGameConfig.SKILL_LEVEL_CONFIG[var_27_0].cost then
					local var_27_5 = NenjuuGameConfig.SKILL_LEVEL_CONFIG[var_27_0].cost[var_26_1.level[var_27_0] + 1]

					if var_27_5 > var_26_1.count then
						setText(var_27_1:Find("status/btn_lock/point"), var_27_5)
						setText(var_27_1:Find("status/btn_lock/Text"), i18n("2023spring_minigame_tip3"))
						setActive(var_27_1:Find("status/btn_lock"), true)
					else
						setText(var_27_1:Find("status/btn_unlock/point"), var_27_5)
						setText(var_27_1:Find("status/btn_unlock/Text"), i18n("2023spring_minigame_tip3"))
						setActive(var_27_1:Find("status/btn_unlock"), true)
					end
				elseif var_27_0 == "bomb" or var_27_0 == "lantern" then
					setText(var_27_1:Find("status/btn_equip/Text"), i18n("2023spring_minigame_tip1"))
					setActive(var_27_1:Find("status/btn_equip"), var_26_1.item ~= var_27_0)
					setText(var_27_1:Find("status/btn_in/Text"), i18n("2023spring_minigame_tip2"))
					setActive(var_27_1:Find("status/btn_in"), var_26_1.item == var_27_0)
				else
					setActive(var_27_1:Find("status/unlock"), true)
				end
			end
		end
	end)

	for iter_26_0, iter_26_1 in ipairs(var_26_2) do
		onToggle(arg_26_0, var_26_0:Find("toggles/" .. iter_26_0), function(arg_32_0)
			arg_26_1 = iter_26_0
			var_26_3 = iter_26_1

			var_26_5:align(4)
			setActive(var_26_0:Find("main/tip"), iter_26_0 == 1)
		end, SFX_PANEL)
	end

	triggerToggle(var_26_0:Find("toggles/" .. arg_26_1), true)
end

local function var_0_2(arg_33_0, arg_33_1, arg_33_2)
	for iter_33_0, iter_33_1 in ipairs(NenjuuGameConfig.ABILITY_LIST) do
		if arg_33_0[iter_33_1] then
			arg_33_1 = arg_33_1 + arg_33_2[iter_33_1]
		end
	end

	return arg_33_1
end

function var_0_0.openReadyPage(arg_34_0)
	local var_34_0 = NenjuuGameConfig.ParsingElements(arg_34_0:GetMGData():GetRuntimeData("elements") or {})
	local var_34_1 = NenjuuGameConfig.GetStageConfig("Spring23Level_" .. arg_34_0.stageIndex)

	if not arg_34_0.abilityCache[arg_34_0.stageIndex] then
		arg_34_0.abilityCache[arg_34_0.stageIndex] = setmetatable({}, {
			__index = var_34_1.ability_config
		})
	end

	setActive(arg_34_0.rtLevel:Find("Ready"), true)
	onButton(arg_34_0, arg_34_0.rtLevel:Find("Ready/bg"), function()
		setActive(arg_34_0.rtLevel:Find("Ready"), false)
	end, SFX_CANCEL)

	local var_34_2 = arg_34_0.rtLevel:Find("Ready/main")

	eachChild(var_34_2:Find("title"), function(arg_36_0)
		setActive(arg_36_0, arg_36_0.name == tostring(arg_34_0.stageIndex))
	end)
	setText(var_34_2:Find("rate/Image/Text"), var_0_2(arg_34_0.abilityCache[arg_34_0.stageIndex], var_34_1.base_rate, var_34_1.ability_rate))
	setText(var_34_2:Find("high/Image/Text"), var_34_0["stage_" .. arg_34_0.stageIndex])
	setText(var_34_2:Find("ability_text/Text"), i18n("2023spring_minigame_tip5"))

	local var_34_3 = underscore.filter(NenjuuGameConfig.ABILITY_LIST, function(arg_37_0)
		return arg_34_0.abilityCache[arg_34_0.stageIndex][arg_37_0]
	end)
	local var_34_4 = UIItemList.New(var_34_2:Find("abilitys"), var_34_2:Find("abilitys/tpl"))

	var_34_4:make(function(arg_38_0, arg_38_1, arg_38_2)
		arg_38_1 = arg_38_1 + 1

		if arg_38_0 == UIItemList.EventUpdate then
			setActive(arg_38_2:Find("empty"), not var_34_3[arg_38_1])
			setActive(arg_38_2:Find("enable"), var_34_3[arg_38_1])

			if var_34_3[arg_38_1] then
				eachChild(arg_38_2:Find("enable"), function(arg_39_0)
					setActive(arg_39_0, arg_39_0.name == var_34_3[arg_38_1])
				end)
			end
		end
	end)
	var_34_4:align(#NenjuuGameConfig.ABILITY_LIST)
	onButton(arg_34_0, var_34_2:Find("btn_rate"), function()
		setActive(arg_34_0.rtLevel:Find("Ready"), false)
		arg_34_0:openRatePage()
	end, SFX_PANEL)
	onButton(arg_34_0, var_34_2:Find("btn_continue"), function()
		setActive(arg_34_0.rtLevel:Find("Ready"), false)
		arg_34_0.gameController:ResetGame()
		arg_34_0.gameController:ReadyGame({
			index = arg_34_0.stageIndex,
			FuShun = NenjuuGameConfig.ParsingElements(arg_34_0:GetMGData():GetRuntimeData("elements") or {}),
			Nenjuu = arg_34_0.abilityCache[arg_34_0.stageIndex],
			rate = var_0_2(arg_34_0.abilityCache[arg_34_0.stageIndex], var_34_1.base_rate, var_34_1.ability_rate)
		})
		arg_34_0:openUI("countdown")
	end, SFX_CONFIRM)
end

function var_0_0.openRatePage(arg_42_0)
	local var_42_0 = NenjuuGameConfig.ParsingElements(arg_42_0:GetMGData():GetRuntimeData("elements") or {})
	local var_42_1 = NenjuuGameConfig.GetStageConfig("Spring23Level_" .. arg_42_0.stageIndex)

	if not arg_42_0.abilityCache[arg_42_0.stageIndex] then
		arg_42_0.abilityCache[arg_42_0.stageIndex] = setmetatable({}, {
			__index = var_42_1.ability_config
		})
	end

	setActive(arg_42_0.rtLevel:Find("Rate"), true)
	onButton(arg_42_0, arg_42_0.rtLevel:Find("Rate/bg"), function()
		setActive(arg_42_0.rtLevel:Find("Rate"), false)
		arg_42_0:openReadyPage()
	end, SFX_CANCEL)

	local var_42_2 = arg_42_0.rtLevel:Find("Rate/main/panel")
	local var_42_3 = var_0_2(arg_42_0.abilityCache[arg_42_0.stageIndex], var_42_1.base_rate, var_42_1.ability_rate)

	setText(var_42_2:Find("info/rate/Text"), var_42_3)

	local var_42_4 = underscore.filter(NenjuuGameConfig.ABILITY_LIST, function(arg_44_0)
		return arg_42_0.abilityCache[arg_42_0.stageIndex][arg_44_0] ~= nil
	end)
	local var_42_5 = var_42_2:Find("view/content")
	local var_42_6 = UIItemList.New(var_42_5, var_42_5:Find("tpl"))

	var_42_6:make(function(arg_45_0, arg_45_1, arg_45_2)
		arg_45_1 = arg_45_1 + 1

		if arg_45_0 == UIItemList.EventUpdate then
			local var_45_0 = var_42_4[arg_45_1]

			setActive(arg_45_2:Find("empty"), not var_45_0)
			setActive(arg_45_2:Find("enable"), var_45_0)

			if var_45_0 then
				local var_45_1 = arg_45_2:Find("enable")

				eachChild(var_45_1:Find("icon"), function(arg_46_0)
					setActive(arg_46_0, arg_46_0.name == var_45_0)
				end)

				local var_45_2 = string.split(i18n("2023spring_minigame_nenjuu_skill" .. table.indexof(NenjuuGameConfig.ABILITY_LIST, var_45_0)), "|")

				setText(var_45_1:Find("name/Text"), var_45_2[1])
				setText(var_45_1:Find("desc"), var_45_2[2])
				onToggle(arg_42_0, var_45_1:Find("toggle"), function(arg_47_0)
					arg_42_0.abilityCache[arg_42_0.stageIndex][var_45_0] = arg_47_0

					local var_47_0 = var_0_2(arg_42_0.abilityCache[arg_42_0.stageIndex], var_42_1.base_rate, var_42_1.ability_rate) - var_42_3

					setText(var_42_2:Find("info/delta"), (var_47_0 < 0 and "" or "+") .. var_47_0)
				end)
				triggerToggle(var_45_1:Find("toggle"), arg_42_0.abilityCache[arg_42_0.stageIndex][var_45_0])
			end
		end
	end)
	var_42_6:align(math.min(#var_42_4 + 1, #NenjuuGameConfig.ABILITY_LIST))
end

function var_0_0.initControllerUI(arg_48_0)
	local var_48_0 = arg_48_0._tf:Find("Controller/top")

	onButton(arg_48_0, var_48_0:Find("btn_back"), function()
		arg_48_0:openUI("exit")
	end, SFX_PANEL)
	onButton(arg_48_0, var_48_0:Find("btn_pause"), function()
		arg_48_0:openUI("pause")
	end)
end

function var_0_0.SaveDataChange(arg_51_0, arg_51_1)
	local var_51_0 = {}

	table.insert(var_51_0, arg_51_1.high)
	table.insert(var_51_0, arg_51_1.count)
	table.insert(var_51_0, arg_51_1.item and table.indexof(NenjuuGameConfig.ITEM_LIST, arg_51_1.item) or 0)

	for iter_51_0 = 1, 7 do
		table.insert(var_51_0, arg_51_1["stage_" .. iter_51_0])
	end

	for iter_51_1, iter_51_2 in ipairs({
		"bomb",
		"lantern",
		"ice",
		"flash",
		"rush",
		"blessing",
		"decoy"
	}) do
		table.insert(var_51_0, arg_51_1.level[iter_51_2])
	end

	arg_51_0:StoreDataToServer(var_51_0)
end

function var_0_0.didEnter(arg_52_0)
	arg_52_0:initPageUI()
	arg_52_0:initLeveUI()
	arg_52_0:initControllerUI()

	arg_52_0.abilityCache = {}
	arg_52_0.gameController = NenjuuGameController.New(arg_52_0, arg_52_0._tf)

	arg_52_0:openUI("main")
end

function var_0_0.onBackPressed(arg_53_0)
	switch(arg_53_0.status, {
		main = function()
			if isActive(arg_53_0.rtLevel:Find("Opreation")) then
				triggerButton(arg_53_0.rtLevel:Find("Opreation/btn_back"))

				return
			end

			if isActive(arg_53_0.rtLevel:Find("Ready")) then
				triggerButton(arg_53_0.rtLevel:Find("Ready/bg"))

				return
			end

			if isActive(arg_53_0.rtLevel:Find("Rate")) then
				triggerButton(arg_53_0.rtLevel:Find("Rate/bg"))

				return
			end

			var_0_0.super.onBackPressed(arg_53_0)
		end,
		countdown = function()
			return
		end,
		pause = function()
			arg_53_0:openUI()
			arg_53_0.gameController:ResumeGame()
		end,
		exit = function()
			arg_53_0:openUI()
			arg_53_0.gameController:ResumeGame()
		end,
		result = function()
			return
		end
	}, function()
		assert(arg_53_0.gameController.isStart)
		arg_53_0:openUI("pause")
	end)
end

function var_0_0.willExit(arg_60_0)
	return
end

return var_0_0
