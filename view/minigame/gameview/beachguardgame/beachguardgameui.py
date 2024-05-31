local var_0_0 = class("BeachGuardGameUI")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_3
	arg_1_0._gameData = arg_1_2
	arg_1_0.gameUI = findTF(arg_1_0._tf, "ui/gameUI")
	arg_1_0.asset = arg_1_0._gameData.asset
	arg_1_0._uiCamera = GameObject.Find("UICamera").GetComponent(typeof(Camera))

	onButton(arg_1_0._event, findTF(arg_1_0.gameUI, "ad/topRight/btnStop"), function()
		arg_1_0._event.emit(BeachGuardGameView.OPEN_PAUSE_UI)
		arg_1_0._event.emit(BeachGuardGameView.PAUSE_GAME, True))
	onButton(arg_1_0._event, findTF(arg_1_0.gameUI, "ad/btnLeave"), function()
		arg_1_0._event.emit(BeachGuardGameView.OPEN_LEVEL_UI)
		arg_1_0._event.emit(BeachGuardGameView.PAUSE_GAME, True))

	arg_1_0.gameTimeS = findTF(arg_1_0.gameUI, "ad/top/time/s")
	arg_1_0.scoreTf = findTF(arg_1_0.gameUI, "ad/top/score")
	arg_1_0.bottom = findTF(arg_1_0.gameUI, "bottom")
	arg_1_0.goods = findTF(arg_1_0.gameUI, "bottom/goods")
	arg_1_0.goodsNum = findTF(arg_1_0.gameUI, "bottom/goods/num")
	arg_1_0.goodsAdd = findTF(arg_1_0.gameUI, "bottom/goods/add")
	arg_1_0.charContent = findTF(arg_1_0.gameUI, "bottom/charContainer/content")
	arg_1_0.cardTpl = findTF(arg_1_0.gameUI, "bottom/cardTpl")
	arg_1_0.dragChar = findTF(arg_1_0.gameUI, "bottom/dragChar")

	setActive(arg_1_0.dragChar, False)

	arg_1_0.cards = {}
	arg_1_0.cardPool = {}
	arg_1_0.dragData = {}
	arg_1_0.recycleFlag = False
	arg_1_0.btnRecycle = findTF(arg_1_0.gameUI, "bottom/recycles")

	onButton(arg_1_0._event, arg_1_0.btnRecycle, function()
		arg_1_0.recycleFlag = True

		setActive(arg_1_0.btnRecycle, False)
		setActive(arg_1_0.btnMask, True)
		arg_1_0._event.emit(BeachGuardGameView.RECYCLES_CHAR, True))

	arg_1_0.enemyComming = findTF(arg_1_0.gameUI, "enemyComming")
	arg_1_0.btnMask = findTF(arg_1_0.gameUI, "bottom/recycleMask")

	onButton(arg_1_0._event, arg_1_0.btnMask, function()
		arg_1_0.cancelRecycle())

	arg_1_0.enemyProgress = findTF(arg_1_0.gameUI, "ad/enemyProgress")
	arg_1_0.bossRate = findTF(arg_1_0.gameUI, "ad/bossRate")

def var_0_0.cancelRecycle(arg_6_0):
	arg_6_0.recycleFlag = False

	setActive(arg_6_0.btnRecycle, True)
	setActive(arg_6_0.btnMask, False)
	arg_6_0._event.emit(BeachGuardGameView.RECYCLES_CHAR, False)

def var_0_0.show(arg_7_0, arg_7_1):
	arg_7_0.recycleFlag = False

	setActive(arg_7_0.btnRecycle, True)
	setActive(arg_7_0.btnMask, False)
	setActive(arg_7_0.gameUI, arg_7_1)

