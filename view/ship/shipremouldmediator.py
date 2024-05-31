local var_0_0 = class("ShipRemouldMediator", import("..base.ContextMediator"))

var_0_0.REMOULD_SHIP = "ShipRemouldMediator.REMOULD_SHIP"
var_0_0.ON_SELECTE_SHIP = "ShipRemouldMediator.ON_SELECTE_SHIP"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(BayProxy)
	local var_1_1 = var_1_0.getShipById(arg_1_0.contextData.shipId)

	arg_1_0.viewComponent.setShipVO(var_1_1)

	local var_1_2 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayer(var_1_2)

	arg_1_0.bagProxy = getProxy(BagProxy)

	arg_1_0.viewComponent.setItems(arg_1_0.bagProxy.getData())
	arg_1_0.bind(var_0_0.REMOULD_SHIP, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
		if arg_1_0.contextData.materialShipIds and #arg_1_0.contextData.materialShipIds > 1:
			pg.TipsMgr.GetInstance().ShowTips(i18n("remould_ship_count_more"))

			return

		arg_1_0.sendNotification(GAME.REMOULD_SHIP, {
			shipId = arg_2_1,
			remouldId = arg_2_2,
			materialIds = arg_1_0.contextData.materialShipIds or {}
		}))
	arg_1_0.bind(var_0_0.ON_SELECTE_SHIP, function(arg_3_0, arg_3_1)
		local var_3_0 = var_1_0.getUpgradeShips(arg_3_1)
		local var_3_1 = pg.ShipFlagMgr.GetInstance().FilterShips(ShipStatus.FILTER_SHIPS_FLAGS_3, underscore.map(var_3_0, function(arg_4_0)
			return arg_4_0.id))

		table.insert(var_3_1, arg_3_1.id)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMax = 1,
			selectedMin = 1,
			destroyCheck = True,
			shipVOs = var_3_0,
			ignoredIds = var_3_1,
			selectedIds = arg_1_0.contextData.materialShipIds or {},
			def onShip:(arg_5_0, arg_5_1)
				if arg_5_0.getFlag("inAdmiral"):
					return False, i18n("confirm_unlock_ship_main")
				elif arg_5_0.GetLockState() == Ship.LOCK_STATE_LOCK:
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						yseBtnLetf = True,
						content = i18n("confirm_unlock_lv", "Lv." .. arg_5_0.level, arg_5_0.getName()),
						def onYes:()
							pg.m02.sendNotification(GAME.UPDATE_LOCK, {
								ship_id_list = {
									arg_5_0.id
								},
								is_locked = Ship.LOCK_STATE_UNLOCK
							}),
						yesText = i18n("msgbox_text_unlock")
					})

					return False, None
				else
					return ShipStatus.canDestroyShip(arg_5_0, arg_5_1),
			def onSelected:(arg_7_0)
				arg_1_0.contextData.materialShipIds = arg_7_0,
			mode = DockyardScene.MODE_REMOULD,
			hideTagFlags = ShipStatus.TAG_HIDE_DESTROY
		}))

def var_0_0.listNotificationInterests(arg_8_0):
	return {
		GAME.REMOULD_SHIP_DONE,
		PlayerProxy.UPDATED,
		BagProxy.ITEM_UPDATED
	}

def var_0_0.handleNotification(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.getName()
	local var_9_1 = arg_9_1.getBody()

	if var_9_0 == GAME.REMOULD_SHIP_DONE:
		arg_9_0.viewComponent.setShipVO(var_9_1.ship)
		arg_9_0.viewComponent.updateLines()

		if #var_9_1.awards != 0:
			arg_9_0.addSubLayers(Context.New({
				mediator = NewShipMediator,
				viewComponent = NewShipLayer,
				data = {
					fromRemould = True,
					ship = var_9_1.ship
				}
			}))
			arg_9_0.viewComponent.initShipModel()

		arg_9_0.contextData.materialShipIds = None

		pg.TipsMgr.GetInstance().ShowTips(i18n("remould_ship_ok"))
	elif var_9_0 == PlayerProxy.UPDATED:
		arg_9_0.viewComponent.setPlayer(var_9_1)
	elif var_9_0 == BagProxy.ITEM_UPDATED:
		arg_9_0.viewComponent.setItems(arg_9_0.bagProxy.getData())

return var_0_0
