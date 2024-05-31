local var_0_0 = class("AtelierCompositeMediator", import("view.base.ContextMediator"))

var_0_0.OPEN_FORMULA = "OPEN_FORMULA"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(GAME.COMPOSITE_ATELIER_RECIPE, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.COMPOSITE_ATELIER_RECIPE, {
			formulaId = arg_1_0.contextData.formulaId,
			items = arg_2_1,
			repeats = arg_2_2
		}))
	arg_1_0.bind(AtelierMaterialDetailMediator.SHOW_DETAIL, function(arg_3_0, arg_3_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = AtelierMaterialDetailMediator,
			viewComponent = AtelierMaterialDetailLayer,
			data = {
				material = arg_3_1
			}
		})))

	local var_1_0 = getProxy(ChapterProxy).getChapterById(1690005, True).isClear()

	arg_1_0.viewComponent.SetEnabled(var_1_0)

	local var_1_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

	assert(var_1_1 and not var_1_1.isEnd())
	arg_1_0.viewComponent.SetActivity(var_1_1)

def var_0_0.listNotificationInterests(arg_4_0):
	return {
		GAME.COMPOSITE_ATELIER_RECIPE_DONE,
		ActivityProxy.ACTIVITY_UPDATED,
		var_0_0.OPEN_FORMULA
	}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

	if var_5_0 == GAME.COMPOSITE_ATELIER_RECIPE_DONE:
		arg_5_0.viewComponent.OnCompositeResult(var_5_1)
	elif var_5_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_5_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_ATELIER_LINK:
			arg_5_0.viewComponent.SetActivity(var_5_1)
	elif var_5_0 == var_0_0.OPEN_FORMULA:
		arg_5_0.viewComponent.OnReceiveFormualRequest(var_5_1)

def var_0_0.remove(arg_6_0):
	return

return var_0_0
