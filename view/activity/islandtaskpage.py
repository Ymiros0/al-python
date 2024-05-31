local var_0_0 = class("IslandTaskPage")
local var_0_1 = {
	5,
	6,
	7,
	8
}
local var_0_2 = 4

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	arg_1_0.taskPage = arg_1_1
	arg_1_0.contextData = arg_1_2
	arg_1_0.taskItemTpl = findTF(arg_1_3, "taskItemTpl")

	setActive(arg_1_0.taskItemTpl, False)

	arg_1_0.IconTpl = findTF(arg_1_3, "IconTpl")

	setActive(arg_1_0.IconTpl, False)

	arg_1_0._event = arg_1_4
	arg_1_0.enterTaskId = None
	arg_1_0.enterTaskIds = None

	if arg_1_0.contextData.task_id:
		arg_1_0.enterTaskId = arg_1_0.contextData.task_id or None
	elif arg_1_0.contextData.task_ids:
		arg_1_0.enterTaskIds = arg_1_0.contextData.task_ids or None

	arg_1_0.activityId = ActivityConst.ISLAND_TASK_ID
	arg_1_0.hideTask = pg.activity_template[arg_1_0.activityId].config_client.hide_task or {}
	arg_1_0.leanTweens = {}
	arg_1_0.exitFlag = False
	arg_1_0.btnGetAll = findTF(arg_1_0.taskPage, "btnGetAll")
	arg_1_0.taskTagPanel = findTF(arg_1_0.taskPage, "taskTagPanel")
	arg_1_0.taskListPanel = findTF(arg_1_0.taskPage, "taskListPanel")
	arg_1_0.scrollRect = findTF(arg_1_0.taskPage, "taskListPanel/Content").GetComponent("LScrollRect")
	arg_1_0.taskDetailPanel = findTF(arg_1_0.taskPage, "taskDetailPanel")
	arg_1_0.detailTag = findTF(arg_1_0.taskDetailPanel, "tag")
	arg_1_0.detailTitleText = findTF(arg_1_0.taskDetailPanel, "title/text")
	arg_1_0.detailIcon = findTF(arg_1_0.taskDetailPanel, "icon/image")
	arg_1_0.detailDescText = findTF(arg_1_0.taskDetailPanel, "desc/text")
	arg_1_0.detaiProgressText = findTF(arg_1_0.taskDetailPanel, "progress/text")
	arg_1_0.detailAwardContent = findTF(arg_1_0.taskDetailPanel, "awardDisplay/viewport/content")
	arg_1_0.detailBtnGo = findTF(arg_1_0.taskDetailPanel, "btnGo")
	arg_1_0.detailBtnGet = findTF(arg_1_0.taskDetailPanel, "btnGet")
	arg_1_0.detailBtnSubmit = findTF(arg_1_0.taskDetailPanel, "btnSubmit")
	arg_1_0.detailBtnDetail = findTF(arg_1_0.taskDetailPanel, "btnDetail")
	arg_1_0.detailActive = findTF(arg_1_0.taskDetailPanel, "active")

	for iter_1_0 = 1, var_0_2:
		local var_1_0 = findTF(arg_1_0.taskTagPanel, "btn" .. iter_1_0)

		if iter_1_0 <= #var_0_1:
			local var_1_1 = var_0_1[iter_1_0]

			setText(findTF(var_1_0, "off/text"), i18n(IslandTaskScene.add_tages[var_1_1]))
			setText(findTF(var_1_0, "on/text"), i18n(IslandTaskScene.add_tages[var_1_1]))
		else
			setActive(var_1_0, False)

	setText(findTF(arg_1_0.taskDetailPanel, "desc/title"), i18n(IslandTaskScene.ryza_task_detail_content))
	setText(findTF(arg_1_0.taskDetailPanel, "awardText/txt"), i18n(IslandTaskScene.ryza_task_detail_award))

	arg_1_0.btnTags = {}

	for iter_1_1 = 1, var_0_2:
		local var_1_2 = iter_1_1
		local var_1_3 = var_0_1[iter_1_1]
		local var_1_4 = findTF(arg_1_0.taskTagPanel, "btn" .. var_1_2)

		onButton(arg_1_0._event, var_1_4, function()
			if arg_1_0.clickIndex:
				setActive(findTF(arg_1_0.btnTags[arg_1_0.clickIndex], "on"), False)

				if arg_1_0.clickIndex == var_1_2:
					arg_1_0.clickIndex = None
				else
					arg_1_0.clickIndex = var_1_2

					setActive(findTF(arg_1_0.btnTags[arg_1_0.clickIndex], "on"), True)
			else
				arg_1_0.clickIndex = var_1_2

				setActive(findTF(arg_1_0.btnTags[arg_1_0.clickIndex], "on"), True)

			arg_1_0.tagId = arg_1_0.clickIndex and var_0_1[arg_1_0.clickIndex] or None

			arg_1_0.onClickTag(var_1_2))
		table.insert(arg_1_0.btnTags, var_1_4)

	function arg_1_0.scrollRect.onUpdateItem(arg_3_0, arg_3_1)
		arg_1_0.onUpdateTaskItem(arg_3_0, arg_3_1)

	arg_1_0.iconTfs = {}
	arg_1_0.awards = {}

	onButton(arg_1_0._event, arg_1_0.btnGetAll, function()
		local var_4_0 = arg_1_0.getAllTasks

		arg_1_0._event.emit(IslandTaskMediator.SUBMIT_TASK_ALL, {
			activityId = arg_1_0.activityId,
			ids = var_4_0
		}), SOUND_BACK)
	onButton(arg_1_0._event, arg_1_0.detailBtnGo, function()
		local var_5_0 = Task.New(arg_1_0.selectTask)

		arg_1_0._event.emit(IslandTaskMediator.TASK_GO, {
			taskVO = var_5_0
		}), SOUND_BACK)
	onButton(arg_1_0._event, arg_1_0.detailBtnSubmit, function()
		local var_6_0 = arg_1_0.selectTask.getConfig("type")

		if arg_1_0.selectTask.getConfig("sub_type") == 1006:
			arg_1_0._event.emit(IslandTaskScene.OPEN_SUBMIT, arg_1_0.selectTask)
		else
			arg_1_0._event.emit(IslandTaskMediator.SUBMIT_TASK, {
				activityId = arg_1_0.activityId,
				id = arg_1_0.selectTask.id
			}), SOUND_BACK)
	onButton(arg_1_0._event, arg_1_0.detailBtnGet, function()
		local var_7_0 = arg_1_0.selectTask.getConfig("type")

		if arg_1_0.selectTask.getConfig("sub_type") == 1006:
			arg_1_0._event.emit(IslandTaskScene.OPEN_SUBMIT, arg_1_0.selectTask)
		else
			arg_1_0._event.emit(IslandTaskMediator.SUBMIT_TASK, {
				activityId = arg_1_0.activityId,
				id = arg_1_0.selectTask.id
			}), SOUND_BACK)
	onButton(arg_1_0._event, arg_1_0.detailBtnDetail, function()
		if arg_1_0.selectTask:
			local var_8_0 = tonumber(arg_1_0.selectTask.getConfig("target_id_2"))

			if var_8_0 and var_8_0 > 0:
				local var_8_1 = AtelierMaterial.New({
					configId = var_8_0,
					count = arg_1_0.selectTask.getConfig("target_num")
				})

				arg_1_0._event.emit(IslandTaskMediator.SHOW_DETAIL, var_8_1), SOUND_BACK)
	arg_1_0.updateTask()
	arg_1_0.onClickTag()

