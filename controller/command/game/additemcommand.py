local var_0_0 = class("AddItemCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	assert(isa(var_1_0, Drop), "should be an instance of Drop")
	var_1_0.AddItemOperation()
	arg_1_0.UpdateLinkActivity(var_1_0)

def var_0_0.UpdateLinkActivity(arg_2_0, arg_2_1):
	local var_2_0 = getProxy(ActivityProxy)
	local var_2_1 = var_2_0.getActivityByType(ActivityConst.ACTIVITY_TYPE_LINK_COLLECT)

	if var_2_1 and not var_2_1.isEnd():
		local var_2_2 = pg.activity_limit_item_guide.get_id_list_by_activity[var_2_1.id]

		assert(var_2_2, "activity_limit_item_guide not exist activity id. " .. var_2_1.id)

		for iter_2_0, iter_2_1 in ipairs(var_2_2):
			local var_2_3 = pg.activity_limit_item_guide[iter_2_1]

			if arg_2_1.type == var_2_3.type and arg_2_1.id == var_2_3.drop_id:
				local var_2_4 = var_2_1.getKVPList(1, var_2_3.id) + arg_2_1.count

				var_2_1.updateKVPList(1, var_2_3.id, var_2_4)

		var_2_0.updateActivity(var_2_1)

return var_0_0
