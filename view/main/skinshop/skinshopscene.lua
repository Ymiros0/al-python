local var_0_0 = class("SkinShopScene", import("...base.BaseUI"))

var_0_0.EVENT_ON_CARD_CLICK = "SkinShopScene:EVENT_ON_CARD_CLICK"

local var_0_1 = pg.skin_page_template
local var_0_2 = pg.ship_skin_template

var_0_0.SHOP_TYPE_COMMON = 1
var_0_0.SHOP_TYPE_TIMELIMIT = 2
var_0_0.PAGE_ALL = -1
var_0_0.PAGE_TIME_LIMIT = -2
var_0_0.PAGE_ENCORE = -3
var_0_0.PAGE_PROPOSE = 9998
var_0_0.PAGE_TRANS = 9997
var_0_0.MSGBOXNAME = "SkinShopMsgbox"

local var_0_3 = {
	{
		"huanzhuangshagndian",
		"huanzhuangshagndian_en"
	},
	{
		"title_01",
		"title_en_01"
	}
}

function var_0_0.forceGC(arg_1_0)
	return true
end

function var_0_0.getUIName(arg_2_0)
	return "SkinShopUI"
end

function var_0_0.ResUISettings(arg_3_0)
	return {
		anim = true,
		showType = PlayerResUI.TYPE_GEM
	}
end

function var_0_0.setSkins(arg_4_0, arg_4_1)
	arg_4_0.skinList = arg_4_1

	arg_4_0:filterSkins()
end

function var_0_0.SetEncoreSkins(arg_5_0, arg_5_1)
	arg_5_0.existAnyEncoreSkin = #arg_5_1 > 0
	arg_5_0.encoreSkinMap = {}

	for iter_5_0, iter_5_1 in ipairs(arg_5_1) do
		arg_5_0.encoreSkinMap[iter_5_1] = true
	end
end

function var_0_0.setPlayer(arg_6_0, arg_6_1)
	arg_6_0.playerVO = arg_6_1
	arg_6_0.skinTicket = arg_6_0.playerVO:getSkinTicket()
end

function var_0_0.filterSkins(arg_7_0)
	arg_7_0.skinGoodsVOs = getProxy(ShipSkinProxy):GetAllSkins()

	arg_7_0:updateShipRect()
end

function var_0_0.init(arg_8_0)
	arg_8_0.downloads = {}
	arg_8_0.bottomTF = arg_8_0:findTF("Main/bottom")
	arg_8_0.topTF = arg_8_0:findTF("Main/blur_panel/adapt/top")
	arg_8_0.leftPanel = arg_8_0:findTF("Main/left_panel")
	arg_8_0.title = arg_8_0:findTF("title", arg_8_0.topTF)
	arg_8_0.titleEn = arg_8_0:findTF("title_en", arg_8_0.topTF)
	arg_8_0.mainPanel = arg_8_0:findTF("Main")
	arg_8_0.namePanel = arg_8_0:findTF("name_bg", arg_8_0.mainPanel)
	arg_8_0.nameTxt = arg_8_0:findTF("name_bg/name", arg_8_0.mainPanel):GetComponent(typeof(Text))
	arg_8_0.skinNameTxt = arg_8_0:findTF("name_bg/skin_name", arg_8_0.mainPanel):GetComponent(typeof(Text))
	arg_8_0.rightPanel = arg_8_0:findTF("Main/right")
	arg_8_0.charParent = arg_8_0:findTF("char", arg_8_0.rightPanel)
	arg_8_0.furParent = arg_8_0:findTF("fur", arg_8_0.rightPanel)
	arg_8_0.interactionPreview = BackYardInteractionPreview.New(arg_8_0.furParent, Vector3(0, 0, 0))
	arg_8_0.paintingTF = arg_8_0:findTF("painting/paint")
	arg_8_0.tags = arg_8_0:findTF("tags", arg_8_0.rightPanel)
	arg_8_0.limitTxt = arg_8_0:findTF("name_bg/limit_time/Text", arg_8_0.mainPanel):GetComponent(typeof(Text))
	arg_8_0.commonPanel = arg_8_0:findTF("common", arg_8_0.rightPanel)
	arg_8_0.commonBGTF = arg_8_0:findTF("bg", arg_8_0.commonPanel)
	arg_8_0.commonLabelTF = arg_8_0:findTF("label", arg_8_0.commonPanel)
	arg_8_0.commonConsumeTF = arg_8_0:findTF("consume", arg_8_0.commonPanel)
	arg_8_0.buyBtn = arg_8_0:findTF("buy_btn", arg_8_0.commonPanel)
	arg_8_0.activityBtn = arg_8_0:findTF("activty_btn", arg_8_0.commonPanel)
	arg_8_0.itemBtn = arg_8_0:findTF("item_btn", arg_8_0.commonPanel)
	arg_8_0.gotBtn = arg_8_0:findTF("got_btn", arg_8_0.commonPanel)
	arg_8_0.backyardBtn = arg_8_0:findTF("backyard", arg_8_0.commonPanel)
	arg_8_0.priceTxt = arg_8_0:findTF("consume/Text", arg_8_0.commonPanel):GetComponent(typeof(Text))
	arg_8_0.originalPriceTxt = arg_8_0:findTF("consume/originalprice/Text", arg_8_0.commonPanel):GetComponent(typeof(Text))
	arg_8_0.timelimtPanel = arg_8_0:findTF("timelimt", arg_8_0.rightPanel)
	arg_8_0.timelimitBtn = arg_8_0:findTF("timelimit_btn", arg_8_0.timelimtPanel)
	arg_8_0.timelimitPriceTxt = arg_8_0:findTF("consume/Text", arg_8_0.timelimtPanel):GetComponent(typeof(Text))
	arg_8_0.live2dFilter = arg_8_0.topTF:Find("live2d")
	arg_8_0.live2dFilterSel = arg_8_0.live2dFilter:Find("selected")
	arg_8_0.indexBtn = arg_8_0.topTF:Find("index_btn")
	arg_8_0.indexBtnSel = arg_8_0.indexBtn:Find("sel")
	arg_8_0.inptuTr = arg_8_0.topTF:Find("search")
	arg_8_0.changeBtn = arg_8_0.topTF:Find("change_btn")

	setText(arg_8_0.inptuTr:Find("holder"), i18n("skinatlas_search_holder"))

	arg_8_0.furnBg = arg_8_0:findTF("Main/right/bg/furn")
	arg_8_0.bgMask = arg_8_0:findTF("Main/right/bg/mask")
	arg_8_0.charBg = arg_8_0:findTF("Main/right/bg/char")
	arg_8_0.switchBtn = arg_8_0:findTF("Main/right/bg/switch")
	arg_8_0.bgRoot = arg_8_0:findTF("bgs/bg")
	arg_8_0.bg1 = arg_8_0:findTF("bgs/bg/bg_1")
	arg_8_0.bg2 = arg_8_0:findTF("bgs/bg/bg_2")
	arg_8_0.bgType = false
	arg_8_0.defaultBg = arg_8_0.bg1:GetComponent(typeof(Image)).sprite
	arg_8_0.blurPanel = arg_8_0:findTF("Main/blur_panel")
	arg_8_0.emptyTr = arg_8_0:findTF("bgs/empty")
	Input.multiTouchEnabled = false
	arg_8_0.viewMode = arg_8_0.contextData.type or var_0_0.SHOP_TYPE_COMMON
	arg_8_0.hideObjToggleTF = arg_8_0:findTF("toggles/hideObjToggle", arg_8_0.rightPanel)

	setActive(arg_8_0.hideObjToggleTF, false)

	arg_8_0.switchCnt = 0
	arg_8_0.l2dPreViewToggle = arg_8_0:findTF("toggles/l2d_preview", arg_8_0.rightPanel)
	arg_8_0.l2dDownloadStateTf = arg_8_0:findTF("toggles/l2d_res_state", arg_8_0.rightPanel)
	arg_8_0.l2dUnDownload = arg_8_0.l2dDownloadStateTf:Find("undownload")
	arg_8_0.l2dDownloaded = arg_8_0.l2dDownloadStateTf:Find("downloaded")
	arg_8_0.live2dContainer = arg_8_0:findTF("painting/paint/live2d")
	arg_8_0.paintingContainer = arg_8_0:findTF("painting")
	arg_8_0.spTF = arg_8_0:findTF("painting/paint/spinePainting")
	arg_8_0.spBg = arg_8_0:findTF("painting/paintBg/spinePainting")
	arg_8_0.defaultIndex = {
		typeIndex = ShipIndexConst.TypeAll,
		campIndex = ShipIndexConst.CampAll,
		rarityIndex = ShipIndexConst.RarityAll,
		extraIndex = SkinIndexLayer.ExtraALL
	}
