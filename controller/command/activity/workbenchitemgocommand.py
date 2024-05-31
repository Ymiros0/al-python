local var_0_0 = class("WorkBenchItemGoCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.body
	local var_1_1 = WorkBenchItem.New({
		configId = var_1_0
	}).GetSource()

	if var_1_1.islandNodes:
		if getProxy(ContextProxy).getCurrentContext().getContextByMediator(SixthAnniversaryIslandMediator):
			arg_1_0.sendNotification(SixthAnniversaryIslandMediator.DISPLAY_NODES, var_1_1.islandNodes)
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SEA, {
				nodeIds = var_1_1.islandNodes
			})
	elif var_1_1.islandShop:
		local var_1_2 = getProxy(ContextProxy).getCurrentContext()

		if var_1_2.getContextByMediator(SixthAnniversaryIslandShopMediator):
			return

		if var_1_2.getContextByMediator(SixthAnniversaryIslandMediator):
			arg_1_0.sendNotification(SixthAnniversaryIslandMediator.DISPLAY_SHOP)
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SEA, {
				wraps = SixthAnniversaryIslandScene.SHOP
			})
	elif var_1_1.recipeid:
		local var_1_3 = var_1_1.recipeid
		local var_1_4 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORKBENCH)

		if not var_1_4 or var_1_4.isEnd():
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

			return

		local var_1_5 = WorkBenchFormula.New({
			configId = var_1_3
		})

		var_1_5.BuildFromActivity()

		if not var_1_5.IsAvaliable():
			pg.TipsMgr.GetInstance().ShowTips(i18n("workbench_tips1"))

			return

		if not var_1_5.IsUnlock():
			local var_1_6 = var_1_5.GetLockLimit()

			pg.TipsMgr.GetInstance().ShowTips(i18n("workbench_tips4", var_1_6 and var_1_6[3]))

			return

		if getProxy(ContextProxy).getCurrentContext().getContextByMediator(AnniversaryIslandComposite2023Mediator):
			arg_1_0.sendNotification(AnniversaryIslandComposite2023Mediator.OPEN_FORMULA, var_1_3)
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_WORKBENCH, {
				formulaId = var_1_3
			})
	elif var_1_1.taskid:
		local var_1_7 = getProxy(ActivityProxy).getActivityById(ActivityConst.ISLAND_TASK_ID)

		if not var_1_7 or var_1_7.isEnd():
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

			return

		local var_1_8 = getProxy(ContextProxy).getCurrentContext()

		if var_1_8.getContextByMediator(IslandTaskMediator):
			return

		arg_1_0.sendNotification(GAME.LOAD_LAYERS, {
			parentContext = var_1_8,
			context = Context.New({
				mediator = IslandTaskMediator,
				viewComponent = IslandTaskScene,
				data = {
					task_ids = var_1_1.taskid
				}
			})
		})
	elif var_1_1.minigame:
		pg.m02.sendNotification(GAME.GO_MINI_GAME, var_1_1.minigame)

return var_0_0
