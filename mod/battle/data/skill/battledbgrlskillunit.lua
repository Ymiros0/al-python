ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleSkillUnit = class("BattleSkillUnit")
var_0_0.Battle.BattleSkillUnit.__name = "BattleSkillUnit"

local var_0_3 = var_0_0.Battle.BattleSkillUnit

function var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0._id = arg_1_1
	arg_1_0._level = arg_1_2
	arg_1_0._tempData = var_0_0.Battle.BattleDataFunction.GetSkillTemplate(arg_1_1, arg_1_2)
	arg_1_0._cd = arg_1_0._tempData.cd
	arg_1_0._effectList = {}
	arg_1_0._lastEffectTarget = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_0._tempData.effect_list) do
		local var_1_0 = iter_1_1.type

		arg_1_0._effectList[iter_1_0] = var_0_0.Battle[var_1_0].New(iter_1_1, arg_1_2)
	end

	arg_1_0._dataProxy = var_0_0.Battle.BattleDataProxy.GetInstance()
end

function var_0_3.GenerateSpell(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	local var_2_0 = var_0_0.Battle.BattleSkillUnit.New(arg_2_0, arg_2_1)

	var_2_0._attachData = arg_2_3

	return var_2_0
end

function var_0_3.GetSkillEffectList(arg_3_0)
	return arg_3_0._effectList
end

function var_0_3.Cast(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = var_0_0.Battle.BattleState.GetInstance():GetUIMediator()

	if arg_4_0._tempData.focus_duration then
		var_4_0:ShowSkillPainting(arg_4_1, arg_4_0._tempData)
	end

	if arg_4_0._tempData.painting == 1 then
		if arg_4_2 then
			arg_4_1:DispatchSkillFloat(arg_4_2:getSkills()[1]:getConfig("name"), arg_4_2:getPainting())
		else
			arg_4_1:DispatchSkillFloat(arg_4_0._tempData.name)
		end
	elseif type(arg_4_0._tempData.painting) == "string" then
		arg_4_1:DispatchSkillFloat(arg_4_0._tempData.name, nil, arg_4_0._tempData.painting)
	end

	local var_4_1 = type(arg_4_0._tempData.castCV)

	if var_4_1 == "string" then
		arg_4_1:DispatchVoice(arg_4_0._tempData.castCV)
	elseif var_4_1 == "table" then
		local var_4_2, var_4_3, var_4_4 = ShipWordHelper.GetWordAndCV(arg_4_0._tempData.castCV.skinID, arg_4_0._tempData.castCV.key)

		pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_4_3)
	end

	local var_4_5 = arg_4_0._attachData

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._effectList) do
		local var_4_6 = iter_4_1:GetTarget(arg_4_1, arg_4_0)

		arg_4_0._lastEffectTarget = var_4_6

		iter_4_1:SetCommander(arg_4_2)
		iter_4_1:Effect(arg_4_1, var_4_6, var_4_5)
	end

	local var_4_7 = arg_4_0._tempData.aniEffect

	if var_4_7 and var_4_7 ~= "" then
		local var_4_8 = {
			effect = var_4_7.effect,
			time = var_4_7.time,
			offset = var_4_7.offset,
			posFun = var_4_7.posFun
		}

		arg_4_1:DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.ADD_EFFECT, var_4_8))
	end
end

function var_0_3.SetTarget(arg_5_0, arg_5_1)
	arg_5_0._lastEffectTarget = arg_5_1
end

function var_0_3.Interrupt(arg_6_0)
	for iter_6_0, iter_6_1 in ipairs(arg_6_0._effectList) do
		iter_6_1:Interrupt()
	end
end

function var_0_3.Clear(arg_7_0)
	for iter_7_0, iter_7_1 in ipairs(arg_7_0._effectList) do
		iter_7_1:Clear()
	end
end

function var_0_3.GetDamageSum(arg_8_0)
	local var_8_0 = 0

	for iter_8_0, iter_8_1 in ipairs(arg_8_0._effectList) do
		var_8_0 = iter_8_1:GetDamageSum() + var_8_0
	end

	return var_8_0
end

function var_0_3.IsFireSkill(arg_9_0, arg_9_1)
	local var_9_0 = false
	local var_9_1 = var_0_0.Battle.BattleDataFunction.GetSkillTemplate(arg_9_0, arg_9_1)

	for iter_9_0, iter_9_1 in ipairs(var_9_1.effect_list) do
		if iter_9_1.type == var_0_0.Battle.BattleSkillFire.__name or iter_9_1.type == var_0_0.Battle.BattleSkillFireSupport.__name then
			var_9_0 = true

			break
		end
	end

	return var_9_0
end
