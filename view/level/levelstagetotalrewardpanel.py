local var_0_0 = class("LevelStageTotalRewardPanel", import("view.level.BaseTotalRewardPanel"))

def var_0_0.getUIName(arg_1_0):
	return "LevelStageTotalRewardPanel"

local var_0_1 = 0.15

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

	arg_2_0.itemList = arg_2_0.boxView.Find("Content/ItemGrid")

	local var_2_0 = Instantiate(arg_2_0.itemList.GetComponent(typeof(ItemList)).prefabItem[0])

	var_2_0.name = "Icon"

	setParent(var_2_0, arg_2_0.itemList.Find("GridItem/Shell"))

	arg_2_0.itemListSub = arg_2_0.boxView.Find("Content/ItemGridSub")

	cloneTplTo(var_2_0, arg_2_0.itemListSub.Find("GridItem/Shell"), var_2_0.name)

	arg_2_0.spList = arg_2_0.window.Find("Fixed/SpList")

	arg_2_0.CloneIconTpl(arg_2_0.spList.Find("Item/Active/Item"), "Icon")
	setText(arg_2_0.boxView.Find("Content/Title/Text"), i18n("battle_end_subtitle1"))
	setText(arg_2_0.boxView.Find("Content/TitleSub/Text"), i18n("settle_rewards_text"))

def var_0_0.didEnter(arg_3_0):
	var_0_0.super.didEnter(arg_3_0)

	local var_3_0 = arg_3_0.contextData.isAutoFight
	local var_3_1 = PlayerPrefs.GetInt(AUTO_BATTLE_LABEL, 0) > 0

	if var_3_0 and var_3_1:
		pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_AUTO_BATTLE)
		LuaHelper.Vibrate()

	local var_3_2 = getProxy(MetaCharacterProxy).getMetaTacticsInfoOnEnd()

	if var_3_2 and #var_3_2 > 0:
		arg_3_0.metaExpView = MetaExpView.New(arg_3_0.window.Find("Layout"), arg_3_0.event, arg_3_0.contextData)

		local var_3_3 = arg_3_0.metaExpView

		var_3_3.Reset()
		var_3_3.Load()
		var_3_3.setData(var_3_2)
		var_3_3.ActionInvoke("Show")

def var_0_0.willExit(arg_4_0):
	arg_4_0.SkipAnim()

	if arg_4_0.metaExpView:
		arg_4_0.metaExpView.Destroy()

	var_0_0.super.willExit(arg_4_0)

