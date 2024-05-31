local var_0_0 = class("BeachGuardGameUI")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_3
	arg_1_0._gameData = arg_1_2
	arg_1_0.gameUI = findTF(arg_1_0._tf, "ui/gameUI")
	arg_1_0.asset = arg_1_0._gameData.asset
	arg_1_0._uiCamera = GameObject.Find("UICamera"):GetComponent(typeof(Camera))

	onButton(arg_1_0._event, findTF(arg_1_0.gameUI, "ad/topRight/btnStop"), function()
		arg_1_0._event:emit(BeachGuardGameView.OPEN_PAUSE_UI)
		arg_1_0._event:emit(BeachGuardGameView.PAUSE_GAME, true)
	end)
	onButton(arg_1_0._event, findTF(arg_1_0.gameUI, "ad/btnLeave"), function()
		arg_1_0._event:emit(BeachGuardGameView.OPEN_LEVEL_UI)
		arg_1_0._event:emit(BeachGuardGameView.PAUSE_GAME, true)
	end)

	arg_1_0.gameTimeS = findTF(arg_1_0.gameUI, "ad/top/time/s")
	arg_1_0.scoreTf = findTF(arg_1_0.gameUI, "ad/top/score")
	arg_1_0.bottom = findTF(arg_1_0.gameUI, "bottom")
	arg_1_0.goods = findTF(arg_1_0.gameUI, "bottom/goods")
	arg_1_0.goodsNum = findTF(arg_1_0.gameUI, "bottom/goods/num")
	arg_1_0.goodsAdd = findTF(arg_1_0.gameUI, "bottom/goods/add")
	arg_1_0.charContent = findTF(arg_1_0.gameUI, "bottom/charContainer/content")
	arg_1_0.cardTpl = findTF(arg_1_0.gameUI, "bottom/cardTpl")
	arg_1_0.dragChar = findTF(arg_1_0.gameUI, "bottom/dragChar")

	setActive(arg_1_0.dragChar, false)

	arg_1_0.cards = {}
	arg_1_0.cardPool = {}
	arg_1_0.dragData = {}
	arg_1_0.recycleFlag = false
	arg_1_0.btnRecycle = findTF(arg_1_0.gameUI, "bottom/recycles")

	onButton(arg_1_0._event, arg_1_0.btnRecycle, function()
		arg_1_0.recycleFlag = true

		setActive(arg_1_0.btnRecycle, false)
		setActive(arg_1_0.btnMask, true)
		arg_1_0._event:emit(BeachGuardGameView.RECYCLES_CHAR, true)
	end)

	arg_1_0.enemyComming = findTF(arg_1_0.gameUI, "enemyComming")
	arg_1_0.btnMask = findTF(arg_1_0.gameUI, "bottom/recycleMask")

	onButton(arg_1_0._event, arg_1_0.btnMask, function()
		arg_1_0:cancelRecycle()
	end)

	arg_1_0.enemyProgress = findTF(arg_1_0.gameUI, "ad/enemyProgress")
	arg_1_0.bossRate = findTF(arg_1_0.gameUI, "ad/bossRate")
end

function var_0_0.cancelRecycle(arg_6_0)
	arg_6_0.recycleFlag = false

	setActive(arg_6_0.btnRecycle, true)
	setActive(arg_6_0.btnMask, false)
	arg_6_0._event:emit(BeachGuardGameView.RECYCLES_CHAR, false)
end

function var_0_0.show(arg_7_0, arg_7_1)
	arg_7_0.recycleFlag = false

	setActive(arg_7_0.btnRecycle, true)
	setActive(arg_7_0.btnMask, false)
	setActive(arg_7_0.gameUI, arg_7_1)
end

