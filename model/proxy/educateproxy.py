local var_0_0 = class("EducateProxy", import(".NetProxy"))

var_0_0.RESOURCE_UPDATED = "EducateProxy.RESOURCE_UPDATED"
var_0_0.ATTR_UPDATED = "EducateProxy.ATTR_UPDATED"
var_0_0.TIME_UPDATED = "EducateProxy.TIME_UPDATED"
var_0_0.TIME_WEEKDAY_UPDATED = "EducateProxy.TIME_WEEKDAY_UPDATED"
var_0_0.BUFF_ADDED = "EducateProxy.BUFF_ADDED"
var_0_0.OPTION_UPDATED = "EducateProxy.OPTION_UPDATED"
var_0_0.ENDING_ADDED = "EducateProxy.ENDING_ADDED"
var_0_0.ITEM_ADDED = "EducateProxy.ITEM_ADDED"
var_0_0.POLAROID_ADDED = "EducateProxy.POLAROID_ADDED"
var_0_0.MEMORY_ADDED = "EducateProxy.MEMORY_ADDED"
var_0_0.UNLCOK_NEW_SECRETARY_BY_CNT = "EducateProxy.UNLCOK_NEW_SECRETARY_BY_CNT"
var_0_0.GUIDE_CHECK = "EducateProxy.GUIDE_CHECK"
var_0_0.MAIN_SCENE_ADD_LAYER = "EducateProxy.MAIN_SCENE_ADD_LAYER"
var_0_0.CLEAR_NEW_TIP = "EducateProxy.CLEAR_NEW_TIP"

def var_0_0.register(arg_1_0):
	arg_1_0.planProxy = EducatePlanProxy.New(arg_1_0)
	arg_1_0.eventProxy = EducateEventProxy.New(arg_1_0)
	arg_1_0.shopProxy = EducateShopProxy.New(arg_1_0)
	arg_1_0.taskProxy = EducateTaskProxy.New(arg_1_0)
	arg_1_0.endTime = pg.gameset.child_end_data.description

	arg_1_0.on(27021, function(arg_2_0)
		for iter_2_0, iter_2_1 in ipairs(arg_2_0.tasks):
			arg_1_0.taskProxy.AddTask(iter_2_1))
	arg_1_0.on(27022, function(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0.ids):
			arg_1_0.taskProxy.RemoveTaskById(iter_3_1))
	arg_1_0.on(27025, function(arg_4_0)
		for iter_4_0, iter_4_1 in ipairs(arg_4_0.tasks):
			arg_1_0.taskProxy.UpdateTask(iter_4_1))

def var_0_0.initData(arg_5_0, arg_5_1):
	arg_5_0.sendNotification(GAME.EDUCATE_GET_ENDINGS)

	local var_5_0 = arg_5_1.child

	arg_5_0.exsitEnding = var_5_0.is_ending == 1 or False
	arg_5_0.gameCount = var_5_0.new_game_plus_count
	arg_5_0.curTime = var_5_0.cur_time or {
		week = 1,
		month = 3,
		day = 7
	}
	arg_5_0.char = EducateChar.New(var_5_0)

	arg_5_0.eventProxy.SetUp({
		waitTriggerEventIds = var_5_0.home_events,
		needRequestHomeEvents = var_5_0.can_trigger_home_event == 1 or False,
		finishSpecEventIds = var_5_0.spec_events
	})
	arg_5_0.planProxy.SetUp({
		history = var_5_0.plan_history,
		selectedPlans = var_5_0.plans
	})
	arg_5_0.shopProxy.SetUp({
		shops = var_5_0.shop,
		discountEventIds = var_5_0.discount_event_id
	})
	arg_5_0.taskProxy.SetUp({
		targetId = var_5_0.target,
		tasks = var_5_0.tasks,
		finishMindTaskIds = var_5_0.realized_wish,
		isGotTargetAward = var_5_0.had_target_stage_award == 1 or False
	})
	arg_5_0.initItems(var_5_0.items)
	arg_5_0.initPolaroids(var_5_0.polaroids)

	arg_5_0.memories = var_5_0.memorys

	arg_5_0.initBuffs(var_5_0.buffs)
	arg_5_0.initOptions(var_5_0.option_records)

	arg_5_0.siteRandomOpts = None

	arg_5_0.UpdateGameStatus()
	arg_5_0.initVirtualStage()
	arg_5_0.initUnlockSecretary(var_5_0.is_special_secretary_valid == 1)

	arg_5_0.requestDataEnd = True

