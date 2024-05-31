local var_0_0 = import(".Chapter")

def var_0_0.update(arg_1_0, arg_1_1):
	assert(arg_1_1.id == arg_1_0.id, "章节ID不一致, 无法更新数据")

	arg_1_0.active = True
	arg_1_0.dueTime = arg_1_1.time
	arg_1_0.loopFlag = arg_1_1.loop_flag
	arg_1_0.modelCount = arg_1_1.model_act_count
	arg_1_0.roundIndex = arg_1_1.round
	arg_1_0.subAutoAttack = arg_1_1.is_submarine_auto_attack
	arg_1_0.barriers = 0
	arg_1_0.pathFinder = OrientedPathFinding.New({}, ChapterConst.MaxRow, ChapterConst.MaxColumn)
	arg_1_0.wallAssets = {}

	if arg_1_0.getConfig("wall_prefab") and #arg_1_0.getConfig("wall_prefab") > 0:
		for iter_1_0, iter_1_1 in ipairs(arg_1_0.getConfig("wall_prefab")):
			arg_1_0.wallAssets[iter_1_1[1] .. "_" .. iter_1_1[2]] = iter_1_1

	arg_1_0.winConditions = {}

	local var_1_0 = arg_1_0.getConfig("win_condition")

	assert(var_1_0, "Assure Chapter's WIN Conditions is not empty")

	for iter_1_2, iter_1_3 in pairs(var_1_0):
		table.insert(arg_1_0.winConditions, {
			type = iter_1_3[1],
			param = iter_1_3[2]
		})

	arg_1_0.loseConditions = {}

	local var_1_1 = arg_1_0.getConfig("lose_condition")

	assert(var_1_1, "Assure Chapter's LOSE Conditions is not empty")

	for iter_1_4, iter_1_5 in pairs(var_1_1):
		table.insert(arg_1_0.loseConditions, {
			type = iter_1_5[1],
			param = iter_1_5[2]
		})

	arg_1_0.theme = ChapterTheme.New(arg_1_0.getConfig("theme"))

	local var_1_2 = arg_1_1.cell_list
	local var_1_3 = arg_1_1.cell_flag_list
	local var_1_4 = arg_1_0.getConfig("float_items")
	local var_1_5 = arg_1_0.getConfig("grids")

	arg_1_0.cells = {}
	arg_1_0.cellAttachments = {}

	local function var_1_6(arg_2_0)
		local var_2_0 = ChapterCell.Line2Name(arg_2_0.pos.row, arg_2_0.pos.column)

		if arg_2_0.item_type == ChapterConst.AttachStory and arg_2_0.item_data == ChapterConst.StoryTrigger:
			if arg_1_0.cellAttachments[var_2_0]:
				warning("Multi Cell Attachemnts in one cell " .. arg_2_0.pos.row .. " " .. arg_2_0.pos.column)

			arg_1_0.cellAttachments[var_2_0] = ChapterCell.New(arg_2_0)
			arg_2_0 = {
				item_id = 0,
				item_data = 0,
				item_flag = 0,
				pos = {
					row = arg_2_0.pos.row,
					column = arg_2_0.pos.column
				},
				item_type = ChapterConst.AttachNone
			}

		if not arg_1_0.cells[var_2_0] or arg_1_0.cells[var_2_0].attachment == ChapterConst.AttachNone:
			local var_2_1 = ChapterCell.New(arg_2_0)

			if var_2_1.attachment == ChapterConst.AttachOni_Target or var_2_1.attachment == ChapterConst.AttachOni:
				var_2_1.attachment = ChapterConst.AttachNone

			local var_2_2 = _.detect(var_1_4, function(arg_3_0)
				return arg_3_0[1] == var_2_1.row and arg_3_0[2] == var_2_1.column)

			if var_2_2:
				var_2_1.item = var_2_2[3]
				var_2_1.itemOffset = Vector2(var_2_2[4], var_2_2[5])

			arg_1_0.cells[var_2_0] = var_2_1

			return var_2_1

	_.each(var_1_2, function(arg_4_0)
		var_1_6(arg_4_0))
	_.each(var_1_5, function(arg_5_0)
		local var_5_0 = ChapterCell.Line2Name(arg_5_0[1], arg_5_0[2])

		;(arg_1_0.cells[var_5_0] or var_1_6({
			pos = {
				row = arg_5_0[1],
				column = arg_5_0[2]
			},
			item_type = ChapterConst.AttachNone
		})).SetWalkable(arg_5_0[3]))

	arg_1_0.indexMin, arg_1_0.indexMax = Vector2(ChapterConst.MaxRow, ChapterConst.MaxColumn), Vector2(-ChapterConst.MaxRow, -ChapterConst.MaxColumn)

	_.each(var_1_5, function(arg_6_0)
		arg_1_0.indexMin.x = math.min(arg_1_0.indexMin.x, arg_6_0[1])
		arg_1_0.indexMin.y = math.min(arg_1_0.indexMin.y, arg_6_0[2])
		arg_1_0.indexMax.x = math.max(arg_1_0.indexMax.x, arg_6_0[1])
		arg_1_0.indexMax.y = math.max(arg_1_0.indexMax.y, arg_6_0[2]))
	_.each(var_1_3 or {}, function(arg_7_0)
		local var_7_0 = ChapterCell.Line2Name(arg_7_0.pos.row, arg_7_0.pos.column)
		local var_7_1 = arg_1_0.cells[var_7_0]

		assert(var_7_1, "Attach cellFlaglist On NIL Cell " .. var_7_0)

		if var_7_1:
			var_7_1.updateFlagList(arg_7_0))

	arg_1_0.buff_list = {}

	if arg_1_1.buff_list:
		for iter_1_6, iter_1_7 in ipairs(arg_1_1.buff_list):
			arg_1_0.buff_list[iter_1_6] = iter_1_7

	arg_1_0.operationBuffList = {}

	for iter_1_8, iter_1_9 in ipairs(arg_1_1.operation_buff):
		arg_1_0.operationBuffList[#arg_1_0.operationBuffList + 1] = iter_1_9

	local var_1_7 = arg_1_0.getNpcShipByType()

	arg_1_0.fleets = {}

	for iter_1_10, iter_1_11 in ipairs(arg_1_1.group_list):
		local var_1_8 = ChapterFleet.New(iter_1_11, var_1_7)

		var_1_8.setup(arg_1_0)

		arg_1_0.fleets[iter_1_10] = var_1_8

	arg_1_0.fleets = _.sort(arg_1_0.fleets, function(arg_8_0, arg_8_1)
		return arg_8_0.id < arg_8_1.id)

	if arg_1_1.escort_list:
		for iter_1_12, iter_1_13 in ipairs(arg_1_1.escort_list):
			arg_1_0.fleets[#arg_1_0.fleets + 1] = ChapterTransportFleet.New(iter_1_13, #arg_1_0.fleets + 1)

	arg_1_0.findex = 0
	arg_1_0.findex = arg_1_0.getNextValidIndex()

	if arg_1_0.findex == 0:
		arg_1_0.findex = 1

	arg_1_0.champions = {}

	if arg_1_1.ai_list:
		for iter_1_14, iter_1_15 in ipairs(arg_1_1.ai_list):
			if iter_1_15.item_flag != 1:
				local var_1_9 = ChapterChampionPackage.New(iter_1_15)

				arg_1_0.mergeChampion(var_1_9, True)

	arg_1_0.airDominanceStatus = None
	arg_1_0.extraFlagList = {}

	for iter_1_16, iter_1_17 in ipairs(arg_1_1.extra_flag_list):
		table.insert(arg_1_0.extraFlagList, iter_1_17)

	arg_1_0.defeatEnemies = arg_1_1.kill_count or 0
	arg_1_0.BaseHP = arg_1_1.chapter_hp or 0
	arg_1_0.orignalShipCount = arg_1_1.init_ship_count or 0
	arg_1_0.combo = arg_1_1.continuous_kill_count or 0
	arg_1_0.scoreHistory = {}

	for iter_1_18 = ys.Battle.BattleConst.BattleScore.D, ys.Battle.BattleConst.BattleScore.S:
		arg_1_0.scoreHistory[iter_1_18] = 0

	if arg_1_1.battle_statistics:
		for iter_1_19, iter_1_20 in ipairs(arg_1_1.battle_statistics):
			arg_1_0.scoreHistory[iter_1_20.id] = iter_1_20.count

	local var_1_10 = {}

	if arg_1_1.chapter_strategy_list:
		for iter_1_21, iter_1_22 in ipairs(arg_1_1.chapter_strategy_list):
			var_1_10[iter_1_22.id] = iter_1_22.count

	arg_1_0.strategies = var_1_10
	arg_1_0.duties = {}

	if #arg_1_1.fleet_duties > 0:
		_.each(arg_1_1.fleet_duties, function(arg_9_0)
			arg_1_0.duties[arg_9_0.key] = arg_9_0.value)

	arg_1_0.moveStep = arg_1_1.move_step_count or 0
	arg_1_0.activateAmbush = not arg_1_0.isLoop() and arg_1_0.GetWillActiveAmbush()

def var_0_0.retreat(arg_10_0, arg_10_1):
	if arg_10_1:
		arg_10_0.todayDefeatCount = arg_10_0.todayDefeatCount + 1

		arg_10_0.updateTodayDefeatCount()

def var_0_0.CleanLevelData(arg_11_0):
	arg_11_0.active = False
	arg_11_0.loopFlag = 0
	arg_11_0.dueTime = None
	arg_11_0.cells = None
	arg_11_0.fleets = None
	arg_11_0.findex = None
	arg_11_0.champions = None
	arg_11_0.cellAttachments = None
	arg_11_0.round = None
	arg_11_0.airDominanceStatus = None
	arg_11_0.winConditions, arg_11_0.loseConditions = None
	arg_11_0.theme = None
	arg_11_0.buff_list = None
	arg_11_0.operationBuffList = None
	arg_11_0.modelCount = None
	arg_11_0.roundIndex = None
	arg_11_0.subAutoAttack = None
	arg_11_0.barriers = None
	arg_11_0.pathFinder = None
	arg_11_0.wallAssets = None
	arg_11_0.strategies = None
	arg_11_0.duties = None
	arg_11_0.indexMin, arg_11_0.indexMax = None
	arg_11_0.extraFlagList = None
	arg_11_0.defeatEnemies = None
	arg_11_0.BaseHP = None
	arg_11_0.orignalShipCount = None
	arg_11_0.combo = None
	arg_11_0.scoreHistory = None

def var_0_0.__index(arg_12_0, arg_12_1):
	if arg_12_1 == "fleet":
		local var_12_0 = rawget(arg_12_0, "fleets")

		if not var_12_0:
			return None

		return var_12_0[rawget(arg_12_0, "findex")]

	return rawget(arg_12_0, arg_12_1) or var_0_0[arg_12_1]

def var_0_0.GetActiveFleet(arg_13_0):
	if not arg_13_0.fleets:
		return None

	return arg_13_0.fleets[arg_13_0.findex]

def var_0_0.getFleetById(arg_14_0, arg_14_1):
	return _.detect(arg_14_0.fleets, function(arg_15_0)
		return arg_15_0.id == arg_14_1)

def var_0_0.getChapterSupportFleet(arg_16_0):
	return table.Find(arg_16_0.fleets, function(arg_17_0, arg_17_1)
		return arg_17_1.getFleetType() == FleetType.Support)

def var_0_0.getFleetByShipVO(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_1.id
	local var_18_1

	for iter_18_0, iter_18_1 in ipairs(arg_18_0.fleets):
		if iter_18_1.getShip(var_18_0):
			var_18_1 = iter_18_1

			break

	return var_18_1

def var_0_0.getRound(arg_19_0):
	return arg_19_0.roundIndex % 2

def var_0_0.getRoundNum(arg_20_0):
	return math.floor(arg_20_0.roundIndex / 2)

def var_0_0.IncreaseRound(arg_21_0):
	arg_21_0.roundIndex = arg_21_0.roundIndex + 1

def var_0_0.existMoveLimit(arg_22_0):
	return arg_22_0.getConfig("is_limit_move") == 1 or arg_22_0.existOni() or arg_22_0.isPlayingWithBombEnemy()

def var_0_0.getChapterCell(arg_23_0, arg_23_1, arg_23_2):
	local var_23_0 = ChapterCell.Line2Name(arg_23_1, arg_23_2)

	return Clone(arg_23_0.cells[var_23_0])

def var_0_0.GetRawChapterCell(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0 = ChapterCell.Line2Name(arg_24_1, arg_24_2)

	return arg_24_0.cells[var_24_0]

def var_0_0.FilterCell(arg_25_0, arg_25_1):
	return table.Checkout(arg_25_0.cells, arg_25_1)

def var_0_0.findChapterCell(arg_26_0, arg_26_1, arg_26_2):
	for iter_26_0, iter_26_1 in pairs(arg_26_0.cells):
		if iter_26_1.attachment == arg_26_1 and (not arg_26_2 or iter_26_1.attachmentId == arg_26_2):
			return iter_26_1

	return None

def var_0_0.findChapterCells(arg_27_0, arg_27_1, arg_27_2):
	local var_27_0 = {}

	for iter_27_0, iter_27_1 in pairs(arg_27_0.cells):
		if iter_27_1.attachment == arg_27_1 and (not arg_27_2 or iter_27_1.attachmentId == arg_27_2):
			table.insert(var_27_0, iter_27_1)

	return var_27_0

def var_0_0.GetBossCell(arg_28_0):
	return table.Find(arg_28_0.cells, function(arg_29_0, arg_29_1)
		return ChapterConst.IsBossCell(arg_29_1))

def var_0_0.mergeChapterCell(arg_30_0, arg_30_1, arg_30_2):
	local var_30_0 = ChapterCell.Line2Name(arg_30_1.row, arg_30_1.column)
	local var_30_1 = arg_30_0.cells[var_30_0]
	local var_30_2 = var_30_1 == None or var_30_1.attachment != arg_30_1.attachment or var_30_1.attachmentId != arg_30_1.attachmentId

	if var_30_1:
		var_30_1.attachment = arg_30_1.attachment
		var_30_1.attachmentId = arg_30_1.attachmentId
		var_30_1.flag = arg_30_1.flag
		var_30_1.data = arg_30_1.data
		arg_30_1 = var_30_1

	if not arg_30_2 and var_30_2 and ChapterConst.NeedMarkAsLurk(arg_30_1):
		arg_30_1.trait = ChapterConst.TraitLurk

	if ChapterConst.IsBossCell(arg_30_1):
		local var_30_3 = arg_30_0.getChampionIndex(arg_30_1.row, arg_30_1.column)

		if var_30_3:
			table.remove(arg_30_0.champions, var_30_3)

	arg_30_0.updateChapterCell(arg_30_1)

def var_0_0.updateChapterCell(arg_31_0, arg_31_1):
	local var_31_0 = ChapterCell.Line2Name(arg_31_1.row, arg_31_1.column)

	arg_31_0.cells[var_31_0] = Clone(arg_31_1)

def var_0_0.clearChapterCell(arg_32_0, arg_32_1, arg_32_2):
	local var_32_0 = ChapterCell.Line2Name(arg_32_1, arg_32_2)
	local var_32_1 = arg_32_0.cells[var_32_0]

	var_32_1.attachment = ChapterConst.AttachNone
	var_32_1.attachmentId = 0
	var_32_1.flag = ChapterConst.CellFlagActive
	var_32_1.data = 0
	var_32_1.trait = ChapterConst.TraitNone

def var_0_0.GetChapterCellAttachemnts(arg_33_0):
	return arg_33_0.cellAttachments

def var_0_0.GetRawChapterAttachemnt(arg_34_0, arg_34_1, arg_34_2):
	local var_34_0 = ChapterCell.Line2Name(arg_34_1, arg_34_2)

	return arg_34_0.cellAttachments[var_34_0]

def var_0_0.getShips(arg_35_0):
	local var_35_0 = {}

	_.each(arg_35_0.fleets, function(arg_36_0)
		local var_36_0 = arg_36_0.getShips(True)

		_.each(var_36_0, function(arg_37_0)
			table.insert(var_35_0, Clone(arg_37_0))))

	return var_35_0

def var_0_0.getNextValidIndex(arg_38_0):
	for iter_38_0 = arg_38_0.findex + 1, #arg_38_0.fleets:
		if arg_38_0.fleets[iter_38_0].getFleetType() == FleetType.Normal and arg_38_0.fleets[iter_38_0].isValid():
			return iter_38_0

	for iter_38_1 = 1, arg_38_0.findex - 1:
		if arg_38_0.fleets[iter_38_1].getFleetType() == FleetType.Normal and arg_38_0.fleets[iter_38_1].isValid():
			return iter_38_1

	return 0

def var_0_0.getAmbushRate(arg_39_0, arg_39_1, arg_39_2):
	local var_39_0 = arg_39_1.getInvestSums()
	local var_39_1 = arg_39_0.getConfig("investigation_ratio")
	local var_39_2 = var_39_1 / (var_39_1 + var_39_0) / 4
	local var_39_3 = _.detect(arg_39_0.getConfig("ambush_ratio_extra"), function(arg_40_0)
		return arg_40_0[1] == arg_39_2.row and arg_40_0[2] == arg_39_2.column)
	local var_39_4 = _.detect(arg_39_0.getConfig("ambush_ratio_extra"), function(arg_41_0)
		return #arg_41_0 == 1)
	local var_39_5

	var_39_5 = var_39_3 and var_39_3[3] / 10000 or 0

	local var_39_6 = var_39_5 + (var_39_4 and var_39_4[1] / 10000 or 0)
	local var_39_7 = 0.05 + var_39_2 * math.max(arg_39_1.step - 1, 0) + var_39_6

	if var_39_6 == 0:
		var_39_7 = var_39_7 - arg_39_1.getEquipAmbushRateReduce()

	return (math.clamp(var_39_7, 0, 1))

def var_0_0.getAmbushDodge(arg_42_0, arg_42_1):
	local var_42_0 = arg_42_1.line
	local var_42_1 = arg_42_1.getDodgeSums()
	local var_42_2 = var_42_1 / (var_42_1 + arg_42_0.getConfig("avoid_ratio"))
	local var_42_3 = _.detect(arg_42_0.getConfig("ambush_ratio_extra"), function(arg_43_0)
		return arg_43_0[1] == var_42_0.row and arg_43_0[2] == var_42_0.column)
	local var_42_4

	var_42_4 = var_42_3 and var_42_3[3] / 10000 or 0

	if var_42_4 == 0:
		var_42_2 = var_42_2 + arg_42_1.getEquipDodgeRateUp()

	return (math.clamp(var_42_2, 0, 1))

def var_0_0.inWartime(arg_44_0):
	return arg_44_0.dueTime and pg.TimeMgr.GetInstance().GetServerTime() < arg_44_0.dueTime

def var_0_0.inActTime(arg_45_0):
	local var_45_0 = arg_45_0.GetBindActID()

	if var_45_0 == 0:
		return True

	local var_45_1 = var_45_0 and getProxy(ActivityProxy).getActivityById(var_45_0)

	return var_45_1 and not var_45_1.isEnd()

def var_0_0.getRemainTime(arg_46_0):
	return arg_46_0.dueTime and math.max(arg_46_0.dueTime - pg.TimeMgr.GetInstance().GetServerTime() - 1, 0) or 0

def var_0_0.getStartTime(arg_47_0):
	return math.max(arg_47_0.dueTime - arg_47_0.getConfig("time"), 0)

def var_0_0.GetWillActiveAmbush(arg_48_0):
	if not arg_48_0.existAmbush():
		return False

	local var_48_0 = arg_48_0.getConfig("avoid_require")

	return not _.any(arg_48_0.fleets, function(arg_49_0)
		return arg_49_0.getFleetType() == FleetType.Normal and arg_49_0.getInvestSums(True) >= var_48_0)

def var_0_0.findPath(arg_50_0, arg_50_1, arg_50_2, arg_50_3):
	local var_50_0 = {}

	for iter_50_0 = 0, ChapterConst.MaxRow - 1:
		var_50_0[iter_50_0] = var_50_0[iter_50_0] or {}

		for iter_50_1 = 0, ChapterConst.MaxColumn - 1:
			var_50_0[iter_50_0][iter_50_1] = var_50_0[iter_50_0][iter_50_1] or {}

			local var_50_1 = PathFinding.PrioForbidden
			local var_50_2 = ChapterConst.ForbiddenAll
			local var_50_3 = ChapterCell.Line2Name(iter_50_0, iter_50_1)
			local var_50_4 = arg_50_0.cells[var_50_3]

			if var_50_4 and var_50_4.IsWalkable():
				var_50_1 = PathFinding.PrioNormal

				if arg_50_0.considerAsObstacle(arg_50_1, var_50_4.row, var_50_4.column):
					var_50_1 = PathFinding.PrioObstacle

				if arg_50_1 == ChapterConst.SubjectPlayer:
					var_50_2 = var_50_4.forbiddenDirections
				else
					var_50_2 = ChapterConst.ForbiddenNone

			var_50_0[iter_50_0][iter_50_1].forbiddens = var_50_2
			var_50_0[iter_50_0][iter_50_1].priority = var_50_1

	if arg_50_1 == ChapterConst.SubjectPlayer:
		local var_50_5 = arg_50_0.getCoastalGunArea()

		for iter_50_2, iter_50_3 in ipairs(var_50_5):
			var_50_0[iter_50_3.row][iter_50_3.column].priority = math.max(var_50_0[iter_50_3.row][iter_50_3.column].priority, PathFinding.PrioObstacle)

	local var_50_6 = var_50_0[arg_50_3.row] and var_50_0[arg_50_3.row][arg_50_3.column]

	if var_50_6:
		var_50_6.priority = arg_50_0.considerAsStayPoint(arg_50_1, arg_50_3.row, arg_50_3.column) and PathFinding.PrioNormal or PathFinding.PrioObstacle

	arg_50_0.pathFinder.cells = var_50_0

	return arg_50_0.pathFinder.Find(arg_50_2, arg_50_3)

def var_0_0.FindBossPath(arg_51_0, arg_51_1, arg_51_2):
	local var_51_0 = ChapterConst.SubjectPlayer
	local var_51_1 = {}

	for iter_51_0 = 0, ChapterConst.MaxRow - 1:
		var_51_1[iter_51_0] = var_51_1[iter_51_0] or {}

		for iter_51_1 = 0, ChapterConst.MaxColumn - 1:
			var_51_1[iter_51_0][iter_51_1] = var_51_1[iter_51_0][iter_51_1] or {}

			local var_51_2 = PathFinding.PrioForbidden
			local var_51_3 = ChapterConst.ForbiddenAll
			local var_51_4
			local var_51_5 = ChapterCell.Line2Name(iter_51_0, iter_51_1)
			local var_51_6 = arg_51_0.cells[var_51_5]

			if var_51_6 and var_51_6.IsWalkable():
				var_51_2 = PathFinding.PrioNormal

				if arg_51_0.considerAsObstacle(var_51_0, var_51_6.row, var_51_6.column):
					var_51_2 = PathFinding.PrioObstacle

				local var_51_7 = arg_51_0.GetEnemy(var_51_6.row, var_51_6.column)

				if var_51_7:
					var_51_2 = PathFinding.PrioNormal
					var_51_4 = not ChapterConst.IsBossCell(var_51_7)

				var_51_3 = var_51_6.forbiddenDirections

			var_51_1[iter_51_0][iter_51_1].forbiddens = var_51_3
			var_51_1[iter_51_0][iter_51_1].priority = var_51_2
			var_51_1[iter_51_0][iter_51_1].isEnemy = var_51_4

	local var_51_8 = arg_51_0.getCoastalGunArea()

	for iter_51_2, iter_51_3 in ipairs(var_51_8):
		var_51_1[iter_51_3.row][iter_51_3.column].priority = math.max(var_51_1[iter_51_3.row][iter_51_3.column].priority, PathFinding.PrioObstacle)

	local var_51_9 = var_51_1[arg_51_2.row] and var_51_1[arg_51_2.row][arg_51_2.column]

	if var_51_9:
		var_51_9.priority = arg_51_0.considerAsStayPoint(var_51_0, arg_51_2.row, arg_51_2.column) and PathFinding.PrioNormal or PathFinding.PrioObstacle

	return OrientedWeightPathFinding.StaticFind(var_51_1, ChapterConst.MaxRow, ChapterConst.MaxColumn, arg_51_1, arg_51_2)

def var_0_0.getWaveCount(arg_52_0):
	local var_52_0 = 0

	for iter_52_0, iter_52_1 in pairs(arg_52_0.cells):
		if iter_52_1.attachment == ChapterConst.AttachEnemy and underscore.detect(arg_52_0.getConfig("grids"), function(arg_53_0)
			if arg_53_0[1] == iter_52_1.row and arg_53_0[2] == iter_52_1.column and (arg_53_0[4] == ChapterConst.AttachElite or arg_53_0[4] == ChapterConst.AttachEnemy):
				return True

			return False):
			var_52_0 = var_52_0 + 1

	local var_52_1 = 0
	local var_52_2 = pg.chapter_group_refresh[arg_52_0.id]

	if var_52_2:
		local var_52_3 = 1

		repeat
			local var_52_4 = False

			for iter_52_2, iter_52_3 in ipairs(var_52_2.enemy_refresh):
				var_52_1 = var_52_1 + (iter_52_3[var_52_3] or 0)
				var_52_4 = var_52_4 or tobool(iter_52_3[var_52_3])

			if var_52_0 <= var_52_1:
				return var_52_3

			var_52_3 = var_52_3 + 1
		until not var_52_4
	else
		local var_52_5 = arg_52_0.getConfig("enemy_refresh")
		local var_52_6 = arg_52_0.getConfig("elite_refresh")

		for iter_52_4, iter_52_5 in pairs(var_52_5):
			var_52_1 = var_52_1 + iter_52_5

			if iter_52_4 <= #var_52_6:
				var_52_1 = var_52_1 + var_52_6[iter_52_4]

			if var_52_0 <= var_52_1:
				return iter_52_4

	return 1

def var_0_0.IsFinalBossRefreshed(arg_54_0):
	return tobool(arg_54_0.findChapterCell(ChapterConst.AttachBoss))

def var_0_0.getFleetAmmo(arg_55_0, arg_55_1):
	local var_55_0 = arg_55_1.getShipAmmo()
	local var_55_1 = arg_55_1.getFleetType()

	if var_55_1 == FleetType.Normal:
		var_55_0 = var_55_0 + arg_55_0.getConfig("ammo_total")
	elif var_55_1 == FleetType.Submarine:
		var_55_0 = var_55_0 + arg_55_0.getConfig("ammo_submarine")
	else
		assert(False, "invalide operation.")

	local var_55_2 = arg_55_1.restAmmo

	return var_55_0, var_55_2

def var_0_0.GetInteractableStrategies(arg_56_0):
	local var_56_0 = arg_56_0.fleet.getStrategies()
	local var_56_1 = _.filter(var_56_0, function(arg_57_0)
		local var_57_0 = pg.strategy_data_template[arg_57_0.id]

		return var_57_0 and var_57_0.type != ChapterConst.StgTypeBindFleetPassive)
	local var_56_2 = arg_56_0.fleet.getFormationStg()

	table.insert(var_56_1, 1, {
		id = var_56_2
	})

	if arg_56_0.GetSubmarineFleet():
		table.insert(var_56_1, 3, {
			id = ChapterConst.StrategyHuntingRange
		})
		table.insert(var_56_1, 4, {
			id = ChapterConst.StrategySubAutoAttack
		})
		table.insert(var_56_1, 5, {
			id = ChapterConst.StrategySubTeleport
		})

	local var_56_3 = arg_56_0.getChapterSupportFleet()

	if var_56_3:
		table.insertto(var_56_1, _.filter(var_56_3.getStrategies(), function(arg_58_0)
			local var_58_0 = pg.strategy_data_template[arg_58_0.id]

			return var_58_0 and var_58_0.type == ChapterConst.StgTypeBindSupportConsume))

	if #arg_56_0.strategies > 0:
		for iter_56_0, iter_56_1 in pairs(arg_56_0.strategies):
			table.insert(var_56_1, {
				id = iter_56_0,
				count = iter_56_1
			})

	return var_56_1

def var_0_0.getFleetStates(arg_59_0, arg_59_1):
	local var_59_0 = {}
	local var_59_1, var_59_2 = arg_59_0.getFleetAmmo(arg_59_1)

	if var_59_2 >= ChapterConst.AmmoRich:
		table.insert(var_59_0, ChapterConst.StrategyAmmoRich)
	elif var_59_2 <= ChapterConst.AmmoPoor:
		table.insert(var_59_0, ChapterConst.StrategyAmmoPoor)

	local var_59_3 = underscore.filter(arg_59_1.getStrategies(), function(arg_60_0)
		local var_60_0 = pg.strategy_data_template[arg_60_0.id]

		return var_60_0 and var_60_0.type == ChapterConst.StgTypeBindFleetPassive and arg_60_0.count > 0)

	table.insertto(var_59_0, underscore.map(var_59_3, function(arg_61_0)
		return arg_61_0.id))
	table.insertto(var_59_0, arg_59_1.stgIds)

	local var_59_4 = arg_59_0.getConfig("chapter_strategy")

	for iter_59_0, iter_59_1 in ipairs(var_59_4):
		table.insert(var_59_0, iter_59_1)

	if OPEN_AIR_DOMINANCE and arg_59_0.getConfig("air_dominance") > 0:
		table.insert(var_59_0, arg_59_0.getAirDominanceStg())

	for iter_59_2, iter_59_3 in ipairs(arg_59_0.getExtraFlags()):
		table.insert(var_59_0, ChapterConst.Status2Stg[iter_59_3])

	local var_59_5 = arg_59_0.getOperationBuffDescStg()

	if var_59_5:
		table.insert(var_59_0, var_59_5)

	underscore.each(arg_59_0.buff_list, function(arg_62_0)
		if ChapterConst.Buff2Stg[arg_62_0]:
			table.insert(var_59_0, ChapterConst.Buff2Stg[arg_62_0]))

	if arg_59_0.getPlayType() == ChapterConst.TypeDOALink:
		local var_59_6 = arg_59_0.GetBuffOfLinkAct()

		if var_59_6:
			local var_59_7 = pg.gameset.doa_fever_buff.description

			table.insert(var_59_0, pg.gameset.doa_fever_strategy.description[table.indexof(var_59_7, var_59_6)])

	return var_59_0

def var_0_0.GetShowingStrategies(arg_63_0):
	local var_63_0 = arg_63_0.fleet
	local var_63_1 = arg_63_0.getFleetStates(var_63_0)

	return (_.filter(var_63_1, function(arg_64_0)
		local var_64_0 = pg.strategy_data_template[arg_64_0]

		return var_64_0 and var_64_0.icon != ""))

def var_0_0.getAirDominanceStg(arg_65_0):
	local var_65_0, var_65_1 = arg_65_0.getAirDominanceValue()

	return ChapterConst.AirDominance[var_65_1].StgId

def var_0_0.getAirDominanceValue(arg_66_0):
	local var_66_0 = 0
	local var_66_1 = 0

	for iter_66_0, iter_66_1 in pairs(arg_66_0.fleets):
		if iter_66_1.isValid() and (iter_66_1.getFleetType() == FleetType.Normal or iter_66_1.getFleetType() == FleetType.Submarine):
			var_66_0 = var_66_0 + iter_66_1.getFleetAirDominanceValue()
			var_66_1 = var_66_1 + iter_66_1.getAntiAircraftSums()

	return var_66_0, calcAirDominanceStatus(var_66_0, arg_66_0.getConfig("air_dominance"), var_66_1), arg_66_0.airDominanceStatus

def var_0_0.setAirDominanceStatus(arg_67_0, arg_67_1):
	arg_67_0.airDominanceStatus = arg_67_1

def var_0_0.updateExtraFlags(arg_68_0, arg_68_1, arg_68_2):
	local var_68_0 = False

	for iter_68_0, iter_68_1 in ipairs(arg_68_2):
		for iter_68_2, iter_68_3 in ipairs(arg_68_0.extraFlagList):
			if iter_68_3 == iter_68_1:
				table.remove(arg_68_0.extraFlagList, iter_68_2)

				var_68_0 = True

				break

	for iter_68_4, iter_68_5 in ipairs(arg_68_1):
		if not table.contains(arg_68_0.extraFlagList, iter_68_5):
			table.insert(arg_68_0.extraFlagList, 1, iter_68_5)

			var_68_0 = True

	return var_68_0

def var_0_0.getExtraFlags(arg_69_0):
	local var_69_0 = arg_69_0.extraFlagList

	if #var_69_0 == 0:
		var_69_0 = ChapterConst.StatusDefaultList

	return var_69_0

def var_0_0.UpdateBuffList(arg_70_0, arg_70_1):
	if not arg_70_1:
		return

	for iter_70_0, iter_70_1 in ipairs(arg_70_1):
		if not _.include(arg_70_0.buff_list, iter_70_1):
			table.insert(arg_70_0.buff_list, iter_70_1)

def var_0_0.getFleetBattleBuffs(arg_71_0, arg_71_1):
	local var_71_0 = table.shallowCopy(arg_71_0.buff_list)

	_.each(arg_71_0.getFleetStates(arg_71_1), function(arg_72_0)
		local var_72_0 = pg.strategy_data_template[arg_72_0]
		local var_72_1 = var_72_0.buff_id

		if var_72_1 == 0:
			return

		if var_72_0.buff_type == ChapterConst.StrategyBuffTypeOnlyBoss:
			local var_72_2 = arg_71_0.GetEnemy(arg_71_1.line.row, arg_71_1.line.column)

			if var_72_2 and not ChapterConst.IsBossCell(var_72_2):
				return

		table.insert(var_71_0, var_72_1))
	table.insertto(var_71_0, arg_71_0.GetCellEventByKey("attach_buff", arg_71_1.line.row, arg_71_1.line.column) or {})
	_.each(arg_71_0.GetWeather(), function(arg_73_0)
		local var_73_0 = pg.weather_data_template[arg_73_0].effect_args

		if type(var_73_0) == "table" and var_73_0.buff and var_73_0.buff > 0:
			table.insert(var_71_0, var_73_0.buff))

	local var_71_1 = arg_71_0.buildBattleBuffList(arg_71_1)

	return var_71_0, var_71_1

def var_0_0.GetStageFlags(arg_74_0):
	local var_74_0 = arg_74_0.fleet.line.row
	local var_74_1 = arg_74_0.fleet.line.column

	return arg_74_0.GetCellEventByKey("stage_flags", var_74_0, var_74_1) or {}

def var_0_0.GetCellEventByKey(arg_75_0, arg_75_1, arg_75_2, arg_75_3):
	arg_75_2 = arg_75_2 or arg_75_0.fleet.line.row
	arg_75_3 = arg_75_3 or arg_75_0.fleet.line.column

	local var_75_0 = ChapterCell.Line2Name(arg_75_2, arg_75_3)
	local var_75_1 = arg_75_0.cells[var_75_0]

	if not var_75_1:
		return

	return var_0_0.GetEventTemplateByKey(arg_75_1, var_75_1.attachmentId)

def var_0_0.GetEventTemplateByKey(arg_76_0, arg_76_1):
	local var_76_0 = pg.map_event_template[arg_76_1]

	if not var_76_0:
		return

	local var_76_1

	for iter_76_0, iter_76_1 in ipairs(var_76_0.effect):
		if iter_76_1[1] == arg_76_0:
			for iter_76_2 = 2, #iter_76_1:
				var_76_1 = var_76_1 or {}

				table.insert(var_76_1, iter_76_1[iter_76_2])

	return var_76_1

def var_0_0.buildBattleBuffList(arg_77_0, arg_77_1):
	local var_77_0 = {}
	local var_77_1, var_77_2 = arg_77_0.triggerSkill(arg_77_1, FleetSkill.TypeBattleBuff)

	if var_77_1 and #var_77_1 > 0:
		local var_77_3 = {}

		for iter_77_0, iter_77_1 in ipairs(var_77_1):
			local var_77_4 = var_77_2[iter_77_0]
			local var_77_5 = arg_77_1.findCommanderBySkillId(var_77_4.id)

			var_77_3[var_77_5] = var_77_3[var_77_5] or {}

			table.insert(var_77_3[var_77_5], iter_77_1)

		for iter_77_2, iter_77_3 in pairs(var_77_3):
			table.insert(var_77_0, {
				iter_77_2,
				iter_77_3
			})

	local var_77_6 = arg_77_1.getCommanders()

	for iter_77_4, iter_77_5 in pairs(var_77_6):
		local var_77_7 = iter_77_5.getTalents()

		for iter_77_6, iter_77_7 in ipairs(var_77_7):
			local var_77_8 = iter_77_7.getBuffsAddition()

			if #var_77_8 > 0:
				local var_77_9

				for iter_77_8, iter_77_9 in ipairs(var_77_0):
					if iter_77_9[1] == iter_77_5:
						var_77_9 = iter_77_9[2]

						break

				if not var_77_9:
					var_77_9 = {}

					table.insert(var_77_0, {
						iter_77_5,
						var_77_9
					})

				for iter_77_10, iter_77_11 in ipairs(var_77_8):
					table.insert(var_77_9, iter_77_11)

	return var_77_0

def var_0_0.updateFleetShipHp(arg_78_0, arg_78_1, arg_78_2):
	for iter_78_0, iter_78_1 in ipairs(arg_78_0.fleets):
		iter_78_1.updateShipHp(arg_78_1, arg_78_2)

		if iter_78_1.id != arg_78_0.fleet.id:
			iter_78_1.clearShipHpChange()

def var_0_0.getDragExtend(arg_79_0):
	local var_79_0 = arg_79_0.theme
	local var_79_1 = 99999999
	local var_79_2 = 99999999
	local var_79_3 = 0
	local var_79_4 = 0

	for iter_79_0, iter_79_1 in pairs(arg_79_0.cells):
		if var_79_1 > iter_79_1.row:
			var_79_1 = iter_79_1.row

		if var_79_3 < iter_79_1.row:
			var_79_3 = iter_79_1.row

		if var_79_2 > iter_79_1.column:
			var_79_2 = iter_79_1.column

		if var_79_4 < iter_79_1.column:
			var_79_4 = iter_79_1.column

	local var_79_5 = (var_79_4 + var_79_2) * 0.5
	local var_79_6 = (var_79_3 + var_79_1) * 0.5
	local var_79_7 = var_79_0.cellSize + var_79_0.cellSpace
	local var_79_8 = math.max((var_79_4 - var_79_5 + 1) * var_79_7.x, 0)
	local var_79_9 = math.max((var_79_5 - var_79_2 + 1) * var_79_7.x, 0)
	local var_79_10 = math.max((var_79_6 - var_79_1 + 1) * var_79_7.y, 0)
	local var_79_11 = math.max((var_79_3 - var_79_6 + 1) * var_79_7.y, 0)

	return var_79_9, var_79_8, var_79_10, var_79_11

def var_0_0.getPoisonArea(arg_80_0, arg_80_1):
	local var_80_0 = {}
	local var_80_1 = arg_80_0.theme.cellSize + arg_80_0.theme.cellSpace

	for iter_80_0, iter_80_1 in pairs(arg_80_0.cells):
		if iter_80_1.checkHadFlag(ChapterConst.FlagPoison):
			local var_80_2 = math.floor((iter_80_1.column - arg_80_0.indexMin.y) * var_80_1.x * arg_80_1)
			local var_80_3 = math.ceil((iter_80_1.column - arg_80_0.indexMin.y + 1) * var_80_1.x * arg_80_1)
			local var_80_4 = math.floor((iter_80_1.row - arg_80_0.indexMin.x) * var_80_1.y * arg_80_1)
			local var_80_5 = math.ceil((iter_80_1.row - arg_80_0.indexMin.x + 1) * var_80_1.y * arg_80_1)
			local var_80_6 = var_80_3 - var_80_2
			local var_80_7 = var_80_5 - var_80_4

			var_80_0[iter_80_0] = {
				x = var_80_2,
				y = var_80_4,
				w = var_80_6,
				h = var_80_7
			}

	return var_80_0

def var_0_0.selectFleets(arg_81_0, arg_81_1):
	local var_81_0 = Clone(arg_81_1) or {}
	local var_81_1 = getProxy(FleetProxy).GetRegularFleets()

	for iter_81_0 = #var_81_0, 1, -1:
		local var_81_2 = var_81_1[var_81_0[iter_81_0]]

		if not var_81_2 or not var_81_2.isUnlock() or var_81_2.isLegalToFight() != True:
			table.remove(var_81_0, iter_81_0)

	local var_81_3 = {
		[FleetType.Normal] = _.filter(var_81_0, function(arg_82_0)
			return var_81_1[arg_82_0].getFleetType() == FleetType.Normal),
		[FleetType.Submarine] = _.filter(var_81_0, function(arg_83_0)
			return var_81_1[arg_83_0].getFleetType() == FleetType.Submarine)
	}
	local var_81_4 = arg_81_0.getConfig("group_num")
	local var_81_5 = arg_81_0.getConfig("submarine_num")

	for iter_81_1 = #var_81_3[FleetType.Normal], var_81_4 + 1, -1:
		table.remove(var_81_3[FleetType.Normal], iter_81_1)

	for iter_81_2 = #var_81_3[FleetType.Submarine], var_81_5 + 1, -1:
		table.remove(var_81_3[FleetType.Submarine], iter_81_2)

	for iter_81_3, iter_81_4 in pairs(var_81_3):
		if #iter_81_4 == 0:
			local var_81_6 = 0

			if iter_81_3 == FleetType.Normal:
				var_81_6 = var_81_4
			elif iter_81_3 == FleetType.Submarine:
				var_81_6 = var_81_5

			for iter_81_5, iter_81_6 in pairs(var_81_1):
				if var_81_6 <= #iter_81_4:
					break

				if iter_81_6 and iter_81_6.getFleetType() == iter_81_3 and iter_81_6.isUnlock() and iter_81_6.isLegalToFight() == True:
					table.insert(iter_81_4, iter_81_5)

	local var_81_7 = {}

	for iter_81_7, iter_81_8 in ipairs(var_81_3):
		for iter_81_9, iter_81_10 in ipairs(iter_81_8):
			table.insert(var_81_7, iter_81_10)

	return var_81_7

def var_0_0.GetDefaultFleetIndex(arg_84_0):
	local var_84_0 = getProxy(ChapterProxy).GetLastFleetIndex()

	return arg_84_0.selectFleets(var_84_0)

def var_0_0.getMaxColumnByRow(arg_85_0, arg_85_1):
	local var_85_0 = -1

	for iter_85_0, iter_85_1 in pairs(arg_85_0.cells):
		if iter_85_1.row == arg_85_1:
			var_85_0 = math.max(var_85_0, iter_85_1.column)

	return var_85_0

def var_0_0.getFleet(arg_86_0, arg_86_1, arg_86_2, arg_86_3):
	return _.detect(arg_86_0.fleets, function(arg_87_0)
		return arg_87_0.line.row == arg_86_2 and arg_87_0.line.column == arg_86_3 and (not arg_86_1 or arg_87_0.getFleetType() == arg_86_1) and arg_87_0.isValid()) or _.detect(arg_86_0.fleets, function(arg_88_0)
		return arg_88_0.line.row == arg_86_2 and arg_88_0.line.column == arg_86_3 and (not arg_86_1 or arg_88_0.getFleetType() == arg_86_1))

def var_0_0.getFleetIndex(arg_89_0, arg_89_1, arg_89_2, arg_89_3):
	local var_89_0 = arg_89_0.getFleet(arg_89_1, arg_89_2, arg_89_3)

	if var_89_0:
		return table.indexof(arg_89_0.fleets, var_89_0)

def var_0_0.getOni(arg_90_0):
	return _.detect(arg_90_0.champions, function(arg_91_0)
		return arg_91_0.attachment == ChapterConst.AttachOni)

def var_0_0.getChampion(arg_92_0, arg_92_1, arg_92_2):
	return (_.detect(arg_92_0.champions, function(arg_93_0)
		return arg_93_0.row == arg_92_1 and arg_93_0.column == arg_92_2))

def var_0_0.getChampionIndex(arg_94_0, arg_94_1, arg_94_2):
	local var_94_0 = arg_94_0.getChampion(arg_94_1, arg_94_2)

	if not var_94_0:
		return

	return table.indexof(arg_94_0.champions, var_94_0)

def var_0_0.getChampionVisibility(arg_95_0, arg_95_1, arg_95_2, arg_95_3):
	assert(arg_95_1, "chapter champion not exist.")

	return arg_95_1.flag == ChapterConst.CellFlagActive

def var_0_0.mergeChampion(arg_96_0, arg_96_1, arg_96_2):
	local var_96_0 = arg_96_0.getChampionIndex(arg_96_1.row, arg_96_1.column)

	if var_96_0:
		arg_96_0.champions[var_96_0] = arg_96_1

		return True
	else
		if not arg_96_2:
			arg_96_1.trait = ChapterConst.TraitLurk

		table.insert(arg_96_0.champions, arg_96_1)

		return False

def var_0_0.RemoveChampion(arg_97_0, arg_97_1):
	local var_97_0 = table.indexof(arg_97_0.champions, arg_97_1)

	if var_97_0:
		table.remove(arg_97_0.champions, var_97_0)

def var_0_0.considerAsObstacle(arg_98_0, arg_98_1, arg_98_2, arg_98_3):
	local var_98_0 = arg_98_0.getChapterCell(arg_98_2, arg_98_3)

	if not var_98_0 or not var_98_0.IsWalkable():
		return True

	if arg_98_0.existBarrier(arg_98_2, arg_98_3):
		return True

	if arg_98_1 == ChapterConst.SubjectPlayer:
		if var_98_0.flag == ChapterConst.CellFlagActive:
			if ChapterConst.IsEnemyAttach(var_98_0.attachment):
				return True

			if var_98_0.attachment == ChapterConst.AttachBox:
				local var_98_1 = pg.box_data_template[var_98_0.attachmentId]

				assert(var_98_1, "box_data_template not exist. " .. var_98_0.attachmentId)

				if var_98_1.type == ChapterConst.BoxTorpedo:
					return True

			if var_98_0.attachment == ChapterConst.AttachStory:
				return True

		if arg_98_0.existVisibleChampion(arg_98_2, arg_98_3):
			return True
	elif arg_98_1 == ChapterConst.SubjectChampion and arg_98_0.existFleet(FleetType.Normal, arg_98_2, arg_98_3):
		return True

	return False

def var_0_0.considerAsStayPoint(arg_99_0, arg_99_1, arg_99_2, arg_99_3):
	local var_99_0 = arg_99_0.getChapterCell(arg_99_2, arg_99_3)

	if not var_99_0 or not var_99_0.IsWalkable():
		return False

	if arg_99_0.existBarrier(arg_99_2, arg_99_3):
		return False

	if arg_99_1 == ChapterConst.SubjectPlayer:
		if var_99_0.flag == ChapterConst.CellFlagActive and var_99_0.attachment == ChapterConst.AttachStory:
			return True

		if var_99_0.attachment == ChapterConst.AttachLandbase and pg.land_based_template[var_99_0.attachmentId] and pg.land_based_template[var_99_0.attachmentId].type == ChapterConst.LBHarbor:
			return False

		if arg_99_0.existFleet(FleetType.Normal, arg_99_2, arg_99_3):
			return False

		if arg_99_0.existOni(arg_99_2, arg_99_3):
			return False

		if arg_99_0.existBombEnemy(arg_99_2, arg_99_3):
			return False
	elif arg_99_1 == ChapterConst.SubjectChampion:
		if var_99_0.flag != ChapterConst.CellFlagDisabled and var_99_0.attachment != ChapterConst.AttachNone:
			return False

		local var_99_1 = arg_99_0.getChampion(arg_99_2, arg_99_3)

		if var_99_1 and var_99_1.flag != ChapterConst.CellFlagDisabled:
			return False

	return True

def var_0_0.existAny(arg_100_0, arg_100_1, arg_100_2):
	local var_100_0 = arg_100_0.getChapterCell(arg_100_1, arg_100_2)

	if var_100_0.attachment != ChapterConst.AttachNone and var_100_0.flag == ChapterConst.CellFlagActive:
		return True

	if arg_100_0.existFleet(None, arg_100_1, arg_100_2):
		return True

	local var_100_1 = arg_100_0.getChampion(arg_100_1, arg_100_2)

	if var_100_1 and var_100_1.flag != ChapterConst.CellFlagDisabled:
		return True

def var_0_0.existBarrier(arg_101_0, arg_101_1, arg_101_2):
	local var_101_0 = arg_101_0.getChapterCell(arg_101_1, arg_101_2)

	if var_101_0.attachment == ChapterConst.AttachBox and var_101_0.flag == ChapterConst.CellFlagActive and pg.box_data_template[var_101_0.attachmentId].type == ChapterConst.BoxBarrier:
		return True

	if var_101_0.attachment == ChapterConst.AttachStory and var_101_0.flag == ChapterConst.CellFlagTriggerActive and pg.map_event_template[var_101_0.attachmentId].type == ChapterConst.StoryObstacle:
		return True

	local var_101_1 = arg_101_0.getChampion(arg_101_1, arg_101_2)

	if var_101_1 and var_101_1.flag != ChapterConst.CellFlagDisabled:
		local var_101_2 = pg.expedition_data_template[var_101_1.attachmentId]

		if var_101_2 and var_101_2.type == ChapterConst.ExpeditionTypeUnTouchable:
			return True

	return False

def var_0_0.GetEnemy(arg_102_0, arg_102_1, arg_102_2):
	local var_102_0 = arg_102_0.getChapterCell(arg_102_1, arg_102_2)

	if var_102_0 and var_102_0.flag == ChapterConst.CellFlagActive and ChapterConst.IsEnemyAttach(var_102_0.attachment):
		return var_102_0

	local var_102_1 = arg_102_0.getChampion(arg_102_1, arg_102_2)

	if var_102_1 and var_102_1.flag != ChapterConst.CellFlagDisabled:
		return var_102_1

def var_0_0.existEnemy(arg_103_0, arg_103_1, arg_103_2, arg_103_3):
	if arg_103_1 == ChapterConst.SubjectPlayer:
		local var_103_0 = arg_103_0.GetEnemy(arg_103_2, arg_103_3)

		if var_103_0:
			local var_103_1

			if isa(var_103_0, ChapterCell):
				var_103_1 = var_103_0.attachment
			else
				var_103_1 = ChapterConst.AttachChampion

			return True, var_103_1
	elif arg_103_1 == ChapterConst.SubjectChampion and (arg_103_0.existFleet(FleetType.Normal, arg_103_2, arg_103_3) or arg_103_0.existFleet(FleetType.Transport, arg_103_2, arg_103_3)):
		return True

def var_0_0.existFleet(arg_104_0, arg_104_1, arg_104_2, arg_104_3):
	if _.any(arg_104_0.fleets, function(arg_105_0)
		return arg_105_0.line.row == arg_104_2 and arg_105_0.line.column == arg_104_3 and (not arg_104_1 or arg_105_0.getFleetType() == arg_104_1) and arg_105_0.isValid()):
		return True

def var_0_0.existVisibleChampion(arg_106_0, arg_106_1, arg_106_2):
	local var_106_0 = arg_106_0.getChampion(arg_106_1, arg_106_2)

	return var_106_0 and arg_106_0.getChampionVisibility(var_106_0)

def var_0_0.existAlly(arg_107_0, arg_107_1):
	return _.any(arg_107_0.fleets, function(arg_108_0)
		return arg_108_0.id != arg_107_1.id and arg_108_0.line.row == arg_107_1.line.row and arg_108_0.line.column == arg_107_1.line.column and arg_108_0.isValid())

def var_0_0.existOni(arg_109_0, arg_109_1, arg_109_2):
	return _.any(arg_109_0.champions, function(arg_110_0)
		return arg_110_0.attachment == ChapterConst.AttachOni and arg_110_0.flag == ChapterConst.CellFlagActive and (not arg_109_1 or arg_109_1 == arg_110_0.row) and (not arg_109_2 or arg_109_2 == arg_110_0.column))

def var_0_0.existBombEnemy(arg_111_0, arg_111_1, arg_111_2):
	if arg_111_1 and arg_111_2:
		local var_111_0 = arg_111_0.getChapterCell(arg_111_1, arg_111_2)

		return var_111_0.attachment == ChapterConst.AttachBomb_Enemy and var_111_0.flag == ChapterConst.CellFlagActive

	for iter_111_0, iter_111_1 in pairs(arg_111_0.cells):
		if iter_111_1.attachment == ChapterConst.AttachBomb_Enemy and iter_111_1.flag == ChapterConst.CellFlagActive and (not arg_111_1 or arg_111_1 == iter_111_1.row) and (not arg_111_2 or arg_111_2 == iter_111_1.column):
			return True

	return False

def var_0_0.isPlayingWithBombEnemy(arg_112_0):
	for iter_112_0, iter_112_1 in pairs(arg_112_0.cells):
		if iter_112_1.attachment == ChapterConst.AttachBomb_Enemy:
			return True

	return False

def var_0_0.existCoastalGunNoMatterLiveOrDead(arg_113_0):
	for iter_113_0, iter_113_1 in pairs(arg_113_0.cells):
		if iter_113_1.attachment == ChapterConst.AttachLandbase:
			local var_113_0 = pg.land_based_template[iter_113_1.attachmentId]

			assert(var_113_0, "land_based_template not exist. " .. iter_113_1.attachmentId)

			if var_113_0.type == ChapterConst.LBCoastalGun:
				return True

	return False

local var_0_1 = {
	{
		1,
		0
	},
	{
		-1,
		0
	},
	{
		0,
		1
	},
	{
		0,
		-1
	}
}

def var_0_0.calcWalkableCells(arg_114_0, arg_114_1, arg_114_2, arg_114_3, arg_114_4):
	local var_114_0 = {}

	for iter_114_0 = 0, ChapterConst.MaxRow - 1:
		if not var_114_0[iter_114_0]:
			var_114_0[iter_114_0] = {}

		for iter_114_1 = 0, ChapterConst.MaxColumn - 1:
			local var_114_1 = ChapterCell.Line2Name(iter_114_0, iter_114_1)
			local var_114_2 = arg_114_0.cells[var_114_1]

			var_114_0[iter_114_0][iter_114_1] = var_114_2 and var_114_2.IsWalkable()

	local var_114_3 = {}

	if arg_114_1 == ChapterConst.SubjectPlayer:
		local var_114_4 = arg_114_0.getCoastalGunArea()

		for iter_114_2, iter_114_3 in ipairs(var_114_4):
			var_114_3[iter_114_3.row .. "_" .. iter_114_3.column] = True

	local var_114_5 = {}
	local var_114_6 = arg_114_0.GetRawChapterCell(arg_114_2, arg_114_3)

	if not var_114_6:
		return var_114_5

	local var_114_7 = {
		{
			step = 0,
			row = arg_114_2,
			column = arg_114_3,
			forbiddens = var_114_6.forbiddenDirections
		}
	}
	local var_114_8 = {}

	while #var_114_7 > 0:
		local var_114_9 = table.remove(var_114_7, 1)

		table.insert(var_114_8, var_114_9)
		_.each(var_0_1, function(arg_115_0)
			local var_115_0 = {
				row = var_114_9.row + arg_115_0[1],
				column = var_114_9.column + arg_115_0[2],
				step = var_114_9.step + 1
			}
			local var_115_1 = arg_114_0.GetRawChapterCell(var_115_0.row, var_115_0.column)

			if not var_115_1:
				return

			var_115_0.forbiddens = var_115_1.forbiddenDirections

			if var_115_0.step <= arg_114_4 and not OrientedPathFinding.IsDirectionForbidden(var_114_9, arg_115_0[1], arg_115_0[2]) and not (_.any(var_114_7, function(arg_116_0)
				return arg_116_0.row == var_115_0.row and arg_116_0.column == var_115_0.column) or _.any(var_114_8, function(arg_117_0)
				return arg_117_0.row == var_115_0.row and arg_117_0.column == var_115_0.column)) and var_114_0[var_115_0.row][var_115_0.column]:
				table.insert(var_114_5, var_115_0)

				if not arg_114_0.existEnemy(arg_114_1, var_115_0.row, var_115_0.column) and not arg_114_0.existBarrier(var_115_0.row, var_115_0.column) and not var_114_3[var_115_0.row .. "_" .. var_115_0.column]:
					table.insert(var_114_7, var_115_0))

	var_114_5 = _.filter(var_114_5, function(arg_118_0)
		return arg_118_0.row == arg_114_2 and arg_118_0.column == arg_114_3 or arg_114_0.considerAsStayPoint(arg_114_1, arg_118_0.row, arg_118_0.column))

	return var_114_5

def var_0_0.calcAreaCells(arg_119_0, arg_119_1, arg_119_2, arg_119_3, arg_119_4):
	local var_119_0 = {}

	for iter_119_0 = 0, ChapterConst.MaxRow - 1:
		if not var_119_0[iter_119_0]:
			var_119_0[iter_119_0] = {}

		for iter_119_1 = 0, ChapterConst.MaxColumn - 1:
			local var_119_1 = ChapterCell.Line2Name(iter_119_0, iter_119_1)
			local var_119_2 = arg_119_0.cells[var_119_1]

			var_119_0[iter_119_0][iter_119_1] = var_119_2 and var_119_2.IsWalkable()

	local var_119_3 = {}
	local var_119_4 = {
		{
			step = 0,
			row = arg_119_1,
			column = arg_119_2
		}
	}
	local var_119_5 = {}

	while #var_119_4 > 0:
		local var_119_6 = table.remove(var_119_4, 1)

		table.insert(var_119_5, var_119_6)
		_.each(var_0_1, function(arg_120_0)
			local var_120_0 = {
				row = var_119_6.row + arg_120_0[1],
				column = var_119_6.column + arg_120_0[2],
				step = var_119_6.step + 1
			}

			if var_120_0.row >= 0 and var_120_0.row < ChapterConst.MaxRow and var_120_0.column >= 0 and var_120_0.column < ChapterConst.MaxColumn and var_120_0.step <= arg_119_4 and not (_.any(var_119_4, function(arg_121_0)
				return arg_121_0.row == var_120_0.row and arg_121_0.column == var_120_0.column) or _.any(var_119_5, function(arg_122_0)
				return arg_122_0.row == var_120_0.row and arg_122_0.column == var_120_0.column)):
				table.insert(var_119_4, var_120_0)

				if var_119_0[var_120_0.row][var_120_0.column] and var_120_0.step >= arg_119_3:
					table.insert(var_119_3, var_120_0))

	return var_119_3

def var_0_0.calcSquareBarrierCells(arg_123_0, arg_123_1, arg_123_2, arg_123_3):
	local var_123_0 = {}

	for iter_123_0 = -arg_123_3, arg_123_3:
		for iter_123_1 = -arg_123_3, arg_123_3:
			local var_123_1 = arg_123_1 + iter_123_0
			local var_123_2 = arg_123_2 + iter_123_1
			local var_123_3 = arg_123_0.getChapterCell(var_123_1, var_123_2)

			if var_123_3 and var_123_3.IsWalkable() and (arg_123_0.existBarrier(var_123_1, var_123_2) or not arg_123_0.existAny(var_123_1, var_123_2)):
				table.insert(var_123_0, {
					row = var_123_1,
					column = var_123_2
				})

	return var_123_0

def var_0_0.checkAnyInteractive(arg_124_0):
	local var_124_0 = arg_124_0.fleet.line
	local var_124_1 = arg_124_0.getChapterCell(var_124_0.row, var_124_0.column)
	local var_124_2 = False

	if arg_124_0.fleet.getFleetType() == FleetType.Normal:
		if arg_124_0.existEnemy(ChapterConst.SubjectPlayer, var_124_1.row, var_124_1.column):
			if arg_124_0.getRound() == ChapterConst.RoundPlayer:
				var_124_2 = True
		elif var_124_1.attachment == ChapterConst.AttachAmbush or var_124_1.attachment == ChapterConst.AttachBox:
			if var_124_1.flag != ChapterConst.CellFlagDisabled:
				var_124_2 = True
		elif var_124_1.attachment == ChapterConst.AttachStory:
			var_124_2 = var_124_1.flag == ChapterConst.CellFlagActive
		elif var_124_1.attachment == ChapterConst.AttachSupply and var_124_1.attachmentId > 0:
			local var_124_3, var_124_4 = arg_124_0.getFleetAmmo(arg_124_0.fleet)

			if var_124_4 < var_124_3:
				var_124_2 = True
		elif var_124_1.attachment == ChapterConst.AttachBox and var_124_1.flag != ChapterConst.CellFlagDisabled:
			var_124_2 = True

	return var_124_2

def var_0_0.getQuadCellPic(arg_125_0, arg_125_1):
	local var_125_0

	if arg_125_1.trait == ChapterConst.TraitLurk:
		-- block empty
	elif arg_125_1.flag == ChapterConst.CellFlagActive and ChapterConst.IsEnemyAttach(arg_125_1.attachment) and arg_125_1.flag == ChapterConst.CellFlagActive:
		var_125_0 = "cell_enemy"
	elif arg_125_1.attachment == ChapterConst.AttachBox and arg_125_1.flag == ChapterConst.CellFlagActive:
		local var_125_1 = pg.box_data_template[arg_125_1.attachmentId]

		assert(var_125_1, "box_data_template not exist. " .. arg_125_1.attachmentId)

		if var_125_1.type == ChapterConst.BoxDrop or var_125_1.type == ChapterConst.BoxStrategy or var_125_1.type == ChapterConst.BoxSupply or var_125_1.type == ChapterConst.BoxEnemy:
			var_125_0 = "cell_box"
		elif var_125_1.type == ChapterConst.BoxTorpedo:
			var_125_0 = "cell_enemy"
		elif var_125_1.type == ChapterConst.BoxBarrier:
			var_125_0 = "cell_green"
	elif arg_125_1.attachment == ChapterConst.AttachStory:
		if arg_125_1.flag == ChapterConst.CellFlagTriggerActive:
			local var_125_2 = pg.map_event_template[arg_125_1.attachmentId].grid_color

			var_125_0 = var_125_2 and #var_125_2 > 0 and var_125_2 or None
	elif arg_125_1.attachment == ChapterConst.AttachSupply and arg_125_1.attachmentId > 0:
		var_125_0 = "cell_box"
	elif arg_125_1.attachment == ChapterConst.AttachTransport_Target:
		var_125_0 = "cell_box"
	elif arg_125_1.attachment == ChapterConst.AttachLandbase:
		local var_125_3 = pg.land_based_template[arg_125_1.attachmentId]

		if var_125_3 and (var_125_3.type == ChapterConst.LBHarbor or var_125_3.type == ChapterConst.LBDock):
			var_125_0 = "cell_box"

	return var_125_0

def var_0_0.getMapShip(arg_126_0, arg_126_1):
	local var_126_0

	if arg_126_1.isValid():
		var_126_0 = _.detect(arg_126_1.getShips(False), function(arg_127_0)
			return arg_127_0.isNpc and arg_127_0.hpRant > 0)

		if not var_126_0:
			local var_126_1 = arg_126_1.getFleetType()

			if var_126_1 == FleetType.Normal:
				var_126_0 = arg_126_1.getShipsByTeam(TeamType.Main, False)[1]
			elif var_126_1 == FleetType.Submarine:
				var_126_0 = arg_126_1.getShipsByTeam(TeamType.Submarine, False)[1]

	return var_126_0

def var_0_0.getStrikeAnimShip(arg_128_0, arg_128_1, arg_128_2):
	return underscore.detect(arg_128_1.getShips(False), function(arg_129_0)
		return arg_129_0.GetMapStrikeAnim() == arg_128_2)

def var_0_0.GetSubmarineFleet(arg_130_0):
	return table.Find(arg_130_0.fleets, function(arg_131_0, arg_131_1)
		return arg_131_1.getFleetType() == FleetType.Submarine and arg_131_1.isValid())

def var_0_0.getStageCell(arg_132_0, arg_132_1, arg_132_2):
	local var_132_0 = arg_132_0.getChampion(arg_132_1, arg_132_2)

	if var_132_0 and var_132_0.flag != ChapterConst.CellFlagDisabled:
		return var_132_0

	local var_132_1 = arg_132_0.getChapterCell(arg_132_1, arg_132_2)

	if var_132_1 and var_132_1.flag != ChapterConst.CellFlagDisabled:
		return var_132_1

def var_0_0.getStageId(arg_133_0, arg_133_1, arg_133_2):
	local var_133_0 = arg_133_0.getChampion(arg_133_1, arg_133_2)

	if var_133_0 and var_133_0.flag != ChapterConst.CellFlagDisabled:
		return var_133_0.id

	local var_133_1 = arg_133_0.getChapterCell(arg_133_1, arg_133_2)

	if var_133_1 and var_133_1.flag != ChapterConst.CellFlagDisabled:
		return var_133_1.attachmentId

def var_0_0.getStageExtraAwards(arg_134_0):
	return

def var_0_0.GetExtraCostRate(arg_135_0):
	local var_135_0 = 1
	local var_135_1 = {}

	for iter_135_0, iter_135_1 in ipairs(arg_135_0.operationBuffList):
		local var_135_2 = pg.benefit_buff_template[iter_135_1]

		var_135_1[#var_135_1 + 1] = var_135_2

		if var_135_2.benefit_type == var_0_0.OPERATION_BUFF_TYPE_COST:
			var_135_0 = var_135_0 + var_135_2.benefit_effect * 0.01

	return math.max(1, var_135_0), var_135_1

def var_0_0.getFleetCost(arg_136_0, arg_136_1, arg_136_2):
	if arg_136_0.getPlayType() == ChapterConst.TypeExtra:
		return {
			gold = 0,
			oil = 0
		}, {
			gold = 0,
			oil = 0
		}

	local var_136_0, var_136_1 = arg_136_1.getCost()
	local var_136_2 = arg_136_0.GetLimitOilCost(arg_136_1.getFleetType() == FleetType.Submarine, arg_136_2)

	var_136_1.oil = math.clamp(var_136_2 - var_136_0.oil, 0, var_136_1.oil)

	local var_136_3 = arg_136_0.GetExtraCostRate()

	for iter_136_0, iter_136_1 in ipairs({
		var_136_0,
		var_136_1
	}):
		for iter_136_2, iter_136_3 in pairs(iter_136_1):
			iter_136_1[iter_136_2] = iter_136_1[iter_136_2] * var_136_3

	return var_136_0, var_136_1

def var_0_0.isOverFleetCost(arg_137_0, arg_137_1, arg_137_2):
	local var_137_0 = arg_137_0.GetLimitOilCost(arg_137_1.getFleetType() == FleetType.Submarine, arg_137_2)
	local var_137_1 = 0

	for iter_137_0, iter_137_1 in ipairs({
		arg_137_1.getCost()
	}):
		var_137_1 = var_137_1 + iter_137_1.oil

	local var_137_2 = arg_137_0.GetExtraCostRate()

	return var_137_0 < var_137_1, var_137_0 * var_137_2, var_137_1 * var_137_2

def var_0_0.writeBack(arg_138_0, arg_138_1, arg_138_2):
	local var_138_0 = arg_138_0.fleet

	local function var_138_1(arg_139_0)
		local var_139_0 = arg_138_2.statistics[arg_139_0.id]

		if not var_139_0:
			return

		arg_139_0.hpRant = var_139_0.bp

	for iter_138_0, iter_138_1 in pairs(var_138_0.ships):
		var_138_1(iter_138_1)

	var_138_0.ResortShips()

	if not arg_138_2.skipAmmo:
		var_138_0.restAmmo = math.max(var_138_0.restAmmo - 1, 0)

	local var_138_2 = _.filter(var_138_0.getStrategies(), function(arg_140_0)
		local var_140_0 = pg.strategy_data_template[arg_140_0.id]

		return var_140_0 and var_140_0.type == ChapterConst.StgTypeBindFleetPassive and arg_140_0.count > 0)

	_.each(var_138_2, function(arg_141_0)
		var_138_0.consumeOneStrategy(arg_141_0.id))

	if arg_138_2.statistics.submarineAid:
		local var_138_3 = arg_138_0.GetSubmarineFleet()

		if var_138_3 and not var_138_3.inHuntingRange(var_138_0.line.row, var_138_0.line.column):
			var_138_3.consumeOneStrategy(ChapterConst.StrategyCallSubOutofRange)

		if var_138_3:
			for iter_138_2, iter_138_3 in pairs(var_138_3.ships):
				var_138_1(iter_138_3)

			var_138_3.restAmmo = math.max(var_138_3.restAmmo - 1, 0)

	arg_138_0.UpdateComboHistory(arg_138_2.statistics._battleScore)

	if arg_138_1:
		local var_138_4
		local var_138_5
		local var_138_6 = arg_138_0.getChampion(var_138_0.line.row, var_138_0.line.column)

		if var_138_6:
			var_138_6.Iter()

			var_138_4 = var_138_6.attachment
			var_138_5 = var_138_6.attachmentId

			if var_138_6.flag == ChapterConst.CellFlagDisabled:
				arg_138_0.RemoveChampion(var_138_6)
		else
			local var_138_7 = arg_138_0.getChapterCell(var_138_0.line.row, var_138_0.line.column)

			var_138_4 = var_138_7.attachment
			var_138_5 = var_138_7.attachmentId

			if var_138_4 == ChapterConst.AttachEnemy or var_138_4 == ChapterConst.AttachBoss:
				var_138_7.flag = ChapterConst.CellFlagDisabled

				arg_138_0.updateChapterCell(var_138_7)
			else
				arg_138_0.clearChapterCell(var_138_7.row, var_138_7.column)

		assert(var_138_4, "attachment can not be None.")

		if var_138_4 == ChapterConst.AttachEnemy or var_138_4 == ChapterConst.AttachElite or var_138_4 == ChapterConst.AttachChampion:
			if not var_138_6 or var_138_6.flag == ChapterConst.CellFlagDisabled:
				local var_138_8 = _.detect(arg_138_0.achieves, function(arg_142_0)
					return arg_142_0.type == ChapterConst.AchieveType2)

				if var_138_8:
					var_138_8.count = var_138_8.count + 1
		elif var_138_4 == ChapterConst.AttachBoss:
			local var_138_9 = _.detect(arg_138_0.achieves, function(arg_143_0)
				return arg_143_0.type == ChapterConst.AchieveType1)

			if var_138_9:
				var_138_9.count = var_138_9.count + 1

		if arg_138_0.CheckChapterWin():
			pg.TrackerMgr.GetInstance().Tracking(TRACKING_KILL_BOSS)

		if var_138_6 and var_138_6.flag == ChapterConst.CellFlagDisabled or not var_138_6 and var_138_4 != ChapterConst.AttachBox:
			var_138_0.defeatEnemies = var_138_0.defeatEnemies + 1
			arg_138_0.defeatEnemies = arg_138_0.defeatEnemies + 1

			local var_138_10 = pg.expedition_data_template[var_138_5]

			if not arg_138_0.isLoop() and var_138_10 and var_138_10.type == ChapterConst.ExpeditionTypeMulBoss:
				local var_138_11 = pg.chapter_model_multistageboss[arg_138_0.id].guild_buff
				local var_138_12 = var_138_0.GetStatusStrategy()

				_.each(var_138_11, function(arg_144_0)
					if not table.contains(var_138_12, arg_144_0):
						table.insert(var_138_12, arg_144_0))

				local var_138_13 = arg_138_0.getNextValidIndex()

				if var_138_13 > 0:
					var_138_12 = arg_138_0.fleets[var_138_13].GetStatusStrategy()

					_.each(var_138_11, function(arg_145_0)
						table.removebyvalue(var_138_12, arg_145_0))

			getProxy(ChapterProxy).RecordLastDefeatedEnemy(arg_138_0.id, {
				score = arg_138_2.statistics._battleScore,
				line = {
					row = var_138_0.line.row,
					column = var_138_0.line.column
				},
				attachment = var_138_4,
				attachmentId = var_138_5
			})

def var_0_0.CleanCurrentEnemy(arg_146_0):
	local var_146_0 = arg_146_0.fleet.line
	local var_146_1
	local var_146_2 = arg_146_0.getChampion(var_146_0.row, var_146_0.column)

	if var_146_2:
		var_146_2.Iter()

		if var_146_2.flag == ChapterConst.CellFlagDisabled:
			arg_146_0.RemoveChampion(var_146_2)

		return

	if arg_146_0.getChapterCell(var_146_0.row, var_146_0.column).attachment == ChapterConst.AttachEnemy:
		arg_146_0.clearChapterCell(var_146_0.row, var_146_0.column)

		return

def var_0_0.UpdateProgressAfterSkipBattle(arg_147_0):
	arg_147_0.writeBack(True, {
		skipAmmo = True,
		statistics = {
			_battleScore = ys.Battle.BattleConst.BattleScore.S
		}
	})

def var_0_0.UpdateProgressOnRetreat(arg_148_0):
	_.each(arg_148_0.achieves, function(arg_149_0)
		if arg_149_0.type == ChapterConst.AchieveType3:
			if _.all(_.values(arg_148_0.cells), function(arg_150_0)
				if arg_150_0.attachment == ChapterConst.AttachEnemy or arg_150_0.attachment == ChapterConst.AttachElite or arg_150_0.attachment == ChapterConst.AttachBox and pg.box_data_template[arg_150_0.attachmentId].type == ChapterConst.BoxEnemy:
					return arg_150_0.flag == ChapterConst.CellFlagDisabled

				return True) and _.all(arg_148_0.champions, function(arg_151_0)
				return arg_151_0.flag == ChapterConst.CellFlagDisabled):
				arg_149_0.count = arg_149_0.count + 1
		elif arg_149_0.type == ChapterConst.AchieveType4:
			if arg_148_0.orignalShipCount <= arg_149_0.config:
				arg_149_0.count = arg_149_0.count + 1
		elif arg_149_0.type == ChapterConst.AchieveType5:
			if not _.any(arg_148_0.getShips(), function(arg_152_0)
				return arg_152_0.getShipType() == arg_149_0.config):
				arg_149_0.count = arg_149_0.count + 1
		elif arg_149_0.type == ChapterConst.AchieveType6:
			local var_149_0 = (arg_148_0.scoreHistory[0] or 0) + (arg_148_0.scoreHistory[1] or 0)

			arg_149_0.count = math.max(var_149_0 <= 0 and arg_148_0.combo or 0, arg_149_0.count or 0))

	if arg_148_0.progress == 100:
		arg_148_0.passCount = arg_148_0.passCount + 1

	local var_148_0 = arg_148_0.progress
	local var_148_1 = math.min(arg_148_0.progress + arg_148_0.getConfig("progress_boss"), 100)

	arg_148_0.progress = var_148_1

	if var_148_0 < 100 and var_148_1 >= 100:
		getProxy(ChapterProxy).RecordJustClearChapters(arg_148_0.id, True)

	arg_148_0.defeatCount = arg_148_0.defeatCount + 1

	local var_148_2 = getProxy(ChapterProxy).getMapById(arg_148_0.getConfig("map")).getMapType()

	if var_148_2 == Map.ELITE:
		pg.TrackerMgr.GetInstance().Tracking(TRACKING_HARD_CHAPTER, arg_148_0.id)
	elif var_148_2 == Map.SCENARIO:
		if arg_148_0.progress == 100 and arg_148_0.passCount == 0:
			pg.TrackerMgr.GetInstance().Tracking(TRACKING_HIGHEST_CHAPTER, arg_148_0.id)

		if arg_148_0.defeatCount == 1:
			if arg_148_0.id == 304:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_3_4)
			elif arg_148_0.id == 404:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_4_4)
			elif arg_148_0.id == 504:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_5_4)
			elif arg_148_0.id == 604:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_6_4)
			elif arg_148_0.id == 1204:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_12_4)
			elif arg_148_0.id == 1301:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_13_1)
			elif arg_148_0.id == 1302:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_13_2)
			elif arg_148_0.id == 1303:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_13_3)
			elif arg_148_0.id == 1304:
				pg.TrackerMgr.GetInstance().Tracking(TRACKING_FIRST_PASS_13_4)

