local var_0_0 = class("ChapterOpRoutine", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	return
end

function var_0_0.initData(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	arg_2_0.op = arg_2_1
	arg_2_0.data = arg_2_2
	arg_2_0.chapter = arg_2_3
	arg_2_0.items = {}
	arg_2_0.fullpath = nil
	arg_2_0.flag = 0
	arg_2_0.extraFlag = 0
end

function var_0_0.doDropUpdate(arg_3_0)
	arg_3_0.items = PlayerConst.addTranDrop(arg_3_0.data.drop_list)
end

function var_0_0.doMapUpdate(arg_4_0)
	local var_4_0 = arg_4_0.data
	local var_4_1 = arg_4_0.flag
	local var_4_2 = arg_4_0.extraFlag
	local var_4_3 = arg_4_0.chapter

	if #var_4_0.map_update > 0 then
		_.each(var_4_0.map_update, function(arg_5_0)
			if arg_5_0.item_type == ChapterConst.AttachStory and arg_5_0.item_data == ChapterConst.StoryTrigger then
				local var_5_0 = ChapterCell.Line2Name(arg_5_0.pos.row, arg_5_0.pos.column)
				local var_5_1 = var_4_3:GetChapterCellAttachemnts()
				local var_5_2 = var_5_1[var_5_0]

				if var_5_2 then
					if var_5_2.flag == ChapterConst.CellFlagTriggerActive and arg_5_0.item_flag == ChapterConst.CellFlagTriggerDisabled then
						local var_5_3 = pg.map_event_template[var_5_2.attachmentId].gametip

						if var_5_3 ~= "" then
							pg.TipsMgr.GetInstance():ShowTips(i18n(var_5_3))
						end
					end

					var_5_2.attachment = arg_5_0.item_type
					var_5_2.attachmentId = arg_5_0.item_id
					var_5_2.flag = arg_5_0.item_flag
					var_5_2.data = arg_5_0.item_data
				else
					var_5_1[var_5_0] = ChapterCell.New(arg_5_0)
				end
			elseif arg_5_0.item_type ~= ChapterConst.AttachNone and arg_5_0.item_type ~= ChapterConst.AttachBorn and arg_5_0.item_type ~= ChapterConst.AttachBorn_Sub then
				local var_5_4 = ChapterCell.New(arg_5_0)

				var_4_3:mergeChapterCell(var_5_4)
			end
		end)

		var_4_1 = bit.bor(var_4_1, ChapterConst.DirtyAttachment)
		var_4_2 = bit.bor(var_4_2, ChapterConst.DirtyAutoAction)
	end

	arg_4_0.flag = var_4_1
	arg_4_0.extraFlag = var_4_2
end

function var_0_0.doCellFlagUpdate(arg_6_0)
	local var_6_0 = arg_6_0.data
	local var_6_1 = arg_6_0.flag
	local var_6_2 = arg_6_0.chapter

	if #var_6_0.cell_flag_list > 0 then
		_.each(var_6_0.cell_flag_list, function(arg_7_0)
			local var_7_0 = var_6_2:getChapterCell(arg_7_0.pos.row, arg_7_0.pos.column)

			if var_7_0 then
				var_7_0:updateFlagList(arg_7_0)
			else
				var_7_0 = ChapterCell.New(arg_7_0)
			end

			arg_6_0.chapter:updateChapterCell(var_7_0)
		end)

		var_6_1 = bit.bor(var_6_1, ChapterConst.DirtyCellFlag)
	end

	arg_6_0.flag = var_6_1
end

function var_0_0.doAIUpdate(arg_8_0)
	local var_8_0 = arg_8_0.data
	local var_8_1 = arg_8_0.flag
	local var_8_2 = arg_8_0.extraFlag
	local var_8_3 = arg_8_0.chapter

	if #var_8_0.ai_list > 0 then
		_.each(var_8_0.ai_list, function(arg_9_0)
			local var_9_0 = ChapterChampionPackage.New(arg_9_0)

			var_8_3:mergeChampion(var_9_0)
		end)

		var_8_1 = bit.bor(var_8_1, ChapterConst.DirtyChampion)
		var_8_2 = bit.bor(var_8_2, ChapterConst.DirtyAutoAction)
	end

	arg_8_0.flag = var_8_1
	arg_8_0.extraFlag = var_8_2
end

function var_0_0.doShipUpdate(arg_10_0)
	local var_10_0 = arg_10_0.data
	local var_10_1 = arg_10_0.flag
	local var_10_2 = arg_10_0.chapter

	if #var_10_0.ship_update > 0 then
		_.each(var_10_0.ship_update, function(arg_11_0)
			var_10_2:updateFleetShipHp(arg_11_0.id, arg_11_0.hp_rant)

			var_10_1 = bit.bor(var_10_1, ChapterConst.DirtyStrategy)
		end)

		var_10_1 = bit.bor(var_10_1, ChapterConst.DirtyFleet)
	end

	arg_10_0.flag = var_10_1
end

function var_0_0.doBuffUpdate(arg_12_0)
	local var_12_0 = arg_12_0.data

	arg_12_0.chapter:UpdateBuffList(var_12_0.buff_list)
end

function var_0_0.doExtraFlagUpdate(arg_13_0)
	local var_13_0 = arg_13_0.data
	local var_13_1 = arg_13_0.chapter
	local var_13_2 = getProxy(ChapterProxy)

	if #var_13_0.add_flag_list > 0 or #var_13_0.del_flag_list > 0 then
		var_13_2:updateExtraFlag(var_13_1, var_13_0.add_flag_list, var_13_0.del_flag_list)

		arg_13_0.flag = bit.bor(arg_13_0.flag, ChapterConst.DirtyFleet, ChapterConst.DirtyStrategy, ChapterConst.DirtyCellFlag, ChapterConst.DirtyFloatItems, ChapterConst.DirtyAttachment)
	end
end

function var_0_0.doRetreat(arg_14_0)
	local var_14_0 = arg_14_0.op
	local var_14_1 = arg_14_0.flag
	local var_14_2 = arg_14_0.chapter

	if var_14_0.id then
		if #var_14_2.fleets > 0 then
			local var_14_3 = var_14_2.fleets[var_14_0.id]

			var_14_2.fleets = _.filter(var_14_2.fleets, function(arg_15_0)
				return arg_15_0.id ~= var_14_0.id
			end)

			if var_14_3 and var_14_3:getFleetType() == FleetType.Normal then
				var_14_2.findex = 1
			end

			var_14_1 = bit.bor(var_14_1, ChapterConst.DirtyFleet, ChapterConst.DirtyAttachment, ChapterConst.DirtyChampion, ChapterConst.DirtyStrategy)
		end
	else
		var_14_2:retreat(var_14_0.win)
	end

	arg_14_0.flag = var_14_1
end

function var_0_0.doMove(arg_16_0)
	local var_16_0 = arg_16_0.extraFlag
	local var_16_1 = arg_16_0.data
	local var_16_2 = arg_16_0.chapter
	local var_16_3

	if #var_16_1.move_path > 0 then
		var_16_3 = _.map(_.rest(var_16_1.move_path, 1), function(arg_17_0)
			return {
				row = arg_17_0.row,
				column = arg_17_0.column
			}
		end)
		var_16_2.moveStep = var_16_2.moveStep + #var_16_1.move_path
		var_16_0 = bit.bor(var_16_0, ChapterConst.DirtyAutoAction)
	end

	arg_16_0.fullpath = var_16_3

	var_16_2:IncreaseRound()

	arg_16_0.extraFlag = var_16_0
end

function var_0_0.doOpenBox(arg_18_0)
	local var_18_0 = arg_18_0.items
	local var_18_1 = arg_18_0.flag
	local var_18_2 = arg_18_0.chapter
	local var_18_3 = var_18_2.fleet
	local var_18_4 = var_18_3.line
	local var_18_5 = var_18_2:getChapterCell(var_18_4.row, var_18_4.column)

	var_18_5.flag = ChapterConst.CellFlagDisabled

	local var_18_6 = bit.bor(var_18_1, ChapterConst.DirtyAttachment)
	local var_18_7 = pg.box_data_template[var_18_5.attachmentId]

	assert(var_18_7, "box_data_template not exist: " .. var_18_5.attachmentId)

	if var_18_7.type == ChapterConst.BoxStrategy then
		local var_18_8 = var_18_7.effect_id
		local var_18_9 = var_18_7.effect_arg

		var_18_3:achievedStrategy(var_18_8, var_18_9)
		table.insert(var_18_0, Drop.New({
			type = DROP_TYPE_STRATEGY,
			id = var_18_8,
			count = var_18_9
		}))

		var_18_6 = bit.bor(var_18_6, ChapterConst.DirtyStrategy)
	elseif var_18_7.type == ChapterConst.BoxSupply then
		local var_18_10, var_18_11 = var_18_2:getFleetAmmo(var_18_3)

		var_18_3.restAmmo = var_18_3.restAmmo + math.min(var_18_10 - var_18_11, var_18_7.effect_id)
		var_18_6 = bit.bor(var_18_6, ChapterConst.DirtyFleet)

		pg.TipsMgr.GetInstance():ShowTips(i18n("level_ammo_supply_p1", var_18_7.effect_id))
	end

	var_18_2:clearChapterCell(var_18_4.row, var_18_4.column)

	arg_18_0.flag = var_18_6
	arg_18_0.extraFlag = bit.bor(arg_18_0.extraFlag, ChapterConst.DirtyAutoAction)
end

function var_0_0.doPlayStory(arg_19_0)
	local var_19_0 = arg_19_0.flag
	local var_19_1 = arg_19_0.chapter
	local var_19_2 = var_19_1.fleet.line
	local var_19_3 = var_19_1:getChapterCell(var_19_2.row, var_19_2.column)

	var_19_3.flag = ChapterConst.CellFlagDisabled

	var_19_1:updateChapterCell(var_19_3)

	arg_19_0.flag = bit.bor(var_19_0, ChapterConst.DirtyAttachment)
end

function var_0_0.doAmbush(arg_20_0)
	local var_20_0 = arg_20_0.op
	local var_20_1 = arg_20_0.chapter
	local var_20_2 = var_20_1.fleet

	if var_20_0.arg1 == 1 then
		local var_20_3 = var_20_2.line
		local var_20_4 = var_20_1:getChapterCell(var_20_3.row, var_20_3.column)

		if var_20_4.flag == ChapterConst.CellFlagAmbush then
			var_20_1:clearChapterCell(var_20_3.row, var_20_3.column)
		end

		pg.TipsMgr.GetInstance():ShowTips(var_20_4.flag == ChapterConst.CellFlagActive and i18n("chapter_tip_aovid_failed") or i18n("chapter_tip_aovid_succeed"))
	end
end

function var_0_0.doStrategy(arg_21_0)
	local var_21_0 = arg_21_0.flag
	local var_21_1 = arg_21_0.op
	local var_21_2 = arg_21_0.chapter
	local var_21_3 = pg.strategy_data_template[var_21_1.arg1]

	if var_21_3.type == ChapterConst.StgTypeForm then
		local var_21_4 = var_21_2.fleet

		for iter_21_0, iter_21_1 in ipairs(var_21_4.stgIds) do
			if pg.strategy_data_template[iter_21_1].type == ChapterConst.StgTypeForm then
				var_21_4.stgIds[iter_21_0] = var_21_3.id
			end
		end

		PlayerPrefs.SetInt("team_formation_" .. var_21_4.id, var_21_3.id)
		pg.TipsMgr.GetInstance():ShowTips(i18n("chapter_tip_change", var_21_3.name))
	elseif var_21_3.type == ChapterConst.StgTypeConsume then
		var_21_2.fleet:consumeOneStrategy(var_21_3.id)

		if var_21_3.id == ChapterConst.StrategyRepair or var_21_3.id == ChapterConst.StrategyExchange then
			pg.TipsMgr.GetInstance():ShowTips(i18n("chapter_tip_use", var_21_3.name))
		end

		if var_21_3.id == ChapterConst.StrategyExchange then
			local var_21_5 = var_21_2:getFleetById(var_21_1.id)
			local var_21_6 = var_21_2:getFleetById(var_21_1.arg2)

			var_21_5.line, var_21_6.line = var_21_6.line, var_21_5.line
			var_21_0 = bit.bor(var_21_0, ChapterConst.DirtyFleet)
		end
	elseif var_21_3.type == ChapterConst.StgTypeBindSupportConsume then
		var_21_2:getChapterSupportFleet():consumeOneStrategy(var_21_3.id)
	end

	arg_21_0.flag = bit.bor(var_21_0, ChapterConst.DirtyStrategy)
end

function var_0_0.doRepair(arg_22_0)
	local var_22_0 = getProxy(ChapterProxy)

	var_22_0.repairTimes = var_22_0.repairTimes + 1

	local var_22_1, var_22_2, var_22_3 = ChapterConst.GetRepairParams()

	if var_22_1 < var_22_0.repairTimes then
		local var_22_4 = getProxy(PlayerProxy)
		local var_22_5 = var_22_4:getData()

		var_22_5:consume({
			gem = var_22_3
		})
		var_22_4:updatePlayer(var_22_5)
	end
end

function var_0_0.doSupply(arg_23_0)
	local var_23_0 = arg_23_0.flag
	local var_23_1 = arg_23_0.chapter
	local var_23_2 = var_23_1.fleet
	local var_23_3, var_23_4 = var_23_1:getFleetAmmo(var_23_2)
	local var_23_5 = var_23_2.line
	local var_23_6 = var_23_1:getChapterCell(var_23_5.row, var_23_5.column)
	local var_23_7 = math.min(var_23_6.attachmentId, var_23_3 - var_23_4)

	var_23_6.attachmentId = var_23_6.attachmentId - var_23_7
	var_23_2.restAmmo = var_23_2.restAmmo + var_23_7

	var_23_1:updateChapterCell(var_23_6)

	if var_23_6.attachmentId > 20 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("level_ammo_supply_p1", var_23_7))
	elseif var_23_6.attachmentId > 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("level_ammo_supply", var_23_7, var_23_6.attachmentId))
	else
		pg.TipsMgr.GetInstance():ShowTips(i18n("level_ammo_empty", var_23_7))
	end

	arg_23_0.flag = bit.bor(var_23_0, ChapterConst.DirtyAttachment, ChapterConst.DirtyFleet)
