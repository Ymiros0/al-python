local var_0_0 = class("AwardInfoMediator", import("..base.ContextMediator"))

var_0_0.ON_DROP = "AwardInfoMediator.ON_DROP"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_DROP, function(arg_2_0, arg_2_1, arg_2_2)
		if arg_2_1.type == DROP_TYPE_EQUIP:
			arg_1_0.addSubLayers(Context.New({
				mediator = EquipmentInfoMediator,
				viewComponent = EquipmentInfoLayer,
				data = {
					equipmentId = arg_2_1.getConfig("id"),
					type = EquipmentInfoMediator.TYPE_DISPLAY,
					onRemoved = arg_2_2,
					LayerWeightMgr_weight = LayerWeightConst.THIRD_LAYER
				}
			}))
		elif arg_2_1.type == DROP_TYPE_SPWEAPON:
			arg_1_0.addSubLayers(Context.New({
				mediator = SpWeaponInfoMediator,
				viewComponent = SpWeaponInfoLayer,
				data = {
					spWeaponConfigId = arg_2_1.getConfig("id"),
					type = SpWeaponInfoLayer.TYPE_DISPLAY,
					onRemoved = arg_2_2,
					LayerWeightMgr_weight = LayerWeightConst.THIRD_LAYER
				}
			}))
		else
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_SINGLE_ITEM,
				drop = arg_2_1,
				onNo = arg_2_2,
				onYes = arg_2_2,
				weight = LayerWeightConst.THIRD_LAYER
			}))

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		GAME.STORY_BEGIN,
		GAME.STORY_END,
		GAME.STORY_NEXT
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == GAME.STORY_BEGIN or var_4_0 == GAME.STORY_NEXT:
		arg_4_0.viewComponent.ShowOrHideSpriteMask(False)
	elif var_4_0 == GAME.STORY_END:
		arg_4_0.viewComponent.ShowOrHideSpriteMask(True)

return var_0_0