end

function var_0_0.didEnter(arg_9_0)
	arg_9_0:bind(var_0_0.EVENT_ON_CARD_CLICK, function(arg_10_0, arg_10_1)
		arg_9_0:OnCardClick(arg_10_1)
	end)
	arg_9_0:initShips()
	arg_9_0:initSkinPage()

	if arg_9_0.contextData.skinId then
		arg_9_0:JumpToSkinById(arg_9_0.contextData.skinId)
	end

	onButton(arg_9_0, arg_9_0.topTF:Find("back_btn"), function()
		arg_9_0:emit(var_0_0.ON_BACK)
	end, SFX_CANCEL)
	onButton(arg_9_0, arg_9_0.bottomTF:Find("bg/atlas"), function()
		arg_9_0:emit(SkinShopMediator.ON_ATLAS)
	end, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.bottomTF:Find("bg/right_arr"), function()
		arg_9_0:onNext()
	end, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.bottomTF:Find("bg/left_arr"), function()
		arg_9_0:onPrev()
	end, SFX_PANEL)

	arg_9_0.inSkinMode = true

	onButton(arg_9_0, arg_9_0.switchBtn, function()
		arg_9_0:SwitchCharBg()
	end, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.indexBtn, function()
		arg_9_0:emit(SkinShopMediator.ON_INDEX, {
			OnFilter = function(arg_17_0)
				arg_9_0:OnFilter(arg_17_0)
			end,
			defaultIndex = arg_9_0.defaultIndex
		})
	end, SFX_PANEL)
	onInputChanged(arg_9_0, arg_9_0.inptuTr, function()
		arg_9_0:OnSearch()
	end)

	local var_9_0 = true

	onButton(arg_9_0, arg_9_0.changeBtn, function()
		var_9_0 = not var_9_0

		setActive(arg_9_0.inptuTr, var_9_0)
		setActive(arg_9_0.indexBtn, var_9_0)
		setActive(arg_9_0.live2dFilter, not var_9_0)

		if getInputText(arg_9_0.inptuTr) ~= "" then
			setInputText(arg_9_0.inptuTr, "")
		end
	end, SFX_PANEL)
	triggerButton(arg_9_0.changeBtn)
	onButton(arg_9_0, arg_9_0.live2dFilter, function()
		if arg_9_0.defaultIndex.extraIndex == SkinIndexLayer.ExtraL2D then
			arg_9_0.defaultIndex.extraIndex = SkinIndexLayer.ExtraALL
		else
			arg_9_0.defaultIndex.extraIndex = SkinIndexLayer.ExtraL2D
		end

		arg_9_0:OnFilter(arg_9_0.defaultIndex)
	end, SFX_PANEL)
end

function var_0_0.OnSkinListUpdate(arg_21_0, arg_21_1)
	local var_21_0 = arg_21_1 == 0

	setActive(arg_21_0.emptyTr, var_21_0)
	setActive(arg_21_0.rightPanel, not var_21_0)
	setActive(arg_21_0.paintingContainer, not var_21_0)
	setActive(arg_21_0.namePanel, not var_21_0)
end

function var_0_0.OnSearch(arg_22_0)
	arg_22_0:updateShipRect()
end

function var_0_0.OnFilter(arg_23_0, arg_23_1)
	arg_23_0.defaultIndex = {
		typeIndex = arg_23_1.typeIndex,
		campIndex = arg_23_1.campIndex,
		rarityIndex = arg_23_1.rarityIndex,
		extraIndex = arg_23_1.extraIndex
	}

	setActive(arg_23_0.live2dFilterSel, arg_23_1.extraIndex == SkinIndexLayer.ExtraL2D)
	arg_23_0:updateShipRect()
	setActive(arg_23_0.indexBtnSel, arg_23_1.typeIndex ~= ShipIndexConst.TypeAll or arg_23_1.campIndex ~= ShipIndexConst.CampAll or arg_23_1.rarityIndex ~= ShipIndexConst.RarityAll or arg_23_1.extraIndex ~= SkinIndexLayer.ExtraALL)
end

function var_0_0.JumpToSkinById(arg_24_0, arg_24_1)
	local var_24_0 = -1
	local var_24_1 = {}

	for iter_24_0, iter_24_1 in ipairs(arg_24_0.displays) do
		if arg_24_1 == iter_24_1:getSkinId() then
			var_24_0 = iter_24_0
			var_24_1 = iter_24_1
		end
	end

	if var_24_0 == -1 then
		return
	end

	local var_24_2 = arg_24_0.shipRect:HeadIndexToValue(var_24_0 - 1)

	arg_24_0.shipRect:ScrollTo(var_24_2)
	onNextTick(function()
		for iter_25_0, iter_25_1 in pairs(arg_24_0.cards) do
			if iter_25_1.goodsVO.id == var_24_1.id then
				triggerButton(iter_25_1._tf)

				break
			end
		end
	end)
end

function var_0_0.SwitchCharBg(arg_26_0, arg_26_1)
	local var_26_0 = arg_26_0.furnBg
	local var_26_1 = arg_26_0.charBg

	if not arg_26_1 then
		if LeanTween.isTweening(go(var_26_0)) or LeanTween.isTweening(go(var_26_1)) then
			return
		end
	else
		LeanTween.cancel(go(var_26_0))
		LeanTween.cancel(go(var_26_1))
	end

	local var_26_2 = arg_26_0.goodsId and _.detect(arg_26_0.skinGoodsVOs, function(arg_27_0)
		return arg_27_0.id == arg_26_0.goodsId
	end)

	if not var_26_2 then
		return
	end

	local function var_26_3()
		setActive(arg_26_0.charParent, arg_26_0.inSkinMode)
		setActive(arg_26_0.furParent, not arg_26_0.inSkinMode)
	end

	local var_26_4 = var_26_0:GetComponent(typeof(CanvasGroup))
	local var_26_5 = var_26_1:GetComponent(typeof(CanvasGroup))
	local var_26_6 = var_26_4.alpha
	local var_26_7 = var_26_5.alpha
	local var_26_8 = var_26_0.anchoredPosition3D
	local var_26_9 = var_26_1.anchoredPosition3D

	LeanTween.moveLocal(go(var_26_0), var_26_9, 0.3):setOnComplete(System.Action(function()
		var_26_4.alpha = var_26_7
	end))
	LeanTween.moveLocal(go(var_26_1), var_26_8, 0.3):setOnComplete(System.Action(function()
		var_26_5.alpha = var_26_6

		var_26_3()
	end))

	arg_26_0.inSkinMode = not arg_26_0.inSkinMode

	if arg_26_0.inSkinMode then
		var_26_0:SetAsFirstSibling()
		var_26_1:SetSiblingIndex(2)
	else
		var_26_1:SetAsFirstSibling()
		var_26_0:SetSiblingIndex(2)

		local var_26_10 = Goods.Id2FurnitureId(var_26_2.id)
		local var_26_11 = Goods.GetFurnitureConfig(var_26_2.id)

		arg_26_0.interactionPreview:Flush(var_26_2:getSkinId(), var_26_10, var_26_11.scale[2] or 1, var_26_11.position[2])
	end

	arg_26_0:updateBuyBtn(var_26_2)
	arg_26_0:updatePrice(var_26_2)
end

