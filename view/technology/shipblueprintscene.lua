local var_0_0 = class("ShipBluePrintScene", import("..base.BaseUI"))
local var_0_1 = pg.ship_data_blueprint
local var_0_2 = pg.ship_data_template
local var_0_3 = pg.ship_data_breakout
local var_0_4 = 3
local var_0_5 = -10
local var_0_6 = 2.3
local var_0_7 = 0.3

function var_0_0.getUIName(arg_1_0)
	return "ShipBluePrintUI"
end

function var_0_0.setVersion(arg_2_0, arg_2_1)
	arg_2_0.version = arg_2_1
end

function var_0_0.setShipVOs(arg_3_0, arg_3_1)
	arg_3_0.shipVOs = arg_3_1
end

function var_0_0.getShipById(arg_4_0, arg_4_1)
	return arg_4_0.shipVOs[arg_4_1]
end

function var_0_0.setTaskVOs(arg_5_0, arg_5_1)
	arg_5_0.taskVOs = arg_5_1
end

function var_0_0.getTaskById(arg_6_0, arg_6_1)
	return arg_6_0.taskVOs[arg_6_1] or Task.New({
		id = arg_6_1
	})
end

function var_0_0.getItemById(arg_7_0, arg_7_1)
	return getProxy(BagProxy):getItemById(arg_7_1) or Item.New({
		count = 0,
		id = arg_7_1
	})
end

function var_0_0.setShipBluePrints(arg_8_0, arg_8_1)
	arg_8_0.bluePrintByIds = arg_8_1
end

function var_0_0.updateShipBluePrintVO(arg_9_0, arg_9_1)
	if arg_9_1 then
		arg_9_0.bluePrintByIds[arg_9_1.id] = arg_9_1
	end

	arg_9_0:initShips()
end

function var_0_0.init(arg_10_0)
	arg_10_0.main = arg_10_0:findTF("main")
	arg_10_0.centerPanel = arg_10_0:findTF("center_panel", arg_10_0.main)
	arg_10_0.blurPanel = arg_10_0:findTF("blur_panel")
	arg_10_0.top = arg_10_0:findTF("adapt", arg_10_0.blurPanel)
	arg_10_0.topPanel = arg_10_0:findTF("top", arg_10_0.top)
	arg_10_0.topBg = arg_10_0:findTF("top_bg", arg_10_0.blurPanel)
	arg_10_0.backBtn = arg_10_0:findTF("top/back", arg_10_0.top)
	arg_10_0.leftPanle = arg_10_0:findTF("left_panel", arg_10_0.top)
	arg_10_0.bottomPanel = arg_10_0:findTF("bottom_panel", arg_10_0.top)
	arg_10_0.rightPanel = arg_10_0:findTF("right_panel", arg_10_0.top)
	arg_10_0.shipContainer = arg_10_0:findTF("ships/bg/content", arg_10_0.bottomPanel)
	arg_10_0.shipTpl = arg_10_0:findTF("ship_tpl", arg_10_0.bottomPanel)
	arg_10_0.versionBtn = arg_10_0:findTF("ships/bg/version/version_btn", arg_10_0.bottomPanel)
	arg_10_0.eyeTF = arg_10_0:findTF("eye", arg_10_0.leftPanle)
	arg_10_0.painting = arg_10_0:findTF("main/center_panel/painting")
	arg_10_0.nameTF = arg_10_0:findTF("name", arg_10_0.centerPanel)
	arg_10_0.shipName = arg_10_0:findTF("name_mask/Text", arg_10_0.nameTF)
	arg_10_0.shipType = arg_10_0:findTF("type", arg_10_0.nameTF)
	arg_10_0.englishName = arg_10_0:findTF("english_name", arg_10_0.nameTF)
	arg_10_0.shipInfoStarTpl = arg_10_0:findTF("star_tpl", arg_10_0.nameTF)

	setActive(arg_10_0.shipInfoStarTpl, false)

	arg_10_0.stars = arg_10_0:findTF("stars", arg_10_0.nameTF)
	arg_10_0.initBtn = arg_10_0:findTF("property_panel/btns/init_toggle", arg_10_0.leftPanle)
	arg_10_0.attrBtn = arg_10_0:findTF("property_panel/btns/attr_toggle", arg_10_0.leftPanle)
	arg_10_0.attrDisableBtn = arg_10_0:findTF("property_panel/btns/attr_toggle/disable", arg_10_0.leftPanle)
	arg_10_0.initPanel = arg_10_0:findTF("property_panel/init_panel", arg_10_0.leftPanle)
	arg_10_0.propertyPanel = PropertyPanel.New(arg_10_0.initPanel, 32)

	setText(arg_10_0:findTF("property_title1/Text", arg_10_0.initPanel), i18n("blueprint_combatperformance"))
	setText(arg_10_0:findTF("property_title2/Text", arg_10_0.initPanel), i18n("blueprint_shipperformance"))

	arg_10_0.skillRect = arg_10_0:findTF("property_panel/init_panel/skills_rect", arg_10_0.leftPanle)
	arg_10_0.skillPanel = arg_10_0:findTF("property_panel/init_panel/skills_rect/skills", arg_10_0.leftPanle)
	arg_10_0.skillTpl = arg_10_0:findTF("skilltpl", arg_10_0.skillPanel)
	arg_10_0.skillArrLeft = arg_10_0:findTF("property_panel/init_panel/arrow1", arg_10_0.leftPanle)
	arg_10_0.skillArrRight = arg_10_0:findTF("property_panel/init_panel/arrow2", arg_10_0.leftPanle)
	arg_10_0.simulationBtn = arg_10_0:findTF("property_panel/init_panel/property_title2/simulation", arg_10_0.leftPanle)
	arg_10_0.attrPanel = arg_10_0:findTF("property_panel/attr_panel", arg_10_0.leftPanle)
	arg_10_0.modAdditionPanel = arg_10_0:findTF("property_panel/attr_panel", arg_10_0.leftPanle)
	arg_10_0.modAdditionContainer = arg_10_0:findTF("scroll_rect/content", arg_10_0.modAdditionPanel)
	arg_10_0.modAdditionTpl = arg_10_0:findTF("addition_tpl", arg_10_0.modAdditionContainer)
	arg_10_0.preViewBtn = arg_10_0:findTF("pre_view", arg_10_0.attrPanel)
	arg_10_0.stateInfo = arg_10_0:findTF("state_info", arg_10_0.centerPanel)
	arg_10_0.startBtn = arg_10_0:findTF("state_info/start_btn", arg_10_0.centerPanel)
	arg_10_0.lockPanel = arg_10_0:findTF("state_info/lock_panel", arg_10_0.centerPanel)
	arg_10_0.lockBtn = arg_10_0:findTF("lock", arg_10_0.lockPanel)
	arg_10_0.finishedBtn = arg_10_0:findTF("state_info/finished_btn", arg_10_0.centerPanel)
	arg_10_0.progressPanel = arg_10_0:findTF("state_info/progress", arg_10_0.centerPanel)

	setText(arg_10_0:findTF("label", arg_10_0.progressPanel), i18n("blueprint_researching"))

	arg_10_0.progressContainer = arg_10_0:findTF("content", arg_10_0.progressPanel)
	arg_10_0.progressTpl = arg_10_0:findTF("item", arg_10_0.progressContainer)
	arg_10_0.openCondition = arg_10_0:findTF("state_info/open_condition", arg_10_0.centerPanel)
	arg_10_0.speedupBtn = arg_10_0:findTF("main/speedup_btn")
	arg_10_0.taskListPanel = arg_10_0:findTF("task_list", arg_10_0.rightPanel)
	arg_10_0.taskContainer = arg_10_0:findTF("task_list/scroll/content", arg_10_0.rightPanel)
	arg_10_0.taskTpl = arg_10_0:findTF("task_list/task_tpl", arg_10_0.rightPanel)
	arg_10_0.modPanel = arg_10_0:findTF("mod_panel", arg_10_0.rightPanel)
	arg_10_0.attrContainer = arg_10_0:findTF("desc/atrrs", arg_10_0.modPanel)
	arg_10_0.levelSlider = arg_10_0:findTF("title/slider", arg_10_0.modPanel):GetComponent(typeof(Slider))
	arg_10_0.levelSliderTxt = arg_10_0:findTF("title/slider/Text", arg_10_0.modPanel)
	arg_10_0.preLevelSlider = arg_10_0:findTF("title/pre_slider", arg_10_0.modPanel):GetComponent(typeof(Slider))
	arg_10_0.modLevel = arg_10_0:findTF("title/level_bg/Text", arg_10_0.modPanel):GetComponent(typeof(Text))
	arg_10_0.needLevelTxt = arg_10_0:findTF("title/Text", arg_10_0.modPanel):GetComponent(typeof(Text))
	arg_10_0.calcPanel = arg_10_0.modPanel:Find("desc/calc_panel")
	arg_10_0.calcMinusBtn = arg_10_0.calcPanel:Find("calc/base/minus")
	arg_10_0.calcPlusBtn = arg_10_0.calcPanel:Find("calc/base/plus")
	arg_10_0.calcTxt = arg_10_0.calcPanel:Find("calc/base/count/Text")
	arg_10_0.calcMaxBtn = arg_10_0.calcPanel:Find("calc/max")
	arg_10_0.itemInfo = arg_10_0.calcPanel:Find("item_bg")
	arg_10_0.itemInfoIcon = arg_10_0.itemInfo:Find("icon")
	arg_10_0.itemInfoCount = arg_10_0.itemInfo:Find("kc")
	arg_10_0.modBtn = arg_10_0.calcPanel:Find("confirm_btn")
	arg_10_0.fittingBtn = arg_10_0:findTF("desc/fitting_btn", arg_10_0.modPanel)
	arg_10_0.fittingBtnEffect = arg_10_0.fittingBtn:Find("anim/ShipBlue02")
	arg_10_0.fittingPanel = arg_10_0:findTF("fitting_panel", arg_10_0.rightPanel)

	setActive(arg_10_0.fittingPanel, false)

	arg_10_0.fittingAttrPanel = arg_10_0:findTF("desc/middle", arg_10_0.fittingPanel)
	arg_10_0.phasePic = arg_10_0:findTF("title/phase", arg_10_0.fittingPanel)
	arg_10_0.phaseSlider = arg_10_0:findTF("desc/top/slider", arg_10_0.fittingPanel):GetComponent(typeof(Slider))
	arg_10_0.phaseSliderTxt = arg_10_0:findTF("desc/top/precent", arg_10_0.fittingPanel)
	arg_10_0.prePhaseSlider = arg_10_0:findTF("desc/top/pre_slider", arg_10_0.fittingPanel):GetComponent(typeof(Slider))
	arg_10_0.fittingNeedMask = arg_10_0:findTF("desc/top/mask", arg_10_0.fittingPanel)
	arg_10_0.fittingCalcPanel = arg_10_0:findTF("desc/bottom", arg_10_0.fittingPanel)
	arg_10_0.fittingCalcMinusBtn = arg_10_0:findTF("calc/base/minus", arg_10_0.fittingCalcPanel)
	arg_10_0.fittingCalcPlusBtn = arg_10_0:findTF("calc/base/plus", arg_10_0.fittingCalcPanel)
	arg_10_0.fittingCalcTxt = arg_10_0:findTF("calc/base/count/Text", arg_10_0.fittingCalcPanel)
	arg_10_0.fittingCalcMaxBtn = arg_10_0:findTF("calc/max", arg_10_0.fittingCalcPanel)
	arg_10_0.fittingItemInfo = arg_10_0:findTF("item_bg", arg_10_0.fittingCalcPanel)
	arg_10_0.fittingItemInfoIcon = arg_10_0:findTF("icon", arg_10_0.fittingItemInfo)
	arg_10_0.fittingItemInfoCount = arg_10_0:findTF("kc", arg_10_0.fittingItemInfo)
	arg_10_0.fittingConfirmBtn = arg_10_0:findTF("confirm_btn", arg_10_0.fittingCalcPanel)
	arg_10_0.fittingCancelBtn = arg_10_0:findTF("cancel_btn", arg_10_0.fittingCalcPanel)
	arg_10_0.msgPanel = arg_10_0:findTF("msg_panel", arg_10_0.blurPanel)

	setActive(arg_10_0.msgPanel, false)

	arg_10_0.versionPanel = arg_10_0._tf:Find("version_panel")

	setActive(arg_10_0.versionPanel, false)

	arg_10_0.preViewer = arg_10_0:findTF("preview")
	arg_10_0.preViewerFrame = arg_10_0:findTF("preview/frame")

	setText(arg_10_0:findTF("bg/title/Image", arg_10_0.preViewerFrame), i18n("word_preview"))
	setActive(arg_10_0.preViewer, false)

	arg_10_0.sea = arg_10_0:findTF("sea", arg_10_0.preViewerFrame)
	arg_10_0.rawImage = arg_10_0.sea:GetComponent("RawImage")

	setActive(arg_10_0.rawImage, false)

	arg_10_0.seaLoading = arg_10_0:findTF("bg/loading", arg_10_0.preViewerFrame)
	arg_10_0.healTF = arg_10_0:findTF("resources/heal")
	arg_10_0.healTF.transform.localPosition = Vector3(-360, 50, 40)

	setActive(arg_10_0.healTF, false)

	arg_10_0.stages = arg_10_0:findTF("stageScrollRect/stages", arg_10_0.preViewerFrame)
	arg_10_0.breakView = arg_10_0:findTF("content/Text", arg_10_0.preViewerFrame)
	arg_10_0.previewAttrPanel = arg_10_0:findTF("preview/attrs_panel/attr_panel")
	arg_10_0.previewAttrContainer = arg_10_0:findTF("content", arg_10_0.previewAttrPanel)

	setText(arg_10_0:findTF("preview/attrs_panel/Text"), i18n("meta_energy_preview_tip"))
	setText(arg_10_0:findTF("preview/attrs_panel/desc"), i18n("meta_energy_preview_title"))

	arg_10_0.helpBtn = arg_10_0:findTF("helpBtn", arg_10_0.top)
	arg_10_0.exchangeBtn = arg_10_0:findTF("exchangeBtn", arg_10_0.top)
	arg_10_0.itemUnlockBtn = arg_10_0:findTF("itemUnlockBtn", arg_10_0.top)
	arg_10_0.bottomWidth = arg_10_0.bottomPanel.rect.height
	arg_10_0.topWidth = arg_10_0.topPanel.rect.height * 2
	arg_10_0.taskTFs = {}
	arg_10_0.leanTweens = {}
	arg_10_0.unlockPanel = arg_10_0.blurPanel:Find("unlock_panel")

	setActive(arg_10_0.unlockPanel, false)

	arg_10_0.svQuickExchange = BlueprintQuickExchangeView.New(arg_10_0._tf, arg_10_0.event)
