﻿local var_0_0 = class("ActivityTask", import(".Task"))

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.actId = arg_1_1
	arg_1_0.id = arg_1_2.id
	arg_1_0.configId = arg_1_0.id
	arg_1_0.progress = arg_1_2.progress or 0
	arg_1_0.acceptTime = arg_1_2.accept_time or 0
	arg_1_0.submitTime = arg_1_2.submit_time or 0
	arg_1_0._isOver = false

	arg_1_0:initConfig()
end

function var_0_0.isFinish(arg_2_0)
	return arg_2_0:getProgress() >= arg_2_0:getConfig("target_num")
end

function var_0_0.setOver(arg_3_0)
	arg_3_0._isOver = true
	arg_3_0.progress = arg_3_0:getConfig("target_num")
end

function var_0_0.isOver(arg_4_0)
	return arg_4_0._isOver
end

function var_0_0.isActivitySubmit(arg_5_0)
	if arg_5_0.type == 16 and arg_5_0.subType == 1006 then
		return true
	elseif arg_5_0.type == 6 and arg_5_0.subType == 1006 then
		return true
	end

	return false
end

function var_0_0.getProgress(arg_6_0)
	local var_6_0

	if arg_6_0:isActivitySubmit() then
		local var_6_1 = tonumber(arg_6_0:getConfig("target_id"))
		local var_6_2 = tonumber(arg_6_0:getConfig("target_id_2"))
		local var_6_3 = pg.activity_drop_type[var_6_1].activity_id
		local var_6_4 = getProxy(ActivityProxy):getActivityById(var_6_3)

		if var_6_4 then
			var_6_0 = var_6_4:getVitemNumber(var_6_2)
		else
			warning("找不到活动数据中物品得的数量")

			var_6_0 = 0
		end
	elseif arg_6_0.type == 6 and arg_6_0.subType == TASK_SUB_TYPE_PT then
		local var_6_5 = tonumber(arg_6_0:getConfig("target_id_2"))
		local var_6_6 = getProxy(ActivityProxy):getActivityById(var_6_5)

		if var_6_6 then
			var_6_0 = var_6_6.data1 or 0
		else
			warning("找不到活动数据中物品得的数量")

			var_6_0 = 0
		end
	else
		var_6_0 = arg_6_0.progress

		if var_6_0 > arg_6_0:getConfig("target_num") then
			var_6_0 = arg_6_0:getConfig("target_num")
		end
	end

	return var_6_0 or 0
end

function var_0_0.getTarget(arg_7_0)
	return arg_7_0.target
end

function var_0_0.isReceive(arg_8_0)
	return false
end

function var_0_0.isSubmit(arg_9_0)
	if arg_9_0.subType == 1006 then
		return true
	end

	return false
end

function var_0_0.getTaskStatus(arg_10_0)
	if arg_10_0.progress >= arg_10_0:getConfig("target_num") then
		return 1
	end

	return 0
end

function var_0_0.onAdded(arg_11_0)
	return
end

function var_0_0.updateProgress(arg_12_0, arg_12_1)
	arg_12_0.progress = arg_12_1
end

function var_0_0.isSelectable(arg_13_0)
	return false
end

function var_0_0.judgeOverflow(arg_14_0, arg_14_1, arg_14_2, arg_14_3)
	return false, false
end

function var_0_0.IsUrTask(arg_15_0)
	return false
end

function var_0_0.GetRealType(arg_16_0)
	return 6
end

function var_0_0.isNew(arg_17_0)
	if arg_17_0:isFinish() or arg_17_0:isOver() or arg_17_0:isCircle() then
		return false
	end

	if arg_17_0.actType == ActivityConst.ACTIVITY_TYPE_TASK_RYZA then
		if arg_17_0.groupIndex ~= 1 and PlayerPrefs.GetInt("ryza_task_" .. getProxy(PlayerProxy):getRawData().id .. "_" .. arg_17_0.id) ~= 1 then
			return true
		end

		return false
	end

	return false
end

function var_0_0.changeNew(arg_18_0)
	if arg_18_0.actType == ActivityConst.ACTIVITY_TYPE_TASK_RYZA and arg_18_0.groupIndex ~= 1 and PlayerPrefs.GetInt("ryza_task_" .. getProxy(PlayerProxy):getRawData().id .. "_" .. arg_18_0.id) ~= 1 then
		PlayerPrefs.SetInt("ryza_task_" .. getProxy(PlayerProxy):getRawData().id .. "_" .. arg_18_0.id, 1)
	end
end

function var_0_0.isCircle(arg_19_0)
	if arg_19_0.actType == ActivityConst.ACTIVITY_TYPE_TASK_RYZA then
		if arg_19_0.type == 16 and arg_19_0.subType == 1006 then
			return true
		elseif arg_19_0:isRepeated() then
			return true
		end
	end

	return false
end

function var_0_0.isRepeated(arg_20_0)
	if arg_20_0.type == 16 and arg_20_0.subType == 20 then
		return true
	end

	return false
end

function var_0_0.isDaily(arg_21_0)
	return arg_21_0.subType == 415 or arg_21_0.subType == 412
end

function var_0_0.IsOverflowShipExpItem(arg_22_0)
	return false
end

function var_0_0.ShowOnTaskScene(arg_23_0)
	return false
end

function var_0_0.getConfig(arg_24_0, arg_24_1)
	return arg_24_0.configData[arg_24_1]
end

function var_0_0.isAvatarTask(arg_25_0)
	return false
end

function var_0_0.initConfig(arg_26_0)
	arg_26_0.actConfig = pg.activity_template[arg_26_0.actId]

	local var_26_0 = Activity.Create({
		id = arg_26_0.actId
	})

	arg_26_0.actType = arg_26_0.actConfig.type
	arg_26_0.groups = var_26_0:GetTaskIdsByDay()

	for iter_26_0 = 1, #arg_26_0.groups do
		if table.contains(arg_26_0.groups[iter_26_0], arg_26_0.id) then
			arg_26_0.groupIndex = iter_26_0
		end
	end

	arg_26_0.configData = pg.task_data_template[arg_26_0.id]
	arg_26_0.target = arg_26_0.configData.target_num
	arg_26_0.type = arg_26_0.configData.type
	arg_26_0.subType = arg_26_0.configData.sub_type
	arg_26_0.targetId1 = arg_26_0.configData.target_id
	arg_26_0.targetId2 = arg_26_0.configData.target_id_2
	arg_26_0.autoCommit = arg_26_0.configData.auto_commit == 1

	if arg_26_0.actType == ActivityConst.ACTIVITY_TYPE_TASK_RYZA then
		-- block empty
	end
end

return var_0_0
