local var_0_0 = class("WorldProxy", import(".NetProxy"))

def var_0_0.register(arg_1_0):
	WPool = BaseEntityPool.New()
	WBank = BaseEntityBank.New()

	arg_1_0.BuildTestFunc()
	arg_1_0.on(33114, function(arg_2_0)
		arg_1_0.isProtoLock = arg_2_0.is_world_open == 0

		arg_1_0.BuildWorld(World.TypeBase)

		arg_1_0.world.baseShipIds = underscore.rest(arg_2_0.ship_id_list, 1)
		arg_1_0.world.baseCmdIds = underscore.rest(arg_2_0.cmd_id_list, 1)

		arg_1_0.world.UpdateProgress(arg_2_0.progress)
		pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inWorld")
		arg_1_0.sendNotification(GAME.WORLD_GET_BOSS))
	arg_1_0.on(33105, function(arg_3_0)
		local var_3_0 = arg_1_0.world.GetActiveMap()

		assert(var_3_0, "active map not exist.")

		local var_3_1 = arg_1_0.NetBuildMapAttachmentCells(arg_3_0.pos_list)

		arg_1_0.UpdateMapAttachmentCells(var_3_0.id, var_3_1)

		local var_3_2 = arg_1_0.NetBuildFleetAttachUpdate(arg_3_0.pos_list)

		arg_1_0.ApplyFleetAttachUpdate(var_3_0.id, var_3_2)
		WPool.ReturnArray(var_3_2))
	arg_1_0.on(33203, function(arg_4_0)
		local var_4_0 = arg_1_0.world.GetTaskProxy()

		for iter_4_0, iter_4_1 in ipairs(arg_4_0.update_list):
			local var_4_1 = WorldTask.New(iter_4_1)

			if var_4_0.getTaskById(var_4_1.id):
				var_4_0.updateTask(var_4_1)
			else
				var_4_0.addTask(var_4_1)
				arg_1_0.sendNotification(GAME.WORLD_TRIGGER_TASK_DONE, {
					task = var_4_1
				}))
	arg_1_0.on(33204, function(arg_5_0)
		local var_5_0 = arg_1_0.world.GetTaskProxy()

		for iter_5_0, iter_5_1 in ipairs(arg_5_0.delete_list):
			var_5_0.deleteTask(iter_5_1))
	arg_1_0.on(33601, function(arg_6_0)
		arg_1_0.NetUpdateAchievements(arg_6_0.target_list))
	arg_1_0.on(34507, function(arg_7_0)
		if arg_1_0.world:
			local var_7_0 = arg_1_0.world.GetBossProxy()
			local var_7_1 = WorldBoss.New()

			var_7_1.Setup(arg_7_0.boss_info, Player.New(arg_7_0.user_info))
			var_7_1.UpdateBossType(arg_7_0.type)
			var_7_1.SetJoinTime(pg.TimeMgr.GetInstance().GetServerTime())

			if var_7_0.isSetup:
				var_7_0.ClearRank(var_7_1.id)
				var_7_0.UpdateCacheBoss(var_7_1)

			if not var_7_0.IsSelfBoss(var_7_1) and arg_1_0.world.IsSystemOpen(WorldConst.SystemWorldBoss):
				pg.WorldBossTipMgr.GetInstance().Show(var_7_1))
	arg_1_0.on(34508, function(arg_8_0)
		local var_8_0 = arg_1_0.world.GetBossProxy()

		if var_8_0.isSetup:
			arg_1_0.sendNotification(GAME.WORLD_GET_BOSS_RANK, {
				bossId = arg_8_0.boss_id,
				def callback:()
					var_8_0.updateBossHp(arg_8_0.boss_id, arg_8_0.hp)
			}))

def var_0_0.remove(arg_10_0):
	if arg_10_0.world:
		arg_10_0.world.GetBossProxy().Dispose()

	removeWorld()
	WPool.Dispose()

	WPool = None

	WBank.Dispose()

	WBank = None