def var_0_0.UpdateComboHistory(arg_153_0, arg_153_1):
	getProxy(ChapterProxy).RecordComboHistory(arg_153_0.id, {
		scoreHistory = Clone(arg_153_0.scoreHistory),
		combo = Clone(arg_153_0.combo)
	})

	arg_153_0.scoreHistory = arg_153_0.scoreHistory or {}
	arg_153_0.scoreHistory[arg_153_1] = (arg_153_0.scoreHistory[arg_153_1] or 0) + 1

	if arg_153_1 <= ys.Battle.BattleConst.BattleScore.C:
		arg_153_0.combo = 0
	else
		arg_153_0.combo = (arg_153_0.combo or 0) + 1

def var_0_0.GetWinConditions(arg_154_0):
	return arg_154_0.winConditions

def var_0_0.GetLoseConditions(arg_155_0):
	return arg_155_0.loseConditions

def var_0_0.CheckChapterWin(arg_156_0):
	local var_156_0 = arg_156_0.GetWinConditions()
	local var_156_1 = False
	local var_156_2 = ChapterConst.ReasonVictory

	for iter_156_0, iter_156_1 in pairs(var_156_0):
		if iter_156_1.type == 1:
			local var_156_3 = arg_156_0.findChapterCells(ChapterConst.AttachBoss)
			local var_156_4 = 0

			_.each(var_156_3, function(arg_157_0)
				if arg_157_0 and arg_157_0.flag == ChapterConst.CellFlagDisabled:
					var_156_4 = var_156_4 + 1)

			var_156_1 = var_156_1 or var_156_4 >= iter_156_1.param
		elif iter_156_1.type == 2:
			var_156_1 = var_156_1 or arg_156_0.GetDefeatCount() >= iter_156_1.param
		elif iter_156_1.type == 3:
			local var_156_5 = arg_156_0.CheckTransportState()

			var_156_1 = var_156_1 or var_156_5 == 1
		elif iter_156_1.type == 4:
			var_156_1 = var_156_1 or arg_156_0.getRoundNum() > iter_156_1.param
		elif iter_156_1.type == 5:
			local var_156_6 = iter_156_1.param
			local var_156_7 = _.any(arg_156_0.champions, function(arg_158_0)
				local var_158_0 = arg_158_0.attachmentId == var_156_6

				for iter_158_0, iter_158_1 in pairs(arg_158_0.idList):
					var_158_0 = var_158_0 or iter_158_1 == var_156_6

				return var_158_0 and arg_158_0.flag != ChapterConst.CellFlagDisabled) or _.any(arg_156_0.cells, function(arg_159_0)
				return arg_159_0.attachmentId == var_156_6 and arg_159_0.flag != ChapterConst.CellFlagDisabled)

			var_156_1 = var_156_1 or not var_156_7
		elif iter_156_1.type == 6:
			local var_156_8 = iter_156_1.param
			local var_156_9 = _.any(arg_156_0.fleets, function(arg_160_0)
				return arg_160_0.getFleetType() == FleetType.Normal and arg_160_0.isValid() and arg_160_0.line.row == var_156_8[1] and arg_160_0.line.column == var_156_8[2])

			var_156_1 = var_156_1 or var_156_9

		if var_156_1:
			break

	return var_156_1, var_156_2