def var_0_0.onUpdateTaskItem(arg_9_0, arg_9_1, arg_9_2):
	if arg_9_0.exitFlag:
		return

	arg_9_0.leanTweens[arg_9_2] = arg_9_2

	table.insert(arg_9_0.leanTweens, arg_9_2)

	local var_9_0 = GetComponent(arg_9_2, typeof(CanvasGroup))

	var_9_0.alpha = 0

	LeanTween.value(arg_9_2, 0, 1, 0.3).setEase(LeanTweenType.linear).setOnUpdate(System.Action_float(function(arg_10_0)
		var_9_0.alpha = arg_10_0)).setOnComplete(System.Action(function()
		arg_9_0.leanTweens[arg_9_2] = None))

	arg_9_1 = arg_9_1 + 1

	local var_9_1 = arg_9_0.showTasks[arg_9_1]
	local var_9_2 = var_9_1.id
	local var_9_3 = var_9_1.getProgress()
	local var_9_4 = var_9_1.getConfig("name")
	local var_9_5 = var_9_1.getConfig("ryza_icon")
	local var_9_6 = var_9_1.isOver()
	local var_9_7 = var_9_1.isFinish()
	local var_9_8 = var_9_1.isCircle()
	local var_9_9 = var_9_1.isDaily()

	setActive(findTF(arg_9_2, "selected"), arg_9_0.selectIndex == arg_9_1)
	setActive(findTF(arg_9_2, "typeNew"), var_9_1.isNew())
	setActive(findTF(arg_9_2, "typeCircle"), var_9_1.isCircle() or var_9_1.isDaily())
	setActive(findTF(arg_9_2, "finish"), var_9_6)
	setActive(findTF(arg_9_2, "mask"), var_9_6)
	setActive(findTF(arg_9_2, "complete"), not var_9_6 and var_9_7 and not var_9_8)
	setText(findTF(arg_9_2, "desc/text"), setColorStr(shortenString(var_9_4, 10), "#9D6B59"))

	if not var_9_5 or var_9_5 == 0:
		var_9_5 = "attack"

	setImageSprite(findTF(arg_9_2, "icon/image"), LoadSprite(IslandTaskScene.icon_atlas, var_9_5))
	onButton(arg_9_0._event, tf(arg_9_2), function()
		if arg_9_0.selectItem:
			setActive(findTF(arg_9_0.selectItem, "selected"), False)
			setText(findTF(arg_9_0.selectItem, "desc/text"), setColorStr(shortenString(arg_9_0.selectTask.getConfig("name"), 10), "#9D6B59"))

		setActive(findTF(arg_9_2, "selected"), True)
		setText(findTF(arg_9_2, "desc/text"), setColorStr(shortenString(var_9_4, 10), "#5C3E24"))

		arg_9_0.selectIndex = arg_9_1
		arg_9_0.selectItem = arg_9_2
		arg_9_0.selectTask = var_9_1

		arg_9_0.updateDetail())

	if arg_9_1 == 1:
		triggerButton(arg_9_2)

		arg_9_0.scrollIndex = None

	if arg_9_0.enterTaskId != None and arg_9_0.enterTaskId > 0:
		if var_9_2 == arg_9_0.enterTaskId:
			triggerButton(arg_9_2)

			arg_9_0.enterTaskId = None
			arg_9_0.scrollIndex = None
	elif arg_9_0.enterTaskIds and #arg_9_0.enterTaskIds > 0:
		for iter_9_0, iter_9_1 in ipairs(arg_9_0.enterTaskIds):
			if var_9_2 == iter_9_1:
				triggerButton(arg_9_2)

				arg_9_0.enterTaskIds = None
				arg_9_0.scrollIndex = None

