local var_0_0 = class("ActivityBossNormalUpdateCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.stageId

	if not var_1_1 then
		return
	end

	local var_1_2 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

	if not var_1_2 or var_1_2:isEnd() then
		return
	end

	local var_1_3 = pg.activity_event_worldboss[var_1_2:getConfig("config_id")]

	if not var_1_3 then
		return
	end

	local var_1_4 = {}

	for iter_1_0, iter_1_1 in pairs(var_1_3.normal_expedition_drop_num or {}) do
		for iter_1_2, iter_1_3 in pairs(iter_1_1[1]) do
			if iter_1_3 == var_1_1 then
				for iter_1_4, iter_1_5 in pairs(iter_1_1[1]) do
					var_1_4[iter_1_5] = true
				end

				break
			end
		end

		if table.getCount(var_1_4) > 0 then
			break
		end
	end

	local var_1_5 = var_1_2.data1KeyValueList
	local var_1_6 = var_1_0.num or -1

	for iter_1_6, iter_1_7 in pairs(var_1_4) do
		if var_1_5[2][iter_1_6] + var_1_6 >= 0 then
			var_1_5[2][iter_1_6] = var_1_5[2][iter_1_6] + var_1_6
		else
			var_1_5[1][iter_1_6] = math.max(var_1_5[1][iter_1_6] + var_1_6, 0)
		end
	end

	var_1_2:AddStage(var_1_1)
	getProxy(ActivityProxy):updateActivity(var_1_2)
end

return var_0_0