def var_0_0.CheckChapterLose(arg_161_0):
	local var_161_0 = arg_161_0.GetLoseConditions()
	local var_161_1 = False
	local var_161_2 = ChapterConst.ReasonDefeat

	for iter_161_0, iter_161_1 in pairs(var_161_0):
		if iter_161_1.type == 1:
			local var_161_3 = _.any(arg_161_0.fleets, function(arg_162_0)
				return arg_162_0.getFleetType() == FleetType.Normal and arg_162_0.isValid())

			var_161_1 = var_161_1 or not var_161_3
		elif iter_161_1.type == 2:
			var_161_1 = var_161_1 or arg_161_0.BaseHP <= 0
			var_161_2 = var_161_1 and ChapterConst.ReasonDefeatDefense or var_161_2

		if var_161_1:
			break

	if arg_161_0.getPlayType() == ChapterConst.TypeTransport:
		local var_161_4 = arg_161_0.CheckTransportState()

		var_161_1 = var_161_1 or var_161_4 == -1

	return var_161_1, var_161_2

def var_0_0.CheckChapterWillWin(arg_163_0):
	if arg_163_0.existOni() or arg_163_0.isPlayingWithBombEnemy():
		return True

	if arg_163_0.CheckChapterWin():
		return True

def var_0_0.triggerSkill(arg_164_0, arg_164_1, arg_164_2):
	local var_164_0 = _.filter(arg_164_1.findSkills(arg_164_2), function(arg_165_0)
		local var_165_0 = arg_165_0.GetTriggers()

		return _.any(var_165_0, function(arg_166_0)
			return arg_166_0[1] == FleetSkill.TriggerInSubTeam and arg_166_0[2] == 1) == (arg_164_1.getFleetType() == FleetType.Submarine) and _.all(arg_165_0.GetTriggers(), function(arg_167_0)
			return arg_164_0.triggerCheck(arg_164_1, arg_165_0, arg_167_0)))

	return _.reduce(var_164_0, None, function(arg_168_0, arg_168_1)
		local var_168_0 = arg_168_1.GetType()
		local var_168_1 = arg_168_1.GetArgs()

		if var_168_0 == FleetSkill.TypeMoveSpeed or var_168_0 == FleetSkill.TypeHuntingLv or var_168_0 == FleetSkill.TypeTorpedoPowerUp:
			return (arg_168_0 or 0) + var_168_1[1]
		elif var_168_0 == FleetSkill.TypeAmbushDodge or var_168_0 == FleetSkill.TypeAirStrikeDodge:
			return math.max(arg_168_0 or 0, var_168_1[1])
		elif var_168_0 == FleetSkill.TypeAttack or var_168_0 == FleetSkill.TypeStrategy:
			arg_168_0 = arg_168_0 or {}

			table.insert(arg_168_0, var_168_1)

			return arg_168_0
		elif var_168_0 == FleetSkill.TypeBattleBuff:
			arg_168_0 = arg_168_0 or {}

			table.insert(arg_168_0, var_168_1[1])

			return arg_168_0), var_164_0

