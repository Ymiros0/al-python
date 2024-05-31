local var_0_0 = class("WorldMapOp", import("...BaseEntity"))

var_0_0.Fields = {
	updateAttachmentCells = "table",
	fleetUpdates = "table",
	anim = "string",
	callbacksWhenApplied = "table",
	op = "number",
	salvageUpdates = "table",
	hiddenAttachments = "table",
	path = "table",
	hiddenCells = "table",
	depth = "number",
	stepOps = "table",
	staminaUpdate = "table",
	arg1 = "number",
	duration = "number",
	arg2 = "number",
	effect = "table",
	applied = "boolean",
	skipDisplay = "boolean",
	destMapId = "number",
	id = "number",
	trap = "number",
	routine = "function",
	updateCarryItems = "table",
	entranceId = "number",
	pos = "table",
	childOps = "table",
	drops = "table",
	locations = "table",
	terrainUpdates = "table",
	attachment = "table",
	shipUpdates = "table",
	fleetAttachUpdates = "table",
	sign = "table",
	destGridId = "number"
}

function var_0_0.Apply(arg_1_0)
	assert(not arg_1_0.applied, "current op has been applied.")

	arg_1_0.applied = true

	local var_1_0 = getProxy(WorldProxy)
	local var_1_1 = nowWorld()
	local var_1_2 = var_1_1:GetActiveMap()

	if arg_1_0.op == WorldConst.OpReqMoveFleet then
		var_1_1:IncRound()
	elseif arg_1_0.op == WorldConst.OpReqRound then
		var_1_1:IncRound()
	elseif arg_1_0.op == WorldConst.OpReqEvent then
		local var_1_3 = var_1_2:GetFleet(arg_1_0.id)
		local var_1_4 = arg_1_0.effect
		local var_1_5 = var_1_4.effect_type
		local var_1_6 = var_1_4.effect_paramater

		if var_1_5 == WorldMapAttachment.EffectEventTeleport or var_1_5 == WorldMapAttachment.EffectEventTeleportBack then
			assert(arg_1_0.destMapId and arg_1_0.destMapId > 0)
			var_1_0:NetUpdateActiveMap(arg_1_0.entranceId, arg_1_0.destMapId, arg_1_0.destGridId)
		elseif var_1_5 == WorldMapAttachment.EffectEventShipBuff then
			local var_1_7 = var_1_6[1]

			_.each(var_1_3:GetShips(true), function(arg_2_0)
				arg_2_0:AddBuff(var_1_7, 1)
			end)
		elseif var_1_5 == WorldMapAttachment.EffectEventAchieveCarry then
			_.each(var_1_6, function(arg_3_0)
				local var_3_0 = WorldCarryItem.New()

				var_3_0:Setup(arg_3_0)
				var_1_3:AddCarry(var_3_0)
			end)
		elseif var_1_5 == WorldMapAttachment.EffectEventConsumeCarry then
			local var_1_8 = var_1_6[1] or {}

			_.each(var_1_8, function(arg_4_0)
				var_1_3:RemoveCarry(arg_4_0)
			end)
		elseif var_1_5 == WorldMapAttachment.EffectEventConsumeItem then
			var_1_1:GetInventoryProxy():RemoveItem(var_1_6[1], var_1_6[2])
		elseif var_1_5 == WorldMapAttachment.EffectEventDropTreasure then
			var_1_1.treasureCount = var_1_1.treasureCount + 1
		elseif var_1_5 == WorldMapAttachment.EffectEventFOV then
			var_1_2:EventEffectOpenFOV(var_1_4)
		elseif var_1_5 == WorldMapAttachment.EffectEventProgress then
			local var_1_9 = math.max(var_1_1:GetProgress(), var_1_6[1])

			var_1_1:UpdateProgress(var_1_9)
		elseif var_1_5 == WorldMapAttachment.EffectEventDeleteTask then
			local var_1_10 = var_1_1:GetTaskProxy()

			for iter_1_0, iter_1_1 in ipairs(var_1_6) do
				var_1_10:deleteTask(iter_1_1)
			end
		elseif var_1_5 == WorldMapAttachment.EffectEventGlobalBuff then
			var_1_1:AddGlobalBuff(var_1_6[1], var_1_6[2])
		elseif var_1_5 == WorldMapAttachment.EffectEventMapClearFlag then
			var_1_2:UpdateClearFlag(var_1_6[1] == 1)
		elseif var_1_5 == WorldMapAttachment.EffectEventBrokenClean then
			for iter_1_2, iter_1_3 in ipairs(var_1_1:GetShips()) do
				if iter_1_3:IsBroken() then
					iter_1_3:RemoveBuff(WorldConst.BrokenBuffId)
				end
			end
		elseif var_1_5 == WorldMapAttachment.EffectEventCatSalvage then
			-- block empty
		elseif var_1_5 == WorldMapAttachment.EffectEventAddWorldBossFreeCount then
			nowWorld():GetBossProxy():AddSummonFree(1)
		end

		if #var_1_4.sound_effects > 0 then
			pg.CriMgr.GetInstance():PlaySoundEffect_V3("event:" .. var_1_4.sound_effects)
		end
	elseif arg_1_0.op == WorldConst.OpReqDiscover then
		_.each(arg_1_0.locations, function(arg_5_0)
			var_1_2:GetCell(arg_5_0.row, arg_5_0.column):UpdateDiscovered(true)
		end)
		_.each(arg_1_0.hiddenAttachments, function(arg_6_0)
			arg_6_0:UpdateLurk(false)
		end)
	elseif arg_1_0.op == WorldConst.OpReqTransport then
		assert(arg_1_0.destMapId and arg_1_0.destMapId > 0)
		var_1_0:NetUpdateActiveMap(arg_1_0.entranceId, arg_1_0.destMapId, arg_1_0.destGridId)

		local var_1_11 = var_1_1:TreasureMap2ItemId(arg_1_0.destMapId, arg_1_0.entranceId)

		if var_1_11 then
			var_1_1:GetInventoryProxy():RemoveItem(var_1_11, 1)
		end
	elseif arg_1_0.op == WorldConst.OpReqSub then
		var_1_1:ResetSubmarine()
		var_1_1:UpdateSubmarineSupport(true)

		local var_1_12 = var_1_1:GetActiveMap()
	elseif arg_1_0.op == WorldConst.OpReqPressingMap then
		local var_1_13 = arg_1_0.arg1

		var_1_1:FlagMapPressingAward(var_1_13)
		var_1_1:GetAtlas():AddPressingMap(var_1_13)

		local var_1_14 = var_1_1:GetMap(var_1_13)

		if not var_1_14.visionFlag and nowWorld():IsMapVisioned(var_1_13) then
			var_1_14:UpdateVisionFlag(true)
		end
	elseif arg_1_0.op == WorldConst.OpReqJumpOut then
		assert(arg_1_0.destMapId and arg_1_0.destMapId > 0)

		local var_1_15 = pg.world_chapter_template_reset[var_1_2.gid].reset_item
		local var_1_16 = var_1_1:GetInventoryProxy()

		_.each(var_1_15, function(arg_7_0)
			var_1_16:RemoveItem(arg_7_0)
		end)
		var_1_0:NetUpdateActiveMap(arg_1_0.entranceId, arg_1_0.destMapId, arg_1_0.destGridId)

		var_1_2 = var_1_1:GetActiveMap()
	elseif arg_1_0.op == WorldConst.OpReqEnterPort then
		-- block empty
	elseif arg_1_0.op == WorldConst.OpReqCatSalvage then
		var_1_2:GetFleet(arg_1_0.id):UpdateCatSalvage(0, nil, 0)
	elseif arg_1_0.op == WorldConst.OpReqSkipBattle then
		var_1_2:WriteBack(true, {
			statistics = {},
			hpDropInfo = {}
		})
	elseif arg_1_0.op == WorldConst.OpActionFleetMove then
		local var_1_17 = arg_1_0.path[#arg_1_0.path]

		var_1_2:UpdateFleetLocation(arg_1_0.id, var_1_17.row, var_1_17.column)

		var_1_1.stepCount = var_1_1.stepCount + #arg_1_0.path
	elseif arg_1_0.op == WorldConst.OpActionMoveStep then
		arg_1_0:ApplyAttachmentUpdate()
		_.each(arg_1_0.hiddenCells, function(arg_8_0)
			arg_8_0:UpdateDiscovered(true)
		end)

		local var_1_18 = var_1_2:GetFleet(arg_1_0.id)
		local var_1_19 = var_1_2:GetCell(var_1_18.row, var_1_18.column):GetEventAttachment()

		if var_1_19 and var_1_19:IsTriggered() then
			var_1_19.triggered = false
		end

		if arg_1_0.updateCarryItems and #arg_1_0.updateCarryItems > 0 then
			local var_1_20 = var_1_18:GetCarries()

			assert(#var_1_20 == #arg_1_0.updateCarryItems)

			for iter_1_4, iter_1_5 in ipairs(var_1_20) do
				iter_1_5:UpdateOffset(arg_1_0.updateCarryItems[iter_1_4].offsetRow, arg_1_0.updateCarryItems[iter_1_4].offsetColumn)
			end

			WPool:ReturnArray(arg_1_0.updateCarryItems)

			arg_1_0.updateCarryItems = nil
		end

		var_1_2:UpdateFleetLocation(arg_1_0.id, arg_1_0.pos.row, arg_1_0.pos.column)
		_.each(arg_1_0.hiddenAttachments, function(arg_9_0)
			arg_9_0:UpdateLurk(false)
		end)
	elseif arg_1_0.op == WorldConst.OpActionAttachmentMove then
		assert(#arg_1_0.path > 0)

		local var_1_21 = arg_1_0.attachment:Clone()
		local var_1_22 = arg_1_0.path[#arg_1_0.path]

		var_1_2:GetCell(arg_1_0.attachment.row, arg_1_0.attachment.column):RemoveAttachment(arg_1_0.attachment)

		local var_1_23 = var_1_2:GetCell(var_1_22.row, var_1_22.column)

		assert(var_1_23, "dest cell not exist: " .. var_1_22.row .. ", " .. var_1_22.column)

		var_1_21.row = var_1_22.row
		var_1_21.column = var_1_22.column

		var_1_23:AddAttachment(var_1_21)
	elseif arg_1_0.op == WorldConst.OpActionEventOp then
		local var_1_24 = arg_1_0.effect

		if var_1_24.effect_type == WorldMapAttachment.EffectEventFOV then
			var_1_2:EventEffectOpenFOV(var_1_24)
		end

		arg_1_0.attachment:UpdateDataOp(arg_1_0.attachment.dataop - 1)
	elseif arg_1_0.op == WorldConst.OpActionTaskGoto then
		local var_1_25 = arg_1_0.effect

		if var_1_25.effect_type == WorldMapAttachment.EffectEventFOV then
			var_1_2:EventEffectOpenFOV(var_1_25)
		end
	end

	if arg_1_0.childOps then
		_.each(arg_1_0.childOps, function(arg_10_0)
			if not arg_10_0.applied then
				arg_10_0:Apply()
			end
		end)
	end

	if arg_1_0.stepOps then
		_.each(arg_1_0.stepOps, function(arg_11_0)
			if not arg_11_0.applied then
				arg_11_0:Apply()
			end
		end)
	end

	arg_1_0:ApplyAttachmentUpdate()
	arg_1_0:ApplyNetUpdate()

	if arg_1_0.callbacksWhenApplied then
		_.each(arg_1_0.callbacksWhenApplied, function(arg_12_0)
			arg_12_0()
		end)
	end
end

function var_0_0.ApplyAttachmentUpdate(arg_13_0)
	local var_13_0 = getProxy(WorldProxy)
	local var_13_1 = nowWorld():GetActiveMap()

	if arg_13_0.updateAttachmentCells then
		var_13_0:UpdateMapAttachmentCells(var_13_1.id, arg_13_0.updateAttachmentCells)

		for iter_13_0, iter_13_1 in pairs(arg_13_0.updateAttachmentCells) do
			local var_13_2 = var_13_1:GetCell(iter_13_1.pos.row, iter_13_1.pos.column)

			_.each(iter_13_1.attachmentList, function(arg_14_0)
				if not var_13_2:ContainsAttachment(arg_14_0) then
					WPool:Return(arg_14_0)
				end
			end)
		end

		arg_13_0.updateAttachmentCells = nil
	end
end

function var_0_0.ApplyNetUpdate(arg_15_0)
	local var_15_0 = getProxy(WorldProxy)
	local var_15_1 = nowWorld()
	local var_15_2 = var_15_1:GetActiveMap()

	if arg_15_0.staminaUpdate then
		var_15_1.staminaMgr:ChangeStamina(arg_15_0.staminaUpdate[1], arg_15_0.staminaUpdate[2])

		arg_15_0.staminaUpdate = nil
	end

	if arg_15_0.shipUpdates and #arg_15_0.shipUpdates > 0 then
		var_15_0:ApplyShipUpdate(arg_15_0.shipUpdates)
		WPool:ReturnArray(arg_15_0.shipUpdates)

		arg_15_0.shipUpdates = nil
	end

	if arg_15_0.fleetAttachUpdates and #arg_15_0.fleetAttachUpdates > 0 then
		var_15_0:ApplyFleetAttachUpdate(var_15_2.id, arg_15_0.fleetAttachUpdates)
		WPool:ReturnArray(arg_15_0.fleetAttachUpdates)

		arg_15_0.fleetAttachUpdates = nil
	end

	if arg_15_0.fleetUpdates and #arg_15_0.fleetUpdates > 0 then
		var_15_0:ApplyFleetUpdate(var_15_2.id, arg_15_0.fleetUpdates)
		WPool:ReturnArray(arg_15_0.fleetUpdates)

		arg_15_0.fleetUpdates = nil
	end

	if arg_15_0.terrainUpdates and #arg_15_0.terrainUpdates > 0 then
		var_15_0:ApplyTerrainUpdate(var_15_2.id, arg_15_0.terrainUpdates)
		WPool:ReturnArray(arg_15_0.terrainUpdates)

		arg_15_0.terrainUpdates = nil
	end

	if arg_15_0.salvageUpdates and #arg_15_0.salvageUpdates > 0 then
		var_15_0:ApplySalvageUpdate(arg_15_0.salvageUpdates)
		WPool:ReturnArray(arg_15_0.salvageUpdates)

		arg_15_0.salvageUpdates = nil
	end
end

function var_0_0.AddCallbackWhenApplied(arg_16_0, arg_16_1)
	if not arg_16_0.callbacksWhenApplied then
		arg_16_0.callbacksWhenApplied = {}
	end

	table.insert(arg_16_0.callbacksWhenApplied, arg_16_1)
end

return var_0_0
