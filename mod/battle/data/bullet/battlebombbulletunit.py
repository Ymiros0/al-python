ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBulletEvent
local var_0_2 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleBombBulletUnit = class("BattleBombBulletUnit", var_0_0.Battle.BattleBulletUnit)
var_0_0.Battle.BattleBombBulletUnit.__name = "BattleBombBulletUnit"

local var_0_3 = var_0_0.Battle.BattleBombBulletUnit

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_3.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._randomOffset = Vector3.zero

def var_0_3.InitSpeed(arg_2_0):
	if arg_2_0._barrageLowPriority:
		arg_2_0._yAngle = arg_2_0._baseAngle + arg_2_0._barrageAngle
	else
		arg_2_0._yAngle = math.rad2Deg * math.atan2(arg_2_0._explodePos.z - arg_2_0._spawnPos.z, arg_2_0._explodePos.x - arg_2_0._spawnPos.x)

	arg_2_0.calcSpeed()

	arg_2_0.updateSpeed = var_0_3.doNothing

def var_0_3.Update(arg_3_0):
	if arg_3_0._exist:
		var_0_3.super.Update(arg_3_0)

def var_0_3.GetPierceCount(arg_4_0):
	return 1

def var_0_3.IsOutRange(arg_5_0, arg_5_1):
	if not arg_5_0._exist:
		return False

	if arg_5_0._explodeTime and arg_5_1 >= arg_5_0._explodeTime:
		return True

	if arg_5_0._reachDestFlag and not arg_5_0._explodeTime:
		return True
	else
		return False

def var_0_3.OutRange(arg_6_0):
	local var_6_0 = {
		UID = unitUniqueID
	}

	arg_6_0.DispatchEvent(var_0_0.Event.New(var_0_1.EXPLODE, var_6_0))
	var_0_3.super.OutRange(arg_6_0)

def var_0_3.SetSpawnPosition(arg_7_0, arg_7_1):
	var_0_3.super.SetSpawnPosition(arg_7_0, arg_7_1)

	if arg_7_0._barragePriority:
		arg_7_0._explodePos = arg_7_0._explodePos + Vector3(arg_7_0._offsetX, 0, arg_7_0._offsetZ)

		local var_7_0 = Quaternion.Euler(0, arg_7_0._barrageAngle, 0)
		local var_7_1 = pg.Tool.FilterY(arg_7_0._spawnPos)

		arg_7_0._explodePos = var_7_0 * (arg_7_0._explodePos - var_7_1) + var_7_1

	if arg_7_0._fixToRange and Vector3.BattleDistance(arg_7_0._explodePos, arg_7_0._spawnPos) > arg_7_0._range:
		local var_7_2 = pg.Tool.FilterY(arg_7_0._explodePos - arg_7_0._spawnPos)

		arg_7_0._explodePos = Vector3.Normalize(var_7_2) * arg_7_0._range + arg_7_0._spawnPos

	if arg_7_0._convertedVelocity != 0:
		local var_7_3 = pg.Tool.FilterY(arg_7_0._spawnPos)
		local var_7_4 = Vector3.Distance(var_7_3, arg_7_0._explodePos) / arg_7_0._convertedVelocity
		local var_7_5 = arg_7_0._explodePos.y - arg_7_0._spawnPos.y

		arg_7_0._verticalSpeed = arg_7_0.GetTemplate().extra_param.launchVrtSpeed or var_7_5 / var_7_4 - 0.5 * arg_7_0._gravity * var_7_4

def var_0_3.SetExplodePosition(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0.GetTemplate().extra_param

	if var_8_0.targetFixX and var_8_0.targetFixZ:
		arg_8_0._explodePos = Vector3(var_8_0.targetFixX, 0, var_8_0.targetFixZ)
	else
		arg_8_0._explodePos = arg_8_1.Clone()

	if not arg_8_0._barragePriority:
		arg_8_0._explodePos = arg_8_0._explodePos + arg_8_0._randomOffset

	arg_8_0._explodePos.y = var_0_2.BombDetonateHeight

def var_0_3.SetTemplateData(arg_9_0, arg_9_1):
	var_0_3.super.SetTemplateData(arg_9_0, arg_9_1)

	local var_9_0 = arg_9_0.GetTemplate().extra_param

	arg_9_0._barragePriority = var_9_0.barragePriority
	arg_9_0._barrageLowPriority = var_9_0.barrageLowPriority
	arg_9_0._fixToRange = var_9_0.fixToRange

	if var_9_0.barragePriority:
		arg_9_0._randomOffset = Vector3.zero
	else
		local var_9_1 = var_9_0.accuracy
		local var_9_2 = 0

		if var_9_1:
			var_9_2 = arg_9_0.GetAttrByName(var_9_1)

		local var_9_3 = var_9_0.randomOffsetX or 0
		local var_9_4 = var_9_0.randomOffsetZ or 0
		local var_9_5 = math.max(0, var_9_3 - var_9_2)
		local var_9_6 = math.max(0, var_9_4 - var_9_2)
		local var_9_7 = var_9_0.offsetX or 0
		local var_9_8 = var_9_0.offsetZ or 0

		if var_9_5 != 0:
			var_9_5 = var_9_5 * (math.random() - 0.5) + var_9_7

		if var_9_6 != 0:
			var_9_6 = var_9_6 * (math.random() - 0.5) + var_9_8

		local var_9_9 = var_9_0.targetOffsetX or 0
		local var_9_10 = var_9_0.targetOffsetZ or 0

		arg_9_0._randomOffset = Vector3(var_9_5 + var_9_9, 0, var_9_6 + var_9_10)

	if var_9_0.timeToExplode:
		arg_9_0._explodeTime = pg.TimeMgr.GetInstance().GetCombatTime() + var_9_0.timeToExplode

	arg_9_0._gravity = var_9_0.gravity or var_0_0.Battle.BattleConfig.GRAVITY
	arg_9_0._hitInterval = arg_9_1.hit_type.interval or 0.2

def var_0_3.DealDamage(arg_10_0):
	arg_10_0._nextDamageTime = pg.TimeMgr.GetInstance().GetCombatTime() + arg_10_0._hitInterval

def var_0_3.CanDealDamage(arg_11_0):
	if not arg_11_0._nextDamageTime:
		arg_11_0._nextDamageTime = pg.TimeMgr.GetInstance().GetCombatTime() + arg_11_0._tempData.extra_param.alert_duration

		return False
	else
		return arg_11_0._nextDamageTime < pg.TimeMgr.GetInstance().GetCombatTime()

def var_0_3.HideBullet(arg_12_0):
	arg_12_0._position.x = 0
	arg_12_0._position.y = 100
	arg_12_0._position.z = 0

def var_0_3.GetExplodePostion(arg_13_0):
	return arg_13_0._explodePos
