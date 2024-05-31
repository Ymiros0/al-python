local var_0_0 = class("YidaliMainPage", import(".TemplatePage.PreviewTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)
	arg_1_0.initUI()

def var_0_0.OnFirstFlush(arg_2_0):
	var_0_0.super.OnFirstFlush(arg_2_0)

	arg_2_0.fight = arg_2_0.findTF("fight", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.fight, function()
		arg_2_0.emit(ActivityMediator.BATTLE_OPERA), SFX_PANEL)

	arg_2_0.build = arg_2_0.findTF("build", arg_2_0.btnList)

	onButton(arg_2_0, arg_2_0.build, function()
		local var_4_0
		local var_4_1

		if arg_2_0.activity.getConfig("config_client") != "":
			var_4_0 = arg_2_0.activity.getConfig("config_client").linkActID

			if var_4_0:
				var_4_1 = getProxy(ActivityProxy).getActivityById(var_4_0)

		if not var_4_0:
			arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
				projectName = BuildShipScene.PROJECTS.ACTIVITY
			})
		elif var_4_1 and not var_4_1.isEnd():
			arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.GETBOAT, {
				projectName = BuildShipScene.PROJECTS.ACTIVITY
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")), SFX_PANEL)
	arg_2_0.initData()
	arg_2_0.submitFinishedTask()

def var_0_0.OnUpdateFlush(arg_5_0):
	arg_5_0.updateAwardBtn()

def var_0_0.initData(arg_6_0):
	arg_6_0.finalTaskID = arg_6_0.activity.getConfig("config_client")[1]
	arg_6_0.YDLtaskIDList = arg_6_0.activity.getConfig("config_data")
	arg_6_0.taskIDList = Clone(pg.task_data_template[arg_6_0.finalTaskID].target_id)
	arg_6_0.taskProxy = getProxy(TaskProxy)

def var_0_0.initUI(arg_7_0):
	arg_7_0.awardTF = arg_7_0.findTF("Item", arg_7_0.bg)
	arg_7_0.activeTF = arg_7_0.findTF("Active", arg_7_0.awardTF)
	arg_7_0.finishedTF = arg_7_0.findTF("Finished", arg_7_0.awardTF)
	arg_7_0.achievedTF = arg_7_0.findTF("Achieved", arg_7_0.awardTF)

	setActive(arg_7_0.activeTF, False)
	setActive(arg_7_0.finishedTF, False)
	setActive(arg_7_0.achievedTF, False)

	arg_7_0.achievementBtn = arg_7_0.findTF("AchieveMentBtn", arg_7_0.bg)
	arg_7_0.subViewContainer = arg_7_0.findTF("SubViewContainer")

def var_0_0.updateAwardBtn(arg_8_0):
	local var_8_0 = arg_8_0.getFinalTaskStatus()

	print("final taskid." .. arg_8_0.finalTaskID)
	print("task status." .. var_8_0)

	if var_8_0 == 0:
		setActive(arg_8_0.activeTF, True)
		setActive(arg_8_0.finishedTF, False)
		setActive(arg_8_0.achievedTF, False)
	elif var_8_0 == 1:
		setActive(arg_8_0.activeTF, False)
		setActive(arg_8_0.finishedTF, True)
		setActive(arg_8_0.achievedTF, False)
		onButton(arg_8_0, arg_8_0.awardTF, function()
			local var_9_0 = arg_8_0.taskProxy.getTaskVO(arg_8_0.finalTaskID)

			arg_8_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_9_0), SFX_PANEL)
	elif var_8_0 == 2:
		setActive(arg_8_0.activeTF, False)
		setActive(arg_8_0.finishedTF, False)
		setActive(arg_8_0.achievedTF, True)
		onButton(arg_8_0, arg_8_0.awardTF, function()
			return, SFX_PANEL)

def var_0_0.submitFinishedTask(arg_11_0):
	for iter_11_0, iter_11_1 in ipairs(arg_11_0.YDLtaskIDList):
		local var_11_0 = arg_11_0.taskProxy.getTaskById(iter_11_1)

		if var_11_0 and var_11_0.isFinish() and not var_11_0.isReceive():
			print("!!!!!!!!!!!!!20190907!!!!!!!YDLtaskIDList emit." .. iter_11_1)
			arg_11_0.emit(ActivityMediator.ON_TASK_SUBMIT, var_11_0)

def var_0_0.getFinalTaskStatus(arg_12_0):
	return arg_12_0.taskProxy.getTaskVO(arg_12_0.finalTaskID).getTaskStatus()

return var_0_0