def var_0_0.BuildTestFunc(arg_11_0):
	world_skip_battle = PlayerPrefs.GetInt("world_skip_battle") or 0

	function switch_world_skip_battle()
		if getProxy(PlayerProxy).getRawData().CheckIdentityFlag():
			world_skip_battle = 1 - world_skip_battle

			PlayerPrefs.SetInt("world_skip_battle", world_skip_battle)
			PlayerPrefs.Save()
			pg.TipsMgr.GetInstance().ShowTips(world_skip_battle == 1 and "已开启大世界战斗跳略" or "已关闭大世界战斗跳略")

	if IsUnityEditor:
		function display_world_debug_panel()
			local var_13_0 = pg.m02.retrieveMediator(WorldMediator.__cname)

			if var_13_0:
				var_13_0.viewComponent.ShowSubView("DebugPanel")

		pg.UIMgr.GetInstance().AddWorldTestButton("WorldDebug", function()
			WorldConst.Debug = True)

def var_0_0.BuildWorld(arg_15_0, arg_15_1, arg_15_2):
	arg_15_0.world = World.New(arg_15_1, arg_15_0.world and arg_15_0.world.Dispose(tobool(arg_15_2)))

	pg.ShipFlagMgr.GetInstance().UpdateFlagShips("inWorld")

def var_0_0.NetFullUpdate(arg_16_0, arg_16_1):
	arg_16_0.isProtoLock = arg_16_1.is_world_open == 0

	arg_16_0.NetUpdateWorld(arg_16_1.world, arg_16_1.global_flag_list, arg_16_1.camp)
	arg_16_0.NetUpdateWorldDefaultFleets(arg_16_1.fleet_list)
	arg_16_0.NetUpdateWorldAchievements(arg_16_1.target_list, arg_16_1.target_fetch_list)
	arg_16_0.NetUpdateWorldCountInfo(arg_16_1.count_info)
	arg_16_0.NetUpdateWorldMapPressing(arg_16_1.clean_chapter)
	arg_16_0.NetUpdateWorldPressingAward(arg_16_1.chapter_award)
	arg_16_0.NetUpdateWorldShopGoods(arg_16_1.out_shop_buy_list)
	arg_16_0.NetUpdateWorldPortShopMark(arg_16_1.port_list, arg_16_1.new_flag_port_list)

