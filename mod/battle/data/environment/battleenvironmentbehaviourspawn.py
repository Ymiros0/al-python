ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleFormulas
local var_0_4 = class("BattleEnvironmentBehaviourSpawn", var_0_0.Battle.BattleEnvironmentBehaviour)

var_0_0.Battle.BattleEnvironmentBehaviourSpawn = var_0_4
var_0_4.__name = "BattleEnvironmentBehaviourSpawn"

def var_0_4.Ctor(arg_1_0):
	arg_1_0._moveEndTime = None
	arg_1_0._targetIndex = 0

	var_0_4.super.Ctor(arg_1_0)

def var_0_4.SetTemplate(arg_2_0, arg_2_1):
	var_0_4.super.SetTemplate(arg_2_0, arg_2_1)

	arg_2_0._content = arg_2_1.content
	arg_2_0._route = arg_2_1.route or {}
	arg_2_0._reloadTime = arg_2_1.reload_time
	arg_2_0._rounds = arg_2_1.rounds

def var_0_4.doBehaviour(arg_3_0):
	arg_3_0._targetIndex = arg_3_0._targetIndex + 1

	if arg_3_0._targetIndex <= arg_3_0._rounds:
		local var_3_0 = arg_3_0._route[arg_3_0._targetIndex]
		local var_3_1 = var_0_0.Battle.BattleDataProxy.GetInstance()
		local var_3_2 = arg_3_0._unit._aoeData
		local var_3_3 = var_3_2.GetPosition()
		local var_3_4 = Clone(arg_3_0._content)

		if var_3_0:
			table.merge(var_3_4, var_3_0)

		local var_3_5 = var_3_4.count
		local var_3_6 = var_3_4.child_prefab
		local var_3_7

		if var_3_2.GetAreaType() == var_0_1.AreaType.CUBE:
			local var_3_8, var_3_9 = unpack(var_3_6.cld_data)

			var_3_7 = arg_3_0.GenerateRandomRectanglePosition(var_3_2.GetWidth(), var_3_2.GetHeight(), var_3_5, math.max(var_3_8, var_3_9 or 0))
		elif var_3_2.GetAreaType() == var_0_1.AreaType.COLUMN:
			local var_3_10, var_3_11 = unpack(var_3_6.cld_data)

			var_3_7 = arg_3_0.GenerateRandomCirclePosition(var_3_2.GetRange(), var_3_5, math.max(var_3_10, var_3_11 or 0))

		for iter_3_0 = 1, var_3_5:
			var_3_7[iter_3_0] = var_3_7[iter_3_0] + var_3_3

		seriesAsync({
			function(arg_4_0)
				if not var_3_4.alert:
					arg_4_0()

					return

				for iter_4_0 = 1, var_3_5:
					local var_4_0 = var_3_7[iter_4_0]

					arg_3_0.PlayAlert(var_3_4.alert, var_4_0)

				arg_3_0.RemoveAlertTimer()

				arg_3_0._alertTimer = pg.TimeMgr.GetInstance().AddBattleTimer("", 1, var_3_4.alert.delay or 1, arg_4_0, True),
			function(arg_5_0)
				for iter_5_0 = 1, var_3_5:
					local var_5_0 = Clone(var_3_6)
					local var_5_1 = var_3_7[iter_5_0]

					var_5_0.coordinate = {
						var_5_1.x,
						var_5_1.y,
						var_5_1.z
					}

					var_3_1.SpawnEnvironment(var_5_0)
		})
		var_0_4.super.doBehaviour(arg_3_0)
	else
		arg_3_0.doExpire()

def var_0_4.RemoveAlertTimer(arg_6_0):
	if arg_6_0._alertTimer:
		pg.TimeMgr.GetInstance().RemoveBattleTimer(arg_6_0._alertTimer)

	arg_6_0._alertTimer = None

