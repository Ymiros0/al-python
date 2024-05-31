local var_0_0 = class("DockyardMediator", import("..base.ContextMediator"))

var_0_0.ON_DESTROY_SHIPS = "DockyardMediator:ON_DESTROY_SHIPS"
var_0_0.ON_SHIP_DETAIL = "DockyardMediator:ON_SHIP_DETAIL"
var_0_0.ON_SHIP_REPAIR = "DockyardMediator:ON_SHIP_REPAIR"
var_0_0.OPEN_DOCKYARD_INDEX = "DockyardMediator:OPEN_DOCKYARD_INDEX"

function var_0_0.register(arg_1_0)
	if arg_1_0.contextData.selectFriend then
		local var_1_0 = getProxy(FriendProxy):getAllFriends()

		arg_1_0.viewComponent:setFriends(var_1_0)
	end

	local var_1_1 = getProxy(BayProxy)

	if arg_1_0.contextData.shipVOs then
		arg_1_0.shipsById = {}

		for iter_1_0, iter_1_1 in ipairs(arg_1_0.contextData.shipVOs) do
			arg_1_0.shipsById[iter_1_1.id] = iter_1_1
		end
	elseif arg_1_0.contextData.mode == DockyardScene.MODE_WORLD then
		arg_1_0.shipsById = {}

		for iter_1_2, iter_1_3 in ipairs(nowWorld():GetShipVOs()) do
			arg_1_0.shipsById[iter_1_3.id] = iter_1_3
		end
	else
		arg_1_0.shipsById = {}

		for iter_1_4, iter_1_5 in pairs(var_1_1.data) do
			arg_1_0.shipsById[iter_1_4] = iter_1_5
		end
	end

	if arg_1_0.contextData.mode == DockyardScene.MODE_MOD then
		local var_1_2 = arg_1_0.contextData.ignoredIds[1]

		arg_1_0.viewComponent:setModShip(arg_1_0.shipsById[var_1_2]:clone())
	end

	arg_1_0.fleetProxy = getProxy(FleetProxy)
	arg_1_0.fleetShipIds = arg_1_0.fleetProxy:getAllShipIds()

	if arg_1_0.contextData.ignoredIds then
		for iter_1_6, iter_1_7 in ipairs(arg_1_0.contextData.ignoredIds) do
			arg_1_0.shipsById[iter_1_7] = nil
		end
	end

	arg_1_0.viewComponent:setShips(arg_1_0.shipsById)
	arg_1_0.viewComponent:setShipsCount(var_1_1:getShipCount())

	local var_1_3 = getProxy(PlayerProxy):getData()

	arg_1_0.viewComponent:setPlayer(var_1_3)
	arg_1_0:bind(var_0_0.ON_DESTROY_SHIPS, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.DESTROY_SHIPS, {
			destroyEquipment = arg_2_2,
			shipIds = arg_2_1
		})
	end)
	arg_1_0:bind(var_0_0.ON_SHIP_DETAIL, function(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_3_1.id,
			shipVOs = arg_3_2,
			selectContextData = arg_3_3
		})
	end)
	arg_1_0:bind(var_0_0.ON_SHIP_REPAIR, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0:sendNotification(GAME.WORLD_SHIP_REPAIR, {
			shipIds = arg_4_1,
			totalCost = arg_4_2
		})
	end)
	arg_1_0:bind(var_0_0.OPEN_DOCKYARD_INDEX, function(arg_5_0, arg_5_1)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = CustomIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_5_1
		}))
	end)
end

function var_0_0.listNotificationInterests(arg_6_0)
	return {
		GAME.DESTROY_SHIP_DONE,
		FleetProxy.FLEET_UPDATED,
		GAME.EXIT_SHIP_DONE,
		GAME.UPDATE_EXERCISE_FLEET_DONE,
		GAME.CANCEL_LEARN_TACTICS_DONE,
		PlayerProxy.UPDATED,
		GAME.WORLD_SHIP_REPAIR_DONE,
		GAME.UPDATE_LOCK_DONE,
		GAME.WORLD_FLEET_REDEPLOY_DONE
	}
end

