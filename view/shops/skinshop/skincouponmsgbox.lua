local var_0_0 = class("SkinCouponMsgBox", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "SkinCouponMsgBoxUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.closeBtn = arg_2_0:findTF("window/top/btnBack")
	arg_2_0.cancelBtn = arg_2_0:findTF("window/button_container/cancel")
	arg_2_0.confirmBtn = arg_2_0:findTF("window/button_container/confirm")
	arg_2_0.label1 = arg_2_0:findTF("window/frame/Text"):GetComponent(typeof(Text))
	arg_2_0.leftItemTr = arg_2_0:findTF("window/frame/left")
	arg_2_0.nameTxt = arg_2_0.leftItemTr:Find("name_bg/Text"):GetComponent(typeof(Text))

	setText(arg_2_0.cancelBtn:Find("pic"), i18n("msgbox_text_cancel"))
	setText(arg_2_0.confirmBtn:Find("pic"), i18n("msgbox_text_confirm"))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0._tf:Find("bg"), function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.Show(arg_7_0, arg_7_1)
	var_0_0.super.Show(arg_7_0)

	arg_7_0.settings = arg_7_1

	arg_7_0:UpdateItem(arg_7_1)
	arg_7_0:RegisterBtn(arg_7_1)
	arg_7_0:UpdateContent(arg_7_1)
end

function var_0_0.RegisterBtn(arg_8_0, arg_8_1)
	onButton(arg_8_0, arg_8_0.confirmBtn, function()
		if arg_8_1.onYes then
			arg_8_1.onYes()
		end

		arg_8_0:Hide()
	end, SFX_PANEL)
end

function var_0_0.UpdateContent(arg_10_0, arg_10_1)
	local var_10_0 = arg_10_1.itemConfig
	local var_10_1 = arg_10_1.skinName
	local var_10_2 = arg_10_1.price

	arg_10_0.label1.text = i18n("skin_purchase_confirm", var_10_0.name, var_10_2, var_10_1)
	arg_10_0.nameTxt.text = var_10_0.name
end

function var_0_0.UpdateItem(arg_11_0, arg_11_1)
	updateDrop(arg_11_0.leftItemTr, {
		count = 1,
		type = DROP_TYPE_ITEM,
		id = arg_11_1.itemConfig.id
	})
end

function var_0_0.Hide(arg_12_0)
	arg_12_0.settings = nil

	var_0_0.super.Hide(arg_12_0)
	arg_12_0:Destroy()
end

function var_0_0.OnDestroy(arg_13_0)
	return
end

return var_0_0
