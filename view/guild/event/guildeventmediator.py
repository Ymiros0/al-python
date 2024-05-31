local var_0_0 = class("GuildEventMediator", import("...base.ContextMediator"))

var_0_0.ON_ACTIVE_EVENT = "GuildEventMediator.ON_ACTIVE_EVENT"
var_0_0.ON_OPEN_REPORT = "GuildEventMediator.ON_OPEN_REPORT"
var_0_0.ON_GET_FORMATION = "GuildEventMediator.ON_GET_FORMATION"
var_0_0.UPDATE_FORMATION = "GuildEventMediator.UPDATE_FORMATION"
var_0_0.ON_SELECT_SHIP = "GuildEventMediator.ON_SELECT_SHIP"
var_0_0.ON_SELECT_MISSION_SHIP = "GuildEventMediator.ON_SELECT_MISSION_SHIP"
var_0_0.REFRESH_MISSION = "GuildEventMediator.REFRESH_MISSION"
var_0_0.JOIN_MISSION = "GuildEventMediator.JOIN_MISSION"
var_0_0.ON_GET_BOSS_INFO = "GuildEventMediator.ON_GET_BOSS_INFO"
var_0_0.ON_REFRESH_BOSS_RANK = "GuildEventMediator.ON_REFRESH_BOSS_RANK"
var_0_0.ON_UPDATE_NODE_ANIM_FLAG = "GuildEventMediator.ON_UPDATE_NODE_ANIM_FLAG"
var_0_0.ON_SELECT_BOSS_SHIP = "GuildEventMediator.ON_SELECT_BOSS_SHIP"
var_0_0.ON_UPDATE_BOSS_FLEET = "GuildEventMediator.ON_UPDATE_BOSS_FLEET"
var_0_0.ON_RECOMM_BOSS_BATTLE_SHIPS = "GuildEventMediator.ON_RECOMM_BOSS_BATTLE_SHIPS"
var_0_0.ON_GET_ALL_ASSULT_FLEET = "GuildEventMediator.ON_GET_ALL_ASSULT_FLEET"
var_0_0.ON_SELECT_COMMANDER = "GuildEventMediator.ON_SELECT_COMMANDER"
var_0_0.FORCE_REFRESH_MISSION = "GuildEventMediator.FORCE_REFRESH_MISSION"
var_0_0.ON_SAVE_FORMATION = "GuildEventMediator.ON_SAVE_FORMATION"
var_0_0.ON_JOIN_EVENT = "GuildEventMediator.ON_JOIN_EVENT"
var_0_0.ON_RECOMM_ASSULT_SHIP = "GuildEventMediator.ON_RECOMM_ASSULT_SHIP"
var_0_0.REFRESH_RECOMMAND_SHIPS = "GuildEventMediator.REFRESH_RECOMMAND_SHIPS"
var_0_0.ON_CLEAR_BOSS_FLEET_INVAILD_SHIP = "GuildEventMediator.ON_CLEAR_BOSS_FLEET_INVAILD_SHIP"
var_0_0.ON_CMD_SKILL = "GuildEventMediator.ON_CMD_SKILL"
var_0_0.COMMANDER_FORMATION_OP = "GuildEventMediator.COMMANDER_FORMATION_OP"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.COMMANDER_FORMATION_OP, function(arg_2_0, arg_2_1)
		arg_1_0.OnComanderOP(arg_2_1))
	arg_1_0.bind(var_0_0.ON_CMD_SKILL, function(arg_3_0, arg_3_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = CommanderSkillMediator,
			viewComponent = CommanderSkillLayer,
			data = {
				skill = arg_3_1
			}
		})))
	arg_1_0.bind(var_0_0.REFRESH_RECOMMAND_SHIPS, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.REFRESH_ALL_ASSULT_SHIP_RECOMMAND_STATE, {
			callback = arg_4_1
		}))
	arg_1_0.bind(var_0_0.ON_RECOMM_ASSULT_SHIP, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0.sendNotification(GAME.GUILD_RECOMMAND_ASSULT_SHIP, {
			shipId = arg_5_1,
			cmd = arg_5_2
		}))
	arg_1_0.bind(var_0_0.ON_JOIN_EVENT, function()
		arg_1_0.sendNotification(GAME.ON_GUILD_JOIN_EVENT))
	arg_1_0.bind(var_0_0.ON_SELECT_COMMANDER, function(arg_7_0, arg_7_1, arg_7_2, arg_7_3)
		arg_1_0.SelectBossBattleCommander(arg_7_1, arg_7_2, arg_7_3))
	arg_1_0.bind(var_0_0.ON_GET_ALL_ASSULT_FLEET, function(arg_8_0, arg_8_1)
		arg_1_0.sendNotification(GAME.GUILD_GET_ASSAULT_FLEET, {
			callback = arg_8_1
		}))
	arg_1_0.bind(var_0_0.ON_RECOMM_BOSS_BATTLE_SHIPS, function(arg_9_0, arg_9_1)
		arg_1_0.sendNotification(GAME.GUILD_GET_ASSAULT_FLEET, {
			def callback:()
				arg_1_0.RecommShipsForBossBattle(arg_9_1)
		}))
	arg_1_0.bind(var_0_0.ON_SAVE_FORMATION, function(arg_11_0, arg_11_1)
		arg_1_0.sendNotification(GAME.GUILD_UPDATE_BOSS_FORMATION, {
			editFleet = arg_1_0.contextData.editBossFleet,
			callback = arg_11_1
		}))
	arg_1_0.bind(var_0_0.ON_CLEAR_BOSS_FLEET_INVAILD_SHIP, function(arg_12_0)
		arg_1_0.sendNotification(GAME.GUILD_UPDATE_BOSS_FORMATION, {
			force = True,
			editFleet = arg_1_0.contextData.editBossFleet
		}))
	arg_1_0.bind(var_0_0.ON_UPDATE_BOSS_FLEET, function(arg_13_0)
		if not arg_1_0.contextData.editBossFleet:
			arg_1_0.StartBossBattle()
		else
			arg_1_0.viewComponent.emit(var_0_0.ON_SAVE_FORMATION, function()
				arg_1_0.StartBossBattle()))
	arg_1_0.bind(var_0_0.ON_SELECT_BOSS_SHIP, function(arg_15_0, arg_15_1, arg_15_2, arg_15_3)
		arg_1_0.sendNotification(GAME.GUILD_GET_ASSAULT_FLEET, {
			def callback:()
				arg_1_0.SelectBossBattleShip(arg_15_1, arg_15_2, arg_15_3)
		}))
	arg_1_0.bind(var_0_0.ON_UPDATE_NODE_ANIM_FLAG, function(arg_17_0, arg_17_1, arg_17_2)
		arg_1_0.sendNotification(GAME.GUILD_UPDATE_NODE_ANIM_FLAG, {
			id = arg_17_1,
			position = arg_17_2
		}))
	arg_1_0.bind(var_0_0.ON_REFRESH_BOSS_RANK, function(arg_18_0)
		arg_1_0.sendNotification(GAME.GET_GUILD_BOSS_RANK, {}))
	arg_1_0.bind(var_0_0.ON_GET_BOSS_INFO, function(arg_19_0)
		arg_1_0.sendNotification(GAME.GUILD_GET_BOSS_INFO))
	arg_1_0.bind(var_0_0.JOIN_MISSION, function(arg_20_0, arg_20_1, arg_20_2)
		arg_1_0.sendNotification(GAME.GUILD_JOIN_MISSION, {
			id = arg_20_1,
			shipIds = arg_20_2
		}))
	arg_1_0.bind(var_0_0.ON_SELECT_MISSION_SHIP, function(arg_21_0, arg_21_1, arg_21_2, arg_21_3)
		arg_1_0.viewComponent.emit(var_0_0.ON_GET_FORMATION, function()
			arg_1_0.OnSelectMissionShips(arg_21_1, arg_21_2, arg_21_3)))
	arg_1_0.bind(var_0_0.REFRESH_MISSION, function(arg_23_0, arg_23_1, arg_23_2)
		arg_1_0.sendNotification(GAME.GUILD_REFRESH_MISSION, {
			force = False,
			id = arg_23_1,
			callback = arg_23_2
		}))
	arg_1_0.bind(var_0_0.FORCE_REFRESH_MISSION, function(arg_24_0, arg_24_1, arg_24_2)
		arg_1_0.sendNotification(GAME.GUILD_REFRESH_MISSION, {
			force = True,
			id = arg_24_1,
			callback = arg_24_2
		}))
	arg_1_0.bind(var_0_0.ON_SELECT_SHIP, function(arg_25_0, arg_25_1, arg_25_2, arg_25_3)
		arg_1_0.OnSelectShips(arg_25_1, arg_25_2, arg_25_3))
	arg_1_0.bind(var_0_0.ON_GET_FORMATION, function(arg_26_0, arg_26_1)
		local var_26_0 = getProxy(GuildProxy).getRawData().GetActiveEvent()
		local var_26_1 = {}

		if var_26_0:
			table.insert(var_26_1, function(arg_27_0)
				arg_1_0.viewComponent.emit(var_0_0.ON_GET_ALL_ASSULT_FLEET, arg_27_0))

		if not getProxy(GuildProxy).isFetchAssaultFleet:
			table.insert(var_26_1, function(arg_28_0)
				arg_1_0.sendNotification(GAME.GUILD_GET_MY_ASSAULT_FLEET, {
					callback = arg_28_0
				}))

		seriesAsync(var_26_1, arg_26_1))
	arg_1_0.bind(var_0_0.UPDATE_FORMATION, function(arg_29_0)
		if not arg_1_0.contextData.editFleet:
			return

		arg_1_0.sendNotification(GAME.GUILD_UPDATE_MY_ASSAULT_FLEET, {
			fleet = arg_1_0.contextData.editFleet
		}))
	arg_1_0.bind(var_0_0.ON_ACTIVE_EVENT, function(arg_30_0, arg_30_1)
		arg_1_0.sendNotification(GAME.GUILD_ACTIVE_EVENT, {
			eventId = arg_30_1
		}))
	arg_1_0.bind(var_0_0.ON_OPEN_REPORT, function(arg_31_0)
		arg_1_0.sendNotification(GAME.GUILD_OPEN_EVENT_REPORT))
	arg_1_0.viewComponent.SetPlayer(getProxy(PlayerProxy).getRawData())

	local var_1_0 = getProxy(GuildProxy)

	arg_1_0.viewComponent.SetGuild(var_1_0.getData())

