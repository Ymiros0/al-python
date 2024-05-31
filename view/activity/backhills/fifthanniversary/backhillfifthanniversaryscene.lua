﻿local var_0_0 = class("BackHillFifthAnniversaryScene", import("..TemplateMV.BackHillTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "BackHillFifthAnniversaryUI"
end

var_0_0.edge2area = {
	default = "_sdPlace",
	["6_7"] = "_sdPlace2"
}

function var_0_0.init(arg_2_0)
	var_0_0.super.init(arg_2_0)

	arg_2_0.top = arg_2_0:findTF("top")
	arg_2_0._bg = arg_2_0:findTF("BG")
	arg_2_0._map = arg_2_0:findTF("map")

	for iter_2_0 = 0, arg_2_0._map.childCount - 1 do
		local var_2_0 = arg_2_0._map:GetChild(iter_2_0)
		local var_2_1 = go(var_2_0).name

		arg_2_0["map_" .. var_2_1] = var_2_0
	end

	arg_2_0._shipTpl = arg_2_0:findTF("ship")
	arg_2_0._sdPlace = arg_2_0:findTF("map/SDPlace")
	arg_2_0._sdPlace2 = arg_2_0:findTF("map/SDPlace2")
	arg_2_0._upper = arg_2_0:findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1 do
		local var_2_2 = arg_2_0._upper:GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2
	end

	arg_2_0.containers = {
		arg_2_0._sdPlace,
		arg_2_0._sdPlace2
	}
	arg_2_0.usableTxt = arg_2_0.top:Find("UsableCount/Text"):GetComponent(typeof(Text))
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.BackHillFifthAnniversaryGraph"))
end

function var_0_0.didEnter(arg_3_0)
	onButton(arg_3_0, arg_3_0:findTF("top/Back"), function()
		arg_3_0:emit(var_0_0.ON_BACK)
	end, SFX_CANCEL)
	onButton(arg_3_0, arg_3_0:findTF("top/Home"), function()
		arg_3_0:emit(var_0_0.ON_HOME)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0:findTF("top/Invitation"), function()
		pg.m02:sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.FIFTH_ANNIVERSARY_INVITATION
		})
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0:findTF("top/UsableCount"), function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 40)
	end, SFX_PANEL)

	local var_3_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.JIUJIU_DUOMAOMAO_ID)

	arg_3_0:InitStudents(var_3_0 and var_3_0.id, 3, 4)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "youxidian", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 40)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "kafeiting", function()
		pg.m02:sendNotification(GAME.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.ACTIVITY_MAID_DAY
		})
	end)
	setActive(arg_3_0.map_longpaifangBanner, PLATFORM_CODE == PLATFORM_CH)

	if PLATFORM_CODE == PLATFORM_CH then
		local function var_3_1()
			arg_3_0:emit(NewYearFestivalMediator.GO_SCENE, SCENE.SUMMARY)
		end

		onButton(arg_3_0, arg_3_0.map_longpaifang, var_3_1, SFX_PANEL)
		onButton(arg_3_0, arg_3_0.map_longpaifangBanner, var_3_1, SFX_PANEL)
	end

	arg_3_0:BindItemSkinShop()

	local function var_3_2()
		local var_11_0
		local var_11_1 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1)
		local var_11_2 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILD)

		if var_11_1 and not var_11_1:isEnd() then
			var_11_0 = BuildShipScene.PROJECTS.ACTIVITY
		elseif var_11_2 and not var_11_2:isEnd() then
			var_11_0 = ({
				BuildShipScene.PROJECTS.SPECIAL,
				BuildShipScene.PROJECTS.LIGHT,
				BuildShipScene.PROJECTS.HEAVY
			})[var_11_2:getConfig("config_client").id]
		else
			pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_end"))

			return
		end

		arg_3_0:emit(BackHillMediatorTemplate.GO_SCENE, SCENE.GETBOAT, {
			page = BuildShipScene.PAGE_BUILD,
			projectName = var_11_0
		})
	end

	onButton(arg_3_0, arg_3_0.map_xianshijianzao, var_3_2, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.map_xianshijianzaoBanner, var_3_2, SFX_PANEL)
	arg_3_0:UpdateView()
end

function var_0_0.UpdateView(arg_12_0)
	local function var_12_0()
		return BackHillTemplate.IsMiniActNeedTip(ActivityConst.JIUJIU_DUOMAOMAO_ID)
	end

	setActive(arg_12_0.upper_youxidian:Find("Tip"), var_12_0())

	local var_12_1 = getProxy(ActivityProxy):getActivityById(ActivityConst.JIUJIU_DUOMAOMAO_ID)
	local var_12_2 = var_12_1 and getProxy(MiniGameProxy):GetHubByHubId(var_12_1:getConfig("config_id"))
	local var_12_3 = var_12_2 and var_12_2.count or 0

	arg_12_0.usableTxt.text = "X" .. var_12_3

	local function var_12_4()
		local var_14_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.ACTIVITY_MAID_DAY)

		return Activity.IsActivityReady(var_14_0)
	end

	setActive(arg_12_0.upper_kafeiting:Find("Tip"), var_12_4())

	local function var_12_5()
		if PLATFORM_CODE ~= PLATFORM_CH then
			return
		end

		local var_15_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

		return Activity.IsActivityReady(var_15_0)
	end

	setActive(arg_12_0.map_longpaifangBanner:Find("Tip"), var_12_5())
end

function var_0_0.IsShowMainTip(arg_16_0)
	local function var_16_0()
		return BackHillTemplate.IsMiniActNeedTip(ActivityConst.JIUJIU_DUOMAOMAO_ID)
	end

	local function var_16_1()
		local var_18_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.ACTIVITY_MAID_DAY)

		return Activity.IsActivityReady(var_18_0)
	end

	local function var_16_2()
		if PLATFORM_CODE ~= PLATFORM_CH then
			return
		end

		local var_19_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

		return Activity.IsActivityReady(var_19_0)
	end

	return var_16_0() or var_16_1() or var_16_2()
end

function var_0_0.willExit(arg_20_0)
	arg_20_0:clearStudents()
	var_0_0.super.willExit(arg_20_0)
end

return var_0_0
