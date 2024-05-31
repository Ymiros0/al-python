local var_0_0 = class("ItemTipPanel", import(".MsgboxSubPanel"))

var_0_0.DetailConfig = {}

def var_0_0.ShowItemTip(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	local var_1_0 = var_0_0.GetDropLackConfig(Drop.New({
		type = arg_1_0,
		id = arg_1_1
	}))

	if not var_1_0:
		return

	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		type = MSGBOX_TYPE_ITEMTIP,
		drop = Drop.New({
			type = arg_1_0,
			id = arg_1_1
		}),
		descriptions = var_1_0.description,
		msgTitle = arg_1_2,
		goSceneCallack = arg_1_3,
		weight = LayerWeightConst.SECOND_LAYER
	})

	return True

def var_0_0.GetDropLackConfig(arg_2_0):
	if arg_2_0.type == DROP_TYPE_RESOURCE:
		arg_2_0 = Drop.New({
			type = DROP_TYPE_ITEM,
			id = id2ItemId(arg_2_0.id)
		})

	if not var_0_0.DetailConfig[arg_2_0.type]:
		var_0_0.DetailConfig[arg_2_0.type] = {}

		for iter_2_0, iter_2_1 in ipairs(pg.item_lack.get_id_list_by_drop_type[arg_2_0.type] or {}):
			local var_2_0 = pg.item_lack[iter_2_1]

			for iter_2_2, iter_2_3 in ipairs(var_2_0.itemids):
				var_0_0.DetailConfig[arg_2_0.type][iter_2_3] = var_2_0

	return var_0_0.DetailConfig[arg_2_0.type][arg_2_0.id]

def var_0_0.ShowItemTipbyID(...):
	return var_0_0.ShowItemTip(DROP_TYPE_ITEM, ...)

def var_0_0.CanShowTip(arg_4_0):
	return tobool(var_0_0.DetailConfig[arg_4_0])

def var_0_0.ShowRingBuyTip():
	GoShoppingMsgBox(i18n("switch_to_shop_tip_2", string.format("<color=#92FC63FF>%s</color>", Item.getConfigData(ITEM_ID_FOR_PROPOSE).name)), ChargeScene.TYPE_ITEM)

def var_0_0.ShowGoldBuyTip(arg_6_0):
	local var_6_0 = getProxy(PlayerProxy).getRawData()

	GoShoppingMsgBox(i18n("switch_to_shop_tip_2", i18n("word_gold")), ChargeScene.TYPE_ITEM, {
		{
			59001,
			arg_6_0 - var_6_0[id2res(1)],
			arg_6_0
		}
	})

def var_0_0.ShowOilBuyTip(arg_7_0, arg_7_1):
	local var_7_0 = getProxy(PlayerProxy).getRawData()
	local var_7_1 = ShoppingStreet.getRiseShopId(ShopArgs.BuyOil, var_7_0.buyOilCount)

	if not var_7_1:
		return

	local var_7_2 = pg.shop_template[var_7_1]
	local var_7_3 = var_7_2.num

	if var_7_2.num == -1 and var_7_2.genre == ShopArgs.BuyOil:
		var_7_3 = ShopArgs.getOilByLevel(var_7_0.level)

	if pg.gameset.buy_oil_limit.key_value <= var_7_0.buyOilCount:
		return

	arg_7_1 = arg_7_1 or "oil_buy_tip_2"

	pg.MsgboxMgr.GetInstance().ShowMsgBox({
		yseBtnLetf = True,
		type = MSGBOX_TYPE_SINGLE_ITEM,
		windowSize = {
			y = 570
		},
		content = i18n(arg_7_1, var_7_2.resource_num, var_7_3, var_7_0.buyOilCount, arg_7_0 - var_7_0[id2res(2)]),
		drop = {
			id = 2,
			type = DROP_TYPE_RESOURCE,
			count = var_7_3
		},
		def onYes:()
			pg.m02.sendNotification(GAME.SHOPPING, {
				isQuickShopping = True,
				count = 1,
				id = var_7_1
			}),
		weight = LayerWeightConst.TOP_LAYER
	})

	return True

def var_0_0.getUIName(arg_9_0):
	return "Msgbox4ItemGo"

def var_0_0.OnInit(arg_10_0):
	arg_10_0.list = arg_10_0.findTF("skipable_list")
	arg_10_0.tpl = arg_10_0.findTF("tpl", arg_10_0.list)
	arg_10_0.title = arg_10_0.findTF("name")

def var_0_0.OnRefresh(arg_11_0, arg_11_1):
	setActive(arg_11_0.viewParent._btnContainer, False)

	local var_11_0 = arg_11_1.drop.getName()
	local var_11_1 = arg_11_1.descriptions

	setText(arg_11_0.title, arg_11_1.msgTitle or i18n("item_lack_title", var_11_0, var_11_0))
	UIItemList.StaticAlign(arg_11_0.list, arg_11_0.tpl, #var_11_1, function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate:
			local var_12_0 = var_11_1[arg_12_1 + 1]
			local var_12_1, var_12_2, var_12_3 = unpack(var_12_0)
			local var_12_4, var_12_5 = unpack(var_12_2)
			local var_12_6 = #var_12_4 > 0

			if var_12_3 and var_12_3 != 0:
				var_12_6 = var_12_6 and getProxy(ActivityProxy).IsActivityNotEnd(var_12_3)

			local var_12_7 = arg_12_2.Find("skip_btn")

			setActive(var_12_7, var_12_6)
			onButton(arg_11_0, var_12_7, function()
				var_0_0.ConfigGoScene(var_12_4, var_12_5, function()
					if arg_11_1.goSceneCallack:
						arg_11_1.goSceneCallack()

					arg_11_0.viewParent.hide()), SFX_PANEL)
			Canvas.ForceUpdateCanvases()
			changeToScrollText(arg_12_2.Find("title"), var_12_1))

