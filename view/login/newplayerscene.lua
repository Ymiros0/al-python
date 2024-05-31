﻿local var_0_0 = class("NewPlayerScene", import("..base.BaseUI"))
local var_0_1 = 0.5
local var_0_2 = -300
local var_0_3 = Vector3(-380, 265, 0)
local var_0_4 = 19
local var_0_5 = {
	101171,
	201211,
	401231
}
local var_0_6 = {
	[401231] = "z23",
	[101171] = "lafei",
	[301051] = "lingbo",
	[201211] = "biaoqiang"
}
local var_0_7 = {
	[101171] = i18n("login_newPlayerScene_word_laFei"),
	[201211] = i18n("login_newPlayerScene_word_biaoqiang"),
	[401231] = i18n("login_newPlayerScene_word_z23")
}

function var_0_0.getUIName(arg_1_0)
	return "NewPlayerUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.eventTriggers = {}
	arg_2_0.characters = arg_2_0:findTF("select_character/characters")
	arg_2_0.propPanel = arg_2_0:findTF("prop_panel")
	arg_2_0.selectPanel = arg_2_0:findTF("select_character")

	setActive(arg_2_0.propPanel, false)
	setActive(arg_2_0.selectPanel, true)

	arg_2_0.confirmBtn = arg_2_0:findTF("bg/qr_btn", arg_2_0.propPanel)
	arg_2_0.tip = arg_2_0:findTF("select_character/tip")
	arg_2_0.skillPanel = arg_2_0:findTF("bg/skill_panel", arg_2_0.propPanel)
	arg_2_0.skillTpl = arg_2_0:getTpl("bg/skill_panel/frame/skilltpl", arg_2_0.propPanel)
	arg_2_0.skillContainer = arg_2_0:findTF("bg/skill_panel/frame", arg_2_0.propPanel)
	arg_2_0.namedPanel = arg_2_0:findTF("named_panel")

	setActive(arg_2_0.namedPanel, false)

	arg_2_0.info = arg_2_0.namedPanel:Find("info")
	arg_2_0.nickname = arg_2_0.info:Find("nickname")
	arg_2_0.qChar = arg_2_0.propPanel:Find("q_char")
	arg_2_0.chat = arg_2_0:findTF("info/tip/chatbgtop0/Text", arg_2_0.namedPanel)
	arg_2_0.propertyPanel = PropertyPanel.New(arg_2_0.propPanel:Find("bg/property_panel/frame"))
	arg_2_0.paintTF = arg_2_0:findTF("prop_panel/bg/paint")
	arg_2_0.nameTF = arg_2_0:findTF("prop_panel/bg/name")
	arg_2_0.nameEnTF = arg_2_0:findTF("prop_panel/bg/english_name_bg")
	arg_2_0.titleShipinfoTF = arg_2_0:findTF("lines/hori/shipinfo_text")
	arg_2_0.titleShipchooseTF = arg_2_0:findTF("lines/hori/shipchoose_text")

	setImageAlpha(arg_2_0.titleShipinfoTF, 1)
	setImageAlpha(arg_2_0.titleShipchooseTF, 0)

	arg_2_0.randBtn = findTF(arg_2_0.info, "random_button")

	setActive(arg_2_0.randBtn, PLATFORM_CODE == PLATFORM_CH)
end

function var_0_0.onBackPressed(arg_3_0)
	if LeanTween.isTweening(go(arg_3_0.propPanel)) then
		return
	end

	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)

	if isActive(arg_3_0.namedPanel) then
		arg_3_0:closeNamedPanel()

		return
	end

	pg.SdkMgr.GetInstance():OnAndoridBackPress()
end

