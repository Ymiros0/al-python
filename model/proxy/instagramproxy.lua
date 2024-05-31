local var_0_0 = class("InstagramProxy", import(".NetProxy"))
local var_0_1 = pg.activity_ins_language
local var_0_2 = pg.activity_ins_npc_template

function var_0_0.register(arg_1_0)
	arg_1_0.caches = {}
	arg_1_0.messages = {}
	arg_1_0.allReply = {}

	local function var_1_0(arg_2_0)
		local var_2_0 = arg_2_0.npc_reply_persist

		if type(arg_2_0.npc_reply_persist) == "string" then
			var_2_0 = {}
		end

		local var_2_1 = ""
		local var_2_2 = pg.TimeMgr.GetInstance():GetServerTime()

		if var_0_1[arg_2_0.message_persist] then
			var_2_1 = var_0_1[arg_2_0.message_persist].value
			var_2_2 = pg.TimeMgr.GetInstance():parseTimeFromConfig(arg_2_0.time_persist)
		end

		return {
			id = arg_2_0.id,
			time = var_2_2,
			text = var_2_1,
			npc_reply = var_2_0
		}
	end

	for iter_1_0, iter_1_1 in ipairs(var_0_2.all) do
		local var_1_1 = var_1_0(var_0_2[iter_1_1])

		arg_1_0.allReply[iter_1_1] = var_1_1
	end

	arg_1_0:on(11700, function(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.ins_message_list) do
			if pg.activity_ins_template[iter_3_1.id].is_active == 1 then
				local var_3_0 = Instagram.New(iter_3_1)

				arg_1_0.messages[var_3_0.id] = var_3_0
			else
				table.insert(arg_1_0.caches, iter_3_1)
			end
		end
	end)
end

function var_0_0.GetAllReply(arg_4_0)
	return arg_4_0.allReply
end

function var_0_0.InitLocalConfigs(arg_5_0)
	if #arg_5_0.caches > 0 then
		for iter_5_0, iter_5_1 in ipairs(arg_5_0.caches) do
			local var_5_0 = Instagram.New(iter_5_1)

			arg_5_0.messages[var_5_0.id] = var_5_0
		end
	end

	arg_5_0.caches = {}
end

function var_0_0.GetMessages(arg_6_0)
	local var_6_0 = {}

	for iter_6_0, iter_6_1 in pairs(arg_6_0.messages) do
		table.insert(var_6_0, iter_6_1)
	end

	return var_6_0
end

function var_0_0.ExistMessage(arg_7_0)
	return table.getCount(arg_7_0.messages) > 0
end

function var_0_0.GetData(arg_8_0)
	return arg_8_0.messages
end

function var_0_0.GetMessageById(arg_9_0, arg_9_1)
	return arg_9_0.messages[arg_9_1]
end

function var_0_0.AddMessage(arg_10_0, arg_10_1)
	arg_10_0.messages[arg_10_1.id] = arg_10_1
end

function var_0_0.UpdateMessage(arg_11_0, arg_11_1)
	if not arg_11_0.messages[arg_11_1.id] then
		arg_11_0:AddMessage(arg_11_1)
	else
		arg_11_0.messages[arg_11_1.id] = arg_11_1
	end
end

function var_0_0.ShouldShowTip(arg_12_0)
	local var_12_0 = arg_12_0:GetMessages()

	return _.any(var_12_0, function(arg_13_0)
		return arg_13_0:ShouldShowTip()
	end)
end

function var_0_0.ExistMsg(arg_14_0)
	return arg_14_0.messages and table.getCount(arg_14_0.messages) > 0 or arg_14_0.caches and #arg_14_0.caches > 0
end

function var_0_0.ExistGroup(arg_15_0, arg_15_1)
	for iter_15_0, iter_15_1 in pairs(arg_15_0.messages) do
		if iter_15_1:getConfig("group_id") == arg_15_1 then
			return true
		end
	end

	return false
end

return var_0_0
