local var_0_0 = class("BuildShipDetailMediator", import("...base.ContextMediator"))

var_0_0.ON_QUICK = "BuildShipDetailMediator.ON_QUICK"
var_0_0.LAUNCH_ALL = "BuildShipDetailMediator.LAUNCH_ALL"
var_0_0.ON_LAUNCHED = "BuildShipDetailMediator.ON_LAUNCHED"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(PlayerProxy)

	arg_1_0.viewComponent.updatePlayer(var_1_0.getData())

	arg_1_0.bagProxy = getProxy(BagProxy)

	arg_1_0.viewComponent.setItems(arg_1_0.bagProxy.getData())

	local var_1_1 = getProxy(BuildShipProxy)

	arg_1_0.viewComponent.setProjectList(var_1_1.getData())
	arg_1_0.viewComponent.setWorkCount(var_1_1.getMaxWorkCount())

	local var_1_2 = getProxy(SettingsProxy)

	arg_1_0.bind(var_0_0.ON_QUICK, function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_2:
			var_1_2.setStopBuildSpeedupRemind()
			arg_1_0.viewComponent.setBuildSpeedUpRemind(True)

		arg_1_0.isBatch = False

		arg_1_0.GetShipProcess({
			arg_2_1
		}))
	arg_1_0.bind(var_0_0.ON_LAUNCHED, function(arg_3_0, arg_3_1)
		arg_1_0.isBatch = False

		arg_1_0.GetShipProcess({
			arg_3_1
		}))
	arg_1_0.bind(var_0_0.LAUNCH_ALL, function(arg_4_0, arg_4_1)
		if arg_4_1:
			var_1_2.setStopBuildSpeedupRemind()
			arg_1_0.viewComponent.setBuildSpeedUpRemind(True)

		arg_1_0.isBatch = True

		local var_4_0 = {}

		for iter_4_0, iter_4_1 in ipairs(var_1_1.getData()):
			table.insert(var_4_0, iter_4_0)

		arg_1_0.GetShipProcess(var_4_0))

	local var_1_3 = var_1_2.getStopBuildSpeedupRemind()

	arg_1_0.viewComponent.setBuildSpeedUpRemind(var_1_3)

def var_0_0.GetShipProcess(arg_5_0, arg_5_1):
	local var_5_0 = getProxy(BuildShipProxy)
	local var_5_1 = {}

	table.insert(var_5_1, function(arg_6_0)
		arg_5_0.sendNotification(GAME.BUILD_SHIP_IMMEDIATELY, {
			pos_list = arg_5_1,
			callback = arg_6_0
		}))
	seriesAsync(var_5_1, function()
		if arg_5_0.isBatch and underscore.any(arg_5_1, function(arg_8_0)
			return var_5_0.getBuildShip(arg_8_0).state != BuildShip.FINISH):
			pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_backyardShipInfoLayer_error_noQuickItem"))

		arg_5_0.sendNotification(GAME.GET_SHIP, {
			pos_list = arg_5_1
		}))

def var_0_0.listNotificationInterests(arg_9_0):
	return {
		BagProxy.ITEM_UPDATED,
		GAME.GET_SHIP_DONE,
		BuildShipProxy.REMOVED,
		BuildShipProxy.UPDATED,
		PlayerProxy.UPDATED
	}

def var_0_0.handleNotification(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1.getName()
	local var_10_1 = arg_10_1.getBody()

	if var_10_0 == BagProxy.ITEM_UPDATED:
		arg_10_0.viewComponent.setItems(arg_10_0.bagProxy.getData())
		arg_10_0.viewComponent.updateItem()
	elif var_10_0 == GAME.GET_SHIP_DONE:
		local var_10_2 = getProxy(BuildShipProxy)

		arg_10_0.viewComponent.setProjectList(var_10_2.getData())
		arg_10_0.viewComponent.initProjectList()

		local var_10_3 = {}

		table.insert(var_10_3, function(arg_11_0)
			arg_10_0.viewComponent.playGetShipAnimate(arg_11_0, var_10_1.type))

		for iter_10_0, iter_10_1 in ipairs(var_10_1.ships):
			table.insert(var_10_3, function(arg_12_0)
				local var_12_0 = var_10_2.getSkipBatchBuildFlag()

				if var_12_0 and not iter_10_1.virgin and iter_10_1.getRarity() < 4:
					arg_12_0()
				else
					arg_10_0.addSubLayers(Context.New({
						mediator = NewShipMediator,
						viewComponent = NewShipLayer,
						data = {
							ship = iter_10_1,
							canSkipBatch = not var_12_0 and iter_10_0 < #var_10_1.ships
						},
						onRemoved = arg_12_0
					})))

		seriesAsync(var_10_3, function()
			arg_10_0.sendNotification(GAME.CONFIRM_GET_SHIP, {
				isBatch = arg_10_0.isBatch,
				ships = var_10_1.ships
			}))
	elif var_10_0 == BuildShipProxy.UPDATED:
		arg_10_0.viewComponent.updateProject(var_10_1.index, var_10_1.buildShip)
	elif var_10_0 == PlayerProxy.UPDATED:
		arg_10_0.viewComponent.updatePlayer(var_10_1)

return var_0_0