def var_0_0.updateTask(arg_13_0, arg_13_1):
	arg_13_0.displayTask = {}
	arg_13_0.allDisplayTask = {}

	local var_13_0 = getProxy(ActivityTaskProxy).getTaskById(arg_13_0.activityId)

	arg_13_0.getAllTasks = {}

	for iter_13_0 = 1, #var_13_0:
		local var_13_1 = var_13_0[iter_13_0]
		local var_13_2 = var_13_1.id

		if not table.contains(arg_13_0.hideTask, var_13_2):
			local var_13_3 = var_13_1.getProgress()
			local var_13_4 = var_13_1.getTarget()
			local var_13_5 = var_13_1.getConfig("ryza_type")

			if not var_13_5 or var_13_5 <= 0:
				var_13_5 = 999

			local var_13_6 = var_13_1.getConfig("type")
			local var_13_7 = var_13_1.getConfig("sub_type")

			if var_13_5 > 0:
				if not arg_13_0.displayTask[var_13_5]:
					arg_13_0.displayTask[var_13_5] = {}

				table.insert(arg_13_0.displayTask[var_13_5], var_13_1)
				table.insert(arg_13_0.allDisplayTask, var_13_1)

				if not var_13_1.isFinish() or var_13_1.isOver() or var_13_7 == 1006:
					-- block empty
				else
					table.insert(arg_13_0.getAllTasks, var_13_2)

	local var_13_8 = getProxy(ActivityProxy).getActivityById(arg_13_0.activityId)
	local var_13_9 = {}

	if var_13_8:
		var_13_9 = var_13_8.data1_list

	if var_13_9 and #var_13_9 > 0:
		for iter_13_1 = 1, #var_13_9:
			local var_13_10 = var_13_9[iter_13_1]
			local var_13_11 = ActivityTask.New(arg_13_0.activityId, {
				progress = 0,
				id = var_13_10
			})

			var_13_11.setOver()

			local var_13_12 = var_13_11.getConfig("ryza_type")

			if var_13_12 > 0:
				if not arg_13_0.displayTask[var_13_12]:
					arg_13_0.displayTask[var_13_12] = {}

				table.insert(arg_13_0.displayTask[var_13_12], var_13_11)
				table.insert(arg_13_0.allDisplayTask, var_13_11)

	local function var_13_13(arg_14_0, arg_14_1)
		if arg_14_0.isOver() and not arg_14_1.isOver():
			return False
		elif not arg_14_0.isOver() and arg_14_1.isOver():
			return True

		if arg_14_0.isFinish() and not arg_14_1.isFinish():
			return True
		elif not arg_14_0.isFinish() and arg_14_1.isFinish():
			return False

		if arg_14_0.isNew() and not arg_14_1.isNew():
			return True
		elif not arg_14_0.isNew() and arg_14_1.isNew():
			return False

		if arg_14_0.id > arg_14_1.id:
			return False
		elif arg_14_0.id < arg_14_1.id:
			return True

	for iter_13_2, iter_13_3 in pairs(arg_13_0.displayTask):
		table.sort(iter_13_3, var_13_13)

	table.sort(arg_13_0.allDisplayTask, var_13_13)

	if arg_13_1:
		arg_13_0.onClickTag()

	if #arg_13_0.getAllTasks > 0:
		setActive(arg_13_0.btnGetAll, True)
	else
		setActive(arg_13_0.btnGetAll, False)

