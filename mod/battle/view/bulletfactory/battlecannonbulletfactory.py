ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst.UnitType
local var_0_2 = var_0_0.Battle.BattleConst.AircraftUnitType
local var_0_3 = var_0_0.Battle.BattleConst.CharacterUnitType

var_0_0.Battle.BattleCannonBulletFactory = singletonClass("BattleCannonBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleCannonBulletFactory.__name = "BattleCannonBulletFactory"

local var_0_4 = var_0_0.Battle.BattleCannonBulletFactory

def var_0_4.Ctor(arg_1_0):
	var_0_4.super.Ctor(arg_1_0)

def var_0_4.MakeBullet(arg_2_0):
	return var_0_0.Battle.BattleCannonBullet.New()

local var_0_5 = Quaternion.Euler(-90, 0, 0)

def var_0_4.onBulletHitFunc(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = var_0_4.GetDataProxy()
	local var_3_1 = arg_3_0.GetBulletData()
	local var_3_2 = var_3_1.GetTemplate()
	local var_3_3

	if table.contains(var_0_2, arg_3_2):
		var_3_3 = var_0_4.GetSceneMediator().GetAircraft(arg_3_1)
	elif table.contains(var_0_3, arg_3_2):
		var_3_3 = var_0_4.GetSceneMediator().GetCharacter(arg_3_1)

	if not var_3_3:
		return

	local var_3_4 = var_3_3.GetUnitData()
	local var_3_5, var_3_6 = var_3_0.HandleDamage(var_3_1, var_3_4)
	local var_3_7

	if var_3_3.GetGO():
		if var_3_5:
			local var_3_8, var_3_9 = var_0_4.GetFXPool().GetFX(arg_3_0.GetMissFXID())
			local var_3_10 = var_3_3.GetUnitData().GetBoxSize()
			local var_3_11 = math.random(0, 1)

			if var_3_11 == 0:
				var_3_11 = -1

			local var_3_12 = (math.random() - 0.5) * var_3_10.x
			local var_3_13 = Vector3(var_3_12, 0, var_3_10.z * var_3_11).Add(var_3_3.GetPosition())

			pg.EffectMgr.GetInstance().PlayBattleEffect(var_3_8, var_3_13.Add(var_3_9), True)
			var_0_0.Battle.PlayBattleSFX(var_3_1.GetMissSFX())
		else
			var_3_7 = var_3_3.AddFX(arg_3_0.GetFXID())

			var_0_0.Battle.PlayBattleSFX(var_3_1.GetHitSFX())

			local var_3_14 = var_3_4.GetDirection()
			local var_3_15 = arg_3_0.GetPosition() - var_3_3.GetPosition()

			var_3_15.x = var_3_15.x * var_3_14

			local var_3_16 = var_3_7.transform.localPosition
			local var_3_17 = (var_0_5 * var_3_3.GetTf().localRotation).eulerAngles.x

			var_3_15.y = math.cos(math.deg2Rad * var_3_17) * var_3_15.z
			var_3_15.z = 0

			local var_3_18 = var_3_15 / var_3_3.GetInitScale()

			var_3_16.Add(var_3_18)

			var_3_7.transform.localPosition = var_3_16

	if var_3_7 and var_3_4.GetIFF() == var_3_0.GetFoeCode():
		local var_3_19 = var_3_7.transform
		local var_3_20 = var_3_19.localRotation

		var_3_19.localRotation = Vector3(var_3_20.x, 180, var_3_20.z)

	if var_3_1.GetPierceCount() <= 0:
		var_3_0.RemoveBulletUnit(var_3_1.GetUniqueID())

def var_0_4.onBulletMissFunc(arg_4_0):
	local var_4_0 = arg_4_0.GetBulletData()
	local var_4_1 = var_4_0.GetTemplate()
	local var_4_2, var_4_3 = var_0_4.GetFXPool().GetFX(arg_4_0.GetMissFXID())

	pg.EffectMgr.GetInstance().PlayBattleEffect(var_4_2, var_4_3.Add(arg_4_0.GetPosition()), True)
	var_0_0.Battle.PlayBattleSFX(var_4_0.GetMissSFX())

def var_0_4.MakeModel(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	local var_5_0 = arg_5_0.GetDataProxy()
	local var_5_1 = arg_5_1.GetBulletData()

	if not arg_5_0.GetBulletPool().InstBullet(arg_5_1.GetModleID(), function(arg_6_0)
		arg_5_1.AddModel(arg_6_0)):
		arg_5_1.AddTempModel(arg_5_0.GetTempGOPool().GetObject())

	arg_5_1.SetSpawn(arg_5_2)
	arg_5_1.SetFXFunc(arg_5_0.onBulletHitFunc, arg_5_0.onBulletMissFunc)
	arg_5_0.GetSceneMediator().AddBullet(arg_5_1)