end

function var_0_0.doSubState(arg_24_0)
	local var_24_0 = arg_24_0.flag
	local var_24_1 = arg_24_0.op

	arg_24_0.chapter.subAutoAttack = var_24_1.arg1
	arg_24_0.flag = bit.bor(var_24_0, ChapterConst.DirtyStrategy)
end

function var_0_0.doCollectAI(arg_25_0)
	local var_25_0 = arg_25_0.data

	arg_25_0.aiActs = arg_25_0.aiActs or {}

	if var_25_0.submarine_act_list then
		_.each(var_25_0.submarine_act_list, function(arg_26_0)
			table.insert(arg_25_0.aiActs, SubAIAction.New(arg_26_0))
		end)
	end

	if var_25_0.escort_act_list then
		_.each(var_25_0.escort_act_list, function(arg_27_0)
			table.insert(arg_25_0.aiActs, TransportAIAction.New(arg_27_0))
		end)
	end

	_.each(var_25_0.ai_act_list, function(arg_28_0)
		local var_28_0

		if arg_28_0.act_type == ChapterConst.ActType_TargetDown then
			if arg_25_0.op.type == ChapterConst.OpStrategy then
				if arg_25_0.op.arg1 == ChapterConst.StrategyMissileStrike then
					var_28_0 = ChapterMissileExplodeAction.New(arg_28_0)
				elseif arg_25_0.op.arg1 == ChapterConst.StrategyAirSupport then
					var_28_0 = ChapterAirSupportAIAction.New(arg_28_0)
				end

				var_28_0:SetTargetLine({
					row = arg_25_0.op.arg2,
					column = arg_25_0.op.arg3
				})
			else
				var_28_0 = ChapterMissileExplodeAction.New(arg_28_0)
			end
		elseif arg_28_0.act_type == ChapterConst.ActType_Expel then
			var_28_0 = ChapterExpelAIAction.New(arg_28_0)

			var_28_0:SetTargetLine({
				row = arg_25_0.op.arg2,
				column = arg_25_0.op.arg3
			}, {
				row = arg_25_0.op.arg4,
				column = arg_25_0.op.arg5
			})
		else
			var_28_0 = ChapterAIAction.New(arg_28_0)
		end

		table.insert(arg_25_0.aiActs, var_28_0)
	end)
	_.each(var_25_0.fleet_act_list, function(arg_29_0)
		table.insert(arg_25_0.aiActs, FleetAIAction.New(arg_29_0))
	end)
