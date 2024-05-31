local var_0_0 = class("NewMeixiV4SkirmishPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.battleBtn = arg_1_0.findTF("battle_btn", arg_1_0.bg)
	arg_1_0.progressBar = arg_1_0.findTF("progress/bar", arg_1_0.bg)
	arg_1_0.curNum = arg_1_0.findTF("progress/cur_num", arg_1_0.bg)
	arg_1_0.curSection = arg_1_0.findTF("progress/cur_section", arg_1_0.bg)
	arg_1_0.item = arg_1_0.findTF("scrollview/item", arg_1_0.bg)
	arg_1_0.items = arg_1_0.findTF("scrollview/items", arg_1_0.bg)
	arg_1_0.uilist = UIItemList.New(arg_1_0.items, arg_1_0.item)

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.initTaskData()

	return updateActivityTaskStatus(arg_2_0.activity)

def var_0_0.initTaskData(arg_3_0):
	arg_3_0.taskProxy = getProxy(TaskProxy)
	arg_3_0.taskGroup = pg.activity_template[ActivityConst.NEWMEIXIV4_SKIRMISH_ID].config_data
	arg_3_0.taskList = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_0.taskGroup):
		for iter_3_2, iter_3_3 in ipairs(iter_3_1):
			table.insert(arg_3_0.taskList, iter_3_3)

	arg_3_0.SetClearNum()
	arg_3_0.SetCurIndex()

def var_0_0.SetClearNum(arg_4_0):
	arg_4_0.clearTaskNum = 0

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.taskList):
		if arg_4_0.taskProxy.getTaskById(iter_4_1) or arg_4_0.taskProxy.getFinishTaskById(iter_4_1):
			arg_4_0.clearTaskNum = iter_4_0 - 1

			return

def var_0_0.SetCurIndex(arg_5_0):
	arg_5_0.curTaskIndex = 1

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.taskList):
		local var_5_0 = arg_5_0.taskProxy.getTaskById(iter_5_1) or arg_5_0.taskProxy.getFinishTaskById(iter_5_1)
		local var_5_1 = arg_5_0.taskList[iter_5_0 + 1]
		local var_5_2 = arg_5_0.taskProxy.getTaskById(var_5_1) or arg_5_0.taskProxy.getFinishTaskById(var_5_1)

		if var_5_0 and var_5_0.getTaskStatus() == 2:
			arg_5_0.curTaskIndex = arg_5_0.curTaskIndex + 1

			if not var_5_1 or not var_5_2:
				arg_5_0.curTaskIndex = arg_5_0.curTaskIndex - 1

	arg_5_0.curTaskIndex = arg_5_0.curTaskIndex + arg_5_0.clearTaskNum

def var_0_0.OnFirstFlush(arg_6_0):
	onButton(arg_6_0, arg_6_0.battleBtn, function()
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.NEWMEIXIV4_SKIRMISH, {
			taskList = arg_6_0.taskList
		}), SFX_PANEL)
	arg_6_0.uilist.make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate:
			local var_8_0 = arg_8_1 + 1
			local var_8_1 = arg_6_0.findTF("item", arg_8_2)
			local var_8_2 = arg_6_0.taskList[var_8_0]
			local var_8_3 = arg_6_0.taskProxy.getTaskById(var_8_2) or arg_6_0.taskProxy.getFinishTaskById(var_8_2)

			setActive(arg_6_0.findTF("finish", arg_8_2), var_8_3 and var_8_3.getTaskStatus() == 2 or var_8_0 <= arg_6_0.clearTaskNum)
			setActive(arg_6_0.findTF("lock", arg_8_2), False)
			setText(arg_6_0.findTF("title", arg_8_2), "P" .. var_8_0))
	arg_6_0.uilist.align(#arg_6_0.taskList)

def var_0_0.OnUpdateFlush(arg_9_0):
	arg_9_0.SetCurIndex()
	setText(arg_9_0.curNum, string.format("%02d", arg_9_0.curTaskIndex))
	setText(arg_9_0.curSection, "POSITION " .. string.format("%02d", arg_9_0.curTaskIndex))

	arg_9_0.progressBar.GetComponent(typeof(Image)).fillAmount = arg_9_0.curTaskIndex / #arg_9_0.taskList
	arg_9_0.items.anchoredPosition = {
		x = 0,
		y = 55 * (arg_9_0.curTaskIndex - 1)
	}

def var_0_0.IsShowRed():
	local var_10_0 = getProxy(TaskProxy)
	local var_10_1 = pg.activity_template[ActivityConst.NEWMEIXIV4_SKIRMISH_ID].config_data
	local var_10_2 = {}

	for iter_10_0, iter_10_1 in ipairs(var_10_1):
		for iter_10_2, iter_10_3 in ipairs(iter_10_1):
			table.insert(var_10_2, iter_10_3)

	local function var_10_3()
		for iter_11_0, iter_11_1 in ipairs(var_10_2):
			if var_10_0.getTaskById(iter_11_1) or var_10_0.getFinishTaskById(iter_11_1):
				return iter_11_0 - 1

		return 0

	local var_10_4 = 1

	for iter_10_4, iter_10_5 in ipairs(var_10_2):
		local var_10_5 = var_10_0.getTaskById(iter_10_5) or var_10_0.getFinishTaskById(iter_10_5)
		local var_10_6 = var_10_2[iter_10_4 + 1]
		local var_10_7 = var_10_0.getTaskById(var_10_6) or var_10_0.getFinishTaskById(var_10_6)

		if var_10_5 and var_10_5.getTaskStatus() == 2:
			var_10_4 = var_10_4 + 1

			if not var_10_6 or not var_10_7:
				var_10_4 = var_10_4 - 1

	local var_10_8 = var_10_2[var_10_4 + var_10_3()]
	local var_10_9 = var_10_0.getTaskById(var_10_8) or var_10_0.getFinishTaskById(var_10_8)

	return var_10_9 and var_10_9.getTaskStatus() == 1

return var_0_0
