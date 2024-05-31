local var_0_0 = class("CommanderDetailPage", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "CommanderDetailUI"
end

function var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	var_0_0.super.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3)
	arg_2_0:Load()
end

function var_0_0.RegisterEvent(arg_3_0)
	arg_3_0:bind(CommanderCatScene.EVENT_CLOSE_DESC, function(arg_4_0)
		triggerToggle(arg_3_0.skillBtn, false)
		triggerToggle(arg_3_0.additionBtn, false)
		triggerToggle(arg_3_0.otherBtn, false)
	end)
	arg_3_0:bind(CommanderCatScene.EVENT_FOLD, function(arg_5_0, arg_5_1)
		triggerToggle(arg_3_0.skillBtn, false)
		triggerToggle(arg_3_0.additionBtn, false)
		triggerToggle(arg_3_0.otherBtn, false)

		if arg_5_1 then
			LeanTween.moveY(rtf(arg_3_0.commanderInfo), -400, 0.5)
		else
			LeanTween.moveY(rtf(arg_3_0.commanderInfo), 71, 0.5)
		end
	end)
	arg_3_0:bind(CommanderCatScene.EVENT_PREVIEW, function(arg_6_0, arg_6_1)
		arg_3_0:UpdatePreView(arg_6_1)
	end)
	arg_3_0:bind(CommanderCatScene.EVENT_PREVIEW_PLAY, function(arg_7_0, arg_7_1, arg_7_2)
		triggerToggle(arg_3_0.skillBtn, true)

		local var_7_0 = not arg_7_1 or #arg_7_1 <= 0 or arg_7_2

		triggerToggle(arg_3_0.otherBtn, not var_7_0)
		triggerToggle(arg_3_0.additionBtn, false)
		setToggleEnabled(arg_3_0.additionBtn, false)
		arg_3_0:UpdatePreViewWithOther(arg_7_1)
	end)
	arg_3_0:bind(CommanderCatScene.EVENT_PREVIEW_ADDITION, function(arg_8_0, arg_8_1)
		triggerToggle(arg_3_0.skillBtn, true)
		triggerToggle(arg_3_0.additionBtn, true)
		arg_3_0:UpdatePreviewAddition(arg_8_1)
	end)
	arg_3_0:bind(CommanderCatDockPage.ON_SORT, function(arg_9_0, arg_9_1)
		arg_3_0:OnSort(arg_9_1)
	end)
end

