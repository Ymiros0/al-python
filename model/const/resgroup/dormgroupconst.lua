local var_0_0 = {}

var_0_0.DormGroupName = "DORM"
var_0_0.DormMgr = nil

function var_0_0.GetDormMgr()
	if not var_0_0.DormMgr then
		var_0_0.DormMgr = BundleWizard.Inst:GetGroupMgr(var_0_0.DormGroupName)
	end

	return var_0_0.DormMgr
end

var_0_0.NotifyDormDownloadFinish = "DormGroupConst.NotifyDormDownloadFinish"

function var_0_0.VerifyDormFileName(arg_2_0)
	return GroupHelper.VerifyFile(var_0_0.DormGroupName, arg_2_0)
end

function var_0_0.CalcDormListSize(arg_3_0)
	local var_3_0 = GroupHelper.CreateArrByLuaFileList(var_0_0.DormGroupName, arg_3_0)
	local var_3_1 = GroupHelper.CalcSizeWithFileArr(var_0_0.DormGroupName, var_3_0)
	local var_3_2 = HashUtil.BytesToString(var_3_1)

	return var_3_1, var_3_2
end

function var_0_0.IsDormNeedCheck()
	if Application.isEditor then
		return false
	end

	if GroupHelper.IsGroupVerLastest(var_0_0.DormGroupName) then
		return false
	end

	if not GroupHelper.IsGroupWaitToUpdate(var_0_0.DormGroupName) then
		return false
	end

	return true
end

function var_0_0.DormDownload(arg_5_0)
	local var_5_0 = {}

	if var_0_0.IsDormNeedCheck() then
		local var_5_1 = arg_5_0.isShowBox
		local var_5_2 = pg.FileDownloadMgr.GetInstance():IsNeedRemind()
		local var_5_3 = IsUsingWifi()
		local var_5_4 = var_5_1 and var_5_2
		local var_5_5 = arg_5_0.fileList

		if #var_5_5 > 0 then
			if not var_5_3 and var_5_4 then
				local var_5_6, var_5_7 = var_0_0.CalcDormListSize(var_5_5)

				if var_5_6 > 0 then
					table.insert(var_5_0, function(arg_6_0)
						pg.MsgboxMgr.GetInstance():ShowMsgBox({
							modal = true,
							locked = true,
							type = MSGBOX_TYPE_FILE_DOWNLOAD,
							content = string.format(i18n("file_down_msgbox", var_5_7)),
							onYes = arg_6_0,
							onNo = arg_5_0.onNo,
							onClose = arg_5_0.onClose
						})
					end)
				end
			end

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

				pg.FileDownloadMgr.GetInstance():Main(var_7_1)
			end)
			table.insert(var_5_0, function(arg_8_0)
				pg.m02:sendNotification(var_0_0.NotifyDormDownloadFinish)
				arg_8_0()
			end)
		end
	end

	seriesAsync(var_5_0, arg_5_0.finishFunc)
end

return var_0_0
