﻿local var_0_0 = class("SSSSMedalCollectionView", import("..TemplateMV.MedalCollectionTemplateView"))
local var_0_1 = {
	"qvzhu",
	"qingxvn",
	"zhongxvn",
	"zhanlie",
	"hangmu",
	"jinghua"
}

var_0_0.INDEX_CONVERT = {
	1,
	4,
	3,
	5,
	6,
	2
}

function var_0_0.getUIName(arg_1_0)
	return "SSSSMedalCollectionUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0:FindUI()

	arg_2_0.loader = AutoLoader.New()
end

function var_0_0.FindUI(arg_3_0)
	local var_3_0 = arg_3_0:findTF("Top")

	arg_3_0.backBtn = arg_3_0:findTF("BackBtn", var_3_0)
	arg_3_0.helpBtn = arg_3_0:findTF("HelpBtn", var_3_0)
	arg_3_0.progressText = arg_3_0:findTF("ProgressText", var_3_0)
	arg_3_0.slots = {}

	for iter_3_0 = 1, 6 do
		arg_3_0.slots[iter_3_0] = {
			char = arg_3_0._tf:Find("Desk/Slot" .. iter_3_0 .. "/Char"),
			point = arg_3_0._tf:Find("Desk/Slot" .. iter_3_0 .. "/Point"),
			pointEffect = arg_3_0._tf:Find("Desk/Slot" .. iter_3_0 .. "/Dengguang"),
			selected = arg_3_0._tf:Find("Desk/Slot" .. iter_3_0 .. "/Selected"),
			saoguang = arg_3_0._tf:Find("Desk/Slot" .. iter_3_0 .. "/Saoguang")
		}
	end

	arg_3_0.medalTF = arg_3_0._tf:Find("Desk/Slot8")
	arg_3_0.infoArea1 = arg_3_0._tf:Find("Desk/Info/Area1")
	arg_3_0.infoArea2 = arg_3_0._tf:Find("Desk/Info/Area2")
	arg_3_0.infoIcon = arg_3_0.infoArea1:Find("Unlock/Icon")
end

function var_0_0.didEnter(arg_4_0)
	var_0_0.super.didEnter(arg_4_0)
	arg_4_0:AddListener()

	arg_4_0.contextData.GKIndex = arg_4_0.contextData.GKIndex or 1

	arg_4_0:UpdateView()
end

function var_0_0.AddListener(arg_5_0)
	onButton(arg_5_0, arg_5_0.backBtn, function()
		arg_5_0:closeView()
	end, SFX_CANCEL)
	onButton(arg_5_0, arg_5_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.ssss_medal_tip.tip
		})
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.infoArea1, function()
		local var_8_0 = var_0_0.INDEX_CONVERT[arg_5_0.contextData.GKIndex]
		local var_8_1 = arg_5_0.allIDList[2 * var_8_0 - 1]

		if not table.contains(arg_5_0.activeIDList, var_8_1) and table.contains(arg_5_0.activatableIDList, var_8_1) then
			arg_5_0:emit(MedalCollectionTemplateMediator.MEMORYBOOK_UNLOCK, {
				id = var_8_1,
				actId = arg_5_0.activityData.id
			})
		end
	end, SFX_PANEL)
	onButton(arg_5_0, arg_5_0.infoArea2, function()
		local var_9_0 = var_0_0.INDEX_CONVERT[arg_5_0.contextData.GKIndex]
		local var_9_1 = arg_5_0.allIDList[2 * var_9_0]

		if not table.contains(arg_5_0.activeIDList, var_9_1) and table.contains(arg_5_0.activatableIDList, var_9_1) then
			arg_5_0:emit(MedalCollectionTemplateMediator.MEMORYBOOK_UNLOCK, {
				id = var_9_1,
				actId = arg_5_0.activityData.id
			})
		end
	end, SFX_PANEL)

	for iter_5_0 = 1, 6 do
		onButton(arg_5_0, arg_5_0._tf:Find("Desk/Slot" .. iter_5_0 .. "/Click"), function()
			arg_5_0.contextData.GKIndex = iter_5_0

			arg_5_0:UpdateView()
		end, SFX_PANEL)
	end
end

function var_0_0.UpdateAfterSubmit(arg_11_0, arg_11_1)
	var_0_0.super.UpdateAfterSubmit(arg_11_0, arg_11_1)

	local var_11_0 = table.indexof(arg_11_0.allIDList, arg_11_1)
	local var_11_1 = math.floor((var_11_0 + 1) / 2)
	local var_11_2 = table.indexof(var_0_0.INDEX_CONVERT, var_11_1)

	SetCompomentEnabled(arg_11_0.slots[var_11_2].char, typeof(Image), false)
	arg_11_0:UpdateView()
	setActive(arg_11_0.slots[var_11_2].saoguang, false)
	setActive(arg_11_0.slots[var_11_2].saoguang, true)
end

function var_0_0.UpdateAfterFinalMedal(arg_12_0)
	var_0_0.super.UpdateAfterFinalMedal(arg_12_0)
	arg_12_0:UpdateView()
end

