local var_0_0 = class("ActivityPermanentProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0:on(11210, function(arg_2_0)
		arg_1_0.finishActivity = {}

		underscore.each(arg_2_0.permanent_activity, function(arg_3_0)
			arg_1_0.finishActivity[arg_3_0] = true
		end)

		arg_1_0.doingActivity = arg_2_0.permanent_now
	end)
end

function var_0_0.startSelectActivity(arg_4_0, arg_4_1)
	arg_4_0.doingActivity = arg_4_1
end

function var_0_0.finishNowActivity(arg_5_0, arg_5_1)
	arg_5_0.finishActivity[arg_5_1] = true
	arg_5_0.doingActivity = 0
end

function var_0_0.isActivityFinish(arg_6_0, arg_6_1)
	return arg_6_0.finishActivity[arg_6_1]
end

function var_0_0.getDoingActivity(arg_7_0)
	if arg_7_0.doingActivity ~= 0 then
		return getProxy(ActivityProxy):getActivityById(arg_7_0.doingActivity)
	end

	return nil
end

return var_0_0
