pg = pg or {}

local var_0_0 = singletonClass("NewStoryMgr")

pg.NewStoryMgr = var_0_0

local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 4
local var_0_5 = 5
local var_0_6 = 6
local var_0_7 = 7
local var_0_8 = Color.New(1, 0.8705, 0.4196, 1)
local var_0_9 = Color.New(1, 1, 1, 1)

require("Mgr/Story/Include")

local var_0_10 = true

local function var_0_11(...)
	if var_0_10 and IsUnityEditor then
		originalPrint(...)
	end
end

local var_0_12 = {
	"",
	"JP",
	"KR",
	"US",
	""
}

local function var_0_13(arg_2_0)
	local var_2_0 = var_0_12[PLATFORM_CODE]

	if arg_2_0 == "index" then
		arg_2_0 = arg_2_0 .. var_2_0
	end

	local var_2_1

	if PLATFORM_CODE == PLATFORM_JP then
		var_2_1 = "GameCfg.story" .. var_2_0 .. "." .. arg_2_0
	else
		var_2_1 = "GameCfg.story" .. "." .. arg_2_0
	end

	local var_2_2, var_2_3 = pcall(function()
		return require(var_2_1)
	end)

	if not var_2_2 then
		local var_2_4 = true

		if UnGamePlayState then
			local var_2_5 = "GameCfg.dungeon." .. arg_2_0

			if pcall(function()
				return require(var_2_5)
			end) then
				var_2_4 = false
			end
		end

		if var_2_4 then
			errorMsg("不存在剧情ID对应的Lua:" .. arg_2_0)
		end
	end

	return var_2_2 and var_2_3
end

function var_0_0.SetData(arg_5_0, arg_5_1)
	arg_5_0.playedList = {}

	for iter_5_0, iter_5_1 in ipairs(arg_5_1) do
		local var_5_0 = iter_5_1

		if iter_5_1 == 20008 then
			var_5_0 = 1131
		end

		if iter_5_1 == 20009 then
			var_5_0 = 1132
		end

		if iter_5_1 == 20010 then
			var_5_0 = 1133
		end

		if iter_5_1 == 20011 then
			var_5_0 = 1134
		end

		if iter_5_1 == 20012 then
			var_5_0 = 1135
		end

		if iter_5_1 == 20013 then
			var_5_0 = 1136
		end

		if iter_5_1 == 20014 then
			var_5_0 = 1137
		end

		arg_5_0.playedList[var_5_0] = true
	end
end

function var_0_0.SetPlayedFlag(arg_6_0, arg_6_1)
	var_0_11("Update story id", arg_6_1)

	arg_6_0.playedList[arg_6_1] = true
end

function var_0_0.GetPlayedFlag(arg_7_0, arg_7_1)
	return arg_7_0.playedList[arg_7_1]
end

