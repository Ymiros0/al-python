local var_0_0 = class("USDefTaskWindowView", import("...base.BaseSubView"))

def var_0_0.Load(arg_1_0):
	arg_1_0._tf = findTF(arg_1_0._parentTf, "USDefTaskWindow")
	arg_1_0._go = go(arg_1_0._tf)

	pg.DelegateInfo.New(arg_1_0)
	arg_1_0.OnInit()

def var_0_0.Destroy(arg_2_0):
	arg_2_0.Hide()

def var_0_0.OnInit(arg_3_0):
	arg_3_0.initData()
	arg_3_0.initUI()
	arg_3_0.updateProgress()
	arg_3_0.updateTaskList()
	arg_3_0.Show()

def var_0_0.OnDestroy(arg_4_0):
	return

def var_0_0.initData(arg_5_0):
	local var_5_0 = arg_5_0.contextData.getConfig("config_client")[1]

	arg_5_0.taskIDList = Clone(pg.task_data_template[var_5_0].target_id)
	arg_5_0.taskProxy = getProxy(TaskProxy)
	arg_5_0.taskVOList = {}

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.taskIDList):
		local var_5_1 = arg_5_0.taskProxy.getTaskVO(iter_5_1)

		table.insert(arg_5_0.taskVOList, var_5_1)

def var_0_0.initUI(arg_6_0):
	arg_6_0.bg = arg_6_0.findTF("BG")
	arg_6_0.curNumTextTF = arg_6_0.findTF("ProgressPanel/CurNumText")
	arg_6_0.totalNumText = arg_6_0.findTF("ProgressPanel/TotalNumText")
	arg_6_0.taskTpl = arg_6_0.findTF("TaskTpl")
	arg_6_0.taskContainer = arg_6_0.findTF("TaskList/Viewport/Content")
	arg_6_0.taskList = UIItemList.New(arg_6_0.taskContainer, arg_6_0.taskTpl)

	onButton(arg_6_0, arg_6_0.bg, function()
		arg_6_0.Destroy(), SFX_CANCEL)

def var_0_0.updateProgress(arg_8_0):
	local var_8_0 = #arg_8_0.taskIDList
	local var_8_1 = 0

	for iter_8_0, iter_8_1 in ipairs(arg_8_0.taskVOList):
		if iter_8_1.getTaskStatus() >= 1:
			var_8_1 = var_8_1 + 1

	setText(arg_8_0.curNumTextTF, string.format("%2d", var_8_1))
	setText(arg_8_0.totalNumText, string.format("%2d", var_8_0))

def var_0_0.updateTaskList(arg_9_0):
	arg_9_0.taskList.make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventUpdate:
			arg_10_1 = arg_10_1 + 1

			local var_10_0 = arg_9_0.taskVOList[arg_10_1]
			local var_10_1 = arg_9_0.findTF("IndexText", arg_10_2)
			local var_10_2 = arg_9_0.findTF("TaskIndexText", arg_10_2)
			local var_10_3 = arg_9_0.findTF("DescText", arg_10_2)
			local var_10_4 = arg_9_0.findTF("ItemBG/Icon", arg_10_2)
			local var_10_5 = arg_9_0.findTF("ItemBG/Finished", arg_10_2)

			setText(var_10_1, string.format("%02d", arg_10_1))
			setText(var_10_2, "TASK-" .. string.format("%02d", arg_10_1))

			local var_10_6 = var_10_0.getConfig("desc")

			setText(var_10_3, var_10_6)

			local var_10_7 = tonumber(var_10_0.getConfig("target_id"))

			if not pg.ship_data_statistics[var_10_7]:
				var_10_7 = 205054

			local var_10_8 = pg.ship_data_statistics[var_10_7].skin_id
			local var_10_9 = pg.ship_skin_template[var_10_8].painting

			LoadImageSpriteAsync("SquareIcon/" .. var_10_9, var_10_4)

			local var_10_10 = var_10_0.getTaskStatus()

			setActive(var_10_5, var_10_10 >= 1))
	arg_9_0.taskList.align(#arg_9_0.taskIDList)

return var_0_0
