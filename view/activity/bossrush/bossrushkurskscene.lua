local var_0_0 = class("BossRushKurskScene", import("view.base.BaseUI"))
local var_0_1 = require("Mgr/Pool/PoolPlural")

var_0_0.DISPLAY = {
	STORY = 2,
	BATTLE = 1
}

function var_0_0.getUIName(arg_1_0)
	return "BossRushKurskUI"
end

function var_0_0.GetAtalsName(arg_2_0)
	return "ui/BossRushKurskUI_atlas"
end

function var_0_0.ResUISettings(arg_3_0)
	return true
end

function var_0_0.Ctor(arg_4_0)
	var_0_0.super.Ctor(arg_4_0)

	arg_4_0.loader = AutoLoader.New()
end

function var_0_0.preload(arg_5_0, arg_5_1)
	existCall(arg_5_1)
	arg_5_0.loader:LoadBundle(arg_5_0:GetAtalsName())
end

function var_0_0.init(arg_6_0)
	arg_6_0.top = arg_6_0._tf:Find("Top")
	arg_6_0.map = arg_6_0._tf:Find("Map")
	arg_6_0.seriesNodes = _.map(_.range(arg_6_0._tf:Find("Battle/Nodes").childCount), function(arg_7_0)
		return arg_6_0._tf:Find("Battle/Nodes"):GetChild(arg_7_0 - 1)
	end)
	arg_6_0.ptText = arg_6_0._tf:Find("Battle/Reward/Text")
	arg_6_0.nodes = {}

	for iter_6_0 = 1, arg_6_0._tf:Find("Map").childCount do
		local var_6_0 = arg_6_0._tf:Find("Map"):GetChild(iter_6_0 - 1)

		arg_6_0.nodes[var_6_0.name] = {
			tfType = 1,
			trans = var_6_0
		}
	end

	for iter_6_1 = 1, arg_6_0._tf:Find("Story/Nodes").childCount do
		local var_6_1 = arg_6_0._tf:Find("Story/Nodes"):GetChild(iter_6_1 - 1)

		arg_6_0.nodes[var_6_1.name] = {
			tfType = 2,
			trans = var_6_1
		}
	end

	arg_6_0.pluralRoot = pg.PoolMgr.GetInstance().root

	local var_6_2 = go(arg_6_0._tf:Find("Link"))

	setActive(var_6_2, false)

	arg_6_0.plural = var_0_1.New(var_6_2, 32)
	arg_6_0.linksContainer = arg_6_0._tf:Find("Links")
	arg_6_0.links = {}
	arg_6_0.storyBar = arg_6_0._tf:Find("Story/StoryBar")
	arg_6_0.storyAward = arg_6_0._tf:Find("Story/PassLevel/Award")
	arg_6_0.ActionSequence = {}

	setText(arg_6_0._tf:Find("Battle/Rank/Title"), i18n("word_billboard"))
	setText(arg_6_0._tf:Find("Battle/Reward/Title"), i18n("series_enemy_reward"))
	setText(arg_6_0._tf:Find("Story/PassLevel/Title"), i18n("series_enemy_storyreward"))
	setText(arg_6_0._tf:Find("Story/PassLevel/PT/Tips"), i18n("series_enemy_storyunlock"))
end

function var_0_0.SetActivity(arg_8_0, arg_8_1)
	arg_8_0.activity = arg_8_1
end

function var_0_0.SetPtActivity(arg_9_0, arg_9_1)
	arg_9_0.ptActivity = arg_9_1
	arg_9_0.ptData = ActivityPtData.New(arg_9_0.ptActivity)
end

