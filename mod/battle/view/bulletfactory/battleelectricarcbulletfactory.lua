ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConst.AircraftUnitType
local var_0_3 = var_0_0.Battle.BattleConst.CharacterUnitType

var_0_0.Battle.BattleElectricArcBulletFactory = singletonClass("BattleElectricArcBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleElectricArcBulletFactory.__name = "BattleElectricArcBulletFactory"

local var_0_4 = var_0_0.Battle.BattleElectricArcBulletFactory

function var_0_4.Ctor(arg_1_0)
	var_0_4.super.Ctor(arg_1_0)
end

function var_0_4.CreateBullet(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5)
	arg_2_0:PlayFireFX(arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5, nil)

	local var_2_0 = arg_2_2:GetDirectHitUnit()

	if var_2_0 == nil then
		return
	end

	local var_2_1 = var_2_0:GetUniqueID()
	local var_2_2 = var_2_0:GetUnitType()
	local var_2_3

	if table.contains(var_0_2, var_2_2) then
		var_2_3 = var_0_4.GetSceneMediator():GetAircraft(var_2_1)
	elseif table.contains(var_0_3, var_2_2) then
		var_2_3 = var_0_4.GetSceneMediator():GetCharacter(var_2_1)
	end

	if var_2_3 then
		var_2_3:AddFX(arg_2_2:GetTemplate().hit_fx)
		arg_2_0:GetDataProxy():HandleDamage(arg_2_2, var_2_0)

		local var_2_4 = arg_2_2:GetWeapon():GetHost()

		if var_2_4 then
			local var_2_5 = arg_2_2:GetWeapon():GetTemplateData().spawn_bound
			local var_2_6 = arg_2_0:GetSceneMediator():GetCharacter(var_2_4:GetUniqueID())

			arg_2_0:GetSceneMediator():AddArcEffect(arg_2_2:GetTemplate().modle_ID, var_2_6, var_2_0, var_2_5)
		end
	end
end
