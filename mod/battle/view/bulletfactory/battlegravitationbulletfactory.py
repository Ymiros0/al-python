ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleGravitationBulletFactory = singletonClass("BattleGravitationBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleGravitationBulletFactory.__name = "BattleGravitationBulletFactory"

local var_0_1 = var_0_0.Battle.BattleGravitationBulletFactory

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.MakeBullet(arg_2_0):
	return var_0_0.Battle.BattleTorpedoBullet.New()

def var_0_1.onBulletHitFunc(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = arg_3_0.GetBulletData()

	if var_3_0.GetPierceCount() <= 0:
		return

	local var_3_1 = var_3_0.GetTemplate().hit_type
	local var_3_2 = var_0_1.GetDataProxy()
	local var_3_3 = arg_3_0.GetBulletData()
	local var_3_4 = var_3_3.GetTemplate()

	var_0_0.Battle.PlayBattleSFX(var_3_3.GetHitSFX())

	local var_3_5 = var_3_3.GetDiveFilter()
	local var_3_6 = var_3_3.GetPosition().Clone()
	local var_3_7 = var_3_3.GetTemplate().extra_param
	local var_3_8 = var_3_7.buff_id
	local var_3_9 = var_3_7.buff_level or 1

	local function var_3_10(arg_4_0)
		if var_3_3.CanDealDamage():
			for iter_4_0, iter_4_1 in ipairs(arg_4_0):
				if iter_4_1.Active:
					local var_4_0 = var_0_1.GetSceneMediator().GetCharacter(iter_4_1.UID).GetUnitData()
					local var_4_1 = var_0_0.Battle.BattleBuffUnit.New(var_3_8, var_3_9)

					var_4_0.AddBuff(var_4_1)

					if not var_3_7.noIntervalDMG:
						var_3_2.HandleDamage(var_3_3, var_4_0)

					local var_4_2 = var_3_7.force or 0.1
					local var_4_3 = pg.Tool.FilterY(var_3_6 - var_4_0.GetPosition())

					if var_4_2 > var_4_3.magnitude:
						var_4_0.SetUncontrollableSpeed(var_4_3, 0.001, 1e-06)
					else
						var_4_0.SetUncontrollableSpeed(var_4_3, var_4_2, 1e-07)

			var_3_3.DealDamage()

	local function var_3_11(arg_5_0)
		if arg_5_0.Active:
			local var_5_0 = var_0_1.GetSceneMediator().GetCharacter(arg_5_0.UID).GetUnitData()

			var_5_0.ClearUncontrollableSpeed()
			var_5_0.RemoveBuff(var_3_8)

	local function var_3_12(arg_6_0)
		local var_6_0 = var_3_7.exploDMG
		local var_6_1 = var_3_7.knockBack

		for iter_6_0, iter_6_1 in ipairs(arg_6_0):
			if iter_6_1.Active:
				local var_6_2 = var_0_1.GetSceneMediator().GetCharacter(iter_6_1.UID).GetUnitData()
				local var_6_3 = False
				local var_6_4 = var_6_2.GetCurrentOxyState()

				for iter_6_2, iter_6_3 in ipairs(var_3_5):
					if var_6_4 == iter_6_3:
						var_6_3 = True

				if not var_6_3:
					var_3_2.HandleDirectDamage(var_6_2, var_6_0, var_3_3)

					if var_6_2.IsAlive():
						local var_6_5 = pg.Tool.FilterY(var_6_2.GetPosition() - var_3_6)

						if var_6_1 != False:
							var_6_2.SetUncontrollableSpeed(var_6_5, 1, 0.2, 6)

						var_6_2.RemoveBuff(var_3_8)

		local var_6_6, var_6_7 = var_0_1.GetFXPool().GetFX(arg_3_0.GetMissFXID())

		pg.EffectMgr.GetInstance().PlayBattleEffect(var_6_6, var_6_7.Add(var_3_6), True)
		var_3_2.RemoveBulletUnit(var_3_3.GetUniqueID())

	var_3_2.SpawnLastingColumnArea(var_3_3.GetEffectField(), var_3_3.GetIFF(), pg.Tool.FilterY(var_3_6), var_3_1.range, var_3_1.time, var_3_10, var_3_11, False, arg_3_0.GetFXID(), var_3_12, True).SetDiveFilter(var_3_5)

def var_0_1.onBulletMissFunc(arg_7_0):
	var_0_1.onBulletHitFunc(arg_7_0)

def var_0_1.MakeModel(arg_8_0, arg_8_1, arg_8_2):
	local var_8_0 = arg_8_1.GetBulletData()
	local var_8_1 = var_8_0.GetTemplate()
	local var_8_2 = arg_8_0.GetDataProxy()

	if not arg_8_0.GetBulletPool().InstBullet(arg_8_1.GetModleID(), function(arg_9_0)
		arg_8_1.AddModel(arg_9_0)):
		arg_8_1.AddTempModel(arg_8_0.GetTempGOPool().GetObject())

	arg_8_1.SetSpawn(arg_8_2)
	arg_8_1.SetFXFunc(arg_8_0.onBulletHitFunc, arg_8_0.onBulletMissFunc)
	arg_8_0.GetSceneMediator().AddBullet(arg_8_1)

	if var_8_0.GetIFF() != var_8_2.GetFriendlyCode() and var_8_1.alert_fx != "":
		arg_8_1.MakeAlert(arg_8_0.GetFXPool().GetFX(var_8_1.alert_fx))
