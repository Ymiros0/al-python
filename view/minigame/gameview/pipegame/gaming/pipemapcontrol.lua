local var_0_0 = class("PipeMapControl")
local var_0_1
local var_0_2 = "left"
local var_0_3 = "right"
local var_0_4 = "top"
local var_0_5 = "bottom"
local var_0_6 = 0
local var_0_7 = 0
local var_0_8 = 1
local var_0_9 = 2
local var_0_10 = 1
local var_0_11 = 2

var_0_0.CLICK_MAP_ITEM = "click map item"

local function var_0_12(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = {
		ctor = function(arg_2_0)
			arg_2_0._itemTf = arg_1_0
			arg_2_0._index = arg_1_1
			arg_2_0._uiCamera = GameObject.Find("UICamera"):GetComponent(typeof(Camera))
			arg_2_0._canvasGroup = GetComponent(arg_2_0._itemTf, typeof(CanvasGroup))
			arg_2_0._animTf = findTF(arg_2_0._itemTf, "anim")
			arg_2_0._imgTf = findTF(arg_2_0._animTf, "img")
			arg_2_0._imgFullTf = findTF(arg_2_0._animTf, "imgFull")
			arg_2_0._animator = GetComponent(findTF(arg_2_0._itemTf, "anim"), typeof(Animator))
			arg_2_0._eventCallback = arg_1_2
			arg_2_0._freeze = false
			arg_2_0._dftEvent = GetComponent(arg_2_0._animTf, typeof(DftAniEvent))
			arg_2_0._clickTf = findTF(arg_2_0._animTf, "click")
			arg_2_0._eventTriggerListener = GetOrAddComponent(arg_2_0._clickTf, typeof(EventTriggerListener))

			arg_2_0._eventTriggerListener:AddPointDownFunc(function()
				if not arg_2_0._data and arg_2_0._eventCallback then
					arg_2_0._eventCallback(var_0_0.CLICK_MAP_ITEM, arg_2_0)
				end
			end)
		end,
		setData = function(arg_4_0, arg_4_1)
			arg_4_0._data = arg_4_1

			if arg_4_0._data then
				arg_4_0._animationFlag = false

				arg_4_0:loadImg(arg_4_0._data.img, arg_4_0._data.img_full)
				arg_4_0:setItemVisible(true)
				arg_4_0:setAlpha(1)
			else
				arg_4_0:setItemVisible(false)
			end
		end,
		getData = function(arg_5_0)
			return arg_5_0._data
		end,
		setTempData = function(arg_6_0, arg_6_1)
			if arg_6_0._data then
				warning("已经存在格子数据，无需设置预览数据")

				return
			end

			arg_6_0._tempData = arg_6_1

			arg_6_0:loadImg(arg_6_0._tempData.img, arg_6_0._tempData.img_full)
			arg_6_0:setItemVisible(true)
			arg_6_0:setAlpha(0.5)
		end,
		getTempData = function(arg_7_0)
			return arg_7_0._tempData
		end,
		loadImg = function(arg_8_0, arg_8_1, arg_8_2)
			setImageSprite(arg_8_0._imgTf, var_0_1.GetSprite(arg_8_1))
			setImageSprite(arg_8_0._imgFullTf, var_0_1.GetSprite(arg_8_2))
		end,
		setItemVisible = function(arg_9_0, arg_9_1)
			setActive(arg_9_0._imgTf, arg_9_1)
			setActive(arg_9_0._imgFullTf, arg_9_1)
		end,
		changeTempToReal = function(arg_10_0)
			if arg_10_0._tempData then
				arg_10_0:setData(arg_10_0._tempData)

				arg_10_0._tempData = nil
			end
		end,
		setTriggerName = function(arg_11_0, arg_11_1)
			if arg_11_0._animationFlag then
				return
			end

			arg_11_0._animationFlag = true

			if arg_11_0.animTriggerName then
				arg_11_0._animator:ResetTrigger(arg_11_0.animTriggerName)
			end

			arg_11_0.animTriggerName = arg_11_1
		end,
		playAnim = function(arg_12_0, arg_12_1)
			arg_12_0._success = true

			if arg_12_0.animTriggerName then
				arg_12_0._animator:SetTrigger(arg_12_0.animTriggerName)

				if arg_12_1 then
					arg_12_0._dftEvent:SetEndEvent(function()
						arg_12_1()
						arg_12_0._dftEvent:SetEndEvent(nil)
					end)
				end
			end
		end,
		getAnimationFlag = function(arg_14_0)
			return arg_14_0._animationFlag
		end,
		setVisible = function(arg_15_0, arg_15_1)
			setActive(arg_15_0._itemTf, arg_15_1)
		end,
		freeze = function(arg_16_0, arg_16_1)
			arg_16_0._freeze = arg_16_1

			arg_16_0:setVisible(not arg_16_0._freeze)
		end,
		getFreeze = function(arg_17_0)
			return arg_17_0._freeze
		end,
		getSuccess = function(arg_18_0)
			return arg_18_0._success
		end,
		setSelect = function(arg_19_0, arg_19_1)
			arg_19_0:setTempData(arg_19_1)
		end,
		setAlpha = function(arg_20_0, arg_20_1)
			arg_20_0._canvasGroup.alpha = arg_20_1
		end,
		setPosition = function(arg_21_0, arg_21_1)
			arg_21_0._itemTf.anchoredPosition = arg_21_1
		end,
		getIndex = function(arg_22_0)
			return arg_22_0._index
		end,
		clear = function(arg_23_0)
			arg_23_0._data = nil
			arg_23_0._tempData = nil
			arg_23_0._success = false

			arg_23_0:setItemVisible(false)
			arg_23_0:setAlpha(1)
		end,
		getScreenPos = function(arg_24_0, arg_24_1)
			if not arg_24_0._screenPos then
				arg_24_0:updateScreenPos()
			end

			return arg_24_0._screenPos
		end,
		updateScreenPos = function(arg_25_0)
			arg_25_0._screenPos = arg_25_0._uiCamera:WorldToScreenPoint(arg_25_0._itemTf.position)
		end,
		getDirect = function(arg_26_0)
			return arg_26_0._data.direct
		end,
		dispose = function(arg_27_0)
			ClearEventTrigger(arg_27_0._eventTriggerListener)
		end
	}

	var_1_0:ctor()

	return var_1_0
end

function var_0_0.Ctor(arg_28_0, arg_28_1, arg_28_2)
	var_0_1 = PipeGameVo
	arg_28_0._mapTf = arg_28_1
	arg_28_0._eventCallback = arg_28_2
	arg_28_0._mapItems = {}

	function arg_28_0.mapItemCallback(arg_29_0, arg_29_1)
		if var_0_0.CLICK_MAP_ITEM == arg_29_0 then
			if arg_28_0._dragTempItem then
				arg_28_0._dragTempItem:clear()

				arg_28_0._dragTempItem = nil
			end

			arg_28_0._eventCallback(PipeGameEvent.STOP_RECT_DRAG)

			if not arg_28_0._clickTempItem then
				arg_28_0._clickTempItem = arg_29_1

				arg_28_0._eventCallback(PipeGameEvent.SET_TOP_RECT)
			elseif arg_28_0._clickTempItem ~= arg_29_1 then
				arg_28_0._clickTempItem:clear()

				arg_28_0._clickTempItem = arg_29_1

				arg_28_0._eventCallback(PipeGameEvent.SET_TOP_RECT)
			elseif arg_28_0._clickTempItem:getTempData() then
				arg_28_0._clickTempItem:changeTempToReal()

				arg_28_0._clickTempItem = nil

				arg_28_0._eventCallback(PipeGameEvent.REMOVE_RECT_TOP)

				if arg_28_0:checkFull() then
					arg_28_0:startOverAniamtion()
				end
			end
		end
	end
end

function var_0_0.setClickTempItem(arg_30_0, arg_30_1)
	if arg_30_0._clickTempItem and not arg_30_0._clickTempItem:getTempData() then
		arg_30_0._clickTempItem:setTempData(arg_30_1)
	end
end

function var_0_0.start(arg_31_0)
	arg_31_0._overFlag = false
	arg_31_0._clickTempItem = nil
	arg_31_0._gameRoundData = PipeGameVo.GetRoundData()
	arg_31_0._mapBound = arg_31_0._gameRoundData.map_bound
	arg_31_0._mapSpacing = arg_31_0._gameRoundData.item_spacing
	arg_31_0._inputIndex = arg_31_0._gameRoundData.input_index
	arg_31_0._randomId = arg_31_0._gameRoundData.random_id
	arg_31_0._randomItemData = PipeGameConst.map_random_data[arg_31_0._randomId]
	findTF(arg_31_0._mapTf, "bg").sizeDelta = Vector2(arg_31_0._mapSpacing[1] * arg_31_0._mapBound[1], arg_31_0._mapSpacing[2] * arg_31_0._mapBound[2])
	arg_31_0._maxItem = arg_31_0._mapBound[1] * arg_31_0._mapBound[2]

	for iter_31_0 = 1, arg_31_0._maxItem do
		local var_31_0

		if iter_31_0 > #arg_31_0._mapItems then
			local var_31_1 = PipeGameVo.GetTplItemFromPool(PipeGameConst.tpl_map_item, arg_31_0._mapTf)
			local var_31_2 = arg_31_0:getItemPosByIndex(iter_31_0, arg_31_0._mapBound[1], arg_31_0._mapSpacing)

			var_31_0 = var_0_12(var_31_1, iter_31_0, arg_31_0.mapItemCallback)

			var_31_0:setPosition(var_31_2)
			table.insert(arg_31_0._mapItems, var_31_0)
		else
			var_31_0 = arg_31_0._mapItems[iter_31_0]
		end

		var_31_0:freeze(false)
		var_31_0:clear()
		var_31_0:setData(arg_31_0:getRandomItemByIndex(iter_31_0))
	end

	for iter_31_1 = arg_31_0._maxItem + 1, #arg_31_0._mapItems do
		arg_31_0._mapItems[iter_31_1]:freeze(true)
	end
end

function var_0_0.getRandomItemByIndex(arg_32_0, arg_32_1)
	for iter_32_0, iter_32_1 in ipairs(arg_32_0._randomItemData.list) do
		if iter_32_1[1] == arg_32_1 then
			if type(iter_32_1[2]) == "number" then
				return PipeGameConst.map_item_data[iter_32_1[2]]
			elseif type(iter_32_1[2]) == "table" then
				local var_32_0 = math.random(1, #iter_32_1[2])
				local var_32_1 = iter_32_1[2][var_32_0]

				return PipeGameConst.map_item_data[var_32_1]
			end
		end
	end

	return nil
end

function var_0_0.step(arg_33_0, arg_33_1)
	if var_0_1.draging then
		if arg_33_0._clickTempItem then
			arg_33_0._clickTempItem:clear()

			arg_33_0._clickTempItem = nil
		end

		local var_33_0 = var_0_1.dragScreenPos
		local var_33_1 = arg_33_0:getItemByScreenPos(var_33_0)

		if var_33_1 and not var_33_1:getData() then
			if arg_33_0._dragTempItem ~= var_33_1 then
				if arg_33_0._dragTempItem then
					arg_33_0._dragTempItem:clear()
				end

				arg_33_0._dragTempItem = var_33_1

				local var_33_2 = var_0_1.dragItem

				arg_33_0._dragTempItem:setTempData(var_33_2)
			end
		else
			if arg_33_0._dragTempItem then
				arg_33_0._dragTempItem:clear()
			end

			arg_33_0._dragTempItem = nil
		end

		arg_33_0._draging = var_0_1.draging
	else
		if arg_33_0._draging and arg_33_0._dragTempItem then
			arg_33_0._dragTempItem:changeTempToReal()

			arg_33_0._dragTempItem = nil

			arg_33_0._eventCallback(PipeGameEvent.REMOVE_RECT_TOP)

			if arg_33_0:checkFull() then
				arg_33_0:startOverAniamtion()
			end
		end

		arg_33_0._draging = var_0_1.draging
	end

	if var_0_1.gameDragTime <= 0 then
		arg_33_0:startOverAniamtion()
	end
end

function var_0_0.startOverAniamtion(arg_34_0)
	if arg_34_0._overFlag then
		return
	end

	arg_34_0._eventCallback(PipeGameEvent.START_SETTLEMENT)

	arg_34_0._overFlag = true
	arg_34_0._animationRound = 1

	local var_34_0 = {}
	local var_34_1 = arg_34_0:getItemByIndex(arg_34_0._inputIndex)

	if var_34_1:getData() and (var_34_1:getDirect()[2] == 0 or var_34_1:getDirect()[2] == 1) then
		var_34_1:setTriggerName(var_0_4)
		table.insert(var_34_0, var_34_1)
		arg_34_0:playOverAniamtion(var_34_0, function()
			arg_34_0._eventCallback(PipeGameEvent.PALY_ANIMATION_COMPLETE)
		end)
	else
		arg_34_0._eventCallback(PipeGameEvent.PALY_ANIMATION_COMPLETE)
	end
end

function var_0_0.getSuccessCount(arg_36_0)
	local var_36_0 = 0

	for iter_36_0 = 1, #arg_36_0._mapItems do
		local var_36_1 = arg_36_0._mapItems[iter_36_0]

		if var_36_1:getSuccess() and not var_36_1:getFreeze() then
			var_36_0 = var_36_0 + 1
		end
	end

	return var_36_0
end

function var_0_0.checkFull(arg_37_0)
	local var_37_0 = 0

	for iter_37_0 = 1, #arg_37_0._mapItems do
		if not arg_37_0._mapItems[iter_37_0]:getFreeze() and not arg_37_0._mapItems[iter_37_0]:getData() then
			var_37_0 = var_37_0 + 1
		end
	end

	return var_37_0 == 0
end

function var_0_0.playOverAniamtion(arg_38_0, arg_38_1, arg_38_2, arg_38_3)
	local var_38_0 = {}
	local var_38_1 = 0
	local var_38_2 = #arg_38_1
	local var_38_3 = arg_38_3 and arg_38_3 + 1 or 1

	local function var_38_4()
		var_38_1 = var_38_1 + 1

		if var_38_1 == var_38_2 then
			if #var_38_0 == 0 and arg_38_2 then
				arg_38_2()
			else
				arg_38_0:playOverAniamtion(var_38_0, arg_38_2, var_38_3)
			end
		end
	end

	for iter_38_0, iter_38_1 in ipairs(arg_38_1) do
		local var_38_5 = arg_38_0:getItemsByDirect(iter_38_1, var_38_3)

		arg_38_0:setItemsTriggerName(iter_38_1, var_38_5)

		for iter_38_2, iter_38_3 in ipairs(var_38_5) do
			if not table.contains(var_38_0, iter_38_3) then
				table.insert(var_38_0, iter_38_3)
			end
		end

		iter_38_1:playAnim(var_38_4)
	end
end

function var_0_0.setItemsTriggerName(arg_40_0, arg_40_1, arg_40_2)
	for iter_40_0, iter_40_1 in ipairs(arg_40_2) do
		local var_40_0 = arg_40_1:getIndex()
		local var_40_1 = iter_40_1:getIndex()
		local var_40_2

		if var_40_1 < var_40_0 then
			if var_40_1 == var_40_0 - 1 then
				var_40_2 = var_0_3
			else
				var_40_2 = var_0_5
			end
		elseif var_40_0 < var_40_1 then
			if var_40_1 == var_40_0 + 1 then
				var_40_2 = var_0_2
			else
				var_40_2 = var_0_4
			end
		end

		if var_40_2 then
			iter_40_1:setTriggerName(var_40_2)
		end
	end
end

function var_0_0.getItemsByDirect(arg_41_0, arg_41_1, arg_41_2)
	local var_41_0 = {}
	local var_41_1 = arg_41_0._mapBound[1]
	local var_41_2 = arg_41_1:getDirect()
	local var_41_3 = arg_41_1:getIndex()

	if var_41_2[1] == var_0_6 or var_41_2[1] == var_0_11 then
		table.insert(var_41_0, var_41_3 + 1)
	end

	if var_41_2[1] == var_0_6 or var_41_2[1] == var_0_10 then
		table.insert(var_41_0, var_41_3 - 1)
	end

	if var_41_2[2] == var_0_7 or var_41_2[2] == var_0_8 then
		table.insert(var_41_0, var_41_3 - arg_41_0._mapBound[1])
	end

	if var_41_2[2] == var_0_7 or var_41_2[2] == var_0_9 then
		table.insert(var_41_0, var_41_3 + arg_41_0._mapBound[1])
	end

	for iter_41_0 = #var_41_0, 1, -1 do
		local var_41_4 = arg_41_0:getItemByIndex(var_41_0[iter_41_0])

		if var_41_4 and var_41_4:getData() then
			if not arg_41_0:checkItemSuccess(var_41_3, var_41_4:getIndex(), var_41_2, var_41_4:getDirect()) then
				table.remove(var_41_0, iter_41_0)
			end
		else
			table.remove(var_41_0, iter_41_0)
		end
	end

	local var_41_5 = {}

	for iter_41_1, iter_41_2 in ipairs(var_41_0) do
		local var_41_6 = arg_41_0:getItemByIndex(iter_41_2)

		if var_41_6 and not var_41_6:getAnimationFlag() then
			table.insert(var_41_5, var_41_6)
		end
	end

	return var_41_5
end

function var_0_0.checkItemSuccess(arg_42_0, arg_42_1, arg_42_2, arg_42_3, arg_42_4)
	local var_42_0 = false
	local var_42_1 = arg_42_0._mapBound[1]
	local var_42_2 = arg_42_3[1]
	local var_42_3 = arg_42_3[2]
	local var_42_4 = arg_42_4[1]
	local var_42_5 = arg_42_4[2]

	if arg_42_2 - arg_42_1 == 1 then
		if (var_42_2 == var_0_6 or var_42_2 == var_0_11) and (var_42_4 == var_0_6 or var_42_4 == var_0_10) then
			if (arg_42_1 - 1) % var_42_1 == var_42_1 - 1 then
				var_42_0 = false
			else
				var_42_0 = true
			end
		end
	elseif arg_42_1 - arg_42_2 == 1 then
		if (var_42_2 == var_0_6 or var_42_2 == var_0_10) and (var_42_4 == var_0_6 or var_42_4 == var_0_11) then
			if (arg_42_1 - 1) % var_42_1 == 0 then
				var_42_0 = false
			else
				var_42_0 = true
			end
		end
	elseif arg_42_2 - arg_42_1 == var_42_1 then
		if (var_42_3 == var_0_7 or var_42_3 == var_0_9) and (var_42_5 == var_0_7 or var_42_5 == var_0_8) then
			var_42_0 = true
		end
	elseif arg_42_1 - arg_42_2 == var_42_1 and (var_42_3 == var_0_7 or var_42_3 == var_0_8) and (var_42_5 == var_0_7 or var_42_5 == var_0_9) then
		var_42_0 = true
	end

	return var_42_0
end

function var_0_0.getItemByIndex(arg_43_0, arg_43_1)
	return arg_43_0._mapItems[arg_43_1]
end

function var_0_0.getItemByScreenPos(arg_44_0, arg_44_1)
	local var_44_0 = arg_44_0:getScreentScaleRate()

	for iter_44_0 = 1, #arg_44_0._mapItems do
		local var_44_1 = arg_44_0._mapItems[iter_44_0]
		local var_44_2 = var_44_1:getScreenPos()

		if arg_44_1.x > var_44_2.x and arg_44_1.x < var_44_2.x + arg_44_0._mapSpacing[1] / var_44_0.x and arg_44_1.y < var_44_2.y and arg_44_1.y > var_44_2.y - arg_44_0._mapSpacing[2] / var_44_0.y then
			return var_44_1
		end
	end

	return nil
end

function var_0_0.getScreentScaleRate(arg_45_0)
	local var_45_0 = UnityEngine.Screen.width
	local var_45_1 = UnityEngine.Screen.height
	local var_45_2 = tf(GameObject.Find("UICamera/Canvas"))
	local var_45_3 = var_45_2.sizeDelta.x
	local var_45_4 = var_45_2.sizeDelta.y

	return Vector2(var_45_3 / var_45_0, var_45_4 / var_45_1)
end

function var_0_0.getItemPosByIndex(arg_46_0, arg_46_1, arg_46_2, arg_46_3)
	local var_46_0 = (arg_46_1 - 1) % arg_46_2
	local var_46_1 = math.floor((arg_46_1 - 1) / arg_46_2)

	return Vector2(var_46_0 * arg_46_3[1], -var_46_1 * arg_46_3[2])
end

function var_0_0.stop(arg_47_0)
	return
end

function var_0_0.clear(arg_48_0)
	if arg_48_0._dragTempItem then
		arg_48_0._dragTempItem:clear()

		arg_48_0._dragTempItem = nil
	end
end

function var_0_0.dispose(arg_49_0)
	return
end

return var_0_0
