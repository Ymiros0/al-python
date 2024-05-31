local var_0_0 = class("MainLiveAreaPage", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "MainLiveAreaUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0._bg = arg_2_0:findTF("bg")

	setText(arg_2_0:findTF("bg/Text", arg_2_0._bg), i18n("word_harbour"))

	arg_2_0.timeCfg = pg.gameset.main_live_area_time.description
	arg_2_0._academyBtn = arg_2_0:findTF("school_btn")
	arg_2_0._haremBtn = arg_2_0:findTF("backyard_btn")
	arg_2_0._commanderBtn = arg_2_0:findTF("commander_btn")
	arg_2_0._educateBtn = arg_2_0:findTF("educate_btn")
	arg_2_0._islandBtn = arg_2_0:findTF("island_btn")
	arg_2_0._dormBtn = arg_2_0:findTF("dorm_btn")

	pg.redDotHelper:AddNode(RedDotNode.New(arg_2_0._haremBtn:Find("tip"), {
		pg.RedDotMgr.TYPES.COURTYARD
	}))
	pg.redDotHelper:AddNode(SelfRefreshRedDotNode.New(arg_2_0._academyBtn:Find("tip"), {
		pg.RedDotMgr.TYPES.SCHOOL
	}))
	pg.redDotHelper:AddNode(SelfRefreshRedDotNode.New(arg_2_0._commanderBtn:Find("tip"), {
		pg.RedDotMgr.TYPES.COMMANDER
	}))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0._commanderBtn, function()
		arg_3_0:emit(NewMainMediator.GO_SCENE, SCENE.COMMANDERCAT, {
			fromMain = true,
			fleetType = CommanderCatScene.FLEET_TYPE_COMMON
		})
		arg_3_0:Hide()
	end, SFX_MAIN)
	onButton(arg_3_0, arg_3_0._haremBtn, function()
		arg_3_0:emit(NewMainMediator.GO_SCENE, SCENE.COURTYARD)
		arg_3_0:Hide()
	end, SFX_MAIN)
	onButton(arg_3_0, arg_3_0._academyBtn, function()
		arg_3_0:emit(NewMainMediator.GO_SCENE, SCENE.NAVALACADEMYSCENE)
		arg_3_0:Hide()
	end, SFX_MAIN)
	onButton(arg_3_0, arg_3_0._educateBtn, function()
		if LOCK_EDUCATE_SYSTEM then
			return
		end

		arg_3_0:emit(NewMainMediator.GO_SCENE, SCENE.EDUCATE, {
			isMainEnter = true
		})
		arg_3_0:Hide()
	end, SFX_MAIN)
	onButton(arg_3_0, arg_3_0._islandBtn, function()
		return
	end, SFX_MAIN)
	onButton(arg_3_0, arg_3_0._dormBtn, function()
		return
	end, SFX_MAIN)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.Show(arg_11_0)
	var_0_0.super.Show(arg_11_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_11_0._tf, true, {
		weight = LayerWeightConst.SECOND_LAYER
	})

	local var_11_0 = getProxy(PlayerProxy):getRawData()

	if not pg.SystemOpenMgr.GetInstance():isOpenSystem(var_11_0.level, "CommanderCatMediator") then
		arg_11_0._commanderBtn:GetComponent(typeof(Image)).color = Color(0.5, 0.5, 0.5, 1)
	else
		arg_11_0._commanderBtn:GetComponent(typeof(Image)).color = Color(1, 1, 1, 1)
	end

	if not pg.SystemOpenMgr.GetInstance():isOpenSystem(var_11_0.level, "CourtYardMediator") then
		arg_11_0._haremBtn:GetComponent(typeof(Image)).color = Color(0.5, 0.5, 0.5, 1)
	else
		arg_11_0._haremBtn:GetComponent(typeof(Image)).color = Color(1, 1, 1, 1)
	end

	if not pg.SystemOpenMgr.GetInstance():isOpenSystem(var_11_0.level, "EducateMediator") then
		arg_11_0._educateBtn:GetComponent(typeof(Image)).color = Color(0.5, 0.5, 0.5, 1)
	else
		arg_11_0._educateBtn:GetComponent(typeof(Image)).color = Color(1, 1, 1, 1)
	end

	arg_11_0:UpdateTime()

	arg_11_0.timer = Timer.New(function()
		arg_11_0:UpdateTime()
	end, 60, -1)

	arg_11_0.timer:Start()
end

function var_0_0.UpdateTime(arg_13_0)
	local var_13_0 = pg.TimeMgr.GetInstance()
	local var_13_1 = var_13_0:GetServerHour()
	local var_13_2 = var_13_1 < 12

	GetSpriteFromAtlasAsync("ui/MainUISecondaryPanel_atlas", var_13_2 and "am" or "pm", function(arg_14_0)
		arg_13_0:findTF("bg/AMPM"):GetComponent(typeof(Image)).sprite = arg_14_0
	end)

	local var_13_3 = arg_13_0:getDayOrNight(var_13_1) == "day"
	local var_13_4 = LoadSprite("bg/" .. (var_13_3 and "bg_livingarea_day" or "bg_livingarea_night"), "")

	arg_13_0:findTF("bg", arg_13_0._bg):GetComponent(typeof(Image)).sprite = var_13_4

	local var_13_5 = GetSpriteFromAtlas("ui/MainUISecondaryPanel_atlas", var_13_3 and "island_build_day" or "island_build_night")

	arg_13_0:findTF("bg", arg_13_0._islandBtn):GetComponent(typeof(Image)).sprite = var_13_5

	local var_13_6 = var_13_0:CurrentSTimeDesc("%Y/%m/%d", true)

	setText(arg_13_0:findTF("date", arg_13_0._bg), var_13_6)

	local var_13_7 = var_13_0:CurrentSTimeDesc(":%M", true)

	if var_13_1 > 12 then
		var_13_1 = var_13_1 - 12
	end

	setText(arg_13_0:findTF("time", arg_13_0._bg), var_13_1 .. var_13_7)

	local var_13_8 = EducateHelper.GetWeekStrByNumber(var_13_0:GetServerWeek())

	setText(arg_13_0:findTF("date/week", arg_13_0._bg), var_13_8)
end

function var_0_0.getDayOrNight(arg_15_0, arg_15_1)
	for iter_15_0, iter_15_1 in ipairs(arg_15_0.timeCfg) do
		local var_15_0 = iter_15_1[1]

		if arg_15_1 >= var_15_0[1] and arg_15_1 < var_15_0[2] then
			return iter_15_1[2]
		end
	end

	return "day"
end

function var_0_0.Hide(arg_16_0)
	if arg_16_0:isShowing() then
		var_0_0.super.Hide(arg_16_0)
		pg.UIMgr.GetInstance():UnblurPanel(arg_16_0._tf, arg_16_0._parentTf)
	end

	if arg_16_0.timer ~= nil then
		arg_16_0.timer:Stop()

		arg_16_0.timer = nil
	end
end

function var_0_0.OnDestroy(arg_17_0)
	arg_17_0:Hide()
end

return var_0_0
