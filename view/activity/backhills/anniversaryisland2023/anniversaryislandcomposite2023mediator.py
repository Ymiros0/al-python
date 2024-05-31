local var_0_0 = class("AnniversaryIslandComposite2023Mediator", import("view.base.ContextMediator"))

var_0_0.OPEN_FORMULA = "OPEN_FORMULA"
var_0_0.OPEN_STOREHOUSE = "AnniversaryIslandComposite2023Mediator.OPEN_STOREHOUSE"
var_0_0.OPEN_UPGRADE_PANEL = "AnniversaryIslandComposite2023Mediator.OPEN_UPGRADE_PANEL"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(GAME.WORKBENCH_COMPOSITE, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0.sendNotification(GAME.WORKBENCH_COMPOSITE, {
			formulaId = arg_2_1,
			repeats = arg_2_2
		}))
	arg_1_0.bind(var_0_0.OPEN_STOREHOUSE, function(arg_3_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = AnniversaryIslandStoreHouse2023Mediator,
			viewComponent = AnniversaryIslandStoreHouse2023Window
		})))
	arg_1_0.bind(var_0_0.OPEN_UPGRADE_PANEL, function(arg_4_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = AnniversaryIslandBuildingUpgrade2023WindowMediator,
			viewComponent = AnniversaryIslandBuildingUpgrade2023Window,
			data = {
				buildingID = table.keyof(AnniversaryIsland2023Scene.Buildings, "craft")
			}
		}), True))
	arg_1_0.bind(WorkBenchItemDetailMediator.SHOW_DETAIL, function(arg_5_0, arg_5_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = WorkBenchItemDetailMediator,
			viewComponent = WorkBenchItemDetailLayer,
			data = {
				material = arg_5_1
			}
		})))
	getProxy(SettingsProxy).SetWorkbenchDailyTip()

def var_0_0.listNotificationInterests(arg_6_0):
	return {
		GAME.WORKBENCH_COMPOSITE_DONE,
		ActivityProxy.ACTIVITY_UPDATED,
		var_0_0.OPEN_FORMULA
	}

def var_0_0.handleNotification(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1.getName()
	local var_7_1 = arg_7_1.getBody()

	if var_7_0 == GAME.WORKBENCH_COMPOSITE_DONE:
		arg_7_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_7_1)
	elif var_7_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_7_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_WORKBENCH or var_7_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG or var_7_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2:
			arg_7_0.viewComponent.BuildActivityEnv()
			arg_7_0.viewComponent.UpdateView()
	elif var_7_0 == var_0_0.OPEN_FORMULA:
		if not var_7_1:
			return

		arg_7_0.viewComponent.OnReceiveFormualRequest(var_7_1)

def var_0_0.remove(arg_8_0):
	return

return var_0_0
