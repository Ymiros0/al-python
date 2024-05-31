ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBuffEvent
local var_0_2 = var_0_0.Battle.BattleConst.BuffEffectType
local var_0_3 = var_0_0.Battle.BattleCardPuzzleFormulas
local var_0_4 = class("BattleCardPuzzleFleetBuffUnit")

var_0_0.Battle.BattleCardPuzzleFleetBuffUnit = var_0_4
var_0_4.__name = "BattleCardPuzzleFleetBuffUnit"

def var_0_4.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_2 = arg_1_2 or 1
	arg_1_0._id = arg_1_1
	arg_1_0._tempData = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(arg_1_1, arg_1_2)
	arg_1_0._effectList = {}
	arg_1_0._triggerSearchTable = {}
	arg_1_0._level = arg_1_2

	for iter_1_0, iter_1_1 in ipairs(arg_1_0._tempData.effect_list):
		local var_1_0 = var_0_0.Battle[iter_1_1.type].New(iter_1_1)

		arg_1_0._effectList[iter_1_0] = var_1_0

		local var_1_1 = iter_1_1.trigger

		for iter_1_2, iter_1_3 in ipairs(var_1_1):
			local var_1_2 = arg_1_0._triggerSearchTable[iter_1_3]

			if var_1_2 == None:
				var_1_2 = {}
				arg_1_0._triggerSearchTable[iter_1_3] = var_1_2

			var_1_2[#var_1_2 + 1] = var_1_0

	arg_1_0.SetActive()

def var_0_4.IsResponTo(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_0._triggerSearchTable[arg_2_1]

	if var_2_0 != None and #var_2_0 > 0:
		return True

	return False

def var_0_4.SetArgs(arg_3_0, arg_3_1):
	arg_3_0._host = arg_3_1

	for iter_3_0, iter_3_1 in ipairs(arg_3_0._effectList):
		iter_3_1.SetArgs(arg_3_1, arg_3_0)

def var_0_4.setRemoveTime(arg_4_0):
	if arg_4_0._tempData.time == None:
		return

	local var_4_0 = arg_4_0._tempData.time

	if type(var_4_0) == "string":
		arg_4_0._duration = math.max(0, var_0_3.parseFormula(var_4_0, arg_4_0._host.GetAttrManager()))
	else
		arg_4_0._duration = var_4_0

	arg_4_0._expireTimeStamp = pg.TimeMgr.GetInstance().GetCombatTime() + arg_4_0._duration

def var_0_4.Attach(arg_5_0, arg_5_1):
	arg_5_0._stack = 1

	arg_5_0.SetArgs(arg_5_1)
	arg_5_0.onTrigger(var_0_2.ON_ATTACH)
	arg_5_0.setRemoveTime()

def var_0_4.Stack(arg_6_0):
	if arg_6_0._tempData.stack == 0:
		arg_6_0._stack = arg_6_0._stack + 1
	else
		arg_6_0._stack = math.min(arg_6_0._stack + 1, arg_6_0._tempData.stack)

	arg_6_0.onTrigger(var_0_2.ON_STACK)
	arg_6_0.setRemoveTime()

def var_0_4.InitStack(arg_7_0):
	return

def var_0_4.UpdateStack(arg_8_0, arg_8_1):
	return

def var_0_4.Remove(arg_9_0):
	arg_9_0.onTrigger(var_0_2.ON_REMOVE)

	arg_9_0._host.GetBuffManager().GetCardPuzzleBuffList()[arg_9_0._id] = None

	arg_9_0.Clear()

def var_0_4.Update(arg_10_0, arg_10_1):
	if arg_10_0.IsExpire(arg_10_1):
		arg_10_0.Remove()
	else
		arg_10_0.onTrigger(var_0_2.ON_UPDATE, arg_10_1)

def var_0_4.onTrigger(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0._triggerSearchTable[arg_11_1]

	if var_11_0 == None or #var_11_0 == 0:
		return

	for iter_11_0, iter_11_1 in ipairs(var_11_0):
		assert(type(iter_11_1[arg_11_1]) == "function", "fleet buff效果的触发函数缺失,buff id.>>" .. arg_11_0._id .. "<<, trigger.>>" .. arg_11_1 .. "<<")

		if iter_11_1.IsActive():
			iter_11_1.NotActive()
			iter_11_1.Trigger(arg_11_1, arg_11_2)
			iter_11_1.SetActive()

def var_0_4.IsExpire(arg_12_0, arg_12_1):
	if arg_12_0._expireTimeStamp == None:
		return False
	else
		return arg_12_1 >= arg_12_0._expireTimeStamp

def var_0_4.IsActive(arg_13_0):
	return arg_13_0._isActive

def var_0_4.SetActive(arg_14_0):
	arg_14_0._isActive = True

def var_0_4.NotActive(arg_15_0):
	arg_15_0._isActive = False

def var_0_4.GetCaster(arg_16_0):
	return None

def var_0_4.GetID(arg_17_0):
	return arg_17_0._id

def var_0_4.GetStack(arg_18_0):
	return arg_18_0._stack

def var_0_4.GetLv(arg_19_0):
	return 1

def var_0_4.GetDurationRate(arg_20_0):
	if arg_20_0._expireTimeStamp == None:
		return 1
	else
		local var_20_0 = pg.TimeMgr.GetInstance().GetCombatTime()

		return (arg_20_0._expireTimeStamp - var_20_0) / arg_20_0._duration

def var_0_4.Clear(arg_21_0):
	arg_21_0._host = None

	for iter_21_0, iter_21_1 in ipairs(arg_21_0._effectList):
		iter_21_1.Clear()
