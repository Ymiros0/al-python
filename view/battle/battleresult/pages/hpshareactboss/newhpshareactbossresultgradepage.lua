local var_0_0 = class("NewHpShareActBossResultGradePage", import("..activityBoss.NewActivityBossResultGradePage"))

function var_0_0.LoadGrade(arg_1_0, arg_1_1)
	local var_1_0 = "battlescore/grade_label_clear"

	LoadImageSpriteAsync(var_1_0, arg_1_0.gradeTxt, true)

	if arg_1_1 then
		arg_1_1()
	end
end

function var_0_0.GetContributionPoint(arg_2_0)
	local var_2_0 = arg_2_0.contextData
	local var_2_1 = pg.activity_template[var_2_0.actId]
	local var_2_2 = pg.activity_event_worldboss[var_2_1.config_id].damage_resource
	local var_2_3 = 0

	for iter_2_0, iter_2_1 in ipairs(var_2_0.drops) do
		if iter_2_1.configId == var_2_2 then
			var_2_3 = iter_2_1.count
		end
	end

	return var_2_3
end

function var_0_0.GetGetObjectives(arg_3_0)
	local var_3_0 = arg_3_0.contextData
	local var_3_1 = {}
	local var_3_2 = arg_3_0:GetContributionPoint()
	local var_3_3 = i18n("battle_result_total_damage")

	table.insert(var_3_1, {
		text = setColorStr(var_3_3, "#FFFFFFFF"),
		value = setColorStr(var_3_0.statistics.specificDamage, COLOR_BLUE)
	})

	local var_3_4 = i18n("battle_result_contribution")

	table.insert(var_3_1, {
		text = setColorStr(var_3_4, "#FFFFFFFF"),
		value = setColorStr(var_3_2, COLOR_YELLOW)
	})

	return var_3_1
end

return var_0_0
