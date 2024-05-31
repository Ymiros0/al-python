local var_0_0 = class("PlayerResChangeCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.oldPlayer
	local var_1_2 = var_1_0.newPlayer
	local var_1_3 = false
	local var_1_4 = pg.player_resource.all

	for iter_1_0 = #var_1_4, 1, -1 do
		local var_1_5 = var_1_4[iter_1_0]

		if var_1_1:getResource(var_1_5) ~= var_1_2:getResource(var_1_5) then
			var_1_3 = true

			break
		end
	end

	if var_1_3 then
		arg_1_0:UpdateActivies(var_1_1, var_1_2)
	end
end

function var_0_0.UpdateActivies(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.activityProxy = arg_2_0.activityProxy or getProxy(ActivityProxy)

	local var_2_0 = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.activityProxy:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PT_RANK)) do
		local var_2_1 = iter_2_1:getConfig("config_id")

		assert(var_2_1)

		var_2_0[var_2_1] = var_2_0[var_2_1] or arg_2_2:getResource(var_2_1) - arg_2_1:getResource(var_2_1)

		var_0_0.UpdateActivity(iter_2_1, var_2_0[var_2_1])
	end

	for iter_2_2, iter_2_3 in ipairs(arg_2_0.activityProxy:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_BOSS_RANK)) do
		local var_2_2 = iter_2_3:getConfig("config_id")

		assert(var_2_2)

		var_2_0[var_2_2] = var_2_0[var_2_2] or arg_2_2:getResource(var_2_2) - arg_2_1:getResource(var_2_2)

		var_0_0.UpdateActivity(iter_2_3, var_2_0[var_2_2])
	end

	for iter_2_4, iter_2_5 in ipairs(arg_2_0.activityProxy:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PT_CRUSING)) do
		local var_2_3 = pg.battlepass_event_pt[iter_2_5.id].pt

		var_2_0[var_2_3] = var_2_0[var_2_3] or arg_2_2:getResource(var_2_3) - arg_2_1:getResource(var_2_3)

		var_0_0.UpdateActivity(iter_2_5, var_2_0[var_2_3])
	end

	for iter_2_6, iter_2_7 in ipairs(arg_2_0.activityProxy:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_RETURN_AWARD)) do
		local var_2_4 = pg.activity_template_headhunting[iter_2_7.id]

		assert(var_2_4)

		local var_2_5 = var_2_4.pt

		var_2_0[var_2_5] = var_2_0[var_2_5] or arg_2_2:getResource(var_2_5) - arg_2_1:getResource(var_2_5)

		var_0_0.UpdateActivity(iter_2_7, var_2_0[var_2_5])
	end

	for iter_2_8, iter_2_9 in ipairs(arg_2_0.activityProxy:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PIZZA_PT)) do
		local var_2_6 = iter_2_9:getDataConfig("pt")

		assert(var_2_6)

		var_2_0[var_2_6] = var_2_0[var_2_6] or arg_2_2:getResource(var_2_6) - arg_2_1:getResource(var_2_6)

		var_0_0.UpdateActivity(iter_2_9, var_2_0[var_2_6])
	end

	for iter_2_10, iter_2_11 in ipairs(arg_2_0.activityProxy:getActivitiesByType(ActivityConst.ACTIVITY_TYPE_PT_BUFF)) do
		local var_2_7 = iter_2_11:getDataConfig("pt")

		if var_2_7 > 0 then
			assert(var_2_7)

			var_2_0[var_2_7] = var_2_0[var_2_7] or arg_2_2:getResource(var_2_7) - arg_2_1:getResource(var_2_7)

			var_0_0.UpdateActivity(iter_2_11, var_2_0[var_2_7])
		end
	end
end

function var_0_0.UpdateActivity(arg_3_0, arg_3_1)
	local var_3_0 = getProxy(ActivityProxy)
	local var_3_1 = arg_3_0:getConfig("type")

	arg_3_0 = var_3_0:getActivityById(arg_3_0.id)

	if var_3_1 == ActivityConst.ACTIVITY_TYPE_PT_RANK then
		if not arg_3_0:isEnd() and arg_3_1 > 0 then
			arg_3_0.data1 = arg_3_0.data1 + arg_3_1

			var_3_0:updateActivity(arg_3_0)
		end
	elseif var_3_1 == ActivityConst.ACTIVITY_TYPE_BOSS_RANK then
		if arg_3_1 ~= 0 then
			arg_3_0.data1 = arg_3_0.data1 + arg_3_1

			var_3_0:updateActivity(arg_3_0)
		end
	elseif var_3_1 == ActivityConst.ACTIVITY_TYPE_PT_CRUSING then
		if not arg_3_0:isEnd() and arg_3_1 ~= 0 then
			arg_3_0.data1 = arg_3_0.data1 + math.abs(arg_3_1)

			var_3_0:updateActivity(arg_3_0)
		end
	elseif var_3_1 == ActivityConst.ACTIVITY_TYPE_RETURN_AWARD then
		local var_3_2 = pg.activity_template_headhunting[arg_3_0.id]

		assert(var_3_2)

		if arg_3_1 ~= 0 then
			arg_3_0.data3 = arg_3_0.data3 + arg_3_1

			var_3_0:updateActivity(arg_3_0)
		end
	elseif var_3_1 == ActivityConst.ACTIVITY_TYPE_PIZZA_PT then
		local var_3_3 = arg_3_0:getDataConfig("pt")

		if arg_3_0:getDataConfig("type") == 1 then
			arg_3_1 = math.max(arg_3_1, 0)
		elseif arg_3_0:getDataConfig("type") == 2 then
			arg_3_1 = math.min(arg_3_1, 0)
		else
			arg_3_1 = 0
		end

		if not arg_3_0:isEnd() and arg_3_1 ~= 0 then
			arg_3_0.data1 = arg_3_0.data1 + math.abs(arg_3_1)

			var_3_0:updateActivity(arg_3_0)
		end
	elseif var_3_1 == ActivityConst.ACTIVITY_TYPE_PT_BUFF and arg_3_0:getDataConfig("pt") > 0 then
		local var_3_4 = arg_3_0:getDataConfig("type") == 2

		if arg_3_0:getDataConfig("type") == 1 then
			arg_3_1 = math.max(arg_3_1, 0)
		elseif var_3_4 then
			arg_3_1 = math.min(arg_3_1, 0)
		else
			arg_3_1 = 0
		end

		if not arg_3_0:isEnd() and (arg_3_1 > 0 or var_3_4) then
			arg_3_0.data1 = arg_3_0.data1 + math.abs(arg_3_1)

			var_3_0:updateActivity(arg_3_0)
		end
	end
end

return var_0_0
