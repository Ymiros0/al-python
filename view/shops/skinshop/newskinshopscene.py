local var_0_0 = class("NewSkinShopScene", import("view.base.BaseUI"))

var_0_0.MODE_OVERVIEW = 1
var_0_0.MODE_EXPERIENCE = 2

local var_0_1 = -1
local var_0_2 = -2
local var_0_3 = -3
local var_0_4 = 9999
local var_0_5 = 9997
local var_0_6 = 9998

var_0_0.PAGE_ALL = var_0_1
var_0_0.optionsPath = {
	"overlay/blur_panel/adapt/top/option"
}

def var_0_0.getUIName(arg_1_0):
	return "NewSkinShopUI"

def var_0_0.forceGC(arg_2_0):
	return True

def var_0_0.ResUISettings(arg_3_0):
	return {
		anim = True,
		showType = PlayerResUI.TYPE_GEM
	}

def var_0_0.GetAllCommodity(arg_4_0):
	return (getProxy(ShipSkinProxy).GetAllSkins())

def var_0_0.GetPlayer(arg_5_0):
	return (getProxy(PlayerProxy).getRawData())

def var_0_0.GetShopTypeIdBySkinId(arg_6_0, arg_6_1):
	local var_6_0 = pg.ship_skin_template.get_id_list_by_shop_type_id

	if not var_0_0.shopTypeIdList:
		var_0_0.shopTypeIdList = {}

	if var_0_0.shopTypeIdList[arg_6_1]:
		return var_0_0.shopTypeIdList[arg_6_1]

	for iter_6_0, iter_6_1 in pairs(var_6_0):
		for iter_6_2, iter_6_3 in ipairs(iter_6_1):
			var_0_0.shopTypeIdList[iter_6_3] = iter_6_0

			if iter_6_3 == arg_6_1:
				return iter_6_0

