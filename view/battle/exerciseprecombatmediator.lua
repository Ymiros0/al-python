﻿local var_0_0 = class("ExercisePreCombatMediator", import("..base.ContextMediator"))

var_0_0.ON_START = "ExercisePreCombatMediator:ON_START"
var_0_0.ON_CHANGE_FLEET = "ExercisePreCombatMediator:ON_CHANGE_FLEET"
var_0_0.ON_COMMIT_EDIT = "ExercisePreCombatMediator:ON_COMMIT_EDIT"
var_0_0.OPEN_SHIP_INFO = "ExercisePreCombatMediator:OPEN_SHIP_INFO"
var_0_0.REMOVE_SHIP = "ExercisePreCombatMediator:REMOVE_SHIP"
var_0_0.CHANGE_FLEET_SHIPS_ORDER = "ExercisePreCombatMediator:CHANGE_FLEET_SHIPS_ORDER"
var_0_0.CHANGE_FLEET_SHIP = "ExercisePreCombatMediator:CHANGE_FLEET_SHIP"
var_0_0.ON_AUTO = "ExercisePreCombatMediator:ON_AUTO"
var_0_0.ON_SUB_AUTO = "ExercisePreCombatMediator:ON_SUB_AUTO"

function var_0_0.register(arg_1_0)
	arg_1_0.ships = getProxy(BayProxy):getRawData()

	arg_1_0.viewComponent:SetShips(arg_1_0.ships)

	local var_1_0 = arg_1_0.contextData.system
	local var_1_1 = getProxy(FleetProxy)
	local var_1_2
	local var_1_3 = var_1_1:getData()

	if arg_1_0.contextData.EdittingFleet then
		var_1_1.EdittingFleet = arg_1_0.contextData.EdittingFleet
		arg_1_0.contextData.EdittingFleet = nil
	end

	if var_1_1.EdittingFleet ~= nil then
		var_1_3[var_1_1.EdittingFleet.id] = var_1_1.EdittingFleet
	end

	arg_1_0.viewComponent:SetFleets(var_1_3)

	local var_1_4 = getProxy(PlayerProxy):getData()

	arg_1_0.viewComponent:SetPlayerInfo(var_1_4)
	arg_1_0.viewComponent:SetCurrentFleet(FleetProxy.PVP_FLEET_ID)
	arg_1_0:bind(var_0_0.ON_CHANGE_FLEET, function(arg_2_0, arg_2_1)
		arg_1_0:changeFleet(arg_2_1)
	end)
	arg_1_0:bind(var_0_0.ON_AUTO, function(arg_3_0, arg_3_1)
		arg_1_0:onAutoBtn(arg_3_1)
	end)
	arg_1_0:bind(var_0_0.ON_SUB_AUTO, function(arg_4_0, arg_4_1)
		arg_1_0:onAutoSubBtn(arg_4_1)
	end)
	arg_1_0:bind(var_0_0.CHANGE_FLEET_SHIPS_ORDER, function(arg_5_0, arg_5_1)
		arg_1_0:refreshEdit(arg_5_1)
	end)
	arg_1_0:bind(var_0_0.REMOVE_SHIP, function(arg_6_0, arg_6_1, arg_6_2)
		arg_6_2:removeShip(arg_6_1)

		getProxy(FleetProxy).EdittingFleet = arg_6_2

		arg_1_0:refreshEdit(arg_6_2)
	end)
	arg_1_0:bind(var_0_0.OPEN_SHIP_INFO, function(arg_7_0, arg_7_1, arg_7_2)
		arg_1_0.contextData.form = ExercisePreCombatLayer.FORM_EDIT

		local var_7_0 = {}

		for iter_7_0, iter_7_1 in ipairs(arg_7_2:getShipIds()) do
			table.insert(var_7_0, arg_1_0.ships[iter_7_1])
		end

		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			shipId = arg_7_1,
			shipVOs = var_7_0
		})
	end)
	arg_1_0:bind(var_0_0.CHANGE_FLEET_SHIP, function(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
		assert(arg_8_2.id == FleetProxy.PVP_FLEET_ID, "fleet type error")

		arg_1_0.contextData.form = ExercisePreCombatLayer.FORM_EDIT

		FormationMediator.saveEdit()

		local var_8_0 = var_1_0 == SYSTEM_DUEL
		local var_8_1 = var_8_0 and ShipStatus.TAG_HIDE_PVP or ShipStatus.TAG_HIDE_NORMAL
		local var_8_2 = var_8_0 and ShipStatus.TAG_BLOCK_PVP or nil
		local var_8_3, var_8_4, var_8_5 = arg_1_0:getDockCallbackFuncsForExercise(arg_8_1, arg_8_2, arg_8_3)
		local var_8_6 = {}

		for iter_8_0, iter_8_1 in ipairs(arg_8_2.ships) do
			if not arg_8_1 or iter_8_1 ~= arg_8_1.id then
				table.insert(var_8_6, iter_8_1)
			end
		end

		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 1,
			useBlackBlock = true,
			selectedMin = 0,
			energyDisplay = true,
			ignoredIds = pg.ShipFlagMgr.GetInstance():FilterShips({
				isActivityNpc = true
			}),
			leastLimitMsg = i18n("battle_preCombatMediator_leastLimit"),
			quitTeam = arg_8_1 ~= nil,
			teamFilter = arg_8_3,
			onShip = var_8_3,
			confirmSelect = var_8_4,
			onSelected = var_8_5,
			hideTagFlags = var_8_1,
			blockTagFlags = var_8_2,
			otherSelectedIds = var_8_6
		})
	end)
	arg_1_0:bind(var_0_0.ON_COMMIT_EDIT, function(arg_9_0, arg_9_1)
		arg_1_0:commitEdit(arg_9_1)
	end)
	arg_1_0:bind(var_0_0.ON_START, function(arg_10_0, arg_10_1)
		local var_10_0

		if arg_1_0.contextData.rivalId then
			var_10_0 = arg_1_0.contextData.rivalId
		else
			var_10_0 = arg_1_0.contextData.stageId
		end

		seriesAsync({
			function(arg_11_0)
				if arg_1_0.contextData.OnConfirm then
					arg_1_0.contextData.OnConfirm(arg_11_0)
				else
					arg_11_0()
				end
			end,
			function()
				arg_1_0:sendNotification(GAME.BEGIN_STAGE, {
					stageId = var_10_0,
					mainFleetId = arg_10_1,
					system = arg_1_0.contextData.system,
					actId = arg_1_0.contextData.actId,
					rivalId = arg_1_0.contextData.rivalId
				})
			end
		})
	end)