def var_0_0.updateDetail(arg_15_0):
	local var_15_0 = arg_15_0.showTasks[arg_15_0.selectIndex]
	local var_15_1 = var_15_0.id
	local var_15_2 = var_15_0.getProgress()
	local var_15_3 = var_15_0.target
	local var_15_4 = pg.task_data_template[var_15_1]
	local var_15_5 = var_15_0.isFinish()
	local var_15_6 = var_15_0.isOver()
	local var_15_7 = var_15_0.isCircle()
	local var_15_8 = var_15_0.isSubmit()

	arg_15_0.awards = var_15_4.award_display

	local var_15_9 = var_15_4.desc
	local var_15_10 = var_15_4.ryza_icon
	local var_15_11 = var_15_0.getConfig("sub_type")

	if not var_15_10 or var_15_10 == 0:
		var_15_10 = "attack"

	if not var_15_8 and var_15_3 < var_15_2:
		var_15_2 = var_15_3

	setText(arg_15_0.detailDescText, var_15_9)

	if not var_15_6:
		setText(arg_15_0.detaiProgressText, setColorStr(var_15_2, "#C2695B") .. " / " .. setColorStr(var_15_3, "#9D6B59"))
	else
		setText(arg_15_0.detaiProgressText, "--/--")

	setText(arg_15_0.detailTitleText, shortenString(var_15_4.name, 11))
	setActive(arg_15_0.detailBtnDetail, var_15_11 == 1006 and not var_15_5 and not var_15_6)
	setActive(arg_15_0.detailBtnGo, not var_15_6 and not var_15_5 and var_15_11 != 1006)
	setActive(arg_15_0.detailBtnGet, not var_15_6 and var_15_5 and not var_15_8)
	setActive(arg_15_0.detailBtnSubmit, not var_15_6 and var_15_5 and var_15_8)
	setActive(arg_15_0.detailActive, not var_15_6 and not var_15_5 and not var_15_7)
	setImageSprite(arg_15_0.detailIcon, LoadSprite(IslandTaskScene.icon_atlas, var_15_10))

	if #arg_15_0.iconTfs < #arg_15_0.awards:
		local var_15_12 = #arg_15_0.awards - #arg_15_0.iconTfs

		for iter_15_0 = 1, var_15_12:
			local var_15_13 = tf(Instantiate(arg_15_0.IconTpl))

			setParent(var_15_13, arg_15_0.detailAwardContent)
			setActive(var_15_13, True)
			table.insert(arg_15_0.iconTfs, var_15_13)

	for iter_15_1 = 1, #arg_15_0.iconTfs:
		if iter_15_1 <= #arg_15_0.awards:
			local var_15_14 = arg_15_0.awards[iter_15_1]
			local var_15_15 = {
				type = var_15_14[1],
				id = var_15_14[2],
				count = var_15_14[3]
			}

			updateDrop(arg_15_0.iconTfs[iter_15_1], var_15_15)
			onButton(arg_15_0._event, arg_15_0.iconTfs[iter_15_1], function()
				arg_15_0._event.emit(BaseUI.ON_DROP, var_15_15), SFX_PANEL)
			setActive(arg_15_0.iconTfs[iter_15_1], True)
		else
			setActive(arg_15_0.iconTfs[iter_15_1], False)

