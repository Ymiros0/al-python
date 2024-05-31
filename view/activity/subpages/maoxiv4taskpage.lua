local var_0_0 = class("MaoxiV4TaskPage", import(".TemplatePage.SkinTemplatePage"))

function var_0_0.OnUpdateFlush(arg_1_0)
	arg_1_0.nday = arg_1_0.activity.data3

	local var_1_0 = arg_1_0.activity:getConfig("config_client").firstStory

	if var_1_0 then
		playStory(var_1_0)
	end

	arg_1_0:PlayStory()

	if arg_1_0.dayTF then
		setText(arg_1_0.dayTF, tostring(arg_1_0.nday))
	end

	arg_1_0.uilist:align(#arg_1_0.taskGroup[arg_1_0.nday])
end

function var_0_0.PlayStory(arg_2_0)
	local var_2_0 = arg_2_0.activity:getConfig("config_client").story
	local var_2_1 = arg_2_0.nday - 1

	if arg_2_0.nday == 7 then
		local var_2_2 = arg_2_0.taskGroup[arg_2_0.nday][1]
		local var_2_3 = arg_2_0.taskGroup[arg_2_0.nday][2]
		local var_2_4 = arg_2_0.taskProxy:getTaskById(var_2_2) or arg_2_0.taskProxy:getFinishTaskById(var_2_2)
		local var_2_5 = arg_2_0.taskProxy:getTaskById(var_2_3) or arg_2_0.taskProxy:getFinishTaskById(var_2_3)

		if var_2_4:getTaskStatus() == 2 and var_2_5:getTaskStatus() == 2 then
			var_2_1 = var_2_1 + 1
		end
	end

	if checkExist(var_2_0, {
		var_2_1
	}, {
		1
	}) then
		pg.NewStoryMgr.GetInstance():Play(var_2_0[var_2_1][1])
	end
end

return var_0_0