end

function var_0_0.changeFleet(arg_13_0, arg_13_1)
	if arg_13_0.contextData.system == SYSTEM_SUB_ROUTINE then
		arg_13_0.contextData.subFleetId = arg_13_1
	else
		getProxy(PlayerProxy).combatFleetId = arg_13_1
	end

	arg_13_0.viewComponent:SetCurrentFleet(arg_13_1)
	arg_13_0.viewComponent:UpdateFleetView(true)
end

function var_0_0.refreshEdit(arg_14_0, arg_14_1)
	local var_14_0 = getProxy(FleetProxy)

	var_14_0.EdittingFleet = arg_14_1

	if arg_14_0.contextData.system ~= SYSTEM_SUB_ROUTINE then
		local var_14_1 = var_14_0:getData()

		var_14_1[arg_14_1.id] = arg_14_1

		arg_14_0.viewComponent:SetFleets(var_14_1)
	end

	arg_14_0.viewComponent:UpdateFleetView(false)
end

function var_0_0.commitEdit(arg_15_0, arg_15_1)
	local var_15_0 = getProxy(FleetProxy)
	local var_15_1 = var_15_0.EdittingFleet

	if var_15_1 == nil or var_15_1:isFirstFleet() or var_15_1:isLegalToFight() == true then
		var_15_0:commitEdittingFleet(arg_15_1)
	elseif #var_15_1.ships == 0 then
		var_15_0:commitEdittingFleet(arg_15_1)

		if arg_15_0.contextData.system == SYSTEM_SUB_ROUTINE then
			-- block empty
		end
	else
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("ship_formationMediaror_trash_warning", var_15_1.defaultName),
			onYes = function()
				local var_16_0 = getProxy(BayProxy):getRawData()
				local var_16_1 = var_15_1.ships

				for iter_16_0 = #var_16_1, 1, -1 do
					var_15_1:removeShip(var_16_0[var_16_1[iter_16_0]])
				end

				if var_15_1.id == FleetProxy.PVP_FLEET_ID then
					var_15_0:commitEdittingFleet()
					arg_15_0:changeFleet(FleetProxy.PVP_FLEET_ID)
				else
					var_15_0:commitEdittingFleet(arg_15_1)
				end
			end
		})
	end
