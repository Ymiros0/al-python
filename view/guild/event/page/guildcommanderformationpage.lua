﻿local var_0_0 = class("GuildCommanderFormationPage", import("....base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "GuildCommanderFormationUI"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0.samllTF = arg_2_0:findTF("small")

	setActive(arg_2_0.samllTF, true)

	arg_2_0.pos1 = arg_2_0:findTF("small/commander1", arg_2_0.topPanel)
	arg_2_0.pos2 = arg_2_0:findTF("small/commander2", arg_2_0.topPanel)
	arg_2_0.descPanel = arg_2_0:findTF("desc")

	setActive(arg_2_0.descPanel, false)

	arg_2_0.descFrameTF = arg_2_0:findTF("desc/frame")
	arg_2_0.descPos1 = arg_2_0:findTF("commander1/frame/info", arg_2_0.descFrameTF)
	arg_2_0.descPos2 = arg_2_0:findTF("commander2/frame/info", arg_2_0.descFrameTF)
	arg_2_0.skillTFPos1 = arg_2_0:findTF("commander1/skill_info", arg_2_0.descFrameTF)
	arg_2_0.skillTFPos2 = arg_2_0:findTF("commander2/skill_info", arg_2_0.descFrameTF)
	arg_2_0.abilitysTF = UIItemList.New(arg_2_0:findTF("atttr_panel/abilitys/mask/content", arg_2_0.descFrameTF), arg_2_0:findTF("atttr_panel/abilitys/mask/content/attr", arg_2_0.descFrameTF))
	arg_2_0.talentsTF = UIItemList.New(arg_2_0:findTF("atttr_panel/talents/mask/content", arg_2_0.descFrameTF), arg_2_0:findTF("atttr_panel/talents/mask/content/attr", arg_2_0.descFrameTF))
	arg_2_0.abilityArr = arg_2_0:findTF("desc/frame/atttr_panel/abilitys/arr")
	arg_2_0.talentsArr = arg_2_0:findTF("desc/frame/atttr_panel/talents/arr")
	arg_2_0.restAllBtn = arg_2_0:findTF("rest_all", arg_2_0.descFrameTF)
	arg_2_0.quickBtn = arg_2_0:findTF("quick_btn", arg_2_0.descFrameTF)
	arg_2_0.recordPanel = arg_2_0:findTF("record_panel")
	arg_2_0.recordCommanders = {
		arg_2_0.recordPanel:Find("current/commanders/commander1/frame/info"),
		arg_2_0.recordPanel:Find("current/commanders/commander2/frame/info")
	}
	arg_2_0.reocrdSkills = {
		arg_2_0.recordPanel:Find("current/commanders/commander1/skill_info"),
		arg_2_0.recordPanel:Find("current/commanders/commander2/skill_info")
	}
	arg_2_0.recordList = UIItemList.New(arg_2_0.recordPanel:Find("record/content"), arg_2_0.recordPanel:Find("record/content/commanders"))

	onButton(arg_2_0, arg_2_0.samllTF, function()
		arg_2_0:openDescPanel()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.descPanel, function()
		arg_2_0:closeDescPanel()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.restAllBtn, function()
		if not arg_2_0.fleet:ExistAnyCommander() then
			return
		end

		arg_2_0:emit(GuildEventMediator.COMMANDER_FORMATION_OP, {
			data = {
				fleet = arg_2_0.fleet,
				type = LevelUIConst.COMMANDER_OP_REST_ALL
			},
			fleetId = arg_2_0.fleet.id
		})
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.quickBtn, function()
		arg_2_0:OpenRecordPanel()
	end, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.recordPanel:Find("back"), function()
		arg_2_0:CloseRecordPanel()
	end, SFX_PANEL)
	arg_2_0:Show()
end

function var_0_0.Update(arg_8_0, arg_8_1, arg_8_2)
	arg_8_0.fleet = arg_8_1
	arg_8_0.prefabFleets = arg_8_2

	local var_8_0 = arg_8_0.fleet:getCommanders()

	for iter_8_0 = 1, CommanderConst.MAX_FORMATION_POS do
		local var_8_1 = var_8_0[iter_8_0]

		assert(arg_8_0["pos" .. iter_8_0], "pos tf can not nil")
		arg_8_0:updateCommander(arg_8_0["pos" .. iter_8_0], iter_8_0, var_8_1)
	end

	arg_8_0:updateDesc()
	arg_8_0:updateRecordPanel()
end

function var_0_0.openDescPanel(arg_9_0, arg_9_1)
	local var_9_0 = arg_9_1 or 0.2

	if LeanTween.isTweening(go(arg_9_0.samllTF)) or LeanTween.isTweening(go(arg_9_0.descFrameTF)) then
		return
	end

	setAnchoredPosition(arg_9_0.samllTF, {
		x = -108
	})
	LeanTween.moveX(arg_9_0.samllTF, 1500, var_9_0):setOnComplete(System.Action(function()
		setActive(arg_9_0.descPanel, true)
		setAnchoredPosition(arg_9_0.descFrameTF, {
			x = 1500
		})
		LeanTween.moveX(arg_9_0.descFrameTF, -108, var_9_0)
	end))

	arg_9_0.contextData.inDescPage = true

	arg_9_0._tf:SetAsLastSibling()
end

function var_0_0.closeDescPanel(arg_11_0, arg_11_1)
	local var_11_0 = arg_11_1 or 0.2

	if LeanTween.isTweening(go(arg_11_0.samllTF)) or LeanTween.isTweening(go(arg_11_0.descFrameTF)) then
		return
	end

	setAnchoredPosition(arg_11_0.descFrameTF, {
		x = -108
	})
	LeanTween.moveX(arg_11_0.descFrameTF, 1500, var_11_0):setOnComplete(System.Action(function()
		setActive(arg_11_0.descPanel, false)
		pg.UIMgr.GetInstance():UnOverlayPanel(arg_11_0._tf, arg_11_0._parentTf)
		setAnchoredPosition(arg_11_0.samllTF, {
			x = 1500
		})
		LeanTween.moveX(arg_11_0.samllTF, -108, var_11_0)
	end))

	arg_11_0.contextData.inDescPage = false
end

function var_0_0.updateDesc(arg_13_0)
	local var_13_0 = arg_13_0.fleet:getCommanders()

	for iter_13_0 = 1, CommanderConst.MAX_FORMATION_POS do
		local var_13_1 = var_13_0[iter_13_0]

		assert(arg_13_0["pos" .. iter_13_0], "pos tf can not nil")
		arg_13_0:updateCommander(arg_13_0["descPos" .. iter_13_0], iter_13_0, var_13_1, true)
		arg_13_0:updateSkillTF(var_13_1, arg_13_0["skillTFPos" .. iter_13_0])
	end

	arg_13_0:updateAdditions()
end

function var_0_0.updateAdditions(arg_14_0)
	local var_14_0 = arg_14_0.fleet
	local var_14_1 = _.values(var_14_0:getCommandersTalentDesc())
	local var_14_2, var_14_3 = var_14_0:getCommandersAddition()

	arg_14_0.abilitysTF:make(function(arg_15_0, arg_15_1, arg_15_2)
		if arg_15_0 == UIItemList.EventUpdate then
			local var_15_0 = var_14_2[arg_15_1 + 1]

			setText(arg_15_2:Find("name"), AttributeType.Type2Name(var_15_0.attrName))
			setText(arg_15_2:Find("Text"), ("+" .. math.floor(var_15_0.value * 1000) / 1000) .. "%")
			GetImageSpriteFromAtlasAsync("attricon", var_15_0.attrName, arg_15_2:Find("icon"), false)
			setImageAlpha(arg_15_2:Find("bg"), arg_15_1 % 2)
		end
	end)
	arg_14_0.abilitysTF:align(#var_14_2)
	setActive(arg_14_0.abilityArr, #var_14_2 > 4)
	arg_14_0.talentsTF:make(function(arg_16_0, arg_16_1, arg_16_2)
		if arg_16_0 == UIItemList.EventUpdate then
			local var_16_0 = var_14_1[arg_16_1 + 1]

			setScrollText(findTF(arg_16_2, "name_mask/name"), var_16_0.name)

			local var_16_1 = var_16_0.type == CommanderConst.TALENT_ADDITION_RATIO and "%" or ""

			setText(arg_16_2:Find("Text"), (var_16_0.value > 0 and "+" or "") .. var_16_0.value .. var_16_1)
			setImageAlpha(arg_16_2:Find("bg"), arg_16_1 % 2)
		end
	end)
	arg_14_0.talentsTF:align(#var_14_1)
	setActive(arg_14_0.talentsArr, #var_14_1 > 4)
	Canvas.ForceUpdateCanvases()
end

function var_0_0.updateSkillTF(arg_17_0, arg_17_1, arg_17_2)
	setActive(arg_17_2, arg_17_1)

	if arg_17_1 then
		local var_17_0 = arg_17_1:getSkills()[1]

		GetImageSpriteFromAtlasAsync("CommanderSkillIcon/" .. var_17_0:getConfig("icon"), "", arg_17_2:Find("icon"))
		setText(arg_17_2:Find("level"), "Lv." .. var_17_0:getLevel())
		onButton(arg_17_0, arg_17_2, function()
			arg_17_0:emit(GuildEventMediator.ON_CMD_SKILL, var_17_0)
		end, SFX_PANEL)
	else
		removeOnButton(arg_17_2)
	end
end

function var_0_0.updateCommander(arg_19_0, arg_19_1, arg_19_2, arg_19_3, arg_19_4)
	local var_19_0 = arg_19_1:Find("add")
	local var_19_1 = arg_19_1:Find("info")

	if arg_19_3 then
		local var_19_2 = arg_19_1:Find("info/mask/icon")
		local var_19_3 = arg_19_1:Find("info/frame")

		GetImageSpriteFromAtlasAsync("CommanderHrz/" .. arg_19_3:getPainting(), "", var_19_2)

		local var_19_4 = arg_19_1:Find("info/name")

		if var_19_4 then
			setText(var_19_4, arg_19_3:getName())
		end

		local var_19_5 = Commander.rarity2Frame(arg_19_3:getRarity())

		setImageSprite(var_19_3, GetSpriteFromAtlas("weaponframes", "commander_" .. var_19_5))
	end

	if arg_19_4 then
		onButton(arg_19_0, var_19_1, function()
			arg_19_0:emit(GuildEventMediator.ON_SELECT_COMMANDER, arg_19_0.fleet.id, arg_19_2, arg_19_3)
		end, SFX_PANEL)
		onButton(arg_19_0, var_19_0, function()
			arg_19_0:emit(GuildEventMediator.ON_SELECT_COMMANDER, arg_19_0.fleet.id, arg_19_2, arg_19_3)
		end, SFX_PANEL)
	end

	setActive(var_19_0, not arg_19_3)
	setActive(var_19_1, arg_19_3)
end

function var_0_0.OpenRecordPanel(arg_22_0)
	setActive(arg_22_0.descFrameTF, false)
	setActive(arg_22_0.recordPanel, true)
end

function var_0_0.updateRecordPanel(arg_23_0)
	local var_23_0 = arg_23_0.fleet:getCommanders()

	for iter_23_0, iter_23_1 in ipairs(arg_23_0.recordCommanders) do
		local var_23_1 = var_23_0[iter_23_0]

		arg_23_0:updateCommander(iter_23_1, iter_23_0, var_23_1)
		arg_23_0:updateSkillTF(var_23_1, arg_23_0.reocrdSkills[iter_23_0])
	end

	arg_23_0.recordList:make(function(arg_24_0, arg_24_1, arg_24_2)
		if arg_24_0 == UIItemList.EventUpdate then
			local var_24_0 = arg_23_0.prefabFleets[arg_24_1 + 1]

			arg_23_0:UpdatePrefabFleet(var_24_0, arg_24_2, var_23_0)
		end
	end)
	arg_23_0.recordList:align(#arg_23_0.prefabFleets)
end

function var_0_0.UpdatePrefabFleet(arg_25_0, arg_25_1, arg_25_2, arg_25_3)
	local var_25_0 = arg_25_2:Find("fleet_name")
	local var_25_1 = arg_25_1:getName()

	onInputEndEdit(arg_25_0, var_25_0, function()
		local var_26_0 = getInputText(var_25_0)

		arg_25_0:emit(GuildEventMediator.COMMANDER_FORMATION_OP, {
			data = {
				fleet = arg_25_0.fleet,
				type = LevelUIConst.COMMANDER_OP_RENAME,
				id = arg_25_1.id,
				str = var_26_0,
				onFailed = function()
					setInputText(var_25_0, var_25_1)
				end
			},
			fleetId = arg_25_0.fleet.id
		})
	end)
	setInputText(var_25_0, var_25_1)
	onButton(arg_25_0, arg_25_2:Find("use_btn"), function()
		arg_25_0:emit(GuildEventMediator.COMMANDER_FORMATION_OP, {
			data = {
				fleet = arg_25_0.fleet,
				type = LevelUIConst.COMMANDER_OP_USE_PREFAB,
				id = arg_25_1.id
			},
			fleetId = arg_25_0.fleet.id
		})
		arg_25_0:CloseRecordPanel()
	end, SFX_PANEL)
	onButton(arg_25_0, arg_25_2:Find("record_btn"), function()
		arg_25_0:emit(GuildEventMediator.COMMANDER_FORMATION_OP, {
			data = {
				fleet = arg_25_0.fleet,
				type = LevelUIConst.COMMANDER_OP_RECORD_PREFAB,
				id = arg_25_1.id
			},
			fleetId = arg_25_0.fleet.id
		})
	end, SFX_PANEL)

	local var_25_2 = {
		arg_25_2:Find("commander1/frame/info"),
		arg_25_2:Find("commander2/frame/info")
	}
	local var_25_3 = {
		arg_25_2:Find("commander1/skill_info"),
		arg_25_2:Find("commander2/skill_info")
	}

	for iter_25_0, iter_25_1 in ipairs(var_25_2) do
		local var_25_4 = arg_25_1:getCommanderByPos(iter_25_0)

		arg_25_0:updateCommander(iter_25_1, iter_25_0, var_25_4)
		arg_25_0:updateSkillTF(var_25_4, var_25_3[iter_25_0])
	end
end

function var_0_0.CloseRecordPanel(arg_30_0)
	setActive(arg_30_0.descFrameTF, true)
	setActive(arg_30_0.recordPanel, false)
end

function var_0_0.OnDestroy(arg_31_0)
	if arg_31_0:isShowing() then
		LeanTween.cancel(go(arg_31_0.samllTF))
		LeanTween.cancel(go(arg_31_0.descFrameTF))
	end
end

return var_0_0
