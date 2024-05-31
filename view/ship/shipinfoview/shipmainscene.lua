local var_0_0 = class("ShipMainScene", import("...base.BaseUI"))
local var_0_1 = 0
local var_0_2 = 0.2
local var_0_3 = 0.3
local var_0_4 = 3
local var_0_5 = 0.5
local var_0_6 = 11

function var_0_0.getUIName(arg_1_0)
	return "ShipMainScene"
end

function var_0_0.ResUISettings(arg_2_0)
	return {
		anim = true,
		showType = PlayerResUI.TYPE_ALL,
		groupName = LayerWeightConst.GROUP_SHIPINFOUI
	}
end

function var_0_0.preload(arg_3_0, arg_3_1)
	local var_3_0 = getProxy(BayProxy):getShipById(arg_3_0.contextData.shipId)

	parallelAsync({
		function(arg_4_0)
			GetSpriteFromAtlasAsync("bg/star_level_bg_" .. var_3_0:rarity2bgPrintForGet(), "", arg_4_0)
		end,
		function(arg_5_0)
			if arg_3_0.exited then
				return
			end

			local var_5_0 = PoolMgr.GetInstance()
			local var_5_1 = "ShipDetailView"

			if not var_5_0:HasCacheUI(var_5_1) then
				var_5_0:GetUI(var_5_1, true, function(arg_6_0)
					var_5_0:ReturnUI(var_5_1, arg_6_0)
					arg_5_0()
				end)
			else
				arg_5_0()
			end
		end
	}, arg_3_1)
end

function var_0_0.setPlayer(arg_7_0, arg_7_1)
	arg_7_0.player = arg_7_1

	arg_7_0:GetShareData():SetPlayer(arg_7_1)
end

function var_0_0.setShipList(arg_8_0, arg_8_1)
	arg_8_0.shipList = arg_8_1
end

function var_0_0.setShip(arg_9_0, arg_9_1)
	arg_9_0:GetShareData():SetShipVO(arg_9_1)

	local var_9_0 = false

	if arg_9_0.shipVO and arg_9_0.shipVO.id ~= arg_9_1.id then
		arg_9_0:StopPreVoice()

		var_9_0 = true
	end

	arg_9_0.shipVO = arg_9_1

	setActive(arg_9_0.npcFlagTF, arg_9_1:isActivityNpc())

	if var_9_0 and not arg_9_0:checkToggleActive(ShipViewConst.currentPage) then
		triggerToggle(arg_9_0.detailToggle, true)
	end

	arg_9_0:setToggleEnable()

	local var_9_1 = pg.ship_skin_template[arg_9_0.shipVO.skinId]

	arg_9_0.isSpBg = var_9_1.rarity_bg and var_9_1.rarity_bg ~= ""

	arg_9_0:updatePreference(arg_9_1)
	arg_9_0.shipDetailView:ActionInvoke("UpdateUI")
	arg_9_0.shipFashionView:ActionInvoke("UpdateUI")
	arg_9_0.shipEquipView:ActionInvoke("UpdateUI")
end

function var_0_0.equipmentChange(arg_10_0)
	if arg_10_0.shipDetailView then
		arg_10_0.shipDetailView:ActionInvoke("UpdateUI")
	end
end

function var_0_0.setToggleEnable(arg_11_0)
	for iter_11_0, iter_11_1 in pairs(arg_11_0.togglesList) do
		setActive(iter_11_1, arg_11_0:checkToggleActive(iter_11_0))
	end

	setActive(arg_11_0.technologyToggle, arg_11_0.shipVO:isBluePrintShip())
	SetActive(arg_11_0.metaToggle, arg_11_0.shipVO:isMetaShip())
end

function var_0_0.checkToggleActive(arg_12_0, arg_12_1)
	if arg_12_1 == ShipViewConst.PAGE.DETAIL then
		return true
	elseif arg_12_1 == ShipViewConst.PAGE.EQUIPMENT then
		return true
	elseif arg_12_1 == ShipViewConst.PAGE.INTENSIFY then
		return not arg_12_0.shipVO:isTestShip() and not arg_12_0.shipVO:isBluePrintShip() and not arg_12_0.shipVO:isMetaShip()
	elseif arg_12_1 == ShipViewConst.PAGE.UPGRADE then
		return not arg_12_0.shipVO:isTestShip() and not arg_12_0.shipVO:isBluePrintShip() and not arg_12_0.shipVO:isMetaShip()
	elseif arg_12_1 == ShipViewConst.PAGE.REMOULD then
		return not arg_12_0.shipVO:isTestShip() and not arg_12_0.shipVO:isBluePrintShip() and pg.ship_data_trans[arg_12_0.shipVO.groupId] and not arg_12_0.shipVO:isMetaShip()
	elseif arg_12_1 == ShipViewConst.PAGE.FASHION then
		if not arg_12_0:hasFashion() then
			return false
		else
			local var_12_0
			local var_12_1

			if not PaintingGroupConst.IsPaintingNeedCheck() then
				var_12_1 = false
			else
				local var_12_2 = PaintingGroupConst.GetPaintingNameListByShipVO(arg_12_0.shipVO)

				var_12_1 = PaintingGroupConst.CalcPaintingListSize(var_12_2) > 0
			end

			return not var_12_1
		end
	else
		return false
	end
end

function var_0_0.setSkinList(arg_13_0, arg_13_1)
	arg_13_0.shipFashionView:ActionInvoke("SetSkinList", arg_13_1)
end

function var_0_0.updateLock(arg_14_0)
	arg_14_0.shipDetailView:ActionInvoke("UpdateLock")
end

function var_0_0.updatePreferenceTag(arg_15_0)
	arg_15_0.shipDetailView:ActionInvoke("UpdatePreferenceTag")
end

function var_0_0.updateFashionTag(arg_16_0)
	arg_16_0.shipDetailView:ActionInvoke("UpdateFashionTag")
end

function var_0_0.closeRecordPanel(arg_17_0)
	arg_17_0.shipDetailView:ActionInvoke("CloseRecordPanel")
end

function var_0_0.updateRecordEquipments(arg_18_0, arg_18_1)
	arg_18_0.shipDetailView:UpdateRecordEquipments(arg_18_1)
	arg_18_0.shipDetailView:UpdateRecordSpWeapons(arg_18_1)
end

function var_0_0.setModPanel(arg_19_0, arg_19_1)
	arg_19_0.modPanel = arg_19_1
end

function var_0_0.setMaxLevelHelpFlag(arg_20_0, arg_20_1)
	arg_20_0.maxLevelHelpFlag = arg_20_1
end

function var_0_0.checkMaxLevelHelp(arg_21_0)
	if not arg_21_0.maxLevelHelpFlag and arg_21_0.shipVO and arg_21_0.shipVO:isReachNextMaxLevel() then
		arg_21_0:openHelpPage()

		arg_21_0.maxLevelHelpFlag = true

		getProxy(SettingsProxy):setMaxLevelHelp(true)
	end
end

function var_0_0.GetShareData(arg_22_0)
	if not arg_22_0.shareData then
		arg_22_0.shareData = ShipViewShareData.New(arg_22_0.contextData)

		arg_22_0.shipDetailView:SetShareData(arg_22_0.shareData)
		arg_22_0.shipFashionView:SetShareData(arg_22_0.shareData)
		arg_22_0.shipEquipView:SetShareData(arg_22_0.shareData)
		arg_22_0.shipEquipView:ActionInvoke("InitEvent")
		arg_22_0.shipHuntingRangeView:SetShareData(arg_22_0.shareData)
		arg_22_0.shipCustomMsgBox:SetShareData(arg_22_0.shareData)
		arg_22_0.shipChangeNameView:SetShareData(arg_22_0.shareData)
	end

	return arg_22_0.shareData
