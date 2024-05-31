ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst

var_0_0.Battle.BattleHammerHeadWeaponUnit = class("BattleHammerHeadWeaponUnit", var_0_0.Battle.BattleWeaponUnit)
var_0_0.Battle.BattleHammerHeadWeaponUnit.__name = "BattleHammerHeadWeaponUnit"

local var_0_3 = var_0_0.Battle.BattleHammerHeadWeaponUnit

def var_0_3.Ctor(arg_1_0):
	var_0_3.super.Ctor(arg_1_0)

def var_0_3.DoAttack(arg_2_0, arg_2_1):
	if arg_2_0._tmpData.bullet_ID[1]:
		local var_2_0 = var_0_1.GetBulletTmpDataFromID(arg_2_0._tmpData.bullet_ID[1]).type

		if var_2_0 == var_0_2.BulletType.DIRECT or var_2_0 == var_0_2.BulletType.ANTI_AIR or var_2_0 == var_0_2.BulletType.ANTI_SEA:
			local var_2_1 = arg_2_0.Spawn(arg_2_0._tmpData.bullet_ID[1], arg_2_1)

			var_2_1.SetDirectHitUnit(arg_2_1)
			arg_2_0.DispatchBulletEvent(var_2_1)
		else
			var_0_3.super.DoAttack(arg_2_0, arg_2_1)
			arg_2_0._host.HandleDamageToDeath()

			return

	var_0_0.Battle.PlayBattleSFX(arg_2_0._tmpData.fire_sfx)
	arg_2_0.TriggerBuffOnFire()
	arg_2_0.CheckAndShake()
	arg_2_0._host.HandleDamageToDeath()
