local var_0_0 = class("CourtYardThemeOwner", import("model.vo.Player"))

def var_0_0.GetName(arg_1_0):
	if getProxy(PlayerProxy).getRawData().ShouldCheckCustomName():
		return i18n("nodisplay_player_home_share")
	else
		return var_0_0.super.GetName(arg_1_0)

return var_0_0
