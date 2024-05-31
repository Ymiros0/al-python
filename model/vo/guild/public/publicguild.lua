local var_0_0 = class("PublicGuild", import("..base.BaseGuild"))
local var_0_1 = pg.guild_technology_template

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.technologyGroups = {}
	arg_1_0.technologys = {}

	for iter_1_0, iter_1_1 in pairs(var_0_1.get_id_list_by_group) do
		local var_1_0 = GuildTechnologyGroup.New({
			id = iter_1_0
		})

		arg_1_0.technologyGroups[iter_1_0] = var_1_0

		local var_1_1 = PublicGuildTechnology.New(var_1_0)

		arg_1_0.technologys[iter_1_0] = var_1_1
	end

	for iter_1_2, iter_1_3 in ipairs(arg_1_1.technologys or {}) do
		local var_1_2 = var_0_1[iter_1_3.id]

		arg_1_0.technologyGroups[var_1_2.group]:update(iter_1_3)
	end

	arg_1_0.maxDonateCntPreDay = pg.guildset.contribution_task_num.key_value
end

function var_0_0.InitUser(arg_2_0, arg_2_1)
	arg_2_0.donateCount = arg_2_1.donate_count
	arg_2_0.donateTasks = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_1.donate_tasks or {}) do
		local var_2_0 = GuildDonateTask.New({
			id = iter_2_1
		})

		table.insert(arg_2_0.donateTasks, var_2_0)
	end

	for iter_2_2, iter_2_3 in ipairs(arg_2_1.tech_id or {}) do
		local var_2_1 = var_0_1[iter_2_3].group
		local var_2_2 = arg_2_0.technologys[var_2_1]
		local var_2_3 = arg_2_0.technologyGroups[var_2_1]

		var_2_2:Update(iter_2_3, var_2_3)
	end
end

function var_0_0.GetTechnologyGroups(arg_3_0)
	return arg_3_0.technologyGroups
end

function var_0_0.GetDonateTasks(arg_4_0)
	return arg_4_0.donateTasks
end

function var_0_0.GetTechnologys(arg_5_0)
	return arg_5_0.technologys
end

function var_0_0.GetTechnologyById(arg_6_0, arg_6_1)
	return arg_6_0.technologys[arg_6_1]
end

function var_0_0.GetDonateCount(arg_7_0)
	return arg_7_0.donateCount
end

function var_0_0.GetDonateTaskById(arg_8_0, arg_8_1)
	for iter_8_0, iter_8_1 in ipairs(arg_8_0.donateTasks) do
		if iter_8_1.id == arg_8_1 then
			return iter_8_1
		end
	end
end

function var_0_0.HasDonateCnt(arg_9_0)
	return arg_9_0:GetRemainDonateCnt() > 0
end

function var_0_0.UpdateDonateTasks(arg_10_0, arg_10_1)
	arg_10_0.donateTasks = arg_10_1
end

function var_0_0.IncDonateCount(arg_11_0)
	arg_11_0.donateCount = arg_11_0.donateCount + 1
end

function var_0_0.GetRemainDonateCnt(arg_12_0)
	return arg_12_0.maxDonateCntPreDay - arg_12_0.donateCount
end

function var_0_0.ResetDonateCnt(arg_13_0)
	arg_13_0.donateCount = 0
end

return var_0_0
