local var_0_0 = class("NewMainSceneBaseTheme", import("view.base.BaseSubView"))

def var_0_0.OnLoaded(arg_1_0):
	arg_1_0.mainCG = GetOrAddComponent(arg_1_0._tf, typeof(CanvasGroup))
	arg_1_0.mainCG.alpha = 0
	arg_1_0.panels = {
		arg_1_0.GetTopPanel(),
		arg_1_0.GetRightPanel(),
		arg_1_0.GetLeftPanel(),
		arg_1_0.GetBottomPanel()
	}
	arg_1_0.tagView = arg_1_0.GetTagView()
	arg_1_0.iconView = arg_1_0.GetIconView()
	arg_1_0.chatRoomView = arg_1_0.GetChatRoomView()
	arg_1_0.bannerView = arg_1_0.GetBannerView()
	arg_1_0.actBtnView = arg_1_0.GetActBtnView()
	arg_1_0.buffView = arg_1_0.GetBuffView()
	arg_1_0.wordView = arg_1_0.GetWordView()

	pg.redDotHelper.Init(arg_1_0.GetRedDots())

def var_0_0.Show(arg_2_0, arg_2_1):
	arg_2_1()
	var_0_0.super.Show(arg_2_0)

def var_0_0.PlayEnterAnimation(arg_3_0, arg_3_1, arg_3_2):
	arg_3_0.bannerView.Init()
	arg_3_0.actBtnView.Init()
	arg_3_0._FoldPanels(True, 0)

	arg_3_0.mainCG.alpha = 1

	arg_3_0._FoldPanels(False, 0.5)
	onDelayTick(arg_3_2, 0.51)

def var_0_0.init(arg_4_0, arg_4_1):
	for iter_4_0, iter_4_1 in ipairs(arg_4_0.panels):
		iter_4_1.Init()

	arg_4_0.iconView.Init(arg_4_1)
	arg_4_0.chatRoomView.Init()
	arg_4_0.buffView.Init()
	arg_4_0.tagView.Init()
	pg.LayerWeightMgr.GetInstance().Add2Overlay(LayerWeightConst.UI_TYPE_OVERLAY_FOREVER, arg_4_0._tf, {
		pbList = arg_4_0.GetPbList(),
		weight = LayerWeightConst.BASE_LAYER + 1
	})

def var_0_0._FoldPanels(arg_5_0, arg_5_1, arg_5_2):
	for iter_5_0, iter_5_1 in ipairs(arg_5_0.panels):
		iter_5_1.Fold(arg_5_1, arg_5_2)

	arg_5_0.iconView.Fold(arg_5_1, arg_5_2)
	arg_5_0.chatRoomView.Fold(arg_5_1, arg_5_2)
	arg_5_0.bannerView.Fold(arg_5_1, arg_5_2)
	arg_5_0.actBtnView.Fold(arg_5_1, arg_5_2)
	arg_5_0.buffView.Fold(arg_5_1, arg_5_2)
	arg_5_0.wordView.Fold(arg_5_1, arg_5_2)
	arg_5_0.tagView.Fold(arg_5_1, arg_5_2)

def var_0_0.OnFoldPanels(arg_6_0, arg_6_1):
	if arg_6_1:
		arg_6_0.mainCG.blocksRaycasts = False
	else
		Timer.New(function()
			if arg_6_0.mainCG:
				arg_6_0.mainCG.blocksRaycasts = True, 0.5, 1).Start()

	arg_6_0._FoldPanels(arg_6_1, 0.5)

def var_0_0.OnSwitchToNextShip(arg_8_0, arg_8_1):
	arg_8_0.iconView.Refresh(arg_8_1)

def var_0_0.Refresh(arg_9_0, arg_9_1):
	for iter_9_0, iter_9_1 in ipairs(arg_9_0.panels):
		iter_9_1.Refresh()

	arg_9_0.iconView.Refresh(arg_9_1)
	arg_9_0.chatRoomView.Refresh()
	arg_9_0.buffView.Refresh()
	arg_9_0.actBtnView.Refresh()
	arg_9_0.bannerView.Refresh()
	arg_9_0.tagView.Refresh()
	pg.LayerWeightMgr.GetInstance().SetVisibleViaLayer(arg_9_0._tf, True)

def var_0_0.Disable(arg_10_0):
	for iter_10_0, iter_10_1 in ipairs(arg_10_0.panels):
		iter_10_1.Disable()

	arg_10_0.iconView.Disable()
	arg_10_0.chatRoomView.Disable()
	arg_10_0.buffView.Disable()
	arg_10_0.actBtnView.Disable()
	arg_10_0.bannerView.Disable()
	arg_10_0.wordView.Disable()
	pg.LayerWeightMgr.GetInstance().SetVisibleViaLayer(arg_10_0._tf, False)

def var_0_0.OnDestroy(arg_11_0):
	pg.LayerWeightMgr.GetInstance().DelFromOverlay(arg_11_0._tf, arg_11_0._parentTf)

	for iter_11_0, iter_11_1 in ipairs(arg_11_0.panels or {}):
		iter_11_1.Dispose()

	arg_11_0.panels = None

	if arg_11_0.iconView:
		arg_11_0.iconView.Dispose()

		arg_11_0.iconView = None

	if arg_11_0.chatRoomView:
		arg_11_0.chatRoomView.Dispose()

		arg_11_0.chatRoomView = None

	if arg_11_0.bannerView:
		arg_11_0.bannerView.Dispose()

		arg_11_0.bannerView = None

	if arg_11_0.actBtnView:
		arg_11_0.actBtnView.Dispose()

		arg_11_0.actBtnView = None

	if arg_11_0.buffView:
		arg_11_0.buffView.Dispose()

		arg_11_0.buffView = None

	if arg_11_0.tagView:
		arg_11_0.tagView.Dispose()

		arg_11_0.tagView = None

	if arg_11_0.wordView:
		arg_11_0.wordView.Dispose()

		arg_11_0.wordView = None

	pg.redDotHelper.Clear()

def var_0_0.GetPbList(arg_12_0):
	return {}

def var_0_0.GetCalibrationBG(arg_13_0):
	assert(False)

def var_0_0.GetPaintingOffset(arg_14_0, arg_14_1):
	return MainPaintingShift.New({
		0,
		-10,
		0,
		0,
		0,
		0,
		1,
		1,
		1
	})

def var_0_0.ApplyDefaultResUI(arg_15_0):
	return True

def var_0_0.GetWordView(arg_16_0):
	assert(False)

def var_0_0.GetTagView(arg_17_0):
	assert(False)

def var_0_0.GetTopPanel(arg_18_0):
	assert(False)

def var_0_0.GetRightPanel(arg_19_0):
	assert(False)

def var_0_0.GetLeftPanel(arg_20_0):
	assert(False)

def var_0_0.GetBottomPanel(arg_21_0):
	assert(False)

def var_0_0.GetIconView(arg_22_0):
	assert(False)

def var_0_0.GetChatRoomView(arg_23_0):
	assert(False)

def var_0_0.GetBannerView(arg_24_0):
	assert(False)

def var_0_0.GetActBtnView(arg_25_0):
	assert(False)

def var_0_0.GetBuffView(arg_26_0):
	assert(False)

def var_0_0.GetRedDots(arg_27_0):
	return {}

return var_0_0