end

function var_0_0.hasFashion(arg_23_0)
	return arg_23_0.shareData:HasFashion()
end

function var_0_0.DisplayRenamePanel(arg_24_0, arg_24_1)
	arg_24_0.shipChangeNameView:Load()
	arg_24_0.shipChangeNameView:ActionInvoke("DisplayRenamePanel", arg_24_1)
end

function var_0_0.init(arg_25_0)
	arg_25_0:initShip()
	arg_25_0:initPages()
	arg_25_0:initEvents()

	arg_25_0.mainCanvasGroup = arg_25_0._tf:GetComponent(typeof(CanvasGroup))
	arg_25_0.commonCanvasGroup = arg_25_0:findTF("blur_panel/adapt"):GetComponent(typeof(CanvasGroup))
	Input.multiTouchEnabled = false
end

function var_0_0.initShip(arg_26_0)
	arg_26_0.shipInfo = arg_26_0:findTF("main/character")

	setActive(arg_26_0.shipInfo, true)

	arg_26_0.tablePainting = {
		arg_26_0:findTF("painting", arg_26_0.shipInfo),
		arg_26_0:findTF("painting2", arg_26_0.shipInfo)
	}
	arg_26_0.nowPainting = nil
	arg_26_0.isRight = true
	arg_26_0.blurPanel = arg_26_0:findTF("blur_panel")
	arg_26_0.common = arg_26_0.blurPanel:Find("adapt")
	arg_26_0.npcFlagTF = arg_26_0.common:Find("name/npc")
	arg_26_0.shipName = arg_26_0.common:Find("name")
	arg_26_0.shipInfoStarTpl = arg_26_0.shipName:Find("star_tpl")
	arg_26_0.nameEditFlag = arg_26_0.shipName:Find("nameRect/editFlag")

	setActive(arg_26_0.shipName, true)
	setActive(arg_26_0.shipInfoStarTpl, false)
	setActive(arg_26_0.nameEditFlag, false)

	arg_26_0.energyTF = arg_26_0.shipName:Find("energy")
	arg_26_0.energyDescTF = arg_26_0.energyTF:Find("desc")
	arg_26_0.energyText = arg_26_0.energyTF:Find("desc/desc")

	setActive(arg_26_0.energyDescTF, false)

	arg_26_0.character = arg_26_0:findTF("main/character")
	arg_26_0.chat = arg_26_0:findTF("main/character/chat")
	arg_26_0.chatBg = arg_26_0:findTF("main/character/chat/chatbgtop")
	arg_26_0.chatText = arg_26_0:findTF("Text", arg_26_0.chat)
	rtf(arg_26_0.chat).localScale = Vector3.New(0, 0, 1)
	arg_26_0.initChatBgH = arg_26_0.chatText.sizeDelta.y
	arg_26_0.initfontSize = arg_26_0.chatText:GetComponent(typeof(Text)).fontSize
	arg_26_0.initChatTextH = arg_26_0.chatText.sizeDelta.y
	arg_26_0.initfontSize = arg_26_0.chatText:GetComponent(typeof(Text)).fontSize

	if PLATFORM_CODE == PLATFORM_US then
		local var_26_0 = GetComponent(arg_26_0.chatText, typeof(Text))

		var_26_0.lineSpacing = 1.1
		var_26_0.fontSize = 25
	end

	pg.UIMgr.GetInstance():OverlayPanel(arg_26_0.chat, {
		groupName = LayerWeightConst.GROUP_SHIPINFOUI
	})
end

function var_0_0.initPages(arg_27_0)
	ShipViewConst.currentPage = nil
	arg_27_0.background = arg_27_0:findTF("background")

	setActive(arg_27_0.background, true)

	arg_27_0.main = arg_27_0:findTF("main")
	arg_27_0.mainMask = arg_27_0.main:GetComponent(typeof(RectMask2D))
	arg_27_0.toggles = arg_27_0:findTF("left_length/frame/root", arg_27_0.common)
	arg_27_0.detailToggle = arg_27_0.toggles:Find("detail_toggle")
	arg_27_0.equipmentToggle = arg_27_0.toggles:Find("equpiment_toggle")
	arg_27_0.intensifyToggle = arg_27_0.toggles:Find("intensify_toggle")
	arg_27_0.upgradeToggle = arg_27_0.toggles:Find("upgrade_toggle")
	arg_27_0.remouldToggle = arg_27_0.toggles:Find("remould_toggle")
	arg_27_0.technologyToggle = arg_27_0.toggles:Find("technology_toggle")
	arg_27_0.metaToggle = arg_27_0.toggles:Find("meta_toggle")
	arg_27_0.togglesList = {}
	arg_27_0.togglesList[ShipViewConst.PAGE.DETAIL] = arg_27_0.detailToggle
	arg_27_0.togglesList[ShipViewConst.PAGE.EQUIPMENT] = arg_27_0.equipmentToggle
	arg_27_0.togglesList[ShipViewConst.PAGE.INTENSIFY] = arg_27_0.intensifyToggle
	arg_27_0.togglesList[ShipViewConst.PAGE.UPGRADE] = arg_27_0.upgradeToggle
	arg_27_0.togglesList[ShipViewConst.PAGE.REMOULD] = arg_27_0.remouldToggle
	arg_27_0.detailContainer = arg_27_0.main:Find("detail_container")

	setAnchoredPosition(arg_27_0.detailContainer, {
		x = 1300
	})

	arg_27_0.fashionContainer = arg_27_0.main:Find("fashion_container")

	setAnchoredPosition(arg_27_0.fashionContainer, {
		x = 900
	})

	arg_27_0.equipContainer = arg_27_0.main:Find("equip_container")
	arg_27_0.equipLCon = arg_27_0.equipContainer:Find("equipment_l_container")
	arg_27_0.equipRCon = arg_27_0.equipContainer:Find("equipment_r_container")
	arg_27_0.equipBCon = arg_27_0.equipContainer:Find("equipment_b_container")

	setAnchoredPosition(arg_27_0.equipRCon, {
		x = 750
	})
	setAnchoredPosition(arg_27_0.equipLCon, {
		x = -700
	})
	setAnchoredPosition(arg_27_0.equipBCon, {
		y = -540
	})

	arg_27_0.shipDetailView = ShipDetailView.New(arg_27_0.detailContainer, arg_27_0.event, arg_27_0.contextData)
	arg_27_0.shipFashionView = ShipFashionView.New(arg_27_0.fashionContainer, arg_27_0.event, arg_27_0.contextData)
	arg_27_0.shipEquipView = ShipEquipView.New(arg_27_0.equipContainer, arg_27_0.event, arg_27_0.contextData)
	arg_27_0.shipHuntingRangeView = ShipHuntingRangeView.New(arg_27_0._tf, arg_27_0.event, arg_27_0.contextData)
	arg_27_0.shipCustomMsgBox = ShipCustomMsgBox.New(arg_27_0._tf, arg_27_0.event, arg_27_0.contextData)
	arg_27_0.shipChangeNameView = ShipChangeNameView.New(arg_27_0._tf, arg_27_0.event, arg_27_0.contextData)
	arg_27_0.expItemUsagePage = ShipExpItemUsagePage.New(arg_27_0._tf, arg_27_0.event, arg_27_0.contextData)
	arg_27_0.viewList = {}
	arg_27_0.viewList[ShipViewConst.PAGE.DETAIL] = arg_27_0.shipDetailView
	arg_27_0.viewList[ShipViewConst.PAGE.FASHION] = arg_27_0.shipFashionView
	arg_27_0.viewList[ShipViewConst.PAGE.EQUIPMENT] = arg_27_0.shipEquipView

	onButton(arg_27_0, arg_27_0.shipName, function()
		if arg_27_0.shipVO.propose and not arg_27_0.shipVO:IsXIdol() then
			if not pg.PushNotificationMgr.GetInstance():isEnableShipName() then
				pg.TipsMgr.GetInstance():ShowTips(i18n("word_rename_switch_tip"))

				return
			end

			local var_28_0 = arg_27_0.shipVO.renameTime + 2592000 - pg.TimeMgr.GetInstance():GetServerTime()

			if var_28_0 > 0 then
				local var_28_1 = math.floor(var_28_0 / 60 / 60 / 24)

				if var_28_1 < 1 then
					var_28_1 = 1
				end

				pg.TipsMgr.GetInstance():ShowTips(i18n("word_rename_time_tip", var_28_1))
			else
				arg_27_0:DisplayRenamePanel(true)
			end
		end
	end, SFX_PANEL)
