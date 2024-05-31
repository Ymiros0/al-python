local var_0_0 = class("BobingPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	if PLATFORM_CODE == PLATFORM_CHT or PLATFORM_CODE == PLATFORM_CH:
		setActive(findTF(arg_1_0._tf, "bobing"), True)
		setActive(findTF(arg_1_0._tf, "lottery"), False)
	else
		setActive(findTF(arg_1_0._tf, "bobing"), False)
		setActive(findTF(arg_1_0._tf, "lottery"), True)

	arg_1_0.bind(ActivityMediator.ON_BOBING_RESULT, function(arg_2_0, arg_2_1, arg_2_2)
		if PLATFORM_CODE == PLATFORM_CHT or PLATFORM_CODE == PLATFORM_CH:
			arg_1_0.displayBBResult(arg_2_1.awards, arg_2_1.numbers, function()
				arg_2_1.callback())
		else
			arg_1_0.displayLotteryAni(arg_2_1.awards, arg_2_1.numbers, function()
				arg_2_1.callback()))

def var_0_0.OnUpdateFlush(arg_5_0):
	if PLATFORM_CODE == PLATFORM_CHT or PLATFORM_CODE == PLATFORM_CH:
		arg_5_0.bobingUpdate()
	else
		arg_5_0.lotteryUpdate()

def var_0_0.lotteryUpdate(arg_6_0):
	local var_6_0 = arg_6_0.activity
	local var_6_1 = findTF(arg_6_0._tf, "lottery/layer")
	local var_6_2 = arg_6_0.lotteryWrap

	if not var_6_2:
		var_6_2 = {
			btnLotteryBtn = findTF(var_6_1, "lottery_btn"),
			phase = findTF(var_6_1, "phase"),
			nums = findTF(var_6_1, "nums")
		}
		arg_6_0.lotteryWrap = var_6_2

	local var_6_3 = var_6_0.getConfig("config_id")

	if var_6_3 <= var_6_0.data1:
		setActive(findTF(var_6_2.phase, "bg"), False)
		setActive(findTF(var_6_2.phase, "Text"), False)
		setActive(findTF(var_6_2.phase, "finish"), True)
	else
		setActive(findTF(var_6_2.phase, "bg"), True)
		setActive(findTF(var_6_2.phase, "Text"), True)
		setText(findTF(var_6_2.phase, "Text"), setColorStr(var_6_0.data1, "FFD43F") .. "/" .. var_6_3)
		setActive(findTF(var_6_2.phase, "finish"), False)

	if var_6_0.data2 < 1:
		LeanTween.alpha(var_6_2.btnLotteryBtn, 1, 1).setLoopPingPong()
		setActive(findTF(var_6_2.btnLotteryBtn, "mask"), False)
		onButton(arg_6_0, var_6_2.btnLotteryBtn, function()
			if arg_6_0.activity.data2 < 1:
				arg_6_0.emit(ActivityMediator.EVENT_OPERATION, {
					cmd = 1,
					activity_id = arg_6_0.activity.id
				})
				arg_6_0.emit(ActivityMainScene.LOCK_ACT_MAIN, True), SFX_PANEL)
	else
		LeanTween.cancel(var_6_2.btnLotteryBtn.gameObject)
		setActive(findTF(var_6_2.btnLotteryBtn, "mask"), True)

		local var_6_4 = arg_6_0.getIndexByNumbers(var_6_0.data1_list)

		setActive(findTF(var_6_2.btnLotteryBtn, "mask/1"), var_6_4 == 1)
		setActive(findTF(var_6_2.btnLotteryBtn, "mask/2"), var_6_4 == 2)
		setActive(findTF(var_6_2.btnLotteryBtn, "mask/3"), var_6_4 == 3)
		onButton(arg_6_0, var_6_2.btnLotteryBtn, function()
			if arg_6_0.activity.data2 < 1:
				arg_6_0.emit(ActivityMediator.EVENT_OPERATION, {
					cmd = 1,
					activity_id = arg_6_0.activity.id
				})
				arg_6_0.emit(ActivityMainScene.LOCK_ACT_MAIN, True), SFX_PANEL)

	local var_6_5 = var_6_0.data2 == 0 and "FFD43F" or "d2d4db"

	setText(findTF(var_6_2.nums, "text"), string.format("<color=#%s>%s</color> / %s", var_6_5, 1 - var_6_0.data2, 1))

def var_0_0.getIndexByNumbers(arg_9_0, arg_9_1):
	local var_9_0 = ActivityConst.BBRule(arg_9_1)
	local var_9_1 = 3

	if var_9_0 and var_9_0 >= 1 and var_9_0 <= 2:
		var_9_1 = 1

	if var_9_0 and var_9_0 >= 3 and var_9_0 <= 4:
		var_9_1 = 2

	return var_9_1

def var_0_0.displayLotteryAni(arg_10_0, arg_10_1, arg_10_2, arg_10_3):
	local var_10_0 = arg_10_0.getIndexByNumbers(arg_10_2)
	local var_10_1 = findTF(arg_10_0._tf, "lottery")
	local var_10_2 = arg_10_0.findTF("omikuji_anim", var_10_1).GetComponent(typeof(DftAniEvent))

	var_10_2.SetEndEvent(function(arg_11_0)
		setActive(var_10_2.gameObject, False)

		local var_11_0 = arg_10_0.findTF("omikuji_result", var_10_1)

		setActive(var_11_0, True)

		local var_11_1 = arg_10_0.findTF("title", var_11_0)

		for iter_11_0 = 1, var_11_1.childCount:
			setActive(var_11_1.GetChild(iter_11_0 - 1), iter_11_0 == var_10_0)

		local var_11_2 = arg_10_0.findTF("desc", var_11_0)
		local var_11_3 = {
			"big",
			"medium",
			"little"
		}
		local var_11_4 = i18n("draw_" .. var_11_3[var_10_0] .. "_luck_" .. math.random(1, 3))

		setText(var_11_2, var_11_4)

		local var_11_5 = arg_10_0.findTF("award", var_11_0)
		local var_11_6 = arg_10_0.findTF("award_list", var_11_0)

		setActive(var_11_5, False)
		removeAllChildren(var_11_6)

		if arg_10_1:
			for iter_11_1, iter_11_2 in ipairs(arg_10_1):
				local var_11_7 = cloneTplTo(var_11_5, var_11_6)
				local var_11_8 = {
					type = iter_11_2.type,
					id = iter_11_2.id,
					count = iter_11_2.count
				}

				updateDrop(var_11_7, var_11_8)
				onButton(arg_10_0, var_11_7, function()
					arg_10_0.emit(BaseUI.ON_DROP, var_11_8), SFX_PANEL)

		arg_10_0.emit(ActivityMainScene.LOCK_ACT_MAIN, False)
		onButton(arg_10_0, var_11_0, function()
			setActive(var_11_0, False)
			arg_10_3()))
	setActive(var_10_2.gameObject, True)

def var_0_0.bobingUpdate(arg_14_0):
	local var_14_0 = arg_14_0.activity
	local var_14_1 = findTF(arg_14_0._tf, "bobing")
	local var_14_2 = arg_14_0.bobingWrap

	if not var_14_2:
		var_14_2 = {
			bg = arg_14_0.findTF("AD", arg_14_0._tf),
			progress = arg_14_0.findTF("award/nums", var_14_1),
			get = arg_14_0.findTF("award/get", var_14_1),
			nums = arg_14_0.findTF("nums/text", var_14_1),
			bowlDisable = arg_14_0.findTF("bowl_disable", var_14_1),
			bowlEnable = arg_14_0.findTF("bowl_enable", var_14_1)
		}
		var_14_2.bowlShine = arg_14_0.findTF("bowl_shine", var_14_2.bowlEnable)
		var_14_2.btnRule = arg_14_0.findTF("btnRule", var_14_1)
		var_14_2.layerRule = arg_14_0.findTF("rule", var_14_1)
		var_14_2.btnReturn = arg_14_0.findTF("btnReturn", var_14_2.layerRule)
		var_14_2.item = arg_14_0.findTF("item", var_14_2.layerRule)
		var_14_2.top = arg_14_0.findTF("top", var_14_2.layerRule)
		var_14_2.itemRow = arg_14_0.findTF("row", var_14_2.layerRule)
		var_14_2.itemColumn = arg_14_0.findTF("column", var_14_2.layerRule)

		setActive(var_14_2.layerRule, False)
		setActive(var_14_2.item, False)
		setActive(var_14_2.itemRow, False)
		setActive(var_14_2.itemColumn, True)

		local var_14_3 = pg.gameset.bb_front_awards.description
		local var_14_4 = var_14_3[1]
		local var_14_5 = _.slice(var_14_3, 2, #var_14_3 - 1)
		local var_14_6 = UIItemList.New(var_14_2.top, var_14_2.item)

		var_14_6.make(function(arg_15_0, arg_15_1, arg_15_2)
			if arg_15_0 == UIItemList.EventUpdate:
				local var_15_0 = {
					type = var_14_4[arg_15_1 + 1][1],
					id = var_14_4[arg_15_1 + 1][2],
					count = var_14_4[arg_15_1 + 1][3]
				}

				updateDrop(arg_15_2, var_15_0)
				onButton(arg_14_0, arg_15_2, function()
					arg_14_0.emit(BaseUI.ON_DROP, var_15_0), SFX_PANEL))
		var_14_6.align(#var_14_4)

		local var_14_7 = UIItemList.New(var_14_2.itemColumn, var_14_2.itemRow)

		var_14_7.make(function(arg_17_0, arg_17_1, arg_17_2)
			if arg_17_0 == UIItemList.EventUpdate:
				local var_17_0 = var_14_5[arg_17_1 + 1]
				local var_17_1 = UIItemList.New(arg_17_2, var_14_2.item)

				var_17_1.make(function(arg_18_0, arg_18_1, arg_18_2)
					if arg_18_0 == UIItemList.EventUpdate:
						local var_18_0 = {
							type = var_17_0[arg_18_1 + 1][1],
							id = var_17_0[arg_18_1 + 1][2],
							count = var_17_0[arg_18_1 + 1][3]
						}

						updateDrop(arg_18_2, var_18_0)
						onButton(arg_14_0, arg_18_2, function()
							arg_14_0.emit(BaseUI.ON_DROP, var_18_0), SFX_PANEL))
				var_17_1.align(#var_17_0))
		var_14_7.align(#var_14_5)
		onButton(arg_14_0, var_14_2.btnRule, function()
			setActive(var_14_2.layerRule, True), SFX_PANEL)
		onButton(arg_14_0, var_14_2.btnReturn, function()
			setActive(var_14_2.layerRule, False), SFX_CANCEL)
		onButton(arg_14_0, var_14_2.bowlEnable, function()
			arg_14_0.emit(ActivityMainScene.LOCK_ACT_MAIN, True)
			arg_14_0.displayBBAnim(function()
				arg_14_0.emit(ActivityMediator.EVENT_OPERATION, {
					cmd = 1,
					activity_id = var_14_0.id
				})), SFX_PANEL)

		arg_14_0.bobingWrap = var_14_2

	local var_14_8 = var_14_0.getConfig("config_id")

	setActive(var_14_2.layerRule, False)
	setActive(var_14_2.get, var_14_8 <= var_14_0.data1)
	setActive(var_14_2.bowlDisable, var_14_0.data2 == 0)
	setActive(var_14_2.bowlEnable, var_14_0.data2 > 0)

	if var_14_0.data2 < 1:
		LeanTween.alpha(var_14_2.bowlShine, 1, 1).setLoopPingPong()
	else
		LeanTween.cancel(var_14_2.bowlShine.gameObject)

	setText(var_14_2.progress, string.format("<color=#%s>%s</color> %s", "FFD43F", math.min(var_14_0.data1, var_14_8) .. "/", var_14_8))

	local var_14_9 = var_14_0.data2 == 0 and "FFD43F" or "d2d4db"

	setActive(var_14_2.progress, var_14_8 > var_14_0.data1)
	setText(var_14_2.nums, string.format("<color=#%s>%s</color>", var_14_9, var_14_0.data2))

def var_0_0.displayBBAnim(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_0.findTF("bobing/bb_anim")
	local var_24_1 = arg_24_0.findTF("ship", var_24_0)
	local var_24_2 = arg_24_0.findTF("bowl", var_24_0)

	if not arg_24_0.animBowl:
		arg_24_0.animBowl = var_24_2.GetComponent(typeof(SpineAnimUI))

		arg_24_0.animBowl.SetAction("bobing", 0)
		arg_24_0.animBowl.SetActionCallBack(function(arg_25_0)
			if arg_25_0 == "finsih":
				setActive(var_24_1, False)
				setActive(var_24_2, False)
				arg_24_1())

	local function var_24_3()
		setActive(var_24_1, True)
		setActive(var_24_2, True)
		arg_24_0.model.GetComponent(typeof(SpineAnimUI)).SetAction("victory", 0)

	if not arg_24_0.model:
		local var_24_4 = getProxy(PlayerProxy).getRawData()
		local var_24_5 = getProxy(BayProxy).getShipById(var_24_4.character)

		PoolMgr.GetInstance().GetSpineChar(var_24_5.getPrefab(), False, function(arg_27_0)
			arg_24_0.model = arg_27_0
			arg_24_0.model.transform.localScale = Vector3(0.5, 0.5, 1)

			arg_24_0.model.transform.SetParent(var_24_1, False)
			var_24_3())
	else
		var_24_3()

	setActive(var_24_0, True)

def var_0_0.displayBBResult(arg_28_0, arg_28_1, arg_28_2, arg_28_3):
	arg_28_0.animation = findTF(arg_28_0._tf, "bobing")

	setActive(arg_28_0.findTF("bb_anim", arg_28_0.animation), False)

	local var_28_0 = arg_28_0.findTF("bb_result", arg_28_0.animation)
	local var_28_1 = arg_28_0.findTF("numbers", var_28_0)
	local var_28_2 = arg_28_0.findTF("number", var_28_0)
	local var_28_3 = arg_28_0.findTF("rank", var_28_0)
	local var_28_4 = arg_28_0.findTF("bgRank", var_28_0)

	setActive(var_28_2, False)

	local var_28_5 = arg_28_0.findTF("award", var_28_0)
	local var_28_6 = arg_28_0.findTF("award_list", var_28_0)

	setActive(var_28_5, False)
	removeAllChildren(var_28_6)

	if arg_28_1:
		for iter_28_0, iter_28_1 in ipairs(arg_28_1):
			local var_28_7 = cloneTplTo(var_28_5, var_28_6)
			local var_28_8 = {
				type = iter_28_1.type,
				id = iter_28_1.id,
				count = iter_28_1.count
			}

			updateDrop(var_28_7, var_28_8)
			onButton(arg_28_0, var_28_7, function()
				arg_28_0.emit(BaseUI.ON_DROP, var_28_8), SFX_PANEL)

	local var_28_9 = UIItemList.New(var_28_1, var_28_2)

	var_28_9.make(function(arg_30_0, arg_30_1, arg_30_2)
		if arg_30_0 == UIItemList.EventUpdate:
			arg_28_0.setSpriteTo("bobing/bb_icon/dice" .. arg_28_2[arg_30_1 + 1], arg_30_2)
			setImageAlpha(arg_30_2, 0))
	var_28_9.align(#arg_28_2)

	local var_28_10 = ActivityConst.BBRule(arg_28_2)

	setActive(var_28_3, var_28_10 < 7)
	setActive(var_28_4, var_28_10 < 7)

	if var_28_10 < 7:
		arg_28_0.setSpriteTo("bobing/bb_icon/rank" .. var_28_10, var_28_3)
		setImageAlpha(var_28_3, 0)

	local var_28_11 = False
	local var_28_12 = LeanTween.value(go(var_28_1), 0, 1, 1).setOnUpdate(System.Action_float(function(arg_31_0)
		var_28_9.each(function(arg_32_0, arg_32_1)
			setImageAlpha(arg_32_1, arg_31_0))))

	if var_28_10 == 7:
		var_28_12.setOnComplete(System.Action(function()
			arg_28_0.emit(ActivityMainScene.LOCK_ACT_MAIN, False)

			var_28_11 = True))
	else
		LeanTween.value(go(var_28_3), 0, 1, 0.2).setDelay(1).setOnUpdate(System.Action_float(function(arg_34_0)
			setImageAlpha(var_28_3, arg_34_0)

			var_28_3.localScale = Vector3.Lerp(Vector3(2, 2, 2), Vector3.one, arg_34_0)))

		local var_28_13 = arg_28_0.findTF("rank_p", var_28_0) or cloneTplTo(var_28_3, var_28_0, "rank_p")

		arg_28_0.setSpriteTo("bobing/bb_icon/rank" .. var_28_10, var_28_13)
		arg_28_0.setSpriteTo("bobing/bb_icon/rank" .. var_28_10, var_28_3)
		LeanTween.value(go(var_28_13), 1, 0, 0.3).setDelay(1.5).setOnUpdate(System.Action_float(function(arg_35_0)
			setImageAlpha(var_28_13, arg_35_0)

			var_28_13.localScale = Vector3.Lerp(Vector3(2, 2, 2), Vector3.one, arg_35_0))).setOnComplete(System.Action(function()
			arg_28_0.emit(ActivityMainScene.LOCK_ACT_MAIN, False)

			var_28_11 = True))

	setActive(var_28_0, True)
	onButton(arg_28_0, var_28_0, function()
		if var_28_11:
			setActive(var_28_0, False)
			arg_28_3())

def var_0_0.setSpriteTo(arg_38_0, arg_38_1, arg_38_2, arg_38_3):
	local var_38_0 = arg_38_2.GetComponent(typeof(Image))

	var_38_0.sprite = arg_38_0.findTF(arg_38_1).GetComponent(typeof(Image)).sprite

	if arg_38_3:
		var_38_0.SetNativeSize()

def var_0_0.OnDestroy(arg_39_0):
	if arg_39_0.bobingWrap:
		clearImageSprite(arg_39_0.bobingWrap.bg)
		LeanTween.cancel(arg_39_0.bobingWrap.bowlShine.gameObject)

return var_0_0
