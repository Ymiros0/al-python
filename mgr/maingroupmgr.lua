pg = pg or {}
pg.MainGroupMgr = singletonClass("MainGroupMgr")

local var_0_0 = pg.MainGroupMgr

var_0_0.GroupNameList = {
	PaintingGroupConst.PaintingGroupName
}

function var_0_0.Ctor(arg_1_0)
	arg_1_0:initData()
end

function var_0_0.StartCheckD(arg_2_0)
	arg_2_0.curGroupIndex = 1

	arg_2_0:checkWithIndex(arg_2_0.curGroupIndex)
	arg_2_0:createCheckTimer()
end

function var_0_0.StartUpdateD(arg_3_0)
	arg_3_0.finishCount = 0

	arg_3_0:SetTotalCount()

	arg_3_0.curGroupIndex = 1

	arg_3_0:updateWithIndex(arg_3_0.curGroupIndex)
	arg_3_0:createUpdateTimer()
end

function var_0_0.GetState(arg_4_0)
	local var_4_0

	if arg_4_0.curGroupIndex > #var_0_0.GroupNameList then
		var_4_0 = #var_0_0.GroupNameList
	else
		var_4_0 = arg_4_0.curGroupIndex
	end

	return arg_4_0.groupList[var_4_0].state
end

function var_0_0.GetCountProgress(arg_5_0)
	local var_5_0 = arg_5_0.groupList[arg_5_0.curGroupIndex]

	return arg_5_0.finishCount + var_5_0.downloadCount, arg_5_0.totalCount
end

function var_0_0.SetTotalCount(arg_6_0)
	arg_6_0.totalCount = 0

	for iter_6_0, iter_6_1 in ipairs(arg_6_0.groupList) do
		arg_6_0.totalCount = arg_6_0.totalCount + iter_6_1.toUpdate.Count
	end

	return arg_6_0.totalCount
end

function var_0_0.GetTotalSize(arg_7_0)
	local var_7_0 = 0

	for iter_7_0, iter_7_1 in ipairs(var_0_0.GroupNameList) do
		var_7_0 = var_7_0 + GroupHelper.GetGroupSize(iter_7_1)
	end

	return var_7_0
end

function var_0_0.initData(arg_8_0)
	arg_8_0.curGroupIndex = 1
	arg_8_0.frameTimer = nil
	arg_8_0.finishCount = 0
	arg_8_0.totalCount = 0
	arg_8_0.groupList = {}

	for iter_8_0, iter_8_1 in ipairs(var_0_0.GroupNameList) do
		local var_8_0 = GroupHelper.GetGroupMgrByName(iter_8_1)

		table.insert(arg_8_0.groupList, var_8_0)
	end
end

function var_0_0.clearTimer(arg_9_0)
	if arg_9_0.frameTimer then
		arg_9_0.frameTimer:Stop()

		arg_9_0.frameTimer = nil
	end
end

function var_0_0.checkWithIndex(arg_10_0, arg_10_1)
	if arg_10_1 > #var_0_0.GroupNameList then
		arg_10_0:clearTimer()

		return
	end

	arg_10_0.groupList[arg_10_0.curGroupIndex]:CheckD()
end

function var_0_0.onCheckD(arg_11_0)
	local var_11_0 = arg_11_0.groupList[arg_11_0.curGroupIndex]
	local var_11_1 = var_11_0.state

	if var_11_1 == DownloadState.CheckToUpdate or var_11_1 == DownloadState.CheckOver or var_11_1 == DownloadState.UpdateSuccess then
		arg_11_0.curGroupIndex = arg_11_0.curGroupIndex + 1

		arg_11_0:checkWithIndex(arg_11_0.curGroupIndex)
	elseif var_11_0.state == DownloadState.CheckFailure then
		arg_11_0:clearTimer()
	end
end

function var_0_0.createCheckTimer(arg_12_0)
	arg_12_0.frameTimer = FrameTimer.New(function()
		arg_12_0:onCheckD()
	end, 1, -1)

	arg_12_0.frameTimer:Start()
end

function var_0_0.updateWithIndex(arg_14_0, arg_14_1)
	if arg_14_1 > #var_0_0.GroupNameList then
		arg_14_0:clearTimer()

		return
	end

	arg_14_0.groupList[arg_14_0.curGroupIndex]:UpdateD()
end

function var_0_0.onUpdateD(arg_15_0)
	local var_15_0 = arg_15_0.groupList[arg_15_0.curGroupIndex]

	if var_15_0.state == DownloadState.UpdateSuccess then
		arg_15_0.finishCount = arg_15_0.finishCount + var_15_0.downloadTotal
		arg_15_0.curGroupIndex = arg_15_0.curGroupIndex + 1

		arg_15_0:updateWithIndex(arg_15_0.curGroupIndex)
	elseif var_15_0.state == DownloadState.UpdateFailure then
		arg_15_0:clearTimer()
	end
end

function var_0_0.createUpdateTimer(arg_16_0)
	arg_16_0.frameTimer = FrameTimer.New(function()
		arg_16_0:onUpdateD()
	end, 1, -1)

	arg_16_0.frameTimer:Start()
end
