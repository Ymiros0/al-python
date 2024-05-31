local var_0_0 = class("WorldBossInfoAndRankPanel", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "WorldBossInfoAndRankUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.toggleRank = arg_2_0:findTF("rank")
	arg_2_0.toggleInfo = arg_2_0:findTF("info")
	arg_2_0.myRankTF = arg_2_0:findTF("rank_panel/tpl")
	arg_2_0.rankList = UIItemList.New(arg_2_0:findTF("rank_panel/list"), arg_2_0.myRankTF)
	arg_2_0.maxRankCnt = pg.gameset.joint_boss_fighter_max.key_value
	arg_2_0.rankCnt1 = arg_2_0:findTF("rank_panel/cnt/Text"):GetComponent(typeof(Text))
	arg_2_0.rankTF = arg_2_0:findTF("rank_panel")
	arg_2_0.maskTF = arg_2_0:findTF("rank_panel/mask")
	arg_2_0.maskTxt = arg_2_0:findTF("rank_panel/mask/Text"):GetComponent(typeof(Text))
	arg_2_0.infoTitle = arg_2_0:findTF("info_panel/title/Text"):GetComponent(typeof(Text))
	arg_2_0.infoSkillList = UIItemList.New(arg_2_0:findTF("info_panel/scrollrect/content"), arg_2_0:findTF("info_panel/scrollrect/content/tpl"))
end

function var_0_0.SetCallback(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0.callback = arg_3_1
	arg_3_0.flushRankCallback = arg_3_2
end

function var_0_0.OnInit(arg_4_0)
	arg_4_0._tf:SetSiblingIndex(2)
	onToggle(arg_4_0, arg_4_0.toggleInfo, function(arg_5_0)
		if arg_5_0 then
			arg_4_0:ResetInfoLayout()
		end
	end)
end

function var_0_0.Flush(arg_6_0, arg_6_1, arg_6_2)
	arg_6_0.boss = arg_6_1
	arg_6_0.proxy = arg_6_2

	arg_6_0:FlushRank()
	arg_6_0:FlushInfo()

	if not arg_6_0.boss:IsFullHp() then
		triggerToggle(arg_6_0.toggleRank, true)
	else
		triggerToggle(arg_6_0.toggleInfo, true)
		arg_6_0:ResetInfoLayout()
	end
end

function var_0_0.FlushInfo(arg_7_0)
	arg_7_0.infoTitle.text = arg_7_0.boss.config.name

	local var_7_0 = arg_7_0.boss.config.description

	arg_7_0.infoSkillList:make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate then
			local var_8_0 = var_7_0[arg_8_1 + 1]
			local var_8_1 = var_8_0[1]
			local var_8_2 = var_8_0[2]

			arg_8_2:Find("color"):GetComponent(typeof(Image)).sprite = GetSpriteFromAtlas("ui/WorldBossUI_atlas", "color_" .. var_8_2)

			local var_8_3 = arg_8_2:Find("color/Text")

			setText(var_8_3, var_8_1)
		end
	end)
	arg_7_0.infoSkillList:align(#var_7_0)
end

function var_0_0.ResetInfoLayout(arg_9_0)
	local var_9_0 = 28
	local var_9_1 = arg_9_0.boss.config.description

	onNextTick(function()
		if arg_9_0.exited then
			return
		end

		arg_9_0.infoSkillList:each(function(arg_11_0, arg_11_1)
			local var_11_0 = var_9_1[arg_11_0 + 1][3]
			local var_11_1 = arg_11_1:Find("color/Text")
			local var_11_2 = "　"
			local var_11_3, var_11_4 = math.modf(var_11_1.sizeDelta.x / var_9_0)
			local var_11_5 = math.ceil(var_9_0 * var_11_4)

			for iter_11_0 = 1, var_11_3 do
				var_11_2 = var_11_2 .. "　"
			end

			if var_11_4 > 0 then
				var_11_2 = var_11_2 .. "<size=" .. var_11_5 .. ">　</size>"
			end

			setText(arg_11_1:Find("Text"), var_11_2 .. var_11_0)
		end)
	end)
end

function var_0_0.FlushRank(arg_12_0)
	local var_12_0 = arg_12_0.boss

	if not var_12_0 then
		return
	end

	local var_12_1 = arg_12_0.proxy:GetRank(var_12_0.id)
	local var_12_2 = 0

	if not var_12_1 then
		arg_12_0:emit(WorldBossMediator.ON_RANK_LIST, var_12_0.id)
	else
		arg_12_0.rankList:make(function(arg_13_0, arg_13_1, arg_13_2)
			if arg_13_0 == UIItemList.EventUpdate then
				local var_13_0 = var_12_1[arg_13_1 + 1]

				arg_12_0:UpdateRankTF(arg_13_2, var_13_0, arg_13_1 + 1)
			end
		end)
		arg_12_0.rankList:align(math.min(#var_12_1, 3))
		arg_12_0:UpdateSelfRank(var_12_1)

		var_12_2 = #var_12_1
	end

	arg_12_0.rankCnt1.text = var_12_2 .. "<color=#A2A2A2>/" .. arg_12_0.maxRankCnt .. "</color>"

	if arg_12_0.flushRankCallback then
		arg_12_0.flushRankCallback(var_12_2, arg_12_0.maxRankCnt)
	end

	arg_12_0:AddWaitResultTimer()
end

function var_0_0.AddWaitResultTimer(arg_14_0)
	arg_14_0:RemoveWaitTimer()

	local var_14_0 = arg_14_0.boss
	local var_14_1 = var_14_0:ShouldWaitForResult()

	setActive(arg_14_0.maskTF, var_14_1)

	if var_14_1 then
		local var_14_2 = var_14_0:GetWaitForResultTime()

		arg_14_0.waitTimer = Timer.New(function()
			local var_15_0 = pg.TimeMgr.GetInstance():GetServerTime()
			local var_15_1 = var_14_2 - var_15_0

			if var_15_1 < 0 then
				arg_14_0:AddWaitResultTimer()

				if arg_14_0.callback then
					arg_14_0.callback(false)
				end
			else
				arg_14_0.maskTxt.text = pg.TimeMgr.GetInstance():DescCDTime(var_15_1)
			end
		end, 1, -1)

		arg_14_0.waitTimer:Start()

		if arg_14_0.callback then
			arg_14_0.callback(true)
		end
	end
end

function var_0_0.RemoveWaitTimer(arg_16_0)
	if arg_16_0.waitTimer then
		arg_16_0.waitTimer:Stop()

		arg_16_0.waitTimer = nil
	end
end

function var_0_0.UpdateRankTF(arg_17_0, arg_17_1, arg_17_2, arg_17_3)
	setText(arg_17_1:Find("name"), arg_17_2.name)
	setText(arg_17_1:Find("value/Text"), arg_17_2.damage)
	setText(arg_17_1:Find("number"), arg_17_2.number or arg_17_3)
	setActive(arg_17_1:Find("value/view"), not arg_17_2.isSelf)
	onButton(arg_17_0, arg_17_1:Find("value/view"), function()
		local var_18_0 = arg_17_0.boss

		arg_17_0:emit(WorldBossMediator.FETCH_RANK_FORMATION, arg_17_2.id, var_18_0.id)
	end, SFX_PANEL)
end

function var_0_0.UpdateSelfRank(arg_19_0, arg_19_1)
	local var_19_0

	for iter_19_0, iter_19_1 in ipairs(arg_19_1) do
		if iter_19_1.isSelf then
			var_19_0 = iter_19_1
			var_19_0.number = iter_19_0

			break
		end
	end

	if var_19_0 then
		arg_19_0:UpdateRankTF(arg_19_0.myRankTF, var_19_0)
	end
end

function var_0_0.OnDestroy(arg_20_0)
	arg_20_0:RemoveWaitTimer()
end

return var_0_0
