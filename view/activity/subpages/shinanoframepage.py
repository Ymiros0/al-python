local var_0_0 = class("ShinanoframePage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.goBtn = arg_1_0.findTF("GoBtn", arg_1_0.bg)
	arg_1_0.getBtn = arg_1_0.findTF("GetBtn", arg_1_0.bg)
	arg_1_0.gotBtn = arg_1_0.findTF("GotBtn", arg_1_0.bg)
	arg_1_0.switchBtn = arg_1_0.findTF("SwitchBtn", arg_1_0.bg)
	arg_1_0.phaseTF_1 = arg_1_0.findTF("Phase1", arg_1_0.bg)
	arg_1_0.phaseTF_2 = arg_1_0.findTF("Phase2", arg_1_0.bg)
	arg_1_0.gotTag = arg_1_0.findTF("Phase2/GotTag", arg_1_0.bg)
	arg_1_0.frameTF = arg_1_0.findTF("Phase2/Icon", arg_1_0.bg)
	arg_1_0.progressBar = arg_1_0.findTF("Phase2/Progress", arg_1_0.bg)
	arg_1_0.progressText = arg_1_0.findTF("Phase2/ProgressText", arg_1_0.bg)

	setActive(arg_1_0.goBtn, False)
	setActive(arg_1_0.getBtn, False)
	setActive(arg_1_0.gotBtn, False)
	setActive(arg_1_0.gotTag, False)
	setActive(arg_1_0.progressBar, False)
	setActive(arg_1_0.progressText, False)
	setActive(arg_1_0.phaseTF_2, False)

def var_0_0.OnDataSetting(arg_2_0):
	if arg_2_0.ptData:
		arg_2_0.ptData.Update(arg_2_0.activity)
	else
		arg_2_0.ptData = ActivityPtData.New(arg_2_0.activity)

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.goBtn, function()
		arg_3_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.TASK), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.getBtn, function()
		local var_5_0, var_5_1 = arg_3_0.ptData.GetResProgress()

		arg_3_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
			cmd = 1,
			activity_id = arg_3_0.ptData.GetId(),
			arg1 = var_5_1
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.switchBtn, function()
		setActive(arg_3_0.phaseTF_1, not isActive(arg_3_0.phaseTF_1))
		setActive(arg_3_0.phaseTF_2, not isActive(arg_3_0.phaseTF_2)), SFX_PANEL)

	local var_3_0 = arg_3_0.ptData.dropList[1][2]
	local var_3_1 = tostring(var_3_0)
	local var_3_2 = LoadAndInstantiateSync("IconFrame", var_3_1)

	setParent(var_3_2, arg_3_0.frameTF, False)

def var_0_0.OnUpdateFlush(arg_7_0):
	local var_7_0 = getProxy(ActivityProxy).getActivityById(ActivityConst.SHINANO_EXP_ACT_ID)

	if not var_7_0 or var_7_0.isEnd():
		setActive(arg_7_0.phaseTF_1, False)
		setActive(arg_7_0.phaseTF_2, True)

		local var_7_1, var_7_2, var_7_3 = arg_7_0.ptData.GetResProgress()

		setText(arg_7_0.progressText, var_7_1 .. "/" .. var_7_2)
		setSlider(arg_7_0.progressBar, 0, 1, var_7_3)
		setActive(arg_7_0.progressBar, True)
		setActive(arg_7_0.progressText, True)

		local var_7_4 = arg_7_0.ptData.CanGetAward()
		local var_7_5 = arg_7_0.ptData.CanGetNextAward()
		local var_7_6 = arg_7_0.ptData.CanGetMorePt()

		setActive(arg_7_0.goBtn, var_7_6 and not var_7_4 and var_7_5)
		setActive(arg_7_0.getBtn, var_7_4)
		setActive(arg_7_0.gotBtn, not var_7_5)
		setActive(arg_7_0.gotTag, not var_7_5)
	else
		setActive(arg_7_0.phaseTF_1, True)
		setActive(arg_7_0.phaseTF_2, False)

		local var_7_7, var_7_8, var_7_9 = arg_7_0.ptData.GetResProgress()

		setText(arg_7_0.progressText, var_7_7 .. "/" .. var_7_8)
		setSlider(arg_7_0.progressBar, 0, 1, var_7_9)
		setActive(arg_7_0.progressBar, True)
		setActive(arg_7_0.progressText, True)

def var_0_0.OnDestroy(arg_8_0):
	return

return var_0_0