def var_0_0.triggerCheck(arg_169_0, arg_169_1, arg_169_2, arg_169_3):
	local var_169_0 = arg_169_3[1]

	if var_169_0 == FleetSkill.TriggerDDHead:
		local var_169_1 = arg_169_1.getShipsByTeam(TeamType.Vanguard, False)

		return #var_169_1 > 0 and ShipType.IsTypeQuZhu(var_169_1[1].getShipType())
	elif var_169_0 == FleetSkill.TriggerVanCount:
		local var_169_2 = arg_169_1.getShipsByTeam(TeamType.Vanguard, False)

		return #var_169_2 >= arg_169_3[2] and #var_169_2 <= arg_169_3[3]
	elif var_169_0 == FleetSkill.TriggerShipCount:
		local var_169_3 = _.filter(arg_169_1.getShips(False), function(arg_170_0)
			return table.contains(arg_169_3[2], arg_170_0.getShipType()))

		return #var_169_3 >= arg_169_3[3] and #var_169_3 <= arg_169_3[4]
	elif var_169_0 == FleetSkill.TriggerAroundEnemy:
		local var_169_4 = {
			row = arg_169_1.line.row,
			column = arg_169_1.line.column
		}

		return _.any(_.values(arg_169_0.cells), function(arg_171_0)
			local var_171_0 = arg_169_0.GetEnemy(arg_171_0.row, arg_171_0.column)

			if not var_171_0:
				return

			local var_171_1 = pg.expedition_data_template[var_171_0.attachmentId]

			if not var_171_1:
				return

			local var_171_2 = var_171_1.type

			return ManhattonDist(var_169_4, {
				row = arg_171_0.row,
				column = arg_171_0.column
			}) <= arg_169_3[2] and (type(arg_169_3[3]) == "number" and arg_169_3[3] == var_171_2 or type(arg_169_3[3]) == "table" and table.contains(arg_169_3[3], var_171_2)))
	elif var_169_0 == FleetSkill.TriggerNekoPos:
		local var_169_5 = arg_169_1.findCommanderBySkillId(arg_169_2.id)

		for iter_169_0, iter_169_1 in pairs(arg_169_1.getCommanders()):
			if var_169_5.id == iter_169_1.id and iter_169_0 == arg_169_3[2]:
				return True
	elif var_169_0 == FleetSkill.TriggerAroundLand:
		local var_169_6 = {
			row = arg_169_1.line.row,
			column = arg_169_1.line.column
		}

		return _.any(_.values(arg_169_0.cells), function(arg_172_0)
			return not arg_172_0.IsWalkable() and ManhattonDist(var_169_6, {
				row = arg_172_0.row,
				column = arg_172_0.column
			}) <= arg_169_3[2])
	elif var_169_0 == FleetSkill.TriggerAroundCombatAlly:
		local var_169_7 = {
			row = arg_169_1.line.row,
			column = arg_169_1.line.column
		}

		return _.any(arg_169_0.fleets, function(arg_173_0)
			return arg_169_1.id != arg_173_0.id and arg_173_0.getFleetType() == FleetType.Normal and arg_169_0.existEnemy(ChapterConst.SubjectPlayer, arg_173_0.line.row, arg_173_0.line.column) and ManhattonDist(var_169_7, {
				row = arg_173_0.line.row,
				column = arg_173_0.line.column
			}) <= arg_169_3[2])
	elif var_169_0 == FleetSkill.TriggerInSubTeam:
		return True
	else
		assert(False, "invalid trigger type. " .. var_169_0)