function var_0_0.initSkinPage(arg_31_0)
	local var_31_0 = {}

	arg_31_0.countByIds = {}

	for iter_31_0, iter_31_1 in ipairs(var_0_1.all) do
		if iter_31_1 == var_0_0.PAGE_PROPOSE or iter_31_1 == var_0_0.PAGE_TRANS then
			-- block empty
		else
			arg_31_0.countByIds[iter_31_1] = 0

			table.insert(var_31_0, iter_31_1)
		end
	end

	for iter_31_2, iter_31_3 in ipairs(arg_31_0.skinGoodsVOs) do
		local var_31_1 = iter_31_3:getSkinId()

		print(var_31_1)

		local var_31_2 = var_0_2[var_31_1]

		if not var_31_2 then
			print("not found = " .. var_31_1)
		end

		local var_31_3 = var_31_2.shop_type_id

		print(var_31_3)

		local var_31_4 = var_31_3 == 0 and 9999 or var_31_3

		arg_31_0.countByIds[var_31_4] = arg_31_0.countByIds[var_31_4] + 1
	end

	local var_31_5 = arg_31_0:findTF("toggles/mask/content", arg_31_0.leftPanel)
	local var_31_6 = {}

	for iter_31_4, iter_31_5 in ipairs(var_31_0) do
		if arg_31_0.countByIds[iter_31_5] > 0 then
			table.insert(var_31_6, iter_31_5)
		end
	end

	if arg_31_0.existAnyEncoreSkin then
		table.insert(var_31_6, var_0_0.PAGE_ENCORE)
	end

	assert(not table.contains(var_31_6, var_0_0.PAGE_ALL) and not table.contains(var_31_6, var_0_0.PAGE_TIME_LIMIT))

	if arg_31_0.viewMode == var_0_0.SHOP_TYPE_TIMELIMIT then
		table.insert(var_31_6, 1, var_0_0.PAGE_TIME_LIMIT)
	end

	table.insert(var_31_6, 1, var_0_0.PAGE_ALL)

	arg_31_0.pageTFs, arg_31_0.mid = {}, 4

	local var_31_7 = var_31_5.parent:Find("0")

	arg_31_0.skinPageToggles = {}

	for iter_31_6, iter_31_7 in ipairs(var_31_6) do
		local var_31_8 = cloneTplTo(var_31_7, var_31_5, iter_31_7)

		setActive(var_31_8, true)

		arg_31_0.skinPageToggles[iter_31_7] = var_31_8:Find("toggle")

		onButton(arg_31_0, var_31_8, function()
			local var_32_0

			for iter_32_0, iter_32_1 in ipairs(arg_31_0.pageTFs) do
				if tonumber(go(iter_32_1).name) == iter_31_7 then
					var_32_0 = iter_32_0

					break
				end
			end

			local var_32_1 = var_32_0 - arg_31_0.mid

			for iter_32_2 = 1, math.abs(var_32_1) do
				arg_31_0:onSwitch(var_32_1)
			end

			arg_31_0:onRelease()
		end, SFX_PANEL)
		arg_31_0:UpdateTagStyle(var_31_8, var_0_1, iter_31_7)
	end

	eachChild(var_31_5, function(arg_33_0)
		if arg_33_0.gameObject.activeSelf then
			table.insert(arg_31_0.pageTFs, 1, arg_33_0)
		end
	end)
	arg_31_0:addVerticalDrag(arg_31_0.leftPanel, function(arg_34_0)
		arg_31_0:onSwitch(arg_34_0)
	end, function()
		arg_31_0:onRelease()
	end)
	arg_31_0:UpdateViewMode(var_31_5)
end

