local var_0_0 = class("PiratePage", import("view.base.BaseActivityPage"))

var_0_0.PROGRESS_TEXT = "%d/7"
var_0_0.DIALOG_DELAY = 15

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.progress = arg_1_0.findTF("progress", arg_1_0.bg)
	arg_1_0.progressText = arg_1_0.findTF("Text", arg_1_0.progress)
	arg_1_0.complete = arg_1_0.findTF("complete", arg_1_0.bg)
	arg_1_0.goBtn = arg_1_0.findTF("go_btn", arg_1_0.bg)
	arg_1_0.red = arg_1_0.findTF("red", arg_1_0.goBtn)
	arg_1_0.dialogTf = arg_1_0.findTF("dialog", arg_1_0.bg)
	arg_1_0.dialogText = arg_1_0.findTF("Text", arg_1_0.dialogTf)

def var_0_0.OnDataSetting(arg_2_0):
	arg_2_0.count = 0
	arg_2_0.taskProxy = getProxy(TaskProxy)
	arg_2_0.taskGroup = arg_2_0.activity.getConfig("config_data")
	arg_2_0.totoalCount = #arg_2_0.taskGroup
	arg_2_0.dialog_progress = arg_2_0.activity.getConfig("config_client").shipyard_phase_1
	arg_2_0.dialog_complete = arg_2_0.activity.getConfig("config_client").shipyard_phase_2

	return updateActivityTaskStatus(arg_2_0.activity)

def var_0_0.OnShowFlush(arg_3_0):
	setActive(arg_3_0.dialogTf, True)
	setImageAlpha(arg_3_0.dialogTf, 1)
	setText(arg_3_0.dialogText, not arg_3_0.activity.canPermanentFinish() and arg_3_0.dialog_progress[math.random(#arg_3_0.dialog_progress)] or arg_3_0.dialog_complete[math.random(#arg_3_0.dialog_complete)])
	LeanTween.alpha(arg_3_0.dialogTf, 0, 0.5).setDelay(var_0_0.DIALOG_DELAY).setOnComplete(System.Action(function()
		SetActive(arg_3_0.dialogTf, False)))

def var_0_0.OnHideFlush(arg_5_0):
	LeanTween.cancel(arg_5_0.dialogTf)

def var_0_0.OnFirstFlush(arg_6_0):
	arg_6_0.count = arg_6_0.activity.data3

	setActive(arg_6_0.red, arg_6_0.CheckRed())
	onButton(arg_6_0, arg_6_0.goBtn, function()
		arg_6_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.SECRET_SHIPYARD), SFX_PANEL)

def var_0_0.CheckRed(arg_8_0):
	local var_8_0 = False

	if arg_8_0.activity.readyToAchieve():
		var_8_0 = True

	local var_8_1 = arg_8_0.activity.getNDay()

	if var_8_1 < 8 and PlayerPrefs.GetInt("PiratePage" .. var_8_1, 0) == 0:
		PlayerPrefs.SetInt("PiratePage" .. var_8_1, 1)

		var_8_0 = True

	return var_8_0

def var_0_0.OnUpdateFlush(arg_9_0):
	arg_9_0.count = arg_9_0.activity.data3

	if arg_9_0.progress:
		setText(arg_9_0.progressText, string.format(var_0_0.PROGRESS_TEXT, arg_9_0.count))
		setActive(arg_9_0.progress, not arg_9_0.activity.canPermanentFinish())
		setActive(arg_9_0.complete, arg_9_0.activity.canPermanentFinish())

return var_0_0
