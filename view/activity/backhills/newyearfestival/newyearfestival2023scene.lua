﻿local var_0_0 = class("NewYearFestival2023Scene", import("..TemplateMV.BackHillTemplate"))

var_0_0.edge2area = {
	default = "map_middle",
	["4_4"] = "map_bottom"
}

function var_0_0.getUIName(arg_1_0)
	return "NewYearFestival2023UI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.top = arg_2_0:findTF("Top")
	arg_2_0._map = arg_2_0:findTF("map")

	for iter_2_0 = 0, arg_2_0._map.childCount - 1 do
		local var_2_0 = arg_2_0._map:GetChild(iter_2_0)
		local var_2_1 = go(var_2_0).name

		arg_2_0["map_" .. var_2_1] = var_2_0
	end

	arg_2_0._shipTpl = arg_2_0._map:Find("ship")
	arg_2_0.containers = {
		arg_2_0.map_middle
	}
	arg_2_0.graphPath = GraphPath.New(import("GameCfg.BackHillGraphs.NewyearFestival2023Graph"))
	arg_2_0._upper = arg_2_0:findTF("upper")

	for iter_2_1 = 0, arg_2_0._upper.childCount - 1 do
		local var_2_2 = arg_2_0._upper:GetChild(iter_2_1)
		local var_2_3 = go(var_2_2).name

		arg_2_0["upper_" .. var_2_3] = var_2_2
	end

	arg_2_0.tipTfs = _.map(_.range(arg_2_0._upper.childCount), function(arg_3_0)
		local var_3_0 = arg_2_0._upper:GetChild(arg_3_0 - 1)

		return {
			name = var_3_0.name,
			trans = var_3_0:Find("Tip")
		}
	end)

	pg.ViewUtils.SetSortingOrder(arg_2_0._map:GetChild(arg_2_0._map.childCount - 1), 1)

	arg_2_0.loader = AutoLoader.New()
end

function var_0_0.didEnter(arg_4_0)
	onButton(arg_4_0, arg_4_0.top:Find("Back"), function()
		arg_4_0:emit(var_0_0.ON_BACK)
	end)
	onButton(arg_4_0, arg_4_0.top:Find("Home"), function()
		arg_4_0:emit(var_0_0.ON_HOME)
	end)
	onButton(arg_4_0, arg_4_0.top:Find("Help"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.resorts_help.tip
		})
	end)
	arg_4_0:InitFacilityCross(arg_4_0._map, arg_4_0._upper, "hotspring", function()
		arg_4_0:emit(BackHillMediatorTemplate.GO_SCENE, SCENE.HOTSPRING)
	end)
	arg_4_0:InitFacilityCross(arg_4_0._map, arg_4_0._upper, "duihuanwu", function()
		local var_9_0 = Context.New()

		SCENE.SetSceneInfo(var_9_0, SCENE.HOTSPRING_SHOP)
		arg_4_0:emit(BackHillMediatorTemplate.GO_SUBLAYER, var_9_0)
	end)
	arg_4_0:InitFacilityCross(arg_4_0._map, arg_4_0._upper, "firework", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 44)
	end)
	arg_4_0:InitFacilityCross(arg_4_0._map, arg_4_0._upper, "shrine", function()
		pg.m02:sendNotification(GAME.GO_MINI_GAME, 45)
	end)
	arg_4_0:InitFacilityCross(arg_4_0._map, arg_4_0._upper, "fudai", function()
		arg_4_0:emit(BackHillMediatorTemplate.GO_SCENE, SCENE.HOTSPRING_REDPACKET)
	end)
	arg_4_0:BindItemBuildShip()
	arg_4_0:BindItemSkinShop()
	arg_4_0:InitStudents(ActivityConst.MINIGAME_FIREWORK_VS_SAIREN, 3, 4)
	arg_4_0:UpdateView()
end

function var_0_0.UpdateActivity(arg_13_0, arg_13_1)
	arg_13_0:UpdateView()
end

function var_0_0.UpdateView(arg_14_0)
	_.each(arg_14_0.tipTfs, function(arg_15_0)
		local var_15_0 = switch(arg_15_0.name, {
			fudai = function()
				return BeachPacketLayer.isShowRedPoint()
			end,
			hotspring = function()
				local var_17_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

				return Activity.IsActivityReady(var_17_0)
			end,
			shrine = function()
				return Shrine2023View.IsNeedShowTipWithoutActivityFinalReward()
			end,
			duihuanwu = function()
				return AmusementParkShopPage.GetActivityShopTip()
			end,
			firework = function()
				return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MINIGAME_FIREWORK_VS_SAIREN)
			end
		}, function()
			return false
		end)

		setActive(arg_15_0.trans, tobool(var_15_0))
	end)
end

function var_0_0.IsShowMainTip(arg_22_0)
	local var_22_0 = {
		fudai = function()
			return BeachPacketLayer.isShowRedPoint()
		end,
		hotspring = function()
			local var_24_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

			return Activity.IsActivityReady(var_24_0)
		end,
		shrine = function()
			return Shrine2023View.IsNeedShowTipWithoutActivityFinalReward()
		end,
		duihuanwu = function()
			return AmusementParkShopPage.GetActivityShopTip()
		end,
		firework = function()
			return BackHillTemplate.IsMiniActNeedTip(ActivityConst.MINIGAME_FIREWORK_VS_SAIREN)
		end
	}

	return _.any(_.values(var_22_0), function(arg_28_0)
		return arg_28_0()
	end)
end

function var_0_0.willExit(arg_29_0)
	arg_29_0:clearStudents()
	var_0_0.super.willExit(arg_29_0)
end

return var_0_0
