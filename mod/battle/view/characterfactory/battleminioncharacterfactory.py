ys = ys or {}

local var_0_0 = ys
local var_0_1 = singletonClass("BattleMinionCharacterFactory", var_0_0.Battle.BattleCharacterFactory)

var_0_0.Battle.BattleMinionCharacterFactory = var_0_1
var_0_1.__name = "BattleMinionCharacterFactory"

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.MakeCharacter(arg_2_0):
	return var_0_0.Battle.BattleMinionCharacter.New()

def var_0_1.MakeModel(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_1.GetUnitData()

	local function var_3_1(arg_4_0)
		arg_3_1.AddModel(arg_4_0)

		local var_4_0 = arg_3_0.GetSceneMediator()

		arg_3_1.CameraOrthogonal(var_0_0.Battle.BattleCameraUtil.GetInstance().GetCamera())
		var_4_0.AddEnemyCharacter(arg_3_1)
		arg_3_0.MakeUIComponentContainer(arg_3_1)
		arg_3_0.MakeFXContainer(arg_3_1)
		arg_3_0.MakePopNumPool(arg_3_1)
		arg_3_0.MakeBloodBar(arg_3_1)
		arg_3_0.MakeWaveFX(arg_3_1)
		arg_3_0.MakeSmokeFX(arg_3_1)
		arg_3_1.UpdateDiveInvisible(True)
		arg_3_1.UpdateBlindInvisible()

		local var_4_1 = var_3_0.GetTemplate().appear_fx

		for iter_4_0, iter_4_1 in ipairs(var_4_1):
			arg_3_1.AddFX(iter_4_1)

		if arg_3_1.GetUnitData().GetAimBias():
			arg_3_0.MakeAimBiasBar(arg_3_1)

	arg_3_0.GetCharacterPool().InstCharacter(arg_3_1.GetModleID(), function(arg_5_0)
		var_3_1(arg_5_0))

def var_0_1.MakeBloodBar(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.GetUnitData()
	local var_6_1

	if var_6_0.GetIFF() == var_0_0.Battle.BattleConfig.FRIENDLY_CODE:
		var_6_1 = var_0_0.Battle.BattleHPBarManager.HP_BAR_FRIENDLY
	else
		var_6_1 = var_0_0.Battle.BattleHPBarManager.HP_BAR_FOE

	local var_6_2 = arg_6_0.GetHPBarPool().GetHPBar(var_6_1)
	local var_6_3 = var_6_0.GetTemplate().icon_type
	local var_6_4 = findTF(var_6_2, "type")

	if var_6_4:
		SetActive(var_6_4, False)

	arg_6_1.AddHPBar(var_6_2)
	arg_6_1.UpdateHPBarPosition()

def var_0_1.MakeAimBiasBar(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_1._HPBarTf.Find("biasBar")

	arg_7_1.AddAimBiasBar(var_7_0)
	arg_7_1.AddAimBiasFogFX()

def var_0_1.MakeWaveFX(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.GetUnitData().GetTemplate().wave_fx

	if var_8_0 != "":
		arg_8_1.AddWaveFX(var_8_0)

def var_0_1.RemoveCharacter(arg_9_0, arg_9_1):
	var_0_0.Battle.BattleCameraUtil.GetInstance().StartShake(pg.shake_template[var_0_0.Battle.BattleConst.ShakeType.UNIT_DIE])
	var_0_1.super.RemoveCharacter(arg_9_0, arg_9_1)
