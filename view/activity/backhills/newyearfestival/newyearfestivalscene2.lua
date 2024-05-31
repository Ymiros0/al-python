﻿local var_0_0 = class("NewYearFestivalScene2", import("..TemplateMV.BackHillTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "NewyearFestivalUI2"
end

var_0_0.edge2area = {
	default = "map_middle",
	["3_4"] = "map_bottom",
	["5_6"] = "map_bottom"
}

function var_0_0.init(arg_2_0)
	var_0_0.super.init(arg_2_0)

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
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.NewyearFestivalGraph2"))

	local var_2_4 = arg_2_0._tf:GetComponentInParent(typeof(UnityEngine.Canvas))
	local var_2_5 = var_2_4 and var_2_4.sortingOrder or 0

	arg_2_0._map:GetComponent(typeof(UnityEngine.Canvas)).sortingOrder = var_2_5 - 2

	local var_2_6 = GetComponent(arg_2_0._map, "ItemList")

	for iter_2_2 = 1, 1 do
		local var_2_7 = var_2_6.prefabItem[iter_2_2 - 1]

		if not IsNil(var_2_7) then
			local var_2_8 = tf(Instantiate(var_2_7))

			setParent(var_2_8, arg_2_0._map)
			pg.ViewUtils.SetSortingOrder(var_2_8, var_2_5 - 1)
		end
	end
end

function var_0_0.didEnter(arg_3_0)
	onButton(arg_3_0, arg_3_0:findTF("top/back"), function()
		arg_3_0:emit(var_0_0.ON_BACK)
	end, SFX_CANCEL)
	onButton(arg_3_0, arg_3_0:findTF("top/home"), function()
		arg_3_0:emit(var_0_0.ON_HOME)
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0:findTF("top/help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_xinnian2021_feast.tip
		})
	end, SFX_PANEL)

	local var_3_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.NEWYEAR_SNACKSTREET_MINIGAME)

	arg_3_0:InitStudents(var_3_0 and var_3_0.id, 3, 4)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "daxuezhang", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 18)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "xiaochijie", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 19)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "qiaozhong", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 20)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "fuzhuangdian", function()
		arg_3_0:emit(NewYearFestivalMediator.GO_SCENE, SCENE.SKINSHOP)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "mofang", function()
		arg_3_0:emit(NewYearFestivalMediator.GO_SCENE, SCENE.GETBOAT, {
			projectName = "new",
			page = 1
		})
	end)
	arg_3_0:UpdateView()
end

function var_0_0.UpdateView(arg_12_0)
	setActive(arg_12_0.upper_daxuezhang:Find("Tip"), var_0_0.IsMiniActNeedTip(ActivityConst.NEWYEAR_SNOWBALL_FIGHT))
	setActive(arg_12_0.upper_xiaochijie:Find("Tip"), NewYearSnackPage.IsTip())
	setActive(arg_12_0.upper_qiaozhong:Find("Tip"), NewYearShrineView.IsNeedShowTipWithoutActivityFinalReward())
end

function var_0_0.willExit(arg_13_0)
	arg_13_0:clearStudents()
	var_0_0.super.willExit(arg_13_0)
end

return var_0_0
