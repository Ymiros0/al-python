local var_0_0 = class("MetaQuickTacticsLayer", import("...base.BaseUI"))

function var_0_0.getUIName(arg_1_0)
	return "MetaQuickTacticsUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:initUITextTips()
	arg_2_0:initData()
	arg_2_0:initUI()
	arg_2_0:addListener()
	arg_2_0:overlayPanel(true)
end

function var_0_0.didEnter(arg_3_0)
	arg_3_0:initSkillInfoPanel()
	arg_3_0:initUIItemList()
end

function var_0_0.willExit(arg_4_0)
	arg_4_0:overlayPanel(false)
end

function var_0_0.onBackPressed(arg_5_0)
	arg_5_0:closeView()
end

function var_0_0.initUITextTips(arg_6_0)
	local var_6_0 = arg_6_0:findTF("Content/SkillInfo/UseTip")

	setText(var_6_0, i18n("metaskill_up"))
end

function var_0_0.initData(arg_7_0)
	arg_7_0.metaProxy = getProxy(MetaCharacterProxy)
	arg_7_0.bagProxy = getProxy(BagProxy)
	arg_7_0.bayProxy = getProxy(BayProxy)
	arg_7_0.shipID = arg_7_0.contextData.shipID
	arg_7_0.skillID = arg_7_0.contextData.skillID
	arg_7_0.bookIDList = pg.item_data_statistics.get_id_list_by_type[Item.METALESSON_TYPE]
	arg_7_0.useCountDict = {}
	arg_7_0.maxCountDict = {}
	arg_7_0.useCountTextDict = {}

	arg_7_0:resetUseData()

	arg_7_0.colorDict = {
		[ItemRarity.Blue] = "#70D4FAFF",
		[ItemRarity.Purple] = "#C380FBFF",
		[ItemRarity.Gold] = "#FFCC4DFF"
	}
	arg_7_0.expDict = {}

	for iter_7_0, iter_7_1 in ipairs(arg_7_0.bookIDList) do
		arg_7_0.expDict[iter_7_1] = tonumber(Item.getConfigData(iter_7_1).usage_arg)
	end
end

function var_0_0.initUI(arg_8_0)
	arg_8_0.bg = arg_8_0:findTF("BG")
	arg_8_0.tpl = arg_8_0:findTF("TacticsTpl")

	local var_8_0 = arg_8_0:findTF("Content")

	arg_8_0.closeBtn = arg_8_0:findTF("Title/CloseBtn", var_8_0)

	local var_8_1 = arg_8_0:findTF("SkillInfo", var_8_0)
	local var_8_2 = arg_8_0:findTF("Skill", var_8_1)

	arg_8_0.skillNameText = arg_8_0:findTF("Name", var_8_2)
	arg_8_0.skillLevelText = arg_8_0:findTF("LevelNum", var_8_2)
	arg_8_0.skillLevelUpText = arg_8_0:findTF("LevelUp", var_8_2)

	local var_8_3 = arg_8_0:findTF("Exp", var_8_1)

	arg_8_0.curExpText = arg_8_0:findTF("CurExp", var_8_3)
	arg_8_0.addExpText = arg_8_0:findTF("AddExp", var_8_3)
	arg_8_0.totalExpText = arg_8_0:findTF("TotalExp", var_8_3)
	arg_8_0.progressBar = arg_8_0:findTF("Slider", var_8_1)
	arg_8_0.containerTF = arg_8_0:findTF("Container", var_8_0)

	local var_8_4 = arg_8_0:findTF("Action", var_8_0)

	arg_8_0.clearBtn = arg_8_0:findTF("ClearBtn", var_8_4)
	arg_8_0.onestepBtn = arg_8_0:findTF("OneStepBtn", var_8_4)
	arg_8_0.confirmBtn = arg_8_0:findTF("ConfirmBtn", var_8_4)
end

