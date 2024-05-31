﻿local var_0_0 = class("CastleMainScene", import("..base.BaseUI"))

var_0_0.optionsPath = {
	"main/top/btn_home"
}

local var_0_1 = "name"
local var_0_2 = "default_value"
local var_0_3 = "random_value"

var_0_0.ACT_ID = ActivityConst.CASTLE_ACT_ID
var_0_0.AWARD_ACT_ID = ActivityConst.CASTLE_AWARD_ID
var_0_0.SKILL_COLOR = {
	"#546190",
	"#835490",
	"#A57D55",
	"#C15348"
}
var_0_0.BAD_FILL_COLOR = Color(0.6588235294117647, 0.5019607843137255, 0.4823529411764706, 0.5)
var_0_0.NORMAL_FILL_COLOR = Color(1, 1, 1, 0.5)
var_0_0.TRANSPARENT_COLOR = Color(1, 1, 1, 0)
var_0_0.MARK_CURRENT = "1"
var_0_0.MARK_UNEXPLORED = "2"
var_0_0.MARK_BAD = "3"
var_0_0.MARK_EXPLORABLE = "4"
var_0_0.MAP_POS = {
	1,
	2,
	3,
	3,
	4,
	5,
	5,
	6,
	7,
	7,
	8,
	9,
	9,
	10,
	11,
	11,
	12,
	13,
	13,
	14,
	15,
	15,
	17,
	16
}
var_0_0.ROOM_NUM = 17
var_0_0.WALK_SE = "event:/ui/castle_walk"
var_0_0.ROLL_SE = "event:/ui/caslte_roll"
var_0_0.CARD_SE = "event:/ui/huihua1"

function var_0_0.getUIName(arg_1_0)
	return "CastleMainUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:InitData()
	arg_2_0:InitTF()
	arg_2_0:InitAward()
	arg_2_0:InitCharacter()
	arg_2_0:InitDice()
	arg_2_0:InitVX()
end

function var_0_0.InitTF(arg_3_0)
	arg_3_0.main = arg_3_0:findTF("main")
	arg_3_0.map = arg_3_0:findTF("map", arg_3_0.main)
	arg_3_0.floors = {
		arg_3_0:findTF("floor1", arg_3_0.map),
		arg_3_0:findTF("floor2", arg_3_0.map)
	}
	arg_3_0.rooms = {
		arg_3_0:findTF("rooms", arg_3_0.floors[1]),
		arg_3_0:findTF("rooms", arg_3_0.floors[2])
	}
	arg_3_0.top = arg_3_0:findTF("top", arg_3_0.main)
	arg_3_0.buttonBack = arg_3_0:findTF("btn_back", arg_3_0.top)
	arg_3_0.buttonHelp = arg_3_0:findTF("btn_help", arg_3_0.top)
	arg_3_0.buttonAward = arg_3_0:findTF("btn_award", arg_3_0.top)
	arg_3_0.buttonCharacter = arg_3_0:findTF("btn_character", arg_3_0.top)
	arg_3_0.buttonDice = arg_3_0:findTF("btn_dice", arg_3_0.top)
	arg_3_0.diceRes = arg_3_0:findTF("dice_res", arg_3_0.buttonDice)
	arg_3_0.button1F = arg_3_0:findTF("btn_1F", arg_3_0.top)
	arg_3_0.button2F = arg_3_0:findTF("btn_2F", arg_3_0.top)
	arg_3_0.window = arg_3_0:findTF("window")
end

function var_0_0.InitData(arg_4_0)
	arg_4_0.storyMgr = pg.NewStoryMgr.GetInstance()
	arg_4_0.activity = getProxy(ActivityProxy):getActivityById(var_0_0.ACT_ID)
	arg_4_0.story2Map = {}
	arg_4_0.map2Story = {}
	arg_4_0.storyGroup = {}

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.activity:getConfig("config_data")[3]) do
		table.insert(arg_4_0.storyGroup, iter_4_1[1][1])
		table.insert(arg_4_0.storyGroup, iter_4_1[2][2])
		table.insert(arg_4_0.storyGroup, iter_4_1[2][1])
	end

	for iter_4_2 = 1, var_0_0.ROOM_NUM do
		table.insert(arg_4_0.map2Story, {})
	end

	for iter_4_3 = 1, #arg_4_0.storyGroup do
		table.insert(arg_4_0.story2Map, arg_4_0.storyGroup[iter_4_3], var_0_0.MAP_POS[iter_4_3])
		table.insert(arg_4_0.map2Story[var_0_0.MAP_POS[iter_4_3]], arg_4_0.storyGroup[iter_4_3])
	end

	arg_4_0.explorableStories = {}
	arg_4_0.exploredStories = {}

	if arg_4_0.activity.data1 ~= nil and arg_4_0.activity.data1 ~= 0 then
		for iter_4_4 = 1, #arg_4_0.storyGroup do
			table.insert(arg_4_0:IsPlayed(arg_4_0.storyGroup[iter_4_4]) and arg_4_0.exploredStories or arg_4_0.explorableStories, arg_4_0.storyGroup[iter_4_4])

			if arg_4_0.storyGroup[iter_4_4] == arg_4_0.activity.data1 then
				break
			end
		end
	end

	arg_4_0.explorablePos = arg_4_0.activity.data1
	arg_4_0.currentPos = #arg_4_0.exploredStories == 0 and 0 or arg_4_0.exploredStories[#arg_4_0.exploredStories]
end

