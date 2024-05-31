local var_0_0 = class("MainOverDueEquipmentSequence", import(".MainSublayerSequence"))

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(EquipmentProxy).getTimeLimitShipList()

	if #var_1_0 > 0:
		arg_1_0.ShowMsgBox({
			item2Row = True,
			itemList = var_1_0,
			content = i18n("time_limit_equip_destroy_on_ship"),
			onYes = arg_1_1,
			onNo = arg_1_1
		})
	else
		arg_1_1()

def var_0_0.ShowMsgBox(arg_2_0, arg_2_1):
	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		hideNo = True,
		type = MSGBOX_TYPE_ITEM_BOX,
		items = arg_2_1.itemList,
		content = arg_2_1.content,
		item2Row = arg_2_1.item2Row,
		def itemFunc:(arg_3_0)
			arg_2_0.ShowItemBox(arg_3_0, function()
				arg_2_0.ShowMsgBox(arg_2_1)),
		weight = LayerWeightConst.TOP_LAYER
	})

def var_0_0.ShowItemBox(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_1.type == DROP_TYPE_EQUIP:
		arg_5_0.AddSubLayers(Context.New({
			mediator = EquipmentInfoMediator,
			viewComponent = EquipmentInfoLayer,
			data = {
				equipmentId = arg_5_1.getConfig("id"),
				type = EquipmentInfoMediator.TYPE_DISPLAY,
				onRemoved = arg_5_2,
				LayerWeightMgr_weight = LayerWeightConst.TOP_LAYER
			}
		}))
	elif arg_5_1.type == DROP_TYPE_SPWEAPON:
		arg_5_0.AddSubLayers(Context.New({
			mediator = SpWeaponInfoMediator,
			viewComponent = SpWeaponInfoLayer,
			data = {
				spWeaponConfigId = arg_5_1.getConfig("id"),
				type = SpWeaponInfoLayer.TYPE_DISPLAY,
				onRemoved = arg_5_2,
				LayerWeightMgr_weight = LayerWeightConst.TOP_LAYER
			}
		}))
	else
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_SINGLE_ITEM,
			drop = arg_5_1,
			onNo = arg_5_2,
			onYes = arg_5_2,
			weight = LayerWeightConst.TOP_LAYER
		})

return var_0_0