function var_0_0.didEnter(arg_10_0)
	onButton(arg_10_0, arg_10_0.top:Find("back_btn"), function()
		arg_10_0:onBackPressed()
	end, SFX_CANCEL)
	onButton(arg_10_0, arg_10_0.top:Find("option"), function()
		arg_10_0:quickExitFunc()
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0._tf:Find("Help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = {
				{
					info = i18n("series_enemy_help")
				}
			}
		})
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0._tf:Find("Battle/Rank"), function()
		arg_10_0:emit(BossRushKurskMediator.ON_EXTRA_RANK)
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0._tf:Find("Battle/Reward"), function()
		arg_10_0:emit(BossRushKurskMediator.GO_ACT_SHOP, arg_10_0.ptData)
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0._tf:Find("Battle/Story"), function()
		arg_10_0:SetDisplayMode(var_0_0.DISPLAY.STORY)
	end, SFX_PANEL)
	onButton(arg_10_0, arg_10_0._tf:Find("Story/Battle"), function()
		arg_10_0:SetDisplayMode(var_0_0.DISPLAY.BATTLE)
	end, SFX_PANEL)

	local var_10_0 = arg_10_0.activity:getConfig("config_client").storys

	arg_10_0.storyNodesDict = {}

	_.each(var_10_0, function(arg_18_0)
		arg_10_0.storyNodesDict[arg_18_0] = BossRushStoryNode.New({
			id = arg_18_0
		})
	end)

	local var_10_1 = arg_10_0.activity:getConfig("config_client").tasks[1]

	arg_10_0.storyTask = getProxy(TaskProxy):getTaskVO(var_10_1) or Task.New({
		submitTime = 1,
		id = var_10_1
	})

	local var_10_2 = arg_10_0.contextData.displayMode or BossRushKurskScene.DISPLAY.BATTLE

	arg_10_0.contextData.displayMode = nil

	arg_10_0:SetDisplayMode(var_10_2)
end

function var_0_0.getBGM(arg_19_0)
	local var_19_0 = pg.voice_bgm[arg_19_0.__cname]

	if not var_19_0 then
		return nil
	end

	local var_19_1 = var_19_0.bgm
	local var_19_2 = var_19_0.special_bgm
	local var_19_3 = arg_19_0.contextData.displayMode

	if var_19_3 == var_0_0.DISPLAY.BATTLE then
		return var_19_1
	elseif var_19_3 == var_0_0.DISPLAY.STORY then
		return var_19_2
	end
end

function var_0_0.SetDisplayMode(arg_20_0, arg_20_1)
	if arg_20_1 == arg_20_0.contextData.displayMode then
		return
	end

	arg_20_0.contextData.displayMode = arg_20_1

	arg_20_0:PlayBGM()
	arg_20_0:UpdateView()
end

function var_0_0.UpdateView(arg_21_0)
	local var_21_0 = arg_21_0.contextData.displayMode == var_0_0.DISPLAY.BATTLE

	setActive(arg_21_0._tf:Find("Battle"), var_21_0)
	setActive(arg_21_0._tf:Find("Story"), not var_21_0)
	setActive(arg_21_0._tf:Find("Links"), not var_21_0)
	arg_21_0:UpdateBattle()
	arg_21_0:UpdateStory()

	local var_21_1 = arg_21_0.contextData.displayMode

	arg_21_0:addbubbleMsgBoxList({
		function(arg_22_0)
			if arg_21_0.activity:HasPassSeries(1001) then
				pg.SystemGuideMgr.GetInstance():PlayByGuideId("NG0036", nil, arg_22_0)

				return
			end

			arg_22_0()
		end,
		function(arg_23_0)
			local var_23_0

			if var_21_1 == var_0_0.DISPLAY.BATTLE then
				var_23_0 = arg_21_0.activity:getConfig("config_client").openActivityStory
			elseif var_21_1 == var_0_0.DISPLAY.STORY then
				var_23_0 = arg_21_0.activity:getConfig("config_client").openStory
			end

			arg_21_0:PlayStory(var_23_0, arg_23_0)
		end,
		function(arg_24_0)
			local var_24_0 = true

			for iter_24_0, iter_24_1 in pairs(arg_21_0.storyNodesDict) do
				local var_24_1 = iter_24_1:GetStory()

				if var_24_1 and var_24_1 ~= "" then
					var_24_0 = var_24_0 and pg.NewStoryMgr.GetInstance():IsPlayed(var_24_1)
				end

				if not var_24_0 then
					break
				end
			end

			if var_24_0 then
				local var_24_2 = arg_21_0.activity:getConfig("config_client").endStory

				arg_21_0:PlayStory(var_24_2, function(arg_25_0)
					arg_24_0()

					if arg_25_0 then
						arg_21_0:UpdateView()
					end
				end)

				return
			end

			arg_24_0()
		end
	})
end