function var_0_0.InitAward(arg_5_0)
	arg_5_0.awardWindow = arg_5_0:findTF("award_window", arg_5_0.window)
	arg_5_0.buttonAwardGet = arg_5_0:findTF("award_bg/btn_get", arg_5_0.awardWindow)
	arg_5_0.awardWindowBg = arg_5_0:findTF("bg", arg_5_0.awardWindow)
	arg_5_0.awardItem = arg_5_0:findTF("award_bg/mask/item", arg_5_0.awardWindow)
	arg_5_0.awardItems = arg_5_0:findTF("award_bg/mask/content", arg_5_0.awardWindow)
	arg_5_0.awardActivity = getProxy(ActivityProxy):getActivityById(var_0_0.AWARD_ACT_ID)
	arg_5_0.taskProxy = getProxy(TaskProxy)
	arg_5_0.taskGroup = arg_5_0.awardActivity:getConfig("config_data")
	arg_5_0.taskList = UIItemList.New(arg_5_0.awardItems, arg_5_0.awardItem)
	arg_5_0.taskMap = {}

	for iter_5_0 = 1, #arg_5_0.taskGroup do
		table.insert(arg_5_0.taskMap, iter_5_0)
	end
end

function var_0_0.InitDice(arg_6_0)
	arg_6_0.diceWindow = arg_6_0:findTF("dice_window", arg_6_0.window)
	arg_6_0.buttonDiceContinue = arg_6_0:findTF("btn_continue", arg_6_0.diceWindow)
	arg_6_0.dice = arg_6_0:findTF("dice", arg_6_0.diceWindow)
	arg_6_0.dices = {
		arg_6_0:findTF("dice1", arg_6_0.dice),
		arg_6_0:findTF("dice2", arg_6_0.dice)
	}
	arg_6_0.result = arg_6_0:findTF("result", arg_6_0.diceWindow)
	arg_6_0.success = arg_6_0:findTF("success", arg_6_0.result)
	arg_6_0.criticalSuccess = arg_6_0:findTF("critical_success", arg_6_0.result)
	arg_6_0.failure = arg_6_0:findTF("failure", arg_6_0.result)
	arg_6_0.criticalFailure = arg_6_0:findTF("critical_failure", arg_6_0.result)
end

function var_0_0.InitCharacter(arg_7_0)
	arg_7_0.characterWindow = arg_7_0:findTF("character_window", arg_7_0.window)
	arg_7_0.characterWindowBg = arg_7_0:findTF("bg", arg_7_0.characterWindow)
	arg_7_0.characterCard = arg_7_0:findTF("character_card", arg_7_0.characterWindowBg)
	arg_7_0.characterName = arg_7_0:findTF("title_base/name", arg_7_0.characterCard)
	arg_7_0.profession = arg_7_0:findTF("title_base/profession", arg_7_0.characterCard)
	arg_7_0.nameInput = arg_7_0:findTF("InputField", arg_7_0.characterName)
	arg_7_0.attrGroup = arg_7_0:findTF("title_attr/attrGroup", arg_7_0.characterCard)
	arg_7_0.skillGroup = arg_7_0:findTF("title_skill/skillGroup", arg_7_0.characterCard)
	arg_7_0.characterTip = arg_7_0:findTF("tip", arg_7_0.characterCard)

	setText(arg_7_0.characterTip, i18n("roll_unlock"))

	arg_7_0.buttonRandom = arg_7_0:findTF("random", arg_7_0.characterCard)
	arg_7_0.randomLock = arg_7_0:findTF("lock", arg_7_0.buttonRandom)
	arg_7_0.randomText = arg_7_0:findTF("Image", arg_7_0.buttonRandom)

	setText(arg_7_0:findTF("title_base", arg_7_0.characterCard), i18n("roll_card_info"))
	setText(arg_7_0:findTF("title_attr", arg_7_0.characterCard), i18n("roll_card_attr"))
	setText(arg_7_0:findTF("title_skill", arg_7_0.characterCard), i18n("roll_card_skill"))

	local var_7_0 = arg_7_0.activity:getConfig("config_client")[2]

	arg_7_0.story2Attr = {}

	for iter_7_0, iter_7_1 in ipairs(var_7_0) do
		table.insert(arg_7_0.story2Attr, iter_7_1[1], iter_7_1[2])
	end

	arg_7_0.attrLock = {}
end

function var_0_0.InitVX(arg_8_0)
	for iter_8_0, iter_8_1 in ipairs({
		"success",
		"Csuccess",
		"failure",
		"Cfailure"
	}) do
		local var_8_0 = arg_8_0.result:GetChild(iter_8_0 - 1)
		local var_8_1 = findTF(var_8_0, iter_8_1)
		local var_8_2 = findTF(var_8_0, "VX/glow")

		setLocalScale(var_8_2, {
			x = var_8_1.rect.width,
			y = var_8_1.rect.height
		})
	end
end

