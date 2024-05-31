ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = var_0_0.Battle.BattleFormulas
local var_0_4 = var_0_0.Battle.BattleConst
local var_0_5 = var_0_0.Battle.BattleConfig
local var_0_6 = var_0_0.Battle.BattleAttr
local var_0_7 = var_0_0.Battle.BattleDataFunction
local var_0_8 = var_0_0.Battle.BattleAttr
local var_0_9 = class("BattleFleetManualSubComponent")

var_0_0.Battle.BattleFleetManualSubComponent = var_0_9
var_0_9.__name = "BattleFleetManualSubComponent"

def var_0_9.Ctor(arg_1_0, arg_1_1):
	arg_1_0._fleetVO = arg_1_1

	arg_1_0.init()
	arg_1_0.attachFunction()

def var_0_9.attachFunction(arg_2_0):
	arg_2_0._fleetVO.GetSubBench = var_0_9.GetSubBench
	arg_2_0._fleetVO.GetSubFreeDiveVO = var_0_9.GetSubFreeDiveVO
	arg_2_0._fleetVO.GetSubFreeFloatVO = var_0_9.GetSubFreeFloatVO
	arg_2_0._fleetVO.GetSubBoostVO = var_0_9.GetSubBoostVO
	arg_2_0._fleetVO.GetSubSpecialVO = var_0_9.GetSubSpecialVO
	arg_2_0._fleetVO.GetSubShiftVO = var_0_9.GetSubShiftVO
	arg_2_0._fleetVO.AddManualSubmarine = var_0_9.AddManualSubmarine

def var_0_9.UpdateAutoComponent(arg_3_0, arg_3_1):
	for iter_3_0, iter_3_1 in ipairs(arg_3_0._manualSubList):
		iter_3_1.UpdateOxygen(arg_3_1)

def var_0_9.UpdateManualWeaponVO(arg_4_0, arg_4_1):
	arg_4_0._submarineDiveVO.Update(arg_4_1)
	arg_4_0._submarineFloatVO.Update(arg_4_1)
	arg_4_0._submarineBoostVO.Update(arg_4_1)
	arg_4_0._submarineShiftVO.Update(arg_4_1)

def var_0_9.RemovePlayerUnit(arg_5_0, arg_5_1):
	for iter_5_0, iter_5_1 in ipairs(arg_5_0._subList, i):
		if iter_5_1 == arg_5_1:
			table.remove(arg_5_0._subList, iter_5_0)

			break

	for iter_5_2, iter_5_3 in ipairs(arg_5_0._manualSubList):
		if iter_5_3 == arg_5_1:
			table.remove(arg_5_0._manualSubList, iter_5_2)

			break

	if not arg_5_0._manualSubUnit:
		arg_5_0.refreshFleetFormation(indexList)