def var_0_0.CheckDataRequestEnd(arg_6_0):
	return arg_6_0.requestDataEnd

def var_0_0.initItems(arg_7_0, arg_7_1):
	arg_7_0.itemData = {}

	for iter_7_0, iter_7_1 in ipairs(arg_7_1):
		arg_7_0.itemData[iter_7_1.id] = EducateItem.New(iter_7_1)

def var_0_0.initOptions(arg_8_0, arg_8_1):
	local var_8_0 = {}

	for iter_8_0, iter_8_1 in ipairs(arg_8_1):
		var_8_0[iter_8_1.id] = iter_8_1.count

	arg_8_0.siteOptionData = {}

	for iter_8_2, iter_8_3 in ipairs(pg.child_site_option.all):
		local var_8_1 = EducateSiteOption.New(iter_8_3, var_8_0[iter_8_3])

		arg_8_0.siteOptionData[iter_8_3] = var_8_1

def var_0_0.initRandomOpts(arg_9_0, arg_9_1):
	arg_9_0.siteRandomOpts = {}

	for iter_9_0, iter_9_1 in ipairs(arg_9_1):
		arg_9_0.siteRandomOpts[iter_9_1.site_id] = iter_9_1.option_ids

def var_0_0.NeedRequestOptsData(arg_10_0):
	return not arg_10_0.siteRandomOpts

def var_0_0.initBuffs(arg_11_0, arg_11_1):
	arg_11_0.buffData = {}

	for iter_11_0, iter_11_1 in ipairs(arg_11_1):
		arg_11_0.buffData[iter_11_1.id] = EducateBuff.New(iter_11_1)

def var_0_0.initPolaroids(arg_12_0, arg_12_1):
	arg_12_0.polaroidData = {}

	for iter_12_0, iter_12_1 in ipairs(arg_12_1):
		arg_12_0.polaroidData[iter_12_1.id] = EducatePolaroid.New(iter_12_1)

def var_0_0.SetEndings(arg_13_0, arg_13_1):
	arg_13_0.endings = arg_13_1

	arg_13_0.updateSecretaryIDs()

def var_0_0.IsFirstGame(arg_14_0):
	return arg_14_0.gameCount == 1

def var_0_0.UpdateGameStatus(arg_15_0):
	arg_15_0.gameStatus = EducateConst.STATUES_NORMAL

	if arg_15_0.exsitEnding:
		arg_15_0.gameStatus = EducateConst.STATUES_RESET
	elif arg_15_0.IsEndingTime():
		arg_15_0.gameStatus = EducateConst.STATUES_ENDING
	elif arg_15_0.taskProxy.CheckTargetSet():
		arg_15_0.gameStatus = EducateConst.STATUES_PREPARE

def var_0_0.GetGameStatus(arg_16_0):
	return arg_16_0.gameStatus

def var_0_0.initVirtualStage(arg_17_0):
	local var_17_0 = getProxy(EducateProxy).GetTaskProxy().GetTargetId()
	local var_17_1 = arg_17_0.char.GetStage()

	if var_17_0 != 0 and pg.child_target_set[var_17_0].stage == var_17_1 + 1:
		arg_17_0.isVirtualStage = True
	else
		arg_17_0.isVirtualStage = False

def var_0_0.SetVirtualStage(arg_18_0, arg_18_1):
	arg_18_0.isVirtualStage = arg_18_1

def var_0_0.InVirtualStage(arg_19_0):
	return arg_19_0.isVirtualStage

def var_0_0.Reset(arg_20_0, arg_20_1):
	EducateTipHelper.ClearAllRecord()
	arg_20_0.GetPlanProxy().ClearLocalPlansData()
	arg_20_0.sendNotification(GAME.EDUCATE_REQUEST, {
		callback = arg_20_1
	})

def var_0_0.Refresh(arg_21_0, arg_21_1):
	EducateTipHelper.ClearAllRecord()
	arg_21_0.GetPlanProxy().ClearLocalPlansData()
	arg_21_0.sendNotification(GAME.EDUCATE_REQUEST, {
		callback = arg_21_1
	})

def var_0_0.GetCurTime(arg_22_0):
	return arg_22_0.curTime

def var_0_0.UpdateTime(arg_23_0):
	arg_23_0.curTime.week = arg_23_0.curTime.week + 1

	if arg_23_0.curTime.week > 4:
		arg_23_0.curTime.week = 1
		arg_23_0.curTime.month = arg_23_0.curTime.month + 1

