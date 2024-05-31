local var_0_0 = class("NavalAcademyScene", import("..base.BaseUI"))

var_0_0.WARP_TO_TACTIC = "WARP_TO_TACTIC"

def var_0_0.getUIName(arg_1_0):
	local var_1_0 = pg.activity_banner.get_id_list_by_type[GAMEUI_BANNER_13]
	local var_1_1 = _.filter(var_1_0, function(arg_2_0)
		local var_2_0 = pg.activity_banner[arg_2_0].time

		return pg.TimeMgr.GetInstance().inTime(var_2_0))
	local var_1_2 = pg.activity_banner[var_1_1[1]]
	local var_1_3 = var_1_2 and var_1_2.pic
	local var_1_4 = pg.naval_academy_theme[var_1_3]

	return var_1_4 and var_1_4.resource_path or "NavalAcademyUI"

def var_0_0.ResUISettings(arg_3_0):
	return True

def var_0_0.SetOilResField(arg_4_0, arg_4_1):
	arg_4_0.oilResField = arg_4_1

def var_0_0.SetGoldResField(arg_5_0, arg_5_1):
	arg_5_0.goldResField = arg_5_1

def var_0_0.SetClassResField(arg_6_0, arg_6_1):
	arg_6_0.classResField = arg_6_1

def var_0_0.SetPlayer(arg_7_0, arg_7_1):
	arg_7_0.player = arg_7_1

def var_0_0.UpdatePlayer(arg_8_0, arg_8_1):
	arg_8_0.player = arg_8_1

def var_0_0.onUILoaded(arg_9_0, arg_9_1):
	arg_9_1.name = "NavalAcademyUI"

	var_0_0.super.onUILoaded(arg_9_0, arg_9_1)

def var_0_0.init(arg_10_0):
	arg_10_0.backBtn = arg_10_0.findTF("blur_container/adapt/top/title/back")
	arg_10_0._blurLayer = arg_10_0.findTF("blur_container")
	arg_10_0._topPanel = arg_10_0._blurLayer.Find("adapt/top")
	arg_10_0.bg = arg_10_0.findTF("academyMap/map")
	arg_10_0.buildings = {
		ShopBuiding.New(arg_10_0),
		CanteenBuiding.New(arg_10_0),
		ClassRoomBuilding.New(arg_10_0),
		FountainBuiding.New(arg_10_0),
		TacticRoomBuilding.New(arg_10_0),
		CommanderBuilding.New(arg_10_0),
		SupplyShopBuilding.New(arg_10_0),
		MinigameHallBuilding.New(arg_10_0)
	}
	arg_10_0.shipsView = NavalAcademyShipsView.New(arg_10_0)
	arg_10_0.resPage = ResourcePage.New(arg_10_0._tf, arg_10_0.event)

def var_0_0.didEnter(arg_11_0):
	onButton(arg_11_0, arg_11_0.backBtn, function()
		arg_11_0.ExitAnim()
		arg_11_0.emit(var_0_0.ON_BACK, None, 0.3), SFX_CANCEL)
	arg_11_0.InitBuildings()
	arg_11_0.shipsView.BindBuildings(arg_11_0.buildings)
	arg_11_0.UpdatePlayer(arg_11_0.player)
	arg_11_0.LoadEffects()
	arg_11_0.OpenDefaultLayer()
	arg_11_0.EnterAnim()
	arg_11_0.InitChars()

	arg_11_0.bulinTip = AprilFoolBulinSubView.ShowAprilFoolBulin(arg_11_0)

def var_0_0.InitBuildings(arg_13_0):
	for iter_13_0, iter_13_1 in ipairs(arg_13_0.buildings):
		iter_13_1.Init()

def var_0_0.EnterAnim(arg_14_0):
	setAnchoredPosition(arg_14_0._topPanel, {
		y = 84
	})
	shiftPanel(arg_14_0._topPanel, None, 0, 0.3, 0, True, True)

def var_0_0.ExitAnim(arg_15_0):
	shiftPanel(arg_15_0._topPanel, None, arg_15_0._topPanel.rect.height, 0.3, 0, True, True)

def var_0_0.OpenDefaultLayer(arg_16_0):
	arg_16_0.warp = arg_16_0.contextData.warp
	arg_16_0.contextData.warp = None

	if arg_16_0.warp == var_0_0.WARP_TO_TACTIC:
		arg_16_0.emit(NavalAcademyMediator.ON_OPEN_TACTICROOM)

