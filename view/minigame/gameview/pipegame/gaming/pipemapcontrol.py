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
		def ctor:(arg_2_0)
			arg_2_0._itemTf = arg_1_0
			arg_2_0._index = arg_1_1
			arg_2_0._uiCamera = GameObject.Find("UICamera").GetComponent(typeof(Camera))
			arg_2_0._canvasGroup = GetComponent(arg_2_0._itemTf, typeof(CanvasGroup))
			arg_2_0._animTf = findTF(arg_2_0._itemTf, "anim")
			arg_2_0._imgTf = findTF(arg_2_0._animTf, "img")
			arg_2_0._imgFullTf = findTF(arg_2_0._animTf, "imgFull")
			arg_2_0._animator = GetComponent(findTF(arg_2_0._itemTf, "anim"), typeof(Animator))
			arg_2_0._eventCallback = arg_1_2
			arg_2_0._freeze = False
			arg_2_0._dftEvent = GetComponent(arg_2_0._animTf, typeof(DftAniEvent))
			arg_2_0._clickTf = findTF(arg_2_0._animTf, "click")
			arg_2_0._eventTriggerListener = GetOrAddComponent(arg_2_0._clickTf, typeof(EventTriggerListener))

			arg_2_0._eventTriggerListener.AddPointDownFunc(function()
				if not arg_2_0._data and arg_2_0._eventCallback:
					arg_2_0._eventCallback(var_0_0.CLICK_MAP_ITEM, arg_2_0)),
		def setData:(arg_4_0, arg_4_1)
			arg_4_0._data = arg_4_1

			if arg_4_0._data:
				arg_4_0._animationFlag = False

				arg_4_0.loadImg(arg_4_0._data.img, arg_4_0._data.img_full)
				arg_4_0.setItemVisible(True)
				arg_4_0.setAlpha(1)
			else
				arg_4_0.setItemVisible(False),
		def getData:(arg_5_0)
			return arg_5_0._data,
		def setTempData:(arg_6_0, arg_6_1)
			if arg_6_0._data:
				warning("已经存在格子数据，无需设置预览数据")

				return

			arg_6_0._tempData = arg_6_1

			arg_6_0.loadImg(arg_6_0._tempData.img, arg_6_0._tempData.img_full)
			arg_6_0.setItemVisible(True)
			arg_6_0.setAlpha(0.5),
		def getTempData:(arg_7_0)
			return arg_7_0._tempData,
		def loadImg:(arg_8_0, arg_8_1, arg_8_2)
			setImageSprite(arg_8_0._imgTf, var_0_1.GetSprite(arg_8_1))
			setImageSprite(arg_8_0._imgFullTf, var_0_1.GetSprite(arg_8_2)),
		def setItemVisible:(arg_9_0, arg_9_1)
			setActive(arg_9_0._imgTf, arg_9_1)
			setActive(arg_9_0._imgFullTf, arg_9_1),
		def changeTempToReal:(arg_10_0)
			if arg_10_0._tempData:
				arg_10_0.setData(arg_10_0._tempData)

				arg_10_0._tempData = None,
		def setTriggerName:(arg_11_0, arg_11_1)
			if arg_11_0._animationFlag:
				return

			arg_11_0._animationFlag = True

			if arg_11_0.animTriggerName:
				arg_11_0._animator.ResetTrigger(arg_11_0.animTriggerName)

			arg_11_0.animTriggerName = arg_11_1,
		def playAnim:(arg_12_0, arg_12_1)
			arg_12_0._success = True

			if arg_12_0.animTriggerName:
				arg_12_0._animator.SetTrigger(arg_12_0.animTriggerName)

				if arg_12_1:
					arg_12_0._dftEvent.SetEndEvent(function()
						arg_12_1()
						arg_12_0._dftEvent.SetEndEvent(None)),
		def getAnimationFlag:(arg_14_0)
			return arg_14_0._animationFlag,
		def setVisible:(arg_15_0, arg_15_1)
			setActive(arg_15_0._itemTf, arg_15_1),
		def freeze:(arg_16_0, arg_16_1)
			arg_16_0._freeze = arg_16_1

			arg_16_0.setVisible(not arg_16_0._freeze),
		def getFreeze:(arg_17_0)
			return arg_17_0._freeze,
		def getSuccess:(arg_18_0)
			return arg_18_0._success,
		def setSelect:(arg_19_0, arg_19_1)
			arg_19_0.setTempData(arg_19_1),
		def setAlpha:(arg_20_0, arg_20_1)
			arg_20_0._canvasGroup.alpha = arg_20_1,
		def setPosition:(arg_21_0, arg_21_1)
			arg_21_0._itemTf.anchoredPosition = arg_21_1,
		def getIndex:(arg_22_0)
			return arg_22_0._index,
		def clear:(arg_23_0)
			arg_23_0._data = None
			arg_23_0._tempData = None
			arg_23_0._success = False

			arg_23_0.setItemVisible(False)
			arg_23_0.setAlpha(1),
		def getScreenPos:(arg_24_0, arg_24_1)
			if not arg_24_0._screenPos:
				arg_24_0.updateScreenPos()

			return arg_24_0._screenPos,
		def updateScreenPos:(arg_25_0)
			arg_25_0._screenPos = arg_25_0._uiCamera.WorldToScreenPoint(arg_25_0._itemTf.position),
		def getDirect:(arg_26_0)
			return arg_26_0._data.direct,
		def dispose:(arg_27_0)
			ClearEventTrigger(arg_27_0._eventTriggerListener)
	}

	var_1_0.ctor()

	return var_1_0

