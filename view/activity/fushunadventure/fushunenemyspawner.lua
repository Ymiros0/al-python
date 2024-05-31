local var_0_0 = class("FuShunEnemySpawner")
local var_0_1 = 1
local var_0_2 = 2

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	arg_1_0.parent = arg_1_1
	arg_1_0.index = 0
	arg_1_0.score = 0
	arg_1_0.changeTime = -1
	arg_1_0.mode = var_0_1
	arg_1_0.OnSpawn = arg_1_2
	arg_1_0.targetTime = 0
	arg_1_0.delta = 0
	arg_1_0.starting = false
	arg_1_0.fushunLoader = arg_1_3
end

function var_0_0.Start(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	arg_2_0.delta = 0
	arg_2_0.changeTime = -1

	if arg_2_3 then
		arg_2_0.delta = arg_2_2
	end

	arg_2_0.targetTime = arg_2_2
	arg_2_0.mode = arg_2_1
	arg_2_0.starting = true

	FushunAdventureGame.LOG(" spawner time  :", arg_2_2)
end

function var_0_0.Update(arg_3_0)
	if not arg_3_0.starting then
		return
	end

	arg_3_0.delta = arg_3_0.delta + Time.deltaTime

	if arg_3_0.delta >= arg_3_0.targetTime then
		arg_3_0.delta = 0

		arg_3_0:Spawn()

		if arg_3_0.changeTime ~= -1 then
			arg_3_0:Start(arg_3_0.mode, arg_3_0.changeTime, false)
		end
	end
end

function var_0_0.NormalMode(arg_4_0)
	local var_4_0 = arg_4_0:CalcTime(arg_4_0.score)

	arg_4_0:Start(var_0_1, var_4_0, true)
end

function var_0_0.CarzyMode(arg_5_0)
	local var_5_0 = FushunAdventureGameConst.EX_ENEMY_SPAWN_TIME

	arg_5_0:Start(var_0_2, var_5_0, true)
end

function var_0_0.Spawn(arg_6_0)
	local var_6_0 = arg_6_0.mode

	arg_6_0.index = arg_6_0.index + 1

	local var_6_1 = arg_6_0.index
	local var_6_2 = arg_6_0:GetConfigByScore(arg_6_0.score)

	assert(var_6_2)
	arg_6_0.fushunLoader:GetPrefab("FushunAdventure/" .. var_6_2.name, "", function(arg_7_0)
		arg_7_0.transform:SetParent(arg_6_0.parent, false)

		if arg_6_0.OnSpawn then
			arg_6_0.OnSpawn({
				go = arg_7_0,
				config = var_6_2,
				speed = var_6_0 == var_0_1 and var_6_2.speed or var_6_2.crazy_speed,
				index = var_6_1
			})
		end
	end, var_6_2.name)
end

function var_0_0.GetConfigByScore(arg_8_0, arg_8_1)
	local var_8_0 = FushunAdventureGameConst.PROPABILITES
	local var_8_1

	for iter_8_0, iter_8_1 in ipairs(var_8_0) do
		local var_8_2 = iter_8_1[1][1]
		local var_8_3 = iter_8_1[1][2]

		if var_8_2 <= arg_8_1 and arg_8_1 <= var_8_3 then
			var_8_1 = iter_8_1

			break
		end
	end

	var_8_1 = var_8_1 or var_8_0[#var_8_0]

	local var_8_4 = var_8_1[2]
	local var_8_5 = var_8_1[3]
	local var_8_6 = var_8_1[4]
	local var_8_7 = math.random(1, 100)

	FushunAdventureGame.LOG("rate :", var_8_4, var_8_5, var_8_6, " r :", var_8_7)

	local var_8_8 = 1

	if var_8_4 < var_8_7 and var_8_7 <= var_8_4 + var_8_5 then
		var_8_8 = 2
	elseif var_8_7 > var_8_4 + var_8_5 and var_8_7 <= 100 then
		var_8_8 = 3
	end

	return FushunAdventureGameConst.ENEMYS[var_8_8]
end

function var_0_0.UpdateScore(arg_9_0, arg_9_1)
	arg_9_0.score = arg_9_1

	if arg_9_0.mode == var_0_2 then
		return
	end

	local var_9_0 = arg_9_0:CalcTime(arg_9_1)

	if arg_9_0.targetTime ~= var_9_0 then
		arg_9_0.changeTime = var_9_0
	end
end

function var_0_0.CalcTime(arg_10_0, arg_10_1)
	local var_10_0 = FushunAdventureGameConst.ENEMY_SPAWN_TIME_ADDITION
	local var_10_1

	for iter_10_0, iter_10_1 in ipairs(var_10_0) do
		local var_10_2 = iter_10_1[1][1]
		local var_10_3 = iter_10_1[1][2]

		if var_10_2 <= arg_10_1 and arg_10_1 <= var_10_3 then
			var_10_1 = iter_10_1

			break
		end
	end

	var_10_1 = var_10_1 or var_10_0[#var_10_0]

	local var_10_4 = var_10_1[2]

	return (math.random(var_10_4[1], var_10_4[2]))
end

function var_0_0.Stop(arg_11_0)
	arg_11_0.starting = false
end

function var_0_0.Dispose(arg_12_0)
	arg_12_0:Stop()
end

return var_0_0