def var_0_0.StartBossBattle(arg_32_0):
	local var_32_0 = getProxy(GuildProxy).getRawData().GetActiveEvent()

	if not var_32_0 or var_32_0 and var_32_0.IsExpired():
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_battle_is_end"))

		return

	local var_32_1 = var_32_0.GetBossMission()

	if not var_32_1:
		return

	local var_32_2 = var_32_1.GetMainFleet()
	local var_32_3, var_32_4 = var_32_2.IsLegal()

	if not var_32_3:
		pg.TipsMgr.GetInstance().ShowTips(var_32_4)

		return

	local var_32_5, var_32_6 = var_32_1.GetSubFleet().IsLegal()

	if not var_32_5:
		pg.TipsMgr.GetInstance().ShowTips(var_32_6)

		return

	local var_32_7 = var_32_2.GetDownloadResShips()
	local var_32_8 = {}

	for iter_32_0, iter_32_1 in ipairs(var_32_7):
		PaintingGroupConst.AddPaintingNameWithFilteMap(var_32_8, iter_32_1)

	local function var_32_9()
		arg_32_0.sendNotification(GAME.BEGIN_STAGE, {
			system = SYSTEM_GUILD
		})

	PaintingGroupConst.PaintingDownload({
		isShowBox = True,
		paintingNameList = var_32_8,
		finishFunc = var_32_9
	})