function var_0_0.onSwitch(arg_36_0, arg_36_1)
	if arg_36_1 > 0 then
		local var_36_0 = table.remove(arg_36_0.pageTFs, 1)

		var_36_0:SetAsLastSibling()
		table.insert(arg_36_0.pageTFs, var_36_0)
	else
		local var_36_1 = table.remove(arg_36_0.pageTFs, #arg_36_0.pageTFs)

		var_36_1:SetAsFirstSibling()
		table.insert(arg_36_0.pageTFs, 1, var_36_1)
	end

	triggerToggle(arg_36_0.pageTFs[arg_36_0.mid]:Find("toggle"), true)
end

function var_0_0.onRelease(arg_37_0)
	local var_37_0 = tonumber(go(arg_37_0.pageTFs[arg_37_0.mid]).name)

	arg_37_0:index2PageId(var_37_0)
end

function var_0_0.index2PageId(arg_38_0, arg_38_1)
	arg_38_0.contextData.pageId = arg_38_1
	arg_38_0.isSwitch = true

	arg_38_0:updateShipRect(0)
	triggerToggle(arg_38_0.skinPageToggles[arg_38_1], true)
	arg_38_0:SwitchCntPlusPlus()
end

function var_0_0.UpdateViewMode(arg_39_0, arg_39_1)
	local var_39_0
	local var_39_1
	local var_39_2

	if arg_39_0.viewMode == var_0_0.SHOP_TYPE_TIMELIMIT then
		var_39_0 = var_0_0.PAGE_TIME_LIMIT
	elseif arg_39_0.viewMode == var_0_0.SHOP_TYPE_COMMON then
		var_39_0 = arg_39_0.contextData.warp or var_0_0.PAGE_ALL
	end

	setActive(arg_39_0.leftPanel, arg_39_0.viewMode == var_0_0.SHOP_TYPE_COMMON)
	triggerButton(arg_39_1:Find(var_39_0))
	setImageSprite(arg_39_0.title, GetSpriteFromAtlas("ui/SkinShopUI_atlas", var_0_3[arg_39_0.viewMode][1]), true)
	setImageSprite(arg_39_0.titleEn, GetSpriteFromAtlas("ui/SkinShopUI_atlas", var_0_3[arg_39_0.viewMode][2]), true)
end

function var_0_0.UpdateTagStyle(arg_40_0, arg_40_1, arg_40_2, arg_40_3)
	if arg_40_2[arg_40_3] then
		setImageSprite(arg_40_1:Find("name"), GetSpriteFromAtlas("SkinClassified", "text_" .. arg_40_2[arg_40_3].res .. "01"), true)
		setImageSprite(arg_40_1:Find("selected/Image"), GetSpriteFromAtlas("SkinClassified", "text_" .. arg_40_2[arg_40_3].res), true)
		setText(arg_40_1:Find("eng"), string.upper(arg_40_2[arg_40_3].english_name or ""))
	elseif arg_40_3 == var_0_0.PAGE_ALL then
		setImageSprite(arg_40_1:Find("name"), GetSpriteFromAtlas("SkinClassified", "text_all01"), true)
		setImageSprite(arg_40_1:Find("selected/Image"), GetSpriteFromAtlas("SkinClassified", "text_all"), true)
		setText(arg_40_1:Find("eng"), "ALL")
	elseif arg_40_3 == var_0_0.PAGE_ENCORE then
		setImageSprite(arg_40_1:Find("name"), GetSpriteFromAtlas("SkinClassified", "text_fanchang"), true)
		setImageSprite(arg_40_1:Find("selected/Image"), GetSpriteFromAtlas("SkinClassified", "text_fanchang01"), true)
		setText(arg_40_1:Find("eng"), "RETURN")
	end
end

function var_0_0.updateMainView(arg_41_0, arg_41_1)
	local var_41_0 = arg_41_1.shipSkinConfig

	arg_41_0.showCardId = arg_41_1.goodsVO.id

	local var_41_1 = ShipGroup.getDefaultShipConfig(var_41_0.ship_group)

	arg_41_0.nameTxt.text = var_41_1.name
	arg_41_0.skinNameTxt.text = SwitchSpecialChar(var_41_0.name, true)

	local var_41_2 = var_41_0.prefab

	if arg_41_0.prefabName ~= var_41_2 then
		arg_41_0:loadChar(var_41_2, var_41_0)

		arg_41_0.prefabName = var_41_2
	end

	local var_41_3 = var_41_0.painting
	local var_41_4 = checkABExist("painting/" .. var_41_3 .. "_n")

	setActive(arg_41_0.hideObjToggleTF, var_41_4)

	local var_41_5 = false

	eachChild(arg_41_0.tags, function(arg_42_0)
		local var_42_0 = go(arg_42_0).name
		local var_42_1 = table.contains(var_41_0.tag, tonumber(var_42_0))

		if var_42_1 then
			var_41_5 = true
		end

		setActive(arg_42_0, var_42_1)
	end)

	if not var_41_4 and var_41_0.bg_sp ~= "" then
		arg_41_0:setBg(var_41_1, var_41_0, true)
	else
		arg_41_0:setBg(var_41_1, var_41_0, var_41_4)
	end

	arg_41_0:updatePrice(arg_41_1.goodsVO)
	arg_41_0:removeShopTimer()
	arg_41_0:addShopTimer(arg_41_1)
	arg_41_0:updateBuyBtn(arg_41_1.goodsVO)

	local var_41_6 = {
		false
	}

	arg_41_0:UpdateLiveToggle(var_41_0.id, var_41_6)

	if var_41_6[1] == false and arg_41_0.painting ~= var_41_3 then
		arg_41_0:loadPainting(var_41_3, true)

		arg_41_0.painting = var_41_3
	end

	arg_41_0.goodsId = arg_41_1.goodsVO.id
end

function var_0_0.UpdateLiveToggle(arg_43_0, arg_43_1, arg_43_2)
	local var_43_0 = ShipSkin.New({
		id = arg_43_1
	})
	local var_43_1 = var_43_0:IsSpine()
	local var_43_2 = var_43_0:IsLive2d()
	local var_43_3 = var_43_2 or var_43_1
	local var_43_4 = getProxy(PlayerProxy):getRawData().id
	local var_43_5 = PlayerPrefs.GetInt("skinShop#l2dPreViewToggle" .. var_43_4, 0) == 1
	local var_43_6 = pg.ship_skin_template[var_43_0.id].painting
	local var_43_7 = checkABExist("painting/" .. var_43_6 .. "_n")
	local var_43_8 = true

	if var_43_3 then
		onToggle(arg_43_0, arg_43_0.l2dPreViewToggle, function(arg_44_0)
			setActive(arg_43_0.hideObjToggleTF, not arg_44_0 and var_43_7)
			setActive(arg_43_0.l2dDownloadStateTf, arg_44_0)

			if arg_44_0 then
				PlayerPrefs.SetInt("skinShop#l2dPreViewToggle" .. var_43_4, 1)

				if var_43_2 then
					arg_43_0:UpdateLive2dDownloadState(var_43_0, arg_43_2)
				elseif var_43_1 then
					arg_43_0:UpdateSpineState(var_43_0, arg_43_2)
				end
			else
				PlayerPrefs.SetInt("skinShop#l2dPreViewToggle" .. var_43_4, 0)
				arg_43_0:loadPainting(var_43_6, arg_43_0.isHideObj)

				arg_43_0.painting = var_43_6
			end

			PlayerPrefs.Save()

			if not var_43_8 then
				arg_43_0:emit(SkinShopMediator.ON_RECORD_ANIM_PREVIEW_BTN, arg_44_0)
			else
				var_43_8 = false
			end
		end, SFX_PANEL)
	else
		removeOnToggle(arg_43_0.l2dPreViewToggle)
		setActive(arg_43_0.l2dDownloadStateTf, false)
		setActive(arg_43_0.hideObjToggleTF, var_43_7)
	end

	triggerToggle(arg_43_0.l2dPreViewToggle, var_43_5)
	setActive(arg_43_0.l2dPreViewToggle, var_43_3)

	arg_43_0.skinId = arg_43_1
end

function var_0_0.UpdateSpineState(arg_45_0, arg_45_1, arg_45_2)
	local var_45_0 = pg.ship_skin_template[arg_45_1.id].painting
	local var_45_1 = "SpinePainting/" .. string.lower(var_45_0)
	local var_45_2 = HXSet.autoHxShiftPath(var_45_1, nil, true)
	local var_45_3 = checkABExist(var_45_2)

	setActive(arg_45_0.l2dUnDownload, not var_45_3)
	setActive(arg_45_0.l2dDownloaded, var_45_3)

	if not var_45_3 then
		onButton(arg_45_0, arg_45_0.l2dDownloadStateTf, function()
			pg.TipsMgr.GetInstance():ShowTips("word_cmdClose")
		end, SFX_PANEL)

		if arg_45_2 then
			arg_45_2[1] = false
		end
	else
		if arg_45_2 then
			arg_45_2[1] = true
		end

		removeOnButton(arg_45_0.l2dDownloadStateTf)
		arg_45_0:LoadSpine(arg_45_1)
	end
end

function var_0_0.LoadSpine(arg_47_0, arg_47_1)
	arg_47_0:recyclePainting()
	arg_47_0:UnLoadLive2d()
	arg_47_0:UnloadSpine()

	local var_47_0 = pg.ship_skin_template[arg_47_1.id].ship_group
	local var_47_1 = ShipGroup.getDefaultShipConfig(var_47_0)
	local var_47_2 = SpinePainting.GenerateData({
		ship = Ship.New({
			id = 999,
			configId = var_47_1.id,
			skin_id = arg_47_1.id
		}),
		position = Vector3(0, 0, 0),
		parent = arg_47_0.spTF,
		effectParent = arg_47_0.spBg
	})

	arg_47_0.spinePainting = SpinePainting.New(var_47_2, function(arg_48_0)
		return
	end)
end

function var_0_0.UnloadSpine(arg_49_0, arg_49_1)
	if arg_49_0.spinePainting then
		arg_49_0.spinePainting:Dispose()

		arg_49_0.spinePainting = nil
	end
end

function var_0_0.UpdateLive2dDownloadState(arg_50_0, arg_50_1, arg_50_2)
	local var_50_0 = pg.ship_skin_template[arg_50_1.id].painting
	local var_50_1 = "live2d/" .. string.lower(var_50_0)
	local var_50_2 = HXSet.autoHxShiftPath(var_50_1, nil, true)
	local var_50_3 = checkABExist(var_50_2)

	setActive(arg_50_0.l2dUnDownload, not var_50_3)
	setActive(arg_50_0.l2dDownloaded, var_50_3)

	if not var_50_3 then
		onButton(arg_50_0, arg_50_0.l2dDownloadStateTf, function()
			if arg_50_0.downloads[arg_50_1.id] then
				return
			end

			local var_51_0 = SkinShopDownloadRequest.New()

			arg_50_0.downloads[arg_50_1.id] = var_51_0

			var_51_0:Start(var_50_2, function(arg_52_0)
				if arg_52_0 and arg_50_0.skinId == arg_50_1.id then
					arg_50_0:UpdateLive2dDownloadState(arg_50_1)
				end

				var_51_0:Dispose()

				arg_50_0.downloads[arg_50_1.id] = nil
			end)
		end, SFX_PANEL)

		if arg_50_2 then
			arg_50_2[1] = false
		end
	else
		if arg_50_2 then
			arg_50_2[1] = true
		end

		removeOnButton(arg_50_0.l2dDownloadStateTf)
		arg_50_0:LoadL2d(arg_50_1)
	end
end

function var_0_0.LoadL2d(arg_53_0, arg_53_1)
	arg_53_0:recyclePainting()
	arg_53_0:UnLoadLive2d()
	arg_53_0:UnloadSpine()

	local var_53_0 = pg.ship_skin_template[arg_53_1.id].ship_group
	local var_53_1 = ShipGroup.getDefaultShipConfig(var_53_0)
	local var_53_2 = Live2D.GenerateData({
		ship = Ship.New({
			id = 999,
			configId = var_53_1.id,
			skin_id = arg_53_1.id
		}),
		scale = Vector3(52, 52, 52),
		position = Vector3(0, 0, -1),
		parent = arg_53_0.live2dContainer
	})

	var_53_2.shopPreView = true

	pg.UIMgr.GetInstance():LoadingOn()

	arg_53_0.live2dChar = Live2D.New(var_53_2, function(arg_54_0)
		arg_53_0:recyclePainting()
		arg_54_0:IgonreReactPos(true)
		pg.UIMgr.GetInstance():LoadingOff()
	end)
end

function var_0_0.UnLoadLive2d(arg_55_0, arg_55_1)
	if arg_55_0.live2dChar then
		arg_55_0.live2dChar:Dispose()

		arg_55_0.live2dChar = nil
	end
end

function var_0_0.setBg(arg_56_0, arg_56_1, arg_56_2, arg_56_3)
	local var_56_0 = Ship.New({
		configId = arg_56_1.id,
		skin_id = arg_56_2.id
	})
	local var_56_1 = var_56_0:getShipBgPrint(true)

	if arg_56_3 and arg_56_2.bg_sp ~= "" then
		var_56_1 = arg_56_2.bg_sp
	end

	if var_56_1 ~= var_56_0:rarity2bgPrintForGet() then
		local var_56_2 = arg_56_0:GetCurBgTransform()

		pg.DynamicBgMgr.GetInstance():LoadBg(arg_56_0, var_56_1, arg_56_0.bgRoot, var_56_2, function(arg_57_0)
			return
		end, function(arg_58_0)
			arg_56_0:AnimBg()
		end)
	else
		setImageSprite(arg_56_0:GetCurBgTransform(), arg_56_0.defaultBg)
		arg_56_0:AnimBg()
	end
end

function var_0_0.GetCurBgTransform(arg_59_0)
	local var_59_0

	if not arg_59_0.bgType then
		var_59_0 = arg_59_0.bg2
	else
		var_59_0 = arg_59_0.bg1
	end

	arg_59_0.bgType = not arg_59_0.bgType

	return var_59_0
end

function var_0_0.AnimBg(arg_60_0)
	local var_60_0
	local var_60_1

	if arg_60_0.bgType then
		var_60_0 = arg_60_0.bg2
		var_60_1 = arg_60_0.bg1
	else
		var_60_0 = arg_60_0.bg1
		var_60_1 = arg_60_0.bg2
	end

	LeanTween.cancel(go(arg_60_0.bg2))
	LeanTween.cancel(go(arg_60_0.bg1))
	setActive(var_60_0, true)
	var_60_0:SetAsLastSibling()
	LeanTween.alpha(var_60_0, 1, 0.8):setFrom(0):setOnComplete(System.Action(function()
		setImageAlpha(var_60_0, 1)
		setImageAlpha(var_60_1, 0)
	end))
end

function var_0_0.onBuyDone(arg_62_0, arg_62_1)
	local var_62_0 = _.detect(arg_62_0.skinGoodsVOs, function(arg_63_0)
		return arg_63_0.id == arg_62_1
	end)

	if var_62_0 then
		arg_62_0:updateBuyBtn(var_62_0)
		arg_62_0:updatePrice(var_62_0)
		arg_62_0:removeShopTimer()
		arg_62_0:addShopTimer({
			goodsVO = var_62_0
		})
	end
end

function var_0_0.OnFurnitureUpdate(arg_64_0, arg_64_1)
	if arg_64_0.goodsId and arg_64_1 and Goods.ExistFurniture(arg_64_0.goodsId) and Goods.Id2FurnitureId(arg_64_0.goodsId) == arg_64_1 then
		local var_64_0 = _.detect(arg_64_0.skinGoodsVOs, function(arg_65_0)
			return arg_65_0.id == arg_64_0.goodsId
		end)

		arg_64_0:updateBuyBtn(var_64_0)
	end
end

function var_0_0.updateBuyBtn(arg_66_0, arg_66_1)
	local var_66_0 = arg_66_1:getConfig("genre") == ShopArgs.SkinShopTimeLimit
	local var_66_1

	if var_66_0 then
		onButton(arg_66_0, arg_66_0.timelimitBtn, function()
			local var_67_0 = arg_66_1:getSkinId()
			local var_67_1 = getProxy(ShipSkinProxy):getSkinById(var_67_0)

			if var_67_1 and not var_67_1:isExpireType() then
				pg.TipsMgr.GetInstance():ShowTips(i18n("already_have_the_skin"))

				return
			end

			arg_66_0:showTimeLimitSkinWindow(arg_66_1)
		end, SFX_PANEL)

		var_66_1 = var_0_2[arg_66_1:getSkinId()]
	else
		local var_66_2 = arg_66_1:getSkinId()

		var_66_1 = var_0_2[var_66_2]

		local var_66_3 = arg_66_1.type
		local var_66_4 = var_66_3 == Goods.TYPE_ACTIVITY or var_66_3 == Goods.TYPE_ACTIVITY_EXTRA
		local var_66_5 = arg_66_1.buyCount == 0
		local var_66_6 = arg_66_1:isDisCount() and arg_66_1:IsItemDiscountType()
		local var_66_7 = not arg_66_0.inSkinMode
		local var_66_8 = false

		if var_66_7 then
			var_66_8 = getProxy(DormProxy):getRawData():HasFurniture(Goods.Id2FurnitureId(arg_66_1.id))
		end

		setActive(arg_66_0.itemBtn, var_66_6 and var_66_5 and not var_66_7)
		setActive(arg_66_0.buyBtn, not var_66_4 and var_66_5 and not var_66_6 and not var_66_7)
		setActive(arg_66_0.gotBtn, not var_66_4 and not var_66_5 and not var_66_7 or var_66_7 and var_66_8)
		setActive(arg_66_0.activityBtn, var_66_4 and not var_66_6 and not var_66_7)
		setActive(arg_66_0.backyardBtn, var_66_7 and not var_66_8)
		onButton(arg_66_0, arg_66_0.itemBtn, function()
			triggerButton(arg_66_0.buyBtn)
		end, SFX_PANEL)
		onButton(arg_66_0, arg_66_0.buyBtn, function()
			local var_69_0 = arg_66_1

			if var_69_0.type == Goods.TYPE_SKIN then
				if arg_66_0.showCardId == var_69_0.id then
					if arg_66_1:isDisCount() and var_69_0:IsItemDiscountType() then
						arg_66_0:emit(SkinShopMediator.ON_SHOPPING_BY_ACT, var_69_0.id, 1)
					else
						local var_69_1 = var_69_0:GetPrice()
						local var_69_2 = i18n("charge_scene_buy_confirm", var_69_1, var_66_1.name)

						pg.MsgboxMgr.GetInstance():ShowMsgBox({
							content = var_69_2,
							onYes = function()
								arg_66_0:emit(SkinShopMediator.ON_SHOPPING, var_69_0.id, 1)
							end
						})
					end
				else
					pg.TipsMgr.GetInstance():ShowTips(ERROR_MESSAGE[9999])

					return
				end
			end
		end, SFX_PANEL)
		onButton(arg_66_0, arg_66_0.activityBtn, function()
			local var_71_0 = arg_66_1
			local var_71_1 = var_71_0:getConfig("time")
			local var_71_2 = var_71_0:getConfig("activity")
			local var_71_3 = getProxy(ActivityProxy):getActivityById(var_71_2)

			if var_71_2 == 0 and pg.TimeMgr.GetInstance():inTime(var_71_1) or var_71_3 and not var_71_3:isEnd() then
				if var_71_0.type == Goods.TYPE_ACTIVITY then
					arg_66_0:emit(SkinShopMediator.GO_SHOPS_LAYER, var_71_0:getConfig("activity"))
				elseif var_71_0.type == Goods.TYPE_ACTIVITY_EXTRA then
					local var_71_4 = var_71_0:getConfig("scene")

					if var_71_4 and #var_71_4 > 0 then
						arg_66_0:emit(SkinShopMediator.OPEN_SCENE, var_71_4)
					else
						arg_66_0:emit(SkinShopMediator.OPEN_ACTIVITY, var_71_2)
					end
				end
			else
				pg.TipsMgr.GetInstance():ShowTips(i18n("common_activity_not_start"))
			end
		end, SFX_PANEL)
		onButton(arg_66_0, arg_66_0.backyardBtn, function()
			arg_66_0:emit(SkinShopMediator.ON_BACKYARD_SHOP)
		end, SFX_PANEL)
	end

	local var_66_9 = ShipGroup.getDefaultShipConfig(var_66_1.ship_group)

	removeOnToggle(arg_66_0.hideObjToggleTF)
	triggerToggle(arg_66_0.hideObjToggleTF, true)

	arg_66_0.isHideObj = true

	onToggle(arg_66_0, arg_66_0.hideObjToggleTF, function(arg_73_0)
		arg_66_0.isHideObj = arg_73_0

		local var_73_0 = arg_66_0.painting

		arg_66_0:loadPainting(var_73_0, arg_73_0)

		arg_66_0.painting = var_73_0

		arg_66_0:setBg(var_66_9, var_66_1, arg_73_0)
	end, SFX_PANEL)
end

function var_0_0.showTimeLimitSkinWindow(arg_74_0, arg_74_1)
	local var_74_0 = arg_74_1:getConfig("resource_num")
	local var_74_1 = arg_74_1:getConfig("time_second") * var_74_0
	local var_74_2 = arg_74_1:getSkinId()
	local var_74_3 = pg.ship_skin_template[var_74_2]

	assert(var_74_3)

	local var_74_4, var_74_5, var_74_6, var_74_7 = pg.TimeMgr.GetInstance():parseTimeFrom(var_74_1)

	pg.MsgboxMgr.GetInstance():ShowMsgBox({
		content = i18n("exchange_limit_skin_tip", var_74_0, var_74_3.name, var_74_4, var_74_5),
		onYes = function()
			if arg_74_0.skinTicket < var_74_0 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("common_no_item_1"))

				return
			end

			arg_74_0:emit(SkinShopMediator.ON_SHOPPING, arg_74_1.id, 1)
		end
	})