function var_0_0.UpdateView(arg_13_0)
	for iter_13_0 = 1, 6 do
		local var_13_0 = 0
		local var_13_1 = false
		local var_13_2 = var_0_0.INDEX_CONVERT[iter_13_0]

		_.each({
			arg_13_0.allIDList[2 * var_13_2 - 1],
			arg_13_0.allIDList[2 * var_13_2]
		}, function(arg_14_0)
			if table.contains(arg_13_0.activeIDList, arg_14_0) then
				var_13_0 = var_13_0 + 1
			elseif table.contains(arg_13_0.activatableIDList, arg_14_0) then
				var_13_1 = true
			end
		end)
		arg_13_0.loader:GetSpriteQuiet("ui/SSSSMedalCollectionUI_atlas", var_13_0 == 2 and "point_green" or "point_red", arg_13_0.slots[iter_13_0].point)
		SetCompomentEnabled(arg_13_0.slots[iter_13_0].point, typeof(Animator), false)
		setActive(arg_13_0.slots[iter_13_0].pointEffect, var_13_1)

		if not var_13_1 then
			setImageColor(arg_13_0.slots[iter_13_0].point, Color(1, 1, 1))
		end

		setActive(arg_13_0.slots[iter_13_0].char, var_13_0 ~= 0)

		if var_13_0 == 1 then
			arg_13_0.loader:GetSpriteQuiet("ui/SSSSMedalCollectionUI_atlas", "baimo_" .. var_0_1[var_13_2], arg_13_0.slots[iter_13_0].char)
		elseif var_13_0 == 2 then
			arg_13_0.loader:GetSpriteQuiet("ui/SSSSMedalCollectionUI_atlas", "wancheng_" .. var_0_1[var_13_2], arg_13_0.slots[iter_13_0].char)
		end

		setActive(arg_13_0.slots[iter_13_0].selected, iter_13_0 == arg_13_0.contextData.GKIndex)
	end

	local var_13_3 = #arg_13_0.activeIDList == #arg_13_0.allIDList and arg_13_0.activityData.data1 == 1

	setActive(arg_13_0.medalTF:Find("Lock"), not var_13_3)
	setActive(arg_13_0.medalTF:Find("Unlock"), var_13_3)
	arg_13_0:UpdateInfo()
	setText(arg_13_0.progressText, i18n("ssssmedal_tip", #arg_13_0.activeIDList))
end

function var_0_0.UpdateInfo(arg_15_0)
	local var_15_0 = var_0_0.INDEX_CONVERT[arg_15_0.contextData.GKIndex]

	;(function()
		local var_16_0 = arg_15_0.allIDList[2 * var_15_0 - 1]
		local var_16_1 = table.contains(arg_15_0.activeIDList, var_16_0)
		local var_16_2 = not var_16_1 and table.contains(arg_15_0.activatableIDList, var_16_0)
		local var_16_3 = not var_16_1 and not var_16_2
		local var_16_4 = arg_15_0.infoArea1

		setActive(var_16_4:Find("Lock"), var_16_3)
		setActive(var_16_4:Find("Unlockable"), var_16_2)
		setActive(var_16_4:Find("Unlock"), var_16_1)

		if var_16_1 then
			setText(var_16_4:Find("Unlock/TextName"), i18n("ssssmedal_name") .. i18n("ssssmedal_name" .. var_15_0))

			local var_16_5 = i18n("ssssmedal_belonging") .. i18n("ssssmedal_belonging" .. (var_15_0 == 6 and 2 or 1))

			setText(var_16_4:Find("Unlock/TextDetail"), var_16_5)
			arg_15_0.loader:GetSpriteQuiet("ui/SSSSMedalCollectionUI_atlas", "icon_" .. var_0_1[var_15_0], arg_15_0.infoIcon)
		elseif var_16_3 then
			local var_16_6 = arg_15_0.activityData:getConfig("config_client").unlock_desc

			setText(var_16_4:Find("Lock/BG/TextTip"), var_16_6[2 * var_15_0 - 1])
		end
	end)()
	;(function()
		local var_17_0 = arg_15_0.allIDList[2 * var_15_0]
		local var_17_1 = table.contains(arg_15_0.activeIDList, var_17_0)
		local var_17_2 = not var_17_1 and table.contains(arg_15_0.activatableIDList, var_17_0)
		local var_17_3 = not var_17_1 and not var_17_2
		local var_17_4 = arg_15_0.infoArea2

		setActive(var_17_4:Find("Lock"), var_17_3)
		setActive(var_17_4:Find("Unlockable"), var_17_2)
		setActive(var_17_4:Find("Unlock"), var_17_1)

		if var_17_1 then
			setText(var_17_4:Find("Unlock"), i18n("ssssmedal_desc" .. var_15_0))
		elseif var_17_3 then
			local var_17_5 = arg_15_0.activityData:getConfig("config_client").unlock_desc

			setText(var_17_4:Find("Lock"), var_17_5[2 * var_15_0])
		end
	end)()
end

function var_0_0.willExit(arg_18_0)
	arg_18_0.loader:Clear()
end

return var_0_0
