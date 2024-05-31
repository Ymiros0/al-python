local var_0_0 = class("NewBackYardShopMediator", import("...base.ContextMediator"))

var_0_0.ON_SHOPPING = "NewBackYardShopMediator.ON_SHOPPING"
var_0_0.ON_CHARGE = "NewBackYardShopMediator.ON_CHARGE"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_SHOPPING, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.BUY_FURNITURE, {
			furnitureIds = arg_2_1,
			type = arg_2_2
		}))
	arg_1_0.bind(var_0_0.ON_CHARGE, function(arg_3_0, arg_3_1)
		if arg_1_0.contextData.onDeattch:
			arg_1_0.contextData.onDeattch = None

		local var_3_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(CourtYardMediator)

		if var_3_0:
			var_3_0.data.skipToCharge = True

		if arg_3_1 == PlayerConst.ResDiamond:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.CHARGE, {
				wrap = ChargeScene.TYPE_DIAMOND
			})
		elif arg_3_1 == PlayerConst.ResDormMoney:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.EVENT))
	arg_1_0.viewComponent.SetDorm(getProxy(DormProxy).getRawData())
	arg_1_0.viewComponent.SetPlayer(getProxy(PlayerProxy).getRawData())

def var_0_0.remove(arg_4_0):
	if arg_4_0.contextData.onRemove:
		arg_4_0.contextData.onRemove()

def var_0_0.listNotificationInterests(arg_5_0):
	return {
		PlayerProxy.UPDATED,
		GAME.BUY_FURNITURE_DONE,
		DormProxy.DORM_UPDATEED
	}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()
	local var_6_2 = arg_6_1.getType()

	if var_6_0 == PlayerProxy.UPDATED:
		arg_6_0.viewComponent.PlayerUpdated(var_6_1)
	elif var_6_0 == GAME.BUY_FURNITURE_DONE:
		arg_6_0.viewComponent.FurnituresUpdated(var_6_2)
	elif var_6_0 == DormProxy.DORM_UPDATEED:
		arg_6_0.viewComponent.DormUpdated(getProxy(DormProxy).getRawData())

return var_0_0
