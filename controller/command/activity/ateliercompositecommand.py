local var_0_0 = class("AtelierCompositeCommand", pm.SimpleCommand)

def var_0_0.SerialAsyncUnitl(arg_1_0, arg_1_1, arg_1_2):
	local var_1_0 = 0
	local var_1_1

	local function var_1_2()
		var_1_0 = var_1_0 + 1

		if var_1_0 <= arg_1_1:
			arg_1_0(var_1_0, var_1_2)
		else
			existCall(arg_1_2)

	var_1_2()

def var_0_0.execute(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.body
	local var_3_1 = var_3_0.formulaId
	local var_3_2 = var_3_0.items
	local var_3_3 = var_3_0.repeats
	local var_3_4 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

	assert(var_3_4)
	pg.ConnectionMgr.GetInstance().Send(26053, {
		act_id = var_3_4.id,
		recipe_id = var_3_1,
		items = var_3_2,
		times = var_3_3
	}, 26054, function(arg_4_0)
		if arg_4_0.result == 0:
			var_3_4 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

			local var_4_0 = var_3_4.GetItems()

			_.each(var_3_2, function(arg_5_0)
				if not var_4_0[arg_5_0.value]:
					return

				var_4_0[arg_5_0.value].count = var_4_0[arg_5_0.value].count - var_3_3

				if var_4_0[arg_5_0.value].count <= 0:
					var_4_0[arg_5_0.value] = None)
			var_3_4.AddFormulaUseCount(var_3_1, var_3_3)
			getProxy(ActivityProxy).updateActivity(var_3_4)

			local var_4_1 = PlayerConst.addTranDrop(arg_4_0.award_list)

			arg_3_0.sendNotification(GAME.COMPOSITE_ATELIER_RECIPE_DONE, var_4_1)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_4_0.result)))

return var_0_0
