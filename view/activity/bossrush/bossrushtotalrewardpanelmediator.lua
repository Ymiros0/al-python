local var_0_0 = class("BossRushTotalRewardPanelMediator", import("view.activity.worldboss.ActivityBossTotalRewardPanelMediator"))

var_0_0.ON_WILL_EXIT = "BossRushTotalRewardPanelMediator:ON_WILL_EXIT"

function var_0_0.register(arg_1_0)
	getProxy(SettingsProxy):ResetContinuousOperationAutoSub()
end

return var_0_0
