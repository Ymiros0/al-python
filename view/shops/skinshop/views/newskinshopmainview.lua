local var_0_0 = class("NewSkinShopMainView", import("view.base.BaseEventLogic"))

var_0_0.EVT_SHOW_OR_HIDE_PURCHASE_VIEW = "NewSkinShopMainView:EVT_SHOW_OR_HIDE_PURCHASE_VIEW"
var_0_0.EVT_ON_PURCHASE = "NewSkinShopMainView:EVT_ON_PURCHASE"

local var_0_1 = 1
local var_0_2 = 2
local var_0_3 = 3
local var_0_4 = 1
local var_0_5 = 2
local var_0_6 = 3
local var_0_7 = 4
local var_0_8 = 5
local var_0_9 = 6
local var_0_10 = 7
local var_0_11 = 8

local function var_0_12(arg_1_0)
	if not var_0_0.obtainBtnSpriteNames then
		var_0_0.obtainBtnSpriteNames = {
			[var_0_4] = "yigoumai_butten",
			[var_0_5] = "goumai_butten",
			[var_0_6] = "qianwanghuoqu_butten",
			[var_0_7] = "item_buy",
			[var_0_8] = "furniture_shop",
			[var_0_9] = "tiyan_btn",
			[var_0_10] = "item_buy",
			[var_0_11] = "buy_with_gift"
		}
	end

	return var_0_0.obtainBtnSpriteNames[arg_1_0]
end

function var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2)
	pg.DelegateInfo.New(arg_2_0)
	var_0_0.super.Ctor(arg_2_0, arg_2_2)

	arg_2_0._go = arg_2_1.gameObject
	arg_2_0._tf = arg_2_1
	arg_2_0.overlay = arg_2_0._tf:Find("overlay")
	arg_2_0.titleTr = arg_2_0._tf:Find("overlay/title")
	arg_2_0.skinNameTxt = arg_2_0._tf:Find("overlay/title/skin_name"):GetComponent(typeof(Text))
	arg_2_0.shipNameTxt = arg_2_0._tf:Find("overlay/title/name"):GetComponent(typeof(Text))
	arg_2_0.timeLimitTr = arg_2_0._tf:Find("overlay/title/limit_time")
	arg_2_0.timeLimitTxt = arg_2_0.timeLimitTr:Find("Text"):GetComponent(typeof(Text))
	arg_2_0.rightTr = arg_2_0._tf:Find("overlay/right")
	arg_2_0.uiTagList = UIItemList.New(arg_2_0._tf:Find("overlay/right/tags"), arg_2_0._tf:Find("overlay/right/tags/tpl"))
	arg_2_0.charContainer = arg_2_0._tf:Find("overlay/right/char")
	arg_2_0.furnitureContainer = arg_2_0._tf:Find("overlay/right/fur")
	arg_2_0.charBg = arg_2_0._tf:Find("overlay/right/bg/char")
	arg_2_0.furnitureBg = arg_2_0._tf:Find("overlay/right/bg/furn")
	arg_2_0.switchPreviewBtn = arg_2_0._tf:Find("overlay/right/switch")
	arg_2_0.obtainBtn = arg_2_0._tf:Find("overlay/right/price/btn")
	arg_2_0.obtainBtnImg = arg_2_0.obtainBtn:GetComponent(typeof(Image))
	arg_2_0.giftTag = arg_2_0.obtainBtn:Find("tag")
	arg_2_0.giftItem = arg_2_0.obtainBtn:Find("item")
	arg_2_0.giftText = arg_2_0._tf:Find("overlay/right/price/btn/Text"):GetComponent(typeof(Text))
	arg_2_0.consumeTr = arg_2_0._tf:Find("overlay/right/price/consume")
	arg_2_0.consumeRealPriceTxt = arg_2_0.consumeTr:Find("Text"):GetComponent(typeof(Text))
	arg_2_0.consumePriceTxt = arg_2_0.consumeTr:Find("originalprice/Text"):GetComponent(typeof(Text))
	arg_2_0.experienceTr = arg_2_0._tf:Find("overlay/right/price/timelimt")
	arg_2_0.experienceTxt = arg_2_0.experienceTr:Find("consume/Text"):GetComponent(typeof(Text))
	arg_2_0.dynamicToggle = arg_2_0._tf:Find("overlay/right/toggles/l2d_preview")
	arg_2_0.showBgToggle = arg_2_0._tf:Find("overlay/right/toggles/hideObjToggle")
	arg_2_0.dynamicResToggle = arg_2_0._tf:Find("overlay/right/toggles/l2d_res_state")
	arg_2_0.dynamicResDownaload = arg_2_0._tf:Find("overlay/right/toggles/l2d_res_state/downloaded")
	arg_2_0.dynamicResUnDownaload = arg_2_0._tf:Find("overlay/right/toggles/l2d_res_state/undownload")
	arg_2_0.paintingTF = arg_2_0._tf:Find("painting/paint")
	arg_2_0.live2dContainer = arg_2_0._tf:Find("painting/paint/live2d")
	arg_2_0.spTF = arg_2_0._tf:Find("painting/paint/spinePainting")
	arg_2_0.spBg = arg_2_0._tf:Find("painting/paintBg/spinePainting")
	arg_2_0.bgsGo = arg_2_0._tf:Find("bgs").gameObject
	arg_2_0.diffBg = arg_2_0._tf:Find("bgs/diffBg/bg")
	arg_2_0.defaultBg = arg_2_0._tf:Find("bgs/default")
	arg_2_0.downloads = {}
	arg_2_0.obtainBtnSprites = {}
	arg_2_0.isToggleDynamic = false
	arg_2_0.isToggleShowBg = true
	arg_2_0.isPreviewFurniture = false
	arg_2_0.interactionPreview = BackYardInteractionPreview.New(arg_2_0.furnitureContainer, Vector3(0, 0, 0))
	arg_2_0.voucherMsgBox = SkinVoucherMsgBox.New(pg.UIMgr.GetInstance().OverlayMain)
	arg_2_0.purchaseView = NewSkinShopPurchaseView.New(arg_2_0._tf, arg_2_2)

	arg_2_0:RegisterEvent()
