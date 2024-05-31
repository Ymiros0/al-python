local var_0_0 = class("SailBoatBgControl")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0._followTarget = None
	arg_1_0._backGrounds = {}
	arg_1_0._bgs = {}
	arg_1_0._bgPool = {}
	arg_1_0._bgMoveSpeed = Vector2(0, 0)
	arg_1_0._bgMoveAmount = Vector2(0, 0)

def var_0_0.start(arg_2_0):
	for iter_2_0 = #arg_2_0._bgs, 1, -1:
		local var_2_0 = table.remove(arg_2_0._bgs, iter_2_0)

		var_2_0.clear()
		table.insert(arg_2_0._bgPool, var_2_0)

	arg_2_0._bgMoveAmount = Vector2(0, 0)

	arg_2_0.initBgRound()

	for iter_2_1 = 1, #arg_2_0._bgs:
		arg_2_0._bgs[iter_2_1].start()

	arg_2_0._bgMoveSpeed.x = var_0_1.moveAmount.x
	arg_2_0._bgMoveSpeed.y = var_0_1.moveAmount.y

	var_0_1.SetGameBgs(arg_2_0._bgs)

def var_0_0.step(arg_3_0, arg_3_1):
	local var_3_0 = var_0_1.GetSceneSpeed()

	arg_3_0._bgMoveAmount.x = arg_3_0._bgMoveAmount.x + var_3_0.x
	arg_3_0._bgMoveAmount.y = arg_3_0._bgMoveAmount.y + var_3_0.y

	for iter_3_0 = 1, #arg_3_0._bgs:
		arg_3_0._bgs[iter_3_0].setMoveAmount(arg_3_0._bgMoveAmount)
		arg_3_0._bgs[iter_3_0].step()

def var_0_0.setTarget(arg_4_0, arg_4_1):
	arg_4_0._followTarget = arg_4_1

def var_0_0.setBackGround(arg_5_0, arg_5_1):
	return

def var_0_0.clear(arg_6_0):
	return

def var_0_0.getBgRoundData(arg_7_0, arg_7_1):
	for iter_7_0 = 1, #SailBoatGameConst.game_bg_round:
		local var_7_0 = SailBoatGameConst.game_bg_round[iter_7_0]

		if var_7_0.round == arg_7_1:
			return Clone(var_7_0)

	return None

def var_0_0.initBgRound(arg_8_0):
	local var_8_0 = var_0_1.GetRoundData()

	if not var_8_0:
		return

	for iter_8_0 = 1, #var_8_0.bg_rule:
		local var_8_1 = SailBoatGameConst.bg_rule[var_8_0.bg_rule[iter_8_0]]
		local var_8_2 = arg_8_0.createAndInitBg(var_8_1)

		table.insert(arg_8_0._bgs, var_8_2)

def var_0_0.createAndInitBg(arg_9_0, arg_9_1):
	local var_9_0

	if arg_9_0._bgPool and #arg_9_0._bgPool > 0:
		var_9_0 = table.remove(arg_9_0._bgPool, 1)

	var_9_0 = var_9_0 or SailBoatBg.New(arg_9_0._tf, arg_9_0._event)

	var_9_0.setRuleData(arg_9_1)

	return var_9_0

def var_0_0.useTestBgMove(arg_10_0):
	return

def var_0_0.dispose(arg_11_0):
	return

return var_0_0
