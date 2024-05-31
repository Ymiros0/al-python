ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleFormulas
local var_0_2 = var_0_0.Battle.BattleUnitEvent

var_0_0.Battle.BattleSkillEffect = class("BattleSkillEffect")
var_0_0.Battle.BattleSkillEffect.__name = "BattleSkillEffect"

local var_0_3 = var_0_0.Battle.BattleSkillEffect

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._tempData = arg_1_1
	arg_1_0._type = arg_1_0._tempData.type
	arg_1_0._targetChoise = arg_1_0._tempData.target_choise or "TargetNull"
	arg_1_0._casterAniEffect = arg_1_0._tempData.casterAniEffect
	arg_1_0._targetAniEffect = arg_1_0._tempData.targetAniEffect
	arg_1_0._delay = arg_1_0._tempData.arg_list.delay or 0
	arg_1_0._lastEffectTarget = {}
	arg_1_0._timerList = {}
	arg_1_0._timerIndex = 0
	arg_1_0._level = arg_1_2

def var_0_3.SetCommander(arg_2_0, arg_2_1):
	arg_2_0._commander = arg_2_1

def var_0_3.Effect(arg_3_0, arg_3_1, arg_3_2, arg_3_3):
	if arg_3_2 and #arg_3_2 > 0:
		for iter_3_0, iter_3_1 in ipairs(arg_3_2):
			arg_3_0.AniEffect(arg_3_1, iter_3_1)
			arg_3_0.DataEffect(arg_3_1, iter_3_1, arg_3_3)
	else
		arg_3_0.DataEffectWithoutTarget(arg_3_1, arg_3_3)

def var_0_3.IsFinaleEffect(arg_4_0):
	return False

def var_0_3.SetFinaleCallback(arg_5_0, arg_5_1):
	arg_5_0._finaleCallback = arg_5_1