end

function var_0_0.initEvents(arg_29_0)
	arg_29_0:bind(ShipViewConst.SWITCH_TO_PAGE, function(arg_30_0, arg_30_1)
		arg_29_0:gotoPage(arg_30_1)
	end)
	arg_29_0:bind(ShipViewConst.LOAD_PAINTING, function(arg_31_0, arg_31_1, arg_31_2)
		arg_29_0:loadPainting(arg_31_1, arg_31_2)
	end)
	arg_29_0:bind(ShipViewConst.LOAD_PAINTING_BG, function(arg_32_0, arg_32_1, arg_32_2, arg_32_3)
		arg_29_0:loadSkinBg(arg_32_1, arg_32_2, arg_32_3, arg_29_0.isSpBg)
	end)
	arg_29_0:bind(ShipViewConst.HIDE_SHIP_WORD, function(arg_33_0)
		arg_29_0:hideShipWord()
	end)
	arg_29_0:bind(ShipViewConst.SET_CLICK_ENABLE, function(arg_34_0, arg_34_1)
		arg_29_0.mainCanvasGroup.blocksRaycasts = arg_34_1
		arg_29_0.commonCanvasGroup.blocksRaycasts = arg_34_1
		GetComponent(arg_29_0.detailContainer, "CanvasGroup").blocksRaycasts = arg_34_1
	end)
	arg_29_0:bind(ShipViewConst.SHOW_CUSTOM_MSG, function(arg_35_0, arg_35_1)
		arg_29_0.shipCustomMsgBox:Load()
		arg_29_0.shipCustomMsgBox:ActionInvoke("showCustomMsgBox", arg_35_1)
	end)
	arg_29_0:bind(ShipViewConst.HIDE_CUSTOM_MSG, function(arg_36_0)
		arg_29_0.shipCustomMsgBox:ActionInvoke("hideCustomMsgBox")
	end)
	arg_29_0:bind(ShipViewConst.DISPLAY_HUNTING_RANGE, function(arg_37_0, arg_37_1)
		if arg_37_1 then
			arg_29_0.shipHuntingRangeView:Load()
			arg_29_0.shipHuntingRangeView:ActionInvoke("DisplayHuntingRange")
		else
			arg_29_0.shipHuntingRangeView:HideHuntingRange()
		end
	end)
	arg_29_0:bind(ShipViewConst.PAINT_VIEW, function(arg_38_0, arg_38_1)
		if arg_38_1 then
			arg_29_0:paintView()
		else
			arg_29_0:hidePaintView(true)
		end
	end)
	arg_29_0:bind(ShipViewConst.SHOW_EXP_ITEM_USAGE, function(arg_39_0, arg_39_1)
		arg_29_0.expItemUsagePage:ExecuteAction("Show", arg_39_1)
	end)
end

function var_0_0.didEnter(arg_40_0)
	arg_40_0:addRingDragListenter()
	onButton(arg_40_0, arg_40_0:findTF("top/back_btn", arg_40_0.common), function()
		GetOrAddComponent(arg_40_0._tf, typeof(CanvasGroup)).interactable = false

		if not arg_40_0.everTriggerBack then
			LeanTween.delayedCall(0.3, System.Action(function()
				arg_40_0:closeView()
			end))

			arg_40_0.everTriggerBack = true
		end
	end, SFX_CANCEL)
	onButton(arg_40_0, arg_40_0.npcFlagTF, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_shipinfo_actnpc.tip
		})
	end, SFX_PANEL)

	arg_40_0.helpBtn = arg_40_0:findTF("help_btn", arg_40_0.common)

	onButton(arg_40_0, arg_40_0.helpBtn, function()
		arg_40_0:openHelpPage(ShipViewConst.currentPage)
	end, SFX_PANEL)

	for iter_40_0, iter_40_1 in pairs(arg_40_0.togglesList) do
		if iter_40_1 == arg_40_0.upgradeToggle or iter_40_1 == arg_40_0.remouldToggle or iter_40_1 == arg_40_0.equipmentToggle then
			onToggle(arg_40_0, iter_40_1, function(arg_45_0)
				if arg_45_0 then
					if LeanTween.isTweening(go(arg_40_0.chat)) then
						LeanTween.cancel(go(arg_40_0.chat))
					end

					rtf(arg_40_0.chat).localScale = Vector3.New(0, 0, 1)
					arg_40_0.chatFlag = false

					arg_40_0:switchToPage(iter_40_0)
				end
			end, SFX_PANEL)
		else
			onToggle(arg_40_0, iter_40_1, function(arg_46_0)
				if arg_46_0 then
					arg_40_0:switchToPage(iter_40_0)
				end
			end, SFX_PANEL)
		end
	end

	onButton(arg_40_0, arg_40_0.technologyToggle, function()
		arg_40_0:emit(ShipMainMediator.ON_TECHNOLOGY, arg_40_0.shipVO)
	end, SFX_PANEL)
	onButton(arg_40_0, arg_40_0.metaToggle, function()
		arg_40_0:emit(ShipMainMediator.ON_META, arg_40_0.shipVO)
	end, SFX_PANEL)
	onButton(arg_40_0, tf(arg_40_0.character), function()
		if ShipViewConst.currentPage ~= ShipViewConst.PAGE.FASHION then
			arg_40_0:displayShipWord("detail")
		end
	end)
	onButton(arg_40_0, arg_40_0.energyTF, function()
		arg_40_0:showEnergyDesc()
	end)
	pg.UIMgr.GetInstance():OverlayPanel(arg_40_0.blurPanel, {
		groupName = LayerWeightConst.GROUP_SHIPINFOUI
	})

	local var_40_0 = arg_40_0:checkToggleActive(arg_40_0.contextData.page) and arg_40_0.contextData.page or ShipViewConst.PAGE.DETAIL

	arg_40_0:gotoPage(var_40_0)

	if ShipViewConst.currentPage == ShipViewConst.PAGE.DETAIL then
		arg_40_0:displayShipWord(arg_40_0:getInitmacyWords())
		arg_40_0:checkMaxLevelHelp()
	end
end

function var_0_0.openHelpPage(arg_51_0, arg_51_1)
	if arg_51_1 == ShipViewConst.PAGE.EQUIPMENT then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_shipinfo_equip.tip,
			weight = LayerWeightConst.THIRD_LAYER
		})
	elseif arg_51_1 == ShipViewConst.PAGE.DETAIL then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_shipinfo_detail.tip,
			weight = LayerWeightConst.THIRD_LAYER
		})
	elseif arg_51_1 == ShipViewConst.PAGE.INTENSIFY then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_shipinfo_intensify.tip,
			weight = LayerWeightConst.THIRD_LAYER
		})
	elseif arg_51_1 == ShipViewConst.PAGE.UPGRADE then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_shipinfo_upgrate.tip,
			weight = LayerWeightConst.THIRD_LAYER
		})
	elseif arg_51_1 == ShipViewConst.PAGE.FASHION then
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_shipinfo_fashion.tip,
			weight = LayerWeightConst.THIRD_LAYER
		})
	else
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.help_shipinfo_maxlevel.tip,
			weight = LayerWeightConst.THIRD_LAYER
		})
	end
