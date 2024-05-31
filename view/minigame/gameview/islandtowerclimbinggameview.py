local var_0_0 = class("IslandTowerClimbingGameView", import("..BaseMiniGameView"))

def var_0_0.getUIName(arg_1_0):
	return "IslandTowerClimbingUI"

def var_0_0.GetMGData(arg_2_0):
	local var_2_0 = arg_2_0.contextData.miniGameId

	return getProxy(MiniGameProxy).GetMiniGameData(var_2_0).clone()

def var_0_0.GetMGHubData(arg_3_0):
	local var_3_0 = arg_3_0.contextData.miniGameId

	return getProxy(MiniGameProxy).GetHubByGameId(var_3_0)

def var_0_0.didEnter(arg_4_0):
	if not Physics2D.autoSimulation:
		Physics2D.autoSimulation = True
		arg_4_0.isChangeAutoSimulation = True

	arg_4_0.Start()

	arg_4_0.backBtn = findTF(arg_4_0._tf, "overview/back")

	onButton(arg_4_0, arg_4_0.backBtn, function()
		arg_4_0.emit(var_0_0.ON_BACK), SFX_PANEL)
	onButton(arg_4_0, findTF(arg_4_0._tf, "overview/item"), function()
		local var_6_0 = {
			mediator = IslandGameLimitMediator,
			viewComponent = IslandGameLimitLayer,
			data = {
				type = IslandGameLimitLayer.limit_type_jiujiu
			}
		}

		arg_4_0.emit(BaseMiniGameMediator.OPEN_SUB_LAYER, var_6_0), SFX_CANCEL)

	local var_4_0 = ActivityConst.ISLAND_GAME_ID
	local var_4_1 = pg.activity_template[var_4_0].config_client.item_id

	arg_4_0.itemConfig = Item.getConfigData(var_4_1)

	LoadImageSpriteAsync(arg_4_0.itemConfig.icon, findTF(arg_4_0._tf, "overview/item/img"), True)

	arg_4_0.hub_id = pg.activity_template[var_4_0].config_id
	arg_4_0.itemNums = getProxy(MiniGameProxy).GetHubByHubId(arg_4_0.hub_id).count or 0

	setText(findTF(arg_4_0._tf, "overview/item/num"), arg_4_0.itemNums)

def var_0_0.Start(arg_7_0):
	arg_7_0.controller = TowerClimbingController.New()

	arg_7_0.controller.view.SetUI(arg_7_0._go)

	local function var_7_0(arg_8_0, arg_8_1, arg_8_2, arg_8_3)
		local var_8_0 = arg_7_0.GetMGData().GetRuntimeData("elements") or {}

		for iter_8_0 = 1, arg_8_3:
			if iter_8_0 > #var_8_0:
				table.insert(var_8_0, 0)

		if arg_8_0 >= var_8_0[arg_8_3]:
			var_8_0[arg_8_3] = arg_8_0

			arg_7_0.StoreDataToServer(var_8_0)
			arg_7_0.updateHighScore()

		if arg_7_0.getGameTimes() and arg_7_0.getGameTimes() > 0:
			arg_7_0.sendSuccessFlag = True

			arg_7_0.SendSuccess(0)

	local function var_7_1(arg_9_0, arg_9_1)
		return

	arg_7_0.controller.SetCallBack(var_7_0, var_7_1)

	local var_7_2 = arg_7_0.PackData()

	arg_7_0.controller.SetUp(var_7_2)

def var_0_0.updateHighScore(arg_10_0):
	local var_10_0 = arg_10_0.GetMGData().GetRuntimeData("elements") or {}

	if arg_10_0.controller:
		-- block empty

	arg_10_0.controller.updateHighScore(var_10_0)

def var_0_0.OnSendMiniGameOPDone(arg_11_0, arg_11_1):
	arg_11_0.itemNums = getProxy(MiniGameProxy).GetHubByHubId(arg_11_0.hub_id).count or 0

	setText(findTF(arg_11_0._tf, "overview/item/num"), arg_11_0.itemNums)
	arg_11_0.updateHighScore()

def var_0_0.getGameTimes(arg_12_0):
	return arg_12_0.GetMGHubData().count

def var_0_0.GetTowerClimbingPageAndScore(arg_13_0):
	local var_13_0 = 0
	local var_13_1 = 1
	local var_13_2 = {
		0,
		0,
		0
	}

	return var_13_0, var_13_1, var_13_2

def var_0_0.GetAwardScores():
	local var_14_0 = pg.mini_game[MiniGameDataCreator.TowerClimbingGameID].simple_config_data

	return (_.map(var_14_0, function(arg_15_0)
		return arg_15_0[1]))

def var_0_0.PackData(arg_16_0):
	local var_16_0 = arg_16_0._tf.rect.width
	local var_16_1 = arg_16_0._tf.rect.height
	local var_16_2 = arg_16_0.GetMGData().GetRuntimeData("elements")
	local var_16_3, var_16_4, var_16_5 = var_0_0.GetTowerClimbingPageAndScore(var_16_2)

	print(var_16_3, "-", var_16_4)

	local var_16_6 = var_0_0.GetAwardScores()

	return {
		shipId = 107031,
		npcName = "TowerClimbingManjuu",
		life = 3,
		screenWidth = var_16_0,
		screenHeight = var_16_1,
		higestscore = var_16_3,
		pageIndex = var_16_4,
		mapScores = var_16_5,
		awards = var_16_6
	}

def var_0_0.onBackPressed(arg_17_0):
	if arg_17_0.controller and arg_17_0.controller.onBackPressed():
		return

	arg_17_0.emit(var_0_0.ON_BACK)

def var_0_0.willExit(arg_18_0):
	if arg_18_0.controller:
		arg_18_0.controller.Dispose()

	if arg_18_0.isChangeAutoSimulation:
		Physics2D.autoSimulation = False
		arg_18_0.isChangeAutoSimulation = None

return var_0_0
