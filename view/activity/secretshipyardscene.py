local var_0_0 = class("SecretShipyardScene", import("..base.BaseUI"))

var_0_0.optionsPath = {
	"main/top/btn_home"
}
var_0_0.ACT_ID = 5023
var_0_0.GAME_ID = 59
var_0_0.ANIMATIONS = {
	"Phase_00",
	"Phase_01",
	"Phase_02",
	"Phase_03",
	"Phase_04",
	"Phase_05",
	"Phase_06",
	"Phase_07"
}
var_0_0.EFFECT_DELAY = 2
var_0_0.ANIMATION_DELAY = 1
var_0_0.STORY_DELAY = 3

def var_0_0.getUIName(arg_1_0):
	return "SecretShipyardUI"

def var_0_0.init(arg_2_0):
	arg_2_0.activity = getProxy(ActivityProxy).getActivityById(var_0_0.ACT_ID)
	arg_2_0.count = 0
	arg_2_0.bgId = 1
	arg_2_0.taskProxy = getProxy(TaskProxy)
	arg_2_0.taskGroup = arg_2_0.activity.getConfig("config_data")
	arg_2_0.main = arg_2_0.findTF("main")
	arg_2_0.bottom = arg_2_0.findTF("bottom", arg_2_0.main)
	arg_2_0.gameButton = arg_2_0.findTF("btn_go_game", arg_2_0.bottom)
	arg_2_0.gameButtonLock = arg_2_0.findTF("btn_go_game_lock", arg_2_0.gameButton)
	arg_2_0.items = arg_2_0.findTF("items", arg_2_0.bottom)
	arg_2_0.item = arg_2_0.findTF("item", arg_2_0.bottom)
	arg_2_0.dayText = arg_2_0.findTF("day/nday", arg_2_0.bottom)
	arg_2_0.description = arg_2_0.findTF("description/Text", arg_2_0.bottom)
	arg_2_0.top = arg_2_0.findTF("top", arg_2_0.main)
	arg_2_0.buttonBack = arg_2_0.findTF("btn_back", arg_2_0.top)
	arg_2_0.buttonHelp = arg_2_0.findTF("btn_help", arg_2_0.top)
	arg_2_0.uilist = UIItemList.New(arg_2_0.items, arg_2_0.item)
	arg_2_0.bg = arg_2_0.findTF("bg")
	arg_2_0.animator = arg_2_0.findTF("anim", arg_2_0.bg).GetComponent(typeof(Animator))
	arg_2_0.effect = arg_2_0.findTF("effect", arg_2_0.bg)

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.buttonBack, function()
		arg_3_0.closeView(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.buttonHelp, function()
		local var_5_0 = i18n("shipyard_phase_1" or "shipyard_phase_2")

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = var_5_0
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.gameButton, function()
		arg_3_0.emit(SecretShipyardMediator.GO_MINI_GAME, var_0_0.GAME_ID), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.gameButtonLock, function()
		pg.TipsMgr.GetInstance().ShowTips(i18n(arg_3_0.checkTaskFinish() and "shipyard_button_1" or "shipyard_button_2")), SFX_PANEL)
	arg_3_0.uilist.make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate:
			arg_3_0.UpdateTask(arg_8_1, arg_8_2))
	setText(arg_3_0.description, i18n("shipyard_introduce"))
	setActive(arg_3_0.effect, False)
	setActive(arg_3_0.buttonHelp, arg_3_0.checkMinigame())

	arg_3_0.count = arg_3_0.activity.data3
	arg_3_0.bgId = arg_3_0.CheckBgId()

	arg_3_0.animator.Play(var_0_0.ANIMATIONS[arg_3_0.bgId])
	arg_3_0.OnUpdateFlush()

	local var_3_0 = arg_3_0.activity.getConfig("config_client").firstStory

	if var_3_0:
		playStory(var_3_0)

	arg_3_0.PlayStory()

