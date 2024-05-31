local var_0_0 = class("IslandHistoryPage")
local var_0_1 = 8
local var_0_2 = {
	{
		-291,
		-6
	},
	{
		-408,
		25
	},
	{
		0,
		0
	},
	{
		-428,
		157
	},
	{
		-341,
		15
	},
	{
		0,
		0
	},
	{
		-414,
		48
	},
	{
		0,
		0
	}
}
local var_0_3 = {
	{
		0,
		0,
		-118
	},
	{
		0,
		0,
		-172
	},
	{
		0,
		0,
		0
	},
	{
		0,
		0,
		-121
	},
	{
		0,
		0,
		-163
	},
	{
		0,
		0,
		0
	},
	{
		0,
		0,
		-256
	},
	{
		0,
		0,
		0
	}
}

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.historyPage = arg_1_1
	arg_1_0.event = arg_1_2
	arg_1_0.activityId = ActivityConst.ISLAND_TASK_ID
	arg_1_0.finishTasks = getProxy(ActivityTaskProxy).getFinishTasksByActId(arg_1_0.activityId)
	arg_1_0.mapDataList = pg.activity_template[arg_1_0.activityId].config_client.map_event_list or {}
	arg_1_0.pageItemContent = findTF(arg_1_0.historyPage, "selectPanel/page")
	arg_1_0.pageItemTpl = findTF(arg_1_0.historyPage, "selectPanel/page/pageItemTpl")

	setActive(arg_1_0.pageItemTpl, False)

	arg_1_0.mapPic = findTF(arg_1_0.historyPage, "pic")
	arg_1_0.mapTitle = findTF(arg_1_0.historyPage, "title/desc")
	arg_1_0.taskDesc = findTF(arg_1_0.historyPage, "taskDesc")

	setText(arg_1_0.taskDesc, i18n(IslandTaskScene.island_history_desc))

	arg_1_0.pageItemTfs = {}

	for iter_1_0 = 1, var_0_1:
		local var_1_0 = iter_1_0
		local var_1_1 = tf(instantiate(arg_1_0.pageItemTpl))

		setParent(var_1_1, arg_1_0.pageItemContent)
		setActive(var_1_1, True)
		onButton(arg_1_0.event, var_1_1, function()
			arg_1_0.selectedPage(var_1_0), SFX_UI_CLICK)
		table.insert(arg_1_0.pageItemTfs, var_1_1)

	arg_1_0.startIndex = 0
	arg_1_0.taskList = {}
	arg_1_0.listConent = findTF(arg_1_0.historyPage, "listPanel/viewcontent/content")
	arg_1_0.taskListTpl = findTF(arg_1_0.historyPage, "listPanel/viewcontent/content/listTpl")

	setActive(arg_1_0.taskListTpl, False)

	arg_1_0.gotTf = findTF(arg_1_0.historyPage, "got")
	arg_1_0.finalAward = findTF(arg_1_0.historyPage, "finalAward")

	arg_1_0.initPageUI()
	arg_1_0.selectedPage(1)

def var_0_0.selectedPage(arg_3_0, arg_3_1):
	if arg_3_0.startIndex + arg_3_1 > #arg_3_0.mapDataList:
		return

	arg_3_0.updatePage(arg_3_1)
	arg_3_0.updateMap(arg_3_1)