def var_0_0.GetSkinClassify(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = {}
	local var_7_1 = {}

	for iter_7_0, iter_7_1 in ipairs(arg_7_1):
		local var_7_2 = arg_7_0.GetShopTypeIdBySkinId(iter_7_1.getSkinId())
		local var_7_3 = var_7_2 == 0 and var_0_4 or var_7_2

		var_7_1[var_7_3] = (var_7_1[var_7_3] or 0) + 1

	if #arg_7_0.GetReturnSkins() > 0:
		table.insert(var_7_0, var_0_3)

	for iter_7_2, iter_7_3 in ipairs(pg.skin_page_template.all):
		if iter_7_3 != var_0_5 and iter_7_3 != var_0_6 and (var_7_1[iter_7_3] or 0) > 0:
			table.insert(var_7_0, iter_7_3)

	if arg_7_2 == var_0_0.MODE_EXPERIENCE:
		table.insert(var_7_0, 1, var_0_2)

	table.insert(var_7_0, 1, var_0_1)

	return var_7_0

def var_0_0.GetReturnSkins(arg_8_0):
	if not arg_8_0.returnSkins:
		arg_8_0.returnSkins = getProxy(ShipSkinProxy).GetEncoreSkins()

	return arg_8_0.returnSkins

def var_0_0.GetReturnSkinMap(arg_9_0):
	if not arg_9_0.encoreSkinMap:
		arg_9_0.encoreSkinMap = {}

		local var_9_0 = arg_9_0.GetReturnSkins()

		for iter_9_0, iter_9_1 in ipairs(var_9_0):
			arg_9_0.encoreSkinMap[iter_9_1] = True

	return arg_9_0.encoreSkinMap

def var_0_0.OnFurnitureUpdate(arg_10_0, arg_10_1):
	if not arg_10_0.mainView.commodity:
		return

	local var_10_0 = arg_10_0.mainView.commodity.id

	if Goods.ExistFurniture(var_10_0) and Goods.Id2FurnitureId(var_10_0) == arg_10_1:
		arg_10_0.mainView.Flush(arg_10_0.mainView.commodity)

def var_0_0.OnShopping(arg_11_0, arg_11_1):
	if not arg_11_0.mainView.commodity:
		return

	arg_11_0.mainView.ClosePurchaseView()

	if arg_11_0.mainView.commodity.id == arg_11_1:
		local var_11_0 = arg_11_0.GetAllCommodity()
		local var_11_1 = _.detect(var_11_0, function(arg_12_0)
			return arg_12_0.id == arg_11_1)

		if var_11_1:
			arg_11_0.mainView.Flush(var_11_1)

		arg_11_0.UpdateCouponBtn()
		arg_11_0.UpdateVoucherBtn()
		arg_11_0.UpdateCommodities(var_11_0, False)

		arg_11_0.commodities = var_11_0

def var_0_0.init(arg_13_0):
	arg_13_0.cgGroup = arg_13_0._tf.GetComponent(typeof(CanvasGroup))
	arg_13_0.backBtn = arg_13_0.findTF("overlay/blur_panel/adapt/top/back_btn")
	arg_13_0.atlasBtn = arg_13_0.findTF("overlay/bottom/bg/atlas")
	arg_13_0.prevBtn = arg_13_0.findTF("overlay/bottom/bg/left_arr")
	arg_13_0.nextBtn = arg_13_0.findTF("overlay/bottom/bg/right_arr")
	arg_13_0.live2dFilter = arg_13_0.findTF("overlay/blur_panel/adapt/top/live2d")
	arg_13_0.live2dFilterSel = arg_13_0.live2dFilter.Find("selected")
	arg_13_0.indexBtn = arg_13_0.findTF("overlay/blur_panel/adapt/top/index_btn")
	arg_13_0.indexBtnSel = arg_13_0.indexBtn.Find("sel")
	arg_13_0.inptuTr = arg_13_0.findTF("overlay/blur_panel/adapt/top/search")
	arg_13_0.changeBtn = arg_13_0.findTF("overlay/blur_panel/adapt/top/change_btn")

	setText(arg_13_0.inptuTr.Find("holder"), i18n("skinatlas_search_holder"))

	arg_13_0.couponTr = arg_13_0.findTF("overlay/blur_panel/adapt/top/discount/coupon")
	arg_13_0.couponSelTr = arg_13_0.couponTr.Find("selected")
	arg_13_0.voucherTr = arg_13_0.findTF("overlay/blur_panel/adapt/top/discount/voucher")
	arg_13_0.voucherSelTr = arg_13_0.voucherTr.Find("selected")
	arg_13_0.rollingCircleRect = RollingCircleRect.New(arg_13_0.findTF("overlay/left/mask/content/0"), arg_13_0.findTF("overlay/left"))

	arg_13_0.rollingCircleRect.SetCallback(arg_13_0, var_0_0.OnSelectSkinPage, var_0_0.OnConfirmSkinPage)

	arg_13_0.rollingCircleMaskTr = arg_13_0.findTF("overlay/left")
	arg_13_0.mainView = NewSkinShopMainView.New(arg_13_0._tf, arg_13_0.event)
	arg_13_0.title = arg_13_0.findTF("overlay/blur_panel/adapt/top/title").GetComponent(typeof(Image))
	arg_13_0.titleEn = arg_13_0.findTF("overlay/blur_panel/adapt/top/title_en").GetComponent(typeof(Image))
	arg_13_0.scrollrect = arg_13_0.findTF("overlay/bottom/scroll").GetComponent("LScrollRect")
	arg_13_0.scrollrect.isNewLoadingMethod = True

	function arg_13_0.scrollrect.onInitItem(arg_14_0)
		arg_13_0.OnInitItem(arg_14_0)

	function arg_13_0.scrollrect.onUpdateItem(arg_15_0, arg_15_1)
		arg_13_0.OnUpdateItem(arg_15_0, arg_15_1)

	arg_13_0.emptyTr = arg_13_0.findTF("bgs/empty")
	arg_13_0.defaultIndex = {
		typeIndex = ShipIndexConst.TypeAll,
		campIndex = ShipIndexConst.CampAll,
		rarityIndex = ShipIndexConst.RarityAll,
		extraIndex = SkinIndexLayer.ExtraALL
	}
	Input.multiTouchEnabled = False

def var_0_0.didEnter(arg_16_0):
	onButton(arg_16_0, arg_16_0.backBtn, function()
		arg_16_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_16_0, arg_16_0.atlasBtn, function()
		arg_16_0.emit(NewSkinShopMediator.ON_ATLAS), SFX_PANEL)
	onButton(arg_16_0, arg_16_0.prevBtn, function()
		arg_16_0.OnPrevCommodity(), SFX_PANEL)
	onButton(arg_16_0, arg_16_0.nextBtn, function()
		arg_16_0.OnNextCommodity(), SFX_PANEL)
	onButton(arg_16_0, arg_16_0.indexBtn, function()
		arg_16_0.emit(NewSkinShopMediator.ON_INDEX, {
			def OnFilter:(arg_22_0)
				arg_16_0.OnFilter(arg_22_0),
			defaultIndex = arg_16_0.defaultIndex
		}), SFX_PANEL)
	onInputChanged(arg_16_0, arg_16_0.inptuTr, function()
		arg_16_0.OnSearch())
	onToggle(arg_16_0, arg_16_0.changeBtn, function(arg_24_0)
		if arg_24_0 and getInputText(arg_16_0.inptuTr) != "":
			setInputText(arg_16_0.inptuTr, ""), SFX_PANEL)
	onButton(arg_16_0, arg_16_0.live2dFilter, function()
		arg_16_0.defaultIndex.extraIndex = arg_16_0.defaultIndex.extraIndex == SkinIndexLayer.ExtraL2D and SkinIndexLayer.ExtraALL or SkinIndexLayer.ExtraL2D

		arg_16_0.OnFilter(arg_16_0.defaultIndex), SFX_PANEL)

	arg_16_0.isFilterCoupon = False

	onButton(arg_16_0, arg_16_0.couponTr, function()
		if not SkinCouponActivity.StaticExistActivityAndCoupon():
			arg_16_0.isFilterCoupon = False

			arg_16_0.UpdateCouponBtn()
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

			return

		arg_16_0.isFilterCoupon = not arg_16_0.isFilterCoupon

		setActive(arg_16_0.couponSelTr, arg_16_0.isFilterCoupon)
		arg_16_0.OnFilter(arg_16_0.defaultIndex), SFX_PANEL)

	arg_16_0.isFilterVoucher = False

	onButton(arg_16_0, arg_16_0.voucherTr, function()
		arg_16_0.isFilterVoucher = not arg_16_0.isFilterVoucher

		setActive(arg_16_0.voucherSelTr, arg_16_0.isFilterVoucher)
		arg_16_0.OnFilter(arg_16_0.defaultIndex), SFX_PANEL)
	arg_16_0.SetUp()

def var_0_0.UpdateCouponBtn(arg_28_0):
	local var_28_0 = SkinCouponActivity.StaticExistActivityAndCoupon() and (not arg_28_0.contextData.mode or arg_28_0.contextData.mode == var_0_0.MODE_OVERVIEW)

	if arg_28_0.isFilterCoupon and not var_28_0:
		arg_28_0.isFilterCoupon = False

	arg_28_0.couponTr.localScale = var_28_0 and Vector3(1, 1, 1) or Vector3(0, 0, 0)

def var_0_0.UpdateVoucherBtn(arg_29_0):
	local var_29_0 = #getProxy(BagProxy).GetSkinShopDiscountItemList() > 0 and (not arg_29_0.contextData.mode or arg_29_0.contextData.mode == var_0_0.MODE_OVERVIEW)

	if arg_29_0.isFilterVoucher and not var_29_0:
		arg_29_0.isFilterVoucher = False

	arg_29_0.voucherTr.localScale = var_29_0 and Vector3(1, 1, 1) or Vector3(0, 0, 0)

def var_0_0.OnSelectSkinPage(arg_30_0, arg_30_1):
	if arg_30_0.selectedSkinPageItem:
		setActive(arg_30_0.selectedSkinPageItem._tr.Find("selected"), False)
		setActive(arg_30_0.selectedSkinPageItem._tr.Find("name"), True)

	setActive(arg_30_1._tr.Find("selected"), True)
	setActive(arg_30_1._tr.Find("name"), False)

	arg_30_0.selectedSkinPageItem = arg_30_1

def var_0_0.OnConfirmSkinPage(arg_31_0, arg_31_1):
	local var_31_0 = arg_31_1.GetID()

	if arg_31_0.skinPageID != var_31_0:
		arg_31_0.skinPageID = var_31_0

		if arg_31_0.commodities:
			arg_31_0.UpdateCommodities(arg_31_0.commodities, True)

def var_0_0.OnFilter(arg_32_0, arg_32_1):
	arg_32_0.defaultIndex = {
		typeIndex = arg_32_1.typeIndex,
		campIndex = arg_32_1.campIndex,
		rarityIndex = arg_32_1.rarityIndex,
		extraIndex = arg_32_1.extraIndex
	}

	setActive(arg_32_0.live2dFilterSel, arg_32_1.extraIndex == SkinIndexLayer.ExtraL2D)

	if arg_32_0.commodities:
		arg_32_0.UpdateCommodities(arg_32_0.commodities, True)

	setActive(arg_32_0.indexBtnSel, arg_32_1.typeIndex != ShipIndexConst.TypeAll or arg_32_1.campIndex != ShipIndexConst.CampAll or arg_32_1.rarityIndex != ShipIndexConst.RarityAll or arg_32_1.extraIndex != SkinIndexLayer.ExtraALL)

def var_0_0.OnSearch(arg_33_0):
	if arg_33_0.commodities:
		arg_33_0.UpdateCommodities(arg_33_0.commodities, True)

def var_0_0.SetUp(arg_34_0):
	local var_34_0 = arg_34_0.contextData.mode or var_0_0.MODE_OVERVIEW
	local var_34_1 = arg_34_0.GetAllCommodity()

	arg_34_0.cgGroup.blocksRaycasts = False

	arg_34_0.UpdateTitle(var_34_0)
	arg_34_0.UpdateCouponBtn()
	arg_34_0.UpdateVoucherBtn()
	setActive(arg_34_0.rollingCircleMaskTr, var_34_0 == var_0_0.MODE_OVERVIEW)

	if var_34_0 == var_0_0.MODE_EXPERIENCE:
		getProxy(SettingsProxy).SetNextTipTimeLimitSkinShop()

	arg_34_0.skinPageID = var_34_0 == var_0_0.MODE_EXPERIENCE and var_0_2 or var_0_1

	parallelAsync({
		function(arg_35_0)
			arg_34_0.InitSkinClassify(var_34_1, var_34_0, arg_35_0),
		function(arg_36_0)
			seriesAsync({
				function(arg_37_0)
					onNextTick(arg_37_0),
				function(arg_38_0)
					if arg_34_0.exited:
						return

					arg_34_0.UpdateCommodities(var_34_1, True, arg_38_0)
			}, arg_36_0)
	}, function()
		arg_34_0.commodities = var_34_1
		arg_34_0.cgGroup.blocksRaycasts = True)

def var_0_0.UpdateTitle(arg_40_0, arg_40_1):
	local var_40_0 = {
		"huanzhuangshagndian",
		"title_01"
	}

	arg_40_0.title.sprite = GetSpriteFromAtlas("ui/SkinShopUI_atlas", var_40_0[arg_40_1])

	arg_40_0.title.SetNativeSize()

	local var_40_1 = {
		"huanzhuangshagndian_en",
		"title_en_01"
	}

	arg_40_0.titleEn.sprite = GetSpriteFromAtlas("ui/SkinShopUI_atlas", var_40_1[arg_40_1])

	arg_40_0.titleEn.SetNativeSize()

local function var_0_7(arg_41_0, arg_41_1)
	local var_41_0 = pg.skin_page_template
	local var_41_1 = arg_41_1.GetID()
	local var_41_2
	local var_41_3

	if var_41_1 == var_0_1 or var_41_1 == var_0_2:
		var_41_2, var_41_3 = "text_all", "ALL"
	elif var_41_1 == var_0_3:
		var_41_2, var_41_3 = "text_fanchang", "RETURN"
	else
		var_41_2, var_41_3 = "text_" .. var_41_0[var_41_1].res, var_41_0[var_41_1].english_name

	LoadSpriteAtlasAsync("SkinClassified", var_41_2 .. "01", function(arg_42_0)
		if arg_41_0.exited:
			return

		local var_42_0 = arg_41_1._tr.Find("name").GetComponent(typeof(Image))

		var_42_0.sprite = arg_42_0

		var_42_0.SetNativeSize())
	LoadSpriteAtlasAsync("SkinClassified", var_41_2, function(arg_43_0)
		if arg_41_0.exited:
			return

		local var_43_0 = arg_41_1._tr.Find("selected/Image").GetComponent(typeof(Image))

		var_43_0.sprite = arg_43_0

		var_43_0.SetNativeSize())
	setText(arg_41_1._tr.Find("eng"), var_41_3)

def var_0_0.InitSkinClassify(arg_44_0, arg_44_1, arg_44_2, arg_44_3):
	local var_44_0 = arg_44_0.GetSkinClassify(arg_44_1, arg_44_2)
	local var_44_1 = {}

	for iter_44_0, iter_44_1 in ipairs(var_44_0):
		table.insert(var_44_1, function(arg_45_0)
			if arg_44_0.exited:
				return

			local var_45_0 = arg_44_0.rollingCircleRect.AddItem(iter_44_1)

			var_0_7(arg_44_0, var_45_0)

			if (iter_44_0 - 1) % 5 == 0 or iter_44_0 == #var_44_0:
				onNextTick(arg_45_0)
			else
				arg_45_0())

	seriesAsync(var_44_1, function()
		if arg_44_0.exited:
			return

		arg_44_0.rollingCircleRect.ScrollTo(arg_44_0.skinPageID)
		arg_44_3())

def var_0_0.IsType(arg_47_0, arg_47_1, arg_47_2):
	if arg_47_2.getConfig("genre") == ShopArgs.SkinShopTimeLimit:
		return arg_47_1 == var_0_2
	elif arg_47_1 == var_0_1:
		return True
	elif arg_47_1 == var_0_3 and arg_47_0.GetReturnSkinMap()[arg_47_2.id]:
		return True
	else
		local var_47_0 = arg_47_0.GetShopTypeIdBySkinId(arg_47_2.getSkinId())

		return (var_47_0 == 0 and var_0_4 or var_47_0) == arg_47_1

	return False

def var_0_0.ToVShip(arg_48_0, arg_48_1):
	if not arg_48_0.vship:
		arg_48_0.vship = {}

		function arg_48_0.vship.getNation()
			return arg_48_0.vship.config.nationality

		function arg_48_0.vship.getShipType()
			return arg_48_0.vship.config.type

		function arg_48_0.vship.getTeamType()
			return TeamType.GetTeamFromShipType(arg_48_0.vship.config.type)

		function arg_48_0.vship.getRarity()
			return arg_48_0.vship.config.rarity

	arg_48_0.vship.config = arg_48_1

	return arg_48_0.vship

def var_0_0.IsAllFilter(arg_53_0, arg_53_1):
	return arg_53_1.typeIndex == ShipIndexConst.TypeAll and arg_53_1.campIndex == ShipIndexConst.CampAll and arg_53_1.rarityIndex == ShipIndexConst.RarityAll and arg_53_1.extraIndex == SkinIndexLayer.ExtraALL

def var_0_0.IsFilterType(arg_54_0, arg_54_1, arg_54_2):
	if arg_54_0.IsAllFilter(arg_54_1):
		return True

	local var_54_0 = arg_54_2.getSkinId()
	local var_54_1 = ShipSkin.New({
		id = var_54_0
	})
	local var_54_2 = var_54_1.GetDefaultShipConfig()

	if not var_54_2:
		return False

	local var_54_3 = arg_54_0.ToVShip(var_54_2)
	local var_54_4 = ShipIndexConst.filterByType(var_54_3, arg_54_1.typeIndex)
	local var_54_5 = ShipIndexConst.filterByCamp(var_54_3, arg_54_1.campIndex)
	local var_54_6 = ShipIndexConst.filterByRarity(var_54_3, arg_54_1.rarityIndex)
	local var_54_7 = SkinIndexLayer.filterByExtra(var_54_1, arg_54_1.extraIndex)

	return var_54_4 and var_54_5 and var_54_6 and var_54_7

def var_0_0.IsSearchType(arg_55_0, arg_55_1, arg_55_2):
	if not arg_55_1 or arg_55_1 == "":
		return True

	local var_55_0 = arg_55_2.getSkinId()

	return ShipSkin.New({
		id = var_55_0
	}).IsMatchKey(arg_55_1)

local function var_0_8(arg_56_0, arg_56_1, arg_56_2)
	local var_56_0 = arg_56_2[arg_56_0.id]
	local var_56_1 = arg_56_2[arg_56_1.id]

	if var_56_0 == var_56_1:
		return arg_56_0.id < arg_56_1.id
	else
		return var_56_1 < var_56_0

def var_0_0.Sort(arg_57_0, arg_57_1, arg_57_2, arg_57_3):
	local var_57_0 = arg_57_1.buyCount == 0 and 1 or 0
	local var_57_1 = arg_57_2.buyCount == 0 and 1 or 0

	if var_57_0 == var_57_1:
		local var_57_2 = arg_57_1.getConfig("order")
		local var_57_3 = arg_57_2.getConfig("order")

		if var_57_2 == var_57_3:
			return var_0_8(arg_57_1, arg_57_2, arg_57_3)
		else
			return var_57_2 < var_57_3
	else
		return var_57_1 < var_57_0

def var_0_0.IsCouponType(arg_58_0, arg_58_1, arg_58_2):
	if arg_58_1 and not SkinCouponActivity.StaticIsShop(arg_58_2.id):
		return False

	return True

def var_0_0.IsVoucherType(arg_59_0, arg_59_1, arg_59_2):
	if arg_59_1 and not arg_59_2:
		return False

	return True

def var_0_0.UpdateCommodities(arg_60_0, arg_60_1, arg_60_2, arg_60_3):
	arg_60_0.ClearCards()

	arg_60_0.cards = {}
	arg_60_0.displays = {}
	arg_60_0.canUseVoucherCache = {}

	local var_60_0 = getInputText(arg_60_0.inptuTr)
	local var_60_1 = getProxy(BagProxy).GetSkinShopDiscountItemList()

	for iter_60_0, iter_60_1 in ipairs(arg_60_1):
		local var_60_2 = iter_60_1.StaticCanUseVoucherType(var_60_1)

		if arg_60_0.IsType(arg_60_0.skinPageID, iter_60_1) and arg_60_0.IsFilterType(arg_60_0.defaultIndex, iter_60_1) and arg_60_0.IsSearchType(var_60_0, iter_60_1) and arg_60_0.IsCouponType(arg_60_0.isFilterCoupon, iter_60_1) and arg_60_0.IsVoucherType(arg_60_0.isFilterVoucher, var_60_2):
			table.insert(arg_60_0.displays, iter_60_1)

		arg_60_0.canUseVoucherCache[iter_60_1.id] = var_60_2

	local var_60_3 = {}

	for iter_60_2, iter_60_3 in ipairs(arg_60_0.displays):
		local var_60_4 = iter_60_3.type == Goods.TYPE_ACTIVITY or iter_60_3.type == Goods.TYPE_ACTIVITY_EXTRA
		local var_60_5 = 0

		if not var_60_4:
			var_60_5 = iter_60_3.GetPrice()

		var_60_3[iter_60_3.id] = var_60_5

	table.sort(arg_60_0.displays, function(arg_61_0, arg_61_1)
		return arg_60_0.Sort(arg_61_0, arg_61_1, var_60_3))

	if arg_60_2:
		arg_60_0.triggerFirstCard = True

		arg_60_0.scrollrect.SetTotalCount(#arg_60_0.displays, 0)
	else
		arg_60_0.scrollrect.SetTotalCount(#arg_60_0.displays)

	local var_60_6 = #arg_60_0.displays <= 0

	setActive(arg_60_0.emptyTr, var_60_6)

	if var_60_6:
		arg_60_0.mainView.Flush(None)

	if arg_60_3:
		arg_60_3()

def var_0_0.OnInitItem(arg_62_0, arg_62_1):
	local var_62_0 = NewShopSkinCard.New(arg_62_1)

	onButton(arg_62_0, var_62_0._go, function()
		if not var_62_0.commodity:
			return

		for iter_63_0, iter_63_1 in pairs(arg_62_0.cards):
			iter_63_1.UpdateSelected(False)

		arg_62_0.selectedId = var_62_0.commodity.id

		var_62_0.UpdateSelected(True)
		arg_62_0.UpdateMainView(var_62_0.commodity)
		arg_62_0.GCHandle(), SFX_PANEL)

	arg_62_0.cards[arg_62_1] = var_62_0

def var_0_0.OnUpdateItem(arg_64_0, arg_64_1, arg_64_2):
	local var_64_0 = arg_64_0.cards[arg_64_2]

	if not var_64_0:
		arg_64_0.OnInitItem(arg_64_2)

		var_64_0 = arg_64_0.cards[arg_64_2]

	local var_64_1 = arg_64_0.displays[arg_64_1 + 1]

	if not var_64_1:
		return

	local var_64_2 = arg_64_0.selectedId == var_64_1.id
	local var_64_3 = arg_64_0.GetReturnSkinMap()[var_64_1.id]

	var_64_0.Update(var_64_1, var_64_2, var_64_3)

	if arg_64_0.triggerFirstCard and arg_64_1 == 0:
		arg_64_0.triggerFirstCard = None

		triggerButton(var_64_0._go)

def var_0_0.GCHandle(arg_65_0):
	var_0_0.GCCNT = (var_0_0.GCCNT or 0) + 1

	if var_0_0.GCCNT == 3:
		gcAll()

		var_0_0.GCCNT = 0

def var_0_0.UpdateMainView(arg_66_0, arg_66_1):
	arg_66_0.mainView.Flush(arg_66_1)

def var_0_0.GetCommodityIndex(arg_67_0, arg_67_1):
	for iter_67_0, iter_67_1 in ipairs(arg_67_0.displays):
		if iter_67_1.id == arg_67_1:
			return iter_67_0

def var_0_0.OnPrevCommodity(arg_68_0):
	if not arg_68_0.selectedId:
		return

	local var_68_0 = arg_68_0.GetCommodityIndex(arg_68_0.selectedId)

	if var_68_0 - 1 > 0:
		arg_68_0.TriggerCommodity(var_68_0, -1)

def var_0_0.OnNextCommodity(arg_69_0):
	if not arg_69_0.selectedId:
		return

	local var_69_0 = arg_69_0.GetCommodityIndex(arg_69_0.selectedId)

	if var_69_0 + 1 <= #arg_69_0.displays:
		arg_69_0.TriggerCommodity(var_69_0, 1)

def var_0_0.CheckCardBound(arg_70_0, arg_70_1, arg_70_2, arg_70_3, arg_70_4):
	local var_70_0 = getBounds(arg_70_0.scrollrect.gameObject.transform)

	if arg_70_3:
		local var_70_1 = getBounds(arg_70_2._tf)
		local var_70_2 = getBounds(arg_70_1._tf)

		if math.ceil(var_70_2.GetMax().x - var_70_0.GetMax().x) > var_70_1.size.x:
			local var_70_3 = arg_70_0.scrollrect.HeadIndexToValue(arg_70_4 - 1) - arg_70_0.scrollrect.HeadIndexToValue(arg_70_4)
			local var_70_4 = arg_70_0.scrollrect.value - var_70_3

			arg_70_0.scrollrect.SetNormalizedPosition(var_70_4, 0)
	else
		local var_70_5 = getBounds(arg_70_1._tf)

		if getBounds(arg_70_1._tf.parent).GetMin().x < var_70_0.GetMin().x and var_70_5.GetMin().x < var_70_0.GetMin().x:
			local var_70_6 = arg_70_0.scrollrect.HeadIndexToValue(arg_70_4 - 1)

			arg_70_0.scrollrect.SetNormalizedPosition(var_70_6, 0)

def var_0_0.TriggerCommodity(arg_71_0, arg_71_1, arg_71_2):
	local var_71_0 = arg_71_0.displays[arg_71_1]
	local var_71_1 = arg_71_0.displays[arg_71_1 + arg_71_2]
	local var_71_2
	local var_71_3

	for iter_71_0, iter_71_1 in pairs(arg_71_0.cards):
		if iter_71_1._tf.gameObject.name != "-1":
			if iter_71_1.commodity.id == var_71_1.id:
				var_71_2 = iter_71_1
			elif iter_71_1.commodity.id == var_71_0.id:
				var_71_3 = iter_71_1

	if var_71_2:
		triggerButton(var_71_2._tf)

	if var_71_2 and var_71_3:
		arg_71_0.CheckCardBound(var_71_2, var_71_3, arg_71_2 > 0, arg_71_1 + arg_71_2)

def var_0_0.ClearCards(arg_72_0):
	if not arg_72_0.cards:
		return

	for iter_72_0, iter_72_1 in pairs(arg_72_0.cards):
		iter_72_1.Dispose()

	arg_72_0.cards = None

def var_0_0.willExit(arg_73_0):
	arg_73_0.ClearCards()
	ClearLScrollrect(arg_73_0.scrollrect)

	if arg_73_0.rollingCircleRect:
		arg_73_0.rollingCircleRect.Dispose()

		arg_73_0.rollingCircleRect = None

	Input.multiTouchEnabled = True

	if arg_73_0.mainView:
		arg_73_0.mainView.Dispose()

		arg_73_0.mainView = None

	var_0_0.shopTypeIdList = None

return var_0_0
