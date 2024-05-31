ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffAura", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffAura = var_0_1
var_0_1.__name = "BattleBuffAura"

local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleConfig

function var_0_1.Ctor(arg_1_0, arg_1_1)
	var_0_1.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0._buffLevel = arg_2_2:GetLv()

	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._auraRange = var_2_0.cld_data.box.range
	arg_2_0._buffID = var_2_0.buff_id
	arg_2_0._friendly = var_2_0.friendly_fire or false

	local var_2_1, var_2_2, var_2_3 = arg_2_0:getAreaCldFunc(arg_2_1)

	arg_2_0._aura = var_0_0.Battle.BattleDataProxy.GetInstance():SpawnLastingColumnArea(var_0_2.AOEField.SURFACE, arg_2_1:GetIFF(), arg_2_1:GetPosition(), arg_2_0._auraRange, 0, var_2_1, var_2_2, arg_2_0._friendly, nil, var_2_3, false)
	arg_2_0._angle = var_2_0.cld_data.angle

	if arg_2_0._angle then
		arg_2_0._aura:SetSectorAngle(arg_2_0._angle, arg_2_1:GetDirection())
	end

	local var_2_4 = var_0_0.Battle.BattleAOEMobilizedComponent.New(arg_2_0._aura)

	var_2_4:SetReferenceUnit(arg_2_1)
	var_2_4:ConfigData(var_2_4.FOLLOW)
end

function var_0_1.getAreaCldFunc(arg_3_0, arg_3_1)
	local function var_3_0(arg_4_0)
		local var_4_0 = arg_3_0:getTargetList(arg_3_1, {
			"TargetEntityUnit"
		})

		for iter_4_0, iter_4_1 in ipairs(arg_4_0) do
			if iter_4_1.Active then
				for iter_4_2, iter_4_3 in ipairs(var_4_0) do
					if iter_4_3:GetUniqueID() == iter_4_1.UID then
						local var_4_1 = var_0_0.Battle.BattleBuffUnit.New(arg_3_0._buffID, arg_3_0._buffLevel, arg_3_0._caster)

						iter_4_3:AddBuff(var_4_1, true)

						break
					end
				end
			end
		end
	end

	local function var_3_1(arg_5_0)
		if arg_5_0.Active then
			local var_5_0 = arg_3_0:getTargetList(arg_3_1, {
				"TargetEntityUnit"
			})

			for iter_5_0, iter_5_1 in ipairs(var_5_0) do
				if iter_5_1:GetUniqueID() == arg_5_0.UID then
					iter_5_1:RemoveBuff(arg_3_0._buffID, true)

					break
				end
			end
		end
	end

	local function var_3_2(arg_6_0)
		if arg_6_0.Active then
			local var_6_0 = arg_3_0:getTargetList(arg_3_1, {
				"TargetEntityUnit"
			})

			for iter_6_0, iter_6_1 in ipairs(var_6_0) do
				if iter_6_1:GetUniqueID() == arg_6_0.UID then
					iter_6_1:RemoveBuff(arg_3_0._buffID, true)

					break
				end
			end
		end
	end

	return var_3_0, var_3_1, var_3_2
end

function var_0_1.Clear(arg_7_0)
	arg_7_0._aura:SetActiveFlag(false)

	arg_7_0._aura = nil

	var_0_1.super.Clear(arg_7_0)
end