function var_0_0.IsPlayed(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0, var_8_1 = arg_8_0:StoryName2StoryId(arg_8_1)
	local var_8_2 = arg_8_0:GetPlayedFlag(var_8_0)
	local var_8_3 = true

	if var_8_1 and not arg_8_2 then
		var_8_3 = arg_8_0:GetPlayedFlag(var_8_1)
	end

	return var_8_2 and var_8_3
end

local function var_0_14(arg_9_0)
	local var_9_0 = {}

	for iter_9_0, iter_9_1 in pairs(arg_9_0) do
		var_9_0[iter_9_1] = iter_9_0
	end

	return var_9_0
end

function var_0_0.StoryName2StoryId(arg_10_0, arg_10_1)
	if not var_0_0.indexs then
		var_0_0.indexs = var_0_14(var_0_13("index"))
	end

	if not var_0_0.againIndexs then
		var_0_0.againIndexs = var_0_14(var_0_13("index_again"))
	end

	return var_0_0.indexs[arg_10_1], var_0_0.againIndexs[arg_10_1]
end

function var_0_0.StoryId2StoryName(arg_11_0, arg_11_1)
	if not var_0_0.indexIds then
		var_0_0.indexIds = var_0_13("index")
	end

	if not var_0_0.againIndexIds then
		var_0_0.againIndexIds = var_0_13("index_again")
	end

	return var_0_0.indexIds[arg_11_1], var_0_0.againIndexIds[arg_11_1]
end

function var_0_0.StoryLinkNames(arg_12_0, arg_12_1)
	if not var_0_0.linkNames then
		var_0_0.linkNames = var_0_13("index_link")
	end

	return var_0_0.linkNames[arg_12_1]
end

function var_0_0._GetStoryPaintingsByName(arg_13_0, arg_13_1)
	return arg_13_1:GetUsingPaintingNames()
end

function var_0_0.GetStoryPaintingsByName(arg_14_0, arg_14_1)
	local var_14_0 = var_0_13(arg_14_1)

	if not var_14_0 then
		var_0_11("not exist story file")

		return {}
	end

	local var_14_1 = Story.New(var_14_0, false)

	return arg_14_0:_GetStoryPaintingsByName(var_14_1)
end

function var_0_0.GetStoryPaintingsByNameList(arg_15_0, arg_15_1)
	local var_15_0 = {}
	local var_15_1 = {}

	for iter_15_0, iter_15_1 in ipairs(arg_15_1) do
		for iter_15_2, iter_15_3 in ipairs(arg_15_0:GetStoryPaintingsByName(iter_15_1)) do
			var_15_1[iter_15_3] = true
		end
	end

	for iter_15_4, iter_15_5 in pairs(var_15_1) do
		table.insert(var_15_0, iter_15_4)
	end

	return var_15_0
end

function var_0_0.GetStoryPaintingsById(arg_16_0, arg_16_1)
	return arg_16_0:GetStoryPaintingsByIdList({
		arg_16_1
	})
end

function var_0_0.GetStoryPaintingsByIdList(arg_17_0, arg_17_1)
	local var_17_0 = _.map(arg_17_1, function(arg_18_0)
		return arg_17_0:StoryId2StoryName(arg_18_0)
	end)

	return arg_17_0:GetStoryPaintingsByNameList(var_17_0)
end

function var_0_0.ShouldDownloadRes(arg_19_0, arg_19_1)
	local var_19_0 = arg_19_0:GetStoryPaintingsByName(arg_19_1)

	return _.any(var_19_0, function(arg_20_0)
		return PaintingGroupConst.VerifyPaintingFileName(arg_20_0)
	end)
end

function var_0_0.Init(arg_21_0, arg_21_1)
	arg_21_0.state = var_0_1
	arg_21_0.playedList = {}
	arg_21_0.playQueue = {}

	PoolMgr.GetInstance():GetUI("NewStoryUI", true, function(arg_22_0)
		arg_21_0._go = arg_22_0
		arg_21_0._tf = tf(arg_21_0._go)
		arg_21_0.frontTr = findTF(arg_21_0._tf, "front")
		arg_21_0.UIOverlay = GameObject.Find("Overlay/UIOverlay")

		arg_21_0._go.transform:SetParent(arg_21_0.UIOverlay.transform, false)

		arg_21_0.skipBtn = findTF(arg_21_0._tf, "front/btns/btns/skip_button")
		arg_21_0.autoBtn = findTF(arg_21_0._tf, "front/btns/btns/auto_button")
		arg_21_0.autoBtnImg = findTF(arg_21_0._tf, "front/btns/btns/auto_button/sel"):GetComponent(typeof(Image))
		arg_21_0.alphaImage = arg_21_0._tf:GetComponent(typeof(Image))
		arg_21_0.recordBtn = findTF(arg_21_0._tf, "front/btns/record")
		arg_21_0.dialogueContainer = findTF(arg_21_0._tf, "front/dialogue")
		arg_21_0.players = {
			AsideStoryPlayer.New(arg_22_0),
			DialogueStoryPlayer.New(arg_22_0),
			BgStoryPlayer.New(arg_22_0),
			CarouselPlayer.New(arg_22_0),
			VedioStoryPlayer.New(arg_22_0),
			CastStoryPlayer.New(arg_22_0)
		}
		arg_21_0.setSpeedPanel = StorySetSpeedPanel.New(arg_21_0._tf)
		arg_21_0.recordPanel = NewStoryRecordPanel.New()
		arg_21_0.recorder = StoryRecorder.New()

		setActive(arg_21_0._go, false)

		arg_21_0.state = var_0_2

		if arg_21_1 then
			arg_21_1()
		end
	end)
end

function var_0_0.Play(arg_23_0, arg_23_1, arg_23_2, arg_23_3, arg_23_4, arg_23_5, arg_23_6)
	table.insert(arg_23_0.playQueue, {
		arg_23_1,
		arg_23_2
	})

	if #arg_23_0.playQueue == 1 then
		local var_23_0

		local function var_23_1()
			if #arg_23_0.playQueue == 0 then
				return
			end

			local var_24_0 = arg_23_0.playQueue[1][1]
			local var_24_1 = arg_23_0.playQueue[1][2]

			arg_23_0:SoloPlay(var_24_0, function(arg_25_0, arg_25_1)
				if var_24_1 then
					var_24_1(arg_25_0, arg_25_1)
				end

				table.remove(arg_23_0.playQueue, 1)
				var_23_1()
			end, arg_23_3, arg_23_4, arg_23_5, arg_23_6)
		end

		var_23_1()
	end
end

function var_0_0.Puase(arg_26_0)
	if arg_26_0.state ~= var_0_3 then
		var_0_11("state is not 'running'")

		return
	end

	arg_26_0.state = var_0_4

	for iter_26_0, iter_26_1 in ipairs(arg_26_0.players) do
		iter_26_1:Pause()
	end
end

function var_0_0.Resume(arg_27_0)
	if arg_27_0.state ~= var_0_4 then
		var_0_11("state is not 'pause'")

		return
	end

	arg_27_0.state = var_0_3

	for iter_27_0, iter_27_1 in ipairs(arg_27_0.players) do
		iter_27_1:Resume()
	end
end

function var_0_0.Stop(arg_28_0)
	if arg_28_0.state ~= var_0_3 then
		var_0_11("state is not 'running'")

		return
	end

	arg_28_0.state = var_0_5

	for iter_28_0, iter_28_1 in ipairs(arg_28_0.players) do
		iter_28_1:Stop()
	end
end

function var_0_0.PlayForWorld(arg_29_0, arg_29_1, arg_29_2, arg_29_3, arg_29_4, arg_29_5, arg_29_6, arg_29_7)
	arg_29_0.optionSelCodes = arg_29_2 or {}
	arg_29_0.autoPlayFlag = arg_29_6

	arg_29_0:Play(arg_29_1, arg_29_3, arg_29_4, arg_29_5, arg_29_7, true)
end

function var_0_0.ForceAutoPlay(arg_30_0, arg_30_1, arg_30_2, arg_30_3, arg_30_4)
	arg_30_0.autoPlayFlag = true

	local function var_30_0(arg_31_0, arg_31_1)
		arg_30_2(arg_31_0, arg_31_1, arg_30_0.isAutoPlay)
	end

	arg_30_0:Play(arg_30_1, var_30_0, arg_30_3, arg_30_4, true)
end

function var_0_0.ForceManualPlay(arg_32_0, arg_32_1, arg_32_2, arg_32_3, arg_32_4)
	arg_32_0.banPlayFlag = true

	local function var_32_0(arg_33_0, arg_33_1)
		arg_32_2(arg_33_0, arg_33_1, arg_32_0.isAutoPlay)
	end

	arg_32_0:Play(arg_32_1, var_32_0, arg_32_3, arg_32_4, true)
end

function var_0_0.SeriesPlay(arg_34_0, arg_34_1, arg_34_2, arg_34_3, arg_34_4, arg_34_5, arg_34_6)
	local var_34_0 = {}

	for iter_34_0, iter_34_1 in ipairs(arg_34_1) do
		table.insert(var_34_0, function(arg_35_0)
			arg_34_0:SoloPlay(iter_34_1, arg_35_0, arg_34_3, arg_34_4, arg_34_5, arg_34_6)
		end)
	end

	seriesAsync(var_34_0, arg_34_2)
end

function var_0_0.SoloPlay(arg_36_0, arg_36_1, arg_36_2, arg_36_3, arg_36_4, arg_36_5, arg_36_6)
	var_0_11("Play Story:", arg_36_1)

	local var_36_0 = 1

	local function var_36_1(arg_37_0, arg_37_1)
		var_36_0 = var_36_0 - 1

		if arg_36_2 and var_36_0 == 0 then
			onNextTick(function()
				arg_36_2(arg_37_0, arg_37_1)
			end)
		end
	end

	local var_36_2 = var_0_13(arg_36_1)

	if not var_36_2 then
		var_36_1(false)
		var_0_11("not exist story file")

		return nil
	end

	if arg_36_0:IsReView() then
		arg_36_3 = true
	end

	arg_36_0.storyScript = Story.New(var_36_2, arg_36_3, arg_36_0.optionSelCodes, arg_36_5, arg_36_6)

	if not arg_36_0:CheckState() then
		var_0_11("story state error")
		var_36_1(false)

		return nil
	end

	if not arg_36_0.storyScript:CanPlay() then
		var_0_11("story cant be played")
		var_36_1(false)

		return nil
	end

	seriesAsync({
		function(arg_39_0)
			arg_36_0:CheckResDownload(arg_36_0.storyScript, arg_39_0)
		end,
		function(arg_40_0)
			originalPrint("start load story window...")
			arg_36_0:CheckAndLoadDialogue(arg_36_0.storyScript, arg_40_0)
		end
	}, function()
		originalPrint("enter story...")
		arg_36_0:OnStart()

		local var_41_0 = {}

		arg_36_0.currPlayer = nil

		for iter_41_0, iter_41_1 in ipairs(arg_36_0.storyScript.steps) do
			table.insert(var_41_0, function(arg_42_0)
				pg.m02:sendNotification(GAME.STORY_NEXT)

				local var_42_0 = arg_36_0.players[iter_41_1:GetMode()]

				arg_36_0.currPlayer = var_42_0

				var_42_0:Play(arg_36_0.storyScript, iter_41_0, arg_42_0)
			end)
		end

		seriesAsync(var_41_0, function()
			arg_36_0:OnEnd(var_36_1)
		end)
	end)
end

function var_0_0.CheckResDownload(arg_44_0, arg_44_1, arg_44_2)
	local var_44_0 = arg_44_0:_GetStoryPaintingsByName(arg_44_1)
	local var_44_1 = table.concat(var_44_0, ",")

	originalPrint("start download res " .. var_44_1)

	local var_44_2 = {}

	for iter_44_0, iter_44_1 in ipairs(var_44_0) do
		PaintingGroupConst.AddPaintingNameWithFilteMap(var_44_2, iter_44_1)
	end

	PaintingGroupConst.PaintingDownload({
		isShowBox = true,
		paintingNameList = var_44_2,
		finishFunc = arg_44_2
	})
end

local function var_0_15(arg_45_0, arg_45_1)
	ResourceMgr.Inst:getAssetAsync("ui/" .. arg_45_0, arg_45_0, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_46_0)
		arg_45_1(arg_46_0)
	end), true, true)
