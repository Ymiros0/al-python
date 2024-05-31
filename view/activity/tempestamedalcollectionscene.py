local var_0_0 = class("TempestaMedalCollectionScene", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "TempestaMedalCollectionUI"

def var_0_0.setActivity(arg_2_0, arg_2_1):
	arg_2_0.activity = arg_2_1

def var_0_0.onBackPressed(arg_3_0):
	if isActive(arg_3_0.rtHelpPanel):
		setActive(arg_3_0.rtHelpPanel)
		pg.UIMgr.GetInstance().UnblurPanel(arg_3_0.rtHelpPanel, arg_3_0._tf)

		return

	arg_3_0.closeView()

def var_0_0.init(arg_4_0):
	onButton(arg_4_0, arg_4_0._tf.Find("top/btn_back"), function()
		arg_4_0.onBackPressed(), SFX_CANCEL)

	arg_4_0.rtMainPanel = arg_4_0._tf.Find("main")

	onButton(arg_4_0, arg_4_0.rtMainPanel.Find("btn_help"), function()
		pg.UIMgr.GetInstance().BlurPanel(arg_4_0.rtHelpPanel)
		setActive(arg_4_0.rtHelpPanel, True), SFX_PANEL)

	arg_4_0.rtHelpPanel = arg_4_0._tf.Find("help_panel")

	setText(arg_4_0.rtHelpPanel.Find("window/Text"), i18n("pirate_wanted_help"))
	onButton(arg_4_0, arg_4_0.rtHelpPanel.Find("bg"), function()
		arg_4_0.onBackPressed(), SFX_CANCEL)

def var_0_0.didEnter(arg_8_0):
	arg_8_0.updateTaskLayers()

def var_0_0.updateTaskLayers(arg_9_0):
	local var_9_0 = getProxy(TaskProxy)
	local var_9_1 = underscore.map(arg_9_0.activity.getConfig("config_data"), function(arg_10_0)
		return var_9_0.getTaskVO(arg_10_0))

	for iter_9_0, iter_9_1 in ipairs(var_9_1):
		local var_9_2 = arg_9_0.rtMainPanel.Find("tasks").GetChild(iter_9_0 - 1)

		if iter_9_0 == #var_9_1:
			setActive(var_9_2.Find("got"), iter_9_1.isReceive())

			local var_9_3 = Drop.Create(iter_9_1.getConfig("award_display")[1])

			onButton(arg_9_0, var_9_2, function()
				arg_9_0.emit(BaseUI.ON_DROP, var_9_3), SFX_PANEL)
		else
			local var_9_4 = {}

			var_9_4.type, var_9_4.id, var_9_4.count = unpack(iter_9_1.getConfig("award_display")[1])

			updateDrop(var_9_2.Find("IconTpl"), var_9_4)
			onButton(arg_9_0, var_9_2.Find("IconTpl"), function()
				arg_9_0.emit(BaseUI.ON_DROP, var_9_4), SFX_PANEL)
			setText(var_9_2.Find("Text"), iter_9_1.getConfig("desc"))

			local var_9_5 = iter_9_1.getTaskStatus()

			setActive(var_9_2.Find("btn_go"), var_9_5 == 0)
			setActive(var_9_2.Find("btn_get"), var_9_5 == 1)
			setActive(var_9_2.Find("btn_got"), var_9_5 == 2)
			onButton(arg_9_0, var_9_2.Find("btn_go"), function()
				arg_9_0.emit(TempestaMedalCollectionMediator.ON_TASK_GO, iter_9_1), SFX_PANEL)
			onButton(arg_9_0, var_9_2.Find("btn_get"), function()
				arg_9_0.emit(TempestaMedalCollectionMediator.ON_TASK_SUBMIT, iter_9_1), SFX_PANEL)

	local var_9_6 = #var_9_1 - 1
	local var_9_7 = underscore.reduce(var_9_1, 0, function(arg_15_0, arg_15_1)
		return arg_15_0 + (arg_15_1.isReceive() and 1 or 0))

	setText(arg_9_0.rtMainPanel.Find("progress/Text"), math.min(var_9_7, var_9_6) .. "/" .. var_9_6)

	if var_9_6 <= var_9_7 and not var_9_1[#var_9_1].isReceive():
		arg_9_0.emit(TempestaMedalCollectionMediator.ON_TASK_SUBMIT, var_9_1[#var_9_1])

def var_0_0.willExit(arg_16_0):
	if isActive(arg_16_0.rtHelpPanel):
		arg_16_0.onBackPressed()

return var_0_0