function var_0_0.OnLoaded(arg_10_0)
	arg_10_0.statement = arg_10_0:findTF("detail/statement")
	arg_10_0.statement.localScale = Vector3(1, 0, 1)
	arg_10_0.talentSkill = arg_10_0:findTF("detail/talent_skill")

	local var_10_0 = arg_10_0:findTF("talent/content", arg_10_0.talentSkill)

	arg_10_0.talentList = UIItemList.New(var_10_0, var_10_0:GetChild(0))
	arg_10_0.abilityAdditionTF = arg_10_0:findTF("atttrs/content", arg_10_0.statement)
	arg_10_0.talentAdditionTF = arg_10_0:findTF("talents/scroll/content", arg_10_0.statement)
	arg_10_0.talentAdditionList = UIItemList.New(arg_10_0.talentAdditionTF, arg_10_0.talentAdditionTF:GetChild(0))
	arg_10_0.skillIcon = arg_10_0:findTF("skill/icon/Image", arg_10_0.talentSkill)
	arg_10_0.lockTF = arg_10_0:findTF("info/lock")
	arg_10_0.commanderInfo = arg_10_0:findTF("info")
	arg_10_0.expPanel = arg_10_0:findTF("exp", arg_10_0.commanderInfo)
	arg_10_0.commanderLevelTxt = arg_10_0:findTF("exp/level", arg_10_0.commanderInfo):GetComponent(typeof(Text))
	arg_10_0.commanderExpImg = arg_10_0:findTF("exp/Image", arg_10_0.commanderInfo):GetComponent(typeof(Image))
	arg_10_0.commanderNameTxt = arg_10_0:findTF("name_bg/mask/Text", arg_10_0.commanderInfo):GetComponent("ScrollText")
	arg_10_0.modifyNameBtn = arg_10_0:findTF("name_bg/modify", arg_10_0.commanderInfo)

	local var_10_1 = pg.gameset.commander_rename_open.key_value == 1

	setActive(arg_10_0.modifyNameBtn, var_10_1)

	arg_10_0.line = arg_10_0:findTF("line", arg_10_0.commanderInfo)
	arg_10_0.fleetnums = arg_10_0:findTF("line/numbers", arg_10_0.commanderInfo)
	arg_10_0.fleetTF = arg_10_0:findTF("line/fleet", arg_10_0.commanderInfo)
	arg_10_0.subTF = arg_10_0:findTF("line/sub_fleet", arg_10_0.commanderInfo)
	arg_10_0.leisureTF = arg_10_0:findTF("line/leisure", arg_10_0.commanderInfo)
	arg_10_0.labelInBattleTF = arg_10_0:findTF("line/inbattle", arg_10_0.commanderInfo)
	arg_10_0.rarityImg = arg_10_0:findTF("rarity", arg_10_0.commanderInfo):GetComponent(typeof(Image))
	arg_10_0.abilityTF = arg_10_0:findTF("ablitys", arg_10_0.commanderInfo)
	arg_10_0.skillBtn = arg_10_0:findTF("skill_btn", arg_10_0.commanderInfo)
	arg_10_0.additionBtn = arg_10_0:findTF("addition_btn", arg_10_0.commanderInfo)
	arg_10_0.otherBtn = arg_10_0:findTF("other_btn", arg_10_0.commanderInfo)
	arg_10_0.otherCommanderNameTxt = arg_10_0:findTF("detail/other/name/Text"):GetComponent(typeof(Text))
	arg_10_0.otherCommanderSkillImg = arg_10_0:findTF("detail/other/skill/Image")
	arg_10_0.otherCommanderTalentList = UIItemList.New(arg_10_0:findTF("detail/other/talent"), arg_10_0:findTF("detail/other/talent/tpl"))
	arg_10_0.otherCommanderDescTxt = arg_10_0:findTF("detail/other/desc/mask/Text"):GetComponent(typeof(ScrollText))
	arg_10_0.blurPanel = arg_10_0._parentTf.parent
	arg_10_0.blurPanelParent = arg_10_0.blurPanel.parent
	arg_10_0.renamePanel = CommanderRenamePage.New(pg.UIMgr.GetInstance().OverlayMain, arg_10_0.event)

	setText(arg_10_0:findTF("detail/statement/atttrs/title/Text"), i18n("commander_subtile_ablity"))
	setText(arg_10_0:findTF("detail/statement/talents/title/Text"), i18n("commander_subtile_talent"))
end

function var_0_0.OnInit(arg_11_0)
	arg_11_0:RegisterEvent()

	arg_11_0.isOnAddition = false
	arg_11_0.isOnSkill = false

	onToggle(arg_11_0, arg_11_0.skillBtn, function(arg_12_0)
		arg_11_0.isOnSkill = arg_12_0

		arg_11_0:Blur()

		if arg_12_0 then
			arg_11_0:emit(CommanderCatScene.EVENT_OPEN_DESC)
		end
	end, SFX_PANEL)
	onToggle(arg_11_0, arg_11_0.additionBtn, function(arg_13_0)
		arg_11_0.isOnAddition = arg_13_0
		arg_11_0.statement.localScale = arg_13_0 and Vector3(1, 1, 1) or Vector3(1, 0, 1)

		arg_11_0:Blur()

		if arg_13_0 then
			arg_11_0:emit(CommanderCatScene.EVENT_OPEN_DESC)
		end
	end, SFX_PANEL)
	onToggle(arg_11_0, arg_11_0.otherBtn, function(arg_14_0)
		arg_11_0.isOnOther = arg_14_0

		arg_11_0:Blur()

		if arg_14_0 then
			arg_11_0:emit(CommanderCatScene.EVENT_OPEN_DESC)
		end
	end, SFX_PANEL)
	onButton(arg_11_0, arg_11_0.modifyNameBtn, function()
		local var_15_0 = arg_11_0.commanderVO

		if not var_15_0:canModifyName() then
			local var_15_1 = var_15_0:getRenameTimeDesc()

			arg_11_0.contextData.msgBox:ExecuteAction("Show", {
				content = i18n("commander_rename_coldtime_tip", var_15_1)
			})
		else
			arg_11_0.renamePanel:ExecuteAction("Show", var_15_0)
		end
	end, SFX_PANEL)
end