end

function var_0_0.CheckAndLoadDialogue(arg_47_0, arg_47_1, arg_47_2)
	local var_47_0 = arg_47_1:GetDialogueStyleName()

	if not arg_47_0.dialogueContainer:Find(var_47_0) then
		var_0_15("NewStoryDialogue" .. var_47_0, function(arg_48_0)
			Object.Instantiate(arg_48_0, arg_47_0.dialogueContainer).name = var_47_0

			arg_47_2()
		end)
	else
		arg_47_2()
	end
end

function var_0_0.CheckState(arg_49_0)
	if arg_49_0.state == var_0_3 or arg_49_0.state == var_0_1 or arg_49_0.state == var_0_4 then
		return false
	end

	return true
end

function var_0_0.RegistSkipBtn(arg_50_0)
	local function var_50_0()
		arg_50_0:TrackingSkip()
		arg_50_0.storyScript:SkipAll()
		arg_50_0.currPlayer:NextOneImmediately()
	end

	onButton(arg_50_0, arg_50_0.skipBtn, function()
		if arg_50_0:IsStopping() or arg_50_0:IsPausing() then
			return
		end

		if not arg_50_0.currPlayer:CanSkip() then
			return
		end

		if arg_50_0:IsReView() or arg_50_0.storyScript:IsPlayed() or not arg_50_0.storyScript:ShowSkipTip() then
			var_50_0()

			return
		end

		arg_50_0:Puase()

		arg_50_0.isOpenMsgbox = true

		pg.MsgboxMgr:GetInstance():ShowMsgBox({
			parent = rtf(arg_50_0._tf:Find("front")),
			content = i18n("story_skip_confirm"),
			onYes = function()
				arg_50_0:Resume()
				var_50_0()
			end,
			onNo = function()
				arg_50_0.isOpenMsgbox = false

				arg_50_0:Resume()
			end,
			weight = LayerWeightConst.TOP_LAYER
		})
	end, SFX_PANEL)