end

function var_0_0.showAwakenCompleteAni(arg_52_0, arg_52_1)
	local function var_52_0()
		arg_52_0.awakenAni:SetActive(true)

		arg_52_0.awakenPlay = true

		onButton(arg_52_0, arg_52_0.awakenAni, function()
			arg_52_0.awakenAni:GetComponent("Animator"):SetBool("endFlag", true)
		end)

		local var_53_0 = tf(arg_52_0.awakenAni)

		pg.UIMgr.GetInstance():BlurPanel(var_53_0, false, {
			weight = LayerWeightConst.TOP_LAYER
		})
		setText(arg_52_0:findTF("window/desc", arg_52_0.awakenAni), arg_52_1)
		var_53_0:GetComponent("DftAniEvent"):SetEndEvent(function(arg_55_0)
			arg_52_0.awakenAni:GetComponent("Animator"):SetBool("endFlag", false)
			pg.UIMgr.GetInstance():UnblurPanel(var_53_0, arg_52_0.common)
			arg_52_0.awakenAni:SetActive(false)

			arg_52_0.awakenPlay = false
		end)
	end

	local var_52_1 = arg_52_0:findTF("AwakenCompleteWindows(Clone)")

	if var_52_1 then
		arg_52_0.awakenAni = go(var_52_1)
	end

	if not arg_52_0.awakenAni then
		PoolMgr.GetInstance():GetUI("AwakenCompleteWindows", true, function(arg_56_0)
			arg_56_0:SetActive(true)

			arg_52_0.awakenAni = arg_56_0

			var_52_0()
		end)
	else
		var_52_0()
	end
end

function var_0_0.updatePreference(arg_57_0, arg_57_1)
	local var_57_0 = arg_57_1:getConfigTable()
	local var_57_1 = arg_57_0.shipVO:getName()

	setScrollText(arg_57_0.shipName:Find("nameRect/name_mask/Text"), var_57_1)
	setText(arg_57_0:findTF("english_name", arg_57_0.shipName), var_57_0.english_name)
	setActive(arg_57_0.nameEditFlag, arg_57_1.propose and not arg_57_1:IsXIdol())

	local var_57_2 = GetSpriteFromAtlas("energy", arg_57_1:getEnergyPrint())

	if not var_57_2 then
		warning("找不到疲劳")
	end

	setImageSprite(arg_57_0.energyTF, var_57_2, true)
	setActive(arg_57_0.energyTF, true)

	local var_57_3 = arg_57_0:findTF("stars", arg_57_0.shipName)

	removeAllChildren(var_57_3)

	local var_57_4 = arg_57_1:getStar()
	local var_57_5 = arg_57_1:getMaxStar()

	for iter_57_0 = 1, var_57_5 do
		local var_57_6 = cloneTplTo(arg_57_0.shipInfoStarTpl, var_57_3, "star_" .. iter_57_0)

		setActive(var_57_6:Find("star_tpl"), iter_57_0 <= var_57_4)
		setActive(var_57_6:Find("empty_star_tpl"), true)
	end

	if ShipViewConst.currentPage ~= ShipViewConst.PAGE.FASHION then
		arg_57_0:loadPainting(arg_57_0.shipVO:getPainting())
		arg_57_0:loadSkinBg(arg_57_0.shipVO:rarity2bgPrintForGet(), arg_57_0.shipVO:isBluePrintShip(), arg_57_0.shipVO:isMetaShip(), arg_57_0.isSpBg)
	end

	local var_57_7 = GetSpriteFromAtlas("shiptype", arg_57_1:getShipType())

	if not var_57_7 then
		warning("找不到船形, shipConfigId: " .. arg_57_1.configId)
	end

	setImageSprite(arg_57_0:findTF("type", arg_57_0.shipName), var_57_7, true)
end

function var_0_0.doUpgradeMaxLeveAnim(arg_58_0, arg_58_1, arg_58_2, arg_58_3)
	arg_58_0.inUpgradeAnim = true

	arg_58_0.shipDetailView:DoLeveUpAnim(arg_58_1, arg_58_2, function()
		if arg_58_3 then
			arg_58_3()
		end

		arg_58_0.inUpgradeAnim = nil
	end)
end

function var_0_0.addRingDragListenter(arg_60_0)
	local var_60_0 = GetOrAddComponent(arg_60_0._tf, "EventTriggerListener")
	local var_60_1
	local var_60_2 = 0
	local var_60_3

	var_60_0:AddBeginDragFunc(function()
		var_60_2 = 0
		var_60_1 = nil
	end)
	var_60_0:AddDragFunc(function(arg_62_0, arg_62_1)
		if not arg_60_0.inPaintingView then
			local var_62_0 = arg_62_1.position

			if not var_60_1 then
				var_60_1 = var_62_0
			end

			var_60_2 = var_62_0.x - var_60_1.x
		end
	end)
	var_60_0:AddDragEndFunc(function(arg_63_0, arg_63_1)
		if not arg_60_0.inPaintingView then
			if var_60_2 < -50 then
				if not arg_60_0.isLoading then
					arg_60_0:emit(ShipMainMediator.NEXTSHIP, -1)
				end
			elseif var_60_2 > 50 and not arg_60_0.isLoading then
				arg_60_0:emit(ShipMainMediator.NEXTSHIP)
			end
		end
	end)
end

function var_0_0.showEnergyDesc(arg_64_0)
	if arg_64_0.energyTimer then
		return
	end

	setActive(arg_64_0.energyDescTF, true)

	local var_64_0, var_64_1 = arg_64_0.shipVO:getEnergyPrint()

	setText(arg_64_0.energyText, i18n(var_64_1))

	arg_64_0.energyTimer = Timer.New(function()
		setActive(arg_64_0.energyDescTF, false)
		arg_64_0.energyTimer:Stop()

		arg_64_0.energyTimer = nil
	end, 2, 1)

	arg_64_0.energyTimer:Start()
end