function var_0_0.didEnter(arg_9_0)
	for iter_9_0 = 1, var_0_0.ROOM_NUM do
		local var_9_0 = arg_9_0:GetRoomTF(iter_9_0)
		local var_9_1 = findTF(var_9_0, "name")

		setText(var_9_1, i18n("roll_room_unexplored"))

		local var_9_2 = findTF(var_9_0, "explorable")

		setImageRaycastTarget(findTF(var_9_0, "fill"), true)
		onButton(arg_9_0, var_9_0, function()
			for iter_10_0, iter_10_1 in ipairs(arg_9_0.map2Story[iter_9_0]) do
				if table.contains(arg_9_0.explorableStories, iter_10_1) then
					arg_9_0:PlayStory(iter_10_1)

					break
				end
			end
		end, SFX_PANEL)
	end

	if table.contains(arg_9_0.explorableStories, arg_9_0.storyGroup[15]) or table.contains(arg_9_0.exploredStories, arg_9_0.storyGroup[15]) then
		local var_9_3

		for iter_9_1 = #arg_9_0.exploredStories, 1, -1 do
			if not arg_9_0:IsBadEnd(arg_9_0.exploredStories[iter_9_1]) then
				var_9_3 = arg_9_0.exploredStories[iter_9_1]

				break
			end
		end

		local var_9_4 = var_9_3 and arg_9_0.story2Map[var_9_3] or 0
		local var_9_5 = var_9_4 > 10 and var_9_4 < 17

		setActive(arg_9_0.floors[1], not var_9_5)
		setActive(arg_9_0.floors[2], var_9_5)
		setActive(arg_9_0.button1F, not var_9_5)
		setActive(arg_9_0.button2F, var_9_5)
	else
		setActive(arg_9_0.button1F, false)
		setActive(arg_9_0.button2F, false)
	end

	arg_9_0.taskList:make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate then
			arg_9_0:UpdateTask(arg_11_1, arg_11_2)
		end
	end)
	arg_9_0.nameInput:GetComponent(typeof(InputField)).onValueChanged:AddListener(function()
		if not nameValidityCheck(getInputText(arg_9_0.nameInput), 0, 40, {
			"spece_illegal_tip",
			"login_newPlayerScene_name_tooShort",
			"ship_renameShip_error_2011",
			"playerinfo_mask_word"
		}) then
			setInputText(arg_9_0.nameInput, getProxy(PlayerProxy):getData().name)
		end
	end)
	arg_9_0:InitButton()
	arg_9_0:UpdateFlush()

	local var_9_6 = arg_9_0.activity:getConfig("config_data")[1]

	if var_9_6 and not arg_9_0:IsPlayed(var_9_6) then
		arg_9_0:emit(CastleMainMediator.CASTLE_ACT_OP, {
			cmd = 3,
			id = var_0_0.ACT_ID,
			arg1 = var_9_6
		})
	else
		arg_9_0:CheckGuide()
	end
end

function var_0_0.InitButton(arg_13_0)
	onButton(arg_13_0, arg_13_0.button1F, function()
		setActive(arg_13_0.button1F, false)
		setActive(arg_13_0.button2F, true)
		setActive(arg_13_0.floors[2], true)
		setActive(arg_13_0.floors[1], false)
	end, var_0_0.WALK_SE)
	onButton(arg_13_0, arg_13_0.button2F, function()
		setActive(arg_13_0.button2F, false)
		setActive(arg_13_0.button1F, true)
		setActive(arg_13_0.floors[1], true)
		setActive(arg_13_0.floors[2], false)
	end, var_0_0.WALK_SE)
	onButton(arg_13_0, arg_13_0.buttonBack, function()
		arg_13_0:closeView()
	end, SFX_CANCEL)
	onButton(arg_13_0, arg_13_0.buttonHelp, function()
		local var_17_0 = i18n("roll_gametip")

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = var_17_0
		})
	end, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.buttonAward, function()
		setActive(arg_13_0.awardWindow, true)
		arg_13_0:CheckAwardGet()
		arg_13_0:ExplorableEffect(false)
	end, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.buttonAwardGet, function()
		local var_19_0 = underscore(arg_13_0.taskGroup):chain():map(function(arg_20_0)
			return arg_13_0.taskProxy:getTaskVO(arg_20_0)
		end):filter(function(arg_21_0)
			return arg_21_0:getTaskStatus() == 1
		end):value()

		if #var_19_0 > 0 then
			arg_13_0:emit(CastleMainMediator.ON_TASK_SUBMIT, var_19_0)
		end
	end, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.awardWindowBg, function()
		setActive(arg_13_0.awardWindow, false)
		arg_13_0:ExplorableEffect(true)
	end, SFX_CANCEL)
	onButton(arg_13_0, arg_13_0.buttonCharacter, function()
		arg_13_0:UpdateCard()
		setActive(arg_13_0.characterWindow, true)
		pg.UIMgr.GetInstance():BlurPanel(arg_13_0.characterCard)
	end, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.characterWindowBg, function()
		setActive(arg_13_0.characterWindow, false)
		pg.UIMgr.GetInstance():UnblurPanel(arg_13_0.characterCard, arg_13_0.characterWindowBg)
		arg_13_0:UpdateFlush()
		arg_13_0:CheckGuide()
	end, SFX_CANCEL)
	onButton(arg_13_0, arg_13_0.buttonRandom, function()
		if arg_13_0:IsFinish() then
			if #getInputText(arg_13_0.nameInput) == 0 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("roll_noname"))
			else
				arg_13_0:RollCharacterCard()
			end
		end
	end, SFX_CANCEL)
	onButton(arg_13_0, arg_13_0.buttonDice, function()
		if arg_13_0.diceCount < 1 then
			if table.contains(arg_13_0.explorableStories, arg_13_0.storyGroup[23]) or table.contains(arg_13_0.explorableStories, arg_13_0.storyGroup[24]) then
				pg.TipsMgr.GetInstance():ShowTips(i18n("roll_ending_tip1"))
			elseif table.contains(arg_13_0.exploredStories, arg_13_0.storyGroup[23]) and table.contains(arg_13_0.exploredStories, arg_13_0.storyGroup[24]) then
				pg.TipsMgr.GetInstance():ShowTips(i18n("roll_ending_tip2"))
			else
				pg.TipsMgr.GetInstance():ShowTips(i18n("roll_notimes"))
			end

			return
		end

		if arg_13_0:IndexofStory(arg_13_0.explorablePos) > arg_13_0:IndexofStory(arg_13_0.currentPos) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("roll_tip2"))

			return
		end

		arg_13_0:emit(CastleMainMediator.CASTLE_ACT_OP, {
			cmd = 1,
			id = var_0_0.ACT_ID
		})
	end, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.buttonDiceContinue, function()
		setActive(arg_13_0.diceWindow, false)
		arg_13_0:UpdateFlush()
		arg_13_0:CheckGuide()
		arg_13_0:ExplorableEffect(true)
	end, SFX_PANEL)
