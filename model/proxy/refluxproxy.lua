local var_0_0 = class("RefluxProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0:initData()
	arg_1_0:addListener()
end

function var_0_0.initData(arg_2_0)
	arg_2_0.active = false
	arg_2_0.returnLV = 0
	arg_2_0.returnTimestamp = 0
	arg_2_0.returnShipNum = 0
	arg_2_0.returnLastTimestamp = 0
	arg_2_0.ptNum = 0
	arg_2_0.ptStage = 0
	arg_2_0.signCount = 0
	arg_2_0.signLastTimestamp = 0
	arg_2_0.autoActionForbidden = false
end

function var_0_0.setData(arg_3_0, arg_3_1)
	arg_3_0.active = arg_3_1.active == 1
	arg_3_0.returnLV = arg_3_1.return_lv
	arg_3_0.returnTimestamp = arg_3_1.return_time
	arg_3_0.returnShipNum = arg_3_1.ship_number
	arg_3_0.returnLastTimestamp = arg_3_1.last_offline_time
	arg_3_0.ptNum = arg_3_1.pt
	arg_3_0.ptStage = arg_3_1.pt_stage
	arg_3_0.signCount = arg_3_1.sign_cnt
	arg_3_0.signLastTimestamp = arg_3_1.sign_last_time
end

function var_0_0.addListener(arg_4_0)
	arg_4_0:on(11752, function(arg_5_0)
		arg_4_0:setData(arg_5_0)
	end)
end

function var_0_0.setSignLastTimestamp(arg_6_0, arg_6_1)
	arg_6_0.signLastTimestamp = arg_6_1 or pg.TimeMgr.GetInstance():GetServerTime()
end

function var_0_0.addSignCount(arg_7_0)
	arg_7_0.signCount = arg_7_0.signCount + 1
end

function var_0_0.addPtAfterSubTasks(arg_8_0, arg_8_1)
	for iter_8_0, iter_8_1 in ipairs(arg_8_1) do
		local var_8_0 = iter_8_1.id
		local var_8_1 = pg.return_task_template[var_8_0].pt_award

		arg_8_0.ptNum = arg_8_0.ptNum + var_8_1
	end
end

function var_0_0.addPTStage(arg_9_0)
	arg_9_0.ptStage = arg_9_0.ptStage + 1
end

function var_0_0.isActive(arg_10_0)
	return arg_10_0.active
end

function var_0_0.isCanSign(arg_11_0)
	if arg_11_0:isActive() and not arg_11_0.autoActionForbidden then
		local var_11_0 = pg.TimeMgr.GetInstance()
		local var_11_1 = arg_11_0.signCount
		local var_11_2 = #pg.return_sign_template.all
		local var_11_3 = arg_11_0.signLastTimestamp
		local var_11_4 = var_11_0:GetServerTime()
		local var_11_5 = var_11_0:IsSameDay(var_11_4, var_11_3)

		if var_11_1 < var_11_2 and not var_11_5 then
			return true
		end
	end
end

function var_0_0.isInRefluxTime(arg_12_0)
	if arg_12_0:isActive() then
		local var_12_0 = pg.TimeMgr.GetInstance()
		local var_12_1 = #pg.return_sign_template.all

		if arg_12_0.returnTimestamp + var_12_1 * 86400 <= var_12_0:GetServerTime() then
			return false
		else
			return true
		end
	else
		return false
	end
end

function var_0_0.setAutoActionForbidden(arg_13_0, arg_13_1)
	arg_13_0.autoActionForbidden = arg_13_1
end

return var_0_0