local var_0_2 = {
	{
		1,
		0
	},
	{
		-1,
		0
	},
	{
		0,
		1
	},
	{
		0,
		-1
	}
}

def var_0_0.checkOniState(arg_174_0):
	local var_174_0 = arg_174_0.getOni()

	assert(var_174_0, "oni not exist.")

	if _.all(var_0_2, function(arg_175_0)
		local var_175_0 = {
			var_174_0.row + arg_175_0[1],
			var_174_0.column + arg_175_0[2]
		}

		if arg_174_0.existFleet(FleetType.Normal, var_175_0[1], var_175_0[2]):
			return True

		local var_175_1 = arg_174_0.getChapterCell(var_175_0[1], var_175_0[2])

		if not var_175_1 or not var_175_1.IsWalkable():
			return True

		if arg_174_0.existBarrier(var_175_1.row, var_175_1.column):
			return True):
		return 1

	local var_174_1 = arg_174_0.getOniChapterInfo().escape_grids

	if _.any(var_174_1, function(arg_176_0)
		return arg_176_0[1] == var_174_0.row and arg_176_0[2] == var_174_0.column):
		return 2

def var_0_0.onOniEnter(arg_177_0):
	for iter_177_0, iter_177_1 in pairs(arg_177_0.cells):
		iter_177_1.attachment = ChapterConst.AttachNone
		iter_177_1.attachmentId = None
		iter_177_1.flag = None
		iter_177_1.data = None

	arg_177_0.champions = {}
	arg_177_0.modelCount = arg_177_0.getOniChapterInfo().special_item
	arg_177_0.roundIndex = 0

