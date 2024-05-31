local var_0_0 = class("SecondaryPWDProxy", import(".NetProxy"))

function var_0_0.register(arg_1_0)
	arg_1_0.data = arg_1_0.data or {}

	local var_1_0 = arg_1_0.data

	var_1_0.state = 0
	var_1_0.fail_count = 0
	var_1_0.fail_cd = nil
	var_1_0.notice = nil
	var_1_0.system_list = {}
end

function var_0_0.SetData(arg_2_0, arg_2_1)
	arg_2_0.data = arg_2_0.data or {}

	local var_2_0 = arg_2_0.data

	var_2_0.state = arg_2_1.state
	var_2_0.fail_count = arg_2_1.fail_count
	var_2_0.fail_cd = arg_2_1.fail_cd
	var_2_0.notice = arg_2_1.notice
	var_2_0.system_list = {}

	for iter_2_0 = 1, #pg.SecondaryPWDMgr.LIMITED_OPERATION do
		table.insert(var_2_0.system_list, arg_2_1.system_list[iter_2_0])
	end
end

function var_0_0.OnFirstSet(arg_3_0, arg_3_1)
	arg_3_0.data = arg_3_0.data or {}

	local var_3_0 = arg_3_0.data

	var_3_0.state = 1
	var_3_0.system_list = Clone(arg_3_1.settings)
	var_3_0.fail_count = 0
	var_3_0.fail_cd = nil
	var_3_0.notice = Clone(arg_3_1.tip)
end

function var_0_0.OnSettingsChange(arg_4_0, arg_4_1)
	arg_4_0.data = arg_4_0.data or {}

	local var_4_0 = arg_4_0.data

	var_4_0.state = #arg_4_1.settings == 0 and 0 or 2
	var_4_0.system_list = Clone(arg_4_1.settings)
	var_4_0.fail_cd = nil
	var_4_0.fail_count = 0
end

function var_0_0.GetPermissionState(arg_5_0)
	if arg_5_0.data.state == 0 then
		return true
	end

	local var_5_0 = arg_5_0.data.fail_cd
	local var_5_1 = pg.TimeMgr.GetInstance():GetServerTime()

	if var_5_0 and var_5_1 < var_5_0 then
		return false, var_5_0 - var_5_1
	end

	return true
end

return var_0_0
