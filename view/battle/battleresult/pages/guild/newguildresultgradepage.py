local var_0_0 = class("NewGuildResultGradePage", import("..NewBattleResultGradePage"))

def var_0_0.LoadBG(arg_1_0, arg_1_1):
	local var_1_0 = "Victory"

	ResourceMgr.Inst.getAssetAsync("BattleResultItems/" .. var_1_0, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_2_0)
		if arg_1_0.exited or IsNil(arg_2_0):
			if arg_1_1:
				arg_1_1()

			return

		Object.Instantiate(arg_2_0, arg_1_0.bgTr).transform.SetAsFirstSibling()

		if arg_1_1:
			arg_1_1()), False, False)

def var_0_0.LoadGrade(arg_3_0, arg_3_1):
	local var_3_0 = "battlescore/grade_label_clear"

	LoadImageSpriteAsync(var_3_0, arg_3_0.gradeTxt, True)

	if arg_3_1:
		arg_3_1()

def var_0_0.GetContributionPoint(arg_4_0):
	local var_4_0 = 0
	local var_4_1 = pg.guildset.guild_damage_resource.key_value

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.contextData.drops):
		if iter_4_1.configId == var_4_1:
			var_4_0 = iter_4_1.count

	return var_4_0

def var_0_0.GetGetObjectives(arg_5_0):
	local var_5_0 = {}
	local var_5_1 = i18n("battle_result_total_damage")

	table.insert(var_5_0, {
		text = setColorStr(var_5_1, "#FFFFFFFF"),
		value = setColorStr(arg_5_0.contextData.statistics.specificDamage, COLOR_BLUE)
	})

	local var_5_2 = i18n("battle_result_contribution")

	table.insert(var_5_0, {
		text = setColorStr(var_5_2, "#FFFFFFFF"),
		value = setColorStr(arg_5_0.GetContributionPoint(), COLOR_YELLOW)
	})

	return var_5_0

return var_0_0