def var_0_9.AddManualSubmarine(arg_6_0, arg_6_1):
	arg_6_0._unitList[#arg_6_0._unitList + 1] = arg_6_1
	arg_6_0._manualSubList[#arg_6_0._manualSubList + 1] = arg_6_1
	arg_6_0._manualSubBench[#arg_6_0._manualSubBench + 1] = arg_6_1
	arg_6_0._maxCount = arg_6_0._maxCount + 1

	arg_6_1.InitOxygen()
	arg_6_1.SetFleetVO(arg_6_0)
	arg_6_1.SetMotion(arg_6_0._motionVO)
	arg_6_1.RegisterEventListener(arg_6_0, var_0_1.UPDATE_HP, arg_6_0.onUnitUpdateHP)

def var_0_9.GetSubBench(arg_7_0):
	return arg_7_0._manualSubBench

def var_0_9.GetSubFreeDiveVO(arg_8_0):
	return arg_8_0._manualSubComponent._submarineDiveVO

def var_0_9.GetSubFreeFloatVO(arg_9_0):
	return arg_9_0._manualSubComponent._submarineFloatVO

def var_0_9.GetSubBoostVO(arg_10_0):
	return arg_10_0._manualSubComponent._submarineBoostVO

def var_0_9.GetSubSpecialVO(arg_11_0):
	return arg_11_0._manualSubComponent._submarineSpecialVO

def var_0_9.GetSubShiftVO(arg_12_0):
	return arg_12_0._manualSubComponent._submarineShiftVO

def var_0_9.init(arg_13_0):
	arg_13_0._submarineDiveVO = var_0_0.Battle.BattleSubmarineFuncVO.New(var_0_5.SR_CONFIG.DIVE_CD)
	arg_13_0._submarineFloatVO = var_0_0.Battle.BattleSubmarineFuncVO.New(var_0_5.SR_CONFIG.FLOAT_CD)
	arg_13_0._submarineVOList = {
		arg_13_0._submarineDiveVO,
		arg_13_0._submarineFloatVO
	}
	arg_13_0._submarineBoostVO = var_0_0.Battle.BattleSubmarineFuncVO.New(var_0_5.SR_CONFIG.BOOST_CD)
	arg_13_0._submarineShiftVO = var_0_0.Battle.BattleSubmarineFuncVO.New(var_0_5.SR_CONFIG.SHIFT_CD)
	arg_13_0._submarineSpecialVO = var_0_0.Battle.BattleSubmarineAidVO.New()

	arg_13_0._submarineSpecialVO.SetCount(1)
	arg_13_0._submarineSpecialVO.SetTotal(1)

	arg_13_0._manualSubList = {}
	arg_13_0._manualSubBench = {}
	arg_13_0._unitList = {}
	arg_13_0._maxCount = 0

def var_0_9.SetSubUnitData(arg_14_0, arg_14_1):
	arg_14_0._subUntiDataList = arg_14_1

def var_0_9.GetSubUnitData(arg_15_0):
	return arg_15_0._subUntiDataList

def var_0_9.GetSubList(arg_16_0):
	return arg_16_0._subList

def var_0_9.ShiftManualSub(arg_17_0):
	local var_17_0

	if arg_17_0._manualSubUnit:
		local var_17_1 = arg_17_0._manualSubUnit.GetTorpedoList()

		for iter_17_0, iter_17_1 in ipairs(var_17_1):
			if iter_17_1.IsAttacking():
				arg_17_0.CancelTorpedo()

			arg_17_0._torpedoWeaponVO.RemoveWeapon(iter_17_1)

		if arg_17_0._manualSubUnit.IsAlive():
			table.insert(arg_17_0._manualSubBench, arg_17_0._manualSubUnit)

		var_17_0 = arg_17_0._motionVO.GetPos().Clone()
	else
		var_17_0 = arg_17_0._manualSubList[1].GetPosition().Clone()

	arg_17_0._manualSubUnit = table.remove(arg_17_0._manualSubBench, 1)
	arg_17_0._scoutList[1] = arg_17_0._manualSubUnit

	local var_17_2 = {}

	for iter_17_2, iter_17_3 in ipairs(arg_17_0._manualSubBench):
		for iter_17_4, iter_17_5 in ipairs(arg_17_0._unitList):
			if iter_17_5 == iter_17_3:
				table.insert(var_17_2, iter_17_4)

				break

	for iter_17_6, iter_17_7 in ipairs(arg_17_0._unitList):
		if iter_17_7 == arg_17_0._manualSubUnit:
			table.insert(var_17_2, 1, iter_17_6)

			break

	arg_17_0.refreshFleetFormation(var_17_2)
	arg_17_0._manualSubUnit.SetMainUnitStatic(False)
	arg_17_0._manualSubUnit.SetPosition(var_17_0)
	arg_17_0.UpdateMotion()
	arg_17_0._submarineSpecialVO.SetUseable(False)

	local var_17_3 = arg_17_0._manualSubUnit.GetBuffList()

	for iter_17_8, iter_17_9 in pairs(var_17_3):
		if iter_17_9.IsSubmarineSpecial():
			arg_17_0._submarineSpecialVO.SetCount(1)
			arg_17_0._submarineSpecialVO.SetUseable(True)

			break

	arg_17_0.ChangeSubmarineState(var_0_0.Battle.OxyState.STATE_FREE_DIVE)
	arg_17_0._torpedoWeaponVO.Reset()

	local var_17_4 = arg_17_0._manualSubUnit.GetTorpedoList()

	for iter_17_10, iter_17_11 in ipairs(var_17_4):
		if iter_17_11.GetCurrentState() != iter_17_11.STATE_OVER_HEAT:
			arg_17_0._torpedoWeaponVO.AppendWeapon(iter_17_11)

	for iter_17_12, iter_17_13 in ipairs(var_17_4):
		if iter_17_13.GetCurrentState() == iter_17_13.STATE_OVER_HEAT:
			arg_17_0._torpedoWeaponVO.AppendWeapon(iter_17_13)

	for iter_17_14, iter_17_15 in ipairs(arg_17_0._manualSubBench):
		iter_17_15.SetPosition(var_0_5.SUB_BENCH_POS[iter_17_14])
		iter_17_15.SetMainUnitStatic(True)
		iter_17_15.ChangeOxygenState(var_0_0.Battle.OxyState.STATE_FREE_BENCH)

	arg_17_0._submarineShiftVO.ResetCurrent()

	if #arg_17_0._manualSubBench == 0:
		arg_17_0._submarineShiftVO.SetActive(False)

def var_0_9.ChangeSubmarineState(arg_18_0, arg_18_1, arg_18_2):
	if not arg_18_0._manualSubUnit:
		return

	arg_18_0._manualSubUnit.ChangeOxygenState(arg_18_1)

	if arg_18_2:
		for iter_18_0, iter_18_1 in ipairs(arg_18_0._submarineVOList):
			iter_18_1.ResetCurrent()

		local var_18_0 = arg_18_0._submarineShiftVO.GetMax() - arg_18_0._submarineShiftVO.GetCurrent()

		if arg_18_0._submarineShiftVO.IsOverLoad() and var_18_0 > var_0_5.SR_CONFIG.DIVE_CD:
			-- block empty
		else
			arg_18_0._submarineShiftVO.SetMax(var_0_5.SR_CONFIG.DIVE_CD)
			arg_18_0._submarineShiftVO.ResetCurrent()

	arg_18_0.DispatchEvent(var_0_0.Event.New(var_0_2.MANUAL_SUBMARINE_SHIFT, {
		state = arg_18_1
	}))

def var_0_9.SubmarinBoost(arg_19_0):
	arg_19_0._manualSubUnit.Boost(Vector3.right, var_0_5.SR_CONFIG.BOOST_SPEED, var_0_5.SR_CONFIG.BOOST_DECAY, var_0_5.SR_CONFIG.BOOST_DURATION, var_0_5.SR_CONFIG.BOOST_DECAY_STAMP)
	arg_19_0._submarineBoostVO.ResetCurrent()

def var_0_9.UnleashSubmarineSpecial(arg_20_0):
	if arg_20_0.GetWeaponBlock():
		return

	arg_20_0._submarineSpecialVO.Cast()
	arg_20_0._manualSubUnit.TriggerBuff(var_0_4.BuffEffectType.ON_SUBMARINE_FREE_SPECIAL)
