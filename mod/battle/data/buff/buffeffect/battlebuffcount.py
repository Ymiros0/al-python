ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleAttr
local var_0_3 = class("BattleBuffCount", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffCount = var_0_3
var_0_3.__name = "BattleBuffCount"

def var_0_3.Ctor(arg_1_0, arg_1_1):
	var_0_3.super.Ctor(arg_1_0, arg_1_1)

def var_0_3.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._countTarget = var_2_0.countTarget or 1
	arg_2_0._countType = var_2_0.countType
	arg_2_0._weaponType = var_2_0.weaponType
	arg_2_0._index = var_2_0.index
	arg_2_0._maxHPRatio = var_2_0.maxHPRatio or 0
	arg_2_0._casterMaxHPRatio = var_2_0.casterMaxHPRatio or 0
	arg_2_0._clock = arg_2_0._tempData.arg_list.clock
	arg_2_0._interrupt = arg_2_0._tempData.arg_list.interrupt
	arg_2_0._iconType = arg_2_0._tempData.arg_list.iconType or 1
	arg_2_0._gunnerBonus = var_2_0.gunnerBonus

	arg_2_0.ResetCount()

	if arg_2_0._clock:
		arg_2_1.DispatchCastClock(True, arg_2_0, arg_2_0._iconType, arg_2_0._interrupt)

def var_0_3.onRemove(arg_3_0, arg_3_1, arg_3_2):
	if arg_3_0._clock:
		local var_3_0 = arg_3_0._interrupt and arg_3_0._count < arg_3_0._countTarget

		arg_3_1.DispatchCastClock(False, arg_3_0, None, var_3_0)

def var_0_3.onTrigger(arg_4_0, arg_4_1, arg_4_2):
	var_0_3.super.onTrigger(arg_4_0, arg_4_1, arg_4_2)

	arg_4_0._count = arg_4_0._count + 1

	arg_4_0.checkCount(arg_4_1)

def var_0_3.onFire(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if not arg_5_0.equipIndexRequire(arg_5_3.equipIndex):
		return

	arg_5_0._count = arg_5_0._count + 1

	arg_5_0.checkModCount(arg_5_1)

def var_0_3.onUpdate(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	local var_6_0 = arg_6_3.timeStamp

	arg_6_0._count = var_6_0 - (arg_6_0._lastTriggerTime or arg_6_2.GetBuffStartTime())

	if arg_6_0._count >= arg_6_0._countTarget:
		arg_6_0._lastTriggerTime = var_6_0

		arg_6_0.ResetCount()
		arg_6_1.TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_BATTLE_BUFF_COUNT, {
			buffFX = arg_6_0
		})

def var_0_3.onTakeDamage(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	if arg_7_0.damageCheck(arg_7_3):
		local var_7_0 = arg_7_3.damage

		arg_7_0._count = arg_7_0._count + var_7_0

		arg_7_0.checkHPCount(arg_7_1)

def var_0_3.onTakeHealing(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	local var_8_0 = arg_8_3.damage

	arg_8_0._count = arg_8_0._count + var_8_0

	arg_8_0.checkHPCount(arg_8_1)

def var_0_3.onHPRatioUpdate(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	local var_9_0 = math.abs(arg_9_3.validDHP)

	arg_9_0._count = arg_9_0._count + var_9_0

	arg_9_0.checkHPCount(arg_9_1)

def var_0_3.onStack(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	arg_10_0._count = arg_10_2.GetStack()

	arg_10_0.checkCount(arg_10_1)

def var_0_3.onBulletHit(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	if not arg_11_0.equipIndexRequire(arg_11_3.equipIndex):
		return

	arg_11_0._count = arg_11_0._count + arg_11_3.damage

	arg_11_0.checkCount(arg_11_1)

def var_0_3.checkCount(arg_12_0, arg_12_1):
	if arg_12_0._count >= arg_12_0._countTarget:
		arg_12_1.TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_BATTLE_BUFF_COUNT, {
			buffFX = arg_12_0
		})

def var_0_3.checkModCount(arg_13_0, arg_13_1):
	if arg_13_0._count >= arg_13_0.getCount(arg_13_1):
		arg_13_1.TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_BATTLE_BUFF_COUNT, {
			buffFX = arg_13_0
		})

def var_0_3.getCount(arg_14_0, arg_14_1):
	local var_14_0 = arg_14_0._countTarget
	local var_14_1 = var_0_2.GetCurrent(arg_14_1, "barrageCounterMod")

	if arg_14_0._gunnerBonus:
		var_14_0 = math.ceil(var_14_0 / var_14_1)

	return var_14_0

def var_0_3.checkHPCount(arg_15_0, arg_15_1):
	if not arg_15_0._hpCountTarget:
		arg_15_0.calcHPCount(arg_15_1)

	if arg_15_0._count >= arg_15_0._hpCountTarget:
		arg_15_1.TriggerBuff(var_0_0.Battle.BattleConst.BuffEffectType.ON_BATTLE_BUFF_COUNT, {
			buffFX = arg_15_0
		})

def var_0_3.calcHPCount(arg_16_0, arg_16_1):
	local var_16_0, var_16_1 = arg_16_1.GetHP()
	local var_16_2, var_16_3 = arg_16_0._caster.GetHP()

	arg_16_0._hpCountTarget = math.floor(arg_16_0._casterMaxHPRatio * var_16_3 + arg_16_0._maxHPRatio * var_16_1 + arg_16_0._countTarget)

def var_0_3.GetCountType(arg_17_0):
	return arg_17_0._countType

def var_0_3.GetCountProgress(arg_18_0):
	return arg_18_0._count / arg_18_0._countTarget

def var_0_3.ResetCount(arg_19_0):
	arg_19_0._count = 0