end

function var_0_0.didEnter(arg_11_0)
	local var_11_0 = getProxy(TechnologyProxy):getConfigMaxVersion()

	if not arg_11_0.contextData.shipBluePrintVO then
		local var_11_1 = {}

		for iter_11_0 = 1, var_11_0 do
			var_11_1[iter_11_0] = 0
		end

		for iter_11_1, iter_11_2 in pairs(arg_11_0.bluePrintByIds) do
			local var_11_2 = iter_11_2:getConfig("blueprint_version")

			var_11_1[var_11_2] = var_11_1[var_11_2] + (iter_11_2.state == ShipBluePrint.STATE_UNLOCK and 1 or 0)

			if iter_11_2.state == ShipBluePrint.STATE_DEV then
				arg_11_0.contextData.shipBluePrintVO = arg_11_0.contextData.shipBluePrintVO or iter_11_2

				break
			end
		end

		if not arg_11_0.contextData.shipBluePrintVO then
			for iter_11_3 = 1, var_11_0 do
				arg_11_0.version = iter_11_3

				if var_11_1[iter_11_3] <= 4 then
					break
				end
			end

			arg_11_0:emit(ShipBluePrintMediator.SET_TECHNOLOGY_VERSION, arg_11_0.version)
		end
	end

	arg_11_0:switchHide()
	arg_11_0:initShips()
	onButton(arg_11_0, arg_11_0.speedupBtn, function()
		arg_11_0:emit(ShipBluePrintMediator.ON_CLICK_SPEEDUP_BTN)
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.backBtn, function()
		arg_11_0:closeView()
	end, SOUND_BACK)
	onButton(arg_11_0, arg_11_0.startBtn, function()
		if not arg_11_0.contextData.shipBluePrintVO then
			return
		end

		local var_14_0 = arg_11_0.contextData.shipBluePrintVO.id

		arg_11_0:emit(ShipBluePrintMediator.ON_START, var_14_0)
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.finishedBtn, function()
		if not arg_11_0.contextData.shipBluePrintVO then
			return
		end

		local var_15_0 = arg_11_0.contextData.shipBluePrintVO.id

		arg_11_0:emit(ShipBluePrintMediator.ON_FINISHED, var_15_0)
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.itemUnlockBtn, function()
		if not arg_11_0.contextData.shipBluePrintVO then
			return
		end

		arg_11_0:showUnlockPanel()
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.preViewBtn, function()
		arg_11_0:openPreView()
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.seaLoading, function()
		if not arg_11_0.previewer then
			arg_11_0:showBarrage()
		end
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.preViewer, function()
		arg_11_0:closePreview()
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.eyeTF, function()
		if arg_11_0.isSwitchAnim then
			return
		end

		arg_11_0:switchHide()
		arg_11_0:switchState(var_0_7, not arg_11_0.flag)
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.main, function()
		if arg_11_0.isSwitchAnim then
			return
		end

		if not arg_11_0.flag then
			arg_11_0:switchHide()
			arg_11_0:switchState(var_0_7, not arg_11_0.flag)
		end
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip[isActive(arg_11_0.fittingPanel) and "help_shipblueprintui_luck" or "help_shipblueprintui"].tip
		})
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.exchangeBtn, function()
		arg_11_0.svQuickExchange:Load()
		arg_11_0.svQuickExchange:ActionInvoke("Show")
		arg_11_0.svQuickExchange:ActionInvoke("UpdateBlueprint", arg_11_0.contextData.shipBluePrintVO)
	end)
	pg.UIMgr.GetInstance():OverlayPanelPB(arg_11_0.blurPanel, {
		pbList = {
			arg_11_0.rightPanel:Find("task_list"),
			arg_11_0.rightPanel:Find("mod_panel"),
			arg_11_0.leftPanle:Find("property_panel"),
			arg_11_0.bottomPanel:Find("ships/bg")
		}
	})
	setText(arg_11_0:findTF("window/top/bg/infomation/title", arg_11_0.msgPanel), i18n("title_info"))
	onButton(arg_11_0, arg_11_0:findTF("window/top/btnBack", arg_11_0.msgPanel), function()
		pg.UIMgr.GetInstance():UnblurPanel(arg_11_0.msgPanel, arg_11_0.top)
		setActive(arg_11_0.msgPanel, false)
	end, SFX_CANCEL)
	setText(arg_11_0:findTF("window/confirm_btn/Text", arg_11_0.msgPanel), i18n("text_confirm"))
	onButton(arg_11_0, arg_11_0:findTF("window/confirm_btn", arg_11_0.msgPanel), function()
		pg.UIMgr.GetInstance():UnblurPanel(arg_11_0.msgPanel, arg_11_0.top)
		setActive(arg_11_0.msgPanel, false)
	end, SFX_CANCEL)
	onButton(arg_11_0, arg_11_0:findTF("bg", arg_11_0.msgPanel), function()
		pg.UIMgr.GetInstance():UnblurPanel(arg_11_0.msgPanel, arg_11_0.top)
		setActive(arg_11_0.msgPanel, false)
	end, SFX_CANCEL)
	onButton(arg_11_0, arg_11_0.unlockPanel:Find("window/top/btnBack"), function()
		pg.UIMgr.GetInstance():UnblurPanel(arg_11_0.unlockPanel, arg_11_0.top)
		setActive(arg_11_0.unlockPanel, false)
	end, SFX_CANCEL)
	setText(arg_11_0.unlockPanel:Find("window/confirm_btn/Text"), i18n("text_confirm"))
	setText(arg_11_0.unlockPanel:Find("window/cancel_btn/Text"), i18n("text_cancel"))
	setText(arg_11_0.unlockPanel:Find("window/top/bg/infomation/title"), i18n("title_info"))
	onButton(arg_11_0, arg_11_0.unlockPanel:Find("window/cancel_btn"), function()
		pg.UIMgr.GetInstance():UnblurPanel(arg_11_0.unlockPanel, arg_11_0.top)
		setActive(arg_11_0.unlockPanel, false)
	end, SFX_CANCEL)
	onButton(arg_11_0, arg_11_0.unlockPanel:Find("bg"), function()
		pg.UIMgr.GetInstance():UnblurPanel(arg_11_0.unlockPanel, arg_11_0.top)
		setActive(arg_11_0.unlockPanel, false)
	end, SFX_CANCEL)
	GetImageSpriteFromAtlasAsync("ui/shipblueprintui_atlas", "version_" .. arg_11_0.version, arg_11_0.versionBtn)
	arg_11_0:updateVersionBtnTip()

	if var_11_0 > 1 then
		onButton(arg_11_0, arg_11_0.versionBtn, function()
			if arg_11_0.cbTimer then
				return
			end

			setActive(arg_11_0.versionPanel, true)
			pg.UIMgr.GetInstance():BlurPanel(arg_11_0.versionPanel)
		end, SFX_PANEL)
		onButton(arg_11_0, arg_11_0.versionPanel:Find("bg"), function()
			pg.UIMgr.GetInstance():UnblurPanel(arg_11_0.versionPanel, arg_11_0._tf)
			setActive(arg_11_0.versionPanel, false)
		end, SFX_CANCEL)

		local var_11_3 = UIItemList.New(arg_11_0.versionPanel:Find("window/content"), arg_11_0.versionPanel:Find("window/content/version_1"))

		var_11_3:make(function(arg_32_0, arg_32_1, arg_32_2)
			arg_32_1 = arg_32_1 + 1

			if arg_32_0 == UIItemList.EventUpdate then
				arg_32_2.name = "version_" .. arg_32_1

				GetImageSpriteFromAtlasAsync("ui/shipblueprintui_atlas", "version_" .. arg_32_1, arg_32_2:Find("image"))
				setText(arg_32_2:Find("number/Text"), string.format("%02d", arg_32_1))
				onButton(arg_11_0, arg_32_2, function()
					arg_11_0.version = arg_32_1

					arg_11_0:emit(ShipBluePrintMediator.SET_TECHNOLOGY_VERSION, arg_11_0.version)

					arg_11_0.contextData.shipBluePrintVO = nil

					GetImageSpriteFromAtlasAsync("ui/shipblueprintui_atlas", "version_" .. arg_11_0.version, arg_11_0.versionBtn)
					arg_11_0:initShips()
					arg_11_0:updateVersionBtnTip()
					pg.UIMgr.GetInstance():UnblurPanel(arg_11_0.versionPanel, arg_11_0._tf)
					setActive(arg_11_0.versionPanel, false)
				end, SFX_CANCEL)
			end
		end)
		var_11_3:align(var_11_0)
		arg_11_0:updateVersionPanelBtnTip()
	end

	LeanTween.alpha(rtf(arg_11_0.skillArrLeft), 0.25, 1):setEase(LeanTweenType.easeInOutSine):setLoopPingPong()
	LeanTween.alpha(rtf(arg_11_0.skillArrRight), 0.25, 1):setEase(LeanTweenType.easeInOutSine):setLoopPingPong()
end

function var_0_0.updateVersionBtnTip(arg_34_0)
	local var_34_0 = getProxy(TechnologyProxy)
	local var_34_1 = var_34_0:getConfigMaxVersion()
	local var_34_2 = {}

	for iter_34_0 = 1, var_34_1 do
		if iter_34_0 ~= arg_34_0.version then
			table.insert(var_34_2, iter_34_0)
		end
	end

	setActive(arg_34_0.versionBtn:Find("tip"), var_34_0:CheckPursuingCostTip(var_34_2))
end

function var_0_0.updateVersionPanelBtnTip(arg_35_0)
	local var_35_0 = getProxy(TechnologyProxy)
	local var_35_1 = var_35_0:getConfigMaxVersion()

	for iter_35_0 = 1, var_35_1 do
		setActive(arg_35_0.versionPanel:Find("window/content/version_" .. iter_35_0 .. "/tip"), var_35_0:CheckPursuingCostTip({
			iter_35_0
		}))
	end
end

function var_0_0.updateAllPursuingCostTip(arg_36_0)
	arg_36_0:updateVersionBtnTip()
	arg_36_0:updateVersionPanelBtnTip()

	for iter_36_0, iter_36_1 in pairs(arg_36_0.bluePrintItems) do
		iter_36_1:updatePursuingTip()
	end
end

function var_0_0.switchHide(arg_37_0)
	local var_37_0 = not arg_37_0.flag

	LeanTween.cancel(arg_37_0.bottomPanel)
	LeanTween.cancel(arg_37_0.topPanel)
	LeanTween.cancel(arg_37_0.topBg)

	if var_37_0 then
		LeanTween.moveY(arg_37_0.bottomPanel, 0, var_0_7)
		LeanTween.moveY(arg_37_0.topPanel, 0, var_0_7)
		LeanTween.moveY(arg_37_0.topBg, 0, var_0_7)
	else
		LeanTween.moveY(arg_37_0.bottomPanel, -arg_37_0.bottomWidth, var_0_7)
		LeanTween.moveY(arg_37_0.topPanel, arg_37_0.topWidth, var_0_7)
		LeanTween.moveY(arg_37_0.topBg, arg_37_0.topWidth, var_0_7)
	end

	setActive(arg_37_0.nameTF, var_37_0)
	setActive(arg_37_0.stateInfo, var_37_0)
	setActive(arg_37_0.helpBtn, var_37_0)
	setActive(arg_37_0.exchangeBtn, var_37_0)
	setImageAlpha(arg_37_0.itemUnlockBtn, var_37_0 and 1 or 0)
	setImageRaycastTarget(arg_37_0.itemUnlockBtn, var_37_0)
	setImageAlpha(arg_37_0.speedupBtn, var_37_0 and 1 or 0)
	setImageRaycastTarget(arg_37_0.speedupBtn, var_37_0)
end

function var_0_0.switchState(arg_38_0, arg_38_1, arg_38_2, arg_38_3, arg_38_4)
	local var_38_0 = {}

	if arg_38_0.flag then
		table.insert(var_38_0, function(arg_39_0)
			arg_38_0.flag = false

			arg_38_0:switchUI(arg_38_1, {
				-arg_38_0.leftPanle.rect.width - 400,
				arg_38_0.rightPanel.rect.width + 400
			}, arg_39_0)
		end)
	end

	table.insert(var_38_0, function(arg_40_0)
		existCall(arg_38_3)

		return arg_40_0()
	end)

	if arg_38_2 then
		table.insert(var_38_0, function(arg_41_0)
			arg_38_0.flag = true

			if arg_38_0.isFate then
				arg_38_0:switchUI(arg_38_1, {
					-arg_38_0.leftPanle.rect.width - 400,
					0,
					-arg_38_0.leftPanle.rect.width / 2
				}, arg_41_0)
			else
				arg_38_0:switchUI(arg_38_1, {
					0,
					0,
					0
				}, arg_41_0)
			end
		end)
	end

	seriesAsync(var_38_0, arg_38_4)
end

function var_0_0.switchUI(arg_42_0, arg_42_1, arg_42_2, arg_42_3)
	LeanTween.cancel(arg_42_0.leftPanle)
	LeanTween.cancel(arg_42_0.rightPanel)
	LeanTween.cancel(arg_42_0.centerPanel)

	arg_42_0.isSwitchAnim = true

	parallelAsync({
		function(arg_43_0)
			LeanTween.moveX(arg_42_0.leftPanle, arg_42_2[1], arg_42_1):setOnComplete(System.Action(arg_43_0))
		end,
		function(arg_44_0)
			LeanTween.moveX(arg_42_0.rightPanel, arg_42_2[2], arg_42_1):setOnComplete(System.Action(arg_44_0))
		end,
		function(arg_45_0)
			if arg_42_2[3] then
				LeanTween.moveX(arg_42_0.centerPanel, arg_42_2[3], arg_42_1):setOnComplete(System.Action(arg_45_0))
			else
				arg_45_0()
			end
		end
	}, function()
		arg_42_0.isSwitchAnim = false

		return arg_42_3()
	end)
end

