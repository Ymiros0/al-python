﻿local var_0_0 = class("EducateCharSelectPage", import("view.base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "EducateCharDockSelectUI"
end

function var_0_0.OnLoaded(arg_2_0)
	arg_2_0.titleTxt = arg_2_0:findTF("title/Text"):GetComponent(typeof(Text))
	arg_2_0.labelTxt = arg_2_0:findTF("left/label/icon"):GetComponent(typeof(Image))
	arg_2_0.paintingTr = arg_2_0:findTF("left/print/painting")
	arg_2_0.scrollrect = arg_2_0:findTF("list")
	arg_2_0.uiItemList = UIItemList.New(arg_2_0:findTF("list/content"), arg_2_0:findTF("list/content/tpl"))
	arg_2_0.dotUIItemList = UIItemList.New(arg_2_0:findTF("list/dots"), arg_2_0:findTF("list/dots/tpl"))
	arg_2_0.confirmBtn = arg_2_0:findTF("confirm_btn")
	arg_2_0.nextArr = arg_2_0:findTF("prints/next")
	arg_2_0.prevArr = arg_2_0:findTF("prints/prev")
	arg_2_0.nextPrint = arg_2_0:findTF("prints/print1")
	arg_2_0.prevPrint = arg_2_0:findTF("prints/print2")
	arg_2_0.animation = arg_2_0._tf:GetComponent(typeof(Animation))
	arg_2_0.dftAniEvent = arg_2_0._tf:GetComponent(typeof(DftAniEvent))
end

function var_0_0.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if arg_3_0.doAnim then
			return
		end

		if not arg_3_0.selectedId then
			return
		end

		arg_3_0.doAnim = true

		arg_3_0:Back(function()
			arg_3_0.doAnim = nil

			arg_3_0:emit(EducateCharDockScene.ON_CONFIRM, arg_3_0.selectedId)
		end)
	end, SFX_PANEL)
	arg_3_0:bind(EducateCharDockScene.MSG_CLEAR_TIP, function(arg_6_0, arg_6_1)
		return
	end)
end

function var_0_0.Back(arg_7_0, arg_7_1)
	arg_7_0.dftAniEvent:SetEndEvent(function(arg_8_0)
		arg_7_0.dftAniEvent:SetEndEvent(nil)
		arg_7_1()
	end)
	arg_7_0.animation:Play("anim_educate_chardockselect_out")
end

function var_0_0.Update(arg_9_0, arg_9_1, arg_9_2)
	arg_9_0.group = arg_9_1

	if arg_9_1:IsSelected(arg_9_2) then
		arg_9_0.selectedId = arg_9_2
	end

	arg_9_0.timers = {}

	arg_9_0:FlushPainting(arg_9_1:GetShowPainting())
	arg_9_0:InitLabel()
	arg_9_0:UpdateTitle()
	arg_9_0:InitList()
	arg_9_0:UpdateDots()
	arg_9_0:Show()
end

function var_0_0.UpdateTitle(arg_10_0)
	local var_10_0 = arg_10_0.group

	arg_10_0.titleTxt.text = var_10_0:GetTitle()
end

function var_0_0.InitLabel(arg_11_0)
	local var_11_0 = arg_11_0.group

	arg_11_0.labelTxt.sprite = GetSpriteFromAtlas("ui/EducateDockUI_atlas", var_11_0:GetSpriteName())

	arg_11_0.labelTxt:SetNativeSize()
end

function var_0_0.FlushPainting(arg_12_0, arg_12_1)
	arg_12_0:ReturnPainting()
	setPaintingPrefab(arg_12_0.paintingTr, arg_12_1, "tb1")

	arg_12_0.paintingName = arg_12_1
end

function var_0_0.InitList(arg_13_0)
	local var_13_0 = arg_13_0.group:GetCharIdList()

	arg_13_0:ReturnCardList()

	arg_13_0.cards = {}

	arg_13_0:RemoveAllTimer()
	arg_13_0.uiItemList:make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventUpdate then
			local var_14_0 = var_13_0[arg_14_1 + 1]

			arg_13_0:UpdateCard(arg_14_2, var_14_0, arg_14_1)

			arg_13_0.cards[var_14_0] = arg_14_2
		end
	end)
	arg_13_0.uiItemList:align(#var_13_0)

	local var_13_1 = #var_13_0 > 2

	setActive(arg_13_0.nextArr, var_13_1)
	setActive(arg_13_0.prevArr, var_13_1)
	setActive(arg_13_0.nextPrint, not var_13_1)
	setActive(arg_13_0.prevPrint, not var_13_1)
	scrollTo(arg_13_0.scrollrect, 0, 0)
end

function var_0_0.UpdateDots(arg_15_0)
	local var_15_0 = arg_15_0.group:GetCharIdList()

	arg_15_0.dotUIItemList:make(function(arg_16_0, arg_16_1, arg_16_2)
		if arg_16_0 == UIItemList.EventUpdate then
			local var_16_0 = var_15_0[arg_16_1 + 1]

			setActive(arg_16_2:Find("Image"), var_16_0 == arg_15_0.selectedId)
		end
	end)
	arg_15_0.dotUIItemList:align(#var_15_0)
end

function var_0_0.IsLockCard(arg_17_0, arg_17_1)
	local var_17_0 = getProxy(EducateProxy):GetSecretaryIDs()

	return not table.contains(var_17_0, arg_17_1)
end

function var_0_0.UpdateCard(arg_18_0, arg_18_1, arg_18_2, arg_18_3)
	local var_18_0 = arg_18_1:Find("anim_root")
	local var_18_1 = pg.secretary_special_ship[arg_18_2]

	setPaintingPrefab(var_18_0:Find("mask/painting"), var_18_1.prefab, "tb")
	setActive(var_18_0:Find("lock"), arg_18_0:IsLockCard(var_18_1.id))
	setText(var_18_0:Find("lock/desc/Text"), var_18_1.unlock_desc)

	local function var_18_2()
		setActive(var_18_0:Find("tip"), getProxy(SettingsProxy):_ShouldEducateCharTip(arg_18_2))
	end

	var_18_2()

	local function var_18_3()
		setActive(var_18_0:Find("mark"), true)

		arg_18_0.selectedId = arg_18_2

		arg_18_0:UpdateDots()
		arg_18_0:FlushPainting(var_18_1.prefab)

		arg_18_0.prevSelected = var_18_0

		arg_18_0.animation:Stop()
		arg_18_0.animation:Play("anim_educate_chardockselect_change")
	end

	onButton(arg_18_0, var_18_0, function()
		if arg_18_0:IsLockCard(arg_18_2) then
			pg.TipsMgr.GetInstance():ShowTips(i18n("secretary_special_lock_tip"))

			return
		end

		if getProxy(SettingsProxy):ClearEducateCharTip(arg_18_2) then
			var_18_2()
		end

		arg_18_0:ClearPrevSelected()

		if arg_18_0.selectedId == arg_18_2 then
			arg_18_0.selectedId = 0

			arg_18_0:UpdateDots()

			return
		end

		var_18_3()
	end, SFX_PANEL)

	if arg_18_0.selectedId == arg_18_2 then
		var_18_3()
	end

	setActive(var_18_0, false)

	arg_18_0.timers[arg_18_3] = Timer.New(function()
		setActive(var_18_0, true)
		var_18_0:GetComponent(typeof(Animation)):Play("anim_educate_chardockselect_tpl")
	end, math.max(1e-05, arg_18_3 * 0.066), 1)

	arg_18_0.timers[arg_18_3]:Start()
end

function var_0_0.RemoveAllTimer(arg_23_0)
	for iter_23_0, iter_23_1 in pairs(arg_23_0.timers) do
		iter_23_1:Stop()

		iter_23_1 = nil
	end

	arg_23_0.timers = {}
end

function var_0_0.ClearPrevSelected(arg_24_0)
	if arg_24_0.prevSelected then
		setActive(arg_24_0.prevSelected:Find("mark"), false)

		arg_24_0.prevSelected = nil
	end
end

function var_0_0.ReturnPainting(arg_25_0)
	if arg_25_0.paintingName then
		retPaintingPrefab(arg_25_0.paintingTr, arg_25_0.paintingName)

		arg_25_0.paintingName = nil
	end
end

function var_0_0.ReturnCardList(arg_26_0)
	for iter_26_0, iter_26_1 in pairs(arg_26_0.cards or {}) do
		local var_26_0 = pg.secretary_special_ship[iter_26_0]

		retPaintingPrefab(iter_26_1:Find("mask/painting"), var_26_0.prefab)
	end

	arg_26_0.cards = {}
end

function var_0_0.Hide(arg_27_0)
	var_0_0.super.Hide(arg_27_0)
	arg_27_0:ClearPrevSelected()

	arg_27_0.selectedId = nil

	arg_27_0:ReturnCardList()
	arg_27_0:RemoveAllTimer()
end

function var_0_0.OnDestroy(arg_28_0)
	arg_28_0:RemoveAllTimer()
	arg_28_0:ReturnPainting()
	arg_28_0:ReturnCardList()
	arg_28_0.dftAniEvent:SetEndEvent(nil)
end

return var_0_0