function var_0_0.displayShipWord(arg_66_0, arg_66_1, arg_66_2)
	if ShipViewConst.currentPage == ShipViewConst.PAGE.EQUIPMENT or ShipViewConst.currentPage == ShipViewConst.PAGE.UPGRADE then
		rtf(arg_66_0.chat).localScale = Vector3.New(0, 0, 1)

		return
	end

	if arg_66_2 or not arg_66_0.chatFlag then
		arg_66_0.chatFlag = true
		arg_66_0.chat.localScale = Vector3.zero

		setActive(arg_66_0.chat, true)

		arg_66_0.chat.localPosition = Vector3(arg_66_0.character.localPosition.x + 100, arg_66_0.chat.localPosition.y, 0)

		local var_66_0 = arg_66_0.shipVO:getCVIntimacy()

		arg_66_0.chat:SetAsLastSibling()

		local var_66_1 = arg_66_0.chatText:GetComponent(typeof(Text))

		if findTF(arg_66_0.nowPainting, "fitter").childCount > 0 then
			ShipExpressionHelper.SetExpression(findTF(arg_66_0.nowPainting, "fitter"):GetChild(0), arg_66_0.paintingCode, arg_66_1, var_66_0)
		end

		local var_66_2, var_66_3, var_66_4 = ShipWordHelper.GetWordAndCV(arg_66_0.shipVO.skinId, arg_66_1, nil, nil, var_66_0)
		local var_66_5 = arg_66_0.chatText:GetComponent(typeof(Text))

		if PLATFORM_CODE ~= PLATFORM_US then
			setText(arg_66_0.chatText, SwitchSpecialChar(var_66_4))
		else
			var_66_5.fontSize = arg_66_0.initfontSize

			setTextEN(arg_66_0.chatText, var_66_4)

			while var_66_5.preferredHeight > arg_66_0.initChatTextH do
				var_66_5.fontSize = var_66_5.fontSize - 2

				setTextEN(arg_66_0.chatText, var_66_4)

				if var_66_5.fontSize < 20 then
					break
				end
			end
		end

		if #var_66_5.text > CHAT_POP_STR_LEN then
			var_66_5.alignment = TextAnchor.MiddleLeft
		else
			var_66_5.alignment = TextAnchor.MiddleCenter
		end

		local var_66_6 = var_66_5.preferredHeight + 120

		if var_66_6 > arg_66_0.initChatBgH then
			arg_66_0.chatBg.sizeDelta = Vector2.New(arg_66_0.chatBg.sizeDelta.x, var_66_6)
		else
			arg_66_0.chatBg.sizeDelta = Vector2.New(arg_66_0.chatBg.sizeDelta.x, arg_66_0.initChatBgH)
		end

		local var_66_7 = var_0_4

		local function var_66_8()
			if arg_66_0.chatFlag then
				if arg_66_0.chatani1Id then
					LeanTween.cancel(arg_66_0.chatani1Id)
				end

				if arg_66_0.chatani2Id then
					LeanTween.cancel(arg_66_0.chatani2Id)
				end
			end

			arg_66_0.chatani1Id = LeanTween.scale(rtf(arg_66_0.chat.gameObject), Vector3.New(1, 1, 1), var_0_3):setEase(LeanTweenType.easeOutBack):setOnComplete(System.Action(function()
				arg_66_0.chatani2Id = LeanTween.scale(rtf(arg_66_0.chat.gameObject), Vector3.New(0, 0, 1), var_0_3):setEase(LeanTweenType.easeInBack):setDelay(var_0_3 + var_66_7):setOnComplete(System.Action(function()
					arg_66_0.chatFlag = nil
				end)).uniqueId
			end)).uniqueId
		end

		if var_66_3 then
			arg_66_0:StopPreVoice()
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(var_66_3, function(arg_70_0)
				if arg_70_0 then
					var_66_7 = arg_70_0:GetLength() * 0.001
				end

				var_66_8()
			end)

			arg_66_0.preVoiceContent = var_66_3
		else
			var_66_8()
		end
	end
end

function var_0_0.StopPreVoice(arg_71_0)
	if arg_71_0.preVoiceContent ~= nil then
		pg.CriMgr.GetInstance():UnloadSoundEffect_V3(arg_71_0.preVoiceContent)
	end
end

function var_0_0.startChatTimer(arg_72_0)
	if arg_72_0.chatFlag then
		return
	end

	if arg_72_0.chatTimer then
		arg_72_0.chatTimer:Stop()

		arg_72_0.chatTimer = nil
	end

	arg_72_0.chatTimer = Timer.New(function()
		arg_72_0:displayShipWord(arg_72_0:getInitmacyWords())
	end, var_0_6, 1)

	arg_72_0.chatTimer:Start()
end

function var_0_0.hideShipWord(arg_74_0)
	if arg_74_0.chatFlag then
		if arg_74_0.chatani1Id then
			LeanTween.cancel(arg_74_0.chatani1Id)
		end

		if arg_74_0.chatani2Id then
			LeanTween.cancel(arg_74_0.chatani2Id)
		end

		LeanTween.scale(rtf(arg_74_0.chat.gameObject), Vector3.New(0, 0, 1), var_0_3):setEase(LeanTweenType.easeInBack):setOnComplete(System.Action(function()
			arg_74_0.chatFlag = nil
		end))
	end

	arg_74_0:StopPreVoice()
end

function var_0_0.gotoPage(arg_76_0, arg_76_1)
	if arg_76_1 == ShipViewConst.PAGE.FASHION then
		local function var_76_0()
			arg_76_0:switchToPage(arg_76_1)
		end

		arg_76_0:checkPaintingRes(var_76_0)
	else
		triggerToggle(arg_76_0.togglesList[arg_76_1], true)
	end
end

function var_0_0.switchToPage(arg_78_0, arg_78_1, arg_78_2)
	local function var_78_0(arg_79_0, arg_79_1)
		setActive(arg_78_0.detailContainer, false)

		if arg_79_0 == ShipViewConst.PAGE.DETAIL then
			setActive(arg_78_0.detailContainer, arg_79_1)

			local var_79_0 = arg_79_1 and {
				arg_78_0.detailContainer.rect.width + 200,
				0
			} or {
				0,
				arg_78_0.detailContainer.rect.width + 200
			}

			shiftPanel(arg_78_0.detailContainer, var_79_0[2], 0, var_0_2, 0):setFrom(var_79_0[1])
		elseif arg_79_0 == ShipViewConst.PAGE.EQUIPMENT then
			local var_79_1 = {
				-(arg_78_0.equipLCon.rect.width + 190),
				190
			}
			local var_79_2 = {
				arg_78_0.equipRCon.rect.width,
				10
			}
			local var_79_3 = {
				-arg_78_0.equipBCon.rect.height,
				0
			}
			local var_79_4 = arg_79_1 and 1 or 2
			local var_79_5 = arg_79_1 and 2 or 1

			shiftPanel(arg_78_0.equipLCon, var_79_1[var_79_5], 0, var_0_2, 0):setFrom(var_79_1[var_79_4])
			shiftPanel(arg_78_0.equipRCon, var_79_2[var_79_5], 0, var_0_2, 0):setFrom(var_79_2[var_79_4])
			shiftPanel(arg_78_0.equipBCon, 0, var_79_3[var_79_5], var_0_2, 0):setFrom(var_79_3[var_79_4])
		elseif arg_79_0 == ShipViewConst.PAGE.FASHION then
			local var_79_6 = arg_79_1 and {
				arg_78_0.fashionContainer.rect.width + 150,
				0
			} or {
				0,
				arg_78_0.fashionContainer.rect.width + 150
			}

			shiftPanel(arg_78_0.fashionContainer, var_79_6[2], 0, var_0_2, 0):setFrom(var_79_6[1])

			if arg_79_1 then
				arg_78_0.shipFashionView:ActionInvoke("UpdateFashion")
			end
		elseif arg_79_0 == ShipViewConst.PAGE.INTENSIFY then
			if arg_79_1 then
				arg_78_0:emit(ShipMainMediator.OPEN_INTENSIFY)
			else
				arg_78_0:emit(ShipMainMediator.CLOSE_INTENSIFY)
			end
		elseif arg_79_0 == ShipViewConst.PAGE.UPGRADE then
			if arg_79_1 then
				arg_78_0:emit(ShipMainMediator.ON_UPGRADE)
			else
				arg_78_0:emit(ShipMainMediator.CLOSE_UPGRADE)
			end
		elseif arg_79_0 == ShipViewConst.PAGE.REMOULD then
			if arg_79_1 then
				arg_78_0:emit(ShipMainMediator.OPEN_REMOULD)
			else
				arg_78_0:emit(ShipMainMediator.CLOSE_REMOULD)
			end
		end

		arg_78_0:blurPage(arg_79_0, arg_79_1)

		if arg_79_0 ~= ShipViewConst.PAGE.FASHION then
			arg_78_0.fashionSkinId = arg_78_0.shipVO.skinId

			arg_78_0:loadPainting(arg_78_0.shipVO:getPainting())
		end

		local var_79_7 = not ShipViewConst.IsSubLayerPage(arg_79_0)
		local var_79_8 = arg_78_0.bgEffect[arg_78_0.shipVO:getRarity()]

		if var_79_8 then
			setActive(var_79_8, arg_79_0 ~= ShipViewConst.PAGE.REMOULD and arg_78_0.shipVO.bluePrintFlag and arg_78_0.shipVO.bluePrintFlag == 0)
		end

		setActive(arg_78_0.helpBtn, var_79_7)
	end

	function switchHandler()
		if arg_78_1 == ShipViewConst.currentPage and arg_78_2 then
			var_78_0(arg_78_1, true)
		elseif arg_78_1 ~= ShipViewConst.currentPage then
			if ShipViewConst.currentPage then
				var_78_0(ShipViewConst.currentPage, false)
			end

			ShipViewConst.currentPage = arg_78_1
			arg_78_0.contextData.page = arg_78_1

			var_78_0(arg_78_1, true)
			arg_78_0:switchPainting()
		end
	end

	if arg_78_0.viewList[arg_78_1] ~= nil then
		local var_78_1 = arg_78_0.viewList[arg_78_1]

		if not var_78_1:GetLoaded() then
			var_78_1:Load()
			var_78_1:CallbackInvoke(switchHandler)
		else
			switchHandler()
		end
	else
		switchHandler()
	end
