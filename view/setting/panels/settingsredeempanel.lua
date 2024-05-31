local var_0_0 = class("SettingsRedeemPanel", import(".SettingsBasePanel"))

function var_0_0.GetUIName(arg_1_0)
	return "SettingsRedeem"
end

function var_0_0.GetTitle(arg_2_0)
	return i18n("Settings_title_Redeem")
end

function var_0_0.GetTitleEn(arg_3_0)
	return "  / KEY"
end

function var_0_0.OnInit(arg_4_0)
	arg_4_0.codeInput = findTF(arg_4_0._tf, "voucher")
	arg_4_0.placeholder = findTF(arg_4_0.codeInput, "Placeholder")
	arg_4_0.placeholder:GetComponent(typeof(Text)).text = i18n("exchangecode_use_placeholder")
	arg_4_0.achieveBtn = findTF(arg_4_0.codeInput, "submit")

	onButton(arg_4_0, arg_4_0.achieveBtn, function()
		pg.m02:sendNotification(GAME.EXCHANGECODE_USE, {
			key = arg_4_0.codeInput:GetComponent(typeof(InputField)).text
		})
	end, SFX_CONFIRM)
	setGray(arg_4_0.achieveBtn, getInputText(arg_4_0.codeInput) == "")
	onInputChanged(arg_4_0, arg_4_0.codeInput, function()
		setGray(arg_4_0.achieveBtn, getInputText(arg_4_0.codeInput) == "")
	end)
	setText(findTF(arg_4_0._tf, "voucher/prompt"), i18n("Settings_title_Redeem_input_label"))
	setText(findTF(arg_4_0._tf, "voucher/Placeholder"), i18n("Settings_title_Redeem_input_placeholder"))
	setText(findTF(arg_4_0._tf, "voucher/submit/Image"), i18n("Settings_title_Redeem_input_submit"))
end

function var_0_0.ClearExchangeCode(arg_7_0)
	arg_7_0.codeInput:GetComponent(typeof(InputField)).text = ""
end

return var_0_0