end

function var_0_0.RegisterEvent(arg_3_0)
	arg_3_0:bind(var_0_0.EVT_SHOW_OR_HIDE_PURCHASE_VIEW, function(arg_4_0, arg_4_1)
		setAnchoredPosition(arg_3_0.paintingTF, {
			x = arg_4_1 and -440 or -120
		})
		setActive(arg_3_0.overlay, not arg_4_1)
	end)
	arg_3_0:bind(var_0_0.EVT_ON_PURCHASE, function(arg_5_0, arg_5_1)
		local var_5_0 = arg_3_0:GetObtainBtnState(arg_5_1)

		arg_3_0:OnClickBtn(var_5_0, arg_5_1)
	end)
end

function var_0_0.Flush(arg_6_0, arg_6_1)
	if not arg_6_1 then
		arg_6_0:FlushStyle(true)

		return
	end

	arg_6_0:FlushStyle(false)

	if not (arg_6_0.commodity and arg_6_0.commodity.id == arg_6_1.id) then
		arg_6_0:FlushName(arg_6_1)
		arg_6_0:FlushPreviewBtn(arg_6_1)
		arg_6_0:FlushTimeline(arg_6_1)
		arg_6_0:FlushTag(arg_6_1)
		arg_6_0:SwitchPreview(arg_6_1, arg_6_0.isPreviewFurniture, false)
		arg_6_0:FlushPaintingToggle(arg_6_1)
		arg_6_0:FlushBG(arg_6_1)
		arg_6_0:FlushPainting(arg_6_1)
	else
		arg_6_0:FlushBG(arg_6_1)
		arg_6_0:FlushPainting(arg_6_1)
	end

	arg_6_0:FlushPrice(arg_6_1)
	arg_6_0:FlushObtainBtn(arg_6_1)

	arg_6_0.commodity = arg_6_1
end

function var_0_0.FlushStyle(arg_7_0, arg_7_1)
	setActive(arg_7_0.paintingTF.parent, not arg_7_1)
	setActive(arg_7_0.defaultBg, arg_7_1)
	setActive(arg_7_0.diffBg.parent, not arg_7_1)
	setActive(arg_7_0.titleTr, not arg_7_1)
	setActive(arg_7_0.rightTr, not arg_7_1)
end

function var_0_0.getUIName(arg_8_0)
	return "NewSkinShopMainView"
end

function var_0_0.FlushBgWithAnim(arg_9_0, arg_9_1)
	local var_9_0 = arg_9_0._tf:GetComponent(typeof(CanvasGroup))

	var_9_0.blocksRaycasts = false

	parallelAsync({
		function(arg_10_0)
			arg_9_0:DoSwitchBgAnim(1, 0.3, 0.8, LeanTweenType.linear, arg_10_0)
		end,
		function(arg_11_0)
			arg_9_0:FlushBG(arg_9_1, arg_11_0)
		end
	}, function()
		arg_9_0:DoSwitchBgAnim(1, 1, 0.01, LeanTweenType.linear, function()
			var_9_0.blocksRaycasts = true
		end)
	end)
end

function var_0_0.DoSwitchBgAnim(arg_14_0, arg_14_1, arg_14_2, arg_14_3, arg_14_4, arg_14_5)
	arg_14_0:ClearSwitchBgAnim()

	local var_14_0 = GetOrAddComponent(arg_14_0.bgsGo, typeof(CanvasGroup))

	var_14_0.alpha = arg_14_1

	LeanTween.value(arg_14_0.bgsGo, arg_14_1, arg_14_2, arg_14_3):setOnUpdate(System.Action_float(function(arg_15_0)
		var_14_0.alpha = arg_15_0
	end)):setEase(arg_14_4):setOnComplete(System.Action(arg_14_5))
end

function var_0_0.ClearSwitchBgAnim(arg_16_0)
	if LeanTween.isTweening(arg_16_0.bgsGo) then
		LeanTween.cancel(arg_16_0.bgsGo)
	end

	GetOrAddComponent(arg_16_0.bgsGo, typeof(CanvasGroup)).alpha = 1
end

function var_0_0.FlushBG(arg_17_0, arg_17_1, arg_17_2)
	local var_17_0 = arg_17_1:getSkinId()
	local var_17_1 = pg.ship_skin_template[var_17_0]
	local var_17_2 = ShipGroup.getDefaultShipConfig(var_17_1.ship_group)
	local var_17_3 = Ship.New({
		id = 999,
		configId = var_17_2.id,
		skin_id = var_17_0
	})
	local var_17_4 = var_17_3:getShipBgPrint(true)
	local var_17_5 = pg.ship_skin_template[var_17_0].painting

	if (arg_17_0.isToggleShowBg or not checkABExist("painting/" .. var_17_5 .. "_n")) and var_17_1.bg_sp ~= "" then
		var_17_4 = var_17_1.bg_sp
	end

	local var_17_6 = var_17_4 ~= var_17_3:rarity2bgPrintForGet()

	if var_17_6 then
		pg.DynamicBgMgr.GetInstance():LoadBg(arg_17_0, var_17_4, arg_17_0.diffBg.parent, arg_17_0.diffBg, function(arg_18_0)
			if arg_17_2 then
				arg_17_2()
			end
		end, function(arg_19_0)
			if arg_17_2 then
				arg_17_2()
			end
		end)
	else
		pg.DynamicBgMgr.GetInstance():ClearBg(arg_17_0:getUIName())

		if arg_17_2 then
			arg_17_2()
		end
	end

	setActive(arg_17_0.diffBg, var_17_6)
	setActive(arg_17_0.defaultBg, not var_17_6)
