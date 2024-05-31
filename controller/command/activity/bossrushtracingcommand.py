local var_0_0 = class("BossRushTracingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	if BeginStageCommand.DockOverload():
		return

	local var_1_0 = arg_1_1.body
	local var_1_1 = var_1_0.seriesId
	local var_1_2 = var_1_0.actId

	if not getProxy(ActivityProxy).getActivityById(var_1_2):
		return

	local var_1_3 = var_1_0.mode
	local var_1_4 = BossRushSeriesData.New({
		id = var_1_1,
		actId = var_1_2,
		mode = var_1_3
	})
	local var_1_5 = var_1_4.GetFleetIds()
	local var_1_6 = var_1_0.mode
	local var_1_7 = Clone(var_1_5)
	local var_1_8 = {
		table.remove(var_1_7)
	}

	if var_1_6 == BossRushSeriesData.MODE.SINGLE:
		var_1_7 = {
			table.remove(var_1_7, 1)
		}

	local var_1_9 = getProxy(FleetProxy).getActivityFleets()[var_1_2]
	local var_1_10 = _.map(var_1_7, function(arg_2_0)
		return var_1_9[arg_2_0])
	local var_1_11 = var_1_9[var_1_8[1]]

	if var_1_11.isEmpty():
		table.remove(var_1_8)

	local var_1_12 = (function()
		local var_3_0 = 0
		local var_3_1 = var_1_4.GetType() == BossRushSeriesData.TYPE.EXTRA and SYSTEM_BOSS_RUSH_EX or SYSTEM_BOSS_RUSH
		local var_3_2 = pg.battle_cost_template[var_3_1]
		local var_3_3 = var_1_4.GetOilLimit()
		local var_3_4 = var_3_2.oil_cost > 0

		local function var_3_5(arg_4_0, arg_4_1)
			local var_4_0 = 0

			if var_3_4:
				var_4_0 = arg_4_0.GetCostSum().oil

				if arg_4_1 > 0:
					var_4_0 = math.min(arg_4_1, var_4_0)

			return var_4_0

		local var_3_6 = #var_1_4.GetExpeditionIds()

		if var_1_6 == BossRushSeriesData.MODE.SINGLE:
			var_3_0 = var_3_0 + var_3_5(var_1_10[1], var_3_3[1])
			var_3_0 = var_3_0 + var_3_5(var_1_11, var_3_3[2])
			var_3_0 = var_3_0 * var_3_6
		else
			var_3_0 = var_3_5(var_1_11, var_3_3[2]) * var_3_6

			_.each(var_1_10, function(arg_5_0)
				var_3_0 = var_3_0 + var_3_5(arg_5_0, var_3_3[1]))

		return var_3_0)()
	local var_1_13 = var_1_4.GetOilCost()
	local var_1_14 = var_1_12 + var_1_13

	if var_1_14 > getProxy(PlayerProxy).getRawData().oil:
		if not ItemTipPanel.ShowOilBuyTip(var_1_14):
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		cmd = 1,
		activity_id = var_1_2,
		arg1 = var_1_1,
		arg2 = var_1_6,
		arg_list = var_1_7,
		arg_list2 = var_1_8
	}, 11203, function(arg_6_0)
		if arg_6_0.result == 0:
			getProxy(ActivityProxy).getActivityById(var_1_2).SetSeriesData(var_1_4)

			if var_1_13 > 0:
				local var_6_0 = getProxy(PlayerProxy).getRawData()

				var_6_0.consume({
					oil = var_1_13
				})
				getProxy(PlayerProxy).updatePlayer(var_6_0)

			;(function()
				local var_7_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_EXTRA_BOSSRUSH_RANK)

				if not var_7_0:
					return

				var_7_0.ResetLast()
				getProxy(ActivityProxy).updateActivity(var_7_0))()
			arg_1_0.sendNotification(GAME.BOSSRUSH_TRACE_DONE, var_1_4)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_6_0.result))
			arg_1_0.sendNotification(GAME.BOSSRUSH_TRACE_ERROR, arg_6_0.result))

return var_0_0
