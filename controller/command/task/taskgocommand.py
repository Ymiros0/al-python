local var_0_0 = class("TaskGoCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().taskVO
	local var_1_1 = getProxy(ChapterProxy)
	local var_1_2 = var_1_0.getConfig("scene")

	if var_1_2 and #var_1_2 > 0:
		if var_1_2[1] == "ACTIVITY_MAP":
			local var_1_3 = {}

			if var_1_2[2]:
				table.insert(var_1_3, function(arg_2_0)
					local var_2_0 = getProxy(ActivityProxy)

					if underscore.any(var_1_2[2], function(arg_3_0)
						local var_3_0 = var_2_0.getActivityById(arg_3_0)

						return var_3_0 and not var_3_0.isEnd()):
						arg_2_0()
					else
						pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_notStartOrEnd")))

			table.insert(var_1_3, function(arg_4_0)
				local var_4_0, var_4_1 = var_1_1.getLastMapForActivity()

				if var_4_0 and var_1_1.getMapById(var_4_0).isUnlock():
					arg_4_0(var_4_0, var_4_1)
				else
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_notStartOrEnd")))
			seriesAsync(var_1_3, function(arg_5_0, arg_5_1)
				pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, {
					chapterId = arg_5_1,
					mapIdx = arg_5_0
				}))
		elif var_1_2[1] == "HARD_MAP":
			local var_1_4 = var_1_1.getUseableMaxEliteMap()

			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, {
				mapIdx = var_1_4 and var_1_4.id
			})
		elif SCENE[var_1_2[1]] == SCENE.LEVEL and var_1_2[2]:
			local var_1_5 = {}

			if var_1_2[2].mapIdx:
				table.insert(var_1_5, function(arg_6_0)
					local var_6_0, var_6_1 = var_1_1.getMapById(var_1_2[2].mapIdx).isUnlock()

					if var_6_0:
						arg_6_0()
					else
						pg.TipsMgr.GetInstance().ShowTips(var_6_1))

			if var_1_2[2].chapterId:
				table.insert(var_1_5, function(arg_7_0)
					if var_1_1.getChapterById(var_1_2[2].chapterId).isUnlock():
						arg_7_0()
					else
						pg.TipsMgr.GetInstance().ShowTips(i18n("battle_levelScene_chapter_lock")))

			seriesAsync(var_1_5, function()
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE[var_1_2[1]], var_1_2[2]))
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE[var_1_2[1]], var_1_2[2])

		return

	if isa(var_1_0, AvatarFrameTask):
		return

	local var_1_6 = var_1_0.getConfig("sub_type")
	local var_1_7 = var_1_1.getActiveChapter()
	local var_1_8 = {
		chapterId = var_1_7 and var_1_7.id,
		mapIdx = var_1_7 and var_1_7.getConfig("map")
	}
	local var_1_9 = math.modf(var_1_6 / 10)
	local var_1_10 = math.fmod(var_1_6, 10)

	if var_1_9 == 0:
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
	elif var_1_9 == 1:
		if var_1_10 == 9:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DAILYLEVEL)
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
	elif var_1_9 == 2:
		if var_1_10 == 6:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DAILYLEVEL)
		elif var_1_10 == 7:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.MILITARYEXERCISE)
		elif var_1_10 == 8:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
		elif var_1_10 == 9:
			local var_1_11 = tonumber(var_1_0.getConfig("target_id"))

			arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
				system = SYSTEM_PERFORM,
				stageId = tonumber(var_1_11)
			})
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
	elif var_1_9 == 3:
		if var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.GETBOAT)
		elif var_1_10 == 1:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
				blockLock = True,
				mode = DockyardScene.MODE_DESTROY,
				onShip = ShipStatus.canDestroyShip,
				selectedMax = getGameset("ship_select_limit")[1],
				leftTopInfo = i18n("word_destroy"),
				ignoredIds = pg.ShipFlagMgr.GetInstance().FilterShips({
					isActivityNpc = True
				})
			})
		elif var_1_10 == 7:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.NAVALACADEMYSCENE, {
				warp = NavalAcademyScene.WARP_TO_TACTIC
			})
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
				mode = DockyardScene.MODE_OVERVIEW
			})
	elif var_1_9 == 4:
		if var_1_10 == 2:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.EQUIPSCENE, {
				warp = StoreHouseConst.WARP_TO_DESIGN
			})
		elif var_1_10 == 3:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
				mode = DockyardScene.MODE_OVERVIEW
			})
		else
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.EQUIPSCENE, {
				warp = StoreHouseConst.WARP_TO_WEAPON
			})
	elif var_1_9 == 5:
		if var_1_10 == 0 or var_1_10 == 1:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.EQUIPSCENE, {
				warp = StoreHouseConst.WARP_TO_MATERIAL
			})
	elif var_1_9 == 6:
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.COURTYARD)
	elif var_1_9 == 7:
		local var_1_12

		if var_1_10 == 1:
			var_1_12 = NavalAcademyScene.WARP_TO_TACTIC

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.NAVALACADEMYSCENE, {
			warp = var_1_12
		})
	elif var_1_9 == 8:
		if var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.EVENT)
		elif var_1_10 == 1:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.NAVALACADEMYSCENE)
	elif var_1_9 == 9:
		if var_1_10 == 2:
			arg_1_0.sendNotification(TaskMediator.TASK_FILTER, "weekly")
	elif var_1_9 == 10:
		if var_1_10 == 4 or var_1_10 == 5:
			local var_1_13 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_INSTAGRAM)

			if var_1_13 and not var_1_13.isEnd():
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.MAINUI, {
					subContext = Context.New({
						viewComponent = InstagramLayer,
						mediator = InstagramMediator,
						data = {
							id = var_1_13.id
						}
					})
				})
	elif var_1_9 == 11:
		if var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.TECHNOLOGY)
	elif var_1_9 == 12:
		if var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
				warp = NewShopsScene.TYPE_SHAM_SHOP
			})
		elif var_1_10 == 1:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
		elif var_1_10 == 2:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
				warp = NewShopsScene.TYPE_SHOP_STREET
			})
	elif var_1_9 == 13:
		if var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
	elif var_1_9 == 14:
		if var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DAILYLEVEL)
	elif var_1_9 == 15:
		if var_1_10 == 1:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP, {
				warp = NewShopsScene.TYPE_GUILD
			})
		elif var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.SHOP)
	elif var_1_9 == 17:
		if var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.COMMANDERCAT, {
				fleetType = CommanderCatScene.FLEET_TYPE_COMMON
			})
	elif var_1_9 == 18:
		if var_1_10 == 2:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
	elif var_1_9 == 30:
		if var_1_10 == 4:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.WORLD)
	elif var_1_9 == 40:
		if var_1_10 == 2:
			if getProxy(GuildProxy).getData():
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.GUILD, {
					page = "office"
				})
			else
				arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.PUBLIC_GUILD)
	elif var_1_9 == 41:
		if var_1_10 == 7:
			pg.m02.sendNotification(GAME.GO_MINI_GAME, 56)
	elif var_1_9 == 43:
		if var_1_10 == 0 or var_1_10 == 1:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.FEAST)
		elif var_1_10 == 2 or var_1_10 == 3:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.FEAST, {
				page = 1
			})
		elif var_1_10 == 4:
			pg.m02.sendNotification(GAME.GO_MINI_GAME, 56)
	elif var_1_9 == 100:
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
	elif var_1_9 == 101:
		if var_1_10 == 3:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
		elif var_1_10 == 5 or var_1_10 == 8:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
				mode = DockyardScene.MODE_OVERVIEW
			})
	elif var_1_9 == 102:
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.LEVEL, var_1_8)
	elif var_1_9 == 200:
		if var_1_10 == 1 or var_1_10 == 2:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.BIANDUI)
	elif var_1_9 == 201:
		if var_1_10 == 0:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.COURTYARD)
		elif var_1_10 == 1:
			arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.MAINUI)

return var_0_0
