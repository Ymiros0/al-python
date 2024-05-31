local var_0_0 = class("DailyLevelMediator", import("..base.ContextMediator"))

var_0_0.ON_STAGE = "DailyLevelMediator.ON_STAGE"
var_0_0.ON_CHALLENGE = "DailyLevelMediator.ON_CHALLENGE"
var_0_0.ON_RESET_CHALLENGE = "DailyLevelMediator.ON_RESET_CHALLENGE"
var_0_0.ON_CONTINUE_CHALLENGE = "DailyLevelMediator.ON_CONTINUE_CHALLENGE"
var_0_0.ON_CHALLENGE_EDIT_FLEET = "DailyLevelMediator.ON_CHALLENGE_EDIT_FLEET"
var_0_0.ON_REQUEST_CHALLENGE = "DailyLevelMediator.ON_REQUEST_CHALLENGE"
var_0_0.ON_CHALLENGE_FLEET_CLEAR = "DailyLevelMediator.ON_CHALLENGE_FLEET_CLEAR"
var_0_0.ON_CHALLENGE_FLEET_RECOMMEND = "DailyLevelMediator.ON_CHALLENGE_FLEET_RECOMMEND"
var_0_0.ON_CHALLENGE_OPEN_DOCK = "DailyLevelMediator.ON_CHALLENGE_OPEN_DOCK"
var_0_0.ON_CHALLENGE_OPEN_RANK = "DailyLevelMediator.ON_CHALLENGE_OPEN_RANK"
var_0_0.ON_QUICK_BATTLE = "DailyLevelMediator.ON_QUICK_BATTLE"