function var_0_0.UpdateBattle(arg_26_0)
	local var_26_0 = arg_26_0.activity
	local var_26_1 = var_26_0:GetActiveSeriesIds()

	table.Foreach(arg_26_0.seriesNodes, function(arg_27_0, arg_27_1)
		local var_27_0 = var_26_1[arg_27_0]
		local var_27_1 = BossRushSeriesData.New({
			id = var_27_0,
			actId = var_26_0.id
		})
		local var_27_2 = var_27_1:IsUnlock(var_26_0)

		setActive(arg_27_1:Find("Pin/NameBG"), var_27_2)
		setActive(arg_27_1:Find("Pin/Lock"), not var_27_2)
		setText(arg_27_1:Find("Pin/ChapterName"), var_27_1:GetSeriesCode())
		setText(arg_27_1:Find("Pin/NameBG/Name"), var_27_1:GetName())

		local var_27_3 = var_27_1:GetType() == BossRushSeriesData.TYPE.SP

		setActive(arg_27_1:Find("Pin/NameBG/BonusCount"), var_27_2 and var_27_3)

		local var_27_4 = true

		if var_27_3 then
			local var_27_5 = var_26_0:GetUsedBonus()[arg_27_0] or 0
			local var_27_6 = var_27_1:GetMaxBonusCount()

			setText(arg_27_1:Find("Pin/NameBG/BonusCount"):GetChild(0), i18n("series_enemy_SP_count"))
			setText(arg_27_1:Find("Pin/NameBG/BonusCount"):GetChild(1), math.max(0, var_27_6 - var_27_5) .. "/" .. var_27_6)

			var_27_4 = var_27_6 - var_27_5 > 0
		end

		onButton(arg_26_0, arg_27_1, function()
			if not var_27_2 then
				local var_28_0 = var_27_1:GetPreSeriesId()
				local var_28_1 = BossRushSeriesData.New({
					id = var_28_0
				})

				pg.TipsMgr.GetInstance():ShowTips(i18n("series_enemy_unlock", var_28_1:GetName()))

				return
			end

			if not var_27_4 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("series_enemy_SP_error"))

				return
			end

			arg_26_0:emit(BossRushKurskMediator.ON_FLEET_SELECT, var_27_1)
		end, SFX_PANEL)
	end)
	setActive(arg_26_0._tf:Find("Battle/Reward/Tip"), arg_26_0.ptData:CanGetAward())
	setText(arg_26_0.ptText, arg_26_0.ptActivity.data1)
end

local var_0_2 = {
	"story_bar_green",
	"story_bar_yellow",
	"story_bar_purple"
}

