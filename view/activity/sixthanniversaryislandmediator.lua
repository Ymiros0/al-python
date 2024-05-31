local var_0_0 = class("SixthAnniversaryIslandMediator", import("..base.ContextMediator"))

var_0_0.TRIGGER_NODE_EVENT = "SixthAnniversaryIslandMediator.TRIGGER_NODE_EVENT"
var_0_0.OPEN_QTE_GAME = "SixthAnniversaryIslandMediator.OPEN_QTE_GAME"
var_0_0.INTO_ENTRANCE = "SixthAnniversaryIslandMediator.INTO_ENTRANCE"
var_0_0.MARK_NODE_AFTER_NEW = "SixthAnniversaryIslandMediator.MARK_NODE_AFTER_NEW"
var_0_0.GO_SHOP = "SixthAnniversaryIslandMediator.GO_SHOP"
var_0_0.OPEN_NOTE = "SixthAnniversaryIslandMediator.OPEN_NOTE"
var_0_0.OPEN_RES = "SixthAnniversaryIslandMediator.OPEN_RES"
var_0_0.DISPLAY_NODES = "SixthAnniversaryIslandMediator.DISPLAY_NODES"
var_0_0.DISPLAY_SHOP = "SixthAnniversaryIslandMediator.DISPLAY_SHOP"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_ISLAND)

	arg_1_0.viewComponent:setActivity(var_1_0)
	arg_1_0.viewComponent:setNodeIds(getProxy(IslandProxy):GetNodeIds())
	arg_1_0.viewComponent:setPlayer(getProxy(PlayerProxy):getData())

	local var_1_1 = getProxy(ActivityProxy):getActivityById(ActivityConst.ISLAND_GAME_ID):getConfig("config_id")

	arg_1_0.viewComponent:setResDrop({
		type = 2,
		id = getProxy(ActivityProxy):getActivityById(ActivityConst.ISLAND_GAME_ID):getConfig("config_client").item_id,
		count = getProxy(MiniGameProxy):GetHubByHubId(var_1_1).count
	}, pg.mini_game_hub[var_1_1].reborn_times)
	arg_1_0:bind(var_0_0.TRIGGER_NODE_EVENT, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.ISLAND_EVENT_TRIGGER, {
			act_id = var_1_0.id,
			node_id = arg_2_1,
			op = arg_2_2
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_QTE_GAME, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0:addSubLayers(Context.New({
			mediator = IslandQTEMiniGameMediator,
			viewComponent = IslandQTEMiniGameLayer,
			data = {
				mark = arg_3_1,
				finishCallback = arg_3_2
			}
		}))
	end)
	arg_1_0:bind(var_0_0.OPEN_NOTE, function(arg_4_0)
		arg_1_0:addSubLayers(Context.New({
			mediator = IslandTaskMediator,
			viewComponent = IslandTaskScene,
			data = {}
		}))
	end)
	arg_1_0:bind(var_0_0.OPEN_RES, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0:addSubLayers(Context.New({
			mediator = SixthAnniversaryIslandItemWindowMediator,
			viewComponent = SixthAnniversaryIslandItemWindowLayer,
			data = {
				drop = arg_5_1,
				text = arg_5_2
			}
		}))
	end)
	arg_1_0:bind(var_0_0.INTO_ENTRANCE, function(arg_6_0, arg_6_1)
		switch(arg_6_1, {
			flowerfield = function()
				arg_1_0:addSubLayers(Context.New({
					mediator = IslandFlowerFieldMediator,
					viewComponent = IslandFlowerFieldLayer,
					data = {}
				}))
			end,
			minigame1 = function()
				arg_1_0:sendNotification(GAME.GO_MINI_GAME, 52)
			end,
			minigame2 = function()
				arg_1_0:sendNotification(GAME.GO_MINI_GAME, 53)
			end,
			minigame3 = function()
				arg_1_0:sendNotification(GAME.GO_MINI_GAME, 54)
			end,
			island = function()
				arg_1_0.viewComponent:closeView()
			end,
			hotspringtask = function()
				arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SPRING_TASK)
			end,
			hotspring = function()
				arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SPRING)
			end
		})
	end)
	arg_1_0:bind(var_0_0.MARK_NODE_AFTER_NEW, function(arg_14_0, arg_14_1)
		arg_1_0:sendNotification(GAME.ISLAND_NODE_MARK, {
			act_id = var_1_0.id,
			node_id = arg_14_1
		})
	end)
	arg_1_0:bind(var_0_0.GO_SHOP, function(arg_15_0)
		arg_1_0:addSubLayers(Context.New({
			mediator = SixthAnniversaryIslandShopMediator,
			viewComponent = SixthAnniversaryIslandShopLayer
		}))
	end)
