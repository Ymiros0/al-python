local var_0_0 = class("MainReceiveBossRushAwardsSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	seriesAsync({
		function(arg_2_0)
			local var_2_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSSRUSH)

			if not var_2_0 or var_2_0.isEnd() or not var_2_0.HasAwards():
				arg_2_0()

				return

			seriesAsync({
				function(arg_3_0)
					pg.m02.sendNotification(GAME.BOSSRUSH_SETTLE, {
						actId = var_2_0.id,
						callback = arg_3_0
					}),
				function(arg_4_0, arg_4_1)
					local var_4_0 = arg_4_1.awards

					if #var_4_0 > 0:
						LoadContextCommand.LoadLayerOnTopContext(Context.New({
							mediator = AwardInfoMediator,
							viewComponent = AwardInfoLayer,
							data = {
								items = var_4_0,
								removeFunc = arg_4_0
							}
						}))

						return

					arg_4_0(),
				arg_2_0
			}),
		arg_1_1
	})

return var_0_0
