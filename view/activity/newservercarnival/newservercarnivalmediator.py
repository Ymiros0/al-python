local var_0_0 = class("NewServerCarnivalMediator", import("...base.ContextMediator"))

var_0_0.TASK_GO = "NewServerCarnivalMediator.TASK_GO"
var_0_0.TASK_SUBMIT = "NewServerCarnivalMediator.TASK_SUBMIT"
var_0_0.TASK_SUBMIT_ONESTEP = "NewServerCarnivalMediator.TASK_SUBMIT_ONESTEP"
var_0_0.GIFT_BUY_ITEM = "NewServerCarnivalMediator.GIFT_BUY_ITEM"
var_0_0.GIFT_OPEN_ITEM_PANEL = "NewServerCarnivalMediator.GIFT_OPEN_ITEM_PANEL"
var_0_0.UPDATE_SHOP_RED_DOT = "NewServerCarnivalMediator.UPDATE_SHOP_RED_DOT"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.TASK_GO, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.TASK_GO, {
			taskVO = arg_2_1
		}))
	arg_1_0.bind(var_0_0.TASK_SUBMIT, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_3_1.id))
	arg_1_0.bind(var_0_0.TASK_SUBMIT_ONESTEP, function(arg_4_0, arg_4_1)
		pg.m02.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
			resultList = arg_4_1
		}))
	arg_1_0.bind(var_0_0.GIFT_BUY_ITEM, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0.sendNotification(GAME.SHOPPING, {
			id = arg_5_1,
			count = arg_5_2
		}))
	arg_1_0.bind(var_0_0.GIFT_OPEN_ITEM_PANEL, function(arg_6_0, arg_6_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChargeItemPanelMediator,
			viewComponent = ChargeItemPanelLayer,
			data = {
				panelConfig = arg_6_1
			}
		})))
	arg_1_0.bind(var_0_0.UPDATE_SHOP_RED_DOT, function(arg_7_0)
		arg_1_0.viewComponent.updateShopDedDot())
	arg_1_0.viewComponent.setData()

def var_0_0.listNotificationInterests(arg_8_0):
	return {
		GAME.SUBMIT_TASK_DONE,
		PlayerProxy.UPDATED,
		GAME.SHOPPING_DONE,
		GAME.NEW_SERVER_SHOP_SHOPPING_DONE
	}

def var_0_0.handleNotification(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.getName()
	local var_9_1 = arg_9_1.getBody()

	if var_9_0 == GAME.SUBMIT_TASK_DONE:
		arg_9_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_9_1, function()
			arg_9_0.viewComponent.onUpdateTask())
	elif var_9_0 == PlayerProxy.UPDATED:
		arg_9_0.viewComponent.onUpdatePlayer(var_9_1)
	elif var_9_0 == GAME.SHOPPING_DONE:
		if #var_9_1.awards > 0:
			arg_9_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_9_1.awards)

		arg_9_0.viewComponent.onUpdateGift()
	elif var_9_0 == GAME.NEW_SERVER_SHOP_SHOPPING_DONE:
		if #var_9_1.awards > 0:
			arg_9_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_9_1.awards)

		if arg_9_0.viewComponent.newServerShopPage and arg_9_0.viewComponent.newServerShopPage.GetLoaded():
			arg_9_0.viewComponent.newServerShopPage.Refresh()

return var_0_0
