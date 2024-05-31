ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffRecordShield = class("BattleBuffRecordShield", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffRecordShield.__name = "BattleBuffRecordShield"

local var_0_1 = var_0_0.Battle.BattleBuffRecordShield

var_0_1.MODE_RECORD = "record"
var_0_1.MODE_SHIELD = "shield"

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.GetEffectAttachData(arg_2_0):
	return arg_2_0._shieldValue

def var_0_1.SetArgs(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = arg_3_0._tempData.arg_list

	arg_3_0._damageAttrRequire = var_3_0.damageAttr
	arg_3_0._damageSrcTagRequire = var_3_0.srcTag
	arg_3_0._convertRate = var_3_0.convertRate
	arg_3_0._shieldDuration = var_3_0.shield_duration
	arg_3_0._recordDuration = var_3_0.record_duration
	arg_3_0._exhaustRemove = var_3_0.exhaust_remove
	arg_3_0._shieldValue = 0
	arg_3_0._recordDamage = 0
	arg_3_0._shieldStartTimeStamp = 0
	arg_3_0._recordStartTimeStamp = 0
	arg_3_0._unit = arg_3_1
	arg_3_0._fxName = var_3_0.effect
	arg_3_0._effectIndex = "BattleBuffRecordShield" .. arg_3_2.GetID()

	arg_3_0.switchMode(var_0_1.MODE_RECORD)

def var_0_1.onUpdate(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = pg.TimeMgr.GetInstance().GetCombatTime()

	if arg_4_0._buffMode == var_0_1.MODE_SHIELD:
		if arg_4_0._shieldDuration and var_4_0 - arg_4_0._shieldStartTimeStamp > arg_4_0._shieldDuration or arg_4_0._shieldValue <= 0:
			arg_4_0.handleShieldExhaust(arg_4_2)
	elif arg_4_0._buffMode == var_0_1.MODE_RECORD and arg_4_0._recordDuration and var_4_0 - arg_4_0._recordStartTimeStamp > arg_4_0._recordDuration:
		arg_4_0.switchMode(var_0_1.MODE_SHIELD)

def var_0_1.handleShieldExhaust(arg_5_0, arg_5_1):
	if arg_5_0._exhaustRemove:
		arg_5_1.SetToCancel()
	else
		arg_5_0.switchMode(var_0_1.MODE_RECORD)

def var_0_1.switchMode(arg_6_0, arg_6_1):
	arg_6_0._buffMode = arg_6_1

	local var_6_0 = pg.TimeMgr.GetInstance().GetCombatTime()

	if arg_6_1 == var_0_1.MODE_SHIELD:
		arg_6_0._shieldStartTimeStamp = var_6_0
		arg_6_0._shieldValue = arg_6_0.calcNumber()
		arg_6_0.onTakeDamage = var_0_1.__shieldTakeDamage

		local var_6_1 = {
			index = arg_6_0._effectIndex,
			effect = arg_6_0._fxName
		}

		arg_6_0._unit.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.ADD_EFFECT, var_6_1))
	elif arg_6_1 == var_0_1.MODE_RECORD:
		arg_6_0._recordStartTimeStamp = var_6_0
		arg_6_0._recordDamage = 0
		arg_6_0._shieldValue = 0
		arg_6_0.onTakeDamage = var_0_1.__recordDamage

		arg_6_0._unit.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.CANCEL_EFFECT, {
			index = arg_6_0._effectIndex
		}))

def var_0_1.__shieldTakeDamage(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	if arg_7_0.damageCheck(arg_7_3):
		local var_7_0 = arg_7_3.damage

		arg_7_0._shieldValue = arg_7_0._shieldValue - var_7_0

		if arg_7_0._shieldValue > 0:
			arg_7_3.damage = 0
		else
			arg_7_3.damage = -arg_7_0._shieldValue

			arg_7_0.handleShieldExhaust(arg_7_2)

def var_0_1.__recordDamage(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	if not arg_8_0.damageCheck(arg_8_3):
		return

	if not arg_8_0.DamageSourceRequire(arg_8_3.damageSrc):
		return

	arg_8_0._recordDamage = arg_8_0._recordDamage + arg_8_3.damage

	if not arg_8_0._recordDuration and arg_8_0.calcNumber() >= 1:
		arg_8_0.switchMode(var_0_1.MODE_SHIELD)

def var_0_1.calcNumber(arg_9_0):
	return (math.max(0, math.floor(arg_9_0._recordDamage * arg_9_0._convertRate)))

def var_0_1.Clear(arg_10_0):
	arg_10_0._unit.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.CANCEL_EFFECT, {
		index = arg_10_0._effectIndex
	}))
	var_0_1.super.Clear(arg_10_0)