end

function var_0_0.RegistAutoBtn(arg_55_0)
	onButton(arg_55_0, arg_55_0.autoBtn, function()
		if arg_55_0:IsStopping() or arg_55_0:IsPausing() then
			return
		end

		if arg_55_0.storyScript:GetAutoPlayFlag() then
			arg_55_0.storyScript:StopAutoPlay()
			arg_55_0.currPlayer:CancelAuto()
		else
			arg_55_0.storyScript:SetAutoPlay()
			arg_55_0.currPlayer:NextOne()
		end

		if arg_55_0.storyScript then
			arg_55_0:UpdateAutoBtn()
		end
	end, SFX_PANEL)

	local var_55_0 = arg_55_0:IsAutoPlay()

	if var_55_0 then
		arg_55_0.storyScript:SetAutoPlay()
		arg_55_0:UpdateAutoBtn()

		arg_55_0.autoPlayFlag = false
	end

	arg_55_0.banPlayFlag = false
	arg_55_0.isAutoPlay = var_55_0
end

function var_0_0.RegistRecordBtn(arg_57_0)
	onButton(arg_57_0, arg_57_0.recordBtn, function()
		if arg_57_0.storyScript:GetAutoPlayFlag() then
			return
		end

		if not arg_57_0.recordPanel:CanOpen() then
			return
		end

		local var_58_0 = "Show"

		arg_57_0.recordPanel[var_58_0](arg_57_0.recordPanel, arg_57_0.recorder)
	end, SFX_PANEL)
