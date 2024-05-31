ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleEvent
local var_0_4 = class("BattleSkillCLSArea", var_0_0.Battle.BattleSkillEffect)

var_0_0.Battle.BattleSkillCLSArea = var_0_4
var_0_4.__name = "BattleSkillCLSArea"
var_0_4.TYPE_BULLET = 1
var_0_4.TYPE_AIRCRAFT = 2
var_0_4.TYPE_MINION = 3

def var_0_4.Ctor(arg_1_0, arg_1_1):
	var_0_4.super.Ctor(arg_1_0, arg_1_1, lv)

	arg_1_0._range = arg_1_0._tempData.arg_list.range
	arg_1_0._width = arg_1_0._tempData.arg_list.width
	arg_1_0._height = arg_1_0._tempData.arg_list.height
	arg_1_0._minRange = arg_1_0._tempData.arg_list.minRange or 0
	arg_1_0._angle = arg_1_0._tempData.arg_list.angle
	arg_1_0._lifeTime = arg_1_0._tempData.arg_list.life_time
	arg_1_0._fx = arg_1_0._tempData.arg_list.effect
	arg_1_0._moveType = arg_1_0._tempData.arg_list.move_type
	arg_1_0._speed = arg_1_0._tempData.arg_list.speed_x
	arg_1_0._finaleFX = arg_1_0._tempData.arg_list.finale_effect
	arg_1_0._delayCLS = arg_1_0._tempData.arg_list.cld_delay
	arg_1_0._bulletType = arg_1_0._tempData.arg_list.bullet_type_list
	arg_1_0._damageSrcUnitTag = arg_1_0._tempData.arg_list.damage_tag_list
	arg_1_0._damageParamA = arg_1_0._tempData.arg_list.damage_param_a
	arg_1_0._damageParamB = arg_1_0._tempData.arg_list.damage_param_b
	arg_1_0._damageSFX = arg_1_0._tempData.arg_list.damage_sfx or ""
	arg_1_0._damageBuffID = arg_1_0._tempData.arg_list.buff_id
	arg_1_0._damageBuffLV = arg_1_0._tempData.arg_list.buff_lv
	arg_1_0._damageDiveFilter = arg_1_0._tempData.arg_list.diveFilter or {
		2
	}
	arg_1_0._damageDiveDMGRate = arg_1_0._tempData.arg_list.diveDamageRate or {
		1,
		1
	}
	arg_1_0._delayCLSTimerList = {}

def var_0_4.DoDataEffect(arg_2_0, arg_2_1):
	arg_2_0.doCLS(arg_2_1)

def var_0_4.DoDataEffectWithoutTarget(arg_3_0, arg_3_1):
	arg_3_0.doCLS(arg_3_1)

def var_0_4.doCLS(arg_4_0, arg_4_1):
	if arg_4_0._angle:
		arg_4_0.cacheSectorData(arg_4_1)

	local var_4_0 = var_0_0.Battle.BattleDataProxy.GetInstance()

	local function var_4_1(arg_5_0)
		for iter_5_0, iter_5_1 in ipairs(arg_5_0):
			local var_5_0 = iter_5_1.UID
			local var_5_1 = var_4_0.GetBulletList()[iter_5_1.UID]

			if var_5_1.GetExist() and arg_4_0.checkBulletType(var_5_1) and not var_5_1.ImmuneCLS() and not var_5_1.ImmuneBombCLS() and not arg_4_0.isEnterBlind(var_5_1) and not arg_4_0.isOutOfAngle(var_5_1):
				if arg_4_0._delayCLS:
					local var_5_2

					local function var_5_3()
						if var_5_1.GetExist():
							var_4_0.RemoveBulletUnit(var_5_0)

						pg.TimeMgr.GetInstance().RemoveBattleTimer(var_5_2)

						arg_4_0._delayCLSTimerList[var_5_2] = None

					var_5_2 = pg.TimeMgr.GetInstance().AddBattleTimer("clsBullet", -1, arg_4_0._delayCLS, var_5_3, True)
					arg_4_0._delayCLSTimerList[var_5_2] = True
				else
					var_4_0.RemoveBulletUnit(var_5_0)

	local function var_4_2()
		for iter_7_0, iter_7_1 in pairs(arg_4_0._delayCLSTimerList):
			iter_7_0.func()
			pg.TimeMgr.GetInstance().RemoveBattleTimer(iter_7_0)

			arg_4_0._delayCLSTimerList[iter_7_0] = None

		arg_4_0._delayCLSTimerList = {}

		if arg_4_0._finaleFX:
			var_4_0.SpawnEffect(arg_4_0._finaleFX, arg_4_0._cldArea.GetPosition(), 1)

	arg_4_0._cldArea = arg_4_0.generateArea(arg_4_1, var_0_1.AOEField.BULLET, var_4_1, var_4_2, arg_4_0._fx)

	if arg_4_0._damageSrcUnitTag:
		local var_4_3 = var_0_0.Battle.BattleTargetChoise.TargetAllHelp(arg_4_1)
		local var_4_4 = var_0_0.Battle.BattleTargetChoise.TargetShipTag(arg_4_1, {
			ship_tag_list = arg_4_0._damageSrcUnitTag
		}, var_4_3)
		local var_4_5 = #var_4_4

		if var_4_5 <= 0:
			return

		local var_4_6 = 0

		for iter_4_0, iter_4_1 in ipairs(var_4_4):
			var_4_6 = var_4_6 + iter_4_1.GetAttrByName("formulaLevel")

		local var_4_7 = math.floor(var_4_6 / var_4_5)
		local var_4_8 = arg_4_0._damageParamA + var_4_7 * arg_4_0._damageParamB

		local function var_4_9(arg_8_0)
			for iter_8_0, iter_8_1 in ipairs(arg_8_0):
				if iter_8_1.Active:
					local var_8_0 = iter_8_1.UID
					local var_8_1 = var_4_0.GetUnitList()[var_8_0]
					local var_8_2 = var_8_1.GetCurrentOxyState()
					local var_8_3 = math.floor(arg_4_0._damageDiveDMGRate[var_8_2] * var_4_8)

					var_4_0.HandleDirectDamage(var_8_1, var_4_8)
					var_0_0.Battle.PlayBattleSFX(arg_4_0._damageSFX)

					if arg_4_0._damageBuffID and var_8_1.IsAlive():
						local var_8_4 = var_0_0.Battle.BattleBuffUnit.New(arg_4_0._damageBuffID, None, arg_4_1)

						var_8_4.SetOrb(arg_4_1, arg_4_0._damageBuffLV or 1)
						var_8_1.AddBuff(var_8_4)

		local function var_4_10()
			return

		local function var_4_11()
			return

		arg_4_0.generateArea(arg_4_1, var_0_1.AOEField.SURFACE, var_4_9, var_4_10).SetDiveFilter(arg_4_0._damageDiveFilter)

