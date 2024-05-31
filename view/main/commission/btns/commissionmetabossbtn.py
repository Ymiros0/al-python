local var_0_0 = class("CommissionMetaBossBtn")

var_0_0.STATE_LOCK = 1
var_0_0.STATE_NORMAL = 2
var_0_0.STATE_AUTO_BATTLE = 3
var_0_0.STATE_FINSH_BATTLE = 4
var_0_0.STATE_GET_AWARDS = 5

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.event = arg_1_2
	arg_1_0.tr = arg_1_1
	arg_1_0.text = arg_1_0.tr.Find("Text").GetComponent(typeof(Text))
	arg_1_0.tip = arg_1_0.tr.Find("tip")
	arg_1_0.timerIcon = arg_1_0.tr.Find("timer")
	arg_1_0.finishIcon = arg_1_0.tr.Find("finish")

	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	return

def var_0_0.Flush(arg_3_0):
	local var_3_0 = arg_3_0.GetBossState()

	arg_3_0.RemoveTimer()

	arg_3_0.text.text = ""

	if var_0_0.STATE_AUTO_BATTLE == var_3_0:
		arg_3_0.SetLeftTime()

	setActive(arg_3_0.timerIcon, var_0_0.STATE_AUTO_BATTLE == var_3_0)
	setActive(arg_3_0.tip, var_0_0.STATE_GET_AWARDS == var_3_0 or var_0_0.STATE_FINSH_BATTLE == var_3_0)
	setActive(arg_3_0.finishIcon, var_0_0.STATE_FINSH_BATTLE == var_3_0)
	setActive(arg_3_0.tr, var_0_0.STATE_LOCK != var_3_0)
	onButton(arg_3_0, arg_3_0.tr, function()
		if var_3_0 != var_0_0.STATE_LOCK:
			arg_3_0.event.emit(CommissionInfoMediator.GO_META_BOSS), SFX_PANEL)

def var_0_0.SetLeftTime(arg_5_0):
	arg_5_0.RemoveTimer()

	arg_5_0.timer = Timer.New(function()
		local var_6_0 = WorldBossConst.GetAutoBattleLeftTime()

		if var_6_0 <= 0:
			arg_5_0.Flush()

		arg_5_0.text.text = pg.TimeMgr.GetInstance().DescCDTimeForMinute(var_6_0), 1, -1)

	arg_5_0.timer.Start()
	arg_5_0.timer.func()

def var_0_0.RemoveTimer(arg_7_0):
	if arg_7_0.timer:
		arg_7_0.timer.Stop()

		arg_7_0.timer = None

def var_0_0.GetBossState(arg_8_0):
	return WorldBossConst.GetCommissionSceneMetaBossBtnState()

def var_0_0.Dispose(arg_9_0):
	pg.DelegateInfo.Dispose(arg_9_0)
	arg_9_0.RemoveTimer()

return var_0_0