def var_0_0.Ctor(arg_28_0, arg_28_1, arg_28_2):
	var_0_1 = PipeGameVo
	arg_28_0._mapTf = arg_28_1
	arg_28_0._eventCallback = arg_28_2
	arg_28_0._mapItems = {}

	function arg_28_0.mapItemCallback(arg_29_0, arg_29_1)
		if var_0_0.CLICK_MAP_ITEM == arg_29_0:
			if arg_28_0._dragTempItem:
				arg_28_0._dragTempItem.clear()

				arg_28_0._dragTempItem = None

			arg_28_0._eventCallback(PipeGameEvent.STOP_RECT_DRAG)

			if not arg_28_0._clickTempItem:
				arg_28_0._clickTempItem = arg_29_1

				arg_28_0._eventCallback(PipeGameEvent.SET_TOP_RECT)
			elif arg_28_0._clickTempItem != arg_29_1:
				arg_28_0._clickTempItem.clear()

				arg_28_0._clickTempItem = arg_29_1

				arg_28_0._eventCallback(PipeGameEvent.SET_TOP_RECT)
			elif arg_28_0._clickTempItem.getTempData():
				arg_28_0._clickTempItem.changeTempToReal()

				arg_28_0._clickTempItem = None

				arg_28_0._eventCallback(PipeGameEvent.REMOVE_RECT_TOP)

				if arg_28_0.checkFull():
					arg_28_0.startOverAniamtion()

def var_0_0.setClickTempItem(arg_30_0, arg_30_1):
	if arg_30_0._clickTempItem and not arg_30_0._clickTempItem.getTempData():
		arg_30_0._clickTempItem.setTempData(arg_30_1)