def var_0_0.SelectBossBattleCommander(arg_34_0, arg_34_1, arg_34_2, arg_34_3):
	if not arg_34_0.contextData.editBossFleet:
		arg_34_0.contextData.editBossFleet = {}

	local var_34_0 = getProxy(GuildProxy).getData().GetActiveEvent()

	if not var_34_0:
		return

	local var_34_1 = var_34_0.GetBossMission()

	if not arg_34_0.contextData.editBossFleet[arg_34_1]:
		arg_34_0.contextData.editBossFleet[arg_34_1] = Clone(var_34_1.GetFleetByIndex(arg_34_1))

	local var_34_2 = arg_34_0.contextData.editBossFleet[arg_34_1]
	local var_34_3 = var_34_2.getCommanders()
	local var_34_4 = {}

	if arg_34_3:
		table.insert(var_34_4, arg_34_3.id)

	pg.m02.sendNotification(GAME.GO_SCENE, SCENE.COMMANDERCAT, {
		maxCount = 1,
		mode = CommanderCatScene.MODE_SELECT,
		fleetType = CommanderCatScene.FLEET_TYPE_GUILDBOSS,
		activeCommander = arg_34_3,
		ignoredIds = var_34_4,
		fleets = arg_34_0.contextData.editBossFleet,
		def onCommander:(arg_35_0)
			return True,
		def onSelected:(arg_36_0, arg_36_1)
			arg_34_0.OnDockSelectCommander(True, var_34_2, arg_34_2, var_34_1, arg_36_0, arg_36_1),
		def onQuit:(arg_37_0)
			var_34_2.RemoveCommander(arg_34_2)
			arg_37_0()
	})

def var_0_0.OnDockSelectCommander(arg_38_0, arg_38_1, arg_38_2, arg_38_3, arg_38_4, arg_38_5, arg_38_6):
	local var_38_0 = arg_38_5[1]
	local var_38_1 = getProxy(CommanderProxy).getCommanderById(var_38_0)

	if not var_38_1:
		arg_38_6()

		return

	local var_38_2 = {}
	local var_38_3 = {}
	local var_38_4 = arg_38_0.contextData.editBossFleet[GuildBossMission.SUB_FLEET_ID] or arg_38_4.GetSubFleet()
	local var_38_5 = arg_38_0.contextData.editBossFleet[GuildBossMission.MAIN_FLEET_ID] or arg_38_4.GetMainFleet()
	local var_38_6 = arg_38_2.IsMainFleet()
	local var_38_7 = var_38_6 and var_38_5 or var_38_4
	local var_38_8 = var_38_7.getCommanders()

	if arg_38_1:
		for iter_38_0, iter_38_1 in pairs(var_38_8):
			if arg_38_3 != iter_38_0 and iter_38_1.isSameGroup(var_38_1.groupId):
				pg.TipsMgr.GetInstance().ShowTips(i18n("commander_can_not_select_same_group"))

				return

	local var_38_9 = var_38_6 and var_38_4 or var_38_5
	local var_38_10 = var_38_9.getCommanders()

	for iter_38_2, iter_38_3 in pairs(var_38_10):
		if iter_38_3.id == var_38_1.id:
			arg_38_0.SwopCommanderForBossBattle(arg_38_4, var_38_1, arg_38_3, iter_38_2, var_38_7, var_38_9, arg_38_6)

			return

	arg_38_2.AddCommander(arg_38_3, var_38_1)
	arg_38_6()