def var_0_0.onBombEnemyEnter(arg_178_0):
	for iter_178_0, iter_178_1 in pairs(arg_178_0.cells):
		iter_178_1.attachment = ChapterConst.AttachNone
		iter_178_1.attachmentId = None
		iter_178_1.flag = None
		iter_178_1.data = None

	arg_178_0.champions = {}
	arg_178_0.modelCount = 0
	arg_178_0.roundIndex = 0

def var_0_0.clearSubmarineFleet(arg_179_0):
	for iter_179_0 = #arg_179_0.fleets, 1, -1:
		if arg_179_0.fleets[iter_179_0].getFleetType() == FleetType.Submarine:
			table.remove(arg_179_0.fleets, iter_179_0)

def var_0_0.getSpAppearStory(arg_180_0):
	if arg_180_0.existOni():
		for iter_180_0, iter_180_1 in ipairs(arg_180_0.champions):
			if iter_180_1.trait == ChapterConst.TraitLurk and iter_180_1.attachment == ChapterConst.AttachOni:
				local var_180_0 = iter_180_1.getConfig("appear_story")

				if var_180_0 and #var_180_0 > 0:
					return var_180_0
	elif arg_180_0.isPlayingWithBombEnemy():
		for iter_180_2, iter_180_3 in pairs(arg_180_0.cells):
			if iter_180_3.attachment == ChapterConst.AttachBomb_Enemy and iter_180_3.trait == ChapterConst.TraitLurk:
				local var_180_1 = pg.specialunit_template[iter_180_3.attachmentId]

				if var_180_1.appear_story and #var_180_1.appear_story > 0:
					return var_180_1.appear_story

