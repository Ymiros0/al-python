local var_0_0 = class("OtherWorldTempleScene", import("..base.BaseUI"))
local var_0_1 = 3
local var_0_2 = "other_world_temple_toggle_1"
local var_0_3 = "other_world_temple_toggle_2"
local var_0_4 = "other_world_temple_toggle_3"
local var_0_5 = "other_world_temple_char"
local var_0_6 = "other_world_temple_award"
local var_0_7 = "other_world_temple_got"
local var_0_8 = "other_world_temple_progress"
local var_0_9 = "other_world_temple_char_title"
local var_0_10 = "other_world_temple_lottery_all"
local var_0_11 = "other_world_temple_award_desc"
local var_0_12 = "other_world_temple_pay"
local var_0_13 = "temple_consume_not_enough"
local var_0_14 = 30

def var_0_0.getUIName(arg_1_0):
	return "OtherWorldTempleUI"

def var_0_0.init(arg_2_0):
	arg_2_0.templeIds = pg.activity_template[ActivityConst.OTHER_WORLD_TERMINAL_LOTTERY_ID].config_data
	arg_2_0.shopDatas = {}

	for iter_2_0, iter_2_1 in ipairs(arg_2_0.templeIds):
		local var_2_0 = pg.activity_random_award_template[iter_2_1]
		local var_2_1 = {}

		for iter_2_2, iter_2_3 in ipairs(var_2_0.item_list):
			table.insert(var_2_1, {
				id = iter_2_3[1],
				count = iter_2_3[2]
			})

		table.insert(arg_2_0.shopDatas, var_2_1)

	arg_2_0.charIds = {}

	for iter_2_4, iter_2_5 in ipairs(pg.guardian_template.all):
		local var_2_2 = pg.guardian_template[iter_2_5]

		if table.contains(arg_2_0.templeIds, var_2_2.guardian_gain_pool):
			table.insert(arg_2_0.charIds, iter_2_5)

def var_0_0.didEnter(arg_3_0):
	local var_3_0 = findTF(arg_3_0._tf, "ad")
	local var_3_1 = findTF(arg_3_0._tf, "pop")

	arg_3_0.picTf = findTF(var_3_0, "pic")

	onButton(arg_3_0, findTF(var_3_0, "btnBack"), function()
		arg_3_0.closeView(), SFX_CANCEL)
	onButton(arg_3_0, findTF(var_3_0, "btnHelp"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.other_world_temple_tip.tip
		}), SFX_CONFIRM)

	arg_3_0.pageToggles = {}

	for iter_3_0 = 1, var_0_1:
		local var_3_2 = findTF(var_3_0, "pageToggle/bg/" .. iter_3_0)

		table.insert(arg_3_0.pageToggles, var_3_2)
		onButton(arg_3_0, var_3_2, function()
			local var_6_0 = iter_3_0

			arg_3_0.selectPage(var_6_0)
			arg_3_0.updateUI(), SFX_CONFIRM)

	onButton(arg_3_0, findTF(var_3_0, "btnDetail"), function()
		arg_3_0.emit(OtherWorldTempleMediator.OPEN_TERMINAL), SFX_CONFIRM)
	onButton(arg_3_0, findTF(var_3_0, "btnAward"), function()
		arg_3_0._awardPage.updateSelect(arg_3_0._selectIndex)
		arg_3_0._awardPage.setActive(True), SFX_CONFIRM)
	onButton(arg_3_0, findTF(var_3_0, "btnPay"), function()
		local var_9_0 = arg_3_0.activityPools[arg_3_0.templeIds[arg_3_0._selectIndex]].getleftItemCount()
		local var_9_1 = arg_3_0.lotteryCount

		if var_9_0 < var_9_1:
			var_9_1 = var_9_0

		local var_9_2 = arg_3_0.getResCount()
		local var_9_3 = arg_3_0.getConsume() * var_9_1

		if var_9_1 > 0 and var_9_3 <= var_9_2:
			if arg_3_0.activity.data1 != arg_3_0.templeIds[arg_3_0._selectIndex]:
				pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, {
					cmd = 2,
					activity_id = ActivityConst.OTHER_WORLD_TERMINAL_LOTTERY_ID,
					arg1 = arg_3_0.templeIds[arg_3_0._selectIndex]
				})

				function arg_3_0._payToLotterCallback()
					arg_3_0.payToLottery(var_9_1)
			else
				arg_3_0.payToLottery(var_9_1)
		elif var_9_2 < var_9_3:
			pg.TipsMgr.GetInstance().ShowTips(i18n(var_0_13)), SFX_CONFIRM)
	onButton(arg_3_0, findTF(var_3_0, "btnChars"), function()
		arg_3_0._charPage.updateSelect()
		arg_3_0._charPage.setActive(True), SFX_CONFIRM)
	onButton(arg_3_0, findTF(var_3_0, "btnMain"), function()
		arg_3_0.emit(BaseUI.ON_HOME), SFX_CONFIRM)

	arg_3_0._coinText = findTF(var_3_0, "coin/text")
	arg_3_0._charPage = OtherWorldTempleChars.New(findTF(arg_3_0._tf, "pop/charPage"), arg_3_0)

	arg_3_0._charPage.setData(arg_3_0.charIds)

	arg_3_0._awardPage = OtherWorldTempleAward.New(findTF(arg_3_0._tf, "pop/awardPage"), arg_3_0)

	arg_3_0._awardPage.setData(arg_3_0.templeIds, arg_3_0.shopDatas)
	arg_3_0._charPage.setActive(False)
	arg_3_0._awardPage.setActive(False)
	setText(findTF(var_3_0, "pageToggle/bg/1/unSelect/text"), i18n(var_0_2))
	setText(findTF(var_3_0, "pageToggle/bg/2/unSelect/text"), i18n(var_0_3))
	setText(findTF(var_3_0, "pageToggle/bg/3/unSelect/text"), i18n(var_0_4))
	setText(findTF(var_3_0, "btnChars/img/text"), i18n(var_0_5))
	setText(findTF(var_3_0, "btnAward/img/text"), i18n(var_0_6))
	setText(findTF(var_3_0, "desc/text"), i18n(var_0_11))
	setText(findTF(var_3_0, "btnComplete/img/text"), i18n(var_0_10))
	arg_3_0.selectPage(1)
	arg_3_0.updateActivity()