end

function var_0_0.addShopTimer(arg_76_0, arg_76_1)
	local var_76_0 = arg_76_1.goodsVO
	local var_76_1 = var_76_0:getSkinId()

	if arg_76_0.skinTimer then
		arg_76_0.skinTimer:Stop()
	end

	setActive(tf(go(arg_76_0.limitTxt)).parent, true)

	if var_76_0:getConfig("genre") == ShopArgs.SkinShopTimeLimit then
		local var_76_2 = getProxy(ShipSkinProxy):getSkinById(var_76_1)
		local var_76_3 = var_76_2 and var_76_2:isExpireType() and not var_76_2:isExpired()

		setActive(tf(go(arg_76_0.limitTxt)).parent, var_76_3)

		if var_76_3 then
			arg_76_0.skinTimer = Timer.New(function()
				local var_77_0 = skinTimeStamp(var_76_2:getRemainTime())

				arg_76_0.limitTxt.text = var_77_0
			end, 1, -1)

			arg_76_0.skinTimer:Start()
			arg_76_0.skinTimer.func()
		else
			setActive(tf(go(arg_76_0.limitTxt)).parent, false)
		end
	else
		local var_76_4, var_76_5 = pg.TimeMgr.GetInstance():inTime(var_76_0:getConfig("time"))

		if not var_76_5 then
			setActive(tf(go(arg_76_0.limitTxt)).parent, false)

			return
		end

		local var_76_6 = pg.TimeMgr.GetInstance()
		local var_76_7 = var_76_6:Table2ServerTime(var_76_5)

		arg_76_0.shopTimer = Timer.New(function()
			local var_78_0 = var_76_6:GetServerTime()

			if var_78_0 > var_76_7 then
				arg_76_0:removeShopTimer()
			end

			local var_78_1 = var_76_7 - var_78_0

			var_78_1 = var_78_1 < 0 and 0 or var_78_1

			local var_78_2 = math.floor(var_78_1 / 86400)

			if var_78_2 > 0 then
				arg_76_0.limitTxt.text = i18n("time_remaining_tip") .. var_78_2 .. i18n("word_date")
			else
				local var_78_3 = math.floor(var_78_1 / 3600)

				if var_78_3 > 0 then
					arg_76_0.limitTxt.text = i18n("time_remaining_tip") .. var_78_3 .. i18n("word_hour")
				else
					local var_78_4 = math.floor(var_78_1 / 60)

					if var_78_4 > 0 then
						arg_76_0.limitTxt.text = i18n("time_remaining_tip") .. var_78_4 .. i18n("word_minute")
					else
						arg_76_0.limitTxt.text = i18n("time_remaining_tip") .. var_78_1 .. i18n("word_second")
					end
				end
			end
		end, 1, -1)

		arg_76_0.shopTimer:Start()
		arg_76_0.shopTimer.func()
	end
