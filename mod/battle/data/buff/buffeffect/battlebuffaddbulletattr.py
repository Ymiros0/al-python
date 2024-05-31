ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffAddBulletAttr = class("BattleBuffAddBulletAttr", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffAddBulletAttr.__name = "BattleBuffAddBulletAttr"

local var_0_1 = var_0_0.Battle.BattleBuffAddBulletAttr

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._attr = arg_2_0._tempData.arg_list.attr
	arg_2_0._number = arg_2_0._tempData.arg_list.number
	arg_2_0._rate = arg_2_0._tempData.arg_list.rate or 10000
	arg_2_0._bulletID = arg_2_0._tempData.arg_list.bulletID
	arg_2_0._weaponIndexList = arg_2_0._tempData.arg_list.index
	arg_2_0._numberBase = arg_2_0._number
	arg_2_0._displacementConvert = arg_2_0._tempData.arg_list.displacement_convert

def var_0_1.onStack(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0._number = arg_3_0._numberBase * arg_3_2._stack

def var_0_1.onBulletCreate(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	if not arg_4_0.equipIndexRequire(arg_4_3.equipIndex):
		return

	arg_4_0.calcBulletAttr(arg_4_3)

def var_0_1.onInternalBulletCreate(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if not arg_5_0.equipIndexRequire(arg_5_3.equipIndex):
		return

	arg_5_0.calcBulletAttr(arg_5_3)

def var_0_1.onManualBulletCreate(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	if not arg_6_0.equipIndexRequire(arg_6_3.equipIndex):
		return

	arg_6_0.calcBulletAttr(arg_6_3)

def var_0_1.onBulletCollide(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	if not arg_7_0.equipIndexRequire(arg_7_3.equipIndex):
		return

	arg_7_0.displacementConvert(arg_7_3)
	arg_7_0.calcBulletAttr(arg_7_3)

def var_0_1.onBombBulletBang(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	if not arg_8_0.equipIndexRequire(arg_8_3.equipIndex):
		return

	arg_8_0.displacementConvert(arg_8_3)
	arg_8_0.calcBulletAttr(arg_8_3)

def var_0_1.onTorpedoBulletBang(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	if not arg_9_0.equipIndexRequire(arg_9_3.equipIndex):
		return

	arg_9_0.displacementConvert(arg_9_3)
	arg_9_0.calcBulletAttr(arg_9_3)

def var_0_1.displacementConvert(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1._bullet.GetCurrentDistance()
	local var_10_1 = arg_10_0._displacementConvert.base
	local var_10_2 = arg_10_0._displacementConvert.rate
	local var_10_3 = arg_10_0._displacementConvert.max

	if var_10_2 > 0:
		arg_10_0._number = math.min(math.max(var_10_0 - var_10_1, 0) * var_10_2, var_10_3)
	elif var_10_2 < 0:
		arg_10_0._number = math.min(math.max(0, var_10_3 + (var_10_0 - var_10_1) * var_10_2), var_10_3)
	elif var_10_2 == 0:
		arg_10_0._number = 0

def var_0_1.calcBulletAttr(arg_11_0, arg_11_1):
	if var_0_0.Battle.BattleFormulas.IsHappen(arg_11_0._rate):
		local var_11_0 = arg_11_1._bullet
		local var_11_1 = var_11_0.GetWeapon().GetEquipmentIndex()
		local var_11_2 = False

		if not arg_11_0._weaponIndexList:
			var_11_2 = True
		elif #arg_11_0._weaponIndexList == 0 and var_11_1 == None:
			var_11_2 = True
		elif table.contains(arg_11_0._weaponIndexList, var_11_1):
			var_11_2 = True

		if var_11_2:
			if arg_11_0._bulletID:
				if var_11_0.GetTemplate().id == arg_11_0._bulletID:
					var_0_0.Battle.BattleAttr.Increase(var_11_0, arg_11_0._attr, arg_11_0._number)
			else
				var_0_0.Battle.BattleAttr.Increase(var_11_0, arg_11_0._attr, arg_11_0._number)