def var_0_0.payToLottery(arg_13_0, arg_13_1):
	if arg_13_0.waitActivityUpdate == True:
		return

	arg_13_0.checkCharAward = True
	arg_13_0.waitActivityUpdate = True
	arg_13_0.poolFetchCount = arg_13_0.activityPools[arg_13_0.templeIds[arg_13_0._selectIndex]].getFetchCount()

	pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, {
		cmd = 1,
		activity_id = ActivityConst.OTHER_WORLD_TERMINAL_LOTTERY_ID,
		arg1 = arg_13_1,
		arg2 = arg_13_0.templeIds[arg_13_0._selectIndex]
	})

def var_0_0.selectPage(arg_14_0, arg_14_1):
	arg_14_0._lastSelectIndex = arg_14_0._selectIndex
	arg_14_0._selectIndex = arg_14_1

	for iter_14_0 = 1, var_0_1:
		local var_14_0 = arg_14_0.pageToggles[iter_14_0]

		setActive(findTF(var_14_0, "select"), iter_14_0 == arg_14_0._selectIndex)
		setActive(findTF(var_14_0, "unSelect"), iter_14_0 != arg_14_0._selectIndex)

		if not arg_14_0._lastSelectIndex:
			local var_14_1 = iter_14_0 == arg_14_0._selectIndex and "alphaOn" or "alphaOff"

			GetComponent(findTF(arg_14_0.picTf, "img/" .. iter_14_0), typeof(Animator)).SetTrigger(var_14_1)
		elif arg_14_0._selectIndex != arg_14_0._lastSelectIndex:
			if arg_14_0._lastSelectIndex < arg_14_0._selectIndex:
				GetComponent(findTF(arg_14_0.picTf, "img/" .. arg_14_0._lastSelectIndex), typeof(Animator)).SetTrigger("leftOut")
				GetComponent(findTF(arg_14_0.picTf, "img/" .. arg_14_0._selectIndex), typeof(Animator)).SetTrigger("rightIn")
			else
				GetComponent(findTF(arg_14_0.picTf, "img/" .. arg_14_0._lastSelectIndex), typeof(Animator)).SetTrigger("rightOut")
				GetComponent(findTF(arg_14_0.picTf, "img/" .. arg_14_0._selectIndex), typeof(Animator)).SetTrigger("leftIn")

	local var_14_2 = arg_14_0.getResIconPath()

	LoadImageSpriteAsync(var_14_2, findTF(arg_14_0._tf, "ad/pt/img/icon"), False)
	LoadImageSpriteAsync(var_14_2, findTF(arg_14_0._tf, "ad/btnPay/img/icon"), False)

