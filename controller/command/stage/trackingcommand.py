local var_0_0 = class("TrackingCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.chapterId
	local var_1_2 = var_1_0.fleetIds
	local var_1_3 = var_1_0.operationItem or 0
	local var_1_4 = var_1_0.loopFlag or 0
	local var_1_5 = var_1_0.duties

	if not var_1_5 or var_1_4 == 0:
		var_1_5 = {}

	local var_1_6 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_5):
		table.insert(var_1_6, {
			key = iter_1_0,
			value = iter_1_1
		})

	local var_1_7 = getProxy(ChapterProxy)
	local var_1_8 = var_1_7.getChapterById(var_1_1)

	var_1_8.loopFlag = var_1_4

	local var_1_9 = var_1_7.getMapById(var_1_8.getConfig("map"))
	local var_1_10 = var_1_7.GetContinuousData(SYSTEM_SCENARIO)

	seriesAsync({
		function(arg_2_0)
			if var_1_9.isRemaster() and var_1_7.remasterTickets <= 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_remaster_tickets_not_enough"))
				arg_1_0.sendNotification(GAME.TRACKING_ERROR, {
					chapter = var_1_8
				})

				return

			if var_1_9.isActivity() and not var_1_9.isRemaster() and not var_1_8.inActTime():
				pg.TipsMgr.GetInstance().ShowTips(i18n("battle_levelScene_close"))
				arg_1_0.sendNotification(GAME.TRACKING_ERROR, {
					chapter = var_1_8
				})

				return

			if var_1_8.isTriesLimit() and not var_1_8.enoughTimes2Start():
				if var_1_8.IsSpChapter():
					pg.TipsMgr.GetInstance().ShowTips(i18n("sp_no_quota"))
				else
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_elite_no_quota"))

				arg_1_0.sendNotification(GAME.TRACKING_ERROR, {
					chapter = var_1_8
				})

				return

			local var_2_0 = getProxy(DailyLevelProxy)

			if var_1_9.getMapType() == Map.ELITE and not var_2_0.IsEliteEnabled():
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_elite_no_quota"))
				arg_1_0.sendNotification(GAME.TRACKING_ERROR, {
					chapter = var_1_8
				})

				return

			if var_1_8.active:
				pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_strategying"))
				arg_1_0.sendNotification(GAME.TRACKING_ERROR, {
					chapter = var_1_8
				})

				return

			if var_1_9.isEscort() and var_1_7.escortChallengeTimes >= var_1_7.getMaxEscortChallengeTimes():
				pg.TipsMgr.GetInstance().ShowTips(i18n("escort_less_count_to_combat"))
				arg_1_0.sendNotification(GAME.TRACKING_ERROR, {
					chapter = var_1_8
				})

				return

			arg_2_0(),
		function(arg_3_0)
			if var_1_8.getConfig("type") != Chapter.CustomFleet:
				arg_3_0()

				return

			local var_3_0, var_3_1 = var_1_8.IsEliteFleetLegal()

			if not var_3_0:
				pg.TipsMgr.GetInstance().ShowTips(var_3_1)
				arg_1_0.sendNotification(GAME.TRACKING_ERROR, {
					chapter = var_1_8
				})

				return

			if var_3_1:
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					modal = True,
					content = i18n("elite_fleet_confirm", Fleet.DEFAULT_NAME[var_3_1]),
					onYes = arg_3_0
				})

				return

			arg_3_0(),
		function(arg_4_0)
			local var_4_0 = var_1_8.getConfig("oil") * var_0_0.CalculateSpItemMoreCostRate(var_1_3)

			if not getProxy(PlayerProxy).getRawData().isEnough({
				oil = var_4_0
			}):
				if not ItemTipPanel.ShowOilBuyTip(var_4_0):
					pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

				arg_1_0.sendNotification(GAME.TRACKING_ERROR, {
					chapter = var_1_8
				})

				return

			arg_4_0(),
		function(arg_5_0)
			if var_1_8.getConfig("type") != Chapter.SelectFleet:
				arg_5_0()

				return

			local var_5_0 = False
			local var_5_1 = ""

			for iter_5_0, iter_5_1 in ipairs(var_1_2):
				var_5_0, var_5_1 = getProxy(FleetProxy).getFleetById(iter_5_1).GetEnergyStatus()

				if var_5_0:
					break

			if var_5_0:
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = var_5_1,
					onYes = arg_5_0
				})

				return

			arg_5_0(),
		function(arg_6_0)
			if var_1_9.isRemaster() and PlayerPrefs.GetString("remaster_tip") != pg.TimeMgr.GetInstance().CurrentSTimeDesc("%Y/%m/%d") and (not var_1_10 or var_1_10.IsFirstBattle()):
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					showStopRemind = True,
					content = i18n("levelScene_activate_remaster"),
					def onYes:()
						if pg.MsgboxMgr.GetInstance().stopRemindToggle.isOn:
							PlayerPrefs.SetString("remaster_tip", pg.TimeMgr.GetInstance().CurrentSTimeDesc("%Y/%m/%d"))

						arg_6_0()
				})

				return

			arg_6_0(),
		function(arg_8_0)
			local var_8_0 = var_1_8.getConfig("enter_story")
			local var_8_1 = var_1_8.getConfig("enter_story_limit")

			if var_8_0 and var_8_0 != "" and arg_1_0.isCrossStoryLimit(var_8_1) and not var_1_9.isRemaster() and not pg.NewStoryMgr.GetInstance().IsPlayed(var_8_0):
				local var_8_2 = tonumber(var_8_0)

				if var_8_2 and var_8_2 > 0:
					arg_1_0.sendNotification(GAME.BEGIN_STAGE, {
						system = SYSTEM_PERFORM,
						stageId = var_8_2,
						exitCallback = arg_8_0
					})

					return
				else
					ChapterOpCommand.PlayChapterStory(var_8_0, arg_8_0, var_1_8.isLoop() and PlayerPrefs.GetInt("chapter_autofight_flag_" .. var_1_8.id, 1) == 1)

					return

			arg_8_0(),
		function(arg_9_0)
			if var_1_10:
				local var_9_0 = var_1_10.GetRestBattleTime()
				local var_9_1 = {
					1,
					1,
					2
				}

				if var_1_9.isRemaster():
					table.insert(var_9_1, 1)

				if var_9_0 > _.reduce(var_9_1, -1, function(arg_10_0, arg_10_1)
					return arg_10_0 + arg_10_1):
					arg_1_0.sendNotification(15300, {
						type = 2,
						ver_str = string.format("tracking Chapter %d by CO times %d", var_1_8.id, var_9_0)
					})

			arg_9_0(),
		function(arg_11_0)
			local var_11_0 = var_1_8.getConfig("map")
			local var_11_1 = var_1_8.getEliteFleetList()
			local var_11_2 = var_1_8.getEliteFleetCommanders()
			local var_11_3 = {}

			for iter_11_0, iter_11_1 in ipairs(var_11_1):
				if var_1_8.singleEliteFleetVertify(iter_11_0):
					local var_11_4 = {}
					local var_11_5 = {}
					local var_11_6 = {}

					for iter_11_2, iter_11_3 in ipairs(iter_11_1):
						var_11_5[#var_11_5 + 1] = iter_11_3

					local var_11_7 = var_11_2[iter_11_0]

					for iter_11_4, iter_11_5 in pairs(var_11_7):
						table.insert(var_11_6, {
							pos = iter_11_4,
							id = iter_11_5
						})

					var_11_4.map_id = var_11_0
					var_11_4.main_id = var_11_5
					var_11_4.commanders = var_11_6
					var_11_3[#var_11_3 + 1] = var_11_4
				else
					var_11_3[#var_11_3 + 1] = {
						main_id = {},
						commanders = {}
					}

			local var_11_8 = var_1_8.getSupportFleet()
			local var_11_9 = {}
			local var_11_10 = {}

			for iter_11_6, iter_11_7 in ipairs(var_11_8):
				var_11_10[#var_11_10 + 1] = iter_11_7

			var_11_9.map_id = var_11_0
			var_11_9.main_id = var_11_10
			var_11_9.commanders = {}
			var_11_3[#var_11_3 + 1] = var_11_9
			arg_1_0.chapterId = var_1_1
			arg_1_0.fleetIds = var_1_2
			arg_1_0.fleetDatas = var_11_3
			arg_1_0.loopFlag = var_1_4
			arg_1_0.operationItem = var_1_3
			arg_1_0.dutiesKeyValue = var_1_6
			arg_1_0.autoFightFlag = var_1_0.autoFightFlag

			arg_1_0.sendProto()
	})

def var_0_0.sendProto(arg_12_0):
	local var_12_0 = arg_12_0.chapterId
	local var_12_1 = arg_12_0.fleetIds
	local var_12_2 = arg_12_0.fleetDatas
	local var_12_3 = arg_12_0.operationItem
	local var_12_4 = arg_12_0.loopFlag
	local var_12_5 = arg_12_0.dutiesKeyValue
	local var_12_6 = arg_12_0.autoFightFlag

	pg.ConnectionMgr.GetInstance().Send(13101, {
		id = var_12_0,
		group_id_list = var_12_1,
		elite_fleet_list = var_12_2,
		operation_item = var_12_3,
		loop_flag = var_12_4,
		fleet_duties = var_12_5
	}, 13102, function(arg_13_0)
		if arg_13_0.result == 0:
			local var_13_0 = getProxy(ChapterProxy)
			local var_13_1 = var_13_0.getChapterById(var_12_0)
			local var_13_2 = var_13_0.getMapById(var_13_1.getConfig("map"))
			local var_13_3 = getProxy(PlayerProxy)
			local var_13_4 = var_13_3.getData()

			var_13_1.update(arg_13_0.current_chapter)

			local var_13_5 = var_13_1.getConfig("oil")

			var_13_4.consume({
				oil = var_13_5 * var_13_1.GetExtraCostRate()
			})
			var_13_3.updatePlayer(var_13_4)

			if var_12_3 != 0:
				getProxy(BagProxy).removeItemById(var_12_3, 1)

			for iter_13_0, iter_13_1 in pairs(var_13_1.cells):
				if ChapterConst.NeedMarkAsLurk(iter_13_1):
					iter_13_1.trait = ChapterConst.TraitLurk

			for iter_13_2, iter_13_3 in ipairs(var_13_1.champions):
				iter_13_3.trait = ChapterConst.TraitLurk

			var_13_0.updateChapter(var_13_1)

			if var_13_2.isEscort():
				var_13_0.escortChallengeTimes = var_13_0.escortChallengeTimes + 1

			if var_13_2.isRemaster():
				var_13_0.remasterTickets = var_13_0.remasterTickets - 1

			local var_13_6 = var_13_0.GetContinuousData(SYSTEM_SCENARIO)

			if var_13_6:
				var_13_6.TryActivate()

			arg_12_0.sendNotification(GAME.TRACKING_DONE, var_13_1)
			getProxy(ChapterProxy).updateExtraFlag(var_13_1, var_13_1.extraFlagList, {}, True)

			if var_12_4 != 0 and var_12_6:
				getProxy(ChapterProxy).SetChapterAutoFlag(var_12_0, True)

			return

		if arg_13_0.result == 1:
			pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_tracking_error_retry"))
			arg_12_0.sendNotification(GAME.CHAPTER_OP, {
				type = ChapterConst.OpRetreat
			})
		elif arg_13_0.result == 3010:
			pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_tracking_error_3001"))
		else
			pg.TipsMgr.GetInstance().ShowTips(errorTip("levelScene_tracking_erro", arg_13_0.result))

		local var_13_7 = getProxy(ChapterProxy).getChapterById(var_12_0)

		arg_12_0.sendNotification(GAME.TRACKING_ERROR, {
			chapter = var_13_7
		}))

def var_0_0.isCrossStoryLimit(arg_14_0, arg_14_1):
	local var_14_0 = True

	if arg_14_1 != "" and #arg_14_1 > 0:
		var_14_0 = _.all(arg_14_1, function(arg_15_0)
			if arg_15_0[1] == 1:
				local var_15_0 = getProxy(TaskProxy).getTaskById(arg_15_0[2])

				return var_15_0 and not var_15_0.isFinish()

			return False)

	return var_14_0

def var_0_0.CalculateSpItemMoreCostRate(arg_16_0):
	local var_16_0 = 1

	if not arg_16_0 or arg_16_0 == 0:
		return var_16_0

	local var_16_1 = Item.getConfigData(arg_16_0).usage_arg
	local var_16_2 = _.map(string.split(string.sub(var_16_1, 2, -2), ","), function(arg_17_0)
		return tonumber(arg_17_0))

	for iter_16_0, iter_16_1 in ipairs(var_16_2):
		local var_16_3 = pg.benefit_buff_template[iter_16_0]

		if var_16_3 and var_16_3.benefit_type == Chapter.OPERATION_BUFF_TYPE_COST:
			var_16_0 = var_16_0 + tonumber(var_16_3.benefit_effect) * 0.01

	return (math.max(1, var_16_0))

return var_0_0