function var_0_0.createShipItem(arg_47_0, arg_47_1)
	local var_47_0 = {
		init = function(arg_48_0)
			arg_48_0._go = arg_47_1
			arg_48_0._tf = tf(arg_47_1)
			arg_48_0.icon = arg_48_0._tf:Find("icon")
			arg_48_0.state = arg_48_0._tf:Find("state")
			arg_48_0.count = arg_48_0._tf:Find("count")
			arg_48_0.tip = arg_48_0._tf:Find("tip")
		end,
		update = function(arg_49_0, arg_49_1, arg_49_2)
			SetCompomentEnabled(arg_49_0._tf, typeof(Toggle), arg_49_1.id > 0)

			arg_49_0.shipBluePrintVO = arg_49_1

			setActive(arg_49_0.state, arg_49_0.shipBluePrintVO.id > 0)
			setActive(arg_49_0.count, arg_49_0.shipBluePrintVO.id > 0)

			if arg_49_0.shipBluePrintVO.id > 0 then
				LoadSpriteAsync("shipdesignicon/" .. arg_49_0.shipBluePrintVO:getShipVO():getPainting(), function(arg_50_0)
					if arg_49_0.shipBluePrintVO.id > 0 and string.find(arg_50_0.name, arg_49_0.shipBluePrintVO:getShipVO():getPainting()) then
						setImageSprite(arg_49_0.icon, arg_50_0)
					end
				end)

				local var_49_0 = {
					tip = false,
					pursuing = arg_49_1:isPursuing(),
					fate = arg_49_1:canFateSimulation()
				}

				switch(arg_49_1.state, {
					[ShipBluePrint.STATE_LOCK] = function()
						var_49_0.state = "lock" .. (arg_49_1:getUnlockItem() and "_item" or "")
					end,
					[ShipBluePrint.STATE_DEV] = function()
						var_49_0.state = "research"
					end,
					[ShipBluePrint.STATE_DEV_FINISHED] = function()
						var_49_0.state = var_49_0.fate and "fate" or "dev"
						var_49_0.tip = true
					end,
					[ShipBluePrint.STATE_UNLOCK] = function()
						var_49_0.state = var_49_0.fate and "fate" or "dev"
					end
				})
				setText(arg_49_0.count, arg_49_2.count > 999 and "999+" or arg_49_2.count)
				setActive(arg_49_0.count:Find("icon"), not var_49_0.pursuing)
				setActive(arg_49_0.count:Find("icon_2"), var_49_0.pursuing)
				setText(arg_49_0.state:Find("dev/Text"), arg_49_0.shipBluePrintVO.level)

				if var_49_0.fate then
					GetImageSpriteFromAtlasAsync("ui/shipblueprintui_atlas", "icon_phase_" .. arg_49_0.shipBluePrintVO.fateLevel, arg_49_0.state:Find("fate/Image"), true)
				end

				eachChild(arg_49_0.state, function(arg_55_0)
					setActive(arg_55_0, arg_55_0.name == var_49_0.state)
				end)
				setActive(arg_49_0.tip, var_49_0.tip)
			else
				LoadSpriteAsync("shipdesignicon/empty", function(arg_56_0)
					if arg_49_0.shipBluePrintVO.id < 0 then
						setImageSprite(arg_49_0.icon, arg_56_0)
					end
				end)
				setActive(arg_49_0.tip, false)
			end
		end,
		updateSelectedStyle = function(arg_57_0, arg_57_1)
			local var_57_0 = arg_57_1 and 0 or -25

			LeanTween.cancel(arg_57_0.icon)
			LeanTween.moveY(arg_57_0.icon, var_57_0, 0.1)
		end,
		updatePursuingTip = function(arg_58_0)
			setActive(arg_58_0.count:Find("icon_2/tip"), arg_58_0.shipBluePrintVO.id > 0 and arg_58_0.shipBluePrintVO:isPursuingCostTip())
		end
	}

	var_47_0:init()
	onButton(arg_47_0, var_47_0.count:Find("icon_2"), function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("blueprint_catchup_by_gold_help")
		})
	end, SFX_PANEL)

	return var_47_0
end