end

function var_0_0.FlushName(arg_20_0, arg_20_1)
	local var_20_0 = arg_20_1:getSkinId()
	local var_20_1 = pg.ship_skin_template[var_20_0]

	arg_20_0.skinNameTxt.text = SwitchSpecialChar(var_20_1.name, true)

	local var_20_2 = ShipGroup.getDefaultShipConfig(var_20_1.ship_group)

	arg_20_0.shipNameTxt.text = var_20_2.name
end

function var_0_0.FlushPaintingToggle(arg_21_0, arg_21_1)
	removeOnToggle(arg_21_0.dynamicToggle)
	removeOnToggle(arg_21_0.showBgToggle)

	local var_21_0 = ShipSkin.New({
		id = arg_21_1:getSkinId()
	})
	local var_21_1 = checkABExist("painting/" .. var_21_0:getConfig("painting") .. "_n")

	if arg_21_0.isToggleShowBg and not var_21_1 then
		triggerToggle(arg_21_0.showBgToggle, false)

		arg_21_0.isToggleShowBg = false
	elseif var_21_1 then
		triggerToggle(arg_21_0.showBgToggle, true)

		arg_21_0.isToggleShowBg = true
	end

	local var_21_2 = var_21_0:IsSpine() or var_21_0:IsLive2d()

	if LOCK_SKIN_SHOP_ANIM_PREVIEW then
		var_21_2 = false
	end

	if var_21_2 and PlayerPrefs.GetInt("skinShop#l2dPreViewToggle" .. getProxy(PlayerProxy):getRawData().id, 0) == 1 then
		arg_21_0.isToggleDynamic = true
	end

	if arg_21_0.isToggleDynamic and not var_21_2 then
		triggerToggle(arg_21_0.dynamicToggle, false)

		arg_21_0.isToggleDynamic = false
	elseif arg_21_0.isToggleDynamic and not arg_21_0.dynamicToggle:GetComponent(typeof(Toggle)).isOn then
		triggerToggle(arg_21_0.dynamicToggle, true)

		arg_21_0.isToggleDynamic = true
	end

	if var_21_1 then
		onToggle(arg_21_0, arg_21_0.showBgToggle, function(arg_22_0)
			arg_21_0.isToggleShowBg = arg_22_0

			arg_21_0:FlushPainting(arg_21_1)
			arg_21_0:FlushBG(arg_21_1)
		end, SFX_PANEL)
	end

	if var_21_0:IsSpine() or var_21_0:IsLive2d() then
		onToggle(arg_21_0, arg_21_0.dynamicToggle, function(arg_23_0)
			arg_21_0.isToggleDynamic = arg_23_0

			setActive(arg_21_0.dynamicResToggle, arg_23_0)
			setActive(arg_21_0.showBgToggle, not arg_23_0 and var_21_1)
			arg_21_0:FlushPainting(arg_21_1)
			arg_21_0:FlushDynamicPaintingResState(arg_21_1)
			arg_21_0:RecordFlag(arg_23_0)
		end, SFX_PANEL)
	end

	if arg_21_0.isToggleDynamic then
		arg_21_0:FlushDynamicPaintingResState(arg_21_1)
	end

	setActive(arg_21_0.dynamicToggle, var_21_2)
	setActive(arg_21_0.dynamicResToggle, arg_21_0.isToggleDynamic)
	setActive(arg_21_0.showBgToggle, not arg_21_0.isToggleDynamic and var_21_1)
end

function var_0_0.RecordFlag(arg_24_0, arg_24_1)
	local var_24_0 = getProxy(PlayerProxy):getRawData().id

	PlayerPrefs.SetInt("skinShop#l2dPreViewToggle" .. var_24_0, arg_24_1 and 1 or 0)
	PlayerPrefs.Save()
	arg_24_0:emit(NewSkinShopMediator.ON_RECORD_ANIM_PREVIEW_BTN, arg_24_1)
end

function var_0_0.ExistL2dRes(arg_25_0, arg_25_1)
	local var_25_0 = "live2d/" .. string.lower(arg_25_1)
	local var_25_1 = HXSet.autoHxShiftPath(var_25_0, nil, true)

	return checkABExist(var_25_1), var_25_1
end

function var_0_0.ExistSpineRes(arg_26_0, arg_26_1)
	local var_26_0 = "SpinePainting/" .. string.lower(arg_26_1)
	local var_26_1 = HXSet.autoHxShiftPath(var_26_0, nil, true)

	return checkABExist(var_26_1), var_26_1
end

function var_0_0.FlushDynamicPaintingResState(arg_27_0, arg_27_1)
	if not arg_27_0.isToggleDynamic then
		return
	end

	local var_27_0 = arg_27_0:GetPaintingState(arg_27_1)
	local var_27_1 = false
	local var_27_2 = ""
	local var_27_3 = pg.ship_skin_template[arg_27_1:getSkinId()].painting

	if var_0_2 == var_27_0 then
		var_27_1, var_27_2 = arg_27_0:ExistL2dRes(var_27_3)
	elseif var_0_3 == var_27_0 then
		var_27_1, var_27_2 = arg_27_0:ExistSpineRes(var_27_3)
	end

	setActive(arg_27_0.dynamicResDownaload, var_27_1)
	setActive(arg_27_0.dynamicResUnDownaload, not var_27_1)
	removeOnButton(arg_27_0.dynamicResUnDownaload)

	if not var_27_1 and var_27_2 ~= "" then
		onButton(arg_27_0, arg_27_0.dynamicResUnDownaload, function()
			arg_27_0:DownloadDynamicPainting(var_27_2, arg_27_1)
		end, SFX_PANEL)
	end
end

