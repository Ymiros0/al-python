ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = class("BattleSkillFireSupport", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillFireSupport = var_0_3
var_0_3.__name = "BattleSkillFireSupport"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_3.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._weaponID = arg_1_0._tempData.arg_list.weapon_id
	arg_1_0._supportTargetFilter = arg_1_0._tempData.arg_list.supportTarget.targetChoice
	arg_1_0._supportTargetArgList = arg_1_0._tempData.arg_list.supportTarget.arg_list

def var_0_3.DoDataEffect(arg_2_0, arg_2_1, arg_2_2):
	if arg_2_0._weapon == None:
		local var_2_0

		for iter_2_0, iter_2_1 in ipairs(arg_2_0._supportTargetFilter):
			var_2_0 = var_0_0.Battle.BattleTargetChoise[iter_2_1](arg_2_1, arg_2_0._supportTargetArgList, var_2_0)

		local var_2_1 = var_2_0[1]

		arg_2_0._weapon = var_0_0.Battle.BattleDataFunction.CreateWeaponUnit(arg_2_0._weaponID, arg_2_1)

		if BATTLE_DEBUG and (arg_2_0._weapon.GetType() == var_0_2.EquipmentType.INTERCEPT_AIRCRAFT or arg_2_0._weapon.GetType() == var_0_2.EquipmentType.STRIKE_AIRCRAFT):
			arg_2_0._weapon.GetATKAircraftList()

		if var_2_1:
			arg_2_0._weapon.SetStandHost(var_2_1)

		local var_2_2 = {
			weapon = arg_2_0._weapon
		}
		local var_2_3 = var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.CREATE_TEMPORARY_WEAPON, var_2_2)

		arg_2_1.DispatchEvent(var_2_3)

	local function var_2_4()
		arg_2_0._weapon.Clear()

	arg_2_0._weapon.updateMovementInfo()
	arg_2_0._weapon.SingleFire(arg_2_2, arg_2_0._emitter, var_2_4)

def var_0_3.DoDataEffectWithoutTarget(arg_4_0, arg_4_1):
	arg_4_0.DoDataEffect(arg_4_1)

def var_0_3.Clear(arg_5_0):
	var_0_3.super.Clear(arg_5_0)

	if arg_5_0._weapon and not arg_5_0._weapon.GetHost().IsAlive():
		arg_5_0._weapon.Clear()

def var_0_3.Interrupt(arg_6_0):
	var_0_3.super.Interrupt(arg_6_0)

	if arg_6_0._weapon:
		arg_6_0._weapon.Cease()
		arg_6_0._weapon.Clear()

def var_0_3.GetDamageSum(arg_7_0):
	local var_7_0 = 0

	if not arg_7_0._weapon:
		var_7_0 = 0
	elif arg_7_0._weapon.GetType() == var_0_2.EquipmentType.INTERCEPT_AIRCRAFT or arg_7_0._weapon.GetType() == var_0_2.EquipmentType.STRIKE_AIRCRAFT:
		for iter_7_0, iter_7_1 in ipairs(arg_7_0._weapon.GetATKAircraftList()):
			local var_7_1 = iter_7_1.GetWeapon()

			for iter_7_2, iter_7_3 in ipairs(var_7_1):
				var_7_0 = var_7_0 + iter_7_3.GetDamageSUM()
	else
		var_7_0 = arg_7_0._weapon.GetDamageSUM()

	return var_7_0
