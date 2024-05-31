ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleMainFleetCharacterFactory = singletonClass("BattleMainFleetCharacterFactory", var_0_0.Battle.BattlePlayerCharacterFactory)
var_0_0.Battle.BattleMainFleetCharacterFactory.__name = "BattleMainFleetCharacterFactory"

local var_0_1 = var_0_0.Battle.BattleMainFleetCharacterFactory

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0.ARROW_BAR_NAME = "EnemyArrowContainer/MainArrow"
end

function var_0_1.MakeCharacter(arg_2_0)
	return var_0_0.Battle.BattleMainFleetCharacter.New()
end

function var_0_1.MakeModel(arg_3_0, arg_3_1, arg_3_2)
	local function var_3_0(arg_4_0)
		arg_3_1:AddModel(arg_4_0)

		local var_4_0 = arg_3_0:GetSceneMediator()

		arg_3_1:CameraOrthogonal(var_0_0.Battle.BattleCameraUtil.GetInstance():GetCamera())
		var_4_0:AddPlayerCharacter(arg_3_1)
		arg_3_0:MakeUIComponentContainer(arg_3_1)
		arg_3_0:MakeFXContainer(arg_3_1)
		arg_3_0:MakePopNumPool(arg_3_1)
		arg_3_0:MakeBloodBar(arg_3_1)
		arg_3_0:MakeWaveFX(arg_3_1)
		arg_3_0:MakeSmokeFX(arg_3_1)
		arg_3_0:MakeArrowBar(arg_3_1)
	end

	arg_3_0:GetCharacterPool():InstCharacter(arg_3_1:GetModleID(), function(arg_5_0)
		var_3_0(arg_5_0)
	end)
end
