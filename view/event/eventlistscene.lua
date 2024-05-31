EventConst = require("view/event/EventConst")
EventListItem = require("view/event/EventListItem")
EventDetailPanel = require("view/event/EventDetailPanel")

local var_0_0 = class("EventListScene", import("..base.BaseUI"))
local var_0_1 = {
	{
		0,
		1,
		3,
		4,
		6
	},
	{
		2,
		5
	}
}

function var_0_0.getUIName(arg_1_0)
	return "EventUI"
end

function var_0_0.init(arg_2_0)
	function arg_2_0.dispatch(...)
		arg_2_0:emit(...)
	end

	arg_2_0.blurPanel = arg_2_0:findTF("blur_panel")
	arg_2_0.lay = arg_2_0.blurPanel:Find("adapt/left_length")
	arg_2_0.topPanel = arg_2_0:findTF("blur_panel/adapt/top").gameObject
	arg_2_0.btnBack = arg_2_0:findTF("blur_panel/adapt/top/back_btn").gameObject
	arg_2_0.topLeft = arg_2_0:findTF("blur_panel/adapt/top/topLeftBg$")
	arg_2_0.topLeftBg = arg_2_0:findTF("blur_panel/adapt/top/topLeftBg$").gameObject
	arg_2_0.labelShipNums = arg_2_0:findTF("blur_panel/adapt/top/topLeftBg$/labelShipNums$"):GetComponent("Text")
	arg_2_0.mask = arg_2_0:findTF("mask$"):GetComponent("Image")
	arg_2_0.scrollItem = EventListItem.New(arg_2_0:findTF("blur_panel/scrollItem").gameObject, arg_2_0.dispatch)

	arg_2_0.scrollItem.go:SetActive(false)

	arg_2_0.detailPanel = EventDetailPanel.New(arg_2_0:findTF("detailPanel").gameObject, arg_2_0.dispatch)

	arg_2_0.detailPanel.go:SetActive(false)

	arg_2_0.scrollRectObj = arg_2_0:findTF("scrollRect$")
	arg_2_0.scrollRect = arg_2_0.scrollRectObj:GetComponent("LScrollRect")

	function arg_2_0.scrollRect.onInitItem(arg_4_0)
		arg_2_0:onInitItem(arg_4_0)
	end

	function arg_2_0.scrollRect.onUpdateItem(arg_5_0, arg_5_1)
		arg_2_0:onUpdateItem(arg_5_0, arg_5_1)
	end

	function arg_2_0.scrollRect.onReturnItem(arg_6_0, arg_6_1)
		arg_2_0:onReturnItem(arg_6_0, arg_6_1)
	end

	arg_2_0.scrollItems = {}
	arg_2_0.selectedItem = nil
	arg_2_0.rawLayouts = {}

	setImageAlpha(arg_2_0.mask, 0)

	arg_2_0.scrollRect.decelerationRate = 0.07
	arg_2_0.listEmptyTF = arg_2_0:findTF("empty")

	setActive(arg_2_0.listEmptyTF, false)

	arg_2_0.listEmptyTxt = arg_2_0:findTF("Text", arg_2_0.listEmptyTF)

	setText(arg_2_0.listEmptyTxt, i18n("list_empty_tip_eventui"))
end

local var_0_2 = {
	"daily",
	"urgency"
}

