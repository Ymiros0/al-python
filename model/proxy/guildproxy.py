local var_0_0 = class("GuildProxy", import(".NetProxy"))

var_0_0.NEW_GUILD_ADDED = "GuildProxy.NEW_GUILD_ADDED"
var_0_0.GUILD_UPDATED = "GuildProxy.GUILD_UPDATED"
var_0_0.EXIT_GUILD = "GuildProxy.EXIT_GUILD"
var_0_0.REQUEST_ADDED = "GuildProxy.REQUEST_ADDED"
var_0_0.REQUEST_DELETED = "GuildProxy.REQUEST_DELETED"
var_0_0.NEW_MSG_ADDED = "GuildProxy.NEW_MSG_ADDED"
var_0_0.REQUEST_COUNT_UPDATED = "GuildProxy.REQUEST_COUNT_UPDATED"
var_0_0.LOG_ADDED = "GuildProxy.LOG_ADDED"
var_0_0.WEEKLYTASK_UPDATED = "GuildProxy.WEEKLYTASK_UPDATED"
var_0_0.SUPPLY_STARTED = "GuildProxy.SUPPLY_STARTED"
var_0_0.WEEKLYTASK_ADDED = "GuildProxy.WEEKLYTASK_ADDED"
var_0_0.DONATE_UPDTAE = "GuildProxy.DONATE_UPDTAE"
var_0_0.TECHNOLOGY_START = "GuildProxy.TECHNOLOGY_START"
var_0_0.TECHNOLOGY_STOP = "GuildProxy.TECHNOLOGY_STOP"
var_0_0.CAPITAL_UPDATED = "GuildProxy.CAPITAL_UPDATED"
var_0_0.GUILD_BATTLE_STARTED = "GuildProxy.GUILD_BATTLE_STARTED"
var_0_0.GUILD_BATTLE_CLOSED = "GuildProxy.GUILD_BATTLE_CLOSED"
var_0_0.ON_DELETED_MEMBER = "GuildProxy.ON_DELETED_MEMBER"
var_0_0.ON_ADDED_MEMBER = "GuildProxy.ON_ADDED_MEMBER"
var_0_0.BATTLE_BTN_FLAG_CHANGE = "GuildProxy.BATTLE_BTN_FLAG_CHANGE"
var_0_0.ON_EXIST_DELETED_MEMBER = "GuildProxy.ON_EXIST_DELETED_MEMBER"
var_0_0.ON_DONATE_LIST_UPDATED = "GuildProxy.ON_DONATE_LIST_UPDATED"

