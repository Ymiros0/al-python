﻿local var_0_0 = class("MemoryBookLayer", import("...base.BaseUI"))
local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3

var_0_0.PAGE_ONE = 1
var_0_0.PAGE_TWO = 2

local var_0_4 = 12
local var_0_5 = {
	{
		-503,
		83
	},
	{
		-371.4,
		72.6
	},
	{
		-464,
		-211
	},
	{
		-234.3,
		-176
	},
	{
		-74.5,
		30.1
	},
	{
		80,
		121.5
	},
	{
		80,
		25.4
	},
	{
		80,
		-89
	},
	{
		291,
		25.4
	},
	{
		483,
		-33
	},
	{
		334,
		-246
	},
	{
		483,
		-217.5
	},
	{
		-478.4,
		84.5
	},
	{
		-290,
		44.5
	},
	{
		-137,
		12.5
	},
	{
		100.5,
		92.5
	},
	{
		-364.3,
		-179.6
	},
	{
		-137,
		-176.9
	},
	{
		78,
		-176.9
	},
	{
		247,
		-242
	},
	{
		383,
		33
	},
	{
		548,
		69
	},
	{
		456,
		-184
	},
	{
		573,
		-106
	}
}

local function var_0_6(arg_1_0)
	local var_1_0 = {}

	local function var_1_1(arg_2_0)
		arg_2_0.root = arg_1_0
		arg_2_0.list = {}
	end

	function var_1_0.Get(arg_3_0)
		local var_3_0

		if #arg_3_0.list == 0 then
			var_3_0 = GameObject("Image")

			var_3_0:AddComponent(typeof(Image))
		else
			var_3_0 = table.remove(arg_3_0.list, #arg_3_0.list)
		end

		setActive(var_3_0, true)

		return var_3_0
	end

	function var_1_0.Return(arg_4_0, arg_4_1)
		arg_4_0:Clear(arg_4_1)
		setParent(arg_4_1, arg_4_0.root)
		table.insert(arg_4_0.list, arg_4_1)
	end

	function var_1_0.Clear(arg_5_0, arg_5_1)
		arg_5_1:GetComponent(typeof(Image)).sprite = nil

		setActive(arg_5_1, false)
	end

	function var_1_0.Dispose(arg_6_0)
		_.each(arg_6_0.list, function(arg_7_0)
			Destroy(arg_7_0)
		end)

		arg_6_0.list = nil
	end

	var_1_1(var_1_0)

	return var_1_0
end

function var_0_0.getUIName(arg_8_0)
	return "MemoryBookUI"
end

function var_0_0.setActivity(arg_9_0, arg_9_1)
	arg_9_0.activity = arg_9_1
	arg_9_0.targetItems = arg_9_0.activity:getConfig("config_data")
	arg_9_0.fetchItems = arg_9_0.activity.data1_list
	arg_9_0.unlockItems = arg_9_0.activity.data2_list
	arg_9_0.awardVO = arg_9_0.activity:getConfig("config_client")[1]
end

function var_0_0.getMemoryState(arg_10_0, arg_10_1)
	local var_10_0 = table.contains(arg_10_0.fetchItems, arg_10_1)

	return table.contains(arg_10_0.unlockItems, arg_10_1) and var_0_3 or var_10_0 and var_0_2 or var_0_1
end

function var_0_0.updateMemorys(arg_11_0)
	arg_11_0.memorys = {}

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.targetItems) do
		local var_11_0 = arg_11_0:getMemoryState(iter_11_1)
		local var_11_1 = iter_11_0 % var_0_4

		table.insert(arg_11_0.memorys, {
			id = iter_11_1,
			index = var_11_1 == 0 and var_0_4 or var_11_1,
			pos = var_0_5[iter_11_0],
			state = var_11_0
		})
	end

	local var_11_2 = arg_11_0.contextData.page or 1

	arg_11_0:updateMemoryBook(var_11_2, true)
end

function var_0_0.init(arg_12_0)
	arg_12_0.backBtn = arg_12_0:findTF("back_btn")
	arg_12_0.page1 = arg_12_0:findTF("page1")
	arg_12_0.page2 = arg_12_0:findTF("page2")

	local var_12_0 = arg_12_0:findTF("get")

	setActive(var_12_0, false)

	arg_12_0.getSprite = var_12_0:GetComponent(typeof(Image)).sprite
	arg_12_0.slider = arg_12_0:findTF("slider"):GetComponent(typeof(Slider))
	arg_12_0.totalTxt = arg_12_0:findTF("progress"):GetComponent(typeof(Text))
	arg_12_0.currValueTxt = arg_12_0:findTF("progress/value"):GetComponent(typeof(Text))
	arg_12_0.awardIcon = arg_12_0:findTF("award_bg/icon")
	arg_12_0.awardLabel = arg_12_0:findTF("award_bg/label")
	arg_12_0.awardLabelGot = arg_12_0:findTF("award_bg/label_got")
	arg_12_0.helpBtn = arg_12_0:findTF("help")
	arg_12_0.pool = var_0_6(arg_12_0._tf)