function var_0_0.DownloadDynamicPainting(arg_29_0, arg_29_1, arg_29_2)
	local var_29_0 = arg_29_2:getSkinId()

	if arg_29_0.downloads[var_29_0] then
		return
	end

	local var_29_1 = SkinShopDownloadRequest.New()

	arg_29_0.downloads[var_29_0] = var_29_1

	var_29_1:Start(arg_29_1, function(arg_30_0)
		if arg_30_0 and arg_29_0.paintingState and arg_29_0.paintingState.id == arg_29_2.id then
			arg_29_0:FlushPainting(arg_29_2)
			arg_29_0:FlushDynamicPaintingResState(arg_29_2)
		end

		var_29_1:Dispose()

		arg_29_0.downloads[var_29_0] = nil
	end)
end

function var_0_0.GetPaintingState(arg_31_0, arg_31_1)
	local var_31_0 = ShipSkin.New({
		id = arg_31_1:getSkinId()
	})

	if arg_31_0.isToggleDynamic and var_31_0:IsLive2d() then
		return var_0_2
	elseif arg_31_0.isToggleDynamic and var_31_0:IsSpine() then
		if var_31_0:getConfig("spine_use_live2d") == 1 then
			return var_0_2
		end

		return var_0_3
	else
		return var_0_1
	end
end

function var_0_0.FlushPainting(arg_32_0, arg_32_1)
	local var_32_0 = arg_32_0:GetPaintingState(arg_32_1)
	local var_32_1 = pg.ship_skin_template[arg_32_1:getSkinId()].painting

	if var_32_0 == var_0_2 and not arg_32_0:ExistL2dRes(var_32_1) or var_32_0 == var_0_3 and not arg_32_0:ExistSpineRes(var_32_1) then
		var_32_0 = var_0_1
	end

	if arg_32_0.paintingState and arg_32_0.paintingState.state == var_32_0 and arg_32_0.paintingState.id == arg_32_1.id and arg_32_0.paintingState.showBg == arg_32_0.isToggleShowBg and arg_32_0.paintingState.purchaseFlag == arg_32_1.buyCount then
		return
	end

	arg_32_0:ClearPainting()

	if var_32_0 == var_0_1 then
		arg_32_0:LoadMeshPainting(arg_32_1, arg_32_0.isToggleShowBg)
	elseif var_32_0 == var_0_2 then
		arg_32_0:LoadL2dPainting(arg_32_1)
	elseif var_32_0 == var_0_3 then
		arg_32_0:LoadSpinePainting(arg_32_1)
	end

	arg_32_0.paintingState = {
		state = var_32_0,
		id = arg_32_1.id,
		showBg = arg_32_0.isToggleShowBg,
		purchaseFlag = arg_32_1.buyCount
	}
end

function var_0_0.ClearPainting(arg_33_0)
	local var_33_0 = arg_33_0.paintingState

	if not var_33_0 then
		return
	end

	if var_33_0.state == var_0_1 then
		arg_33_0:ClearMeshPainting()
	elseif var_33_0.state == var_0_2 then
		arg_33_0:ClearL2dPainting()
	elseif var_33_0.state == var_0_3 then
		arg_33_0:ClearSpinePainting()
	end

	arg_33_0.paintingState = nil
end

function var_0_0.LoadMeshPainting(arg_34_0, arg_34_1, arg_34_2)
	local var_34_0 = findTF(arg_34_0.paintingTF, "fitter")
	local var_34_1 = GetOrAddComponent(var_34_0, "PaintingScaler")

	var_34_1.FrameName = "chuanwu"
	var_34_1.Tween = 1

	local var_34_2 = pg.ship_skin_template[arg_34_1:getSkinId()].painting
	local var_34_3 = var_34_2

	if not arg_34_2 and checkABExist("painting/" .. var_34_2 .. "_n") then
		var_34_2 = var_34_2 .. "_n"
	end

	if not checkABExist("painting/" .. var_34_2) then
		return
	end

	pg.UIMgr.GetInstance():LoadingOn()
	PoolMgr.GetInstance():GetPainting(var_34_2, true, function(arg_35_0)
		pg.UIMgr.GetInstance():LoadingOff()
		setParent(arg_35_0, var_34_0, false)
		ShipExpressionHelper.SetExpression(var_34_0:GetChild(0), var_34_3)

		arg_34_0.paintingName = var_34_2

		if arg_34_0.paintingState and arg_34_0.paintingState.id ~= arg_34_1.id then
			arg_34_0:ClearMeshPainting()
		end

		local var_35_0 = arg_35_0.transform:Find("shop_hx")

		arg_34_0:CheckShowShopHx(var_35_0, arg_34_1)
	end)
end

function var_0_0.ClearMeshPainting(arg_36_0)
	local var_36_0 = arg_36_0.paintingTF:Find("fitter")

	if arg_36_0.paintingName and var_36_0.childCount > 0 then
		local var_36_1 = var_36_0:GetChild(0).gameObject
		local var_36_2 = var_36_1.transform:Find("shop_hx")

		arg_36_0:RevertShopHx(var_36_2)
		PoolMgr.GetInstance():ReturnPainting(arg_36_0.paintingName, var_36_1)
	end

	arg_36_0.paintingName = nil
end

function var_0_0.LoadL2dPainting(arg_37_0, arg_37_1)
	local var_37_0 = arg_37_1:getSkinId()
	local var_37_1 = pg.ship_skin_template[var_37_0].ship_group
	local var_37_2 = ShipGroup.getDefaultShipConfig(var_37_1)
	local var_37_3 = Live2D.GenerateData({
		ship = Ship.New({
			id = 999,
			configId = var_37_2.id,
			skin_id = var_37_0
		}),
		scale = Vector3(52, 52, 52),
		position = Vector3(0, 0, -1),
		parent = arg_37_0.live2dContainer
	})

	var_37_3.shopPreView = true

	pg.UIMgr.GetInstance():LoadingOn()

	arg_37_0.live2dChar = Live2D.New(var_37_3, function(arg_38_0)
		arg_38_0:IgonreReactPos(true)
		arg_37_0:CheckShowShopHxForL2d(arg_38_0, arg_37_1)

		if arg_37_0.paintingState and arg_37_0.paintingState.id ~= arg_37_1.id then
			arg_37_0:ClearL2dPainting()
		end

		pg.UIMgr.GetInstance():LoadingOff()
	end)
