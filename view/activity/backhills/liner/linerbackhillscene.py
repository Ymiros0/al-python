local var_0_0 = class("LinerBackHillScene", import("..TemplateMV.BackHillTemplate"))

var_0_0.optionsPath = {
	"top/btn_home"
}
var_0_0.ACT_ID = ActivityConst.LINER_ID
var_0_0.MINIGAME_ID = 65
var_0_0.TASK_ACT_ID = ActivityConst.LINER_SIGN_ID
var_0_0.NAME_ID = ActivityConst.LINER_NAMED_ID

def var_0_0.getUIName(arg_1_0):
	return "LinerBackHillUI"

def var_0_0.getBGM(arg_2_0):
	return arg_2_0.activity.getConfig("config_client").backHillBgm[var_0_0.IsDay() and "day" or "night"]

def var_0_0.IsDay():
	local var_3_0 = pg.TimeMgr.GetInstance().GetServerHour()
	local var_3_1 = getProxy(ActivityProxy).getActivityById(var_0_0.ACT_ID)

	assert(var_3_1 and not var_3_1.isEnd(), "not exist liner act, type. " .. var_0_0.ACT_ID)

	local var_3_2 = var_3_1.getConfig("config_client").time

	return var_3_0 >= var_3_2[1] and var_3_0 < var_3_2[2]

def var_0_0.init(arg_4_0):
	arg_4_0._dayTF = arg_4_0.findTF("day")
	arg_4_0._nightTF = arg_4_0.findTF("night")

	for iter_4_0 = 0, arg_4_0._dayTF.childCount - 1:
		local var_4_0 = arg_4_0._dayTF.GetChild(iter_4_0)
		local var_4_1 = go(var_4_0).name

		arg_4_0["day_" .. var_4_1] = var_4_0

	for iter_4_1 = 0, arg_4_0._nightTF.childCount - 1:
		local var_4_2 = arg_4_0._nightTF.GetChild(iter_4_1)
		local var_4_3 = go(var_4_2).name

		arg_4_0["night_" .. var_4_3] = var_4_2

	arg_4_0._map = arg_4_0._dayTF
	arg_4_0._upper = arg_4_0._nightTF
	arg_4_0._log_tip = arg_4_0.findTF("top/btn_log/tip")
	arg_4_0._unlock = arg_4_0.findTF("top/unlock_info")
	arg_4_0.activity = getProxy(ActivityProxy).getActivityById(var_0_0.ACT_ID)
	arg_4_0.timeMgr = pg.TimeMgr.GetInstance()

def var_0_0.didEnter(arg_5_0):
	onButton(arg_5_0, arg_5_0.findTF("top/btn_back"), function()
		arg_5_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_5_0, arg_5_0.findTF("top/btn_help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip["7th_main_tip"].tip
		}), SFX_PANEL)
	arg_5_0.BindItemSkinShop()
	arg_5_0.BindItemBuildShip()
	arg_5_0.InitFacilityCross(arg_5_0._dayTF, arg_5_0._nightTF, "btn_game", function()
		arg_5_0.emit(LinerBackHillMediator.GO_MINIGAME, var_0_0.MINIGAME_ID))
	arg_5_0.InitFacilityCross(arg_5_0._dayTF, arg_5_0._nightTF, "btn_cruise", function()
		arg_5_0.emit(LinerBackHillMediator.GO_SCENE, SCENE.LINER)
		PlayerPrefs.SetString("LinerBackHillScene", var_0_0.GetDate()))
	arg_5_0.InitFacilityCross(arg_5_0._dayTF, arg_5_0._nightTF, "btn_task", function()
		arg_5_0.emit(LinerBackHillMediator.GO_SCENE, SCENE.ACTIVITY, {
			id = var_0_0.TASK_ACT_ID
		}))

	local var_5_0 = getProxy(ActivityProxy).getActivityById(var_0_0.TASK_ACT_ID).getConfig("config_client").preStory
	local var_5_1 = not pg.NewStoryMgr.GetInstance().IsPlayed(var_5_0)

	onButton(arg_5_0, arg_5_0.findTF("top/btn_log"), function()
		if var_5_1:
			pg.TipsMgr.GetInstance().ShowTips(i18n("liner_activity_lock"))
		else
			arg_5_0.emit(LinerBackHillMediator.GO_SUBLAYER, Context.New({
				mediator = LinerLogBookMediator,
				viewComponent = LinerLogBookLayer
			})), SFX_PANEL)
	setActive(arg_5_0.day_btn_task, var_5_1)
	setActive(arg_5_0.night_btn_task, var_5_1)
	setActive(arg_5_0._unlock, var_5_1)
	setActive(arg_5_0.day_btn_cruise, not var_5_1)
	setActive(arg_5_0.night_btn_cruise, not var_5_1)
	setActive(arg_5_0._dayTF, var_0_0.IsDay())
	setActive(arg_5_0._nightTF, not var_0_0.IsDay())
	arg_5_0.UpdateView()

def var_0_0.UpdateView(arg_12_0):
	setActive(arg_12_0._log_tip, var_0_0.LogTip())
	setActive(arg_12_0.findTF("tip", arg_12_0.day_btn_game), var_0_0.MiniGameTip())
	setActive(arg_12_0.findTF("tip", arg_12_0.night_btn_game), var_0_0.MiniGameTip())
	setActive(arg_12_0.findTF("tip", arg_12_0.day_btn_cruise), var_0_0.CruiseTip())
	setActive(arg_12_0.findTF("tip", arg_12_0.night_btn_cruise), var_0_0.CruiseTip())

def var_0_0.GetDate():
	return pg.TimeMgr.GetInstance().STimeDescC(pg.TimeMgr.GetInstance().GetServerTime(), "%Y/%m/%d")

def var_0_0.LogTip():
	return LinerLogBookLayer.IsTip()

def var_0_0.MiniGameTip():
	return getProxy(MiniGameProxy).GetHubByGameId(var_0_0.MINIGAME_ID).count > 0

def var_0_0.CruiseTip():
	local var_16_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_LINER).IsFinishAllTime()
	local var_16_1 = PlayerPrefs.GetString("LinerBackHillScene") == var_0_0.GetDate()

	return not var_16_0 and not var_16_1

def var_0_0.IsShowMainTip(arg_17_0):
	if arg_17_0 and not arg_17_0.isEnd():
		return var_0_0.LogTip() or var_0_0.MiniGameTip() or var_0_0.CruiseTip()

def var_0_0.willExit(arg_18_0):
	return

return var_0_0