end

function var_0_0.blurPage(arg_81_0, arg_81_1, arg_81_2)
	local var_81_0 = pg.UIMgr.GetInstance()

	if arg_81_1 == ShipViewConst.PAGE.DETAIL then
		arg_81_0.shipDetailView:ActionInvoke("OnSelected", arg_81_2)
	elseif arg_81_1 == ShipViewConst.PAGE.EQUIPMENT then
		arg_81_0.shipEquipView:ActionInvoke("OnSelected", arg_81_2)
	elseif arg_81_1 == ShipViewConst.PAGE.FASHION then
		arg_81_0.shipFashionView:ActionInvoke("OnSelected", arg_81_2)
	elseif arg_81_1 == ShipViewConst.PAGE.INTENSIFY then
		-- block empty
	elseif arg_81_1 == ShipViewConst.PAGE.UPGRADE then
		-- block empty
	elseif arg_81_1 == ShipViewConst.PAGE.REMOULD then
		-- block empty
	end
end

function var_0_0.switchPainting(arg_82_0)
	setActive(arg_82_0.shipInfo, not ShipViewConst.IsSubLayerPage(ShipViewConst.currentPage))
	setActive(arg_82_0.shipName, not ShipViewConst.IsSubLayerPage(ShipViewConst.currentPage))

	if ShipViewConst.currentPage == ShipViewConst.PAGE.EQUIPMENT then
		shiftPanel(arg_82_0.shipInfo, -20, 0, var_0_2, 0)

		arg_82_0.paintingFrameName = "zhuangbei"
	else
		shiftPanel(arg_82_0.shipInfo, -460, 0, var_0_2, 0)

		arg_82_0.paintingFrameName = "chuanwu"
	end

	local var_82_0 = GetOrAddComponent(findTF(arg_82_0.nowPainting, "fitter"), "PaintingScaler")

	var_82_0:Snapshoot()

	var_82_0.FrameName = arg_82_0.paintingFrameName

	local var_82_1 = LeanTween.value(go(arg_82_0.nowPainting), 0, 1, var_0_2):setOnUpdate(System.Action_float(function(arg_83_0)
		var_82_0.Tween = arg_83_0
		arg_82_0.chat.localPosition = Vector3(arg_82_0.character.localPosition.x + 100, arg_82_0.chat.localPosition.y, 0)
	end)):setEase(LeanTweenType.easeInOutSine)
end

function var_0_0.setPreOrNext(arg_84_0, arg_84_1, arg_84_2)
	if arg_84_1 then
		arg_84_0.isRight = true
	else
		arg_84_0.isRight = false
	end

	if arg_84_0.shipVO:getGroupId() ~= arg_84_2:getGroupId() then
		arg_84_0.switchCnt = (arg_84_0.switchCnt or 0) + 1
	end

	if arg_84_0.switchCnt and arg_84_0.switchCnt >= 10 then
		gcAll()

		arg_84_0.switchCnt = 0
	end
end

function var_0_0.loadPainting(arg_85_0, arg_85_1, arg_85_2)
	local var_85_0 = arg_85_1

	arg_85_1 = MainMeshImagePainting.StaticGetPaintingName(var_85_0)

	if arg_85_0.isLoading == true then
		return
	end

	for iter_85_0, iter_85_1 in pairs(arg_85_0.tablePainting) do
		iter_85_1.localScale = Vector3(1, 1, 1)
	end

	if arg_85_0.LoadShipVOId and not arg_85_2 and arg_85_0.LoadShipVOId == arg_85_0.shipVO.id and arg_85_0.LoadPaintingCode == arg_85_1 then
		return
	end

	local var_85_1 = 0
	local var_85_2 = arg_85_0.isRight and 1800 or -1800
	local var_85_3 = arg_85_0:getPaintingFromTable(false)

	arg_85_0.isLoading = true

	local var_85_4 = arg_85_0.paintingCode
	local var_85_5 = {}

	if var_85_3 then
		table.insert(var_85_5, function(arg_86_0)
			local var_86_0 = var_85_3:GetComponent(typeof(RectTransform))
			local var_86_1 = var_85_3:GetComponent(typeof(CanvasGroup))

			LeanTween.cancel(go(var_86_1))
			LeanTween.alphaCanvas(var_86_1, 0, 0.3):setFrom(1):setUseEstimatedTime(true)
			LeanTween.moveX(var_86_0, -var_85_2, 0.3):setFrom(0):setOnComplete(System.Action(function()
				retPaintingPrefab(var_85_3, var_85_4)
				arg_86_0()
			end))
		end)
	end

	local var_85_6 = arg_85_0:getPaintingFromTable(true)

	arg_85_0.paintingCode = arg_85_1

	if arg_85_0.paintingCode and var_85_6 then
		local var_85_7 = var_85_6:GetComponent(typeof(RectTransform))

		table.insert(var_85_5, function(arg_88_0)
			arg_85_0.nowPainting = var_85_6

			LoadPaintingPrefabAsync(var_85_6, var_85_0, arg_85_0.paintingCode, arg_85_0.paintingFrameName or "chuanwu", function()
				ShipExpressionHelper.SetExpression(findTF(var_85_6, "fitter"):GetChild(0), arg_85_0.paintingCode)
				arg_88_0()
			end)
		end)
		table.insert(var_85_5, function(arg_90_0)
			LeanTween.cancel(go(var_85_7))
			LeanTween.moveX(var_85_7, 0, 0.3):setFrom(var_85_2):setOnComplete(System.Action(arg_90_0))

			local var_90_0 = var_85_6:GetComponent(typeof(CanvasGroup))

			LeanTween.alphaCanvas(var_90_0, 1, 0.3):setFrom(0):setUseEstimatedTime(true)
		end)
	end

	parallelAsync(var_85_5, function()
		arg_85_0.LoadShipVOId = arg_85_0.shipVO.id
		arg_85_0.LoadPaintingCode = arg_85_1
		arg_85_0.isLoading = false
	end)
end

function var_0_0.getPaintingFromTable(arg_92_0, arg_92_1)
	if arg_92_0.tablePainting == nil then
		print("self.tablePainting为空")

		return
	end

	for iter_92_0 = 1, #arg_92_0.tablePainting do
		if findTF(arg_92_0.tablePainting[iter_92_0], "fitter").childCount == 0 then
			if arg_92_1 == true and arg_92_0.tablePainting[iter_92_0] then
				return arg_92_0.tablePainting[iter_92_0]
			end
		elseif arg_92_1 == false and arg_92_0.tablePainting[iter_92_0] then
			return arg_92_0.tablePainting[iter_92_0]
		end
	end