def var_0_0.SwopCommanderForBossBattle(arg_39_0, arg_39_1, arg_39_2, arg_39_3, arg_39_4, arg_39_5, arg_39_6, arg_39_7):
	if not arg_39_0.contextData.editBossFleet[arg_39_6.id]:
		arg_39_0.contextData.editBossFleet[arg_39_6.id] = Clone(arg_39_1.GetFleetByIndex(arg_39_6.id))
		arg_39_6 = arg_39_0.contextData.editBossFleet[arg_39_6.id]

	local var_39_0 = arg_39_4 == 1 and i18n("commander_main_pos") or i18n("commander_assistant_pos")
	local var_39_1 = arg_39_5.GetName()

	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		content = i18n("comander_repalce_tip", var_39_1, var_39_0),
		def onYes:()
			arg_39_6.RemoveCommander(arg_39_4)
			arg_39_5.AddCommander(arg_39_3, arg_39_2)

			if arg_39_7:
				arg_39_7()
	})

def var_0_0.RecommShipsForBossBattle(arg_41_0, arg_41_1):
	if not arg_41_0.contextData.editBossFleet:
		arg_41_0.contextData.editBossFleet = {}

	local var_41_0 = {}
	local var_41_1 = {}
	local var_41_2 = {}
	local var_41_3 = getProxy(GuildProxy).getData()
	local var_41_4 = getProxy(PlayerProxy).getRawData()
	local var_41_5 = var_41_3.GetActiveEvent()

	if not var_41_5:
		return

	local var_41_6 = var_41_5.GetBossMission()

	if not arg_41_0.contextData.editBossFleet[arg_41_1]:
		arg_41_0.contextData.editBossFleet[arg_41_1] = Clone(var_41_6.GetFleetByIndex(arg_41_1))

	local var_41_7 = arg_41_0.contextData.editBossFleet[arg_41_1]

	var_41_7.RemoveAll()

	local function var_41_8(arg_42_0, arg_42_1)
		if arg_42_0 == TeamType.Main:
			table.insert(var_41_0, arg_42_1)
		elif arg_42_0 == TeamType.Vanguard:
			table.insert(var_41_1, arg_42_1)
		elif arg_42_0 == TeamType.Submarine:
			table.insert(var_41_2, arg_42_1)

	local var_41_9 = getProxy(BayProxy).getData()

	for iter_41_0, iter_41_1 in pairs(var_41_9):
		if not pg.ShipFlagMgr.GetInstance().GetShipFlag(iter_41_1.id, "inEvent") and not iter_41_1.isActivityNpc():
			iter_41_1.id = GuildAssaultFleet.GetVirtualId(var_41_4.id, iter_41_1.id)

			local var_41_10 = iter_41_1.getShipCombatPower()

			var_41_8(iter_41_1.getTeamType(), {
				power = var_41_10,
				id = iter_41_1.id
			})

	local var_41_11 = 0
	local var_41_12 = 0
	local var_41_13 = 0

	local function var_41_14(arg_43_0, arg_43_1)
		local var_43_0 = GuildAssaultFleet.GetRealId(arg_43_0)
		local var_43_1 = var_41_9[var_43_0]

		if not var_41_7.ExistSameKindShip(var_43_1):
			local var_43_2 = GuildAssaultFleet.GetUserId(arg_43_0)

			var_41_7.AddUserShip(var_43_2, var_43_0)

			if arg_43_1 == TeamType.Main:
				var_41_11 = var_41_11 + 1

			if arg_43_1 == TeamType.Vanguard:
				var_41_12 = var_41_12 + 1

			if arg_43_1 == TeamType.Submarine:
				var_41_13 = var_41_13 + 1

	if var_41_7.IsMainFleet():
		table.sort(var_41_0, function(arg_44_0, arg_44_1)
			return arg_44_0.power > arg_44_1.power)
		table.sort(var_41_1, function(arg_45_0, arg_45_1)
			return arg_45_0.power > arg_45_1.power)

		for iter_41_2 = 1, #var_41_0:
			if var_41_11 == 3:
				break

			var_41_14(var_41_0[iter_41_2].id, TeamType.Main)

		for iter_41_3 = 1, #var_41_1:
			if var_41_12 == 3:
				break

			var_41_14(var_41_1[iter_41_3].id, TeamType.Vanguard)
	else
		table.sort(var_41_2, function(arg_46_0, arg_46_1)
			return arg_46_0.power > arg_46_1.power)

		for iter_41_4 = 1, #var_41_2:
			if var_41_13 == 3:
				break

			var_41_14(var_41_2[iter_41_4].id, TeamType.Submarine)

	local var_41_15 = arg_41_0.viewComponent.missBossForamtionPage

	if var_41_15 and var_41_15.GetLoaded():
		var_41_15.UpdateFleet(arg_41_1)