def var_0_0.register(arg_1_0):
	arg_1_0.Init()
	arg_1_0.on(60000, function(arg_2_0)
		local var_2_0 = Guild.New(arg_2_0.guild)

		if var_2_0.id == 0:
			arg_1_0.exitGuild()
		elif arg_1_0.data == None:
			arg_1_0.addGuild(var_2_0)

			if not getProxy(GuildProxy).isGetChatMsg:
				arg_1_0.sendNotification(GAME.GET_GUILD_CHAT_LIST)

			arg_1_0.sendNotification(GAME.GUILD_GET_USER_INFO)
			arg_1_0.sendNotification(GAME.GUILD_GET_MY_ASSAULT_FLEET, {})
			arg_1_0.sendNotification(GAME.GUILD_GET_ASSAULT_FLEET, {})
			arg_1_0.sendNotification(GAME.GUILD_GET_ACTIVATION_EVENT, {
				force = True
			})
			arg_1_0.sendNotification(GAME.GUILD_GET_REQUEST_LIST, var_2_0.id)
		else
			arg_1_0.updateGuild(var_2_0))
	arg_1_0.on(60009, function(arg_3_0)
		arg_1_0.requestCount = arg_3_0.count

		arg_1_0.sendNotification(var_0_0.REQUEST_COUNT_UPDATED, arg_3_0.count))
	arg_1_0.on(60030, function(arg_4_0)
		local var_4_0 = arg_1_0.getData()

		if not var_4_0:
			return

		var_4_0.updateBaseInfo({
			base = arg_4_0.guild
		})
		arg_1_0.updateGuild(var_4_0))
	arg_1_0.on(60031, function(arg_5_0)
		local var_5_0 = arg_1_0.getData()

		if not var_5_0:
			return

		local var_5_1 = False

		for iter_5_0, iter_5_1 in ipairs(arg_5_0.member_list):
			local var_5_2 = GuildMember.New(iter_5_1)

			if var_5_2.duty == 0:
				local var_5_3 = var_5_0.getMemberById(var_5_2.id).clone()

				var_5_0.deleteMember(var_5_2.id)
				arg_1_0.sendNotification(GuildProxy.ON_DELETED_MEMBER, {
					member = var_5_3
				})

				var_5_1 = True
			elif var_5_0.member[var_5_2.id]:
				var_5_0.updateMember(var_5_2)
			else
				var_5_0.addMember(var_5_2)
				arg_1_0.sendNotification(GuildProxy.ON_ADDED_MEMBER, {
					member = var_5_2
				})

		for iter_5_2, iter_5_3 in ipairs(arg_5_0.log_list):
			local var_5_4 = GuildLogInfo.New(iter_5_3)

			var_5_0.addLog(var_5_4)
			arg_1_0.sendNotification(var_0_0.LOG_ADDED, Clone(var_5_4))

		var_5_0.setMemberCount(table.getCount(var_5_0.member or {}))
		arg_1_0.updateGuild(var_5_0)

		if var_5_1:
			arg_1_0.sendNotification(GuildProxy.ON_EXIST_DELETED_MEMBER))
	arg_1_0.on(60032, function(arg_6_0)
		local var_6_0 = arg_1_0.getData()

		if not var_6_0:
			return

		var_6_0.updateExp(arg_6_0.exp)
		var_6_0.updateLevel(arg_6_0.lv)
		arg_1_0.updateGuild(var_6_0))
	arg_1_0.on(60008, function(arg_7_0)
		local var_7_0 = arg_7_0.chat
		local var_7_1 = arg_1_0.data.warpChatInfo(var_7_0)

		if var_7_1:
			arg_1_0.AddNewMsg(var_7_1))
	arg_1_0.on(62004, function(arg_8_0)
		local var_8_0 = arg_1_0.getData()

		if not var_8_0 or not var_8_0.IsCompletion():
			return

		local var_8_1 = GuildTask.New(arg_8_0.this_weekly_tasks)

		var_8_0.updateWeeklyTask(var_8_1)
		var_8_0.setWeeklyTaskFlag(0)
		arg_1_0.updateGuild(var_8_0)
		arg_1_0.sendNotification(var_0_0.WEEKLYTASK_ADDED))
	arg_1_0.on(62005, function(arg_9_0)
		local var_9_0 = arg_1_0.getData()

		if not var_9_0 or not var_9_0.IsCompletion():
			return

		var_9_0.startSupply(arg_9_0.benefit_finish_time)

		local var_9_1 = var_9_0.getSupplyConsume()

		var_9_0.consumeCapital(var_9_1)
		arg_1_0.updateGuild(var_9_0)
		arg_1_0.sendNotification(var_0_0.CAPITAL_UPDATED)
		arg_1_0.sendNotification(var_0_0.SUPPLY_STARTED))
	arg_1_0.on(62018, function(arg_10_0)
		local var_10_0 = arg_1_0.getData()

		if not var_10_0 or not var_10_0.IsCompletion():
			return

		local var_10_1 = pg.guild_technology_template[arg_10_0.id].group
		local var_10_2 = var_10_0.getActiveTechnologyGroup()

		if var_10_2:
			var_10_2.Stop()

		var_10_0.getTechnologyGroupById(var_10_1).Start()
		var_10_0.UpdateTechCancelCnt()
		arg_1_0.updateGuild(var_10_0)
		arg_1_0.sendNotification(var_0_0.TECHNOLOGY_START))
	arg_1_0.on(62019, function(arg_11_0)
		local var_11_0 = arg_1_0.getData()

		if not var_11_0 or not var_11_0.IsCompletion():
			return

		local var_11_1 = GuildDonateTask.New({
			id = arg_11_0.id
		})
		local var_11_2 = arg_11_0.has_capital == 1
		local var_11_3 = arg_11_0.has_tech_point == 1
		local var_11_4 = arg_11_0.user_id
		local var_11_5 = getProxy(PlayerProxy).getRawData().id

		if var_11_2:
			local var_11_6 = var_11_1.getCapital()
			local var_11_7 = var_11_0.getCapital()

			var_11_0.updateCapital(var_11_7 + var_11_6)

			if var_11_5 == var_11_4:
				pg.TipsMgr.GetInstance().ShowTips(i18n("guild_donate_addition_capital_tip", var_11_6))

		if var_11_3:
			local var_11_8 = var_11_0.getActiveTechnologyGroup()

			if var_11_8:
				local var_11_9 = var_11_8.pid
				local var_11_10 = var_11_1.getConfig("award_tech_exp")

				var_11_8.AddProgress(var_11_10)

				local var_11_11 = var_11_8.pid

				if var_11_9 != var_11_11 and var_11_8.GuildMemberCntType():
					local var_11_12 = var_11_0.getTechnologyById(var_11_8.id)

					assert(var_11_12)
					var_11_12.Update(var_11_11, var_11_8)

				if var_11_5 == var_11_4:
					pg.TipsMgr.GetInstance().ShowTips(i18n("guild_donate_addition_techpoint_tip", var_11_10))

		if var_11_2 or var_11_3:
			arg_1_0.updateGuild(var_11_0)
			arg_1_0.sendNotification(var_0_0.DONATE_UPDTAE)

		if var_11_2:
			arg_1_0.sendNotification(var_0_0.CAPITAL_UPDATED)

		if not var_11_2 and var_11_4 == var_11_5:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_donate_capital_toplimit"))

		if not var_11_3 and var_11_4 == var_11_5:
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_donate_techpoint_toplimit")))
	arg_1_0.on(62031, function(arg_12_0)
		local var_12_0 = arg_1_0.getData()

		if not var_12_0 or not var_12_0.IsCompletion():
			return

		local var_12_1 = {}

		for iter_12_0, iter_12_1 in ipairs(arg_12_0.donate_tasks):
			local var_12_2 = GuildDonateTask.New({
				id = iter_12_1
			})

			table.insert(var_12_1, var_12_2)

		if var_12_0:
			var_12_0.donateCount = 0

			var_12_0.updateDonateTasks(var_12_1)
			arg_1_0.updateGuild(var_12_0)
			arg_1_0.sendNotification(var_0_0.ON_DONATE_LIST_UPDATED)
		else
			local var_12_3 = arg_1_0.GetPublicGuild()

			if var_12_3:
				var_12_3.ResetDonateCnt()
				var_12_3.UpdateDonateTasks(var_12_1)
				arg_1_0.sendNotification(GAME.PUBLIC_GUILD_REFRESH_DONATE_LIST_DONE))
	arg_1_0.on(61021, function(arg_13_0)
		local var_13_0 = getProxy(PlayerProxy).getData()

		arg_1_0.refreshActivationEventTime = 0

		if arg_13_0.user_id != var_13_0.id:
			arg_1_0.sendNotification(var_0_0.GUILD_BATTLE_STARTED))

def var_0_0.AddPublicGuild(arg_14_0, arg_14_1):
	arg_14_0.publicGuild = arg_14_1

def var_0_0.GetPublicGuild(arg_15_0):
	return arg_15_0.publicGuild

def var_0_0.Init(arg_16_0):
	arg_16_0.data = None
	arg_16_0.chatMsgs = {}
	arg_16_0.bossRanks = {}
	arg_16_0.isGetChatMsg = False
	arg_16_0.refreshActivationEventTime = 0
	arg_16_0.nextRequestBattleRankTime = 0
	arg_16_0.refreshBossTime = 0
	arg_16_0.bossRankUpdateTime = 0
	arg_16_0.isFetchAssaultFleet = False
	arg_16_0.battleRanks = {}
	arg_16_0.ranks = {}
	arg_16_0.requests = None
	arg_16_0.rankUpdateTime = 0
	arg_16_0.requestReportTime = 0
	arg_16_0.newChatMsgCnt = 0
	arg_16_0.requestCount = 0
	arg_16_0.cdTime = {
		0,
		0
	}

def var_0_0.AddNewMsg(arg_17_0, arg_17_1):
	arg_17_0.newChatMsgCnt = arg_17_0.newChatMsgCnt + 1

	arg_17_0.addMsg(arg_17_1)
	arg_17_0.sendNotification(var_0_0.NEW_MSG_ADDED, arg_17_1)

def var_0_0.ResetRequestCount(arg_18_0):
	arg_18_0.requestCount = 0

def var_0_0.UpdatePosCdTime(arg_19_0, arg_19_1, arg_19_2):
	arg_19_0.cdTime[arg_19_1] = arg_19_2

def var_0_0.GetNextCanFormationTime(arg_20_0, arg_20_1):
	local var_20_0 = pg.guildset.operation_assault_team_cd.key_value

	return (arg_20_0.cdTime[arg_20_1] or 0) + var_20_0

def var_0_0.CanFormationPos(arg_21_0, arg_21_1):
	return arg_21_0.GetNextCanFormationTime(arg_21_1) <= pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.ClearNewChatMsgCnt(arg_22_0):
	arg_22_0.newChatMsgCnt = 0

def var_0_0.GetNewChatMsgCnt(arg_23_0):
	return arg_23_0.newChatMsgCnt

def var_0_0.setRequestList(arg_24_0, arg_24_1):
	arg_24_0.requests = arg_24_1

def var_0_0.addGuild(arg_25_0, arg_25_1):
	assert(isa(arg_25_1, Guild), "guild should instance of Guild")

	arg_25_0.data = arg_25_1

	arg_25_0.sendNotification(var_0_0.NEW_GUILD_ADDED, Clone(arg_25_1))

def var_0_0.updateGuild(arg_26_0, arg_26_1):
	assert(isa(arg_26_1, Guild), "guild should instance of Guild")

	arg_26_0.data = arg_26_1

	arg_26_0.sendNotification(var_0_0.GUILD_UPDATED, Clone(arg_26_1))

def var_0_0.exitGuild(arg_27_0):
	arg_27_0.Init()
	arg_27_0.sendNotification(var_0_0.EXIT_GUILD)
	pg.ShipFlagMgr.GetInstance().ClearShipsFlag("inGuildEvent")
	pg.ShipFlagMgr.GetInstance().ClearShipsFlag("inGuildBossEvent")

def var_0_0.getRequests(arg_28_0):
	return arg_28_0.requests

def var_0_0.getSortRequest(arg_29_0):
	if not arg_29_0.requests:
		return None

	local var_29_0 = {}

	for iter_29_0, iter_29_1 in pairs(arg_29_0.requests):
		table.insert(var_29_0, iter_29_1)

	return var_29_0

def var_0_0.deleteRequest(arg_30_0, arg_30_1):
	if not arg_30_0.requests:
		return

	arg_30_0.requests[arg_30_1] = None

	arg_30_0.sendNotification(var_0_0.REQUEST_DELETED, arg_30_1)

def var_0_0.addMsg(arg_31_0, arg_31_1):
	table.insert(arg_31_0.chatMsgs, arg_31_1)

	if #arg_31_0.chatMsgs > GuildConst.CHAT_LOG_MAX_COUNT:
		table.remove(arg_31_0.chatMsgs, 1)

def var_0_0.getChatMsgs(arg_32_0):
	return arg_32_0.chatMsgs

def var_0_0.GetMessagesByUniqueId(arg_33_0, arg_33_1):
	return _.select(arg_33_0.chatMsgs, function(arg_34_0)
		return arg_34_0.uniqueId == arg_33_1)

def var_0_0.UpdateMsg(arg_35_0, arg_35_1):
	for iter_35_0, iter_35_1 in ipairs(arg_35_0.chatMsgs):
		if iter_35_1.IsSame(arg_35_1.uniqueId):
			arg_35_0.data[iter_35_0] = arg_35_1

def var_0_0.ShouldFetchActivationEvent(arg_36_0):
	return pg.TimeMgr.GetInstance().GetServerTime() > arg_36_0.refreshActivationEventTime

def var_0_0.AddFetchActivationEventCDTime(arg_37_0):
	arg_37_0.refreshActivationEventTime = GuildConst.REFRESH_ACTIVATION_EVENT_TIME + pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.AddActivationEventTimer(arg_38_0, arg_38_1):
	return

def var_0_0.RemoveActivationEventTimer(arg_39_0):
	if arg_39_0.timer:
		arg_39_0.timer.Stop()

		arg_39_0.timer = None

def var_0_0.remove(arg_40_0):
	arg_40_0.RemoveActivationEventTimer()

def var_0_0.SetRank(arg_41_0, arg_41_1, arg_41_2):
	arg_41_0.ranks[arg_41_1] = arg_41_2
	arg_41_0["rankTimer" .. arg_41_1] = pg.TimeMgr.GetInstance().GetServerTime() + 1800

def var_0_0.GetRanks(arg_42_0):
	return arg_42_0.ranks

def var_0_0.ShouldRefreshRank(arg_43_0, arg_43_1):
	if not arg_43_0["rankTimer" .. arg_43_1] or pg.TimeMgr.GetInstance().GetServerTime() >= arg_43_0["rankTimer" .. arg_43_1]:
		return True

	return False

def var_0_0.SetReports(arg_44_0, arg_44_1):
	arg_44_0.reports = arg_44_1

def var_0_0.GetReports(arg_45_0):
	return arg_45_0.reports or {}

def var_0_0.GetReportById(arg_46_0, arg_46_1):
	return arg_46_0.reports[arg_46_1]

def var_0_0.AddReport(arg_47_0, arg_47_1):
	if not arg_47_0.reports:
		arg_47_0.reports = {}

	arg_47_0.reports[arg_47_1.id] = arg_47_1

def var_0_0.GetMaxReportId(arg_48_0):
	local var_48_0 = arg_48_0.GetReports()
	local var_48_1 = 0

	for iter_48_0, iter_48_1 in pairs(var_48_0):
		if var_48_1 < iter_48_1.id:
			var_48_1 = iter_48_1.id

	return var_48_1

def var_0_0.AnyRepoerCanGet(arg_49_0):
	return #arg_49_0.GetCanGetReports() > 0

def var_0_0.GetCanGetReports(arg_50_0):
	local var_50_0 = {}
	local var_50_1 = arg_50_0.GetReports()

	for iter_50_0, iter_50_1 in pairs(var_50_1):
		if iter_50_1.CanSubmit():
			table.insert(var_50_0, iter_50_1.id)

	return var_50_0

def var_0_0.ShouldRequestReport(arg_51_0):
	if not arg_51_0.requestReportTime:
		arg_51_0.requestReportTime = 0

	local function var_51_0()
		local var_52_0 = arg_51_0.getRawData().GetActiveEvent()

		if var_52_0 and var_52_0.GetMissionFinishCnt() > 0:
			return True

		return False

	local var_51_1 = pg.TimeMgr.GetInstance().GetServerTime()

	if not arg_51_0.reports and var_51_0() or var_51_1 > arg_51_0.requestReportTime:
		arg_51_0.requestReportTime = var_51_1 + GuildConst.REQUEST_REPORT_CD

		return True

	return False

def var_0_0.ShouldRequestForamtion(arg_53_0):
	if not arg_53_0.requestFormationTime:
		arg_53_0.requestFormationTime = 0

	local var_53_0 = pg.TimeMgr.GetInstance().GetServerTime()

	if var_53_0 > arg_53_0.requestFormationTime:
		arg_53_0.requestFormationTime = var_53_0 + GuildConst.REQUEST_FORMATION_CD

		return True

	return False

def var_0_0.GetRecommendShipsForMission(arg_54_0, arg_54_1):
	if arg_54_1.IsEliteType():
		return arg_54_0.GetRecommendShipsForEliteMission(arg_54_1)
	else
		local var_54_0 = {}
		local var_54_1 = getProxy(BayProxy).getRawData()
		local var_54_2 = {}

		for iter_54_0, iter_54_1 in pairs(var_54_1):
			table.insert(var_54_2, {
				id = iter_54_1.id,
				power = iter_54_1.getShipCombatPower(),
				nation = iter_54_1.getNation(),
				type = iter_54_1.getShipType(),
				level = iter_54_1.level,
				tagList = iter_54_1.getConfig("tag_list"),
				configId = iter_54_1.configId,
				attrs = iter_54_1.getProperties(),
				def isActivityNpc:()
					return iter_54_1.isActivityNpc()
			})

		local var_54_3 = arg_54_1.GetRecommendShipNation()
		local var_54_4 = arg_54_1.GetRecommendShipTypes()

		table.sort(var_54_2, CompareFuncs({
			function(arg_56_0)
				return table.contains(var_54_3, arg_56_0.nation) and 0 or 1,
			function(arg_57_0)
				return table.contains(var_54_4, arg_57_0.type) and 0 or 1,
			function(arg_58_0)
				return -arg_58_0.level,
			function(arg_59_0)
				return -arg_59_0.power
		}))

		for iter_54_2, iter_54_3 in ipairs(var_54_2):
			if GuildEventMediator.OnCheckMissionShip(arg_54_1.id, var_54_0, iter_54_3):
				table.insert(var_54_0, iter_54_3.id)

			if #var_54_0 == 4:
				break

		return var_54_0

def var_0_0.GetRecommendShipsForEliteMission(arg_60_0, arg_60_1):
	assert(arg_60_1.IsEliteType())

	local var_60_0 = {}
	local var_60_1 = getProxy(BayProxy).getRawData()
	local var_60_2 = {}
	local var_60_3 = {}
	local var_60_4 = {}

	for iter_60_0, iter_60_1 in pairs(var_60_1):
		local var_60_5 = {
			id = iter_60_1.id,
			power = iter_60_1.getShipCombatPower(),
			nation = iter_60_1.getNation(),
			type = iter_60_1.getShipType(),
			level = iter_60_1.level,
			tagList = iter_60_1.getConfig("tag_list"),
			configId = iter_60_1.configId,
			attrs = iter_60_1.getProperties(),
			def isActivityNpc:()
				return iter_60_1.isActivityNpc()
		}

		if arg_60_1.SameSquadron(var_60_5):
			table.insert(var_60_3, var_60_5)
		else
			table.insert(var_60_4, var_60_5)

	local function var_60_6(arg_62_0)
		if arg_62_0 and not table.contains(var_60_0, arg_62_0.id) and GuildEventMediator.OnCheckMissionShip(arg_60_1.id, var_60_0, arg_62_0):
			table.insert(var_60_0, arg_62_0.id)

	local var_60_7 = arg_60_1.GetEffectAttr()
	local var_60_8 = CompareFuncs({
		function(arg_63_0)
			return arg_60_1.MatchAttr(arg_63_0) and 0 or 1,
		function(arg_64_0)
			return arg_60_1.MatchNation(arg_64_0) and 0 or 1,
		function(arg_65_0)
			return arg_60_1.MatchShipType(arg_65_0) and 0 or 1,
		function(arg_66_0)
			return -(arg_66_0.attrs[var_60_7] or 0),
		function(arg_67_0)
			return -arg_67_0.level,
		function(arg_68_0)
			return -arg_68_0.power
	})
	local var_60_9 = arg_60_1.GetSquadronTargetCnt()

	if #var_60_3 > 0 and var_60_9 > 0:
		table.sort(var_60_3, var_60_8)

		for iter_60_2 = 1, var_60_9:
			var_60_6(var_60_3[iter_60_2])

	if #var_60_0 < 4 and #var_60_4 > 0:
		table.sort(var_60_4, var_60_8)

		for iter_60_3 = 1, #var_60_4:
			if #var_60_0 == 4:
				break

			var_60_6(var_60_4[iter_60_3])

	if #var_60_0 < 4 and var_60_9 > 0 and var_60_9 < #var_60_3:
		for iter_60_4 = var_60_9 + 1, #var_60_3:
			if #var_60_0 == 4:
				break

			var_60_6(var_60_3[iter_60_4])

	return var_60_0

def var_0_0.ShouldShowApplyTip(arg_69_0):
	if arg_69_0.data and GuildMember.IsAdministrator(arg_69_0.data.getSelfDuty()):
		if not arg_69_0.requests:
			return arg_69_0.requestCount > 0

		return table.getCount(arg_69_0.requests) + arg_69_0.requestCount > 0

	return False

def var_0_0.ShouldShowBattleTip(arg_70_0):
	local var_70_0 = arg_70_0.getData()
	local var_70_1 = False

	local function var_70_2(arg_71_0)
		if arg_71_0 and arg_71_0.IsParticipant():
			local var_71_0 = arg_71_0.GetBossMission()

			return var_71_0 and var_71_0.IsActive() and var_71_0.CanEnterBattle()

		return False

	local function var_70_3()
		for iter_72_0, iter_72_1 in ipairs(pg.guild_operation_template.all):
			local var_72_0 = pg.guild_operation_template[iter_72_1]

			if var_70_0.level >= var_72_0.unlock_guild_level and var_70_0.getCapital() >= var_72_0.consume:
				return True

		return False

	if var_70_0:
		local var_70_4 = var_70_0.GetActiveEvent()
		local var_70_5 = GuildMember.IsAdministrator(var_70_0.getSelfDuty()) and var_70_0.ShouldTipActiveEvent()

		var_70_1 = arg_70_0.ShouldShowMainTip() or not var_70_4 and var_70_5 and var_70_3() or var_70_4 and not arg_70_0.GetBattleBtnRecord()

		if var_70_4 and not var_70_1:
			local var_70_6 = var_70_4.IsParticipant()

			var_70_1 = var_70_6 and var_70_4.AnyMissionCanFormation() or var_70_2(var_70_4) or not var_70_6 and not var_70_4.IsLimitedJoin()

	return var_70_1

def var_0_0.SetBattleBtnRecord(arg_73_0):
	if not arg_73_0.GetBattleBtnRecord():
		local var_73_0 = arg_73_0.getRawData()

		if var_73_0 and var_73_0.GetActiveEvent():
			local var_73_1 = getProxy(PlayerProxy).getRawData()

			PlayerPrefs.SetInt("guild_battle_btn_flag" .. var_73_1.id, 1)
			PlayerPrefs.Save()
			arg_73_0.sendNotification(var_0_0.BATTLE_BTN_FLAG_CHANGE)

def var_0_0.GetBattleBtnRecord(arg_74_0):
	local var_74_0 = getProxy(PlayerProxy).getRawData()

	return PlayerPrefs.GetInt("guild_battle_btn_flag" .. var_74_0.id, 0) > 0

def var_0_0.ShouldShowMainTip(arg_75_0):
	local function var_75_0()
		local var_76_0 = getProxy(PlayerProxy).getRawData().id

		return arg_75_0.data.getMemberById(var_76_0).IsRecruit()

	return _.any(arg_75_0.reports or {}, function(arg_77_0)
		return arg_77_0.CanSubmit()) and not var_75_0()

def var_0_0.ShouldShowTip(arg_78_0):
	local var_78_0 = {}
	local var_78_1 = arg_78_0.getData()

	if var_78_1:
		table.insert(var_78_0, var_78_1.ShouldShowDonateTip())
		table.insert(var_78_0, arg_78_0.ShouldShowApplyTip())
		table.insert(var_78_0, var_78_1.ShouldWeeklyTaskTip())
		table.insert(var_78_0, var_78_1.ShouldShowSupplyTip())
		table.insert(var_78_0, var_78_1.ShouldShowTechTip())

		if not LOCK_GUILD_BATTLE:
			table.insert(var_78_0, arg_78_0.ShouldShowBattleTip())

	return #var_78_0 > 0 and _.any(var_78_0, function(arg_79_0)
		return arg_79_0 == True)

