ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = var_0_0.Battle.BattleConst.AircraftUnitType
local var_0_4 = var_0_0.Battle.BattleConst.CharacterUnitType

var_0_0.Battle.BattleShrapnelBulletFactory = singletonClass("BattleShrapnelBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleShrapnelBulletFactory.__name = "BattleShrapnelBulletFactory"

local var_0_5 = var_0_0.Battle.BattleShrapnelBulletFactory

var_0_5.INHERIT_NONE = 0
var_0_5.INHERIT_ANGLE = 1
var_0_5.INHERIT_SPEED_NORMALIZE = 2

def var_0_5.Ctor(arg_1_0):
	var_0_5.super.Ctor(arg_1_0)

def var_0_5.MakeBullet(arg_2_0):
	return var_0_0.Battle.BattleShrapnelBullet.New()

def var_0_5.CreateBullet(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5):
	arg_3_2.SetOutRangeCallback(arg_3_0.OutRangeFunc)

	local var_3_0 = arg_3_0.MakeBullet()

	var_3_0.SetFactory(arg_3_0)
	var_3_0.SetBulletData(arg_3_2)
	arg_3_0.MakeModel(var_3_0, arg_3_3, arg_3_4, arg_3_5)

	if arg_3_4 and arg_3_4 != "":
		arg_3_0.PlayFireFX(arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5, None)

	if not arg_3_2.GetTemplate().extra_param.rangeAA:
		var_0_5.bulletSplit(var_3_0)

	return var_3_0

def var_0_5.onBulletHitFunc(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = var_0_5.GetDataProxy()
	local var_4_1 = arg_4_0.GetBulletData()
	local var_4_2 = var_4_1.GetCurrentState()
	local var_4_3 = var_4_1.GetTemplate()
	local var_4_4 = var_4_3.extra_param.shrapnel

	if var_4_3.extra_param.fragile and arg_4_1:
		var_0_0.Battle.BattleCannonBulletFactory.onBulletHitFunc(arg_4_0, arg_4_1, arg_4_2)

		return

	if var_4_2 == var_4_1.STATE_SPLIT or var_4_2 == var_4_1.STATE_SPIN:
		-- block empty
	elif var_4_2 == var_4_1.STATE_FINAL_SPLIT:
		return
	elif var_4_1.GetPierceCount() > 0:
		var_0_0.Battle.BattleCannonBulletFactory.onBulletHitFunc(arg_4_0, arg_4_1, arg_4_2)

		return

	if arg_4_1 != None and arg_4_2 != None:
		local var_4_5

		if table.contains(var_0_3, arg_4_2):
			var_4_5 = var_0_5.GetSceneMediator().GetAircraft(arg_4_1)
		elif table.contains(var_0_4, arg_4_2):
			var_4_5 = var_0_5.GetSceneMediator().GetCharacter(arg_4_1)

		local var_4_6 = var_4_5.GetUnitData()
		local var_4_7 = var_4_5.AddFX(arg_4_0.GetFXID())

		if var_4_6.GetIFF() == var_4_0.GetFoeCode():
			local var_4_8 = var_4_7.transform
			local var_4_9 = var_4_8.localRotation

			var_4_8.localRotation = Vector3(var_4_9.x, 180, var_4_9.z)

	var_0_0.Battle.PlayBattleSFX(var_4_1.GetHitSFX())

	if var_4_3.extra_param.rangeAA:
		var_0_5.areaSplit(arg_4_0)
	else
		var_0_5.bulletSplit(arg_4_0, True)

def var_0_5.areaSplit(arg_5_0):
	local var_5_0 = var_0_5.GetDataProxy()
	local var_5_1 = arg_5_0.GetBulletData()

	var_5_1.GetWeapon().DoAreaSplit(var_5_1)
	var_5_0.RemoveBulletUnit(var_5_1.GetUniqueID())

def var_0_5.bulletSplit(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0.GetBulletData()
	local var_6_1 = var_0_5.GetDataProxy()
	local var_6_2 = var_6_0.GetTemplate()
	local var_6_3 = var_6_2.extra_param.shrapnel
	local var_6_4 = var_6_0.GetSrcHost()
	local var_6_5 = var_6_0.GetWeapon()

	if var_6_2.extra_param.FXID != None:
		local var_6_6, var_6_7 = var_0_5.GetFXPool().GetFX(var_6_2.extra_param.FXID)

		pg.EffectMgr.GetInstance().PlayBattleEffect(var_6_6, var_6_7.Add(arg_6_0.GetPosition()), True)

	local var_6_8
	local var_6_9 = var_6_0.GetSpeed().x > 0 and 0 or 180

	for iter_6_0, iter_6_1 in ipairs(var_6_3):
		if arg_6_1 != iter_6_1.initialSplit:
			local var_6_10 = iter_6_1.barrage_ID
			local var_6_11 = iter_6_1.bullet_ID
			local var_6_12 = iter_6_1.emitterType or var_0_0.Battle.BattleWeaponUnit.EMITTER_SHOTGUN
			local var_6_13 = iter_6_1.inheritAngle
			local var_6_14 = iter_6_1.reaim
			local var_6_15 = iter_6_1.rotateOffset

			local function var_6_16(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
				local var_7_0 = var_6_1.CreateBulletUnit(var_6_11, var_6_4, var_6_5, Vector3.zero)

				var_7_0.OverrideCorrectedDMG(iter_6_1.damage)
				var_7_0.SetOffsetPriority(arg_7_3)

				if var_6_15:
					local var_7_1 = math.sqrt(arg_7_0 * arg_7_0 + arg_7_1 * arg_7_1)
					local var_7_2 = math.atan2(arg_7_1, arg_7_0)
					local var_7_3 = math.rad(var_6_0.GetYAngle())
					local var_7_4 = var_7_2 + var_7_3
					local var_7_5 = math.abs(math.cos(var_7_3))

					arg_7_0 = var_7_1 * math.cos(var_7_4) * (0.5 + 0.5 * var_7_5)
					arg_7_1 = var_7_1 * math.sin(var_7_4) * (2 - var_7_5)

				var_7_0.SetShiftInfo(arg_7_0, arg_7_1)

				local var_7_6 = var_6_9

				if var_6_13 == var_0_5.INHERIT_ANGLE:
					var_7_6 = var_6_0.GetYAngle()
				elif var_6_13 == var_0_5.INHERIT_SPEED_NORMALIZE:
					var_7_6 = var_6_0.GetCurrentYAngle()

				if var_6_14:
					local var_7_7 = var_0_0.Battle.BattleTargetChoise.TargetHarmNearest(var_6_0)[1]

					if var_7_7 == None:
						var_7_0.SetRotateInfo(None, var_7_6, arg_7_2)
					else
						var_7_0.SetRotateInfo(var_7_7.GetBeenAimedPosition(), var_7_6, arg_7_2)
				else
					var_7_0.SetRotateInfo(None, var_7_6, arg_7_2)

				var_0_5.GetFactoryList()[var_7_0.GetTemplate().type].CreateBullet(arg_6_0.GetTf(), var_7_0, arg_6_0.GetPosition())

			local var_6_17

			local function var_6_18()
				var_6_17.Destroy()
				var_6_0.SplitFinishCount()

				if var_6_0.IsAllSplitFinish():
					var_6_1.RemoveBulletUnit(var_6_0.GetUniqueID())

			var_6_17 = var_0_0.Battle[var_6_12].New(var_6_16, var_6_18, var_6_10)

			var_6_0.CacheChildEimtter(var_6_17)
			var_6_17.Ready()
			var_6_17.Fire(None, var_6_5.GetDirection(), var_0_0.Battle.BattleDataFunction.GetBarrageTmpDataFromID(var_6_10).angle)

	if arg_6_1:
		var_6_0.ChangeShrapnelState(var_0_0.Battle.BattleShrapnelBulletUnit.STATE_FINAL_SPLIT)

def var_0_5.onBulletMissFunc(arg_9_0):
	return

def var_0_5.MakeModel(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4):
	local var_10_0 = arg_10_1.GetBulletData()

	if not arg_10_0.GetBulletPool().InstBullet(arg_10_1.GetModleID(), function(arg_11_0)
		arg_10_1.AddModel(arg_11_0)):
		arg_10_1.AddTempModel(arg_10_0.GetTempGOPool().GetObject())

	arg_10_1.SetSpawn(arg_10_2)
	arg_10_1.SetFXFunc(arg_10_0.onBulletHitFunc, arg_10_0.onBulletMissFunc)
	arg_10_0.GetSceneMediator().AddBullet(arg_10_1)

def var_0_5.OutRangeFunc(arg_12_0):
	if arg_12_0.IsOutRange():
		arg_12_0.ChangeShrapnelState(var_0_0.Battle.BattleShrapnelBulletUnit.STATE_SPIN)
	else
		arg_12_0.ChangeShrapnelState(var_0_0.Battle.BattleShrapnelBulletUnit.STATE_SPLIT)
