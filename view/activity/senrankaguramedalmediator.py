local var_0_0 = class("SenrankaguraMedalMediator", import("..base.ContextMediator"))

var_0_0.SUBMIT_TASK_ALL = "activity submit task all"
var_0_0.SUBMIT_TASK = "activity submit task "
var_0_0.TASK_GO = "task go "

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.SUBMIT_TASK, function(arg_2_0, arg_2_1)
		arg_1_0.displayAwards = {}

		arg_1_0.sendNotification(GAME.SUBMIT_TASK, arg_2_1, function(arg_3_0)
			if not arg_3_0:
				-- block empty))
	arg_1_0.bind(var_0_0.SUBMIT_TASK_ALL, function(arg_4_0, arg_4_1)
		local var_4_0 = getProxy(TaskProxy)
		local var_4_1 = False
		local var_4_2 = {}

		for iter_4_0 = 1, #arg_4_1:
			local var_4_3 = var_4_0.getTaskById(arg_4_1[iter_4_0])

			table.insert(var_4_2, var_4_3)

			if not var_4_3:
				return

			if not var_4_1 and var_4_3.IsOverflowShipExpItem():
				var_4_1 = True

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("player_expResource_mail_fullBag"),
					def onYes:()
						arg_1_0.displayAwards = {}

						arg_1_0.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
							resultList = var_4_2
						}),
					def onNo:()
						return
				})

		if not var_4_1:
			arg_1_0.displayAwards = {}

			arg_1_0.sendNotification(GAME.SUBMIT_TASK_ONESTEP, {
				resultList = var_4_2
			}))
	arg_1_0.bind(var_0_0.TASK_GO, function(arg_7_0, arg_7_1)
		arg_1_0.sendNotification(GAME.TASK_GO, {
			taskVO = arg_7_1
		}))

def var_0_0.listNotificationInterests(arg_8_0):
	return {
		GAME.SUBMIT_TASK_DONE,
		ActivityProxy.ACTIVITY_UPDATED,
		ActivityProxy.ACTIVITY_SHOW_AWARDS,
		GAME.MEMORYBOOK_UNLOCK_DONE,
		GAME.MEMORYBOOK_UNLOCK_AWARD_DONE
	}

def var_0_0.handleNotification(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.getName()
	local var_9_1 = arg_9_1.getBody()

	if var_9_0 == GAME.SUBMIT_TASK_DONE:
		if #var_9_1 > 0:
			for iter_9_0 = 1, #var_9_1:
				if var_9_1[iter_9_0].configId == arg_9_0.viewComponent.ptId:
					-- block empty
				else
					table.insert(arg_9_0.displayAwards, var_9_1[iter_9_0])

		arg_9_0.checkShowTaskAward()
	elif var_9_0 == GAME.ACTIVITY_UPDATED:
		-- block empty
	elif var_9_0 == GAME.MEMORYBOOK_UNLOCK_DONE:
		arg_9_0.viewComponent.updateUI()
	elif var_9_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS:
		arg_9_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_9_1.awards, var_9_1.callback)
		arg_9_0.viewComponent.updateUI()
	elif var_9_0 == GAME.MEMORYBOOK_UNLOCK_AWARD_DONE:
		-- block empty

def var_0_0.checkShowTaskAward(arg_10_0):
	if #arg_10_0.displayAwards > 0:
		arg_10_0.viewComponent.emit(BaseUI.ON_ACHIEVE, arg_10_0.displayAwards)

	arg_10_0.viewComponent.updateUI()

	arg_10_0.displayAwards = {}

return var_0_0