function var_0_0.addListener(arg_9_0)
	local function var_9_0()
		arg_9_0:closeView()
	end

	onButton(arg_9_0, arg_9_0.bg, var_9_0, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.closeBtn, var_9_0, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.clearBtn, function()
		arg_9_0:resetUseData()
		arg_9_0:updateAfterModifyUseCount()
	end, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.onestepBtn, function()
		arg_9_0:oneStep()
		arg_9_0:updateAfterModifyUseCount()
	end, SFX_PANEL)
	onButton(arg_9_0, arg_9_0.confirmBtn, function()
		local var_13_0 = 0

		for iter_13_0, iter_13_1 in ipairs(arg_9_0.bookIDList) do
			var_13_0 = var_13_0 + arg_9_0.useCountDict[iter_13_1]
		end

		if var_13_0 <= 0 then
			pg.TipsMgr.GetInstance():ShowTips(i18n("word_materal_no_enough"))
		else
			local var_13_1, var_13_2 = arg_9_0:preCalcExpOverFlow(0, 0)

			if var_13_1 then
				arg_9_0:emit(MetaQuickTacticsMediator.OPEN_OVERFLOW_LAYER, arg_9_0.shipID, arg_9_0.skillID, arg_9_0.useCountDict, var_13_2)
			else
				arg_9_0:emit(MetaQuickTacticsMediator.USE_TACTICS_BOOK, arg_9_0.shipID, arg_9_0.skillID, arg_9_0.useCountDict)
			end
		end
	end, SFX_PANEL)
end

function var_0_0.overlayPanel(arg_14_0, arg_14_1)
	if arg_14_1 and arg_14_0._tf then
		pg.UIMgr.GetInstance():OverlayPanel(arg_14_0._tf, {
			groupName = LayerWeightConst.GROUP_META,
			weight = LayerWeightConst.BASE_LAYER
		})
	elseif arg_14_0._tf then
		pg.UIMgr.GetInstance():UnOverlayPanel(arg_14_0._tf)
	end
end

function var_0_0.initSkillInfoPanel(arg_15_0)
	local var_15_0 = arg_15_0.skillID
	local var_15_1 = arg_15_0.bayProxy:getShipById(arg_15_0.shipID):getMetaSkillLevelBySkillID(var_15_0)
	local var_15_2 = getSkillConfig(var_15_0)
	local var_15_3 = getSkillName(var_15_2.id)

	setText(arg_15_0.skillNameText, var_15_3)
	setText(arg_15_0.skillLevelText, "LEVEL:" .. var_15_1)
	setText(arg_15_0.skillLevelUpText, "")

	local var_15_4 = arg_15_0.metaProxy:getMetaTacticsInfoByShipID(arg_15_0.shipID):getSkillExp(var_15_0)
	local var_15_5 = MetaCharacterConst.getMetaSkillTacticsConfig(var_15_0, var_15_1).need_exp

	setText(arg_15_0.curExpText, var_15_4)
	setText(arg_15_0.totalExpText, var_15_5)
	setText(arg_15_0.addExpText, "[+0]")
	setSlider(arg_15_0.progressBar, 0, var_15_5, var_15_4)
end

