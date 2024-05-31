local var_0_0 = class("ConfirmEquipmentDeletePanel", import(".MsgboxSubPanel"))

def var_0_0.getUIName(arg_1_0):
	return "EquipDeleteConfirmBox"

def var_0_0.UpdateView(arg_2_0, arg_2_1):
	arg_2_1.hideYes = True

	var_0_0.super.UpdateView(arg_2_0, arg_2_1)

def var_0_0.OnRefresh(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.data

	arg_3_0.SetWindowSize(Vector2(937, 540))

	local var_3_1 = arg_3_0._tf.Find("intro")
	local var_3_2 = arg_3_0._tf.Find("InputField")
	local var_3_3 = var_3_2.Find("Placeholder")

	setText(var_3_3, i18n("box_equipment_del_click"))
	setText(var_3_1, SwitchSpecialChar(i18n("destory_important_equipment_tip", var_3_0.name)))

	local function var_3_4()
		local var_4_0 = getInputText(var_3_2)

		if not var_4_0 or var_4_0 == "":
			pg.TipsMgr.GetInstance().ShowTips(i18n("word_should_input"))

			return

		if var_4_0 != var_3_0.name:
			pg.TipsMgr.GetInstance().ShowTips(i18n("destory_important_equipment_input_erro"))

			return

		existCall(arg_3_1.onYes)
		arg_3_0.closeView()

	arg_3_0.yesBtn = arg_3_0.viewParent.createBtn({
		noQuit = True,
		text = arg_3_1.yesText or arg_3_0.viewParent.TEXT_CONFIRM,
		btnType = arg_3_1.yesBtnType or arg_3_0.viewParent.BUTTON_BLUE,
		onCallback = var_3_4,
		sound = arg_3_1.yesSound or SFX_CONFIRM,
		alignment = arg_3_1.yesSize and TextAnchor.MiddleCenter
	})

	if arg_3_1.yesSize:
		arg_3_0.yesBtn.sizeDelta = arg_3_1.yesSize

	setGray(arg_3_0.yesBtn, arg_3_1.yesGray, True)

return var_0_0