end

function var_0_0.didEnter(arg_13_0)
	arg_13_0:addRingDragListenter()
	onButton(arg_13_0, arg_13_0.backBtn, function()
		arg_13_0:emit(var_0_0.ON_CLOSE)
	end, SOUND_BACK)
	onButton(arg_13_0, arg_13_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.memorybook_notice.tip
		})
	end, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.page1:Find("switch"), function()
		arg_13_0:updateMemoryBook(var_0_0.PAGE_TWO)
	end, SFX_PANEL)
	onButton(arg_13_0, arg_13_0.page2:Find("switch"), function()
		arg_13_0:updateMemoryBook(var_0_0.PAGE_ONE)
	end, SFX_PANEL)

	arg_13_0.sprites = {}
	arg_13_0.gameObjects = {}

	arg_13_0:updateMemorys()
	arg_13_0:updateProgress()
end

function var_0_0.getStartAndEndIndex(arg_18_0, arg_18_1)
	local var_18_0 = (arg_18_1 - 1) * var_0_4 + 1
	local var_18_1 = var_18_0 + var_0_4 - 1

	return var_18_0, var_18_1
end

function var_0_0.updateMemoryBook(arg_19_0, arg_19_1, arg_19_2)
	for iter_19_0, iter_19_1 in ipairs(arg_19_0.gameObjects) do
		arg_19_0.pool:Return(iter_19_1)
	end

	arg_19_0.gameObjects = {}

	local var_19_0 = arg_19_0["page" .. arg_19_1]
	local var_19_1, var_19_2 = arg_19_0:getStartAndEndIndex(arg_19_1)

	for iter_19_2 = var_19_1, var_19_2 do
		local var_19_3 = arg_19_0.memorys[iter_19_2]

		arg_19_0:updateMemoryItem(arg_19_1, var_19_3)
	end

	local var_19_4 = false

	if arg_19_1 == var_0_0.PAGE_ONE then
		var_19_4 = arg_19_0:updatePageTip(var_0_0.PAGE_TWO)
	elseif arg_19_1 == var_0_0.PAGE_TWO then
		var_19_4 = arg_19_0:updatePageTip(var_0_0.PAGE_ONE)
	end

	setActive(var_19_0:Find("switch/tip"), var_19_4)

	arg_19_0.page = arg_19_1
	arg_19_0.contextData.page = arg_19_1

	if arg_19_2 then
		if arg_19_1 == var_0_0.PAGE_TWO then
			local var_19_5 = arg_19_0.page2:Find("switch")

			arg_19_0.page2.localPosition = Vector3.New(0, 0)
			arg_19_0.page1.localPosition = Vector3.New(-1280, 0)

			setActive(var_19_5, true)
		else
			local var_19_6 = arg_19_0.page1:Find("switch")

			arg_19_0.page2.localPosition = Vector3.New(1280, 0)
			arg_19_0.page1.localPosition = Vector3.New(0, 0)

			setActive(var_19_6, true)
		end
	elseif arg_19_1 == var_0_0.PAGE_TWO then
		local var_19_7 = arg_19_0.page2:Find("switch")

		setActive(var_19_7, false)

		arg_19_0.page2.localPosition = Vector3.New(1280, 0)
		arg_19_0.page1.localPosition = Vector3.New(0, 0)

		LeanTween.moveX(arg_19_0.page2, 0, 0.5)
		LeanTween.moveX(arg_19_0.page1, -1280, 0.5):setOnComplete(System.Action(function()
			setActive(var_19_7, true)
		end))
	else
		local var_19_8 = arg_19_0.page1:Find("switch")

		setActive(var_19_8, false)

		arg_19_0.page2.localPosition = Vector3.New(0, 0)
		arg_19_0.page1.localPosition = Vector3.New(-1280, 0)

		LeanTween.moveX(arg_19_0.page2, 1280, 0.5)
		LeanTween.moveX(arg_19_0.page1, 0, 0.5):setOnComplete(System.Action(function()
			setActive(var_19_8, true)
		end))
	end
end

function var_0_0.addRingDragListenter(arg_22_0)
	local var_22_0 = GetOrAddComponent(arg_22_0._tf, "EventTriggerListener")
	local var_22_1 = 0
	local var_22_2

	var_22_0:AddBeginDragFunc(function()
		var_22_1 = 0
		var_22_2 = nil
	end)
	var_22_0:AddDragFunc(function(arg_24_0, arg_24_1)
		local var_24_0 = arg_24_1.position

		if not var_22_2 then
			var_22_2 = var_24_0
		end

		var_22_1 = var_24_0.x - var_22_2.x
	end)
	var_22_0:AddDragEndFunc(function(arg_25_0, arg_25_1)
		if var_22_1 < -50 then
			if arg_22_0.page == var_0_0.PAGE_ONE then
				arg_22_0:updateMemoryBook(var_0_0.PAGE_TWO)
			end
		elseif var_22_1 > 50 and arg_22_0.page == var_0_0.PAGE_TWO then
			arg_22_0:updateMemoryBook(var_0_0.PAGE_ONE)
		end
	end)