end

function var_0_0.removeShopTimer(arg_79_0)
	if arg_79_0.shopTimer then
		arg_79_0.shopTimer:Stop()

		arg_79_0.shopTimer = nil
	end
end

function var_0_0.updatePrice(arg_80_0, arg_80_1)
	local var_80_0 = arg_80_1:getSkinId()
	local var_80_1 = var_0_2[var_80_0]
	local var_80_2 = arg_80_1
	local var_80_3 = var_80_2:getConfig("genre") == ShopArgs.SkinShopTimeLimit

	setActive(arg_80_0.commonPanel, not var_80_3)
	setActive(arg_80_0.timelimtPanel, var_80_3)

	if var_80_3 then
		local var_80_4 = var_80_2:getConfig("resource_num")
		local var_80_5 = (var_80_4 > arg_80_0.skinTicket and "<color=" .. COLOR_RED .. ">" or "") .. arg_80_0.skinTicket .. (var_80_4 > arg_80_0.skinTicket and "</color>" or "")

		arg_80_0.timelimitPriceTxt.text = var_80_5 .. "/" .. var_80_4
	elseif arg_80_0.inSkinMode then
		local var_80_6 = var_80_2.type == Goods.TYPE_SKIN

		setActive(arg_80_0.commonBGTF, var_80_6)
		setActive(arg_80_0.commonLabelTF, var_80_6)
		setActive(arg_80_0.commonConsumeTF, var_80_6)

		if var_80_6 then
			local var_80_7 = (100 - var_80_2:getConfig("discount")) / 100
			local var_80_8 = var_80_2:getConfig("resource_num")
			local var_80_9 = var_80_2:isDisCount()

			arg_80_0.priceTxt.text = var_80_2:GetPrice()
			arg_80_0.originalPriceTxt.text = var_80_8

			setActive(tf(go(arg_80_0.originalPriceTxt)).parent, var_80_9)
		end
	else
		local var_80_10 = Goods.Id2FurnitureId(var_80_2.id)
		local var_80_11 = Furniture.New({
			id = var_80_10
		})
		local var_80_12 = var_80_11:getConfig("gem_price")

		arg_80_0.originalPriceTxt.text = var_80_12

		local var_80_13 = var_80_11:getPrice(PlayerConst.ResDiamond)

		arg_80_0.priceTxt.text = var_80_13

		setActive(tf(go(arg_80_0.originalPriceTxt)).parent, var_80_12 ~= var_80_13)
	end
end

function var_0_0.loadPainting(arg_81_0, arg_81_1, arg_81_2)
	arg_81_0:recyclePainting()
	arg_81_0:UnLoadLive2d()
	arg_81_0:UnloadSpine()
	arg_81_0:setPaintingPrefab(arg_81_0.paintingTF, arg_81_1, "chuanwu", arg_81_2)
end

function var_0_0.setPaintingPrefab(arg_82_0, arg_82_1, arg_82_2, arg_82_3, arg_82_4)
	local var_82_0 = findTF(arg_82_1, "fitter")

	assert(var_82_0, "请添加子物体fitter")
	removeAllChildren(var_82_0)

	local var_82_1 = GetOrAddComponent(var_82_0, "PaintingScaler")

	var_82_1.FrameName = arg_82_3 or ""
	var_82_1.Tween = 1

	local var_82_2 = arg_82_2

	if not arg_82_4 and checkABExist("painting/" .. arg_82_2 .. "_n") then
		arg_82_2 = arg_82_2 .. "_n"
	end

	if checkABExist("painting/" .. arg_82_2) then
		pg.UIMgr.GetInstance():LoadingOn()
		PoolMgr.GetInstance():GetPainting(arg_82_2, true, function(arg_83_0)
			pg.UIMgr.GetInstance():LoadingOff()
			setParent(arg_83_0, var_82_0, false)

			local var_83_0 = findTF(arg_83_0, "Touch")

			if not IsNil(var_83_0) then
				setActive(var_83_0, false)
			end

			ShipExpressionHelper.SetExpression(var_82_0:GetChild(0), var_82_2)
		end)
	end
