ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleAirFighterCharacterFactory = singletonClass("BattleAirFighterCharacterFactory", var_0_0.Battle.BattleAircraftCharacterFactory)
var_0_0.Battle.BattleAirFighterCharacterFactory.__name = "BattleAirFighterCharacterFactory"

function var_0_0.Battle.BattleAirFighterCharacterFactory.Ctor(arg_1_0)
	var_0_0.Battle.BattleAirFighterCharacterFactory.super.Ctor(arg_1_0)

	arg_1_0.HP_BAR_NAME = var_0_0.Battle.BattleHPBarManager.HP_BAR_FOE
end

function var_0_0.Battle.BattleAirFighterCharacterFactory.MakeCharacter(arg_2_0)
	return var_0_0.Battle.BattleAirFighterCharacter.New()
end

function var_0_0.Battle.BattleAirFighterCharacterFactory.MakeModel(arg_3_0, arg_3_1)
	local function var_3_0(arg_4_0)
		arg_3_1:AddModel(arg_4_0)
		arg_3_1:InitWeapon()

		local var_4_0 = arg_3_0:GetSceneMediator()

		arg_3_1:CameraOrthogonal(var_0_0.Battle.BattleCameraUtil.GetInstance():GetCamera())
		var_4_0:AddAirCraftCharacter(arg_3_1)
		arg_3_0:MakeUIComponentContainer(arg_3_1)
		arg_3_0:MakeFXContainer(arg_3_1)
		arg_3_0:MakePopNumPool(arg_3_1)
		arg_3_0:MakeBloodBar(arg_3_1)
		arg_3_0:MakeShadow(arg_3_1)
	end

	arg_3_0:GetCharacterPool():InstAirCharacter(arg_3_1:GetModleID(), function(arg_5_0)
		var_3_0(arg_5_0)
	end)
end

function var_0_0.Battle.BattleAirFighterCharacterFactory.MakeBloodBar(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_0:GetHPBarPool():GetHPBar(arg_6_0.HP_BAR_NAME)

	arg_6_1:AddHPBar(var_6_0)
	var_6_0:SetActive(false)
	arg_6_1:UpdateHPBarPosition()
end