end

function var_0_0.ClearL2dPainting(arg_39_0)
	if arg_39_0.live2dChar then
		arg_39_0:RevertShopHxForL2d(arg_39_0.live2dChar)
		arg_39_0.live2dChar:Dispose()

		arg_39_0.live2dChar = nil
	end
end

function var_0_0.LoadSpinePainting(arg_40_0, arg_40_1)
	local var_40_0 = arg_40_1:getSkinId()
	local var_40_1 = pg.ship_skin_template[var_40_0].ship_group
	local var_40_2 = ShipGroup.getDefaultShipConfig(var_40_1)
	local var_40_3 = SpinePainting.GenerateData({
		ship = Ship.New({
			id = 999,
			configId = var_40_2.id,
			skin_id = var_40_0
		}),
		position = Vector3(0, 0, 0),
		parent = arg_40_0.spTF,
		effectParent = arg_40_0.spBg
	})

	pg.UIMgr.GetInstance():LoadingOn()

	arg_40_0.spinePainting = SpinePainting.New(var_40_3, function(arg_41_0)
		if arg_40_0.paintingState and arg_40_0.paintingState.id ~= arg_40_1.id then
			arg_40_0:ClearSpinePainting()
		end

		local var_41_0 = arg_41_0._tf:Find("shop_hx")

		arg_40_0:CheckShowShopHx(var_41_0, arg_40_1)
		pg.UIMgr.GetInstance():LoadingOff()
	end)
end

function var_0_0.ClearSpinePainting(arg_42_0)
	if arg_42_0.spinePainting and arg_42_0.spinePainting._tf then
		local var_42_0 = arg_42_0.spinePainting._tf:Find("shop_hx")

		arg_42_0:RevertShopHx(arg_42_0.shopHx)
		arg_42_0.spinePainting:Dispose()

		arg_42_0.spinePainting = nil
	end
end

function var_0_0.CheckShowShopHxForL2d(arg_43_0, arg_43_1, arg_43_2)
	if PLATFORM_CODE ~= PLATFORM_CH then
		return
	end

	if not HXSet.isHx() then
		return
	end

	local var_43_0 = arg_43_2.buyCount <= 0 and 1 or 0

	arg_43_1:changeParamaterValue("shophx", var_43_0)
end

function var_0_0.RevertShopHxForL2d(arg_44_0, arg_44_1)
	arg_44_1:changeParamaterValue("shophx", 0)
end

function var_0_0.CheckShowShopHx(arg_45_0, arg_45_1, arg_45_2)
	if PLATFORM_CODE ~= PLATFORM_CH then
		return
	end

	if not HXSet.isHx() then
		return
	end

	if not IsNil(arg_45_1) and arg_45_2.buyCount <= 0 then
		setActive(arg_45_1, true)
	end
end

function var_0_0.RevertShopHx(arg_46_0, arg_46_1)
	if not IsNil(arg_46_1) then
		setActive(arg_46_1, false)
	end
end

function var_0_0.FlushPreviewBtn(arg_47_0, arg_47_1)
	local var_47_0 = Goods.ExistFurniture(arg_47_1.id)

	removeOnButton(arg_47_0.switchPreviewBtn)

	if not var_47_0 and arg_47_0.isPreviewFurniture then
		arg_47_0.isPreviewFurniture = false
	end

	setActive(arg_47_0.switchPreviewBtn, var_47_0)

	if var_47_0 then
		onButton(arg_47_0, arg_47_0.switchPreviewBtn, function()
			if arg_47_0:IsSwitchTweening() then
				return
			end

			arg_47_0.isPreviewFurniture = not arg_47_0.isPreviewFurniture

			arg_47_0:SwitchPreview(arg_47_1, arg_47_0.isPreviewFurniture, true)
			arg_47_0:FlushPrice(arg_47_1)
			arg_47_0:FlushObtainBtn(arg_47_1)
		end, SFX_PANEL)
	end
end

function var_0_0.IsSwitchTweening(arg_49_0)
	return LeanTween.isTweening(go(arg_49_0.furnitureBg)) or LeanTween.isTweening(go(arg_49_0.charBg))
end

function var_0_0.ClearSwitchTween(arg_50_0)
	if arg_50_0:IsSwitchTweening() then
		LeanTween.cancel(go(arg_50_0.furnitureBg))
		LeanTween.cancel(go(arg_50_0.charBg))
	end
end

function var_0_0.StartSwitchAnim(arg_51_0, arg_51_1, arg_51_2, arg_51_3, arg_51_4)
	arg_51_0:ClearSwitchTween()

	local var_51_0 = arg_51_1:GetComponent(typeof(CanvasGroup))
	local var_51_1 = arg_51_2:GetComponent(typeof(CanvasGroup))
	local var_51_2 = var_51_0.alpha
	local var_51_3 = var_51_1.alpha
	local var_51_4 = arg_51_1.anchoredPosition3D
	local var_51_5 = arg_51_2.anchoredPosition3D

	LeanTween.moveLocal(go(arg_51_1), var_51_5, arg_51_3):setOnComplete(System.Action(function()
		var_51_0.alpha = var_51_3
	end))
	LeanTween.moveLocal(go(arg_51_2), var_51_4, arg_51_3):setOnComplete(System.Action(function()
		var_51_1.alpha = var_51_2

		arg_51_4()
	end))
end