end

function var_0_0.recyclePainting(arg_84_0)
	if arg_84_0.painting then
		retPaintingPrefab(arg_84_0.paintingTF, arg_84_0.painting)
	end

	arg_84_0.painting = nil
end

function var_0_0.loadChar(arg_85_0, arg_85_1, arg_85_2)
	arg_85_0:recycleChar()
	pg.UIMgr.GetInstance():LoadingOn()
	PoolMgr.GetInstance():GetSpineChar(arg_85_1, true, function(arg_86_0)
		pg.UIMgr.GetInstance():LoadingOff()

		arg_85_0.modelTf = tf(arg_86_0)

		local var_86_0 = pg.skinshop_spine_scale[arg_85_2.id]

		if var_86_0 then
			arg_85_0.modelTf.localScale = Vector3(var_86_0.skinshop_scale, var_86_0.skinshop_scale, 1)
		else
			arg_85_0.modelTf.localScale = Vector3(0.9, 0.9, 1)
		end

		arg_85_0.modelTf.localPosition = Vector3(0, 0, 0)

		pg.ViewUtils.SetLayer(arg_85_0.modelTf, Layer.UI)
		setParent(arg_85_0.modelTf, arg_85_0.charParent)
		arg_86_0:GetComponent("SpineAnimUI"):SetAction("normal", 0)
	end)
end

function var_0_0.recycleChar(arg_87_0)
	if not IsNil(arg_87_0.modelTf) then
		arg_87_0.modelTf.gameObject:GetComponent("SpineAnimUI"):SetActionCallBack(nil)
		PoolMgr.GetInstance():ReturnSpineChar(arg_87_0.prefabName, arg_87_0.modelTf.gameObject)
	end

	if arg_87_0.timer then
		arg_87_0.timer:Stop()

		arg_87_0.timer = nil
	end
end

function var_0_0.OnCardClick(arg_88_0, arg_88_1)
	if arg_88_0.card and arg_88_0.contextData.key == arg_88_1.goodsVO:getKey() then
		return
	end

	if arg_88_0.contextData.key then
		for iter_88_0, iter_88_1 in pairs(arg_88_0.cards) do
			if iter_88_1.goodsVO:getKey() == arg_88_0.contextData.key then
				iter_88_1:updateSelected(false)
			end
		end
	end

	arg_88_1:updateSelected(true)

	arg_88_0.contextData.key = arg_88_1.goodsVO:getKey()
	arg_88_0.card = arg_88_1

	if not arg_88_0.inSkinMode then
		arg_88_0:SwitchCharBg(true)
	end

	arg_88_0:updateMainView(arg_88_1)
	arg_88_0:UpdateSkinOrFurnitureMode(Goods.ExistFurniture(arg_88_1.goodsVO.id))

	for iter_88_2, iter_88_3 in ipairs(arg_88_0.displays) do
		if iter_88_3 == arg_88_0.card.goodsVO then
			arg_88_0.index = iter_88_2
		end
	end

	arg_88_0:SwitchCntPlusPlus()
end

function var_0_0.UpdateSkinOrFurnitureMode(arg_89_0, arg_89_1)
	setActive(arg_89_0.switchBtn, arg_89_1)
	setActive(arg_89_0.furnBg, arg_89_1)
	setActive(arg_89_0.bgMask, arg_89_1)
end

function var_0_0.initShips(arg_90_0)
	arg_90_0.cards = {}
	arg_90_0.shipRect = arg_90_0.bottomTF:Find("scroll"):GetComponent("LScrollRect")

	function arg_90_0.shipRect.onInitItem(arg_91_0)
		local var_91_0 = ShopSkinCard.New(arg_91_0, arg_90_0)

		arg_90_0.cards[arg_91_0] = var_91_0
	end

	function arg_90_0.shipRect.onUpdateItem(arg_92_0, arg_92_1)
		local var_92_0 = arg_90_0.cards[arg_92_1]

		if not var_92_0 then
			var_92_0 = ShopSkinCard.New(arg_92_1, arg_90_0)
			arg_90_0.cards[arg_92_1] = var_92_0
		end

		local var_92_1 = arg_90_0.displays[arg_92_0 + 1]

		var_92_0:update(var_92_1)
		var_92_0:updateSelected(arg_90_0.contextData.key == var_92_0.goodsVO:getKey())

		if arg_90_0.isSwitch and arg_92_0 == 0 then
			arg_90_0.isSwitch = nil

			triggerButton(var_92_0._tf)
		end
	end
end

function var_0_0.SwitchCntPlusPlus(arg_93_0)
	arg_93_0.switchCnt = arg_93_0.switchCnt + 1

	if arg_93_0.switchCnt >= 2 then
		gcAll()

		arg_93_0.switchCnt = 0
	end
end