function var_0_0.Update(arg_16_0, arg_16_1, arg_16_2)
	arg_16_0.commanderVO = arg_16_1

	arg_16_0:UpdateInfo()
	arg_16_0:UpdateTalents()
	arg_16_0:UpdateSkills()
	arg_16_0:UpdateAbilityAddition()
	arg_16_0:UpdateTalentAddition()
	arg_16_0:UpdateAbilitys()
	arg_16_0:UpdateLockState()
	arg_16_0:UpdateLevel()
	arg_16_0:UpdateStyle(arg_16_2)
	arg_16_0._tf:SetAsFirstSibling()
	arg_16_0:Show()
end

function var_0_0.UpdateLockState(arg_17_0)
	local var_17_0 = arg_17_0.commanderVO:getLock()

	setActive(arg_17_0.lockTF:Find("image"), var_17_0 == 0)
	onButton(arg_17_0, arg_17_0.lockTF, function()
		local var_18_0 = 1 - var_17_0

		arg_17_0:emit(CommanderCatMediator.LOCK, arg_17_0.commanderVO.id, var_18_0)
	end, SFX_PANEL)
end

function var_0_0.UpdateStyle(arg_19_0, arg_19_1)
	if arg_19_1 then
		triggerToggle(arg_19_0.skillBtn, true)
		triggerToggle(arg_19_0.additionBtn, true)
		setActive(arg_19_0.lockTF, false)
	end

	setButtonEnabled(arg_19_0.modifyNameBtn, not arg_19_1)
end

function var_0_0.UpdateInfo(arg_20_0)
	local var_20_0 = arg_20_0.commanderVO
	local var_20_1 = Commander.rarity2Print(var_20_0:getRarity())

	if arg_20_0.rarityPrint ~= var_20_1 then
		LoadImageSpriteAsync("CommanderRarity/" .. var_20_1, arg_20_0.rarityImg, true)

		arg_20_0.rarityPrint = var_20_1
	end

	eachChild(arg_20_0.fleetnums, function(arg_21_0)
		setActive(arg_21_0, go(arg_21_0).name == tostring(var_20_0.fleetId or ""))
	end)

	local var_20_2 = var_20_0.fleetId and not var_20_0.inBattle and var_20_0.sub
	local var_20_3 = var_20_2 and 260 or 200

	arg_20_0.line.sizeDelta = Vector2(var_20_3, arg_20_0.line.sizeDelta.y)

	setActive(arg_20_0.subTF, var_20_2)
	setActive(arg_20_0.fleetTF, var_20_0.fleetId and not var_20_0.inBattle and not var_20_0.sub)
	setActive(arg_20_0.leisureTF, not var_20_0.inFleet and not var_20_0.inBattle)
	setActive(arg_20_0.labelInBattleTF, var_20_0.inBattle)

	local var_20_4 = arg_20_0.commanderVO
	local var_20_5 = defaultValue(arg_20_0.forceDefaultName, false)

	arg_20_0.commanderNameTxt:SetText(var_20_4:getName(var_20_5))
end

function var_0_0.OnSort(arg_22_0, arg_22_1)
	local var_22_0 = arg_22_0.commanderVO
	local var_22_1 = not arg_22_1

	arg_22_0.forceDefaultName = var_22_1

	arg_22_0.commanderNameTxt:SetText(var_22_0:getName(var_22_1))
end

function var_0_0.UpdatePreView(arg_23_0, arg_23_1)
	arg_23_0:UpdateAbilitys(arg_23_1)
	arg_23_0:UpdatePreviewAddition(arg_23_1)
	arg_23_0:UpdateLevel(arg_23_1)
end