def var_0_0.SetRefreshBossTime(arg_80_0, arg_80_1):
	arg_80_0.refreshBossTime = arg_80_1 + GuildConst.REFRESH_BOSS_TIME

def var_0_0.ShouldRefreshBoss(arg_81_0):
	local var_81_0 = arg_81_0.getRawData().GetActiveEvent()

	return var_81_0 and not var_81_0.IsExpired() and pg.TimeMgr.GetInstance().GetServerTime() >= arg_81_0.refreshBossTime

def var_0_0.ResetRefreshBossTime(arg_82_0):
	arg_82_0.refreshBossTime = 0

def var_0_0.ShouldRefreshBossRank(arg_83_0):
	local var_83_0 = arg_83_0.getRawData().GetActiveEvent()
	local var_83_1 = pg.TimeMgr.GetInstance().GetServerTime()

	return var_83_0 and var_83_1 - arg_83_0.bossRankUpdateTime >= GuildConst.REFRESH_MISSION_BOSS_RANK_TIME

def var_0_0.UpdateBossRank(arg_84_0, arg_84_1):
	arg_84_0.bossRanks = arg_84_1

def var_0_0.GetBossRank(arg_85_0):
	return arg_85_0.bossRanks

def var_0_0.ResetBossRankTime(arg_86_0):
	arg_86_0.rankUpdateTime = 0

def var_0_0.UpdateBossRankRefreshTime(arg_87_0, arg_87_1):
	arg_87_0.rankUpdateTime = arg_87_1

def var_0_0.GetAdditionGuild(arg_88_0):
	if arg_88_0.data == None:
		return arg_88_0.publicGuild
	else
		return arg_88_0.data

def var_0_0.SetReportRankList(arg_89_0, arg_89_1, arg_89_2):
	if not arg_89_0.reportRankList:
		arg_89_0.reportRankList = {}

	arg_89_0.reportRankList[arg_89_1] = arg_89_2

def var_0_0.GetReportRankList(arg_90_0, arg_90_1):
	if arg_90_0.reportRankList:
		return arg_90_0.reportRankList[arg_90_1]

	return None

return var_0_0
