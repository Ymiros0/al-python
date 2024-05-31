local var_0_0 = class("SelectCommanderCatForPlayScene", import(".CommanderCatScene"))

def var_0_0.emit(arg_1_0, ...):
	if unpack({
		...
	}) == var_0_0.ON_BACK:
		var_0_0.super.emit(arg_1_0, var_0_0.ON_CLOSE)
	else
		var_0_0.super.emit(arg_1_0, ...)

def var_0_0.didEnter(arg_2_0):
	local var_2_0 = arg_2_0.contextData.activeCommander

	arg_2_0.contextData.mode = var_0_0.MODE_SELECT
	arg_2_0.contextData.maxCount = 10
	arg_2_0.contextData.fleetType = CommanderCatScene.FLEET_TYPE_COMMON
	arg_2_0.contextData.activeGroupId = var_2_0.groupId
	arg_2_0.contextData.ignoredIds = {}

	table.insert(arg_2_0.contextData.ignoredIds, var_2_0.id)
	arg_2_0.CollectIgnoredIdsForPlay(arg_2_0.contextData.ignoredIds)

	function arg_2_0.contextData.onCommander(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
		return arg_2_0.IsLegalForPlay(var_2_0, arg_3_0, arg_3_1, arg_3_2)

	var_0_0.super.didEnter(arg_2_0)

def var_0_0.RegisterEvent(arg_4_0):
	var_0_0.super.RegisterEvent(arg_4_0)
	arg_4_0.bind(CommanderCatDockPage.ON_SORT, function(arg_5_0)
		onNextTick(function()
			local var_6_0 = arg_4_0.pages[CommanderCatScene.PAGE_DOCK]

			if var_6_0 and var_6_0.GetLoaded():
				local var_6_1 = Clone(var_6_0.sortData)

				if arg_4_0.contextData.OnSort:
					arg_4_0.contextData.OnSort(var_6_1)))

def var_0_0.CollectIgnoredIdsForPlay(arg_7_0, arg_7_1):
	local var_7_0 = getProxy(CommanderProxy).getRawData()

	for iter_7_0, iter_7_1 in pairs(var_7_0):
		if iter_7_1.isLocked():
			table.insert(arg_7_1, iter_7_1.id)

	local var_7_1 = getProxy(ChapterProxy).getActiveChapter()

	if var_7_1:
		_.each(var_7_1.fleets, function(arg_8_0)
			local var_8_0 = arg_8_0.getCommanders()

			for iter_8_0, iter_8_1 in pairs(var_8_0):
				table.insert(arg_7_1, iter_8_1.id))

def var_0_0.IsLegalForPlay(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4):
	if nowWorld().CheckCommanderInFleet(arg_9_2.id):
		return False, i18n("commander_is_in_bigworld")

	if arg_9_1.isMaxLevel() and not arg_9_1.isSameGroup(arg_9_2.groupId):
		return False, i18n("commander_select_matiral_erro")

	if getProxy(CommanderProxy).IsHome(arg_9_2.id):
		return False, i18n("cat_sleep_notplay")

	if not arg_9_0.CheckFormation(arg_9_2, arg_9_4, arg_9_3):
		return False, None

	if not arg_9_0.CheckGuild(arg_9_2, arg_9_4, arg_9_3):
		return False, None

	if not arg_9_0.CheckExtra(arg_9_2, arg_9_4, arg_9_3):
		return False, None

	return True

def var_0_0.CheckFormation(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	local var_10_0 = getProxy(FleetProxy)
	local var_10_1 = var_10_0.getCommanders()
	local var_10_2 = _.detect(var_10_1, function(arg_11_0)
		return arg_10_1.id == arg_11_0.commanderId)

	if not var_10_2:
		return True

	arg_10_0.contextData.msgBox.ExecuteAction("Show", {
		content = i18n("commander_material_is_in_fleet_tip"),
		def onYes:()
			pg.m02.sendNotification(GAME.COOMMANDER_EQUIP_TO_FLEET, {
				commanderId = 0,
				fleetId = var_10_2.fleetId,
				pos = var_10_2.pos,
				def callback:()
					var_10_1 = var_10_0.getCommanders()

					if arg_10_2:
						arg_10_2()
			}),
		onNo = arg_10_3,
		onClose = arg_10_3
	})

	return False

def var_0_0.CheckGuild(arg_14_0, arg_14_1, arg_14_2, arg_14_3):
	local var_14_0 = getProxy(GuildProxy).getRawData()

	if not var_14_0 or not var_14_0.ExistCommander(arg_14_1.id):
		return True

	arg_14_0.contextData.msgBox.ExecuteAction("Show", {
		content = i18n("commander_is_in_guild"),
		def onYes:()
			local var_15_0 = var_14_0.GetActiveEvent()

			if not var_15_0:
				return

			local var_15_1 = var_15_0.GetBossMission()

			if not var_15_1 or not var_15_1.IsActive():
				return

			local var_15_2 = var_15_1.GetFleetCommanderId(arg_14_1.id)

			if not var_15_2:
				return

			local var_15_3 = Clone(var_15_2)
			local var_15_4 = var_15_3.GetCommanderPos(arg_14_1.id)

			if not var_15_4:
				return

			var_15_3.RemoveCommander(var_15_4)
			pg.m02.sendNotification(GAME.GUILD_UPDATE_BOSS_FORMATION, {
				force = True,
				editFleet = {
					[var_15_3.id] = var_15_3
				},
				callback = arg_14_2
			}),
		onNo = arg_14_3,
		onClose = arg_14_3
	})

	return False

def var_0_0.CheckExtra(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	local var_16_0 = getProxy(FleetProxy)
	local var_16_1 = var_16_0.getCommanders()
	local var_16_2 = var_16_0.GetExtraCommanders()
	local var_16_3 = _.detect(var_16_2, function(arg_17_0)
		return arg_16_1.id == arg_17_0.commanderId)

	if not var_16_3:
		return True

	arg_16_0.contextData.msgBox.ExecuteAction("Show", {
		content = i18n("commander_material_is_in_fleet_tip"),
		def onYes:()
			pg.m02.sendNotification(GAME.COOMMANDER_EQUIP_TO_FLEET, {
				commanderId = 0,
				fleetId = var_16_3.fleetId,
				pos = var_16_3.pos,
				def callback:()
					var_16_1 = var_16_0.getCommanders()

					if arg_16_2:
						arg_16_2()
			}),
		onNo = arg_16_3,
		onClose = arg_16_3
	})

	return False

return var_0_0
