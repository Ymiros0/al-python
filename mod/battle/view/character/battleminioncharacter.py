ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattleMinionCharacter = class("BattleMinionCharacter", var_0_0.Battle.BattleCharacter)
var_0_0.Battle.BattleMinionCharacter.__name = "BattleMinionCharacter"

local var_0_4 = var_0_0.Battle.BattleMinionCharacter

def var_0_4.Ctor(arg_1_0):
	var_0_4.super.Ctor(arg_1_0)

	arg_1_0._preCastBound = False

def var_0_4.RegisterWeaponListener(arg_2_0, arg_2_1):
	var_0_4.super.RegisterWeaponListener(arg_2_0, arg_2_1)
	arg_2_1.RegisterEventListener(arg_2_0, var_0_3.WEAPON_PRE_CAST, arg_2_0.onWeaponPreCast)
	arg_2_1.RegisterEventListener(arg_2_0, var_0_3.WEAPON_PRE_CAST_FINISH, arg_2_0.onWeaponPrecastFinish)

def var_0_4.UnregisterWeaponListener(arg_3_0, arg_3_1):
	var_0_4.super.UnregisterWeaponListener(arg_3_0, arg_3_1)
	arg_3_1.UnregisterEventListener(arg_3_0, var_0_3.WEAPON_PRE_CAST)
	arg_3_1.UnregisterEventListener(arg_3_0, var_0_3.WEAPON_PRE_CAST_FINISH)

def var_0_4.Update(arg_4_0):
	var_0_4.super.Update(arg_4_0)
	arg_4_0.UpdatePosition()
	arg_4_0.UpdateMatrix()

def var_0_4.updateComponentVisible(arg_5_0):
	if arg_5_0._unitData.GetIFF() != var_0_2.FOE_CODE:
		return

	local var_5_0 = arg_5_0._unitData.GetExposed()
	local var_5_1 = arg_5_0._unitData.GetDiveDetected()
	local var_5_2 = arg_5_0._unitData.GetDiveInvisible()
	local var_5_3 = var_5_0 and (not var_5_2 or not not var_5_1)

	SetActive(arg_5_0._HPBarTf, var_5_3)
	SetActive(arg_5_0._FXAttachPoint, var_5_3)

def var_0_4.updateComponentDiveInvisible(arg_6_0):
	local var_6_0 = arg_6_0._unitData.GetDiveDetected() and arg_6_0._unitData.GetIFF() == var_0_2.FOE_CODE
	local var_6_1 = arg_6_0._unitData.GetDiveInvisible()
	local var_6_2
	local var_6_3 = (var_6_0 or not var_6_1) and True or False

	SetActive(arg_6_0._HPBarTf, var_6_3)
	SetActive(arg_6_0._FXAttachPoint, var_6_3)

def var_0_4.Dispose(arg_7_0):
	arg_7_0.AddShaderColor()
	var_0_4.super.Dispose(arg_7_0)

def var_0_4.GetModleID(arg_8_0):
	return arg_8_0._unitData.GetTemplate().prefab

def var_0_4.onWeaponPreCast(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_1.Data
	local var_9_1 = var_9_0.fx

	arg_9_0.AddFX(var_9_1, True)

	arg_9_0._preCastBound = var_9_0.isBound

def var_0_4.onWeaponPrecastFinish(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1.Data.fx

	arg_10_0.RemoveCacheFX(var_10_0)

	arg_10_0._preCastBound = False

def var_0_4.OnUpdateHP(arg_11_0, arg_11_1):
	var_0_4.super.OnUpdateHP(arg_11_0, arg_11_1)

	if arg_11_1.Data.dHP <= 0:
		arg_11_0.AddBlink(1, 1, 1, 0.1, 0.1, True)

def var_0_4.AddModel(arg_12_0, arg_12_1):
	var_0_4.super.AddModel(arg_12_0, arg_12_1)

	local var_12_0 = arg_12_0._unitData.GetTemplate().hp_bar[2]

	arg_12_0._hpBarOffset = Vector3(0, var_12_0, 0)

def var_0_4.GetSpecificFXScale(arg_13_0):
	return arg_13_0._unitData.GetTemplate().specific_fx_scale

def var_0_4.OnAnimatorTrigger(arg_14_0):
	arg_14_0._unitData.CharacterActionTriggerCallback()

def var_0_4.OnAnimatorEnd(arg_15_0):
	arg_15_0._unitData.CharacterActionEndCallback()

def var_0_4.OnAnimatorStart(arg_16_0):
	arg_16_0._unitData.CharacterActionStartCallback()

def var_0_4.UpdateAimBiasBar(arg_17_0):
	var_0_4.super.UpdateAimBiasBar(arg_17_0)

	if arg_17_0._fogFx:
		local var_17_0 = arg_17_0.GetUnitData().GetAimBias().GetCurrentRate()

		arg_17_0._fogFx.transform.localScale = Vector3(var_17_0, var_17_0, 1)
