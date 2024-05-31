local var_0_0 = class("ShipEvaluationMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(CollectionProxy)

	arg_1_0.showTrans = arg_1_0.contextData.showTrans
	arg_1_0.groupId = arg_1_0.contextData.groupId

	local var_1_1 = var_1_0.getShipGroup(arg_1_0.groupId)

	arg_1_0.viewComponent.setShipGroup(var_1_1)
	arg_1_0.viewComponent.setShowTrans(arg_1_0.showTrans)
	arg_1_0.viewComponent.flushAll()
	arg_1_0.bind(ShipEvaluationLayer.EVENT_LIKE, function(arg_2_0)
		arg_1_0.sendNotification(GAME.LIKE_SHIP, arg_1_0.groupId))
	arg_1_0.bind(ShipEvaluationLayer.EVENT_EVA, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.EVALUATE_SHIP, {
			groupId = arg_1_0.groupId,
			content = arg_3_1
		}))
	arg_1_0.bind(ShipEvaluationLayer.EVENT_ZAN, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0.sendNotification(GAME.ZAN_SHIP_EVALUATION, {
			groupId = arg_1_0.groupId,
			evaId = arg_4_1,
			operation = arg_4_2
		}))
	arg_1_0.bind(ShipEvaluationLayer.EVENT_IMPEACH, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0.sendNotification(GAME.IMPEACH_SHIP_EVALUATION, {
			groupId = arg_1_0.groupId,
			evaId = arg_5_1,
			reason = arg_5_2
		}))

def var_0_0.listNotificationInterests(arg_6_0):
	return {
		CollectionProxy.GROUP_INFO_UPDATE,
		CollectionProxy.GROUP_EVALUATION_UPDATE
	}

def var_0_0.handleNotification(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.getName()
	local var_7_1 = arg_7_1.getBody()

	if var_7_0 == CollectionProxy.GROUP_INFO_UPDATE:
		local var_7_2 = var_7_1

		if arg_7_0.groupId == var_7_2:
			local var_7_3 = getProxy(CollectionProxy).getShipGroup(var_7_2)

			arg_7_0.viewComponent.setShipGroup(var_7_3)
			arg_7_0.viewComponent.flushHeart()
	elif var_7_0 == CollectionProxy.GROUP_EVALUATION_UPDATE:
		local var_7_4 = var_7_1

		if arg_7_0.groupId == var_7_4:
			local var_7_5 = getProxy(CollectionProxy).getShipGroup(var_7_4)

			arg_7_0.viewComponent.setShipGroup(var_7_5)
			arg_7_0.viewComponent.flushEva()

return var_0_0
