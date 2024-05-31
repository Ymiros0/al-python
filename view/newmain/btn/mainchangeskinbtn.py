local var_0_0 = class("MainChangeSkinBtn", import(".MainBaseBtn"))

def var_0_0.OnClick(arg_1_0):
	arg_1_0.emit(NewMainScene.ON_CHANGE_SKIN)

def var_0_0.Flush(arg_2_0, arg_2_1):
	arg_2_0.UpdateChangeSkinBtn()

def var_0_0.UpdateChangeSkinBtn(arg_3_0):
	local var_3_0

	if getProxy(SettingsProxy).IsOpenRandomFlagShip():
		var_3_0 = _.select(getProxy(SettingsProxy).GetRandomFlagShipList(), function(arg_4_0)
			return getProxy(BayProxy).RawGetShipById(arg_4_0) != None)
	else
		var_3_0 = getProxy(PlayerProxy).getRawData().characters

	local var_3_1 = getProxy(SettingsProxy).GetFlagShipDisplayMode()
	local var_3_2 = var_3_1 == FlAG_SHIP_DISPLAY_ONLY_EDUCATECHAR and 0 or #var_3_0

	if getProxy(PlayerProxy).getRawData().ExistEducateChar() and var_3_1 != FlAG_SHIP_DISPLAY_ONLY_SHIP:
		var_3_2 = var_3_2 + 1

	setActive(arg_3_0._tf, var_3_2 > 1)

return var_0_0
