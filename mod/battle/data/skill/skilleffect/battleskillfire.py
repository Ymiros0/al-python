ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = class("BattleSkillFire", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillFire = var_0_3
var_0_3.__name = "BattleSkillFire"

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_3.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._weaponID = arg_1_0._tempData.arg_list.weapon_id
	arg_1_0._emitter = arg_1_0._tempData.arg_list.emitter
	arg_1_0._useSkin = arg_1_0._tempData.arg_list.useSkin
	arg_1_0._equipIndex = arg_1_0._tempData.arg_list.equip_index or -1
	arg_1_0._atkAttrConvert = arg_1_0._tempData.arg_list.attack_attribute_convert

def var_0_3.SetWeaponSkin(arg_2_0, arg_2_1):
	arg_2_0._modelID = arg_2_1

def var_0_3.IsFinaleEffect(arg_3_0):
	return True

def var_0_3.DoDataEffect(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_0._weapon == None:
		arg_4_0._weapon = var_0_0.Battle.BattleDataFunction.CreateWeaponUnit(arg_4_0._weaponID, arg_4_1, None, arg_4_0._equipIndex)

		if BATTLE_DEBUG and (arg_4_0._weapon.GetType() == var_0_2.EquipmentType.INTERCEPT_AIRCRAFT or arg_4_0._weapon.GetType() == var_0_2.EquipmentType.STRIKE_AIRCRAFT):
			arg_4_0._weapon.GetATKAircraftList()
			arg_4_0._weapon.GetDEFAircraftList()

		if arg_4_0._modelID:
			arg_4_0._weapon.SetModelID(arg_4_0._modelID)
		elif arg_4_0._useSkin:
			local var_4_0 = arg_4_1.GetPriorityWeaponSkin()

			if var_4_0:
				arg_4_0._weapon.SetModelID(var_0_1.GetEquipSkin(var_4_0))

		local var_4_1 = {
			weapon = arg_4_0._weapon
		}
		local var_4_2 = var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.CREATE_TEMPORARY_WEAPON, var_4_1)

		arg_4_1.DispatchEvent(var_4_2)

	local function var_4_3()
		arg_4_0._weapon.Clear()

		if arg_4_0._finaleCallback:
			arg_4_0._finaleCallback()

	if arg_4_0._atkAttrConvert:
		arg_4_0._weapon.SetAtkAttrTrasnform(arg_4_0._atkAttrConvert.attr_type, arg_4_0._atkAttrConvert.A, arg_4_0._atkAttrConvert.B)

	arg_4_0._weapon.updateMovementInfo()
	arg_4_0._weapon.SingleFire(arg_4_2, arg_4_0._emitter, var_4_3)

def var_0_3.DoDataEffectWithoutTarget(arg_6_0, arg_6_1):
	arg_6_0.DoDataEffect(arg_6_1)

def var_0_3.Clear(arg_7_0):
	var_0_3.super.Clear(arg_7_0)

	if arg_7_0._weapon and not arg_7_0._weapon.GetHost().IsAlive():
		arg_7_0._weapon.Clear()

def var_0_3.Interrupt(arg_8_0):
	var_0_3.super.Interrupt(arg_8_0)

	if arg_8_0._weapon:
		arg_8_0._weapon.Cease()
		arg_8_0._weapon.Clear()

def var_0_3.GetDamageSum(arg_9_0):
	local var_9_0 = 0

	if not arg_9_0._weapon:
		var_9_0 = 0
	elif arg_9_0._weapon.GetType() == var_0_2.EquipmentType.INTERCEPT_AIRCRAFT or arg_9_0._weapon.GetType() == var_0_2.EquipmentType.STRIKE_AIRCRAFT:
		for iter_9_0, iter_9_1 in ipairs(arg_9_0._weapon.GetATKAircraftList()):
			local var_9_1 = iter_9_1.GetWeapon()

			for iter_9_2, iter_9_3 in ipairs(var_9_1):
				var_9_0 = var_9_0 + iter_9_3.GetDamageSUM()
	else
		var_9_0 = arg_9_0._weapon.GetDamageSUM()

	return var_9_0
