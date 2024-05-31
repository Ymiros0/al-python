﻿local var_0_0 = class("NewYearHotSpringShipSelectLayer", import("view.base.BaseUI"))
local var_0_1 = import(".NewYearHotSpringFormationCard")

function var_0_0.getUIName(arg_1_0)
	return "NewYearHotSpringShipSelectUI"
end

function var_0_0.init(arg_2_0)
	arg_2_0.counterTxt = arg_2_0:findTF("frame/top/value/Text"):GetComponent(typeof(Text))
	arg_2_0.cardContainer = arg_2_0:findTF("frame/panel")
	arg_2_0.mainPanel = arg_2_0:findTF("frame")
	arg_2_0.addShipTpl = arg_2_0.cardContainer:Find("AddShipTpl")
	arg_2_0.extendShipTpl = arg_2_0.cardContainer:Find("ExtendShipTpl")
	arg_2_0.shipCardTpl = arg_2_0.cardContainer:Find("ShipCardTpl")

	setActive(arg_2_0.addShipTpl, false)
	setActive(arg_2_0.extendShipTpl, false)
	setActive(arg_2_0.shipCardTpl, false)

	arg_2_0.cardContainer = arg_2_0.cardContainer:Find("Scroll View/Content")
	arg_2_0.shipCards = {}

	setText(arg_2_0:findTF("frame/desc"), i18n("hotspring_tip1"))
end

function var_0_0.SetActivity(arg_3_0, arg_3_1)
	arg_3_0.activity = arg_3_1
end

function var_0_0.didEnter(arg_4_0)
	arg_4_0._tf:Find("BG"):SetSiblingIndex(0)
	onButton(arg_4_0, arg_4_0._tf:Find("BG"), function()
		arg_4_0:emit(var_0_0.ON_CLOSE)
	end, SFX_PANEL)

	local function var_4_0(arg_6_0)
		setActive(arg_4_0:findTF("frame/panel/ArrowRight"), arg_6_0.x < 0.01)
		setActive(arg_4_0:findTF("frame/panel/ArrowLeft"), arg_6_0.x > 0.99)
	end

	onScroll(arg_4_0, arg_4_0.cardContainer.parent, var_4_0)
	var_4_0({
		x = 0
	})
	pg.UIMgr.GetInstance():BlurPanel(arg_4_0._tf, false, {
		weight = LayerWeightConst.BASE_LAYER
	})
	arg_4_0:UpdateSlots()
end

function var_0_0.UpdateSlots(arg_7_0)
	local var_7_0 = arg_7_0.activity
	local var_7_1 = 0
	local var_7_2 = 0

	arg_7_0:CleanCards()
	_.each(_.range(1, var_7_0:GetTotalSlotCount()), function(arg_8_0)
		local var_8_0 = var_7_0:GetShipIds()[arg_8_0] or 0
		local var_8_1 = math.clamp(arg_8_0 - var_7_0:GetSlotCount(), 0, 2)
		local var_8_2 = var_8_0 > 0 and getProxy(BayProxy):RawGetShipById(var_8_0)

		arg_7_0:AddCard(arg_8_0, var_8_1, var_8_2)

		var_7_1 = var_7_1 + (var_8_1 == 0 and 1 or 0)
		var_7_2 = var_7_2 + (var_8_2 and 1 or 0)
	end)

	arg_7_0.counterTxt.text = var_7_2 .. "/" .. var_7_1
end

function var_0_0.AddCard(arg_9_0, arg_9_1, arg_9_2, arg_9_3)
	local var_9_0

	if arg_9_2 == 0 and arg_9_3 then
		var_9_0 = cloneTplTo(arg_9_0.shipCardTpl, arg_9_0.cardContainer)

		local var_9_1 = var_9_0:Find("content")
		local var_9_2 = var_0_1.New(go(var_9_0))

		onButton(arg_9_0, var_9_1, function()
			arg_9_0:emit(NewYearHotSpringShipSelectMediator.OPEN_CHUANWU, arg_9_1, arg_9_3)
		end, SFX_PANEL)

		local var_9_3 = GetOrAddComponent(var_9_1, typeof(UILongPressTrigger))

		var_9_3.onLongPressed:RemoveAllListeners()
		var_9_3.onLongPressed:AddListener(function()
			if not arg_9_3 then
				return
			end

			arg_9_0:emit(NewYearHotSpringShipSelectMediator.LOOG_PRESS_SHIP, arg_9_1, arg_9_3)
		end)
		var_9_2:update(arg_9_3)

		local var_9_4 = arg_9_3:getRecoverEnergyPoint() + arg_9_0.activity:GetEnergyRecoverAddition()
		local var_9_5 = 0

		if arg_9_3.state == Ship.STATE_REST or arg_9_3.state == Ship.STATE_TRAIN then
			if arg_9_3.state == Ship.STATE_TRAIN then
				var_9_4 = var_9_4 + Ship.BACKYARD_1F_ENERGY_ADDITION
			elseif arg_9_3.state == Ship.STATE_REST then
				var_9_4 = var_9_4 + Ship.BACKYARD_2F_ENERGY_ADDITION
			end

			for iter_9_0, iter_9_1 in ipairs(getProxy(ActivityProxy):getBackyardEnergyActivityBuffs()) do
				var_9_5 = var_9_5 + tonumber(iter_9_1:getConfig("benefit_effect"))
			end
		end

		var_9_2:updateProps1({
			{
				i18n("word_lv"),
				arg_9_3.level
			},
			{
				i18n("word_nowenergy"),
				arg_9_3.energy
			},
			{
				i18n("word_energy_recov_speed"),
				setColorStr(10 * var_9_4, COLOR_GREEN) .. (var_9_5 > 0 and setColorStr("+" .. 10 * var_9_5, COLOR_GREEN) or "") .. "/h"
			}
		})
		setActive(var_9_2.propsTr, false)
		setActive(var_9_2.propsTr1, true)
		table.insert(arg_9_0.shipCards, {
			info = var_9_2,
			longpressedTigger = var_9_3
		})
	else
		var_9_0 = cloneTplTo(arg_9_0.extendShipTpl, arg_9_0.cardContainer)

		local var_9_6 = var_9_0:Find("content")

		setActive(var_9_6:Find("label/add"), arg_9_2 == 0)
		setActive(var_9_6:Find("label/unlock"), arg_9_2 == 1)
		setActive(var_9_6:Find("label/lock"), arg_9_2 == 2)
		setActive(var_9_6:Find("mask"), arg_9_2 == 2)

		if arg_9_2 == 0 then
			onButton(arg_9_0, var_9_6, function()
				arg_9_0:emit(NewYearHotSpringShipSelectMediator.OPEN_CHUANWU, arg_9_1)
			end, SFX_PANEL)
		elseif arg_9_2 == 1 then
			onButton(arg_9_0, var_9_6, function()
				arg_9_0:emit(NewYearHotSpringShipSelectMediator.EXTEND, arg_9_1)
			end, SFX_PANEL)
		elseif arg_9_2 == 2 then
			-- block empty
		end
	end

	setActive(var_9_0, true)
end

function var_0_0.CleanCards(arg_14_0)
	_.each(arg_14_0.shipCards, function(arg_15_0)
		arg_15_0.longpressedTigger.onLongPressed:RemoveAllListeners()
		arg_15_0.info:clear()
	end)

	arg_14_0.shipCards = {}

	removeAllChildren(arg_14_0.cardContainer)
end

function var_0_0.willExit(arg_16_0)
	pg.UIMgr.GetInstance():UnblurPanel(arg_16_0._tf)
	arg_16_0:CleanCards()
end

return var_0_0
