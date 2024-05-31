local var_0_0 = class("Msgbox4SpweaponConfirm", import(".MsgboxSubPanel"))

function var_0_0.getUIName(arg_1_0)
	return "Msgbox4SpweaponConfirm"
end

function var_0_0.OnRefresh(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_1.op

	if var_2_0 == SpWeapon.CONFIRM_OP_DISCARD then
		setText(arg_2_0._tf:Find("Desc"), i18n("spweapon_ui_change_attr_text1"))
		setText(arg_2_0._tf:Find("Tip"), i18n("spweapon_ui_change_attr_text2"))

		local var_2_1 = arg_2_1.attrs[1]

		setText(arg_2_0._tf:Find("Desc (1)/Attr"), var_2_1[1])
		setText(arg_2_0._tf:Find("Desc (1)/Value1"), setColorStr(var_2_1[2], "#ffde38"))
		setText(arg_2_0._tf:Find("Desc (1)/Value2"), setColorStr(var_2_1[3], COLOR_GREY))
		setText(arg_2_0._tf:Find("Desc (1)/Symbol"), "")

		local var_2_2 = arg_2_1.attrs[2]

		setText(arg_2_0._tf:Find("Desc (2)/Attr"), var_2_2[1])
		setText(arg_2_0._tf:Find("Desc (2)/Value1"), setColorStr(var_2_2[2], "#ffde38"))
		setText(arg_2_0._tf:Find("Desc (2)/Value2"), setColorStr(var_2_2[3], COLOR_GREY))
		setText(arg_2_0._tf:Find("Desc (2)/Symbol"), "")
	elseif var_2_0 == SpWeapon.CONFIRM_OP_EXCHANGE then
		setText(arg_2_0._tf:Find("Desc"), i18n("spweapon_ui_keep_attr_text1"))
		setText(arg_2_0._tf:Find("Tip"), i18n("spweapon_ui_keep_attr_text2"))

		local var_2_3 = arg_2_1.attrs[1]

		setText(arg_2_0._tf:Find("Desc (1)/Attr"), var_2_3[1])
		setText(arg_2_0._tf:Find("Desc (1)/Value1"), var_2_3[2])
		setText(arg_2_0._tf:Find("Desc (1)/Value2"), setColorStr(var_2_3[3], "#92fc63"))
		setText(arg_2_0._tf:Find("Desc (1)/Symbol"), ">")

		local var_2_4 = arg_2_1.attrs[2]

		setText(arg_2_0._tf:Find("Desc (2)/Attr"), var_2_4[1])
		setText(arg_2_0._tf:Find("Desc (2)/Value1"), var_2_4[2])
		setText(arg_2_0._tf:Find("Desc (2)/Value2"), setColorStr(var_2_4[3], "#92fc63"))
		setText(arg_2_0._tf:Find("Desc (2)/Symbol"), ">")
	end
end

return var_0_0