function var_0_0.initUIItemList(arg_16_0)
	arg_16_0.uiitemList = UIItemList.New(arg_16_0.containerTF, arg_16_0.tpl)

	arg_16_0.uiitemList:make(function(arg_17_0, arg_17_1, arg_17_2)
		if arg_17_0 == UIItemList.EventUpdate then
			arg_17_1 = arg_17_1 + 1

			arg_16_0:updateTpl(arg_17_1, arg_17_2)
		end
	end)
	arg_16_0.uiitemList:align(#arg_16_0.bookIDList)
end

function var_0_0.updateUIItemList(arg_18_0)
	arg_18_0.uiitemList:align(#arg_18_0.bookIDList)
end

function var_0_0.updateTpl(arg_19_0, arg_19_1, arg_19_2)
	local var_19_0 = arg_19_0:findTF("IconTpl", arg_19_2)
	local var_19_1 = arg_19_0:findTF("Name", arg_19_2)
	local var_19_2 = arg_19_0:findTF("MinusTenBtn", arg_19_2)
	local var_19_3 = arg_19_0:findTF("AddTenBtn", arg_19_2)
	local var_19_4 = arg_19_0:findTF("MinusBtn", arg_19_2)
	local var_19_5 = arg_19_0:findTF("AddBtn", arg_19_2)
	local var_19_6 = arg_19_0:findTF("TextBG/UseNum", arg_19_2)
	local var_19_7 = arg_19_0.bookIDList[arg_19_1]
	local var_19_8 = arg_19_0:getBookItem(var_19_7)
	local var_19_9 = arg_19_0.bagProxy:getItemCountById(var_19_7)

	if var_19_9 == 0 then
		var_19_9 = "0"
	end

	local var_19_10 = Drop.New({
		id = var_19_7,
		type = DROP_TYPE_ITEM,
		count = var_19_9
	})

	updateDrop(var_19_0, var_19_10)

	local var_19_11 = var_19_8:getConfig("name")
	local var_19_12 = var_19_8:getConfig("rarity")
	local var_19_13 = setColorStr(var_19_11, arg_19_0.colorDict[var_19_12])

	setText(var_19_1, var_19_13)

	arg_19_0.useCountTextDict[var_19_7] = var_19_6

	onButton(arg_19_0, var_19_2, function()
		arg_19_0:tryModifyUseCount(var_19_7, -10)
		arg_19_0:updateAfterModifyUseCount()
	end, SFX_PANEL)
	onButton(arg_19_0, var_19_3, function()
		if not arg_19_0:isMaxLevel() and not arg_19_0:isCanUpMax() then
			arg_19_0:tryModifyUseCount(var_19_7, 10)
			arg_19_0:updateAfterModifyUseCount()
		end
	end, SFX_PANEL)
	onButton(arg_19_0, var_19_4, function()
		arg_19_0:tryModifyUseCount(var_19_7, -1)
		arg_19_0:updateAfterModifyUseCount()
	end, SFX_PANEL)
	onButton(arg_19_0, var_19_5, function()
		if not arg_19_0:isMaxLevel() and not arg_19_0:isCanUpMax() then
			arg_19_0:tryModifyUseCount(var_19_7, 1)
			arg_19_0:updateAfterModifyUseCount()
		end
	end, SFX_PANEL)
end

function var_0_0.updateAfterModifyUseCount(arg_24_0)
	for iter_24_0, iter_24_1 in ipairs(arg_24_0.bookIDList) do
		local var_24_0 = arg_24_0.useCountTextDict[iter_24_1]
		local var_24_1 = arg_24_0.useCountDict[iter_24_1]

		setText(var_24_0, var_24_1)
	end

	local var_24_2 = arg_24_0.shipID
	local var_24_3 = arg_24_0.skillID
	local var_24_4 = arg_24_0.bayProxy:getShipById(var_24_2):getMetaSkillLevelBySkillID(var_24_3)
	local var_24_5 = arg_24_0:calcAwardExp()
	local var_24_6 = arg_24_0:calcLevelWithAwardExp(var_24_5) - var_24_4

	if var_24_6 > 0 then
		setText(arg_24_0.skillLevelUpText, "+" .. var_24_6)
	else
		setText(arg_24_0.skillLevelUpText, "")
	end

	setText(arg_24_0.addExpText, string.format("[+%d]", var_24_5))

	local var_24_7 = MetaCharacterConst.getMetaSkillTacticsConfig(var_24_3, var_24_4)

	if var_24_7 then
		local var_24_8 = var_24_7.need_exp
		local var_24_9 = arg_24_0.metaProxy:getMetaTacticsInfoByShipID(var_24_2):getSkillExp(var_24_3)

		setText(arg_24_0.curExpText, var_24_9)
		setText(arg_24_0.totalExpText, var_24_8)
		setSlider(arg_24_0.progressBar, 0, var_24_8, var_24_9 + var_24_5)
	end
end

function var_0_0.updateAfterUse(arg_25_0)
	local var_25_0 = arg_25_0.shipID
	local var_25_1 = arg_25_0.skillID
	local var_25_2 = arg_25_0.bayProxy:getShipById(var_25_0):getMetaSkillLevelBySkillID(var_25_1)

	setText(arg_25_0.skillLevelText, "LEVEL:" .. var_25_2)

	if arg_25_0:isMaxLevel() then
		setText(arg_25_0.curExpText, "MAX")
		setSlider(arg_25_0.progressBar, 0, 1, 1)
	end

	arg_25_0:updateUIItemList()
end

function var_0_0.getBookItem(arg_26_0, arg_26_1)
	return arg_26_0.bagProxy:getItemById(arg_26_1) or Drop.New({
		count = 0,
		type = DROP_TYPE_ITEM,
		id = arg_26_1
	})
end

function var_0_0.resetUseData(arg_27_0)
	arg_27_0.useCountDict = arg_27_0.useCountDict or {}
	arg_27_0.maxCountDict = arg_27_0.maxCountDict or {}

	for iter_27_0, iter_27_1 in ipairs(arg_27_0.bookIDList) do
		arg_27_0.useCountDict[iter_27_1] = 0
		arg_27_0.maxCountDict[iter_27_1] = arg_27_0.bagProxy:getItemCountById(iter_27_1)
	end
end

function var_0_0.tryModifyUseCount(arg_28_0, arg_28_1, arg_28_2)
	local var_28_0 = arg_28_0.maxCountDict[arg_28_1]
	local var_28_1 = arg_28_0.useCountDict[arg_28_1]

	if var_28_0 <= 0 then
		return
	end

	if arg_28_2 < 0 then
		local var_28_2 = math.clamp(var_28_1 + arg_28_2, 0, var_28_0)

		arg_28_0.useCountDict[arg_28_1] = var_28_2
	else
		local var_28_3 = math.min(var_28_0, arg_28_2)
		local var_28_4 = arg_28_0.expDict[arg_28_1]
		local var_28_5 = 0

		for iter_28_0 = 0, var_28_3 do
			local var_28_6 = var_28_5 * var_28_4

			if not arg_28_0:preCalcExpOverFlow(var_28_6, 0) then
				var_28_5 = iter_28_0

				if var_28_3 <= var_28_5 or var_28_0 <= var_28_1 + var_28_5 then
					break
				end
			end
		end

		arg_28_0.useCountDict[arg_28_1] = var_28_1 + var_28_5
	end
end

function var_0_0.getLevelTotalExp(arg_29_0, arg_29_1)
	local var_29_0 = arg_29_0.skillID
	local var_29_1 = arg_29_0.bayProxy:getShipById(arg_29_0.shipID)
	local var_29_2 = pg.skill_data_template[var_29_0].max_level
	local var_29_3 = pg.ship_meta_skilltask.get_id_list_by_skill_ID[var_29_0]
	local var_29_4 = 0

	for iter_29_0, iter_29_1 in ipairs(var_29_3) do
		local var_29_5 = pg.ship_meta_skilltask[iter_29_1]
		local var_29_6 = var_29_5.level
		local var_29_7 = var_29_5.need_exp

		if var_29_6 < arg_29_1 then
			var_29_4 = var_29_4 + var_29_7
		end
	end

	return var_29_4
end

function var_0_0.getCurLevelExp(arg_30_0)
	local var_30_0 = arg_30_0.skillID
	local var_30_1 = arg_30_0.bayProxy:getShipById(arg_30_0.shipID):getMetaSkillLevelBySkillID(var_30_0)
	local var_30_2 = arg_30_0.metaProxy:getMetaTacticsInfoByShipID(arg_30_0.shipID):getSkillExp(var_30_0)

	return arg_30_0:getLevelTotalExp(var_30_1) + var_30_2
end

function var_0_0.calcAwardExp(arg_31_0)
	local var_31_0 = 0

	for iter_31_0, iter_31_1 in ipairs(arg_31_0.bookIDList) do
		var_31_0 = var_31_0 + arg_31_0.useCountDict[iter_31_1] * arg_31_0.expDict[iter_31_1]
	end

	return var_31_0
end

function var_0_0.calcLevelWithAwardExp(arg_32_0, arg_32_1)
	local var_32_0 = arg_32_0:getCurLevelExp() + arg_32_1
	local var_32_1 = arg_32_0.skillID
	local var_32_2 = pg.ship_meta_skilltask.get_id_list_by_skill_ID[var_32_1]
	local var_32_3 = 1

	for iter_32_0, iter_32_1 in ipairs(var_32_2) do
		local var_32_4 = pg.ship_meta_skilltask[iter_32_1].need_exp

		if var_32_4 <= var_32_0 then
			var_32_0 = var_32_0 - var_32_4
			var_32_3 = var_32_3 + 1
		else
			break
		end
	end

	return var_32_3
end

function var_0_0.isCanUpMax(arg_33_0)
	local var_33_0 = arg_33_0.skillID
	local var_33_1 = pg.skill_data_template[var_33_0].max_level

	return arg_33_0:getLevelTotalExp(var_33_1) <= arg_33_0:getCurLevelExp() + arg_33_0:calcAwardExp()
end

function var_0_0.preCalcExpOverFlow(arg_34_0, arg_34_1, arg_34_2)
	local var_34_0 = arg_34_0.skillID
	local var_34_1 = pg.skill_data_template[var_34_0].max_level
	local var_34_2 = arg_34_0:getLevelTotalExp(var_34_1) - arg_34_0:getCurLevelExp()
	local var_34_3 = arg_34_0:calcAwardExp()
	local var_34_4 = false
	local var_34_5
	local var_34_6 = var_34_3 + arg_34_1

	if var_34_2 <= var_34_6 then
		var_34_5 = var_34_6 - var_34_2

		if arg_34_2 <= var_34_5 then
			var_34_4 = true
		end
	end

	return var_34_4, var_34_5
end

function var_0_0.oneStep(arg_35_0)
	if arg_35_0:isMaxLevel() then
		return
	end

	arg_35_0:resetUseData()

	local var_35_0 = {}

	for iter_35_0, iter_35_1 in ipairs(arg_35_0.bookIDList) do
		if arg_35_0:getBookItem(iter_35_1).count > 0 then
			table.insert(var_35_0, iter_35_1)
		end
	end

	table.sort(var_35_0, function(arg_36_0, arg_36_1)
		return arg_36_1 < arg_36_0
	end)

	for iter_35_2, iter_35_3 in ipairs(var_35_0) do
		local var_35_1 = arg_35_0:getBookItem(iter_35_3)
		local var_35_2 = arg_35_0.expDict[iter_35_3]
		local var_35_3 = iter_35_2 + 1 > #var_35_0 and 0 or arg_35_0.expDict[var_35_0[iter_35_2 + 1]]

		for iter_35_4 = 1, var_35_1.count do
			if iter_35_2 < #var_35_0 and arg_35_0:preCalcExpOverFlow(var_35_2, var_35_3) then
				break
			else
				arg_35_0.useCountDict[iter_35_3] = arg_35_0.useCountDict[iter_35_3] + 1

				if arg_35_0:isCanUpMax() then
					return
				end
			end
		end
	end
end

function var_0_0.isMaxLevel(arg_37_0)
	local var_37_0 = arg_37_0.skillID
	local var_37_1 = arg_37_0.shipID

	return arg_37_0.bayProxy:getShipById(var_37_1):isSkillLevelMax(var_37_0)
end

return var_0_0
