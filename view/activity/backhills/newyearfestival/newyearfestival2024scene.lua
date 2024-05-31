﻿local var_0_0 = class("NewYearFestival2024Scene", import("view.activity.BackHills.TemplateMV.BackHillTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "NewYearFestival2024UI"
end

var_0_0.edge2area = {
	default = "_SDPlace"
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

	arg_2_0._upper = arg_2_0:findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1 do
		local var_2_2 = arg_2_0._upper:GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2
	end

	arg_2_0._SDPlace = arg_2_0._tf:Find("SDPlace")
	arg_2_0.containers = {
		arg_2_0._SDPlace
	}
	arg_2_0._shipTpl = arg_2_0._map:Find("ship")
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.NewyearFestival2024Graph"))
end

function var_0_0.didEnter(arg_3_0)
	onButton(arg_3_0, arg_3_0:findTF("top/Back"), function()
		arg_3_0:onBackPressed()
	end, SFX_CANCEL)
	onButton(arg_3_0, arg_3_0:findTF("top/Home"), function()
		arg_3_0:quickExitFunc()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0:findTF("top/Help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.newyear2024_backhill_help.tip
		})
	end, SFX_PANEL)

	local var_3_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.MINIGAME_COOKGAME2_ID)

	arg_3_0:InitStudents(var_3_0 and var_3_0.id, 2, 3)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "nvpudian", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 60)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "huimaqiyuan", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 62)
	end)
	arg_3_0:BindItemSkinShop()
	arg_3_0:BindItemBuildShip()
	arg_3_0:UpdateView()
end

function var_0_0.UpdateView(arg_9_0)
	setActive(arg_9_0.upper_nvpudian:Find("Tip"), var_0_0.MiniGameTip())
	setActive(arg_9_0.upper_huimaqiyuan:Find("Tip"), var_0_0.ShrineTip())
end

function var_0_0.ShrineTip()
	return Shrine2024View.IsNeedShowTipWithoutActivityFinalReward()
end

function var_0_0.MiniGameTip()
	local var_11_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.MINIGAME_COOKGAME2_ID)

	return Activity.IsActivityReady(var_11_0)
end

function var_0_0.willExit(arg_12_0)
	arg_12_0:clearStudents()
	var_0_0.super.willExit(arg_12_0)
end

function var_0_0.IsShowMainTip(arg_13_0)
	if arg_13_0 and not arg_13_0:isEnd() then
		return var_0_0.MiniGameTip() or var_0_0.ShrineTip()
	end
end

return var_0_0
