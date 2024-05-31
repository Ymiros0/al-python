ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffBlindedHorizon", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffBlindedHorizon = var_0_1
var_0_1.__name = "BattleBuffBlindedHorizon"

local var_0_2 = var_0_0.Battle.BattleConst

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._horizonRange = arg_2_0._tempData.arg_list.range

	local var_2_0 = arg_2_1:GetUniqueID()

	local function var_2_1(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0) do
			if iter_3_1.Active then
				local var_3_0 = arg_2_0:getTargetList(arg_2_1, {
					"TargetAllHarm"
				})

				for iter_3_2, iter_3_3 in ipairs(var_3_0) do
					if iter_3_3:GetUniqueID() == iter_3_1.UID then
						iter_3_3:AppendExposed(var_2_0)

						break
					end
				end
			end
		end
	end

	local function var_2_2(arg_4_0)
		if arg_4_0.Active then
			local var_4_0 = arg_2_0:getTargetList(arg_2_1, {
				"TargetAllHarm"
			})

			for iter_4_0, iter_4_1 in ipairs(var_4_0) do
				if iter_4_1:GetUniqueID() == arg_4_0.UID then
					iter_4_1:RemoveExposed(var_2_0)

					break
				end
			end
		end
	end

	local function var_2_3(arg_5_0)
		if arg_5_0.Active then
			local var_5_0 = arg_2_0:getTargetList(arg_2_1, {
				"TargetAllHarm"
			})

			for iter_5_0, iter_5_1 in ipairs(var_5_0) do
				if iter_5_1:GetUniqueID() == arg_5_0.UID then
					iter_5_1:RemoveExposed(var_2_0)

					break
				end
			end
		end
	end

	arg_2_0._aura = var_0_0.Battle.BattleDataProxy.GetInstance():SpawnLastingColumnArea(var_0_2.AOEField.SURFACE, arg_2_1:GetIFF(), arg_2_1:GetPosition(), arg_2_0._horizonRange, 0, var_2_1, var_2_2, false, nil, var_2_3, true)

	local var_2_4 = var_0_0.Battle.BattleAOEMobilizedComponent.New(arg_2_0._aura)

	var_2_4:SetReferenceUnit(arg_2_1)
	var_2_4:ConfigData(var_2_4.FOLLOW)
end

function var_0_1.onAttach(arg_6_0, arg_6_1, arg_6_2)
	var_0_0.Battle.BattleAttr.FlashByBuff(arg_6_1, "blindedHorizon", arg_6_0._horizonRange)

	local var_6_0 = arg_6_1:GetFleetVO()

	if var_6_0 then
		var_6_0:UpdateHorizon()
	end
end

function var_0_1.onRemove(arg_7_0, arg_7_1, arg_7_2)
	var_0_0.Battle.BattleAttr.FlashByBuff(arg_7_1, "blindedHorizon", 0)
end

function var_0_1.Clear(arg_8_0)
	arg_8_0._aura:SetActiveFlag(false)

	arg_8_0._aura = nil

	var_0_1.super.Clear(arg_8_0)
end
