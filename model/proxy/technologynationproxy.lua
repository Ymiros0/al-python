﻿local var_0_0 = class("TechnologyNationProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0.typeAttrTable = {}
	arg_1_0.typeOrder = {}
	arg_1_0.typeAttrOrderTable = {}
	arg_1_0.groupListInCount = {}
	arg_1_0.nationToPoint = {}
	arg_1_0.ifShowRedPoint = false
	arg_1_0.techList = {}

	arg_1_0:on(64000, function(arg_2_0)
		for iter_2_0, iter_2_1 in ipairs(arg_2_0.tech_list) do
			arg_1_0.techList[iter_2_1.group_id] = {
				completeID = iter_2_1.effect_tech_id,
				studyID = iter_2_1.study_tech_id,
				finishTime = iter_2_1.study_finish_time,
				rewardedID = iter_2_1.rewarded_tech
			}
		end

		arg_1_0:flushData()
		arg_1_0:setTimer()
		arg_1_0:initSetableAttrAddition(arg_2_0.techset_list)
	end)

	if IsUnityEditor then
		local var_1_0 = {
			ShipType.FengFanM,
			ShipType.FengFanS,
			ShipType.FengFanV
		}

		local function var_1_1(arg_3_0)
			if #var_1_0 ~= #arg_3_0 then
				return false
			end

			local var_3_0 = {}
			local var_3_1 = {}

			for iter_3_0, iter_3_1 in ipairs(var_1_0) do
				var_3_0[iter_3_1] = (var_3_0[iter_3_1] or 0) + 1
			end

			for iter_3_2, iter_3_3 in ipairs(arg_3_0) do
				var_3_1[iter_3_3] = (var_3_1[iter_3_3] or 0) + 1
			end

			for iter_3_4, iter_3_5 in pairs(var_3_0) do
				if var_3_1[iter_3_4] ~= iter_3_5 then
					return false
				end
			end

			return true
		end

		for iter_1_0, iter_1_1 in ipairs(pg.fleet_tech_ship_class.all) do
			if pg.fleet_tech_ship_class[iter_1_1].nation == Nation.MOT then
				local var_1_2 = pg.fleet_tech_ship_template[iter_1_1]
				local var_1_3 = var_1_2.add_get_shiptype
				local var_1_4 = var_1_2.add_level_shiptype

				if not var_1_1(var_1_3) then
					assert(false, "请检查fleet_tech_ship_class中的add_get_shiptype， ID：" .. iter_1_1)
				end

				if not var_1_1(var_1_4) then
					assert(false, "请检查fleet_tech_ship_class中的add_level_shiptype， ID：" .. iter_1_1)
				end
			end
		end
	end
end

function var_0_0.flushData(arg_4_0)
	arg_4_0:shipGroupFilter()
	arg_4_0:nationPointFilter()
	arg_4_0:calculateTecBuff()
	arg_4_0:refreshRedPoint()
end

function var_0_0.updateTecItem(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4, arg_5_5)
	if not arg_5_0.techList[arg_5_1] then
		arg_5_0.techList[arg_5_1] = {
			completeID = 0,
			rewardedID = 0,
			studyID = arg_5_3,
			finishTime = arg_5_4
		}

		return
	end

	arg_5_0.techList[arg_5_1] = {
		completeID = arg_5_2 or arg_5_0.techList[arg_5_1].completeID,
		studyID = arg_5_3,
		finishTime = arg_5_4,
		rewardedID = arg_5_5 or arg_5_0.techList[arg_5_1].rewardedID
	}
end

function var_0_0.updateTecItemAward(arg_6_0, arg_6_1, arg_6_2)
	arg_6_0.techList[arg_6_1].rewardedID = arg_6_2
end

function var_0_0.updateTecItemAwardOneStep(arg_7_0)
	for iter_7_0, iter_7_1 in pairs(arg_7_0.techList) do
		iter_7_1.rewardedID = iter_7_1.completeID
	end
end

function var_0_0.shipGroupFilter(arg_8_0)
	arg_8_0.groupListInCount = {}

	local var_8_0 = getProxy(CollectionProxy).shipGroups

	for iter_8_0, iter_8_1 in pairs(var_8_0) do
		if pg.fleet_tech_ship_template[iter_8_1.id] then
			table.insert(arg_8_0.groupListInCount, iter_8_1)
		end
	end
end

function var_0_0.nationPointFilter(arg_9_0)
	local var_9_0 = {
		Nation.US,
		Nation.EN,
		Nation.JP,
		Nation.DE,
		Nation.CN,
		Nation.ITA,
		Nation.SN,
		Nation.FF,
		Nation.MNF,
		Nation.FR,
		Nation.META
	}

	if not LOCK_TEC_MOT then
		table.insert(var_9_0, Nation.MOT)
	end

	arg_9_0.nationToPoint = {}
	arg_9_0.nationToPointLog = {}
	arg_9_0.nationToPointLog2 = {}

	for iter_9_0, iter_9_1 in ipairs(var_9_0) do
		arg_9_0.nationToPoint[iter_9_1] = 0
		arg_9_0.nationToPointLog[iter_9_1] = {
			{},
			{},
			{}
		}
		arg_9_0.nationToPointLog2[iter_9_1] = {}
	end

	for iter_9_2, iter_9_3 in ipairs(arg_9_0.groupListInCount) do
		local var_9_1 = iter_9_3:getNation()
		local var_9_2 = iter_9_3.id

		if var_9_1 ~= tonumber(string.sub(tostring(var_9_2), 1, 1)) then
			table.insert(arg_9_0.nationToPointLog2[var_9_1], iter_9_3)
		end

		local var_9_3 = pg.fleet_tech_ship_template[var_9_2]
		local var_9_4 = 0 + var_9_3.pt_get

		table.insert(arg_9_0.nationToPointLog[var_9_1][1], var_9_2)

		if iter_9_3.maxLV and iter_9_3.maxLV >= TechnologyConst.SHIP_LEVEL_FOR_BUFF then
			var_9_4 = var_9_4 + var_9_3.pt_level

			table.insert(arg_9_0.nationToPointLog[var_9_1][2], var_9_2)
		end

		if iter_9_3.star >= var_9_3.max_star then
			var_9_4 = var_9_4 + var_9_3.pt_upgrage

			table.insert(arg_9_0.nationToPointLog[var_9_1][3], var_9_2)
		end

		arg_9_0.nationToPoint[var_9_1] = arg_9_0.nationToPoint[var_9_1] + var_9_4
	end

	arg_9_0.point = 0

	for iter_9_4, iter_9_5 in pairs(arg_9_0.nationToPoint) do
		arg_9_0.point = arg_9_0.point + iter_9_5
	end
end

function var_0_0.calculateTecBuff(arg_10_0)
	arg_10_0.typeBuffList = {}
	arg_10_0.typeOrder = {}

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.groupListInCount) do
		local var_10_0 = iter_10_1.id
		local var_10_1 = pg.fleet_tech_ship_template[var_10_0].add_get_shiptype
		local var_10_2 = pg.fleet_tech_ship_template[var_10_0].add_get_attr
		local var_10_3 = pg.fleet_tech_ship_template[var_10_0].add_get_value

		for iter_10_2, iter_10_3 in ipairs(var_10_1) do
			if not arg_10_0.typeBuffList[iter_10_3] then
				arg_10_0.typeBuffList[iter_10_3] = {
					{
						var_10_2,
						var_10_3
					}
				}
				arg_10_0.typeOrder[#arg_10_0.typeOrder + 1] = iter_10_3
			else
				arg_10_0.typeBuffList[iter_10_3][#arg_10_0.typeBuffList[iter_10_3] + 1] = {
					var_10_2,
					var_10_3
				}
			end
		end

		if iter_10_1.maxLV >= TechnologyConst.SHIP_LEVEL_FOR_BUFF then
			local var_10_4 = pg.fleet_tech_ship_template[var_10_0].add_level_shiptype
			local var_10_5 = pg.fleet_tech_ship_template[var_10_0].add_level_attr
			local var_10_6 = pg.fleet_tech_ship_template[var_10_0].add_level_value

			for iter_10_4, iter_10_5 in ipairs(var_10_4) do
				if not arg_10_0.typeBuffList[iter_10_5] then
					arg_10_0.typeBuffList[iter_10_5] = {
						{
							var_10_5,
							var_10_6
						}
					}
					arg_10_0.typeOrder[#arg_10_0.typeOrder + 1] = iter_10_5
				else
					arg_10_0.typeBuffList[iter_10_5][#arg_10_0.typeBuffList[iter_10_5] + 1] = {
						var_10_5,
						var_10_6
					}
				end
			end
		end
	end

	for iter_10_6, iter_10_7 in pairs(arg_10_0.techList) do
		if iter_10_7.completeID ~= 0 then
			local var_10_7 = pg.fleet_tech_template[iter_10_7.completeID].add

			for iter_10_8, iter_10_9 in ipairs(var_10_7) do
				local var_10_8 = iter_10_9[1]
				local var_10_9 = iter_10_9[2]
				local var_10_10 = iter_10_9[3]

				for iter_10_10, iter_10_11 in ipairs(var_10_8) do
					if not arg_10_0.typeBuffList[iter_10_11] then
						arg_10_0.typeBuffList[iter_10_11] = {
							{
								var_10_9,
								var_10_10
							}
						}
						arg_10_0.typeOrder[#arg_10_0.typeOrder + 1] = iter_10_11
					else
						arg_10_0.typeBuffList[iter_10_11][#arg_10_0.typeBuffList[iter_10_11] + 1] = {
							var_10_9,
							var_10_10
						}
					end
				end
			end
		end
	end

	arg_10_0.typeAttrTable = {}
	arg_10_0.typeAttrOrderTable = {}

	for iter_10_12, iter_10_13 in pairs(arg_10_0.typeBuffList) do
		if not arg_10_0.typeAttrTable[iter_10_12] then
			arg_10_0.typeAttrTable[iter_10_12] = {}
			arg_10_0.typeAttrOrderTable[iter_10_12] = {}
		end

		for iter_10_14, iter_10_15 in ipairs(iter_10_13) do
			local var_10_11 = iter_10_15[1]
			local var_10_12 = iter_10_15[2]

			if not arg_10_0.typeAttrTable[iter_10_12][var_10_11] then
				arg_10_0.typeAttrTable[iter_10_12][var_10_11] = var_10_12
				arg_10_0.typeAttrOrderTable[iter_10_12][#arg_10_0.typeAttrOrderTable[iter_10_12] + 1] = var_10_11
			else
				arg_10_0.typeAttrTable[iter_10_12][var_10_11] = arg_10_0.typeAttrTable[iter_10_12][var_10_11] + var_10_12
			end
		end
	end

	table.sort(arg_10_0.typeOrder, function(arg_11_0, arg_11_1)
		return arg_11_0 < arg_11_1
	end)

	for iter_10_16, iter_10_17 in pairs(arg_10_0.typeAttrOrderTable) do
		table.sort(iter_10_17, function(arg_12_0, arg_12_1)
			return arg_12_0 < arg_12_1
		end)
	end
end

function var_0_0.setTimer(arg_13_0)
	for iter_13_0, iter_13_1 in pairs(arg_13_0.techList) do
		if iter_13_1.studyID ~= 0 then
			local var_13_0 = iter_13_1.finishTime
			local var_13_1 = pg.TimeMgr.GetInstance():GetServerTime()
			local var_13_2 = table.indexof(pg.fleet_tech_group[iter_13_0].techs, iter_13_1.completeID, 1) or 0
			local var_13_3 = pg.fleet_tech_group[iter_13_0].techs[var_13_2 + 1]

			if var_13_0 < var_13_1 then
				arg_13_0:sendNotification(GAME.FINISH_CAMP_TEC, {
					tecID = iter_13_0,
					levelID = var_13_3
				})

				return
			else
				onDelayTick(function()
					arg_13_0:sendNotification(GAME.FINISH_CAMP_TEC, {
						tecID = iter_13_0,
						levelID = var_13_3
					})
				end, var_13_0 - var_13_1)

				return
			end
		end
	end
end

function var_0_0.refreshRedPoint(arg_15_0)
	arg_15_0.ifShowRedPoint = false

	for iter_15_0, iter_15_1 in pairs(arg_15_0.techList) do
		if iter_15_1.studyID ~= 0 then
			if iter_15_1.finishTime < pg.TimeMgr.GetInstance():GetServerTime() then
				arg_15_0.ifShowRedPoint = true

				return
			else
				return
			end
		end
	end

	for iter_15_2, iter_15_3 in ipairs(pg.fleet_tech_group.all) do
		if not arg_15_0.techList[iter_15_3] or arg_15_0.techList[iter_15_3].studyID == 0 then
			local var_15_0 = arg_15_0:getLevelByTecID(iter_15_3)

			if var_15_0 < #pg.fleet_tech_group[iter_15_3].techs then
				local var_15_1 = pg.fleet_tech_group[iter_15_3].nation[1]
				local var_15_2 = pg.fleet_tech_group[iter_15_3].techs[var_15_0 + 1]

				if arg_15_0.nationToPoint[var_15_1] >= pg.fleet_tech_template[var_15_2].pt then
					arg_15_0.ifShowRedPoint = true

					break
				end
			end
		end
	end

	arg_15_0.ifShowRedPoint = arg_15_0:isAnyTecCampCanGetAward()
end

function var_0_0.isAnyTecCampCanGetAward(arg_16_0)
	local var_16_0 = false

	if not LOCK_TEC_NATION_AWARD then
		for iter_16_0, iter_16_1 in pairs(arg_16_0.techList) do
			local var_16_1 = pg.fleet_tech_group[iter_16_0]
			local var_16_2 = iter_16_1.rewardedID
			local var_16_3 = iter_16_1.completeID

			if (table.indexof(var_16_1.techs, var_16_2, 1) or 0) < (table.indexof(var_16_1.techs, var_16_3, 1) or 0) then
				var_16_0 = true

				break
			end
		end
	end

	return var_16_0
end

function var_0_0.GetTecList(arg_17_0)
	return arg_17_0.techList
end

function var_0_0.GetTecItemByGroupID(arg_18_0, arg_18_1)
	return arg_18_0.techList[arg_18_1]
end

function var_0_0.getLevelByTecID(arg_19_0, arg_19_1)
	local var_19_0

	return not arg_19_0.techList[arg_19_1] and 0 or table.indexof(pg.fleet_tech_group[arg_19_1].techs, arg_19_0.techList[arg_19_1].completeID, 1) or 0
end

function var_0_0.getGroupListInCount(arg_20_0)
	return arg_20_0.groupListInCount
end

function var_0_0.getShowRedPointTag(arg_21_0)
	return arg_21_0.ifShowRedPoint
end

function var_0_0.getStudyingTecItem(arg_22_0)
	for iter_22_0, iter_22_1 in pairs(arg_22_0.techList) do
		if iter_22_1.studyID ~= 0 then
			return iter_22_0
		end
	end

	return nil
end

function var_0_0.getPoint(arg_23_0)
	return arg_23_0.point
end

function var_0_0.getNationPointList(arg_24_0)
	return arg_24_0.nationToPoint
end

function var_0_0.getNationPoint(arg_25_0, arg_25_1)
	return arg_25_0.nationToPoint[arg_25_1]
end

function var_0_0.getLeftTime(arg_26_0)
	local var_26_0 = arg_26_0.techList[arg_26_0:getStudyingTecItem()]

	if var_26_0 then
		local var_26_1 = var_26_0.finishTime - pg.TimeMgr.GetInstance():GetServerTime()

		return var_26_1 > 0 and var_26_1 or 0
	else
		return 0
	end
end

function var_0_0.getTecBuff(arg_27_0)
	if OPEN_TEC_TREE_SYSTEM then
		return arg_27_0.typeAttrTable, arg_27_0.typeOrder, arg_27_0.typeAttrOrderTable
	end
end

function var_0_0.getShipAddition(arg_28_0, arg_28_1, arg_28_2)
	local var_28_0 = table.indexof(TechnologyConst.TECH_NATION_ATTRS, arg_28_2)
	local var_28_1 = 0
	local var_28_2 = (arg_28_0:getTecBuff() or {})[arg_28_1]

	if var_28_2 and var_28_0 and var_28_2[var_28_0] then
		var_28_1 = arg_28_0:getSetableAttrAdditionValueByTypeAttr(arg_28_1, var_28_0)
	end

	return var_28_1
end

function var_0_0.getShipMaxAddition(arg_29_0, arg_29_1, arg_29_2)
	local var_29_0 = table.indexof(TechnologyConst.TECH_NATION_ATTRS, arg_29_2)
	local var_29_1 = 0
	local var_29_2 = (arg_29_0:getTecBuff() or {})[arg_29_1]

	if var_29_2 and var_29_0 and var_29_2[var_29_0] then
		var_29_1 = var_29_2[var_29_0]
	end

	return var_29_1
end

function var_0_0.printNationPointLog(arg_30_0)
	for iter_30_0, iter_30_1 in pairs(arg_30_0.nationToPointLog) do
		print("----------------" .. iter_30_0 .. "----------------")

		for iter_30_2, iter_30_3 in ipairs(iter_30_1) do
			local var_30_0 = iter_30_2 .. "    :"

			for iter_30_4, iter_30_5 in ipairs(iter_30_3) do
				var_30_0 = var_30_0 .. "  " .. iter_30_5
			end

			print(var_30_0)
		end
	end

	print("----------------Filte----------------")

	for iter_30_6, iter_30_7 in pairs(arg_30_0.nationToPointLog2) do
		local var_30_1 = iter_30_6 .. " :"

		for iter_30_8, iter_30_9 in ipairs(iter_30_7) do
			local var_30_2 = iter_30_9.id
			local var_30_3 = iter_30_9:getNation()
			local var_30_4

			for iter_30_10 = 4, 1, -1 do
				if pg.ship_data_statistics[tonumber(var_30_2 .. iter_30_10)] then
					var_30_4 = pg.ship_data_statistics[tonumber(var_30_2 .. iter_30_10)].nationality
				end
			end

			var_30_1 = var_30_1 .. tostring(var_30_2) .. " " .. tostring(var_30_3) .. " " .. tostring(var_30_4) .. "||"
		end

		print(var_30_1)
	end
end

function var_0_0.initSetableAttrAddition(arg_31_0, arg_31_1)
	arg_31_0.setValueTypeAttrTable = {}

	for iter_31_0, iter_31_1 in ipairs(arg_31_1) do
		local var_31_0 = iter_31_1.ship_type
		local var_31_1 = iter_31_1.attr_type
		local var_31_2 = iter_31_1.set_value

		if not arg_31_0.setValueTypeAttrTable[var_31_0] then
			arg_31_0.setValueTypeAttrTable[var_31_0] = {}
		end

		arg_31_0.setValueTypeAttrTable[var_31_0][var_31_1] = var_31_2
	end
end

function var_0_0.getSetableAttrAddition(arg_32_0)
	return arg_32_0.setValueTypeAttrTable
end

function var_0_0.getSetableAttrAdditionValueByTypeAttr(arg_33_0, arg_33_1, arg_33_2)
	if arg_33_0.setValueTypeAttrTable[arg_33_1] and arg_33_0.setValueTypeAttrTable[arg_33_1][arg_33_2] then
		return arg_33_0.setValueTypeAttrTable[arg_33_1][arg_33_2]
	else
		return arg_33_0.typeAttrTable[arg_33_1][arg_33_2]
	end
end

return var_0_0
