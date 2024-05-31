ys = ys or {}

local var_0_0 = ys
local var_0_1 = singletonClass("BattleNPCCharacterFactory", var_0_0.Battle.BattleEnemyCharacterFactory)

var_0_0.Battle.BattleNPCCharacterFactory = var_0_1
var_0_1.__name = "BattleNPCCharacterFactory"

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0.HP_BAR_NAME = var_0_0.Battle.BattleHPBarManager.HP_BAR_FOE
end

function var_0_1.CreateCharacter(arg_2_0, arg_2_1)
	local var_2_0 = arg_2_1.extraInfo
	local var_2_1 = arg_2_1.unit
	local var_2_2 = arg_2_0:MakeCharacter()

	var_2_2:SetFactory(arg_2_0)
	var_2_2:SetUnitData(var_2_1)

	if var_2_0.modleID then
		var_2_2:SetModleID(var_2_0.modleID)
	end

	if var_2_0.HPColor then
		var_2_2:SetHPColor(var_2_0.HPColor)
	end

	if var_2_0.isUnvisible then
		var_2_2:SetUnvisible()
	end

	arg_2_0:MakeModel(var_2_2)

	return var_2_2
end

function var_0_1.MakeModel(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1:GetUnitData()

	local function var_3_1(arg_4_0)
		arg_3_1:AddModel(arg_4_0)

		local var_4_0 = arg_3_0:GetSceneMediator()

		arg_3_1:CameraOrthogonal(var_0_0.Battle.BattleCameraUtil.GetInstance():GetCamera())
		var_4_0:AddEnemyCharacter(arg_3_1)
		arg_3_0:MakeUIComponentContainer(arg_3_1)
		arg_3_0:MakeFXContainer(arg_3_1)
		arg_3_0:MakePopNumPool(arg_3_1)
		arg_3_0:MakeBloodBar(arg_3_1)
		arg_3_0:MakeWaveFX(arg_3_1)
		arg_3_0:MakeSmokeFX(arg_3_1)
		arg_3_0:MakeArrowBar(arg_3_1)

		local var_4_1 = var_3_0:GetTemplate().appear_fx

		for iter_4_0, iter_4_1 in ipairs(var_4_1) do
			arg_3_1:AddFX(iter_4_1)
		end

		arg_3_1:MakeVisible()
	end

	arg_3_0:GetCharacterPool():InstCharacter(arg_3_1:GetModleID(), function(arg_5_0)
		var_3_1(arg_5_0)
	end)
end

function var_0_1.MakeCharacter(arg_6_0)
	return var_0_0.Battle.BattleNPCCharacter.New()
end

function var_0_1.MakeBloodBar(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_0:GetHPBarPool():GetHPBar(arg_7_0.HP_BAR_NAME)
	local var_7_1 = var_7_0.transform
	local var_7_2 = arg_7_1:GetHPColor()

	if var_7_2 then
		var_7_1:Find("blood"):GetComponent(typeof(Image)).color = var_7_2
	end

	arg_7_1:AddHPBar(var_7_0)
	arg_7_1:UpdateHPBarPosition()
end