def var_0_0.UpdateView(arg_5_0):
	local var_5_0 = arg_5_0.contextData

	onButton(arg_5_0, arg_5_0._tf.Find("BG"), function()
		if arg_5_0.isRewardAnimating:
			arg_5_0.SkipAnim()

			return

		existCall(var_5_0.onClose)
		arg_5_0.closeView())
	onButton(arg_5_0, arg_5_0.window.Find("Fixed/ButtonGO"), function()
		if arg_5_0.contextData.spItemID and not (PlayerPrefs.GetInt("autoFight_firstUse_sp", 0) == 1):
			PlayerPrefs.SetInt("autoFight_firstUse_sp", 1)
			PlayerPrefs.Save()

			local function var_7_0()
				arg_5_0.contextData.spItemID = None

				arg_5_0.UpdateSPItem()

			arg_5_0.HandleShowMsgBox({
				hideNo = True,
				content = i18n("autofight_special_operation_tip"),
				onYes = var_7_0,
				onNo = var_7_0
			})

			return

		local var_7_1 = Chapter.GetSPOperationItemCacheKey(arg_5_0.contextData.chapter.id)

		PlayerPrefs.SetInt(var_7_1, arg_5_0.contextData.spItemID or 0)

		local var_7_2 = True

		arg_5_0.emit(LevelMediator2.ON_RETRACKING, arg_5_0.contextData.chapter, var_7_2)
		arg_5_0.closeView(), SFX_CONFIRM)
	onButton(arg_5_0, arg_5_0.window.Find("Fixed/ButtonExit"), function()
		existCall(var_5_0.onClose)
		arg_5_0.closeView(), SFX_CANCEL)
	arg_5_0.UpdateSPItem()

	local var_5_1 = var_5_0.rewards
	local var_5_2 = var_5_0.resultRewards
	local var_5_3 = var_5_0.events
	local var_5_4 = var_5_0.guildTasks
	local var_5_5 = var_5_0.guildAutoReceives
	local var_5_6 = var_5_1 and #var_5_1 > 0
	local var_5_7 = var_5_2 and #var_5_2 > 0
	local var_5_8 = var_5_3 and #var_5_3 > 0
	local var_5_9 = var_5_4 and table.getCount(var_5_4) > 0
	local var_5_10 = var_5_5 and table.getCount(var_5_5) > 0
	local var_5_11 = True
	local var_5_12 = {}

	setActive(arg_5_0.boxView.Find("Content/Title"), False)
	setActive(arg_5_0.itemList, False)

	if var_5_6:
		var_5_11 = False
		arg_5_0.hasRewards = True

		table.insert(var_5_12, function(arg_10_0)
			setActive(arg_5_0.boxView.Find("Content/Title"), True)
			setActive(arg_5_0.itemList, True)
			arg_10_0())

		local var_5_13 = CustomIndexLayer.Clone2Full(arg_5_0.itemList, #var_5_1)

		for iter_5_0, iter_5_1 in ipairs(var_5_13):
			local var_5_14 = var_5_1[iter_5_0]
			local var_5_15 = var_5_13[iter_5_0]

			updateDrop(var_5_15.Find("Shell/Icon"), var_5_14)
			onButton(arg_5_0, var_5_15.Find("Shell/Icon"), function()
				arg_5_0.emit(BaseUI.ON_DROP, var_5_14), SFX_PANEL)

		arg_5_0.isRewardAnimating = True

		for iter_5_2 = 1, #var_5_1:
			local var_5_16 = var_5_13[iter_5_2]

			setActive(var_5_16, False)
			table.insert(var_5_12, function(arg_12_0)
				if arg_5_0.exited:
					return

				setActive(var_5_16, True)
				scrollTo(arg_5_0.boxView.Find("Content"), {
					y = 0
				})

				arg_5_0.LTid = LeanTween.delayedCall(var_0_1, System.Action(arg_12_0)).uniqueId)

	setActive(arg_5_0.boxView.Find("Content/TitleSub"), False)
	setActive(arg_5_0.itemListSub, False)

	if var_5_7:
		var_5_11 = False
		arg_5_0.hasResultRewards = True

		table.insert(var_5_12, function(arg_13_0)
			setActive(arg_5_0.boxView.Find("Content/TitleSub"), True)
			setActive(arg_5_0.itemListSub, True)
			arg_13_0())

		local var_5_17 = CustomIndexLayer.Clone2Full(arg_5_0.itemListSub, #var_5_2)

		for iter_5_3, iter_5_4 in ipairs(var_5_17):
			local var_5_18 = var_5_2[iter_5_3]
			local var_5_19 = var_5_17[iter_5_3]

			updateDrop(var_5_19.Find("Shell/Icon"), var_5_18)
			onButton(arg_5_0, var_5_19.Find("Shell/Icon"), function()
				arg_5_0.emit(BaseUI.ON_DROP, var_5_18), SFX_PANEL)

		arg_5_0.isRewardAnimating = True

		local var_5_20 = {}

		for iter_5_5 = 1, #var_5_2:
			local var_5_21 = var_5_17[iter_5_5]

			setActive(var_5_21, False)
			table.insert(var_5_12, function(arg_15_0)
				if arg_5_0.exited:
					return

				setActive(var_5_21, True)
				scrollTo(arg_5_0.boxView.Find("Content"), {
					y = 0
				})

				arg_5_0.LTid = LeanTween.delayedCall(var_0_1, System.Action(arg_15_0)).uniqueId)

	setActive(arg_5_0.boxView.Find("Content/TextArea"), False)

	local var_5_22 = {}

	if var_5_8:
		for iter_5_6, iter_5_7 in ipairs(var_5_3):
			local var_5_23 = pg.collection_template[iter_5_7] and pg.collection_template[iter_5_7].title or ""

			table.insert(var_5_22, i18n("autofight_entrust", var_5_23))

	if var_5_9:
		for iter_5_8, iter_5_9 in pairs(var_5_4):
			table.insert(var_5_22, i18n("autofight_task", iter_5_9))

	if var_5_10:
		for iter_5_10, iter_5_11 in pairs(var_5_5):
			table.insert(var_5_22, i18n("guild_task_autoaccept_1", iter_5_11))

	if #var_5_22 > 0:
		var_5_11 = False
		arg_5_0.hasEventMsg = True

		setText(arg_5_0.boxView.Find("Content/TextArea/Text"), table.concat(var_5_22, "\n"))
		table.insert(var_5_12, function(arg_16_0)
			setActive(arg_5_0.boxView.Find("Content/TextArea"), True)
			arg_16_0())

	setActive(arg_5_0.boxView, not var_5_11)
	setActive(arg_5_0.emptyTip, var_5_11)
	seriesAsync(var_5_12, function()
		arg_5_0.SkipAnim())

def var_0_0.UpdateSPItem(arg_18_0):
	local var_18_0 = getProxy(BagProxy).getItemsByType(Item.SPECIAL_OPERATION_TICKET)
	local var_18_1 = arg_18_0.contextData.chapter.getConfig("special_operation_list")

	var_18_1 = var_18_1 == "" and {} or var_18_1

	local var_18_2 = {}

	for iter_18_0, iter_18_1 in ipairs(pg.benefit_buff_template.all):
		local var_18_3 = pg.benefit_buff_template[iter_18_1]

		if var_18_3.benefit_type == Chapter.OPERATION_BUFF_TYPE_DESC and table.contains(var_18_1, iter_18_1):
			table.insert(var_18_2, var_18_3)

	local var_18_4 = 1

	setActive(arg_18_0.spList, #var_18_2 != 0 and arg_18_0.contextData.chapter.GetRestDailyBonus() == 0)

	if #var_18_2 == 0:
		return

	UIItemList.StaticAlign(arg_18_0.spList, arg_18_0.spList.GetChild(0), var_18_4, function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 != UIItemList.EventUpdate:
			return

		local var_19_0 = var_18_2[arg_19_1 + 1]
		local var_19_1 = tonumber(var_19_0.benefit_condition)

		setText(arg_19_2.Find("Active/Desc"), var_19_0.desc)

		local var_19_2 = _.detect(var_18_0, function(arg_20_0)
			return arg_20_0.configId == var_19_1)
		local var_19_3 = var_19_2 and var_19_2.count > 0

		setActive(arg_19_2.Find("Active"), var_19_3)
		setActive(arg_19_2.Find("Block"), not var_19_3)

		if not var_19_3:
			setText(arg_19_2.Find("Block").Find("Desc"), i18n("levelScene_select_noitem"))

			return

		setActive(arg_19_2.Find("Active/Item"), True)
		updateDrop(arg_19_2.Find("Active/Item/Icon"), Drop.New({
			id = var_19_1,
			type = DROP_TYPE_ITEM,
			count = var_19_2 and var_19_2.count or 0
		}))
		onButton(arg_18_0, arg_19_2, function()
			arg_18_0.contextData.spItemID = not arg_18_0.contextData.spItemID and var_19_1 or None

			if arg_18_0.contextData.spItemID:
				pg.TipsMgr.GetInstance().ShowTips(i18n("levelScene_select_sp"))

			arg_18_0.UpdateSPItem(), SFX_PANEL)
		onButton(arg_18_0, arg_19_2.Find("Active/Item/Icon"), function()
			arg_18_0.emit(BaseUI.ON_ITEM, var_19_1))
		setActive(arg_19_2.Find("Active/Checkbox/Mark"), tobool(arg_18_0.contextData.spItemID)))

def var_0_0.SkipAnim(arg_23_0):
	if not arg_23_0.isRewardAnimating:
		return

	arg_23_0.isRewardAnimating = None

	if arg_23_0.LTid:
		LeanTween.cancel(arg_23_0.LTid)

		arg_23_0.LTid = None

	eachChild(arg_23_0.itemList, function(arg_24_0)
		setActive(arg_24_0, True))
	eachChild(arg_23_0.itemListSub, function(arg_25_0)
		setActive(arg_25_0, True))
	setActive(arg_23_0.boxView.Find("Content/Title"), arg_23_0.hasRewards)
	setActive(arg_23_0.itemList, arg_23_0.hasRewards)
	setActive(arg_23_0.boxView.Find("Content/TitleSub"), arg_23_0.hasResultRewards)
	setActive(arg_23_0.itemListSub, arg_23_0.hasResultRewards)
	setActive(arg_23_0.boxView.Find("Content/TextArea"), arg_23_0.hasEventMsg)

return var_0_0
