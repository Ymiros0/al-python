﻿local var_0_0 = class("DOALinkIslandScene", import("..TemplateMV.BackHillTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "DOALinkIslandUI"
end

var_0_0.edge2area = {
	default = "map_middle",
	["2_2"] = "map_bridge"
}

function var_0_0.init(arg_2_0)
	arg_2_0.top = arg_2_0:findTF("top")
	arg_2_0._map = arg_2_0:findTF("map")

	for iter_2_0 = 0, arg_2_0._map.childCount - 1 do
		local var_2_0 = arg_2_0._map:GetChild(iter_2_0)
		local var_2_1 = go(var_2_0).name

		arg_2_0["map_" .. var_2_1] = var_2_0
	end

	arg_2_0._shipTpl = arg_2_0._map:Find("ship")
	arg_2_0._upper = arg_2_0:findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1 do
		local var_2_2 = arg_2_0._upper:GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2
	end

	arg_2_0.containers = {
		arg_2_0.map_middle
	}
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.DOAIslandGraph"))

	local var_2_4 = arg_2_0._tf:GetComponentInParent(typeof(UnityEngine.Canvas))
	local var_2_5 = var_2_4 and var_2_4.sortingOrder

	arg_2_0._map:GetComponent(typeof(UnityEngine.Canvas)).sortingOrder = var_2_5 - 3
	arg_2_0.map_tebiezuozhan:GetComponent(typeof(UnityEngine.Canvas)).sortingOrder = var_2_5 - 1
	arg_2_0.map_bridge:GetComponent(typeof(UnityEngine.Canvas)).sortingOrder = var_2_5 - 1

	local var_2_6 = GetComponent(arg_2_0._map, "ItemList")

	for iter_2_2 = 1, 1 do
		local var_2_7 = var_2_6.prefabItem[iter_2_2 - 1]
		local var_2_8 = tf(Instantiate(var_2_7))

		pg.ViewUtils.SetSortingOrder(var_2_8, var_2_5 - 2)
		setParent(var_2_8, arg_2_0._map)
	end

	arg_2_0.loader = AutoLoader.New()
end

function var_0_0.didEnter(arg_3_0)
	onButton(arg_3_0, arg_3_0:findTF("top/return_btn"), function()
		arg_3_0:emit(var_0_0.ON_BACK)
	end)
	onButton(arg_3_0, arg_3_0:findTF("top/return_main_btn"), function()
		arg_3_0:emit(var_0_0.ON_HOME)
	end)
	onButton(arg_3_0, arg_3_0:findTF("top/help_btn"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.doa_main.tip
		})
	end)
	arg_3_0:InitStudents(ActivityConst.MINIGAME_VOLLEYBALL, 2, 3)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "shatanpaiqiu", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 17)
	end)
	onButton(arg_3_0, arg_3_0._upper:Find("pengpengdong"), function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 51)
	end, SFX_PANEL)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "daoyvjianshe", function()
		arg_3_0:emit(DOALinkIslandMediator.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.DOA_PT_ID
		})
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "bujishangdian", function()
		arg_3_0:emit(DOALinkIslandMediator.GO_SCENE, SCENE.SHOP, {
			warp = NewShopsScene.TYPE_ACTIVITY
		})
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "huanzhuangshangdian", function()
		arg_3_0:emit(DOALinkIslandMediator.GO_SCENE, SCENE.SKINSHOP)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "xianshijianzao", function()
		arg_3_0:emit(DOALinkIslandMediator.GO_SCENE, SCENE.GETBOAT, {
			projectName = "new",
			page = 1
		})
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "jinianzhang", function()
		arg_3_0:emit(DOALinkIslandMediator.GO_SCENE, SCENE.DOA2_MEDAL_COLLECTION_SCENE)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "tebiezuozhan", function()
		local var_14_0 = getProxy(ChapterProxy)
		local var_14_1, var_14_2 = var_14_0:getLastMapForActivity()

		if not var_14_1 or not var_14_0:getMapById(var_14_1):isUnlock() then
			pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_end"))
		else
			arg_3_0:emit(DOALinkIslandMediator.GO_SCENE, SCENE.LEVEL, {
				chapterId = var_14_2,
				mapIdx = var_14_1
			})
		end
	end)
	arg_3_0:UpdateView()
end

function var_0_0.UpdateView(arg_15_0)
	local var_15_0 = getProxy(ActivityProxy)
	local var_15_1

	setActive(arg_15_0.upper_shatanpaiqiu:Find("tip"), var_0_0.IsMiniActNeedTip(ActivityConst.MINIGAME_VOLLEYBALL))
	setActive(arg_15_0.upper_pengpengdong:Find("tip"), var_0_0.IsMiniActNeedTip(ActivityConst.MINIGAME_PENGPENGDONG))

	local var_15_2 = var_15_0:getActivityById(ActivityConst.MINIGAME_VOLLEYBALL)

	assert(var_15_2)

	local var_15_3 = getProxy(MiniGameProxy):GetHubByHubId(var_15_2:getConfig("config_id"))

	assert(var_15_3)
	arg_15_0.loader:GetSpriteQuiet("ui/DOALinkIslandUI_atlas", tostring(var_15_3.usedtime or 0), arg_15_0.map_shatanpaiqiu:Find("Digit"), true)

	local var_15_4 = var_15_0:getActivityById(ActivityConst.DOA_PT_ID)

	assert(var_15_4)

	local var_15_5 = arg_15_0.upper_daoyvjianshe:Find("tip")
	local var_15_6 = var_15_4 and var_15_4:readyToAchieve()

	setActive(var_15_5, var_15_6)

	local var_15_7 = arg_15_0.upper_jinianzhang:Find("tip")
	local var_15_8 = var_0_0.MedalTip()

	setActive(var_15_7, var_15_8)
end

function var_0_0.willExit(arg_16_0)
	arg_16_0:clearStudents()
	var_0_0.super.willExit(arg_16_0)
end

function var_0_0.MedalTip()
	local var_17_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_PUZZLA)

	return Activity.IsActivityReady(var_17_0)
end

function var_0_0.IsShowMainTip(arg_18_0)
	if arg_18_0 and not arg_18_0:isEnd() then
		local var_18_0 = getProxy(ActivityProxy)

		local function var_18_1()
			local var_19_0 = var_18_0:getActivityById(ActivityConst.DOA_PT_ID)

			return var_19_0 and not var_19_0:isEnd() and var_19_0:readyToAchieve()
		end

		local var_18_2 = var_0_0.MedalTip

		local function var_18_3()
			return var_0_0.IsMiniActNeedTip(ActivityConst.MINIGAME_VOLLEYBALL)
		end

		local function var_18_4()
			return var_0_0.IsMiniActNeedTip(ActivityConst.MINIGAME_PENGPENGDONG)
		end

		return var_18_1() or var_18_2() or var_18_3() or var_18_4()
	end
end

return var_0_0
