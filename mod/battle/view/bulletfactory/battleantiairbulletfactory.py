ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleAntiAirBulletFactory = singletonClass("BattleAntiAirBulletFactory", var_0_0.Battle.BattleBulletFactory)
var_0_0.Battle.BattleAntiAirBulletFactory.__name = "BattleAntiAirBulletFactory"

local var_0_1 = var_0_0.Battle.BattleAntiAirBulletFactory

def var_0_1.Ctor(arg_1_0):
	var_0_1.super.Ctor(arg_1_0)

	arg_1_0._tmpTimerList = {}

def var_0_1.NeutralizeBullet(arg_2_0):
	for iter_2_0, iter_2_1 in pairs(arg_2_0._tmpTimerList):
		pg.TimeMgr.GetInstance().RemoveBattleTimer(iter_2_1)

		arg_2_0._tmpTimerList[iter_2_1] = None

def var_0_1.CreateBullet(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5):
	local var_3_0 = arg_3_2.GetTemplate().hit_type
	local var_3_1 = arg_3_0.GetDataProxy()
	local var_3_2 = arg_3_2.GetDirectHitUnit()

	if not var_3_2:
		var_3_1.RemoveBulletUnit(arg_3_2.GetUniqueID())

		return

	local var_3_3 = var_3_2.GetUniqueID()
	local var_3_4 = arg_3_0.GetSceneMediator().GetAircraft(var_3_3)

	if var_3_4 == None:
		var_3_1.RemoveBulletUnit(arg_3_2.GetUniqueID())

		return

	local var_3_5 = var_3_4.GetPosition().Clone()
	local var_3_6 = var_3_0.range

	local function var_3_7(arg_4_0)
		local var_4_0 = {}

		for iter_4_0, iter_4_1 in ipairs(arg_4_0):
			if iter_4_1.Active:
				local var_4_1 = arg_3_0.GetSceneMediator().GetAircraft(iter_4_1.UID)

				if var_4_1:
					local var_4_2 = var_4_1.GetUnitData()

					if var_4_2.IsVisitable():
						var_4_0[#var_4_0 + 1] = var_4_2

		var_3_1.HandleMeteoDamage(arg_3_2, var_4_0)

	local function var_3_8()
		var_3_1.SpawnColumnArea(arg_3_2.GetEffectField(), arg_3_2.GetIFF(), var_3_5, var_3_6, var_3_0.time, var_3_7)
		var_3_1.RemoveBulletUnit(arg_3_2.GetUniqueID())

	local function var_3_9()
		local var_6_0

		if var_3_2.IsAlive() and var_3_4:
			var_6_0 = var_3_4.GetPosition().Clone().Add(Vector3(math.random(var_3_6) - var_3_6 * 0.5, 0, math.random(var_3_6) - var_3_6 * 0.5))
			var_3_5 = var_6_0
		else
			var_6_0 = var_3_5

		local var_6_1, var_6_2 = arg_3_0.GetFXPool().GetFX(arg_3_2.GetTemplate().hit_fx)

		pg.EffectMgr.GetInstance().PlayBattleEffect(var_6_1, var_6_2.Add(var_6_0), True)

	local var_3_10
	local var_3_11

	local function var_3_12()
		if arg_3_4 == None:
			var_3_8()
		else
			arg_3_0.PlayFireFX(arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5, var_3_11)

	function var_3_11()
		if arg_3_0._tmpTimerList[var_3_10] != None:
			var_3_12()
			var_3_9()
		else
			var_3_8()

	local function var_3_13()
		pg.TimeMgr.GetInstance().RemoveBattleTimer(var_3_10)

		arg_3_0._tmpTimerList[var_3_10] = None
		var_3_10 = None

	var_3_10 = pg.TimeMgr.GetInstance().AddBattleTimer("antiAirTimer", -1, 0.5, var_3_13, True)
	arg_3_0._tmpTimerList[var_3_10] = var_3_10

	var_3_12()