def var_0_4.PlayAlert(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.range
	local var_7_1 = arg_7_0.alert_fx

	if not var_7_1:
		return

	local var_7_2 = var_0_0.Battle.BattleFXPool.GetInstance().GetFX(var_7_1)
	local var_7_3 = var_7_2.transform
	local var_7_4 = 0
	local var_7_5 = pg.effect_offset

	if var_7_5[var_7_1] and var_7_5[var_7_1].y_scale == True:
		var_7_4 = var_7_0

	var_7_3.localScale = Vector3(var_7_0, var_7_4, var_7_0)

	pg.EffectMgr.GetInstance().PlayBattleEffect(var_7_2, arg_7_1)

local var_0_5 = math

def var_0_4.GenerateRandomRectanglePosition(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	local var_8_0 = var_0_5.ceil(var_0_5.sqrt(arg_8_2))
	local var_8_1 = {}

	for iter_8_0 = 1, var_8_0 * var_8_0:
		table.insert(var_8_1, {
			weight = 65536,
			rst = iter_8_0
		})

	local var_8_2 = {}

	for iter_8_1 = 1, arg_8_2:
		local var_8_3 = var_0_3.WeightRandom(var_8_1)

		var_8_1[var_8_3].weight = 0

		local var_8_4 = var_0_5.floor((var_8_3 - 1) / var_8_0)
		local var_8_5 = var_8_4 * var_8_0

		for iter_8_2 = 0, var_8_0 - 1:
			var_8_1[var_8_5 + iter_8_2 + 1].weight = var_8_1[var_8_5 + iter_8_2 + 1].weight / 2

		local var_8_6 = var_8_3 - var_8_4 * var_8_0

		for iter_8_3 = 0, var_8_0 - 1:
			var_8_1[var_8_6 + iter_8_3 * var_8_0].weight = var_8_1[var_8_6 + iter_8_3 * var_8_0].weight / 2

		arg_8_3 = arg_8_3 / 2

		local var_8_7 = (var_8_6 - 1 - var_8_0 / 2) * (arg_8_0 / var_8_0) + var_0_5.random(1, 1000) / 1000 * (arg_8_0 / var_8_0 - 2 * arg_8_3) + arg_8_3
		local var_8_8 = (var_8_4 - var_8_0 / 2) * (arg_8_1 / var_8_0) + var_0_5.random(1, 1000) / 1000 * (arg_8_1 / var_8_0 - 2 * arg_8_3) + arg_8_3

		table.insert(var_8_2, Vector3(var_8_7, 0, var_8_8))

	return var_8_2

local var_0_6 = {
	Vector2(0, 0),
	Vector2(-0.66, 0),
	Vector2(-0.33, 0.58),
	Vector2(0.33, 0.58),
	Vector2(0.66, 0),
	Vector2(0.33, -0.58),
	Vector2(-0.33, -0.58)
}

def var_0_4.GenerateRandomCirclePosition(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = 1
	local var_9_1 = 1
	local var_9_2 = arg_9_0

	while var_9_1 < arg_9_1:
		var_9_1 = var_9_1 * 7
		var_9_0 = var_9_0 + 1
		var_9_2 = var_9_2 / 3

	local var_9_3 = {}

	for iter_9_0 = 1, var_9_1:
		table.insert(var_9_3, {
			weight = 256,
			rst = iter_9_0
		})

	local var_9_4 = {}

	for iter_9_1 = 1, arg_9_1:
		local var_9_5 = var_0_3.WeightRandom(var_9_3)

		var_9_3[var_9_5].weight = 0

		local var_9_6 = var_9_5 - 1
		local var_9_7 = 1
		local var_9_8 = Vector2(0, 0)
		local var_9_9 = var_9_2

		for iter_9_2 = var_9_0, 2, -1:
			local var_9_10 = var_9_6

			var_9_6 = var_0_5.floor(var_9_6 / 7)

			local var_9_11 = var_9_10 - var_9_6 * 7

			var_9_9 = var_9_9 * 3

			var_9_8.Add(var_9_9 * var_0_6[var_9_11 + 1])

			var_9_7 = var_9_7 * 7

			if iter_9_2 > 2 and iter_9_2 == var_9_0:
				for iter_9_3 = var_9_6 * var_9_7 + 1, var_9_6 * var_9_7 + var_9_7:
					var_9_3[iter_9_3].weight = var_9_3[iter_9_3].weight / 2

		local var_9_12 = var_0_5.random(1, 360)
		local var_9_13 = var_0_5.random(1, 1000) / 1000 * var_0_5.max(var_9_2 - arg_9_2, 0)

		var_9_8.Add(Vector2(var_9_13 * var_0_5.cos(var_9_12), var_9_13 * var_0_5.sin(var_9_12)))
		table.insert(var_9_4, Vector3(var_9_8.x, 0, var_9_8.y))

	return var_9_4

def var_0_4.Dispose(arg_10_0):
	arg_10_0.RemoveAlertTimer()
	table.clear(arg_10_0)
	var_0_4.super.Dispose(arg_10_0)