def var_0_0.start(arg_31_0):
	arg_31_0._overFlag = False
	arg_31_0._clickTempItem = None
	arg_31_0._gameRoundData = PipeGameVo.GetRoundData()
	arg_31_0._mapBound = arg_31_0._gameRoundData.map_bound
	arg_31_0._mapSpacing = arg_31_0._gameRoundData.item_spacing
	arg_31_0._inputIndex = arg_31_0._gameRoundData.input_index
	arg_31_0._randomId = arg_31_0._gameRoundData.random_id
	arg_31_0._randomItemData = PipeGameConst.map_random_data[arg_31_0._randomId]
	findTF(arg_31_0._mapTf, "bg").sizeDelta = Vector2(arg_31_0._mapSpacing[1] * arg_31_0._mapBound[1], arg_31_0._mapSpacing[2] * arg_31_0._mapBound[2])
	arg_31_0._maxItem = arg_31_0._mapBound[1] * arg_31_0._mapBound[2]

	for iter_31_0 = 1, arg_31_0._maxItem:
		local var_31_0

		if iter_31_0 > #arg_31_0._mapItems:
			local var_31_1 = PipeGameVo.GetTplItemFromPool(PipeGameConst.tpl_map_item, arg_31_0._mapTf)
			local var_31_2 = arg_31_0.getItemPosByIndex(iter_31_0, arg_31_0._mapBound[1], arg_31_0._mapSpacing)

			var_31_0 = var_0_12(var_31_1, iter_31_0, arg_31_0.mapItemCallback)

			var_31_0.setPosition(var_31_2)
			table.insert(arg_31_0._mapItems, var_31_0)
		else
			var_31_0 = arg_31_0._mapItems[iter_31_0]

		var_31_0.freeze(False)
		var_31_0.clear()
		var_31_0.setData(arg_31_0.getRandomItemByIndex(iter_31_0))

	for iter_31_1 = arg_31_0._maxItem + 1, #arg_31_0._mapItems:
		arg_31_0._mapItems[iter_31_1].freeze(True)