function var_0_0.didEnter(arg_7_0)
	onButton(arg_7_0, arg_7_0.btnBack, function()
		if arg_7_0.selectedItem then
			arg_7_0:easeOut(function()
				arg_7_0:emit(var_0_0.ON_BACK)
			end)
		else
			arg_7_0:emit(var_0_0.ON_BACK)
		end
	end, SFX_CANCEL)
	setActive(arg_7_0:findTF("stamp"), getProxy(TaskProxy):mingshiTouchFlagEnabled())

	if LOCK_CLICK_MINGSHI then
		setActive(arg_7_0:findTF("stamp"), false)
	end

	onButton(arg_7_0, arg_7_0:findTF("stamp"), function()
		getProxy(TaskProxy):dealMingshiTouchFlag(9)
	end, SFX_CONFIRM)

	arg_7_0.toggles = {}
	arg_7_0.toggleIndex = -1

	for iter_7_0, iter_7_1 in ipairs(var_0_2) do
		arg_7_0.toggles[iter_7_0] = arg_7_0.lay:Find("frame/scroll_rect/tagRoot/" .. iter_7_1 .. "_btn")

		onToggle(arg_7_0, arg_7_0.toggles[iter_7_0], function(arg_11_0)
			local var_11_0 = arg_7_0.toggleIndex == -1

			if arg_11_0 and arg_7_0.toggleIndex ~= iter_7_0 then
				arg_7_0.toggleIndex = iter_7_0

				if arg_7_0.selectedItem then
					pg.UIMgr.GetInstance():UnblurPanel(arg_7_0.blurPanel, arg_7_0._tf)

					local var_11_1 = arg_7_0.scrollRect.content
					local var_11_2 = var_11_1.childCount
					local var_11_3 = 1000000

					for iter_11_0 = 0, var_11_2 - 1 do
						local var_11_4 = var_11_1:GetChild(iter_11_0)

						if var_11_4 == arg_7_0.selectedItem.tr then
							var_11_3 = iter_11_0
						elseif var_11_3 < iter_11_0 then
							var_11_4:GetComponent(typeof(LayoutElement)).ignoreLayout = arg_7_0.rawLayouts[var_11_4] or false
						end
					end

					arg_7_0.rawLayouts = {}

					arg_7_0.mask.gameObject:SetActive(false)
					arg_7_0.scrollItem.go:SetActive(false)
					arg_7_0.detailPanel.go:SetActive(false)

					arg_7_0.scrollRect.enabled = true
					arg_7_0.selectedItem = nil
				end

				arg_7_0.contextData.index = iter_7_0

				arg_7_0:Flush(not var_11_0)
			end
		end)
	end

	local var_7_0 = arg_7_0.contextData.index or 1

	triggerToggle(arg_7_0.toggles[var_7_0], true)

	local function var_7_1()
		if arg_7_0.scrollItem.event.state == EventInfo.StateFinish then
			arg_7_0.dispatch(EventConst.EVENT_FINISH, arg_7_0.scrollItem.event)
		else
			arg_7_0:easeOut()
		end
	end

	onButton(arg_7_0, arg_7_0.scrollItem.bgNormal, var_7_1, SFX_PANEL)
	onButton(arg_7_0, arg_7_0.scrollItem.bgEmergence, var_7_1, SFX_PANEL)
	onButton(arg_7_0, arg_7_0.mask.gameObject, function()
		arg_7_0:easeOut()
	end, SFX_CANCEL)
	arg_7_0:ctimer()
	arg_7_0:updateBtnTip()
end

function var_0_0.onBackPressed(arg_14_0)
	pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_CANCEL)
	triggerButton(arg_14_0.btnBack)
end

function var_0_0.updateAll(arg_15_0, arg_15_1, arg_15_2, arg_15_3)
	arg_15_0.eventProxy = arg_15_1

	if arg_15_2 then
		if arg_15_0.selectedItem then
			local var_15_0 = arg_15_0.selectedItem.event.id

			if arg_15_0.eventProxy:findInfoById(var_15_0) then
				arg_15_0:updateOne(var_15_0)
			else
				arg_15_0:easeOut()
			end

			if not arg_15_3 then
				arg_15_0.invalide = true
			end
		else
			arg_15_0:Flush()
		end

		arg_15_0:updateBtnTip()
	end
end

function var_0_0.updateOne(arg_16_0, arg_16_1)
	arg_16_0.labelShipNums.text = arg_16_0.eventProxy.maxFleetNums - arg_16_0.eventProxy.busyFleetNums .. "/" .. arg_16_0.eventProxy.maxFleetNums

	for iter_16_0, iter_16_1 in pairs(arg_16_0.scrollItems) do
		if iter_16_1.event and iter_16_1.event.id == arg_16_1 then
			iter_16_1:Flush()

			break
		end
	end

	if arg_16_0.selectedItem then
		if arg_16_0.scrollItem.event and arg_16_0.scrollItem.event.id == arg_16_1 then
			arg_16_0.scrollItem:Flush()
			arg_16_0.scrollItem:UpdateTime()
		end

		if arg_16_0.detailPanel.event and arg_16_0.detailPanel.event.id == arg_16_1 then
			arg_16_0.detailPanel:Flush()
		end
	end

	arg_16_0:updateBtnTip()
