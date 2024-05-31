local var_0_0 = {}

var_0_0.DormGroupName = "DORM"
var_0_0.DormMgr = None

def var_0_0.GetDormMgr():
	if not var_0_0.DormMgr:
		var_0_0.DormMgr = BundleWizard.Inst.GetGroupMgr(var_0_0.DormGroupName)

	return var_0_0.DormMgr

var_0_0.NotifyDormDownloadFinish = "DormGroupConst.NotifyDormDownloadFinish"

def var_0_0.VerifyDormFileName(arg_2_0):
	return GroupHelper.VerifyFile(var_0_0.DormGroupName, arg_2_0)

def var_0_0.CalcDormListSize(arg_3_0):
	local var_3_0 = GroupHelper.CreateArrByLuaFileList(var_0_0.DormGroupName, arg_3_0)
	local var_3_1 = GroupHelper.CalcSizeWithFileArr(var_0_0.DormGroupName, var_3_0)
	local var_3_2 = HashUtil.BytesToString(var_3_1)

	return var_3_1, var_3_2

def var_0_0.IsDormNeedCheck():
	if Application.isEditor:
		return False

	if GroupHelper.IsGroupVerLastest(var_0_0.DormGroupName):
		return False

	if not GroupHelper.IsGroupWaitToUpdate(var_0_0.DormGroupName):
		return False

	return True

def var_0_0.DormDownload(arg_5_0):
	local var_5_0 = {}

	if var_0_0.IsDormNeedCheck():
		local var_5_1 = arg_5_0.isShowBox
		local var_5_2 = pg.FileDownloadMgr.GetInstance().IsNeedRemind()
		local var_5_3 = IsUsingWifi()
		local var_5_4 = var_5_1 and var_5_2
		local var_5_5 = arg_5_0.fileList

		if #var_5_5 > 0:
			if not var_5_3 and var_5_4:
				local var_5_6, var_5_7 = var_0_0.CalcDormListSize(var_5_5)

				if var_5_6 > 0:
					table.insert(var_5_0, function(arg_6_0)
						pg.MsgboxMgr.GetInstance().ShowMsgBox({
							modal = True,
							locked = True,
							type = MSGBOX_TYPE_FILE_DOWNLOAD,
							content = string.format(i18n("file_down_msgbox", var_5_7)),
							onYes = arg_6_0,
							onNo = arg_5_0.onNo,
							onClose = arg_5_0.onClose
						}))

			table.insert(var_5_0, function(arg_7_0)
				local var_7_0 = {
					groupName = var_0_0.DormGroupName,
					fileNameList = var_5_5
				}
				local var_7_1 = {
					dataList = {
						var_7_0
					},
					onFinish = arg_7_0
				}

				pg.FileDownloadMgr.GetInstance().Main(var_7_1))
			table.insert(var_5_0, function(arg_8_0)
				pg.m02.sendNotification(var_0_0.NotifyDormDownloadFinish)
				arg_8_0())

	seriesAsync(var_5_0, arg_5_0.finishFunc)

return var_0_0