end

function var_0_0.initNotificationHandleDic(arg_16_0)
	arg_16_0.handleDic = {
		[GAME.ISLAND_EVENT_TRIGGER_DONE] = function(arg_17_0, arg_17_1)
			local var_17_0 = arg_17_1:getBody()
			local var_17_1 = {}

			if #var_17_0.awards > 0 then
				table.insert(var_17_1, function(arg_18_0)
					arg_17_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_17_0.awards, arg_18_0)
				end)
			end

			seriesAsync(var_17_1, function()
				arg_17_0.viewComponent:afterTriggerEvent(var_17_0.node_id)
			end)
		end,
		[GAME.ISLAND_NODE_MARK_DONE] = function(arg_20_0, arg_20_1)
			local var_20_0 = arg_20_1:getBody()

			arg_20_0.viewComponent:refreshNode(var_20_0.node_id)
		end,
		[GAME.ZERO_HOUR_OP_DONE] = function(arg_21_0, arg_21_1)
			getProxy(IslandProxy):CheckAndRequest(function()
				arg_21_0.viewComponent.nodeItemList:align(#arg_21_0.viewComponent.ids)
				arg_21_0.viewComponent:refreshDailyPanel()
			end)
		end,
		[PlayerProxy.UPDATED] = function(arg_23_0, arg_23_1)
			local var_23_0 = arg_23_1:getBody()

			arg_23_0.viewComponent:setPlayer(var_23_0)
		end,
		[MiniGameProxy.ON_HUB_DATA_UPDATE] = function(arg_24_0, arg_24_1)
			local var_24_0 = arg_24_1:getBody()
			local var_24_1 = getProxy(ActivityProxy):getActivityById(ActivityConst.ISLAND_GAME_ID):getConfig("config_id")

			if var_24_0.id == var_24_1 then
				arg_24_0.viewComponent:setResDrop({
					type = 2,
					id = getProxy(ActivityProxy):getActivityById(ActivityConst.ISLAND_GAME_ID):getConfig("config_client").item_id,
					count = getProxy(MiniGameProxy):GetHubByHubId(var_24_1).count
				}, pg.mini_game_hub[var_24_1].reborn_times)
			end
		end,
		[var_0_0.DISPLAY_NODES] = function(arg_25_0, arg_25_1)
			local var_25_0 = arg_25_1:getBody()

			if var_25_0 and #var_25_0 > 0 and not arg_25_0.viewComponent:focusList(var_25_0, LeanTweenType.easeInOutSine) then
				pg.TipsMgr.GetInstance():ShowTips(i18n("islandnode_tips8"))
			end
		end,
		[var_0_0.DISPLAY_SHOP] = function(arg_26_0, arg_26_1)
			arg_26_0:addSubLayers(Context.New({
				mediator = SixthAnniversaryIslandShopMediator,
				viewComponent = SixthAnniversaryIslandShopLayer
			}))
		end,
		[GAME.ISLAND_FLOWER_GET_DONE] = function(arg_27_0, arg_27_1)
			for iter_27_0, iter_27_1 in pairs(getProxy(IslandProxy):GetNodeDic()) do
				if iter_27_1:getConfig("type") == 5 and iter_27_1:getConfig("params")[1] == "flowerfield" then
					arg_27_0.viewComponent:refreshNode(iter_27_0)
				end
			end
		end,
		[ActivityProxy.ACTIVITY_UPDATED] = function(arg_28_0, arg_28_1)
			if arg_28_1:getBody().id == ActivityConst.ISLAND_TASK_ID then
				arg_28_0.viewComponent:updateTaskTip()
			end
		end
	}
end

return var_0_0
