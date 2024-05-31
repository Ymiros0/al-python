﻿local var_0_0 = class("CommanderCatPlayPage", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "CommanderCatPlayui"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.skillTF = arg_2_0:findTF("skill/frame")
	arg_2_0.skillNameTxt = arg_2_0:findTF("name", arg_2_0.skillTF):GetComponent(typeof(Text))
	arg_2_0.skillIcon = arg_2_0:findTF("icon/Image", arg_2_0.skillTF)
	arg_2_0.skillLvTxt = arg_2_0:findTF("level_container/level", arg_2_0.skillTF):GetComponent(typeof(Text))
	arg_2_0.skillAdditionTxt = arg_2_0:findTF("level_container/addition", arg_2_0.skillTF):GetComponent(typeof(Text))
	arg_2_0.expTxt = arg_2_0:findTF("exp/Text", arg_2_0.skillTF):GetComponent(typeof(Text))
	arg_2_0.descBtn = arg_2_0:findTF("skill/frame/desc")
	arg_2_0.descPage = arg_2_0:findTF("skill_desc")
	arg_2_0.descToggle = arg_2_0:findTF("tags", arg_2_0.descPage)
	arg_2_0.descToggleMark = arg_2_0.descToggle:Find("sel")
	arg_2_0.skillDescList = UIItemList.New(arg_2_0:findTF("content/list", arg_2_0.descPage), arg_2_0:findTF("content/list/tpl", arg_2_0.descPage))

	setActive(arg_2_0.descPage, false)

	arg_2_0.commanderLvTxt = arg_2_0:findTF("select_panel/exp_bg/level_bg/Text"):GetComponent(typeof(Text))
	arg_2_0.levelAdditionTxt = arg_2_0:findTF("select_panel/exp_bg/level_bg/addition"):GetComponent(typeof(Text))
	arg_2_0.preExpSlider = arg_2_0:findTF("select_panel/exp_bg/slider"):GetComponent(typeof(Slider))
	arg_2_0.expSlider = arg_2_0:findTF("select_panel/exp_bg/slider/exp"):GetComponent(typeof(Slider))
	arg_2_0.sliderExpTxt = arg_2_0:findTF("select_panel/exp_bg/slider/Text"):GetComponent(typeof(Text))
	arg_2_0.uilist = UIItemList.New(arg_2_0:findTF("select_panel/frame/list"), arg_2_0:findTF("select_panel/frame/list/commandeTF"))
	arg_2_0.consumeTxt = arg_2_0:findTF("select_panel/consume/Text"):GetComponent(typeof(Text))
	arg_2_0.confirmBtn = arg_2_0:findTF("select_panel/confirm_btn")
	arg_2_0.animation = CommanderCatPlayAnimation.New(arg_2_0.expSlider)

	setText(arg_2_0:findTF("select_panel/title"), i18n("commander_confirm_tip"))
	setText(arg_2_0:findTF("skill_desc/title"), i18n("commander_skill_effect"))
end

function var_0_0.OnInit(arg_3_0)
	arg_3_0:RegisterEvent()
	onButton(arg_3_0, arg_3_0.descBtn, function()
		if arg_3_0.isOpenDescPage then
			arg_3_0:CloseDescPage()

			arg_3_0.isOpenDescPage = false
		else
			arg_3_0.isOpenDescPage = true

			arg_3_0:UpdateDescPage()
			arg_3_0:emit(CommanderCatScene.EVENT_CLOSE_DESC)
		end

		setActive(arg_3_0.descBtn:Find("sel"), arg_3_0.isOpenDescPage)
	end, SFX_PANEL)
	setActive(arg_3_0.descBtn:Find("sel"), false)

	arg_3_0.commonFlag = true

	onButton(arg_3_0, arg_3_0.descToggle, function()
		arg_3_0.commonFlag = not arg_3_0.commonFlag

		local var_5_0 = arg_3_0.commonFlag and 0 or arg_3_0.descToggleMark.rect.width

		setAnchoredPosition(arg_3_0.descToggleMark, {
			x = var_5_0
		})
		arg_3_0:UpdateDescPage()
	end, SFX_PANEL)
end

function var_0_0.RegisterEvent(arg_6_0)
	arg_6_0:bind(CommanderCatScene.EVENT_OPEN_DESC, function(arg_7_0)
		if arg_6_0.isOpenDescPage then
			triggerButton(arg_6_0.descBtn)
		end
	end)
	arg_6_0:bind(CommanderCatScene.MSG_UPGRADE, function(arg_8_0, arg_8_1, arg_8_2)
		arg_6_0.preExpSlider.value = 0

		pg.UIMgr.GetInstance():LoadingOn(false)
		arg_6_0.animation:Action(arg_8_1, arg_8_2, function()
			pg.UIMgr.GetInstance():LoadingOff()
			arg_6_0:Flush(arg_8_2)
			arg_6_0:emit(CommanderCatScene.EVENT_UPGRADE)
		end)
	end)
	arg_6_0:bind(CommanderCatScene.EVENT_FOLD, function(arg_10_0, arg_10_1)
		if arg_10_1 then
			LeanTween.moveX(rtf(arg_6_0._tf), 1000, 0.5)
		else
			LeanTween.moveX(rtf(arg_6_0._tf), -410, 0.5)
		end
	end)
	arg_6_0:bind(CommanderCatScene.EVENT_SWITCH_PAGE, function(arg_11_0, arg_11_1)
		if arg_11_1 == CommanderCatScene.PAGE_DOCK then
			arg_6_0:ClearSortData()
		end
	end)
	arg_6_0:bind(CommanderCatScene.EVENT_SELECTED, function(arg_12_0, arg_12_1)
		arg_6_0:Flush(arg_12_1)
	end)
end

function var_0_0.Flush(arg_13_0, arg_13_1)
	arg_13_0.commander = arg_13_1
	arg_13_0.contextData.materialIds = {}

	arg_13_0:UpdateMaterials()
end

function var_0_0.Show(arg_14_0, arg_14_1)
	var_0_0.super.Show(arg_14_0)

	arg_14_0.commander = arg_14_1

	arg_14_0:UpdateMaterials()

	if arg_14_0.isOpenDescPage then
		arg_14_0:UpdateDescPage()
	end
end

function var_0_0.UpdateMaterials(arg_15_0)
	arg_15_0.uilist:make(function(arg_16_0, arg_16_1, arg_16_2)
		if arg_16_0 == UIItemList.EventUpdate then
			arg_15_0:UpdateCard(arg_16_1, arg_16_2)
		end
	end)
	arg_15_0.uilist:align(CommanderConst.PLAY_MAX_COUNT)
	arg_15_0:UpdateMainView()
end

function var_0_0.UpdateMainView(arg_17_0)
	local var_17_0 = arg_17_0.contextData.materialIds or {}
	local var_17_1, var_17_2 = CommanderCatUtil.GetSkillExpAndCommanderExp(arg_17_0.commander, var_17_0)

	arg_17_0:UpdateSkillTF(var_17_2)
	arg_17_0:UpdateCommanderTF(var_17_1)
	arg_17_0:UpdateConsume(var_17_0, var_17_2)
	setActive(go(arg_17_0.skillAdditionTxt), #var_17_0 > 0)
	setActive(go(arg_17_0.levelAdditionTxt), #var_17_0 > 0)
end

function var_0_0.UpdateDescPage(arg_18_0)
	local function var_18_0(arg_19_0, arg_19_1)
		if not arg_19_0 and arg_19_1.desc_world and arg_19_1.desc_world ~= "" then
			return arg_19_1.desc_world
		else
			return arg_19_1.desc
		end
	end

	setActive(arg_18_0.descPage, true)

	local var_18_1 = arg_18_0.commander:getSkills()[1]
	local var_18_2 = var_18_1:GetSkillGroup()
	local var_18_3 = var_18_1:getConfig("lv")

	arg_18_0.skillDescList:make(function(arg_20_0, arg_20_1, arg_20_2)
		if arg_20_0 == UIItemList.EventUpdate then
			local var_20_0 = var_18_2[arg_20_1 + 1]
			local var_20_1 = var_18_0(arg_18_0.commonFlag, var_20_0)
			local var_20_2 = var_18_3 >= var_20_0.lv and "#66472a" or "#a3a2a2"
			local var_20_3 = var_18_3 < var_20_0.lv and "(Lv." .. var_20_0.lv .. i18n("word_take_effect") .. ")" or ""

			setText(arg_20_2, "<color=" .. var_20_2 .. ">" .. var_20_1 .. "</color>" .. var_20_3)
			setText(arg_20_2:Find("level"), "<color=" .. var_20_2 .. ">" .. "Lv." .. var_20_0.lv .. "</color>")
		end
	end)
	arg_18_0.skillDescList:align(#var_18_2)
end

function var_0_0.CloseDescPage(arg_21_0)
	setActive(arg_21_0.descPage, false)
end

function var_0_0.SimulateAddSkillExp(arg_22_0, arg_22_1)
	local var_22_0 = arg_22_0.commander:getSkills()[1]
	local var_22_1 = Clone(var_22_0)

	var_22_1:addExp(arg_22_1)

	return var_22_1, var_22_0
end

function var_0_0.UpdateSkillTF(arg_23_0, arg_23_1)
	local var_23_0, var_23_1 = arg_23_0:SimulateAddSkillExp(arg_23_1)
	local var_23_2 = var_23_1:getConfig("lv")

	GetImageSpriteFromAtlasAsync("CommanderSkillIcon/" .. var_23_1:getConfig("icon"), "", arg_23_0.skillIcon)

	arg_23_0.skillNameTxt.text = var_23_1:getConfig("name")
	arg_23_0.skillLvTxt.text = "Lv." .. var_23_1:getLevel()
	arg_23_0.skillAdditionTxt.text = "+" .. var_23_0:getLevel() - var_23_1:getLevel()

	if var_23_1:isMaxLevel() then
		arg_23_0.expTxt.text = "0/0"
	else
		arg_23_0.expTxt.text = var_23_1.exp .. (arg_23_1 == 0 and "" or "<color=#A9F548FF>(+" .. arg_23_1 .. ")</color>") .. "/" .. var_23_1:getNextLevelExp()
	end
end

function var_0_0.SimulateAddCommanderExp(arg_24_0, arg_24_1)
	local var_24_0 = arg_24_0.commander
	local var_24_1 = Clone(var_24_0)

	var_24_1:addExp(arg_24_1)

	return var_24_1, var_24_0
end

function var_0_0.UpdateCommanderTF(arg_25_0, arg_25_1)
	local var_25_0, var_25_1 = arg_25_0:SimulateAddCommanderExp(arg_25_1)

	arg_25_0:emit(CommanderCatScene.EVENT_PREVIEW, var_25_0)

	arg_25_0.commanderLvTxt.text = "LV." .. var_25_1.level

	if var_25_1:isMaxLevel() then
		arg_25_0.expSlider.value = 1
		arg_25_0.sliderExpTxt.text = "EXP: +0/MAX"
		arg_25_0.preExpSlider.value = 1
		arg_25_0.levelAdditionTxt.text = "+0"
	else
		arg_25_0.expSlider.value = arg_25_1 > 0 and 0 or var_25_1.exp / var_25_1:getNextLevelExp()

		local var_25_2 = arg_25_1 > 0 and "<color=#A9F548FF>" .. var_25_1.exp + arg_25_1 .. "</color>" or var_25_1.exp

		arg_25_0.sliderExpTxt.text = "EXP: " .. var_25_2 .. "/" .. var_25_1:getNextLevelExp()

		if var_25_0:isMaxLevel() then
			arg_25_0.preExpSlider.value = 1
		else
			arg_25_0.preExpSlider.value = var_25_0.exp / var_25_0:getNextLevelExp()
		end

		arg_25_0.levelAdditionTxt.text = "+" .. var_25_0.level - var_25_1.level
	end
end

function var_0_0.UpdateConsume(arg_26_0, arg_26_1, arg_26_2)
	local var_26_0 = getProxy(PlayerProxy):getRawData()

	arg_26_0.total = CommanderCatUtil.CalcCommanderConsume(arg_26_1)
	arg_26_0.consumeTxt.text = var_26_0.gold < arg_26_0.total and "<color=" .. COLOR_RED .. ">" .. arg_26_0.total .. "</color>" or arg_26_0.total

	local function var_26_1()
		if var_26_0.gold < arg_26_0.total then
			GoShoppingMsgBox(i18n("switch_to_shop_tip_2", i18n("word_gold")), ChargeScene.TYPE_ITEM, {
				{
					59001,
					arg_26_0.total - var_26_0.gold,
					arg_26_0.total
				}
			})

			return
		end

		local var_27_0 = arg_26_0.commander:getSkills()[1]

		arg_26_0:emit(CommanderCatMediator.UPGRADE, arg_26_0.commander.id, arg_26_1, var_27_0.id)
	end

	onButton(arg_26_0, arg_26_0.confirmBtn, function()
		if not arg_26_1 or #arg_26_1 <= 0 then
			return
		end

		arg_26_0:CheckTip(arg_26_1, arg_26_2, var_26_1)
	end, SFX_PANEL)
end

function var_0_0.CheckTip(arg_29_0, arg_29_1, arg_29_2, arg_29_3)
	local var_29_0 = {}

	if CommanderCatUtil.AnySSRCommander(arg_29_1) then
		table.insert(var_29_0, function(arg_30_0)
			arg_29_0.contextData.msgBox:ExecuteAction("Show", {
				content = i18n("commander_material_is_rarity"),
				onYes = arg_30_0
			})
		end)
	end

	local var_29_1, var_29_2 = arg_29_0:SimulateAddSkillExp(arg_29_2)

	if var_29_1:isMaxLevel() and var_29_1.exp > 0 and not var_29_2:isMaxLevel() then
		table.insert(var_29_0, function(arg_31_0)
			arg_29_0.contextData.msgBox:ExecuteAction("Show", {
				content = i18n("commander_exp_overflow_tip"),
				onYes = arg_31_0
			})
		end)
	end

	if arg_29_0.commander:isMaxLevel() then
		table.insert(var_29_0, function(arg_32_0)
			arg_29_0.contextData.msgBox:ExecuteAction("Show", {
				content = i18n("commander_material_is_maxLevel"),
				onYes = arg_32_0
			})
		end)
	end

	seriesAsync(var_29_0, arg_29_3)
end

function var_0_0.UpdateCard(arg_33_0, arg_33_1, arg_33_2)
	local var_33_0 = arg_33_0.contextData.materialIds or {}
	local var_33_1 = var_33_0[arg_33_1 + 1]
	local var_33_2 = arg_33_2:Find("add")
	local var_33_3 = arg_33_2:Find("icon")

	if var_33_1 then
		onButton(arg_33_0, var_33_3, function()
			local var_34_0 = table.indexof(var_33_0, var_33_1)

			table.remove(var_33_0, var_34_0)
			arg_33_0:UpdateMaterials()
		end, SFX_PANEL)

		local var_33_4 = getProxy(CommanderProxy):getCommanderById(var_33_1)

		GetImageSpriteFromAtlasAsync("commandericon/" .. var_33_4:getPainting(), "", var_33_3)
		setActive(var_33_3:Find("up"), arg_33_0.commander:isSameGroup(var_33_4.groupId))
		setActive(var_33_3:Find("formation"), var_33_4.inFleet)
		setText(var_33_3:Find("level_bg/Text"), var_33_4.level)
	else
		onButton(arg_33_0, var_33_2, function()
			if table.getCount(getProxy(CommanderProxy):getRawData()) == 1 then
				pg.TipsMgr.GetInstance():ShowTips(i18n("commander_material_noenough"))

				return
			end

			if not arg_33_0.commander:getSkills()[1]:isMaxLevel() or not arg_33_0.commander:isMaxLevel() then
				arg_33_0:emit(CommanderCatMediator.ON_SELECT, arg_33_0:GenSelectData())
			end
		end, SFX_PANEL)
	end

	setActive(var_33_2, not var_33_1)
	setActive(var_33_3, var_33_1)
end

function var_0_0.GenSelectData(arg_36_0)
	local var_36_0 = arg_36_0.commander

	return {
		activeCommander = var_36_0,
		selectedIds = arg_36_0.contextData.materialIds or {},
		onSelected = function(arg_37_0, arg_37_1)
			arg_36_0.contextData.materialIds = arg_37_0

			arg_36_0:UpdateMaterials()
			arg_37_1()
		end,
		OnSort = function(arg_38_0)
			arg_36_0:SaveSortData(arg_38_0)
		end,
		sortData = arg_36_0:GetSortData()
	}
end

function var_0_0.Hide(arg_39_0)
	var_0_0.super.Hide(arg_39_0)
end

function var_0_0.OnDestroy(arg_40_0)
	if arg_40_0.animation then
		arg_40_0.animation:Dispose()

		arg_40_0.animation = nil
	end

	arg_40_0:ClearSortData()
end

function var_0_0.GetSortData(arg_41_0)
	if not var_0_0.SortData then
		var_0_0.SortData = Clone(arg_41_0.contextData.sortData) or {
			asc = true,
			sortData = "Rarity",
			nationData = {},
			rarityData = {}
		}
	end

	return var_0_0.SortData
end

function var_0_0.SaveSortData(arg_42_0, arg_42_1)
	var_0_0.SortData = arg_42_1
end

function var_0_0.ClearSortData(arg_43_0)
	var_0_0.SortData = nil
end

return var_0_0
