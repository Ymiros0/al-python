ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBulletEvent
local var_0_2 = var_0_0.Battle.BattleResourceManager
local var_0_3 = var_0_0.Battle.BattleConfig
local var_0_4 = class("BattleBombBullet", var_0_0.Battle.BattleBullet)

var_0_0.Battle.BattleBombBullet = var_0_4
var_0_4.__name = "BattleBombBullet"

def var_0_4.Ctor(arg_1_0):
	var_0_4.super.Ctor(arg_1_0)

def var_0_4.Dispose(arg_2_0):
	if arg_2_0._alert:
		arg_2_0._alert.Dispose()

	var_0_4.super.Dispose(arg_2_0)

def var_0_4.AddBulletEvent(arg_3_0):
	arg_3_0._bulletData.RegisterEventListener(arg_3_0, var_0_1.EXPLODE, arg_3_0.onBulletExplode)

def var_0_4.RemoveBulletEvent(arg_4_0):
	arg_4_0._bulletData.UnregisterEventListener(arg_4_0, var_0_1.EXPLODE)

def var_0_4.onBulletExplode(arg_5_0, arg_5_1):
	arg_5_0._bulletHitFunc(arg_5_0)

def var_0_4.UpdatePosition(arg_6_0):
	local var_6_0 = Vector3.Lerp(arg_6_0._tf.localPosition, arg_6_0.GetPosition(), var_0_3.BulletMotionRate)

	arg_6_0._tf.localPosition = var_6_0

	arg_6_0._cacheTFPos.Set(var_6_0.x, var_6_0.y, var_6_0.z)