end

function var_0_0.UpdateFlush(arg_28_0)
	arg_28_0.activity = getProxy(ActivityProxy):getActivityById(var_0_0.ACT_ID)
	arg_28_0.awardActivity = getProxy(ActivityProxy):getActivityById(var_0_0.AWARD_ACT_ID)
	arg_28_0.taskGroup = arg_28_0.awardActivity:getConfig("config_data")

	arg_28_0:UpdateDice()
	arg_28_0:UpdateMap()
	arg_28_0:UpdateAward()
	arg_28_0:UpdateCharacter()

	if arg_28_0:IndexofStory(arg_28_0.explorablePos) == 15 and arg_28_0:IndexofStory(arg_28_0.explorablePos) > arg_28_0:IndexofStory(arg_28_0.currentPos) then
		setActive(arg_28_0.button1F, true)
	end

	setActive(arg_28_0.buttonDice, not arg_28_0:IsFinish())
end

function var_0_0.UpdateDice(arg_29_0)
	arg_29_0.diceCount = arg_29_0.activity.data2

	if table.contains(arg_29_0.explorableStories, arg_29_0.explorablePos) and arg_29_0:IsBadEnd(arg_29_0.explorablePos) then
		arg_29_0.diceCount = arg_29_0.diceCount - 1
	end

	setText(arg_29_0.diceRes, i18n("roll_times_left", arg_29_0.diceCount))

	if arg_29_0.explorablePos == arg_29_0.currentPos and arg_29_0.diceCount > 0 then
		arg_29_0.buttonDice:GetComponent(typeof(Animation)):Play("anim_castle_dice_tiploop")
	else
		arg_29_0.buttonDice:GetComponent(typeof(Animation)):Stop()
	end
end

function var_0_0.UpdateMap(arg_30_0)
	for iter_30_0 = 1, var_0_0.ROOM_NUM do
		arg_30_0:ChangeRoomColor(iter_30_0, var_0_0.TRANSPARENT_COLOR)
		arg_30_0:ChangeRoomMark(iter_30_0, nil)
	end

	for iter_30_1, iter_30_2 in ipairs(arg_30_0.exploredStories) do
		local var_30_0 = arg_30_0.story2Map[iter_30_2]
		local var_30_1 = arg_30_0:GetRoomTF(var_30_0)

		setText(findTF(var_30_1, "name"), i18n("roll_room" .. var_30_0))
	end

	setActive(findTF(arg_30_0.main, "finish_mask"), false)

	if arg_30_0:IsFinish() then
		setActive(findTF(arg_30_0.main, "finish_mask"), true)

		return
	end

	for iter_30_3, iter_30_4 in ipairs(arg_30_0.exploredStories) do
		local var_30_2 = arg_30_0.story2Map[iter_30_4]

		if arg_30_0:IsBadEnd(iter_30_4) then
			if var_30_2 ~= 17 then
				if var_30_2 ~= 4 then
					arg_30_0:ChangeRoomColor(var_30_2, var_0_0.BAD_FILL_COLOR)
				end

				arg_30_0:ChangeRoomMark(var_30_2, var_0_0.MARK_BAD)
			end
		else
			arg_30_0:ChangeRoomColor(var_30_2, var_0_0.NORMAL_FILL_COLOR)
		end
	end

	for iter_30_5, iter_30_6 in ipairs(arg_30_0.explorableStories) do
		local var_30_3 = arg_30_0.story2Map[iter_30_6]

		arg_30_0:ChangeRoomMark(var_30_3, var_0_0.MARK_EXPLORABLE)
		arg_30_0:ChangeRoomMark(var_30_3, var_0_0.MARK_UNEXPLORED, true)
	end

	if #arg_30_0.exploredStories > 0 then
		local var_30_4

		for iter_30_7, iter_30_8 in ipairs(arg_30_0.storyGroup) do
			if not arg_30_0:IsBadEnd(iter_30_8) and table.contains(arg_30_0.exploredStories, iter_30_8) then
				var_30_4 = iter_30_8
			end
		end

		arg_30_0:ChangeRoomMark(arg_30_0.story2Map[var_30_4], var_0_0.MARK_CURRENT, true)
	end

	setActive(arg_30_0.button1F:Find("Image"), table.contains(arg_30_0.explorableStories, arg_30_0.storyGroup[24]))
	setActive(arg_30_0.button2F:Find("Image"), table.contains(arg_30_0.explorableStories, arg_30_0.storyGroup[23]))
end

