local var_0_0 = class("NewYearHotSpringMediator", import("view.base.ContextMediator"))

var_0_0.UNLOCK_SLOT = "UNLOCK_SLOT"
var_0_0.OPEN_INFO = "OPEN_INFO"
var_0_0.OPEN_CHUANWU = "NewYearHotSpringMediator.Open chuanwu"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.UNLOCK_SLOT, function(arg_2_0, arg_2_1)
		local var_2_0, var_2_1 = arg_1_0.activity.GetUpgradeCost()

		MsgboxMediator.ShowMsgBox({
			type = MSGBOX_TYPE_NORMAL,
			content = i18n("hotspring_expand", var_2_1),
			contextSprites = {
				{
					name = "wenquanbi",
					path = "props/wenquanbi"
				}
			},
			def onYes:()
				if arg_1_0.activity.GetCoins() < var_2_1:
					pg.TipsMgr.GetInstance().ShowTips(i18n("hotspring_tip2"))

					return

				arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, {
					activity_id = arg_2_1,
					cmd = SpringActivity.OPERATION_UNLOCK
				})
		}))
	arg_1_0.bind(var_0_0.OPEN_CHUANWU, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0.OnSelShips(arg_4_1, arg_4_2))

	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

	arg_1_0.activity = var_1_0

	arg_1_0.viewComponent.SetActivity(var_1_0)
	arg_1_0.bind(var_0_0.OPEN_INFO, function()
		arg_1_0.addSubLayers(Context.New({
			mediator = NewYearHotSpringShipSelectMediator,
			viewComponent = NewYearHotSpringShipSelectLayer,
			data = {
				actId = var_1_0.id
			}
		})))

def var_0_0.OnSelShips(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_0.GetSelectedShipIds(arg_6_2)
	local var_6_1 = {
		callbackQuit = True,
		selectedMax = arg_6_0.activity.GetSlotCount(),
		quitTeam = arg_6_2 != None,
		ignoredIds = pg.ShipFlagMgr.GetInstance().FilterShips({
			isActivityNpc = True
		}),
		selectedIds = Clone(var_6_0),
		preView = arg_6_0.viewComponent.__cname,
		hideTagFlags = ShipStatus.TAG_HIDE_BACKYARD,
		blockTagFlags = ShipStatus.TAG_BLOCK_BACKYARD,
		def onShip:(arg_7_0, arg_7_1, arg_7_2)
			return arg_6_0.OnShip(arg_7_0, arg_7_1, arg_7_2),
		def onSelected:(arg_8_0, arg_8_1)
			arg_6_0.OnSelected(arg_6_1, arg_8_0, arg_8_1),
		priorEquipUpShipIDList = _.filter(arg_6_0.activity.GetShipIds(), function(arg_9_0)
			return arg_9_0 > 0),
		leftTopWithFrameInfo = i18n("backyard_longpress_ship_tip")
	}

	var_6_1.isLayer = True
	var_6_1.energyDisplay = True

	arg_6_0.addSubLayers(Context.New({
		viewComponent = DockyardScene,
		mediator = DockyardMediator,
		data = var_6_1
	}))

def var_0_0.GetSelectedShipIds(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1 and arg_10_1.id or -1
	local var_10_1 = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.activity.GetShipIds()):
		local var_10_2 = iter_10_1 > 0 and getProxy(BayProxy).RawGetShipById(iter_10_1)

		if var_10_2 and var_10_2.id != var_10_0:
			table.insert(var_10_1, var_10_2.id)

	return var_10_1

def var_0_0.OnShip(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	local var_11_0, var_11_1 = ShipStatus.ShipStatusCheck("inBackyard", arg_11_1, function(arg_12_0)
		arg_11_2())

	return var_11_0, var_11_1

def var_0_0.OnSelected(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	local var_13_0 = Clone(arg_13_0.activity.GetShipIds())

	_.each(_.range(arg_13_0.activity.GetSlotCount()), function(arg_14_0)
		var_13_0[arg_14_0] = var_13_0[arg_14_0] or 0)

	if arg_13_2 == None or #arg_13_2 == 0:
		if var_13_0[arg_13_1] > 0:
			arg_13_0.sendNotification(GAME.ACTIVITY_OPERATION, {
				activity_id = arg_13_0.activity.id,
				cmd = SpringActivity.OPERATION_SETSHIP,
				kvargs1 = {
					{
						value = 0,
						key = arg_13_1
					}
				}
			})

		existCall(arg_13_3)

		return

	local var_13_1 = _.filter(arg_13_2, function(arg_15_0)
		return not table.contains(var_13_0, arg_15_0))

	table.Foreach(var_13_0, function(arg_16_0, arg_16_1)
		if arg_16_1 == 0 or table.contains(arg_13_2, arg_16_1):
			return

		var_13_0[arg_16_0] = 0)

	if #var_13_1 == 1 and var_13_0[arg_13_1] == 0:
		var_13_0[arg_13_1] = var_13_1[1]
	else
		local var_13_2 = 0

		_.each(var_13_1, function(arg_17_0)
			while var_13_2 <= #var_13_0:
				var_13_2 = var_13_2 + 1

				if var_13_0[var_13_2] == 0:
					break

			var_13_0[var_13_2] = arg_17_0)

	local var_13_3 = {}
	local var_13_4 = arg_13_0.activity.GetShipIds()

	table.Foreach(var_13_0, function(arg_18_0, arg_18_1)
		if (var_13_4[arg_18_0] or 0) != arg_18_1:
			table.insert(var_13_3, {
				key = arg_18_0,
				value = arg_18_1
			}))

	if #var_13_3 > 0:
		arg_13_0.sendNotification(GAME.ACTIVITY_OPERATION, {
			activity_id = arg_13_0.activity.id,
			cmd = SpringActivity.OPERATION_SETSHIP,
			kvargs1 = var_13_3
		})

	arg_13_3()

def var_0_0.listNotificationInterests(arg_19_0):
	return {
		PlayerProxy.UPDATED,
		ActivityProxy.ACTIVITY_UPDATED,
		ActivityProxy.ACTIVITY_SHOW_AWARDS,
		var_0_0.OPEN_CHUANWU,
		var_0_0.UNLOCK_SLOT
	}

def var_0_0.handleNotification(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_1.getName()
	local var_20_1 = arg_20_1.getBody()

	if var_20_0 == None:
		-- block empty
	elif var_20_0 == ActivityProxy.ACTIVITY_SHOW_AWARDS:
		arg_20_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_20_1.awards, var_20_1.callback)
	elif var_20_0 == ActivityProxy.ACTIVITY_UPDATED:
		if var_20_1.getConfig("type") == ActivityConst.ACTIVITY_TYPE_HOTSPRING:
			arg_20_0.activity = var_20_1

			arg_20_0.viewComponent.SetActivity(var_20_1)
			arg_20_0.viewComponent.UpdateView()
	elif var_20_0 == var_0_0.OPEN_CHUANWU:
		arg_20_0.viewComponent.emit(var_0_0.OPEN_CHUANWU, unpack(var_20_1))
	elif var_20_0 == var_0_0.UNLOCK_SLOT:
		arg_20_0.viewComponent.emit(var_0_0.UNLOCK_SLOT, var_20_1)

def var_0_0.remove(arg_21_0):
	return

return var_0_0