function var_0_0.initShips(arg_60_0)
	arg_60_0:checkStory()
	arg_60_0:filterBlueprints()

	if not arg_60_0.itemList then
		arg_60_0.bluePrintItems = {}
		arg_60_0.itemList = UIItemList.New(arg_60_0.shipContainer, arg_60_0.shipContainer:Find("ship_tpl"))

		arg_60_0.itemList:make(function(arg_61_0, arg_61_1, arg_61_2)
			if arg_61_0 == UIItemList.EventUpdate then
				onToggle(arg_60_0, arg_61_2, function(arg_62_0)
					if arg_62_0 then
						if arg_60_0.cbTimer then
							arg_60_0.cbTimer:Stop()

							arg_60_0.cbTimer = nil
						end

						arg_60_0:clearLeanTween()

						arg_60_0.contextData.shipBluePrintVO = arg_60_0.bluePrintItems[arg_61_2].shipBluePrintVO

						if arg_60_0.nowShipId ~= arg_60_0.contextData.shipBluePrintVO.id then
							arg_60_0.nowShipId = arg_60_0.contextData.shipBluePrintVO.id

							arg_60_0:switchState(var_0_7, true, function()
								arg_60_0:setSelectedBluePrint()
							end)
						else
							arg_60_0:setSelectedBluePrint()
						end
					end

					arg_60_0.bluePrintItems[arg_61_2]:updateSelectedStyle(arg_62_0)
				end, SFX_PANEL)

				arg_60_0.bluePrintItems[arg_61_2] = arg_60_0.bluePrintItems[arg_61_2] or arg_60_0:createShipItem(arg_61_2)

				local var_61_0 = arg_60_0.filterBlueprintVOs[arg_61_1 + 1]

				if var_61_0.id > 0 then
					local var_61_1 = var_61_0:getItemId()
					local var_61_2 = arg_60_0:getItemById(var_61_1)

					arg_60_0.bluePrintItems[arg_61_2]:update(var_61_0, var_61_2)
					arg_60_0.bluePrintItems[arg_61_2]:updatePursuingTip()
				else
					arg_60_0.bluePrintItems[arg_61_2]:update(var_61_0, nil)
				end

				triggerToggle(arg_61_2, false)
			end
		end)
	end

	setActive(arg_60_0.shipContainer, false)
	arg_60_0.itemList:align(#arg_60_0.filterBlueprintVOs)
	setActive(arg_60_0.shipContainer, true)

	if not arg_60_0.contextData.shipBluePrintVO or underscore.all(arg_60_0.filterBlueprintVOs, function(arg_64_0)
		return arg_60_0.contextData.shipBluePrintVO.id ~= arg_64_0.id
	end) then
		arg_60_0.contextData.shipBluePrintVO = arg_60_0.filterBlueprintVOs[1]
	end

	eachChild(arg_60_0.shipContainer, function(arg_65_0)
		if arg_60_0.contextData.shipBluePrintVO.id == arg_60_0.bluePrintItems[arg_65_0].shipBluePrintVO.id then
			triggerToggle(arg_65_0, true)
		end
	end)
end

function var_0_0.filterBlueprints(arg_66_0)
	if arg_66_0.contextData.shipBluePrintVO then
		arg_66_0.version = arg_66_0.contextData.shipBluePrintVO:getConfig("blueprint_version")

		arg_66_0:emit(ShipBluePrintMediator.SET_TECHNOLOGY_VERSION, arg_66_0.version)
	end

	arg_66_0.filterBlueprintVOs = {}

	local var_66_0 = 0

	for iter_66_0, iter_66_1 in pairs(arg_66_0.bluePrintByIds) do
		if iter_66_1:getConfig("blueprint_version") == arg_66_0.version then
			table.insert(arg_66_0.filterBlueprintVOs, iter_66_1)

			var_66_0 = var_66_0 + 1
		end
	end

	for iter_66_2 = var_66_0, 5 do
		table.insert(arg_66_0.filterBlueprintVOs, {
			id = -1,
			state = -1
		})
	end

	table.sort(arg_66_0.filterBlueprintVOs, CompareFuncs({
		function(arg_67_0)
			return -arg_67_0.state
		end,
		function(arg_68_0)
			return arg_68_0.id
		end
	}))
end

function var_0_0.setSelectedBluePrint(arg_69_0)
	assert(arg_69_0.contextData.shipBluePrintVO, "should exist blue print")

	local var_69_0 = arg_69_0.contextData.shipBluePrintVO

	arg_69_0:updateInfo()
	arg_69_0:updatePainting()
	arg_69_0:updateProperty()

	local var_69_1 = var_69_0:isUnlock()

	setActive(arg_69_0.taskListPanel, not var_69_1)
	setActive(arg_69_0.attrDisableBtn, not var_69_1)

	if var_69_1 then
		if not var_69_0:canFateSimulation() or not pg.NewStoryMgr.GetInstance():IsPlayed(var_69_0:getConfig("luck_story")) then
			arg_69_0.isFate = false
		end

		arg_69_0:updateMod()
		setActive(arg_69_0.taskListPanel, false)
		setActive(arg_69_0.attrDisableBtn, false)
	else
		arg_69_0.isFate = false

		arg_69_0:updateTaskList()
		triggerToggle(arg_69_0.initBtn, true)
	end

	setActive(arg_69_0.fittingPanel, var_69_1 and arg_69_0.isFate)
	setActive(arg_69_0.modPanel, var_69_1 and not arg_69_0.isFate)
	setActive(arg_69_0.itemUnlockBtn, not var_69_1 and var_69_0:getUnlockItem())

	if var_69_0:isDeving() then
		arg_69_0:emit(ShipBluePrintMediator.ON_CHECK_TAKES, var_69_0.id)
	end
end

function var_0_0.updateMod(arg_70_0)
	if arg_70_0.noUpdateMod then
		return
	end

	arg_70_0:updateModPanel()
	arg_70_0:updateModAdditionPanel()
end

function var_0_0.updateModInfo(arg_71_0, arg_71_1)
	local var_71_0 = arg_71_0:getShipById(arg_71_1.shipId)
	local var_71_1 = arg_71_0.contextData.shipBluePrintVO
	local var_71_2 = intProperties(var_71_1:getShipProperties(var_71_0))
	local var_71_3 = intProperties(arg_71_1:getShipProperties(var_71_0))
	local var_71_4 = Clone(arg_71_1)

	var_71_4.level = var_71_4:getMaxLevel()

	local var_71_5 = intProperties(var_71_4:getShipProperties(var_71_0))

	local function var_71_6(arg_72_0, arg_72_1, arg_72_2, arg_72_3)
		local var_72_0 = arg_71_0:findTF("attr_bg/name", arg_72_0)
		local var_72_1 = arg_71_0:findTF("attr_bg/value", arg_72_0)
		local var_72_2 = arg_71_0:findTF("attr_bg/max", arg_72_0)
		local var_72_3 = arg_71_0:findTF("slider", arg_72_0):GetComponent(typeof(Slider))
		local var_72_4 = arg_71_0:findTF("pre_slider", arg_72_0):GetComponent(typeof(Slider))
		local var_72_5 = arg_71_0:findTF("exp", arg_72_0)

		if arg_71_1:isMaxLevel() then
			arg_72_3 = arg_72_2
		end

		setText(var_72_2, arg_72_3)
		setText(var_72_0, AttributeType.Type2Name(arg_72_1))
		setText(var_72_1, arg_72_2)

		local var_72_6, var_72_7 = var_71_1:getBluePrintAddition(arg_72_1)
		local var_72_8 = table.indexof(ShipModAttr.BLUEPRINT_ATTRS, arg_72_1)
		local var_72_9 = var_71_1:getExpRetio(var_72_8)

		var_72_3.value = var_72_7 / var_72_9

		local var_72_10, var_72_11 = arg_71_1:getBluePrintAddition(arg_72_1)
		local var_72_12 = arg_71_1:getExpRetio(var_72_8)

		setText(var_72_5, math.floor(var_72_11) .. "/" .. var_72_9)

		var_72_4.value = math.floor(var_72_10) > math.floor(var_72_6) and 1 or var_72_11 / var_72_12
	end

	local var_71_7 = 0

	for iter_71_0, iter_71_1 in pairs(var_71_3) do
		if table.contains(ShipModAttr.BLUEPRINT_ATTRS, iter_71_0) then
			local var_71_8 = arg_71_0.attrContainer:Find(iter_71_0)

			var_71_7 = var_71_7 + 1

			var_71_6(var_71_8, iter_71_0, iter_71_1, var_71_5[iter_71_0] or 0)
		end
	end

	arg_71_0.modLevel.text = arg_71_0:formatModLvTxt(arg_71_1.level, arg_71_1:getMaxLevel())

	local var_71_9 = var_71_1:getNextLevelExp()

	if var_71_9 == -1 then
		arg_71_0.levelSlider.value = 1
	else
		arg_71_0.levelSlider.value = var_71_1.exp / var_71_9
	end

	local var_71_10 = arg_71_1:getNextLevelExp()

	if var_71_10 == -1 then
		setText(arg_71_0.levelSliderTxt, "MAX")

		arg_71_0.preLevelSlider.value = 1
	else
		setText(arg_71_0.levelSliderTxt, arg_71_1.exp .. "/" .. arg_71_1:getNextLevelExp())

		arg_71_0.preLevelSlider.value = arg_71_1.level > var_71_1.level and 1 or arg_71_1.exp / var_71_10
	end

	local var_71_11, var_71_12 = arg_71_1:isShipModMaxLevel(var_71_0)

	setActive(arg_71_0.needLevelTxt, var_71_11)
	setActive(arg_71_0.levelSliderTxt, not var_71_11)

	if var_71_11 then
		setText(arg_71_0.needLevelTxt, i18n("buleprint_need_level_tip", var_71_12))

		arg_71_0.levelSlider.value = 1
	end
end

function var_0_0.inModAnim(arg_73_0)
	return arg_73_0.inAnim
end

function var_0_0.formatModLvTxt(arg_74_0, arg_74_1, arg_74_2)
	return "<size=45>" .. arg_74_1 .. "</size>/<size=27>" .. arg_74_2 .. "</size>"
end

local var_0_8 = 0.2

function var_0_0.doModAnim(arg_75_0, arg_75_1, arg_75_2)
	arg_75_0:clearLeanTween()

	arg_75_0.inAnim = true

	local var_75_0 = {}
	local var_75_1 = arg_75_2:getMaxLevel()

	if arg_75_1.level ~= var_75_1 then
		local function var_75_2(arg_76_0, arg_76_1, arg_76_2)
			arg_76_0 = Clone(arg_76_0)
			arg_76_0.level = arg_76_1
			arg_76_0.exp = arg_76_2

			return arg_76_0
		end

		arg_75_0.preLevelSlider.value = 0

		for iter_75_0 = arg_75_1.level, arg_75_2.level do
			local var_75_3 = iter_75_0 == arg_75_1.level and arg_75_1.exp / arg_75_1:getNextLevelExp() or 0
			local var_75_4 = iter_75_0 == arg_75_2.level and arg_75_2.level ~= var_75_1 and arg_75_2.exp / arg_75_2:getNextLevelExp() or 1

			table.insert(var_75_0, function(arg_77_0)
				TweenValue(go(arg_75_0.levelSlider), var_75_3, var_75_4, var_0_8, nil, function(arg_78_0)
					arg_75_0.levelSlider.value = arg_78_0
				end, function()
					local var_79_0 = iter_75_0 == arg_75_1.level and arg_75_1 or var_75_2(arg_75_1, iter_75_0, 0)
					local var_79_1 = iter_75_0 == arg_75_2.level and arg_75_2 or var_75_2(arg_75_1, iter_75_0 + 1, 0)

					arg_75_0:doAttrsAinm(var_79_0, var_79_1, arg_77_0)

					arg_75_0.modLevel.text = arg_75_0:formatModLvTxt(var_79_1.level, var_75_1)
				end)
			end)
		end

		table.insert(arg_75_0.leanTweens, arg_75_0.levelSlider)
	else
		var_75_1 = arg_75_2:getMaxFateLevel()

		local function var_75_5(arg_80_0, arg_80_1, arg_80_2)
			arg_80_0 = Clone(arg_80_0)
			arg_80_0.fateLevel = arg_80_1
			arg_80_0.exp = arg_80_2

			return arg_80_0
		end

		arg_75_0.prePhaseSlider.value = 0

		for iter_75_1 = arg_75_1.fateLevel, arg_75_2.fateLevel do
			local var_75_6 = iter_75_1 == arg_75_1.fateLevel and arg_75_1.exp / arg_75_1:getNextFateLevelExp() or 0
			local var_75_7 = iter_75_1 == arg_75_2.fateLevel and arg_75_2.fateLevel ~= var_75_1 and arg_75_2.exp / arg_75_2:getNextFateLevelExp() or 1

			table.insert(var_75_0, function(arg_81_0)
				TweenValue(go(arg_75_0.phaseSlider), var_75_6, var_75_7, var_0_8, nil, function(arg_82_0)
					arg_75_0.phaseSlider.value = arg_82_0
				end, function()
					if iter_75_1 ~= arg_75_1.fateLevel or not arg_75_1 then
						local var_83_0 = var_75_5(arg_75_1, iter_75_1, 0)
					end

					local var_83_1 = iter_75_1 == arg_75_2.fateLevel and arg_75_2 or var_75_5(arg_75_1, iter_75_1 + 1, 0)

					arg_75_0:updateFittingAttrPanel(var_83_1)
					GetImageSpriteFromAtlasAsync("ui/shipblueprintui_atlas", "phase_" .. math.min(var_83_1.fateLevel + 1, var_83_1:getMaxFateLevel()), arg_75_0.phasePic, true)
					arg_81_0()
				end)
			end)
		end

		table.insert(arg_75_0.leanTweens, arg_75_0.phaseSlider)
	end

	seriesAsync(var_75_0, function()
		arg_75_0.noUpdateMod = false

		arg_75_0:updateMod()

		arg_75_0.inAnim = false
	end)
end

function var_0_0.doAttrsAinm(arg_85_0, arg_85_1, arg_85_2, arg_85_3)
	local var_85_0 = {}
	local var_85_1 = arg_85_0:getShipById(arg_85_1.shipId)
	local var_85_2 = intProperties(arg_85_1:getShipProperties(var_85_1))
	local var_85_3 = intProperties(arg_85_2:getShipProperties(var_85_1))

	for iter_85_0, iter_85_1 in ipairs(ShipModAttr.BLUEPRINT_ATTRS) do
		if iter_85_1 ~= AttributeType.AntiAircraft then
			local var_85_4 = arg_85_0.attrContainer:Find(iter_85_1)
			local var_85_5 = arg_85_0:findTF("attr_bg/value", var_85_4):GetComponent(typeof(Text))
			local var_85_6 = arg_85_0:findTF("slider", var_85_4):GetComponent(typeof(Slider))
			local var_85_7 = arg_85_0:findTF("pre_slider", var_85_4):GetComponent(typeof(Slider))
			local var_85_8 = table.indexof(ShipModAttr.BLUEPRINT_ATTRS, iter_85_1)
			local var_85_9 = arg_85_1:getExpRetio(var_85_8)
			local var_85_10 = var_85_2[iter_85_1]
			local var_85_11 = var_85_3[iter_85_1]
			local var_85_12, var_85_13 = arg_85_1:getBluePrintAddition(iter_85_1)
			local var_85_14, var_85_15 = arg_85_2:getBluePrintAddition(iter_85_1)
			local var_85_16 = var_85_13 / var_85_9
			local var_85_17 = var_85_15 / var_85_9

			var_85_7.value = 0

			table.insert(var_85_0, function(arg_86_0)
				arg_85_0:doAttrAnim(var_85_6, var_85_5, var_85_16, var_85_17, math.floor(var_85_12), math.floor(var_85_14), var_85_10, var_85_11, arg_86_0)
			end)
		end
	end

	parallelAsync(var_85_0, arg_85_3)
end

local var_0_9 = 0.1

function var_0_0.doAttrAnim(arg_87_0, arg_87_1, arg_87_2, arg_87_3, arg_87_4, arg_87_5, arg_87_6, arg_87_7, arg_87_8, arg_87_9)
	table.insert(arg_87_0.leanTweens, arg_87_1)

	local var_87_0 = {}

	for iter_87_0 = arg_87_5, arg_87_6 do
		local var_87_1 = iter_87_0 == arg_87_5 and arg_87_3 or 0
		local var_87_2 = iter_87_0 == arg_87_6 and arg_87_4 or 1

		table.insert(var_87_0, function(arg_88_0)
			TweenValue(go(arg_87_1), var_87_1, var_87_2, var_0_9, nil, function(arg_89_0)
				arg_87_1.value = arg_89_0
			end, function()
				arg_87_2.text = arg_87_8 - math.min(arg_87_6 - iter_87_0, arg_87_8 - arg_87_7)

				arg_88_0()
			end)
		end)
	end

	seriesAsync(var_87_0, function()
		arg_87_9()
	end)
end

function var_0_0.clearLeanTween(arg_92_0, arg_92_1)
	for iter_92_0, iter_92_1 in pairs(arg_92_0.leanTweens) do
		if LeanTween.isTweening(go(iter_92_1)) then
			LeanTween.cancel(go(iter_92_1))
		end
	end

	if arg_92_0.inAnim then
		arg_92_0.inAnim = nil

		if not arg_92_1 then
			arg_92_0.noUpdateMod = false
		end
	end

	arg_92_0.leanTweens = {}
end

function var_0_0.updateModPanel(arg_93_0)
	local var_93_0 = arg_93_0.contextData.shipBluePrintVO
	local var_93_1 = arg_93_0:getShipById(var_93_0.shipId)
	local var_93_2 = var_93_0:getConfig("strengthen_item")
	local var_93_3 = arg_93_0:getItemById(var_93_2)
	local var_93_4 = var_93_3.count == 0 and var_93_0:isPursuing()
	local var_93_5 = 0
	local var_93_6
	local var_93_7

	if var_93_4 then
		local var_93_8 = getProxy(TechnologyProxy)

		var_93_6 = math.min(var_93_8:calcMaxPursuingCount(var_93_0), var_93_0:getUseageMaxItem())

		function var_93_7(arg_94_0)
			local var_94_0 = arg_94_0 * var_93_0:getItemExp()
			local var_94_1 = Clone(var_93_0)

			var_94_1:addExp(var_94_0)
			arg_93_0:updateModInfo(var_94_1)
			setText(arg_93_0.calcTxt, arg_94_0)

			local var_94_2 = var_93_0:isRarityUR()
			local var_94_3 = TechnologyProxy.getPursuingDiscount(var_93_8:getPursuingTimes(var_94_2) + var_93_5 + 1, var_94_2)

			setText(arg_93_0.itemInfoIcon:Find("icon_bg/count"), var_93_0:getPursuingPrice(var_94_3))
			setActive(arg_93_0.itemInfo:Find("no_cost"), var_94_3 == 0)
			setActive(arg_93_0.itemInfo:Find("discount"), var_94_3 > 0 and var_94_3 < 100)

			if var_94_3 > 0 and var_94_3 < 100 then
				setText(arg_93_0.itemInfo:Find("discount/Text"), 100 - var_94_3 .. "%OFF")
			end

			setActive(arg_93_0.modBtn:Find("pursuing_cost"), var_93_5 > 0)
			setText(arg_93_0.modBtn:Find("pursuing_cost/Text"), var_93_8:calcPursuingCost(var_93_0, arg_94_0))
		end

		local var_93_9 = {
			type = DROP_TYPE_RESOURCE,
			id = PlayerConst.ResGold
		}

		updateDrop(arg_93_0.itemInfoIcon, var_93_9)
		onButton(arg_93_0, arg_93_0.itemInfoIcon, function()
			if LOCK_TECHNOLOGY_PURSUING_TIP then
				arg_93_0:emit(BaseUI.ON_DROP, var_93_9)
			else
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					type = MSGBOX_TYPE_HELP,
					helps = i18n("blueprint_catchup_by_gold_help")
				})
			end
		end, SFX_PANEL)
		setScrollText(findTF(arg_93_0.itemInfo, "name/Text"), var_93_9:getConfig("name"))
		setText(arg_93_0.itemInfoCount, i18n("tec_tip_material_stock") .. ":" .. getProxy(PlayerProxy):getRawData():getResource(PlayerConst.ResGold))
		setText(arg_93_0.itemInfo:Find("no_cost/Text"), i18n("tec_tip_no_consumption"))
		setText(arg_93_0.modBtn:Find("pursuing_cost/word"), i18n("tec_tip_to_consumption"))
		onButton(arg_93_0, arg_93_0.modBtn, function()
			if arg_93_0:inModAnim() then
				return
			end

			if var_93_5 == 0 then
				return
			end

			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("blueprint_catchup_by_gold_confirm", var_93_8:calcPursuingCost(var_93_0, var_93_5)),
				onYes = function()
					arg_93_0:emit(ShipBluePrintMediator.ON_PURSUING, var_93_0.id, var_93_5)
				end
			})
		end, SFX_PANEL)
	else
		var_93_6 = math.min(var_93_3.count, var_93_0:getUseageMaxItem())

		function var_93_7(arg_98_0)
			local var_98_0 = arg_98_0 * var_93_0:getItemExp()
			local var_98_1 = Clone(var_93_0)

			var_98_1:addExp(var_98_0)
			arg_93_0:updateModInfo(var_98_1)
			setText(arg_93_0.calcTxt, arg_98_0)
		end

		updateDrop(arg_93_0.itemInfoIcon, {
			type = DROP_TYPE_ITEM,
			id = var_93_3.id
		})
		onButton(arg_93_0, arg_93_0.itemInfoIcon, function()
			ItemTipPanel.ShowItemTipbyID(var_93_3.id, i18n("title_item_ways", var_93_3:getConfig("name")))
		end, SFX_PANEL)
		setScrollText(findTF(arg_93_0.itemInfo, "name/Text"), var_93_3:getConfig("name"))
		setText(arg_93_0.itemInfoCount, i18n("tec_tip_material_stock") .. ":" .. var_93_3.count)
		setActive(arg_93_0.itemInfo:Find("no_cost"), false)
		setActive(arg_93_0.itemInfo:Find("discount"), false)
		setActive(arg_93_0.modBtn:Find("pursuing_cost"), false)
		onButton(arg_93_0, arg_93_0.modBtn, function()
			if arg_93_0:inModAnim() then
				return
			end

			if var_93_5 == 0 then
				return
			end

			arg_93_0:emit(ShipBluePrintMediator.ON_MOD, var_93_0.id, var_93_5)
		end, SFX_PANEL)
	end

	var_93_7(var_93_5)

	local var_93_10 = 0
	local var_93_11 = Clone(var_93_0)
	local var_93_12 = var_93_0:getItemExp()

	while var_93_11.level < var_93_11:getMaxLevel() and var_93_1.level >= var_93_11:getStrengthenConfig(math.min(var_93_11.level + 1, var_93_11:getMaxLevel())).need_lv do
		var_93_10 = var_93_10 + 1

		var_93_11:addExp(var_93_12)
	end

	local var_93_13 = math.min(var_93_6, var_93_10)

	pressPersistTrigger(arg_93_0.calcMinusBtn, 0.5, function()
		if arg_93_0:inModAnim() or var_93_0:isMaxLevel() or var_93_5 == 0 then
			return
		end

		var_93_5 = var_93_5 - 1

		var_93_7(var_93_5)
	end, nil, true, true, 0.1, SFX_PANEL)
	pressPersistTrigger(arg_93_0.calcPlusBtn, 0.5, function()
		if arg_93_0:inModAnim() or var_93_0:isMaxLevel() or var_93_5 == var_93_13 then
			return
		end

		var_93_5 = var_93_5 + 1

		var_93_7(var_93_5)
	end, nil, true, true, 0.1, SFX_PANEL)
	onButton(arg_93_0, arg_93_0.calcMaxBtn, function()
		if arg_93_0:inModAnim() or var_93_0:isMaxLevel() or var_93_5 == var_93_13 then
			return
		end

		var_93_5 = var_93_13

		var_93_7(var_93_5)
	end, SFX_PANEL)
	setActive(arg_93_0.calcMaxBtn, not var_93_4)

	local var_93_14 = var_93_0:canFateSimulation()

	if var_93_14 then
		onButton(arg_93_0, arg_93_0.fittingBtn, function()
			if arg_93_0.isSwitchAnim then
				return
			end

			setActive(arg_93_0.fittingBtnEffect, true)

			arg_93_0.cbTimer = Timer.New(function()
				arg_93_0.cbTimer = nil

				setActive(arg_93_0.fittingBtnEffect, false)
				arg_93_0:switchState(var_0_7, true, function()
					arg_93_0.isFate = true

					setActive(arg_93_0.fittingPanel, arg_93_0.isFate)
					setActive(arg_93_0.modPanel, not arg_93_0.isFate)

					if not PlayerPrefs.HasKey("first_fate") then
						triggerButton(arg_93_0.helpBtn)
						PlayerPrefs.SetInt("first_fate", 1)
						PlayerPrefs.Save()
					end
				end)
			end, 0.6)

			arg_93_0.cbTimer:Start()
		end, SFX_PANEL)
		arg_93_0:updateFittingPanel()
		pg.NewStoryMgr.GetInstance():Play(var_93_0:getConfig("luck_story"), function(arg_107_0)
			if arg_107_0 then
				arg_93_0:buildStartAni("fateStartWindow", function()
					triggerButton(arg_93_0.fittingBtn)
				end)
			end
		end)
	end

	setActive(arg_93_0.calcPanel, not var_93_14)
	setActive(arg_93_0.fittingBtn, var_93_14)
	setActive(arg_93_0.fittingBtnEffect, false)
end

