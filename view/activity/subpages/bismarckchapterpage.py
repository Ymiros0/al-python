local var_0_0 = class("BismarckChapterPage", import("...base.BaseActivityPage"))

var_0_0.tabPos = {
	[1] = 10,
	[2] = 182.3
}
var_0_0.IconShowFunc = {
	[DROP_TYPE_SHIP] = function(arg_1_0, arg_1_1)
		local var_1_0 = pg.ship_data_statistics[arg_1_1].skin_id
		local var_1_1 = pg.ship_skin_template[var_1_0].painting

		GetImageSpriteFromAtlasAsync("SquareIcon/" .. var_1_1, "", arg_1_0),
	[DROP_TYPE_FURNITURE] = function(arg_2_0, arg_2_1)
		local var_2_0 = pg.furniture_data_template[arg_2_1]

		GetImageSpriteFromAtlasAsync("furnitureicon/" .. var_2_0.icon, "", arg_2_0)
}
var_0_0.TransformType = {
	[TASK_SUB_TYPE_COLLECT_SHIP] = DROP_TYPE_SHIP,
	[TASK_SUB_TYPE_COLLECT_FURNITURE] = DROP_TYPE_FURNITURE
}

def var_0_0.OnInit(arg_3_0):
	arg_3_0.bg = arg_3_0.findTF("AD")
	arg_3_0.items = {}
	arg_3_0.items[1] = arg_3_0.findTF("AD/Item1")
	arg_3_0.items[2] = arg_3_0.findTF("AD/Item2")
	arg_3_0.awardTF = arg_3_0.findTF("AD/award")
	arg_3_0.battleBtn = arg_3_0.findTF("AD/battle_btn")
	arg_3_0.shopBtn = arg_3_0.findTF("AD/exchange_btn")
	arg_3_0.buildBtn = arg_3_0.findTF("AD/build_btn")
	arg_3_0.tab = arg_3_0.findTF("tab")
	arg_3_0.bar = arg_3_0.findTF("bar")
	arg_3_0.scrollList = arg_3_0.findTF("Scroll View", arg_3_0.tab)
	arg_3_0.content = arg_3_0.findTF("Content", arg_3_0.scrollList)
	arg_3_0.listTmpl = arg_3_0.findTF("listitem", arg_3_0.tab)
	arg_3_0.taskList = UIItemList.New(arg_3_0.content, arg_3_0.listTmpl)
	arg_3_0.finalTasks = {}
	arg_3_0.subtasks = {}
	arg_3_0.tabType = 0

def var_0_0.OnFirstFlush(arg_4_0):
	arg_4_0.finalTasks = Clone(arg_4_0.activity.getConfig("config_client"))

	local var_4_0 = arg_4_0.finalTasks

	_.each(var_4_0, function(arg_5_0)
		local var_5_0 = pg.task_data_template[arg_5_0]
		local var_5_1 = var_5_0 and var_5_0.target_id

		if var_5_1:
			table.insert(arg_4_0.subtasks, Clone(var_5_1)))
	setText(arg_4_0.findTF("desc", arg_4_0.bg), i18n("bismarck_chapter_desc"))
	arg_4_0.SubimtCompletedMission()
	arg_4_0.InitInteractable()

