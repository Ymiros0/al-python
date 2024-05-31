﻿local var_0_0 = class("OreEnemiesControl")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	arg_1_0.binder = arg_1_1
	arg_1_0.collisionMgr = arg_1_3
	arg_1_0._tf = arg_1_2
	arg_1_0.poolTF = findTF(arg_1_0._tf, "pool")

	arg_1_0:Init()
end

function var_0_0.AddListener(arg_2_0)
	arg_2_0.binder:bind(OreGameConfig.EVENT_ENEMY_DESTROY, function(arg_3_0, arg_3_1)
		arg_2_0.enemyList[arg_3_1.roadID][arg_3_1.index] = nil

		arg_2_0:ReturnEnemy(findTF(arg_2_0.roadTFs[arg_3_1.roadID], arg_3_1.index), arg_3_1.id)
	end)
end

function var_0_0.Init(arg_4_0)
	arg_4_0:AddListener()

	arg_4_0.roadTFs = {
		findTF(arg_4_0._tf, "road_1"),
		findTF(arg_4_0._tf, "road_2"),
		(findTF(arg_4_0._tf, "road_3"))
	}
	arg_4_0.tpls = findTF(arg_4_0._tf, "tpls")
	arg_4_0.enemyList = {}

	arg_4_0:Reset()
end

function var_0_0.InitCreatList(arg_5_0)
	local function var_5_0(arg_6_0, arg_6_1)
		if not arg_5_0.createList[arg_6_0] then
			local var_6_0 = {
				arg_6_1
			}

			arg_5_0.createList[arg_6_0] = var_6_0
		else
			table.insert(arg_5_0.createList[arg_6_0], arg_6_1)
		end
	end

	local function var_5_1(arg_7_0, arg_7_1, arg_7_2)
		local var_7_0 = OreGameConfig.CREATE_CONFIG[arg_7_2].num
		local var_7_1 = Clone(OreGameConfig.CREATE_CONFIG[arg_7_2].enemy)

		assert(var_7_0 <= #var_7_1, "create cfg illegal. ID: " .. arg_7_2)

		local var_7_2 = arg_7_0

		for iter_7_0 = 1, var_7_0 do
			local var_7_3 = math.random(1, #var_7_1)
			local var_7_4 = var_7_1[var_7_3]

			table.remove(var_7_1, var_7_3)

			local var_7_5 = {
				roadID = arg_7_1,
				enemyID = var_7_4
			}

			var_5_0(var_7_2, var_7_5)

			var_7_2 = var_7_2 + 1
		end
	end

	arg_5_0.roadDir = OreGameConfig.ROAD_DIRECTION[math.random(#OreGameConfig.ROAD_DIRECTION)]

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.roadTFs) do
		local var_5_2 = OreGameConfig["CREATE_ENEMY_ROAD_" .. iter_5_0]
		local var_5_3 = OreGameConfig.ROAD_CONFIG_TYPE[iter_5_0]

		if var_5_3 == 1 then
			for iter_5_2, iter_5_3 in ipairs(var_5_2) do
				var_5_1(iter_5_3.time, iter_5_0, iter_5_3.create)
			end
		elseif var_5_3 == 2 then
			for iter_5_4, iter_5_5 in ipairs(var_5_2) do
				local var_5_4 = iter_5_5.time

				while var_5_4 < iter_5_5.stop do
					var_5_1(var_5_4, iter_5_0, iter_5_5.create)

					var_5_4 = var_5_4 + math.random(iter_5_5.step[1], iter_5_5.step[2])
				end
			end
		end
	end
end

function var_0_0.CreateEnemy(arg_8_0, arg_8_1)
	for iter_8_0, iter_8_1 in ipairs(arg_8_1) do
		local var_8_0 = arg_8_0.indexTags[iter_8_1.roadID] + 1

		arg_8_0.indexTags[iter_8_1.roadID] = var_8_0

		local var_8_1 = arg_8_0:GetEnemy(iter_8_1.enemyID)

		var_8_1:SetParent(tf(arg_8_0.roadTFs[iter_8_1.roadID]), false)

		var_8_1.name = var_8_0

		SetActive(var_8_1, true)

		if not arg_8_0.enemyList[iter_8_1.roadID] then
			arg_8_0.enemyList[iter_8_1.roadID] = {}
		end

		arg_8_0.enemyList[iter_8_1.roadID][var_8_0] = OreEnemy.New(arg_8_0.binder, var_8_1, arg_8_0.collisionMgr, iter_8_1.enemyID, iter_8_1.roadID, arg_8_0.roadDir[iter_8_1.roadID])
	end
end

function var_0_0.Reset(arg_9_0)
	arg_9_0.time = 0
	arg_9_0.createList = {}

	for iter_9_0, iter_9_1 in pairs(arg_9_0.enemyList) do
		for iter_9_2, iter_9_3 in pairs(iter_9_1) do
			iter_9_3:Dispose()
		end
	end

	arg_9_0.enemyList = {}
	arg_9_0.indexTags = {
		0,
		0,
		0
	}

	for iter_9_4, iter_9_5 in pairs(arg_9_0.roadTFs) do
		removeAllChildren(iter_9_5)
	end

	arg_9_0:InitCreatList()

	arg_9_0.pools = {}

	removeAllChildren(arg_9_0.poolTF)
end

function var_0_0.OnTimer(arg_10_0, arg_10_1)
	arg_10_0.time = arg_10_0.time + arg_10_1

	for iter_10_0, iter_10_1 in pairs(arg_10_0.createList) do
		if iter_10_0 <= arg_10_0.time then
			arg_10_0:CreateEnemy(iter_10_1)

			arg_10_0.createList[iter_10_0] = nil
		end
	end

	for iter_10_2, iter_10_3 in pairs(arg_10_0.enemyList) do
		for iter_10_4, iter_10_5 in pairs(iter_10_3) do
			iter_10_5:OnTimer(arg_10_1)
		end
	end
end

function var_0_0.GetEnemy(arg_11_0, arg_11_1)
	if arg_11_0.pools[arg_11_1] and #arg_11_0.pools[arg_11_1] > 0 then
		return table.remove(arg_11_0.pools[arg_11_1])
	end

	return (tf(Instantiate(findTF(arg_11_0.tpls, arg_11_1))))
end

function var_0_0.ReturnEnemy(arg_12_0, arg_12_1, arg_12_2)
	if not arg_12_0.pools[arg_12_2] then
		arg_12_0.pools[arg_12_2] = {}
	end

	arg_12_1:SetParent(tf(arg_12_0.poolTF), false)
	setActive(arg_12_1, false)
	table.insert(arg_12_0.pools[arg_12_2], tf(arg_12_1))
end

return var_0_0
