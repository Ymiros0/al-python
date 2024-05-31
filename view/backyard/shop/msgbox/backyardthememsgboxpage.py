local var_0_0 = class("BackYardThemeMsgBoxPage", import(".BackYardFurnitureMsgBoxPage"))

def var_0_0.getUIName(arg_1_0):
	return "ThemeMsgboxPage"

def var_0_0.OnLoaded(arg_2_0):
	var_0_0.super.OnLoaded(arg_2_0)

	arg_2_0.purchaseTr = arg_2_0.findTF("frame/tip")
	arg_2_0.purchase = arg_2_0.findTF("frame/tip/Text").GetComponent(typeof(Text))

def var_0_0.OnInit(arg_3_0):
	var_0_0.super.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.gemPurchaseBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.goldPurchaseBtn, function()
		local var_5_0 = arg_3_0.GetAddList()

		if #var_5_0 <= 0:
			return

		local var_5_1 = _.map(var_5_0, function(arg_6_0)
			return arg_6_0.id)

		arg_3_0.emit(NewBackYardShopMediator.ON_SHOPPING, var_5_1, PlayerConst.ResDormMoney)
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.SetUp(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	arg_7_0.dorm = arg_7_2
	arg_7_0.themeVO = arg_7_1
	arg_7_0.player = arg_7_3
	arg_7_0.count = 1
	arg_7_0.maxCount = 1

	arg_7_0.UpdateMainInfo()
	arg_7_0.UpdateBtns()
	arg_7_0.UpdatePrice()
	arg_7_0.Show()

	arg_7_0.purchase.text = i18n("purchase_backyard_theme_desc_for_onekey")

	setActive(arg_7_0.purchaseTr, True)
	setText(arg_7_0.gemPurchaseBtn.Find("content/Text"), i18n("word_buy"))
	setText(arg_7_0.goldPurchaseBtn.Find("content/Text"), i18n("word_buy"))

def var_0_0.UpdateMainInfo(arg_8_0):
	arg_8_0.nameTxt.text = arg_8_0.themeVO.getConfig("name")
	arg_8_0.themeTxt.text = ""
	arg_8_0.descTxt.text = arg_8_0.themeVO.getConfig("desc")
	arg_8_0.maxCnt.text = ""
	arg_8_0.icon.sprite = GetSpriteFromAtlas("BackYardTheme/" .. arg_8_0.themeVO.id, "")
	tf(arg_8_0.icon.gameObject).sizeDelta = Vector2(336, 336)
	arg_8_0.maxBtnTxt.text = "+" .. arg_8_0.maxCount

def var_0_0.UpdateBtns(arg_9_0):
	local var_9_0 = True
	local var_9_1 = False

	setActive(arg_9_0.goldPurchaseBtn, var_9_0)
	setActive(arg_9_0.gemPurchaseBtn, var_9_1)
	setActive(arg_9_0.gemIcon, var_9_1)
	setActive(arg_9_0.gemCount, var_9_1)
	setActive(arg_9_0.goldIcon, var_9_0)
	setActive(arg_9_0.goldCount, var_9_0)
	setActive(arg_9_0.line, var_9_0 and var_9_1)

def var_0_0.GetAddList(arg_10_0):
	local var_10_0 = {}
	local var_10_1 = arg_10_0.themeVO.GetFurnitures()
	local var_10_2 = arg_10_0.dorm.GetPurchasedFurnitures()

	for iter_10_0, iter_10_1 in ipairs(var_10_1):
		if not var_10_2[iter_10_1]:
			table.insert(var_10_0, Furniture.New({
				id = iter_10_1
			}))

	return var_10_0

def var_0_0.UpdatePrice(arg_11_0):
	local var_11_0 = arg_11_0.GetAddList()
	local var_11_1 = 0
	local var_11_2 = _.reduce(var_11_0, 0, function(arg_12_0, arg_12_1)
		return arg_12_0 + arg_12_1.getPrice(PlayerConst.ResDormMoney))

	arg_11_0.gemCount.text = var_11_1 * arg_11_0.count
	arg_11_0.goldCount.text = var_11_2 * arg_11_0.count

	arg_11_0.UpdateEnergy(var_11_0)

def var_0_0.OnDestroy(arg_13_0):
	return

return var_0_0
