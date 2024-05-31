local var_0_0 = class("RefluxShopView", import("..base.BaseSubView"))

var_0_0.GiftPackType = {
	Gold = 3,
	Money = 1,
	Diamond = 2
}
var_0_0.GiftPackTypeName = {
	"pack_type_1",
	"pack_type_2",
	"pack_type_3"
}
var_0_0.Special_ID_Gold = 1
var_0_0.Special_ID_Gem = 14

def var_0_0.getUIName(arg_1_0):
	return "RefluxShopUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.initData()
	arg_2_0.initUI()
	arg_2_0.updateUI()
	var_0_0.SaveEnterTag()

def var_0_0.OnDestroy(arg_3_0):
	for iter_3_0, iter_3_1 in pairs(var_0_0.GiftPackType):
		local var_3_0 = arg_3_0.packTimerList[iter_3_1]

		if var_3_0:
			var_3_0.Stop()

			arg_3_0.packTimerList[iter_3_1] = None

		local var_3_1 = arg_3_0.packNextTimerList[iter_3_1]

		if var_3_1:
			var_3_1.Stop()

			arg_3_0.packNextTimerList[iter_3_1] = None

def var_0_0.OnBackPress(arg_4_0):
	arg_4_0.Hide()

def var_0_0.initData(arg_5_0):
	arg_5_0.refluxProxy = getProxy(RefluxProxy)
	arg_5_0.shopProxy = getProxy(ShopsProxy)

def var_0_0.initUI(arg_6_0):
	local var_6_0 = arg_6_0.findTF("BG/MoneyTip")

	setActive(var_6_0, False)

	arg_6_0.itemTpl = arg_6_0.findTF("ItemTpl")
	arg_6_0.packTpl = arg_6_0.findTF("PackTpl")
	arg_6_0.packContainerTF = arg_6_0.findTF("Container")
	arg_6_0.packItemList = UIItemList.New(arg_6_0.packContainerTF, arg_6_0.packTpl)

	arg_6_0.packItemList.make(function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_0 == UIItemList.EventUpdate:
			arg_7_1 = arg_7_1 + 1

			local var_7_0 = arg_6_0.goodVOList[arg_7_1]

			arg_6_0.updatePack(arg_7_2, var_7_0, arg_7_1))

	arg_6_0.packTimerList = {}
	arg_6_0.packNextTimerList = {}

	local var_6_1 = GetComponent(arg_6_0._tf, "ItemList").prefabItem[0]
	local var_6_2 = tf(Instantiate(var_6_1))

	setActive(arg_6_0.findTF("icon_bg/count", var_6_2), True)
	setParent(var_6_2, arg_6_0.itemTpl)
	setLocalScale(var_6_2, {
		x = 0.45,
		y = 0.45
	})

def var_0_0.updateData(arg_8_0):
	local var_8_0 = arg_8_0.getCurDayGiftPackIDList()
	local var_8_1 = False

	if var_8_0[1]:
		var_8_1 = Goods.Create({
			shop_id = var_8_0[1]
		}, Goods.TYPE_CHARGE)

	local var_8_2 = Goods.Create({
		shop_id = var_8_0[2]
	}, Goods.TYPE_GIFT_PACKAGE)
	local var_8_3 = Goods.Create({
		shop_id = var_8_0[3]
	}, Goods.TYPE_GIFT_PACKAGE)

	arg_8_0.goodVOList = {
		var_8_1,
		var_8_2,
		var_8_3
	}

def var_0_0.updateUI(arg_9_0):
	arg_9_0.updateData()
	arg_9_0.updatePackList()

def var_0_0.updateOutline(arg_10_0):
	local var_10_0 = arg_10_0.packContainerTF.childCount

	for iter_10_0 = 1, var_10_0:
		local var_10_1 = iter_10_0 - 1
		local var_10_2 = arg_10_0.packContainerTF.GetChild(var_10_1)
		local var_10_3 = arg_10_0.findTF("TimeLimit/Text", var_10_2).GetComponent(typeof(Text))

		var_10_3.material = Object.Instantiate(var_10_3.material)

		local var_10_4 = arg_10_0.findTF("Price/Text", var_10_2).GetComponent(typeof(Text))

		var_10_4.material = Object.Instantiate(var_10_4.material)

		local var_10_5 = arg_10_0.findTF("Mask/Text", var_10_2).GetComponent(typeof(Text))

		var_10_5.material = Object.Instantiate(var_10_5.material)

