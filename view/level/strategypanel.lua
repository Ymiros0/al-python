﻿local var_0_0 = class("StrategyPanel", import("..base.BasePanel"))

function var_0_0.init(arg_1_0)
	var_0_0.super.init(arg_1_0)

	arg_1_0.icon = arg_1_0:findTF("window/panel/item/icon_bg/icon")
	arg_1_0.count = arg_1_0:findTF("window/panel/item/icon_bg/count")
	arg_1_0.name = arg_1_0:findTF("window/panel/item/name")
	arg_1_0.desc = arg_1_0:findTF("window/panel/item/desc")
	arg_1_0.btnCancel = arg_1_0:findTF("window/panel/actions/cancel_button")
	arg_1_0.btnUse = arg_1_0:findTF("window/panel/actions/use_button")
	arg_1_0.btnBack = arg_1_0:findTF("top/btnBack")
	arg_1_0.tips = arg_1_0:findTF("window/panel/tips")
	arg_1_0.txSwitch = findTF(arg_1_0.btnUse, "switch")
	arg_1_0.txUse = findTF(arg_1_0.btnUse, "use")
	arg_1_0.onConfirm = nil
	arg_1_0.onCancel = nil
end

function var_0_0.set(arg_2_0, arg_2_1)
	arg_2_0.strategy = arg_2_1

	local var_2_0 = pg.strategy_data_template[arg_2_1.id]

	GetImageSpriteFromAtlasAsync("strategyicon/" .. var_2_0.icon, "", arg_2_0.icon)

	if var_2_0.type == 1 then
		setText(arg_2_0.count, "")
		setActive(arg_2_0.tips, true)
		setActive(arg_2_0.txSwitch, true)
		setActive(arg_2_0.txUse, false)
	else
		setText(arg_2_0.count, arg_2_1.count)
		setActive(arg_2_0.tips, false)
		setActive(arg_2_0.txSwitch, false)
		setActive(arg_2_0.txUse, true)
	end

	setText(arg_2_0.name, var_2_0.name)
	setText(arg_2_0.desc, var_2_0.desc)
	onButton(arg_2_0, arg_2_0.btnBack, function()
		if arg_2_0.onCancel then
			arg_2_0.onCancel()
		end
	end, SFX_CANCEL)
	onButton(arg_2_0, arg_2_0.btnCancel, function()
		if arg_2_0.onCancel then
			arg_2_0.onCancel()
		end
	end, SFX_CANCEL)
	onButton(arg_2_0, arg_2_0.btnUse, function()
		if arg_2_0.onConfirm then
			arg_2_0.onConfirm()
		end
	end, SFX_CONFIRM)
end

return var_0_0
