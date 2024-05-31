local var_0_0 = class("ShipUpgradeMediator2", import("..base.ContextMediator"))

var_0_0.UPGRADE_SHIP = "ShipUpgradeMediator2.UPGRADE_SHIP"
var_0_0.ON_SELECT_SHIP = "ShipUpgradeMediator2.ON_SELECT_SHIP"
var_0_0.NEXTSHIP = "ShipUpgradeMediator2.NEXTSHIP"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayer(var_1_0)

	local var_1_1 = getProxy(BagProxy)

	arg_1_0.viewComponent.setItems(var_1_1.getData())

	local var_1_2 = getProxy(BayProxy)
	local var_1_3 = var_1_2.getShipById(arg_1_0.contextData.shipId)

	arg_1_0.viewComponent.setShip(var_1_3)
	arg_1_0.bind(var_0_0.UPGRADE_SHIP, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.UPGRADE_STAR, {
			shipId = arg_1_0.contextData.shipId,
			shipIds = arg_2_1
		}))
	arg_1_0.bind(var_0_0.ON_SELECT_SHIP, function(arg_3_0, arg_3_1, arg_3_2)
		local var_3_0 = var_1_2.getUpgradeShips(arg_3_1)
		local var_3_1 = pg.ShipFlagMgr.GetInstance().FilterShips(ShipStatus.FILTER_SHIPS_FLAGS_3, underscore.map(var_3_0, function(arg_4_0)
			return arg_4_0.id))

		table.insert(var_3_1, arg_3_1.id)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			destroyCheck = True,
			leftTopInfo = i18n("word_upgrade"),
			mode = DockyardScene.MODE_UPGRADE,
			selectedMax = arg_3_2 or 1,
			selectedMin = arg_3_2 or 1,
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
			hideTagFlags = ShipStatus.TAG_HIDE_DESTROY
		}))
	arg_1_0.bind(var_0_0.NEXTSHIP, function(arg_8_0, arg_8_1)
		arg_1_0.sendNotification(var_0_0.NEXTSHIP, arg_8_1))

def var_0_0.listNotificationInterests(arg_9_0):
	return {
		GAME.UPGRADE_STAR_DONE,
		BagProxy.ITEM_UPDATED,
		BayProxy.SHIP_REMOVED,
		PlayerProxy.UPDATED
	}

def var_0_0.handleNotification(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1.getName()
	local var_10_1 = arg_10_1.getBody()

	if var_10_0 == PlayerProxy.UPDATED:
		arg_10_0.viewComponent.setPlayer(var_10_1)
	elif var_10_0 == GAME.UPGRADE_STAR_DONE:
		arg_10_0.contextData.materialShipIds = None

		arg_10_0.viewComponent.setShip(var_10_1.newShip)
		arg_10_0.viewComponent.updateStagesScrollView()
		arg_10_0.addSubLayers(Context.New({
			viewComponent = ShipBreakResultLayer,
			mediator = ShipBreakResultMediator,
			data = {
				newShip = var_10_1.newShip,
				oldShip = var_10_1.oldShip
			}
		}))
	elif var_10_0 == BagProxy.ITEM_UPDATED:
		local var_10_2 = getProxy(BagProxy)

		arg_10_0.viewComponent.setItems(var_10_2.getRawData())

return var_0_0