function var_0_0.firstUpdate(arg_8_0, arg_8_1)
	local var_8_0 = arg_8_1.chapter
	local var_8_1 = BeachGuardConst.chapter_data[var_8_0]

	arg_8_0.enemyTime = BeachGuardConst.chapater_enemy[var_8_0].time

	if not arg_8_0.enemyTime or arg_8_0.enemyTime == 0 then
		setActive(arg_8_0.enemyProgress, false)
		setActive(arg_8_0.bossRate, false)
	else
		setActive(arg_8_0.enemyProgress, true)
		setActive(arg_8_0.bossRate, true)
	end

	arg_8_0.bossRateNum = BeachGuardConst.chapater_enemy[var_8_0].boss_rate

	if not arg_8_0.bossRateNum or arg_8_0.bossRateNum == 0 then
		setActive(arg_8_0.bossRate, false)
	else
		setActive(arg_8_0.bossRate, true)
		setSlider(arg_8_0.bossRate, 0, 1, arg_8_0.bossRateNum)
	end

	setActive(arg_8_0.enemyComming, false)

	arg_8_0.showCards = var_8_1.show_card
	arg_8_0.runningData = arg_8_1
	arg_8_0.recycleFlag = false

	setActive(arg_8_0.btnRecycle, true)
	setActive(arg_8_0.btnMask, false)
	setActive(arg_8_0.goodsAdd, false)
	arg_8_0:resetChaCard()
	arg_8_0:createCharCard()
	arg_8_0:update()
end

function var_0_0.update(arg_9_0)
	local var_9_0 = arg_9_0.runningData.goodsNum
	local var_9_1 = arg_9_0.runningData.sceneChars

	for iter_9_0 = 1, #arg_9_0.cards do
		local var_9_2 = arg_9_0.cards[iter_9_0].config
		local var_9_3 = arg_9_0.cards[iter_9_0].tf
		local var_9_4 = var_9_2.cost
		local var_9_5 = var_9_2.once
		local var_9_6 = var_9_2.char_id
		local var_9_7 = GetComponent(var_9_3, typeof(CanvasGroup))

		if var_9_0 < var_9_4 then
			var_9_7.blocksRaycasts = false
			var_9_7.interactable = false

			setActive(findTF(var_9_3, "mask"), true)
		elseif var_9_5 and table.contains(var_9_1, var_9_6) then
			var_9_7.blocksRaycasts = false
			var_9_7.interactable = false

			setActive(findTF(var_9_3, "mask"), true)
		else
			var_9_7.blocksRaycasts = true
			var_9_7.interactable = true

			setActive(findTF(var_9_3, "mask"), false)
		end
	end

	setText(arg_9_0.scoreTf, arg_9_0.runningData.scoreNum)
	setText(arg_9_0.gameTimeS, math.ceil(arg_9_0.runningData.gameTime))

	if arg_9_0.enemyTime and arg_9_0.enemyTime > 0 then
		local var_9_8 = (arg_9_0.enemyTime - arg_9_0.runningData.gameStepTime) / arg_9_0.enemyTime

		setSlider(arg_9_0.enemyProgress, 0, 1, var_9_8)
	end

	setText(arg_9_0.goodsNum, var_9_0)
end

function var_0_0.updateGoods(arg_10_0, arg_10_1, arg_10_2)
	if arg_10_1 and arg_10_1 > 0 then
		setActive(arg_10_0.goodsAdd, false)
		setText(findTF(arg_10_0.goodsAdd, "text"), "+" .. tostring(arg_10_1))
		setActive(arg_10_0.goodsAdd, true)
	end
end

