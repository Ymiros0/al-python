local var_0_0 = class("FleetAIAction")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.actType = arg_1_1.act_type
	arg_1_0.line = {
		row = arg_1_1.ai_pos.row,
		column = arg_1_1.ai_pos.column
	}

	if arg_1_1.target_pos and arg_1_1.target_pos.row < 9999 and arg_1_1.target_pos.column < 9999:
		arg_1_0.target = {
			row = arg_1_1.target_pos.row,
			column = arg_1_1.target_pos.column
		}

	arg_1_0.shipUpdate = _.map(arg_1_1.ship_update, function(arg_2_0)
		return {
			id = arg_2_0.id,
			hpRant = arg_2_0.hp_rant
		})
	arg_1_0.cellUpdates = {}

	_.each(arg_1_1.map_update, function(arg_3_0)
		if arg_3_0.item_type != ChapterConst.AttachNone and arg_3_0.item_type != ChapterConst.AttachBorn and arg_3_0.item_type != ChapterConst.AttachBorn_Sub and (arg_3_0.item_type != ChapterConst.AttachStory or arg_3_0.item_data != ChapterConst.StoryTrigger):
			local var_3_0 = arg_3_0.item_type == ChapterConst.AttachChampion and ChapterChampionPackage.New(arg_3_0) or ChapterCell.New(arg_3_0)

			table.insert(arg_1_0.cellUpdates, var_3_0))

	arg_1_0.commanderSkillEffectId = arg_1_1.commander_skill_effect_id

def var_0_0.applyTo(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_1.getFleet(FleetType.Normal, arg_4_0.line.row, arg_4_0.line.column)

	if var_4_0:
		return arg_4_0.applyToFleet(arg_4_1, var_4_0, arg_4_2)

	return False, "can not find any fleet at. [" .. arg_4_0.line.row .. ", " .. arg_4_0.line.column .. "]"

def var_0_0.applyToFleet(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if not arg_5_2.isValid():
		return False, "fleet " .. arg_5_2.id .. " is invalid."

	local var_5_0 = 0

	if arg_5_1.isPlayingWithBombEnemy():
		if not arg_5_3:
			_.each(arg_5_0.cellUpdates, function(arg_6_0)
				local var_6_0 = arg_5_1.getChapterCell(arg_6_0.row, arg_6_0.column)

				if var_6_0.flag == ChapterConst.CellFlagActive and arg_6_0.flag == ChapterConst.CellFlagDisabled:
					local var_6_1 = pg.specialunit_template[var_6_0.attachmentId]

					assert(var_6_1, "specialunit_template not exist. " .. var_6_0.attachmentId)

					arg_5_1.modelCount = arg_5_1.modelCount + var_6_1.enemy_point

				arg_5_1.mergeChapterCell(arg_6_0)

				var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyAttachment))
	elif arg_5_0.target:
		local var_5_1 = _.detect(arg_5_0.cellUpdates, function(arg_7_0)
			return arg_7_0.row == arg_5_0.target.row and arg_7_0.column == arg_5_0.target.column)

		if not arg_5_3:
			if arg_5_0.shipUpdate:
				_.each(arg_5_0.shipUpdate, function(arg_8_0)
					arg_5_1.updateFleetShipHp(arg_8_0.id, arg_8_0.hpRant))

				var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyFleet)

			if var_5_1:
				if isa(var_5_1, ChapterChampionPackage):
					arg_5_1.mergeChampion(var_5_1)

					var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyChampion)
				else
					arg_5_1.mergeChapterCell(var_5_1)

					var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyAttachment)

				var_5_0 = bit.bor(var_5_0, ChapterConst.DirtyFleet)

	return True, var_5_0

def var_0_0.PlayAIAction(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	local var_9_0 = arg_9_1.getFleetIndex(FleetType.Normal, arg_9_0.line.row, arg_9_0.line.column)

	assert(var_9_0)

	if arg_9_1.isPlayingWithBombEnemy():
		local var_9_1 = arg_9_1.fleets[var_9_0]
		local var_9_2 = arg_9_1.getMapShip(var_9_1)

		arg_9_2.viewComponent.doPlayStrikeAnim(var_9_2, var_9_2.GetMapStrikeAnim(), arg_9_3)
	elif arg_9_0.actType == ChapterConst.ActType_Poison:
		arg_9_3()
	elif arg_9_0.target:
		local var_9_3 = arg_9_1.fleets[var_9_0]
		local var_9_4 = _.detect(arg_9_0.cellUpdates, function(arg_10_0)
			return arg_10_0.row == arg_9_0.target.row and arg_10_0.column == arg_9_0.target.column)

		assert(var_9_4, "can not find cell")

		if var_9_4.attachment == ChapterConst.AttachLandbase:
			if pg.land_based_template[var_9_4.attachmentId].type == ChapterConst.LBCoastalGun:
				local var_9_5 = arg_9_1.getMapShip(var_9_3)

				arg_9_2.viewComponent.doPlayStrikeAnim(var_9_5, var_9_5.GetMapStrikeAnim(), arg_9_3)
			else
				assert(False)

			return

		local var_9_6 = "-" .. var_9_4.data / 100 .. "%"
		local var_9_7 = arg_9_0.commanderSkillEffectId
		local var_9_8 = var_9_3.getSkill(var_9_7)

		assert(var_9_8, "can not find skill. " .. var_9_7)

		local var_9_9 = var_9_3.findCommanderBySkillId(var_9_7)

		assert(var_9_9, "command can not find by skill id. " .. var_9_7)
		arg_9_2.viewComponent.doPlayCommander(var_9_9, function()
			if var_9_8.GetType() == FleetSkill.TypeAirStrikeDodge:
				arg_9_2.viewComponent.easeAvoid(arg_9_2.viewComponent.grid.cellFleets[var_9_3.id].tf.position, arg_9_3)

				return
			elif var_9_8.GetType() == FleetSkill.TypeAttack:
				local var_11_0 = var_9_8.GetArgs()
				local var_11_1

				switch(var_11_0[1], {
					def airfight:()
						var_11_1 = "AirStrikeUI",
					def torpedo:()
						var_11_1 = "SubTorpedoUI",
					def cannon:()
						var_11_1 = "CannonUI"
				})
				assert(var_11_1)
				arg_9_2.viewComponent.doPlayStrikeAnim(arg_9_1.getStrikeAnimShip(var_9_3, var_11_1), var_11_1, function()
					arg_9_2.viewComponent.strikeEnemy(arg_9_0.target, var_9_6, arg_9_3))

				return
			else
				assert(False))
	else
		arg_9_3()

return var_0_0
