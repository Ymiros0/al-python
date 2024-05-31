local var_0_0 = class("PlayerVitaeMediator", import("..base.ContextMediator"))

var_0_0.CHANGE_SKIN = "PlayerVitaeMediator.CHANGE_SKIN"
var_0_0.ON_ATTIRE = "PlayerVitaeMediator.ON_ATTIRE"
var_0_0.CHANGE_MANIFESTO = "PlayerVitaeMediator.CHANGE_MANIFESTO"
var_0_0.ON_CHANGE_PLAYER_NAME = "PlayerVitaeMediator.ON_CHANGE_PLAYER_NAME"
var_0_0.CHANGE_PAINTS = "PlayerVitaeMediator.CHANGE_PAINTS"
var_0_0.CHANGE_PAINT = "PlayerVitaeMediator.CHANGE_PAINT"
var_0_0.CHANGE_RANDOM_SETTING = "PlayerVitaeMediator.CHANGE_RANDOM_SETTING"
var_0_0.GO_SCENE = "PlayerVitaeMediator.GO_SCENE"
var_0_0.ON_SWITCH_RANDOM_FLAG_SHIP_BTN = "PlayerVitaeMediator.ON_SWITCH_RANDOM_FLAG_SHIP_BTN"
var_0_0.OPEN_CRYPTOLALIA = "PlayerVitaeMediator.OPEN_CRYPTOLALIA"
var_0_0.ON_SEL_EDUCATE_CHAR = "PlayerVitaeMediator.ON_SEL_EDUCATE_CHAR"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.ON_SEL_EDUCATE_CHAR, function(arg_2_0)
		arg_1_0.addSubLayers(Context.New({
			mediator = EducateCharDockMediator,
			viewComponent = EducateCharDockScene,
			data = {
				def OnSelected:(arg_3_0)
					arg_1_0.sendNotification(GAME.CHANGE_EDUCATE, {
						id = arg_3_0
					})
			}
		})))
	arg_1_0.bind(var_0_0.OPEN_CRYPTOLALIA, function(arg_4_0, arg_4_1)
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.CRYPTOLALIA, {
			groupId = arg_4_1
		}))
	arg_1_0.bind(var_0_0.ON_SWITCH_RANDOM_FLAG_SHIP_BTN, function(arg_5_0, arg_5_1)
		arg_1_0.sendNotification(GAME.RANDOM_FLAG_SHIP, {
			isOn = arg_5_1
		}))
	arg_1_0.bind(var_0_0.GO_SCENE, function(arg_6_0, arg_6_1, arg_6_2)
		arg_1_0.sendNotification(GAME.GO_SCENE, arg_6_1, arg_6_2))
	arg_1_0.bind(var_0_0.CHANGE_RANDOM_SETTING, function(arg_7_0, arg_7_1)
		arg_1_0.sendNotification(GAME.CHANGE_RANDOM_SHIP_AND_SKIN_SETTING, arg_7_1))
	arg_1_0.bind(var_0_0.CHANGE_SKIN, function(arg_8_0, arg_8_1)
		arg_1_0.addSubLayers(Context.New({
			mediator = SwichSkinMediator,
			viewComponent = SwichSkinLayer,
			data = {
				shipVO = arg_8_1
			}
		})))
	arg_1_0.bind(var_0_0.CHANGE_PAINTS, function(arg_9_0, arg_9_1, arg_9_2)
		arg_1_0.sendNotification(GAME.CHANGE_PLAYER_ICON, {
			characterId = arg_9_1,
			callback = arg_9_2
		}))
	arg_1_0.bind(var_0_0.ON_CHANGE_PLAYER_NAME, function(arg_10_0, arg_10_1)
		arg_1_0.sendNotification(GAME.CHANGE_PLAYER_NAME, {
			name = arg_10_1
		}))
	arg_1_0.bind(var_0_0.ON_ATTIRE, function()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.ATTIRE))
	arg_1_0.bind(var_0_0.CHANGE_MANIFESTO, function(arg_12_0, arg_12_1)
		arg_1_0.sendNotification(GAME.CHANGE_PLAYER_MANIFESTO, {
			manifesto = arg_12_1
		}))
	arg_1_0.bind(var_0_0.CHANGE_PAINT, function(arg_13_0, arg_13_1)
		local var_13_0 = {}

		arg_1_0.contextData.showSelectCharacters = True

		local var_13_1 = getProxy(PlayerProxy).getRawData()
		local var_13_2 = {}

		for iter_13_0, iter_13_1 in ipairs(var_13_1.characters):
			if not arg_13_1 or iter_13_1 != arg_13_1.id:
				table.insert(var_13_0, iter_13_1)

			table.insert(var_13_2, iter_13_1)

		local var_13_3, var_13_4 = PlayerVitaeShipsPage.GetSlotMaxCnt()
		local var_13_5 = {
			callbackQuit = True,
			selectedMax = var_13_4,
			hideTagFlags = ShipStatus.TAG_HIDE_ADMIRAL,
			selectedIds = var_13_0,
			ignoredIds = pg.ShipFlagMgr.GetInstance().FilterShips({
				isActivityNpc = True
			}),
			def onSelected:(arg_14_0, arg_14_1)
				local var_14_0 = arg_1_0.ReSortShipIds(var_13_2, arg_14_0)

				arg_1_0.contextData.showSelectCharacters = False

				arg_1_0.sendNotification(GAME.CHANGE_PLAYER_ICON, {
					characterId = var_14_0,
					callback = arg_14_1
				})
		}

		arg_1_0.addSubLayers(Context.New({
			viewComponent = PlayerVitaeDockyardScene,
			mediator = DockyardMediator,
			data = var_13_5
		})))