def var_0_0.OnNextWeek(arg_24_0):
	arg_24_0.SetVirtualStage(False)
	arg_24_0.UpdateTime()
	arg_24_0.char.OnNewWeek(arg_24_0.curTime)
	arg_24_0.planProxy.OnNewWeek(arg_24_0.curTime)
	arg_24_0.eventProxy.OnNewWeek(arg_24_0.curTime)
	arg_24_0.shopProxy.OnNewWeek(arg_24_0.curTime)
	arg_24_0.taskProxy.OnNewWeek(arg_24_0.curTime)
	arg_24_0.RefreshBuffs()
	arg_24_0.RefreshOptions()

	arg_24_0.siteRandomOpts = None

	arg_24_0.UpdateGameStatus()
	arg_24_0.sendNotification(var_0_0.TIME_UPDATED)

def var_0_0.GetCharData(arg_25_0):
	return arg_25_0.char

def var_0_0.GetPersonalityId(arg_26_0):
	return arg_26_0.char.GetPersonalityId()

def var_0_0.UpdateRes(arg_27_0, arg_27_1, arg_27_2):
	arg_27_0.char.UpdateRes(arg_27_1, arg_27_2)
	arg_27_0.sendNotification(var_0_0.RESOURCE_UPDATED)

def var_0_0.ReduceResForPlans(arg_28_0):
	local var_28_0, var_28_1 = arg_28_0.planProxy.GetCost()

	arg_28_0.UpdateRes(EducateChar.RES_MONEY_ID, -var_28_0)
	arg_28_0.UpdateRes(EducateChar.RES_MOOD_ID, -var_28_1)

def var_0_0.ReduceResForCosts(arg_29_0, arg_29_1):
	for iter_29_0, iter_29_1 in ipairs(arg_29_1):
		arg_29_0.UpdateRes(iter_29_1.id, -iter_29_1.num)

def var_0_0.UpdateAttr(arg_30_0, arg_30_1, arg_30_2):
	arg_30_0.char.UpdateAttr(arg_30_1, arg_30_2)
	arg_30_0.sendNotification(var_0_0.ATTR_UPDATED)

def var_0_0.CheckExtraAttr(arg_31_0):
	return arg_31_0.char.CheckExtraAttrAdd()

def var_0_0.AddExtraAttr(arg_32_0, arg_32_1):
	arg_32_0.UpdateAttr(arg_32_1, arg_32_0.char.getConfig("attr_2_add"))
	arg_32_0.char.SetIsAddedExtraAttr(True)

def var_0_0.GetPlanProxy(arg_33_0):
	return arg_33_0.planProxy

def var_0_0.GetEventProxy(arg_34_0):
	return arg_34_0.eventProxy

def var_0_0.GetShopProxy(arg_35_0):
	return arg_35_0.shopProxy

def var_0_0.GetTaskProxy(arg_36_0):
	return arg_36_0.taskProxy

def var_0_0.GetFinishEndings(arg_37_0):
	return arg_37_0.endings

def var_0_0.AddEnding(arg_38_0, arg_38_1):
	arg_38_0.exsitEnding = True

	arg_38_0.UpdateGameStatus()

	if table.contains(arg_38_0.endings, arg_38_1):
		return

	table.insert(arg_38_0.endings, arg_38_1)

	local var_38_0 = Clone(arg_38_0.GetSecretaryIDs())

	arg_38_0.updateSecretaryIDs()
	getProxy(SettingsProxy).UpdateEducateCharTip(var_38_0)
	arg_38_0.sendNotification(var_0_0.ENDING_ADDED)

def var_0_0.IsEndingTime(arg_39_0):
	local var_39_0 = arg_39_0.GetCurTime()

	if var_39_0.month >= arg_39_0.endTime[1] and var_39_0.week >= arg_39_0.endTime[2] and var_39_0.day >= arg_39_0.endTime[3]:
		return True

	return False

def var_0_0.GetEndingResult(arg_40_0):
	local var_40_0 = underscore.detect(pg.child_ending.all, function(arg_41_0)
		local var_41_0 = pg.child_ending[arg_41_0].condition

		return arg_40_0.char.CheckEndCondition(var_41_0))

	assert(var_40_0, "not matching ending")

	return var_40_0

def var_0_0.GetBuffData(arg_42_0):
	return arg_42_0.buffData

