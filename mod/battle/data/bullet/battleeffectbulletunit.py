ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleEffectBulletUnit", var_0_0.Battle.BattleBulletUnit)

var_0_0.Battle.BattleEffectBulletUnit = var_0_1
var_0_1.__name = "BattleEffectBulletUnit"

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

def var_0_1.Update(arg_2_0, arg_2_1):
	var_0_1.super.Update(arg_2_0, arg_2_1)

	if arg_2_0._flare:
		arg_2_0._flare.SetPosition(pg.Tool.FilterY(arg_2_0.GetPosition().Clone()))

def var_0_1.IsFlare(arg_3_0):
	return arg_3_0.GetTemplate().attach_buff[1].flare

def var_0_1.OutRange(arg_4_0):
	var_0_1.super.OutRange(arg_4_0)

	if arg_4_0._flare:
		arg_4_0._flare.SetActiveFlag(False)

		arg_4_0._flare = None

def var_0_1.spawnArea(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.GetTemplate()
	local var_5_1 = var_5_0.hit_type
	local var_5_2 = var_5_0.attach_buff[1]
	local var_5_3 = var_5_2.buff_id
	local var_5_4 = var_5_2.buff_level or 1

	local function var_5_5(arg_6_0)
		for iter_6_0, iter_6_1 in ipairs(arg_6_0):
			if iter_6_1.Active:
				local var_6_0 = arg_5_0._battleProxy.GetUnitList()[iter_6_1.UID]
				local var_6_1 = var_0_0.Battle.BattleBuffUnit.New(var_5_3, var_5_4)

				var_6_0.AddBuff(var_6_1, True)

	local function var_5_6(arg_7_0)
		if arg_7_0.Active:
			arg_5_0._battleProxy.GetUnitList()[arg_7_0.UID].RemoveBuff(var_5_3, True)

	time = var_5_1.time

	local var_5_7 = arg_5_0._battleProxy.SpawnLastingColumnArea(arg_5_0.GetEffectField(), arg_5_0.GetIFF(), pg.Tool.FilterY(arg_5_0.GetPosition().Clone()), var_5_1.range, time, var_5_5, var_5_6, var_5_2.friendly, var_5_2.effect_id)

	if arg_5_1:
		arg_5_0._flare = var_5_7

	return var_5_7

def var_0_1.GetExplodePostion(arg_8_0):
	return arg_8_0._explodePos

def var_0_1.SetExplodePosition(arg_9_0, arg_9_1):
	arg_9_0._explodePos = arg_9_1