def var_0_0.getRandomItemByIndex(arg_32_0, arg_32_1):
	for iter_32_0, iter_32_1 in ipairs(arg_32_0._randomItemData.list):
		if iter_32_1[1] == arg_32_1:
			if type(iter_32_1[2]) == "number":
				return PipeGameConst.map_item_data[iter_32_1[2]]
			elif type(iter_32_1[2]) == "table":
				local var_32_0 = math.random(1, #iter_32_1[2])
				local var_32_1 = iter_32_1[2][var_32_0]

				return PipeGameConst.map_item_data[var_32_1]

	return None

def var_0_0.step(arg_33_0, arg_33_1):
	if var_0_1.draging:
		if arg_33_0._clickTempItem:
			arg_33_0._clickTempItem.clear()

			arg_33_0._clickTempItem = None

		local var_33_0 = var_0_1.dragScreenPos
		local var_33_1 = arg_33_0.getItemByScreenPos(var_33_0)

		if var_33_1 and not var_33_1.getData():
			if arg_33_0._dragTempItem != var_33_1:
				if arg_33_0._dragTempItem:
					arg_33_0._dragTempItem.clear()

				arg_33_0._dragTempItem = var_33_1

				local var_33_2 = var_0_1.dragItem

				arg_33_0._dragTempItem.setTempData(var_33_2)
		else
			if arg_33_0._dragTempItem:
				arg_33_0._dragTempItem.clear()

			arg_33_0._dragTempItem = None

		arg_33_0._draging = var_0_1.draging
	else
		if arg_33_0._draging and arg_33_0._dragTempItem:
			arg_33_0._dragTempItem.changeTempToReal()

			arg_33_0._dragTempItem = None

			arg_33_0._eventCallback(PipeGameEvent.REMOVE_RECT_TOP)

			if arg_33_0.checkFull():
				arg_33_0.startOverAniamtion()

		arg_33_0._draging = var_0_1.draging

	if var_0_1.gameDragTime <= 0:
		arg_33_0.startOverAniamtion()

def var_0_0.startOverAniamtion(arg_34_0):
	if arg_34_0._overFlag:
		return

	arg_34_0._eventCallback(PipeGameEvent.START_SETTLEMENT)

	arg_34_0._overFlag = True
	arg_34_0._animationRound = 1

	local var_34_0 = {}
	local var_34_1 = arg_34_0.getItemByIndex(arg_34_0._inputIndex)

	if var_34_1.getData() and (var_34_1.getDirect()[2] == 0 or var_34_1.getDirect()[2] == 1):
		var_34_1.setTriggerName(var_0_4)
		table.insert(var_34_0, var_34_1)
		arg_34_0.playOverAniamtion(var_34_0, function()
			arg_34_0._eventCallback(PipeGameEvent.PALY_ANIMATION_COMPLETE))
	else
		arg_34_0._eventCallback(PipeGameEvent.PALY_ANIMATION_COMPLETE)

def var_0_0.getSuccessCount(arg_36_0):
	local var_36_0 = 0

	for iter_36_0 = 1, #arg_36_0._mapItems:
		local var_36_1 = arg_36_0._mapItems[iter_36_0]

		if var_36_1.getSuccess() and not var_36_1.getFreeze():
			var_36_0 = var_36_0 + 1

	return var_36_0

def var_0_0.checkFull(arg_37_0):
	local var_37_0 = 0

	for iter_37_0 = 1, #arg_37_0._mapItems:
		if not arg_37_0._mapItems[iter_37_0].getFreeze() and not arg_37_0._mapItems[iter_37_0].getData():
			var_37_0 = var_37_0 + 1

	return var_37_0 == 0

def var_0_0.playOverAniamtion(arg_38_0, arg_38_1, arg_38_2, arg_38_3):
	local var_38_0 = {}
	local var_38_1 = 0
	local var_38_2 = #arg_38_1
	local var_38_3 = arg_38_3 and arg_38_3 + 1 or 1

	local function var_38_4()
		var_38_1 = var_38_1 + 1

		if var_38_1 == var_38_2:
			if #var_38_0 == 0 and arg_38_2:
				arg_38_2()
			else
				arg_38_0.playOverAniamtion(var_38_0, arg_38_2, var_38_3)

	for iter_38_0, iter_38_1 in ipairs(arg_38_1):
		local var_38_5 = arg_38_0.getItemsByDirect(iter_38_1, var_38_3)

		arg_38_0.setItemsTriggerName(iter_38_1, var_38_5)

		for iter_38_2, iter_38_3 in ipairs(var_38_5):
			if not table.contains(var_38_0, iter_38_3):
				table.insert(var_38_0, iter_38_3)

		iter_38_1.playAnim(var_38_4)

def var_0_0.setItemsTriggerName(arg_40_0, arg_40_1, arg_40_2):
	for iter_40_0, iter_40_1 in ipairs(arg_40_2):
		local var_40_0 = arg_40_1.getIndex()
		local var_40_1 = iter_40_1.getIndex()
		local var_40_2

		if var_40_1 < var_40_0:
			if var_40_1 == var_40_0 - 1:
				var_40_2 = var_0_3
			else
				var_40_2 = var_0_5
		elif var_40_0 < var_40_1:
			if var_40_1 == var_40_0 + 1:
				var_40_2 = var_0_2
			else
				var_40_2 = var_0_4

		if var_40_2:
			iter_40_1.setTriggerName(var_40_2)

def var_0_0.getItemsByDirect(arg_41_0, arg_41_1, arg_41_2):
	local var_41_0 = {}
	local var_41_1 = arg_41_0._mapBound[1]
	local var_41_2 = arg_41_1.getDirect()
	local var_41_3 = arg_41_1.getIndex()

	if var_41_2[1] == var_0_6 or var_41_2[1] == var_0_11:
		table.insert(var_41_0, var_41_3 + 1)

	if var_41_2[1] == var_0_6 or var_41_2[1] == var_0_10:
		table.insert(var_41_0, var_41_3 - 1)

	if var_41_2[2] == var_0_7 or var_41_2[2] == var_0_8:
		table.insert(var_41_0, var_41_3 - arg_41_0._mapBound[1])

	if var_41_2[2] == var_0_7 or var_41_2[2] == var_0_9:
		table.insert(var_41_0, var_41_3 + arg_41_0._mapBound[1])

	for iter_41_0 = #var_41_0, 1, -1:
		local var_41_4 = arg_41_0.getItemByIndex(var_41_0[iter_41_0])

		if var_41_4 and var_41_4.getData():
			if not arg_41_0.checkItemSuccess(var_41_3, var_41_4.getIndex(), var_41_2, var_41_4.getDirect()):
				table.remove(var_41_0, iter_41_0)
		else
			table.remove(var_41_0, iter_41_0)

	local var_41_5 = {}

	for iter_41_1, iter_41_2 in ipairs(var_41_0):
		local var_41_6 = arg_41_0.getItemByIndex(iter_41_2)

		if var_41_6 and not var_41_6.getAnimationFlag():
			table.insert(var_41_5, var_41_6)

	return var_41_5

def var_0_0.checkItemSuccess(arg_42_0, arg_42_1, arg_42_2, arg_42_3, arg_42_4):
	local var_42_0 = False
	local var_42_1 = arg_42_0._mapBound[1]
	local var_42_2 = arg_42_3[1]
	local var_42_3 = arg_42_3[2]
	local var_42_4 = arg_42_4[1]
	local var_42_5 = arg_42_4[2]

	if arg_42_2 - arg_42_1 == 1:
		if (var_42_2 == var_0_6 or var_42_2 == var_0_11) and (var_42_4 == var_0_6 or var_42_4 == var_0_10):
			if (arg_42_1 - 1) % var_42_1 == var_42_1 - 1:
				var_42_0 = False
			else
				var_42_0 = True
	elif arg_42_1 - arg_42_2 == 1:
		if (var_42_2 == var_0_6 or var_42_2 == var_0_10) and (var_42_4 == var_0_6 or var_42_4 == var_0_11):
			if (arg_42_1 - 1) % var_42_1 == 0:
				var_42_0 = False
			else
				var_42_0 = True
	elif arg_42_2 - arg_42_1 == var_42_1:
		if (var_42_3 == var_0_7 or var_42_3 == var_0_9) and (var_42_5 == var_0_7 or var_42_5 == var_0_8):
			var_42_0 = True
	elif arg_42_1 - arg_42_2 == var_42_1 and (var_42_3 == var_0_7 or var_42_3 == var_0_8) and (var_42_5 == var_0_7 or var_42_5 == var_0_9):
		var_42_0 = True

	return var_42_0

def var_0_0.getItemByIndex(arg_43_0, arg_43_1):
	return arg_43_0._mapItems[arg_43_1]

def var_0_0.getItemByScreenPos(arg_44_0, arg_44_1):
	local var_44_0 = arg_44_0.getScreentScaleRate()

	for iter_44_0 = 1, #arg_44_0._mapItems:
		local var_44_1 = arg_44_0._mapItems[iter_44_0]
		local var_44_2 = var_44_1.getScreenPos()

		if arg_44_1.x > var_44_2.x and arg_44_1.x < var_44_2.x + arg_44_0._mapSpacing[1] / var_44_0.x and arg_44_1.y < var_44_2.y and arg_44_1.y > var_44_2.y - arg_44_0._mapSpacing[2] / var_44_0.y:
			return var_44_1

	return None

def var_0_0.getScreentScaleRate(arg_45_0):
	local var_45_0 = UnityEngine.Screen.width
	local var_45_1 = UnityEngine.Screen.height
	local var_45_2 = tf(GameObject.Find("UICamera/Canvas"))
	local var_45_3 = var_45_2.sizeDelta.x
	local var_45_4 = var_45_2.sizeDelta.y

	return Vector2(var_45_3 / var_45_0, var_45_4 / var_45_1)

def var_0_0.getItemPosByIndex(arg_46_0, arg_46_1, arg_46_2, arg_46_3):
	local var_46_0 = (arg_46_1 - 1) % arg_46_2
	local var_46_1 = math.floor((arg_46_1 - 1) / arg_46_2)

	return Vector2(var_46_0 * arg_46_3[1], -var_46_1 * arg_46_3[2])

def var_0_0.stop(arg_47_0):
	return

def var_0_0.clear(arg_48_0):
	if arg_48_0._dragTempItem:
		arg_48_0._dragTempItem.clear()

		arg_48_0._dragTempItem = None

def var_0_0.dispose(arg_49_0):
	return

return var_0_0
