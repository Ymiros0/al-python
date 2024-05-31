local var_0_0 = class("GoldExchangeView")

var_0_0.itemid1 = 12
var_0_0.itemid2 = 24
var_0_0.const = 5
var_0_0.goldNum = {
	[1] = 3000,
	[2] = 15000
}
var_0_0.gemNum = {
	[1] = 100,
	[2] = 450
}

def var_0_0.Ctor(arg_1_0):
	pg.DelegateInfo.New(arg_1_0)
	PoolMgr.GetInstance().GetUI("GoldExchangeWindow", False, function(arg_2_0)
		local var_2_0 = pg.UIMgr.GetInstance().UIMain

		arg_2_0.transform.SetParent(var_2_0.transform, False)

		arg_1_0._go = arg_2_0
		arg_1_0._tf = arg_2_0.transform

		arg_1_0.init())

def var_0_0.init(arg_3_0):
	arg_3_0.initData()
	arg_3_0.initUI()
	arg_3_0.addListener()
	arg_3_0.overLayMyself(True)
	arg_3_0.updateView()

def var_0_0.findTF(arg_4_0, arg_4_1, arg_4_2):
	assert(arg_4_0._tf, "transform should exist")

	return findTF(arg_4_2 or arg_4_0._tf, arg_4_1)

def var_0_0.exit(arg_5_0):
	pg.DelegateInfo.Dispose(arg_5_0)
	arg_5_0.overLayMyself(False)
	PoolMgr.GetInstance().ReturnUI("GoldExchangeWindow", arg_5_0._go)

	pg.goldExchangeMgr = None

def var_0_0.initData(arg_6_0):
	arg_6_0.selectedIndex = 1
	arg_6_0.selectedNum = 1
	arg_6_0.selectedMax = 10
	arg_6_0.player = getProxy(PlayerProxy).getData()

def var_0_0.initUI(arg_7_0):
	arg_7_0.bg = arg_7_0.findTF("BG")
	arg_7_0.btnBack = arg_7_0.findTF("Window/top/btnBack")
	arg_7_0.contentTF = arg_7_0.findTF("Window/Content")
	arg_7_0.goldTF = {}
	arg_7_0.goldTF[1] = {}
	arg_7_0.goldTF_1 = arg_7_0.findTF("Gold1", arg_7_0.contentTF)
	arg_7_0.goldTF[1].itemTF = arg_7_0.goldTF_1
	arg_7_0.goldTF[1].countTF = arg_7_0.findTF("item/icon_bg/count", arg_7_0.goldTF_1)
	arg_7_0.goldTF[1].priceTF = arg_7_0.findTF("item/consume/contain/price", arg_7_0.goldTF_1)
	arg_7_0.goldTF[1].selectedTF = arg_7_0.findTF("item/selected", arg_7_0.goldTF_1)
	arg_7_0.goldTF[1].selectedNumTF = arg_7_0.findTF("reduce/Text", arg_7_0.goldTF[1].selectedTF)

	setText(arg_7_0.goldTF[1].countTF, var_0_0.goldNum[1])
	setText(arg_7_0.goldTF[1].priceTF, var_0_0.gemNum[1])

	arg_7_0.goldTF[2] = {}
	arg_7_0.goldTF_2 = arg_7_0.findTF("Gold2", arg_7_0.contentTF)
	arg_7_0.goldTF[2].itemTF = arg_7_0.goldTF_2
	arg_7_0.goldTF[2].countTF = arg_7_0.findTF("item/icon_bg/count", arg_7_0.goldTF_2)
	arg_7_0.goldTF[2].priceTF = arg_7_0.findTF("item/consume/contain/price", arg_7_0.goldTF_2)
	arg_7_0.goldTF[2].selectedTF = arg_7_0.findTF("item/selected", arg_7_0.goldTF_2)
	arg_7_0.goldTF[2].selectedNumTF = arg_7_0.findTF("reduce/Text", arg_7_0.goldTF[2].selectedTF)

	setText(arg_7_0.goldTF[2].countTF, var_0_0.goldNum[2])
	setText(arg_7_0.goldTF[2].priceTF, var_0_0.gemNum[2])

	arg_7_0.gemCountText = arg_7_0.findTF("Tip/DiamondCount", arg_7_0.contentTF)
	arg_7_0.goldCountText = arg_7_0.findTF("Tip/GoldCount", arg_7_0.contentTF)
	arg_7_0.shopBtn = arg_7_0.findTF("Window/button_container/ShopBtn")
	arg_7_0.confirmBtn = arg_7_0.findTF("Window/button_container/ConfirmBtn")