end

function var_0_0.TriggerAutoBtn(arg_59_0)
	if not arg_59_0:IsRunning() then
		return
	end

	triggerButton(arg_59_0.autoBtn)
end

function var_0_0.TriggerSkipBtn(arg_60_0)
	if not arg_60_0:IsRunning() then
		return
	end

	triggerButton(arg_60_0.skipBtn)
end

function var_0_0.ForEscPress(arg_61_0)
	if arg_61_0.recordPanel:IsShowing() then
		arg_61_0.recordPanel:Hide()
	else
		arg_61_0:TriggerSkipBtn()
	end
end

function var_0_0.UpdatePlaySpeed(arg_62_0, arg_62_1)
	if arg_62_0:IsRunning() and arg_62_0.storyScript then
		arg_62_0.storyScript:SetPlaySpeed(arg_62_1)
	end
end

function var_0_0.GetPlaySpeed(arg_63_0)
	if arg_63_0:IsRunning() and arg_63_0.storyScript then
		return arg_63_0.storyScript:GetPlaySpeed()
	end
end

function var_0_0.OnStart(arg_64_0)
	arg_64_0.recorder:Clear()
	removeOnButton(arg_64_0._go)
	removeOnButton(arg_64_0.skipBtn)
	removeOnButton(arg_64_0.autoBtn)
	removeOnButton(arg_64_0.recordBtn)

	arg_64_0.alphaImage.color = Color(0, 0, 0, arg_64_0.storyScript:GetStoryAlpha())

	setActive(arg_64_0.recordBtn, not arg_64_0.storyScript:ShouldHideRecord())
	arg_64_0:ClearStoryEventTriggerListener()

	local var_64_0 = arg_64_0.storyScript:GetAllStepDispatcherRecallName()

	if #var_64_0 > 0 then
		arg_64_0.storyEventTriggerListener = StoryEventTriggerListener.New(var_64_0)
	end

	arg_64_0.state = var_0_3

	arg_64_0:TrackingStart()
	pg.m02:sendNotification(GAME.STORY_BEGIN, arg_64_0.storyScript:GetName())
	pg.m02:sendNotification(GAME.STORY_UPDATE, {
		storyId = arg_64_0.storyScript:GetName()
	})
	pg.DelegateInfo.New(arg_64_0)

	for iter_64_0, iter_64_1 in ipairs(arg_64_0.players) do
		iter_64_1:StoryStart(arg_64_0.storyScript)
	end

	setActive(arg_64_0._go, true)
	arg_64_0._tf:SetAsLastSibling()
	setActive(arg_64_0.skipBtn, not arg_64_0.storyScript:ShouldHideSkip())
	setActive(arg_64_0.autoBtn, not arg_64_0.storyScript:ShouldHideAutoBtn())

	arg_64_0.bgmVolumeValue = pg.CriMgr.GetInstance():getBGMVolume()

	arg_64_0:RegistSkipBtn()
	arg_64_0:RegistAutoBtn()
	arg_64_0:RegistRecordBtn()