function var_0_0.UpdateAward(arg_31_0)
	arg_31_0:CheckAwardGet()
	table.sort(arg_31_0.taskMap, function(arg_32_0, arg_32_1)
		local var_32_0 = arg_31_0.taskProxy:getTaskVO(arg_31_0.taskGroup[arg_32_0]):getTaskStatus() == 2 and 1 or 0
		local var_32_1 = arg_31_0.taskProxy:getTaskVO(arg_31_0.taskGroup[arg_32_1]):getTaskStatus() == 2 and 1 or 0

		if var_32_0 == var_32_1 then
			return arg_32_0 < arg_32_1
		end

		return var_32_0 < var_32_1
	end)
	arg_31_0.taskList:align(#arg_31_0.taskGroup)

	local var_31_0 = arg_31_0.storyMgr:StoryId2StoryName(arg_31_0.activity:getConfig("config_client")[1][3])

	if not arg_31_0:IsPlayed(var_31_0) and getProxy(TaskProxy):isReceiveTasks(arg_31_0.taskGroup) then
		playStory(var_31_0)
	end
end

function var_0_0.UpdateCharacter(arg_33_0)
	setActive(arg_33_0.randomLock, not arg_33_0:IsFinish())
	setActive(arg_33_0.randomText, arg_33_0:IsFinish())

	arg_33_0.nameInput:GetComponent(typeof(InputField)).interactable = arg_33_0:IsFinish()

	setActive(arg_33_0:findTF("edit", arg_33_0.characterName), arg_33_0:IsFinish())
end

function var_0_0.UpdateTask(arg_34_0, arg_34_1, arg_34_2)
	local var_34_0 = arg_34_0.taskMap[arg_34_1 + 1]
	local var_34_1 = arg_34_0:findTF("IconTpl", arg_34_2)
	local var_34_2 = arg_34_0.taskGroup[var_34_0]
	local var_34_3 = arg_34_0.taskProxy:getTaskVO(var_34_2)

	assert(var_34_3, "without this task by id: " .. var_34_2)
	setText(arg_34_0:findTF("title", arg_34_2), i18n("roll_reward_word" .. var_34_0))

	local var_34_4 = var_34_3:getConfig("award_display")[1]
	local var_34_5 = {
		type = var_34_4[1],
		id = var_34_4[2],
		count = var_34_4[3]
	}

	updateDrop(var_34_1, var_34_5)
	onButton(arg_34_0, var_34_1, function()
		arg_34_0:emit(BaseUI.ON_DROP, var_34_5)
	end, SFX_PANEL)

	local var_34_6 = var_34_3:getProgress()
	local var_34_7 = var_34_3:getConfig("target_num")

	setText(arg_34_0:findTF("progress", arg_34_2), i18n("roll_reward_tip", var_34_6, var_34_7))
	setText(arg_34_0:findTF("mask/Text", arg_34_2), i18n("roll_reward_got"))
	setActive(arg_34_0:findTF("mask", arg_34_2), var_34_3:isReceive())
end

function var_0_0.UpdateAttrLock(arg_36_0)
	arg_36_0.attrLock = {}

	for iter_36_0, iter_36_1 in ipairs(arg_36_0.exploredStories) do
		if arg_36_0.story2Attr[iter_36_1] ~= nil then
			for iter_36_2, iter_36_3 in ipairs(arg_36_0.story2Attr[iter_36_1]) do
				table.insert(arg_36_0.attrLock, iter_36_3)
			end
		end
	end
end

function var_0_0.UpdateCard(arg_37_0)
	arg_37_0:UpdateAttrLock()
	setText(arg_37_0.characterName, var_0_0.GetRollData(1, var_0_1) .. ":")
	setInputText(arg_37_0.nameInput, getProxy(PlayerProxy):getData().name)
	setText(arg_37_0.profession, var_0_0.GetRollData(2, var_0_1) .. ":")
	setText(findTF(arg_37_0.profession, "Text"), var_0_0.GetRollData(2, var_0_2))

	for iter_37_0 = 1, arg_37_0.attrGroup.childCount do
		local var_37_0 = arg_37_0.attrGroup:GetChild(iter_37_0 - 1)

		for iter_37_1 = 1, var_37_0.childCount do
			local var_37_1 = var_37_0:GetChild(iter_37_1 - 1)
			local var_37_2 = (iter_37_1 - 1) * arg_37_0.attrGroup.childCount + iter_37_0 + 2

			setText(findTF(var_37_1, "name"), var_0_0.GetRollData(var_37_2, var_0_1))
			setText(findTF(var_37_1, "Text"), table.contains(arg_37_0.attrLock, var_37_2) and var_0_0.GetRollData(var_37_2, var_0_2) or "---")
			setActive(findTF(var_37_1, "Text/Image"), not table.contains(arg_37_0.attrLock, var_37_2))
		end
	end

	for iter_37_2 = 1, arg_37_0.skillGroup.childCount do
		local var_37_3 = arg_37_0.skillGroup:GetChild(iter_37_2 - 1)

		for iter_37_3 = 1, var_37_3.childCount do
			local var_37_4 = var_37_3:GetChild(iter_37_3 - 1)
			local var_37_5 = (iter_37_3 - 1) * arg_37_0.attrGroup.childCount + iter_37_2 + 10

			setText(findTF(var_37_4, "group/skill_name"), table.contains(arg_37_0.attrLock, var_37_5) and var_0_0.GetRollData(var_37_5, var_0_1) or "")
			setText(findTF(var_37_4, "group/Text"), table.contains(arg_37_0.attrLock, var_37_5) and var_0_0.GetColorValue(var_37_5, var_0_0.GetRollData(var_37_5, var_0_2)) or "")
			setActive(findTF(var_37_4, "Image"), not table.contains(arg_37_0.attrLock, var_37_5))
		end
	end
end

function var_0_0.RollCharacterCard(arg_38_0)
	for iter_38_0 = 1, arg_38_0.attrGroup.childCount do
		local var_38_0 = arg_38_0.attrGroup:GetChild(iter_38_0 - 1)

		for iter_38_1 = 1, var_38_0.childCount do
			local var_38_1 = var_38_0:GetChild(iter_38_1 - 1)
			local var_38_2 = (iter_38_1 - 1) * arg_38_0.attrGroup.childCount + iter_38_0 + 2
			local var_38_3 = var_0_0.GetRollData(var_38_2, var_0_3)

			setText(findTF(var_38_1, "Text"), math.random(var_38_3[1], var_38_3[2]))
		end
	end

	local var_38_4 = var_0_0.GetRandomValue(i18n("roll_attr_list"), 8)
	local var_38_5 = 1

	for iter_38_2 = 1, arg_38_0.skillGroup.childCount do
		local var_38_6 = arg_38_0.skillGroup:GetChild(iter_38_2 - 1)

		for iter_38_3 = 1, var_38_6.childCount do
			local var_38_7 = var_38_6:GetChild(iter_38_3 - 1)
			local var_38_8 = (iter_38_3 - 1) * arg_38_0.attrGroup.childCount + iter_38_2 + 10

			setText(findTF(var_38_7, "group/skill_name"), var_38_4[var_38_5])

			var_38_5 = var_38_5 + 1

			setText(findTF(var_38_7, "group/Text"), var_0_0.GetColorValue(var_38_8, var_0_0.GetRandomValue(var_0_0.GetRollData(var_38_8, var_0_3), 1)[1]))
		end
	end
end

function var_0_0.IsFinish(arg_39_0)
	return #arg_39_0.exploredStories == 24
end

function var_0_0.GetRandomValue(arg_40_0, arg_40_1)
	local var_40_0 = {}

	for iter_40_0 = 1, #arg_40_0 do
		table.insert(var_40_0, iter_40_0)
	end

	shuffle(var_40_0)

	local var_40_1 = {}

	for iter_40_1 = 1, arg_40_1 do
		table.insert(var_40_1, arg_40_0[var_40_0[iter_40_1]])
	end

	return var_40_1
end

function var_0_0.GetColorValue(arg_41_0, arg_41_1)
	local var_41_0 = var_0_0.GetRollData(arg_41_0, var_0_3)
	local var_41_1 = table.indexof(var_41_0, arg_41_1)

	return setColorStr(arg_41_1, var_0_0.SKILL_COLOR[var_41_1])
end

function var_0_0.CheckAwardGet(arg_42_0)
	local var_42_0 = false

	for iter_42_0, iter_42_1 in ipairs(arg_42_0.taskGroup) do
		if arg_42_0.taskProxy:getTaskVO(iter_42_1):getTaskStatus() == 1 then
			var_42_0 = true
		end
	end

	setActive(arg_42_0.buttonAwardGet, var_42_0)
	setActive(findTF(arg_42_0.buttonAward, "red"), var_42_0)
end

function var_0_0.PlayStory(arg_43_0, arg_43_1)
	if arg_43_0:IsPlayed(arg_43_1) then
		return
	end

	arg_43_0.waitPlayStory = arg_43_1

	arg_43_0:emit(CastleMainMediator.CASTLE_ACT_OP, {
		cmd = 2,
		id = var_0_0.ACT_ID,
		arg1 = arg_43_1
	})
end

function var_0_0.StoryActEnd(arg_44_0, arg_44_1)
	if not arg_44_0.waitPlayStory then
		return
	end

	local var_44_0, var_44_1 = arg_44_0.storyMgr:StoryId2StoryName(arg_44_0.waitPlayStory)

	local function var_44_2()
		if arg_44_0.story2Attr[arg_44_0.waitPlayStory] == nil then
			return false
		end

		local var_45_0 = 0

		for iter_45_0, iter_45_1 in ipairs(arg_44_0.story2Attr[arg_44_0.waitPlayStory]) do
			if not table.contains(arg_44_0.attrLock, iter_45_1) then
				var_45_0 = var_45_0 + 1
			end
		end

		return var_45_0 > 0
	end

	playStory(var_44_0, function()
		if var_44_2() then
			arg_44_0:UpdateCard()
			setActive(arg_44_0.characterWindow, true)
			pg.UIMgr.GetInstance():BlurPanel(arg_44_0.characterCard)
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_0.CARD_SE)

			for iter_46_0, iter_46_1 in ipairs(arg_44_0.story2Attr[arg_44_0.waitPlayStory]) do
				if iter_46_1 < 11 then
					local var_46_0 = iter_46_1 - 3
					local var_46_1 = math.floor(var_46_0 / arg_44_0.attrGroup.childCount)
					local var_46_2 = var_46_0 % arg_44_0.attrGroup.childCount
					local var_46_3 = arg_44_0.attrGroup:GetChild(var_46_2):GetChild(var_46_1)

					setText(findTF(var_46_3, "Text"), var_0_0.GetRollData(iter_46_1, var_0_2))
					findTF(var_46_3, "Text/Image"):GetComponent(typeof(Animation)):Play("anim_castle_skill")
				else
					local var_46_4 = iter_46_1 - 11
					local var_46_5 = math.floor(var_46_4 / arg_44_0.skillGroup.childCount)
					local var_46_6 = var_46_4 % arg_44_0.skillGroup.childCount
					local var_46_7 = arg_44_0.skillGroup:GetChild(var_46_6):GetChild(var_46_5)

					setText(findTF(var_46_7, "group/skill_name"), var_0_0.GetRollData(iter_46_1, var_0_1))
					setText(findTF(var_46_7, "group/Text"), var_0_0.GetColorValue(iter_46_1, var_0_0.GetRollData(iter_46_1, var_0_2)))
					findTF(var_46_7, "Image"):GetComponent(typeof(Animation)):Play("anim_castle_skill")
				end
			end

			arg_44_0:ExploreStory(arg_44_0.waitPlayStory)
			arg_44_0:UnlockStory(arg_44_1)
			arg_44_0:UpdateAttrLock()
		else
			arg_44_0:ExploreStory(arg_44_0.waitPlayStory)
			arg_44_0:UnlockStory(arg_44_1)
			arg_44_0:UpdateAttrLock()
			arg_44_0:UpdateFlush()
			arg_44_0:CheckGuide()
		end
	end)
