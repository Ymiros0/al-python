local var_0_0 = class("TechnologyProxy", import(".NetProxy"))

var_0_0.TECHNOLOGY_UPDATED = "TechnologyProxy:TECHNOLOGY_UPDATED"
var_0_0.BLUEPRINT_ADDED = "TechnologyProxy:BLUEPRINT_ADDED"
var_0_0.BLUEPRINT_UPDATED = "TechnologyProxy:BLUEPRINT_UPDATED"
var_0_0.REFRESH_UPDATED = "TechnologyProxy:REFRESH_UPDATED"

function var_0_0.register(arg_1_0)
	arg_1_0.tendency = {}

	arg_1_0:on(63000, function(arg_2_0)
		arg_1_0:updateTechnologys(arg_2_0.refresh_list)

		arg_1_0.refreshTechnologysFlag = arg_2_0.refresh_flag

		arg_1_0:updateTecCatchup(arg_2_0.catchup)
		arg_1_0:updateTechnologyQueue(arg_2_0.queue)
	end)

	arg_1_0.bluePrintData = {}
	arg_1_0.item2blueprint = {}
	arg_1_0.maxConfigVersion = 0

	_.each(pg.ship_data_blueprint.all, function(arg_3_0)
		local var_3_0 = ShipBluePrint.New({
			id = arg_3_0
		})

		arg_1_0.maxConfigVersion = math.max(arg_1_0.maxConfigVersion, var_3_0:getConfig("blueprint_version"))
		arg_1_0.bluePrintData[var_3_0.id] = var_3_0
		arg_1_0.item2blueprint[var_3_0:getItemId()] = var_3_0.id
	end)
	arg_1_0:on(63100, function(arg_4_0)
		for iter_4_0, iter_4_1 in ipairs(arg_4_0.blueprint_list) do
			local var_4_0 = arg_1_0.bluePrintData[iter_4_1.id]

			assert(var_4_0, "miss config ship_data_blueprint>>>>>>>>" .. iter_4_1.id)
			var_4_0:updateInfo(iter_4_1)
		end

		arg_1_0.coldTime = arg_4_0.cold_time or 0
		arg_1_0.pursuingTimes = arg_4_0.daily_catchup_strengthen or 0
		arg_1_0.pursuingTimesUR = arg_4_0.daily_catchup_strengthen_ur or 0
	end)
end

function var_0_0.setVersion(arg_5_0, arg_5_1)
	PlayerPrefs.SetInt("technology_version", arg_5_1)
	PlayerPrefs.Save()
end

function var_0_0.getVersion(arg_6_0)
	if not PlayerPrefs.HasKey("technology_version") then
		arg_6_0:setVersion(1)

		return 1
	else
		return PlayerPrefs.GetInt("technology_version")
	end
end

function var_0_0.getConfigMaxVersion(arg_7_0)
	return arg_7_0.maxConfigVersion
end

function var_0_0.setTendency(arg_8_0, arg_8_1, arg_8_2)
	arg_8_0.tendency[arg_8_1] = arg_8_2
end

function var_0_0.getTendency(arg_9_0, arg_9_1)
	return arg_9_0.tendency[arg_9_1]
end

function var_0_0.updateBlueprintStates(arg_10_0)
	for iter_10_0, iter_10_1 in pairs(arg_10_0.bluePrintData or {}) do
		iter_10_1:updateState()
	end
end

function var_0_0.getColdTime(arg_11_0)
	return arg_11_0.coldTime
end

function var_0_0.updateColdTime(arg_12_0)
	arg_12_0.coldTime = pg.TimeMgr.GetInstance():GetServerTime() + 86400
end

function var_0_0.updateRefreshFlag(arg_13_0, arg_13_1)
	arg_13_0.refreshTechnologysFlag = arg_13_1

	arg_13_0:sendNotification(var_0_0.REFRESH_UPDATED, arg_13_0.refreshTechnologysFlag)
end

function var_0_0.updateTechnologys(arg_14_0, arg_14_1)
	arg_14_0.data = {}

	for iter_14_0, iter_14_1 in ipairs(arg_14_1) do
		arg_14_0.tendency[iter_14_1.id] = iter_14_1.target

		for iter_14_2, iter_14_3 in ipairs(iter_14_1.technologys) do
			arg_14_0.data[iter_14_3.id] = Technology.New({
				id = iter_14_3.id,
				time = iter_14_3.time,
				pool_id = iter_14_1.id
			})
		end
	end
end

