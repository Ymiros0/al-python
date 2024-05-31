pg = pg or {}

local var_0_0 = pg

var_0_0.FileDownloadMgr = singletonClass("FileDownloadMgr")

local var_0_1 = var_0_0.FileDownloadMgr
local var_0_2 = FileDownloadConst

def var_0_1.Init(arg_1_0, arg_1_1):
	print("initializing filedownloadmgr manager...")
	PoolMgr.GetInstance().GetUI("FileDownloadUI", True, function(arg_2_0)
		arg_1_0._go = arg_2_0

		arg_1_0._go.SetActive(False)

		arg_1_0._tf = arg_1_0._go.transform

		arg_1_0._tf.SetParent(var_0_0.UIMgr.GetInstance().OverlayMain, False)
		arg_1_0.initUI()
		arg_1_0.initUITextTips()
		arg_1_1())

def var_0_1.Main(arg_3_0, arg_3_1):
	arg_3_0.initData()
	arg_3_0.setData(arg_3_1)
	arg_3_0.show()
	arg_3_0.startDownload()

def var_0_1.IsRunning(arg_4_0):
	return isActive(arg_4_0._go)

var_0_1.KEY_STOP_REMIND = "File_Download_Remind_Time"

def var_0_1.SetRemind(arg_5_0, arg_5_1):
	arg_5_0.isStopRemind = arg_5_1

def var_0_1.IsNeedRemind(arg_6_0):
	if arg_6_0.isStopRemind == True:
		return False
	else
		return True

def var_0_1.show(arg_7_0):
	arg_7_0._go.SetActive(True)

def var_0_1.hide(arg_8_0):
	arg_8_0._go.SetActive(False)

def var_0_1.initUI(arg_9_0):
	arg_9_0.mainTF = arg_9_0._tf.Find("Main")
	arg_9_0.titleText = arg_9_0.mainTF.Find("Title")
	arg_9_0.progressText = arg_9_0.mainTF.Find("ProgressText")
	arg_9_0.progressBar = arg_9_0.mainTF.Find("ProgressBar")

def var_0_1.initUITextTips(arg_10_0):
	setText(arg_10_0.titleText, i18n("file_down_mgr_title"))

def var_0_1.initData(arg_11_0):
	arg_11_0.curGroupIndex = 0
	arg_11_0.curGroupMgr = None
	arg_11_0.validGroupNameList = None
	arg_11_0.validFileNameArrMap = None
	arg_11_0.dataList = None
	arg_11_0.onFinish = None

def var_0_1.setData(arg_12_0, arg_12_1):
	arg_12_0.dataList = arg_12_1.dataList
	arg_12_0.onFinish = arg_12_1.onFinish

def var_0_1.fileProgress(arg_13_0, arg_13_1, arg_13_2, arg_13_3, arg_13_4):
	local var_13_0 = HashUtil.BytesToString(arg_13_3)
	local var_13_1 = HashUtil.BytesToString(arg_13_4)

	setText(arg_13_0.progressText, i18n("file_down_mgr_progress", var_13_0, var_13_1))
	setSlider(arg_13_0.progressBar, 0, arg_13_4, arg_13_3)

def var_0_1.fileFinish(arg_14_0, arg_14_1, arg_14_2):
	return

def var_0_1.groupComplete(arg_15_0, arg_15_1):
	local var_15_0 = HashUtil.BytesToString(arg_15_1)

	setText(arg_15_0.progressText, i18n("file_down_mgr_progress", var_15_0, var_15_0))
	setSlider(arg_15_0.progressBar, 0, 1, 1)

	arg_15_0.curGroupIndex = arg_15_0.curGroupIndex + 1

	if arg_15_0.curGroupIndex > #arg_15_0.validGroupNameList:
		arg_15_0.allComplete()
	else
		arg_15_0.download(arg_15_0.curGroupIndex)

def var_0_1.allComplete(arg_16_0):
	if arg_16_0.onFinish:
		arg_16_0.onFinish()

	arg_16_0.initData()
	arg_16_0.hide()

def var_0_1.error(arg_17_0, arg_17_1, arg_17_2):
	local function var_17_0()
		arg_17_0.show()
		arg_17_0.startDownload()

	local function var_17_1()
		Application.Quit()

	arg_17_0.hide()
	var_0_0.MsgboxMgr.GetInstance().ShowMsgBox({
		modal = True,
		locked = True,
		content = i18n("file_down_mgr_error", arg_17_1, arg_17_2),
		onYes = var_17_0,
		onNo = var_17_1,
		onClose = var_17_1,
		weight = LayerWeightConst.TOP_LAYER
	})

def var_0_1.download(arg_20_0):
	local var_20_0 = arg_20_0.validGroupNameList[arg_20_0.curGroupIndex]
	local var_20_1 = arg_20_0.validFileNameArrMap[var_20_0]

	if not var_20_1 or var_20_1.Length == 0:
		arg_20_0.groupComplete()

		return

	arg_20_0.curGroupMgr = GroupHelper.GetGroupMgrByName(var_20_0)

	local function var_20_2(arg_21_0, arg_21_1, arg_21_2, arg_21_3)
		arg_20_0.fileProgress(arg_21_0, arg_21_1, arg_21_2, arg_21_3)

	local function var_20_3(arg_22_0, arg_22_1)
		arg_20_0.fileFinish(arg_22_0, arg_22_1)

	local function var_20_4(arg_23_0, arg_23_1)
		warning("----------------------Tag 单组下载完成,恢复UpdateD----------------------")

		arg_20_0.curGroupMgr.isPauseUpdateD = False

		warning("----------------------Tag 单组下载完成,调用groupComplete----------------------")
		arg_20_0.groupComplete(arg_23_1)

	local function var_20_5(arg_24_0, arg_24_1)
		arg_20_0.error(arg_24_0, arg_24_1)

	warning("----------------------Tag 停止UpdateD----------------------")

	arg_20_0.curGroupMgr.isPauseUpdateD = True

	warning("----------------------Tag 开始UpdateFileArray----------------------")
	arg_20_0.curGroupMgr.UpdateFileArray(var_20_1, var_20_2, var_20_3, var_20_4, var_20_5)

def var_0_1.startDownload(arg_25_0):
	if arg_25_0.verifyValidData():
		arg_25_0.curGroupIndex = 1

		arg_25_0.download(arg_25_0.curGroupIndex)
	else
		arg_25_0.allComplete()

def var_0_1.verifyValidData(arg_26_0):
	arg_26_0.validGroupNameList = {}
	arg_26_0.validFileNameArrMap = {}

	for iter_26_0, iter_26_1 in ipairs(arg_26_0.dataList):
		local var_26_0 = iter_26_1.groupName
		local var_26_1 = iter_26_1.fileNameList
		local var_26_2

		if var_26_1 and #var_26_1 > 0:
			var_26_2 = GroupHelper.CreateArrByLuaFileList(var_26_0, var_26_1)

		if var_26_2 and var_26_2.Length > 0:
			table.insert(arg_26_0.validGroupNameList, var_26_0)

			arg_26_0.validFileNameArrMap[var_26_0] = var_26_2

	return #arg_26_0.validGroupNameList > 0
