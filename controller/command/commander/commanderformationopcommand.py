local var_0_0 = class("CommanderFormationOPCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().data
	local var_1_1 = var_1_0.FleetType
	local var_1_2 = getProxy(CommanderProxy)
	local var_1_3 = getProxy(ChapterProxy)
	local var_1_4 = getProxy(FleetProxy)
	local var_1_5 = var_1_0.data

	if var_1_5.type == LevelUIConst.COMMANDER_OP_RENAME:
		local var_1_6 = var_1_5.id
		local var_1_7 = var_1_5.str
		local var_1_8 = var_1_5.onFailed

		arg_1_0.sendNotification(GAME.SET_COMMANDER_PREFAB_NAME, {
			id = var_1_6,
			name = var_1_7,
			onFailed = var_1_8
		})

		return

	if var_1_1 == LevelUIConst.FLEET_TYPE_SELECT:
		local var_1_9 = var_1_5.id
		local var_1_10 = var_1_0.fleetId
		local var_1_11 = var_1_0.chapterId

		if var_1_5.type == LevelUIConst.COMMANDER_OP_RECORD_PREFAB:
			local var_1_12 = var_1_4.getFleetById(var_1_10).getCommanders()

			arg_1_0.sendNotification(GAME.SET_COMMANDER_PREFAB, {
				id = var_1_9,
				commanders = var_1_12
			})
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_USE_PREFAB:
			arg_1_0.sendNotification(GAME.USE_COMMANDER_PREFBA, {
				pid = var_1_9,
				fleetId = var_1_10
			})
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_REST_ALL:
			local var_1_13 = {
				function(arg_2_0)
					arg_1_0.sendNotification(GAME.COOMMANDER_EQUIP_TO_FLEET, {
						commanderId = 0,
						pos = 1,
						fleetId = var_1_10,
						callback = arg_2_0
					}),
				function(arg_3_0)
					arg_1_0.sendNotification(GAME.COOMMANDER_EQUIP_TO_FLEET, {
						commanderId = 0,
						pos = 2,
						fleetId = var_1_10,
						callback = arg_3_0
					})
			}

			seriesAsync(var_1_13)
	elif var_1_1 == LevelUIConst.FLEET_TYPE_EDIT:
		local var_1_14 = var_1_5.id
		local var_1_15 = var_1_2.getPrefabFleetById(var_1_14)
		local var_1_16 = var_1_0.index
		local var_1_17 = var_1_0.chapterId

		if var_1_5.type == LevelUIConst.COMMANDER_OP_RECORD_PREFAB:
			local var_1_18 = var_1_3.getChapterById(var_1_17)
			local var_1_19 = var_1_18.getEliteFleetCommanders()[var_1_16]

			if table.getCount(var_1_19) == 0:
				return

			local var_1_20 = {}

			for iter_1_0 = 1, 2:
				local var_1_21 = var_1_19[iter_1_0]
				local var_1_22 = var_1_2.getCommanderById(var_1_21)

				if var_1_22:
					var_1_20[iter_1_0] = var_1_22

			arg_1_0.sendNotification(GAME.SET_COMMANDER_PREFAB, {
				id = var_1_14,
				commanders = var_1_20
			})
			var_1_3.updateChapter(var_1_18)
			arg_1_0.sendNotification(GAME.COMMANDER_ELIT_FORMATION_OP_DONE, {
				chapterId = var_1_18.id,
				index = var_1_16
			})
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_USE_PREFAB:
			local var_1_23 = {}

			for iter_1_1 = 1, 2:
				local var_1_24 = var_1_15.getCommanderByPos(iter_1_1)

				if var_1_24:
					local var_1_25, var_1_26 = Commander.canEquipToEliteChapter(var_1_17, var_1_16, iter_1_1, var_1_24.id)

					if not var_1_25:
						pg.TipsMgr.GetInstance().ShowTips(var_1_26)

						return

			local var_1_27 = var_1_3.getChapterById(var_1_17)
			local var_1_28 = var_1_27.getEliteFleetCommanders()[var_1_16]

			if var_1_15.isSameId(var_1_28):
				return

			for iter_1_2 = 1, 2:
				local var_1_29 = var_1_15.getCommanderByPos(iter_1_2)

				if var_1_29:
					arg_1_0.sendNotification(GAME.SELECT_ELIT_CHAPTER_COMMANDER, {
						chapterId = var_1_17,
						index = var_1_16,
						pos = iter_1_2,
						commanderId = var_1_29.id
					})
				else
					arg_1_0.sendNotification(GAME.SELECT_ELIT_CHAPTER_COMMANDER, {
						chapterId = var_1_17,
						index = var_1_16,
						pos = iter_1_2
					})

			arg_1_0.sendNotification(GAME.COMMANDER_ELIT_FORMATION_OP_DONE, {
				chapterId = var_1_27.id,
				index = var_1_16
			})
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_REST_ALL:
			local var_1_30 = var_1_3.getChapterById(var_1_17)

			for iter_1_3 = 1, 2:
				arg_1_0.sendNotification(GAME.SELECT_ELIT_CHAPTER_COMMANDER, {
					chapterId = var_1_17,
					index = var_1_16,
					pos = iter_1_3
				})

			arg_1_0.sendNotification(GAME.COMMANDER_ELIT_FORMATION_OP_DONE, {
				chapterId = var_1_30.id,
				index = var_1_16
			})
	elif var_1_1 == LevelUIConst.FLEET_TYPE_ACTIVITY:
		local var_1_31 = var_1_5.id
		local var_1_32 = var_1_2.getPrefabFleetById(var_1_31)
		local var_1_33 = var_1_0.fleetId
		local var_1_34 = var_1_0.actId

		if var_1_5.type == LevelUIConst.COMMANDER_OP_RECORD_PREFAB:
			local var_1_35 = var_1_4.getActivityFleets()[var_1_34][var_1_33].getCommanders()

			arg_1_0.sendNotification(GAME.SET_COMMANDER_PREFAB, {
				id = var_1_31,
				commanders = var_1_35
			})
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_USE_PREFAB:
			local var_1_36 = {}
			local var_1_37 = var_1_4.getActivityFleets()[var_1_34]
			local var_1_38 = pg.activity_template[var_1_34]
			local var_1_39 = var_1_38 and var_1_38.type or 0

			local function var_1_40(arg_4_0)
				for iter_4_0, iter_4_1 in pairs(var_1_37):
					local var_4_0 = var_1_33 != iter_4_0

					if var_1_39 == ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2 or var_1_39 == ActivityConst.ACTIVITY_TYPE_BOSSSINGLE:
						var_4_0 = iter_4_0 == ActivityBossMediatorTemplate.GetPairedFleetIndex(var_1_33)

					if var_4_0:
						local var_4_1 = iter_4_1.getCommanders()

						for iter_4_2, iter_4_3 in pairs(var_4_1):
							if arg_4_0 == iter_4_3.id:
								return iter_4_0, iter_4_2

				return None

			for iter_1_4 = 1, 2:
				local var_1_41 = var_1_32.getCommanderByPos(iter_1_4)

				if var_1_41:
					local var_1_42, var_1_43 = var_1_40(var_1_41.id)

					if var_1_42 and var_1_43:
						table.insert(var_1_36, function(arg_5_0)
							local var_5_0 = var_1_43 == 1 and i18n("commander_main_pos") or i18n("commander_assistant_pos")
							local var_5_1 = Fleet.DEFAULT_NAME[var_1_42]

							pg.MsgboxMgr.GetInstance().ShowMsgBox({
								content = i18n("comander_repalce_tip", var_5_1, var_5_0),
								def onYes:()
									local var_6_0 = var_1_37[var_1_42]

									var_6_0.updateCommanderByPos(var_1_43, None)
									var_1_4.updateActivityFleet(var_1_34, var_1_42, var_6_0)

									local var_6_1 = var_1_37[var_1_33]

									var_6_1.updateCommanderByPos(iter_1_4, var_1_41)
									var_1_4.updateActivityFleet(var_1_34, var_1_33, var_6_1)
									arg_5_0(),
								onNo = arg_5_0
							}))
					else
						table.insert(var_1_36, function(arg_7_0)
							local var_7_0 = var_1_37[var_1_33]

							var_7_0.updateCommanderByPos(iter_1_4, var_1_41)
							var_1_4.updateActivityFleet(var_1_34, var_1_33, var_7_0)
							arg_7_0())
				else
					table.insert(var_1_36, function(arg_8_0)
						local var_8_0 = var_1_37[var_1_33]

						var_8_0.updateCommanderByPos(iter_1_4, None)
						var_1_4.updateActivityFleet(var_1_34, var_1_33, var_8_0)
						arg_8_0())

			seriesAsync(var_1_36, function()
				arg_1_0.sendNotification(GAME.COMMANDER_ACTIVITY_FORMATION_OP_DONE, {
					actId = var_1_34,
					fleetId = var_1_33
				}))
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_REST_ALL:
			local var_1_44 = var_1_4.getActivityFleets()[var_1_34][var_1_33]

			for iter_1_5 = 1, 2:
				var_1_44.updateCommanderByPos(iter_1_5, None)

			var_1_4.updateActivityFleet(var_1_34, var_1_33, var_1_44)
			arg_1_0.sendNotification(GAME.COMMANDER_ACTIVITY_FORMATION_OP_DONE, {
				actId = var_1_34,
				fleetId = var_1_33
			})
	elif var_1_1 == LevelUIConst.FLEET_TYPE_WORLD:
		local var_1_45 = var_1_5.id
		local var_1_46 = var_1_2.getPrefabFleetById(var_1_45)
		local var_1_47 = var_1_0.fleets
		local var_1_48 = var_1_0.fleetType
		local var_1_49 = var_1_0.fleetIndex
		local var_1_50 = var_1_47[var_1_48][var_1_49]
		local var_1_51 = Fleet.New({
			ship_list = {},
			commanders = var_1_50.commanders
		})

		if var_1_5.type == LevelUIConst.COMMANDER_OP_RECORD_PREFAB:
			local var_1_52 = var_1_51.getCommanders()

			arg_1_0.sendNotification(GAME.SET_COMMANDER_PREFAB, {
				id = var_1_45,
				commanders = var_1_52
			})
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_USE_PREFAB:
			local var_1_53 = {}

			local function var_1_54(arg_10_0)
				for iter_10_0, iter_10_1 in pairs(var_1_47):
					for iter_10_2, iter_10_3 in pairs(iter_10_1):
						if var_1_50 != iter_10_3:
							for iter_10_4, iter_10_5 in ipairs(iter_10_3.commanders):
								if iter_10_5.id == arg_10_0:
									return iter_10_0, iter_10_2, iter_10_5.pos

				return None

			for iter_1_6 = 1, 2:
				local var_1_55 = var_1_46.getCommanderByPos(iter_1_6)

				if var_1_55:
					local var_1_56, var_1_57, var_1_58 = var_1_54(var_1_55.id)

					if var_1_56 and var_1_57 and var_1_58:
						table.insert(var_1_53, function(arg_11_0)
							local var_11_0 = var_1_58 == 1 and i18n("commander_main_pos") or i18n("commander_assistant_pos")
							local var_11_1 = Fleet.DEFAULT_NAME[var_1_57 + (var_1_56 == FleetType.Submarine and 10 or 0)]

							pg.MsgboxMgr.GetInstance().ShowMsgBox({
								content = i18n("comander_repalce_tip", var_11_1, var_11_0),
								def onYes:()
									local var_12_0 = var_1_47[var_1_56][var_1_57]
									local var_12_1 = Fleet.New({
										ship_list = {},
										commanders = var_12_0.commanders
									})

									var_12_1.updateCommanderByPos(iter_1_6, None)

									var_12_0.commanders = var_12_1.outputCommanders()

									var_1_51.updateCommanderByPos(iter_1_6, var_1_55)

									var_1_50.commanders = var_1_51.outputCommanders()

									arg_11_0(),
								onNo = arg_11_0
							}))
					else
						table.insert(var_1_53, function(arg_13_0)
							var_1_51.updateCommanderByPos(iter_1_6, var_1_55)

							var_1_50.commanders = var_1_51.outputCommanders()

							arg_13_0())
				else
					table.insert(var_1_53, function(arg_14_0)
						var_1_51.updateCommanderByPos(iter_1_6, None)

						var_1_50.commanders = var_1_51.outputCommanders()

						arg_14_0())

			seriesAsync(var_1_53, function()
				arg_1_0.sendNotification(GAME.COMMANDER_WORLD_FORMATION_OP_DONE, {
					fleet = var_1_51
				}))
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_REST_ALL:
			for iter_1_7 = 1, 2:
				var_1_51.updateCommanderByPos(iter_1_7, None)

			var_1_50.commanders = var_1_51.outputCommanders()

			arg_1_0.sendNotification(GAME.COMMANDER_WORLD_FORMATION_OP_DONE, {
				fleet = var_1_51
			})
	elif var_1_1 == LevelUIConst.FLEET_TYPE_BOSSRUSH:
		local var_1_59 = var_1_5.id
		local var_1_60 = var_1_2.getPrefabFleetById(var_1_59)
		local var_1_61 = var_1_0.fleetId
		local var_1_62 = var_1_0.actId

		if var_1_5.type == LevelUIConst.COMMANDER_OP_RECORD_PREFAB:
			local var_1_63 = var_1_4.getActivityFleets()[var_1_62][var_1_61].getCommanders()

			arg_1_0.sendNotification(GAME.SET_COMMANDER_PREFAB, {
				id = var_1_59,
				commanders = var_1_63
			})
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_USE_PREFAB:
			local var_1_64 = {}
			local var_1_65 = {}

			_.each(var_1_0.fleets, function(arg_16_0)
				var_1_65[arg_16_0.id] = arg_16_0)

			local function var_1_66(arg_17_0)
				for iter_17_0, iter_17_1 in pairs(var_1_65):
					if var_1_61 != iter_17_0:
						local var_17_0 = iter_17_1.getCommanders()

						for iter_17_2, iter_17_3 in pairs(var_17_0):
							if arg_17_0 == iter_17_3.id:
								return iter_17_0, iter_17_2

				return None

			for iter_1_8 = 1, 2:
				local var_1_67 = var_1_60.getCommanderByPos(iter_1_8)

				if var_1_67:
					local var_1_68, var_1_69 = var_1_66(var_1_67.id)

					if var_1_68 and var_1_69:
						table.insert(var_1_64, function(arg_18_0)
							local var_18_0 = var_1_69 == 1 and i18n("commander_main_pos") or i18n("commander_assistant_pos")
							local var_18_1 = table.indexof(var_1_0.fleets, var_1_65[var_1_68])
							local var_18_2 = Fleet.DEFAULT_NAME[var_18_1]

							pg.MsgboxMgr.GetInstance().ShowMsgBox({
								content = i18n("comander_repalce_tip", var_18_2, var_18_0),
								def onYes:()
									local var_19_0 = var_1_65[var_1_68]

									var_19_0.updateCommanderByPos(var_1_69, None)
									var_1_4.updateActivityFleet(var_1_62, var_1_68, var_19_0)

									local var_19_1 = var_1_65[var_1_61]

									var_19_1.updateCommanderByPos(iter_1_8, var_1_67)
									var_1_4.updateActivityFleet(var_1_62, var_1_61, var_19_1)
									arg_18_0(),
								onNo = arg_18_0
							}))
					else
						table.insert(var_1_64, function(arg_20_0)
							local var_20_0 = var_1_65[var_1_61]

							var_20_0.updateCommanderByPos(iter_1_8, var_1_67)
							var_1_4.updateActivityFleet(var_1_62, var_1_61, var_20_0)
							arg_20_0())
				else
					table.insert(var_1_64, function(arg_21_0)
						local var_21_0 = var_1_65[var_1_61]

						var_21_0.updateCommanderByPos(iter_1_8, None)
						var_1_4.updateActivityFleet(var_1_62, var_1_61, var_21_0)
						arg_21_0())

			seriesAsync(var_1_64, function()
				arg_1_0.sendNotification(GAME.COMMANDER_ACTIVITY_FORMATION_OP_DONE, {
					actId = var_1_62,
					fleetId = var_1_61
				}))
		elif var_1_5.type == LevelUIConst.COMMANDER_OP_REST_ALL:
			local var_1_70 = var_1_4.getActivityFleets()[var_1_62][var_1_61]

			for iter_1_9 = 1, 2:
				var_1_70.updateCommanderByPos(iter_1_9, None)

			var_1_4.updateActivityFleet(var_1_62, var_1_61, var_1_70)
			arg_1_0.sendNotification(GAME.COMMANDER_ACTIVITY_FORMATION_OP_DONE, {
				actId = var_1_62,
				fleetId = var_1_61
			})

return var_0_0
