local var_0_0 = class("EquipmentTransformMediator", import("view.base.ContextMediator"))

var_0_0.TRANSFORM_EQUIP = "transform equip"
var_0_0.UPDATE_NEW_FLAG = "UPDATE NEW FLAG"
var_0_0.OPEN_TRANSFORM_TREE = "OPEN TRANSFORM TREE"
var_0_0.SELECT_TRANSFORM_FROM_STOREHOUSE = "SELECT_TRANSFORM_FROM_STOREHOUSE"
var_0_0.OPEN_LAYER = "OPEN_LAYER"

def var_0_0.register(arg_1_0):
	arg_1_0.BindEvent()

	arg_1_0.env = {}

	arg_1_0.getViewComponent().SetEnv(arg_1_0.env)

	arg_1_0.env.tracebackHelper = getProxy(EquipmentProxy).GetWeakEquipsDict()

	arg_1_0.getViewComponent().UpdatePlayer(getProxy(PlayerProxy).getData())

def var_0_0.BindEvent(arg_2_0):
	arg_2_0.bind(var_0_0.TRANSFORM_EQUIP, function(arg_3_0, arg_3_1, arg_3_2)
		arg_2_0.sendNotification(GAME.TRANSFORM_EQUIPMENT, {
			candicate = arg_3_1,
			formulaIds = {
				arg_3_2
			}
		}))
	arg_2_0.bind(var_0_0.UPDATE_NEW_FLAG, function(arg_4_0, arg_4_1)
		arg_2_0.sendNotification(var_0_0.UPDATE_NEW_FLAG, arg_4_1))
	arg_2_0.bind(var_0_0.OPEN_TRANSFORM_TREE, function(arg_5_0, arg_5_1)
		arg_2_0.getViewComponent().closeView()
		arg_2_0.sendNotification(GAME.GO_SCENE, SCENE.EQUIPMENT_TRANSFORM, {
			targetEquipId = arg_5_1,
			mode = EquipmentTransformTreeScene.MODE_HIDESIDE
		}))
	arg_2_0.bind(var_0_0.SELECT_TRANSFORM_FROM_STOREHOUSE, function(arg_6_0, arg_6_1)
		local var_6_0 = arg_2_0.env.tracebackHelper.GetEquipmentTransformCandicates(arg_6_1)

		arg_2_0.sendNotification(GAME.GO_SCENE, SCENE.SELECT_TRANSFORM_EQUIPMENT, {
			warp = StoreHouseConst.WARP_TO_WEAPON,
			sourceVOs = var_6_0,
			def onSelect:(arg_7_0)
				if arg_7_0.type == DROP_TYPE_ITEM and arg_7_0.template.count < arg_7_0.composeCfg.material_num:
					pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_upgrade_feedback_lack_of_fragment", arg_7_0.template.getConfig("name")))

					return False
				elif arg_7_0.type == DROP_TYPE_EQUIP and arg_7_0.template.count <= 0:
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_x", arg_7_0.template.getConfig("name")))

					return False

				return True,
			def onConfirm:(arg_8_0)
				arg_2_0.contextData.sourceEquipmentInstance = arg_8_0[1] or arg_2_0.contextData.sourceEquipmentInstance

				return True
		}))
	arg_2_0.bind(var_0_0.OPEN_LAYER, function(arg_9_0, ...)
		arg_2_0.addSubLayers(...))

def var_0_0.listNotificationInterests(arg_10_0):
	return {
		GAME.TRANSFORM_EQUIPMENT_DONE,
		GAME.TRANSFORM_EQUIPMENT_FAIL,
		PlayerProxy.UPDATED,
		BagProxy.ITEM_UPDATED,
		EquipmentProxy.EQUIPMENT_UPDATED,
		GAME.EQUIP_TO_SHIP_DONE,
		GAME.UNEQUIP_FROM_SHIP_DONE
	}

def var_0_0.handleNotification(arg_11_0, arg_11_1):
	local var_11_0 = arg_11_1.getName()
	local var_11_1 = arg_11_1.getBody()

	if var_11_0 == PlayerProxy.UPDATED:
		arg_11_0.getViewComponent().UpdatePlayer(var_11_1)
	elif var_11_0 == BagProxy.ITEM_UPDATED:
		arg_11_0.getViewComponent().UpdatePage()
	elif var_11_0 == EquipmentProxy.EQUIPMENT_UPDATED:
		if arg_11_0.contextData.sourceEquipmentInstance:
			local var_11_2 = var_11_1.count == 0
			local var_11_3 = arg_11_0.contextData.sourceEquipmentInstance

			if var_11_2 and var_11_3.type == DROP_TYPE_EQUIP and EquipmentProxy.SameEquip(var_11_1, var_11_3.template):
				arg_11_0.contextData.sourceEquipmentInstance = None

		local var_11_4 = arg_11_0.getViewComponent()

		var_11_4.UpdateSourceEquipmentPaths()
		var_11_4.UpdateSourceInfo()
		var_11_4.UpdateTargetInfo()
	elif var_11_0 == GAME.UNEQUIP_FROM_SHIP_DONE or var_11_0 == GAME.EQUIP_TO_SHIP_DONE:
		local var_11_5 = arg_11_0.contextData.sourceEquipmentInstance

		if var_11_5 and var_11_5.type == DROP_TYPE_EQUIP:
			local var_11_6 = var_11_1.getEquip(var_11_5.template.shipPos)

			if var_11_5.template.shipId == var_11_1.id and (not var_11_6 or var_11_6.id != var_11_5.id):
				arg_11_0.contextData.sourceEquipmentInstance = None

		local var_11_7 = arg_11_0.getViewComponent()

		var_11_7.UpdateSourceEquipmentPaths()
		var_11_7.UpdateSourceInfo()
		var_11_7.UpdateTargetInfo()
	elif var_11_0 == GAME.TRANSFORM_EQUIPMENT_DONE:
		arg_11_0.contextData.sourceEquipmentInstance = None

		arg_11_0.getViewComponent().UpdatePage()
	elif var_11_0 == GAME.TRANSFORM_EQUIPMENT_FAIL:
		arg_11_0.getViewComponent().UpdatePage()

return var_0_0