end

function var_0_0.onAutoBtn(arg_17_0, arg_17_1)
	local var_17_0 = arg_17_1.isOn
	local var_17_1 = arg_17_1.toggle

	arg_17_0:sendNotification(GAME.AUTO_BOT, {
		isActiveBot = var_17_0,
		toggle = var_17_1
	})
end

function var_0_0.onAutoSubBtn(arg_18_0, arg_18_1)
	local var_18_0 = arg_18_1.isOn
	local var_18_1 = arg_18_1.toggle

	arg_18_0:sendNotification(GAME.AUTO_SUB, {
		isActiveSub = var_18_0,
		toggle = var_18_1
	})
end

function var_0_0.listNotificationInterests(arg_19_0)
	return {
		GAME.BEGIN_STAGE_DONE,
		PlayerProxy.UPDATED,
		GAME.BEGIN_STAGE_ERRO
	}
end

function var_0_0.handleNotification(arg_20_0, arg_20_1)
	local var_20_0 = arg_20_1:getName()
	local var_20_1 = arg_20_1:getBody()

	if var_20_0 == GAME.BEGIN_STAGE_DONE then
		arg_20_0:sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_20_1)
	elseif var_20_0 == PlayerProxy.UPDATED then
		arg_20_0.viewComponent:SetPlayerInfo(getProxy(PlayerProxy):getData())
	elseif var_20_0 == GAME.BEGIN_STAGE_ERRO and var_20_1 == 3 then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			hideNo = true,
			content = i18n("battle_preCombatMediator_timeout"),
			onYes = function()
				arg_20_0.viewComponent:emit(BaseUI.ON_CLOSE)
			end
		})
	end
end

function var_0_0.getDockCallbackFuncsForExercise(arg_22_0, arg_22_1, arg_22_2, arg_22_3)
	local var_22_0 = getProxy(FleetProxy)
	local var_22_1 = getProxy(BayProxy)

	local function var_22_2(arg_23_0, arg_23_1)
		local var_23_0, var_23_1 = ShipStatus.ShipStatusCheck("inFleet", arg_23_0, arg_23_1)

		if not var_23_0 then
			return var_23_0, var_23_1
		end

		local var_23_2, var_23_3 = FormationMediator.checkChangeShip(arg_22_2, arg_22_1, arg_23_0)

		if not var_23_2 then
			return false, var_23_3
		end

		return true
	end

	local function var_22_3(arg_24_0, arg_24_1, arg_24_2)
		arg_24_1()
	end

	local function var_22_4(arg_25_0)
		local var_25_0 = var_22_1:getShipById(arg_25_0[1])
		local var_25_1 = arg_22_2:getShipPos(arg_22_1) or -1

		if var_25_1 > 0 then
			arg_22_2:removeShip(arg_22_1)
		end

		local var_25_2 = arg_22_2:getShipPos(var_25_0) or -1

		if var_25_2 > 0 then
			arg_22_2:removeShip(var_25_0)
		end

		local var_25_3 = {}

		if arg_22_1 and var_25_2 > 0 then
			table.insert(var_25_3, {
				var_25_2,
				arg_22_1
			})
		end

		if var_25_0 then
			table.insert(var_25_3, {
				var_25_1,
				var_25_0
			})
		end

		table.sort(var_25_3, function(arg_26_0, arg_26_1)
			return arg_26_0[1] < arg_26_1[1]
		end)

		for iter_25_0, iter_25_1 in ipairs(var_25_3) do
			local var_25_4 = iter_25_1[1] > 0 and iter_25_1[1] or nil
			local var_25_5 = iter_25_1[2]

			arg_22_2:insertShip(var_25_5, var_25_4, arg_22_3)
		end

		var_22_0.EdittingFleet = arg_22_2
	end

	return var_22_2, var_22_3, var_22_4
end

return var_0_0
