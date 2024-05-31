ys = ys or {}

local var_0_0 = ys
local var_0_1 = singletonClass("BattleSpaceLaserFactory", var_0_0.Battle.BattleBulletFactory)

var_0_1.__name = "BattleSpaceLaserFactory"
var_0_0.Battle.BattleSpaceLaserFactory = var_0_1

def var_0_1.MakeBullet(arg_1_0):
	return var_0_0.Battle.BattleLaserArea.New()

def var_0_1.MakeModel(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_1.GetBulletData()
	local var_2_1 = var_2_0.GetTemplate()
	local var_2_2 = arg_2_0.GetDataProxy()
	local var_2_3 = arg_2_0.GetBulletPool().InstFX(arg_2_1.GetModleID())

	if var_2_3:
		arg_2_1.AddModel(var_2_3)
	else
		arg_2_1.AddTempModel(arg_2_0.GetTempGOPool().GetObject())

	var_0_0.Battle.PlayBattleSFX(var_2_0.GetHitSFX())

	local function var_2_4(arg_3_0, arg_3_1, arg_3_2)
		local var_3_0 = arg_3_0.GetBulletData()
		local var_3_1 = var_3_0.GetTemplate()
		local var_3_2 = var_3_0.GetDiveFilter()
		local var_3_3, var_3_4 = var_3_0.GetCollidedList()

		if var_3_0.IsAlert():
			return

		local var_3_5 = var_3_4[arg_3_1] or 0

		if pg.TimeMgr.GetInstance().GetCombatTime() < var_3_5 + var_3_0.GetHitInterval():
			return

		local var_3_6 = var_0_1.GetSceneMediator().GetCharacter(arg_3_1).GetUnitData()

		if var_3_6.GetCldData().Active:
			local var_3_7 = False
			local var_3_8 = var_3_6.GetCurrentOxyState()

			for iter_3_0, iter_3_1 in ipairs(var_3_2):
				if var_3_8 == iter_3_1:
					var_3_7 = True

			if not var_3_7:
				var_2_2.HandleDamage(var_3_0, var_3_6)

		var_3_4[arg_3_1] = pg.TimeMgr.GetInstance().GetCombatTime()

	local function var_2_5(arg_4_0)
		return

	arg_2_1.SetSpawn(arg_2_2)
	arg_2_1.SetFXFunc(var_2_4, var_2_5)
	arg_2_0.GetSceneMediator().AddBullet(arg_2_1)

def var_0_1.OutRangeFunc(arg_5_0):
	arg_5_0.ExecuteLifeEndCallback()
	var_0_1.GetDataProxy().RemoveBulletUnit(arg_5_0.GetUniqueID())