function var_0_0.handleNotification(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_1:getName()
	local var_7_1 = arg_7_1:getBody()

	if var_7_0 == GAME.DESTROY_SHIP_DONE then
		if not pg.m02:hasMediator(ShipMainMediator.__cname) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("ship_dockyardMediator_destroy"))
		end

		for iter_7_0, iter_7_1 in ipairs(var_7_1.destroiedShipIds) do
			arg_7_0.viewComponent:removeShip(iter_7_1)
		end

		arg_7_0.viewComponent:updateShipCount()
		arg_7_0.viewComponent:setShipsCount(getProxy(BayProxy):getShipCount())
		arg_7_0.viewComponent:updateBarInfo()
		arg_7_0.viewComponent:updateSelected()
		arg_7_0.viewComponent:updateDestroyRes()

		local function var_7_2()
			if table.getCount(var_7_1.equipments) > 0 then
				local var_8_0 = {}

				for iter_8_0, iter_8_1 in pairs(var_7_1.equipments) do
					table.insert(var_8_0, iter_8_1)
				end

				arg_7_0:addSubLayers(Context.New({
					viewComponent = ResolveEquipmentLayer,
					mediator = ResolveEquipmentMediator,
					data = {
						Equipments = var_8_0
					}
				}))
			end
		end

		arg_7_0.viewComponent:emit(BaseUI.ON_AWARD, {
			items = var_7_1.bonus,
			title = AwardInfoLayer.TITLE.ITEM,
			removeFunc = var_7_2
		})
		arg_7_0.viewComponent:closeDestroyPanel()
	elseif var_7_0 == FleetProxy.FLEET_UPDATED then
		local var_7_3 = arg_7_0.fleetShipIds

		arg_7_0.fleetShipIds = arg_7_0.fleetProxy:getAllShipIds()

		local var_7_4 = {}

		for iter_7_2, iter_7_3 in ipairs(var_7_3) do
			var_7_4[iter_7_3] = 1
		end

		for iter_7_4, iter_7_5 in ipairs(arg_7_0.fleetShipIds) do
			if var_7_4[iter_7_5] == 1 then
				var_7_4[iter_7_5] = 2
			else
				var_7_4[iter_7_5] = 3
			end
		end

		for iter_7_6, iter_7_7 in ipairs(var_7_3) do
			if var_7_4[iter_7_7] == 1 then
				var_7_4[iter_7_7] = 0
			end
		end

		for iter_7_8, iter_7_9 in pairs(var_7_4) do
			if iter_7_9 == 0 then
				arg_7_0:setShipFlag(iter_7_8, "inFleet", false)
			elseif iter_7_9 == 3 then
				arg_7_0:setShipFlag(iter_7_8, "inFleet", true)
			end

			arg_7_0.viewComponent:updateShipStatusById(iter_7_8)
		end
	elseif var_7_0 == GAME.EXIT_SHIP_DONE then
		arg_7_0:setShipFlag(var_7_1.id, "inBackyard", false)
		arg_7_0.viewComponent:updateShipStatusById(var_7_1.id)
	elseif var_7_0 == GAME.UPDATE_LOCK_DONE then
		arg_7_0.shipsById[var_7_1.id].lockState = var_7_1.lockState

		arg_7_0.viewComponent:updateShipStatusById(var_7_1.id)
	elseif var_7_0 == GAME.CANCEL_LEARN_TACTICS_DONE then
		arg_7_0:setShipFlag(var_7_1.shipId, "inTactics", false)
		arg_7_0.viewComponent:updateShipStatusById(var_7_1.shipId)
	elseif var_7_0 == GAME.UPDATE_EXERCISE_FLEET_DONE then
		local var_7_5 = var_7_1.oldFleet
		local var_7_6 = var_7_1.newFleet

		for iter_7_10, iter_7_11 in ipairs(var_7_5.ships) do
			arg_7_0:setShipFlag(iter_7_11, "inExercise", false)
			arg_7_0.viewComponent:updateShipStatusById(iter_7_11)
		end

		for iter_7_12, iter_7_13 in ipairs(var_7_6.ships) do
			arg_7_0:setShipFlag(iter_7_13, "inExercise", true)
			arg_7_0.viewComponent:updateShipStatusById(iter_7_13)
		end
	elseif var_7_0 == PlayerProxy.UPDATED then
		arg_7_0.viewComponent:setPlayer(var_7_1)
	elseif var_7_0 == GAME.WORLD_SHIP_REPAIR_DONE then
		_.each(var_7_1.shipIds, function(arg_9_0)
			arg_7_0.viewComponent:updateShipStatusById(arg_9_0)
		end)
	elseif var_7_0 == GAME.WORLD_FLEET_REDEPLOY_DONE then
		arg_7_0.viewComponent:emit(BaseUI.ON_BACK)
	end
end

function var_0_0.setShipFlag(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	local var_10_0 = arg_10_0.shipsById[arg_10_1]

	if var_10_0 then
		var_10_0[arg_10_2] = arg_10_3
	end
end

return var_0_0