end

function var_0_0.loadSkinBg(arg_93_0, arg_93_1, arg_93_2, arg_93_3, arg_93_4)
	if not arg_93_0.bgEffect then
		arg_93_0.bgEffect = {}
	end

	if arg_93_0.shipSkinBg ~= arg_93_1 or arg_93_0.isDesign ~= arg_93_2 or arg_93_0.isMeta ~= arg_93_3 then
		arg_93_0.shipSkinBg = arg_93_1
		arg_93_0.isDesign = arg_93_2
		arg_93_0.isMeta = arg_93_3

		if arg_93_0.isDesign then
			if arg_93_0.bgEffect then
				for iter_93_0, iter_93_1 in pairs(arg_93_0.bgEffect) do
					setActive(iter_93_1, false)
				end
			end

			if arg_93_0.bgEffect then
				for iter_93_2, iter_93_3 in pairs(arg_93_0.bgEffect) do
					setActive(iter_93_3, false)
				end
			end

			if arg_93_0.designBg and arg_93_0.designName ~= "raritydesign" .. arg_93_0.shipVO:getRarity() then
				PoolMgr.GetInstance():ReturnUI(arg_93_0.designName, arg_93_0.designBg)

				arg_93_0.designBg = nil
			end

			if not arg_93_0.designBg then
				PoolMgr.GetInstance():GetUI("raritydesign" .. arg_93_0.shipVO:getRarity(), true, function(arg_94_0)
					arg_93_0.designBg = arg_94_0
					arg_93_0.designName = "raritydesign" .. arg_93_0.shipVO:getRarity()

					arg_94_0.transform:SetParent(arg_93_0._tf, false)

					arg_94_0.transform.localPosition = Vector3(1, 1, 1)
					arg_94_0.transform.localScale = Vector3(1, 1, 1)

					arg_94_0.transform:SetSiblingIndex(1)
					setActive(arg_94_0, true)
				end)
			else
				setActive(arg_93_0.designBg, true)
			end
		elseif arg_93_0.isMeta then
			if arg_93_0.designBg then
				setActive(arg_93_0.designBg, false)
			end

			if arg_93_0.metaBg and arg_93_0.metaName ~= "raritymeta" .. arg_93_0.shipVO:getRarity() then
				PoolMgr.GetInstance():ReturnUI(arg_93_0.metaName, arg_93_0.metaBg)

				arg_93_0.metaBg = nil
			end

			if not arg_93_0.metaBg then
				PoolMgr.GetInstance():GetUI("raritymeta" .. arg_93_0.shipVO:getRarity(), true, function(arg_95_0)
					arg_93_0.metaBg = arg_95_0
					arg_93_0.metaName = "raritymeta" .. arg_93_0.shipVO:getRarity()

					arg_95_0.transform:SetParent(arg_93_0._tf, false)

					arg_95_0.transform.localPosition = Vector3(1, 1, 1)
					arg_95_0.transform.localScale = Vector3(1, 1, 1)

					arg_95_0.transform:SetSiblingIndex(1)
					setActive(arg_95_0, true)
				end)
			else
				setActive(arg_93_0.metaBg, true)
			end
		else
			if arg_93_0.designBg then
				setActive(arg_93_0.designBg, false)
			end

			if arg_93_0.metaBg then
				setActive(arg_93_0.metaBg, false)
			end

			for iter_93_4 = 1, 5 do
				local var_93_0 = arg_93_0.shipVO:getRarity()

				if arg_93_0.bgEffect[iter_93_4] then
					setActive(arg_93_0.bgEffect[iter_93_4], iter_93_4 == var_93_0 and ShipViewConst.currentPage ~= ShipViewConst.PAGE.REMOULD and not arg_93_4)
				elseif var_93_0 > 2 and var_93_0 == iter_93_4 and not arg_93_4 then
					PoolMgr.GetInstance():GetUI("al_bg02_" .. var_93_0 - 1, true, function(arg_96_0)
						arg_93_0.bgEffect[iter_93_4] = arg_96_0

						arg_96_0.transform:SetParent(arg_93_0._tf, false)

						arg_96_0.transform.localPosition = Vector3(0, 0, 0)
						arg_96_0.transform.localScale = Vector3(1, 1, 1)

						arg_96_0.transform:SetSiblingIndex(1)
						setActive(arg_96_0, not ShipViewConst.IsSubLayerPage(ShipViewConst.currentPage))
					end)
				end
			end
		end

		GetSpriteFromAtlasAsync("bg/star_level_bg_" .. arg_93_1, "", function(arg_97_0)
			if not arg_93_0.exited and arg_93_0.shipSkinBg == arg_93_1 then
				setImageSprite(arg_93_0.background, arg_97_0)
			end
		end)
	end
end

function var_0_0.getInitmacyWords(arg_98_0)
	local var_98_0 = arg_98_0.shipVO:getIntimacyLevel()
	local var_98_1 = Mathf.Clamp(var_98_0, 1, 5)

	return "feeling" .. var_98_1
end