def var_0_0.initPageUI(arg_4_0):
	for iter_4_0 = 1, var_0_1:
		local var_4_0 = arg_4_0.startIndex + iter_4_0

		setText(findTF(arg_4_0.pageItemTfs[iter_4_0], "num"), tostring(var_4_0))
		setActive(findTF(arg_4_0.pageItemTfs[iter_4_0], "lock"), var_4_0 > #arg_4_0.mapDataList)
		setActive(arg_4_0.pageItemTfs[iter_4_0], var_4_0 <= #arg_4_0.mapDataList)
		setActive(findTF(arg_4_0.pageItemTfs[iter_4_0], "selected"), False)

		local var_4_1 = setColorStr(var_4_0, "#c57053")

		setText(findTF(arg_4_0.pageItemTfs[iter_4_0], "num"), var_4_1)

def var_0_0.updatePage(arg_5_0, arg_5_1):
	local var_5_0

	if arg_5_0.selectedPageItem:
		setActive(findTF(arg_5_0.selectedPageItem, "selected"), False)

		local var_5_1 = setColorStr(arg_5_0.selectedIndex, "#c57053")

		setText(findTF(arg_5_0.selectedPageItem, "num"), var_5_1)

	arg_5_0.selectedPageItem = arg_5_0.pageItemTfs[arg_5_1]
	arg_5_0.selectedIndex = arg_5_1

	setActive(findTF(arg_5_0.selectedPageItem, "selected"), True)

	local var_5_2 = setColorStr(arg_5_0.selectedIndex, "#84412A")

	setText(findTF(arg_5_0.selectedPageItem, "num"), var_5_2)

def var_0_0.updateMap(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1 + arg_6_0.startIndex

	arg_6_0.showMapId = arg_6_0.mapDataList[var_6_0]

	local var_6_1 = pg.activity_map_event_list[arg_6_0.showMapId]

	arg_6_0.mapIndex = var_6_1.area

	setImageSprite(arg_6_0.mapPic, LoadSprite(IslandTaskScene.ui_atlas, "map_" .. arg_6_0.mapIndex), True)
	setImageSprite(arg_6_0.mapTitle, LoadSprite(IslandTaskScene.ui_atlas, "map_" .. arg_6_0.mapIndex .. "_desc"), True)

	arg_6_0.taskDatas = var_6_1.open_task

	local var_6_2 = #arg_6_0.taskDatas - #arg_6_0.taskList

	if var_6_2 > 0:
		arg_6_0.addTaskList(var_6_2)

	local var_6_3 = True

	for iter_6_0 = 1, #arg_6_0.taskList:
		local var_6_4 = arg_6_0.taskList[iter_6_0]

		if iter_6_0 <= #arg_6_0.taskDatas:
			setActive(var_6_4, True)

			local var_6_5 = pg.task_data_template[arg_6_0.taskDatas[iter_6_0]]

			setText(findTF(var_6_4, "text"), var_6_5.name)

			local var_6_6 = arg_6_0.checkTaskFinish(var_6_5.id)

			if var_6_3 and var_6_6 != var_6_3:
				var_6_3 = False

			setActive(findTF(var_6_4, "tag/complete"), var_6_6)
		else
			setActive(var_6_4, False)

	local var_6_7 = getProxy(IslandProxy).GetNode(arg_6_0.showMapId).IsCompleted()

	print("mapId ." .. arg_6_0.showMapId .. " get flag = " .. tostring(var_6_7))
	setActive(arg_6_0.finalAward, var_6_3 and not var_6_7)
	setActive(arg_6_0.gotTf, var_6_3 and var_6_7)
	setLocalPosition(findTF(arg_6_0.historyPage, "finalAward"), Vector3(var_0_2[arg_6_0.mapIndex][1], var_0_2[arg_6_0.mapIndex][2], var_0_2[arg_6_0.mapIndex][3]))
	setLocalEulerAngles(findTF(arg_6_0.historyPage, "finalAward/arrow"), Vector3(var_0_3[arg_6_0.mapIndex][1], var_0_3[arg_6_0.mapIndex][2], var_0_3[arg_6_0.mapIndex][3]))

def var_0_0.addTaskList(arg_7_0, arg_7_1):
	for iter_7_0 = 1, arg_7_1:
		local var_7_0 = tf(instantiate(arg_7_0.taskListTpl))

		setActive(var_7_0, False)
		setParent(var_7_0, arg_7_0.listConent)
		table.insert(arg_7_0.taskList, var_7_0)

def var_0_0.checkTaskFinish(arg_8_0, arg_8_1):
	for iter_8_0 = 1, #arg_8_0.finishTasks:
		if arg_8_0.finishTasks[iter_8_0].id == arg_8_1:
			return True

	return False

def var_0_0.setActive(arg_9_0, arg_9_1):
	setActive(arg_9_0.historyPage, arg_9_1)

def var_0_0.dispose(arg_10_0):
	return

return var_0_0
