﻿local var_0_0 = class("BuildShipMediator", import("...base.ContextMediator"))

var_0_0.OPEN_DESTROY = "BuildShipMediator OPEN_CHUANWUSTART"
var_0_0.OPEN_START_PROJECT = "BuildShipMediator OPEN_START_PROJECT"
var_0_0.ACTIVITY_OPERATION = "BuildShipMediator ACTIVITY_OPERATION"
var_0_0.OPEN_PROJECT_LIST = "BuildShipMediator OPEN_PROJECT_LIST"
var_0_0.REMOVE_PROJECT_LIST = "BuildShipMediator REMOVE_PROJECT_LIST"
var_0_0.ON_BUILD = "BuildShipMediator ON_BUILD"
var_0_0.ACT_ON_BUILD = "BuildShipMediator ACT_ON_BUILD"
var_0_0.ON_UPDATE_ACT = "BuildShipMediator ON_UPDATE_ACT"
var_0_0.ON_UPDATE_FREE_BUILD_ACT = "BuildShipMediator ON_UPDATE_FREE_BUILD_ACT"
var_0_0.SIMULATION_BATTLE = "BuildShipMediator SIMULATION_BATTLE"
var_0_0.ON_SUPPORT_SHOP = "BuildShipMediator ON_SUPPORT_SHOP"
var_0_0.OPEN_PRAY_PAGE = "BuildShipMediator OPEN_PRAY_PAGE"
var_0_0.CLOSE_PRAY_PAGE = "BuildShipMediator CLOSE_PRAY_PAGE"
var_0_0.ON_BUILDPOOL_EXCHANGE = "BuildShipMediator:ON_BUILDPOOL_EXCHANGE"
var_0_0.ON_BUILDPOOL_UR_EXCHANGE = "BuildShipMediator.ON_BUILDPOOL_UR_EXCHANGE"
var_0_0.ON_SUPPORT_EXCHANGE = "BuildShipMediator:ON_SUPPORT_EXCHANGE"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(PlayerProxy):getData()

	arg_1_0.viewComponent:setPlayer(var_1_0)

	local var_1_1 = getProxy(BagProxy)

	arg_1_0.useItem = pg.ship_data_create_material[1].use_item

	local var_1_2 = var_1_1:getItemById(arg_1_0.useItem)

	arg_1_0.viewComponent:setUseItem(var_1_2)

	local var_1_3 = getProxy(BayProxy):getShipById(var_1_0.character)

	arg_1_0.viewComponent:setFlagShip(var_1_3)

	local var_1_4 = getProxy(BuildShipProxy)
	local var_1_5 = var_1_4:getRawData()

	arg_1_0.viewComponent:setStartCount(table.getCount(var_1_5))
	arg_1_0:bind(var_0_0.ON_SUPPORT_SHOP, function()
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
			warp = NewShopsScene.TYPE_MEDAL
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_DESTROY, function(arg_3_0)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			blockLock = true,
			mode = DockyardScene.MODE_DESTROY,
			selectedMax = getGameset("ship_select_limit")[1],
			leftTopInfo = i18n("word_destroy"),
			onShip = ShipStatus.canDestroyShip,
			ignoredIds = pg.ShipFlagMgr.GetInstance():FilterShips({
				isActivityNpc = true
			}),
			preView = arg_1_0.viewComponent.__cname
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_PROJECT_LIST, function(arg_4_0)
		if arg_1_0.facade:hasMediator(BuildShipDetailMediator.__cname) then
			return
		end

		arg_1_0:addSubLayers(Context.New({
			mediator = BuildShipDetailMediator,
			viewComponent = BuildShipDetailLayer,
			data = {
				LayerWeightMgr_groupName = LayerWeightConst.GROUP_BUILDSHIPSCENE
			}
		}))
	end)
	arg_1_0:bind(var_0_0.REMOVE_PROJECT_LIST, function(arg_5_0)
		local var_5_0 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(BuildShipDetailMediator)

		if var_5_0 then
			arg_1_0:sendNotification(GAME.REMOVE_LAYERS, {
				context = var_5_0
			})
		end
	end)
	arg_1_0:bind(var_0_0.ON_BUILD, function(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
		arg_1_0:sendNotification(GAME.BUILD_SHIP, {
			buildId = arg_6_1,
			count = arg_6_2,
			isTicket = arg_6_3
		})
	end)
	arg_1_0:bind(var_0_0.ACT_ON_BUILD, function(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4)
		arg_1_0:sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = arg_7_1,
			arg1 = arg_7_3,
			arg2 = arg_7_4 and 1 or 0,
			buildId = arg_7_2
		})
	end)
	arg_1_0:bind(var_0_0.ON_SUPPORT_EXCHANGE, function(arg_8_0, arg_8_1)
		arg_1_0:sendNotification(GAME.SUPPORT_SHIP, {
			count = arg_8_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_UPDATE_ACT, function(arg_9_0)
		arg_1_0.viewComponent:setPools(getProxy(BuildShipProxy):GetPools())
		arg_1_0.viewComponent:checkPage()
	end)
	arg_1_0:bind(var_0_0.OPEN_PRAY_PAGE, function(arg_10_0)
		arg_1_0:addSubLayers(Context.New({
			mediator = PrayPoolMediator,
			viewComponent = PrayPoolScene,
			data = {
				LayerWeightMgr_groupName = LayerWeightConst.GROUP_BUILDSHIPSCENE
			}
		}))
	end)
	arg_1_0:bind(var_0_0.CLOSE_PRAY_PAGE, function(arg_11_0)
		local var_11_0 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(PrayPoolMediator)

		if var_11_0 then
			arg_1_0:sendNotification(GAME.REMOVE_LAYERS, {
				context = var_11_0
			})
		end
	end)
	arg_1_0:bind(var_0_0.SIMULATION_BATTLE, function(arg_12_0, arg_12_1)
		arg_1_0:sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_SIMULATION,
			stageId = arg_12_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_BUILDPOOL_EXCHANGE, function(arg_13_0, arg_13_1)
		arg_1_0:sendNotification(GAME.ACTIVITY_BUILD_POOL_EXCHANGE, {
			activity_id = arg_13_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_BUILDPOOL_UR_EXCHANGE, function(arg_14_0)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = BuildShipRegularExchangeLayer,
			mediator = BuildShipRegularExchangeMediator
		}))
	end)

	local var_1_6 = var_1_4:getFinishCount()

	arg_1_0.viewComponent:updateQueueTip(var_1_6)
	arg_1_0.viewComponent:setPools(getProxy(BuildShipProxy):GetPools())

	if arg_1_0.contextData.goToPray == true then
		arg_1_0.viewComponent:switchPage(arg_1_0.viewComponent.PAGE_PRAY, true)
	end
end

function var_0_0.buildFinishComeback(arg_15_0)
	local var_15_0 = getProxy(BuildShipProxy)

	if table.getCount(var_15_0:getData()) == 0 and arg_15_0.viewComponent then
		local var_15_1 = BuildShip.getPageFromPoolType(var_15_0:getLastBuildShipPoolType()) or BuildShipScene.PAGE_BUILD

		if var_15_1 == BuildShipScene.PAGE_PRAY then
			local var_15_2 = getProxy(ActivityProxy):getActivityById(ActivityConst.ACTIVITY_PRAY_POOL)

			if not var_15_2 or var_15_2:isEnd() then
				var_15_1 = BuildShipScene.PAGE_BUILD
			end
		end

		triggerToggle(arg_15_0.viewComponent.toggles[var_15_1], true)
	end
end

function var_0_0.listNotificationInterests(arg_16_0)
	return {
		GAME.BUILD_SHIP_DONE,
		BagProxy.ITEM_UPDATED,
		PlayerProxy.UPDATED,
		GAME.CONFIRM_GET_SHIP,
		BuildShipProxy.ADDED,
		BuildShipProxy.REMOVED,
		GAME.BEGIN_STAGE_DONE,
		GAME.ACTIVITY_BUILD_POOL_EXCHANGE_DONE,
		GAME.REGULAR_BUILD_POOL_EXCHANGE_DONE,
		ActivityProxy.ACTIVITY_UPDATED,
		GAME.SUPPORT_SHIP_DONE,
		BuildShipProxy.REGULAR_BUILD_POOL_COUNT_UPDATE
	}
end

function var_0_0.handleNotification(arg_17_0, arg_17_1)
	local var_17_0 = arg_17_1:getName()
	local var_17_1 = arg_17_1:getBody()

	if var_17_0 == PlayerProxy.UPDATED then
		arg_17_0.viewComponent:setPlayer(var_17_1)
	elseif var_17_0 == GAME.CONFIRM_GET_SHIP then
		local var_17_2 = getProxy(BuildShipProxy)
		local var_17_3 = var_17_2:getFinishCount()

		arg_17_0.viewComponent:updateQueueTip(var_17_3)

		local var_17_4 = {}

		if var_17_1.isBatch then
			var_17_2:setSkipBatchBuildFlag(false)

			local var_17_5 = {}

			for iter_17_0, iter_17_1 in ipairs(var_17_1.ships) do
				local var_17_6 = {
					type = DROP_TYPE_SHIP,
					id = iter_17_1.configId
				}

				var_17_6.count = 1
				var_17_6.virgin = iter_17_1.virgin
				var_17_6.reMetaSpecialItemVO = iter_17_1:getReMetaSpecialItemVO()
				var_17_5[#var_17_5 + 1] = var_17_6
			end

			if #var_17_5 > 0 then
				table.insert(var_17_4, function(arg_18_0)
					arg_17_0.viewComponent:emit(BaseUI.ON_AWARD, {
						items = var_17_5,
						title = AwardInfoLayer.TITLE.SHIP,
						removeFunc = arg_18_0
					})
				end)
			end
		end

		seriesAsync(var_17_4, function()
			if var_17_1.isBatch and var_17_3 > 0 then
				NoPosMsgBox(i18n("switch_to_shop_tip_noDockyard"), openDockyardClear, gotoChargeScene, openDockyardIntensify)
			else
				arg_17_0:buildFinishComeback()
			end
		end)
	elseif var_17_0 == GAME.BUILD_SHIP_DONE then
		triggerToggle(arg_17_0.viewComponent.toggles[BuildShipScene.PAGE_QUEUE], true)
	elseif var_17_0 == BagProxy.ITEM_UPDATED then
		local var_17_7 = getProxy(BagProxy):getItemById(arg_17_0.useItem)

		arg_17_0.viewComponent:setUseItem(var_17_7)
	elseif var_17_0 == BuildShipProxy.ADDED or var_17_0 == BuildShipProxy.REMOVED then
		local var_17_8 = getProxy(BuildShipProxy):getRawData()

		arg_17_0.viewComponent:setStartCount(table.getCount(var_17_8))
	elseif var_17_0 == GAME.SUPPORT_SHIP_DONE then
		local var_17_9 = {}

		for iter_17_2, iter_17_3 in ipairs(var_17_1.ships) do
			if iter_17_3.virgin or iter_17_3:getRarity() >= 4 then
				table.insert(var_17_9, function(arg_20_0)
					arg_17_0:addSubLayers(Context.New({
						mediator = NewShipMediator,
						viewComponent = NewShipLayer,
						data = {
							ship = iter_17_3
						},
						onRemoved = arg_20_0
					}))
				end)
			end
		end

		seriesAsync(var_17_9, function()
			arg_17_0.viewComponent:emit(BaseUI.ON_AWARD, {
				items = underscore.map(var_17_1.ships, function(arg_22_0)
					local var_22_0 = Drop.New({
						count = 1,
						type = DROP_TYPE_SHIP,
						id = arg_22_0.configId
					})

					var_22_0.virgin = arg_22_0.virgin

					return var_22_0
				end),
				title = AwardInfoLayer.TITLE.SHIP,
				removeFunc = function()
					if arg_17_0.viewComponent then
						arg_17_0.viewComponent.supportShipPoolPage:UpdateMedal()
					end
				end
			})
		end)
	elseif var_17_0 == GAME.BEGIN_STAGE_DONE then
		arg_17_0:sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_17_1)
	elseif var_17_0 == ActivityProxy.ACTIVITY_UPDATED then
		local var_17_10 = var_17_1

		if var_17_10 then
			local var_17_11 = var_17_10:getConfig("type")

			if var_17_11 == ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1 then
				arg_17_0.viewComponent:RefreshActivityBuildPool(var_17_10)
			elseif var_17_11 == ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD then
				local var_17_12 = pg.ship_data_create_exchange[var_17_10.id] or {}

				if var_17_10.data2 < (var_17_12.exchange_available_times or 0) then
					arg_17_0.viewComponent:RefreshActivityBuildPool(var_17_10)
				else
					arg_17_0.viewComponent:setPools(getProxy(BuildShipProxy):GetPools())
					arg_17_0.viewComponent:checkPage()
				end
			elseif var_17_11 == ActivityConst.ACTIVITY_TYPE_BUILD_FREE then
				arg_17_0.viewComponent:RefreshFreeBuildActivity()
			end
		end
	elseif var_17_0 == BuildShipProxy.REGULAR_BUILD_POOL_COUNT_UPDATE then
		arg_17_0.viewComponent:RefreshRegularExchangeCount()
	elseif var_17_0 == GAME.ACTIVITY_BUILD_POOL_EXCHANGE_DONE or var_17_0 == GAME.REGULAR_BUILD_POOL_EXCHANGE_DONE then
		arg_17_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_17_1.awards)
	end
end

return var_0_0