end

function var_0_0.TrackingStart(arg_65_0)
	arg_65_0.trackFlag = false

	if not arg_65_0.storyScript then
		return
	end

	local var_65_0 = arg_65_0:StoryName2StoryId(arg_65_0.storyScript:GetName())

	if not arg_65_0:GetPlayedFlag(var_65_0) then
		TrackConst.StoryStart(var_65_0)

		arg_65_0.trackFlag = true
	end
end

function var_0_0.TrackingSkip(arg_66_0)
	if not arg_66_0.trackFlag or not arg_66_0.storyScript then
		return
	end

	local var_66_0 = arg_66_0:StoryName2StoryId(arg_66_0.storyScript:GetName())

	TrackConst.StorySkip(var_66_0)
end

function var_0_0.ClearStoryEvent(arg_67_0)
	if arg_67_0.storyEventTriggerListener then
		arg_67_0.storyEventTriggerListener:Clear()
	end
end

function var_0_0.CheckStoryEvent(arg_68_0, arg_68_1)
	if arg_68_0.storyEventTriggerListener then
		return arg_68_0.storyEventTriggerListener:ExistCache(arg_68_1)
	end

	return false
end

function var_0_0.GetStoryEventArg(arg_69_0, arg_69_1)
	if not arg_69_0:CheckStoryEvent(arg_69_1) then
		return nil
	end

	if arg_69_0.storyEventTriggerListener and arg_69_0.storyEventTriggerListener:ExistArg(arg_69_1) then
		return arg_69_0.storyEventTriggerListener:GetArg(arg_69_1)
	end

	return nil