function var_0_0.updateFittingPanel(arg_109_0)
	local var_109_0 = arg_109_0.contextData.shipBluePrintVO
	local var_109_1 = arg_109_0:getShipById(var_109_0.shipId)
	local var_109_2 = var_109_0:getConfig("strengthen_item")
	local var_109_3 = arg_109_0:getItemById(var_109_2)
	local var_109_4 = var_109_3.count == 0 and var_109_0:isPursuing()
	local var_109_5 = 0
	local var_109_6
	local var_109_7

	if var_109_4 then
		local var_109_8 = getProxy(TechnologyProxy)

		var_109_6 = math.min(var_109_8:calcMaxPursuingCount(var_109_0), var_109_0:getFateUseageMaxItem())

		function var_109_7(arg_110_0)
			local var_110_0 = arg_110_0 * var_109_0:getItemExp()
			local var_110_1 = Clone(var_109_0)

			var_110_1:addExp(var_110_0)
			arg_109_0:updateFittingInfo(var_110_1)
			setText(arg_109_0.fittingCalcTxt, arg_110_0)

			local var_110_2 = var_109_0:isRarityUR()
			local var_110_3 = TechnologyProxy.getPursuingDiscount(var_109_8:getPursuingTimes(var_110_2) + var_109_5 + 1, var_110_2)

			setText(arg_109_0.fittingItemInfoIcon:Find("icon_bg/count"), var_109_0:getPursuingPrice(var_110_3))
			setActive(arg_109_0.fittingItemInfo:Find("no_cost"), var_110_3 == 0)
			setActive(arg_109_0.fittingItemInfo:Find("discount"), var_110_3 > 0 and var_110_3 < 100)

			if var_110_3 > 0 and var_110_3 < 100 then
				setText(arg_109_0.fittingItemInfo:Find("discount/Text"), 100 - var_110_3 .. "%OFF")
			end

			setActive(arg_109_0.fittingConfirmBtn:Find("pursuing_cost"), arg_110_0 > 0)
			setText(arg_109_0.fittingConfirmBtn:Find("pursuing_cost/Text"), var_109_8:calcPursuingCost(var_109_0, arg_110_0))
		end

		local var_109_9 = {
			type = DROP_TYPE_RESOURCE,
			id = PlayerConst.ResGold
		}

		updateDrop(arg_109_0.fittingItemInfoIcon, var_109_9)
		onButton(arg_109_0, arg_109_0.fittingItemInfoIcon, function()
			if LOCK_TECHNOLOGY_PURSUING_TIP then
				arg_109_0:emit(BaseUI.ON_DROP, var_109_9)
			else
				pg.MsgboxMgr.GetInstance():ShowMsgBox({
					type = MSGBOX_TYPE_HELP,
					helps = i18n("blueprint_catchup_by_gold_help")
				})
			end
		end, SFX_PANEL)
		setScrollText(findTF(arg_109_0.fittingItemInfo, "name/Text"), var_109_9:getConfig("name"))
		setText(arg_109_0.fittingItemInfoCount, i18n("tec_tip_material_stock") .. ":" .. getProxy(PlayerProxy):getRawData():getResource(PlayerConst.ResGold))
		setText(arg_109_0.fittingItemInfo:Find("no_cost/Text"), i18n("tec_tip_no_consumption"))
		setText(arg_109_0.fittingConfirmBtn:Find("pursuing_cost/word"), i18n("tec_tip_to_consumption"))
		onButton(arg_109_0, arg_109_0.fittingConfirmBtn, function()
			if arg_109_0:inModAnim() then
				return
			end

			if var_109_5 == 0 then
				return
			end

			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("blueprint_catchup_by_gold_confirm", var_109_8:calcPursuingCost(var_109_0, var_109_5)),
				onYes = function()
					arg_109_0:emit(ShipBluePrintMediator.ON_PURSUING, var_109_0.id, var_109_5)
				end
			})
		end, SFX_PANEL)
	else
		var_109_6 = math.min(var_109_3.count, var_109_0:getFateUseageMaxItem())

		function var_109_7(arg_114_0)
			local var_114_0 = arg_114_0 * var_109_0:getItemExp()
			local var_114_1 = Clone(var_109_0)

			var_114_1:addExp(var_114_0)
			arg_109_0:updateFittingInfo(var_114_1)
			setText(arg_109_0.fittingCalcTxt, arg_114_0)
		end

		updateDrop(arg_109_0.fittingItemInfoIcon, {
			type = DROP_TYPE_ITEM,
			id = var_109_3.id
		})
		onButton(arg_109_0, arg_109_0.fittingItemInfoIcon, function()
			ItemTipPanel.ShowItemTipbyID(var_109_3.id, i18n("title_item_ways", var_109_3:getConfig("name")))
		end, SFX_PANEL)
		setScrollText(arg_109_0.fittingItemInfo:Find("name/Text"), var_109_3:getConfig("name"))
		setText(arg_109_0.fittingItemInfoCount, i18n("tec_tip_material_stock") .. ":" .. var_109_3.count)
		setActive(arg_109_0.fittingItemInfo:Find("no_cost"), false)
		setActive(arg_109_0.fittingItemInfo:Find("discount"), false)
		setActive(arg_109_0.fittingConfirmBtn:Find("pursuing_cost"), false)
		onButton(arg_109_0, arg_109_0.fittingConfirmBtn, function()
			if arg_109_0:inModAnim() then
				return
			end

			if var_109_5 == 0 then
				return
			end

			arg_109_0:emit(ShipBluePrintMediator.ON_MOD, var_109_0.id, var_109_5)
		end, SFX_PANEL)
	end

	setText(arg_109_0.fittingAttrPanel:Find("attr/name"), AttributeType.Type2Name(AttributeType.Luck))
	setText(arg_109_0.fittingPanel:Find("desc/top/text/Text"), i18n("fate_phase_word"))
	onButton(arg_109_0, arg_109_0.fittingCancelBtn, function()
		arg_109_0:switchState(var_0_7, true, function()
			arg_109_0.isFate = false

			setActive(arg_109_0.fittingPanel, arg_109_0.isFate)
			setActive(arg_109_0.modPanel, not arg_109_0.isFate)
		end)
	end, SFX_PANEL)

	local var_109_10 = 0
	local var_109_11 = Clone(var_109_0)
	local var_109_12 = var_109_0:getItemExp()

	while var_109_11.fateLevel < var_109_11:getMaxFateLevel() and var_109_1.level >= var_109_11:getFateStrengthenConfig(math.min(var_109_11.fateLevel + 1, var_109_11:getMaxFateLevel())).need_lv do
		var_109_10 = var_109_10 + 1

		var_109_11:addExp(var_109_12)
	end

	local var_109_13 = math.min(var_109_6, var_109_10)

	pressPersistTrigger(arg_109_0.fittingCalcMinusBtn, 0.5, function()
		if arg_109_0:inModAnim() or var_109_0:isMaxFateLevel() or var_109_5 == 0 then
			return
		end

		var_109_5 = math.max(var_109_5 - 1, 0)

		var_109_7(var_109_5)
	end, nil, true, true, 0.1, SFX_PANEL)
	pressPersistTrigger(arg_109_0.fittingCalcPlusBtn, 0.5, function()
		if arg_109_0:inModAnim() or var_109_0:isMaxFateLevel() or var_109_5 == var_109_13 then
			return
		end

		var_109_5 = math.max(math.min(var_109_5 + 1, var_109_13), 0)

		var_109_7(var_109_5)
	end, nil, true, true, 0.1, SFX_PANEL)
	onButton(arg_109_0, arg_109_0.fittingCalcMaxBtn, function()
		if arg_109_0:inModAnim() or var_109_0:isMaxFateLevel() or var_109_5 == var_109_13 then
			return
		end

		var_109_5 = var_109_13

		var_109_7(var_109_5)
	end, SFX_PANEL)
	setActive(arg_109_0.fittingCalcMaxBtn, not var_109_4)

	local var_109_14 = arg_109_0.fittingAttrPanel:Find("phase_panel")
	local var_109_15 = var_109_14:Find("phase_tpl")

	setActive(var_109_15, false)

	local var_109_16 = {
		0,
		-60,
		0,
		60
	}
	local var_109_17 = {}

	for iter_109_0 = 1, var_109_0:getMaxFateLevel() do
		local var_109_18 = var_109_14:Find("phase_" .. iter_109_0) or cloneTplTo(var_109_15, var_109_14, "phase_" .. iter_109_0)
		local var_109_19 = var_109_0:getFateStrengthenConfig(iter_109_0)

		assert(var_109_19.special == 1 and type(var_109_19.special_effect) == "table", "without fate config")

		local var_109_20 = var_109_19.special_effect
		local var_109_21

		for iter_109_1, iter_109_2 in ipairs(var_109_20) do
			if iter_109_2[1] == ShipBluePrint.STRENGTHEN_TYPE_CHANGE_SKILL then
				var_109_21 = iter_109_2[2][2]

				break
			end
		end

		for iter_109_3, iter_109_4 in ipairs({
			"off",
			"on"
		}) do
			setActive(var_109_18:Find(iter_109_4 .. "/icon"), not var_109_21)
			setActive(var_109_18:Find(iter_109_4 .. "/skill"), var_109_21)
			setActive(var_109_18:Find(iter_109_4 .. "/icon/line"), var_109_16[iter_109_0])
			setActive(var_109_18:Find(iter_109_4 .. "/skill/line"), var_109_16[iter_109_0])

			if var_109_16[iter_109_0] then
				var_109_18:Find(iter_109_4 .. "/icon/line").localEulerAngles = Vector3(0, 0, var_109_16[iter_109_0])
				var_109_18:Find(iter_109_4 .. "/skill/line").localEulerAngles = Vector3(0, 0, var_109_16[iter_109_0])

				GetImageSpriteFromAtlasAsync("ui/shipblueprintui_atlas", iter_109_0 .. "_" .. iter_109_4, var_109_18:Find(iter_109_4 .. "/icon/icon"), true)
			end
		end

		if var_109_21 then
			GetImageSpriteFromAtlasAsync("tecfateskillicon/skill_" .. var_109_21, "", var_109_18:Find("off/skill/icon"), true)
			GetImageSpriteFromAtlasAsync("tecfateskillicon/skill_on_" .. var_109_21, "", var_109_18:Find("on/skill/icon"), true)

			var_109_17[iter_109_0] = 55
		else
			var_109_17[iter_109_0] = 40
		end

		onButton(arg_109_0, var_109_18, function()
			arg_109_0:showFittingMsgPanel(iter_109_0)
		end, SFX_PANEL)
	end

	local var_109_22 = Vector2.zero
	local var_109_23 = Vector2.zero
	local var_109_24 = Vector2.zero

	for iter_109_5 = 1, var_109_0:getMaxFateLevel() do
		local var_109_25 = var_109_14:Find("phase_" .. iter_109_5)

		setAnchoredPosition(var_109_25, var_109_22)

		var_109_23.x = math.min(var_109_23.x, var_109_22.x)
		var_109_23.y = math.min(var_109_23.y, var_109_22.y)
		var_109_24.x = math.max(var_109_24.x, var_109_22.x)
		var_109_24.y = math.max(var_109_24.y, var_109_22.y)

		if var_109_16[iter_109_5] then
			var_109_22 = var_109_22 + (var_109_17[iter_109_5] + var_109_17[iter_109_5 + 1]) * Vector2(math.cos(math.pi * var_109_16[iter_109_5] / 180), math.sin(math.pi * var_109_16[iter_109_5] / 180))
		end
	end

	setSizeDelta(var_109_14, var_109_24 - var_109_23)
	setAnchoredPosition(var_109_14, {
		y = -var_109_24.y
	})
	var_109_7(var_109_5)
end

function var_0_0.updateFittingInfo(arg_123_0, arg_123_1)
	local var_123_0 = arg_123_0:getShipById(arg_123_1.shipId)
	local var_123_1 = arg_123_0.contextData.shipBluePrintVO

	arg_123_0:updateFittingAttrPanel(var_123_1, arg_123_1)
	GetImageSpriteFromAtlasAsync("ui/shipblueprintui_atlas", "phase_" .. math.max(arg_123_1.fateLevel, 1), arg_123_0.phasePic, true)

	local var_123_2 = var_123_1:getNextFateLevelExp()

	if var_123_2 == -1 then
		arg_123_0.phaseSlider.value = 1
	else
		arg_123_0.phaseSlider.value = var_123_1.exp / var_123_2
	end

	local var_123_3 = arg_123_1:getNextFateLevelExp()

	if var_123_3 == -1 then
		setText(arg_123_0.phaseSliderTxt, "MAX")

		arg_123_0.prePhaseSlider.value = 1
	else
		local var_123_4 = math.floor(arg_123_1.exp / arg_123_1:getNextFateLevelExp() * 100)

		setText(arg_123_0.phaseSliderTxt, tostring(var_123_4) .. "%")

		arg_123_0.prePhaseSlider.value = arg_123_1.fateLevel > var_123_1.fateLevel and 1 or arg_123_1.exp / var_123_3
	end

	local var_123_5, var_123_6 = arg_123_1:isShipModMaxFateLevel(var_123_0)

	setActive(arg_123_0.fittingNeedMask, var_123_5)

	if var_123_5 then
		setText(arg_123_0:findTF("limit", arg_123_0.fittingNeedMask), i18n("buleprint_need_level_tip", var_123_6))

		arg_123_0.phaseSlider.value = 1
	end
end

function var_0_0.updateFittingAttrPanel(arg_124_0, arg_124_1, arg_124_2)
	setText(arg_124_0:findTF("attr/name/Text", arg_124_0.fittingAttrPanel), " + " .. defaultValue((arg_124_2 or arg_124_1):attrSpecialAddition()[AttributeType.Luck], 0))

	arg_124_0.blinkTarget = arg_124_0.blinkTarget or {
		{},
		{}
	}

	for iter_124_0 = 1, arg_124_1:getMaxFateLevel() do
		local var_124_0 = arg_124_0:findTF("phase_panel/phase_" .. iter_124_0, arg_124_0.fittingAttrPanel)
		local var_124_1 = arg_124_0:findTF("off", var_124_0)
		local var_124_2 = arg_124_0:findTF("on", var_124_0)

		if arg_124_2 and iter_124_0 > arg_124_1.fateLevel and iter_124_0 <= arg_124_2.fateLevel then
			setActive(var_124_1, true)
			setActive(var_124_2, true)

			if not table.contains(arg_124_0.blinkTarget[1], var_124_1) then
				table.insert(arg_124_0.blinkTarget[1], var_124_1)
				table.insert(arg_124_0.blinkTarget[2], var_124_2)
			end
		else
			local var_124_3 = table.indexof(arg_124_0.blinkTarget[1], var_124_1)

			if var_124_3 then
				table.remove(arg_124_0.blinkTarget[1], var_124_3)
				table.remove(arg_124_0.blinkTarget[2], var_124_3)
			end

			setActive(var_124_1, iter_124_0 > arg_124_1.fateLevel)
			setActive(var_124_2, iter_124_0 <= arg_124_1.fateLevel)

			var_124_1:GetComponent(typeof(CanvasGroup)).alpha = 1
			var_124_2:GetComponent(typeof(CanvasGroup)).alpha = 1
		end
	end

	if #arg_124_0.blinkTarget[1] == 0 then
		LeanTween.cancel(go(arg_124_0.fittingAttrPanel))
	elseif not LeanTween.isTweening(go(arg_124_0.fittingAttrPanel)) then
		LeanTween.value(go(arg_124_0.fittingAttrPanel), 1, 0, 0.8):setOnUpdate(System.Action_float(function(arg_125_0)
			for iter_125_0, iter_125_1 in ipairs(arg_124_0.blinkTarget[1]) do
				iter_125_1:GetComponent(typeof(CanvasGroup)).alpha = arg_125_0
			end

			for iter_125_2, iter_125_3 in ipairs(arg_124_0.blinkTarget[2]) do
				iter_125_3:GetComponent(typeof(CanvasGroup)).alpha = 1 - arg_125_0
			end
		end)):setEase(LeanTweenType.easeInOutSine):setLoopPingPong(0)
	end
