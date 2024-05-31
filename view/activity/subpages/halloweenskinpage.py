local var_0_0 = class("HalloweenSkinPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.stage = arg_1_0.findTF("AD/Text").GetComponent(typeof(Text))
	arg_1_0.goBtn = arg_1_0.findTF("AD/go_btn")
	arg_1_0.gotBtn = arg_1_0.findTF("AD/got_btn")

def var_0_0.OnFirstFlush(arg_2_0):
	arg_2_0.tasks = _.flatten(arg_2_0.activity.getConfig("config_data"))

	onButton(arg_2_0, arg_2_0.goBtn, function()
		if arg_2_0.LastTaskBeFinished():
			return

		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.NAVALACADEMYSCENE), SFX_PANEL)

def var_0_0.LastTaskBeFinished(arg_4_0):
	local var_4_0 = getProxy(TaskProxy)
	local var_4_1 = arg_4_0.tasks[#arg_4_0.tasks]
	local var_4_2 = var_4_0.getTaskVO(var_4_1)

	if var_4_2 and var_4_2.isReceive():
		return True

	return False

def var_0_0.OnUpdateFlush(arg_5_0):
	local var_5_0 = arg_5_0.activity
	local var_5_1 = 0
	local var_5_2 = getProxy(TaskProxy)

	for iter_5_0 = #arg_5_0.tasks, 1, -1:
		local var_5_3 = arg_5_0.tasks[iter_5_0]
		local var_5_4 = var_5_2.getTaskVO(var_5_3)

		if var_5_4 and var_5_4.isReceive():
			var_5_1 = iter_5_0
		elif var_5_4 and not var_5_4.isReceive():
			var_5_1 = iter_5_0 - 1

	arg_5_0.stage.text = var_5_1 .. "/" .. #arg_5_0.tasks

	local var_5_5 = arg_5_0.LastTaskBeFinished()

	setActive(arg_5_0.gotBtn, var_5_5)

def var_0_0.OnDestroy(arg_6_0):
	return

return var_0_0