function var_0_0.updateTecCatchup(arg_15_0, arg_15_1)
	arg_15_0.curCatchupTecID = arg_15_1.version
	arg_15_0.curCatchupGroupID = arg_15_1.target
	arg_15_0.catchupData = {}

	for iter_15_0, iter_15_1 in ipairs(arg_15_1.pursuings) do
		local var_15_0 = TechnologyCatchup.New(iter_15_1)

		arg_15_0.catchupData[var_15_0.id] = var_15_0
	end

	arg_15_0.curCatchupPrintsNum = arg_15_0:getCurCatchNum()

	print("初始下发的科研追赶信息", arg_15_0.curCatchupTecID, arg_15_0.curCatchupGroupID, arg_15_0.curCatchupPrintsNum)
end

function var_0_0.updateTechnologyQueue(arg_16_0, arg_16_1)
	arg_16_0.queue = {}

	for iter_16_0, iter_16_1 in ipairs(arg_16_1) do
		table.insert(arg_16_0.queue, Technology.New({
			queue = true,
			id = iter_16_1.id,
			time = iter_16_1.time
		}))
	end

	table.sort(arg_16_0.queue, function(arg_17_0, arg_17_1)
		return arg_17_0.time < arg_17_1.time
	end)
end

function var_0_0.moveTechnologyToQueue(arg_18_0, arg_18_1)
	local var_18_0 = arg_18_0.data[arg_18_1]

	var_18_0.inQueue = true

	table.insert(arg_18_0.queue, var_18_0)

	arg_18_0.data[arg_18_1] = nil
end