def var_0_0.updateItem(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0.findTF("Frame", arg_11_1)
	local var_11_1 = arg_11_0.findTF("Icon", arg_11_1)
	local var_11_2 = arg_11_0.findTF("Count", arg_11_1)
	local var_11_3 = arg_11_2.type or arg_11_2[1]
	local var_11_4 = arg_11_2.id or arg_11_2[2]
	local var_11_5 = arg_11_2.count or arg_11_2[3]

	setText(var_11_2, var_11_5)

	if var_11_3 != DROP_TYPE_SHIP:
		setImageSprite(var_11_1, LoadSprite(Drop.New({
			type = var_11_3,
			id = var_11_4
		}).getIcon()))
	else
		local var_11_6 = Ship.New({
			configId = var_11_4
		}).getPainting()

		setImageSprite(var_11_1, LoadSprite("QIcon/" .. var_11_6))

	setActive(var_11_0, False)
	setActive(var_11_1, False)
	setActive(var_11_2, False)

	local var_11_7 = arg_11_0.findTF("CommonItemTemplate(Clone)", arg_11_1)

	setActive(var_11_7, True)
	updateDrop(var_11_7, {
		type = var_11_3,
		id = var_11_4,
		count = var_11_5
	})

def var_0_0.updatePack(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	if arg_12_2 == False:
		setActive(arg_12_1, False)

		return
	elif arg_12_3 == var_0_0.GiftPackType.Money and arg_12_0.isBuyEver(arg_12_2.id):
		setActive(arg_12_1, False)

		return
	else
		setActive(arg_12_1, True)

	local var_12_0
	local var_12_1

	if arg_12_3 == var_0_0.GiftPackType.Money:
		-- block empty
	else
		local var_12_2 = arg_12_2.getConfig("effect_args")

		var_12_1 = Item.getConfigData(var_12_2[1])

	local var_12_3 = arg_12_0.findTF("PackIcon", arg_12_1)
	local var_12_4

	if arg_12_3 == var_0_0.GiftPackType.Money:
		var_12_4 = "chargeicon/" .. arg_12_2.getConfig("picture")
	else
		var_12_4 = var_12_1.icon

	setImageSprite(var_12_3, LoadSprite(var_12_4), True)

	local var_12_5 = arg_12_0.findTF("PackName", arg_12_1)

	if arg_12_3 == var_0_0.GiftPackType.Money:
		setText(var_12_5, arg_12_2.getConfig("name_display"))
	else
		setText(var_12_5, var_12_1.name)

	local var_12_6 = arg_12_0.findTF("ItemList", arg_12_1)
	local var_12_7

	if arg_12_3 == var_0_0.GiftPackType.Money:
		var_12_7 = arg_12_2.getConfig("display")
	else
		var_12_7 = var_12_1.display_icon

	local var_12_8 = UIItemList.New(var_12_6, arg_12_0.itemTpl)

	var_12_8.make(function(arg_13_0, arg_13_1, arg_13_2)
		if arg_13_0 == UIItemList.EventUpdate:
			arg_13_1 = arg_13_1 + 1

			local var_13_0 = var_12_7[arg_13_1]

			arg_12_0.updateItem(arg_13_2, var_13_0))
	var_12_8.align(#var_12_7)

	local var_12_9 = arg_12_0.findTF("DescFrame/Text", arg_12_1)

	if arg_12_3 == var_0_0.GiftPackType.Money:
		setText(var_12_9, arg_12_2.getConfig("descrip"))
	else
		setText(var_12_9, var_12_1.display)

	local var_12_10 = arg_12_0.findTF("TimeLimit", arg_12_1)
	local var_12_11 = arg_12_0.findTF("Text", var_12_10)
	local var_12_12 = arg_12_3 != var_0_0.GiftPackType.Money and arg_12_0.isHaveNextPack(var_0_0.GiftPackTypeName[arg_12_3])

	var_12_12 = var_12_12 and not arg_12_0.isBuyEver(arg_12_2.id)

	if var_12_12:
		setActive(var_12_10, True)
		arg_12_0.updatePackTimeLimit(var_12_11, arg_12_3)
	else
		setActive(var_12_10, False)

	local var_12_13 = arg_12_0.findTF("MoneyTag", arg_12_1)

	setActive(var_12_13, arg_12_3 == var_0_0.GiftPackType.Money)

	local var_12_14 = arg_12_0.findTF("Price/IconMoney", arg_12_1)
	local var_12_15 = arg_12_0.findTF("Price/Icon", arg_12_1)
	local var_12_16 = arg_12_0.findTF("Price/Icon/Res", arg_12_1)
	local var_12_17 = arg_12_0.findTF("Price/Text", arg_12_1)

	if arg_12_3 == var_0_0.GiftPackType.Money:
		setActive(var_12_14, True)
		setActive(var_12_15, False)
		setText(var_12_17, arg_12_2.getConfig("money"))
	else
		setActive(var_12_14, False)
		setActive(var_12_15, True)
		setText(var_12_17, arg_12_2.getConfig("resource_num"))

		local var_12_18 = arg_12_2.getConfig("resource_type")
		local var_12_19

		if var_12_18 == var_0_0.Special_ID_Gem:
			var_12_19 = "props/gem"
		elif var_12_18 == var_0_0.Special_ID_Gold:
			var_12_19 = "props/gold"

		setImageSprite(var_12_16, LoadSprite(var_12_19), True)

	local var_12_20 = arg_12_0.findTF("Mask", arg_12_1)
	local var_12_21 = arg_12_0.isBuyEver(arg_12_2.id)

	setActive(var_12_20, var_12_21)

	if var_12_21:
		local var_12_22 = arg_12_0.findTF("NextTime", var_12_20)
		local var_12_23 = arg_12_0.findTF("Text", var_12_20)
		local var_12_24 = arg_12_0.findTF("Sellout", var_12_20)

		if arg_12_0.isHaveNextPack(var_0_0.GiftPackTypeName[arg_12_3]):
			setActive(var_12_22, True)
			setActive(var_12_23, True)
			setActive(var_12_24, False)
			arg_12_0.updatePackNextTime(var_12_23, arg_12_3)
		else
			setActive(var_12_22, False)
			setActive(var_12_23, False)
			setActive(var_12_24, True)

	onButton(arg_12_0, arg_12_1, function()
		if not isActive(var_12_20):
			arg_12_0.confirm(arg_12_2), SFX_PANEL)

def var_0_0.updatePackTimeLimit(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = arg_15_0.getCurDay()
	local var_15_1 = var_0_0.GiftPackTypeName[arg_15_2]
	local var_15_2 = arg_15_0.calcNextGiftPackSecByType(var_15_1, var_15_0)
	local var_15_3 = arg_15_0.packTimerList[arg_15_2]

	if var_15_3:
		var_15_3.Stop()

		arg_15_0.packTimerList[arg_15_2] = None

	local function var_15_4()
		if var_15_2 >= 0:
			local var_16_0 = pg.TimeMgr.GetInstance().DescCDTime(var_15_2)

			setText(arg_15_1, var_16_0)

			var_15_2 = var_15_2 - 1
		else
			var_15_3.Stop()

			arg_15_0.packTimerList[arg_15_2] = None

	var_15_3 = Timer.New(var_15_4, 1, -1)

	var_15_3.Start()

	arg_15_0.packTimerList[arg_15_2] = var_15_3

	var_15_4()

def var_0_0.updatePackNextTime(arg_17_0, arg_17_1, arg_17_2):
	local var_17_0 = arg_17_0.getCurDay()
	local var_17_1 = var_0_0.GiftPackTypeName[arg_17_2]
	local var_17_2 = arg_17_0.calcNextGiftPackSecByType(var_17_1, var_17_0)
	local var_17_3 = arg_17_0.packNextTimerList[arg_17_2]

	if var_17_3:
		var_17_3.Stop()

		arg_17_0.packNextTimerList[arg_17_2] = None

	local function var_17_4()
		if var_17_2 >= 0:
			local var_18_0 = pg.TimeMgr.GetInstance().DescCDTime(var_17_2)

			setText(arg_17_1, var_18_0)

			var_17_2 = var_17_2 - 1
		else
			var_17_3.Stop()

			arg_17_0.packNextTimerList[arg_17_2] = None

	var_17_3 = Timer.New(var_17_4, 1, -1)

	var_17_3.Start()

	arg_17_0.packNextTimerList[arg_17_2] = var_17_3

	var_17_4()

def var_0_0.updatePackList(arg_19_0):
	arg_19_0.packItemList.align(#arg_19_0.goodVOList)

def var_0_0.isShowRedPot():
	if PlayerPrefs.GetInt("RefluxShop_Enter_Day", 0) < getProxy(RefluxProxy).signCount:
		return True
	else
		return False

def var_0_0.SaveEnterTag():
	local var_21_0 = getProxy(RefluxProxy).signCount

	PlayerPrefs.SetInt("RefluxShop_Enter_Day", var_21_0)

def var_0_0.getCurDay(arg_22_0):
	local var_22_0 = arg_22_0.refluxProxy.returnTimestamp
	local var_22_1 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_22_2 = pg.TimeMgr.GetInstance().DiffDay(var_22_0, var_22_1)
	local var_22_3 = #pg.return_giftpack_template.all

	if var_22_2 < var_22_3:
		return var_22_2 + 1
	else
		return var_22_3

def var_0_0.getLevelIndex(arg_23_0, arg_23_1):
	local var_23_0 = arg_23_1 or arg_23_0.getCurDay()
	local var_23_1 = pg.return_giftpack_template[var_23_0].level
	local var_23_2 = arg_23_0.refluxProxy.returnLV
	local var_23_3

	for iter_23_0, iter_23_1 in ipairs(var_23_1):
		local var_23_4 = iter_23_1[1]
		local var_23_5 = iter_23_1[2]

		if var_23_4 <= var_23_2 and var_23_2 <= var_23_5:
			return iter_23_0

def var_0_0.getCurDayGiftPackIDByType(arg_24_0, arg_24_1, arg_24_2):
	local var_24_0 = arg_24_2 or arg_24_0.getCurDay()

	if var_24_0 > #pg.return_giftpack_template.all:
		return False

	local var_24_1 = pg.return_giftpack_template[var_24_0][arg_24_1]
	local var_24_2 = var_24_0

	while var_24_1 == "" and var_24_2 > 1:
		var_24_2 = var_24_2 - 1
		var_24_1 = pg.return_giftpack_template[var_24_2][arg_24_1]

	if var_24_1 == "":
		return False
	else
		return var_24_1[arg_24_0.getLevelIndex(var_24_2)]

def var_0_0.getCurDayGiftPackIDList(arg_25_0):
	local var_25_0 = arg_25_0.getCurDay()

	return {
		[var_0_0.GiftPackType.Money] = arg_25_0.getCurDayGiftPackIDByType("pack_type_1", var_25_0),
		[var_0_0.GiftPackType.Diamond] = arg_25_0.getCurDayGiftPackIDByType("pack_type_2", var_25_0),
		[var_0_0.GiftPackType.Gold] = arg_25_0.getCurDayGiftPackIDByType("pack_type_3", var_25_0)
	}

def var_0_0.getNextGiftPackDayByType(arg_26_0, arg_26_1, arg_26_2):
	local var_26_0 = arg_26_2 or arg_26_0.getCurDay()

	if var_26_0 >= #pg.return_giftpack_template.all:
		return False

	local var_26_1 = var_26_0 + 1
	local var_26_2 = pg.return_giftpack_template[var_26_1][arg_26_1]
	local var_26_3 = var_26_1

	while var_26_2 == "" and var_26_3 > 1 and var_26_3 <= #pg.return_giftpack_template.all:
		var_26_2 = pg.return_giftpack_template[var_26_3][arg_26_1]
		var_26_3 = var_26_3 + 1

	if var_26_2 == "":
		return False
	else
		return var_26_3

def var_0_0.isHaveNextPack(arg_27_0, arg_27_1, arg_27_2):
	local var_27_0 = arg_27_2 or arg_27_0.getCurDay()

	return arg_27_0.getNextGiftPackDayByType(arg_27_1, var_27_0) != False

def var_0_0.calcNextGiftPackSecByType(arg_28_0, arg_28_1, arg_28_2):
	local var_28_0 = arg_28_2 or arg_28_0.getCurDay()
	local var_28_1 = arg_28_0.getNextGiftPackDayByType(arg_28_1, var_28_0)
	local var_28_2 = 86400

	return arg_28_0.refluxProxy.returnTimestamp + (var_28_1 - 1) * var_28_2 - pg.TimeMgr.GetInstance().GetServerTime()

def var_0_0.isBuyEver(arg_29_0, arg_29_1):
	local var_29_0 = getProxy(ShopsProxy)
	local var_29_1 = var_29_0.getChargedList()
	local var_29_2 = var_29_0.GetNormalList()

	return 0 + ChargeConst.getBuyCount(var_29_1, arg_29_1) + ChargeConst.getBuyCount(var_29_2, arg_29_1) > 0

def var_0_0.confirm(arg_30_0, arg_30_1):
	if not arg_30_1:
		return

	arg_30_1 = Clone(arg_30_1)

	if arg_30_1.isChargeType():
		local var_30_0 = not table.contains(arg_30_0.firstChargeIds, arg_30_1.id) and arg_30_1.firstPayDouble()
		local var_30_1 = var_30_0 and 4 or arg_30_1.getConfig("tag")

		if arg_30_1.isMonthCard() or arg_30_1.isGiftBox() or arg_30_1.isItemBox() or arg_30_1.isPassItem():
			local var_30_2 = underscore.map(arg_30_1.getConfig("extra_service_item"), function(arg_31_0)
				return Drop.Create(arg_31_0))
			local var_30_3

			if arg_30_1.isPassItem():
				local var_30_4 = arg_30_1.getConfig("sub_display")
				local var_30_5 = var_30_4[1]
				local var_30_6 = pg.battlepass_event_pt[var_30_5].pt

				var_30_3 = Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = pg.battlepass_event_pt[var_30_5].pt,
					count = var_30_4[2]
				})
				var_30_2 = PlayerConst.MergePassItemDrop(underscore.map(pg.battlepass_event_pt[var_30_5].drop_client_pay, function(arg_32_0)
					return Drop.Create(arg_32_0)))

			local var_30_7 = arg_30_1.getConfig("gem") + arg_30_1.getConfig("extra_gem")
			local var_30_8

			if arg_30_1.isMonthCard():
				var_30_8 = Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResDiamond,
					count = var_30_7
				})
			elif var_30_7 > 0:
				table.insert(var_30_2, Drop.New({
					type = DROP_TYPE_RESOURCE,
					id = PlayerConst.ResDiamond,
					count = var_30_7
				}))

			local var_30_9
			local var_30_10

			if arg_30_1.isPassItem():
				var_30_9 = i18n("battlepass_pay_tip")
			elif arg_30_1.isMonthCard():
				var_30_9 = i18n("charge_title_getitem_month")
				var_30_10 = i18n("charge_title_getitem_soon")
			else
				var_30_9 = i18n("charge_title_getitem")

			local var_30_11 = {
				isChargeType = True,
				icon = "chargeicon/" .. arg_30_1.getConfig("picture"),
				name = arg_30_1.getConfig("name_display"),
				tipExtra = var_30_9,
				extraItems = var_30_2,
				price = arg_30_1.getConfig("money"),
				isLocalPrice = arg_30_1.IsLocalPrice(),
				tagType = var_30_1,
				isMonthCard = arg_30_1.isMonthCard(),
				tipBonus = var_30_10,
				bonusItem = var_30_8,
				extraDrop = var_30_3,
				descExtra = arg_30_1.getConfig("descrip_extra"),
				limitArgs = arg_30_1.getConfig("limit_args"),
				def onYes:()
					if ChargeConst.isNeedSetBirth():
						arg_30_0.emit(RefluxMediator.OPEN_CHARGE_BIRTHDAY)
					else
						pg.m02.sendNotification(GAME.CHARGE_OPERATION, {
							shopId = arg_30_1.id
						})
			}

			arg_30_0.emit(RefluxMediator.OPEN_CHARGE_ITEM_PANEL, var_30_11)
		elif arg_30_1.isGem():
			local var_30_12 = arg_30_1.getConfig("money")
			local var_30_13 = arg_30_1.getConfig("gem")

			if var_30_0:
				var_30_13 = var_30_13 + arg_30_1.getConfig("gem")
			else
				var_30_13 = var_30_13 + arg_30_1.getConfig("extra_gem")

			local var_30_14 = {
				isChargeType = True,
				icon = "chargeicon/" .. arg_30_1.getConfig("picture"),
				name = arg_30_1.getConfig("name_display"),
				price = arg_30_1.getConfig("money"),
				isLocalPrice = arg_30_1.IsLocalPrice(),
				tagType = var_30_1,
				normalTip = i18n("charge_start_tip", var_30_12, var_30_13),
				def onYes:()
					if ChargeConst.isNeedSetBirth():
						arg_30_0.emit(RefluxMediator.OPEN_CHARGE_BIRTHDAY)
					else
						pg.m02.sendNotification(GAME.CHARGE_OPERATION, {
							shopId = arg_30_1.id
						})
			}

			arg_30_0.emit(RefluxMediator.OPEN_CHARGE_ITEM_BOX, var_30_14)
	else
		local var_30_15 = {}
		local var_30_16 = arg_30_1.getConfig("effect_args")
		local var_30_17 = Item.getConfigData(var_30_16[1])
		local var_30_18 = var_30_17.display_icon

		if type(var_30_18) == "table":
			for iter_30_0, iter_30_1 in ipairs(var_30_18):
				table.insert(var_30_15, Drop.Create(iter_30_1))

		local var_30_19 = arg_30_1.getConfig("resource_type") == var_0_0.Special_ID_Gold
		local var_30_20

		if var_30_19:
			var_30_20 = i18n("charge_scene_buy_confirm_gold", arg_30_1.getConfig("resource_num"), var_30_17.name)
		else
			var_30_20 = i18n("charge_scene_buy_confirm", arg_30_1.getConfig("resource_num"), var_30_17.name)

		local var_30_21 = {
			isMonthCard = False,
			isChargeType = False,
			isLocalPrice = False,
			icon = var_30_17.icon,
			name = var_30_17.name,
			tipExtra = i18n("charge_title_getitem"),
			extraItems = var_30_15,
			price = arg_30_1.getConfig("resource_num"),
			tagType = arg_30_1.getConfig("tag"),
			isForceGold = var_30_19,
			def onYes:()
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = var_30_20,
					def onYes:()
						pg.m02.sendNotification(GAME.SHOPPING, {
							count = 1,
							id = arg_30_1.id
						})
				})
		}

		arg_30_0.emit(RefluxMediator.OPEN_CHARGE_ITEM_PANEL, var_30_21)

def var_0_0.getAllRefluxPackID():
	local var_37_0 = {}

	for iter_37_0, iter_37_1 in ipairs(pg.return_giftpack_template.all):
		local var_37_1 = pg.return_giftpack_template[iter_37_1]
		local var_37_2 = var_37_1.pack_type_1
		local var_37_3 = var_37_1.pack_type_2
		local var_37_4 = var_37_1.pack_type_3

		if type(var_37_2) == "table":
			for iter_37_2, iter_37_3 in pairs(var_37_2):
				table.insert(var_37_0, iter_37_3)

		if type(var_37_3) == "table":
			for iter_37_4, iter_37_5 in pairs(var_37_3):
				table.insert(var_37_0, iter_37_5)

		if type(var_37_4) == "table":
			for iter_37_6, iter_37_7 in pairs(var_37_4):
				table.insert(var_37_0, iter_37_7)

	return var_37_0

return var_0_0
