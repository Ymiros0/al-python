ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConst.AircraftUnitType
local var_0_3 = var_0_0.Battle.BattleConst.CharacterUnitType

var_0_0.Battle.BattleElectricArcBulletFactory = singletonClass("BattleElectricArcBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleElectricArcBulletFactory.__name = "BattleElectricArcBulletFactory"

local var_0_4 = var_0_0.Battle.BattleElectricArcBulletFactory

def var_0_4.Ctor(arg_1_0):
	var_0_4.super.Ctor(arg_1_0)

def var_0_4.CreateBullet(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5):
	arg_2_0.PlayFireFX(arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5, None)

	local var_2_0 = arg_2_2.GetDirectHitUnit()

	if var_2_0 == None:
		return

	local var_2_1 = var_2_0.GetUniqueID()
	local var_2_2 = var_2_0.GetUnitType()
	local var_2_3

	if table.contains(var_0_2, var_2_2):
		var_2_3 = var_0_4.GetSceneMediator().GetAircraft(var_2_1)
	elif table.contains(var_0_3, var_2_2):
		var_2_3 = var_0_4.GetSceneMediator().GetCharacter(var_2_1)

	if var_2_3:
		var_2_3.AddFX(arg_2_2.GetTemplate().hit_fx)
		arg_2_0.GetDataProxy().HandleDamage(arg_2_2, var_2_0)

		local var_2_4 = arg_2_2.GetWeapon().GetHost()

		if var_2_4:
			local var_2_5 = arg_2_2.GetWeapon().GetTemplateData().spawn_bound
			local var_2_6 = arg_2_0.GetSceneMediator().GetCharacter(var_2_4.GetUniqueID())

			arg_2_0.GetSceneMediator().AddArcEffect(arg_2_2.GetTemplate().modle_ID, var_2_6, var_2_0, var_2_5)
