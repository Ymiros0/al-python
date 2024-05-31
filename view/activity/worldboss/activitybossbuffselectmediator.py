local var_0_0 = class("ActivityBossBuffSelectMediator", import("view.base.ContextMediator"))

var_0_0.ON_START = "ActivityBossBuffSelectMediator.ON_START"
var_0_0.SHOW_REWARDS = "ActivityBossBuffSelectMediator.SHOW_REWARDS"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_START, function(arg_2_0, arg_2_1)
		local var_2_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

		getProxy(ActivityProxy).GetActivityBossRuntime(var_2_0.id).buffIds = _.map(arg_2_1, function(arg_3_0)
			return arg_3_0.GetConfigID())

		arg_1_0.sendNotification(var_0_0.ON_START)
		arg_1_0.viewComponent.closeView())
	arg_1_0.bind(var_0_0.SHOW_REWARDS, function(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
		arg_1_0.addSubLayers(Context.New({
			mediator = ActivityBossScoreAwardMediator,
			viewComponent = ActivityBossScoreAwardLayer,
			data = {
				awards = arg_4_1,
				targets = arg_4_2,
				score = arg_4_3
			}
		})))

def var_0_0.listNotificationInterests(arg_5_0):
	return {}

def var_0_0.handleNotification(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.getName()
	local var_6_1 = arg_6_1.getBody()

	if var_6_0 == None:
		-- block empty

def var_0_0.remove(arg_7_0):
	return

return var_0_0
