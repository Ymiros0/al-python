local var_0_0 = class("IslandFlowerFieldMediator", import("..base.ContextMediator"))

var_0_0.GET_FLOWER_AWARD = "IslandFlowerFieldMediator.GET_FLOWER_AWARD"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_FLOWER_FIELD)

	arg_1_0.viewComponent.setActivity(var_1_0)
	arg_1_0.bind(var_0_0.GET_FLOWER_AWARD, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.ISLAND_FLOWER_GET, {
			act_id = var_1_0.id,
			isAuto = arg_2_1
		}))

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		GAME.ISLAND_FLOWER_GET_DONE,
		ActivityProxy.ACTIVITY_UPDATED
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == GAME.ISLAND_FLOWER_GET_DONE:
		if #var_4_1.awards > 0:
			if var_4_1.isAuto:
				arg_4_0.addSubLayers(Context.New({
					mediator = SixthAnniversaryIslandFlowerWindowMediator,
					viewComponent = SixthAnniversaryIslandFlowerWindowLayer,
					data = {
						awards = var_4_1.awards,
						name = pg.ship_data_statistics[arg_4_0.contextData.shipConfigId].name
					}
				}))
			else
				arg_4_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_4_1.awards)
	elif var_4_0 == ActivityProxy.ACTIVITY_UPDATED and var_4_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_FLOWER_FIELD:
		arg_4_0.viewComponent.setActivity(var_4_1)
		arg_4_0.viewComponent.refreshDisplay()

return var_0_0