end

function var_0_0.Flush(arg_17_0, arg_17_1)
	arg_17_1 = false

	if var_0_2[arg_17_0.contextData.index] == "urgency" and arg_17_0.eventProxy:checkNightEvent() then
		arg_17_0.dispatch(EventConst.EVENT_FLUSH_NIGHT)

		return
	end

	if not arg_17_1 then
		arg_17_0.labelShipNums.text = arg_17_0.eventProxy.maxFleetNums - arg_17_0.eventProxy.busyFleetNums .. "/" .. arg_17_0.eventProxy.maxFleetNums

		if arg_17_0.eventProxy.selectedEvent then
			local function var_17_0()
				local var_18_0 = arg_17_0.eventProxy.selectedEvent.id
				local var_18_1 = 1

				for iter_18_0, iter_18_1 in ipairs(arg_17_0.eventList) do
					if iter_18_1.id == var_18_0 then
						var_18_1 = iter_18_0

						break
					end
				end

				local var_18_2 = arg_17_0.scrollRect:HeadIndexToValue(var_18_1 - 1)

				arg_17_0.scrollRect:ScrollTo(var_18_2)

				for iter_18_2, iter_18_3 in pairs(arg_17_0.scrollItems) do
					if iter_18_3.event and iter_18_3.event.id == var_18_0 then
						arg_17_0.selectedItem = iter_18_3

						arg_17_0:showDetail()

						break
					end
				end

				arg_17_0.eventProxy.selectedEvent = nil

				pg.UIMgr.GetInstance():LoadingOff()
			end

			if arg_17_0.scrollRect.isStart then
				var_17_0()
			else
				arg_17_0.scrollRect.onStart = var_17_0

				pg.UIMgr.GetInstance():LoadingOn()
			end
		end
	end

	arg_17_0:filter()
	arg_17_0.scrollRect:SetTotalCount(#arg_17_0.eventList, arg_17_1 and 0 or arg_17_0.scrollRect.value)
	setActive(arg_17_0.listEmptyTF, #arg_17_0.eventList <= 0)
end

function var_0_0.filter(arg_19_0)
	arg_19_0.eventList = {}

	local var_19_0 = var_0_1[arg_19_0.contextData.index]

	for iter_19_0, iter_19_1 in ipairs(arg_19_0.eventProxy.eventList) do
		for iter_19_2, iter_19_3 in ipairs(var_19_0) do
			if iter_19_1.template.type == iter_19_3 then
				table.insert(arg_19_0.eventList, iter_19_1)

				break
			end
		end
	end

	arg_19_0.eventList = _.sort(arg_19_0.eventList, function(arg_20_0, arg_20_1)
		local var_20_0 = arg_20_0:IsActivityType() and 1 or 0
		local var_20_1 = arg_20_1:IsActivityType() and 1 or 0

		if var_20_0 == var_20_1 then
			if arg_20_0.state ~= arg_20_1.state then
				return arg_20_0.state > arg_20_1.state
			end

			if arg_20_0.template.type == 3 and arg_20_1.template.type ~= 3 then
				return true
			end

			if arg_20_0.template.type ~= 3 and arg_20_1.template.type == 3 then
				return false
			end

			return arg_20_0.id < arg_20_1.id
		else
			return var_20_1 < var_20_0
		end
	end)
end

function var_0_0.onInitItem(arg_21_0, arg_21_1)
	local var_21_0 = EventListItem.New(arg_21_1, arg_21_0.dispatch)

	local function var_21_1()
		if var_21_0.event.state == EventInfo.StateFinish then
			arg_21_0.dispatch(EventConst.EVENT_FINISH, var_21_0.event)
		else
			arg_21_0:easeIn(var_21_0)
		end
	end

	onButton(arg_21_0, var_21_0.bgNormal, var_21_1, SFX_PANEL)
	onButton(arg_21_0, var_21_0.bgEmergence, var_21_1, SFX_PANEL)

	arg_21_0.scrollItems[arg_21_1] = var_21_0
end

function var_0_0.onUpdateItem(arg_23_0, arg_23_1, arg_23_2)
	GetComponent(tf(arg_23_2), "CanvasGroup").alpha = 1

	local var_23_0 = arg_23_0.scrollItems[arg_23_2]

	if not var_23_0 then
		arg_23_0:onInitItem(arg_23_2)

		var_23_0 = arg_23_0.scrollItems[arg_23_2]
	end

	local var_23_1 = arg_23_0.eventList[arg_23_1 + 1]

	if var_23_1 then
		var_23_0:Update(arg_23_1, var_23_1)
		var_23_0:UpdateTime()
	end
end

function var_0_0.onReturnItem(arg_24_0, arg_24_1, arg_24_2)
	if arg_24_0.scrollItems and arg_24_0.scrollItems[arg_24_2] then
		arg_24_0.scrollItems[arg_24_2]:Clear()
	end
end

function var_0_0.easeIn(arg_25_0, arg_25_1)
	if not arg_25_0.easing then
		arg_25_0.easing = true
		arg_25_0.selectedItem = arg_25_1

		arg_25_0:setOpEnabled(false)
		arg_25_0:easeInDetail(function()
			pg.UIMgr.GetInstance():BlurPanel(arg_25_0.blurPanel)

			arg_25_0.easing = false

			arg_25_0:setOpEnabled(true)
		end)
	end
end

function var_0_0.easeOut(arg_27_0, arg_27_1)
	if not arg_27_0.easing then
		arg_27_0.easing = true

		arg_27_0:setOpEnabled(false)
		arg_27_0:easeOutDetail(function()
			pg.UIMgr.GetInstance():UnblurPanel(arg_27_0.blurPanel, arg_27_0._tf)

			arg_27_0.easing = false
			arg_27_0.selectedItem = nil

			arg_27_0:setOpEnabled(true)

			if arg_27_0.invalide then
				arg_27_0.invalide = false

				arg_27_0:Flush()
			end

			if arg_27_1 then
				arg_27_1()
			end
		end)
	end
end

function var_0_0.easeInDetail(arg_29_0, arg_29_1)
	local var_29_0 = 0.3
	local var_29_1 = 0.3

	arg_29_0.mask.gameObject:SetActive(true)

	arg_29_0.scrollRect.enabled = false

	local var_29_2 = arg_29_0.scrollRect.transform
	local var_29_3 = arg_29_0.scrollRect.content
	local var_29_4 = var_29_2.rect.yMax
	local var_29_5 = var_29_0 * math.abs(var_29_4 - var_29_3.localPosition.y - arg_29_0.selectedItem.tr.localPosition.y) / var_29_2.rect.height
	local var_29_6 = arg_29_0.scrollRect.value
	local var_29_7 = arg_29_0.scrollRect:HeadIndexToValue(arg_29_0.selectedItem.index)

	LeanTween.value(var_29_3.gameObject, var_29_6, var_29_7, var_29_5):setEase(LeanTweenType.easeInOutCirc):setOnUpdate(System.Action_float(function(arg_30_0)
		arg_29_0.scrollRect:SetNormalizedPosition(arg_30_0, 1)
	end)):setOnComplete(System.Action(function()
		local var_31_0 = arg_29_0.scrollItem.tr.localPosition

		var_31_0.y = var_29_4 + var_29_2.localPosition.y
		arg_29_0.scrollItem.tr.localPosition = var_31_0

		arg_29_0.scrollItem.go:SetActive(true)
		arg_29_0.scrollItem:Update(arg_29_0.selectedItem.index, arg_29_0.selectedItem.event)
		arg_29_0.scrollItem:UpdateTime()

		local var_31_1 = -347
		local var_31_2 = arg_29_0.detailPanel.tr

		var_31_2:SetParent(arg_29_0.scrollItem:findTF("maskDetail"), true)

		var_31_2.localPosition = Vector3.zero

		arg_29_0.detailPanel.go:SetActive(true)
		arg_29_0.detailPanel:Update(arg_29_0.selectedItem.index, arg_29_0.selectedItem.event)
		shiftPanel(arg_29_0.detailPanel.go, nil, -155, var_29_1, 0, true):setEase(LeanTweenType.easeInOutCirc):setOnComplete(System.Action(arg_29_1))

		local var_31_3 = var_29_3.childCount
		local var_31_4 = 100000
		local var_31_5 = {}

		for iter_31_0 = 0, var_31_3 - 1 do
			local var_31_6 = var_29_3:GetChild(iter_31_0)

			if var_31_6 == arg_29_0.selectedItem.tr then
				var_31_4 = iter_31_0
			elseif var_31_4 < iter_31_0 then
				table.insert(var_31_5, var_31_6)
			end
		end

		arg_29_0.rawLayouts = {}

		for iter_31_1, iter_31_2 in ipairs(var_31_5) do
			local var_31_7 = iter_31_2:GetComponent(typeof(LayoutElement))

			arg_29_0.rawLayouts[iter_31_2] = var_31_7.ignoreLayout
			var_31_7.ignoreLayout = true

			shiftPanel(iter_31_2, nil, iter_31_2.localPosition.y + var_31_1, var_29_1, 0, true):setEase(LeanTweenType.easeInOutCirc)
		end
	end))
end

function var_0_0.easeOutDetail(arg_32_0, arg_32_1)
	local var_32_0 = 0.2
	local var_32_1 = 268
	local var_32_2 = arg_32_0.scrollRect.content
	local var_32_3 = var_32_2.childCount
	local var_32_4 = 100000
	local var_32_5 = {}

	for iter_32_0 = 0, var_32_3 - 1 do
		local var_32_6 = var_32_2:GetChild(iter_32_0)

		if var_32_6 == arg_32_0.selectedItem.tr then
			var_32_4 = iter_32_0
		elseif var_32_4 < iter_32_0 then
			table.insert(var_32_5, var_32_6)
		end
	end

	for iter_32_1, iter_32_2 in ipairs(var_32_5) do
		shiftPanel(iter_32_2, nil, iter_32_2.localPosition.y + var_32_1, var_32_0, 0, true):setEase(LeanTweenType.easeInOutCirc)
	end

	shiftPanel(arg_32_0.detailPanel.go, nil, 129, var_32_0, 0, true):setEase(LeanTweenType.easeInOutCirc):setOnComplete(System.Action(function()
		for iter_33_0, iter_33_1 in ipairs(var_32_5) do
			iter_33_1:GetComponent(typeof(LayoutElement)).ignoreLayout = arg_32_0.rawLayouts[iter_33_1] or false
		end

		arg_32_0.rawLayouts = {}

		arg_32_0.mask.gameObject:SetActive(false)
		arg_32_0.scrollItem.go:SetActive(false)
		arg_32_0.detailPanel.go:SetActive(false)

		arg_32_0.scrollRect.enabled = true

		arg_32_1()
	end))
end

function var_0_0.showDetail(arg_34_0)
	arg_34_0.scrollRect.enabled = false

	arg_34_0.mask.gameObject:SetActive(true)

	local var_34_0 = arg_34_0.scrollRect.transform
	local var_34_1 = arg_34_0.scrollRect.content
	local var_34_2 = arg_34_0.scrollItem.tr.localPosition

	var_34_2.y = var_34_0.rect.yMax + var_34_0.localPosition.y
	arg_34_0.scrollItem.tr.localPosition = var_34_2

	arg_34_0.scrollItem.go:SetActive(true)
	arg_34_0.scrollItem:Update(arg_34_0.selectedItem.index, arg_34_0.selectedItem.event)
	arg_34_0.scrollItem:UpdateTime()

	local var_34_3 = -347
	local var_34_4 = arg_34_0.detailPanel.tr

	var_34_4:SetParent(arg_34_0.scrollItem:findTF("maskDetail"), true)

	var_34_4.anchoredPosition = Vector3.New(-1, -155, 0)

	arg_34_0.detailPanel.go:SetActive(true)
	arg_34_0.detailPanel:Update(arg_34_0.selectedItem.index, arg_34_0.selectedItem.event)

	local var_34_5 = var_34_1.childCount
	local var_34_6 = 100000

	arg_34_0.rawLayouts = {}

	for iter_34_0 = 0, var_34_5 - 1 do
		local var_34_7 = var_34_1:GetChild(iter_34_0)
		local var_34_8 = var_34_7:GetComponent(typeof(LayoutElement))

		if var_34_8.ignoreLayout or not var_34_7.gameObject.activeSelf then
			arg_34_0.rawLayouts[var_34_7] = var_34_8.ignoreLayout
		elseif var_34_7 == arg_34_0.selectedItem.tr then
			var_34_6 = iter_34_0
		elseif var_34_6 < iter_34_0 then
			arg_34_0.rawLayouts[var_34_7] = var_34_8.ignoreLayout
			var_34_8.ignoreLayout = true
			var_34_7.localPosition = var_34_7.localPosition + Vector3.New(-1, var_34_3, 0)
		end
	end

	pg.UIMgr.GetInstance():BlurPanel(arg_34_0.blurPanel)
end

function var_0_0.ctimer(arg_35_0)
	local var_35_0 = 1

	arg_35_0.timer = Timer.New(function()
		if arg_35_0.selectedItem then
			arg_35_0.scrollItem:UpdateTime()
		end

		local var_36_0 = pg.TimeMgr.GetInstance():GetServerTime()
		local var_36_1 = false

		for iter_36_0, iter_36_1 in pairs(arg_35_0.scrollItems) do
			if iter_36_1.go.name ~= "-1" then
				iter_36_1:UpdateTime()

				local var_36_2 = iter_36_1.event:GetCountDownTime()

				if var_36_2 and var_36_2 < 0 then
					local var_36_3, var_36_4 = arg_35_0.eventProxy:findInfoById(iter_36_1.event.id)

					table.remove(arg_35_0.eventProxy.eventList, var_36_4)

					var_36_1 = true
				end
			end
		end

		if var_36_1 then
			arg_35_0.dispatch(EventConst.EVENT_LIST_UPDATE)
		end
	end, var_35_0, -1, true)

	arg_35_0.timer:Start()
end

function var_0_0.ktimer(arg_37_0)
	if arg_37_0.timer then
		arg_37_0.timer:Stop()

		arg_37_0.timer = nil
	end
end

function var_0_0.setOpEnabled(arg_38_0, arg_38_1)
	_.each(arg_38_0.toggles, function(arg_39_0)
		setToggleEnabled(arg_39_0, arg_38_1)
	end)
	setButtonEnabled(arg_38_0.btnBack, arg_38_1)
end

function var_0_0.updateBtnTip(arg_40_0)
	local var_40_0 = {
		false,
		arg_40_0.eventProxy:checkNightEvent()
	}

	for iter_40_0, iter_40_1 in ipairs(arg_40_0.eventProxy.eventList) do
		if iter_40_1.state == EventInfo.StateFinish then
			var_40_0[iter_40_1.template.type] = true
		end
	end

	for iter_40_2, iter_40_3 in ipairs(arg_40_0.toggles) do
		setActive(findTF(iter_40_3, "tip"), var_40_0[iter_40_2])
	end
end

function var_0_0.willExit(arg_41_0)
	if arg_41_0.tweens then
		cancelTweens(arg_41_0.tweens)
	end

	pg.UIMgr.GetInstance():UnblurPanel(arg_41_0.blurPanel, arg_41_0._tf)
	arg_41_0:ktimer()

	for iter_41_0, iter_41_1 in pairs(arg_41_0.scrollItems) do
		iter_41_1:Clear()
	end

	arg_41_0.scrollItem:Clear()
	arg_41_0.detailPanel:Clear()
end

return var_0_0
