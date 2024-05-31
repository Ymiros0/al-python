﻿local var_0_0 = class("WorldMediaCollectionFilePreviewLayer", import("view.base.BaseUI"))

function var_0_0.__index(arg_1_0, arg_1_1)
	local var_1_0 = rawget(var_0_0, arg_1_1) or var_0_0.super[arg_1_1]

	var_1_0 = var_1_0 or WorldMediaCollectionFileDetailLayer[arg_1_1]

	return var_1_0
end

function var_0_0.getUIName(arg_2_0)
	return "WorldMediaCollectionFilePreviewUI"
end

function var_0_0.init(arg_3_0)
	arg_3_0.canvasGroup = arg_3_0._tf:GetComponent(typeof(CanvasGroup))

	arg_3_0:InitDocument()

	arg_3_0.tipTF = arg_3_0._tf:Find("Tip")
	arg_3_0.animBar = arg_3_0._tf:Find("Bar")

	setActive(arg_3_0.animBar, false)
	setActive(arg_3_0.document, false)
	setActive(arg_3_0.tipTF, false)

	arg_3_0.loader = AutoLoader.New()

	setText(arg_3_0.animBar:Find("Text"), i18n("world_collection_back"))
end

function var_0_0.didEnter(arg_4_0)
	pg.UIMgr.GetInstance():BlurPanel(arg_4_0._tf)

	local var_4_0 = WorldCollectionProxy.GetCollectionTemplate(arg_4_0.contextData.collectionId)

	arg_4_0:SetDocument(var_4_0)
	setActive(arg_4_0.animBar, true)

	local var_4_1 = arg_4_0.animBar:Find("Anim/Frame/Mask"):GetComponent(typeof(LayoutElement))
	local var_4_2 = arg_4_0.animBar:Find("Anim/Frame/Mask/Name")
	local var_4_3 = var_4_2:GetComponent(typeof(Text))

	RemoveComponent(var_4_2, typeof(ScrollText))

	local var_4_4 = var_4_1.preferredWidth

	var_4_2.pivot = Vector2(0, 0.5)
	var_4_2.anchorMin = Vector2(0, 0.5)
	var_4_2.anchorMax = Vector2(0, 0.5)
	var_4_2.anchoredPosition = Vector2.zero
	var_4_3.text = tostring(var_4_0.name or "")
	var_4_1.preferredWidth = math.min(var_4_3.preferredWidth, var_4_4)

	local function var_4_5()
		onButton(arg_4_0, arg_4_0._tf, function()
			arg_4_0:closeView()
		end)
	end

	local function var_4_6()
		if var_4_3.preferredWidth > var_4_4 then
			var_4_2.pivot = Vector2(0.5, 0.5)
			var_4_2.anchorMin = Vector2(0.5, 0.5)
			var_4_2.anchorMax = Vector2(0.5, 0.5)

			setScrollText(var_4_2, var_4_0.name or "")
		end
	end

	local var_4_7 = arg_4_0.animBar:GetComponent(typeof(DftAniEvent))

	removeOnButton(arg_4_0._tf)

	if var_4_7 then
		var_4_7:SetTriggerEvent(var_4_6)
		var_4_7:SetEndEvent(var_4_5)
	else
		var_4_6()
		var_4_5()
	end

	onButton(arg_4_0, arg_4_0.animBar:Find("Button"), function()
		setActive(arg_4_0.animBar, false)
		setActive(arg_4_0.document, true)
		setActive(arg_4_0.tipTF, true)
		var_4_5()
	end, SFX_PANEL)

	local var_4_8 = WorldCollectionProxy.GetCollectionGroup(var_4_0.id)
	local var_4_9 = WorldCollectionProxy.GetCollectionFileGroupTemplate(var_4_8)

	setImageSprite(arg_4_0.animBar:Find("Anim/Icon"), LoadSprite("ui/WorldMediaCollectionFilePreviewUI_atlas", var_4_9.type))
end

function var_0_0.willExit(arg_9_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_9_0._tf)
	arg_9_0.loader:Clear()

	local var_9_0 = arg_9_0.contextData.callback

	if var_9_0 then
		var_9_0()
	end

	var_0_0.super.willExit(arg_9_0)
end

return var_0_0
