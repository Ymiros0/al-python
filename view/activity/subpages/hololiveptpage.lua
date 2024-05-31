﻿local var_0_0 = class("HoloLivePtPage", import(".TemplatePage.PtTemplatePage"))

function var_0_0.OnInit(arg_1_0)
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.charImg = arg_1_0:findTF("charImg", arg_1_0.bg)
	arg_1_0.numImg = arg_1_0:findTF("numImg", arg_1_0.bg)
	arg_1_0.chapterImg = arg_1_0:findTF("chapterImg", arg_1_0.bg)
	arg_1_0.spineCharContainer = arg_1_0:findTF("SpineChar", arg_1_0.bg)
	arg_1_0.scrollTextMask = arg_1_0:findTF("ScrollText", arg_1_0.bg)
	arg_1_0.scrollTextContainer = arg_1_0:findTF("ScrollText/TextList", arg_1_0.bg)
	arg_1_0.scrollTextTpl = arg_1_0:findTF("TextTpl", arg_1_0.bg)
end

function var_0_0.OnDataSetting(arg_2_0)
	var_0_0.super.OnDataSetting(arg_2_0)

	arg_2_0.ptCount = arg_2_0.ptData:GetResProgress()
	arg_2_0.ptRank = pg.activity_event_pt[arg_2_0.activity.id].pt_list
	arg_2_0.picNameList = pg.activity_event_pt[arg_2_0.activity.id].pic_list
end

function var_0_0.OnFirstFlush(arg_3_0)
	var_0_0.super.OnFirstFlush(arg_3_0)
	arg_3_0:initScrollTextList()

	local var_3_0 = arg_3_0.ptRank[2] - arg_3_0.ptRank[1]
	local var_3_1 = math.floor(arg_3_0.ptCount / var_3_0) + 1

	if var_3_1 > #arg_3_0.picNameList then
		var_3_1 = #arg_3_0.picNameList
	end

	local var_3_2 = arg_3_0.picNameList[var_3_1]

	LoadSpriteAtlasAsync("ui/activityuipage/hololiveptpage", var_3_2, function(arg_4_0)
		setImageSprite(arg_3_0.charImg, arg_4_0)
	end)
	LoadSpriteAtlasAsync("ui/activityuipage/hololiveptpage", "#" .. var_3_1, function(arg_5_0)
		setImageSprite(arg_3_0.numImg, arg_5_0)
	end)
	LoadSpriteAtlasAsync("ui/activityuipage/hololiveptpage", "jiaobiao_" .. var_3_1, function(arg_6_0)
		setImageSprite(arg_3_0.chapterImg, arg_6_0)
	end)

	local var_3_3 = "vtuber_shion"

	pg.UIMgr.GetInstance():LoadingOn()
	PoolMgr.GetInstance():GetSpineChar(var_3_3, true, function(arg_7_0)
		pg.UIMgr.GetInstance():LoadingOff()

		arg_3_0.prefab = var_3_3
		arg_3_0.model = arg_7_0
		tf(arg_7_0).localScale = Vector3(1, 1, 1)

		arg_7_0:GetComponent("SpineAnimUI"):SetAction("stand", 0)
		setParent(arg_7_0, arg_3_0.spineCharContainer)
	end)
end

function var_0_0.OnDestroy(arg_8_0)
	if arg_8_0.scrollTextTimer then
		arg_8_0.scrollTextTimer:Stop()

		arg_8_0.scrollTextTimer = nil
	end

	if arg_8_0.prefab and arg_8_0.model then
		PoolMgr.GetInstance():ReturnSpineChar(arg_8_0.prefab, arg_8_0.model)

		arg_8_0.prefab = nil
		arg_8_0.model = nil
	end
end

function var_0_0.initScrollTextList(arg_9_0)
	setText(arg_9_0.scrollTextTpl, arg_9_0.activity:getConfig("config_client").scrollStr)

	local var_9_0 = GetComponent(arg_9_0.scrollTextTpl, "Text").preferredWidth + arg_9_0.scrollTextMask.rect.width + 50
	local var_9_1 = arg_9_0.scrollTextContainer.localPosition.x - var_9_0
	local var_9_2 = 50
	local var_9_3 = 0.016666666666666666

	UIItemList.New(arg_9_0.scrollTextContainer, arg_9_0.scrollTextTpl):align(2)

	local var_9_4 = arg_9_0.scrollTextContainer:GetChild(1)

	arg_9_0.scrollTextTimer = Timer.New(function()
		local var_10_0 = arg_9_0.scrollTextContainer.localPosition.x - var_9_2 * var_9_3

		if var_10_0 <= var_9_1 then
			var_10_0 = var_9_4.localPosition.x + arg_9_0.scrollTextContainer.localPosition.x
		end

		arg_9_0.scrollTextContainer.localPosition = Vector3(var_10_0, 0, 0)
	end, var_9_3, -1, true)

	arg_9_0.scrollTextTimer:Start()
end

return var_0_0
