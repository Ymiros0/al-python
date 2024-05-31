local var_0_0 = class("EquipmentInfoMediator", import("..base.ContextMediator"))

var_0_0.TYPE_DEFAULT = 1
var_0_0.TYPE_SHIP = 2
var_0_0.TYPE_REPLACE = 3
var_0_0.TYPE_DISPLAY = 4
var_0_0.SHOW_UNIQUE = {
	1,
	2,
	3,
	4
}
var_0_0.ON_DESTROY = "EquipmentInfoMediator.ON_DESTROY"
var_0_0.ON_EQUIP = "EquipmentInfoMediator.ON_EQUIP"
var_0_0.ON_INTENSIFY = "EquipmentInfoMediator.ON_INTENSIFY"
var_0_0.ON_CHANGE = "EquipmentInfoMediator.ON_CHANGE"
var_0_0.ON_UNEQUIP = "EquipmentInfoMediator.ON_UNEQUIP"
var_0_0.ON_REVERT = "EquipmentInfoMediator.ON_REVERT"
var_0_0.ON_MOVE = "EquipmentInfoMediator.ON_MOVE"
var_0_0.OPEN_LAYER = "OPEN LAYER"

def var_0_0.register(arg_1_0):
	if getProxy(ContextProxy).getCurrentContext().scene == SCENE.EQUIPSCENE:
		arg_1_0.viewComponent.fromEquipmentView = True

	arg_1_0.bind(var_0_0.ON_DESTROY, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.DESTROY_EQUIPMENTS, {
			equipments = {
				{
					arg_1_0.contextData.equipmentId,
					arg_2_1
				}
			}
		}))
	arg_1_0.bind(var_0_0.ON_EQUIP, function(arg_3_0)
		if arg_1_0.contextData.oldShipId:
			local var_3_0 = getProxy(BayProxy).getShipById(arg_1_0.contextData.oldShipId)
			local var_3_1, var_3_2 = ShipStatus.ShipStatusCheck("onModify", var_3_0)

			if not var_3_1:
				pg.TipsMgr.GetInstance().ShowTips(var_3_2)
			else
				if arg_1_0.viewComponent.fromEquipmentView:
					arg_1_0.sendNotification(EquipmentMediator.NO_UPDATE)

				arg_1_0.sendNotification(GAME.EQUIP_FROM_SHIP, {
					equipmentId = arg_1_0.contextData.equipmentId,
					shipId = arg_1_0.contextData.shipId,
					pos = arg_1_0.contextData.pos,
					oldShipId = arg_1_0.contextData.oldShipId,
					oldPos = arg_1_0.contextData.oldPos
				})
		else
			if arg_1_0.viewComponent.fromEquipmentView:
				arg_1_0.sendNotification(EquipmentMediator.NO_UPDATE)

			arg_1_0.sendNotification(GAME.EQUIP_TO_SHIP, {
				equipmentId = arg_1_0.contextData.equipmentId,
				shipId = arg_1_0.contextData.shipId,
				pos = arg_1_0.contextData.pos
			}))
	arg_1_0.bind(var_0_0.ON_UNEQUIP, function(arg_4_0)
		arg_1_0.sendNotification(GAME.UNEQUIP_FROM_SHIP, {
			shipId = arg_1_0.contextData.shipId,
			pos = arg_1_0.contextData.pos
		})
		arg_1_0.viewComponent.emit(BaseUI.ON_CLOSE))
	arg_1_0.bind(var_0_0.ON_INTENSIFY, function(arg_5_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = EquipUpgradeMediator,
			viewComponent = EquipUpgradeLayer,
			data = {
				equipmentId = arg_1_0.contextData.equipmentId,
				shipId = arg_1_0.contextData.shipId,
				pos = arg_1_0.contextData.pos
			}
		}), True, function()
			arg_1_0.viewComponent.emit(BaseUI.ON_CLOSE)))
	arg_1_0.bind(var_0_0.ON_CHANGE, function(arg_7_0)
		local var_7_0 = getProxy(BayProxy)
		local var_7_1 = var_7_0.getShipById(arg_1_0.contextData.shipId)
		local var_7_2 = getProxy(EquipmentProxy).getEquipments(True)
		local var_7_3 = var_7_0.getEquipsInShips(function(arg_8_0, arg_8_1)
			return var_7_1.id != arg_8_1 and not var_7_1.isForbiddenAtPos(arg_8_0, arg_1_0.contextData.pos))

		for iter_7_0, iter_7_1 in ipairs(var_7_2):
			if not var_7_1.isForbiddenAtPos(iter_7_1, arg_1_0.contextData.pos):
				table.insert(var_7_3, iter_7_1)

		_.each(var_7_3, function(arg_9_0)
			if not var_7_1.canEquipAtPos(arg_9_0, arg_1_0.contextData.pos):
				arg_9_0.mask = True)
		arg_1_0.viewComponent.emit(BaseUI.ON_CLOSE)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.EQUIPSCENE, {
			lock = True,
			equipmentVOs = var_7_3,
			shipId = arg_1_0.contextData.shipId,
			pos = arg_1_0.contextData.pos,
			warp = StoreHouseConst.WARP_TO_WEAPON,
			mode = StoreHouseConst.EQUIPMENT
		}))
	arg_1_0.bind(var_0_0.ON_REVERT, function(arg_10_0, arg_10_1)
		arg_1_0.sendNotification(GAME.REVERT_EQUIPMENT, {
			id = arg_10_1
		}))
	arg_1_0.bind(var_0_0.ON_MOVE, function(arg_11_0, arg_11_1)
		arg_1_0.viewComponent.emit(BaseUI.ON_CLOSE)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHIPINFO, {
			page = 2,
			shipId = arg_11_1
		}))
	arg_1_0.bind(var_0_0.OPEN_LAYER, function(arg_12_0, ...)
		arg_1_0.addSubLayers(...))

	if arg_1_0.contextData.equipment:
		arg_1_0.viewComponent.setEquipment(arg_1_0.contextData.equipment)
	else
		local var_1_0 = getProxy(EquipmentProxy)
		local var_1_1 = arg_1_0.contextData.equipmentId
		local var_1_2 = var_1_0.getEquipmentById(var_1_1) or var_1_1 and var_1_1 > 0 and Equipment.New({
			id = var_1_1
		}) or None

		arg_1_0.viewComponent.setEquipment(var_1_2)

	local var_1_3 = getProxy(BayProxy)
	local var_1_4 = arg_1_0.contextData.shipVO or var_1_3.getShipById(arg_1_0.contextData.shipId)
	local var_1_5 = arg_1_0.contextData.oldShipId and var_1_3.getShipById(arg_1_0.contextData.oldShipId) or None

	arg_1_0.viewComponent.setShip(var_1_4, var_1_5)

	local var_1_6 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.setPlayer(var_1_6)

def var_0_0.listNotificationInterests(arg_13_0):
	return {
		GAME.DESTROY_EQUIPMENTS_DONE,
		GAME.EQUIP_TO_SHIP_DONE,
		GAME.REVERT_EQUIPMENT_DONE
	}

def var_0_0.handleNotification(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_1.getName()
	local var_14_1 = arg_14_1.getBody()

	if var_14_0 == GAME.DESTROY_EQUIPMENTS_DONE or var_14_0 == GAME.EQUIP_TO_SHIP_DONE or var_14_0 == GAME.REVERT_EQUIPMENT_DONE:
		arg_14_0.viewComponent.emit(BaseUI.ON_CLOSE)

return var_0_0