def var_0_0.getSpAppearGuide(arg_181_0):
	if arg_181_0.existOni():
		for iter_181_0, iter_181_1 in ipairs(arg_181_0.champions):
			if iter_181_1.trait == ChapterConst.TraitLurk and iter_181_1.attachment == ChapterConst.AttachOni:
				local var_181_0 = iter_181_1.getConfig("appear_guide")

				if var_181_0 and #var_181_0 > 0:
					return var_181_0
	elif arg_181_0.isPlayingWithBombEnemy():
		for iter_181_2, iter_181_3 in pairs(arg_181_0.cells):
			if iter_181_3.attachment == ChapterConst.AttachBomb_Enemy and iter_181_3.trait == ChapterConst.TraitLurk:
				local var_181_1 = pg.specialunit_template[iter_181_3.attachmentId]

				if var_181_1.appear_guide and #var_181_1.appear_guide > 0:
					return var_181_1.appear_guide

def var_0_0.CheckTransportState(arg_182_0):
	local var_182_0 = _.detect(arg_182_0.fleets, function(arg_183_0)
		return arg_183_0.getFleetType() == FleetType.Transport)

	if not var_182_0:
		return -1

	local var_182_1 = arg_182_0.findChapterCell(ChapterConst.AttachTransport_Target)

	assert(var_182_0, "transport fleet not exist.")
	assert(var_182_1, "transport target not exist.")

	if not var_182_0.isValid():
		return -1
	elif var_182_0.line.row == var_182_1.row and var_182_0.line.column == var_182_1.column and not arg_182_0.existEnemy(ChapterConst.SubjectPlayer, var_182_1.row, var_182_1.column):
		return 1
	else
		return 0