def var_0_0.GetBuffList(arg_43_0):
	local var_43_0 = {}

	for iter_43_0, iter_43_1 in pairs(arg_43_0.buffData):
		table.insert(var_43_0, iter_43_1)

	return var_43_0

def var_0_0.AddBuff(arg_44_0, arg_44_1):
	if arg_44_0.buffData[arg_44_1]:
		arg_44_0.buffData[arg_44_1].ResetEndTime()
	else
		arg_44_0.buffData[arg_44_1] = EducateBuff.New({
			id = arg_44_1
		})

	arg_44_0.sendNotification(var_0_0.BUFF_ADDED)

def var_0_0.RefreshBuffs(arg_45_0):
	for iter_45_0, iter_45_1 in pairs(arg_45_0.buffData):
		if iter_45_1.IsEnd():
			arg_45_0.buffData[iter_45_1.id] = None

def var_0_0.GetAttrBuffEffects(arg_46_0, arg_46_1):
	local var_46_0 = {}

	for iter_46_0, iter_46_1 in pairs(arg_46_0.buffData):
		if iter_46_1.IsAttrType() and iter_46_1.IsId(arg_46_1):
			table.insert(var_46_0, iter_46_1)

	return EducateBuff.GetBuffEffects(var_46_0)

def var_0_0.GetResBuffEffects(arg_47_0, arg_47_1):
	local var_47_0 = {}

	for iter_47_0, iter_47_1 in pairs(arg_47_0.buffData):
		if iter_47_1.IsResType() and iter_47_1.IsId(arg_47_1):
			table.insert(var_47_0, iter_47_1)

	return EducateBuff.GetBuffEffects(var_47_0)

def var_0_0.GetOptionById(arg_48_0, arg_48_1):
	return arg_48_0.siteOptionData[arg_48_1]

def var_0_0.UpdateOptionData(arg_49_0, arg_49_1):
	arg_49_0.siteOptionData[arg_49_1.id] = arg_49_1

	arg_49_0.sendNotification(var_0_0.OPTION_UPDATED)

def var_0_0.RefreshOptions(arg_50_0):
	local var_50_0 = arg_50_0.GetCurTime()

	for iter_50_0, iter_50_1 in pairs(arg_50_0.siteOptionData):
		iter_50_1.OnWeekUpdate(var_50_0)

def var_0_0.GetShowSiteIds(arg_51_0):
	return underscore.select(pg.child_site.all, function(arg_52_0)
		return pg.child_site[arg_52_0].type == 1 and EducateHelper.IsSiteUnlock(arg_52_0, arg_51_0.IsFirstGame()))

def var_0_0.GetOptionsBySiteId(arg_53_0, arg_53_1):
	local var_53_0 = pg.child_site[arg_53_1].option
	local var_53_1 = arg_53_0.GetCurTime()
	local var_53_2 = {}
	local var_53_3 = {}

	underscore.each(var_53_0, function(arg_54_0)
		local var_54_0 = arg_53_0.siteOptionData[arg_54_0]

		if var_54_0 and var_54_0.IsShow(var_53_1):
			if var_54_0.IsReplace():
				var_53_3[var_54_0.getConfig("replace")] = var_54_0
			else
				table.insert(var_53_2, var_54_0))
	underscore.each(var_53_2, function(arg_55_0)
		if var_53_3[arg_55_0.id]:
			table.removebyvalue(var_53_2, arg_55_0)
			table.insert(var_53_2, var_53_3[arg_55_0.id]))

	local var_53_4 = arg_53_0.siteRandomOpts and arg_53_0.siteRandomOpts[arg_53_1] or {}

	underscore.each(var_53_4, function(arg_56_0)
		local var_56_0 = arg_53_0.siteOptionData[arg_56_0]

		if var_56_0.IsShow(var_53_1):
			table.insert(var_53_2, var_56_0))
	table.sort(var_53_2, CompareFuncs({
		function(arg_57_0)
			return arg_57_0.getConfig("order"),
		function(arg_58_0)
			return arg_58_0.id
	}))

	return var_53_2

def var_0_0.GetItemData(arg_59_0):
	return arg_59_0.itemData

def var_0_0.GetItemList(arg_60_0):
	local var_60_0 = {}

	for iter_60_0, iter_60_1 in pairs(arg_60_0.itemData):
		table.insert(var_60_0, iter_60_1)

	return var_60_0