def var_0_0.LoadEffects(arg_17_0):
	arg_17_0.LoadWaveEffect()
	arg_17_0.LoadMainEffect()

def var_0_0.LoadWaveEffect(arg_18_0):
	arg_18_0.GetEffect("xueyuan02", function(arg_19_0)
		setParent(arg_19_0, arg_18_0.bg)

		arg_18_0.waveEffect = arg_19_0)

def var_0_0.LoadMainEffect(arg_20_0):
	return

def var_0_0.InitChars(arg_21_0):
	arg_21_0.shipsView.Init()

def var_0_0.OpenGoldResField(arg_22_0):
	arg_22_0.resPage.ExecuteAction("Flush", arg_22_0.goldResField)

def var_0_0.OpenOilResField(arg_23_0):
	arg_23_0.resPage.ExecuteAction("Flush", arg_23_0.oilResField)

def var_0_0.OnAddLayer(arg_24_0):
	arg_24_0.layerCnt = (arg_24_0.layerCnt or 0) + 1

	if arg_24_0.layerCnt == 1:
		arg_24_0.EnableEffects(False)

def var_0_0.OnRemoveLayer(arg_25_0, arg_25_1):
	arg_25_0.layerCnt = (arg_25_0.layerCnt or 0) - 1

	if arg_25_0.layerCnt <= 0:
		arg_25_0.layerCnt = 0

		arg_25_0.EnableEffects(True)

	if arg_25_1.context.mediator == NewNavalTacticsMediator:
		arg_25_0.buildings[5].RefreshTip()

def var_0_0.EnableEffects(arg_26_0, arg_26_1):
	if arg_26_0.waveEffect:
		setActive(arg_26_0.waveEffect, arg_26_1)

	if arg_26_0.mainEffect:
		setActive(arg_26_0.mainEffect, arg_26_1)

def var_0_0.OnGetRes(arg_27_0, arg_27_1, arg_27_2):
	if arg_27_0.buildings[arg_27_1]:
		arg_27_0.buildings[arg_27_1].PlayGetResAnim(arg_27_2)

def var_0_0.OnStartUpgradeResField(arg_28_0, arg_28_1):
	local var_28_0

	if isa(arg_28_1, OilResourceField):
		var_28_0 = arg_28_0.buildings[2]
		page = arg_28_0.resPage
	elif isa(arg_28_1, GoldResourceField):
		var_28_0 = arg_28_0.buildings[1]
		page = arg_28_0.resPage
	elif isa(arg_28_1, ClassResourceField):
		var_28_0 = arg_28_0.buildings[3]

	if var_28_0:
		var_28_0.UpdateResField()

	if page and page.GetLoaded() and page.isShowing() and page.resourceField and page.resourceField.GetKeyWord() == arg_28_1.GetKeyWord():
		page.Update(arg_28_1)

def var_0_0.OnResFieldLevelUp(arg_29_0, arg_29_1):
	arg_29_0.OnStartUpgradeResField(arg_29_1)

def var_0_0.OnCollectionUpdate(arg_30_0):
	arg_30_0.buildings[4].RefreshTip()

def var_0_0.RefreshChars(arg_31_0):
	arg_31_0.shipsView.Refresh()

def var_0_0.willExit(arg_32_0):
	for iter_32_0, iter_32_1 in ipairs(arg_32_0.buildings):
		iter_32_1.Dispose()

	arg_32_0.buildings = None

	if arg_32_0.resPage:
		arg_32_0.resPage.Destroy()

		arg_32_0.resPage = None

	if arg_32_0.mainEffect:
		Destroy(arg_32_0.mainEffect)

		arg_32_0.mainEffect = None

	if arg_32_0.waveEffect:
		Destroy(arg_32_0.waveEffect)

		arg_32_0.waveEffect = None

	if arg_32_0.bulinTip:
		arg_32_0.bulinTip.Destroy()

		arg_32_0.bulinTip = None

	if arg_32_0.shipsView:
		arg_32_0.shipsView.Dispose()

		arg_32_0.shipsView = None

def var_0_0.GetEffect(arg_33_0, arg_33_1, arg_33_2):
	ResourceMgr.Inst.getAssetAsync("ui/" .. arg_33_1, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_34_0)
		if arg_33_0.exited:
			return

		arg_33_2(Instantiate(arg_34_0))), True, True)

return var_0_0
