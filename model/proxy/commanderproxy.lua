local var_0_0 = class("CommanderProxy", import(".NetProxy"))

var_0_0.COMMANDER_UPDATED = "CommanderProxy:COMMANDER_UPDATED"
var_0_0.COMMANDER_ADDED = "CommanderProxy:COMMANDER_ADDED"
var_0_0.COMMANDER_DELETED = "CommanderProxy:COMMANDER_DELETED"
var_0_0.RESERVE_CNT_UPDATED = "CommanderProxy:RESERVE_CNT_UPDATED"
var_0_0.COMMANDER_BOX_FINISHED = "CommanderProxy:COMMANDER_BOX_FINISHED"
var_0_0.PREFAB_FLEET_UPDATE = "CommanderProxy:PREFAB_FLEET_UPDATE"
var_0_0.MAX_WORK_COUNT = 4
var_0_0.MAX_SLOT = 10
var_0_0.MAX_PREFAB_FLEET = 3

function var_0_0.register(arg_1_0)
	arg_1_0.data = {}
	arg_1_0.boxes = {}
	arg_1_0.prefabFleet = {}
	arg_1_0.openCommanderScene = false

	for iter_1_0 = 1, var_0_0.MAX_PREFAB_FLEET do
		arg_1_0.prefabFleet[iter_1_0] = CommnaderFleet.New({
			id = iter_1_0
		})
	end

	local var_1_0 = pg.gameset.commander_box_count.key_value

	for iter_1_1 = 1, var_1_0 do
		local var_1_1 = CommanderBox.New({
			id = iter_1_1
		})

		arg_1_0:addBox(var_1_1)
	end

	arg_1_0.pools = {}

	for iter_1_2, iter_1_3 in ipairs(pg.commander_data_create_material.all) do
		local var_1_2 = CommanderBuildPool.New({
			id = iter_1_3
		})

		table.insert(arg_1_0.pools, var_1_2)
	end

	arg_1_0.boxUsageCount = 0

	arg_1_0:on(25001, function(arg_2_0)
		for iter_2_0, iter_2_1 in ipairs(arg_2_0.commanders) do
			local var_2_0 = Commander.New(iter_2_1)

			arg_1_0:addCommander(var_2_0)
		end

		for iter_2_2, iter_2_3 in ipairs(arg_2_0.box) do
			local var_2_1 = CommanderBox.New(iter_2_3, iter_2_2)

			arg_1_0:updateBox(var_2_1)
		end

		for iter_2_4, iter_2_5 in ipairs(arg_2_0.presets) do
			local var_2_2 = iter_2_5.id
			local var_2_3 = iter_2_5.commandersid
			local var_2_4 = {}

			for iter_2_6, iter_2_7 in ipairs(var_2_3) do
				local var_2_5 = arg_1_0:getCommanderById(iter_2_7.id)

				if var_2_5 then
					var_2_4[iter_2_7.pos] = var_2_5
				end
			end

			arg_1_0.prefabFleet[var_2_2]:Update({
				id = var_2_2,
				name = arg_2_0.name,
				commanders = var_2_4
			})
		end

		arg_1_0.boxUsageCount = arg_2_0.usage_count or 0

		if not LOCK_CATTERY then
			arg_1_0:sendNotification(GAME.GET_COMMANDER_HOME)
		end
	end)

	arg_1_0.newCommanderList = {}

	arg_1_0:on(25039, function(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.commander_list) do
			local var_3_0 = Commander.New(iter_3_1)

			arg_1_0:addCommander(var_3_0)
			table.insert(arg_1_0.newCommanderList, var_3_0)
		end
	end)
end