function var_0_0.UpdateStory(arg_29_0)
	local var_29_0 = {}
	local var_29_1 = pg.NewStoryMgr.GetInstance()
	local var_29_2 = 1
	local var_29_3 = 2
	local var_29_4 = 3
	local var_29_5 = 0
	local var_29_6 = 0

	for iter_29_0, iter_29_1 in pairs(arg_29_0.storyNodesDict) do
		var_29_0[iter_29_0] = {}

		local var_29_7 = iter_29_1:GetStory()
		local var_29_8 = true

		if var_29_7 and var_29_7 ~= "" then
			var_29_8 = var_29_1:IsPlayed(var_29_7)
			var_29_5 = var_29_5 + (var_29_8 and 1 or 0)
			var_29_6 = var_29_6 + 1
		end

		var_29_0[iter_29_0].status = var_29_8 and var_29_4 or var_29_2
	end

	local var_29_9
	local var_29_10
	local var_29_11 = _.sort(_.values(arg_29_0.storyNodesDict), function(arg_30_0, arg_30_1)
		return arg_30_0.id < arg_30_1.id
	end)

	_.each(var_29_11, function(arg_31_0)
		local var_31_0 = arg_31_0:GetTriggers()

		if var_29_0[arg_31_0.id].status == var_29_4 then
			return
		end

		if not _.any(var_31_0, function(arg_32_0)
			if arg_32_0.type == BossRushStoryNode.TRIGGER_TYPE.PT_GOT then
				return arg_29_0.ptActivity.data1 < arg_32_0.value
			elseif arg_32_0.type == BossRushStoryNode.TRIGGER_TYPE.SERIES_PASSED then
				return not BossRushSeriesData.New({
					id = arg_32_0.value,
					actId = arg_29_0.activity.id
				}):IsUnlock(arg_29_0.activity)
			elseif arg_32_0.type == BossRushStoryNode.TRIGGER_TYPE.STORY_READED then
				return var_29_0[arg_32_0.value].status < var_29_4
			end
		end) then
			var_29_0[arg_31_0.id].status = var_29_3
		end
	end)
	_.each(var_29_11, function(arg_33_0)
		local var_33_0 = arg_33_0:GetTriggers()

		_.each(var_33_0, function(arg_34_0)
			if arg_34_0.type == BossRushStoryNode.TRIGGER_TYPE.PT_GOT then
				if var_29_0[arg_33_0.id].status > var_29_2 then
					var_29_10 = var_29_10 and math.max(arg_34_0.value, var_29_10) or arg_34_0.value
				elseif var_29_0[arg_33_0.id].status == var_29_2 then
					var_29_9 = var_29_9 and math.min(arg_34_0.value, var_29_9) or arg_34_0.value
				end
			end
		end)
	end)
	setText(arg_29_0._tf:Find("Story/PassLevel/PT/Text"), arg_29_0.ptActivity.data1 .. "/" .. (var_29_9 or var_29_10 or ""))
	setText(arg_29_0._tf:Find("Story/PassLevel/Values"):GetChild(0), var_29_5)
	setText(arg_29_0._tf:Find("Story/PassLevel/Values"):GetChild(2), var_29_6)
	arg_29_0:ReturnLinks()

	local var_29_12 = false

	table.Foreach(arg_29_0.storyNodesDict, function(arg_35_0, arg_35_1)
		local var_35_0 = arg_29_0.nodes[arg_35_1:GetIconName()].trans
		local var_35_1 = var_29_0[arg_35_0].status == var_29_3
		local var_35_2 = arg_35_1:GetType()

		if var_35_2 == BossRushStoryNode.NODE_TYPE.NORMAL then
			arg_29_0.loader:GetSprite(arg_29_0:GetAtalsName(), var_35_1 and "story_green_active" or "story_green", var_35_0:GetChild(0), true)
		elseif var_35_2 == BossRushStoryNode.NODE_TYPE.EVENT then
			setActive(var_35_0, var_29_0[arg_35_0].status > var_29_2)
			arg_29_0.loader:GetSprite(arg_29_0:GetAtalsName(), var_35_1 and "story_yellow_active" or "story_yellow", var_35_0:GetChild(0), true)
		elseif var_35_2 == BossRushStoryNode.NODE_TYPE.BATTLE then
			-- block empty
		end

		if var_35_1 then
			local var_35_3 = arg_29_0._tf:Find("Story"):InverseTransformPoint(var_35_0.position)

			setAnchoredPosition(arg_29_0.storyBar, var_35_3)
			setText(arg_29_0.storyBar:Find("Text"), arg_35_1:GetName())
			arg_29_0.loader:GetSprite(arg_29_0:GetAtalsName(), var_0_2[var_35_2], arg_29_0.storyBar, true)
			onButton(arg_29_0, arg_29_0.storyBar, function()
				local var_36_0 = arg_35_1:GetStory()

				arg_29_0:PlayStory(var_36_0, function()
					arg_29_0:UpdateView()
				end)
			end)

			var_29_12 = true
		end

		local var_35_4 = arg_35_1:GetActiveLink()

		;(function()
			if var_35_4 == 0 or var_29_0[var_35_4].status ~= var_29_4 then
				return
			end

			local var_38_0 = arg_29_0.storyNodesDict[var_35_4]
			local var_38_1 = arg_29_0.nodes[var_38_0:GetIconName()].trans
			local var_38_2 = arg_29_0.plural:Dequeue()

			table.insert(arg_29_0.links, go(var_38_2))
			setActive(var_38_2, true)
			setParent(var_38_2, arg_29_0.linksContainer)

			local var_38_3 = arg_29_0.linksContainer:InverseTransformPoint(var_35_0.position)
			local var_38_4 = arg_29_0.linksContainer:InverseTransformPoint(var_38_1.position) - var_38_3
			local var_38_5 = Vector2.Magnitude(var_38_4)

			tf(var_38_2).sizeDelta = Vector2(var_38_5, 2)
			tf(var_38_2).anchoredPosition = var_38_3
			tf(var_38_2).localRotation = Quaternion.FromToRotation(Vector3.right, var_38_4)
		end)()
	end)
	setActive(arg_29_0.storyBar, var_29_12)
	setActive(arg_29_0.storyAward, tobool(arg_29_0.storyTask))

	if arg_29_0.storyTask then
		local var_29_13 = arg_29_0.storyTask:getConfig("award_display")
		local var_29_14 = {
			type = var_29_13[1][1],
			id = var_29_13[1][2],
			count = var_29_13[1][3]
		}

		updateDrop(arg_29_0.storyAward:Find("Mask"):GetChild(0), var_29_14)
		onButton(arg_29_0, arg_29_0.storyAward:Find("Mask"):GetChild(0), function()
			arg_29_0:emit(BaseUI.ON_DROP, var_29_14)
		end)

		local var_29_15 = arg_29_0.storyTask:getTaskStatus()

		setActive(arg_29_0.storyAward:Find("Got"), var_29_15 == 2)

		if var_29_15 == 1 then
			arg_29_0:emit(BossRushKurskMediator.ON_TASK_SUBMIT, arg_29_0.storyTask)
		end
	end

	setActive(arg_29_0._tf:Find("Battle/Story/New"), var_29_12)
