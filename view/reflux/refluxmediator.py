local var_0_0 = class("RefluxMediator", import("..base.ContextMediator"))

var_0_0.OnTaskSubmit = "RefluxMediator.OnTaskSubmit"
var_0_0.OnTaskGo = "RefluxMediator.OnTaskGo"
var_0_0.OPEN_CHARGE_ITEM_PANEL = "RefluxMediator.OPEN_CHARGE_ITEM_PANEL"
var_0_0.OPEN_CHARGE_ITEM_BOX = "RefluxMediator.OPEN_CHARGE_ITEM_BOX"
var_0_0.OPEN_CHARGE_BIRTHDAY = "RefluxMediator.OPEN_CHARGE_BIRTHDAY"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.OnTaskSubmit, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_2_1))
	arg_1_0.bind(var_0_0.OnTaskGo, function(arg_3_0, arg_3_1)
		arg_1_0.sendNotification(GAME.TASK_GO, {
			taskVO = arg_3_1
		}))
	arg_1_0.bind(var_0_0.OPEN_CHARGE_ITEM_PANEL, function(arg_4_0, arg_4_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChargeItemPanelMediator,
			viewComponent = ChargeItemPanelLayer,
			data = {
				panelConfig = arg_4_1
			}
		})))
	arg_1_0.bind(var_0_0.OPEN_CHARGE_ITEM_BOX, function(arg_5_0, arg_5_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChargeItemBoxMediator,
			viewComponent = ChargeItemBoxLayer,
			data = {
				panelConfig = arg_5_1
			}
		})))
	arg_1_0.bind(var_0_0.OPEN_CHARGE_BIRTHDAY, function(arg_6_0, arg_6_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = ChargeBirthdayMediator,
			viewComponent = ChargeBirthdayLayer,
			data = {}
		})))

def var_0_0.listNotificationInterests(arg_7_0):
	return {
		GAME.REFLUX_SIGN_DONE,
		GAME.SUBMIT_TASK_DONE,
		GAME.REFLUX_GET_PT_AWARD_DONE,
		TaskProxy.TASK_UPDATED,
		TaskProxy.TASK_REMOVED,
		GAME.SHOPPING_DONE,
		GAME.CHARGE_CONFIRM_FAILED,
		GAME.CHARGED_LIST_UPDATED,
		GAME.ZERO_HOUR_OP_DONE
	}

def var_0_0.handleNotification(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.getName()
	local var_8_1 = arg_8_1.getBody()

	if var_8_0 == GAME.REFLUX_SIGN_DONE:
		if arg_8_0.isCanUpdateView(arg_8_0.viewComponent.signView):
			arg_8_0.viewComponent.signView.updateUI()
			arg_8_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_1.awards)

		arg_8_0.viewComponent.updateRedPotList()
	elif var_8_0 == GAME.SUBMIT_TASK_DONE:
		if arg_8_0.isCanUpdateView(arg_8_0.viewComponent.taskView) and #var_8_1 > 0:
			local var_8_2 = arg_8_0.viewComponent.taskView.calcLastSubmitTaskPT()

			table.insert(var_8_1, var_8_2)
			arg_8_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_1)

		if arg_8_0.isCanUpdateView(arg_8_0.viewComponent.ptView):
			arg_8_0.viewComponent.ptView.updateUI()

		arg_8_0.viewComponent.updateRedPotList()
	elif var_8_0 == TaskProxy.TASK_UPDATED or var_8_0 == TaskProxy.TASK_REMOVED:
		if arg_8_0.isCanUpdateView(arg_8_0.viewComponent.taskView):
			arg_8_0.viewComponent.taskView.updateUI()

		arg_8_0.viewComponent.updateRedPotList()
	elif var_8_0 == GAME.REFLUX_GET_PT_AWARD_DONE:
		if arg_8_0.isCanUpdateView(arg_8_0.viewComponent.ptView):
			arg_8_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_1.awards)
			arg_8_0.viewComponent.ptView.updateAfterServer()

		arg_8_0.viewComponent.updateRedPotList()
	elif var_8_0 == GAME.SHOPPING_DONE:
		if arg_8_0.isCanUpdateView(arg_8_0.viewComponent.shopView):
			arg_8_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_8_1.awards)
			arg_8_0.viewComponent.shopView.updateUI()
	elif var_8_0 == GAME.CHARGE_CONFIRM_FAILED:
		-- block empty
	elif var_8_0 == GAME.CHARGED_LIST_UPDATED:
		if arg_8_0.isCanUpdateView(arg_8_0.viewComponent.shopView):
			arg_8_0.viewComponent.shopView.updateUI()
	elif var_8_0 == GAME.ZERO_HOUR_OP_DONE:
		arg_8_0.viewComponent.closeView()

def var_0_0.isCanUpdateView(arg_9_0, arg_9_1):
	if arg_9_1 and arg_9_1.GetLoaded():
		return True
	else
		return False

return var_0_0
