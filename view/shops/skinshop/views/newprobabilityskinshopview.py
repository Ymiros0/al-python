local var_0_0 = class("NewProbabilitySkinShopView", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "ProbabilitySkinShopItem"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.purchaseBtn = arg_2_0.findTF("frame")
	arg_2_0.tipTxt = arg_2_0.findTF("tip/Text").GetComponent(typeof(Text))
	arg_2_0.icon = arg_2_0.findTF("frame/icon/Image").GetComponent(typeof(Image))
	arg_2_0.tag = arg_2_0.findTF("frame/icon/tag").GetComponent(typeof(Image))
	arg_2_0.nameTxt = arg_2_0.findTF("frame/name/Text").GetComponent(typeof(Text))
	arg_2_0.priceTxt = arg_2_0.findTF("frame/price").GetComponent(typeof(Text))
	arg_2_0.descTxt = arg_2_0.findTF("frame/desc").GetComponent(typeof(Text))
	arg_2_0.limitTxt = arg_2_0.findTF("frame/count").GetComponent(typeof(Text))
	arg_2_0.uiList = UIItemList.New(arg_2_0.findTF("frame/awards"), arg_2_0.findTF("frame/awards/award"))

	arg_2_0._tf.SetSiblingIndex(2)

def var_0_0.Show(arg_3_0, arg_3_1):
	var_0_0.super.Show(arg_3_0)
	arg_3_0.UpdateCommodity(arg_3_1)
	arg_3_0.UpdateTip()

def var_0_0.Flush(arg_4_0, arg_4_1):
	arg_4_0.UpdateCommodity(arg_4_1)

local function var_0_1(arg_5_0)
	return ({
		"hot",
		"new_tag",
		"tuijian",
		"shuangbei_tag",
		"activity",
		"xianshi"
	})[arg_5_0] or "hot"

local function var_0_2(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_1.getConfig("display")

	arg_6_0.uiList.make(function(arg_7_0, arg_7_1, arg_7_2)
		if arg_7_0 == UIItemList.EventUpdate:
			local var_7_0 = var_6_0[arg_7_1 + 1]
			local var_7_1 = {
				type = var_7_0[1],
				id = var_7_0[2],
				count = var_7_0[3]
			}

			updateDrop(arg_7_2, var_7_1))
	arg_6_0.uiList.align(#var_6_0)

def var_0_0.UpdateCommodity(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.getConfig("picture")

	arg_8_0.icon.sprite = LoadSprite("ChargeIcon/" .. var_8_0)

	arg_8_0.icon.SetNativeSize()

	arg_8_0.nameTxt.text = arg_8_1.getConfig("name_display")
	arg_8_0.priceTxt.text = "$" .. arg_8_1.getConfig("money")
	arg_8_0.limitTxt.text = arg_8_1.GetLimitDesc()
	arg_8_0.descTxt.text = arg_8_1.getConfig("descrip")

	local var_8_1 = arg_8_1.getConfig("tag")

	arg_8_0.tag.sprite = LoadSprite("chargeTag", var_0_1(var_8_1))

	arg_8_0.tag.SetNativeSize()
	var_0_2(arg_8_0, arg_8_1)
	onButton(arg_8_0, arg_8_0.purchaseBtn, function()
		if arg_8_1.canPurchase():
			arg_8_0.OnCharge(arg_8_1)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("buy_countLimit")), SFX_PANEL)

def var_0_0.OnCharge(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1
	local var_10_1 = underscore.map(var_10_0.getConfig("extra_service_item"), function(arg_11_0)
		return {
			type = arg_11_0[1],
			id = arg_11_0[2],
			count = arg_11_0[3]
		})
	local var_10_2 = var_10_0.getConfig("gem") + var_10_0.getConfig("extra_gem")

	if var_10_2 > 0:
		table.insert(var_10_1, {
			id = 4,
			type = 1,
			count = var_10_2
		})

	local var_10_3 = {
		isMonthCard = False,
		isChargeType = True,
		icon = "chargeicon/" .. var_10_0.getConfig("picture"),
		name = var_10_0.getConfig("name_display"),
		tipExtra = i18n("charge_title_getitem"),
		extraItems = var_10_1,
		price = var_10_0.getConfig("money"),
		isLocalPrice = var_10_0.IsLocalPrice(),
		tagType = var_10_0.getConfig("tag"),
		descExtra = var_10_0.getConfig("descrip_extra"),
		limitArgs = var_10_0.getConfig("limit_args"),
		def onYes:()
			if ChargeConst.isNeedSetBirth():
				arg_10_0.emit(NewProbabilitySkinShopMediator.OPEN_CHARGE_BIRTHDAY)
			else
				arg_10_0.emit(NewProbabilitySkinShopMediator.CHARGE, var_10_0.id)
	}

	arg_10_0.emit(NewProbabilitySkinShopMediator.OPEN_CHARGE_ITEM_PANEL, var_10_3)

def var_0_0.UpdateTip(arg_13_0):
	arg_13_0.tipTxt.text = i18n("probabilityskinshop_tip")

def var_0_0.OnDestroy(arg_14_0):
	return

return var_0_0
