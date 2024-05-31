local var_0_0 = class("SystemTimeUtil")

function var_0_0.Ctor(arg_1_0)
	return
end

function var_0_0.SetUp(arg_2_0, arg_2_1)
	arg_2_0.callback = arg_2_1

	arg_2_0:Flush()
end

function var_0_0.Flush(arg_3_0)
	local var_3_0 = pg.TimeMgr.GetInstance():GetServerHour()
	local var_3_1 = var_3_0 < 12 and "AM" or "PM"
	local var_3_2 = pg.TimeMgr.GetInstance():CurrentSTimeDesc("%M", true)

	if arg_3_0.callback then
		arg_3_0.callback(var_3_0, var_3_2, var_3_1)
	end

	local var_3_3 = pg.TimeMgr.GetInstance():GetServerTime()
	local var_3_4 = arg_3_0:GetSecondsToNextMinute(var_3_3)

	arg_3_0:AddTimer(var_3_4)
end

function var_0_0.GetSecondsToNextMinute(arg_4_0, arg_4_1)
	local var_4_0 = math.ceil(arg_4_1 / 60) * 60 - arg_4_1

	if var_4_0 <= 0 then
		return 60
	end

	return var_4_0
end

function var_0_0.AddTimer(arg_5_0, arg_5_1)
	arg_5_0:RemoveTimer()

	arg_5_0.timer = Timer.New(function()
		arg_5_0:Flush()
	end, arg_5_1, 1)

	arg_5_0.timer:Start()
end

function var_0_0.RemoveTimer(arg_7_0)
	if arg_7_0.timer then
		arg_7_0.timer:Stop()

		arg_7_0.timer = nil
	end
end

function var_0_0.Dispose(arg_8_0)
	arg_8_0:RemoveTimer()
end

return var_0_0
