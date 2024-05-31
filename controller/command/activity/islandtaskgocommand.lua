local var_0_0 = class("IslandTaskGoCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1.body.taskVO:getConfig("scene")

	if var_1_0 and #var_1_0 > 0 then
		if var_1_0[1] == "ANNIVERSARY_ISLAND_SEA" then
			local var_1_1 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(SixthAnniversaryIslandMediator)
			local var_1_2 = var_1_0[2].nodeIds

			if var_1_1 then
				arg_1_0:sendNotification(SixthAnniversaryIslandMediator.DISPLAY_NODES, var_1_2)
			else
				arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_SEA, {
					nodeIds = var_1_2
				})
			end
		elseif var_1_0[1] == "ANNIVERSARY_ISLAND_WORKBENCH" then
			local var_1_3 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_WORKBENCH)

			if not var_1_3 or var_1_3:isEnd() then
				pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_end"))

				return
			end

			local var_1_4 = AcessWithinNull(var_1_0[2], "formulaId")

			if var_1_4 and var_1_4 > 0 then
				local var_1_5 = WorkBenchFormula.New({
					configId = var_1_4
				})

				var_1_5:BuildFromActivity()

				if not var_1_5:IsAvaliable() then
					pg.TipsMgr.GetInstance():ShowTips(i18n("workbench_tips1"))

					return
				end

				if not var_1_5:IsUnlock() then
					local var_1_6 = var_1_5:GetLockLimit()

					pg.TipsMgr.GetInstance():ShowTips(i18n("workbench_tips4", var_1_6 and var_1_6[3]))

					return
				end
			end

			if getProxy(ContextProxy):getCurrentContext():getContextByMediator(AnniversaryIslandComposite2023Mediator) then
				arg_1_0:sendNotification(AnniversaryIslandComposite2023Mediator.OPEN_FORMULA, var_1_4)
			else
				arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.ANNIVERSARY_ISLAND_WORKBENCH, {
					formulaId = var_1_4
				})
			end
		elseif var_1_0[1] == "ISLAND_BUILDING" then
			local var_1_7 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(AnniversaryIsland2023Mediator)
			local var_1_8 = var_1_0[2].build
			local var_1_9 = Context.New({
				mediator = AnniversaryIslandBuildingUpgrade2023WindowMediator,
				viewComponent = AnniversaryIslandBuildingUpgrade2023Window,
				data = {
					isLayer = true,
					buildingID = var_1_8
				}
			})

			if var_1_7 then
				arg_1_0:sendNotification(GAME.LOAD_LAYERS, {
					parentContext = var_1_7,
					context = var_1_9
				})
			else
				local var_1_10 = Context.New()

				SCENE.SetSceneInfo(var_1_10, SCENE.ANNIVERSARY_ISLAND_BACKHILL_2023)
				var_1_10:addChild(var_1_9)
				print("load scene: " .. SCENE.ANNIVERSARY_ISLAND_BACKHILL_2023)
				arg_1_0:sendNotification(GAME.LOAD_SCENE, {
					context = var_1_10
				})
			end
		else
			local var_1_11 = Context.New()

			SCENE.SetSceneInfo(var_1_11, SCENE[var_1_0[1]])

			local var_1_12 = var_1_11.mediator

			if getProxy(ContextProxy):getCurrentContext():getContextByMediator(var_1_12) then
				warning("Enter Current Context")

				return
			end

			arg_1_0:sendNotification(GAME.GO_SCENE, SCENE[var_1_0[1]], var_1_0[2])
		end
	end
end

return var_0_0