def var_0_0.AddItem(arg_61_0, arg_61_1, arg_61_2):
	if arg_61_0.itemData[arg_61_1]:
		arg_61_0.itemData[arg_61_1].AddCount(arg_61_2)
	else
		arg_61_0.itemData[arg_61_1] = EducateItem.New({
			id = arg_61_1,
			num = arg_61_2
		})

	arg_61_0.sendNotification(var_0_0.ITEM_ADDED)

def var_0_0.GetItemCntById(arg_62_0, arg_62_1):
	return arg_62_0.itemData[arg_62_1] and arg_62_0.itemData[arg_62_1].count or 0

def var_0_0.GetPolaroidData(arg_63_0):
	return arg_63_0.polaroidData

def var_0_0.GetPolaroidList(arg_64_0):
	local var_64_0 = {}

	for iter_64_0, iter_64_1 in pairs(arg_64_0.polaroidData):
		table.insert(var_64_0, iter_64_1)

	return var_64_0

def var_0_0.GetPolaroidIdList(arg_65_0):
	local var_65_0 = {}

	for iter_65_0, iter_65_1 in pairs(arg_65_0.polaroidData):
		table.insert(var_65_0, iter_65_0)

	return var_65_0

def var_0_0.AddPolaroid(arg_66_0, arg_66_1):
	if arg_66_0.polaroidData[arg_66_1]:
		return

	arg_66_0.polaroidData[arg_66_1] = EducatePolaroid.New({
		id = arg_66_1,
		time = arg_66_0.GetCurTime()
	})

	EducateTipHelper.SetNewTip(EducateTipHelper.NEW_POLAROID)

	local var_66_0 = Clone(arg_66_0.GetSecretaryIDs())

	arg_66_0.updateSecretaryIDs()
	getProxy(SettingsProxy).UpdateEducateCharTip(var_66_0)
	arg_66_0.sendNotification(var_0_0.POLAROID_ADDED)

def var_0_0.IsExistPolaroidByGroup(arg_67_0, arg_67_1):
	local var_67_0 = pg.child_polaroid.get_id_list_by_group[arg_67_1]

	return underscore.any(var_67_0, function(arg_68_0)
		return arg_67_0.polaroidData[arg_68_0])

def var_0_0.CanGetPolaroidByGroup(arg_69_0, arg_69_1):
	local var_69_0 = pg.child_polaroid.get_id_list_by_group[arg_69_1]

	return underscore.any(var_69_0, function(arg_70_0)
		return arg_69_0.CanGetPolaroidById(arg_70_0))

def var_0_0.CanGetPolaroidById(arg_71_0, arg_71_1):
	local var_71_0 = arg_71_0.char.GetStage()
	local var_71_1 = arg_71_0.GetPersonalityId()
	local var_71_2 = pg.child_polaroid[arg_71_1]

	if table.contains(var_71_2.stage, var_71_0):
		if var_71_2.xingge == "":
			return True

		return table.contains(var_71_2.xingge, var_71_1)

	return False

def var_0_0.GetPolaroidGroupCnt(arg_72_0):
	local var_72_0 = 0
	local var_72_1 = 0

	for iter_72_0, iter_72_1 in pairs(pg.child_polaroid.get_id_list_by_group):
		if arg_72_0.IsExistPolaroidByGroup(iter_72_0):
			var_72_0 = var_72_0 + 1

		var_72_1 = var_72_1 + 1

	return var_72_0, var_72_1

def var_0_0.GetMemories(arg_73_0):
	return arg_73_0.memories

def var_0_0.AddMemory(arg_74_0, arg_74_1):
	if table.contains(arg_74_0.memories, arg_74_1):
		return

	table.insert(arg_74_0.memories, arg_74_1)
	EducateTipHelper.SetNewTip(EducateTipHelper.NEW_MEMORY, arg_74_1)
	arg_74_0.sendNotification(var_0_0.MEMORY_ADDED)

def var_0_0.CheckGuide(arg_75_0, arg_75_1):
	arg_75_0.sendNotification(var_0_0.GUIDE_CHECK, {
		view = arg_75_1
	})

def var_0_0.MainAddLayer(arg_76_0, arg_76_1):
	arg_76_0.sendNotification(var_0_0.MAIN_SCENE_ADD_LAYER, arg_76_1)