def var_0_0.addListener(arg_8_0):
	onButton(arg_8_0, arg_8_0.bg, function()
		arg_8_0.exit(), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.btnBack, function()
		arg_8_0.exit(), SFX_CANCEL)
	onButton(arg_8_0, arg_8_0.shopBtn, function()
		if getProxy(ContextProxy).getContextByMediator(ChargeMediator):
			arg_8_0.exit()
		else
			pg.m02.sendNotification(GAME.GO_SCENE, SCENE.CHARGE, {
				wrap = ChargeScene.TYPE_ITEM
			}), SFX_PANEL)
	onButton(arg_8_0, arg_8_0.confirmBtn, function()
		local var_12_0

		if arg_8_0.selectedIndex == 1:
			var_12_0 = var_0_0.itemid1
		elif arg_8_0.selectedIndex == 2:
			var_12_0 = var_0_0.itemid2

		pg.m02.sendNotification(GAME.SHOPPING, {
			isQuickShopping = True,
			id = var_12_0,
			count = arg_8_0.selectedNum
		})
		arg_8_0.exit(), SFX_PANEL)

	for iter_8_0 = 1, 2:
		onButton(arg_8_0, arg_8_0.goldTF[iter_8_0].itemTF, function()
			if arg_8_0.selectedIndex == iter_8_0:
				arg_8_0.selectedNum = math.min(arg_8_0.selectedNum + 1, arg_8_0.selectedMax)
			else
				arg_8_0.selectedIndex = iter_8_0
				arg_8_0.selectedNum = 1

			arg_8_0.updateView(), SFX_PANEL)
		onButton(arg_8_0, arg_8_0.goldTF[iter_8_0].selectedTF, function()
			if arg_8_0.selectedNum > 1:
				arg_8_0.selectedNum = arg_8_0.selectedNum - 1

				arg_8_0.updateView(), SFX_PANEL)

def var_0_0.updateView(arg_15_0):
	for iter_15_0 = 1, 2:
		setActive(arg_15_0.goldTF[iter_15_0].selectedTF, iter_15_0 == arg_15_0.selectedIndex)
		setActive(arg_15_0.goldTF[3 - iter_15_0].selectedTF, iter_15_0 != arg_15_0.selectedIndex)

		if iter_15_0 == arg_15_0.selectedIndex:
			setText(arg_15_0.goldTF[iter_15_0].selectedNumTF, arg_15_0.selectedNum)

	local var_15_0
	local var_15_1
	local var_15_2 = var_0_0.gemNum[arg_15_0.selectedIndex] * arg_15_0.selectedNum
	local var_15_3 = var_0_0.goldNum[arg_15_0.selectedIndex] * arg_15_0.selectedNum

	setText(arg_15_0.gemCountText, var_15_2)

	if var_15_2 > arg_15_0.player.getTotalGem():
		setTextColor(arg_15_0.gemCountText, Color.red)
	else
		setTextColor(arg_15_0.gemCountText, Color.yellow)

	setText(arg_15_0.goldCountText, var_15_3)

def var_0_0.overLayMyself(arg_16_0, arg_16_1):
	if arg_16_1 == True:
		pg.UIMgr.GetInstance().BlurPanel(arg_16_0._tf, False, {
			weight = LayerWeightConst.TOP_LAYER
		})
	else
		pg.UIMgr.GetInstance().UnblurPanel(arg_16_0._tf)

return var_0_0
