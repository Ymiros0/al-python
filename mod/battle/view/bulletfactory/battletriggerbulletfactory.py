ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleTriggerBulletFactory = singletonClass("BattleTriggerBulletFactory", var_0_0.Battle.BattleBombBulletFactory)
var_0_0.Battle.BattleTriggerBulletFactory.__name = "BattleTriggerBulletFactory"

local var_0_1 = var_0_0.Battle.BattleTriggerBulletFactory

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

def var_0_1.OutRangeFunc(arg_2_0):
	local var_2_0 = arg_2_0.GetTemplate()
	local var_2_1 = var_2_0.hit_type
	local var_2_2 = var_2_0.extra_param.multy or 1
	local var_2_3 = var_0_1.GetDataProxy()
	local var_2_4 = arg_2_0.GetDiveFilter()
	local var_2_5

	local function var_2_6(arg_3_0)
		local var_3_0 = var_2_1.decay

		if var_3_0:
			var_2_5.UpdateDistanceInfo()

		for iter_3_0, iter_3_1 in ipairs(arg_3_0):
			if iter_3_1.Active:
				local var_3_1 = iter_3_1.UID
				local var_3_2 = 0

				if var_3_0:
					var_3_2 = var_2_5.GetDistance(var_3_1) / (var_2_1.range * 0.5) * var_3_0

				local var_3_3 = var_0_1.GetSceneMediator().GetCharacter(var_3_1).GetUnitData()
				local var_3_4 = 0

				while var_3_3.IsAlive() and var_3_4 < var_2_2:
					var_2_3.HandleDamage(arg_2_0, var_3_3, var_3_2)

					var_3_4 = var_3_4 + 1

		var_0_0.Battle.PlayBattleSFX(arg_2_0.GetHitSFX())
		var_2_3.SpawnEffect(var_2_0.hit_fx, arg_2_0.GetExplodePostion())

	var_2_5 = var_2_3.SpawnTriggerColumnArea(arg_2_0.GetEffectField(), arg_2_0.GetIFF(), arg_2_0.GetExplodePostion(), var_2_1.range, var_2_1.time, False, var_2_0.miss_fx, var_2_6)

	var_2_5.SetDiveFilter(var_2_4)
	var_2_3.RemoveBulletUnit(arg_2_0.GetUniqueID())

def var_0_1.onBulletHitFunc(arg_4_0, arg_4_1, arg_4_2):
	return

def var_0_1.CreateBulletAlert(arg_5_0):
	return