end

function var_0_0.ReturnLinks(arg_40_0, arg_40_1)
	for iter_40_0, iter_40_1 in ipairs(arg_40_0.links) do
		if not arg_40_0.plural:Enqueue(iter_40_1, arg_40_1) then
			setParent(iter_40_1, arg_40_0.pluralRoot)
		end
	end

	table.clean(arg_40_0.links)
end

function var_0_0.PlayStory(arg_41_0, arg_41_1, arg_41_2)
	if not arg_41_1 then
		return existCall(arg_41_2)
	end

	local var_41_0 = pg.NewStoryMgr.GetInstance()
	local var_41_1 = var_41_0:IsPlayed(arg_41_1)

	seriesAsync({
		function(arg_42_0)
			if var_41_1 then
				return arg_42_0()
			end

			local var_42_0 = tonumber(arg_41_1)

			if var_42_0 and var_42_0 > 0 then
				arg_41_0:emit(BossRushKurskMediator.ON_PERFORM_COMBAT, var_42_0)
			else
				var_41_0:Play(arg_41_1, arg_42_0)
			end
		end,
		function(arg_43_0, ...)
			existCall(arg_41_2, ...)
		end
	})
end

function var_0_0.UpdateTasks(arg_44_0, arg_44_1)
	if _.any(arg_44_1, function(arg_45_0)
		return arg_44_0.storyTask and arg_44_0.storyTask.id == arg_45_0
	end) then
		arg_44_0.storyTask.submitTime = 1

		arg_44_0:UpdateView()
	end
end

function var_0_0.addbubbleMsgBoxList(arg_46_0, arg_46_1)
	local var_46_0 = #arg_46_0.ActionSequence == 0

	table.insertto(arg_46_0.ActionSequence, arg_46_1)

	if not var_46_0 then
		return
	end

	arg_46_0:resumeBubble()
end

function var_0_0.addbubbleMsgBox(arg_47_0, arg_47_1)
	local var_47_0 = #arg_47_0.ActionSequence == 0

	table.insert(arg_47_0.ActionSequence, arg_47_1)

	if not var_47_0 then
		return
	end

	arg_47_0:resumeBubble()
end

function var_0_0.resumeBubble(arg_48_0)
	if #arg_48_0.ActionSequence == 0 then
		return
	end

	local var_48_0

	local function var_48_1()
		local var_49_0 = arg_48_0.ActionSequence[1]

		if var_49_0 then
			var_49_0(function()
				table.remove(arg_48_0.ActionSequence, 1)
				var_48_1()
			end)
		end
	end

	var_48_1()
end

function var_0_0.CleanBubbleMsgbox(arg_51_0)
	table.clean(arg_51_0.ActionSequence)
end

function var_0_0.willExit(arg_52_0)
	arg_52_0:ReturnLinks(true)
	arg_52_0.loader:Clear()
	var_0_0.super.willExit(arg_52_0)
end

return var_0_0
