﻿local var_0_0 = class("EducateFavorPanel", import("...base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "EducateFavorPanel"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0.favorPanelTF = arg_2_0:findTF("favor_panel")
	arg_2_0.favorPanelAnim = arg_2_0.favorPanelTF:GetComponent(typeof(Animation))
	arg_2_0.favorPanelAnimEvent = arg_2_0.favorPanelTF:GetComponent(typeof(DftAniEvent))

	arg_2_0.favorPanelAnimEvent:SetEndEvent(function()
		setActive(arg_2_0.favorPanelTF, false)
	end)
	setActive(arg_2_0.favorPanelTF, false)

	arg_2_0.favorUIList = UIItemList.New(arg_2_0:findTF("panel/bg/view/content", arg_2_0.favorPanelTF), arg_2_0:findTF("panel/bg/view/content/tpl", arg_2_0.favorPanelTF))
	arg_2_0.favorCurTF = arg_2_0:findTF("panel/bg/cur", arg_2_0.favorPanelTF)

	pg.UIMgr.GetInstance():OverlayPanelPB(arg_2_0._tf, {
		pbList = {
			arg_2_0:findTF("panel/bg", arg_2_0.favorPanelTF)
		},
		groupName = LayerWeightConst.GROUP_EDUCATE,
		weight = LayerWeightConst.BASE_LAYER
	})
	arg_2_0:addListener()
	arg_2_0:Flush()
end

function var_0_0.addListener(arg_4_0)
	onButton(arg_4_0, arg_4_0.favorPanelTF, function()
		arg_4_0:Hide()
	end, SFX_PANEL)
	arg_4_0.favorUIList:make(function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_0 == UIItemList.EventUpdate then
			arg_4_0:updateFavorItem(arg_6_1, arg_6_2)
		end
	end)
end

function var_0_0.updateFavorPanel(arg_7_0)
	arg_7_0.char = getProxy(EducateProxy):GetCharData()

	local var_7_0 = arg_7_0.char:GetFavor()

	setText(arg_7_0:findTF("lv", arg_7_0.favorCurTF), var_7_0.lv)

	local var_7_1 = arg_7_0.char:GetFavorUpgradExp(var_7_0.lv)
	local var_7_2 = var_7_0.exp .. "/" .. var_7_1

	setText(arg_7_0:findTF("progress", arg_7_0.favorCurTF), i18n("child_favor_progress", var_7_2))
	setSlider(arg_7_0:findTF("slider", arg_7_0.favorCurTF), 0, 1, var_7_0.exp / var_7_1)
	arg_7_0.favorUIList:align(arg_7_0.char:getConfig("favor_level") - 1)
end

function var_0_0.updateFavorItem(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = arg_8_1 + 1

	setText(arg_8_0:findTF("lv", arg_8_2), var_8_0 + 1)

	local var_8_1 = var_8_0 < arg_8_0.char:GetFavor().lv

	setActive(arg_8_0:findTF("lock", arg_8_2), not var_8_1)
	setActive(arg_8_0:findTF("unlock", arg_8_2), var_8_1)

	if not var_8_1 then
		local var_8_2 = arg_8_0.char:GetFavorUpgradExp(var_8_0)

		setText(arg_8_0:findTF("Text", arg_8_2), i18n("child_favor_lock1", var_8_0 + 1))
		setTextColor(arg_8_0:findTF("Text", arg_8_2), Color.NewHex("F5F5F5"))
		setTextColor(arg_8_0:findTF("lv", arg_8_2), Color.NewHex("F5F5F5"))
	else
		local var_8_3 = arg_8_0.char:GetPerformByReplace(var_8_0)

		if var_8_3[1] then
			local var_8_4 = pg.child_performance[var_8_3[1]].param
			local var_8_5 = arg_8_0:getStoryTitle(var_8_4)

			setText(arg_8_0:findTF("Text", arg_8_2), var_8_5)
		end

		setTextColor(arg_8_0:findTF("Text", arg_8_2), Color.NewHex("393A3C"))
		setTextColor(arg_8_0:findTF("lv", arg_8_2), Color.NewHex("FFFFFF"))
		onButton(arg_8_0, arg_8_0:findTF("unlock", arg_8_2), function()
			pg.PerformMgr.GetInstance():PlayOne(var_8_3[1])
		end, SFX_PANEL)
	end
end

function var_0_0.getStoryTitle(arg_10_0, arg_10_1)
	for iter_10_0, iter_10_1 in ipairs(pg.memory_template.all) do
		local var_10_0 = pg.memory_template[iter_10_1]

		if var_10_0.story == arg_10_1 then
			return var_10_0.title
		end
	end

	return arg_10_1
end

function var_0_0.Show(arg_11_0)
	if not arg_11_0:GetLoaded() then
		return
	end

	setActive(arg_11_0.favorPanelTF, true)
	arg_11_0:updateFavorPanel()
end

function var_0_0.Hide(arg_12_0)
	arg_12_0.favorPanelAnim:Play("anim_educate_educateUI_favor_out")
end

function var_0_0.Flush(arg_13_0)
	if not arg_13_0:GetLoaded() then
		return
	end

	arg_13_0:updateFavorPanel()
end

function var_0_0.OnDestroy(arg_14_0)
	arg_14_0.favorPanelAnimEvent:SetEndEvent(nil)
	pg.UIMgr.GetInstance():UnOverlayPanel(arg_14_0._tf)
end

return var_0_0
