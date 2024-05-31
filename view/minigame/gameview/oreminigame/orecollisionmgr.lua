local var_0_0 = class("OreCollisionMgr")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.binder = arg_1_1
	arg_1_0.oreMap = {}
	arg_1_0.enemyMap = {}
end

function var_0_0.SetAkashiObject(arg_2_0, arg_2_1)
	arg_2_0.akashiControl = arg_2_1
end

function var_0_0.AddOreObject(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0.oreMap[arg_3_1] = arg_3_2
end

function var_0_0.RemoveOreObject(arg_4_0, arg_4_1, arg_4_2)
	arg_4_0.oreMap[arg_4_1] = nil
end

function var_0_0.AddEnemyObject(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	if not arg_5_0.enemyMap[arg_5_1] then
		arg_5_0.enemyMap[arg_5_1] = {}
	end

	arg_5_0.enemyMap[arg_5_1][arg_5_2] = arg_5_3
end

function var_0_0.RemoveEnemyObject(arg_6_0, arg_6_1, arg_6_2, arg_6_3)
	arg_6_0.enemyMap[arg_6_1][arg_6_2] = nil
end

function var_0_0.Reset(arg_7_0)
	arg_7_0.oreMap = {}
	arg_7_0.enemyMap = {}
	arg_7_0.oreTarget = ""
end

local function var_0_1(arg_8_0, arg_8_1)
	local var_8_0 = {
		x = math.abs(arg_8_1.pos.x - arg_8_0.pos.x),
		y = math.abs(arg_8_1.pos.y - arg_8_0.pos.y)
	}
	local var_8_1 = arg_8_0.aabb
	local var_8_2 = arg_8_1.aabb
	local var_8_3 = math.abs(var_8_1[2][1] - var_8_1[1][1]) / 2 + math.abs(var_8_2[2][1] - var_8_2[1][1]) / 2
	local var_8_4 = math.abs(var_8_1[2][2] - var_8_1[1][2]) / 2 + math.abs(var_8_2[2][2] - var_8_2[1][2]) / 2

	if var_8_3 > var_8_0.x and var_8_4 > var_8_0.y then
		return true
	end

	return false
end

local function var_0_2(arg_9_0, arg_9_1, arg_9_2)
	switch(arg_9_0, {
		W = function()
			return arg_9_2.x < arg_9_1.x
		end,
		N = function()
			return arg_9_2.y > arg_9_1.y
		end,
		E = function()
			return arg_9_2.x > arg_9_1.x
		end,
		S = function()
			return arg_9_2.y < arg_9_1.y
		end
	})

	return false
end

function var_0_0.GetCarryOreTarget(arg_14_0)
	local var_14_0
	local var_14_1
	local var_14_2 = OreGameConfig.CARRY_RADIUS
	local var_14_3 = OreGameConfig.CARRY_LOOKAT_RADIUS
	local var_14_4 = arg_14_0.akashiControl:GetAnimDirLabel()
	local var_14_5 = arg_14_0.akashiControl:GetCollisionInfo().pos

	for iter_14_0, iter_14_1 in pairs(arg_14_0.oreMap) do
		local var_14_6 = iter_14_1:GetCollisionInfo().pos

		if var_0_2(var_14_4, var_14_5, var_14_6) then
			local var_14_7 = Vector2.Distance(var_14_5, var_14_6)

			if var_14_7 <= var_14_3 and (not var_14_1 or var_14_7 <= var_14_1) then
				var_14_0, var_14_1 = iter_14_0, var_14_7
			end
		end
	end

	if var_14_0 and var_14_1 then
		return var_14_0
	end

	for iter_14_2, iter_14_3 in pairs(arg_14_0.oreMap) do
		local var_14_8 = iter_14_3:GetCollisionInfo().pos
		local var_14_9 = Vector2.Distance(var_14_5, var_14_8)

		if var_14_9 <= var_14_2 and (not var_14_1 or var_14_9 <= var_14_1) then
			var_14_0, var_14_1 = iter_14_2, var_14_9
		end
	end

	return var_14_0 or ""
end

function var_0_0.UpdateOreStatus(arg_15_0)
	local var_15_0 = arg_15_0:GetCarryOreTarget()

	if arg_15_0.oreTarget ~= var_15_0 then
		arg_15_0.oreTarget = var_15_0

		arg_15_0.binder:emit(OreGameConfig.EVENT_UPDATE_ORE_TARGET, {
			index = arg_15_0.oreTarget
		})
	end
end

function var_0_0.UpdateAkashiCollision(arg_16_0)
	if arg_16_0.akashiControl:IsInvincible() then
		return
	end

	local var_16_0 = arg_16_0.akashiControl:GetCollisionInfo()

	for iter_16_0, iter_16_1 in pairs(arg_16_0.enemyMap) do
		for iter_16_2, iter_16_3 in pairs(iter_16_1) do
			local var_16_1 = iter_16_3:GetCollisionInfo()

			if var_0_1(var_16_0, var_16_1) then
				arg_16_0.binder:emit(OreGameConfig.EVENT_AKASHI_COLLISION, {
					a = arg_16_0.akashiControl,
					b = iter_16_3
				})

				return
			end
		end
	end
end

function var_0_0.UpdateEnemyCollision(arg_17_0)
	for iter_17_0, iter_17_1 in pairs(arg_17_0.enemyMap) do
		local var_17_0 = {}

		for iter_17_2, iter_17_3 in pairs(iter_17_1) do
			if not var_17_0[iter_17_2] then
				var_17_0[iter_17_2] = {}
			end

			local var_17_1 = iter_17_3:GetCollisionInfo()

			for iter_17_4, iter_17_5 in pairs(iter_17_1) do
				if not var_17_0[iter_17_4] then
					var_17_0[iter_17_4] = {}
				end

				if iter_17_4 ~= iter_17_2 and not var_17_0[iter_17_2][iter_17_4] and not var_17_0[iter_17_4][iter_17_2] then
					local var_17_2 = iter_17_5:GetCollisionInfo()

					if var_0_1(var_17_1, var_17_2) then
						arg_17_0.binder:emit(OreGameConfig.EVENT_ENEMY_COLLISION, {
							a = iter_17_3,
							b = iter_17_5
						})
					end

					var_17_0[iter_17_2][iter_17_4] = true
					var_17_0[iter_17_4][iter_17_2] = true
				end
			end
		end
	end
end

function var_0_0.OnTimer(arg_18_0, arg_18_1)
	arg_18_0:UpdateOreStatus()
	arg_18_0:UpdateAkashiCollision()
	arg_18_0:UpdateEnemyCollision()
end

return var_0_0
