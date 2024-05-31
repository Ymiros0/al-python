local var_0_0 = class("IslandTaskGoCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.body.taskVO.getConfig("scene")

	if var_1_0 and #var_1_0 > 0:
		if var_1_0[1] == "ANNIVERSARY_ISLAND_SEA":
			local var_1_1 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(SixthAnniversaryIslandMediator)
			local var_1_2 = var_1_0[2].nodeIds

			if var_1_1:
				arg_1_0.sendNotification(SixthAnniversaryIslandMediator.DISPLAY_NODES, var_1_2)
			else
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SEA, {
					nodeIds = var_1_2
				})
		elif var_1_0[1] == "ANNIVERSARY_ISLAND_WORKBENCH":
			local var_1_3 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORKBENCH)

			if not var_1_3 or var_1_3.isEnd():
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

				return

			local var_1_4 = AcessWithinNull(var_1_0[2], "formulaId")

			if var_1_4 and var_1_4 > 0:
				local var_1_5 = WorkBenchFormula.New({
					configId = var_1_4
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
				arg_1_0.sendNotification(AnniversaryIslandComposite2023Mediator.OPEN_FORMULA, var_1_4)
			else
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_WORKBENCH, {
					formulaId = var_1_4
				})
		elif var_1_0[1] == "ISLAND_BUILDING":
			local var_1_7 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(AnniversaryIsland2023Mediator)
			local var_1_8 = var_1_0[2].build
			local var_1_9 = Context.New({
				mediator = AnniversaryIslandBuildingUpgrade2023WindowMediator,
				viewComponent = AnniversaryIslandBuildingUpgrade2023Window,
				data = {
					isLayer = True,
					buildingID = var_1_8
				}
			})

			if var_1_7:
				arg_1_0.sendNotification(GAME.LOAD_LAYERS, {
					parentContext = var_1_7,
					context = var_1_9
				})
			else
				local var_1_10 = Context.New()

				SCENE.SetSceneInfo(var_1_10, SCENE.ANNIVERSARY_ISLAND_BACKHILL_2023)
				var_1_10.addChild(var_1_9)
				print("load scene. " .. SCENE.ANNIVERSARY_ISLAND_BACKHILL_2023)
				arg_1_0.sendNotification(GAME.LOAD_SCENE, {
					context = var_1_10
				})
		else
			local var_1_11 = Context.New()

			SCENE.SetSceneInfo(var_1_11, SCENE[var_1_0[1]])

			local var_1_12 = var_1_11.mediator

			if getProxy(ContextProxy).getCurrentContext().getContextByMediator(var_1_12):
				warning("Enter Current Context")

				return

			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE[var_1_0[1]], var_1_0[2])

return var_0_0