end

function var_0_0.FirstStory(arg_47_0)
	local var_47_0 = arg_47_0.activity:getConfig("config_data")[1]
	local var_47_1, var_47_2 = arg_47_0.storyMgr:StoryId2StoryName(var_47_0)

	playStory(var_47_1, function()
		local var_48_0 = {
			8,
			59496,
			1
		}
		local var_48_1 = {
			type = var_48_0[1],
			id = var_48_0[2],
			count = var_48_0[3]
		}

		arg_47_0:UpdateFlush()
		arg_47_0:emit(BaseUI.ON_AWARD, {
			items = {
				var_48_1
			},
			title = AwardInfoLayer.TITLE.ITEM,
			removeFunc = function()
				arg_47_0:CheckGuide()
			end
		})
	end)
end

function var_0_0.RollDice(arg_50_0, arg_50_1, arg_50_2)
	for iter_50_0, iter_50_1 in ipairs({
		arg_50_0.success,
		arg_50_0.criticalSuccess,
		arg_50_0.failure,
		arg_50_0.criticalFailure
	}) do
		setActive(iter_50_1, false)
	end

	setActive(arg_50_0.diceWindow, true)
	setActive(arg_50_0.buttonDiceContinue, false)
	arg_50_0:ExplorableEffect(false)
	setImageAlpha(arg_50_0.buttonDiceContinue, 0)

	arg_50_0.diceNumber = arg_50_1

	if arg_50_1 == 100 then
		arg_50_1 = 0
	end

	local var_50_0 = math.floor(arg_50_1 / 10)
	local var_50_1 = arg_50_1 % 10

	pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_0_0.ROLL_SE)
	arg_50_0:SetAnim(arg_50_0.dices[1], var_50_0, nil)
	arg_50_0:SetAnim(arg_50_0.dices[2], var_50_1, function()
		LeanTween.delayedCall(go(arg_50_0._tf), 0.12, System.Action(function()
			if arg_50_0.diceNumber <= 5 then
				setActive(arg_50_0.criticalSuccess, true)
			elseif arg_50_0.diceNumber <= 50 then
				setActive(arg_50_0.success, true)
			elseif arg_50_0.diceNumber <= 94 then
				setActive(arg_50_0.failure, true)
			else
				setActive(arg_50_0.criticalFailure, true)
			end

			setActive(arg_50_0.buttonDiceContinue, true)
			LeanTween.delayedCall(go(arg_50_0._tf), 0.495, System.Action(function()
				LeanTween.alpha(arg_50_0.buttonDiceContinue, 1, 0.26)
			end))
		end))
	end)

	arg_50_0.explorablePos = arg_50_2

	for iter_50_2, iter_50_3 in ipairs(arg_50_0.storyGroup) do
		arg_50_0:UnlockStory(iter_50_3)

		if iter_50_3 == arg_50_2 then
			break
		end
	end