function var_0_0.SwitchPreview(arg_54_0, arg_54_1, arg_54_2, arg_54_3)
	local var_54_0 = arg_54_1:getSkinId()
	local var_54_1 = arg_54_0.furnitureBg
	local var_54_2 = arg_54_0.charBg

	arg_54_0:StartSwitchAnim(var_54_1, var_54_2, arg_54_3 and 0.3 or 0, function()
		setActive(arg_54_0.charContainer, not arg_54_2)
		setActive(arg_54_0.furnitureContainer, arg_54_2)
	end)

	if not arg_54_2 then
		var_54_1:SetAsFirstSibling()
		var_54_2:SetSiblingIndex(2)

		local var_54_3 = pg.ship_skin_template[var_54_0]

		arg_54_0:FlushChar(var_54_3.prefab, var_54_3.id)
	else
		var_54_2:SetAsFirstSibling()
		var_54_1:SetSiblingIndex(2)

		local var_54_4 = Goods.Id2FurnitureId(arg_54_1.id)
		local var_54_5 = Goods.GetFurnitureConfig(arg_54_1.id)

		arg_54_0.interactionPreview:Flush(var_54_0, var_54_4, var_54_5.scale[2] or 1, var_54_5.position[2])
	end
end

function var_0_0.GetObtainBtnState(arg_56_0, arg_56_1)
	if arg_56_1:getConfig("genre") == ShopArgs.SkinShopTimeLimit then
		return var_0_9
	elseif arg_56_0.isPreviewFurniture then
		if getProxy(DormProxy):getRawData():HasFurniture(Goods.Id2FurnitureId(arg_56_1.id)) then
			return var_0_4
		else
			return var_0_8
		end
	elseif arg_56_1.type == Goods.TYPE_ACTIVITY or arg_56_1.type == Goods.TYPE_ACTIVITY_EXTRA then
		return var_0_6
	elseif arg_56_1.buyCount > 0 then
		return var_0_4
	elseif arg_56_1:isDisCount() and arg_56_1:IsItemDiscountType() then
		return var_0_7
	elseif arg_56_1:CanUseVoucherType() then
		return var_0_10
	elseif #arg_56_1:GetGiftList() > 0 then
		return var_0_11
	else
		return var_0_5
	end
end

function var_0_0.FlushPrice(arg_57_0, arg_57_1)
	local var_57_0 = arg_57_1:getConfig("genre") == ShopArgs.SkinShopTimeLimit
	local var_57_1 = arg_57_1.type == Goods.TYPE_ACTIVITY or arg_57_1.type == Goods.TYPE_ACTIVITY_EXTRA

	if var_57_0 then
		arg_57_0:UpdateExperiencePrice(arg_57_1)
	elseif arg_57_0.isPreviewFurniture then
		arg_57_0:UpdateFurniturePrice(arg_57_1)
	elseif var_57_1 then
		-- block empty
	else
		arg_57_0:UpdateCommodityPrice(arg_57_1)
	end

	local var_57_2 = arg_57_1.type == Goods.TYPE_SKIN

	setActive(arg_57_0.experienceTr, var_57_0 and not var_57_1)
	setActive(arg_57_0.consumeTr, var_57_2 and not var_57_0 and not var_57_1)
end

function var_0_0.UpdateExperiencePrice(arg_58_0, arg_58_1)
	local var_58_0 = arg_58_1:getConfig("resource_num")
	local var_58_1 = getProxy(PlayerProxy):getRawData():getSkinTicket()
	local var_58_2 = (var_58_1 < var_58_0 and "<color=" .. COLOR_RED .. ">" or "") .. var_58_1 .. (var_58_1 < var_58_0 and "</color>" or "")

	arg_58_0.experienceTxt.text = var_58_2 .. "/" .. var_58_0
end

function var_0_0.UpdateCommodityPrice(arg_59_0, arg_59_1)
	local var_59_0 = arg_59_1:GetPrice()
	local var_59_1 = arg_59_1:getConfig("resource_num")

	arg_59_0.consumeRealPriceTxt.text = var_59_0
	arg_59_0.consumePriceTxt.text = var_59_1

	setActive(tf(go(arg_59_0.consumePriceTxt)).parent, var_59_0 ~= var_59_1)
end

function var_0_0.UpdateFurniturePrice(arg_60_0, arg_60_1)
	local var_60_0 = Goods.Id2FurnitureId(arg_60_1.id)
	local var_60_1 = Furniture.New({
		id = var_60_0
	})
	local var_60_2 = var_60_1:getConfig("gem_price")

	arg_60_0.consumePriceTxt.text = var_60_2

	local var_60_3 = var_60_1:getPrice(PlayerConst.ResDiamond)

	arg_60_0.consumeRealPriceTxt.text = var_60_3

	setActive(tf(go(arg_60_0.consumePriceTxt)).parent, var_60_2 ~= var_60_3)
end

function var_0_0.FlushObtainBtn(arg_61_0, arg_61_1)
	local var_61_0 = arg_61_0:GetObtainBtnState(arg_61_1)
	local var_61_1 = arg_61_0.obtainBtnSprites[var_61_0]

	if not var_61_1 then
		var_61_1 = GetSpriteFromAtlas("ui/skinshopui_atlas", var_0_12(var_61_0))
		arg_61_0.obtainBtnSprites[var_61_0] = var_61_1
	end

	arg_61_0.obtainBtnImg.sprite = var_61_1

	arg_61_0.obtainBtnImg:SetNativeSize()
	setActive(arg_61_0.giftTag, var_61_0 == var_0_11)
	setActive(arg_61_0.giftItem, var_61_0 == var_0_11)

	if var_61_0 == var_0_11 then
		arg_61_0:FlushGift(arg_61_1)
	else
		arg_61_0.giftText.text = ""
	end

	onButton(arg_61_0, arg_61_0.obtainBtn, function()
		if var_61_0 == var_0_5 or var_61_0 == var_0_7 or var_61_0 == var_0_11 then
			arg_61_0.purchaseView:ExecuteAction("Show", arg_61_1)
		else
			arg_61_0:OnClickBtn(var_61_0, arg_61_1)
		end
	end, SFX_PANEL)
