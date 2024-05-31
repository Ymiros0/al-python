ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattleCardPuzzleSkillEffect = class("BattleCardPuzzleSkillEffect")
var_0_0.Battle.BattleCardPuzzleSkillEffect.__name = "BattleCardPuzzleSkillEffect"

local var_0_3 = var_0_0.Battle.BattleCardPuzzleSkillEffect

def var_0_3.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tempData = arg_1_1
	arg_1_0._type = arg_1_0._tempData.type
	arg_1_0._targetChoise = arg_1_0._tempData.target_choise
	arg_1_0._delay = arg_1_0._tempData.arg_list.delay or 0
	arg_1_0._timerList = {}
	arg_1_0._timerIndex = 0

def var_0_3.Execute(arg_2_0, arg_2_1):
	arg_2_0._caster = var_0_0.Battle.BattleTargetChoise.TargetFleetIndex(None, {
		fleetPos = arg_2_0._tempData.caster
	})[1]

	if arg_2_0._delay > 0:
		local var_2_0
		local var_2_1 = arg_2_0._timerIndex + 1

		arg_2_0._timerIndex = var_2_1

		local function var_2_2()
			if arg_2_0._caster and arg_2_0._caster.IsAlive():
				arg_2_0.SkillEffectHandler()

			pg.TimeMgr.GetInstance().RemoveBattleTimer(var_2_0)

			arg_2_0._timerList[var_2_1] = None

		var_2_0 = pg.TimeMgr.GetInstance().AddBattleTimer("BattleSkill", -1, arg_2_0._delay, var_2_2, True)
		arg_2_0._timerList[var_2_1] = var_2_0
	else
		arg_2_0.SkillEffectHandler()

def var_0_3.SkillEffectHandler(arg_4_0, arg_4_1):
	return

def var_0_3.AniEffect(arg_5_0, arg_5_1, arg_5_2):
	local var_5_0 = arg_5_2.GetPosition()
	local var_5_1 = arg_5_1.GetPosition()

	if arg_5_0._casterAniEffect and arg_5_0._casterAniEffect != "":
		local var_5_2 = arg_5_0._casterAniEffect
		local var_5_3

		if var_5_2.posFun:
			function var_5_3(arg_6_0)
				return var_5_2.posFun(var_5_1, var_5_0, arg_6_0)

		local var_5_4 = {
			effect = var_5_2.effect,
			offset = var_5_2.offset,
			posFun = var_5_3
		}

		arg_5_1.DispatchEvent(var_0_0.Event.New(var_0_2.ADD_EFFECT, var_5_4))

	if arg_5_0._targetAniEffect and arg_5_0._targetAniEffect != "":
		local var_5_5 = arg_5_0._targetAniEffect
		local var_5_6

		if var_5_5.posFun:
			function var_5_6(arg_7_0)
				return var_5_5.posFun(var_5_1, var_5_0, arg_7_0)

		local var_5_7 = {
			effect = var_5_5.effect,
			offset = var_5_5.offset,
			posFun = var_5_6
		}

		arg_5_2.DispatchEvent(var_0_0.Event.New(var_0_2.ADD_EFFECT, var_5_7))

def var_0_3.GetTarget(arg_8_0):
	if not arg_8_0._targetChoise:
		return {}

	local var_8_0

	for iter_8_0, iter_8_1 in ipairs(arg_8_0._targetChoise):
		var_8_0 = var_0_0.Battle.BattleTargetChoise[iter_8_1](arg_8_0._caster, arg_8_0._tempData.arg_list, var_8_0)

	return var_8_0

def var_0_3.GetCardPuzzleComponent(arg_9_0):
	return arg_9_0._card.GetClient()

def var_0_3.GetFleetVO(arg_10_0):
	return arg_10_0.GetCardPuzzleComponent().GetFleetVO()

def var_0_3.ConfigCard(arg_11_0, arg_11_1):
	arg_11_0._card = arg_11_1

def var_0_3.SetQueue(arg_12_0, arg_12_1):
	arg_12_0._queue = arg_12_1

def var_0_3.Finale(arg_13_0):
	arg_13_0._queue.EffectFinale(arg_13_0)

def var_0_3.HoldForInput(arg_14_0):
	return False

def var_0_3.MoveCardAfterCast(arg_15_0):
	return var_0_0.Battle.BattleFleetCardPuzzleComponent.CARD_PILE_INDEX_DISCARD

def var_0_3.Interrupt(arg_16_0):
	return

def var_0_3.Clear(arg_17_0):
	for iter_17_0, iter_17_1 in pairs(arg_17_0._timerList):
		pg.TimeMgr.GetInstance().RemoveBattleTimer(iter_17_1)

		arg_17_0._timerList[iter_17_0] = None

	arg_17_0._commander = None