end

function var_0_0.SetAnim(arg_54_0, arg_54_1, arg_54_2, arg_54_3)
	local var_54_0 = arg_54_1:GetComponent(typeof(SpineAnimUI))

	var_54_0:SetActionCallBack(nil)
	var_54_0:SetAction("roll" .. arg_54_2, 0)
	var_54_0:SetActionCallBack(function(arg_55_0)
		if arg_55_0 == "finish" then
			var_54_0:SetActionCallBack(nil)
			var_54_0:SetAction("normal" .. arg_54_2, 0)

			if arg_54_3 then
				arg_54_3()
			end
		end
	end)
end

function var_0_0.UnlockStory(arg_56_0, arg_56_1)
	if table.contains(arg_56_0.explorableStories, arg_56_1) or table.contains(arg_56_0.exploredStories, arg_56_1) then
		return
	end

	table.insert(arg_56_0.explorableStories, arg_56_1)

	if arg_56_0:IndexofStory(arg_56_1) > arg_56_0:IndexofStory(arg_56_0.explorablePos) then
		arg_56_0.explorablePos = arg_56_1
	end
end

function var_0_0.ExploreStory(arg_57_0, arg_57_1)
	if table.contains(arg_57_0.exploredStories, arg_57_1) then
		return
	end

	if not table.contains(arg_57_0.explorableStories, arg_57_1) then
		return
	end

	table.removebyvalue(arg_57_0.explorableStories, arg_57_1)
	table.insert(arg_57_0.exploredStories, arg_57_1)

	if arg_57_0:IndexofStory(arg_57_1) > arg_57_0:IndexofStory(arg_57_0.currentPos) then
		arg_57_0.currentPos = arg_57_1
	end
end

function var_0_0.IndexofStory(arg_58_0, arg_58_1)
	local var_58_0 = table.indexof(arg_58_0.storyGroup, arg_58_1)

	if var_58_0 == false then
		return -1
	end

	return var_58_0
end

function var_0_0.IsPlayed(arg_59_0, arg_59_1)
	local var_59_0, var_59_1 = arg_59_0.storyMgr:StoryId2StoryName(arg_59_1)

	return arg_59_0.storyMgr:IsPlayed(var_59_0, var_59_1)
end

function var_0_0.IsBadEnd(arg_60_0, arg_60_1)
	return (table.indexof(arg_60_0.storyGroup, arg_60_1) + 1) % 3 == 0
end