function var_0_0.GetNewestCommander(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = defaultValue(arg_4_2, true)

	if arg_4_1 >= #arg_4_0.newCommanderList then
		return arg_4_0.newCommanderList
	else
		local var_4_1 = {}

		for iter_4_0 = #arg_4_0.newCommanderList - arg_4_1 + 1, #arg_4_0.newCommanderList do
			table.insert(var_4_1, arg_4_0.newCommanderList[iter_4_0])
		end

		return var_4_1
	end

	if var_4_0 then
		arg_4_0.newCommanderList = {}
	end
end

function var_0_0.getPrefabFleetById(arg_5_0, arg_5_1)
	return arg_5_0.prefabFleet[arg_5_1]
end

function var_0_0.getPrefabFleet(arg_6_0)
	return Clone(arg_6_0.prefabFleet)
end

function var_0_0.updatePrefabFleet(arg_7_0, arg_7_1)
	arg_7_0.prefabFleet[arg_7_1.id] = arg_7_1

	arg_7_0:sendNotification(var_0_0.PREFAB_FLEET_UPDATE)
end

function var_0_0.updatePrefabFleetName(arg_8_0, arg_8_1, arg_8_2)
	arg_8_0.prefabFleet[arg_8_1]:updateName(arg_8_2)
	arg_8_0:sendNotification(var_0_0.PREFAB_FLEET_UPDATE)
end

function var_0_0.getCommanderCnt(arg_9_0)
	return table.getCount(arg_9_0.data)
end

function var_0_0.getPoolById(arg_10_0, arg_10_1)
	return _.detect(arg_10_0:getPools(), function(arg_11_0)
		return arg_11_0.id == arg_10_1
	end)
end

function var_0_0.getPools(arg_12_0)
	return arg_12_0.pools
end

function var_0_0.getBoxUseCnt(arg_13_0)
	return arg_13_0.boxUsageCount
end

function var_0_0.updateBoxUseCnt(arg_14_0, arg_14_1)
	arg_14_0.boxUsageCount = arg_14_0.boxUsageCount + arg_14_1

	arg_14_0:sendNotification(var_0_0.RESERVE_CNT_UPDATED, arg_14_0.boxUsageCount)
end

function var_0_0.resetBoxUseCnt(arg_15_0)
	arg_15_0.boxUsageCount = 0

	arg_15_0:sendNotification(var_0_0.RESERVE_CNT_UPDATED, 0)
end

function var_0_0.updateBox(arg_16_0, arg_16_1)
	arg_16_0.boxes[arg_16_1.id] = arg_16_1
end

function var_0_0.addBox(arg_17_0, arg_17_1)
	arg_17_0.boxes[arg_17_1.id] = arg_17_1
end

function var_0_0.getBoxes(arg_18_0)
	local var_18_0 = {}

	for iter_18_0, iter_18_1 in ipairs(arg_18_0.boxes) do
		table.insert(var_18_0, iter_18_1)
	end

	return var_18_0
end

function var_0_0.getBoxById(arg_19_0, arg_19_1)
	assert(arg_19_0.boxes[arg_19_1], "attemp to get a nil box" .. arg_19_1)

	return arg_19_0.boxes[arg_19_1]
end

function var_0_0.getCommanderById(arg_20_0, arg_20_1)
	local var_20_0 = arg_20_0.data[arg_20_1]

	if var_20_0 then
		return var_20_0:clone()
	end
end

function var_0_0.RawGetCommanderById(arg_21_0, arg_21_1)
	local var_21_0 = arg_21_0.data[arg_21_1]

	if var_21_0 then
		return var_21_0
	end
end

function var_0_0.GetSameConfigIdCommanderCount(arg_22_0, arg_22_1)
	local var_22_0 = 0

	for iter_22_0, iter_22_1 in pairs(arg_22_0.data) do
		if iter_22_1.configId == arg_22_1 then
			var_22_0 = var_22_0 + 1
		end
	end

	return var_22_0
end

function var_0_0.addCommander(arg_23_0, arg_23_1)
	arg_23_0.data[arg_23_1.id] = arg_23_1

	if getProxy(PlayerProxy):getInited() then
		arg_23_0:sendNotification(var_0_0.COMMANDER_ADDED, arg_23_1:clone())
	end
end

function var_0_0.updateCommander(arg_24_0, arg_24_1)
	assert(arg_24_0.data[arg_24_1.id], "commander can not be nil")
	assert(isa(arg_24_1, Commander), "commander should be and instance of Commander")

	arg_24_0.data[arg_24_1.id] = arg_24_1

	arg_24_0:sendNotification(var_0_0.COMMANDER_UPDATED, arg_24_1:clone())
end

function var_0_0.removeCommanderById(arg_25_0, arg_25_1)
	arg_25_0:checkPrefabFleet(arg_25_1)
	assert(arg_25_0.data[arg_25_1], "commander can not be nil")

	arg_25_0.data[arg_25_1] = nil

	arg_25_0:sendNotification(var_0_0.COMMANDER_DELETED, arg_25_1)
end

function var_0_0.checkPrefabFleet(arg_26_0, arg_26_1)
	for iter_26_0, iter_26_1 in pairs(arg_26_0.prefabFleet) do
		if iter_26_1:contains(arg_26_1) then
			iter_26_1:removeCommander(arg_26_1)
		end
	end
end

function var_0_0.haveFinishedBox(arg_27_0)
	for iter_27_0, iter_27_1 in pairs(arg_27_0.boxes) do
		if iter_27_1:getState() == CommanderBox.STATE_FINISHED then
			return true
		end
	end

	return false
end

function var_0_0.IsFinishAllBox(arg_28_0)
	local var_28_0 = 0
	local var_28_1 = 0
	local var_28_2 = 0

	for iter_28_0, iter_28_1 in pairs(arg_28_0.boxes) do
		local var_28_3 = iter_28_1:getState()

		if var_28_3 == CommanderBox.STATE_FINISHED then
			var_28_0 = var_28_0 + 1
		elseif var_28_3 == CommanderBox.STATE_EMPTY then
			var_28_1 = var_28_1 + 1
		end

		var_28_2 = var_28_2 + 1
	end

	return var_28_0 > 0 and var_28_0 + var_28_1 == var_28_2
end

function var_0_0.onRemove(arg_29_0)
	arg_29_0:RemoveCalcExpTimer()
	var_0_0.super.onRemove(arg_29_0)

	arg_29_0.openCommanderScene = false
end

function var_0_0.AddCommanderHome(arg_30_0, arg_30_1)
	arg_30_0.commanderHome = arg_30_1

	local var_30_0 = pg.TimeMgr.GetInstance():GetServerTime()
	local var_30_1 = GetNextHour(1) - var_30_0

	arg_30_0:StartCalcExpTimer(var_30_1)
end

function var_0_0.GetCommanderHome(arg_31_0)
	return arg_31_0.commanderHome
end

function var_0_0.StartCalcExpTimer(arg_32_0, arg_32_1)
	arg_32_0:RemoveCalcExpTimer()

	arg_32_0.calcExpTimer = Timer.New(function()
		arg_32_0:RemoveCalcExpTimer()
		arg_32_0:sendNotification(GAME.CALC_CATTERY_EXP, {
			isPeriod = arg_32_1 == 3600
		})
		arg_32_0:StartCalcExpTimer(3600)
	end, arg_32_1, 1)

	arg_32_0.calcExpTimer:Start()
end

function var_0_0.RemoveCalcExpTimer(arg_34_0)
	if arg_34_0.calcExpTimer then
		arg_34_0.calcExpTimer:Stop()

		arg_34_0.calcExpTimer = nil
	end
end

function var_0_0.AnyCatteryExistOP(arg_35_0)
	local var_35_0 = arg_35_0:GetCommanderHome()

	if var_35_0 then
		return var_35_0:AnyCatteryExistOP()
	end

	return false
end

function var_0_0.AnyCatteryCanUse(arg_36_0)
	local var_36_0 = arg_36_0:GetCommanderHome()

	if var_36_0 then
		return var_36_0:AnyCatteryCanUse()
	end

	return false
end

function var_0_0.IsHome(arg_37_0, arg_37_1)
	local var_37_0 = arg_37_0:GetCommanderHome()

	if var_37_0 then
		return var_37_0:CommanderInHome(arg_37_1)
	end

	return false
end

function var_0_0.UpdateOpenCommanderScene(arg_38_0, arg_38_1)
	arg_38_0.openCommanderScene = arg_38_1
end

function var_0_0.InCommanderScene(arg_39_0)
	return arg_39_0.openCommanderScene
end

function var_0_0.AnyPoolIsWaiting(arg_40_0)
	local var_40_0 = 0

	for iter_40_0, iter_40_1 in pairs(arg_40_0.boxes) do
		local var_40_1 = iter_40_1:getState()

		if var_40_1 == CommanderBox.STATE_WAITING or var_40_1 == CommanderBox.STATE_STARTING then
			return false
		end

		if var_40_1 == CommanderBox.STATE_FINISHED then
			var_40_0 = var_40_0 + 1
		end
	end

	return var_40_0 > 0
end

function var_0_0.ShouldTipBox(arg_41_0)
	local function var_41_0()
		local var_42_0 = 0

		for iter_42_0, iter_42_1 in pairs(arg_41_0.pools) do
			var_42_0 = var_42_0 + iter_42_1:getItemCount()
		end

		return var_42_0 > 0
	end

	local function var_41_1()
		for iter_43_0, iter_43_1 in pairs(arg_41_0.boxes) do
			if iter_43_1:getState() == CommanderBox.STATE_EMPTY then
				return true
			end
		end

		return false
	end

	if var_41_0() then
		if var_41_1() then
			return true
		else
			return arg_41_0:IsFinishAllBox()
		end
	else
		return arg_41_0:IsFinishAllBox()
	end
end

function var_0_0.CalcQuickItemUsageCnt(arg_44_0)
	local var_44_0 = Item.COMMANDER_QUICKLY_TOOL_ID
	local var_44_1 = Item.getConfigData(var_44_0).usage_arg[1]

	local function var_44_2(arg_45_0, arg_45_1)
		local var_45_0 = arg_45_1 - arg_45_0

		return math.ceil(var_45_0 / var_44_1)
	end

	local var_44_3 = getProxy(BagProxy):getItemCountById(var_44_0)
	local var_44_4 = 0
	local var_44_5 = 0
	local var_44_6 = 0
	local var_44_7 = {}
	local var_44_8 = {}

	for iter_44_0, iter_44_1 in pairs(arg_44_0.boxes) do
		table.insert(var_44_8, iter_44_1)
	end

	table.sort(var_44_8, function(arg_46_0, arg_46_1)
		local var_46_0 = arg_46_0.state
		local var_46_1 = arg_46_1.state

		if var_46_0 == var_46_1 then
			return arg_46_0.index < arg_46_1.index
		else
			return var_46_1 < var_46_0
		end
	end)

	for iter_44_2, iter_44_3 in ipairs(var_44_8) do
		local var_44_9 = var_44_6
		local var_44_10 = iter_44_3:getState()

		if var_44_10 == CommanderBox.STATE_WAITING then
			var_44_4 = var_44_4 + 1
			var_44_6 = var_44_6 + 1

			table.insert(var_44_7, iter_44_3)

			var_44_5 = var_44_5 + var_44_2(iter_44_3.beginTime, iter_44_3.finishTime)
		elseif var_44_10 == CommanderBox.STATE_STARTING then
			var_44_4 = var_44_4 + 1
			var_44_6 = var_44_6 + 1

			table.insert(var_44_7, iter_44_3)

			local var_44_11 = pg.TimeMgr.GetInstance():GetServerTime()

			var_44_5 = var_44_5 + var_44_2(var_44_11, iter_44_3.finishTime)
		end

		if var_44_5 == var_44_3 then
			break
		elseif var_44_3 < var_44_5 then
			var_44_5 = var_44_3
			var_44_6 = var_44_6 - 1

			table.remove(var_44_7, #var_44_7)

			break
		end
	end

	local var_44_12 = {
		0,
		0,
		0
	}

	for iter_44_4, iter_44_5 in ipairs(var_44_7) do
		local var_44_13 = iter_44_5.pool:getRarity()

		var_44_12[var_44_13] = var_44_12[var_44_13] + 1
	end

	return var_44_5, var_44_4, var_44_6, var_44_12
end

return var_0_0