def var_0_0.UpdateTask(arg_9_0, arg_9_1, arg_9_2):
	local var_9_0 = arg_9_1 + 1
	local var_9_1 = arg_9_0.findTF("item", arg_9_2)
	local var_9_2 = arg_9_0.taskGroup[arg_9_0.count][var_9_0]
	local var_9_3 = arg_9_0.taskProxy.getTaskById(var_9_2) or arg_9_0.taskProxy.getFinishTaskById(var_9_2)

	assert(var_9_3, "without this task by id. " .. var_9_2)

	local var_9_4 = var_9_3.getConfig("award_display")[1]
	local var_9_5 = {
		type = var_9_4[1],
		id = var_9_4[2],
		count = var_9_4[3]
	}

	updateDrop(var_9_1, var_9_5)
	onButton(arg_9_0, var_9_1, function()
		warning("click")
		arg_9_0.emit(BaseUI.ON_DROP, var_9_5), SFX_PANEL)

	local var_9_6 = var_9_3.getProgress()
	local var_9_7 = var_9_3.getConfig("target_num")

	setText(arg_9_0.findTF("description", arg_9_2), var_9_3.getConfig("desc"))

	local var_9_8 = var_9_6
	local var_9_9 = "/" .. var_9_7

	setText(arg_9_0.findTF("progress_text", arg_9_2), var_9_8 .. var_9_9)
	setSlider(arg_9_0.findTF("progress", arg_9_2), 0, var_9_7, var_9_6)

	local var_9_10 = arg_9_0.findTF("go_btn", arg_9_2)
	local var_9_11 = arg_9_0.findTF("get_btn", arg_9_2)
	local var_9_12 = arg_9_0.findTF("got_btn", arg_9_2)
	local var_9_13 = var_9_3.getTaskStatus()

	setActive(var_9_10, var_9_13 == 0)
	setActive(var_9_11, var_9_13 == 1)
	setActive(var_9_12, var_9_13 == 2)
	onButton(arg_9_0, var_9_10, function()
		arg_9_0.emit(SecretShipyardMediator.TASK_GO, var_9_3), SFX_PANEL)
	onButton(arg_9_0, var_9_11, function()
		arg_9_0.emit(SecretShipyardMediator.SUBMIT_TASK, var_9_3.id), SFX_PANEL)
	setActive(arg_9_0.findTF("mask", arg_9_2), arg_9_0.taskProxy.getFinishTaskById(var_9_2) != None)

def var_0_0.updateTaskLayers(arg_13_0):
	updateActivityTaskStatus(arg_13_0.activity)

	arg_13_0.activity = getProxy(ActivityProxy).getActivityById(var_0_0.ACT_ID)

	arg_13_0.OnUpdateFlush()

def var_0_0.CheckBgId(arg_14_0):
	local var_14_0 = arg_14_0.activity.data3

	if arg_14_0.taskProxy.getFinishTaskById(arg_14_0.taskGroup[arg_14_0.count][1]) != None and arg_14_0.taskProxy.getFinishTaskById(arg_14_0.taskGroup[arg_14_0.count][2]) != None:
		var_14_0 = var_14_0 + 1

	return var_14_0

def var_0_0.OnUpdateFlush(arg_15_0):
	arg_15_0.count = arg_15_0.activity.data3

	if arg_15_0.bgId != arg_15_0.CheckBgId():
		arg_15_0.bgId = arg_15_0.CheckBgId()

		arg_15_0.ChangeBackground()

	if arg_15_0.dayText:
		setText(arg_15_0.dayText, tostring(arg_15_0.count))

	setActive(arg_15_0.gameButtonLock, not arg_15_0.checkTaskFinish() or not arg_15_0.checkMinigame())
	setActive(arg_15_0.gameButton, arg_15_0.checkTaskFinish() or arg_15_0.checkMinigame())
	arg_15_0.uilist.align(#arg_15_0.taskGroup[arg_15_0.count])

def var_0_0.ChangeBackground(arg_16_0):
	LeanTween.cancel(go(arg_16_0._tf))
	setActive(arg_16_0.effect, True)
	LeanTween.delayedCall(go(arg_16_0._tf), var_0_0.ANIMATION_DELAY, System.Action(function()
		arg_16_0.animator.Play(var_0_0.ANIMATIONS[arg_16_0.bgId])))
	LeanTween.delayedCall(go(arg_16_0._tf), var_0_0.EFFECT_DELAY, System.Action(function()
		setActive(arg_16_0.effect, False)))
	LeanTween.delayedCall(go(arg_16_0._tf), var_0_0.STORY_DELAY, System.Action(function()
		arg_16_0.PlayStory()))

def var_0_0.PlayStory(arg_20_0):
	local var_20_0 = arg_20_0.activity.getConfig("config_client").story

	if checkExist(var_20_0, {
		arg_20_0.bgId - 1
	}, {
		1
	}):
		playStory(var_20_0[arg_20_0.bgId - 1][1])

def var_0_0.checkTaskFinish(arg_21_0):
	if arg_21_0.count < #arg_21_0.taskGroup:
		return False

	for iter_21_0, iter_21_1 in ipairs(arg_21_0.taskGroup[arg_21_0.count]):
		if not arg_21_0.taskProxy.getFinishTaskById(iter_21_1):
			return False

	return True

def var_0_0.checkMinigame(arg_22_0):
	return pg.mini_game[var_0_0.GAME_ID] != None

def var_0_0.willExit(arg_23_0):
	LeanTween.cancel(go(arg_23_0._tf))

return var_0_0