end

function var_0_0.doBarrier(arg_30_0)
	local var_30_0 = arg_30_0.flag
	local var_30_1 = arg_30_0.op
	local var_30_2 = arg_30_0.chapter
	local var_30_3 = var_30_2:getChapterCell(var_30_1.arg1, var_30_1.arg2)

	assert(var_30_3, "cell not exist: " .. var_30_1.arg1 .. ", " .. var_30_1.arg2)

	local var_30_4 = ChapterConst.AttachBox
	local var_30_5 = _.detect(pg.box_data_template.all, function(arg_31_0)
		return pg.box_data_template[arg_31_0].type == ChapterConst.BoxBarrier
	end)

	if var_30_3.attachment ~= var_30_4 or var_30_3.attachmentId ~= var_30_5 then
		var_30_3.attachment = var_30_4
		var_30_3.attachmentId = var_30_5
		var_30_3.flag = ChapterConst.CellFlagDisabled
	end

	var_30_2.modelCount = var_30_2.modelCount + (var_30_3.flag == ChapterConst.CellFlagDisabled and -1 or 1)
	var_30_3.flag = 1 - var_30_3.flag

	var_30_2:updateChapterCell(var_30_3)

	arg_30_0.flag = bit.bor(var_30_0, ChapterConst.DirtyAttachment, ChapterConst.DirtyStrategy)