def var_0_0.register(arg_1_0):
	local var_1_0 = getProxy(DailyLevelProxy)

	arg_1_0.viewComponent.setDailyCounts(var_1_0.getRawData())

	arg_1_0.ships = getProxy(BayProxy).getRawData()

	arg_1_0.viewComponent.setShips(arg_1_0.ships)

	local var_1_1 = getProxy(PlayerProxy).getData()

	arg_1_0.viewComponent.updateRes(var_1_1)
	arg_1_0.bind(var_0_0.ON_QUICK_BATTLE, function(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
		arg_1_0.CheckShipExpItemOverflow(arg_2_2, function()
			arg_1_0.sendNotification(GAME.DAILY_LEVEL_QUICK_BATTLE, {
				dailyLevelId = arg_2_1,
				stageId = arg_2_2,
				cnt = arg_2_3
			})))
	arg_1_0.bind(var_0_0.ON_STAGE, function(arg_4_0, arg_4_1)
		var_1_0.dailyLevelId = arg_1_0.contextData.dailyLevelId

		local var_4_0 = PreCombatLayer
		local var_4_1 = SYSTEM_ROUTINE

		if pg.expedition_data_template[arg_4_1.id].type == Stage.SubmarinStage:
			var_4_0 = PreCombatLayerSubmarine
			var_4_1 = SYSTEM_SUB_ROUTINE

		arg_1_0.addSubLayers(Context.New({
			mediator = PreCombatMediator,
			viewComponent = var_4_0,
			data = {
				stageId = arg_4_1.id,
				system = var_4_1,
				def OnConfirm:(arg_5_0)
					arg_1_0.CheckShipExpItemOverflow(arg_4_1.id, arg_5_0)
			}
		})))
	arg_1_0.bind(var_0_0.ON_CHALLENGE, function()
		arg_1_0.viewComponent.openChallengeView())
	arg_1_0.bind(var_0_0.ON_CHALLENGE_EDIT_FLEET, function(arg_7_0, arg_7_1)
		local var_7_0 = challengeProxy.getCurrentChallengeInfo()

		var_7_0.setDamageRateID(arg_7_1.damageRateID)
		var_7_0.setLevelRateID(arg_7_1.levelRateID)
		challengeProxy.updateChallenge(var_7_0)
		arg_1_0.viewComponent.openChallengeFleetEditView())
	arg_1_0.bind(var_0_0.ON_CONTINUE_CHALLENGE, function()
		arg_1_0.addSubLayers(Context.New({
			mediator = ChallengePreCombatMediator,
			viewComponent = ChallengePreCombatLayer,
			data = {}
		})))
	arg_1_0.bind(var_0_0.ON_RESET_CHALLENGE, function()
		arg_1_0.sendNotification(GAME.CHALLENGE_RESET))
	arg_1_0.bind(var_0_0.ON_CHALLENGE_FLEET_CLEAR, function()
		challengeProxy.clearEdittingFleet()
		arg_1_0.viewComponent.flushFleetEditButton())
	arg_1_0.bind(var_0_0.ON_CHALLENGE_FLEET_RECOMMEND, function()
		challengeProxy.recommendChallengeFleet()
		arg_1_0.viewComponent.flushFleetEditButton())
	arg_1_0.bind(var_0_0.ON_REQUEST_CHALLENGE, function()
		local var_12_0 = challengeProxy.getCurrentChallengeInfo()
		local var_12_1 = var_12_0.getGSRateID()

		for iter_12_0 = 1, 4:
			PlayerPrefs.SetInt("challengeShipUID_" .. iter_12_0, None)

		for iter_12_1 = 1, #var_12_0.getShips():
			PlayerPrefs.SetInt("challengeShipUID_" .. iter_12_1, var_12_0.getShips()[iter_12_1].id)

		arg_1_0.sendNotification(GAME.CHALLENGE_REQUEST, {
			shipIDList = var_12_0.getShips(),
			levelRate = var_12_0.getLevelRateID(),
			damageRate = var_12_0.getDamageRateID(),
			gsRate = var_12_1
		}))
	arg_1_0.bind(var_0_0.ON_CHALLENGE_OPEN_RANK, function()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.BILLBOARD, {
			page = PowerRank.TYPE_CHALLENGE
		}))
	arg_1_0.bind(var_0_0.ON_CHALLENGE_OPEN_DOCK, function(arg_14_0, arg_14_1)
		local var_14_0 = arg_14_1.shipType
		local var_14_1 = arg_14_1.shipVO
		local var_14_2 = arg_14_1.fleet
		local var_14_3 = arg_14_1.teamType
		local var_14_4 = getProxy(BayProxy).getRawData()
		local var_14_5 = {}

		for iter_14_0, iter_14_1 in pairs(var_14_4):
			if iter_14_1.getTeamType() != var_14_3 or var_14_0 != 0 and not table.contains({
				var_14_0
			}, iter_14_1.getShipType()):
				table.insert(var_14_5, iter_14_0)

		local var_14_6
		local var_14_7
		local var_14_8

		if var_14_1 == None:
			var_14_6 = False
			var_14_8 = None
		else
			var_14_6 = True
			var_14_8 = var_14_1.id

		local var_14_9 = {
			inChallenge = True,
			inEvent = False,
			inBackyard = False,
			inFleet = False,
			inClass = False,
			inTactics = False,
			inAdmiral = False
		}

		arg_1_0.contextData.challenge = True

		local var_14_10, var_14_11, var_14_12 = arg_1_0.getDockCallbackFuncs(var_14_2, var_14_1)

		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.DOCKYARD, {
			selectedMin = 0,
			selectedMax = 1,
			ignoredIds = var_14_5,
			activeShipId = var_14_8,
			leastLimitMsg = i18n("ship_formationMediator_leastLimit"),
			quitTeam = var_14_6,
			leftTopInfo = i18n("word_formation"),
			onShip = var_14_10,
			confirmSelect = var_14_11,
			onSelected = var_14_12,
			flags = var_14_9
		}))

	if arg_1_0.contextData.loadBillBoard:
		arg_1_0.contextData.loadBillBoard = None

		arg_1_0.viewComponent.emit(var_0_0.ON_CHALLENGE_OPEN_RANK)

def var_0_0.CheckShipExpItemOverflow(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = pg.expedition_data_template[arg_15_1].award_display

	if _.any(var_15_0, function(arg_16_0)
		local var_16_0 = getProxy(BagProxy).getItemCountById(arg_16_0[2])
		local var_16_1 = Item.getConfigData(arg_16_0[2])

		return arg_16_0[1] == DROP_TYPE_ITEM and var_16_1.type == Item.EXP_BOOK_TYPE and var_16_0 >= var_16_1.max_num):
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("player_expResource_mail_fullBag"),
			onYes = arg_15_2,
			weight = LayerWeightConst.THIRD_LAYER
		})
	else
		arg_15_2()

def var_0_0.listNotificationInterests(arg_17_0):
	return {
		PlayerProxy.UPDATED,
		ChallengeProxy.PRECOMBAT,
		ChallengeProxy.CHALLENGE_UPDATED,
		GAME.CHALLENGE_REQUEST_DONE,
		GAME.CHALLENGE_RESET_DONE,
		GAME.DAILY_LEVEL_QUICK_BATTLE_DONE,
		GAME.REMOVE_LAYERS
	}

