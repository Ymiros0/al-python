ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleBuffEvent
local var_0_2 = var_0_0.Battle.BattleConst.BuffEffectType
local var_0_3 = class("BattleBuffUnit")

var_0_0.Battle.BattleBuffUnit = var_0_3
var_0_3.__name = "BattleBuffUnit"
var_0_3.DEFAULT_ANI_FX_CONFIG = {
	effect = "jineng",
	offset = {
		0,
		-2,
		0
	}
}

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_2 = arg_1_2 or 1
	arg_1_0._id = arg_1_1

	arg_1_0.SetTemplate(arg_1_1, arg_1_2)

	arg_1_0._time = arg_1_0._tempData.time
	arg_1_0._RemoveTime = 0
	arg_1_0._effectList = {}
	arg_1_0._triggerSearchTable = {}
	arg_1_0._level = arg_1_2
	arg_1_0._caster = arg_1_3

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

def var_0_3.SetTemplate(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._tempData = var_0_0.Battle.BattleDataFunction.GetBuffTemplate(arg_2_1, arg_2_2)

def var_0_3.Attach(arg_3_0, arg_3_1):
	arg_3_0._owner = arg_3_1
	arg_3_0._stack = 1

	arg_3_0.SetArgs(arg_3_1)
	arg_3_0.onTrigger(var_0_2.ON_ATTACH, arg_3_1)
	arg_3_0.SetRemoveTime()

def var_0_3.Stack(arg_4_0, arg_4_1):
	arg_4_0._stack = math.min(arg_4_0._stack + 1, arg_4_0._tempData.stack)

	arg_4_0.onTrigger(var_0_2.ON_STACK, arg_4_1)
	arg_4_0.SetRemoveTime()

def var_0_3.SetOrb(arg_5_0, arg_5_1, arg_5_2):
	for iter_5_0, iter_5_1 in ipairs(arg_5_0._effectList):
		iter_5_1.SetOrb(arg_5_0, arg_5_1, arg_5_2)

def var_0_3.SetOrbDuration(arg_6_0, arg_6_1):
	arg_6_0._time = arg_6_1 + arg_6_0._time

def var_0_3.SetOrbLevel(arg_7_0, arg_7_1):
	arg_7_0._level = arg_7_1

def var_0_3.SetCommander(arg_8_0, arg_8_1):
	arg_8_0._commander = arg_8_1

	for iter_8_0, iter_8_1 in ipairs(arg_8_0._effectList):
		iter_8_1.SetCommander(arg_8_1)

def var_0_3.GetEffectList(arg_9_0):
	return arg_9_0._effectList

def var_0_3.GetCommander(arg_10_0):
	return arg_10_0._commander

def var_0_3.UpdateStack(arg_11_0, arg_11_1, arg_11_2):
	if arg_11_0._stack == arg_11_2:
		return

	arg_11_0._stack = math.min(arg_11_2, arg_11_0._tempData.stack)

	arg_11_0.onTrigger(var_0_2.ON_STACK, arg_11_1)
	arg_11_0.SetRemoveTime()

	local var_11_0 = {
		unit_id = arg_11_1.GetUniqueID(),
		buff_id = arg_11_0._id,
		stack_count = arg_11_0._stack
	}

	arg_11_1.DispatchEvent(var_0_0.Event.New(var_0_1.BUFF_STACK, var_11_0))

def var_0_3.Remove(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_0._owner
	local var_12_1 = arg_12_0._id
	local var_12_2 = {
		unit_id = var_12_0.GetUniqueID(),
		buff_id = var_12_1
	}

	var_12_0.DispatchEvent(var_0_0.Event.New(var_0_1.BUFF_REMOVE, var_12_2))
	arg_12_0.onTrigger(var_0_2.ON_REMOVE, var_12_0)
	arg_12_0.Clear()

	var_12_0.GetBuffList()[var_12_1] = None

def var_0_3.Update(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_0.IsTimeToRemove(arg_13_2):
		arg_13_0.Remove(arg_13_2)
	else
		arg_13_0.onTrigger(var_0_2.ON_UPDATE, arg_13_1, {
			timeStamp = arg_13_2
		})

def var_0_3.SetArgs(arg_14_0, arg_14_1):
	for iter_14_0, iter_14_1 in ipairs(arg_14_0._effectList):
		iter_14_1.SetCaster(arg_14_0._caster)
		iter_14_1.SetArgs(arg_14_1, arg_14_0)

def var_0_3.Trigger(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = arg_15_0.GetBuffList() or {}
	local var_15_1 = {}

	for iter_15_0, iter_15_1 in pairs(var_15_0):
		local var_15_2 = iter_15_1._triggerSearchTable[arg_15_1]

		if var_15_2 != None and #var_15_2 > 0:
			var_15_1[#var_15_1 + 1] = iter_15_1

	for iter_15_2, iter_15_3 in ipairs(var_15_1):
		iter_15_3.onTrigger(arg_15_1, arg_15_0, arg_15_2)

def var_0_3.DisptachSkillFloat(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	if arg_16_3.trigger == None or table.contains(arg_16_3.trigger, arg_16_2):
		local var_16_0

		if arg_16_3.painting and type(arg_16_3.painting) == "string":
			var_16_0 = arg_16_3

		local var_16_1 = getSkillName(arg_16_3.displayID or arg_16_0._id)

		arg_16_1.DispatchSkillFloat(var_16_1, None, var_16_0)

		local var_16_2

		if arg_16_3.castCV != False:
			var_16_2 = arg_16_3.castCV or "skill"

		local var_16_3 = type(var_16_2)

		if var_16_3 == "string":
			arg_16_1.DispatchVoice(var_16_2)
		elif var_16_3 == "table":
			local var_16_4, var_16_5, var_16_6 = ShipWordHelper.GetWordAndCV(var_16_2.skinID, var_16_2.key)

			pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_16_5)

		local var_16_7 = arg_16_3.aniEffect or var_0_3.DEFAULT_ANI_FX_CONFIG
		local var_16_8 = {
			effect = var_16_7.effect,
			offset = var_16_7.offset
		}

		arg_16_1.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.ADD_EFFECT, var_16_8))

def var_0_3.IsSubmarineSpecial(arg_17_0):
	local var_17_0 = arg_17_0._triggerSearchTable[var_0_0.Battle.BattleConst.BuffEffectType.ON_SUBMARINE_FREE_SPECIAL] or {}

	for iter_17_0, iter_17_1 in ipairs(var_17_0):
		if iter_17_1.HaveQuota():
			return True

	return False

def var_0_3.onTrigger(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	local var_18_0 = arg_18_0._triggerSearchTable[arg_18_1]

	if var_18_0 == None or #var_18_0 == 0:
		return

	for iter_18_0, iter_18_1 in ipairs(var_18_0):
		assert(type(iter_18_1[arg_18_1]) == "function", "buff效果的触发名字和触发函数不相符,buff id.>>" .. arg_18_0._id .. "<<, trigger.>>" .. arg_18_1 .. "<<")

		if iter_18_1.HaveQuota() and iter_18_1.IsActive():
			iter_18_1.NotActive()
			iter_18_1.Trigger(arg_18_1, arg_18_2, arg_18_0, arg_18_3)

			local var_18_1 = iter_18_1.GetPopConfig()

			if var_18_1:
				arg_18_0.DisptachSkillFloat(arg_18_2, arg_18_1, var_18_1)

			iter_18_1.SetActive()

		if arg_18_0._isCancel:
			break

	if arg_18_0._isCancel:
		arg_18_0._isCancel = None

		arg_18_0.Remove()

def var_0_3.SetRemoveTime(arg_19_0):
	local var_19_0 = pg.TimeMgr.GetInstance().GetCombatTime()

	arg_19_0._buffStartTimeStamp = var_19_0
	arg_19_0._RemoveTime = var_19_0 + arg_19_0._time
	arg_19_0._cancelTime = None

def var_0_3.IsTimeToRemove(arg_20_0, arg_20_1):
	if arg_20_0._isCancel:
		return True
	elif arg_20_0._cancelTime and arg_20_1 >= arg_20_0._cancelTime:
		return True
	elif arg_20_0._time == 0:
		return False
	else
		return arg_20_1 >= arg_20_0._RemoveTime

def var_0_3.GetBuffLifeTime(arg_21_0):
	return arg_21_0._time

def var_0_3.GetBuffStartTime(arg_22_0):
	return arg_22_0._buffStartTimeStamp

def var_0_3.Interrupt(arg_23_0):
	for iter_23_0, iter_23_1 in ipairs(arg_23_0._effectList):
		iter_23_1.Interrupt()

def var_0_3.Clear(arg_24_0):
	for iter_24_0, iter_24_1 in ipairs(arg_24_0._effectList):
		iter_24_1.Clear()

def var_0_3.GetID(arg_25_0):
	return arg_25_0._id

def var_0_3.GetCaster(arg_26_0):
	return arg_26_0._caster

def var_0_3.GetLv(arg_27_0):
	return arg_27_0._level or 1

def var_0_3.GetDuration(arg_28_0):
	return arg_28_0._time

def var_0_3.GetStack(arg_29_0):
	return arg_29_0._stack or 1

def var_0_3.SetToCancel(arg_30_0, arg_30_1):
	if arg_30_1:
		if not arg_30_0._cancelTime:
			arg_30_0._cancelTime = pg.TimeMgr.GetInstance().GetCombatTime() + arg_30_1
	else
		arg_30_0._isCancel = True

def var_0_3.Dispose(arg_31_0):
	arg_31_0._triggerSearchTable = None
	arg_31_0._commander = None
