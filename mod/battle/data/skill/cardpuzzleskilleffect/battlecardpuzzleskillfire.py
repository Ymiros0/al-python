ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleCardPuzzleFormulas
local var_0_3 = var_0_0.Battle.BattleConst
local var_0_4 = class("BattleCardPuzzleSkillFire", var_0_0.Battle.BattleCardPuzzleSkillEffect)

var_0_0.Battle.BattleCardPuzzleSkillFire = var_0_4
var_0_4.__name = "BattleCardPuzzleSkillFire"

def var_0_4.Ctor(arg_1_0, arg_1_1):
	var_0_4.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._weaponID = arg_1_0._tempData.arg_list.weapon_id
	arg_1_0._emitter = arg_1_0._tempData.arg_list.emitter
	arg_1_0._useSkin = arg_1_0._tempData.arg_list.useSkin
	arg_1_0._enhance = arg_1_0._tempData.arg_list.enhance_formula

def var_0_4.SetWeaponSkin(arg_2_0, arg_2_1):
	arg_2_0._modelID = arg_2_1

def var_0_4.SkillEffectHandler(arg_3_0):
	if arg_3_0._weapon == None:
		arg_3_0._weapon = var_0_0.Battle.BattleDataFunction.CreateWeaponUnit(arg_3_0._weaponID, arg_3_0._caster)

		if arg_3_0._modelID:
			arg_3_0._weapon.SetModelID(arg_3_0._modelID)
		elif arg_3_0._useSkin:
			local var_3_0 = arg_3_0._caster.GetPriorityWeaponSkin()

			if var_3_0:
				arg_3_0._weapon.SetModelID(var_0_1.GetEquipSkin(var_3_0))

		local var_3_1 = {
			weapon = arg_3_0._weapon
		}
		local var_3_2 = var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.CREATE_TEMPORARY_WEAPON, var_3_1)

		arg_3_0._caster.DispatchEvent(var_3_2)

	local function var_3_3()
		arg_3_0._weapon.Clear()
		arg_3_0.Finale()

	if arg_3_0._enhance:
		local var_3_4 = var_0_2.parseFormula(arg_3_0._enhance, arg_3_0.GetCardPuzzleComponent().GetAttrManager())

		arg_3_0._weapon.SetCardPuzzleDamageEnhance(var_3_4)

	arg_3_0._weapon.updateMovementInfo()

	local var_3_5 = arg_3_0.GetTarget()

	if #var_3_5 > 0:
		for iter_3_0, iter_3_1 in ipairs(var_3_5):
			arg_3_0._weapon.SingleFire(iter_3_1, arg_3_0._emitter, var_3_3)
	else
		arg_3_0._weapon.SingleFire(None, arg_3_0._emitter, var_3_3)

def var_0_4.Clear(arg_5_0):
	var_0_4.super.Clear(arg_5_0)

	if arg_5_0._weapon and not arg_5_0._weapon.GetHost().IsAlive():
		arg_5_0._weapon.Clear()

def var_0_4.Interrupt(arg_6_0):
	var_0_4.super.Interrupt(arg_6_0)

	if arg_6_0._weapon:
		arg_6_0._weapon.Cease()
		arg_6_0._weapon.Clear()