def var_0_0.ConfigGoScene(arg_15_0, arg_15_1, arg_15_2):
	arg_15_1 = arg_15_1 or {}

	if arg_15_0 == SCENE.SHOP and arg_15_1.warp == "supplies" and not pg.SystemOpenMgr.GetInstance().isOpenSystem(getProxy(PlayerProxy).getRawData().level, "MilitaryExerciseMediator"):
		pg.TipsMgr.GetInstance().ShowTips(i18n("military_shop_no_open_tip"))

		return
	elif arg_15_0 == SCENE.LEVEL:
		local var_15_0 = getProxy(ChapterProxy)
		local var_15_1 = getProxy(PlayerProxy).getRawData()

		if arg_15_1.leastChapterId:
			local var_15_2 = arg_15_1.leastChapterId
			local var_15_3 = var_15_0.getChapterById(var_15_2)
			local var_15_4 = var_15_0.getMapById(var_15_3.getConfig("map"))

			if not var_15_4:
				pg.TipsMgr.GetInstance().ShowTips(i18n("target_chapter_is_lock"))

				return
			elif not var_15_3.isUnlock() or var_15_4.getMapType() == Map.ELITE and not var_15_4.isEliteEnabled() or var_15_3.getConfig("unlocklevel") > var_15_1.level:
				pg.TipsMgr.GetInstance().ShowTips(i18n("target_chapter_is_lock"))

				return

		if arg_15_1.eliteDefault and not getProxy(DailyLevelProxy).IsEliteEnabled():
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_elite_no_quota"))

			return

		if arg_15_1.lastDigit:
			local var_15_5 = 0
			local var_15_6 = {}

			if arg_15_1.mapType:
				var_15_6 = var_15_0.getMapsByType(arg_15_1.mapType)
			else
				for iter_15_0, iter_15_1 in ipairs({
					Map.SCENARIO,
					Map.ELITE
				}):
					for iter_15_2, iter_15_3 in ipairs(var_15_0.getMapsByType(iter_15_1)):
						table.insert(var_15_6, iter_15_3)

			for iter_15_4, iter_15_5 in ipairs(var_15_6):
				if iter_15_5.isUnlock() and (arg_15_1.mapType != Map.ELITE or iter_15_5.isEliteEnabled()) and var_15_5 < iter_15_5.id:
					for iter_15_6, iter_15_7 in pairs(iter_15_5.getChapters()):
						if math.fmod(iter_15_7.id, 10) == arg_15_1.lastDigit and iter_15_7.isUnlock() and iter_15_7.getConfig("unlocklevel") <= var_15_1.level:
							arg_15_1.chapterId = iter_15_7.id
							var_15_5 = iter_15_5.id
							arg_15_1.mapIdx = iter_15_5.id

							break

		if arg_15_1.chapterId:
			local var_15_7 = arg_15_1.chapterId
			local var_15_8 = var_15_0.getChapterById(var_15_7)
			local var_15_9 = var_15_0.getMapById(var_15_8.getConfig("map"))

			if var_15_9 and var_15_9.getMapType() == Map.ELITE and not getProxy(DailyLevelProxy).IsEliteEnabled():
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_elite_no_quota"))

				return

			if var_15_8.isUnlock():
				if var_15_8.active:
					arg_15_1.mapIdx = var_15_8.getConfig("map")
				elif var_15_0.getActiveChapter():
					pg.MsgboxMgr.GetInstance().ShowMsgBox({
						content = i18n("collect_chapter_is_activation"),
						def onYes:()
							pg.m02.sendNotification(GAME.CHAPTER_OP, {
								type = ChapterConst.OpRetreat
							})
					})

					return
				else
					arg_15_1.mapIdx = var_15_8.getConfig("map")
					arg_15_1.openChapterId = var_15_7
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("target_chapter_is_lock"))
	elif arg_15_0 == SCENE.TASK and arg_15_1.awards:
		local var_15_10 = {}

		for iter_15_8, iter_15_9 in ipairs(arg_15_1.awards):
			var_15_10[iter_15_9] = True

		local var_15_11

		if next(var_15_10):
			local var_15_12 = getProxy(TaskProxy).getRawData()

			for iter_15_10, iter_15_11 in pairs(var_15_12):
				local var_15_13 = False

				for iter_15_12, iter_15_13 in ipairs(iter_15_11.getConfig("award_display")):
					if var_15_10[iter_15_13[2]]:
						var_15_11 = iter_15_11.id
						var_15_13 = True

						break

				if var_15_13:
					break

		if not var_15_11:
			pg.TipsMgr.GetInstance().ShowTips(i18n("task_has_finished"))

			return

		arg_15_1.targetId = var_15_11
	elif arg_15_0 == SCENE.COLLECTSHIP:
		arg_15_1.toggle = 2
	elif arg_15_0 == SCENE.DAILYLEVEL and arg_15_1.dailyLevelId:
		local var_15_14, var_15_15 = DailyLevelScene.CanOpenDailyLevel(arg_15_1.dailyLevelId)

		if not var_15_14:
			pg.TipsMgr.GetInstance().ShowTips(var_15_15)

			return
	elif arg_15_0 == SCENE.MILITARYEXERCISE and not getProxy(MilitaryExerciseProxy).getSeasonInfo().canExercise():
		pg.TipsMgr.GetInstance().ShowTips(i18n("exercise_count_insufficient"))

		return

	existCall(arg_15_2)
	pg.m02.sendNotification(GAME.GO_SCENE, arg_15_0, arg_15_1)

return var_0_0
