local var_0_0 = class("ShipPreviewMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	assert(arg_1_0.contextData.shipVO, "shipVO is None")
	assert(arg_1_0.contextData.weaponIds, "weaponIds is None")
	assert(arg_1_0.contextData.equipSkinId, "equipment skin id is None")
	arg_1_0.viewComponent.setShip(arg_1_0.contextData.shipVO, arg_1_0.contextData.weaponIds, arg_1_0.contextData.equipSkinId)

def var_0_0.listNotificationInterests(arg_2_0):
	return {}

def var_0_0.handleNotification(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.getName()
	local var_3_1 = arg_3_1.getBody()

return var_0_0
