local var_0_0 = class("LuodeniTaskPage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnUpdateFlush(arg_1_0):
	arg_1_0.nday = arg_1_0.activity.data3

	local var_1_0 = arg_1_0.activity.getConfig("config_client").firstStory

	if var_1_0:
		playStory(var_1_0)

	arg_1_0.PlayStory()

	if arg_1_0.dayTF:
		setText(arg_1_0.dayTF, tostring(arg_1_0.nday))

	arg_1_0.uilist.align(#arg_1_0.taskGroup[arg_1_0.nday])
	setText(arg_1_0.dayTF, setColorStr(arg_1_0.nday, "#F2F5FF") .. setColorStr("/" .. #arg_1_0.taskGroup, "#F2F5FF"))

def var_0_0.PlayStory(arg_2_0):
	local var_2_0 = arg_2_0.activity.getConfig("config_client").story
	local var_2_1 = False

	if arg_2_0.nday == 1:
		local var_2_2 = arg_2_0.taskGroup[1][1]
		local var_2_3 = arg_2_0.taskGroup[1][2]
		local var_2_4 = arg_2_0.taskProxy.getTaskById(var_2_2) or arg_2_0.taskProxy.getFinishTaskById(var_2_2)
		local var_2_5 = arg_2_0.taskProxy.getTaskById(var_2_3) or arg_2_0.taskProxy.getFinishTaskById(var_2_3)

		if var_2_4.getTaskStatus() == 2 and var_2_5.getTaskStatus() == 2 and checkExist(var_2_0, {
			1
		}, {
			1
		}):
			var_2_1 = True

	if arg_2_0.nday == 2:
		var_2_1 = True

	if arg_2_0.nday == 1 and var_2_1 or arg_2_0.nday == 2:
		pg.NewStoryMgr.GetInstance().Play(var_2_0[1][1])

	if arg_2_0.nday == 5:
		local var_2_6 = arg_2_0.nday
		local var_2_7 = arg_2_0.taskGroup[arg_2_0.nday][1]
		local var_2_8 = arg_2_0.taskGroup[arg_2_0.nday][2]
		local var_2_9 = arg_2_0.taskProxy.getTaskById(var_2_7) or arg_2_0.taskProxy.getFinishTaskById(var_2_7)
		local var_2_10 = arg_2_0.taskProxy.getTaskById(var_2_8) or arg_2_0.taskProxy.getFinishTaskById(var_2_8)

		if var_2_9.getTaskStatus() == 2 and var_2_10.getTaskStatus() == 2:
			var_2_6 = var_2_6 + 1

		if checkExist(var_2_0, {
			var_2_6
		}, {
			1
		}):
			pg.NewStoryMgr.GetInstance().Play(var_2_0[var_2_6][1])
	elif arg_2_0.nday != 1 and checkExist(var_2_0, {
		arg_2_0.nday
	}, {
		1
	}):
		pg.NewStoryMgr.GetInstance().Play(var_2_0[arg_2_0.nday][1])

def var_0_0.GetProgressColor(arg_3_0):
	return "#98A7D1", "#98A7D1"

return var_0_0