end

function var_0_0.OnClickBtn(arg_63_0, arg_63_1, arg_63_2)
	if arg_63_1 == var_0_5 or arg_63_1 == var_0_7 or arg_63_1 == var_0_11 then
		arg_63_0:OnPurchase(arg_63_2)
	elseif arg_63_1 == var_0_10 then
		arg_63_0:OnItemPurchase(arg_63_2)
	elseif arg_63_1 == var_0_6 then
		arg_63_0:OnActivity(arg_63_2)
	elseif arg_63_1 == var_0_8 then
		arg_63_0:OnBackyard(arg_63_2)
	elseif arg_63_1 == var_0_9 then
		arg_63_0:OnExperience(arg_63_2)
	end
end

function var_0_0.FlushGift(arg_64_0, arg_64_1)
	local var_64_0 = arg_64_1:GetGiftList()
	local var_64_1 = var_64_0[1]

	updateDrop(arg_64_0.giftItem, {
		type = var_64_1.type,
		id = var_64_1.id,
		count = var_64_1.count
	})

	local var_64_2 = #var_64_0 > 1 and "+" .. #var_64_0 - 1 .. "..." or ""

	arg_64_0.giftText.text = var_64_2
end

function var_0_0.OnItemPurchase(arg_65_0, arg_65_1)
	if arg_65_1.type ~= Goods.TYPE_SKIN then
		return
	end

	local var_65_0 = arg_65_1:GetVoucherIdList()

	if #var_65_0 <= 0 then
		return
	end

	local var_65_1 = arg_65_1:getSkinId()
	local var_65_2 = pg.ship_skin_template[var_65_1]
	local var_65_3 = SwitchSpecialChar(var_65_2.name, true)

	arg_65_0.voucherMsgBox:ExecuteAction("Show", {
		itemList = var_65_0,
		skinName = var_65_3,
		price = arg_65_1:GetPrice(),
		onYes = function(arg_66_0)
			if arg_66_0 then
				arg_65_0:emit(NewSkinShopMediator.ON_ITEM_PURCHASE, arg_66_0, arg_65_1.id)
			else
				arg_65_0:emit(NewSkinShopMediator.ON_SHOPPING, arg_65_1.id, 1)
			end
		end
	})
end

function var_0_0.OnPurchase(arg_67_0, arg_67_1)
	if arg_67_1.type ~= Goods.TYPE_SKIN then
		return
	end

	if arg_67_1:isDisCount() and arg_67_1:IsItemDiscountType() then
		arg_67_0:emit(NewSkinShopMediator.ON_SHOPPING_BY_ACT, arg_67_1.id, 1)
	else
		arg_67_0:emit(NewSkinShopMediator.ON_SHOPPING, arg_67_1.id, 1)
	end
end

function var_0_0.OnActivity(arg_68_0, arg_68_1)
	local var_68_0 = arg_68_1:getConfig("time")
	local var_68_1 = arg_68_1:getConfig("activity")
	local var_68_2 = getProxy(ActivityProxy):getActivityById(var_68_1)

	if var_68_1 == 0 and pg.TimeMgr.GetInstance():inTime(var_68_0) or var_68_2 and not var_68_2:isEnd() then
		if arg_68_1.type == Goods.TYPE_ACTIVITY then
			arg_68_0:emit(NewSkinShopMediator.GO_SHOPS_LAYER, arg_68_1:getConfig("activity"))
		elseif arg_68_1.type == Goods.TYPE_ACTIVITY_EXTRA then
			local var_68_3 = arg_68_1:getConfig("scene")

			if var_68_3 and #var_68_3 > 0 then
				arg_68_0:emit(NewSkinShopMediator.OPEN_SCENE, var_68_3)
			else
				arg_68_0:emit(NewSkinShopMediator.OPEN_ACTIVITY, var_68_1)
			end
		end
	else
		pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_not_start"))
	end
end

function var_0_0.OnBackyard(arg_69_0, arg_69_1)
	if not pg.SystemOpenMgr.GetInstance():isOpenSystem(getProxy(PlayerProxy):getRawData().level, "BackYardMediator") then
		local var_69_0 = pg.open_systems_limited[1]

		pg.TipsMgr.GetInstance():ShowTips(i18n("no_open_system_tip", var_69_0.name, var_69_0.level))

		return
	end

	arg_69_0:emit(NewSkinShopMediator.ON_BACKYARD_SHOP)
end

function var_0_0.OnExperience(arg_70_0, arg_70_1)
	local var_70_0 = arg_70_1:getSkinId()
	local var_70_1 = getProxy(ShipSkinProxy):getSkinById(var_70_0)

	if var_70_1 and not var_70_1:isExpireType() then
		pg.TipsMgr.GetInstance():ShowTips(i18n("already_have_the_skin"))

		return
	end

	local var_70_2 = arg_70_1:getConfig("resource_num")
	local var_70_3 = arg_70_1:getConfig("time_second") * var_70_2
	local var_70_4, var_70_5, var_70_6, var_70_7 = pg.TimeMgr.GetInstance():parseTimeFrom(var_70_3)
	local var_70_8 = pg.ship_skin_template[arg_70_1:getSkinId()].name

	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		content = i18n("exchange_limit_skin_tip", var_70_2, var_70_8, var_70_4, var_70_5),
		onYes = function()
			if getProxy(PlayerProxy):getRawData():getSkinTicket() < var_70_2 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_item_1"))

				return
			end

			arg_70_0:emit(NewSkinShopMediator.ON_SHOPPING, arg_70_1.id, 1)
		end
	})
end

