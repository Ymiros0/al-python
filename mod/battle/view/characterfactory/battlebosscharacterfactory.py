ys = ys or {}

local var_0_0 = ys
local var_0_1 = singletonClass("BattleBossCharacterFactory", var_0_0.Battle.BattleEnemyCharacterFactory)

var_0_0.Battle.BattleBossCharacterFactory = var_0_1
var_0_1.__name = "BattleBossCharacterFactory"
var_0_1.BOMB_FX_NAME = "Bossbomb"

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0.HP_BAR_NAME = "BossBarContainer/heroBlood"
	arg_1_0.DUAL_BAR_NAME = {
		"BossBarContainer/heroBlood_ivory",
		"BossBarContainer/heroBlood_ebony"
	}

def var_0_1.CreateCharacter(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_1.unit
	local var_2_1 = arg_2_0.MakeCharacter()

	var_2_1.SetFactory(arg_2_0)
	var_2_1.SetUnitData(var_2_0)
	var_2_1.SetBossData(arg_2_1.bossData)
	arg_2_0.MakeModel(var_2_1)
	arg_2_0.MakeCastClock(var_2_1)
	arg_2_0.MakeBarrierClock(var_2_1)

	return var_2_1

def var_0_1.MakeCharacter(arg_3_0):
	return var_0_0.Battle.BattleBossCharacter.New()

def var_0_1.MakeBloodBar(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.GetSceneMediator()
	local var_4_1 = arg_4_1.GetBossIndex()

	if var_4_1:
		arg_4_1.AddHPBar(var_4_0.InstantiateCharacterComponent(arg_4_0.DUAL_BAR_NAME[var_4_1]))
	else
		arg_4_1.AddHPBar(var_4_0.InstantiateCharacterComponent(arg_4_0.HP_BAR_NAME), True)

def var_0_1.MakeAimBiasBar(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.GetHPBarPool().GetHPBar(var_0_0.Battle.BattleHPBarManager.HP_BAR_FOE).transform

	setActive(var_5_0.Find("bg"), False)
	setActive(var_5_0.Find("blood"), False)
	arg_5_1.AddAimBiasBar(var_5_0)
	arg_5_1.AddAimBiasFogFX()

def var_0_1.RemoveCharacter(arg_6_0, arg_6_1):
	var_0_1.super.RemoveCharacter(arg_6_0, arg_6_1)
