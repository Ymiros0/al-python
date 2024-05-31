local var_0_0 = class("MetaCharacterMediator", import("...base.ContextMediator"))

var_0_0.OPEN_PT_PREVIEW_LAYER = "MetaCharacterMediator.OPEN_PT_PREVIEW_LAYER"
var_0_0.OPEN_PT_GET_WAY_LAYER = "MetaCharacterMediator.OPEN_PT_GET_WAY_LAYER"
var_0_0.OPEN_INDEX_LAYER = "MetaCharacterMediator.OPEN_INDEX_LAYER"
var_0_0.ON_REPAIR = "MetaCharacterMediator.ON_REPAIR"
var_0_0.ON_ENERGY = "MetaCharacterMediator.ON_ENERGY"
var_0_0.ON_TACTICS = "MetaCharacterMediator.ON_TACTICS"
var_0_0.ON_SYN = "MetaCharacterMediator.ON_SYN"
var_0_0.ON_UNLOCK = "MetaCharacterMediator.ON_UNLOCK"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.OPEN_PT_PREVIEW_LAYER, function(arg_2_0, arg_2_1)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = MetaPTAwardPreviewLayer,
			mediator = MetaPTAwardPreviewMediator,
			data = {
				metaProgressVO = arg_2_1
			}
		})))
	arg_1_0.bind(var_0_0.OPEN_PT_GET_WAY_LAYER, function(arg_3_0)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = MetaPTGetPreviewLayer,
			mediator = MetaPTGetPreviewMediator,
			data = {}
		})))
	arg_1_0.bind(var_0_0.OPEN_INDEX_LAYER, function(arg_4_0, arg_4_1)
		arg_1_0.addSubLayers(Context.New({
			viewComponent = CustomIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_4_1
		})))
	arg_1_0.bind(var_0_0.ON_REPAIR, function(arg_5_0, arg_5_1, arg_5_2)
		arg_1_0.enbalePage(Context.New({
			viewComponent = MetaCharacterRepairLayer,
			mediator = MetaCharacterRepairMediator,
			data = {
				shipID = arg_5_1,
				LayerWeightMgr_groupName = LayerWeightConst.GROUP_META
			},
			def onRemoved:()
				arg_1_0.viewComponent.enterMenuPage(False)

				arg_1_0.viewComponent.curPageIndex = None

				arg_1_0.viewComponent.resetToggleList()
				arg_1_0.viewComponent.refreshBannerTF()
				arg_1_0.viewComponent.updateRedPoints()
		}), arg_5_2))
	arg_1_0.bind(var_0_0.ON_ENERGY, function(arg_7_0, arg_7_1, arg_7_2)
		local var_7_0 = arg_1_0.viewComponent.isMainOpenLayerTag and True or None

		arg_1_0.viewComponent.isMainOpenLayerTag = None

		arg_1_0.enbalePage(Context.New({
			viewComponent = MetaCharacterEnergyLayer,
			mediator = MetaCharacterEnergyMediator,
			data = {
				shipID = arg_7_1,
				LayerWeightMgr_groupName = LayerWeightConst.GROUP_META,
				isMainOpen = var_7_0
			},
			def onRemoved:()
				arg_1_0.viewComponent.enterMenuPage(False)

				arg_1_0.viewComponent.curPageIndex = None

				arg_1_0.viewComponent.resetToggleList()
				arg_1_0.viewComponent.refreshBannerTF()
				arg_1_0.viewComponent.updateRedPoints()
		}), arg_7_2))
	arg_1_0.bind(var_0_0.ON_TACTICS, function(arg_9_0, arg_9_1, arg_9_2)
		local var_9_0 = arg_1_0.viewComponent.isMainOpenLayerTag and True or None

		arg_1_0.viewComponent.isMainOpenLayerTag = None

		arg_1_0.enbalePage(Context.New({
			viewComponent = MetaCharacterTacticsLayer,
			mediator = MetaCharacterTacticsMediator,
			data = {
				shipID = arg_9_1,
				LayerWeightMgr_groupName = LayerWeightConst.GROUP_META,
				isMainOpen = var_9_0
			},
			def onRemoved:()
				if arg_1_0.contextData.isFromNavalMeta == True:
					arg_1_0.viewComponent.closeView()

					arg_1_0.contextData.isFromNavalMeta = None
				else
					arg_1_0.viewComponent.enterMenuPage(False)

					arg_1_0.viewComponent.curPageIndex = None

					arg_1_0.viewComponent.resetToggleList()
					arg_1_0.viewComponent.updateRedPoints()
		}), arg_9_2))
	arg_1_0.bind(var_0_0.ON_SYN, function(arg_11_0, arg_11_1, arg_11_2)
		local var_11_0 = arg_1_0.viewComponent.isMainOpenLayerTag and True or None

		arg_1_0.viewComponent.isMainOpenLayerTag = None

		arg_1_0.enbalePage(Context.New({
			viewComponent = MetaCharacterSynLayer,
			mediator = MetaCharacterSynMediator,
			data = {
				shipID = arg_11_1,
				LayerWeightMgr_groupName = LayerWeightConst.GROUP_META,
				isMainOpen = var_11_0
			},
			def onRemoved:()
				arg_1_0.viewComponent.enterMenuPage(False)

				arg_1_0.viewComponent.curPageIndex = None

				arg_1_0.viewComponent.resetToggleList()
				arg_1_0.viewComponent.updateRedPoints()
		}), arg_11_2))

def var_0_0.enbalePage(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_2:
		arg_13_0.addSubLayers(arg_13_1)
	else
		local var_13_0 = getProxy(ContextProxy).getContextByMediator(arg_13_1.mediator)

		if var_13_0:
			arg_13_0.sendNotification(GAME.REMOVE_LAYERS, {
				context = var_13_0
			})

def var_0_0.listNotificationInterests(arg_14_0):
	return {
		GAME.ACT_NEW_PT_DONE,
		BayProxy.SHIP_ADDED,
		GAME.GET_META_PT_AWARD_DONE
	}

def var_0_0.handleNotification(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_1.getName()
	local var_15_1 = arg_15_1.getBody()

	if var_15_0 == BayProxy.SHIP_ADDED:
		local var_15_2 = arg_15_0.viewComponent.getCurMetaProgressVO()

		var_15_2.updateDataAfterAddShip()

		if var_15_2.isPassType() or var_15_2.isBuildType():
			arg_15_0.viewComponent.refreshBannerTF()
			arg_15_0.viewComponent.updateMain()
	elif var_15_0 == GAME.GET_META_PT_AWARD_DONE:
		local function var_15_3()
			if var_15_1.callback:
				var_15_1.callback()

			arg_15_0.viewComponent.refreshBannerTF()
			arg_15_0.viewComponent.updateMain(True)

		arg_15_0.viewComponent.emit(BaseUI.ON_ACHIEVE, var_15_1.awards, var_15_3)

return var_0_0
