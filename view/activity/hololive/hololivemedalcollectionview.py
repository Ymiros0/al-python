local var_0_0 = class("HololiveMedalCollectionView", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "HololiveMedalCollectionUI"

def var_0_0.init(arg_2_0):
	arg_2_0.InitData()
	arg_2_0.FindUI()
	arg_2_0.AddListener()

def var_0_0.didEnter(arg_3_0):
	arg_3_0.UpdateView()

def var_0_0.InitData(arg_4_0):
	local var_4_0 = getProxy(ActivityProxy)

	arg_4_0.taskProxy = getProxy(TaskProxy)
	arg_4_0.actMedal = var_4_0.getActivityById(ActivityConst.HOLOLIVE_MEDAL_COLLECTION)
	arg_4_0.allIDList = arg_4_0.actMedal.getConfig("config_data")
	arg_4_0.taskGroup = pg.activity_template[ActivityConst.HOLOLIVE_MEDAL_COLLECTION_TASK].config_data
	arg_4_0.activatableIDList = arg_4_0.actMedal.data1_list
	arg_4_0.activeIDList = arg_4_0.actMedal.data2_list

local var_0_1 = {
	"mio",
	"fubuki",
	"matsuri",
	"sora",
	"shion",
	"aqua",
	"ayame",
	"purer",
	"tnt"
}
local var_0_2 = {
	1,
	2,
	3,
	6,
	9,
	8,
	7,
	4,
	5
}

def var_0_0.FindUI(arg_5_0):
	arg_5_0.bg = arg_5_0.findTF("bg")
	arg_5_0.top = arg_5_0.findTF("top")
	arg_5_0.backBtn = arg_5_0.findTF("back", arg_5_0.top)
	arg_5_0.helpBtn = arg_5_0.findTF("help", arg_5_0.top)
	arg_5_0.progressText = arg_5_0.findTF("middle/board/progress")
	arg_5_0.taskScroll = arg_5_0.findTF("middle/board/Scroll View")
	arg_5_0.taskScrollBar = arg_5_0.findTF("middle/board/Scrollbar")
	arg_5_0.taskListItems = CustomIndexLayer.Clone2Full(arg_5_0.taskScroll.Find("Content"), #arg_5_0.taskGroup)
	arg_5_0.medalListItems = CustomIndexLayer.Clone2Full(arg_5_0.findTF("middle/console/grid"), 9)
	arg_5_0.medalImg = arg_5_0.findTF("middle/console/slot").GetComponent(typeof(Image))
	arg_5_0.medalGet = arg_5_0.findTF("middle/console/get")
	arg_5_0.medalGot = arg_5_0.findTF("middle/console/got")

	for iter_5_0 = 1, #arg_5_0.taskGroup:
		local var_5_0 = LoadSprite("ui/HololiveMedalCollectionUI_atlas", var_0_1[iter_5_0])
		local var_5_1 = arg_5_0.taskListItems[iter_5_0].Find("icon").GetComponent(typeof(Image))

		var_5_1.sprite = var_5_0
		var_5_1.enabled = True

		local var_5_2 = arg_5_0.medalListItems[var_0_2[iter_5_0]].Find("icon").GetComponent(typeof(Image))

		var_5_2.sprite = var_5_0
		var_5_2.enabled = True

	arg_5_0.materialGray = LoadAny("ui/HololiveMedalCollectionUI_atlas", "gray.mat")

def var_0_0.AddListener(arg_6_0):
	onButton(arg_6_0, arg_6_0.backBtn, function()
		arg_6_0.closeView(), SFX_CANCEL)
	onButton(arg_6_0, arg_6_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.hololive_dalaozhang.tip
		}), SFX_PANEL)

	local var_6_0 = arg_6_0.findTF("middle/board/arrow")

	onScroll(arg_6_0, arg_6_0.taskScroll, function(arg_9_0)
		setActive(var_6_0, arg_9_0.y > 0.001))
	onButton(arg_6_0, arg_6_0.medalGet, function()
		arg_6_0.GetFinal(), SFX_PANEL)

def var_0_0.DataSetting(arg_11_0):
	if #arg_11_0.activatableIDList > 0:
		local var_11_0 = 1
		local var_11_1

		while #arg_11_0.activatableIDList >= 1:
			local var_11_2 = arg_11_0.activatableIDList[var_11_0]

			if not table.contains(arg_11_0.activeIDList, var_11_2):
				var_11_1 = var_11_2

				break

			var_11_0 = var_11_0 + 1

		if var_11_1:
			pg.m02.sendNotification(GAME.MEMORYBOOK_UNLOCK, {
				id = var_11_1,
				actId = ActivityConst.HOLOLIVE_MEDAL_COLLECTION
			})

			return True