def var_0_0.handleNotification(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_1.getName()
	local var_18_1 = arg_18_1.getBody()

	if var_18_0 == PlayerProxy.UPDATED:
		arg_18_0.viewComponent.updateRes(var_18_1)
	elif var_18_0 == ChallengeProxy.PRECOMBAT:
		arg_18_0.addSubLayers(Context.New({
			mediator = ChallengePreCombatMediator,
			viewComponent = ChallengePreCombatLayer,
			data = {
				stageId = stage.id,
				system = SYSTEM_ROUTINE
			}
		}))
	elif var_18_0 == GAME.CHALLENGE_REQUEST_DONE:
		arg_18_0.addSubLayers(Context.New({
			mediator = ChallengePreCombatMediator,
			viewComponent = ChallengePreCombatLayer,
			data = {}
		}))
		arg_18_0.viewComponent.closeChallengeFleetEditView()
	elif var_18_0 == GAME.CHALLENGE_RESET_DONE:
		arg_18_0.viewComponent.closeChallengeSettingView()
		arg_18_0.viewComponent.openChallengeSettingView()
	elif var_18_0 == ChallengeProxy.CHALLENGE_UPDATED:
		local var_18_2 = getProxy(ChallengeProxy).getCurrentChallengeInfo()

		arg_18_0.viewComponent.setChallengeInfo(var_18_2)
	elif var_18_0 == GAME.DAILY_LEVEL_QUICK_BATTLE_DONE:
		local var_18_3 = var_18_1.awards

		if #var_18_3 > 0:
			arg_18_0.DisplayAwards(var_18_3)

		local var_18_4 = getProxy(DailyLevelProxy)

		arg_18_0.viewComponent.setDailyCounts(var_18_4.getRawData())
		arg_18_0.viewComponent.UpdateBattleBtn({
			id = var_18_1.stageId
		})
		arg_18_0.viewComponent.UpdateDailyLevelCnt(var_18_1.dailyLevelId)
		arg_18_0.viewComponent.UpdateDailyLevelCntForDescPanel(var_18_1.dailyLevelId)
	elif var_18_0 == GAME.REMOVE_LAYERS and var_18_1.context.mediator.__cname == "PreCombatMediator":
		setActive(arg_18_0.viewComponent.blurPanel, True)

def var_0_0.getDockCallbackFuncs(arg_19_0, arg_19_1, arg_19_2):
	local var_19_0 = getProxy(BayProxy)
	local var_19_1 = getProxy(ChallengeProxy)
	local var_19_2 = var_19_1.getCurrentChallengeInfo()
	local var_19_3 = var_19_2.getShips()

	local function var_19_4(arg_20_0, arg_20_1)
		if arg_19_2 and arg_19_2.isSameKind(arg_20_0):
			return True

		local var_20_0 = Challenge.shipTypeFixer(arg_20_0.getShipType())
		local var_20_1 = 0

		for iter_20_0, iter_20_1 in pairs(arg_19_1):
			if Challenge.shipTypeFixer(iter_20_0.getShipType()) == var_20_0:
				var_20_1 = var_20_1 + 1

			if arg_20_0.isSameKind(iter_20_0):
				return False, i18n("event_same_type_not_allowed")

		if arg_19_2 and Challenge.shipTypeFixer(arg_19_2.getShipType()) == var_20_0:
			var_20_1 = var_20_1 - 1

		if var_20_1 >= Challenge.SAME_TYPE_LIMIT:
			return False, i18n("challenge_fleet_type_fail")

		return True

	local function var_19_5(arg_21_0, arg_21_1, arg_21_2)
		arg_21_1()

	local function var_19_6(arg_22_0)
		if arg_19_2:
			local var_22_0

			for iter_22_0, iter_22_1 in ipairs(var_19_3):
				if iter_22_1.id == arg_19_2.id:
					var_22_0 = iter_22_0

					break

			table.remove(var_19_3, var_22_0)

		if #arg_22_0 > 0:
			var_19_3[#var_19_3 + 1] = {
				id = arg_22_0[1]
			}

		var_19_1.updateChallenge(var_19_2)

	return var_19_4, var_19_5, var_19_6

def var_0_0.DisplayAwards(arg_23_0, arg_23_1):
	local var_23_0 = {}

	for iter_23_0, iter_23_1 in ipairs(arg_23_1):
		for iter_23_2, iter_23_3 in ipairs(iter_23_1):
			table.insert(var_23_0, iter_23_3)

	arg_23_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_23_0)

return var_0_0