def var_0_0.updateUI(arg_15_0):
	local var_15_0 = arg_15_0.getConsume()
	local var_15_1 = arg_15_0.getResCount()
	local var_15_2 = arg_15_0.activityPools[arg_15_0.templeIds[arg_15_0._selectIndex]].getleftItemCount()
	local var_15_3 = math.min(var_15_2, var_0_14)
	local var_15_4 = math.floor(var_15_1 / var_15_0)

	arg_15_0.lotteryCount = math.min(var_15_3, var_15_4)

	if arg_15_0.lotteryCount <= 0:
		arg_15_0.lotteryCount = 1

	local var_15_5 = arg_15_0.getConsume() * arg_15_0.lotteryCount

	setText(findTF(arg_15_0._tf, "ad/btnPay/img/text"), var_15_5)
	setText(findTF(arg_15_0._tf, "ad/btnPay/img/desc"), i18n(var_0_12, arg_15_0.lotteryCount))
	setText(findTF(arg_15_0._tf, "ad/pt/img/text"), var_15_1)
	setActive(findTF(arg_15_0._tf, "ad/btnPay"), var_15_2 > 0)
	setActive(findTF(arg_15_0._tf, "ad/btnComplete"), var_15_2 <= 0)

	arg_15_0.grayComponent = GetComponent(findTF(arg_15_0._tf, "ad/btnComplete/img/bg"), typeof("UIGrayScale"))
	arg_15_0.grayComponent.enabled = False

	onNextTick(function()
		if arg_15_0.grayComponent:
			arg_15_0.grayComponent.enabled = True)

def var_0_0.getResCount(arg_17_0):
	local var_17_0 = getProxy(PlayerProxy).getData()
	local var_17_1 = pg.activity_random_award_template[arg_17_0.templeIds[arg_17_0._selectIndex]].resource_type

	return var_17_0.getResById(var_17_1) or 0

def var_0_0.getConsume(arg_18_0):
	return pg.activity_random_award_template[arg_18_0.templeIds[arg_18_0._selectIndex]].resource_num

def var_0_0.getResIconPath(arg_19_0):
	return Drop.New({
		type = DROP_TYPE_RESOURCE,
		id = pg.activity_random_award_template[arg_19_0.templeIds[arg_19_0._selectIndex]].resource_type
	}).getIcon()

def var_0_0.updateActivity(arg_20_0):
	arg_20_0.activity = getProxy(ActivityProxy).getActivityById(ActivityConst.OTHER_WORLD_TERMINAL_LOTTERY_ID)
	arg_20_0.awardInfos = arg_20_0.activity.getAwardInfos()
	arg_20_0.activityPools = {}

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.templeIds):
		local var_20_0 = ActivityItemPool.New({
			id = iter_20_1,
			awards = arg_20_0.awardInfos[iter_20_1],
			index = iter_20_0
		})

		arg_20_0.activityPools[var_20_0.id] = var_20_0

	if arg_20_0._payToLotterCallback:
		print("活动数据更新,当前奖池" .. arg_20_0.activity.data1)
		arg_20_0._payToLotterCallback()

		arg_20_0._payToLotterCallback = None
	else
		arg_20_0.updateUI()
		arg_20_0._awardPage.updateActivityPool(arg_20_0.activityPools)
		arg_20_0._charPage.updateActivityPool(arg_20_0.activityPools)

	arg_20_0.waitActivityUpdate = False

def var_0_0.displayTempleCharAward(arg_21_0):
	if arg_21_0.checkCharAward:
		local var_21_0 = arg_21_0.activityPools[arg_21_0.templeIds[arg_21_0._selectIndex]]

		if var_21_0.getFetchCount() == arg_21_0.poolFetchCount:
			return

		arg_21_0.checkCharAward = False

		local var_21_1 = var_21_0.getTempleNewChar(arg_21_0.poolFetchCount)

		if var_21_1 and #var_21_1 > 0:
			local var_21_2 = {}

			for iter_21_0, iter_21_1 in ipairs(var_21_1):
				local var_21_3 = pg.guardian_template[iter_21_1].drop

				for iter_21_2, iter_21_3 in ipairs(var_21_3):
					table.insert(var_21_2, Drop.New({
						type = iter_21_3[1],
						id = iter_21_3[2],
						count = iter_21_3[3]
					}))

			arg_21_0.emit(OtherWorldTempleMediator.SHOW_CHAR_AWARDS, var_21_2)

return var_0_0