def var_0_0.initUnlockSecretary(arg_77_0, arg_77_1):
	arg_77_0.isUnlockSecretary = arg_77_1
	arg_77_0.unlockSecretaryTaskId = (function()
		for iter_78_0, iter_78_1 in ipairs(pg.secretary_special_ship.all):
			if pg.secretary_special_ship[iter_78_1].unlock_type == EducateConst.SECRETARY_UNLCOK_TYPE_DEFAULT:
				return pg.secretary_special_ship[iter_78_1].unlock[1])()
	arg_77_0.unlcokTipByPolaroidCnt = {}

	for iter_77_0, iter_77_1 in ipairs(pg.secretary_special_ship.all):
		local var_77_0 = pg.secretary_special_ship[iter_77_1]

		if var_77_0.unlock_type == EducateConst.SECRETARY_UNLCOK_TYPE_POLAROID:
			local var_77_1 = var_77_0.unlock[1]

			if not table.contains(arg_77_0.unlcokTipByPolaroidCnt, var_77_1):
				table.insert(arg_77_0.unlcokTipByPolaroidCnt, var_77_1)

def var_0_0.GetUnlockSecretaryTaskId(arg_79_0):
	return arg_79_0.unlockSecretaryTaskId

def var_0_0.SetSecretaryUnlock(arg_80_0):
	arg_80_0.isUnlockSecretary = True

	arg_80_0.updateSecretaryIDs()

def var_0_0.CheckNewSecretaryTip(arg_81_0):
	local var_81_0 = arg_81_0.GetPolaroidGroupCnt()

	if table.contains(arg_81_0.unlcokTipByPolaroidCnt, var_81_0):
		arg_81_0.updateSecretaryIDs()
		arg_81_0.sendNotification(var_0_0.UNLCOK_NEW_SECRETARY_BY_CNT)

		return True

	return False

def var_0_0.checkSecretaryID(arg_82_0, arg_82_1, arg_82_2):
	if arg_82_2 == "or":
		for iter_82_0, iter_82_1 in ipairs(arg_82_1):
			if table.contains(arg_82_0.endings, iter_82_1[1]):
				return True

		return False
	elif arg_82_2 == "and":
		for iter_82_2, iter_82_3 in ipairs(arg_82_1):
			if not table.contains(arg_82_0.endings, iter_82_3):
				return False

			return True

	return False

def var_0_0.updateSecretaryIDs(arg_83_0):
	if not arg_83_0.IsUnlockSecretary():
		arg_83_0.unlockSecretaryIds = {}

		return

	arg_83_0.unlockSecretaryIds = {}

	local var_83_0 = #arg_83_0.GetPolaroidIdList()

	for iter_83_0, iter_83_1 in ipairs(pg.secretary_special_ship.all):
		local var_83_1 = pg.secretary_special_ship[iter_83_1].unlock_type
		local var_83_2 = pg.secretary_special_ship[iter_83_1].unlock

		switch(var_83_1, {
			[EducateConst.SECRETARY_UNLCOK_TYPE_DEFAULT] = function()
				if arg_83_0.IsUnlockSecretary():
					table.insert(arg_83_0.unlockSecretaryIds, iter_83_1),
			[EducateConst.SECRETARY_UNLCOK_TYPE_POLAROID] = function()
				if var_83_2[1] and var_83_0 >= var_83_2[1]:
					table.insert(arg_83_0.unlockSecretaryIds, iter_83_1),
			[EducateConst.SECRETARY_UNLCOK_TYPE_ENDING] = function()
				if var_83_2[1]:
					if type(var_83_2[1]) == "table":
						if arg_83_0.checkSecretaryID(var_83_2, "or"):
							table.insert(arg_83_0.unlockSecretaryIds, iter_83_1)
					elif type(var_83_2[1]) == "number" and arg_83_0.checkSecretaryID(var_83_2, "and"):
						table.insert(arg_83_0.unlockSecretaryIds, iter_83_1)
		})

def var_0_0.GetEducateGroupList(arg_87_0):
	local var_87_0 = {}

	for iter_87_0, iter_87_1 in pairs(pg.secretary_special_ship.get_id_list_by_group):
		table.insert(var_87_0, EducateCharGroup.New(iter_87_0))

	return var_87_0

def var_0_0.GetStoryInfo(arg_88_0):
	return arg_88_0.char.GetPaintingName(), arg_88_0.char.GetCallName(), arg_88_0.char.GetBGName()

def var_0_0.GetSecretaryIDs(arg_89_0):
	return arg_89_0.unlockSecretaryIds

def var_0_0.GetPolaroidCnt(arg_90_0):
	return #arg_90_0.GetPolaroidIdList()

def var_0_0.IsUnlockSecretary(arg_91_0):
	return arg_91_0.isUnlockSecretary

def var_0_0.remove(arg_92_0):
	return

return var_0_0