def var_0_0.NetUpdateWorld(arg_17_0, arg_17_1, arg_17_2, arg_17_3):
	local var_17_0 = arg_17_0.world

	var_17_0.SetRealm(arg_17_3)

	var_17_0.activateTime = arg_17_1.time
	var_17_0.expiredTime = arg_17_1.last_change_group_timestamp
	var_17_0.roundIndex = arg_17_1.round
	var_17_0.submarineSupport = arg_17_1.submarine_state == 1

	var_17_0.staminaMgr.Setup({
		arg_17_1.action_power,
		arg_17_1.action_power_extra,
		arg_17_1.last_recover_timestamp,
		arg_17_1.action_power_fetch_count
	})

	var_17_0.gobalFlag = underscore.map(arg_17_2, function(arg_18_0)
		return arg_18_0 > 0)

	local var_17_1 = var_17_0.GetAtlas()

	var_17_1.SetCostMapList(_.rest(arg_17_1.chapter_list, 1))
	var_17_1.SetSairenEntranceList(_.rest(arg_17_1.sairen_chapter, 1))
	var_17_1.InitWorldNShopGoods(arg_17_1.goods_list)
	var_17_0.SetFleets(arg_17_0.NetBuildMapFleetList(arg_17_1.group_list))

	local var_17_2 = arg_17_1.map_id > 0 and _.detect(arg_17_1.chapter_list, function(arg_19_0)
		return arg_19_0.random_id == arg_17_1.map_id)

	assert(arg_17_1.map_id > 0 == tobool(var_17_2), "error active map info." .. arg_17_1.map_id)

	if var_17_2:
		local var_17_3 = arg_17_1.enter_map_id
		local var_17_4 = var_17_2.random_id
		local var_17_5 = var_17_2.template_id
		local var_17_6 = var_17_0.GetEntrance(var_17_3)
		local var_17_7 = var_17_0.GetMap(var_17_4)

		assert(var_17_6, "entrance not exist. " .. var_17_3)
		assert(var_17_7, "map not exist. " .. var_17_4)
		assert(pg.world_chapter_template[var_17_5], "world_chapter_template not exist. " .. var_17_5)
		assert(#arg_17_1.group_list > 0, "amount of group_list is not enough.")
		var_17_6.UpdateActive(True)
		var_17_7.UpdateGridId(var_17_5)

		local var_17_8 = arg_17_1.group_list[1].id

		var_17_7.findex = table.indexof(var_17_0.fleets, var_17_0.GetFleet(var_17_8))

		var_17_7.BindFleets(var_17_0.fleets)
		var_17_7.UpdateActive(True)

	var_17_0.GetInventoryProxy().Setup(arg_17_1.item_list)

	local var_17_9 = var_17_0.GetTaskProxy()

	var_17_9.Setup(arg_17_1.task_list)

	var_17_9.taskFinishCount = arg_17_1.task_finish_count

	_.each(arg_17_1.cd_list, function(arg_20_0)
		var_17_0.cdTimeList[arg_20_0.id] = arg_20_0.time)
	_.each(arg_17_1.buff_list, function(arg_21_0)
		var_17_0.globalBuffDic[arg_21_0.id] = WorldBuff.New()

		var_17_0.globalBuffDic[arg_21_0.id].Setup({
			id = arg_21_0.id,
			floor = arg_21_0.stack
		}))
	underscore.each(arg_17_1.month_boss, function(arg_22_0)
		var_17_0.lowestHP[arg_22_0.key] = arg_22_0.value)

def var_0_0.NetUpdateWorldDefaultFleets(arg_23_0, arg_23_1):
	local var_23_0 = {}

	_.each(arg_23_1, function(arg_24_0)
		local var_24_0 = WorldBaseFleet.New()

		var_24_0.Setup(arg_24_0)
		table.insert(var_23_0, var_24_0))
	table.sort(var_23_0, function(arg_25_0, arg_25_1)
		return arg_25_0.id < arg_25_1.id)
	arg_23_0.world.SetDefaultFleets(var_23_0)

def var_0_0.NetUpdateWorldAchievements(arg_26_0, arg_26_1, arg_26_2):
	arg_26_0.world.achievements = {}

	arg_26_0.NetUpdateAchievements(arg_26_1)

	arg_26_0.world.achieveEntranceStar = {}

	_.each(arg_26_2, function(arg_27_0)
		for iter_27_0, iter_27_1 in ipairs(arg_27_0.star_list):
			arg_26_0.world.SetAchieveSuccess(arg_27_0.id, iter_27_1))

def var_0_0.NetUpdateWorldCountInfo(arg_28_0, arg_28_1):
	arg_28_0.world.stepCount = arg_28_1.step_count
	arg_28_0.world.treasureCount = arg_28_1.treasure_count
	arg_28_0.world.activateCount = arg_28_1.activate_count

	arg_28_0.world.GetCollectionProxy().Setup(arg_28_1.collection_list)
	arg_28_0.world.UpdateProgress(arg_28_1.task_progress)

def var_0_0.NetUpdateActiveMap(arg_29_0, arg_29_1, arg_29_2, arg_29_3):
	local var_29_0 = arg_29_0.world.GetActiveEntrance()
	local var_29_1 = arg_29_0.world.GetActiveMap()

	if var_29_1.NeedClear() and var_29_0.becomeSairen and var_29_0.GetSairenMapId() == var_29_1.id:
		arg_29_0.world.GetAtlas().RemoveSairenEntrance(var_29_0)

	local var_29_2 = arg_29_0.world.GetEntrance(arg_29_1)

	assert(var_29_2, "entrance not exist. " .. arg_29_1)

	if var_29_0.id != var_29_2.id:
		var_29_0.UpdateActive(False)
		var_29_2.UpdateActive(True)

	local var_29_3 = arg_29_0.world.GetMap(arg_29_2)

	assert(var_29_3, "map not exist. " .. arg_29_2)

	if var_29_1.id != var_29_3.id:
		var_29_1.UpdateActive(False)
		var_29_1.RemoveFleetsCarries()
		var_29_1.UnbindFleets()

		var_29_3.findex = var_29_1.findex
		var_29_1.findex = None

		var_29_3.UpdateGridId(arg_29_3)
		var_29_3.BindFleets(arg_29_0.world.fleets)
		var_29_3.UpdateActive(True)

	arg_29_0.world.OnSwitchMap()

def var_0_0.NetUpdateMap(arg_30_0, arg_30_1):
	local var_30_0 = arg_30_1.id.random_id
	local var_30_1 = arg_30_1.id.template_id

	assert(pg.world_chapter_random[var_30_0], "world_chapter_random not exist. " .. var_30_0)
	assert(pg.world_chapter_template[var_30_1], "world_chapter_template not exist. " .. var_30_1)

	local var_30_2 = {}

	_.each(arg_30_1.state_flag, function(arg_31_0)
		var_30_2[arg_31_0] = True)

	local var_30_3 = arg_30_0.world.GetMap(var_30_0)

	var_30_3.UpdateClearFlag(var_30_2[1])
	var_30_3.UpdateVisionFlag(var_30_2[2] or arg_30_0.world.IsMapVisioned(var_30_0))
	arg_30_0.NetUpdateMapDiscoveredCells(var_30_3.id, var_30_2[3], arg_30_1.cell_list)

	local var_30_4 = arg_30_0.NetBuildMapAttachmentCells(arg_30_1.pos_list)

	arg_30_0.UpdateMapAttachmentCells(var_30_3.id, var_30_4)

	local var_30_5 = arg_30_0.NetBuildFleetAttachUpdate(arg_30_1.pos_list)

	arg_30_0.ApplyFleetAttachUpdate(var_30_3.id, var_30_5)
	WPool.ReturnArray(var_30_5)

	local var_30_6 = arg_30_0.NetBulidTerrainUpdate(arg_30_1.land_list)

	arg_30_0.ApplyTerrainUpdate(var_30_3.id, var_30_6)
	WPool.ReturnArray(var_30_6)
	var_30_3.SetValid(True)

def var_0_0.NetUpdateMapDiscoveredCells(arg_32_0, arg_32_1, arg_32_2, arg_32_3):
	local var_32_0 = arg_32_0.world.GetMap(arg_32_1)

	assert(var_32_0, "map not exist. " .. arg_32_1)

	if arg_32_2:
		for iter_32_0, iter_32_1 in pairs(var_32_0.cells):
			iter_32_1.UpdateDiscovered(True)
	else
		_.each(arg_32_3, function(arg_33_0)
			local var_33_0 = var_32_0.GetCell(arg_33_0.pos.row, arg_33_0.pos.column)

			assert(var_33_0, "cell not exist. " .. arg_33_0.pos.row .. ", " .. arg_33_0.pos.column)
			var_33_0.UpdateDiscovered(True))

def var_0_0.NetUpdateMapPort(arg_34_0, arg_34_1, arg_34_2):
	local var_34_0 = arg_34_0.world.GetMap(arg_34_1)

	assert(var_34_0, "map not exist. " .. arg_34_1)

	local var_34_1 = var_34_0.GetPort(arg_34_2.port_id)

	assert(var_34_1, "port not exist. " .. arg_34_2.port_id)
	var_34_1.UpdateTaskIds(_.rest(arg_34_2.task_list, 1))
	var_34_1.UpdateGoods(_.map(arg_34_2.goods_list, function(arg_35_0)
		local var_35_0 = WPool.Get(WorldGoods)

		var_35_0.Setup(arg_35_0)

		return var_35_0))
	var_34_1.UpdateExpiredTime(arg_34_2.next_refresh_time)

def var_0_0.NetUpdateAchievements(arg_36_0, arg_36_1):
	_.each(arg_36_1, function(arg_37_0)
		local var_37_0 = arg_36_0.world.GetAchievement(arg_37_0.id)

		arg_36_0.world.DispatchEvent(World.EventAchieved, var_37_0.NetUpdate(arg_37_0.process_list)))

def var_0_0.NetBuildMapFleetList(arg_38_0, arg_38_1):
	local var_38_0 = {}

	if arg_38_1 and #arg_38_1 > 0:
		_.each(arg_38_1, function(arg_39_0)
			local var_39_0 = WorldMapFleet.New()

			var_39_0.Setup(arg_39_0)
			table.insert(var_38_0, var_39_0))
		table.sort(var_38_0, function(arg_40_0, arg_40_1)
			return arg_40_0.id < arg_40_1.id)

		local var_38_1 = {
			[FleetType.Normal] = 1,
			[FleetType.Submarine] = 1
		}

		_.each(var_38_0, function(arg_41_0)
			local var_41_0 = arg_41_0.GetFleetType()

			arg_41_0.index = var_38_1[var_41_0]
			var_38_1[var_41_0] = var_38_1[var_41_0] + 1)

	return var_38_0

def var_0_0.NetBuildPortShipList(arg_42_0, arg_42_1):
	return _.map(arg_42_1, function(arg_43_0)
		local var_43_0 = WPool.Get(WorldMapShip)

		var_43_0.Setup(arg_43_0)

		return var_43_0)

def var_0_0.NetResetWorld(arg_44_0):
	arg_44_0.sendNotification(GAME.SEND_CMD, {
		cmd = "world",
		arg1 = "reset"
	})
	arg_44_0.sendNotification(GAME.SEND_CMD, {
		cmd = "kick"
	})

def var_0_0.NetBuildMapAttachmentCells(arg_45_0, arg_45_1):
	local var_45_0 = {}

	_.each(arg_45_1, function(arg_46_0)
		var_45_0[WorldMapCell.GetName(arg_46_0.pos.row, arg_46_0.pos.column)] = {
			pos = {
				row = arg_46_0.pos.row,
				column = arg_46_0.pos.column
			},
			attachmentList = arg_46_0.item_list
		})

	for iter_45_0, iter_45_1 in pairs(var_45_0):
		local var_45_1 = {}

		_.each(iter_45_1.attachmentList, function(arg_47_0)
			local var_47_0 = WPool.Get(WorldMapAttachment)

			var_47_0.Setup(setmetatable({
				pos = iter_45_1.pos
			}, {
				__index = arg_47_0
			}))
			table.insert(var_45_1, var_47_0))

		iter_45_1.attachmentList = var_45_1

	return var_45_0

def var_0_0.UpdateMapAttachmentCells(arg_48_0, arg_48_1, arg_48_2):
	local var_48_0 = arg_48_0.world.GetMap(arg_48_1)

	assert(var_48_0, "map not exist. " .. arg_48_1)

	for iter_48_0, iter_48_1 in pairs(arg_48_2):
		local var_48_1 = var_48_0.GetCell(iter_48_1.pos.row, iter_48_1.pos.column)
		local var_48_2 = var_48_1.attachments

		for iter_48_2 = #var_48_2, 1, -1:
			local var_48_3 = var_48_2[iter_48_2]

			if not WorldMapAttachment.IsFakeType(var_48_2[iter_48_2].type) and not _.any(iter_48_1.attachmentList, function(arg_49_0)
				return var_48_3.type == arg_49_0.type and var_48_3.id == arg_49_0.id):
				var_48_1.RemoveAttachment(iter_48_2)

		_.each(iter_48_1.attachmentList, function(arg_50_0)
			if arg_50_0.type != WorldMapAttachment.TypeFleet:
				local var_50_0 = _.detect(var_48_1.attachments, function(arg_51_0)
					return arg_51_0.type == arg_50_0.type and arg_51_0.id == arg_50_0.id)

				if var_50_0:
					var_50_0.UpdateFlag(arg_50_0.flag)
					var_50_0.UpdateData(arg_50_0.data, arg_50_0.effects)
					var_48_0.AddPhaseDisplay(var_50_0.UpdateBuffList(arg_50_0.buffList))
				else
					var_48_1.AddAttachment(arg_50_0))

def var_0_0.NetBuildFleetAttachUpdate(arg_52_0, arg_52_1):
	local var_52_0 = {}

	_.each(arg_52_1, function(arg_53_0)
		local var_53_0 = {
			row = arg_53_0.pos.row,
			column = arg_53_0.pos.column
		}

		_.each(arg_53_0.item_list, function(arg_54_0)
			if arg_54_0.item_type == WorldMapAttachment.TypeFleet:
				local var_54_0 = WPool.Get(NetFleetAttachUpdate)

				var_54_0.Setup(setmetatable({
					pos = var_53_0
				}, {
					__index = arg_54_0
				}))
				table.insert(var_52_0, var_54_0)))

	return var_52_0

def var_0_0.ApplyFleetAttachUpdate(arg_55_0, arg_55_1, arg_55_2):
	local var_55_0 = arg_55_0.world.GetMap(arg_55_1)

	assert(var_55_0, "map not exist. " .. arg_55_1)
	_.each(arg_55_2, function(arg_56_0)
		var_55_0.UpdateFleetLocation(arg_56_0.id, arg_56_0.row, arg_56_0.column))

def var_0_0.NetBulidTerrainUpdate(arg_57_0, arg_57_1):
	return _.map(arg_57_1, function(arg_58_0)
		local var_58_0 = WPool.Get(NetTerrainUpdate)

		var_58_0.Setup(arg_58_0)

		return var_58_0)

def var_0_0.ApplyTerrainUpdate(arg_59_0, arg_59_1, arg_59_2):
	local var_59_0 = arg_59_0.world.GetMap(arg_59_1)

	assert(var_59_0, "map not exist. " .. arg_59_1)
	_.each(arg_59_2, function(arg_60_0)
		local var_60_0 = var_59_0.GetCell(arg_60_0.row, arg_60_0.column)
		local var_60_1 = var_59_0.FindFleet(var_60_0.row, var_60_0.column)

		if var_60_1:
			var_59_0.CheckFleetUpdateFOV(var_60_1, function()
				var_60_0.UpdateTerrain(arg_60_0.GetTerrain(), arg_60_0.terrainDir, arg_60_0.terrainStrong))
		else
			var_60_0.UpdateTerrain(arg_60_0.GetTerrain(), arg_60_0.terrainDir, arg_60_0.terrainStrong))

def var_0_0.NetBuildFleetUpdate(arg_62_0, arg_62_1):
	return _.map(arg_62_1, function(arg_63_0)
		local var_63_0 = WPool.Get(NetFleetUpdate)

		var_63_0.Setup(arg_63_0)

		return var_63_0)

def var_0_0.ApplyFleetUpdate(arg_64_0, arg_64_1, arg_64_2):
	local var_64_0 = arg_64_0.world.GetMap(arg_64_1)

	assert(var_64_0, "map not exist. " .. arg_64_1)
	_.each(arg_64_2, function(arg_65_0)
		local var_65_0 = var_64_0.GetFleet(arg_65_0.id)

		assert(var_65_0, "fleet not exist. " .. arg_65_0.id)
		var_64_0.CheckFleetUpdateFOV(var_65_0, function()
			var_65_0.UpdateBuffs(arg_65_0.buffs)))

def var_0_0.NetBuildShipUpdate(arg_67_0, arg_67_1):
	return _.map(arg_67_1, function(arg_68_0)
		local var_68_0 = WPool.Get(NetShipUpdate)

		var_68_0.Setup(arg_68_0)

		return var_68_0)

def var_0_0.ApplyShipUpdate(arg_69_0, arg_69_1):
	_.each(arg_69_1, function(arg_70_0)
		local var_70_0 = arg_69_0.world.GetShip(arg_70_0.id)

		assert(var_70_0, "ship not exist. " .. arg_70_0.id)
		var_70_0.UpdateHpRant(arg_70_0.hpRant))

def var_0_0.NetUpdateWorldSairenChapter(arg_71_0, arg_71_1):
	local var_71_0 = _.rest(arg_71_1, 1)

	arg_71_0.world.GetAtlas().SetSairenEntranceList(var_71_0)

def var_0_0.NetUpdateWorldMapPressing(arg_72_0, arg_72_1):
	local var_72_0 = _.rest(arg_72_1, 1)

	arg_72_0.world.GetAtlas().SetPressingMarkList(var_72_0)
	arg_72_0.world.GetAtlas().InitPortMarkNShopList()

def var_0_0.NetUpdateWorldShopGoods(arg_73_0, arg_73_1):
	arg_73_0.world.InitWorldShopGoods()
	arg_73_0.world.UpdateWorldShopGoods(arg_73_1)

def var_0_0.NetUpdateWorldPressingAward(arg_74_0, arg_74_1):
	local var_74_0 = arg_74_0.world.GetAtlas()

	_.each(arg_74_1, function(arg_75_0)
		local var_75_0 = arg_75_0.id
		local var_75_1 = {
			id = arg_75_0.award,
			flag = arg_75_0.flag == 1
		}

		arg_74_0.world.pressingAwardDic[var_75_0] = var_75_1

		if not var_75_1.flag:
			var_74_0.MarkMapTransport(var_75_0))

def var_0_0.NetUpdateWorldPortShopMark(arg_76_0, arg_76_1, arg_76_2):
	arg_76_0.world.GetAtlas().SetPortMarkList(arg_76_1, arg_76_2)

def var_0_0.NetBuildSalvageUpdate(arg_77_0, arg_77_1):
	return _.map(arg_77_1, function(arg_78_0)
		local var_78_0 = WPool.Get(NetSalvageUpdate)

		var_78_0.Setup(arg_78_0)

		return var_78_0)

def var_0_0.ApplySalvageUpdate(arg_79_0, arg_79_1):
	_.each(arg_79_1, function(arg_80_0)
		local var_80_0 = arg_79_0.world.GetFleet(arg_80_0.id)

		assert(var_80_0, "fleet not exit. " .. arg_80_0.id)
		var_80_0.UpdateCatSalvage(arg_80_0.step, arg_80_0.list, arg_80_0.mapId))

return var_0_0