function var_0_0.UpdatePreViewWithOther(arg_24_0, arg_24_1)
	if not arg_24_1 or #arg_24_1 <= 0 then
		return
	end

	local var_24_0 = Clone(arg_24_0.commanderVO)
	local var_24_1 = CommanderCatUtil.GetSkillExpAndCommanderExp(var_24_0, arg_24_1)

	var_24_0:addExp(var_24_1)

	local var_24_2 = arg_24_1[#arg_24_1]
	local var_24_3 = getProxy(CommanderProxy):getCommanderById(var_24_2)

	arg_24_0:UpdateOtherCommander(var_24_3)
	arg_24_0:UpdateLevel(var_24_0)
	arg_24_0:UpdateAbilitys(var_24_0)
end

function var_0_0.UpdatePreviewAddition(arg_25_0, arg_25_1)
	arg_25_0:UpdateAbilityAddition(arg_25_1)
	arg_25_0:UpdateTalentAddition()
end

function var_0_0.UpdateOtherCommander(arg_26_0, arg_26_1)
	arg_26_0.otherCommanderNameTxt.text = arg_26_1:getName()

	local var_26_0 = arg_26_1:getSkills()[1]
	local var_26_1 = arg_26_1:GetDisplayTalents()

	GetImageSpriteFromAtlasAsync("commanderskillicon/" .. var_26_0:getConfig("icon"), "", arg_26_0.otherCommanderSkillImg)
	arg_26_0.otherCommanderTalentList:make(function(arg_27_0, arg_27_1, arg_27_2)
		if arg_27_0 == UIItemList.EventUpdate then
			setText(arg_27_2:Find("Text"), "")

			local var_27_0 = var_26_1[arg_27_1 + 1]

			if var_27_0 then
				arg_26_0:UpdateTalent(arg_26_1, var_27_0, arg_27_2)
				onToggle(arg_26_0, arg_27_2, function(arg_28_0)
					if arg_28_0 then
						arg_26_0.otherCommanderDescTxt:SetText(var_27_0:getConfig("desc"))
					end
				end, SFX_PANEL)

				if arg_27_1 == 0 then
					triggerToggle(arg_27_2, true)
				end
			end

			setActive(arg_27_2:Find("empty"), var_27_0 == nil)

			arg_27_2:GetComponent(typeof(Image)).enabled = var_27_0 ~= nil

			setActive(arg_27_2:Find("lock"), var_27_0 and not arg_26_1:IsLearnedTalent(var_27_0.id))
		end
	end)
	arg_26_0.otherCommanderTalentList:align(5)
end

function var_0_0.UpdateLevel(arg_29_0, arg_29_1)
	local var_29_0 = arg_29_1 or arg_29_0.commanderVO
	local var_29_1 = arg_29_1 and arg_29_1.level > arg_29_0.commanderVO.level and COLOR_GREEN or COLOR_WHITE
	local var_29_2 = setColorStr("LV." .. var_29_0.level, var_29_1)

	arg_29_0.commanderLevelTxt.text = var_29_2

	if var_29_0:isMaxLevel() then
		arg_29_0.commanderExpImg.fillAmount = 1
	else
		arg_29_0.commanderExpImg.fillAmount = var_29_0.exp / var_29_0:getNextLevelExp()
	end
end

function var_0_0.UpdateAbilitys(arg_30_0, arg_30_1)
	local var_30_0 = arg_30_0.commanderVO:getAbilitys()
	local var_30_1

	if arg_30_1 then
		var_30_1 = arg_30_1:getAbilitys()
	end

	for iter_30_0, iter_30_1 in pairs(var_30_0) do
		local var_30_2 = arg_30_0.abilityTF:Find(iter_30_0)
		local var_30_3

		if var_30_1 then
			var_30_3 = var_30_1[iter_30_0].value - iter_30_1.value

			if var_30_3 <= 0 then
				var_30_3 = nil
			end
		end

		local var_30_4 = var_30_3 and setColorStr("+" .. var_30_3, COLOR_GREEN) or " "
		local var_30_5 = var_30_2:Find("add/base")

		setText(var_30_5, iter_30_1.value)

		local var_30_6 = var_30_2:Find("add")

		setText(var_30_6, var_30_4)
	end
end

function var_0_0.UpdateAbilityAddition(arg_31_0, arg_31_1)
	local var_31_0 = arg_31_0.commanderVO:getAbilitysAddition()
	local var_31_1

	if arg_31_1 then
		var_31_1 = arg_31_1:getAbilitysAddition()
	end

	local var_31_2 = 0

	for iter_31_0, iter_31_1 in pairs(var_31_0) do
		if iter_31_1 > 0 then
			local var_31_3 = arg_31_0.abilityAdditionTF:GetChild(var_31_2)

			GetImageSpriteFromAtlasAsync("attricon", iter_31_0, var_31_3:Find("bg/icon"), false)
			setText(var_31_3:Find("bg/name"), AttributeType.Type2Name(iter_31_0))

			local var_31_4 = string.format("%0.3f", iter_31_1)

			setText(var_31_3:Find("bg/value"), ("+" .. math.floor(iter_31_1 * 1000) / 1000) .. "%")

			local var_31_5 = var_31_1 and var_31_1[iter_31_0] or iter_31_1

			setActive(var_31_3:Find("up"), var_31_5 < iter_31_1)
			setActive(var_31_3:Find("down"), iter_31_1 < var_31_5)

			var_31_2 = var_31_2 + 1
		end
	end
end

function var_0_0.UpdateTalents(arg_32_0)
	local var_32_0 = arg_32_0.commanderVO
	local var_32_1 = var_32_0:GetDisplayTalents()

	arg_32_0.talentList:make(function(arg_33_0, arg_33_1, arg_33_2)
		if arg_33_0 == UIItemList.EventUpdate then
			local var_33_0 = var_32_1[arg_33_1 + 1]

			arg_32_0:UpdateTalent(var_32_0, var_33_0, arg_33_2)
		end
	end)
	arg_32_0.talentList:align(#var_32_1)
end

function var_0_0.UpdateTalent(arg_34_0, arg_34_1, arg_34_2, arg_34_3)
	setText(arg_34_3:Find("Text"), arg_34_2:getConfig("name"))
	GetImageSpriteFromAtlasAsync("CommanderTalentIcon/" .. arg_34_2:getConfig("icon"), "", arg_34_3)

	if arg_34_3:GetComponent(typeof(Button)) then
		onButton(arg_34_0, arg_34_3, function()
			arg_34_0.contextData.treePanel:ExecuteAction("Show", arg_34_2)
		end, SFX_PANEL)
	end

	setActive(arg_34_3:Find("lock"), not arg_34_1:IsLearnedTalent(arg_34_2.id))
end

function var_0_0.UpdateTalentAddition(arg_36_0)
	local var_36_0 = arg_36_0.commanderVO
	local var_36_1
	local var_36_2 = _.values(var_36_0:getTalentsDesc())

	arg_36_0.talentAdditionList:make(function(arg_37_0, arg_37_1, arg_37_2)
		if arg_37_0 == UIItemList.EventUpdate then
			local var_37_0 = var_36_2[arg_37_1 + 1]

			setScrollText(findTF(arg_37_2, "bg/name_mask/name"), var_37_0.name)

			local var_37_1 = var_37_0.type == CommanderConst.TALENT_ADDITION_RATIO and "%" or ""

			setText(arg_37_2:Find("bg/value"), (var_37_0.value > 0 and "+" or "") .. var_37_0.value .. var_37_1)
			setActive(arg_37_2:Find("up"), false)
			setActive(arg_37_2:Find("down"), false)

			arg_37_2:Find("bg"):GetComponent(typeof(Image)).enabled = arg_37_1 % 2 ~= 0
		end
	end)
	arg_36_0.talentAdditionList:align(#var_36_2)
end

function var_0_0.UpdateSkills(arg_38_0)
	local var_38_0 = arg_38_0.commanderVO:getSkills()[1]

	GetImageSpriteFromAtlasAsync("commanderskillicon/" .. var_38_0:getConfig("icon"), "", arg_38_0.skillIcon)
	onButton(arg_38_0, arg_38_0.skillIcon, function()
		arg_38_0:emit(CommanderCatMediator.SKILL_INFO, var_38_0)
	end, SFX_PANEL)
end

function var_0_0.CanBack(arg_40_0)
	if arg_40_0.renamePanel and arg_40_0.renamePanel:GetLoaded() and arg_40_0.renamePanel:isShowing() then
		arg_40_0.renamePanel:Hide()

		return false
	end

	return true
end

function var_0_0.OnDestroy(arg_41_0)
	if arg_41_0.isBlur then
		pg.UIMgr.GetInstance():UnblurPanel(arg_41_0.blurPanel, arg_41_0.blurPanelParent)
	end

	if arg_41_0.renamePanel then
		arg_41_0.renamePanel:Destroy()

		arg_41_0.renamePanel = nil
	end
end

function var_0_0.Blur(arg_42_0)
	if arg_42_0.isOnAddition or arg_42_0.isOnSkill or arg_42_0.isOnOther then
		arg_42_0.isBlur = true

		pg.UIMgr.GetInstance():BlurPanel(arg_42_0.blurPanel)
	else
		arg_42_0.isBlur = false

		pg.UIMgr.GetInstance():UnblurPanel(arg_42_0.blurPanel, arg_42_0.blurPanelParent)
	end
end

return var_0_0
