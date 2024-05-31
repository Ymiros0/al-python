local var_0_0 = class("BossRushTotalRewardPanelMediator", import("view.activity.worldboss.ActivityBossTotalRewardPanelMediator"))

var_0_0.ON_WILL_EXIT = "BossRushTotalRewardPanelMediator.ON_WILL_EXIT"

def var_0_0.register(arg_1_0):
	getProxy(SettingsProxy).ResetContinuousOperationAutoSub()

return var_0_0