def var_0_4.generateArea(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4, arg_11_5):
	local function var_11_0()
		return

	local var_11_1 = var_0_0.Battle.BattleDataProxy.GetInstance()
	local var_11_2 = arg_11_1.GetIFF()
	local var_11_3

	if arg_11_0._range:
		var_11_3 = var_11_1.SpawnLastingColumnArea(arg_11_2, var_11_2, arg_11_1.GetPosition(), arg_11_0._range, arg_11_0._lifeTime, arg_11_3, var_11_0, False, arg_11_5, arg_11_4)
	else
		var_11_3 = var_11_1.SpawnLastingCubeArea(arg_11_2, var_11_2, arg_11_1.GetPosition(), arg_11_0._width, arg_11_0._height, arg_11_0._lifeTime, arg_11_3, var_11_0, False, arg_11_5, arg_11_4)

		if var_11_2 == var_0_2.FRIENDLY_CODE:
			var_11_3.SetAnchorPointAlignment(var_11_3.ALIGNMENT_LEFT)
		elif var_11_2 == var_0_2.FOE_CODE:
			var_11_3.SetAnchorPointAlignment(var_11_3.ALIGNMENT_RIGHT)

	local var_11_4 = var_0_0.Battle.BattleAOEMobilizedComponent.New(var_11_3)

	var_11_4.SetReferenceUnit(arg_11_1)

	local var_11_5 = arg_11_0._speed * var_11_2

	var_11_4.ConfigData(arg_11_0._moveType, {
		speedX = var_11_5
	})

	return var_11_3

def var_0_4.cacheSectorData(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_1.GetIFF()
	local var_13_1 = arg_13_0._angle / 2

	arg_13_0._upperEdge = math.deg2Rad * var_13_1
	arg_13_0._lowerEdge = -1 * arg_13_0._upperEdge

	if var_13_0 == var_0_2.FRIENDLY_CODE:
		arg_13_0._normalizeOffset = 0
	elif var_13_0 == var_0_2.FOE_CODE:
		arg_13_0._normalizeOffset = math.pi

	arg_13_0._wholeCircle = math.pi - arg_13_0._normalizeOffset
	arg_13_0._negativeCircle = -math.pi - arg_13_0._normalizeOffset
	arg_13_0._wholeCircleNormalizeOffset = arg_13_0._normalizeOffset - math.pi * 2
	arg_13_0._negativeCircleNormalizeOffset = arg_13_0._normalizeOffset + math.pi * 2

def var_0_4.isOutOfAngle(arg_14_0, arg_14_1):
	if not arg_14_0._angle:
		return False

	local var_14_0 = arg_14_1.GetPosition()
	local var_14_1 = arg_14_0._cldArea.GetPosition()
	local var_14_2 = math.atan2(var_14_0.z - var_14_1.z, var_14_0.x - var_14_1.x)

	if var_14_2 > arg_14_0._wholeCircle:
		var_14_2 = var_14_2 + arg_14_0._wholeCircleNormalizeOffset
	elif var_14_2 < arg_14_0._negativeCircle:
		var_14_2 = var_14_2 + arg_14_0._negativeCircleNormalizeOffset
	else
		var_14_2 = var_14_2 + arg_14_0._normalizeOffset

	if var_14_2 > arg_14_0._lowerEdge and var_14_2 < arg_14_0._upperEdge:
		return False
	else
		return True

def var_0_4.isEnterBlind(arg_15_0, arg_15_1):
	if arg_15_0._minRange == 0:
		return False

	local var_15_0 = arg_15_1.GetPosition()
	local var_15_1 = arg_15_0._cldArea.GetPosition()

	return Vector3.BattleDistance(var_15_1, var_15_0) < arg_15_0._minRange

def var_0_4.checkBulletType(arg_16_0, arg_16_1):
	if not arg_16_0._bulletType:
		return True
	else
		local var_16_0 = arg_16_1.GetType()

		if table.contains(arg_16_0._bulletType, var_16_0):
			return True
		else
			return False
