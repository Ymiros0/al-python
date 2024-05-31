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

def var_0_0.Apply(arg_1_0):
	assert(not arg_1_0.applied, "current op has been applied.")

	arg_1_0.applied = True

	local var_1_0 = getProxy(WorldProxy)
	local var_1_1 = nowWorld()
	local var_1_2 = var_1_1.GetActiveMap()

	if arg_1_0.op == WorldConst.OpReqMoveFleet:
		var_1_1.IncRound()
	elif arg_1_0.op == WorldConst.OpReqRound:
		var_1_1.IncRound()
	elif arg_1_0.op == WorldConst.OpReqEvent:
		local var_1_3 = var_1_2.GetFleet(arg_1_0.id)
		local var_1_4 = arg_1_0.effect
		local var_1_5 = var_1_4.effect_type
		local var_1_6 = var_1_4.effect_paramater

		if var_1_5 == WorldMapAttachment.EffectEventTeleport or var_1_5 == WorldMapAttachment.EffectEventTeleportBack:
			assert(arg_1_0.destMapId and arg_1_0.destMapId > 0)
			var_1_0.NetUpdateActiveMap(arg_1_0.entranceId, arg_1_0.destMapId, arg_1_0.destGridId)
		elif var_1_5 == WorldMapAttachment.EffectEventShipBuff:
			local var_1_7 = var_1_6[1]

			_.each(var_1_3.GetShips(True), function(arg_2_0)
				arg_2_0.AddBuff(var_1_7, 1))
		elif var_1_5 == WorldMapAttachment.EffectEventAchieveCarry:
			_.each(var_1_6, function(arg_3_0)
				local var_3_0 = WorldCarryItem.New()

				var_3_0.Setup(arg_3_0)
				var_1_3.AddCarry(var_3_0))
		elif var_1_5 == WorldMapAttachment.EffectEventConsumeCarry:
			local var_1_8 = var_1_6[1] or {}

			_.each(var_1_8, function(arg_4_0)
				var_1_3.RemoveCarry(arg_4_0))
		elif var_1_5 == WorldMapAttachment.EffectEventConsumeItem:
			var_1_1.GetInventoryProxy().RemoveItem(var_1_6[1], var_1_6[2])
		elif var_1_5 == WorldMapAttachment.EffectEventDropTreasure:
			var_1_1.treasureCount = var_1_1.treasureCount + 1
		elif var_1_5 == WorldMapAttachment.EffectEventFOV:
			var_1_2.EventEffectOpenFOV(var_1_4)
		elif var_1_5 == WorldMapAttachment.EffectEventProgress:
			local var_1_9 = math.max(var_1_1.GetProgress(), var_1_6[1])

			var_1_1.UpdateProgress(var_1_9)
		elif var_1_5 == WorldMapAttachment.EffectEventDeleteTask:
			local var_1_10 = var_1_1.GetTaskProxy()

			for iter_1_0, iter_1_1 in ipairs(var_1_6):
				var_1_10.deleteTask(iter_1_1)
		elif var_1_5 == WorldMapAttachment.EffectEventGlobalBuff:
			var_1_1.AddGlobalBuff(var_1_6[1], var_1_6[2])
		elif var_1_5 == WorldMapAttachment.EffectEventMapClearFlag:
			var_1_2.UpdateClearFlag(var_1_6[1] == 1)
		elif var_1_5 == WorldMapAttachment.EffectEventBrokenClean:
			for iter_1_2, iter_1_3 in ipairs(var_1_1.GetShips()):
				if iter_1_3.IsBroken():
					iter_1_3.RemoveBuff(WorldConst.BrokenBuffId)
		elif var_1_5 == WorldMapAttachment.EffectEventCatSalvage:
			-- block empty
		elif var_1_5 == WorldMapAttachment.EffectEventAddWorldBossFreeCount:
			nowWorld().GetBossProxy().AddSummonFree(1)

		if #var_1_4.sound_effects > 0:
			pg.CriMgr.GetInstance().PlaySoundEffect_V3("event." .. var_1_4.sound_effects)
	elif arg_1_0.op == WorldConst.OpReqDiscover:
		_.each(arg_1_0.locations, function(arg_5_0)
			var_1_2.GetCell(arg_5_0.row, arg_5_0.column).UpdateDiscovered(True))
		_.each(arg_1_0.hiddenAttachments, function(arg_6_0)
			arg_6_0.UpdateLurk(False))
	elif arg_1_0.op == WorldConst.OpReqTransport:
		assert(arg_1_0.destMapId and arg_1_0.destMapId > 0)
		var_1_0.NetUpdateActiveMap(arg_1_0.entranceId, arg_1_0.destMapId, arg_1_0.destGridId)

		local var_1_11 = var_1_1.TreasureMap2ItemId(arg_1_0.destMapId, arg_1_0.entranceId)

		if var_1_11:
			var_1_1.GetInventoryProxy().RemoveItem(var_1_11, 1)
	elif arg_1_0.op == WorldConst.OpReqSub:
		var_1_1.ResetSubmarine()
		var_1_1.UpdateSubmarineSupport(True)

		local var_1_12 = var_1_1.GetActiveMap()
	elif arg_1_0.op == WorldConst.OpReqPressingMap:
		local var_1_13 = arg_1_0.arg1

		var_1_1.FlagMapPressingAward(var_1_13)
		var_1_1.GetAtlas().AddPressingMap(var_1_13)

		local var_1_14 = var_1_1.GetMap(var_1_13)

		if not var_1_14.visionFlag and nowWorld().IsMapVisioned(var_1_13):
			var_1_14.UpdateVisionFlag(True)
	elif arg_1_0.op == WorldConst.OpReqJumpOut:
		assert(arg_1_0.destMapId and arg_1_0.destMapId > 0)

		local var_1_15 = pg.world_chapter_template_reset[var_1_2.gid].reset_item
		local var_1_16 = var_1_1.GetInventoryProxy()

		_.each(var_1_15, function(arg_7_0)
			var_1_16.RemoveItem(arg_7_0))
		var_1_0.NetUpdateActiveMap(arg_1_0.entranceId, arg_1_0.destMapId, arg_1_0.destGridId)

		var_1_2 = var_1_1.GetActiveMap()
	elif arg_1_0.op == WorldConst.OpReqEnterPort:
		-- block empty
	elif arg_1_0.op == WorldConst.OpReqCatSalvage:
		var_1_2.GetFleet(arg_1_0.id).UpdateCatSalvage(0, None, 0)
	elif arg_1_0.op == WorldConst.OpReqSkipBattle:
		var_1_2.WriteBack(True, {
			statistics = {},
			hpDropInfo = {}
		})
	elif arg_1_0.op == WorldConst.OpActionFleetMove:
		local var_1_17 = arg_1_0.path[#arg_1_0.path]

		var_1_2.UpdateFleetLocation(arg_1_0.id, var_1_17.row, var_1_17.column)

		var_1_1.stepCount = var_1_1.stepCount + #arg_1_0.path
	elif arg_1_0.op == WorldConst.OpActionMoveStep:
		arg_1_0.ApplyAttachmentUpdate()
		_.each(arg_1_0.hiddenCells, function(arg_8_0)
			arg_8_0.UpdateDiscovered(True))

		local var_1_18 = var_1_2.GetFleet(arg_1_0.id)
		local var_1_19 = var_1_2.GetCell(var_1_18.row, var_1_18.column).GetEventAttachment()

		if var_1_19 and var_1_19.IsTriggered():
			var_1_19.triggered = False

		if arg_1_0.updateCarryItems and #arg_1_0.updateCarryItems > 0:
			local var_1_20 = var_1_18.GetCarries()

			assert(#var_1_20 == #arg_1_0.updateCarryItems)

			for iter_1_4, iter_1_5 in ipairs(var_1_20):
				iter_1_5.UpdateOffset(arg_1_0.updateCarryItems[iter_1_4].offsetRow, arg_1_0.updateCarryItems[iter_1_4].offsetColumn)

			WPool.ReturnArray(arg_1_0.updateCarryItems)

			arg_1_0.updateCarryItems = None

		var_1_2.UpdateFleetLocation(arg_1_0.id, arg_1_0.pos.row, arg_1_0.pos.column)
		_.each(arg_1_0.hiddenAttachments, function(arg_9_0)
			arg_9_0.UpdateLurk(False))
	elif arg_1_0.op == WorldConst.OpActionAttachmentMove:
		assert(#arg_1_0.path > 0)

		local var_1_21 = arg_1_0.attachment.Clone()
		local var_1_22 = arg_1_0.path[#arg_1_0.path]

		var_1_2.GetCell(arg_1_0.attachment.row, arg_1_0.attachment.column).RemoveAttachment(arg_1_0.attachment)

		local var_1_23 = var_1_2.GetCell(var_1_22.row, var_1_22.column)

		assert(var_1_23, "dest cell not exist. " .. var_1_22.row .. ", " .. var_1_22.column)

		var_1_21.row = var_1_22.row
		var_1_21.column = var_1_22.column

		var_1_23.AddAttachment(var_1_21)
	elif arg_1_0.op == WorldConst.OpActionEventOp:
		local var_1_24 = arg_1_0.effect

		if var_1_24.effect_type == WorldMapAttachment.EffectEventFOV:
			var_1_2.EventEffectOpenFOV(var_1_24)

		arg_1_0.attachment.UpdateDataOp(arg_1_0.attachment.dataop - 1)
	elif arg_1_0.op == WorldConst.OpActionTaskGoto:
		local var_1_25 = arg_1_0.effect

		if var_1_25.effect_type == WorldMapAttachment.EffectEventFOV:
			var_1_2.EventEffectOpenFOV(var_1_25)

	if arg_1_0.childOps:
		_.each(arg_1_0.childOps, function(arg_10_0)
			if not arg_10_0.applied:
				arg_10_0.Apply())

	if arg_1_0.stepOps:
		_.each(arg_1_0.stepOps, function(arg_11_0)
			if not arg_11_0.applied:
				arg_11_0.Apply())

	arg_1_0.ApplyAttachmentUpdate()
	arg_1_0.ApplyNetUpdate()

	if arg_1_0.callbacksWhenApplied:
		_.each(arg_1_0.callbacksWhenApplied, function(arg_12_0)
			arg_12_0())

def var_0_0.ApplyAttachmentUpdate(arg_13_0):
	local var_13_0 = getProxy(WorldProxy)
	local var_13_1 = nowWorld().GetActiveMap()

	if arg_13_0.updateAttachmentCells:
		var_13_0.UpdateMapAttachmentCells(var_13_1.id, arg_13_0.updateAttachmentCells)

		for iter_13_0, iter_13_1 in pairs(arg_13_0.updateAttachmentCells):
			local var_13_2 = var_13_1.GetCell(iter_13_1.pos.row, iter_13_1.pos.column)

			_.each(iter_13_1.attachmentList, function(arg_14_0)
				if not var_13_2.ContainsAttachment(arg_14_0):
					WPool.Return(arg_14_0))

		arg_13_0.updateAttachmentCells = None

def var_0_0.ApplyNetUpdate(arg_15_0):
	local var_15_0 = getProxy(WorldProxy)
	local var_15_1 = nowWorld()
	local var_15_2 = var_15_1.GetActiveMap()

	if arg_15_0.staminaUpdate:
		var_15_1.staminaMgr.ChangeStamina(arg_15_0.staminaUpdate[1], arg_15_0.staminaUpdate[2])

		arg_15_0.staminaUpdate = None

	if arg_15_0.shipUpdates and #arg_15_0.shipUpdates > 0:
		var_15_0.ApplyShipUpdate(arg_15_0.shipUpdates)
		WPool.ReturnArray(arg_15_0.shipUpdates)

		arg_15_0.shipUpdates = None

	if arg_15_0.fleetAttachUpdates and #arg_15_0.fleetAttachUpdates > 0:
		var_15_0.ApplyFleetAttachUpdate(var_15_2.id, arg_15_0.fleetAttachUpdates)
		WPool.ReturnArray(arg_15_0.fleetAttachUpdates)

		arg_15_0.fleetAttachUpdates = None

	if arg_15_0.fleetUpdates and #arg_15_0.fleetUpdates > 0:
		var_15_0.ApplyFleetUpdate(var_15_2.id, arg_15_0.fleetUpdates)
		WPool.ReturnArray(arg_15_0.fleetUpdates)

		arg_15_0.fleetUpdates = None

	if arg_15_0.terrainUpdates and #arg_15_0.terrainUpdates > 0:
		var_15_0.ApplyTerrainUpdate(var_15_2.id, arg_15_0.terrainUpdates)
		WPool.ReturnArray(arg_15_0.terrainUpdates)

		arg_15_0.terrainUpdates = None

	if arg_15_0.salvageUpdates and #arg_15_0.salvageUpdates > 0:
		var_15_0.ApplySalvageUpdate(arg_15_0.salvageUpdates)
		WPool.ReturnArray(arg_15_0.salvageUpdates)

		arg_15_0.salvageUpdates = None

def var_0_0.AddCallbackWhenApplied(arg_16_0, arg_16_1):
	if not arg_16_0.callbacksWhenApplied:
		arg_16_0.callbacksWhenApplied = {}

	table.insert(arg_16_0.callbacksWhenApplied, arg_16_1)

return var_0_0