def var_0_0.onClickTag(arg_17_0, arg_17_1):
	if arg_17_0.tagId and arg_17_0.tagId > 0:
		if arg_17_0.displayTask[arg_17_0.tagId] and #arg_17_0.displayTask[arg_17_0.tagId] > 0:
			arg_17_0.showTasks = arg_17_0.displayTask[arg_17_0.tagId]
		else
			triggerButton(arg_17_0.btnTags[arg_17_1])

			return
	else
		arg_17_0.showTasks = arg_17_0.allDisplayTask

	if arg_17_0.enterTaskId and arg_17_0.enterTaskId > 0:
		for iter_17_0 = 1, #arg_17_0.showTasks:
			if arg_17_0.showTasks[iter_17_0].id == arg_17_0.enterTaskId:
				arg_17_0.scrollIndex = iter_17_0

	arg_17_0.scrollRect.SetTotalCount(#arg_17_0.showTasks, 0)

	if arg_17_0.scrollIndex != None:
		local var_17_0 = arg_17_0.scrollRect.HeadIndexToValue(arg_17_0.scrollIndex - 1)

		arg_17_0.scrollRect.ScrollTo(var_17_0)

def var_0_0.setActive(arg_18_0, arg_18_1):
	setActive(arg_18_0.taskPage, arg_18_1)

def var_0_0.dispose(arg_19_0):
	arg_19_0.exitFlag = True

	if arg_19_0.leanTweens and #arg_19_0.leanTweens > 0:
		for iter_19_0, iter_19_1 in pairs(arg_19_0.leanTweens):
			if LeanTween.isTweening(iter_19_1):
				LeanTween.cancel(iter_19_1)

		arg_19_0.leanTweens = {}

	for iter_19_2 = 1, #arg_19_0.allDisplayTask:
		local var_19_0 = arg_19_0.allDisplayTask[iter_19_2]

		if var_19_0.isNew():
			var_19_0.changeNew()

return var_0_0
