local var_0_0 = class("PipeRectControll")
local var_0_1
local var_0_2 = 140
local var_0_3 = 4
local var_0_4 = Vector2(0, 90)

local function var_0_5(arg_1_0, arg_1_1, arg_1_2)
	local var_1_0 = {
		def ctor:(arg_2_0)
			arg_2_0._rectItem = arg_1_0
			arg_2_0._dragContent = arg_1_1
			arg_2_0._rectImg = findTF(arg_2_0._rectItem, "img")
			arg_2_0._rectSelect = findTF(arg_2_0._rectItem, "select")
			arg_2_0._rectParent = arg_2_0._rectItem.parent
			arg_2_0._eventCallback = arg_1_2
			arg_2_0._eventTrigger = GetOrAddComponent(arg_2_0._rectItem, typeof(EventTriggerListener))
			arg_2_0._uiCamera = GameObject.Find("UICamera").GetComponent(typeof(Camera))
			arg_2_0._dragPos = Vector2(0, 0)
			arg_2_0._draging = False

			arg_2_0._eventTrigger.AddBeginDragFunc(function(arg_3_0, arg_3_1, arg_3_2)
				if var_0_1.startSettlement:
					return

				if arg_2_0._index == 1 and not arg_2_0.isTweening():
					arg_2_0._screenScaleRate = arg_2_0.getScreentScaleRate()
					arg_2_0._draging = True
					var_0_1.draging = True
					var_0_1.dragItem = arg_2_0._itemData
					var_0_1.dragScreenPos = arg_3_1.position
					arg_2_0._startDragPos = arg_3_1.position
					arg_2_0._startTfPos = arg_2_0._rectImg.anchoredPosition

					local var_3_0 = arg_2_0._uiCamera.ScreenToWorldPoint(arg_3_1.position)
					local var_3_1 = arg_2_0._rectImg.InverseTransformPoint(var_3_0)

					var_3_1.x = var_3_1.x - var_0_2 / 2
					var_3_1.y = var_3_1.y + var_0_4.y
					arg_2_0._startOffsetPos = var_3_1

					setParent(arg_2_0._rectImg, arg_2_0._dragContent, False))
			arg_2_0._eventTrigger.AddDragFunc(function(arg_4_0, arg_4_1, arg_4_2)
				if not arg_2_0._draging:
					return

				if var_0_1.startSettlement:
					arg_2_0.stopDrag()

					return

				var_0_1.dragScreenPos = Vector2(arg_4_1.position.x, arg_4_1.position.y + var_0_4.y)
				arg_2_0._dragPos.x = arg_2_0._startOffsetPos.x + (arg_4_1.position.x - arg_2_0._startDragPos.x) * arg_2_0._screenScaleRate.x
				arg_2_0._dragPos.y = arg_2_0._startOffsetPos.y + (arg_4_1.position.y - arg_2_0._startDragPos.y) * arg_2_0._screenScaleRate.y
				arg_2_0._rectImg.anchoredPosition = arg_2_0._dragPos)
			arg_2_0._eventTrigger.AddDragEndFunc(function(arg_5_0, arg_5_1, arg_5_2)
				if var_0_1.startSettlement:
					return

				if arg_2_0._index == 1:
					arg_2_0.stopDrag())
			arg_2_0.setActive(False),
		def stopDrag:(arg_6_0)
			if arg_6_0._draging:
				arg_6_0._draging = False
				var_0_1.draging = False
				var_0_1.dragItem = None
				var_0_1.dragScreenPos = None

				SetParent(arg_6_0._rectImg, arg_6_0._rectItem, False)

				if arg_6_0._startTfPos:
					arg_6_0._rectImg.anchoredPosition = Vector2(0, 0),
		def getScreentScaleRate:(arg_7_0)
			local var_7_0 = UnityEngine.Screen.width
			local var_7_1 = UnityEngine.Screen.height
			local var_7_2 = tf(GameObject.Find("UICamera/Canvas"))
			local var_7_3 = var_7_2.sizeDelta.x
			local var_7_4 = var_7_2.sizeDelta.y

			return Vector2(var_7_3 / var_7_0, var_7_4 / var_7_1),
		def setItem:(arg_8_0, arg_8_1)
			arg_8_0._itemData = arg_8_1

			if arg_8_0._itemData:
				arg_8_0.setImg(arg_8_0._itemData.img)
				arg_8_0.setActive(True)
			else
				arg_8_0.setActive(False),
		def isTweening:(arg_9_0)
			return LeanTween.isTweening(go(arg_9_0._rectItem)),
		def getItem:(arg_10_0)
			return arg_10_0._itemData,
		def setActive:(arg_11_0, arg_11_1)
			setActive(arg_11_0._rectItem, arg_11_1),
		def setIndex:(arg_12_0, arg_12_1, arg_12_2)
			if not arg_12_2:
				arg_12_0.setPostionByIndex(arg_12_1)
			else
				arg_12_0.fadeTo(arg_12_1)

			arg_12_0._index = arg_12_1

			setActive(arg_12_0._rectSelect, arg_12_1 == 1),
		def setImg:(arg_13_0, arg_13_1)
			setImageSprite(arg_13_0._rectImg, var_0_1.GetSprite(arg_13_1)),
		def fadeTo:(arg_14_0, arg_14_1)
			arg_14_0.clearTween()

			local var_14_0 = arg_14_0._rectItem.anchoredPosition.x
			local var_14_1 = arg_14_0.getIndexPosition(arg_14_1).x
			local var_14_2 = Vector2(0, arg_14_0._rectItem.anchoredPosition.y)

			LeanTween.value(go(arg_14_0._rectItem), var_14_0, var_14_1, 0.1).setOnUpdate(System.Action_float(function(arg_15_0)
				var_14_2.x = arg_15_0
				arg_14_0._rectItem.anchoredPosition = var_14_2)).setOnComplete(System.Action(function()
				return)),
		def getIndexPosition:(arg_17_0, arg_17_1)
			return Vector2(-(arg_17_1 - 1) * var_0_2, 0),
		def setPostionByIndex:(arg_18_0, arg_18_1)
			local var_18_0 = arg_18_0.getIndexPosition(arg_18_1)

			arg_18_0._rectItem.anchoredPosition = var_18_0,
		def getIndex:(arg_19_0)
			return arg_19_0._index,
		def isDraging:(arg_20_0)
			return arg_20_0._draging,
		def getDragScreenPos:(arg_21_0)
			return arg_21_0._dragScreenPos,
		def clearTween:(arg_22_0)
			if LeanTween.isTweening(go(arg_22_0._rectItem)):
				LeanTween.cancel(go(arg_22_0._rectItem)),
		def setVisible:(arg_23_0, arg_23_1)
			setActive(arg_23_0._rectItem, arg_23_1),
		def clear:(arg_24_0)
			arg_24_0._index = None
			arg_24_0._itemData = None

			arg_24_0.clearTween()
			arg_24_0.setVisible(False),
		def dispose:(arg_25_0)
			ClearEventTrigger(arg_25_0._eventTrigger)
	}

	var_1_0.ctor()

	return var_1_0

