local var_0_0 = class("StoryAwardPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("bg")
	arg_1_0.itemTpl = arg_1_0.findTF("Item")
	arg_1_0.taskItemTpl = arg_1_0.findTF("TaskItem")
	arg_1_0.scrollTF = arg_1_0.findTF("Mask/ScrollView")
	arg_1_0.container = arg_1_0.findTF("Mask/ScrollView/Content")
	arg_1_0.arrow = arg_1_0.findTF("Mask/Arrow")

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.config = pg.activity_event_chapter_award[arg_2_0.activity.getConfig("config_id")]
	arg_2_0.chapterIDList = arg_2_0.config.chapter

def var_0_0.OnFirstFlush(arg_3_0):
	for iter_3_0 = 1, #arg_3_0.chapterIDList:
		local var_3_0 = arg_3_0.chapterIDList[iter_3_0]
		local var_3_1 = pg.chapter_template[var_3_0].chapter_name
		local var_3_2 = cloneTplTo(arg_3_0.taskItemTpl, arg_3_0.container, "TaskItem" .. tostring(iter_3_0))
		local var_3_3 = arg_3_0.findTF("TaskTitle/LevelBum", var_3_2)
		local var_3_4 = arg_3_0.findTF("ItemListContainer", var_3_2)
		local var_3_5 = arg_3_0.findTF("GotTag", var_3_2)
		local var_3_6 = arg_3_0.findTF("GetBtn", var_3_2)

		setText(var_3_3, var_3_1)

		for iter_3_1 = 1, #arg_3_0.config.award_display[iter_3_0]:
			local var_3_7 = cloneTplTo(arg_3_0.itemTpl, var_3_4)
			local var_3_8 = arg_3_0.config.award_display[iter_3_0][iter_3_1]
			local var_3_9 = {
				type = var_3_8[1],
				id = var_3_8[2],
				count = var_3_8[3]
			}

			updateDrop(var_3_7, var_3_9)
			onButton(arg_3_0, var_3_7, function()
				arg_3_0.emit(BaseUI.ON_DROP, var_3_9), SFX_PANEL)

		onButton(arg_3_0, var_3_6, function()
			arg_3_0.emit(ActivityMediator.EVENT_OPERATION, {
				cmd = 1,
				activity_id = arg_3_0.activity.id,
				arg1 = var_3_0
			}), SFX_PANEL)

	onScroll(arg_3_0, arg_3_0.scrollTF, function(arg_6_0)
		setActive(arg_3_0.arrow, arg_6_0.y >= 0.01))

def var_0_0.OnUpdateFlush(arg_7_0):
	for iter_7_0 = 1, #arg_7_0.chapterIDList:
		local var_7_0 = arg_7_0.chapterIDList[iter_7_0]
		local var_7_1 = arg_7_0.findTF("TaskItem" .. tostring(iter_7_0), arg_7_0.container)
		local var_7_2 = arg_7_0.findTF("GotTag", var_7_1)
		local var_7_3 = arg_7_0.findTF("GetBtn", var_7_1)
		local var_7_4 = _.include(arg_7_0.activity.data1_list, var_7_0)

		if var_7_4:
			var_7_1.transform.SetAsLastSibling()

		local var_7_5 = arg_7_0.findTF("TaskTitle", var_7_1)
		local var_7_6 = arg_7_0.findTF("ItemListContainer", var_7_1)

		setGray(var_7_5, var_7_4)
		setGray(var_7_6, var_7_4)
		setActive(var_7_2, var_7_4)
		setActive(var_7_3, getProxy(ChapterProxy).isClear(var_7_0) and not var_7_4)

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
