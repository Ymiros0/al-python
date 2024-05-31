local var_0_0 = class("MainTagsView", import("..base.MainBaseView"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.monthCardTag = findTF(arg_1_0._tf, "monthcard")
	arg_1_0.sellTag = findTF(arg_1_0._tf, "sell")
	arg_1_0.skinTag = findTF(arg_1_0._tf, "skin")
	arg_1_0.buildTag = findTF(arg_1_0._tf, "build")
	arg_1_0.tecShipGiftTag = findTF(arg_1_0._tf, "tecshipgift")
	arg_1_0.mallTip = findTF(arg_1_0._tf, "tip")

def var_0_0.Init(arg_2_0):
	local var_2_0 = {}

	table.insert(var_2_0, function(arg_3_0)
		TagTipHelper.TecShipGiftTip(arg_2_0.tecShipGiftTag)
		onNextTick(arg_3_0))
	table.insert(var_2_0, function(arg_4_0)
		TagTipHelper.MonthCardTagTip(arg_2_0.monthCardTag)
		onNextTick(arg_4_0))
	table.insert(var_2_0, function(arg_5_0)
		TagTipHelper.SkinTagTip(arg_2_0.skinTag)
		onNextTick(arg_5_0))
	table.insert(var_2_0, function(arg_6_0)
		TagTipHelper.FuDaiTagTip(arg_2_0.sellTag)
		onNextTick(arg_6_0))
	table.insert(var_2_0, function(arg_7_0)
		if not arg_2_0.AnyMallTipShowing():
			TagTipHelper.FreeGiftTag({
				arg_2_0.mallTip
			})
		else
			setActive(arg_2_0.mallTip, False)

		onNextTick(arg_7_0))
	table.insert(var_2_0, function(arg_8_0)
		TagTipHelper.FreeBuildTicketTip(arg_2_0.buildTag)
		onNextTick(arg_8_0))
	seriesAsync(var_2_0)

def var_0_0.AnyMallTipShowing(arg_9_0):
	local var_9_0 = {
		arg_9_0.monthCardTag,
		arg_9_0.sellTag,
		arg_9_0.skinTag,
		arg_9_0.tecShipGiftTag
	}

	return _.any(var_9_0, function(arg_10_0)
		return arg_10_0.GetComponent(typeof(Image)).enabled)

def var_0_0.Refresh(arg_11_0):
	arg_11_0.Init()

return var_0_0