end

function var_0_0.updateModAdditionPanel(arg_126_0)
	local var_126_0 = arg_126_0.contextData.shipBluePrintVO
	local var_126_1 = var_126_0:specialStrengthens()

	for iter_126_0 = arg_126_0.modAdditionContainer.childCount - 1, #var_126_1 do
		arg_126_0:cloneTplTo(arg_126_0.modAdditionTpl, arg_126_0.modAdditionContainer)
	end

	local var_126_2 = arg_126_0.modAdditionContainer.childCount

	for iter_126_1 = 1, var_126_2 do
		local var_126_3 = iter_126_1 <= #var_126_1
		local var_126_4 = arg_126_0.modAdditionContainer:GetChild(iter_126_1 - 1)

		setActive(var_126_4, var_126_3)

		if var_126_3 then
			arg_126_0:updateAdvanceTF(var_126_0, var_126_4, var_126_1[iter_126_1])
		end
	end
end

function var_0_0.updateAdvanceTF(arg_127_0, arg_127_1, arg_127_2, arg_127_3)
	local var_127_0 = arg_127_1.level < arg_127_3.level

	setActive(arg_127_2:Find("mask"), var_127_0)

	if var_127_0 then
		setText(arg_127_2:Find("mask/content/Text"), i18n("blueprint_mod_addition_lock", arg_127_3.level))
	end

	local var_127_1 = arg_127_3.des
	local var_127_2 = arg_127_3.extraDes or {}
	local var_127_3 = arg_127_2:Find("additions")

	removeAllChildren(var_127_3)

	local var_127_4 = arg_127_0:findTF("scroll_rect/info", arg_127_0.modAdditionPanel)

	local function var_127_5(arg_128_0, arg_128_1)
		local var_128_0 = arg_128_1[2]
		local var_128_1 = pg.ship_data_breakout[var_128_0].pre_id
		local var_128_2 = Ship.New({
			configId = var_128_0
		})
		local var_128_3 = Ship.New({
			configId = var_128_1
		}):getStar()
		local var_128_4 = var_128_2:getStar()
		local var_128_5 = arg_128_0:Find("star_tpl")
		local var_128_6 = arg_128_0:Find("stars")
		local var_128_7 = arg_128_0:Find("pre_stars")

		removeAllChildren(var_128_6)
		removeAllChildren(var_128_7)

		for iter_128_0 = 1, var_128_3 do
			cloneTplTo(var_128_5, var_128_6)
		end

		for iter_128_1 = 1, var_128_4 do
			cloneTplTo(var_128_5, var_128_7)
		end
	end

	for iter_127_0 = 1, #var_127_1 do
		local var_127_6 = cloneTplTo(var_127_4, var_127_3)
		local var_127_7 = var_127_6:Find("text_tpl")
		local var_127_8 = var_127_6:Find("breakout_tpl")

		setActive(var_127_7, false)
		setActive(var_127_6:Find("attr_tpl"), false)
		setActive(var_127_8, false)
		setActive(var_127_6:Find("empty_tpl"), false)

		if var_127_1[iter_127_0] then
			if var_127_1[iter_127_0][1] == ShipBluePrint.STRENGTHEN_TYPE_BREAKOUT then
				setActive(var_127_8, true)
				var_127_5(var_127_8, var_127_1[iter_127_0])
			else
				setActive(var_127_7, true)
				setScrollText(var_127_7:Find("Text"), var_127_1[iter_127_0][3])
			end
		end
	end

	for iter_127_1 = 1, #var_127_2 do
		local var_127_9 = cloneTplTo(var_127_4, var_127_3)
		local var_127_10 = var_127_9:Find("text_tpl")

		setActive(var_127_10, true)
		setActive(var_127_9:Find("attr_tpl"), false)
		setActive(var_127_9:Find("breakout_tpl"), false)
		setActive(var_127_9:Find("empty_tpl"), false)
		setScrollText(var_127_10:Find("Text"), var_127_2[iter_127_1])
	end
end

function var_0_0.updateInfo(arg_129_0)
	local var_129_0 = arg_129_0.contextData.shipBluePrintVO
	local var_129_1

	if var_129_0:isFetched() then
		var_129_1 = arg_129_0.shipVOs[var_129_0.shipId]
	end

	var_129_1 = var_129_1 or var_129_0:getShipVO()

	local var_129_2 = var_129_1:getConfigTable()
	local var_129_3 = var_129_1:getName()

	setText(arg_129_0.shipName, var_129_3)
	setText(arg_129_0.englishName, var_129_2.english_name)
	removeAllChildren(arg_129_0.stars)

	local var_129_4 = var_129_1:getStar()
	local var_129_5 = var_129_1:getMaxStar()

	for iter_129_0 = 1, var_129_5 do
		cloneTplTo(arg_129_0.shipInfoStarTpl, arg_129_0.stars, "star_" .. iter_129_0)
	end

	local var_129_6 = var_129_5 - var_129_4

	for iter_129_1 = 1, var_129_6 do
		local var_129_7 = arg_129_0.stars:GetChild(var_129_5 - iter_129_1)

		setActive(var_129_7:Find("star_tpl"), false)
		setActive(var_129_7:Find("empty_star_tpl"), true)
	end

	local var_129_8 = GetSpriteFromAtlas("shiptype", var_129_1:getShipType())

	if not var_129_8 then
		warning("找不到船形, shipConfigId: " .. var_129_1.configId)
	end

	setImageSprite(arg_129_0.shipType, var_129_8, true)

	local var_129_9 = var_129_0:isLock()

	setActive(arg_129_0.finishedBtn, var_129_0:isFinished())

	local var_129_10 = var_129_0:isDeving()

	setActive(arg_129_0.progressPanel, var_129_10)

	if not var_129_10 then
		setActive(arg_129_0.speedupBtn, false)
	end

	if var_129_10 then
		arg_129_0:updateTasksProgress()
	end

	local var_129_11, var_129_12 = var_129_0:isFinishPrevTask()

	if var_129_9 and not var_129_12 then
		if var_129_11 then
			for iter_129_2, iter_129_3 in ipairs(var_129_0:getOpenTaskList()) do
				arg_129_0:emit(ShipBluePrintMediator.ON_FINISH_TASK, iter_129_3)
			end

			var_129_12 = true
		else
			local var_129_13 = getProxy(TaskProxy)
			local var_129_14 = var_129_0:getOpenTaskList()

			for iter_129_4, iter_129_5 in ipairs(var_129_14) do
				local var_129_15 = var_129_13:getTaskVO(iter_129_5)
				local var_129_16 = iter_129_4 > arg_129_0.lockPanel.childCount and cloneTplTo(arg_129_0.lockBtn, arg_129_0.lockPanel) or arg_129_0.lockPanel:GetChild(iter_129_4 - 1)

				setActive(var_129_16, true)

				local var_129_17 = var_129_15:getProgress()
				local var_129_18 = var_129_15:getConfig("target_num")

				setText(arg_129_0:findTF("Text", var_129_16), (var_129_18 <= var_129_17 and setColorStr(var_129_17, COLOR_GREEN) or var_129_17) .. "/" .. var_129_18)
			end

			for iter_129_6 = #var_129_14 + 1, arg_129_0.lockPanel.childCount do
				setActive(arg_129_0.lockPanel:GetChild(iter_129_6 - 1), false)
			end
		end
	end

	setText(arg_129_0:findTF("Text", arg_129_0.openCondition), var_129_0:getConfig("unlock_word"))
	setActive(arg_129_0.openCondition, var_129_9)
	setActive(arg_129_0.startBtn, var_129_9 and var_129_12)
	setActive(arg_129_0.lockPanel, var_129_9 and not var_129_12)
end

function var_0_0.updateTasksProgress(arg_130_0)
	local var_130_0 = arg_130_0.contextData.shipBluePrintVO
	local var_130_1 = var_130_0:getTaskIds()

	for iter_130_0 = arg_130_0.progressContainer.childCount, #var_130_1 do
		cloneTplTo(arg_130_0.progressTpl, arg_130_0.progressContainer)
	end

	local var_130_2 = arg_130_0.progressContainer.childCount

	for iter_130_1 = 1, var_130_2 do
		local var_130_3 = arg_130_0.progressContainer:GetChild(iter_130_1 - 1)
		local var_130_4 = iter_130_1 <= #var_130_1

		setActive(var_130_3, var_130_4)

		if var_130_4 then
			local var_130_5 = var_130_0:getTaskStateById(var_130_1[iter_130_1])

			setActive(findTF(var_130_3, "complete"), var_130_5 == ShipBluePrint.TASK_STATE_FINISHED)
			setActive(findTF(var_130_3, "lock"), var_130_5 == ShipBluePrint.TASK_STATE_LOCK or var_130_5 == ShipBluePrint.TASK_STATE_WAIT)
			setActive(findTF(var_130_3, "working"), var_130_5 == ShipBluePrint.TASK_STATE_ACHIEVED or var_130_5 == ShipBluePrint.TASK_STATE_OPENING or var_130_5 == ShipBluePrint.TASK_STATE_START)
		end
	end

	local var_130_6 = var_130_0:getConfig("blueprint_version")
	local var_130_7 = pg.gameset.technology_catchup_itemid.description[var_130_6]

	if var_130_7 then
		local var_130_8 = var_130_0:getTaskStateById(var_130_1[1])
		local var_130_9 = var_130_0:getTaskStateById(var_130_1[4])
		local var_130_10 = var_130_7[1]
		local var_130_11 = getProxy(BagProxy):getItemCountById(var_130_10)

		setActive(arg_130_0.speedupBtn, (var_130_8 == ShipBluePrint.TASK_STATE_START or var_130_9 == ShipBluePrint.TASK_STATE_START) and var_130_11 > 0)
	else
		setActive(arg_130_0.speedupBtn, false)
	end
end

function var_0_0.updatePainting(arg_131_0)
	local var_131_0 = arg_131_0.contextData.shipBluePrintVO:getShipVO()

	if arg_131_0.lastPaintingName and arg_131_0.lastPaintingName ~= var_131_0:getPainting() then
		retPaintingPrefab(arg_131_0.painting, arg_131_0.lastPaintingName)
	end

	local var_131_1 = var_131_0:getPainting()

	setPaintingPrefab(arg_131_0.painting, var_131_1, "tuzhi")

	arg_131_0.lastPaintingName = var_131_1

	arg_131_0:paintBreath()
end

function var_0_0.updateProperty(arg_132_0)
	local var_132_0 = arg_132_0.contextData.shipBluePrintVO
	local var_132_1 = var_132_0:getShipVO()

	arg_132_0.propertyPanel:initProperty(var_132_1.configId, PropertyPanel.TypeFlat)

	local var_132_2 = var_0_2[var_132_1.configId].buff_list_display

	for iter_132_0 = arg_132_0.skillPanel.childCount, #var_132_2 - 1 do
		cloneTplTo(arg_132_0.skillTpl, arg_132_0.skillPanel)
	end

	local var_132_3 = arg_132_0.skillPanel.childCount

	for iter_132_1 = 1, var_132_3 do
		local var_132_4 = arg_132_0.skillPanel:GetChild(iter_132_1 - 1)
		local var_132_5 = iter_132_1 <= #var_132_2
		local var_132_6 = findTF(var_132_4, "icon")

		if var_132_5 then
			local var_132_7 = var_132_2[iter_132_1]
			local var_132_8 = getSkillConfig(var_132_7)

			LoadImageSpriteAsync("skillicon/" .. var_132_8.icon, var_132_6)
			onButton(arg_132_0, var_132_4, function()
				arg_132_0:emit(ShipBluePrintMediator.SHOW_SKILL_INFO, var_132_8.id, {
					id = var_132_8.id,
					level = pg.skill_data_template[var_132_8.id].max_level
				}, function()
					return
				end)
			end, SFX_PANEL)
		end

		setActive(var_132_4, var_132_5)
	end

	setActive(arg_132_0.skillArrLeft, #var_132_2 > 3)
	setActive(arg_132_0.skillArrRight, #var_132_2 > 3)

	if #var_132_2 > 3 then
		onScroll(arg_132_0, arg_132_0.skillRect, function(arg_135_0)
			setActive(arg_132_0.skillArrLeft, arg_135_0.x > 0.01)
			setActive(arg_132_0.skillArrRight, arg_135_0.x < 0.99)
		end)
	else
		GetComponent(arg_132_0.skillRect, typeof(ScrollRect)).onValueChanged:RemoveAllListeners()
	end

	setAnchoredPosition(arg_132_0.skillPanel, {
		x = 0
	})

	local var_132_9 = var_132_0:getConfig("simulate_dungeon")

	setActive(arg_132_0.simulationBtn, var_132_9 ~= 0)
	onButton(arg_132_0, arg_132_0.simulationBtn, function()
		if var_132_9 == 0 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("tech_simulate_closed"))
		else
			local var_136_0 = i18n("blueprint_simulation_confirm_" .. var_132_0.id)

			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = var_136_0,
				onYes = function()
					arg_132_0:emit(ShipBluePrintMediator.SIMULATION_BATTLE, var_132_9)
				end
			})
		end
	end, SFX_CONFIRM)
end

