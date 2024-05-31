local var_0_0 = class("CourtYardRenamePage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CourtYardRenameUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.confirmBtn = arg_2_0.findTF("frame/confirm")
	arg_2_0.cancelBtn = arg_2_0.findTF("frame/cancel")
	arg_2_0.closeBtn = arg_2_0.findTF("frame/close")
	arg_2_0.input = arg_2_0.findTF("frame/input")

	setText(arg_2_0.findTF("frame/cancel/Text"), i18n("word_cancel"))
	setText(arg_2_0.findTF("frame/confirm/Text"), i18n("word_ok"))
	setText(arg_2_0.findTF("frame/title"), i18n("backyard_rename_title"))
	setText(arg_2_0.findTF("frame/input/placehoder"), i18n("backyard_rename_tip"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		local var_4_0 = getInputText(arg_3_0.input)

		if not var_4_0 or var_4_0 == "":
			pg.TipsMgr.GetInstance().ShowTips(i18n("word_should_input"))

			return

		if not nameValidityCheck(var_4_0, 0, 20, {
			"spece_illegal_tip",
			"login_newPlayerScene_name_tooShort",
			"login_newPlayerScene_name_tooLong",
			"playerinfo_mask_word"
		}):
			return

		arg_3_0.emit(CourtYardMediator.RENAME, var_4_0)
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Flush(arg_8_0):
	arg_8_0.Show()

def var_0_0.OnDestroy(arg_9_0):
	arg_9_0.Hide()

return var_0_0