def var_0_0.SelectBossBattleShip(arg_47_0, arg_47_1, arg_47_2, arg_47_3):
	if not arg_47_0.contextData.editBossFleet:
		arg_47_0.contextData.editBossFleet = {}

	local var_47_0 = {}
	local var_47_1 = getProxy(GuildProxy).getData()
	local var_47_2 = var_47_1.GetActiveEvent()

	if not var_47_2:
		return

	local var_47_3 = var_47_2.GetBossMission()
	local var_47_4 = var_47_3.GetFleetByIndex(arg_47_2)

	assert(var_47_4, arg_47_2)

	local var_47_5

	if not arg_47_0.contextData.editBossFleet[arg_47_2]:
		var_47_5 = Clone(var_47_4)
	else
		var_47_5 = Clone(arg_47_0.contextData.editBossFleet[arg_47_2])

	local var_47_6

	if arg_47_3:
		local var_47_7 = arg_47_3.member.id
		local var_47_8 = GuildAssaultFleet.GetRealId(arg_47_3.ship.id)

		var_47_6 = var_47_5.RemoveUserShip(var_47_7, var_47_8)

	local var_47_9 = getProxy(PlayerProxy).getRawData()
	local var_47_10 = 0

	if var_47_5.IsMainFleet():
		var_47_10 = (arg_47_0.contextData.editBossFleet[GuildBossMission.SUB_FLEET_ID] or var_47_3.GetFleetByIndex(GuildBossMission.SUB_FLEET_ID)).GetOtherMemberShipCnt(var_47_9.id)
	else
		var_47_10 = (arg_47_0.contextData.editBossFleet[GuildBossMission.MAIN_FLEET_ID] or var_47_3.GetFleetByIndex(GuildBossMission.MAIN_FLEET_ID)).GetOtherMemberShipCnt(var_47_9.id)

	local var_47_11

	for iter_47_0, iter_47_1 in pairs(var_47_1.member):
		local var_47_12 = iter_47_1.GetAssaultFleet()

		if var_47_9.id != iter_47_1.id:
			local var_47_13 = var_47_12.GetShipList()

			for iter_47_2, iter_47_3 in pairs(var_47_13):
				if iter_47_3.getTeamType() == arg_47_1:
					iter_47_3.user = iter_47_1

					table.insert(var_47_0, iter_47_3)
		else
			var_47_11 = var_47_12

	local var_47_14 = getProxy(BayProxy).getData()

	for iter_47_4, iter_47_5 in pairs(var_47_14):
		iter_47_5.user = var_47_9

		local var_47_15 = var_47_11.GetShipByRealId(var_47_9.id, iter_47_5.id)

		iter_47_5.id = GuildAssaultFleet.GetVirtualId(var_47_9.id, iter_47_5.id)

		if var_47_15:
			iter_47_5.guildRecommand = var_47_15.guildRecommand

		table.insert(var_47_0, GuildAssaultShip.ConverteFromShip(iter_47_5))

	local var_47_16 = {}

	if arg_47_3:
		table.insert(var_47_16, arg_47_3.ship.id)

	for iter_47_6, iter_47_7 in ipairs(var_47_5.GetShipIds()):
		if iter_47_7:
			table.insert(var_47_16, GuildAssaultFleet.GetVirtualId(iter_47_7.uid, iter_47_7.id))

	local var_47_17 = var_47_5.GetShips()

	arg_47_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
		selectedMin = 1,
		selectedMax = 1,
		quitTeam = arg_47_3,
		ignoredIds = var_47_16,
		teamFilter = arg_47_1,
		shipVOs = var_47_0,
		mode = DockyardScene.MODE_GUILD_BOSS,
		hideTagFlags = ShipStatus.TAG_HIDE_CHALLENGE,
		def onShip:(arg_48_0, arg_48_1, arg_48_2)
			if var_47_5.GetOtherMemberShipCnt(var_47_9.id) + var_47_10 >= 3 and arg_48_0.user.id != var_47_9.id:
				return False, i18n("guild_boss_formation_1")

			if arg_48_0.user.id != var_47_9.id and var_47_5.ExistUserShip(arg_48_0.user.id):
				return False, i18n("guild_boss_formation_2")

			if _.any(var_47_17, function(arg_49_0)
				return arg_49_0.ship.isSameKind(arg_48_0)):
				return False, i18n("guild_boss_formation_3")

			local var_48_0 = GuildAssaultFleet.GetRealId(arg_48_0.id)

			if pg.ShipFlagMgr.GetInstance().GetShipFlag(var_48_0, "inEvent"):
				return False, i18n("word_shipState_collect")

			if arg_48_0.isActivityNpc():
				return False, i18n("common_npc_formation_tip")

			return True,
		def onSelected:(arg_50_0, arg_50_1)
			local var_50_0 = arg_50_0[1]

			if var_50_0:
				local var_50_1 = GuildAssaultFleet.GetRealId(var_50_0)
				local var_50_2 = GuildAssaultFleet.GetUserId(var_50_0)

				var_47_5.AddUserShip(var_50_2, var_50_1, var_47_6)

			arg_47_0.contextData.editBossFleet[arg_47_2] = var_47_5
	})

