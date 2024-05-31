ys = ys or {}

local var_0_0 = ys
local var_0_1 = singletonClass("BattleMissileFactory", var_0_0.Battle.BattleBombBulletFactory)

var_0_1.__name = "BattleMissileFactory"
var_0_0.Battle.BattleMissileFactory = var_0_1

def var_0_1.MakeModel(arg_1_0, arg_1_1, arg_1_2):
	local var_1_0 = arg_1_1.GetBulletData()
	local var_1_1 = arg_1_0.GetBulletPool().InstFX(arg_1_1.GetModleID())

	if var_1_1:
		arg_1_1.AddModel(var_1_1)
	else
		arg_1_1.AddTempModel(arg_1_0.GetTempGOPool().GetObject())

	arg_1_1.SetSpawn(arg_1_2)
	arg_1_1.SetFXFunc(arg_1_0.onBulletHitFunc, arg_1_0.onBulletHitFunc)
	arg_1_0.GetSceneMediator().AddBullet(arg_1_1)

def var_0_1.CreateBulletAlert(arg_2_0):
	local var_2_0 = arg_2_0.GetTemplate()

	if arg_2_0.GetIFF() == var_0_1.GetDataProxy().GetFriendlyCode():
		return

	if #var_2_0.alert_fx <= 0:
		return

	local var_2_1 = var_2_0.hit_type.range
	local var_2_2 = var_2_0.alert_fx
	local var_2_3 = var_0_0.Battle.BattleFXPool.GetInstance().GetFX(var_2_2)
	local var_2_4 = var_2_3.transform
	local var_2_5 = 0
	local var_2_6 = pg.effect_offset

	if var_2_6[var_2_2] and var_2_6[var_2_2].y_scale == True:
		var_2_5 = var_2_1

	var_2_4.localScale = Vector3(var_2_1, var_2_5, var_2_1)

	pg.EffectMgr.GetInstance().PlayBattleEffect(var_2_3, arg_2_0.GetExplodePostion())
