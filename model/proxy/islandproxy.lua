local var_0_0 = class("IslandProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0.nodeDic = nil
	arg_1_0.timeStamp = 0
end

function var_0_0.CheckValid(arg_2_0)
	local var_2_0 = pg.TimeMgr.GetInstance()

	return arg_2_0.nodeDic and var_2_0:IsSameDay(arg_2_0.timeStamp, var_2_0:GetServerTime())
end

function var_0_0.GetNodeDic(arg_3_0)
	if arg_3_0:CheckValid() then
		return arg_3_0.nodeDic
	else
		return {}
	end
end

function var_0_0.CheckAndRequest(arg_4_0, arg_4_1)
	local var_4_0 = {}
	local var_4_1 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_ISLAND)

	if var_4_1 and not var_4_1:isEnd() and not arg_4_0:CheckValid() then
		table.insert(var_4_0, function(arg_5_0)
			arg_4_0:sendNotification(GAME.REQUEST_NODE_LIST, {
				act_id = var_4_1.id,
				callback = arg_5_0
			})
		end)
	end

	seriesAsync(var_4_0, arg_4_1)
end

function var_0_0.GetNode(arg_6_0, arg_6_1)
	return arg_6_0.nodeDic[arg_6_1]
end

function var_0_0.GetNodeIds(arg_7_0)
	local var_7_0 = underscore.keys(arg_7_0.nodeDic)

	table.sort(var_7_0)

	return var_7_0
end

return var_0_0