def var_0_3.AniEffect(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = arg_6_2.GetPosition()
	local var_6_1 = arg_6_1.GetPosition()

	if arg_6_0._casterAniEffect and arg_6_0._casterAniEffect != "":
		local var_6_2 = arg_6_0._casterAniEffect
		local var_6_3

		if var_6_2.posFun:
			function var_6_3(arg_7_0)
				return var_6_2.posFun(var_6_1, var_6_0, arg_7_0)

		local var_6_4 = {
			effect = var_6_2.effect,
			offset = var_6_2.offset,
			posFun = var_6_3
		}

		arg_6_1.DispatchEvent(var_0_0.Event.New(var_0_2.ADD_EFFECT, var_6_4))

	if arg_6_0._targetAniEffect and arg_6_0._targetAniEffect != "":
		local var_6_5 = arg_6_0._targetAniEffect
		local var_6_6

		if var_6_5.posFun:
			function var_6_6(arg_8_0)
				return var_6_5.posFun(var_6_1, var_6_0, arg_8_0)

		local var_6_7 = {
			effect = var_6_5.effect,
			offset = var_6_5.offset,
			posFun = var_6_6
		}

		arg_6_2.DispatchEvent(var_0_0.Event.New(var_0_2.ADD_EFFECT, var_6_7))

def var_0_3.DataEffect(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	if arg_9_0._delay > 0:
		local var_9_0
		local var_9_1 = arg_9_0._timerIndex + 1

		arg_9_0._timerIndex = var_9_1

		local function var_9_2()
			if arg_9_1 and arg_9_1.IsAlive():
				arg_9_0.DoDataEffect(arg_9_1, arg_9_2, arg_9_3)

			pg.TimeMgr.GetInstance().RemoveBattleTimer(var_9_0)

			arg_9_0._timerList[var_9_1] = None

		var_9_0 = pg.TimeMgr.GetInstance().AddBattleTimer("BattleSkill", -1, arg_9_0._delay, var_9_2, True)
		arg_9_0._timerList[var_9_1] = var_9_0
	else
		arg_9_0.DoDataEffect(arg_9_1, arg_9_2, arg_9_3)

def var_0_3.DoDataEffect(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	return

def var_0_3.DataEffectWithoutTarget(arg_12_0, arg_12_1, arg_12_2):
	if arg_12_0._delay > 0:
		local var_12_0
		local var_12_1 = arg_12_0._timerIndex + 1

		arg_12_0._timerIndex = var_12_1

		local function var_12_2()
			if arg_12_1 and arg_12_1.IsAlive():
				arg_12_0.DoDataEffectWithoutTarget(arg_12_1, arg_12_2)

			pg.TimeMgr.GetInstance().RemoveBattleTimer(var_12_0)

			arg_12_0._timerList[var_12_1] = None

		var_12_0 = pg.TimeMgr.GetInstance().AddBattleTimer("BattleSkill", -1, arg_12_0._delay, var_12_2, True)
		arg_12_0._timerList[var_12_1] = var_12_0
	else
		arg_12_0.DoDataEffectWithoutTarget(arg_12_1, arg_12_2)

def var_0_3.DoDataEffectWithoutTarget(arg_14_0, arg_14_1, arg_14_2):
	return

def var_0_3.GetTarget(arg_15_0, arg_15_1, arg_15_2):
	if type(arg_15_0._targetChoise) == "string":
		if arg_15_0._targetChoise == "TargetSameToLastEffect":
			return arg_15_2._lastEffectTarget
		else
			return var_0_0.Battle.BattleTargetChoise[arg_15_0._targetChoise](arg_15_1, arg_15_0._tempData.arg_list)
	elif type(arg_15_0._targetChoise) == "table":
		local var_15_0

		for iter_15_0, iter_15_1 in ipairs(arg_15_0._targetChoise):
			var_15_0 = var_0_0.Battle.BattleTargetChoise[iter_15_1](arg_15_1, arg_15_0._tempData.arg_list, var_15_0)

		return var_15_0

def var_0_3.Interrupt(arg_16_0):
	return

def var_0_3.Clear(arg_17_0):
	for iter_17_0, iter_17_1 in pairs(arg_17_0._timerList):
		pg.TimeMgr.GetInstance().RemoveBattleTimer(iter_17_1)

		arg_17_0._timerList[iter_17_0] = None

	arg_17_0._commander = None

def var_0_3.calcCorrdinate(arg_18_0, arg_18_1, arg_18_2):
	local var_18_0

	if arg_18_0.absoulteCorrdinate:
		var_18_0 = Vector3(arg_18_0.absoulteCorrdinate.x, 0, arg_18_0.absoulteCorrdinate.z)
	elif arg_18_0.absoulteRandom:
		var_18_0 = var_0_1.RandomPos(arg_18_0.absoulteRandom)
	elif arg_18_0.casterRelativeCorrdinate:
		local var_18_1 = arg_18_1.GetIFF()
		local var_18_2 = arg_18_1.GetPosition()
		local var_18_3 = var_18_1 * arg_18_0.casterRelativeCorrdinate.hrz + var_18_2.x
		local var_18_4 = var_18_1 * arg_18_0.casterRelativeCorrdinate.vrt + var_18_2.z

		var_18_0 = Vector3(var_18_3, 0, var_18_4)
	elif arg_18_0.casterRelativeRandom:
		local var_18_5 = arg_18_1.GetIFF()
		local var_18_6 = arg_18_1.GetPosition()
		local var_18_7 = {
			X1 = var_18_5 * arg_18_0.casterRelativeRandom.front + var_18_6.x,
			X2 = var_18_5 * arg_18_0.casterRelativeRandom.rear + var_18_6.x,
			Z1 = arg_18_0.casterRelativeRandom.upper + var_18_6.z,
			Z2 = arg_18_0.casterRelativeRandom.lower + var_18_6.z
		}

		var_18_0 = var_0_1.RandomPos(var_18_7)
	elif arg_18_0.targetRelativeCorrdinate:
		if arg_18_2:
			local var_18_8 = arg_18_2.GetIFF()
			local var_18_9 = arg_18_2.GetPosition()
			local var_18_10 = var_18_8 * arg_18_0.targetRelativeCorrdinate.hrz + var_18_9.x
			local var_18_11 = var_18_8 * arg_18_0.targetRelativeCorrdinate.vrt + var_18_9.z

			var_18_0 = Vector3(var_18_10, 0, var_18_11)
	elif arg_18_0.targetRelativeRandom and arg_18_2:
		local var_18_12 = arg_18_2.GetIFF()
		local var_18_13 = arg_18_2.GetPosition()
		local var_18_14 = {
			X1 = var_18_12 * arg_18_0.targetRelativeRandom.front + var_18_13.x,
			X2 = var_18_12 * arg_18_0.targetRelativeRandom.rear + var_18_13.x,
			Z1 = arg_18_0.targetRelativeRandom.upper + var_18_13.z,
			Z2 = arg_18_0.targetRelativeRandom.lower + var_18_13.z
		}

		var_18_0 = var_0_1.RandomPos(var_18_14)

	return var_18_0

def var_0_3.GetDamageSum(arg_19_0):
	return 0