def var_0_0.OnSelectShips(arg_51_0, arg_51_1, arg_51_2, arg_51_3):
	local var_51_0 = arg_51_3.GetShipList()

	arg_51_0.contextData.editFleet = Clone(arg_51_3)

	local var_51_1 = getProxy(BayProxy).getData()
	local var_51_2 = {}

	if arg_51_2:
		table.insert(var_51_2, arg_51_2.id)

	arg_51_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
		selectedMin = 1,
		selectedMax = 1,
		ignoredIds = var_51_2,
		def onShip:(arg_52_0, arg_52_1, arg_52_2)
			for iter_52_0, iter_52_1 in pairs(var_51_0):
				local var_52_0 = GuildAssaultFleet.GetRealId(iter_52_1.id)

				if iter_52_0 != arg_51_1 and var_52_0 == arg_52_0.id:
					return False, i18n("guild_fleet_exist_same_kind_ship")

			if arg_52_0.isActivityNpc():
				return False, i18n("common_npc_formation_tip")

			return True,
		def onSelected:(arg_53_0, arg_53_1)
			local var_53_0 = arg_53_0[1]
			local var_53_1 = var_51_1[var_53_0]

			arg_51_0.contextData.editFleet.InsertBayShip(arg_51_1, var_53_1)
	})

def var_0_0.OnCheckMissionShip(arg_54_0, arg_54_1, arg_54_2):
	local var_54_0 = getProxy(GuildProxy).getData()
	local var_54_1 = getProxy(PlayerProxy).getRawData().id
	local var_54_2 = var_54_0.getMemberById(var_54_1)
	local var_54_3 = var_54_2.GetAssaultFleet()
	local var_54_4 = var_54_2.GetExternalAssaultFleet()
	local var_54_5 = var_54_0.GetActiveEvent()
	local var_54_6 = var_54_5.GetJoinShips()
	local var_54_7 = getProxy(BayProxy).getData()
	local var_54_8 = _.map(arg_54_1, function(arg_55_0)
		return var_54_7[arg_55_0])

	if arg_54_2.isActivityNpc():
		return False, i18n("common_npc_formation_tip")

	local var_54_9 = var_54_5.GetMissionById(arg_54_0).GetMyShips()

	if _.any(var_54_9, function(arg_56_0)
		return var_54_7[arg_56_0] and var_54_7[arg_56_0].isSameKind(arg_54_2)):
		return False, i18n("guild_event_exist_same_kind_ship")

	if _.any(var_54_8, function(arg_57_0)
		return arg_57_0.isSameKind(arg_54_2)):
		return False, i18n("guild_event_exist_same_kind_ship")

	local var_54_10 = GuildAssaultFleet.GetVirtualId(var_54_1, arg_54_2.id)

	if var_54_3.ExistShip(var_54_10):
		return False, i18n("guild_event_exist_assult_ship")

	if var_54_4.ExistShip(var_54_10):
		return False, i18n("guild_event_exist_assult_ship")

	if _.any(var_54_6, function(arg_58_0)
		return arg_54_2.id == arg_58_0):
		return False, i18n("guidl_event_ship_in_event")

	return True

def var_0_0.OnSelectMissionShips(arg_59_0, arg_59_1, arg_59_2, arg_59_3):
	if not arg_59_0.contextData.missionShips:
		arg_59_0.contextData.missionShips = Clone(arg_59_3)

	local var_59_0 = getProxy(GuildProxy).getData()
	local var_59_1 = getProxy(PlayerProxy).getRawData().id
	local var_59_2 = var_59_0.getMemberById(var_59_1).GetAssaultFleet()
	local var_59_3 = _.map(var_59_2.GetShipIds(), function(arg_60_0)
		return GuildAssaultFleet.GetRealId(arg_60_0))

	_.each(arg_59_3, function(arg_61_0)
		table.insert(var_59_3, arg_61_0))

	local var_59_4 = var_59_0.GetActiveEvent().GetJoinShips()

	_.each(var_59_4, function(arg_62_0)
		table.insert(var_59_3, arg_62_0))
	arg_59_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
		selectedMin = 1,
		selectedMax = 1,
		quitTeam = arg_59_3[arg_59_2],
		ignoredIds = var_59_3,
		def onShip:(arg_63_0)
			return var_0_0.OnCheckMissionShip(arg_59_1, arg_59_3, arg_63_0),
		def onSelected:(arg_64_0, arg_64_1)
			if arg_59_3[arg_59_2]:
				for iter_64_0, iter_64_1 in ipairs(arg_59_0.contextData.missionShips):
					if iter_64_1 == arg_59_3[arg_59_2]:
						table.remove(arg_59_0.contextData.missionShips, iter_64_0)

			table.insert(arg_59_0.contextData.missionShips, arg_64_0[1])
	})

