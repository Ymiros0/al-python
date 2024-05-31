﻿local var_0_0 = class("BattleContributionResultLayer", import(".BattleActivityBossResultLayer"))

function var_0_0.setActId(arg_1_0, arg_1_1)
	arg_1_0._actID = arg_1_1

	local var_1_0 = pg.activity_template[arg_1_1]

	arg_1_0._resourceID = pg.activity_event_worldboss[var_1_0.config_id].damage_resource
end

function var_0_0.didEnter(arg_2_0)
	var_0_0.super.didEnter(arg_2_0)
	arg_2_0:setPoint()
end

function var_0_0.setPoint(arg_3_0)
	arg_3_0._contributionPoint = 0

	for iter_3_0, iter_3_1 in ipairs(arg_3_0.contextData.drops) do
		if iter_3_1.configId == arg_3_0._resourceID then
			arg_3_0._contributionPoint = iter_3_1.count
		end
	end
end

function var_0_0.setGradeLabel(arg_4_0)
	local var_4_0 = arg_4_0:findTF("grade/Xyz/bg13")
	local var_4_1 = arg_4_0:findTF("grade/Xyz/bg14")

	setActive(var_4_0, false)

	local var_4_2 = "battlescore/grade_label_clear"

	LoadImageSpriteAsync(var_4_2, var_4_1, false)
end

function var_0_0.rankAnimaFinish(arg_5_0)
	setActive(arg_5_0._conditionBGNormal, false)
	setActive(arg_5_0._conditionBGContribute, true)
	arg_5_0:setCondition(i18n("battle_result_total_damage"), arg_5_0.contextData.statistics.specificDamage, COLOR_BLUE)
	arg_5_0:setCondition(i18n("battle_result_contribution"), arg_5_0._contributionPoint, COLOR_YELLOW)

	local var_5_0 = LeanTween.delayedCall(1, System.Action(function()
		arg_5_0._stateFlag = var_0_0.STATE_REPORTED

		SetActive(arg_5_0:findTF("jieuan01/tips", arg_5_0._bg), true)
	end))

	table.insert(arg_5_0._delayLeanList, var_5_0.id)

	arg_5_0._stateFlag = var_0_0.STATE_REPORT
end

function var_0_0.setCondition(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
	local var_7_0 = cloneTplTo(arg_7_0._conditionContributeTpl, arg_7_0._conditionContainer)

	setActive(var_7_0, false)

	local var_7_1

	var_7_0:Find("text"):GetComponent(typeof(Text)).text = setColorStr(arg_7_1, "#FFFFFFFF")
	var_7_0:Find("value"):GetComponent(typeof(Text)).text = setColorStr(arg_7_2, arg_7_3)

	local var_7_2 = arg_7_0._conditionContainer.childCount - 1

	if var_7_2 > 0 then
		local var_7_3 = LeanTween.delayedCall(var_0_0.CONDITIONS_FREQUENCE * var_7_2, System.Action(function()
			setActive(var_7_0, true)
		end))

		table.insert(arg_7_0._delayLeanList, var_7_3.id)
	else
		setActive(var_7_0, true)
	end
end

return var_0_0
