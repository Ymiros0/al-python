local var_0_0 = class("WorkBenchCompositeCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.body
	local var_1_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_WORKBENCH)

	if not var_1_1 or var_1_1.isEnd():
		return

	local var_1_2 = var_1_1.id
	local var_1_3 = var_1_0.formulaId
	local var_1_4 = var_1_0.repeats
	local var_1_5 = WorkBenchFormula.New({
		configId = var_1_3
	})

	var_1_5.BuildFromActivity()

	local var_1_6 = var_1_5.GetMaterials()

	if not (function()
		if not var_1_5.IsUnlock():
			return

		local var_2_0 = var_1_5.GetMaxLimit()
		local var_2_1 = var_1_5.GetUsedCount()

		if var_1_4 <= 0:
			return

		if var_2_0 > 0 and var_1_4 > var_2_0 - var_2_1:
			return

		local var_2_2 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

		if not _.all(var_1_6, function(arg_3_0)
			assert(arg_3_0[1] > DROP_TYPE_USE_ACTIVITY_DROP)

			local var_3_0 = arg_3_0[2]

			return arg_3_0[3] * var_1_4 <= var_2_2.getVitemNumber(var_3_0)):
			pg.TipsMgr.GetInstance().ShowTips(i18n("workbench_tips2"))

			return

		return True)():
		return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		cmd = 1,
		activity_id = var_1_2,
		arg1 = var_1_3,
		arg2 = var_1_4,
		arg_list = {}
	}, 11203, function(arg_4_0)
		if arg_4_0.result == 0:
			local var_4_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_VIRTUAL_BAG)

			_.each(var_1_6, function(arg_5_0)
				local var_5_0 = arg_5_0[2]
				local var_5_1 = arg_5_0[3] * var_1_4

				var_4_0.subVitemNumber(var_5_0, var_5_1))
			getProxy(ActivityProxy).updateActivity(var_4_0)

			local var_4_1 = PlayerConst.GetTranAwards(var_1_0, arg_4_0)
			local var_4_2 = getProxy(ActivityProxy).getActivityById(var_1_2)

			var_4_2.AddFormulaUseCount(var_1_3, var_1_4)
			getProxy(ActivityProxy).updateActivity(var_4_2)
			arg_1_0.sendNotification(GAME.WORKBENCH_COMPOSITE_DONE, var_4_1)
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_4_0.result)))

return var_0_0