function var_0_0.FlushTag(arg_72_0, arg_72_1)
	local var_72_0 = arg_72_1:getSkinId()
	local var_72_1 = pg.ship_skin_template[var_72_0].tag

	arg_72_0.uiTagList:make(function(arg_73_0, arg_73_1, arg_73_2)
		if arg_73_0 == UIItemList.EventUpdate then
			LoadSpriteAtlasAsync("SkinIcon", "type_" .. ShipSkin.Tag2Name(var_72_1[arg_73_1 + 1]), function(arg_74_0)
				if arg_72_0.exited then
					return
				end

				local var_74_0 = arg_73_2:Find("icon"):GetComponent(typeof(Image))

				var_74_0.sprite = arg_74_0

				var_74_0:SetNativeSize()
			end)
		end
	end)
	arg_72_0.uiTagList:align(#var_72_1)
end

function var_0_0.FlushChar(arg_75_0, arg_75_1, arg_75_2)
	if arg_75_0.prefabName and arg_75_0.prefabName == arg_75_1 then
		return
	end

	arg_75_0:ReturnChar()
	PoolMgr.GetInstance():GetSpineChar(arg_75_1, true, function(arg_76_0)
		arg_75_0.spineChar = tf(arg_76_0)
		arg_75_0.prefabName = arg_75_1

		local var_76_0 = pg.skinshop_spine_scale[arg_75_2]

		if var_76_0 then
			arg_75_0.spineChar.localScale = Vector3(var_76_0.skinshop_scale, var_76_0.skinshop_scale, 1)
		else
			arg_75_0.spineChar.localScale = Vector3(0.9, 0.9, 1)
		end

		arg_75_0.spineChar.localPosition = Vector3(0, 0, 0)

		pg.ViewUtils.SetLayer(arg_75_0.spineChar, Layer.UI)
		setParent(arg_75_0.spineChar, arg_75_0.charContainer)
		arg_76_0:GetComponent("SpineAnimUI"):SetAction("normal", 0)
	end)
end

function var_0_0.FlushTimeline(arg_77_0, arg_77_1)
	local var_77_0 = arg_77_1:getSkinId()
	local var_77_1 = false
	local var_77_2

	if arg_77_1:IsActivityExtra() and arg_77_1:ShowMaintenanceTime() then
		local var_77_3, var_77_4 = arg_77_1:GetMaintenanceMonthAndDay()

		function var_77_2()
			return i18n("limit_skin_time_before_maintenance", var_77_3, var_77_4)
		end

		var_77_1 = true
	elseif arg_77_1:getConfig("genre") == ShopArgs.SkinShopTimeLimit then
		local var_77_5 = getProxy(ShipSkinProxy):getSkinById(var_77_0)

		var_77_1 = var_77_5 and var_77_5:isExpireType() and not var_77_5:isExpired()

		if var_77_1 then
			function var_77_2()
				return skinTimeStamp(var_77_5:getRemainTime())
			end
		end
	else
		local var_77_6, var_77_7 = pg.TimeMgr.GetInstance():inTime(arg_77_1:getConfig("time"))

		var_77_1 = var_77_7

		if var_77_1 then
			local var_77_8 = pg.TimeMgr.GetInstance():Table2ServerTime(var_77_7)

			function var_77_2()
				return skinCommdityTimeStamp(var_77_8)
			end
		end
	end

	setActive(arg_77_0.timeLimitTr, var_77_1)
	arg_77_0:ClearTimer()

	if var_77_1 then
		arg_77_0:AddTimer(var_77_2)
	end
end

function var_0_0.AddTimer(arg_81_0, arg_81_1)
	arg_81_0.timer = Timer.New(function()
		arg_81_0.timeLimitTxt.text = arg_81_1()
	end, 1, -1)

	arg_81_0.timer.func()
	arg_81_0.timer:Start()
end

function var_0_0.ClearTimer(arg_83_0)
	if arg_83_0.timer then
		arg_83_0.timer:Stop()

		arg_83_0.timer = nil
	end
end

function var_0_0.ReturnChar(arg_84_0)
	if not IsNil(arg_84_0.spineChar) then
		arg_84_0.spineChar.gameObject:GetComponent("SpineAnimUI"):SetActionCallBack(nil)
		PoolMgr.GetInstance():ReturnSpineChar(arg_84_0.prefabName, arg_84_0.spineChar.gameObject)

		arg_84_0.spineChar = nil
		arg_84_0.prefabName = nil
	end
end

function var_0_0.ClosePurchaseView(arg_85_0)
	if arg_85_0.purchaseView and arg_85_0.purchaseView:GetLoaded() then
		arg_85_0.purchaseView:Hide()
	end
end

function var_0_0.Dispose(arg_86_0)
	arg_86_0.exited = true

	pg.DelegateInfo.Dispose(arg_86_0)
	arg_86_0:ClearSwitchBgAnim()
	pg.DynamicBgMgr.GetInstance():ClearBg(arg_86_0:getUIName())

	if arg_86_0.voucherMsgBox then
		arg_86_0.voucherMsgBox:Destroy()

		arg_86_0.voucherMsgBox = nil
	end

	if arg_86_0.purchaseView then
		arg_86_0.purchaseView:Destroy()

		arg_86_0.purchaseView = nil
	end

	for iter_86_0, iter_86_1 in pairs(arg_86_0.downloads) do
		iter_86_1:Dispose()
	end

	arg_86_0.downloads = {}

	arg_86_0:ClearPainting()

	for iter_86_2, iter_86_3 in pairs(arg_86_0.obtainBtnSprites) do
		arg_86_0.obtainBtnSprites[iter_86_3] = nil
	end

	arg_86_0.obtainBtnSprites = nil

	if arg_86_0.interactionPreview then
		arg_86_0.interactionPreview:Dispose()

		arg_86_0.interactionPreview = nil
	end

	arg_86_0:ClearSwitchTween()
	arg_86_0:disposeEvent()
	arg_86_0:ClearTimer()
	arg_86_0:ReturnChar()
end

return var_0_0
