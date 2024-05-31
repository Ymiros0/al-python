ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst

var_0_0.Battle.BattleBulletFactory = singletonClass("BattleBulletFactory")
var_0_0.Battle.BattleBulletFactory.__name = "BattleBulletFactory"

local var_0_2 = var_0_0.Battle.BattleBulletFactory

def var_0_2.Ctor(arg_1_0):
	return

def var_0_2.RecyleTempModel(arg_2_0, arg_2_1):
	arg_2_0._tempGOPool.Recycle(arg_2_1)

def var_0_2.Clear(arg_3_0):
	if arg_3_0._tempGOPool:
		arg_3_0._tempGOPool.Dispose()

		arg_3_0._tempGOPool = None

def var_0_2.CreateBullet(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4, arg_4_5):
	arg_4_2.SetOutRangeCallback(arg_4_0.OutRangeFunc)

	local var_4_0 = arg_4_0.MakeBullet()

	var_4_0.SetFactory(arg_4_0)
	var_4_0.SetBulletData(arg_4_2)
	arg_4_0.MakeModel(var_4_0, arg_4_3, arg_4_4, arg_4_5)

	if arg_4_4 and arg_4_4 != "":
		arg_4_0.PlayFireFX(arg_4_1, arg_4_2, arg_4_3, arg_4_4, arg_4_5, None)

	return var_4_0

def var_0_2.GetSceneMediator(arg_5_0):
	return var_0_0.Battle.BattleState.GetInstance().GetSceneMediator()

def var_0_2.GetDataProxy(arg_6_0):
	return var_0_0.Battle.BattleDataProxy.GetInstance()

def var_0_2.GetFXPool(arg_7_0):
	return var_0_0.Battle.BattleFXPool.GetInstance()

def var_0_2.GetBulletPool(arg_8_0):
	return var_0_0.Battle.BattleResourceManager.GetInstance()

def var_0_2.OutRangeFunc(arg_9_0):
	var_0_2.GetDataProxy().RemoveBulletUnit(arg_9_0.GetUniqueID())

def var_0_2.GetTempGOPool(arg_10_0):
	if arg_10_0._tempGOPool == None:
		local var_10_0 = GameObject("temp_bullet_OBJ")

		SetActive(var_10_0, False)

		local var_10_1 = arg_10_0.GetSceneMediator().GetBulletRoot().transform

		LuaHelper.SetGOParentTF(var_10_0, var_10_1, False)

		arg_10_0._tempGOPool = pg.Pool.New(var_10_1, var_10_0, 1, 15, False, False).InitSize()

	return arg_10_0._tempGOPool

def var_0_2.PlayFireFX(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4, arg_11_5, arg_11_6):
	local var_11_0 = arg_11_2.GetWeaponTempData().effect_move == 1

	if arg_11_4 == "" or arg_11_4 == None:
		if arg_11_6:
			arg_11_6()
	else
		local var_11_1
		local var_11_2

		if var_11_0:
			var_11_1, var_11_2 = arg_11_0.GetFXPool().GetFX(arg_11_4, arg_11_1)
		else
			var_11_1, var_11_2 = arg_11_0.GetFXPool().GetFX(arg_11_4)
			var_11_2 = var_11_2.Add(arg_11_3)

		if arg_11_5 == var_0_1.UnitDir.LEFT:
			local var_11_3 = var_11_1.transform
			local var_11_4 = var_11_3.localEulerAngles

			var_11_4.y = 180
			var_11_3.localEulerAngles = var_11_4

		pg.EffectMgr.GetInstance().PlayBattleEffect(var_11_1, var_11_2, True, arg_11_6, True)

def var_0_2.MakeBullet(arg_12_0):
	return None

def var_0_2.MakeModel(arg_13_0, arg_13_1, arg_13_2):
	return None

def var_0_2.MakeBombPreCastAlter(arg_14_0, arg_14_1, arg_14_2):
	return arg_14_0.MakeModel(arg_14_1, arg_14_2)

def var_0_2.MakeModelAfterBombPreCastAlert(arg_15_0, arg_15_1):
	return None

def var_0_2.MakeTrack(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	arg_16_1.AddTrack(arg_16_2)
	pg.EffectMgr.GetInstance().PlayBattleEffect(arg_16_2, arg_16_3, True)

def var_0_2.RemoveBullet(arg_17_0, arg_17_1):
	arg_17_1.Dispose()

def var_0_2.GetFactoryList():
	if var_0_2._factoryList == None:
		var_0_2._factoryList = {
			[var_0_1.BulletType.CANNON] = var_0_0.Battle.BattleCannonBulletFactory.GetInstance(),
			[var_0_1.BulletType.BOMB] = var_0_0.Battle.BattleBombBulletFactory.GetInstance(),
			[var_0_1.BulletType.TORPEDO] = var_0_0.Battle.BattleTorpedoBulletFactory.GetInstance(),
			[var_0_1.BulletType.DIRECT] = var_0_0.Battle.BattleDirectBulletFactory.GetInstance(),
			[var_0_1.BulletType.SHRAPNEL] = var_0_0.Battle.BattleShrapnelBulletFactory.GetInstance(),
			[var_0_1.BulletType.ANTI_AIR] = var_0_0.Battle.BattleAntiAirBulletFactory.GetInstance(),
			[var_0_1.BulletType.ANTI_SEA] = var_0_0.Battle.BattleAntiSeaBulletFactory.GetInstance(),
			[var_0_1.BulletType.STRAY] = var_0_0.Battle.BattleStrayBulletFactory.GetInstance(),
			[var_0_1.BulletType.EFFECT] = var_0_0.Battle.BattleEffectBulletFactory.GetInstance(),
			[var_0_1.BulletType.BEAM] = var_0_0.Battle.BattleBeamBulletFactory.GetInstance(),
			[var_0_1.BulletType.G_BULLET] = var_0_0.Battle.BattleGravitationBulletFactory.GetInstance(),
			[var_0_1.BulletType.ELECTRIC_ARC] = var_0_0.Battle.BattleElectricArcBulletFactory.GetInstance(),
			[var_0_1.BulletType.SPACE_LASER] = var_0_0.Battle.BattleSpaceLaserFactory.GetInstance(),
			[var_0_1.BulletType.MISSILE] = var_0_0.Battle.BattleMissileFactory.GetInstance(),
			[var_0_1.BulletType.SCALE] = var_0_0.Battle.BattleScaleBulletFactory.GetInstance(),
			[var_0_1.BulletType.TRIGGER_BOMB] = var_0_0.Battle.BattleTriggerBulletFactory.GetInstance(),
			[var_0_1.BulletType.AAMissile] = var_0_0.Battle.BattleAAMissileFactory.GetInstance()
		}

	return var_0_2._factoryList

def var_0_2.DestroyFactory():
	var_0_2._factoryList = None

def var_0_2.NeutralizeBullet():
	var_0_0.Battle.BattleAntiAirBulletFactory.GetInstance().NeutralizeBullet()
	var_0_0.Battle.BattleAntiSeaBulletFactory.GetInstance().NeutralizeBullet()

def var_0_2.GetRandomBone(arg_21_0):
	return arg_21_0[math.floor(math.Random(0, #arg_21_0)) + 1]
