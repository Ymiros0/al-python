local var_0_0 = class("EquipmentTraceBackMediator", import("view.base.ContextMediator"))

var_0_0.TRANSFORM_EQUIP = "transform equip"

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

	arg_1_0.env = {}

	arg_1_0.getViewComponent().SetEnv(arg_1_0.env)
	assert(arg_1_0.contextData.TargetEquipmentId, "Should Set TargetEquipment First")

	arg_1_0.env.tracebackHelper = getProxy(EquipmentProxy).GetWeakEquipsDict()

	arg_1_0.getViewComponent().UpdatePlayer(getProxy(PlayerProxy).getData())

	arg_1_0.stopUpdateView = False

def var_0_0.BindEvent(arg_2_0):
	arg_2_0.bind(var_0_0.TRANSFORM_EQUIP, function(arg_3_0, arg_3_1, arg_3_2)
		arg_2_0.stopUpdateView = True

		arg_2_0.sendNotification(GAME.TRANSFORM_EQUIPMENT, {
			candicate = arg_3_1,
			formulaIds = arg_3_2
		}))

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		PlayerProxy.UPDATED,
		BagProxy.ITEM_UPDATED,
		EquipmentProxy.EQUIPMENT_UPDATED,
		GAME.EQUIP_TO_SHIP_DONE,
		GAME.UNEQUIP_FROM_SHIP_DONE,
		GAME.TRANSFORM_EQUIPMENT_DONE,
		GAME.TRANSFORM_EQUIPMENT_FAIL
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == PlayerProxy.UPDATED:
		arg_5_0.getViewComponent().UpdatePlayer(var_5_1)
	elif var_5_0 == BagProxy.ITEM_UPDATED:
		if arg_5_0.stopUpdateView:
			return

		local var_5_2 = arg_5_0.getViewComponent()

		var_5_2.UpdateSort()
		var_5_2.UpdateSourceList()
		var_5_2.UpdateFormula()
	elif var_5_0 == EquipmentProxy.EQUIPMENT_UPDATED:
		if arg_5_0.stopUpdateView:
			return

		if arg_5_0.contextData.sourceEquipmentInstance:
			local var_5_3 = var_5_1.count == 0
			local var_5_4 = arg_5_0.contextData.sourceEquipmentInstance

			if var_5_3 and var_5_4.type == DROP_TYPE_EQUIP and EquipmentProxy.SameEquip(var_5_1, var_5_4.template):
				arg_5_0.contextData.sourceEquipmentInstance = None

		local var_5_5 = arg_5_0.getViewComponent()

		var_5_5.UpdateSourceEquipmentPaths()
		var_5_5.UpdateSort()
		var_5_5.UpdateSourceList()
		var_5_5.UpdateFormula()
	elif var_5_0 == GAME.UNEQUIP_FROM_SHIP_DONE or var_5_0 == GAME.EQUIP_TO_SHIP_DONE:
		if arg_5_0.stopUpdateView:
			return

		local var_5_6 = arg_5_0.contextData.sourceEquipmentInstance

		if var_5_6 and var_5_6.type == DROP_TYPE_EQUIP:
			local var_5_7 = var_5_1.getEquip(var_5_6.template.shipPos)

			if var_5_6.template.shipId == var_5_1.id and (not var_5_7 or var_5_7.id != var_5_6.id):
				arg_5_0.contextData.sourceEquipmentInstance = None

		local var_5_8 = arg_5_0.getViewComponent()

		var_5_8.UpdateSourceEquipmentPaths()
		var_5_8.UpdateSort()
		var_5_8.UpdateSourceList()
		var_5_8.UpdateFormula()
	elif var_5_0 == GAME.TRANSFORM_EQUIPMENT_DONE or var_5_0 == GAME.TRANSFORM_EQUIPMENT_FAIL:
		arg_5_0.stopUpdateView = False

		local var_5_9 = arg_5_0.getViewComponent()

		var_5_9.UpdateSourceEquipmentPaths()
		var_5_9.UpdateSort()
		var_5_9.UpdateSourceList()
		var_5_9.UpdateFormula()

return var_0_0