end

function var_0_0.UpdateAutoBtn(arg_70_0)
	local var_70_0 = arg_70_0.storyScript:GetAutoPlayFlag()

	arg_70_0:ClearAutoBtn(var_70_0)
end

function var_0_0.ClearAutoBtn(arg_71_0, arg_71_1)
	arg_71_0.autoBtnImg.color = arg_71_1 and var_0_8 or var_0_9
	arg_71_0.isAutoPlay = arg_71_1

	local var_71_0 = arg_71_1 and "Show" or "Hide"

	arg_71_0.setSpeedPanel[var_71_0](arg_71_0.setSpeedPanel)
end

function var_0_0.ClearStoryEventTriggerListener(arg_72_0)
	if arg_72_0.storyEventTriggerListener then
		arg_72_0.storyEventTriggerListener:Dispose()

		arg_72_0.storyEventTriggerListener = nil
	end
end

function var_0_0.Clear(arg_73_0)
	arg_73_0:ClearStoryEventTriggerListener()
	arg_73_0.recorder:Clear()
	arg_73_0.recordPanel:Hide()

	arg_73_0.autoPlayFlag = false
	arg_73_0.banPlayFlag = false

	removeOnButton(arg_73_0._go)
	removeOnButton(arg_73_0.skipBtn)
	removeOnButton(arg_73_0.recordBtn)
	removeOnButton(arg_73_0.autoBtn)
	arg_73_0:ClearAutoBtn(false)

	if isActive(arg_73_0._go) then
		pg.DelegateInfo.Dispose(arg_73_0)
	end

	if arg_73_0.setSpeedPanel then
		arg_73_0.setSpeedPanel:Clear()
	end

	setActive(arg_73_0.skipBtn, false)
	setActive(arg_73_0._go, false)

	for iter_73_0, iter_73_1 in ipairs(arg_73_0.players) do
		iter_73_1:StoryEnd(arg_73_0.storyScript)
	end

	arg_73_0.optionSelCodes = nil

	pg.BgmMgr.GetInstance():ContinuePlay()
	pg.m02:sendNotification(GAME.STORY_END)

	if arg_73_0.isOpenMsgbox then
		pg.MsgboxMgr:GetInstance():hide()
	end

	local var_73_0 = pg.CriMgr.GetInstance():getBGMVolume()

	if arg_73_0.bgmVolumeValue and arg_73_0.bgmVolumeValue ~= var_73_0 then
		pg.CriMgr.GetInstance():setBGMVolume(arg_73_0.bgmVolumeValue)
	end

	arg_73_0.bgmVolumeValue = nil
end

function var_0_0.OnEnd(arg_74_0, arg_74_1)
	arg_74_0:Clear()

	if arg_74_0.state == var_0_3 or arg_74_0.state == var_0_5 then
		arg_74_0.state = var_0_6

		local var_74_0 = arg_74_0.storyScript:GetNextScriptName()

		if var_74_0 and not arg_74_0:IsReView() then
			arg_74_0.storyScript = nil

			arg_74_0:Play(var_74_0, arg_74_1)
		else
			local var_74_1 = arg_74_0.storyScript:GetBranchCode()

			arg_74_0.storyScript = nil

			if arg_74_1 then
				arg_74_1(true, var_74_1)
			end
		end
	else
		arg_74_0.state = var_0_6

		local var_74_2 = arg_74_0.storyScript:GetBranchCode()

		if arg_74_1 then
			arg_74_1(true, var_74_2)
		end
	end
end

function var_0_0.OnSceneEnter(arg_75_0, arg_75_1)
	if not arg_75_0.scenes then
		arg_75_0.scenes = {}
	end

	arg_75_0.scenes[arg_75_1.view] = true
end

