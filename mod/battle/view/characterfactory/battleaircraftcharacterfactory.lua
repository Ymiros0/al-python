ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = singletonClass("BattleAircraftCharacterFactory", var_0_0.Battle.BattleCharacterFactory)

var_0_0.Battle.BattleAircraftCharacterFactory = var_0_2
var_0_2.__name = "BattleAircraftCharacterFactory"
var_0_2.BOMB_FX_NAME = "feijibaozha"

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)
end

function var_0_2.MakeCharacter(arg_2_0)
	return var_0_0.Battle.BattleAircraftCharacter.New()
end

function var_0_2.MakeModel(arg_3_0, arg_3_1)
	local function var_3_0(arg_4_0)
		arg_3_1:AddModel(arg_4_0)
		arg_3_1:InitWeapon()

		local var_4_0 = arg_3_0:GetSceneMediator()

		arg_3_1:CameraOrthogonal(var_0_0.Battle.BattleCameraUtil.GetInstance():GetCamera())
		var_4_0:AddAirCraftCharacter(arg_3_1)
		arg_3_0:MakeUIComponentContainer(arg_3_1)
		arg_3_0:MakeFXContainer(arg_3_1)
		arg_3_0:MakeShadow(arg_3_1)

		if arg_3_1:GetUnitData():GetIFF() == var_0_1.FOE_CODE then
			arg_3_0:MakePopNumPool(arg_3_1)
			arg_3_0:MakeBloodBar(arg_3_1)
		end
	end

	arg_3_0:GetCharacterPool():InstAirCharacter(arg_3_1:GetModleID(), function(arg_5_0)
		var_3_0(arg_5_0)
	end)
end

function var_0_2.MakeBloodBar(arg_6_0, arg_6_1)
	local var_6_0

	if arg_6_1:GetUnitData():IsPlayerAircraft() then
		var_6_0 = arg_6_0:GetHPBarPool():GetHPBar(var_0_0.Battle.BattleHPBarManager.HP_BAR_FRIENDLY)
	else
		var_6_0 = arg_6_0:GetHPBarPool():GetHPBar(var_0_0.Battle.BattleHPBarManager.HP_BAR_FOE)
	end

	arg_6_1:AddHPBar(var_6_0)
	arg_6_1:UpdateHPBarPosition()
end

function var_0_2.SetHPBarWidth(arg_7_0, arg_7_1, arg_7_2)
	local var_7_0 = 40
	local var_7_1 = arg_7_1.transform
	local var_7_2 = var_7_1.rect.height

	var_7_1.sizeDelta = Vector2(var_7_0, var_7_2)

	local var_7_3 = var_7_1:Find("blood").transform
	local var_7_4 = var_7_3.rect.height

	var_7_3.sizeDelta = Vector2(var_7_0 - arg_7_2 or 0, var_7_4)
end

function var_0_2.MakeShadow(arg_8_0, arg_8_1)
	arg_8_1:AddShadow()
	arg_8_1:UpdateShadow()
end