function var_0_0.onNext(arg_94_0)
	if arg_94_0.index == #arg_94_0.displays then
		return
	end

	local var_94_0

	for iter_94_0, iter_94_1 in ipairs(arg_94_0.displays) do
		if iter_94_1:getKey() == arg_94_0.contextData.key then
			var_94_0 = iter_94_0

			break
		end
	end

	if var_94_0 then
		local var_94_1 = false
		local var_94_2 = math.min(var_94_0 + 1, #arg_94_0.displays)

		arg_94_0.index = var_94_2

		local var_94_3
		local var_94_4 = arg_94_0.displays[var_94_2]

		for iter_94_2, iter_94_3 in pairs(arg_94_0.cards) do
			if iter_94_3.goodsVO:getKey() == var_94_4:getKey() and iter_94_3._tf.gameObject.name ~= "-1" then
				triggerButton(iter_94_3._tf)

				var_94_1 = true
				var_94_3 = iter_94_3

				break
			end
		end

		local function var_94_5()
			local var_95_0 = getBounds(arg_94_0.bottomTF:Find("scroll"))
			local var_95_1 = getBounds(var_94_3._tf)
			local var_95_2 = getBounds(arg_94_0.card._tf)

			return math.ceil(var_95_1:GetMax().x - var_95_0:GetMax().x) > var_95_2.size.x
		end

		if var_94_1 and var_94_5() then
			local var_94_6 = arg_94_0.shipRect:HeadIndexToValue(var_94_2 - 1) - arg_94_0.shipRect:HeadIndexToValue(var_94_2)
			local var_94_7 = arg_94_0.shipRect.value - var_94_6

			arg_94_0.shipRect:SetNormalizedPosition(var_94_7, 0)
		end
	end
end

function var_0_0.onPrev(arg_96_0)
	if arg_96_0.index == 1 then
		return
	end

	local var_96_0

	for iter_96_0, iter_96_1 in ipairs(arg_96_0.displays) do
		if iter_96_1:getKey() == arg_96_0.contextData.key then
			var_96_0 = iter_96_0

			break
		end
	end

	if var_96_0 then
		local var_96_1 = false
		local var_96_2 = math.max(var_96_0 - 1, 1)

		arg_96_0.index = var_96_2

		local var_96_3 = arg_96_0.displays[var_96_2]

		for iter_96_2, iter_96_3 in pairs(arg_96_0.cards) do
			if iter_96_3.goodsVO:getKey() == var_96_3:getKey() and iter_96_3._tf.gameObject.name ~= "-1" then
				triggerButton(iter_96_3._tf)

				var_96_1 = true

				break
			end
		end

		local function var_96_4()
			local var_97_0 = getBounds(arg_96_0.bottomTF:Find("scroll"))
			local var_97_1 = getBounds(arg_96_0.bottomTF:Find("scroll/content"))
			local var_97_2 = getBounds(arg_96_0.card._tf)

			return var_97_1:GetMin().x < var_97_0:GetMin().x and var_97_2:GetMin().x < var_97_0:GetMin().x
		end

		if var_96_1 and var_96_4() then
			local var_96_5 = arg_96_0.shipRect:HeadIndexToValue(var_96_2 - 1)

			arg_96_0.shipRect:SetNormalizedPosition(var_96_5, 0)
		end
	end
end

function var_0_0.updateShipRect(arg_98_0, arg_98_1)
	arg_98_0.card = nil

	if arg_98_0.contextData.pageId and arg_98_0.shipRect then
		arg_98_0.displays = {}

		local function var_98_0(arg_99_0)
			return arg_98_0.encoreSkinMap[arg_99_0] == true
		end

		local var_98_1 = {}

		local function var_98_2(arg_100_0)
			if #var_98_1 == 0 then
				for iter_100_0, iter_100_1 in ipairs(arg_98_0.skinGoodsVOs) do
					if iter_100_1:getConfig("genre") == ShopArgs.SkinShop then
						local var_100_0 = iter_100_1:getSkinId()

						var_98_1[var_100_0] = true
					end
				end
			end

			return var_98_1[arg_100_0] == true
		end

		for iter_98_0, iter_98_1 in ipairs(arg_98_0.skinGoodsVOs) do
			local var_98_3 = iter_98_1:getSkinId()
			local var_98_4 = var_0_2[var_98_3].shop_type_id
			local var_98_5 = var_98_4 == 0 and 9999 or var_98_4
			local var_98_6 = iter_98_1:getConfig("genre") == ShopArgs.SkinShopTimeLimit
			local var_98_7 = arg_98_0.contextData.pageId

			if var_98_6 and var_98_7 == var_0_0.PAGE_TIME_LIMIT and var_98_2(var_98_3) or not var_98_6 and (var_98_7 == var_0_0.PAGE_ALL or var_98_5 == arg_98_0.contextData.pageId) or not var_98_6 and var_98_7 == var_0_0.PAGE_ENCORE and var_98_0(iter_98_1.id) then
				local var_98_8 = ShipSkin.New({
					id = var_98_3
				})

				if arg_98_0:MatchIndex(var_98_8) and var_98_8:IsMatchKey(getInputText(arg_98_0.inptuTr)) then
					table.insert(arg_98_0.displays, iter_98_1)
				end
			end
		end

		local function var_98_9(arg_101_0, arg_101_1)
			local var_101_0 = (arg_101_0.type == Goods.TYPE_ACTIVITY or arg_101_0.type == Goods.TYPE_ACTIVITY_EXTRA) and 0 or arg_101_0:GetPrice()
			local var_101_1 = (arg_101_1.type == Goods.TYPE_ACTIVITY or arg_101_1.type == Goods.TYPE_ACTIVITY_EXTRA) and 0 or arg_101_1:GetPrice()

			if var_101_0 == var_101_1 then
				return arg_101_0.id < arg_101_1.id
			else
				return var_101_1 < var_101_0
			end
		end

		table.sort(arg_98_0.displays, function(arg_102_0, arg_102_1)
			local var_102_0 = arg_102_0.buyCount == 0 and 1 or 0
			local var_102_1 = arg_102_1.buyCount == 0 and 1 or 0

			if var_102_0 == var_102_1 then
				local var_102_2 = arg_102_0:getConfig("order")
				local var_102_3 = arg_102_1:getConfig("order")

				if var_102_2 == var_102_3 then
					return var_98_9(arg_102_0, arg_102_1)
				else
					return var_102_2 < var_102_3
				end
			else
				return var_102_1 < var_102_0
			end
		end)

		if arg_98_1 then
			arg_98_0.shipRect:SetTotalCount(#arg_98_0.displays, arg_98_1)
		else
			arg_98_0.shipRect:SetTotalCount(#arg_98_0.displays)
		end

		arg_98_0:OnSkinListUpdate(#arg_98_0.displays)
	end
end

function var_0_0.ToVShip(arg_103_0, arg_103_1)
	if not arg_103_0.vship then
		arg_103_0.vship = {}

		function arg_103_0.vship.getNation()
			return arg_103_0.vship.config.nationality
		end

		function arg_103_0.vship.getShipType()
			return arg_103_0.vship.config.type
		end

		function arg_103_0.vship.getTeamType()
			return TeamType.GetTeamFromShipType(arg_103_0.vship.config.type)
		end

		function arg_103_0.vship.getRarity()
			return arg_103_0.vship.config.rarity
		end
	end

	arg_103_0.vship.config = arg_103_1

	return arg_103_0.vship
end

function var_0_0.MatchIndex(arg_108_0, arg_108_1)
	local var_108_0 = arg_108_1:GetDefaultShipConfig()

	if not var_108_0 then
		return false
	end

	local var_108_1 = arg_108_0:ToVShip(var_108_0)
	local var_108_2 = ShipIndexConst.filterByType(var_108_1, arg_108_0.defaultIndex.typeIndex)
	local var_108_3 = ShipIndexConst.filterByCamp(var_108_1, arg_108_0.defaultIndex.campIndex)
	local var_108_4 = ShipIndexConst.filterByRarity(var_108_1, arg_108_0.defaultIndex.rarityIndex)
	local var_108_5 = SkinIndexLayer.filterByExtra(arg_108_1, arg_108_0.defaultIndex.extraIndex)

	return var_108_2 and var_108_3 and var_108_4 and var_108_5
end

function var_0_0.addVerticalDrag(arg_109_0, arg_109_1, arg_109_2, arg_109_3)
	local var_109_0 = GetOrAddComponent(arg_109_1, "EventTriggerListener")
	local var_109_1 = 90
	local var_109_2
	local var_109_3 = 0
	local var_109_4 = 0
	local var_109_5 = 0

	var_109_0:AddBeginDragFunc(function(arg_110_0, arg_110_1)
		var_109_3 = 0
		var_109_4 = 0
		var_109_2 = arg_110_1.position
		var_109_5 = var_109_2.y
	end)
	var_109_0:AddDragFunc(function(arg_111_0, arg_111_1)
		if var_109_5 > arg_111_1.position.y and var_109_4 ~= 0 then
			var_109_2 = arg_111_1.position
			var_109_4 = 0
		elseif var_109_5 < arg_111_1.position.y and var_109_3 ~= 0 then
			var_109_2 = arg_111_1.position
			var_109_3 = 0
		end

		local var_111_0 = arg_111_1.position.y - var_109_2.y
		local var_111_1 = math.abs(math.floor(var_111_0 / var_109_1))

		if arg_109_2 and var_111_1 > var_109_3 then
			var_109_3 = var_111_1

			arg_109_2(var_111_0)
		end

		if arg_109_2 and var_111_1 < var_109_4 then
			var_109_4 = var_111_1

			arg_109_2(var_111_0)
		end

		var_109_5 = var_109_2.y
	end)
	var_109_0:AddDragEndFunc(function(arg_112_0, arg_112_1)
		if arg_109_3 then
			arg_109_3()
		end
	end)
end

function var_0_0.willExit(arg_113_0)
	for iter_113_0, iter_113_1 in ipairs(arg_113_0.cards) do
		iter_113_1:Dispose()
	end

	arg_113_0.cards = nil

	ClearEventTrigger(GetOrAddComponent(arg_113_0._tf, "EventTriggerListener"))
	ClearLScrollrect(arg_113_0.shipRect)

	arg_113_0.shipRect = nil

	arg_113_0:UnloadSpine()
	arg_113_0:UnLoadLive2d()
	arg_113_0:recycleChar()
	arg_113_0:recyclePainting()
	arg_113_0:removeShopTimer()

	for iter_113_2, iter_113_3 in pairs(arg_113_0.downloads) do
		iter_113_3:Dispose()
	end

	arg_113_0.downloads = {}

	LeanTween.cancel(go(arg_113_0.furnBg))
	LeanTween.cancel(go(arg_113_0.charBg))
	LeanTween.cancel(go(arg_113_0.bg1))
	LeanTween.cancel(go(arg_113_0.bg2))

	Input.multiTouchEnabled = true

	arg_113_0.interactionPreview:Dispose()

	arg_113_0.interactionPreview = nil

	if arg_113_0.skinTimer then
		arg_113_0.skinTimer:Stop()
	end

	arg_113_0.skinTimer = nil
	arg_113_0.contextData.key = nil
	arg_113_0.switchCnt = nil
	arg_113_0.contextData.skinId = nil
end

return var_0_0