function var_0_0.OnSceneExit(arg_76_0, arg_76_1)
	if not arg_76_0.scenes then
		return
	end

	arg_76_0.scenes[arg_76_1.view] = nil
end

function var_0_0.IsReView(arg_77_0)
	local var_77_0 = getProxy(ContextProxy):GetPrevContext(1)

	return arg_77_0.scenes[WorldMediaCollectionScene.__cname] == true or var_77_0 and var_77_0.mediator == WorldMediaCollectionMediator
end

function var_0_0.IsRunning(arg_78_0)
	return arg_78_0.state == var_0_3
end

function var_0_0.IsStopping(arg_79_0)
	return arg_79_0.state == var_0_5
end

function var_0_0.IsPausing(arg_80_0)
	return arg_80_0.state == var_0_4
end

function var_0_0.IsAutoPlay(arg_81_0)
	if arg_81_0.banPlayFlag then
		return false
	end

	return getProxy(SettingsProxy):GetStoryAutoPlayFlag() or arg_81_0.autoPlayFlag == true
end

function var_0_0.GetRectSize(arg_82_0)
	return Vector2(arg_82_0._tf.rect.width, arg_82_0._tf.rect.height)
end

function var_0_0.AddRecord(arg_83_0, arg_83_1)
	arg_83_0.recorder:Add(arg_83_1)
end

function var_0_0.Quit(arg_84_0)
	arg_84_0.recorder:Dispose()
	arg_84_0.recordPanel:Dispose()
	arg_84_0.setSpeedPanel:Dispose()

	arg_84_0.state = var_0_7
	arg_84_0.storyScript = nil
	arg_84_0.playQueue = {}
	arg_84_0.playedList = {}
	arg_84_0.scenes = {}
end

function var_0_0.Fix(arg_85_0)
	local var_85_0 = getProxy(PlayerProxy):getRawData():GetRegisterTime()
	local var_85_1 = pg.TimeMgr.GetInstance():parseTimeFromConfig({
		{
			2021,
			4,
			8
		},
		{
			9,
			0,
			0
		}
	})
	local var_85_2 = {
		10020,
		10021,
		10022,
		10023,
		10024,
		10025,
		10026,
		10027
	}

	if var_85_0 <= var_85_1 then
		_.each(var_85_2, function(arg_86_0)
			arg_85_0.playedList[arg_86_0] = true
		end)
	end

	local var_85_3 = 5001
	local var_85_4 = 5020
	local var_85_5 = getProxy(TaskProxy)
	local var_85_6 = 0

	for iter_85_0 = var_85_3, var_85_4, -1 do
		if var_85_5:getFinishTaskById(iter_85_0) or var_85_5:getTaskById(iter_85_0) then
			var_85_6 = iter_85_0

			break
		end
	end

	for iter_85_1 = var_85_6, var_85_4, -1 do
		local var_85_7 = pg.task_data_template[iter_85_1]

		if var_85_7 then
			local var_85_8 = var_85_7.story_id

			if var_85_8 and #var_85_8 > 0 and not arg_85_0:IsPlayed(var_85_8) then
				arg_85_0.playedList[var_85_8] = true
			end
		end
	end

	local var_85_9 = getProxy(ActivityProxy):getActivityById(ActivityConst.JYHZ_ACTIVITY_ID)

	if var_85_9 and not var_85_9:isEnd() then
		local var_85_10 = _.flatten(var_85_9:getConfig("config_data"))
		local var_85_11

		for iter_85_2 = #var_85_10, 1, -1 do
			local var_85_12 = pg.task_data_template[var_85_10[iter_85_2]].story_id

			if var_85_12 and #var_85_12 > 0 then
				local var_85_13 = arg_85_0:IsPlayed(var_85_12)

				if var_85_11 then
					if not var_85_13 then
						arg_85_0.playedList[var_85_12] = true
					end
				elseif var_85_13 then
					var_85_11 = iter_85_2
				end
			end
		end
	end
end
