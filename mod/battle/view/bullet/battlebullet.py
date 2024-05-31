ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBulletEvent
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleBullet = class("BattleBullet", var_0_0.Battle.BattleSceneObject)
var_0_0.Battle.BattleBullet.__name = "BattleBullet"

local var_0_4 = var_0_0.Battle.BattleBullet

def var_0_4.Ctor(arg_1_0):
	var_0_4.super.Ctor(arg_1_0)
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0.resMgr = var_0_0.Battle.BattleResourceManager.GetInstance()
	arg_1_0._cacheSpeed = Vector3.zero
	arg_1_0._calcSpeed = Vector3.zero
	arg_1_0._cacheTFPos = Vector3.zero

def var_0_4.Update(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0._bulletData.GetSpeed()

	arg_2_0._calcSpeed.Set(var_2_0.x, var_2_0.y, var_2_0.z)

	local var_2_1 = arg_2_0._bulletData.GetVerticalSpeed()

	if var_2_1 != 0:
		arg_2_0._calcSpeed.y = arg_2_0._calcSpeed.y + var_2_1

	if arg_2_0._cacheSpeed != arg_2_0._calcSpeed:
		if arg_2_0._rotateScript:
			arg_2_0._rotateScript.SetSpeed(arg_2_0._calcSpeed)

		arg_2_0._cacheSpeed.Set(arg_2_0._calcSpeed.x, arg_2_0._calcSpeed.y, arg_2_0._calcSpeed.z)

	if math.abs(arg_2_0._calcSpeed.x) >= 0.01 or math.abs(arg_2_0._calcSpeed.z) >= 0.01 or math.abs(arg_2_0._calcSpeed.y) >= 0.01:
		arg_2_0.UpdatePosition()
	else
		local var_2_2 = arg_2_0.GetPosition()

		if math.abs(arg_2_0._cacheTFPos.x - var_2_2.x) >= 0.1 or math.abs(arg_2_0._cacheTFPos.z - var_2_2.z) >= 0.1 or math.abs(arg_2_0._cacheTFPos.y - var_2_2.y) >= 0.1:
			arg_2_0.UpdatePosition()

def var_0_4.UpdatePosition(arg_3_0):
	local var_3_0 = arg_3_0.GetPosition()

	arg_3_0._tf.localPosition = var_3_0

	arg_3_0._cacheTFPos.Set(var_3_0.x, var_3_0.y, var_3_0.z)

def var_0_4.DoOutRange(arg_4_0):
	arg_4_0._bulletMissFunc(arg_4_0)

def var_0_4.SetBulletData(arg_5_0, arg_5_1):
	arg_5_0._bulletData = arg_5_1

	arg_5_0._bulletData.SetStartTimeStamp(pg.TimeMgr.GetInstance().GetCombatTime())

	arg_5_0._cfgTpl = arg_5_1.GetTemplate()
	arg_5_0._IFF = arg_5_1.GetIFF()

	arg_5_0.AddBulletEvent()

def var_0_4.AddBulletEvent(arg_6_0):
	arg_6_0._bulletData.RegisterEventListener(arg_6_0, var_0_1.HIT, arg_6_0.onBulletHit)
	arg_6_0._bulletData.RegisterEventListener(arg_6_0, var_0_1.INTERCEPTED, arg_6_0.onIntercepted)
	arg_6_0._bulletData.RegisterEventListener(arg_6_0, var_0_1.OUT_RANGE, arg_6_0.onOutRange)

def var_0_4.RemoveBulletEvent(arg_7_0):
	arg_7_0._bulletData.UnregisterEventListener(arg_7_0, var_0_1.HIT)
	arg_7_0._bulletData.UnregisterEventListener(arg_7_0, var_0_1.INTERCEPTED)
	arg_7_0._bulletData.UnregisterEventListener(arg_7_0, var_0_1.OUT_RANGE)

def var_0_4.onBulletHit(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.Data
	local var_8_1 = arg_8_1.Data.UID
	local var_8_2 = arg_8_1.Data.type

	arg_8_0._bulletHitFunc(arg_8_0, var_8_1, var_8_2)

def var_0_4.onIntercepted(arg_9_0):
	local var_9_0, var_9_1 = var_0_0.Battle.BattleFXPool.GetInstance().GetFX(arg_9_0.GetBulletData().GetTemplate().hit_fx)

	pg.EffectMgr.GetInstance().PlayBattleEffect(var_9_0, var_9_1.Add(arg_9_0.GetPosition()), True)

def var_0_4.onOutRange(arg_10_0, arg_10_1):
	arg_10_0.DoOutRange()

def var_0_4.GetBulletData(arg_11_0):
	return arg_11_0._bulletData

def var_0_4.GetPosition(arg_12_0):
	return arg_12_0._bulletData.GetPosition()

def var_0_4.Dispose(arg_13_0):
	if arg_13_0._rotateScript:
		arg_13_0._rotateScript.SetSpeed(Vector3.zero)

	arg_13_0.RemoveBulletEvent()

	if arg_13_0._isTempGO:
		arg_13_0._factory.RecyleTempModel(arg_13_0._go)
	else
		var_0_0.Battle.BattleResourceManager.GetInstance().DestroyOb(arg_13_0._go)

	if arg_13_0._trackFX:
		arg_13_0.resMgr.GetInstance().DestroyOb(arg_13_0._trackFX)

	arg_13_0._skeleton = None
	arg_13_0._go = None
	arg_13_0._tf = None
	arg_13_0._trackFX = None

	var_0_0.EventListener.DetachEventListener(arg_13_0)

def var_0_4.GetModleID(arg_14_0):
	return arg_14_0._bulletData.GetModleID()

def var_0_4.GetFXID(arg_15_0):
	return arg_15_0._cfgTpl.hit_fx

def var_0_4.GetMissFXID(arg_16_0):
	return arg_16_0._cfgTpl.miss_fx

def var_0_4.GetTrackFXID(arg_17_0):
	return arg_17_0._cfgTpl.track_fx

def var_0_4.AddModel(arg_18_0, arg_18_1):
	if arg_18_0._isTempGO and arg_18_0._go == None:
		var_0_0.Battle.BattleResourceManager.GetInstance().DestroyOb(arg_18_1)

		return False
	else
		if arg_18_0._isTempGO:
			LuaHelper.CopyTransformInfoGO(arg_18_1, arg_18_0._go)
			arg_18_0._factory.RecyleTempModel(arg_18_0._go)

			arg_18_0._isTempGO = False

		arg_18_0.SetGO(arg_18_1)
		arg_18_0._bulletData.ActiveCldBox()

		if arg_18_0._bulletData.IsAutoRotate():
			arg_18_0.AddRotateScript()

		local var_18_0 = arg_18_0._tf.Find("bullet")

		if var_18_0 and var_18_0.GetComponent(typeof(SpineAnim)):
			arg_18_0._skeleton = var_18_0.GetComponent("SkeletonAnimation")
			arg_18_0._spineBullet = True

			var_18_0.GetComponent(typeof(SpineAnim)).SetAction("normal", 0, False)

		local var_18_1 = arg_18_0._tf.Find("bullet_random")

		if var_18_1 and var_18_1.GetComponent(typeof(SpineAnim)):
			arg_18_0._skeleton = var_18_1.GetComponent("SkeletonAnimation")
			arg_18_0._spineBullet = True

			local var_18_2 = var_18_1.GetComponent(typeof(SpineAnim))
			local var_18_3 = tostring(math.random(3))

			var_18_2.SetAction(var_18_3, 0, False)

		return True

def var_0_4.SetAnimaSpeed(arg_19_0, arg_19_1):
	if arg_19_0._skeleton:
		arg_19_1 = arg_19_1 or 1
		arg_19_0._skeleton.timeScale = arg_19_1

def var_0_4.AddRotateScript(arg_20_0):
	arg_20_0._rotateScript = arg_20_0.resMgr.GetRotateScript(arg_20_0._go)

def var_0_4.AddTempModel(arg_21_0, arg_21_1):
	arg_21_0._isTempGO = True

	arg_21_0.SetGO(arg_21_1)

	if arg_21_0._bulletData.IsAutoRotate():
		arg_21_0.AddRotateScript()

def var_0_4.AddTrack(arg_22_0, arg_22_1):
	arg_22_0._trackFX = arg_22_1

	LuaHelper.SetGOParentTF(arg_22_1, arg_22_0._tf, False)

def var_0_4.SetSpawn(arg_23_0, arg_23_1):
	local var_23_0, var_23_1 = arg_23_0.getHeightAdjust(arg_23_1)
	local var_23_2 = var_23_0.Clone()

	var_23_2.z = var_23_2.z + var_23_1
	arg_23_0._tf.localPosition = var_23_2

	arg_23_0._bulletData.SetSpawnPosition(var_23_2)

	local var_23_3, var_23_4, var_23_5 = arg_23_0._bulletData.GetRotateInfo()

	if var_23_3:
		local var_23_6

		if arg_23_0._bulletData.GetOffsetPriority():
			var_23_6 = math.rad2Deg * math.atan2(var_23_3.z - var_23_0.z, var_23_3.x - var_23_2.x)
		else
			var_23_6 = math.rad2Deg * math.atan2(var_23_3.z - var_23_0.z - var_23_1, var_23_3.x - var_23_2.x)

		arg_23_0._bulletData.InitSpeed(var_23_6)
	else
		arg_23_0._bulletData.InitSpeed(None)

def var_0_4.getHeightAdjust(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_0._bulletData.GetTemplate().extra_param

	if var_24_0.airdrop:
		local var_24_1 = arg_24_0._bulletData.GetExplodePostion()
		local var_24_2 = 0

		if var_24_0.dropOffset:
			var_24_2 = math.sqrt(math.abs(var_24_0.offsetY * 2 / arg_24_0._bulletData._gravity)) * arg_24_0._bulletData.GetConvertedVelocity()

			if arg_24_0._bulletData.GetHost().GetDirection() < 0:
				var_24_2 = var_24_2 * -1

		return Vector3(var_24_1.x - var_24_2, var_24_0.offsetY or arg_24_1.y, var_24_1.z), 0
	else
		local var_24_3, var_24_4 = arg_24_0._bulletData.GetOffset()
		local var_24_5 = arg_24_1.x + var_24_3
		local var_24_6 = arg_24_1.z + var_24_4

		if arg_24_0._bulletData.IsGravitate():
			return Vector3(var_24_5, arg_24_1.y, var_24_6), 0
		else
			local var_24_7 = 0
			local var_24_8
			local var_24_9 = var_0_2.BulletHeight

			if var_24_9 >= arg_24_1.y:
				var_24_8 = arg_24_1.y
			else
				var_24_8 = var_24_9
				var_24_7 = arg_24_0.GetZExtraOffset(arg_24_1.y)

			return Vector3(var_24_5, var_24_8, var_24_6), var_24_7

def var_0_4.GetZExtraOffset(arg_25_0):
	return var_0_2.HeightOffsetRate * (arg_25_0 - var_0_2.BulletHeight)

def var_0_4.GetFactory(arg_26_0):
	return arg_26_0._factory

def var_0_4.SetFactory(arg_27_0, arg_27_1):
	arg_27_0._factory = arg_27_1

def var_0_4.SetFXFunc(arg_28_0, arg_28_1, arg_28_2):
	arg_28_0._bulletHitFunc = arg_28_1
	arg_28_0._bulletMissFunc = arg_28_2

def var_0_4.Neutrailze(arg_29_0):
	if arg_29_0._bulletMissFunc:
		arg_29_0._bulletMissFunc(arg_29_0)

	SetActive(arg_29_0._go, False)
