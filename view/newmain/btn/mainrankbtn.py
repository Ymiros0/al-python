local var_0_0 = class("MainRankBtn", import(".MainBaseBtn"))

def var_0_0.OnClick(arg_1_0):
	arg_1_0.emit(NewMainMediator.GO_SCENE, SCENE.BILLBOARD, {
		index = PowerRank.TYPE_POWER
	})

def var_0_0.Flush(arg_2_0):
	local var_2_0 = arg_2_0.IsActive()

	setActive(arg_2_0._tf, var_2_0)

def var_0_0.IsActive(arg_3_0):
	return getProxy(PlayerProxy).getRawData().level >= pg.open_systems_limited[6].level

return var_0_0
