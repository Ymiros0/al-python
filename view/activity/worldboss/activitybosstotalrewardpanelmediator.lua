local var_0_0 = class("ActivityBossTotalRewardPanelMediator", import("view.base.ContextMediator"))

function var_0_0.register(arg_1_0)
	getProxy(SettingsProxy):ResetContinuousOperationAutoSub()
end

return var_0_0