function var_0_0.createCharCard(arg_11_0)
	for iter_11_0 = 1, #arg_11_0.showCards do
		local var_11_0 = iter_11_0
		local var_11_1 = BeachGuardConst.char_card[arg_11_0.showCards[iter_11_0]]
		local var_11_2 = arg_11_0:getCardFromPool(var_11_1.id)
		local var_11_3

		if not var_11_2 then
			var_11_3 = tf(instantiate(arg_11_0.cardTpl))

			SetParent(var_11_3, arg_11_0.charContent)

			var_11_2 = {
				tf = var_11_3,
				config = var_11_1
			}
		else
			var_11_3 = var_11_2.tf
		end

		table.insert(arg_11_0.cards, var_11_2)
		setActive(var_11_3, true)

		local var_11_4 = GetComponent(findTF(var_11_3, "icon"), typeof(Image))

		var_11_4.sprite = BeachGuardAsset.getCardQIcon(var_11_1.icon)

		var_11_4:SetNativeSize()

		local var_11_5 = GetOrAddComponent(var_11_3, typeof(EventTriggerListener))

		ClearEventTrigger(var_11_5)
		var_11_5:AddBeginDragFunc(function(arg_12_0, arg_12_1)
			if arg_11_0.recycleFlag then
				return
			end

			setActive(arg_11_0.dragChar, true)

			local var_12_0 = GetComponent(findTF(arg_11_0.dragChar, "icon"), typeof(Image))

			var_12_0.sprite = BeachGuardAsset.getCardIcon(var_11_1.icon)

			var_12_0:SetNativeSize()

			arg_11_0.dragData = {
				flag = true,
				config = var_11_1
			}

			arg_11_0._event:emit(BeachGuardGameView.DRAG_CHAR, arg_11_0.dragData)
		end)
		var_11_5:AddDragFunc(function(arg_13_0, arg_13_1)
			if arg_11_0.recycleFlag then
				return
			end

			local var_13_0 = arg_13_1.position

			var_13_0.y = var_13_0.y

			local var_13_1 = arg_11_0._uiCamera:ScreenToWorldPoint(var_13_0)

			arg_11_0.dragChar.anchoredPosition = arg_11_0.bottom:InverseTransformPoint(var_13_1)

			if not arg_11_0.dragData.pos then
				arg_11_0.dragData.pos = Vector3(0, 0)
			end

			arg_11_0.dragData.pos.x = var_13_1.x
			arg_11_0.dragData.pos.y = var_13_1.y
			arg_11_0.dragData.pos.z = var_13_1.z
		end)
		var_11_5:AddDragEndFunc(function(arg_14_0, arg_14_1)
			if arg_11_0.recycleFlag then
				return
			end

			setActive(arg_11_0.dragChar, false)

			arg_11_0.dragData.flag = false
			arg_11_0.dragData.pos = nil

			arg_11_0._event:emit(BeachGuardGameView.DRAG_CHAR, arg_11_0.dragData)
		end)
		setText(findTF(var_11_3, "cost"), tostring(var_11_1.cost))
	end
end

function var_0_0.getCardFromPool(arg_15_0, arg_15_1)
	for iter_15_0 = #arg_15_0.cardPool, 1, -1 do
		if arg_15_0.cardPool[iter_15_0].config.id == arg_15_1 then
			return table.remove(arg_15_0.cardPool, iter_15_0)
		end
	end

	return nil
end

function var_0_0.resetChaCard(arg_16_0)
	for iter_16_0 = 1, #arg_16_0.cards do
		local var_16_0 = arg_16_0.cards[iter_16_0].tf

		setActive(findTF(var_16_0, "mask"), false)

		GetComponent(findTF(var_16_0, "icon"), typeof(Image)).sprite = nil

		setText(findTF(var_16_0, "cost"), "0")
		setActive(var_16_0, false)

		local var_16_1 = GetOrAddComponent(var_16_0, typeof(EventTriggerListener))

		ClearEventTrigger(var_16_1)
	end

	for iter_16_1 = #arg_16_0.cards, 1, -1 do
		local var_16_2 = table.remove(arg_16_0.cards, iter_16_1)

		table.insert(arg_16_0.cardPool, var_16_2)
	end
end

function var_0_0.setEnemyComming(arg_17_0)
	setActive(arg_17_0.enemyComming, false)
	setActive(arg_17_0.enemyComming, true)
end

function var_0_0.setDragCallback(arg_18_0, arg_18_1)
	return
end

return var_0_0
