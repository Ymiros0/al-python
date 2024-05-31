﻿local var_0_0 = class("ActivityBossHuanChangScene", import(".ActivityBossSceneTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "ActivityBossHuanChangUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.mainTF = arg_2_0:findTF("adapt")
	arg_2_0.bg = arg_2_0:findTF("bg")
	arg_2_0.bottom = arg_2_0:findTF("bottom", arg_2_0.mainTF)
	arg_2_0.hpBar = arg_2_0:findTF("progress", arg_2_0.bottom)
	arg_2_0.barList = {}

	for iter_2_0 = 1, 4 do
		arg_2_0.barList[iter_2_0] = arg_2_0:findTF(iter_2_0, arg_2_0.hpBar)
	end

	arg_2_0.progressDigit = arg_2_0:findTF("digit", arg_2_0.bottom)
	arg_2_0.digitbig = arg_2_0.progressDigit:Find("big")
	arg_2_0.digitsmall = arg_2_0.progressDigit:Find("small")
	arg_2_0.left = arg_2_0:findTF("left", arg_2_0.mainTF)
	arg_2_0.right = arg_2_0:findTF("right", arg_2_0.mainTF)
	arg_2_0.rankTF = arg_2_0:findTF("rank", arg_2_0.right)
	arg_2_0.rankList = CustomIndexLayer.Clone2Full(arg_2_0.rankTF:Find("layout"), 3)

	for iter_2_1, iter_2_2 in ipairs(arg_2_0.rankList) do
		setActive(iter_2_2, false)
	end

	arg_2_0.stageList = {}

	for iter_2_3 = 1, 4 do
		arg_2_0.stageList[iter_2_3] = arg_2_0:findTF(iter_2_3, arg_2_0.right)
	end

	arg_2_0.stageSP = arg_2_0:findTF("6", arg_2_0.right)

	if not IsNil(arg_2_0.stageSP) then
		setActive(arg_2_0.stageSP, false)
	end

	arg_2_0.awardFlash = arg_2_0:findTF("ptaward/flash", arg_2_0.right)
	arg_2_0.awardBtn = arg_2_0:findTF("ptaward/button", arg_2_0.right)
	arg_2_0.ptScoreTxt = arg_2_0:findTF("ptaward/Text", arg_2_0.right)
	arg_2_0.top = arg_2_0:findTF("top", arg_2_0.mainTF)
	arg_2_0.ticketNum = arg_2_0:findTF("ticket/Text", arg_2_0.top)
	arg_2_0.helpBtn = arg_2_0:findTF("help", arg_2_0.top)

	onButton(arg_2_0, arg_2_0.top:Find("back_btn"), function()
		arg_2_0:emit(var_0_0.ON_BACK)
	end, SOUND_BACK)
	setActive(arg_2_0.top, false)
	setAnchoredPosition(arg_2_0.top, {
		y = 1080
	})
	setActive(arg_2_0.left, false)
	setAnchoredPosition(arg_2_0.left, {
		x = -1920
	})
	setActive(arg_2_0.right, false)
	setAnchoredPosition(arg_2_0.right, {
		x = 1920
	})
	setActive(arg_2_0.bottom, false)
	setAnchoredPosition(arg_2_0.bottom, {
		y = -1080
	})
	arg_2_0:buildCommanderPanel()
end

function var_0_0.UpdateDropItems(arg_4_0)
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.contextData.DisplayItems or {}) do
		local var_4_0 = arg_4_0:findTF("milestone/item", arg_4_0.barList[iter_4_0])
		local var_4_1 = {
			type = arg_4_0.contextData.DisplayItems[5 - iter_4_0][1],
			id = arg_4_0.contextData.DisplayItems[5 - iter_4_0][2],
			count = arg_4_0.contextData.DisplayItems[5 - iter_4_0][3]
		}

		updateDrop(var_4_0:GetChild(0), var_4_1)
		onButton(arg_4_0, var_4_0, function()
			arg_4_0:emit(var_0_0.ON_DROP, var_4_1)
		end, SFX_PANEL)
	end
end

function var_0_0.UpdatePage(arg_6_0)
	local var_6_0 = arg_6_0.contextData.bossHP

	setText(arg_6_0.digitbig, math.floor(var_6_0 / 100))
	setText(arg_6_0.digitsmall, string.format("%02d", var_6_0 % 100) .. "%")

	local var_6_1 = pg.TimeMgr.GetInstance()

	for iter_6_0 = 1, 4 do
		local var_6_2 = arg_6_0.barList[iter_6_0]

		setSlider(arg_6_0:findTF("Slider", var_6_2), 0, 2500, math.min(math.max(var_6_0 - (iter_6_0 - 1) * 2500, 0), 2500))

		local var_6_3 = arg_6_0.contextData.mileStones[5 - iter_6_0]

		setActive(arg_6_0:findTF("milestone/item", var_6_2), not var_6_3)
		setActive(arg_6_0:findTF("milestone/time", var_6_2), var_6_3)

		if var_6_3 then
			local var_6_4 = var_6_1:STimeDescC(arg_6_0.contextData.mileStones[5 - iter_6_0], "%m/%d/%H:%M")

			setText(arg_6_0:findTF("milestone/time/Text", var_6_2), var_6_4)
		end
	end

	for iter_6_1 = 1, #arg_6_0.stageList - 1 do
		local var_6_5 = arg_6_0.contextData.normalStageIDs[iter_6_1]
		local var_6_6 = arg_6_0.stageList[iter_6_1]

		for iter_6_2, iter_6_3 in ipairs(arg_6_0.contextData.ticketInitPools) do
			for iter_6_4, iter_6_5 in ipairs(iter_6_3[1]) do
				if iter_6_5 == var_6_5 then
					local var_6_7 = iter_6_3[2]
					local var_6_8 = arg_6_0.contextData.stageTickets[var_6_5] or 0
					local var_6_9 = var_6_6:Find("count")

					setActive(var_6_9, var_6_8 > 0)
					setText(var_6_9:Find("res"), var_6_8)
					setText(var_6_9:Find("max"), var_6_7)
				end
			end
		end
	end

	setText(arg_6_0.ptScoreTxt, arg_6_0.contextData.ptData.count)
	setActive(arg_6_0.awardFlash, arg_6_0.contextData.ptData:CanGetAward())

	if arg_6_0.bonusWindow and arg_6_0.bonusWindow:IsShowing() then
		arg_6_0.bonusWindow.buffer:UpdateView(arg_6_0.contextData.ptData)
	end

	local var_6_10 = arg_6_0:GetEXTicket()

	setText(arg_6_0.ticketNum, var_6_10)
end

function var_0_0.UpdateRank(arg_7_0, arg_7_1)
	arg_7_1 = arg_7_1 or {}

	for iter_7_0 = 1, #arg_7_0.rankList do
		local var_7_0 = arg_7_0.rankList[iter_7_0]

		setActive(var_7_0, iter_7_0 <= #arg_7_1)

		if iter_7_0 <= #arg_7_1 then
			local var_7_1 = var_7_0:Find("Text")
			local var_7_2 = tostring(arg_7_1[iter_7_0].name)

			if #var_7_2 >= 11 then
				var_7_1:GetComponent(typeof(Text)).fontSize = 23
			else
				var_7_1:GetComponent(typeof(Text)).fontSize = 28
			end

			setText(var_7_1, var_7_2)
		end
	end
end

return var_0_0