function var_0_0.removeFirstQueueTechnology(arg_19_0)
	assert(#arg_19_0.queue > 0)
	table.remove(arg_19_0.queue, 1)
end

function var_0_0.getActivateTechnology(arg_20_0)
	for iter_20_0, iter_20_1 in pairs(arg_20_0.data or {}) do
		if iter_20_1:isActivate() then
			return Clone(iter_20_1)
		end
	end
end

function var_0_0.getTechnologyById(arg_21_0, arg_21_1)
	assert(arg_21_0.data[arg_21_1], "technology should exist>>" .. arg_21_1)

	return arg_21_0.data[arg_21_1]:clone()
end

function var_0_0.updateTechnology(arg_22_0, arg_22_1)
	assert(arg_22_0.data[arg_22_1.id], "technology should exist>>" .. arg_22_1.id)
	assert(isa(arg_22_1, Technology), "technology should be instance of Technology")

	arg_22_0.data[arg_22_1.id] = arg_22_1

	arg_22_0:sendNotification(var_0_0.TECHNOLOGY_UPDATED, arg_22_1:clone())
end

function var_0_0.getTechnologys(arg_23_0)
	return underscore.values(arg_23_0.data)
end

function var_0_0.getPlanningTechnologys(arg_24_0)
	return table.mergeArray(arg_24_0.queue, {
		arg_24_0:getActivateTechnology()
	})
end

function var_0_0.getBluePrints(arg_25_0)
	return Clone(arg_25_0.bluePrintData)
end

function var_0_0.getBluePrintById(arg_26_0, arg_26_1)
	return Clone(arg_26_0.bluePrintData[arg_26_1])
end

function var_0_0.getRawBluePrintById(arg_27_0, arg_27_1)
	return arg_27_0.bluePrintData[arg_27_1]
end

function var_0_0.addBluePrint(arg_28_0, arg_28_1)
	assert(isa(arg_28_1, ShipBluePrint), "bluePrint should be instance of ShipBluePrint")
	assert(arg_28_0.bluePrintData[arg_28_1.id] == nil, "use function updateBluePrint instead")

	arg_28_0.bluePrintData[arg_28_1.id] = arg_28_1

	arg_28_0:sendNotification(var_0_0.BLUEPRINT_ADDED, arg_28_1:clone())
end

function var_0_0.updateBluePrint(arg_29_0, arg_29_1)
	assert(isa(arg_29_1, ShipBluePrint), "bluePrint should be instance of ShipBluePrint")
	assert(arg_29_0.bluePrintData[arg_29_1.id], "use function addBluePrint instead")

	arg_29_0.bluePrintData[arg_29_1.id] = arg_29_1

	arg_29_0:sendNotification(var_0_0.BLUEPRINT_UPDATED, arg_29_1:clone())
end

function var_0_0.getBuildingBluePrint(arg_30_0)
	for iter_30_0, iter_30_1 in pairs(arg_30_0.bluePrintData) do
		if iter_30_1:isDeving() or iter_30_1:isFinished() then
			return iter_30_1
		end
	end
end

function var_0_0.GetBlueprint4Item(arg_31_0, arg_31_1)
	return arg_31_0.item2blueprint[arg_31_1]
end

function var_0_0.getCatchupData(arg_32_0, arg_32_1)
	if not arg_32_0.catchupData[arg_32_1] then
		local var_32_0 = TechnologyCatchup.New({
			version = arg_32_1
		})

		arg_32_0.catchupData[arg_32_1] = var_32_0
	end

	return arg_32_0.catchupData[arg_32_1]
end

function var_0_0.updateCatchupData(arg_33_0, arg_33_1, arg_33_2, arg_33_3)
	arg_33_0.catchupData[arg_33_1]:addTargetNum(arg_33_2, arg_33_3)
end

function var_0_0.getCurCatchNum(arg_34_0)
	if arg_34_0.curCatchupTecID ~= 0 and arg_34_0.curCatchupGroupID ~= 0 then
		return arg_34_0.catchupData[arg_34_0.curCatchupTecID]:getTargetNum(arg_34_0.curCatchupGroupID)
	else
		return 0
	end
end

function var_0_0.getCatchupState(arg_35_0, arg_35_1)
	if not arg_35_0.catchupData[arg_35_1] then
		return TechnologyCatchup.STATE_UNSELECT
	end

	return arg_35_0.catchupData[arg_35_1]:getState()
end

function var_0_0.updateCatchupStates(arg_36_0)
	for iter_36_0, iter_36_1 in pairs(arg_36_0.catchupData) do
		iter_36_1:updateState()
	end
end

function var_0_0.isOpenTargetCatchup(arg_37_0)
	return pg.technology_catchup_template ~= nil and #pg.technology_catchup_template.all > 0
end

function var_0_0.getNewestCatchupTecID(arg_38_0)
	return math.max(unpack(pg.technology_catchup_template.all))
end

function var_0_0.isOnCatchup(arg_39_0)
	return arg_39_0.curCatchupTecID ~= 0 and arg_39_0.curCatchupGroupID ~= 0
end

function var_0_0.getBluePrintVOByGroupID(arg_40_0, arg_40_1)
	return arg_40_0.bluePrintData[arg_40_1]
end

function var_0_0.getCurCatchupTecInfo(arg_41_0)
	return {
		tecID = arg_41_0.curCatchupTecID,
		groupID = arg_41_0.curCatchupGroupID,
		printNum = arg_41_0.curCatchupPrintsNum
	}
end

function var_0_0.setCurCatchupTecInfo(arg_42_0, arg_42_1, arg_42_2)
	arg_42_0.curCatchupTecID = arg_42_1
	arg_42_0.curCatchupGroupID = arg_42_2
	arg_42_0.curCatchupPrintsNum = arg_42_0:getCurCatchNum()

	arg_42_0:updateCatchupStates()
	print("设置后的科研追赶信息", arg_42_0.curCatchupTecID, arg_42_0.curCatchupGroupID, arg_42_0.curCatchupPrintsNum)
end

function var_0_0.addCatupPrintsNum(arg_43_0, arg_43_1)
	arg_43_0:updateCatchupData(arg_43_0.curCatchupTecID, arg_43_0.curCatchupGroupID, arg_43_1)

	arg_43_0.curCatchupPrintsNum = arg_43_0:getCurCatchNum()

	print("增加科研图纸", arg_43_1, arg_43_0.curCatchupPrintsNum)
end

function var_0_0.IsShowTip(arg_44_0)
	local var_44_0 = SelectTechnologyMediator.onTechnologyNotify()
	local var_44_1 = SelectTechnologyMediator.onBlueprintNotify()
	local var_44_2, var_44_3 = pg.SystemOpenMgr.GetInstance():isOpenSystem(getProxy(PlayerProxy):getData().level, "TechnologyMediator")

	return OPEN_TEC_TREE_SYSTEM and getProxy(TechnologyNationProxy):getShowRedPointTag() or (var_44_1 or var_44_0) and var_44_2
end

function var_0_0.addPursuingTimes(arg_45_0, arg_45_1, arg_45_2)
	if arg_45_2 then
		arg_45_0.pursuingTimesUR = arg_45_0.pursuingTimesUR + arg_45_1
	else
		arg_45_0.pursuingTimes = arg_45_0.pursuingTimes + arg_45_1
	end
end

function var_0_0.resetPursuingTimes(arg_46_0)
	arg_46_0.pursuingTimes = 0
	arg_46_0.pursuingTimesUR = 0

	arg_46_0:sendNotification(GAME.PURSUING_RESET_DONE)
end

function var_0_0.getPursuingTimes(arg_47_0, arg_47_1)
	if arg_47_1 then
		return arg_47_0.pursuingTimesUR
	else
		return arg_47_0.pursuingTimes
	end
end

function var_0_0.calcMaxPursuingCount(arg_48_0, arg_48_1)
	local var_48_0 = pg.gameset[arg_48_1:isRarityUR() and "blueprint_pursue_discount_ur" or "blueprint_pursue_discount_ssr"].description
	local var_48_1 = getProxy(PlayerProxy):getRawData():getResource(PlayerConst.ResGold)
	local var_48_2 = 0

	local function var_48_3(arg_49_0)
		local var_49_0 = #var_48_0

		while arg_49_0 < var_48_0[var_49_0][1] do
			var_49_0 = var_49_0 - 1
		end

		return var_48_0[var_49_0][2]
	end

	local var_48_4

	for iter_48_0 = arg_48_0:getPursuingTimes(arg_48_1:isRarityUR()) + 1, var_48_0[#var_48_0][1] - 1 do
		local var_48_5 = arg_48_1:getPursuingPrice(var_48_3(iter_48_0))

		if var_48_1 < var_48_5 then
			return var_48_2
		else
			var_48_1 = var_48_1 - var_48_5
			var_48_2 = var_48_2 + 1
		end
	end

	return var_48_2 + math.floor(var_48_1 / arg_48_1:getPursuingPrice())
end

function var_0_0.calcPursuingCost(arg_50_0, arg_50_1, arg_50_2)
	local var_50_0 = pg.gameset[arg_50_1:isRarityUR() and "blueprint_pursue_discount_ur" or "blueprint_pursue_discount_ssr"].description
	local var_50_1 = 0

	local function var_50_2(arg_51_0)
		local var_51_0 = #var_50_0

		while arg_51_0 < var_50_0[var_51_0][1] do
			var_51_0 = var_51_0 - 1
		end

		return var_50_0[var_51_0][2]
	end

	local var_50_3

	for iter_50_0 = arg_50_0:getPursuingTimes(arg_50_1:isRarityUR()) + 1, var_50_0[#var_50_0][1] - 1 do
		local var_50_4 = arg_50_1:getPursuingPrice(var_50_2(iter_50_0))

		if arg_50_2 == 0 then
			return var_50_1
		else
			var_50_1 = var_50_1 + var_50_4
			arg_50_2 = arg_50_2 - 1
		end
	end

	return var_50_1 + arg_50_2 * arg_50_1:getPursuingPrice()
end

function var_0_0.getPursuingDiscount(arg_52_0, arg_52_1)
	local var_52_0 = getGameset(arg_52_1 and "blueprint_pursue_discount_ur" or "blueprint_pursue_discount_ssr")[2]
	local var_52_1 = #var_52_0

	while arg_52_0 < var_52_0[var_52_1][1] do
		var_52_1 = var_52_1 - 1
	end

	return var_52_0[var_52_1][2]
end

function var_0_0.getItemCanUnlockBluePrint(arg_53_0, arg_53_1)
	if not arg_53_0.unlockItemDic then
		arg_53_0.unlockItemDic = {}

		for iter_53_0, iter_53_1 in ipairs(pg.ship_data_blueprint.all) do
			local var_53_0 = arg_53_0.bluePrintData[iter_53_1]

			for iter_53_2, iter_53_3 in ipairs(var_53_0:getConfig("gain_item_id")) do
				arg_53_0.unlockItemDic[iter_53_3] = arg_53_0.unlockItemDic[iter_53_3] or {}

				table.insert(arg_53_0.unlockItemDic[iter_53_3], iter_53_1)
			end
		end
	end

	return arg_53_0.unlockItemDic[arg_53_1]
end

function var_0_0.CheckPursuingCostTip(arg_54_0, arg_54_1)
	if var_0_0.getPursuingDiscount(arg_54_0.pursuingTimes + 1, false) > 0 and var_0_0.getPursuingDiscount(arg_54_0.pursuingTimesUR + 1, true) > 0 then
		return false
	end

	local var_54_0 = {}

	if arg_54_1 then
		for iter_54_0, iter_54_1 in ipairs(arg_54_1) do
			var_54_0[iter_54_1] = true
		end
	else
		for iter_54_2 = 1, arg_54_0.maxConfigVersion do
			var_54_0[iter_54_2] = true
		end
	end

	for iter_54_3, iter_54_4 in pairs(arg_54_0.bluePrintData) do
		if var_54_0[iter_54_4:getConfig("blueprint_version")] and iter_54_4:isPursuingCostTip() then
			return true
		end
	end

	return false
end

return var_0_0