function var_0_0.switchPanel(arg_4_0)
	setActive(arg_4_0.propPanel, true)

	local var_4_0 = arg_4_0.propPanel:GetComponent(typeof(CanvasGroup))
	local var_4_1 = arg_4_0.selectPanel:GetComponent(typeof(CanvasGroup))

	LeanTween.value(go(arg_4_0.propPanel), 0, 1, 0.5):setOnUpdate(System.Action_float(function(arg_5_0)
		var_4_0.alpha = arg_5_0
		var_4_1.alpha = 1 - arg_5_0
	end)):setOnComplete(System.Action(function()
		setActive(arg_4_0.selectPanel, false)
	end))

	arg_4_0.skillPanel.localPosition = Vector3.New(-1000, arg_4_0.skillPanel.localPosition.y, arg_4_0.skillPanel.localPosition.z)

	LeanTween.moveX(arg_4_0.skillPanel, 339, 0.2)

	local var_4_2 = arg_4_0:findTF("lines/line")
	local var_4_3 = arg_4_0:findTF("lines/hori")

	LeanTween.moveY(var_4_2, -328, 0.2)
	LeanTween.moveX(var_4_3, -820, 0.2)

	for iter_4_0 = 1, 3 do
		local var_4_4 = arg_4_0:findTF("character_" .. iter_4_0, arg_4_0.characters)
		local var_4_5 = arg_4_0:findTF("bg/characters/character_" .. iter_4_0, arg_4_0.propPanel)

		setImageAlpha(var_4_4, 1)
		LeanTween.alpha(var_4_4, 0, 0.25)
		LeanTween.move(go(var_4_4), var_4_5.position, 0.3)
		setImageAlpha(arg_4_0.titleShipinfoTF, 0)
		setImageAlpha(arg_4_0.titleShipchooseTF, 1)
		LeanTween.alpha(arg_4_0.titleShipinfoTF, 1, 0.25)
		LeanTween.alpha(arg_4_0.titleShipchooseTF, 0, 0.25)
	end
end

function var_0_0.initCharacters(arg_7_0)
	arg_7_0.charInitPos = {}

	for iter_7_0 = 1, 3 do
		local var_7_0 = arg_7_0:findTF("prop_panel/bg/characters/character_" .. iter_7_0)

		onToggle(arg_7_0, var_7_0, function(arg_8_0)
			if arg_8_0 then
				arg_7_0:selectCharacterByIdx(var_7_0, var_0_5[iter_7_0])
				setActive(arg_7_0:findTF("selected", var_7_0), true)

				var_7_0:GetComponent(typeof(RectTransform)).sizeDelta = Vector2(196, 196)
			else
				setActive(arg_7_0:findTF("selected", var_7_0), false)

				var_7_0:GetComponent(typeof(RectTransform)).sizeDelta = Vector2(140, 140)
			end
		end)
	end

	local var_7_1 = {
		0.2,
		0.3,
		0.1
	}

	for iter_7_1 = 1, 3 do
		local var_7_2 = arg_7_0:findTF("character_" .. iter_7_1, arg_7_0.characters)

		onButton(arg_7_0, var_7_2, function()
			arg_7_0:switchPanel()
			triggerToggle(arg_7_0:findTF("prop_panel/bg/characters/character_" .. iter_7_1), true)
		end)

		var_7_2.localPosition = Vector3.New(var_7_2.localPosition.x, 912, var_7_2.localPosition.z)

		setImageAlpha(var_7_2, 0)
		LeanTween.alpha(var_7_2, 1, 0.3):setDelay(var_7_1[iter_7_1])
		LeanTween.moveY(var_7_2, 0, 0.2):setDelay(var_7_1[iter_7_1])
	end
end