def var_0_0.Ctor(arg_26_0, arg_26_1, arg_26_2, arg_26_3):
	var_0_1 = PipeGameVo
	arg_26_0._rectTf = arg_26_1
	arg_26_0._dragPos = arg_26_2
	arg_26_0._content = findTF(arg_26_0._rectTf, "pos")
	arg_26_0._event = arg_26_3
	arg_26_0.rectItems = {}

	local function var_26_0()
		arg_26_0.onRectEventCall()

	for iter_26_0 = 1, var_0_3:
		local var_26_1 = PipeGameVo.GetTplItemFromPool(PipeGameConst.tpl_rect_item, arg_26_0._content)
		local var_26_2 = var_0_5(var_26_1, arg_26_0._dragPos, var_26_0)

		table.insert(arg_26_0.rectItems, var_26_2)

def var_0_0.start(arg_28_0):
	arg_28_0.rectDatas = arg_28_0.getRandomRectDatas()

	arg_28_0.fillRectItem()

def var_0_0.step(arg_29_0, arg_29_1):
	return

def var_0_0.stop(arg_30_0):
	return

def var_0_0.clear(arg_31_0):
	arg_31_0.rectDatas = {}

	for iter_31_0 = 1, #arg_31_0.rectItems:
		arg_31_0.rectItems[iter_31_0].clear()

	arg_31_0._draging = False

def var_0_0.fillRectItem(arg_32_0):
	if #arg_32_0.rectDatas >= 0:
		for iter_32_0 = 1, #arg_32_0.rectItems:
			local var_32_0 = arg_32_0.rectItems[iter_32_0]

			var_32_0.setIndex(iter_32_0)

			if var_32_0.getItem() == None:
				local var_32_1 = table.remove(arg_32_0.rectDatas, 1)

				var_32_0.setItem(PipeGameConst.map_item_data[var_32_1])

def var_0_0.onRectEventCall(arg_33_0, arg_33_1, arg_33_2):
	return

def var_0_0.stopTopDrag(arg_34_0):
	arg_34_0.rectItems[1].stopDrag()

def var_0_0.getTopData(arg_35_0):
	return arg_35_0.rectItems[1].getItem()

def var_0_0.removeTopRectData(arg_36_0):
	local var_36_0 = table.remove(arg_36_0.rectItems, 1)

	table.insert(arg_36_0.rectItems, var_36_0)
	var_36_0.setPostionByIndex(var_0_3 + 1, False)

	local var_36_1 = table.remove(arg_36_0.rectDatas, 1)

	var_36_0.setItem(PipeGameConst.map_item_data[var_36_1])

	for iter_36_0 = 1, #arg_36_0.rectItems:
		arg_36_0.rectItems[iter_36_0].setIndex(iter_36_0, True)

def var_0_0.getRandomRectDatas(arg_37_0):
	local var_37_0 = {}
	local var_37_1 = var_0_1.GetRoundData().id
	local var_37_2
	local var_37_3 = PipeGameConst.map_rect_data[var_37_1].list
	local var_37_4 = PipeGameConst.map_rect_list[var_37_3[math.random(1, #var_37_3)]]

	for iter_37_0, iter_37_1 in ipairs(var_37_4):
		local var_37_5 = iter_37_1[1]
		local var_37_6 = iter_37_1[2]

		for iter_37_2 = 1, var_37_6:
			table.insert(var_37_0, var_37_5)

	return arg_37_0.shuffleArray(var_37_0)

def var_0_0.shuffleArray(arg_38_0, arg_38_1):
	for iter_38_0 = #arg_38_1, 2, -1:
		local var_38_0 = math.random(iter_38_0)

		arg_38_1[iter_38_0], arg_38_1[var_38_0] = arg_38_1[var_38_0], arg_38_1[iter_38_0]

	return arg_38_1

def var_0_0.dispose(arg_39_0):
	for iter_39_0 = 1, #arg_39_0.rectItems:
		arg_39_0.rectItems[iter_39_0].dispose()

return var_0_0
