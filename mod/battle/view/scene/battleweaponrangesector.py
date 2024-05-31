ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleWeaponRangeSector = class("BattleWeaponRangeSector")
var_0_0.Battle.BattleWeaponRangeSector.__name = "BattleWeaponRangeSector"

local var_0_1 = var_0_0.Battle.BattleWeaponRangeSector

def var_0_1.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1

	setActive(arg_1_0._tf, True)
	arg_1_0.initSector()

def var_0_1.ConfigHost(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._host = arg_2_1
	arg_2_0._weapon = arg_2_2

	arg_2_0.updateSector(arg_2_0._weapon)

def var_0_1.initSector(arg_3_0):
	arg_3_0._minRange = arg_3_0._tf.Find("minSector")
	arg_3_0._minSector = arg_3_0._minRange.Find("sector").GetComponent(typeof(Renderer)).material
	arg_3_0._maxRange = arg_3_0._tf.Find("maxSector")
	arg_3_0._maxSector = arg_3_0._maxRange.Find("sector").GetComponent(typeof(Renderer)).material

def var_0_1.updateSector(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.GetAttackAngle()
	local var_4_1 = arg_4_1._maxRangeSqr * 2
	local var_4_2 = arg_4_1._minRangeSqr * 2

	arg_4_0._maxRange.localScale = Vector3(var_4_1, 1, var_4_1)
	arg_4_0._minRange.localScale = Vector3(var_4_2, 1, var_4_2)

	arg_4_0._maxSector.SetInt("_Angle", var_4_0)
	arg_4_0._minSector.SetInt("_Angle", var_4_0)

def var_0_1.Dispose(arg_5_0):
	Destroy(arg_5_0._tf)

	arg_5_0._host = None
	arg_5_0._weapon = None
