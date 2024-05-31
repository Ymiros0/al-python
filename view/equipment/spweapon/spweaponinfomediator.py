local var_0_0 = class("SpWeaponInfoMediator", import("view.base.ContextMediator"))

var_0_0.ON_DESTROY = "SpWeaponInfoMediator.ON_DESTROY"
var_0_0.ON_EQUIP = "SpWeaponInfoMediator.ON_EQUIP"
var_0_0.ON_INTENSIFY = "SpWeaponInfoMediator.ON_INTENSIFY"
var_0_0.ON_CHANGE = "SpWeaponInfoMediator.ON_CHANGE"
var_0_0.ON_UNEQUIP = "SpWeaponInfoMediator.ON_UNEQUIP"
var_0_0.ON_MOVE = "SpWeaponInfoMediator.ON_MOVE"
var_0_0.ON_MODIFY = "SpWeaponInfoMediator.ON_MODIFY"

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

	if getProxy(ContextProxy).getCurrentContext().scene == SCENE.SPWEAPON_STOREHOUSE:
		arg_1_0.viewComponent.fromEquipmentView = True

	local var_1_0 = getProxy(BayProxy).getShipById()
	local var_1_1, var_1_2 = unpack(arg_1_0.contextData.shipVO and {
		arg_1_0.contextData.shipVO.GetSpWeapon(),
		arg_1_0.contextData.shipVO
	} or {
		EquipmentProxy.StaticGetSpWeapon(arg_1_0.contextData.shipId, arg_1_0.contextData.spWeaponUid)
	})

	if arg_1_0.contextData.spWeaponConfigId:
		var_1_1 = SpWeapon.New({
			id = arg_1_0.contextData.spWeaponConfigId
		})

	local var_1_3, var_1_4 = EquipmentProxy.StaticGetSpWeapon(arg_1_0.contextData.oldShipId, arg_1_0.contextData.oldSpWeaponUid)

	arg_1_0.viewComponent.setShip(var_1_2, var_1_4)
	arg_1_0.viewComponent.setEquipment(var_1_1, var_1_3)

	local var_1_5 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayer(var_1_5)

def var_0_0.BindEvent(arg_2_0):
	arg_2_0.bind(var_0_0.ON_EQUIP, function(arg_3_0)
		if arg_2_0.contextData.oldShipId:
			arg_2_0.sendNotification(GAME.EQUIP_SPWEAPON_FROM_SHIP, {
				spWeaponUid = arg_2_0.contextData.oldSpWeaponUid,
				oldShipId = arg_2_0.contextData.oldShipId,
				shipId = arg_2_0.contextData.shipId
			})
		else
			arg_2_0.sendNotification(GAME.EQUIP_SPWEAPON_TO_SHIP, {
				spWeaponUid = arg_2_0.contextData.oldSpWeaponUid,
				shipId = arg_2_0.contextData.shipId
			}))
	arg_2_0.bind(var_0_0.ON_UNEQUIP, function(arg_4_0)
		arg_2_0.sendNotification(GAME.EQUIP_SPWEAPON_TO_SHIP, {
			shipId = arg_2_0.contextData.shipId
		})
		arg_2_0.viewComponent.emit(BaseUI.ON_CLOSE))
	arg_2_0.bind(var_0_0.ON_MODIFY, function(arg_5_0)
		arg_2_0.addSubLayers(Context.New({
			mediator = SpWeaponModifyMediator,
			viewComponent = SpWeaponModifyLayer,
			data = {
				spWeaponUid = arg_2_0.contextData.spWeaponUid,
				shipId = arg_2_0.contextData.shipId
			}
		}), True)
		arg_2_0.viewComponent.emit(BaseUI.ON_CLOSE))
	arg_2_0.bind(var_0_0.ON_INTENSIFY, function(arg_6_0)
		local var_6_0 = getProxy(BayProxy).getShipById(arg_2_0.contextData.shipId)

		if var_6_0:
			local var_6_1, var_6_2 = ShipStatus.ShipStatusCheck("onModify", var_6_0)

			if not var_6_1:
				pg.TipsMgr.GetInstance().ShowTips(var_6_2)

				return

		arg_2_0.addSubLayers(Context.New({
			mediator = SpWeaponUpgradeMediator,
			viewComponent = SpWeaponUpgradeLayer,
			data = {
				spWeaponUid = arg_2_0.contextData.spWeaponUid,
				shipId = arg_2_0.contextData.shipId
			}
		}), True, function()
			arg_2_0.viewComponent.emit(BaseUI.ON_CLOSE)))
	arg_2_0.bind(var_0_0.ON_CHANGE, function(arg_8_0)
		local var_8_0 = getProxy(BayProxy).getShipById(arg_2_0.contextData.shipId)
		local var_8_1, var_8_2 = ShipStatus.ShipStatusCheck("onModify", var_8_0)

		if not var_8_1:
			pg.TipsMgr.GetInstance().ShowTips(var_8_2)

			return

		arg_2_0.viewComponent.emit(BaseUI.ON_CLOSE)
		arg_2_0.sendNotification(GAME.GO_SCENE, SCENE.SPWEAPON_STOREHOUSE, {
			lock = True,
			shipId = arg_2_0.contextData.shipId,
			warp = StoreHouseConst.WARP_TO_WEAPON,
			mode = StoreHouseConst.EQUIPMENT
		}))
	arg_2_0.bind(var_0_0.ON_MOVE, function(arg_9_0, arg_9_1)
		arg_2_0.viewComponent.emit(BaseUI.ON_CLOSE)
		arg_2_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			page = 2,
			shipId = arg_9_1
		}))

def var_0_0.listNotificationInterests(arg_10_0):
	return {
		GAME.EQUIP_SPWEAPON_TO_SHIP_DONE
	}

def var_0_0.handleNotification(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1.getName()
	local var_11_1 = arg_11_1.getBody()

	if var_11_0 == GAME.EQUIP_SPWEAPON_TO_SHIP_DONE:
		arg_11_0.viewComponent.emit(BaseUI.ON_CLOSE)

return var_0_0
