local var_0_0 = class("SixthAnniversaryJPDarkScene", import("view.base.BaseUI"))

var_0_0.STATUS_LOCK = 1
var_0_0.STATUS_FOG = 2
var_0_0.STATUS_STORY = 3
var_0_0.STATUS_NOROMAL = 4
var_0_0.ARROW_ANIM_DELTA = 20
var_0_0.ARROW_ANIM_TIME = 0.5

def var_0_0.getUIName(arg_1_0):
	return "SixthAnniversaryJPDarkUI"

def var_0_0.init(arg_2_0):
	var_0_0.super.init(arg_2_0)

	arg_2_0.top = arg_2_0.findTF("top")
	arg_2_0._bg = arg_2_0.findTF("BG")
	arg_2_0.countText = arg_2_0.findTF("top/Count/Text")

	setText(arg_2_0.findTF("top/Count/explain"), i18n("jp6th_lihoushan_pt1"))

	arg_2_0.levelcontainer = arg_2_0.findTF("upper")
	arg_2_0.player = getProxy(PlayerProxy).getRawData()
	arg_2_0.activityID = ActivityConst.MINIGAME_ZUMA
	arg_2_0.config = pg.activity_template[arg_2_0.activityID]
	arg_2_0.arrowPosYList = {}

	for iter_2_0 = 1, 7:
		local var_2_0 = arg_2_0.findTF(tostring(iter_2_0), arg_2_0.levelcontainer)

		arg_2_0.arrowPosYList[iter_2_0] = arg_2_0.findTF("arrow", var_2_0).localPosition.y

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.findTF("top/Back"), function()
		arg_3_0.onBackPressed(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Home"), function()
		arg_3_0.quickExitFunc(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.jp6th_lihoushan_help.tip
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Shop"), function()
		arg_3_0.emit(SixthAnniversaryJPDarkMediator.GO_SCENE, SCENE.ZUMA_PT_SHOP), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("top/Task"), function()
		arg_3_0.emit(SixthAnniversaryJPDarkMediator.GO_SCENE, SCENE.LAUNCH_BALL_TASK), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("BG/door"), function()
		pg.SceneAnimMgr.GetInstance().SixthAnniversaryJPCoverGoScene(SCENE.SIXTH_ANNIVERSARY_JP), SFX_PANEL)
	arg_3_0.UpdateView()

	local var_3_0 = arg_3_0.config.config_client.lihoushanstory

	pg.NewStoryMgr.GetInstance().Play(var_3_0)

def var_0_0.UpdateView(arg_10_0):
	arg_10_0.UpdateLevels()
	arg_10_0.UpdateCount()
	arg_10_0.UpdateTaskTip()

def var_0_0.UpdateLevels(arg_11_0):
	arg_11_0.unlockCnt = LaunchBallActivityMgr.GetActivityDay(arg_11_0.activityID)
	arg_11_0.finishCnt = LaunchBallActivityMgr.GetRoundCount(arg_11_0.activityID)
	arg_11_0.maxCnt = LaunchBallActivityMgr.GetRoundCountMax(arg_11_0.activityID)
	arg_11_0.curIndex = arg_11_0.finishCnt < arg_11_0.maxCnt and arg_11_0.finishCnt + 1 or -1

	for iter_11_0 = 1, 7:
		local var_11_0 = arg_11_0.findTF(tostring(iter_11_0), arg_11_0.levelcontainer)
		local var_11_1 = arg_11_0.GetLevelStatus(iter_11_0)

		arg_11_0.UpdateLevelByStatus(var_11_0, var_11_1)

	for iter_11_1 = 1, 3:
		local var_11_2 = arg_11_0.findTF("role" .. iter_11_1, arg_11_0.levelcontainer)
		local var_11_3 = LaunchBallActivityMgr.CheckZhuanShuAble(arg_11_0.activityID, iter_11_1)
		local var_11_4 = LaunchBallActivityMgr.IsFinishZhuanShu(arg_11_0.activityID, iter_11_1)

		setActive(var_11_2, var_11_3 and not var_11_4)
		onButton(arg_11_0, var_11_2, function()
			local var_12_0 = arg_11_0.config.config_client.roleStory[iter_11_1]

			pg.NewStoryMgr.GetInstance().Play(var_12_0, function()
				LaunchBallActivityMgr.OpenGame(LaunchBallGameConst.round_type_zhuanshu, iter_11_1)), SFX_PANEL)

	local var_11_5 = arg_11_0.findTF("endless", arg_11_0.levelcontainer)
	local var_11_6 = arg_11_0.finishCnt >= arg_11_0.maxCnt

	setActive(var_11_5, var_11_6)
	onButton(arg_11_0, var_11_5, function()
		LaunchBallActivityMgr.OpenGame(LaunchBallGameConst.round_type_wuxian, 1), SFX_PANEL)

def var_0_0.GetLevelStatus(arg_15_0, arg_15_1):
	local var_15_0 = var_0_0.STATUS_NOROMAL

	if arg_15_1 <= arg_15_0.finishCnt:
		var_15_0 = var_0_0.STATUS_NOROMAL
	elif arg_15_1 == arg_15_0.curIndex:
		if arg_15_1 <= arg_15_0.unlockCnt:
			local var_15_1 = arg_15_0.config.config_client.zumaStory[arg_15_1]

			if pg.NewStoryMgr.GetInstance().IsPlayed(var_15_1):
				var_15_0 = var_0_0.STATUS_NOROMAL
			else
				var_15_0 = var_0_0.STATUS_STORY
		else
			var_15_0 = var_0_0.STATUS_LOCK
	else
		var_15_0 = var_0_0.STATUS_FOG

	return var_15_0

def var_0_0.UpdateLevelByStatus(arg_16_0, arg_16_1, arg_16_2):
	if arg_16_2 == var_0_0.STATUS_LOCK:
		setActive(arg_16_0.findTF("lock", arg_16_1), True)
		setActive(arg_16_0.findTF("title/lock", arg_16_1), True)
		setActive(arg_16_0.findTF("fog", arg_16_1), False)
		setActive(arg_16_0.findTF("tag", arg_16_1), False)
		onButton(arg_16_0, arg_16_1, function()
			pg.TipsMgr.GetInstance().ShowTips(i18n("jp6th_lihoushan_time")), SFX_PANEL)
	elif arg_16_2 == var_0_0.STATUS_FOG:
		setActive(arg_16_0.findTF("lock", arg_16_1), False)
		setActive(arg_16_0.findTF("title/lock", arg_16_1), False)
		setActive(arg_16_0.findTF("fog", arg_16_1), True)
		setActive(arg_16_0.findTF("tag", arg_16_1), False)
		onButton(arg_16_0, arg_16_1, function()
			pg.TipsMgr.GetInstance().ShowTips(i18n("jp6th_lihoushan_order")), SFX_PANEL)
	elif arg_16_2 == var_0_0.STATUS_STORY:
		setActive(arg_16_0.findTF("lock", arg_16_1), False)
		setActive(arg_16_0.findTF("title/lock", arg_16_1), False)
		setActive(arg_16_0.findTF("fog", arg_16_1), False)
		setActive(arg_16_0.findTF("tag", arg_16_1), False)
		onButton(arg_16_0, arg_16_1, function()
			local var_19_0 = arg_16_0.config.config_client.zumaStory[tonumber(arg_16_1.name)]

			pg.NewStoryMgr.GetInstance().Play(var_19_0, function()
				arg_16_0.UpdateLevels()), SFX_PANEL)
	elif arg_16_2 == var_0_0.STATUS_NOROMAL:
		setActive(arg_16_0.findTF("lock", arg_16_1), False)
		setActive(arg_16_0.findTF("title/lock", arg_16_1), False)
		setActive(arg_16_0.findTF("fog", arg_16_1), False)
		setActive(arg_16_0.findTF("tag", arg_16_1), True)
		onButton(arg_16_0, arg_16_1, function()
			LaunchBallActivityMgr.OpenGame(LaunchBallGameConst.round_type_juqing, tonumber(arg_16_1.name)), SFX_PANEL)

	local var_16_0 = arg_16_0.findTF("arrow", arg_16_1)

	LeanTween.cancel(var_16_0.gameObject)

	local var_16_1 = tonumber(arg_16_1.name)

	if var_16_1 == arg_16_0.curIndex:
		setLocalPosition(var_16_0, {
			y = arg_16_0.arrowPosYList[var_16_1]
		})
		setActive(var_16_0, True)
		LeanTween.moveY(var_16_0, arg_16_0.arrowPosYList[var_16_1] + var_0_0.ARROW_ANIM_DELTA, var_0_0.ARROW_ANIM_TIME).setLoopPingPong()
	else
		setActive(var_16_0, False)

def var_0_0.UpdateCount(arg_22_0):
	setText(arg_22_0.countText, LaunchBallActivityMgr.GetRemainCount(arg_22_0.activityID))

def var_0_0.UpdateTaskTip(arg_23_0):
	setActive(arg_23_0.findTF("Task/Tip", arg_23_0.top), LaunchBallTaskMgr.GetRedTip())

def var_0_0.onBackPressed(arg_24_0):
	arg_24_0.emit(SixthAnniversaryJPDarkMediator.GO_SCENE, SCENE.SIXTH_ANNIVERSARY_JP)

return var_0_0
