local var_0_0 = class("MonthCardSetLayer", import("..base.BaseUI"))

var_0_0.PIECES = 100

def var_0_0.getUIName(arg_1_0):
	return "MonthCardSetUI"

def var_0_0.setPlayer(arg_2_0, arg_2_1):
	arg_2_0.player = arg_2_1

def var_0_0.setRatio(arg_3_0, arg_3_1):
	arg_3_0.ratio = math.clamp(arg_3_1, 0, var_0_0.PIECES)

def var_0_0.init(arg_4_0):
	arg_4_0.name = arg_4_0.findTF("window/bg/name")
	arg_4_0.desc = arg_4_0.findTF("window/bg/desc")
	arg_4_0.oil = arg_4_0.findTF("window/black/oil/icon_bg/count")
	arg_4_0.gold = arg_4_0.findTF("window/black/gold/icon_bg/count")
	arg_4_0.slider = arg_4_0.findTF("window/black/slider")
	arg_4_0.rate = arg_4_0.findTF("window/black/misc/rate")
	arg_4_0.confirm = arg_4_0.findTF("window/confirm")
	arg_4_0.cancel = arg_4_0.findTF("window/cancel")

def var_0_0.didEnter(arg_5_0):
	onButton(arg_5_0, arg_5_0._tf, function()
		arg_5_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	onButton(arg_5_0, arg_5_0.cancel, function()
		arg_5_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	onButton(arg_5_0, arg_5_0.confirm, function()
		arg_5_0.emit(MonthCardSetMediator.ON_SET_RATIO, arg_5_0.ratio), SFX_CANCEL)
	onSlider(arg_5_0, arg_5_0.slider, function(arg_9_0)
		arg_5_0.setRatio(arg_9_0)
		arg_5_0.updateRatioView())
	arg_5_0.updateView()
	arg_5_0.updateRatioView()
	pg.UIMgr.GetInstance().BlurPanel(arg_5_0._tf)

def var_0_0.updateView(arg_10_0):
	local var_10_0 = arg_10_0.player.getCardById(VipCard.MONTH)
	local var_10_1 = math.floor((var_10_0.getLeftDate() - pg.TimeMgr.GetInstance().GetServerTime()) / 86400)

	setText(arg_10_0.name, string.format("贸易许可证（剩余%s天）", var_10_1))
	setText(arg_10_0.rate, "1 . 5")

def var_0_0.updateRatioView(arg_11_0):
	setSlider(arg_11_0.slider, 0, var_0_0.PIECES, arg_11_0.ratio)
	setText(arg_11_0.oil, 400 * arg_11_0.ratio / var_0_0.PIECES)
	setText(arg_11_0.gold, 2000 * (var_0_0.PIECES - arg_11_0.ratio) / var_0_0.PIECES)

def var_0_0.willExit(arg_12_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_12_0._tf)

return var_0_0
