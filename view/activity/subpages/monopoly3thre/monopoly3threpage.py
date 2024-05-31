local var_0_0 = class("Monopoly3thRePage", import("....base.BaseActivityPage"))

var_0_0.ON_START = "MonopolyGame.ON_START"
var_0_0.ON_MOVE = "MonopolyGame.ON_MOVE"
var_0_0.ON_TRIGGER = "MonopolyGame.ON_TRIGGER"
var_0_0.ON_AWARD = "MonopolyGame.ON_AWARD"
var_0_0.MONOPOLY_OP_LAST = "MonopolyGame.MONOPOLY_OP_LAST"
var_0_0.ON_STOP = "MonopolyGame.MONOPOLY_ON_STOP"
var_0_0.AWARDS = {}

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bind(Monopoly3thRePage.ON_STOP, function(arg_2_0, arg_2_1, arg_2_2)
		if not arg_1_0.gameUI.autoFlag and #Monopoly3thRePage.AWARDS > 0:
			arg_1_0.emit(BaseUI.ON_ACHIEVE, Monopoly3thRePage.AWARDS, arg_2_2)

			Monopoly3thRePage.AWARDS = {})
	arg_1_0.bind(Monopoly3thRePage.MONOPOLY_OP_LAST, function(arg_3_0, arg_3_1, arg_3_2)
		pg.m02.sendNotification(GAME.MONOPOLY_OP, {
			activity_id = arg_3_1,
			cmd = ActivityConst.MONOPOLY_OP_LAST,
			callback = arg_3_2
		}))
	arg_1_0.bind(Monopoly3thRePage.ON_START, function(arg_4_0, arg_4_1, arg_4_2)
		pg.m02.sendNotification(GAME.MONOPOLY_OP, {
			activity_id = arg_4_1,
			cmd = ActivityConst.MONOPOLY_OP_THROW,
			callback = arg_4_2
		}))
	arg_1_0.bind(Monopoly3thRePage.ON_MOVE, function(arg_5_0, arg_5_1, arg_5_2)
		pg.m02.sendNotification(GAME.MONOPOLY_OP, {
			activity_id = arg_5_1,
			cmd = ActivityConst.MONOPOLY_OP_MOVE,
			callback = arg_5_2
		}))
	arg_1_0.bind(Monopoly3thRePage.ON_TRIGGER, function(arg_6_0, arg_6_1, arg_6_2)
		pg.m02.sendNotification(GAME.MONOPOLY_OP, {
			activity_id = arg_6_1,
			cmd = ActivityConst.MONOPOLY_OP_TRIGGER,
			callback = arg_6_2
		}))
	arg_1_0.bind(Monopoly3thRePage.ON_AWARD, function(arg_7_0)
		arg_1_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.REDPACKEY))

def var_0_0.getLeftRpCount():
	local var_8_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_MONOPOLY)
	local var_8_1 = var_8_0.data2_list[2]

	return var_8_0.data2_list[1] - var_8_1

def var_0_0.onAward(arg_9_0, arg_9_1, arg_9_2):
	for iter_9_0 = 1, #arg_9_1:
		table.insert(Monopoly3thRePage.AWARDS, arg_9_1[iter_9_0])

	if arg_9_0.gameUI.autoFlag:
		arg_9_0.gameUI.addAwards(arg_9_1)

		if arg_9_2:
			arg_9_2()
	else
		arg_9_0.emit(BaseUI.ON_ACHIEVE, Monopoly3thRePage.AWARDS, arg_9_2)

		Monopoly3thRePage.AWARDS = {}

def var_0_0.OnUpdateFlush(arg_10_0):
	arg_10_0.updateGameUI()

def var_0_0.updateGameUI(arg_11_0):
	if not arg_11_0.activity:
		return

	if arg_11_0.gameUI:
		arg_11_0.gameUI.updataActivity(arg_11_0.activity)
	else
		arg_11_0.gameUI = Monopoly3thReGame.New(arg_11_0, findTF(arg_11_0._tf, "AD"), arg_11_0.event, 4)

		arg_11_0.gameUI.firstUpdata(arg_11_0.activity)

		if not arg_11_0.gameUI.autoFlag and #Monopoly3thRePage.AWARDS > 0:
			arg_11_0.emit(BaseUI.ON_ACHIEVE, Monopoly3thRePage.AWARDS, function()
				return)

			Monopoly3thRePage.AWARDS = {}

def var_0_0.OnDestroy(arg_13_0):
	if arg_13_0.gameUI:
		Monopoly3thRePage.AWARDS = {}

		arg_13_0.gameUI.dispose()

		arg_13_0.gameUI = None

def var_0_0.OnHideFlush(arg_14_0):
	if arg_14_0.gameUI:
		Monopoly3thRePage.AWARDS = {}

		arg_14_0.gameUI.dispose()

		arg_14_0.gameUI = None

return var_0_0