function var_0_0.didEnter(arg_10_0)
	onButton(arg_10_0, arg_10_0.confirmBtn, function()
		arg_10_0:showNamedPanel()
	end, SFX_PANEL)
	onButton(arg_10_0, findTF(arg_10_0.info, "random_button"), function()
		local var_12_0 = require("GameCfg.names")
		local var_12_1 = var_12_0[1][math.random(#var_12_0[1])]
		local var_12_2 = var_12_0[2][math.random(#var_12_0[2])]
		local var_12_3 = var_12_0[3][math.random(#var_12_0[3])]
		local var_12_4 = var_12_0[4][math.random(#var_12_0[4])]

		setInputText(arg_10_0.nickname, var_12_1 .. var_12_2 .. var_12_3 .. var_12_4)
	end, SFX_MAIN)
	onButton(arg_10_0, findTF(arg_10_0.info, "btn_container/enter_button"), function()
		if not arg_10_0.contextData.configId then
			pg.TipsMgr.GetInstance():ShowTips(i18n("login_newPlayerScene_error_notChoiseShip"))

			return
		end

		local var_13_0 = getInputText(arg_10_0.nickname)

		if var_13_0 == "" then
			pg.TipsMgr.GetInstance():ShowTips(i18n("login_newPlayerScene_inputName"))

			return
		end

		if not nameValidityCheck(var_13_0, 4, 14, {
			"spece_illegal_tip",
			"login_newPlayerScene_name_tooShort",
			"login_newPlayerScene_name_tooLong",
			"login_newPlayerScene_invalideName"
		}) then
			return
		end

		arg_10_0.event:emit(NewPlayerMediator.ON_CREATE, var_13_0, arg_10_0.contextData.configId)
	end, SFX_CONFIRM)
	onButton(arg_10_0, findTF(arg_10_0.info, "btn_container/cancel_button"), function()
		arg_10_0:closeNamedPanel()
	end)
	arg_10_0:initCharacters()
end

local var_0_8 = 0.3
local var_0_9 = -47

function var_0_0.selectCharacterByIdx(arg_15_0, arg_15_1, arg_15_2)
	arg_15_0.inProp = true
	arg_15_0.contextData.configId = arg_15_2

	arg_15_0.propertyPanel:initProperty(arg_15_2)
	arg_15_0:initSkills()

	local var_15_0 = pg.ship_data_statistics[arg_15_2]

	setPaintingPrefab(arg_15_0.paintTF, var_0_6[arg_15_2], "chuanwu")
	setText(arg_15_0:findTF("name_mask/Text", arg_15_0.nameTF), var_15_0.name)
	setText(arg_15_0:findTF("english_name", arg_15_0.nameTF), var_15_0.english_name)
	setText(arg_15_0.nameEnTF, string.upper(var_15_0.english_name))

	local var_15_1 = Ship.New({
		configId = arg_15_0.contextData.configId
	}):getPrefab()

	if var_15_1 == arg_15_0.shipPrefab then
		return
	end

	arg_15_0:recycleSpineChar()
	pg.UIMgr.GetInstance():LoadingOn()
	PoolMgr.GetInstance():GetSpineChar(var_15_1, true, function(arg_16_0)
		pg.UIMgr.GetInstance():LoadingOff()

		arg_15_0.shipPrefab = var_15_1
		arg_15_0.shipModel = arg_16_0

		arg_16_0:GetComponent("SpineAnimUI"):SetAction("stand", 0)

		tf(arg_16_0).localScale = Vector3(0.5, 0.5, 1)
		tf(arg_16_0).localPosition = Vector3(15, -95, 0)

		pg.ViewUtils.SetLayer(tf(arg_16_0), Layer.UI)
		removeAllChildren(arg_15_0.qChar)
		SetParent(arg_16_0, arg_15_0.qChar, false)
	end)
end

function var_0_0.initSkills(arg_17_0)
	local var_17_0 = pg.ship_data_template[arg_17_0.contextData.configId]

	removeAllChildren(arg_17_0.skillContainer)

	for iter_17_0, iter_17_1 in ipairs(var_17_0.buff_list_display) do
		local var_17_1 = getSkillConfig(iter_17_1)
		local var_17_2 = table.contains(var_17_0.buff_list, iter_17_1)
		local var_17_3 = cloneTplTo(arg_17_0.skillTpl, arg_17_0.skillContainer)

		setActive(var_17_3:Find("mask"), not var_17_2)
		onButton(arg_17_0, var_17_3, function()
			arg_17_0:emit(NewPlayerMediator.ON_SKILLINFO, var_17_1.id)
		end, SFX_PANEL)
		LoadImageSpriteAsync("skillicon/" .. var_17_1.icon, findTF(var_17_3, "icon"))
	end
end

function var_0_0.showNamedPanel(arg_19_0)
	arg_19_0.qChar:SetParent(arg_19_0.info)
	pg.UIMgr.GetInstance():BlurPanel(arg_19_0.namedPanel)
	setActive(arg_19_0.namedPanel, true)
	setInputText(arg_19_0.nickname, "")
	setText(arg_19_0.chat, var_0_7[arg_19_0.contextData.configId])
end

function var_0_0.closeNamedPanel(arg_20_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_20_0.namedPanel, arg_20_0._tf)
	setActive(arg_20_0.namedPanel, false)
	arg_20_0.qChar:SetParent(arg_20_0.propPanel)
end

function var_0_0.recycleSpineChar(arg_21_0)
	if arg_21_0.shipPrefab and arg_21_0.shipModel then
		PoolMgr.GetInstance():ReturnSpineChar(arg_21_0.shipPrefab, arg_21_0.shipModel)

		arg_21_0.shipPrefab = nil
		arg_21_0.shipModel = nil
	end
end

function var_0_0.willExit(arg_22_0)
	if arg_22_0.eventTriggers then
		for iter_22_0, iter_22_1 in pairs(arg_22_0.eventTriggers) do
			ClearEventTrigger(iter_22_0)
		end

		arg_22_0.eventTriggers = nil
	end

	arg_22_0:closeNamedPanel()
end

return var_0_0