def var_0_0.UpdateView(arg_12_0):
	arg_12_0.InitData()

	if arg_12_0.DataSetting():
		return

	local var_12_0 = #arg_12_0.activeIDList == #arg_12_0.allIDList and arg_12_0.actMedal.data1 != 1
	local var_12_1 = arg_12_0.actMedal.data1 == 1
	local var_12_2 = 0

	for iter_12_0 = 1, #arg_12_0.taskGroup:
		local var_12_3 = arg_12_0.taskListItems[iter_12_0]
		local var_12_4 = arg_12_0.taskGroup[iter_12_0]
		local var_12_5 = arg_12_0.taskProxy.getTaskVO(var_12_4)
		local var_12_6 = arg_12_0.findTF("btn_go", var_12_3)
		local var_12_7 = arg_12_0.findTF("btn_get", var_12_3)
		local var_12_8 = arg_12_0.findTF("btn_got", var_12_3)
		local var_12_9 = table.contains(arg_12_0.activeIDList, arg_12_0.allIDList[iter_12_0])
		local var_12_10
		local var_12_11 = 0

		if var_12_5:
			local var_12_12 = var_12_5.getProgress()
			local var_12_13 = var_12_5.getConfig("target_num")
			local var_12_14 = var_12_5.getConfig("desc")
			local var_12_15 = string.gsub(var_12_14, "$1", var_12_12)
			local var_12_16 = string.gsub(var_12_15, "$2", var_12_13)

			setText(arg_12_0.findTF("desc", var_12_3), var_12_16)

			var_12_11 = var_12_5.getTaskStatus()
			var_12_10 = var_12_11 == 2 and arg_12_0.materialGray or None

			onButton(arg_12_0, var_12_6, function()
				arg_12_0.emit(ActivityMediator.ON_TASK_GO, var_12_5), SFX_PANEL)
			onButton(arg_12_0, var_12_7, function()
				arg_12_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_12_5), SFX_PANEL)
		else
			local var_12_17 = pg.task_data_template[var_12_4].target_num
			local var_12_18 = var_12_9 and var_12_17 or 0
			local var_12_19 = pg.task_data_template[var_12_4].desc
			local var_12_20 = string.gsub(var_12_19, "$1", var_12_18)
			local var_12_21 = string.gsub(var_12_20, "$2", var_12_17)

			setText(arg_12_0.findTF("desc", var_12_3), var_12_21)

			var_12_11 = var_12_9 and 2 or 0
			var_12_10 = arg_12_0.materialGray

			onButton(arg_12_0, var_12_6, function()
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")), SFX_PANEL)

		setActive(var_12_6, var_12_11 == 0)
		setActive(var_12_7, var_12_11 == 1)
		setActive(var_12_8, var_12_11 == 2)

		var_12_3.GetComponent(typeof(Image)).material = var_12_10
		var_12_3.Find("icon").GetComponent(typeof(Image)).material = var_12_10

		local var_12_22 = arg_12_0.medalListItems[var_0_2[iter_12_0]].Find("icon").GetComponent(typeof(Image))

		var_12_22.enabled = var_12_9
		var_12_22.material = var_12_1 and arg_12_0.materialGray or None
		var_12_2 = var_12_2 + (var_12_11 == 2 and 1 or 0)

	setText(arg_12_0.progressText, var_12_2 .. "/9")

	arg_12_0.medalImg.material = not var_12_0 and not var_12_1 and arg_12_0.materialGray

	setActive(arg_12_0.medalGet, var_12_0)
	setActive(arg_12_0.medalGot, var_12_1)

def var_0_0.GetFinal(arg_16_0):
	if #arg_16_0.activeIDList == #arg_16_0.allIDList and arg_16_0.actMedal.data1 != 1:
		pg.m02.sendNotification(GAME.ACTIVITY_OPERATION, {
			cmd = 1,
			activity_id = ActivityConst.HOLOLIVE_MEDAL_COLLECTION
		})

def var_0_0.PlayStory(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_0.actMedal.getConfig("config_client").story

	if var_17_0:
		pg.NewStoryMgr.GetInstance().Play(var_17_0, arg_17_1)
	else
		arg_17_1()

def var_0_0.IsTip():
	local var_18_0 = getProxy(ActivityProxy)
	local var_18_1 = getProxy(TaskProxy)
	local var_18_2 = var_18_0.getActivityById(ActivityConst.HOLOLIVE_MEDAL_COLLECTION)

	if var_18_2 and not var_18_2.isEnd():
		local var_18_3 = var_18_2.getConfig("config_data")
		local var_18_4 = pg.activity_template[ActivityConst.HOLOLIVE_MEDAL_COLLECTION_TASK].config_data
		local var_18_5 = var_18_2.data1_list
		local var_18_6 = var_18_2.data2_list

		for iter_18_0, iter_18_1 in ipairs(var_18_4):
			local var_18_7 = var_18_4[iter_18_0]
			local var_18_8 = var_18_1.getTaskVO(var_18_7)

			if var_18_8 and var_18_8.getTaskStatus() == 1:
				return True

		for iter_18_2, iter_18_3 in ipairs(var_18_5):
			if not table.contains(var_18_6, iter_18_3):
				return True

		if #var_18_6 == #var_18_3 and var_18_2.data1 != 1:
			return True

return var_0_0