def var_0_0.getCoastalGunArea(arg_184_0):
	local var_184_0 = {}

	for iter_184_0, iter_184_1 in pairs(arg_184_0.cells):
		if iter_184_1.attachment == ChapterConst.AttachLandbase and iter_184_1.flag != ChapterConst.CellFlagDisabled:
			local var_184_1 = pg.land_based_template[iter_184_1.attachmentId]

			if var_184_1.type == ChapterConst.LBCoastalGun:
				local var_184_2 = var_184_1.function_args
				local var_184_3 = {
					math.abs(var_184_2[1]),
					math.abs(var_184_2[2])
				}
				local var_184_4 = {
					Mathf.Sign(var_184_2[1]),
					Mathf.Sign(var_184_2[2])
				}
				local var_184_5 = math.max(var_184_3[1], var_184_3[2])

				for iter_184_2 = 1, var_184_5:
					table.insert(var_184_0, {
						row = iter_184_1.row + math.min(var_184_3[1], iter_184_2) * var_184_4[1],
						column = iter_184_1.column + math.min(var_184_3[2], iter_184_2) * var_184_4[2]
					})

	return var_184_0

def var_0_0.GetAntiAirGunArea(arg_185_0):
	local var_185_0 = {}
	local var_185_1 = {}

	for iter_185_0, iter_185_1 in pairs(arg_185_0.cells):
		if iter_185_1.attachment == ChapterConst.AttachLandbase and iter_185_1.flag != ChapterConst.CellFlagDisabled:
			local var_185_2 = pg.land_based_template[iter_185_1.attachmentId]

			if var_185_2.type == ChapterConst.LBAntiAir:
				local var_185_3 = var_185_2.function_args
				local var_185_4 = math.abs(var_185_3[1])

				local function var_185_5(arg_186_0, arg_186_1)
					return ChapterConst.MaxColumn * arg_186_0 + arg_186_1

				local var_185_6 = {}
				local var_185_7 = {}

				if var_185_4 > 0:
					var_185_6[var_185_5(iter_185_1.row, iter_185_1.column)] = iter_185_1

				while next(var_185_6):
					local var_185_8 = next(var_185_6)
					local var_185_9 = var_185_6[var_185_8]

					var_185_6[var_185_8] = None

					if var_185_4 >= math.abs(var_185_9.row - iter_185_1.row) and var_185_4 >= math.abs(var_185_9.column - iter_185_1.column):
						var_185_7[var_185_8] = var_185_9

						for iter_185_2 = 1, #var_0_2:
							local var_185_10 = var_185_9.row + var_0_2[iter_185_2][1]
							local var_185_11 = var_185_9.column + var_0_2[iter_185_2][2]
							local var_185_12 = var_185_5(var_185_10, var_185_11)

							if not var_185_7[var_185_12]:
								var_185_6[var_185_12] = {
									row = var_185_10,
									column = var_185_11
								}

				for iter_185_3, iter_185_4 in pairs(var_185_7):
					var_185_1[iter_185_3] = iter_185_4

	for iter_185_5, iter_185_6 in pairs(var_185_1):
		table.insert(var_185_0, iter_185_6)

	return var_185_0

def var_0_0.GetDefeatCount(arg_187_0):
	return arg_187_0.defeatEnemies

def var_0_0.ExistDivingChampion(arg_188_0):
	return _.any(arg_188_0.champions, function(arg_189_0)
		return arg_189_0.flag == ChapterConst.CellFlagDiving)

def var_0_0.IsSkipPrecombat(arg_190_0):
	return arg_190_0.isLoop() and getProxy(ChapterProxy).GetSkipPrecombat()

def var_0_0.CanActivateAutoFight(arg_191_0):
	local var_191_0 = pg.chapter_template_loop[arg_191_0.id]

	return var_191_0 and var_191_0.fightauto == 1 and arg_191_0.isLoop() and AutoBotCommand.autoBotSatisfied() and not arg_191_0.existOni() and not arg_191_0.existBombEnemy()

def var_0_0.IsAutoFight(arg_192_0):
	return arg_192_0.CanActivateAutoFight() and getProxy(ChapterProxy).GetChapterAutoFlag(arg_192_0.id) == 1

def var_0_0.getOperationBuffDescStg(arg_193_0):
	for iter_193_0, iter_193_1 in ipairs(arg_193_0.operationBuffList):
		if pg.benefit_buff_template[iter_193_1].benefit_type == Chapter.OPERATION_BUFF_TYPE_DESC:
			return iter_193_1

def var_0_0.GetOperationDesc(arg_194_0):
	local var_194_0 = ""

	for iter_194_0, iter_194_1 in ipairs(arg_194_0.operationBuffList):
		local var_194_1 = pg.benefit_buff_template[iter_194_1]

		if var_194_1.benefit_type == var_0_0.OPERATION_BUFF_TYPE_DESC:
			var_194_0 = var_194_1.desc

			break

	return var_194_0

def var_0_0.GetOperationBuffList(arg_195_0):
	return arg_195_0.operationBuffList

def var_0_0.GetAllEnemies(arg_196_0, arg_196_1):
	local var_196_0 = {}

	for iter_196_0, iter_196_1 in pairs(arg_196_0.cells):
		if ChapterConst.IsEnemyAttach(iter_196_1.attachment) and (arg_196_1 or iter_196_1.flag != ChapterConst.CellFlagDisabled):
			table.insert(var_196_0, iter_196_1)

	for iter_196_2, iter_196_3 in pairs(arg_196_0.champions):
		if arg_196_1 or iter_196_3.flag != ChapterConst.CellFlagDisabled:
			table.insert(var_196_0, iter_196_3)

	return var_196_0

def var_0_0.GetFleetofDuty(arg_197_0, arg_197_1):
	local var_197_0

	for iter_197_0, iter_197_1 in ipairs(arg_197_0.fleets):
		if iter_197_1.isValid() and iter_197_1.getFleetType() == FleetType.Normal:
			local var_197_1 = arg_197_0.duties[iter_197_1.id] or 0

			if var_197_1 == ChapterFleet.DUTY_KILLALL or arg_197_1 and var_197_1 == ChapterFleet.DUTY_KILLBOSS or not arg_197_1 and var_197_1 == ChapterFleet.DUTY_CLEANPATH:
				return iter_197_1

			var_197_0 = iter_197_1

	return var_197_0

def var_0_0.GetBuffOfLinkAct(arg_198_0):
	if arg_198_0.getPlayType() == ChapterConst.TypeDOALink:
		local var_198_0 = pg.gameset.doa_fever_buff.description

		return _.detect(arg_198_0.buff_list, function(arg_199_0)
			return table.contains(var_198_0, arg_199_0))

def var_0_0.GetAttachmentStories(arg_200_0):
	local var_200_0 = arg_200_0.cellAttachments
	local var_200_1 = 0
	local var_200_2

	for iter_200_0, iter_200_1 in pairs(var_200_0):
		local var_200_3 = var_0_0.GetEventTemplateByKey("mult_story", iter_200_1.attachmentId)

		if var_200_3:
			assert(not var_200_2 or table.equal(var_200_2, var_200_3[1]), "Not the same Config of Mult_story ID. " .. iter_200_1.attachmentId)

			var_200_2 = var_200_2 or var_200_3[1]

			local var_200_4 = arg_200_0.cells[iter_200_0]

			if var_200_4 and var_200_4.flag == ChapterConst.CellFlagDisabled:
				var_200_1 = var_200_1 + 1

	return var_200_2, var_200_1

def var_0_0.GetWeather(arg_201_0, arg_201_1, arg_201_2):
	arg_201_1 = arg_201_1 or arg_201_0.fleet.line.row
	arg_201_2 = arg_201_2 or arg_201_0.fleet.line.column

	local var_201_0 = ChapterCell.Line2Name(arg_201_1, arg_201_2)
	local var_201_1 = arg_201_0.cells[var_201_0]

	return var_201_1 and var_201_1.GetWeatherFlagList() or {}

def var_0_0.getDisplayEnemyCount(arg_202_0):
	local var_202_0 = 0

	local function var_202_1(arg_203_0)
		if arg_203_0.flag != ChapterConst.CellFlagDisabled:
			var_202_0 = var_202_0 + 1

	local var_202_2 = {
		[ChapterConst.AttachEnemy] = var_202_1,
		[ChapterConst.AttachElite] = var_202_1,
		[ChapterConst.AttachBox] = function(arg_204_0)
			if pg.box_data_template[arg_204_0.attachmentId].type == ChapterConst.BoxEnemy:
				var_202_1(arg_204_0)
	}

	for iter_202_0, iter_202_1 in pairs(arg_202_0.cells):
		switch(iter_202_1.attachment, var_202_2, None, iter_202_1)

	for iter_202_2, iter_202_3 in ipairs(arg_202_0.champions):
		var_202_1(iter_202_3)

	return var_202_0

def var_0_0.getNearestEnemyCell(arg_205_0):
	local function var_205_0(arg_206_0, arg_206_1)
		return (arg_206_0.row - arg_206_1.row) * (arg_206_0.row - arg_206_1.row) + (arg_206_0.column - arg_206_1.column) * (arg_206_0.column - arg_206_1.column)

	local var_205_1

	local function var_205_2(arg_207_0)
		if arg_207_0.flag != ChapterConst.CellFlagDisabled and (not var_205_1 or var_205_0(arg_205_0.fleet.line, arg_207_0) < var_205_0(arg_205_0.fleet.line, var_205_1)):
			var_205_1 = arg_207_0

	local var_205_3 = {
		[ChapterConst.AttachEnemy] = var_205_2,
		[ChapterConst.AttachElite] = var_205_2,
		[ChapterConst.AttachBox] = function(arg_208_0)
			if pg.box_data_template[arg_208_0.attachmentId].type == ChapterConst.BoxEnemy:
				var_205_2(arg_208_0)
	}

	for iter_205_0, iter_205_1 in pairs(arg_205_0.cells):
		switch(iter_205_1.attachment, var_205_3, None, iter_205_1)

	for iter_205_2, iter_205_3 in ipairs(arg_205_0.champions):
		var_205_2(iter_205_3)

	return var_205_1

def var_0_0.GetRegularFleetIds(arg_209_0):
	return (_.map(_.filter(arg_209_0.fleets, function(arg_210_0)
		local var_210_0 = arg_210_0.getFleetType()

		return var_210_0 == FleetType.Normal or var_210_0 == FleetType.Submarine), function(arg_211_0)
		return arg_211_0.fleetId))

return var_0_0
