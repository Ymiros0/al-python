ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleDataFunction
local var_0_3 = class("BattleBuffNewWeapon", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffNewWeapon = var_0_3
var_0_3.__name = "BattleBuffNewWeapon"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_3.super.Ctor(arg_1_0, arg_1_1)

def var_0_3.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._weaponID = arg_2_0._tempData.arg_list.weapon_id
	arg_2_0._reverse = arg_2_0._tempData.arg_list.reverse

def var_0_3.onAttach(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_0._reverse:
		arg_3_1.RemoveAutoWeaponByWeaponID(arg_3_0._weaponID)
	elif var_0_2.GetWeaponPropertyDataFromID(arg_3_0._weaponID).type == var_0_1.EquipmentType.FLEET_ANTI_AIR:
		arg_3_1.AddWeapon(arg_3_0._weaponID)
		arg_3_1.GetFleetVO().GetFleetAntiAirWeapon().FlushCrewUnit(arg_3_1)
	else
		arg_3_0._weapon = arg_3_1.AddNewAutoWeapon(arg_3_0._weaponID)

def var_0_3.onRemove(arg_4_0, arg_4_1, arg_4_2):
	if arg_4_0._reverse:
		arg_4_1.AddNewAutoWeapon(arg_4_0._weaponID)
	elif arg_4_0._weapon:
		if var_0_2.GetWeaponPropertyDataFromID(arg_4_0._weaponID).type == var_0_1.EquipmentType.FLEET_ANTI_AIR:
			arg_4_1.RemoveWeapon(arg_4_0._weaponID)
			arg_4_1.RemoveFleetAntiAirWeapon(arg_4_0._weapon)
			arg_4_1.GetFleetVO().GetFleetAntiAirWeapon().FlushCrewUnit(arg_4_1)
		else
			arg_4_0._weapon.Clear()
			arg_4_1.RemoveAutoWeapon(arg_4_0._weapon)

def var_0_3.Dispose(arg_5_0):
	var_0_3.super.Dispose(arg_5_0)

	arg_5_0._weapon = None
