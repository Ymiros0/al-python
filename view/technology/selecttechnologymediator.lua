local var_0_0 = class("SelectTechnologyMediator", import("..base.ContextMediator"))

var_0_0.ON_BLUEPRINT = "SelectTechnologyMediator:ON_BLUEPRINT"
var_0_0.ON_TECHNOLOGY = "SelectTechnologyMediator:ON_TECHNOLOGY"
var_0_0.ON_TRANSFORM_EQUIPMENT = "SelectTechnologyMediator:ON_TRANSFORM_EQUIPMENT"
var_0_0.ON_META = "SelectTechnologyMediator:ON_META"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_TECHNOLOGY, function()
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.TECHNOLOGY)
	end)
	arg_1_0:bind(var_0_0.ON_BLUEPRINT, function()
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SHIPBLUEPRINT)
	end)
	arg_1_0:bind(TechnologyConst.OPEN_TECHNOLOGY_TREE_SCENE, function()
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.TECHNOLOGY_TREE_SCENE)
	end)
	arg_1_0:bind(var_0_0.ON_TRANSFORM_EQUIPMENT, function()
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.EQUIPMENT_TRANSFORM)
	end)
	arg_1_0:bind(var_0_0.ON_META, function()
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.METACHARACTER)
	end)

	local var_1_0 = getProxy(PlayerProxy)

	arg_1_0.viewComponent:setPlayer(var_1_0:getData())

	local var_1_1 = var_0_0.onTechnologyNotify()

	arg_1_0.viewComponent:notifyTechnology(var_1_1)

	local var_1_2 = var_0_0.onBlueprintNotify()

	arg_1_0.viewComponent:notifyBlueprint(var_1_2)

	local var_1_3 = getProxy(TechnologyNationProxy):getShowRedPointTag()

	arg_1_0.viewComponent:notifyFleet(var_1_3)

	local var_1_4 = MetaCharacterConst.isMetaMainEntRedPoint()

	arg_1_0.viewComponent:notifyMeta(var_1_4)
end

function var_0_0.onTechnologyNotify()
	local var_7_0 = getProxy(TechnologyProxy):getPlanningTechnologys()

	return #var_7_0 > 0 and var_7_0[#var_7_0]:isCompleted()
end

function var_0_0.onBlueprintNotify()
	local var_8_0 = getProxy(TechnologyProxy)

	if PlayerPrefs.GetString("technology_day_mark", "") ~= pg.TimeMgr.GetInstance():CurrentSTimeDesc("%Y/%m/%d", true) and var_8_0:CheckPursuingCostTip() then
		return true
	end

	local var_8_1 = var_8_0:getBluePrints()
	local var_8_2 = var_8_0:getBuildingBluePrint()

	if not var_8_2 then
		return _.any(_.values(var_8_1), function(arg_9_0)
			local var_9_0 = arg_9_0:getState() == ShipBluePrint.STATE_LOCK
			local var_9_1, var_9_2 = arg_9_0:isFinishPrevTask()

			return var_9_0 and var_9_1
		end)
	else
		if var_8_2:getState() == ShipBluePrint.STATE_DEV_FINISHED then
			return true
		end

		local var_8_3 = false
		local var_8_4 = var_8_2:getTaskIds()

		return _.any(var_8_4, function(arg_10_0)
			local var_10_0 = var_8_2:getTaskStateById(arg_10_0)
			local var_10_1 = getProxy(TaskProxy):isFinishPrevTasks(arg_10_0)

			return var_10_0 == (ShipBluePrint.TASK_STATE_OPENING and var_10_1) or var_10_0 == ShipBluePrint.TASK_STATE_ACHIEVED
		end)
	end

	return false
end

function var_0_0.listNotificationInterests(arg_11_0)
	return {
		PlayerProxy.UPDATED
	}
end

function var_0_0.handleNotification(arg_12_0, arg_12_1)
	local var_12_0 = arg_12_1:getName()
	local var_12_1 = arg_12_1:getBody()

	if var_12_0 == PlayerProxy.UPDATED then
		arg_12_0.viewComponent:setPlayer(var_12_1)
	end
end

return var_0_0