function var_0_0.paintView(arg_99_0)
	if LeanTween.isTweening(arg_99_0.chat.gameObject) then
		LeanTween.cancel(arg_99_0.chat.gameObject)

		arg_99_0.chat.localScale = Vector3(0, 0, 0)
		arg_99_0.chatFlag = nil
	end

	arg_99_0.character:GetComponent("Image").enabled = false
	arg_99_0.inPaintingView = true

	local var_99_0 = {}
	local var_99_1 = arg_99_0._tf.childCount
	local var_99_2 = 0

	while var_99_2 < var_99_1 do
		local var_99_3 = arg_99_0._tf:GetChild(var_99_2)

		if var_99_3.gameObject.activeSelf and var_99_3 ~= arg_99_0.main and var_99_3 ~= arg_99_0.background then
			var_99_0[#var_99_0 + 1] = var_99_3

			setActive(var_99_3, false)
		end

		var_99_2 = var_99_2 + 1
	end

	local var_99_4 = arg_99_0.main.childCount
	local var_99_5 = 0

	while var_99_5 < var_99_4 do
		local var_99_6 = arg_99_0.main:GetChild(var_99_5)

		if var_99_6.gameObject.activeSelf and var_99_6 ~= arg_99_0.shipInfo then
			var_99_0[#var_99_0 + 1] = var_99_6

			setActive(var_99_6, false)
		end

		var_99_5 = var_99_5 + 1
	end

	arg_99_0.shipDetailView:Hide()
	setActive(arg_99_0.blurPanel, false)
	setActive(pg.playerResUI._go, false)

	var_99_0[#var_99_0 + 1] = arg_99_0.chat

	openPortrait()
	setActive(arg_99_0.common, false)

	arg_99_0.mainMask.enabled = false

	arg_99_0.mainMask:PerformClipping()

	local var_99_7 = arg_99_0.nowPainting
	local var_99_8 = var_99_7.anchoredPosition.x
	local var_99_9 = var_99_7.anchoredPosition.y
	local var_99_10 = var_99_7.rect.width
	local var_99_11 = var_99_7.rect.height
	local var_99_12 = arg_99_0._tf.rect.width / UnityEngine.Screen.width
	local var_99_13 = arg_99_0._tf.rect.height / UnityEngine.Screen.height
	local var_99_14 = var_99_10 / 2
	local var_99_15 = var_99_11 / 2
	local var_99_16
	local var_99_17
	local var_99_18 = GetOrAddComponent(arg_99_0.background, "PinchZoom")
	local var_99_19 = GetOrAddComponent(arg_99_0.background, "EventTriggerListener")
	local var_99_20 = true
	local var_99_21 = false

	var_99_19:AddPointDownFunc(function(arg_100_0)
		if Input.touchCount == 1 or IsUnityEditor then
			var_99_21 = true
			var_99_20 = true
		elseif Input.touchCount >= 2 then
			var_99_20 = false
			var_99_21 = false
		end
	end)
	var_99_19:AddPointUpFunc(function(arg_101_0)
		if Input.touchCount <= 2 then
			var_99_20 = true
		end
	end)
	var_99_19:AddBeginDragFunc(function(arg_102_0, arg_102_1)
		var_99_21 = false
		var_99_16 = arg_102_1.position.x * var_99_12 - var_99_14 - tf(arg_99_0.nowPainting).localPosition.x
		var_99_17 = arg_102_1.position.y * var_99_13 - var_99_15 - tf(arg_99_0.nowPainting).localPosition.y
	end)
	var_99_19:AddDragFunc(function(arg_103_0, arg_103_1)
		if var_99_18.processing then
			return
		end

		if var_99_20 then
			local var_103_0 = tf(arg_99_0.nowPainting).localPosition

			tf(arg_99_0.nowPainting).localPosition = Vector3(arg_103_1.position.x * var_99_12 - var_99_14 - var_99_16, arg_103_1.position.y * var_99_13 - var_99_15 - var_99_17, -22)
		end
	end)
	onButton(arg_99_0, arg_99_0.background, function()
		arg_99_0:hidePaintView()
	end, SFX_CANCEL)

	function var_0_0.hidePaintView(arg_105_0, arg_105_1)
		if not arg_105_1 and not var_99_21 then
			return
		end

		arg_105_0.character:GetComponent("Image").enabled = true
		Input.multiTouchEnabled = false

		setActive(arg_105_0.common, true)
		SwitchPanel(arg_105_0.shipInfo, -460, nil, var_0_2 * 2)

		var_99_19.enabled = false
		var_99_18.enabled = false
		arg_105_0.character.localScale = Vector3.one

		arg_105_0.shipDetailView:Show()
		setActive(arg_105_0.blurPanel, true)
		setActive(pg.playerResUI._go, true)

		for iter_105_0, iter_105_1 in ipairs(var_99_0) do
			setActive(iter_105_1, true)
		end

		closePortrait()

		arg_105_0.nowPainting.localScale = Vector3(1, 1, 1)

		setAnchoredPosition(arg_105_0.nowPainting, {
			x = var_99_8,
			y = var_99_9
		})

		arg_105_0.background:GetComponent("Button").enabled = false
		arg_105_0.nowPainting:GetComponent("CanvasGroup").blocksRaycasts = true
		arg_105_0.mainMask.enabled = true

		arg_105_0.mainMask:PerformClipping()

		arg_105_0.inPaintingView = false
	end

	SwitchPanel(arg_99_0.shipInfo, var_0_1, nil, var_0_2 * 2):setOnComplete(System.Action(function()
		var_99_18.enabled = true
		var_99_19.enabled = true
		arg_99_0.background:GetComponent("Button").enabled = true
		arg_99_0.nowPainting:GetComponent("CanvasGroup").blocksRaycasts = false
	end))
end

function var_0_0.onBackPressed(arg_107_0)
	if arg_107_0.inUpgradeAnim then
		return
	end

	if arg_107_0.awakenPlay then
		return
	end

	if arg_107_0.shipChangeNameView.isOpenRenamePanel then
		arg_107_0.shipChangeNameView:ActionInvoke("DisplayRenamePanel", false)

		return
	end

	if arg_107_0.shipCustomMsgBox.isShowCustomMsgBox then
		arg_107_0.shipCustomMsgBox:ActionInvoke("hideCustomMsgBox")

		return
	end

	if arg_107_0.shipHuntingRangeView.onSelected then
		arg_107_0.shipHuntingRangeView:ActionInvoke("HideHuntingRange")

		return
	end

	if arg_107_0.inPaintingView then
		arg_107_0:hidePaintView(true)

		return
	end

	if arg_107_0.expItemUsagePage and arg_107_0.expItemUsagePage:GetLoaded() and arg_107_0.expItemUsagePage:isShowing() then
		arg_107_0.expItemUsagePage:Hide()

		return
	end

	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_107_0:findTF("top/back_btn", arg_107_0.common))
end

function var_0_0.willExit(arg_108_0)
	Input.multiTouchEnabled = true

	pg.UIMgr.GetInstance():UnOverlayPanel(arg_108_0.chat, arg_108_0.character)
	arg_108_0:blurPage(ShipViewConst.currentPage)
	setActive(arg_108_0.background, false)

	if arg_108_0.designBg then
		PoolMgr.GetInstance():ReturnUI(arg_108_0.designName, arg_108_0.designBg)
	end

	if arg_108_0.metaBg then
		PoolMgr.GetInstance():ReturnUI(arg_108_0.metaName, arg_108_0.metaBg)
	end

	arg_108_0.intensifyToggle:GetComponent("Toggle").onValueChanged:RemoveAllListeners()
	arg_108_0.upgradeToggle:GetComponent("Toggle").onValueChanged:RemoveAllListeners()
	LeanTween.cancel(arg_108_0.chat.gameObject)

	if arg_108_0.paintingCode then
		for iter_108_0 = 1, #arg_108_0.tablePainting do
			local var_108_0 = go(arg_108_0.tablePainting[iter_108_0])

			if LeanTween.isTweening(var_108_0) then
				LeanTween.cancel(go(var_108_0))
			end
		end

		retPaintingPrefab(arg_108_0.nowPainting, arg_108_0.paintingCode)
	end

	arg_108_0.shipDetailView:Destroy()
	arg_108_0.shipFashionView:Destroy()
	arg_108_0.shipEquipView:Destroy()
	arg_108_0.shipHuntingRangeView:Destroy()
	arg_108_0.shipCustomMsgBox:Destroy()
	arg_108_0.shipChangeNameView:Destroy()
	clearImageSprite(arg_108_0.background)

	if arg_108_0.energyTimer then
		arg_108_0.energyTimer:Stop()

		arg_108_0.energyTimer = nil
	end

	if arg_108_0.chatTimer then
		arg_108_0.chatTimer:Stop()

		arg_108_0.chatTimer = nil
	end

	arg_108_0:StopPreVoice()
	cameraPaintViewAdjust(false)

	if arg_108_0.tweens then
		cancelTweens(arg_108_0.tweens)
	end

	pg.UIMgr.GetInstance():UnOverlayPanel(arg_108_0.blurPanel, arg_108_0._tf)

	arg_108_0.shareData = nil
end

function var_0_0.RefreshShipExpItemUsagePage(arg_109_0)
	if arg_109_0.expItemUsagePage and arg_109_0.expItemUsagePage:GetLoaded() and arg_109_0.expItemUsagePage:isShowing() then
		arg_109_0.expItemUsagePage:Flush(arg_109_0.shipVO)
	end
end

function var_0_0.OnWillLogout(arg_110_0)
	if arg_110_0.inPaintingView then
		arg_110_0:hidePaintView(true)
	end
end

function var_0_0.checkPaintingRes(arg_111_0, arg_111_1)
	local var_111_0 = PaintingGroupConst.GetPaintingNameListByShipVO(arg_111_0.shipVO)
	local var_111_1 = {
		isShowBox = true,
		paintingNameList = var_111_0,
		finishFunc = arg_111_1
	}

	PaintingGroupConst.PaintingDownload(var_111_1)
end

return var_0_0
