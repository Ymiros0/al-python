local var_0_0 = class("RepairPanel", import("..base.BasePanel"))

def var_0_0.init(arg_1_0):
	var_0_0.super.init(arg_1_0)

	arg_1_0.desc = arg_1_0.findTF("window/desc")
	arg_1_0.descFree = arg_1_0.findTF("window/text_free")
	arg_1_0.descCharge = arg_1_0.findTF("window/text_charge")
	arg_1_0.free = arg_1_0.findTF("window/text_free/time")
	arg_1_0.charge = arg_1_0.findTF("window/text_charge/time")
	arg_1_0.diamond = arg_1_0.findTF("window/diamond")
	arg_1_0.cost = findTF(arg_1_0.diamond, "cost")
	arg_1_0.cancel = arg_1_0.findTF("window/actions/cancel_button")
	arg_1_0.confirm = arg_1_0.findTF("window/actions/use_button")
	arg_1_0.back = arg_1_0.findTF("top/btnBack")
	arg_1_0.onConfirm = None
	arg_1_0.onCancel = None

def var_0_0.set(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4):
	arg_2_0.repairTimes = arg_2_1
	arg_2_0.freeTimes = arg_2_2
	arg_2_0.chargeTimes = arg_2_3
	arg_2_0.chargeDiamond = arg_2_4

	local var_2_0 = arg_2_0.freeTimes - math.min(arg_2_0.repairTimes, arg_2_0.freeTimes)
	local var_2_1 = arg_2_0.chargeTimes - (arg_2_0.repairTimes - (arg_2_0.freeTimes - var_2_0))

	setText(arg_2_0.free, var_2_0 .. "/" .. arg_2_0.freeTimes)
	setText(arg_2_0.charge, var_2_1 .. "/" .. arg_2_0.chargeTimes)
	setText(arg_2_0.cost, arg_2_0.chargeDiamond)
	setActive(arg_2_0.descFree, var_2_0 > 0)
	setActive(arg_2_0.descCharge, var_2_0 <= 0)
	setText(arg_2_0.desc, i18n("battle_repair_special_tip"))
	setText(arg_2_0.descFree, i18n("battle_repair_normal_name"))
	setText(arg_2_0.descCharge, i18n("battle_repair_special_name"))

	local var_2_2 = arg_2_0.repairTimes < arg_2_0.freeTimes + arg_2_0.chargeTimes

	setActive(arg_2_0.diamond, var_2_2 and arg_2_0.repairTimes >= arg_2_0.freeTimes)
	setButtonEnabled(arg_2_0.confirm, var_2_2)
	setGray(arg_2_0.confirm, not var_2_2, True)
	onButton(arg_2_0, arg_2_0.back, function()
		if arg_2_0.onCancel:
			arg_2_0.onCancel(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0.cancel, function()
		if arg_2_0.onCancel:
			arg_2_0.onCancel(), SFX_CANCEL)
	onButton(arg_2_0, arg_2_0.confirm, function()
		if arg_2_0.onConfirm:
			arg_2_0.onConfirm(), SFX_CONFIRM)

return var_0_0
