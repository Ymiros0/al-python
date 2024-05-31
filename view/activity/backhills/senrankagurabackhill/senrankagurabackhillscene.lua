﻿local var_0_0 = class("SenrankaguraBackHillScene", import("view.activity.BackHills.TemplateMV.BackHillTemplate"))

function var_0_0.getUIName(arg_1_0)
	return "SenrankaguraBackHillUI"
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
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.SenrankaguraBackHillGraph"))
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
			helps = pg.gametip.senrankagura_backhill_help.tip
		})
	end, SFX_PANEL)

	local var_3_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_BUFF)

	arg_3_0:InitStudents(var_3_0 and var_3_0.id, 2, 3)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "renshuzhidaochang", function()
		arg_3_0:emit(BackHillMediatorTemplate.GO_SCENE, SCENE.SENRANKAGURA_TRAIN)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "michuanrenfashu", function()
		arg_3_0:emit(BackHillMediatorTemplate.GO_SCENE, SCENE.SENRANKAGURA_MEDAL)
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "renzherenwuban", function()
		arg_3_0:emit(BackHillMediatorTemplate.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.SENRANKAGURA_TURNTABLE
		})
	end)
	arg_3_0:InitFacilityCross(arg_3_0._map, arg_3_0._upper, "baochouleijisuo", function()
		arg_3_0:emit(BackHillMediatorTemplate.GO_SCENE, SCENE.ACTIVITY, {
			id = ActivityConst.SENRANKAGURA_PT
		})
	end)
	arg_3_0:BindItemActivityShop()
	arg_3_0:BindItemSkinShop()
	arg_3_0:BindItemBuildShip()
	arg_3_0:BindItemBattle()
	arg_3_0:UpdateView()
end

function var_0_0.UpdateView(arg_11_0)
	setActive(arg_11_0.upper_renshuzhidaochang:Find("Tip"), var_0_0.TrainTip())
	setActive(arg_11_0.upper_michuanrenfashu:Find("Tip"), var_0_0.MedalTip())
	setActive(arg_11_0.upper_renzherenwuban:Find("Tip"), var_0_0.TaskTip())
	setActive(arg_11_0.upper_baochouleijisuo:Find("Tip"), var_0_0.PTTip())
end

function var_0_0.willExit(arg_12_0)
	arg_12_0:clearStudents()
	var_0_0.super.willExit(arg_12_0)
end

function var_0_0.MedalTip()
	local var_13_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_MEDAL_ID)

	return Activity.IsActivityReady(var_13_0) or SenrankaguraMedalScene.GetTaskCountAble()
end

function var_0_0.TaskTip()
	local var_14_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_TURNTABLE)

	return Activity.IsActivityReady(var_14_0)
end

function var_0_0.PTTip()
	local var_15_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_PT)

	return Activity.IsActivityReady(var_15_0)
end

function var_0_0.TrainTip()
	local var_16_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.SENRANKAGURA_TRAIN_ACT_ID)

	return Activity.IsActivityReady(var_16_0)
end

function var_0_0.IsShowMainTip(arg_17_0)
	if arg_17_0 and not arg_17_0:isEnd() then
		return var_0_0.PTTip() or var_0_0.MedalTip() or var_0_0.TaskTip() or var_0_0.TrainTip()
	end
end

return var_0_0
