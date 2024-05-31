local var_0_0 = class("MainTechnologySequence")

var_0_0.DontNotifyBluePrintTaskAgain = False

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(TechnologyProxy).getBuildingBluePrint()

	if not var_1_0:
		arg_1_1()

		return

	local var_1_1 = var_1_0.getTaskIds()
	local var_1_2 = False

	for iter_1_0, iter_1_1 in ipairs(var_1_1):
		if var_1_0.getTaskOpenTimeStamp(iter_1_1) <= pg.TimeMgr.GetInstance().GetServerTime():
			local var_1_3 = getProxy(TaskProxy).getTaskById(iter_1_1) or getProxy(TaskProxy).getFinishTaskById(iter_1_1)
			local var_1_4 = getProxy(TaskProxy).isFinishPrevTasks(iter_1_1)

			if not var_1_3 and var_1_4:
				var_1_2 = True

				arg_1_0.TriggerTask(iter_1_1)

	if var_1_2 and not var_0_0.DontNotifyBluePrintTaskAgain:
		local var_1_5 = var_1_0.getShipVO()

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("blueprint_task_update_tip", var_1_5.getConfig("name")),
			weight = LayerWeightConst.SECOND_LAYER,
			def onYes:()
				pg.m02.sendNotification(GAME.GO_SCENE, SCENE.SHIPBLUEPRINT)
				arg_1_1(),
			def onNo:()
				var_0_0.DontNotifyBluePrintTaskAgain = True

				arg_1_1()
		})
	else
		arg_1_1()

def var_0_0.TriggerTask(arg_4_0, arg_4_1):
	if not getProxy(TaskProxy).isFinishPrevTasks(arg_4_1):
		return

	pg.m02.sendNotification(GAME.TRIGGER_TASK, arg_4_1)

return var_0_0
