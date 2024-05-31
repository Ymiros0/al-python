ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffOverHealingShield = class("BattleBuffOverHealingShield", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffOverHealingShield.__name = "BattleBuffOverHealingShield"

local var_0_1 = var_0_0.Battle.BattleBuffOverHealingShield

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._shieldDuration = arg_2_0._tempData.arg_list.shield_duration
	arg_2_0._shieldRate = arg_2_0._tempData.arg_list.shield_rate
	arg_2_0._shieldLabel = arg_2_0._tempData.arg_list.shield_tag_list or {}
	arg_2_0._shieldList = {}
end

function var_0_1.onOverHealing(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	local var_3_0 = arg_3_3.overHealing
	local var_3_1 = math.ceil(var_3_0 * arg_3_0._shieldRate)

	if var_3_1 > 0 then
		local var_3_2 = pg.TimeMgr.GetInstance():GetCombatTime()

		table.insert(arg_3_0._shieldList, {
			timeStamp = var_3_2,
			value = var_3_1
		})
	end

	arg_3_0:updateLabelTag(arg_3_1)
end

function var_0_1.onUpdate(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = #arg_4_0._shieldList
	local var_4_1 = pg.TimeMgr.GetInstance():GetCombatTime() - arg_4_0._shieldDuration

	while var_4_0 > 0 do
		if var_4_1 >= arg_4_0._shieldList[var_4_0].timeStamp then
			table.remove(arg_4_0._shieldList, var_4_0)
		end

		var_4_0 = var_4_0 - 1
	end

	arg_4_0:updateLabelTag(arg_4_1)
end

function var_0_1.onTakeDamage(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	local var_5_0 = #arg_5_0._shieldList

	if arg_5_0:damageCheck(arg_5_3) and var_5_0 > 0 then
		local var_5_1 = arg_5_3.damage
		local var_5_2 = 0

		while var_5_1 > 0 and var_5_2 < var_5_0 do
			var_5_2 = var_5_2 + 1

			local var_5_3 = arg_5_0._shieldList[var_5_2].value

			if var_5_1 <= var_5_3 then
				arg_5_0._shieldList[var_5_2].value = var_5_3 - var_5_1
				var_5_1 = 0
			else
				var_5_1 = var_5_1 - var_5_3
				arg_5_0._shieldList[var_5_2].value = 0
			end
		end

		arg_5_3.damage = var_5_1

		while var_5_0 > 0 do
			if arg_5_0._shieldList[var_5_0].value <= 0 then
				table.remove(arg_5_0._shieldList, var_5_0)
			end

			var_5_0 = var_5_0 - 1
		end

		arg_5_0:updateLabelTag(arg_5_1)
	end
end

function var_0_1.updateLabelTag(arg_6_0, arg_6_1)
	if #arg_6_0._shieldList <= 0 then
		for iter_6_0, iter_6_1 in ipairs(arg_6_0._shieldLabel) do
			arg_6_1:RemoveLabelTag(iter_6_1)
		end
	elseif not arg_6_1:ContainsLabelTag(arg_6_0._shieldLabel) then
		for iter_6_2, iter_6_3 in ipairs(arg_6_0._shieldLabel) do
			arg_6_1:AddLabelTag(iter_6_3)
		end
	end
end
