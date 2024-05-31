local var_0_0 = class("NewProbabilitySkinShopMediator", import(".NewSkinShopMediator"))

var_0_0.OPEN_CHARGE_BIRTHDAY = "NewProbabilitySkinShopMediator.OPEN_CHARGE_BIRTHDAY"
var_0_0.CHARGE = "NewProbabilitySkinShopMediator.CHARGE"
var_0_0.OPEN_CHARGE_ITEM_PANEL = "NewProbabilitySkinShopMediator.OPEN_CHARGE_ITEM_PANEL"

def var_0_0.register(arg_1_0):
	var_0_0.super.register(arg_1_0)
	arg_1_0.bind(var_0_0.OPEN_CHARGE_BIRTHDAY, function(arg_2_0, arg_2_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChargeBirthdayMediator,
			viewComponent = ChargeBirthdayLayer,
			data = {}
		})))
	arg_1_0.bind(var_0_0.CHARGE, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.CHARGE_OPERATION, {
			shopId = arg_3_1
		}))
	arg_1_0.bind(var_0_0.OPEN_CHARGE_ITEM_PANEL, function(arg_4_0, arg_4_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChargeItemPanelMediator,
			viewComponent = ChargeItemPanelLayer,
			data = {
				panelConfig = arg_4_1
			}
		})))

def var_0_0.listNotificationInterests(arg_5_0):
	local var_5_0 = var_0_0.super.listNotificationInterests(arg_5_0)

	table.insert(var_5_0, GAME.CHARGE_SUCCESS)

	return var_5_0

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	var_0_0.super.handleNotification(arg_6_0, arg_6_1)

	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == GAME.CHARGE_SUCCESS:
		arg_6_0.viewComponent.OnChargeSuccess(var_6_1.shopId)

return var_0_0
