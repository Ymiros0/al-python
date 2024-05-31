ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleAttr
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleBuffDOT = class("BattleBuffDOT", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffDOT.__name = "BattleBuffDOT"

local var_0_4 = var_0_0.Battle.BattleBuffDOT

var_0_4.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TYPE_DOT

function var_0_4.Ctor(arg_1_0, arg_1_1)
	var_0_4.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_4.GetEffectType(arg_2_0)
	return var_0_0.Battle.BattleBuffEffect.FX_TYPE_DOT
end

function var_0_4.SetArgs(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0._number = arg_3_0._tempData.arg_list.number or 0
	arg_3_0._numberBase = arg_3_0._number
	arg_3_0._time = arg_3_0._tempData.arg_list.time or 0
	arg_3_0._nextEffectTime = pg.TimeMgr.GetInstance():GetCombatTime() + arg_3_0._time
	arg_3_0._maxHPRatio = arg_3_0._tempData.arg_list.maxHPRatio or 0
	arg_3_0._currentHPRatio = arg_3_0._tempData.arg_list.currentHPRatio or 0
	arg_3_0._minRestHPRatio = arg_3_0._tempData.arg_list.minRestHPRatio or 0
	arg_3_0._randExtraRange = arg_3_0._tempData.arg_list.randExtraRange or 0
	arg_3_0._cloakExpose = arg_3_0._tempData.arg_list.cloakExpose or 0
	arg_3_0._exposeGroup = arg_3_0._tempData.arg_list._exposeGroup or arg_3_2:GetID()
	arg_3_0._level = arg_3_0._level or 0
	arg_3_0._metaDot = arg_3_0._tempData.arg_list.metaDot

	local var_3_0 = 0

	if not arg_3_0._metaDot then
		var_3_0 = var_0_2.CaclulateDOTDuration(arg_3_0._tempData, arg_3_0._orb, arg_3_1)
	end

	arg_3_2:SetOrbDuration(var_3_0)

	if arg_3_0._tempData.arg_list.WorldBossDotDamage then
		local var_3_1 = arg_3_0._tempData.arg_list.WorldBossDotDamage

		arg_3_0._igniteDMG = (var_0_0.Battle.BattleDataProxy.GetInstance():GetInitData()[var_3_1.useGlobalAttr] or pg.bfConsts.NUM0) * (var_3_1.paramA or pg.bfConsts.NUM1)
	elseif arg_3_0._orb then
		arg_3_0._igniteAttr = arg_3_0._tempData.arg_list.attr
		arg_3_0._igniteCoefficient = arg_3_0._tempData.arg_list.k
		arg_3_0._igniteDMG = var_0_2.CalculateIgniteDamage(arg_3_0._orb, arg_3_0._igniteAttr, arg_3_0._igniteCoefficient)
	else
		arg_3_0._igniteDMG = 0
	end

	if arg_3_0._cloakExpose and arg_3_0._cloakExpose > 0 then
		arg_3_1:CloakExpose(arg_3_0._cloakExpose)
	end
end

function var_0_4.onStack(arg_4_0, arg_4_1, arg_4_2)
	return
end

function var_0_4.onUpdate(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	if arg_5_3.timeStamp >= arg_5_0._nextEffectTime then
		local var_5_0 = arg_5_0:CalcNumber(arg_5_1, arg_5_2)
		local var_5_1 = {
			isMiss = false,
			isCri = false,
			isHeal = false
		}
		local var_5_2 = arg_5_1:UpdateHP(-var_5_0, var_5_1)

		var_0_0.Battle.BattleDataProxy.GetInstance():DamageStatistics(nil, arg_5_1:GetAttrByName("id"), -var_5_2)

		if arg_5_1:IsAlive() then
			arg_5_0._nextEffectTime = arg_5_0._nextEffectTime + arg_5_0._time
		end
	end
end

function var_0_4.onRemove(arg_6_0, arg_6_1, arg_6_2)
	local var_6_0 = arg_6_0:CalcNumber(arg_6_1, arg_6_2)
	local var_6_1 = {
		isMiss = false,
		isCri = false,
		isHeal = false
	}
	local var_6_2 = arg_6_1:UpdateHP(-var_6_0, var_6_1)

	var_0_0.Battle.BattleDataProxy.GetInstance():DamageStatistics(nil, arg_6_1:GetAttrByName("id"), -var_6_2)
end

function var_0_4.CalcNumber(arg_7_0, arg_7_1, arg_7_2)
	if arg_7_0._metaDot then
		local var_7_0 = var_0_0.Battle.BattleDataProxy.GetInstance():GetInitData()

		return (var_0_2.CaclulateMetaDotaDamage(var_7_0.bossConfigId, var_7_0.bossLevel))
	else
		local var_7_1 = var_0_2.CaclulateDOTDamageEnhanceRate(arg_7_0._tempData, arg_7_0._orb, arg_7_1)
		local var_7_2, var_7_3 = arg_7_1:GetHP()
		local var_7_4 = var_7_2 * arg_7_0._currentHPRatio + var_7_3 * arg_7_0._maxHPRatio + arg_7_0._number + arg_7_0._igniteDMG

		if arg_7_0._randExtraRange > 0 then
			var_7_4 = var_7_4 + math.random(0, arg_7_0._randExtraRange)
		end

		local var_7_5 = var_7_4 * (1 + var_7_1)

		return math.max(0, math.floor(math.min(var_7_2 - var_7_3 * arg_7_0._minRestHPRatio, var_7_5 * arg_7_2._stack * var_0_1.GetCurrent(arg_7_1, "repressReduce"))))
	end
end

function var_0_4.SetOrb(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
	arg_8_0._orb = arg_8_2
	arg_8_0._level = arg_8_3

	arg_8_1:SetOrbLevel(arg_8_0._level)
end

function var_0_4.UpdateCloakLock(arg_9_0)
	local var_9_0 = arg_9_0:GetBuffList()
	local var_9_1 = 0
	local var_9_2 = {}

	for iter_9_0, iter_9_1 in pairs(var_9_0) do
		for iter_9_2, iter_9_3 in ipairs(iter_9_1._effectList) do
			if iter_9_3:GetEffectType() == var_0_4.FX_TYPE then
				local var_9_3 = iter_9_3._cloakExpose
				local var_9_4 = iter_9_3._exposeGroup
				local var_9_5 = var_9_2[var_9_4] or 0

				if var_9_5 < var_9_3 then
					var_9_1 = var_9_1 + var_9_3 - var_9_5
					var_9_5 = var_9_3
				end

				var_9_2[var_9_4] = var_9_5
			end
		end
	end

	arg_9_0:CloakOnFire(var_9_1)
end