function var_0_0.updateTaskList(arg_138_0)
	local var_138_0 = arg_138_0.contextData.shipBluePrintVO
	local var_138_1 = var_138_0:getTaskIds()

	for iter_138_0 = arg_138_0.taskContainer.childCount, #var_138_1 do
		cloneTplTo(arg_138_0.taskTpl, arg_138_0.taskContainer)
	end

	local var_138_2 = arg_138_0.taskContainer.childCount

	for iter_138_1 = 1, var_138_2 do
		local var_138_3 = arg_138_0.taskContainer:GetChild(iter_138_1 - 1)

		setActive(var_138_3, iter_138_1 <= #var_138_1)

		if arg_138_0.taskTFs[iter_138_1] then
			arg_138_0.taskTFs[iter_138_1]:clear()
		end

		if iter_138_1 <= #var_138_1 then
			if not arg_138_0.taskTFs[iter_138_1] then
				arg_138_0.taskTFs[iter_138_1] = arg_138_0:createTask(var_138_3)
			end

			local var_138_4 = var_138_1[iter_138_1]
			local var_138_5 = arg_138_0:getTaskById(var_138_4)

			if var_138_0.duration > 0 then
				var_138_5.leftTime = var_138_0:getTaskOpenTimeStamp(var_138_4) - var_138_0.duration
			end

			var_138_5.taskState = var_138_0:getTaskStateById(var_138_4)
			var_138_5.dueTime = var_138_0:getTaskOpenTimeStamp(var_138_4)
			var_138_5.index = iter_138_1

			arg_138_0.taskTFs[iter_138_1]:update(var_138_5)
		end
	end
end

function var_0_0.createTask(arg_139_0, arg_139_1)
	local var_139_0 = {
		title = arg_139_0:findTF("title/name", arg_139_1),
		desc = arg_139_0:findTF("desc/Text", arg_139_1),
		timerTF = arg_139_0:findTF("title/timer", arg_139_1),
		timerTFTxt = arg_139_0:findTF("title/timer/Text", arg_139_1),
		timerOpen = arg_139_0:findTF("title/timer/open", arg_139_1),
		timerClose = arg_139_0:findTF("title/timer/close", arg_139_1),
		maskAchieved = arg_139_0:findTF("title/slider/complete", arg_139_1),
		tip = arg_139_0:findTF("title/tip", arg_139_1),
		commitBtn = arg_139_0:findTF("desc/commit_panel/commit_btn", arg_139_1),
		itemInfo = arg_139_0:findTF("desc/item_info", arg_139_1)
	}

	var_139_0.itemContainer = arg_139_0:findTF("items", var_139_0.itemInfo)
	var_139_0.itemTpl = arg_139_0:findTF("item_tpl", var_139_0.itemContainer)
	var_139_0.numberTF = arg_139_0:findTF("title/number", arg_139_1)
	var_139_0.progressTF = arg_139_0:findTF("title/slider", arg_139_1)
	var_139_0.progessSlider = var_139_0.progressTF:GetComponent(typeof(Slider))
	var_139_0.lockBtn = arg_139_0:findTF("desc/commit_panel/lock_btn", arg_139_1)
	var_139_0.itemCount = var_139_0.itemTpl:Find("award/icon_bg/count")
	var_139_0.progres = arg_139_0:findTF("desc/commit_panel/progress", arg_139_1)
	var_139_0.progreshadow = arg_139_0:findTF("title/shadow", arg_139_1)
	var_139_0.check = findTF(arg_139_1, "title/complete")
	var_139_0.lock = findTF(arg_139_1, "title/lock")
	var_139_0.working = findTF(arg_139_1, "title/working")
	var_139_0.pause = findTF(arg_139_1, "title/pause")
	var_139_0.pauseLock = findTF(arg_139_1, "title/pause_lock")
	var_139_0.view = arg_139_0

	onToggle(arg_139_0, arg_139_1, function(arg_140_0)
		setActive(var_139_0.desc, arg_140_0)
		setActive(var_139_0.progreshadow, arg_140_0)

		if arg_140_0 then
			Canvas.ForceUpdateCanvases()

			local var_140_0 = arg_139_0.taskContainer.parent.transform:InverseTransformPoint(arg_139_1.position).y
			local var_140_1 = var_140_0 - arg_139_1.rect.height
			local var_140_2 = arg_139_0.taskContainer.parent.transform.rect
			local var_140_3 = 0

			if var_140_1 < var_140_2.yMin then
				var_140_3 = var_140_2.yMin - var_140_1
			end

			if var_140_0 > var_140_2.yMax then
				var_140_3 = var_140_2.yMax - var_140_0
			end

			local var_140_4 = arg_139_0.taskContainer.localPosition

			var_140_4.y = var_140_4.y + var_140_3
			arg_139_0.taskContainer.localPosition = var_140_4
			var_139_0.progreshadow.localPosition = Vector3(39, -(148 + var_139_0.desc.rect.height - 150))
		end
	end, SFX_PANEL)

	function var_139_0.update(arg_141_0, arg_141_1)
		arg_141_0:clearTimer()

		arg_141_0.autoCommit = true
		arg_141_0.isExpTask = false

		removeOnButton(arg_141_0.commitBtn)
		arg_141_0:updateItemInfo(arg_141_1)
		arg_141_0:updateView(arg_141_1)
		arg_141_0:updateProgress(arg_141_1)
	end

	function var_139_0.updateItemInfo(arg_142_0, arg_142_1)
		arg_142_0.taskVO = arg_142_1

		changeToScrollText(arg_142_0.title, arg_142_1:getConfig("name"))
		setText(arg_142_0.desc, arg_142_1:getConfig("desc") .. "\n\n")

		local var_142_0
		local var_142_1 = arg_142_1:getConfig("target_num")
		local var_142_2 = arg_142_1:getConfig("sub_type")

		if var_142_2 == TASK_SUB_TYPE_GIVE_ITEM then
			arg_142_0.autoCommit = false
			var_142_0 = tonumber(arg_142_1:getConfig("target_id"))
		elseif var_142_2 == TASK_SUB_TYPE_PLAYER_RES then
			arg_142_0.autoCommit = false
			var_142_0 = id2ItemId(tonumber(arg_142_1:getConfig("target_id")))
		elseif var_142_2 == TASK_SUB_TYPE_BATTLE_EXP then
			arg_142_0.isExpTask = true
			var_142_0 = 59000
		end

		setActive(arg_142_0.itemContainer, not arg_142_0.autoCommit or arg_142_0.isExpTask)

		if var_142_0 then
			updateDrop(arg_142_0.itemTpl:Find("award"), {
				type = 2,
				id = var_142_0,
				count = var_142_1
			})
			setText(arg_142_0.itemCount, var_142_1 > 1000 and math.floor(var_142_1 / 1000) .. "K" or var_142_1)
		end

		setText(arg_142_0.numberTF, arg_142_1.index)
	end

	function var_139_0.updateView(arg_143_0, arg_143_1)
		local var_143_0 = arg_143_1.taskState
		local var_143_1 = false
		local var_143_2 = false
		local var_143_3 = false

		if var_143_0 == ShipBluePrint.TASK_STATE_PAUSE and arg_143_1.leftTime then
			local var_143_4 = getProxy(TaskProxy):getTaskVO(arg_143_1.id)

			var_143_1 = var_143_4 and var_143_4:isFinish()
			var_143_3 = arg_143_1.leftTime > 0
			var_143_2 = var_143_4 and var_143_4:isReceive()

			if arg_143_1.leftTime > 0 then
				setText(var_139_0.timerTFTxt, pg.TimeMgr.GetInstance():DescCDTime(arg_143_1.leftTime))
			end
		end

		setActive(arg_143_0.pause, ShipBluePrint.TASK_STATE_PAUSE == var_143_0 and not var_143_1 and not var_143_3 or ShipBluePrint.TASK_STATE_PAUSE == var_143_0 and not var_143_3 and var_143_1 and not arg_143_0.autoCommit)
		setActive(arg_143_0.pauseLock, ShipBluePrint.TASK_STATE_PAUSE == var_143_0 and not var_143_1 and var_143_3)
		setActive(arg_143_0.lockBtn, var_143_0 ~= ShipBluePrint.TASK_STATE_ACHIEVED and (var_143_0 ~= ShipBluePrint.TASK_STATE_START or not not arg_143_0.autoCommit))
		setActive(arg_143_0.commitBtn, var_143_0 == ShipBluePrint.TASK_STATE_ACHIEVED or var_143_0 == ShipBluePrint.TASK_STATE_START and not arg_143_0.autoCommit)
		setActive(arg_143_0.progressTF, var_143_0 == ShipBluePrint.TASK_STATE_ACHIEVED or var_143_0 == ShipBluePrint.TASK_STATE_START or var_143_0 == ShipBluePrint.TASK_STATE_FINISHED or var_143_0 == ShipBluePrint.TASK_STATE_PAUSE and not var_143_3)
		setActive(arg_143_0.lock, var_143_0 == ShipBluePrint.TASK_STATE_LOCK or var_143_0 == ShipBluePrint.TASK_STATE_WAIT)
		setActive(arg_143_0.working, var_143_0 == ShipBluePrint.TASK_STATE_OPENING or var_143_0 == ShipBluePrint.TASK_STATE_START or var_143_0 == ShipBluePrint.TASK_STATE_ACHIEVED)
		setActive(arg_143_0.maskAchieved, var_143_0 == ShipBluePrint.TASK_STATE_FINISHED or var_143_0 == ShipBluePrint.TASK_STATE_PAUSE and var_143_2)
		setActive(arg_143_0.timerTF, var_143_0 == ShipBluePrint.TASK_STATE_WAIT or var_143_0 == ShipBluePrint.TASK_STATE_PAUSE and arg_143_1.leftTime and arg_143_1.leftTime > 0)
		setActive(arg_143_0.check, arg_143_0.autoCommit and var_143_0 == ShipBluePrint.TASK_STATE_ACHIEVED or var_143_0 == ShipBluePrint.TASK_STATE_FINISHED or var_143_0 == ShipBluePrint.TASK_STATE_PAUSE and var_143_2)
		setActive(arg_143_0.tip, var_143_0 == ShipBluePrint.TASK_STATE_ACHIEVED)
		setActive(arg_143_0.timerOpen, var_143_0 == ShipBluePrint.TASK_STATE_WAIT)
		setActive(arg_143_0.timerClose, var_143_0 == ShipBluePrint.TASK_STATE_PAUSE and arg_143_1.leftTime and arg_143_1.leftTime > 0)
	end

	function var_139_0.updateProgress(arg_144_0, arg_144_1)
		local var_144_0 = arg_144_1.taskState
		local var_144_1 = arg_144_1:getProgress() / arg_144_1:getConfig("target_num")

		if var_144_0 == ShipBluePrint.TASK_STATE_WAIT then
			arg_144_0:addTimer(arg_144_1, arg_144_1.dueTime)

			var_144_1 = 0
		elseif var_144_0 == ShipBluePrint.TASK_STATE_OPENING then
			var_144_1 = 0

			arg_144_0.view:emit(ShipBluePrintMediator.ON_TASK_OPEN, arg_144_1.id)
		elseif var_144_0 == ShipBluePrint.TASK_STATE_PAUSE then
			if arg_144_1:isReceive() then
				var_144_1 = 1
			end
		elseif var_144_0 == ShipBluePrint.TASK_STATE_LOCK then
			var_144_1 = 0
		elseif var_144_0 == ShipBluePrint.TASK_STATE_ACHIEVED then
			onButton(arg_144_0.view, arg_144_0.commitBtn, function()
				arg_144_0.view:emit(ShipBluePrintMediator.ON_FINISH_TASK, arg_144_1.id)
			end, SFX_PANEL)

			var_144_1 = 1
		elseif var_144_0 == ShipBluePrint.TASK_STATE_FINISHED then
			var_144_1 = 1
		elseif var_144_0 == ShipBluePrint.TASK_STATE_START and not arg_144_0.autoCommit then
			onButton(arg_144_0.view, arg_144_0.commitBtn, function()
				arg_144_0.view:emit(ShipBluePrintMediator.ON_FINISH_TASK, arg_144_1.id)
			end, SFX_PANEL)

			var_144_1 = 0
		end

		if var_144_1 > 0 then
			arg_144_0.itemSliderLT = LeanTween.value(go(arg_144_0.progressTF), 0, math.min(var_144_1, 1), 0.5 * math.min(var_144_1, 1)):setOnUpdate(System.Action_float(function(arg_147_0)
				arg_144_0.progessSlider.value = arg_147_0
			end)).uniqueId
		else
			arg_144_0.progessSlider.value = var_144_1
		end

		local var_144_2 = math.floor(var_144_1 * 100)

		setText(arg_144_0.progres, math.ceil(math.min(var_144_2, 100)) .. "%")
		setText(arg_144_0.progreshadow, math.min(var_144_2, 100) .. "%")
	end

	function var_139_0.addTimer(arg_148_0, arg_148_1, arg_148_2)
		arg_148_0:clearTimer()

		arg_148_0.taskTimer = Timer.New(function()
			local var_149_0 = pg.TimeMgr.GetInstance():GetServerTime()
			local var_149_1 = arg_148_2 - var_149_0

			if var_149_1 > 0 then
				setText(arg_148_0.timerTFTxt, pg.TimeMgr.GetInstance():DescCDTime(var_149_1))
			else
				arg_148_0:clearTimer()
				setText(arg_148_0.timerTFTxt, "00:00:00")
				arg_148_0.view:emit(ShipBluePrintMediator.ON_TASK_OPEN, arg_148_1.id)
			end
		end, 1, -1)

		arg_148_0.taskTimer:Start()
		arg_148_0.taskTimer.func()
	end

	function var_139_0.clearTimer(arg_150_0)
		if arg_150_0.taskTimer then
			arg_150_0.taskTimer:Stop()

			arg_150_0.taskTimer = nil
		end
	end

	function var_139_0.clear(arg_151_0)
		arg_151_0:clearTimer()

		if arg_151_0.itemSliderLT then
			LeanTween.cancel(arg_151_0.itemSliderLT)

			arg_151_0.itemSliderLT = nil
		end
	end

	return var_139_0
end

function var_0_0.openPreView(arg_152_0)
	local var_152_0 = arg_152_0.contextData.shipBluePrintVO

	if var_152_0 then
		setActive(arg_152_0.preViewer, true)
		setParent(arg_152_0.blurPanel, arg_152_0._tf)
		pg.UIMgr.GetInstance():BlurPanel(arg_152_0.preViewer)
		arg_152_0:playLoadingAni()

		arg_152_0.viewShipVO = var_152_0:getShipVO()
		arg_152_0.breakIds = arg_152_0:getStages(arg_152_0.viewShipVO)

		for iter_152_0 = 1, var_0_4 do
			local var_152_1 = arg_152_0.breakIds[iter_152_0]
			local var_152_2 = var_0_3[var_152_1]
			local var_152_3 = arg_152_0:findTF("stage" .. iter_152_0, arg_152_0.stages)

			onToggle(arg_152_0, var_152_3, function(arg_153_0)
				if arg_153_0 then
					setText(arg_152_0.breakView, var_0_3[var_152_1].breakout_view)
					arg_152_0:switchStage(var_152_1)
				end
			end, SFX_PANEL)

			if iter_152_0 == 1 then
				triggerToggle(var_152_3, true)
			end
		end

		arg_152_0.isShowPreview = true

		arg_152_0:updateMaxLevelAttrs(var_152_0)
	end
end

var_0_0.MAX_LEVEL_ATTRS = {
	AttributeType.Durability,
	AttributeType.Cannon,
	AttributeType.Torpedo,
	AttributeType.AntiAircraft,
	AttributeType.Air,
	AttributeType.Reload,
	AttributeType.ArmorType,
	AttributeType.Dodge
}

function var_0_0.updateMaxLevelAttrs(arg_154_0, arg_154_1)
	if not arg_154_1:isFetched() then
		return
	end

	local var_154_0 = arg_154_0.shipVOs[arg_154_1.shipId]
	local var_154_1 = Clone(var_154_0)

	var_154_1.level = 125

	local var_154_2 = Clone(arg_154_1)

	var_154_2.level = arg_154_1:getMaxLevel()

	local var_154_3 = intProperties(var_154_2:getShipProperties(var_154_1, false))

	for iter_154_0, iter_154_1 in ipairs(var_0_0.MAX_LEVEL_ATTRS) do
		local var_154_4 = arg_154_0.previewAttrContainer:Find(iter_154_1)

		if iter_154_1 == AttributeType.ArmorType then
			setText(var_154_4:Find("bg/value"), var_154_0:getShipArmorName())
		else
			setText(var_154_4:Find("bg/value"), var_154_3[iter_154_1] or 0)
		end

		setText(var_154_4:Find("bg/name"), AttributeType.Type2Name(iter_154_1))
	end
end

function var_0_0.closePreview(arg_155_0, arg_155_1)
	if arg_155_0.previewer then
		arg_155_0.previewer:clear()

		arg_155_0.previewer = nil
	end

	setActive(arg_155_0.preViewer, false)
	setActive(arg_155_0.rawImage, false)

	if not arg_155_1 then
		SetParent(arg_155_0.blurPanel, pg.UIMgr.GetInstance().OverlayMain)
	end

	pg.UIMgr.GetInstance():UnblurPanel(arg_155_0.preViewer, arg_155_0._tf)

	arg_155_0.isShowPreview = nil
end

function var_0_0.playLoadingAni(arg_156_0)
	setActive(arg_156_0.seaLoading, true)
end

function var_0_0.stopLoadingAni(arg_157_0)
	setActive(arg_157_0.seaLoading, false)
end

function var_0_0.showBarrage(arg_158_0)
	arg_158_0.previewer = WeaponPreviewer.New(arg_158_0.rawImage)

	arg_158_0.previewer:configUI(arg_158_0.healTF)
	arg_158_0.previewer:setDisplayWeapon(arg_158_0:getWaponIdsById(arg_158_0.breakOutId))
	arg_158_0.previewer:load(40000, arg_158_0.viewShipVO, arg_158_0:getAllWeaponIds(), function()
		arg_158_0:stopLoadingAni()
	end)
end

function var_0_0.getWaponIdsById(arg_160_0, arg_160_1)
	return var_0_3[arg_160_1].weapon_ids
end

function var_0_0.getAllWeaponIds(arg_161_0)
	local var_161_0 = {}

	for iter_161_0, iter_161_1 in ipairs(arg_161_0.breakIds) do
		local var_161_1 = Clone(var_0_3[iter_161_1].weapon_ids)
		local var_161_2 = {
			__add = function(arg_162_0, arg_162_1)
				for iter_162_0, iter_162_1 in ipairs(arg_162_0) do
					if not table.contains(arg_162_1, iter_162_1) then
						table.insert(arg_162_1, iter_162_1)
					end
				end

				return arg_162_1
			end
		}

		setmetatable(var_161_0, var_161_2)

		var_161_0 = var_161_0 + var_161_1
	end

	return var_161_0
end

function var_0_0.getStages(arg_163_0, arg_163_1)
	local var_163_0 = {}
	local var_163_1 = math.floor(arg_163_1.configId / 10)

	for iter_163_0 = 1, 4 do
		local var_163_2 = tonumber(var_163_1 .. iter_163_0)

		assert(var_0_3[var_163_2], "必须存在配置" .. var_163_2)
		table.insert(var_163_0, var_163_2)
	end

	return var_163_0
end

function var_0_0.switchStage(arg_164_0, arg_164_1)
	if arg_164_0.breakOutId == arg_164_1 then
		return
	end

	arg_164_0.breakOutId = arg_164_1

	if arg_164_0.previewer then
		arg_164_0.previewer:setDisplayWeapon(arg_164_0:getWaponIdsById(arg_164_0.breakOutId))
	end
end

function var_0_0.clearTimers(arg_165_0)
	for iter_165_0, iter_165_1 in pairs(arg_165_0.taskTFs or {}) do
		iter_165_1:clear()
	end
end

function var_0_0.cloneTplTo(arg_166_0, arg_166_1, arg_166_2)
	local var_166_0 = tf(Instantiate(arg_166_1))

	SetActive(var_166_0, true)
	var_166_0:SetParent(tf(arg_166_2), false)

	return var_166_0
end

function var_0_0.onBackPressed(arg_167_0)
	if isActive(arg_167_0.msgPanel) then
		pg.UIMgr.GetInstance():UnblurPanel(arg_167_0.msgPanel, arg_167_0.top)
		setActive(arg_167_0.msgPanel, false)
	elseif isActive(arg_167_0.unlockPanel) then
		pg.UIMgr.GetInstance():UnblurPanel(arg_167_0.unlockPanel, arg_167_0.top)
		setActive(arg_167_0.unlockPanel, false)
	elseif isActive(arg_167_0.versionPanel) then
		triggerButton(arg_167_0.versionPanel:Find("bg"))
	elseif arg_167_0.isShowPreview then
		arg_167_0:closePreview(true)
	elseif arg_167_0.svQuickExchange:isShowing() then
		arg_167_0.svQuickExchange:Hide()
	elseif arg_167_0.awakenPlay or arg_167_0:inModAnim() then
		-- block empty
	else
		arg_167_0:emit(var_0_0.ON_BACK_PRESSED)
	end
end

function var_0_0.willExit(arg_168_0)
	if isActive(arg_168_0.msgPanel) then
		pg.UIMgr.GetInstance():UnblurPanel(arg_168_0.msgPanel, arg_168_0.top)
		setActive(arg_168_0.msgPanel, false)
	end

	if isActive(arg_168_0.unlockPanel) then
		pg.UIMgr.GetInstance():UnblurPanel(arg_168_0.unlockPanel, arg_168_0.top)
		setActive(arg_168_0.unlockPanel, false)
	end

	pg.UIMgr.GetInstance():UnOverlayPanel(arg_168_0.blurPanel, arg_168_0._tf)
	LeanTween.cancel(go(arg_168_0.fittingAttrPanel))

	if arg_168_0.lastPaintingName then
		retPaintingPrefab(arg_168_0.painting, arg_168_0.lastPaintingName)
	end

	for iter_168_0, iter_168_1 in pairs(arg_168_0.taskTFs or {}) do
		iter_168_1:clear()
	end

	arg_168_0:closePreview(true)
	arg_168_0:clearLeanTween(true)

	if arg_168_0.previewer then
		arg_168_0.previewer:clear()

		arg_168_0.previewer = nil
	end

	if arg_168_0.cbTimer then
		arg_168_0.cbTimer:Stop()

		arg_168_0.cbTimer = nil
	end

	arg_168_0.svQuickExchange:Destroy()
end

function var_0_0.paintBreath(arg_169_0)
	LeanTween.cancel(go(arg_169_0.painting))
	LeanTween.moveY(rtf(arg_169_0.painting), var_0_5, var_0_6):setLoopPingPong():setEase(LeanTweenType.easeInOutCubic):setFrom(0)
end

function var_0_0.buildStartAni(arg_170_0, arg_170_1, arg_170_2)
	if arg_170_1 == "researchStartWindow" then
		arg_170_0.progressPanel.localScale = Vector3(0, 1, 1)

		LeanTween.scale(arg_170_0.progressPanel, Vector3(1, 1, 1), 0.2):setDelay(2)
	end

	local function var_170_0()
		arg_170_0.awakenAni:SetActive(true)

		arg_170_0.awakenPlay = true

		local var_171_0 = tf(arg_170_0.awakenAni)

		pg.UIMgr.GetInstance():BlurPanel(var_171_0)
		var_171_0:SetAsLastSibling()
		var_171_0:GetComponent("DftAniEvent"):SetEndEvent(function(arg_172_0)
			if not IsNil(arg_170_0.awakenAni) then
				pg.UIMgr.GetInstance():UnblurPanel(var_171_0, arg_170_0.blurPanel)
				arg_170_0.awakenAni:SetActive(false)

				arg_170_0.awakenPlay = false

				if arg_170_2 then
					arg_170_2()
				end
			end
		end)
	end

	local var_170_1 = arg_170_0:findTF(arg_170_1 .. "(Clone)")

	arg_170_0.awakenAni = var_170_1 and go(var_170_1)

	if not arg_170_0.awakenAni then
		PoolMgr.GetInstance():GetUI(arg_170_1, true, function(arg_173_0)
			arg_173_0:SetActive(true)

			arg_170_0.awakenAni = arg_173_0

			var_170_0()
		end)
	else
		var_170_0()
	end
end

function var_0_0.showFittingMsgPanel(arg_174_0, arg_174_1)
	pg.UIMgr.GetInstance():BlurPanel(arg_174_0.msgPanel)
	setActive(arg_174_0.msgPanel, true)

	local var_174_0 = arg_174_0.contextData.shipBluePrintVO
	local var_174_1 = var_174_0:getMaxFateLevel()
	local var_174_2 = arg_174_0:findTF("window/content", arg_174_0.msgPanel)
	local var_174_3 = arg_174_0:findTF("pre_btn", var_174_2)
	local var_174_4 = arg_174_0:findTF("next_btn", var_174_2)
	local var_174_5 = arg_174_0:findTF("attrl_panel", var_174_2)
	local var_174_6 = arg_174_0:findTF("skill_panel", var_174_2)
	local var_174_7 = arg_174_0:findTF("phase", var_174_2)
	local var_174_8 = {
		"I",
		"II",
		"III",
		"IV",
		"V"
	}

	local function var_174_9()
		setActive(var_174_3, arg_174_1 > 1)
		setActive(var_174_4, arg_174_1 < var_174_1)
		setText(var_174_7, "PHASE." .. var_174_8[arg_174_1])

		local var_175_0 = var_174_0:getFateStrengthenConfig(arg_174_1)

		assert(var_175_0.special == 1 and type(var_175_0.special_effect) == "table", "without fate config")

		local var_175_1 = var_175_0.special_effect
		local var_175_2
		local var_175_3 = {}

		for iter_175_0, iter_175_1 in ipairs(var_175_1) do
			local var_175_4 = iter_175_1[1]

			if var_175_4 == ShipBluePrint.STRENGTHEN_TYPE_CHANGE_SKILL then
				var_175_2 = iter_175_1[2][2]
			elseif var_175_4 == ShipBluePrint.STRENGTHEN_TYPE_ATTR then
				table.insert(var_175_3, iter_175_1[2])
			end
		end

		setActive(var_174_5, #var_175_3 > 0)
		setActive(var_174_6, var_175_2)

		if var_175_2 then
			local var_175_5 = getSkillConfig(var_175_2)

			GetImageSpriteFromAtlasAsync("skillicon/" .. var_175_5.icon, "", arg_174_0:findTF("skill_icon", var_174_6))
			setText(arg_174_0:findTF("skill_name", var_174_6), getSkillName(var_175_2))

			local var_175_6 = 1

			setText(arg_174_0:findTF("skill_lv", var_174_6), "Lv." .. var_175_6)
			setText(arg_174_0:findTF("help_panel/skill_intro", var_174_6), getSkillDescGet(var_175_2))
		end

		if #var_175_3 > 0 then
			for iter_175_2, iter_175_3 in ipairs(var_175_3) do
				local var_175_7 = iter_175_2 < var_174_5.childCount and var_174_5:GetChild(iter_175_2) or cloneTplTo(var_174_5:GetChild(iter_175_2 - 1), var_174_5)

				setText(var_175_7:Find("name"), AttributeType.Type2Name(iter_175_3[1]))
				setText(var_175_7:Find("number"), " + " .. iter_175_3[2])
			end

			for iter_175_4 = #var_175_3 + 1, var_174_5.childCount - 1 do
				setActive(var_174_5:GetChild(iter_175_4), false)
			end
		end
	end

	onButton(arg_174_0, var_174_3, function()
		arg_174_1 = arg_174_1 - 1

		var_174_9()
	end)
	onButton(arg_174_0, var_174_4, function()
		arg_174_1 = arg_174_1 + 1

		var_174_9()
	end)
	setText(arg_174_0:findTF("desc", var_174_5), i18n("fate_attr_word"))
	var_174_9()
end

function var_0_0.showUnlockPanel(arg_178_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_178_0.unlockPanel)
	setActive(arg_178_0.unlockPanel, true)

	local var_178_0 = arg_178_0.contextData.shipBluePrintVO.id
	local var_178_1 = arg_178_0.contextData.shipBluePrintVO:getUnlockItem()
	local var_178_2 = Drop.New({
		type = DROP_TYPE_ITEM,
		id = var_178_1
	})
	local var_178_3 = arg_178_0.contextData.shipBluePrintVO:getShipVO()
	local var_178_4 = var_178_3:getPainting()
	local var_178_5 = arg_178_0.unlockPanel:Find("window/content")

	GetImageSpriteFromAtlasAsync("shipYardIcon/" .. var_178_4, var_178_4, var_178_5:Find("Image/mask/icon"), true)
	setText(var_178_5:Find("words/Text"), i18n("techpackage_item_use_1", var_178_3:getName()))
	setText(var_178_5:Find("words/Text_2"), i18n("techpackage_item_use_2", var_178_2:getName()))
	GetImageSpriteFromAtlasAsync(var_178_2:getIcon(), "", arg_178_0.unlockPanel:Find("window/confirm_btn/Image/Image"))
	setText(arg_178_0.unlockPanel:Find("window/confirm_btn/Image/Text"), i18n("event_ui_consume"))
	onButton(arg_178_0, arg_178_0.unlockPanel:Find("window/confirm_btn"), function()
		pg.UIMgr.GetInstance():UnblurPanel(arg_178_0.unlockPanel, arg_178_0.top)
		setActive(arg_178_0.unlockPanel, false)
		arg_178_0:emit(ShipBluePrintMediator.ON_ITEM_UNLOCK, var_178_0, var_178_1)
	end, SFX_CANCEL)
end

function var_0_0.checkStory(arg_180_0)
	local var_180_0 = {
		nil,
		"FANGAN3"
	}

	arg_180_0.storyMgr = arg_180_0.storyMgr or pg.NewStoryMgr.GetInstance()

	if var_180_0[arg_180_0.version] and not arg_180_0.storyMgr:IsPlayed(var_180_0[arg_180_0.version]) then
		arg_180_0.storyMgr:Play(var_180_0[arg_180_0.version])
	end
end

return var_0_0