end

function var_0_0.doRequest(arg_32_0)
	local var_32_0 = arg_32_0.data
	local var_32_1 = -1
	local var_32_2 = arg_32_0.chapter.fleet

	if #var_32_0.move_path > 0 then
		local var_32_3 = var_32_0.move_path[#var_32_0.move_path]

		var_32_2.line = {
			row = var_32_3.row,
			column = var_32_3.column
		}
	end

	arg_32_0.flag = var_32_1
end

function var_0_0.doSkipBattle(arg_33_0)
	local var_33_0 = arg_33_0.flag

	arg_33_0.flag = bit.bor(var_33_0, ChapterConst.DirtyStrategy, ChapterConst.DirtyAttachment, ChapterConst.DirtyAchieve, ChapterConst.DirtyFleet, ChapterConst.DirtyChampion)
end

function var_0_0.doTeleportSub(arg_34_0)
	local var_34_0 = arg_34_0.op
	local var_34_1 = arg_34_0.chapter
	local var_34_2 = _.detect(var_34_1.fleets, function(arg_35_0)
		return arg_35_0.id == var_34_0.id
	end).startPos

	arg_34_0.fullpath = {
		var_34_2,
		{
			row = var_34_0.arg1,
			column = var_34_0.arg2
		}
	}
end

function var_0_0.doEnemyRound(arg_36_0)
	local var_36_0 = arg_36_0.chapter
	local var_36_1 = arg_36_0.extraFlag

	var_36_0:IncreaseRound()

	if var_36_0:getPlayType() == ChapterConst.TypeDefence then
		arg_36_0.flag = bit.bor(arg_36_0.flag, ChapterConst.DirtyAttachment)
	end

	arg_36_0.extraFlag = bit.bor(var_36_1, ChapterConst.DirtyAutoAction)
end

function var_0_0.doTeleportByPortal(arg_37_0)
	local var_37_0 = arg_37_0.fullpath and arg_37_0.fullpath[#arg_37_0.fullpath]

	if not var_37_0 then
		return
	end

	local var_37_1 = arg_37_0.chapter
	local var_37_2

	if arg_37_0.op.type == ChapterConst.OpMove then
		var_37_2 = var_37_1:GetCellEventByKey("jump", var_37_0.row, var_37_0.column)
	elseif arg_37_0.op.type == ChapterConst.OpSubTeleport then
		var_37_2 = var_37_1:GetCellEventByKey("jumpsub", var_37_0.row, var_37_0.column)
	end

	if not var_37_2 then
		return
	end

	local var_37_3 = {
		row = var_37_2[1],
		column = var_37_2[2]
	}

	if arg_37_0.op.type == ChapterConst.OpMove and var_37_1:getFleet(FleetType.Normal, var_37_3.row, var_37_3.column) then
		return
	end

	arg_37_0.teleportPaths = arg_37_0.teleportPaths or {}

	table.insert(arg_37_0.teleportPaths, {
		row = var_37_0.row,
		column = var_37_0.column
	})
	table.insert(arg_37_0.teleportPaths, var_37_3)
end

function var_0_0.doCollectCommonAction(arg_38_0)
	arg_38_0.aiActs = arg_38_0.aiActs or {}

	table.insert(arg_38_0.aiActs, ChapterCommonAction.New(arg_38_0))
end

function var_0_0.AddBoxAction(arg_39_0)
	local var_39_0 = arg_39_0.chapter
	local var_39_1 = var_39_0.fleet.line
	local var_39_2 = var_39_0:getChapterCell(var_39_1.row, var_39_1.column)
	local var_39_3 = pg.box_data_template[var_39_2.attachmentId]

	assert(var_39_3, "box_data_template not exist: " .. var_39_2.attachmentId)

	if var_39_3.type == ChapterConst.BoxStrategy then
		local var_39_4 = var_39_3.effect_id
		local var_39_5 = var_39_3.effect_arg

		table.insert(arg_39_0.items, Drop.New({
			type = DROP_TYPE_STRATEGY,
			id = var_39_4,
			count = var_39_5
		}))
	end

	arg_39_0.aiActs = arg_39_0.aiActs or {}

	table.insert(arg_39_0.aiActs, ChapterBoxAction.New(arg_39_0))
end

return var_0_0