end

function var_0_0.updatePageTip(arg_26_0, arg_26_1)
	local var_26_0, var_26_1 = arg_26_0:getStartAndEndIndex(arg_26_1)

	return _.any(_.slice(arg_26_0.memorys, var_26_0, var_0_4), function(arg_27_0)
		return arg_27_0.state == var_0_2
	end)
end

function var_0_0.updateMemoryItem(arg_28_0, arg_28_1, arg_28_2)
	local var_28_0 = arg_28_2.state
	local var_28_1 = arg_28_0["page" .. arg_28_1]

	local function var_28_2()
		local var_29_0 = arg_28_0.pool:Get()
		local var_29_1 = var_28_0 == var_0_2 and arg_28_0.getSprite or arg_28_0:GetMemorySprite(arg_28_1, arg_28_2.index)

		setImageSprite(var_29_0, var_29_1, true)

		var_29_0:GetComponent(typeof(Image)).raycastTarget = var_28_0 == var_0_2

		setParent(var_29_0, var_28_1:Find("container"))

		tf(var_29_0).localPosition = Vector3(arg_28_2.pos[1], arg_28_2.pos[2], 0)

		table.insert(arg_28_0.gameObjects, var_29_0)

		return var_29_0
	end

	if var_28_0 == var_0_1 then
		-- block empty
	elseif var_28_0 == var_0_2 then
		local var_28_3 = var_28_2()

		onButton(arg_28_0, var_28_3, function()
			arg_28_0:emit(MemoryBookMediator.ON_UNLOCK, arg_28_2.id, arg_28_0.activity.id)
		end, SFX_PANEL)
	elseif var_28_0 == var_0_3 then
		var_28_2()
	end
end

function var_0_0.GetMemorySprite(arg_31_0, arg_31_1, arg_31_2)
	local var_31_0 = arg_31_1 .. "_" .. arg_31_2

	if arg_31_0.sprites[var_31_0] then
		return arg_31_0.sprites[var_31_0]
	else
		local var_31_1 = GetSpriteFromAtlas("puzzla/bg_2", var_31_0)

		arg_31_0.sprites[var_31_0] = var_31_1

		return var_31_1
	end
end

function var_0_0.updateProgress(arg_32_0)
	local var_32_0 = #arg_32_0.targetItems
	local var_32_1 = #arg_32_0.unlockItems

	arg_32_0.slider.value = var_32_1 / var_32_0
	arg_32_0.totalTxt.text = var_32_0
	arg_32_0.currValueTxt.text = var_32_1

	local var_32_2 = var_32_1 == var_32_0

	arg_32_0:updateAward(var_32_2)
end

function var_0_0.updateAward(arg_33_0, arg_33_1)
	if not arg_33_0.isInitAward then
		arg_33_0.isInitAward = true

		local var_33_0 = arg_33_0.awardVO[1]
		local var_33_1 = arg_33_0.awardVO[2]

		if var_33_0 == DROP_TYPE_FURNITURE then
			local var_33_2 = Furniture.New({
				id = var_33_1
			})

			GetSpriteFromAtlasAsync("furniture/" .. var_33_2:getConfig("picture"), "", function(arg_34_0)
				if arg_33_0.exited then
					return
				end

				setImageSprite(arg_33_0.awardIcon, arg_34_0, true)
			end)
		else
			assert(false, "this award type is not deal")
		end
	end

	local var_33_3 = arg_33_0.activity.data1 == 1

	setGray(arg_33_0.awardIcon, not arg_33_1, false)
	setActive(arg_33_0.awardLabel, arg_33_1 and not var_33_3)
	setActive(arg_33_0.awardLabelGot, var_33_3)

	if LeanTween.isTweening(go(arg_33_0.awardLabel)) then
		LeanTween.cancel(go(arg_33_0.awardLabel))
	end

	if arg_33_1 and not var_33_3 then
		blinkAni(arg_33_0.awardLabel, 0.8, nil, 0.5)
	end

	removeOnButton(arg_33_0.awardIcon)

	if not var_33_3 then
		onButton(arg_33_0, arg_33_0.awardIcon, function()
			if not arg_33_1 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("memorybook_get_award_tip"))
			else
				arg_33_0:emit(MemoryBookMediator.EVENT_OPERATION, {
					cmd = 1,
					activity_id = arg_33_0.activity.id
				})
			end
		end, SFX_PANEL)
	end
end

function var_0_0.willExit(arg_36_0)
	arg_36_0.pool:Dispose()

	arg_36_0.sprites = nil
	arg_36_0.getSprite = nil
end

return var_0_0