def var_0_0.OnComanderOP(arg_65_0, arg_65_1):
	local var_65_0 = arg_65_1.data

	if var_65_0.type == LevelUIConst.COMMANDER_OP_RENAME:
		local var_65_1 = var_65_0.id
		local var_65_2 = var_65_0.str
		local var_65_3 = var_65_0.onFailed

		arg_65_0.sendNotification(GAME.SET_COMMANDER_PREFAB_NAME, {
			id = var_65_1,
			name = var_65_2,
			onFailed = var_65_3
		})
	elif var_65_0.type == LevelUIConst.COMMANDER_OP_RECORD_PREFAB:
		local var_65_4 = var_65_0.id
		local var_65_5 = var_65_0.fleet.getCommanders()

		arg_65_0.sendNotification(GAME.SET_COMMANDER_PREFAB, {
			id = var_65_4,
			commanders = Clone(var_65_5)
		})
	else
		local var_65_6 = var_65_0.id
		local var_65_7 = var_65_0.fleet

		if not arg_65_0.contextData.editBossFleet:
			arg_65_0.contextData.editBossFleet = {}

		if not arg_65_0.contextData.editBossFleet[var_65_7.id]:
			arg_65_0.contextData.editBossFleet[var_65_7.id] = Clone(var_65_7)

		local var_65_8 = arg_65_0.contextData.editBossFleet[var_65_7.id]

		if var_65_0.type == LevelUIConst.COMMANDER_OP_USE_PREFAB:
			local var_65_9 = getProxy(GuildProxy).getData().GetActiveEvent().GetBossMission()

			var_65_8.ClearCommanders()

			local var_65_10 = getProxy(CommanderProxy).getPrefabFleetById(var_65_6).getCommander()
			local var_65_11 = {}

			for iter_65_0, iter_65_1 in pairs(var_65_10):
				table.insert(var_65_11, function(arg_66_0)
					arg_65_0.OnDockSelectCommander(False, var_65_8, iter_65_0, var_65_9, {
						iter_65_1.id
					}, arg_66_0))

			seriesAsync(var_65_11, function()
				arg_65_0.viewComponent.OnBossCommanderFormationChange())
		elif var_65_0.type == LevelUIConst.COMMANDER_OP_REST_ALL:
			var_65_8.ClearCommanders()
			arg_65_0.viewComponent.OnBossCommanderFormationChange()

def var_0_0.listNotificationInterests(arg_68_0):
	return {
		PlayerProxy.UPDATED,
		GuildProxy.GUILD_UPDATED,
		GAME.GUILD_ACTIVE_EVENT_DONE,
		GuildProxy.GUILD_BATTLE_STARTED,
		GAME.GUILD_UPDATE_MY_ASSAULT_FLEET_DONE,
		GAME.GUILD_JOIN_MISSION_DONE,
		GAME.GUILD_REFRESH_MISSION_DONE,
		GAME.GUILD_GET_BOSS_INFO_DONE,
		GAME.GET_GUILD_BOSS_RANK_DONE,
		GAME.GUILD_UPDATE_NODE_ANIM_FLAG_DONE,
		GAME.GUILD_UPDATE_BOSS_FORMATION_DONE,
		GAME.GUILD_GET_ASSAULT_FLEET_DONE,
		GAME.GUILD_GET_MY_ASSAULT_FLEET_DONE,
		GAME.SUBMIT_GUILD_REPORT_DONE,
		GAME.ON_GUILD_JOIN_EVENT_DONE,
		GAME.GUILD_END_BATTLE,
		GuildProxy.ON_EXIST_DELETED_MEMBER,
		GAME.GUILD_RECOMMAND_ASSULT_SHIP_DONE,
		GAME.REFRESH_ALL_ASSULT_SHIP_RECOMMAND_STATE_DONE,
		TaskProxy.TASK_PROGRESS_UPDATE,
		GAME.SET_COMMANDER_PREFAB_NAME_DONE,
		GAME.SET_COMMANDER_PREFAB_DONE,
		GAME.ON_GUILD_EVENT_END
	}

