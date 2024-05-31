ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst

var_0_0.Battle.BattleFleetBuffBlindAura = class("BattleFleetBuffBlindAura", var_0_0.Battle.BattleFleetBuffEffect)
var_0_0.Battle.BattleFleetBuffBlindAura.__name = "BattleFleetBuffBlindAura"

local var_0_2 = var_0_0.Battle.BattleFleetBuffBlindAura

function var_0_2.Ctor(arg_1_0, arg_1_1)
	var_0_2.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_2.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0._tempData.arg_list.target
	local var_2_1 = arg_2_1:GetIFF()

	local function var_2_2(arg_3_0)
		local var_3_0 = arg_2_0:getTargetList(arg_2_1, var_2_0, arg_2_0._tempData.arg_list)

		for iter_3_0, iter_3_1 in ipairs(arg_3_0) do
			if iter_3_1.Active then
				for iter_3_2, iter_3_3 in ipairs(var_3_0) do
					if iter_3_3:GetUniqueID() == iter_3_1.UID then
						iter_3_3:SetBlindInvisible(true)

						break
					end
				end
			end
		end
	end

	local function var_2_3(arg_4_0)
		if arg_4_0.Active then
			local var_4_0 = arg_2_0:getTargetList(arg_2_1, var_2_0, arg_2_0._tempData.arg_list)

			for iter_4_0, iter_4_1 in ipairs(var_4_0) do
				if iter_4_1:GetUniqueID() == arg_4_0.UID then
					iter_4_1:SetBlindInvisible(false)

					break
				end
			end
		end
	end

	arg_2_0._aura = var_0_0.Battle.BattleDataProxy.GetInstance():SpawnLastingCubeArea(var_0_1.AOEField.SURFACE, var_2_1, Vector3(-55, 0, 55), 180, 70, 0, var_2_2, var_2_3, false)
end

function var_0_2.Clear(arg_5_0)
	arg_5_0._aura:SetActiveFlag(false)

	arg_5_0._aura = nil

	var_0_2.super.Clear(arg_5_0)
end