def var_0_0.InitInteractable(arg_6_0):
	local var_6_0 = getProxy(TaskProxy)

	for iter_6_0, iter_6_1 in ipairs(arg_6_0.finalTasks):
		local var_6_1 = pg.task_data_template[iter_6_1]
		local var_6_2 = arg_6_0.items[iter_6_0]

		onButton(arg_6_0, var_6_2, function()
			local var_7_0 = var_6_0.getTaskVO(iter_6_1)

			if var_7_0.getTaskStatus() == 1:
				arg_6_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_7_0)

				return

			if arg_6_0.tabType == iter_6_0:
				return

			arg_6_0.tabType = iter_6_0

			arg_6_0.UpdateTab(), SFX_PANEL)

	onButton(arg_6_0, arg_6_0.battleBtn, function()
		arg_6_0.emit(ActivityMediator.BATTLE_OPERA), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.shopBtn, function()
		local var_9_0 = _.detect(getProxy(ActivityProxy).getActivitiesByType(ActivityConst.ACTIVITY_TYPE_SHOP), function(arg_10_0)
			return arg_10_0.getConfig("config_client").pt_id == pg.gameset.activity_res_id.key_value)

		arg_6_0.emit(ActivityMediator.GO_SHOPS_LAYER, {
			warp = NewShopsScene.TYPE_ACTIVITY,
			actId = var_9_0 and var_9_0.id
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.buildBtn, function()
		arg_6_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
			projectName = BuildShipScene.PROJECTS.ACTIVITY
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.bg, function()
		if arg_6_0.tabType > 0:
			arg_6_0.tabType = 0

			arg_6_0.UpdateTab())

def var_0_0.OnUpdateFlush(arg_13_0):
	arg_13_0.UpdateView()
	arg_13_0.UpdateTab()

def var_0_0.UpdateView(arg_14_0):
	local var_14_0 = getProxy(TaskProxy)

	for iter_14_0 = 1, #arg_14_0.finalTasks:
		local var_14_1 = arg_14_0.finalTasks[iter_14_0]
		local var_14_2 = pg.task_data_template[var_14_1]
		local var_14_3 = arg_14_0.items[iter_14_0]

		setActive(var_14_3, True)

		local var_14_4 = var_14_2.award_display[1]

		arg_14_0.UpdateIcon(arg_14_0.findTF("icon", var_14_3), var_14_4[1], var_14_4[2])

		local var_14_5 = var_14_0.getTaskVO(var_14_1).getTaskStatus()

		setActive(var_14_3.Find("active"), var_14_5 == 0)
		setActive(var_14_3.Find("finished"), var_14_5 == 1)
		setActive(var_14_3.Find("achieved"), var_14_5 == 2)
		setButtonEnabled(var_14_3, var_14_5 < 2)

		arg_14_0.tabType = arg_14_0.tabType == iter_14_0 and var_14_5 == 2 and 0 or arg_14_0.tabType

	for iter_14_1 = #arg_14_0.finalTasks + 1, #arg_14_0.items:
		setActive(arg_14_0.items[iter_14_1], False)

		arg_14_0.tabType = arg_14_0.tabType == iter_14_1 and 0 or arg_14_0.tabType

def var_0_0.UpdateTab(arg_15_0):
	if arg_15_0.tabType == 0:
		setActive(arg_15_0.tab, False)

		return

	local var_15_0 = arg_15_0.subtasks[arg_15_0.tabType]
	local var_15_1 = #var_15_0

	arg_15_0.taskList.align(var_15_1)

	local var_15_2 = getProxy(TaskProxy)
	local var_15_3 = 0

	for iter_15_0 = 1, var_15_1:
		local var_15_4 = arg_15_0.content.GetChild(iter_15_0 - 1)

		setText(arg_15_0.findTF("title/Text", var_15_4), string.format("Task-%02d", iter_15_0))

		local var_15_5 = var_15_0[iter_15_0]
		local var_15_6 = pg.task_data_template[var_15_5]
		local var_15_7 = tonumber(var_15_6.target_id)
		local var_15_8 = var_0_0.TransformType[var_15_6.sub_type]

		setActive(var_15_4.Find("tip2"), var_15_8 == DROP_TYPE_FURNITURE)
		setActive(var_15_4.Find("tip"), var_15_8 == DROP_TYPE_SHIP)

		local var_15_9 = False
		local var_15_10 = var_15_2.getTaskById(var_15_5) or var_15_2.getFinishTaskById(var_15_5)

		setActive(var_15_4.Find("completed"), defaultValue(var_15_10 and var_15_10.isFinish(), False))
		setText(arg_15_0.findTF("text", var_15_4), var_15_6.desc)
		arg_15_0.UpdateIcon(arg_15_0.findTF("icon", var_15_4), var_15_8, var_15_7)

		var_15_3 = var_15_3 + (var_15_10 and var_15_10.isFinish() and 1 or 0)

	setText(arg_15_0.findTF("slider/progress", arg_15_0.tab), string.format("[%d/%d]", var_15_3, var_15_1))

	arg_15_0.scrollList.GetComponent(typeof(ScrollRect)).verticalNormalizedPosition = 1

	local var_15_11 = arg_15_0.tab.transform.anchoredPosition
	local var_15_12 = arg_15_0.tab.sizeDelta

	var_15_11.x = var_0_0.tabPos[arg_15_0.tabType]

	setAnchoredPosition(arg_15_0.tab, var_15_11)

	local var_15_13

	var_15_13.x, var_15_13 = arg_15_0._tf.sizeDelta.x - arg_15_0.bar.anchoredPosition.x - var_15_11.x - var_15_12.x, arg_15_0.bar.sizeDelta
	arg_15_0.bar.sizeDelta = var_15_13

	setActive(arg_15_0.tab, True)

def var_0_0.UpdateIcon(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	if var_0_0.IconShowFunc[arg_16_2]:
		var_0_0.IconShowFunc[arg_16_2](arg_16_1, arg_16_3)

def var_0_0.OnDestroy(arg_17_0):
	return

def var_0_0.SubimtCompletedMission(arg_18_0):
	local var_18_0 = getProxy(TaskProxy)

	for iter_18_0, iter_18_1 in pairs(arg_18_0.subtasks):
		for iter_18_2, iter_18_3 in pairs(iter_18_1):
			local var_18_1 = var_18_0.getTaskById(iter_18_3)

			if var_18_1 and var_18_1.isFinish():
				arg_18_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_18_1)

return var_0_0