def var_0_0.firstUpdate(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_1.chapter
	local var_8_1 = BeachGuardConst.chapter_data[var_8_0]

	arg_8_0.enemyTime = BeachGuardConst.chapater_enemy[var_8_0].time

	if not arg_8_0.enemyTime or arg_8_0.enemyTime == 0:
		setActive(arg_8_0.enemyProgress, False)
		setActive(arg_8_0.bossRate, False)
	else
		setActive(arg_8_0.enemyProgress, True)
		setActive(arg_8_0.bossRate, True)

	arg_8_0.bossRateNum = BeachGuardConst.chapater_enemy[var_8_0].boss_rate

	if not arg_8_0.bossRateNum or arg_8_0.bossRateNum == 0:
		setActive(arg_8_0.bossRate, False)
	else
		setActive(arg_8_0.bossRate, True)
		setSlider(arg_8_0.bossRate, 0, 1, arg_8_0.bossRateNum)

	setActive(arg_8_0.enemyComming, False)

	arg_8_0.showCards = var_8_1.show_card
	arg_8_0.runningData = arg_8_1
	arg_8_0.recycleFlag = False

	setActive(arg_8_0.btnRecycle, True)
	setActive(arg_8_0.btnMask, False)
	setActive(arg_8_0.goodsAdd, False)
	arg_8_0.resetChaCard()
	arg_8_0.createCharCard()
	arg_8_0.update()

def var_0_0.update(arg_9_0):
	local var_9_0 = arg_9_0.runningData.goodsNum
	local var_9_1 = arg_9_0.runningData.sceneChars

	for iter_9_0 = 1, #arg_9_0.cards:
		local var_9_2 = arg_9_0.cards[iter_9_0].config
		local var_9_3 = arg_9_0.cards[iter_9_0].tf
		local var_9_4 = var_9_2.cost
		local var_9_5 = var_9_2.once
		local var_9_6 = var_9_2.char_id
		local var_9_7 = GetComponent(var_9_3, typeof(CanvasGroup))

		if var_9_0 < var_9_4:
			var_9_7.blocksRaycasts = False
			var_9_7.interactable = False

			setActive(findTF(var_9_3, "mask"), True)
		elif var_9_5 and table.contains(var_9_1, var_9_6):
			var_9_7.blocksRaycasts = False
			var_9_7.interactable = False

			setActive(findTF(var_9_3, "mask"), True)
		else
			var_9_7.blocksRaycasts = True
			var_9_7.interactable = True

			setActive(findTF(var_9_3, "mask"), False)

	setText(arg_9_0.scoreTf, arg_9_0.runningData.scoreNum)
	setText(arg_9_0.gameTimeS, math.ceil(arg_9_0.runningData.gameTime))

	if arg_9_0.enemyTime and arg_9_0.enemyTime > 0:
		local var_9_8 = (arg_9_0.enemyTime - arg_9_0.runningData.gameStepTime) / arg_9_0.enemyTime

		setSlider(arg_9_0.enemyProgress, 0, 1, var_9_8)

	setText(arg_9_0.goodsNum, var_9_0)

def var_0_0.updateGoods(arg_10_0, arg_10_1, arg_10_2):
	if arg_10_1 and arg_10_1 > 0:
		setActive(arg_10_0.goodsAdd, False)
		setText(findTF(arg_10_0.goodsAdd, "text"), "+" .. tostring(arg_10_1))
		setActive(arg_10_0.goodsAdd, True)

def var_0_0.createCharCard(arg_11_0):
	for iter_11_0 = 1, #arg_11_0.showCards:
		local var_11_0 = iter_11_0
		local var_11_1 = BeachGuardConst.char_card[arg_11_0.showCards[iter_11_0]]
		local var_11_2 = arg_11_0.getCardFromPool(var_11_1.id)
		local var_11_3

		if not var_11_2:
			var_11_3 = tf(instantiate(arg_11_0.cardTpl))

			SetParent(var_11_3, arg_11_0.charContent)

			var_11_2 = {
				tf = var_11_3,
				config = var_11_1
			}
		else
			var_11_3 = var_11_2.tf

		table.insert(arg_11_0.cards, var_11_2)
		setActive(var_11_3, True)

		local var_11_4 = GetComponent(findTF(var_11_3, "icon"), typeof(Image))

		var_11_4.sprite = BeachGuardAsset.getCardQIcon(var_11_1.icon)

		var_11_4.SetNativeSize()

		local var_11_5 = GetOrAddComponent(var_11_3, typeof(EventTriggerListener))

		ClearEventTrigger(var_11_5)
		var_11_5.AddBeginDragFunc(function(arg_12_0, arg_12_1)
			if arg_11_0.recycleFlag:
				return

			setActive(arg_11_0.dragChar, True)

			local var_12_0 = GetComponent(findTF(arg_11_0.dragChar, "icon"), typeof(Image))

			var_12_0.sprite = BeachGuardAsset.getCardIcon(var_11_1.icon)

			var_12_0.SetNativeSize()

			arg_11_0.dragData = {
				flag = True,
				config = var_11_1
			}

			arg_11_0._event.emit(BeachGuardGameView.DRAG_CHAR, arg_11_0.dragData))
		var_11_5.AddDragFunc(function(arg_13_0, arg_13_1)
			if arg_11_0.recycleFlag:
				return

			local var_13_0 = arg_13_1.position

			var_13_0.y = var_13_0.y

			local var_13_1 = arg_11_0._uiCamera.ScreenToWorldPoint(var_13_0)

			arg_11_0.dragChar.anchoredPosition = arg_11_0.bottom.InverseTransformPoint(var_13_1)

			if not arg_11_0.dragData.pos:
				arg_11_0.dragData.pos = Vector3(0, 0)

			arg_11_0.dragData.pos.x = var_13_1.x
			arg_11_0.dragData.pos.y = var_13_1.y
			arg_11_0.dragData.pos.z = var_13_1.z)
		var_11_5.AddDragEndFunc(function(arg_14_0, arg_14_1)
			if arg_11_0.recycleFlag:
				return

			setActive(arg_11_0.dragChar, False)

			arg_11_0.dragData.flag = False
			arg_11_0.dragData.pos = None

			arg_11_0._event.emit(BeachGuardGameView.DRAG_CHAR, arg_11_0.dragData))
		setText(findTF(var_11_3, "cost"), tostring(var_11_1.cost))

def var_0_0.getCardFromPool(arg_15_0, arg_15_1):
	for iter_15_0 = #arg_15_0.cardPool, 1, -1:
		if arg_15_0.cardPool[iter_15_0].config.id == arg_15_1:
			return table.remove(arg_15_0.cardPool, iter_15_0)

	return None

def var_0_0.resetChaCard(arg_16_0):
	for iter_16_0 = 1, #arg_16_0.cards:
		local var_16_0 = arg_16_0.cards[iter_16_0].tf

		setActive(findTF(var_16_0, "mask"), False)

		GetComponent(findTF(var_16_0, "icon"), typeof(Image)).sprite = None

		setText(findTF(var_16_0, "cost"), "0")
		setActive(var_16_0, False)

		local var_16_1 = GetOrAddComponent(var_16_0, typeof(EventTriggerListener))

		ClearEventTrigger(var_16_1)

	for iter_16_1 = #arg_16_0.cards, 1, -1:
		local var_16_2 = table.remove(arg_16_0.cards, iter_16_1)

		table.insert(arg_16_0.cardPool, var_16_2)

def var_0_0.setEnemyComming(arg_17_0):
	setActive(arg_17_0.enemyComming, False)
	setActive(arg_17_0.enemyComming, True)

def var_0_0.setDragCallback(arg_18_0, arg_18_1):
	return

return var_0_0
