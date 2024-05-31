local var_0_0 = class("TaskCommonPage", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "TaskListPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0._scrllPanel = arg_2_0.findTF("right_panel")
	arg_2_0._scrollView = arg_2_0._scrllPanel.GetComponent("LScrollRect")

def var_0_0.OnInit(arg_3_0):
	arg_3_0.taskCards = {}

	function arg_3_0._scrollView.onInitItem(arg_4_0)
		arg_3_0.onInitTask(arg_4_0)

	function arg_3_0._scrollView.onUpdateItem(arg_5_0, arg_5_1)
		arg_3_0.onUpdateTask(arg_5_0, arg_5_1)

def var_0_0.onInitTask(arg_6_0, arg_6_1):
	local var_6_0 = TaskCard.New(arg_6_1, arg_6_0.contextData.viewComponent)

	arg_6_0.taskCards[arg_6_1] = var_6_0

def var_0_0.onUpdateTask(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = arg_7_0.taskCards[arg_7_2]

	if not var_7_0:
		arg_7_0.onInitTask(arg_7_2)

		var_7_0 = arg_7_0.taskCards[arg_7_2]

	local var_7_1 = arg_7_0.taskVOs[arg_7_1 + 1]

	var_7_0.update(var_7_1)

def var_0_0.Update(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	arg_8_0.Show()

	arg_8_0.taskVOs = {}

	local var_8_0 = arg_8_0.contextData.taskVOsById

	for iter_8_0, iter_8_1 in pairs(var_8_0):
		if iter_8_1.ShowOnTaskScene() and arg_8_2[iter_8_1.GetRealType()]:
			table.insert(arg_8_0.taskVOs, iter_8_1)

	if (arg_8_1 == TaskScene.PAGE_TYPE_ALL or arg_8_1 == TaskScene.PAGE_TYPE_ROUTINE) and TaskScene.IsPassScenario() and TaskScene.IsNewStyleTime():
		local var_8_1 = pg.gameset.daily_task_new.description
		local var_8_2 = getProxy(TaskProxy)

		for iter_8_2, iter_8_3 in ipairs(var_8_1):
			if not (var_8_2.getTaskById(iter_8_3) or var_8_2.getFinishTaskById(iter_8_3)):
				table.insert(arg_8_0.taskVOs, Task.New({
					progress = 0,
					id = iter_8_3
				}))

	if arg_8_1 == TaskScene.PAGE_TYPE_ALL or arg_8_1 == TaskScene.PAGE_TYPE_ACT:
		local var_8_3 = getProxy(AvatarFrameProxy).getAllAvatarFrame()

		for iter_8_4, iter_8_5 in ipairs(var_8_3):
			local var_8_4 = iter_8_5.tasks

			for iter_8_6, iter_8_7 in ipairs(var_8_4):
				table.insert(arg_8_0.taskVOs, iter_8_7)

	arg_8_0.Sort()
	arg_8_0._scrollView.SetTotalCount(#arg_8_0.taskVOs, -1)

	local var_8_5 = arg_8_0.GetSliderValue()

	if var_8_5 > 0:
		arg_8_0._scrollView.ScrollTo(var_8_5)

	if arg_8_3:
		arg_8_3(arg_8_0.taskVOs)

def var_0_0.GetSliderValue(arg_9_0):
	local var_9_0 = -1

	if arg_9_0.contextData.targetId:
		local var_9_1

		for iter_9_0, iter_9_1 in ipairs(arg_9_0.taskVOs):
			if iter_9_1.id == arg_9_0.contextData.targetId:
				var_9_1 = iter_9_0 - 1

				break

		if var_9_1:
			var_9_0 = arg_9_0._scrollView.HeadIndexToValue(var_9_1)

	return var_9_0

def var_0_0.Sort(arg_10_0):
	local function var_10_0(arg_11_0, arg_11_1, arg_11_2)
		local function var_11_0(arg_12_0)
			for iter_12_0, iter_12_1 in ipairs(arg_11_2):
				if arg_12_0 == iter_12_1:
					return iter_12_0

		return var_11_0(arg_11_0) < var_11_0(arg_11_1)

	local function var_10_1(arg_13_0)
		return arg_13_0.IsUrTask() and 1 or 0

	local function var_10_2(arg_14_0)
		return arg_14_0.configId or 0

	local function var_10_3(arg_15_0, arg_15_1)
		if arg_15_0.GetRealType() == arg_15_1.GetRealType():
			if arg_15_0.isAvatarTask() and arg_15_1.isAvatarTask():
				local var_15_0 = var_10_2(arg_15_0)
				local var_15_1 = var_10_2(arg_15_1)

				if var_15_0 == var_15_1:
					return arg_15_0.id < arg_15_1.id
				else
					return var_15_1 < var_15_0
			else
				return arg_15_0.id < arg_15_1.id
		elif arg_15_0.getTaskStatus() == 0:
			return var_10_0(arg_15_0.GetRealType(), arg_15_1.GetRealType(), {
				26,
				36,
				6,
				3,
				4,
				13,
				5,
				2,
				1
			})
		elif arg_15_0.getTaskStatus() == 1:
			return var_10_0(arg_15_0.GetRealType(), arg_15_1.GetRealType(), {
				26,
				36,
				6,
				1,
				4,
				13,
				2,
				5,
				3
			})

	table.sort(arg_10_0.taskVOs, function(arg_16_0, arg_16_1)
		if arg_16_0.getTaskStatus() == arg_16_1.getTaskStatus():
			local var_16_0 = arg_16_0.id == 10302 and 1 or 0
			local var_16_1 = arg_16_1.id == 10302 and 1 or 0

			if var_16_0 == var_16_1:
				local var_16_2 = var_10_1(arg_16_0)
				local var_16_3 = var_10_1(arg_16_1)

				if var_16_2 == var_16_3:
					return var_10_3(arg_16_0, arg_16_1)
				else
					return var_16_3 < var_16_2
			else
				return var_16_1 < var_16_0
		else
			return var_10_0(arg_16_0.getTaskStatus(), arg_16_1.getTaskStatus(), {
				1,
				0,
				2,
				-1
			}))

def var_0_0.OnDestroy(arg_17_0):
	for iter_17_0, iter_17_1 in pairs(arg_17_0.taskCards):
		iter_17_1.dispose()

def var_0_0.GetWaitToCheckList(arg_18_0):
	local var_18_0 = arg_18_0.taskVOs or {}
	local var_18_1 = {}

	for iter_18_0, iter_18_1 in pairs(var_18_0):
		if iter_18_1.getTaskStatus() == 1 and iter_18_1.ShowOnTaskScene():
			table.insert(var_18_1, iter_18_1)

	return var_18_1

def var_0_0.ExecuteOneStepSubmit(arg_19_0):
	local var_19_0 = arg_19_0.GetWaitToCheckList()
	local var_19_1
	local var_19_2 = False
	local var_19_3

	local function var_19_4()
		var_19_1, var_19_2 = arg_19_0.filterOverflowTaskVOList(var_19_0)
		var_19_1 = arg_19_0.filterSubmitTaskVOList(var_19_1, var_19_3)
		var_19_1 = arg_19_0.filterChoiceTaskVOList(var_19_1, var_19_3)

		local var_20_0 = {}

		for iter_20_0 = #var_19_1, 1, -1:
			local var_20_1 = var_19_1[iter_20_0]

			if var_20_1.isAvatarTask():
				if not var_20_0[var_20_1.actId]:
					var_20_0[var_20_1.actId] = {}

				table.insert(var_20_0[var_20_1.actId], var_20_1.id)
				table.remove(var_19_1, iter_20_0)

		for iter_20_1, iter_20_2 in pairs(var_20_0):
			if #iter_20_2 > 0:
				pg.m02.sendNotification(GAME.AVATAR_FRAME_AWARD, {
					act_id = iter_20_1,
					task_ids = iter_20_2,
					def callback:()
						var_19_3()
				})
				coroutine.yield()

		if #var_19_1 > 0:
			pg.m02.sendNotification(GAME.MERGE_TASK_ONE_STEP_AWARD, {
				resultList = var_19_1
			})

	var_19_3 = coroutine.wrap(var_19_4)

	var_19_3()

	if var_19_2:
		pg.TipsMgr.GetInstance().ShowTips(i18n("award_overflow_tip"))

		var_19_2 = False

def var_0_0.filterOverflowTaskVOList(arg_22_0, arg_22_1):
	local var_22_0 = {}
	local var_22_1 = getProxy(PlayerProxy).getData()
	local var_22_2 = pg.gameset.urpt_chapter_max.description[1]
	local var_22_3 = var_22_1.gold
	local var_22_4 = var_22_1.oil
	local var_22_5 = not LOCK_UR_SHIP and getProxy(BagProxy).GetLimitCntById(var_22_2) or 0
	local var_22_6 = pg.gameset.max_gold.key_value
	local var_22_7 = pg.gameset.max_oil.key_value

	if LOCK_UR_SHIP or not pg.gameset.urpt_chapter_max.description[2]:
		local var_22_8 = 0

	local var_22_9 = False

	for iter_22_0, iter_22_1 in pairs(arg_22_1):
		local var_22_10 = iter_22_1.judgeOverflow(var_22_3, var_22_4, var_22_5)

		if not var_22_10:
			table.insert(var_22_0, iter_22_1)

		if var_22_10:
			var_22_9 = True

	return var_22_0, var_22_9

def var_0_0.filterSubmitTaskVOList(arg_23_0, arg_23_1, arg_23_2):
	local var_23_0 = {}
	local var_23_1 = arg_23_1

	for iter_23_0, iter_23_1 in ipairs(var_23_1):
		if iter_23_1.getConfig("sub_type") == TASK_SUB_TYPE_GIVE_ITEM or iter_23_1.getConfig("sub_type") == TASK_SUB_TYPE_GIVE_VIRTUAL_ITEM or iter_23_1.getConfig("sub_type") == TASK_SUB_TYPE_PLAYER_RES:
			local var_23_2 = DROP_TYPE_ITEM

			if iter_23_1.getConfig("sub_type") == TASK_SUB_TYPE_PLAYER_RES:
				var_23_2 = DROP_TYPE_RESOURCE

			local var_23_3 = {
				type = var_23_2,
				id = tonumber(iter_23_1.getConfig("target_id")),
				count = iter_23_1.getConfig("target_num")
			}

			local function var_23_4()
				table.insert(var_23_0, iter_23_1)
				arg_23_2()

			local function var_23_5()
				arg_23_2()

			local var_23_6 = {
				type = MSGBOX_TYPE_ITEM_BOX,
				content = i18n("sub_item_warning"),
				items = {
					var_23_3
				},
				onYes = var_23_4,
				onNo = var_23_5
			}

			pg.MsgboxMgr.GetInstance().ShowMsgBox(var_23_6)
			coroutine.yield()
		else
			table.insert(var_23_0, iter_23_1)

	return var_23_0

def var_0_0.filterChoiceTaskVOList(arg_26_0, arg_26_1, arg_26_2):
	local var_26_0 = {}
	local var_26_1 = arg_26_1

	for iter_26_0, iter_26_1 in ipairs(var_26_1):
		if iter_26_1.isSelectable():
			local var_26_2 = iter_26_1.getConfig("award_choice")
			local var_26_3 = {}

			for iter_26_2, iter_26_3 in ipairs(var_26_2):
				var_26_3[#var_26_3 + 1] = {
					type = iter_26_3[1],
					id = iter_26_3[2],
					count = iter_26_3[3],
					index = iter_26_2
				}

			local var_26_4

			local function var_26_5(arg_27_0)
				var_26_4 = arg_27_0.index

			local function var_26_6()
				if not var_26_4:
					pg.TipsMgr.GetInstance().ShowTips(i18n("no_item_selected_tip"))
				else
					local var_28_0 = {}
					local var_28_1 = var_26_2[var_26_4]

					for iter_28_0, iter_28_1 in ipairs(var_28_1):
						table.insert(var_28_0, {
							type = iter_28_1[1],
							id = iter_28_1[2],
							number = iter_28_1[3]
						})

					iter_26_1.choiceItemList = var_28_0

					table.insert(var_26_0, iter_26_1)
					arg_26_2()

			local function var_26_7()
				arg_26_2()

			local var_26_8 = {
				type = MSGBOX_TYPE_ITEM_BOX,
				content = i18n("select_award_warning"),
				items = var_26_3,
				itemFunc = var_26_5,
				onYes = var_26_6,
				onNo = var_26_7
			}

			pg.MsgboxMgr.GetInstance().ShowMsgBox(var_26_8)
			coroutine.yield()
		else
			table.insert(var_26_0, iter_26_1)

	return var_26_0

return var_0_0