def var_0_0.handleNotification(arg_69_0, arg_69_1):
	local var_69_0 = arg_69_1.getName()
	local var_69_1 = arg_69_1.getBody()

	if var_69_0 == PlayerProxy.UPDATED:
		arg_69_0.viewComponent.SetPlayer(var_69_1)
	elif var_69_0 == GuildProxy.GUILD_UPDATED:
		arg_69_0.viewComponent.UpdateGuild(var_69_1)
	elif var_69_0 == GAME.GUILD_ACTIVE_EVENT_DONE:
		arg_69_0.sendNotification(GAME.GUILD_GET_ACTIVATION_EVENT, {
			force = True,
			def callback:()
				arg_69_0.viewComponent.EnterEvent()
		})
	elif var_69_0 == GAME.GUILD_UPDATE_MY_ASSAULT_FLEET_DONE:
		arg_69_0.contextData.editFleet = None

		arg_69_0.viewComponent.OnMyAssultFleetFormationDone()
		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_event_start_done"))
	elif var_69_0 == GAME.GUILD_JOIN_MISSION_DONE:
		arg_69_0.contextData.missionShips = None

		arg_69_0.sendNotification(GAME.GUILD_REFRESH_MISSION, {
			force = True,
			id = var_69_1.id
		})
		arg_69_0.viewComponent.OnMissionFormationDone()
	elif var_69_0 == GAME.GUILD_REFRESH_MISSION_DONE:
		arg_69_0.viewComponent.RefreshMission(var_69_1.id)
	elif var_69_0 == GAME.GUILD_GET_BOSS_INFO_DONE:
		arg_69_0.viewComponent.RefreshBossMission()
	elif var_69_0 == GAME.GET_GUILD_BOSS_RANK_DONE:
		arg_69_0.viewComponent.OnBossRankUpdate()
	elif var_69_0 == GAME.GUILD_UPDATE_NODE_ANIM_FLAG_DONE:
		arg_69_0.viewComponent.RefreshMission(var_69_1.id)
	elif var_69_0 == GAME.GUILD_UPDATE_BOSS_FORMATION_DONE:
		arg_69_0.contextData.editBossFleet = None

		pg.TipsMgr.GetInstance().ShowTips(i18n("guild_fleet_update_done"))
		arg_69_0.viewComponent.OnBossMissionFormationChanged()
	elif var_69_0 == GAME.GUILD_GET_ASSAULT_FLEET_DONE:
		arg_69_0.viewComponent.OnMemberAssultFleetUpdate()
	elif var_69_0 == GAME.GUILD_GET_MY_ASSAULT_FLEET_DONE:
		arg_69_0.viewComponent.OnMyAssultFleetUpdate()
	elif var_69_0 == GAME.SUBMIT_GUILD_REPORT_DONE:
		arg_69_0.viewComponent.OnReportUpdated()
	elif var_69_0 == GuildProxy.GUILD_BATTLE_STARTED:
		local var_69_2 = getProxy(GuildProxy).getRawData().IsAdministrator()
		local var_69_3 = i18n("guild_event_start_tip1")

		if var_69_2 and arg_69_0.viewComponent.eventInfoPage and arg_69_0.viewComponent.eventInfoPage.GetLoaded() and arg_69_0.viewComponent.eventInfoPage.isShowing():
			var_69_3 = i18n("guild_event_start_tip2")

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = var_69_3,
			def onYes:()
				arg_69_0.sendNotification(GAME.GUILD_GET_ACTIVATION_EVENT, {
					force = True,
					def callback:()
						arg_69_0.viewComponent.EnterEvent()
				})
		})
	elif var_69_0 == GAME.ON_GUILD_JOIN_EVENT_DONE:
		arg_69_0.viewComponent.EnterEvent()
	elif var_69_0 == GAME.GUILD_END_BATTLE:
		arg_69_0.viewComponent.EnterEvent()
	elif var_69_0 == GuildProxy.ON_EXIST_DELETED_MEMBER:
		arg_69_0.viewComponent.OnMemberDeleted()
	elif var_69_0 == GAME.GUILD_RECOMMAND_ASSULT_SHIP_DONE:
		arg_69_0.viewComponent.OnAssultShipBeRecommanded(var_69_1.shipId)
	elif var_69_0 == GAME.REFRESH_ALL_ASSULT_SHIP_RECOMMAND_STATE_DONE:
		arg_69_0.viewComponent.OnRefreshAllAssultShipRecommandState()
	elif var_69_0 == TaskProxy.TASK_PROGRESS_UPDATE:
		pg.GuildMsgBoxMgr.GetInstance().NotificationForGuildEvent(var_69_1)
	elif var_69_0 == GAME.SET_COMMANDER_PREFAB_NAME_DONE or var_69_0 == GAME.SET_COMMANDER_PREFAB_DONE:
		arg_69_0.viewComponent.OnBossCommanderPrefabFormationChange()
	elif var_69_0 == GAME.ON_GUILD_EVENT_END:
		arg_69_0.viewComponent.OnEventEnd()

return var_0_0
