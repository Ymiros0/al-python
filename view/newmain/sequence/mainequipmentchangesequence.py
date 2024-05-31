local var_0_0 = class("MainEquipmentChangeSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = ItemShowPanel.ConfigData

	if not var_1_0.isOpen:
		arg_1_1()

		return

	local var_1_1 = var_1_0.equipID

	if PlayerPrefs.GetInt("ItemIconChange_" .. var_1_1, 0) == 0:
		local function var_1_2()
			arg_1_1()
			PlayerPrefs.SetInt("ItemIconChange_" .. var_1_1, 1)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			modal = True,
			hideNo = True,
			hideClose = True,
			type = MSGBOX_TYPE_JUST_FOR_SHOW,
			title = pg.MsgboxMgr.TITLE_INFORMATION,
			weight = LayerWeightConst.TOP_LAYER,
			onClose = var_1_2,
			onYes = var_1_2
		})
	else
		arg_1_1()

return var_0_0