function var_0_0.ExplorableEffect(arg_61_0, arg_61_1)
	for iter_61_0 = 1, var_0_0.ROOM_NUM do
		local var_61_0 = arg_61_0:GetRoomTF(iter_61_0)

		setActive(findTF(var_61_0, "explorable/glow"), arg_61_1)
		setActive(findTF(var_61_0, "explorable/glow1"), arg_61_1)
	end
end

function var_0_0.ChangeRoomColor(arg_62_0, arg_62_1, arg_62_2)
	local var_62_0 = arg_62_0:GetRoomTF(arg_62_1)
	local var_62_1 = findTF(var_62_0, "fill")

	if arg_62_2 then
		setImageColor(var_62_1, arg_62_2)
	end
end

function var_0_0.ChangeRoomMark(arg_63_0, arg_63_1, arg_63_2, arg_63_3)
	cover = cover or false

	local var_63_0 = arg_63_0:GetRoomTF(arg_63_1)
	local var_63_1 = findTF(var_63_0, "current")
	local var_63_2 = findTF(var_63_0, "unexplored")
	local var_63_3 = findTF(var_63_0, "bad")
	local var_63_4 = findTF(var_63_0, "explorable")

	if not arg_63_3 then
		for iter_63_0, iter_63_1 in ipairs({
			var_63_1,
			var_63_2,
			var_63_3,
			var_63_4
		}) do
			setActive(iter_63_1, false)
		end
	end

	if arg_63_2 then
		if arg_63_2 == var_0_0.MARK_CURRENT then
			setActive(var_63_1, true)
		elseif arg_63_2 == var_0_0.MARK_UNEXPLORED then
			setActive(var_63_2, true)
		elseif arg_63_2 == var_0_0.MARK_BAD then
			setActive(var_63_3, true)
		elseif arg_63_2 == var_0_0.MARK_EXPLORABLE then
			setActive(var_63_4, true)
		end
	end
end

function var_0_0.GetRoomTF(arg_64_0, arg_64_1)
	if arg_64_1 == var_0_0.ROOM_NUM then
		return arg_64_0.rooms[1]:GetChild(arg_64_0.rooms[1].childCount - 1)
	elseif arg_64_1 < arg_64_0.rooms[1].childCount then
		return arg_64_0.rooms[1]:GetChild(arg_64_1 - 1)
	end

	arg_64_1 = arg_64_1 - arg_64_0.rooms[1].childCount

	return arg_64_0.rooms[2]:GetChild(arg_64_1)
end

function var_0_0.CheckGuide(arg_65_0)
	for iter_65_0, iter_65_1 in pairs({
		{
			"guide",
			"Castle000",
			function(arg_66_0)
				return #arg_66_0.exploredStories == 0
			end
		},
		{
			"guide",
			"Castle001",
			function(arg_67_0)
				return #arg_67_0.exploredStories == 1 and arg_67_0:IndexofStory(arg_67_0.explorablePos) <= arg_67_0:IndexofStory(arg_67_0.currentPos)
			end
		},
		{
			"story",
			arg_65_0.storyMgr:StoryId2StoryName(arg_65_0.activity:getConfig("config_client")[1][1]),
			function(arg_68_0)
				return #arg_68_0.exploredStories == 1 and arg_68_0:IndexofStory(arg_68_0.explorablePos) > arg_68_0:IndexofStory(arg_68_0.currentPos)
			end
		},
		{
			"story",
			arg_65_0.storyMgr:StoryId2StoryName(arg_65_0.activity:getConfig("config_client")[1][2]),
			function(arg_69_0)
				return #arg_69_0.exploredStories == 2 and arg_69_0:IndexofStory(arg_69_0.explorablePos) <= arg_69_0:IndexofStory(arg_69_0.currentPos)
			end
		},
		{
			"guide",
			"Castle002",
			function(arg_70_0)
				return arg_70_0:IndexofStory(arg_70_0.explorablePos) == 15 and arg_70_0:IndexofStory(arg_70_0.explorablePos) > arg_70_0:IndexofStory(arg_70_0.currentPos)
			end
		},
		{
			"story",
			arg_65_0.storyMgr:StoryId2StoryName(arg_65_0.activity:getConfig("config_client")[1][3]),
			function(arg_71_0)
				return getProxy(TaskProxy):isReceiveTasks(arg_71_0.taskGroup)
			end
		}
	}) do
		local var_65_0, var_65_1, var_65_2 = unpack(iter_65_1)

		if not arg_65_0:IsPlayed(var_65_1) and var_65_2(arg_65_0) then
			if var_65_0 == "guide" then
				pg.NewGuideMgr.GetInstance():Play(var_65_1, nil, function()
					arg_65_0:emit(CastleMainMediator.UPDATE_GUIDE, var_65_1)
				end)
			elseif var_65_0 == "story" then
				playStory(var_65_1)
			else
				assert(false)
			end

			break
		end
	end
end

function var_0_0.PlaySE(arg_73_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(arg_73_0)
end

function var_0_0.GetRollData(arg_74_0, arg_74_1)
	return pg.roll_attr[arg_74_0][arg_74_1]
end

function var_0_0.willExit(arg_75_0)
	if isActive(arg_75_0.characterWindow) then
		setActive(arg_75_0.characterWindow, false)
		pg.UIMgr.GetInstance():UnblurPanel(arg_75_0.characterCard, arg_75_0.characterWindowBg)
	end

	LeanTween.cancel(go(arg_75_0._tf))
end

function var_0_0.onBackPressed(arg_76_0)
	if isActive(arg_76_0.diceWindow) then
		return
	end

	arg_76_0:emit(var_0_0.ON_BACK_PRESSED)
end

return var_0_0