def var_0_0.ReSortShipIds(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = {}
	local var_15_1 = math.max(#arg_15_1, #arg_15_2)

	for iter_15_0, iter_15_1 in ipairs(arg_15_1):
		if table.contains(arg_15_2, iter_15_1):
			var_15_0[iter_15_0] = iter_15_1

			table.removebyvalue(arg_15_2, iter_15_1)

	for iter_15_2 = 1, var_15_1:
		if not var_15_0[iter_15_2] and #arg_15_2 > 0:
			var_15_0[iter_15_2] = table.remove(arg_15_2, 1)

	local var_15_2 = {}

	for iter_15_3, iter_15_4 in pairs(var_15_0):
		table.insert(var_15_2, iter_15_4)

	return var_15_2

def var_0_0.listNotificationInterests(arg_16_0):
	return {
		GAME.CHANGE_PLAYER_NAME_DONE,
		SetShipSkinCommand.SKIN_UPDATED,
		GAME.UPDATE_SKINCONFIG,
		GAME.CHANGE_PLAYER_ICON_DONE,
		PaintingGroupConst.NotifyPaintingDownloadFinish,
		GAME.CHANGE_EDUCATE_DONE,
		GAME.CLEAR_EDUCATE_TIP
	}

def var_0_0.handleNotification(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_1.getName()
	local var_17_1 = arg_17_1.getBody()

	if var_17_0 == GAME.CHANGE_PLAYER_NAME_DONE:
		arg_17_0.viewComponent.OnPlayerNameChange()
	elif var_17_0 == SetShipSkinCommand.SKIN_UPDATED:
		arg_17_0.viewComponent.OnShipSkinChanged(var_17_1.ship)
	elif var_17_0 == GAME.UPDATE_SKINCONFIG:
		arg_17_0.viewComponent.ReloadPanting(var_17_1.skinId)
	elif var_17_0 == GAME.CHANGE_PLAYER_ICON_DONE:
		arg_17_0.viewComponent.RefreshShips()
	elif var_17_0 == PaintingGroupConst.NotifyPaintingDownloadFinish:
		arg_17_0.viewComponent.updateSwitchSkinBtnTag()

		if arg_17_0.viewComponent.shipsPage and arg_17_0.viewComponent.shipsPage.GetLoaded():
			arg_17_0.viewComponent.shipsPage.UpdateCardPaintingTag()
	elif var_17_0 == GAME.CHANGE_EDUCATE_DONE:
		arg_17_0.viewComponent.UpdatePainting(True)

		if arg_17_0.viewComponent.shipsPage and arg_17_0.viewComponent.shipsPage.GetLoaded():
			arg_17_0.viewComponent.shipsPage.UpdateEducateChar()
	elif var_17_0 == GAME.CLEAR_EDUCATE_TIP and arg_17_0.viewComponent.shipsPage and arg_17_0.viewComponent.shipsPage.GetLoaded():
		arg_17_0.viewComponent.shipsPage.UpdateEducateCharTrTip()

return var_0_0
