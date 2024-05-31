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
local var_0_9 = class("BattleFleetVO")

var_0_0.Battle.BattleFleetVO = var_0_9
var_0_9.__name = "BattleFleetVO"

def var_0_9.Ctor(arg_1_0, arg_1_1):
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_1_0)
	var_0_0.EventListener.AttachEventListener(arg_1_0)

	arg_1_0._IFF = arg_1_1
	arg_1_0._lastDist = 0

	arg_1_0.init()

def var_0_9.UpdateMotion(arg_2_0):
	if arg_2_0._motionReferenceUnit:
		arg_2_0._motionVO.UpdatePos(arg_2_0._motionReferenceUnit)
		arg_2_0._motionVO.UpdateVelocityAndDirection(arg_2_0.GetFleetVelocity(), arg_2_0._motionSourceFunc())

	local var_2_0 = math.max(arg_2_0._motionVO.GetPos().x - arg_2_0._rightBound, 0)

	if var_2_0 >= 0 and var_2_0 != arg_2_0._lastDist:
		arg_2_0._lastDist = var_2_0

		arg_2_0.DispatchEvent(var_0_0.Event.New(var_0_2.SHOW_BUFFER, {
			dist = var_2_0
		}))

def var_0_9.UpdateAutoComponent(arg_3_0, arg_3_1):
	for iter_3_0, iter_3_1 in ipairs(arg_3_0._scoutList):
		iter_3_1.UpdateWeapon(arg_3_1)
		iter_3_1.UpdateAirAssist()

	for iter_3_2, iter_3_3 in ipairs(arg_3_0._mainList):
		iter_3_3.UpdateWeapon(arg_3_1)
		iter_3_3.UpdateAirAssist()

	for iter_3_4, iter_3_5 in ipairs(arg_3_0._cloakList):
		iter_3_5.UpdateCloak(arg_3_1)

	for iter_3_6, iter_3_7 in ipairs(arg_3_0._subList):
		iter_3_7.UpdateWeapon(arg_3_1)
		iter_3_7.UpdateOxygen(arg_3_1)
		iter_3_7.UpdatePhaseSwitcher()

	for iter_3_8, iter_3_9 in ipairs(arg_3_0._manualSubList):
		iter_3_9.UpdateOxygen(arg_3_1)

	arg_3_0._fleetAntiAir.Update(arg_3_1)
	arg_3_0._fleetRangeAntiAir.Update(arg_3_1)
	arg_3_0._fleetStaticSonar.Update(arg_3_1)

	for iter_3_10, iter_3_11 in pairs(arg_3_0._indieSonarList):
		iter_3_10.Update(arg_3_1)

	arg_3_0.UpdateBuff(arg_3_1)

def var_0_9.UpdateBuff(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0._buffList

	for iter_4_0, iter_4_1 in pairs(var_4_0):
		iter_4_1.Update(arg_4_0, arg_4_1)

def var_0_9.UpdateManualWeaponVO(arg_5_0, arg_5_1):
	arg_5_0._chargeWeaponVO.Update(arg_5_1)
	arg_5_0._torpedoWeaponVO.Update(arg_5_1)
	arg_5_0._airAssistVO.Update(arg_5_1)
	arg_5_0._submarineDiveVO.Update(arg_5_1)
	arg_5_0._submarineFloatVO.Update(arg_5_1)
	arg_5_0._submarineBoostVO.Update(arg_5_1)
	arg_5_0._submarineShiftVO.Update(arg_5_1)

def var_0_9.UpdateFleetDamage(arg_6_0, arg_6_1):
	local var_6_0 = var_0_3.CalculateFleetDamage(arg_6_1)

	arg_6_0._currentDMGRatio = arg_6_0._currentDMGRatio + var_6_0

	arg_6_0.DispatchFleetDamageChange()

def var_0_9.UpdateFleetOverDamage(arg_7_0, arg_7_1):
	local var_7_0 = var_0_3.CalculateFleetOverDamage(arg_7_0, arg_7_1)

	arg_7_0._currentDMGRatio = arg_7_0._currentDMGRatio - var_7_0

	arg_7_0.DispatchFleetDamageChange()

def var_0_9.DispatchFleetDamageChange(arg_8_0):
	arg_8_0.DispatchEvent(var_0_0.Event.New(var_0_2.FLEET_DMG_CHANGE, {}))

def var_0_9.DispatchSonarScan(arg_9_0, arg_9_1):
	arg_9_0.DispatchEvent(var_0_0.Event.New(var_0_2.SONAR_SCAN, {
		indieSonar = arg_9_1
	}))

def var_0_9.FreeMainUnit(arg_10_0, arg_10_1):
	if arg_10_0._mainUnitFree:
		return

	arg_10_0._mainUnitFree = True

	for iter_10_0, iter_10_1 in ipairs(arg_10_0._mainList):
		local var_10_0 = var_0_0.Battle.BattleBuffUnit.New(arg_10_1)

		iter_10_1.AddBuff(var_10_0)
		iter_10_1.SetMainUnitStatic(False)

def var_0_9.RandomMainVictim(arg_11_0, arg_11_1):
	arg_11_1 = arg_11_1 or {}

	local var_11_0 = {}
	local var_11_1

	for iter_11_0, iter_11_1 in ipairs(arg_11_0._mainList):
		local var_11_2 = True

		for iter_11_2, iter_11_3 in ipairs(arg_11_1):
			if iter_11_1.GetAttrByName(iter_11_3) == 1:
				var_11_2 = False

				break

		if var_11_2:
			table.insert(var_11_0, iter_11_1)

	if #var_11_0 > 0:
		var_11_1 = var_11_0[math.random(#var_11_0)]

	return var_11_1

def var_0_9.NearestUnitByType(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = 999
	local var_12_1

	for iter_12_0, iter_12_1 in ipairs(arg_12_0._unitList):
		local var_12_2 = iter_12_1.GetTemplate().type

		if table.contains(arg_12_2, var_12_2):
			local var_12_3 = iter_12_1.GetPosition()
			local var_12_4 = Vector3.BattleDistance(var_12_3, arg_12_1)

			if var_12_4 < var_12_0:
				var_12_0 = var_12_4
				var_12_1 = iter_12_1

	return var_12_1

def var_0_9.SetMotionSource(arg_13_0, arg_13_1):
	if arg_13_1 == None:
		function arg_13_0._motionSourceFunc()
			local var_14_0 = pg.UIMgr.GetInstance()

			return var_14_0.hrz, var_14_0.vtc
	else
		arg_13_0._motionSourceFunc = arg_13_1

def var_0_9.SetSubAidData(arg_15_0, arg_15_1, arg_15_2):
	arg_15_0._submarineVO = var_0_0.Battle.BattleSubmarineAidVO.New()

	if arg_15_2 == var_0_4.SubAidFlag.AID_EMPTY or arg_15_2 == var_0_4.SubAidFlag.OIL_EMPTY:
		arg_15_0._submarineVO.SetUseable(False)
	else
		arg_15_0._submarineVO.SetCount(arg_15_2)
		arg_15_0._submarineVO.SetTotal(arg_15_1)
		arg_15_0._submarineVO.SetUseable(True)

def var_0_9.SetBound(arg_16_0, arg_16_1, arg_16_2, arg_16_3, arg_16_4):
	arg_16_0._upperBound = arg_16_1
	arg_16_0._lowerBound = arg_16_2
	arg_16_0._leftBound = arg_16_3
	arg_16_0._rightBound = arg_16_4

def var_0_9.SetTotalBound(arg_17_0, arg_17_1, arg_17_2, arg_17_3, arg_17_4):
	arg_17_0._totalUpperBound = arg_17_1
	arg_17_0._totalLowerBound = arg_17_2
	arg_17_0._totalLeftBound = arg_17_3
	arg_17_0._totalRightBound = arg_17_4

def var_0_9.CalcSubmarineBaseLine(arg_18_0, arg_18_1):
	local var_18_0 = (arg_18_0._totalRightBound + arg_18_0._totalLeftBound) * 0.5

	if arg_18_0._IFF == var_0_5.FRIENDLY_CODE:
		if arg_18_1 == SYSTEM_DUEL:
			-- block empty
		else
			arg_18_0._subAttackBaseLine = var_18_0
			arg_18_0._subRetreatBaseLine = arg_18_0._leftBound - 10
	elif arg_18_0._IFF == var_0_5.FOE_CODE and arg_18_1 == SYSTEM_DUEL:
		-- block empty

def var_0_9.SetExposeLine(arg_19_0, arg_19_1, arg_19_2):
	arg_19_0._visionLineX = arg_19_1
	arg_19_0._exposeLineX = arg_19_2

def var_0_9.AppendPlayerUnit(arg_20_0, arg_20_1):
	arg_20_0._unitList[#arg_20_0._unitList + 1] = arg_20_1
	arg_20_0._maxCount = arg_20_0._maxCount + 1

	if arg_20_1.IsMainFleetUnit():
		arg_20_0.appendMainUnit(arg_20_1)
	else
		arg_20_0.appendScoutUnit(arg_20_1)

	arg_20_1.SetFleetVO(arg_20_0)
	arg_20_1.SetMotion(arg_20_0._motionVO)
	arg_20_1.RegisterEventListener(arg_20_0, var_0_1.UPDATE_HP, arg_20_0.onUnitUpdateHP)

def var_0_9.RemovePlayerUnit(arg_21_0, arg_21_1):
	local var_21_0 = {}

	for iter_21_0, iter_21_1 in ipairs(arg_21_0._unitList):
		if iter_21_1 != arg_21_1:
			var_21_0[#var_21_0 + 1] = iter_21_0
		else
			iter_21_1.UnregisterEventListener(arg_21_0, var_0_1.UPDATE_HP)
			iter_21_1.DeactiveCldBox()

			local var_21_1 = iter_21_1.GetChargeList()

			for iter_21_2, iter_21_3 in ipairs(var_21_1):
				if iter_21_3.IsAttacking():
					arg_21_0._chargeWeaponVO.CancelFocus()
					arg_21_0._chargeWeaponVO.ResetFocus()
					arg_21_0.CancelChargeWeapon()

				arg_21_0._chargeWeaponVO.RemoveWeapon(iter_21_3)
				iter_21_3.Clear()

			arg_21_0._fleetAntiAir.RemoveCrewUnit(arg_21_1)
			arg_21_0._fleetRangeAntiAir.RemoveCrewUnit(arg_21_1)
			arg_21_0._fleetStaticSonar.RemoveCrewUnit(arg_21_1)

			local var_21_2 = iter_21_1.GetTorpedoList()

			for iter_21_4, iter_21_5 in ipairs(var_21_2):
				arg_21_0.RemoveManunalTorpedo(iter_21_5)

			local var_21_3 = iter_21_1.GetAirAssistList()

			if var_21_3:
				for iter_21_6, iter_21_7 in ipairs(var_21_3):
					arg_21_0._airAssistVO.RemoveWeapon(iter_21_7)

	for iter_21_8, iter_21_9 in ipairs(arg_21_0._scoutList):
		if iter_21_9 == arg_21_1:
			if #arg_21_0._scoutList == 1:
				arg_21_0.CancelChargeWeapon()

			table.remove(arg_21_0._scoutList, iter_21_8)

			break

	for iter_21_10, iter_21_11 in ipairs(arg_21_0._mainList):
		if iter_21_11 == arg_21_1:
			table.remove(arg_21_0._mainList, iter_21_10)

			break

	for iter_21_12, iter_21_13 in ipairs(arg_21_0._cloakList):
		if iter_21_13 == arg_21_1:
			table.remove(arg_21_0._cloakList, iter_21_12)

			break

	for iter_21_14, iter_21_15 in ipairs(arg_21_0._subList, i):
		if iter_21_15 == arg_21_1:
			table.remove(arg_21_0._subList, iter_21_14)

			break

	for iter_21_16, iter_21_17 in ipairs(arg_21_0._manualSubList):
		if iter_21_17 == arg_21_1:
			table.remove(arg_21_0._manualSubList, iter_21_16)

			break

	if not arg_21_0._manualSubUnit:
		arg_21_0.refreshFleetFormation(var_21_0)

def var_0_9.OverrideJoyStickAutoBot(arg_22_0, arg_22_1):
	arg_22_0._autoBotAIID = arg_22_1

	local var_22_0 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.OVERRIDE_AUTO_BOT)

	arg_22_0.DispatchEvent(var_22_0)

def var_0_9.SnapShot(arg_23_0):
	arg_23_0._totalDMGRatio = var_0_3.GetFleetTotalHP(arg_23_0)
	arg_23_0._currentDMGRatio = arg_23_0._totalDMGRatio

def var_0_9.GetIFF(arg_24_0):
	return arg_24_0._IFF

def var_0_9.GetMaxCount(arg_25_0):
	return arg_25_0._maxCount

def var_0_9.GetFlagShip(arg_26_0):
	return arg_26_0._flagShip

def var_0_9.GetLeaderShip(arg_27_0):
	return arg_27_0._scoutList[1]

def var_0_9.GetUnitList(arg_28_0):
	return arg_28_0._unitList

def var_0_9.GetMainList(arg_29_0):
	return arg_29_0._mainList

def var_0_9.GetScoutList(arg_30_0):
	return arg_30_0._scoutList

def var_0_9.GetCloakList(arg_31_0):
	return arg_31_0._cloakList

def var_0_9.GetSubBench(arg_32_0):
	return arg_32_0._manualSubBench

def var_0_9.GetMotion(arg_33_0):
	return arg_33_0._motionVO

def var_0_9.GetMotionReferenceUnit(arg_34_0):
	return arg_34_0._motionReferenceUnit

def var_0_9.GetAutoBotAIID(arg_35_0):
	return arg_35_0._autoBotAIID

def var_0_9.GetChargeWeaponVO(arg_36_0):
	return arg_36_0._chargeWeaponVO

def var_0_9.GetTorpedoWeaponVO(arg_37_0):
	return arg_37_0._torpedoWeaponVO

def var_0_9.GetAirAssistVO(arg_38_0):
	return arg_38_0._airAssistVO

def var_0_9.GetSubAidVO(arg_39_0):
	return arg_39_0._submarineVO

def var_0_9.GetSubFreeDiveVO(arg_40_0):
	return arg_40_0._submarineDiveVO

def var_0_9.GetSubFreeFloatVO(arg_41_0):
	return arg_41_0._submarineFloatVO

def var_0_9.GetSubBoostVO(arg_42_0):
	return arg_42_0._submarineBoostVO

def var_0_9.GetSubSpecialVO(arg_43_0):
	return arg_43_0._submarineSpecialVO

def var_0_9.GetSubShiftVO(arg_44_0):
	return arg_44_0._submarineShiftVO

def var_0_9.GetFleetAntiAirWeapon(arg_45_0):
	return arg_45_0._fleetAntiAir

def var_0_9.GetFleetRangeAntiAirWeapon(arg_46_0):
	return arg_46_0._fleetRangeAntiAir

def var_0_9.GetFleetVelocity(arg_47_0):
	return var_0_3.GetFleetVelocity(arg_47_0._scoutList)

def var_0_9.GetFleetBound(arg_48_0):
	return arg_48_0._upperBound, arg_48_0._lowerBound, arg_48_0._leftBound, arg_48_0._rightBound

def var_0_9.GetFleetExposeLine(arg_49_0):
	return arg_49_0._exposeLineX

def var_0_9.GetFleetVisionLine(arg_50_0):
	return arg_50_0._visionLineX

def var_0_9.GetLeaderPersonality(arg_51_0):
	return arg_51_0._motionReferenceUnit.GetAutoPilotPreference()

def var_0_9.GetDamageRatioResult(arg_52_0):
	return string.format("%0.2f", arg_52_0._currentDMGRatio / arg_52_0._totalDMGRatio * 100), arg_52_0._totalDMGRatio

def var_0_9.GetDamageRatio(arg_53_0):
	return arg_53_0._currentDMGRatio / arg_53_0._totalDMGRatio

def var_0_9.GetSubmarineBaseLine(arg_54_0):
	return arg_54_0._subAttackBaseLine, arg_54_0._subRetreatBaseLine

def var_0_9.GetFleetSonar(arg_55_0):
	return arg_55_0._fleetStaticSonar

def var_0_9.Dispose(arg_56_0):
	var_0_0.EventDispatcher.DetachEventDispatcher(arg_56_0)
	var_0_0.EventListener.DetachEventListener(arg_56_0)

	arg_56_0._leaderUnit = None

	arg_56_0._fleetAntiAir.Dispose()
	arg_56_0._fleetRangeAntiAir.Dispose()
	arg_56_0._fleetStaticSonar.Dispose()

	arg_56_0._fleetStaticSonar = None
	arg_56_0._buffList = None
	arg_56_0._indieSonarList = None
	arg_56_0._scoutAimBias = None

def var_0_9.refreshFleetFormation(arg_57_0, arg_57_1):
	local var_57_0 = var_0_7.GetFormationTmpDataFromID(var_0_5.FORMATION_ID).pos_offset

	arg_57_0._unitList = var_0_7.SortFleetList(arg_57_1, arg_57_0._unitList)

	local var_57_1 = var_0_5.BornOffset

	if not arg_57_0._mainUnitFree:
		for iter_57_0, iter_57_1 in ipairs(arg_57_0._unitList):
			if not table.contains(arg_57_0._subList, iter_57_1):
				local var_57_2 = var_57_0[iter_57_0]

				iter_57_1.UpdateFormationOffset(Vector3(var_57_2.x, var_57_2.y, var_57_2.z) + var_57_1 * (iter_57_0 - 1))

	if #arg_57_0._scoutList > 0:
		arg_57_0._motionReferenceUnit = arg_57_0._scoutList[1]
		arg_57_0._leaderUnit = arg_57_0._scoutList[1]

		arg_57_0._leaderUnit.LeaderSetting()
		arg_57_0._fleetAntiAir.SwitchHost(arg_57_0._motionReferenceUnit)
		arg_57_0._fleetStaticSonar.SwitchHost(arg_57_0._motionReferenceUnit)

		for iter_57_2, iter_57_3 in pairs(arg_57_0._indieSonarList):
			iter_57_2.SwitchHost(arg_57_0._motionReferenceUnit)

		arg_57_0._motionVO.UpdatePos(arg_57_0._motionReferenceUnit)
	elif arg_57_0._fleetAntiAir.GetCurrentState() != arg_57_0._fleetAntiAir.STATE_DISABLE:
		local var_57_3 = arg_57_0._fleetAntiAir.GetCrewUnitList()

		for iter_57_4, iter_57_5 in pairs(var_57_3):
			arg_57_0._motionReferenceUnit = iter_57_4

			arg_57_0._fleetAntiAir.SwitchHost(iter_57_4)

			break
	else
		arg_57_0._motionReferenceUnit = arg_57_0._mainList[1]
		arg_57_0._leaderUnit = None

	if #arg_57_0.GetUnitList() == 0:
		return

	local var_57_4 = var_0_0.Event.New(var_0_0.Battle.BattleEvent.REFRESH_FLEET_FORMATION)

	arg_57_0.DispatchEvent(var_57_4)

def var_0_9.init(arg_58_0):
	arg_58_0._chargeWeaponVO = var_0_0.Battle.BattleChargeWeaponVO.New()
	arg_58_0._torpedoWeaponVO = var_0_0.Battle.BattleTorpedoWeaponVO.New()
	arg_58_0._airAssistVO = var_0_0.Battle.BattleAllInStrikeVO.New()
	arg_58_0._submarineDiveVO = var_0_0.Battle.BattleSubmarineFuncVO.New(var_0_5.SR_CONFIG.DIVE_CD)
	arg_58_0._submarineFloatVO = var_0_0.Battle.BattleSubmarineFuncVO.New(var_0_5.SR_CONFIG.FLOAT_CD)
	arg_58_0._submarineVOList = {
		arg_58_0._submarineDiveVO,
		arg_58_0._submarineFloatVO
	}
	arg_58_0._submarineBoostVO = var_0_0.Battle.BattleSubmarineFuncVO.New(var_0_5.SR_CONFIG.BOOST_CD)
	arg_58_0._submarineShiftVO = var_0_0.Battle.BattleSubmarineFuncVO.New(var_0_5.SR_CONFIG.SHIFT_CD)
	arg_58_0._submarineSpecialVO = var_0_0.Battle.BattleSubmarineAidVO.New()

	arg_58_0._submarineSpecialVO.SetCount(1)
	arg_58_0._submarineSpecialVO.SetTotal(1)

	arg_58_0._fleetAntiAir = var_0_0.Battle.BattleFleetAntiAirUnit.New()
	arg_58_0._fleetRangeAntiAir = var_0_0.Battle.BattleFleetRangeAntiAirUnit.New()
	arg_58_0._motionVO = var_0_0.Battle.BattleFleetMotionVO.New()
	arg_58_0._fleetStaticSonar = var_0_0.Battle.BattleFleetStaticSonar.New(arg_58_0)
	arg_58_0._indieSonarList = {}
	arg_58_0._scoutList = {}
	arg_58_0._mainList = {}
	arg_58_0._subList = {}
	arg_58_0._cloakList = {}
	arg_58_0._manualSubList = {}
	arg_58_0._manualSubBench = {}
	arg_58_0._unitList = {}
	arg_58_0._maxCount = 0
	arg_58_0._blockCast = 0
	arg_58_0._buffList = {}

	arg_58_0.SetMotionSource()

def var_0_9.appendScoutUnit(arg_59_0, arg_59_1):
	arg_59_0._scoutList[#arg_59_0._scoutList + 1] = arg_59_1

	local var_59_0 = arg_59_1.GetTorpedoList()

	for iter_59_0, iter_59_1 in ipairs(var_59_0):
		arg_59_0._torpedoWeaponVO.AppendWeapon(iter_59_1)

	if #arg_59_1.GetHiveList() > 0:
		local var_59_1 = var_0_7.CreateAllInStrike(arg_59_1)

		for iter_59_2, iter_59_3 in ipairs(var_59_1):
			arg_59_0._airAssistVO.AppendWeapon(iter_59_3)

		arg_59_1.SetAirAssistList(var_59_1)

	arg_59_0._fleetAntiAir.AppendCrewUnit(arg_59_1)
	arg_59_0._fleetStaticSonar.AppendCrewUnit(arg_59_1)

	local var_59_2 = 1
	local var_59_3 = #arg_59_0._unitList
	local var_59_4 = {}

	while var_59_2 < var_59_3:
		table.insert(var_59_4, var_59_2)

		var_59_2 = var_59_2 + 1

	table.insert(var_59_4, #arg_59_0._scoutList, var_59_2)
	arg_59_0.refreshFleetFormation(var_59_4)

def var_0_9.appendMainUnit(arg_60_0, arg_60_1):
	if #arg_60_0._mainList == 0:
		arg_60_0._flagShip = arg_60_1

	arg_60_0._mainList[#arg_60_0._mainList + 1] = arg_60_1

	arg_60_1.SetMainUnitIndex(#arg_60_0._mainList)

	if ShipType.CloakShipType(arg_60_1.GetTemplate().type):
		arg_60_0.AttachCloak(arg_60_1)

	local var_60_0 = arg_60_1.GetChargeList()

	for iter_60_0, iter_60_1 in ipairs(var_60_0):
		arg_60_0._chargeWeaponVO.AppendWeapon(iter_60_1)

	local var_60_1 = arg_60_1.GetTorpedoList()

	for iter_60_2, iter_60_3 in ipairs(var_60_1):
		arg_60_0._torpedoWeaponVO.AppendWeapon(iter_60_3)

	if #arg_60_1.GetHiveList() > 0:
		local var_60_2 = var_0_7.CreateAllInStrike(arg_60_1)

		for iter_60_4, iter_60_5 in ipairs(var_60_2):
			arg_60_0._airAssistVO.AppendWeapon(iter_60_5)

		arg_60_1.SetAirAssistList(var_60_2)

	arg_60_0._fleetAntiAir.AppendCrewUnit(arg_60_1)
	arg_60_0._fleetRangeAntiAir.AppendCrewUnit(arg_60_1)
	arg_60_0._fleetStaticSonar.AppendCrewUnit(arg_60_1)

	local var_60_3 = {}

	for iter_60_6, iter_60_7 in ipairs(arg_60_0._unitList):
		table.insert(var_60_3, iter_60_6)

	arg_60_0.refreshFleetFormation(var_60_3)

def var_0_9.appendSubUnit(arg_61_0, arg_61_1):
	arg_61_0._subList[#arg_61_0._subList + 1] = arg_61_1

	arg_61_1.SetMainUnitIndex(#arg_61_0._subList)

def var_0_9.FleetWarcry(arg_62_0):
	local var_62_0
	local var_62_1 = math.random(0, 1)
	local var_62_2 = arg_62_0.GetScoutList()[1]
	local var_62_3 = arg_62_0.GetMainList()[1]

	if var_62_3 == None or var_62_1 == 0:
		var_62_0 = var_62_2
	elif var_62_1 == 1:
		var_62_0 = var_62_3

	local var_62_4 = "battle"
	local var_62_5 = var_62_0.GetIntimacy()
	local var_62_6 = var_0_0.Battle.BattleDataFunction.GetWords(var_62_0.GetSkinID(), var_62_4, var_62_5)

	var_62_0.DispatchVoice(var_62_4)
	var_62_0.DispatchChat(var_62_6, 2.5, var_62_4)

def var_0_9.FleetUnitSpwanFinish(arg_63_0):
	local var_63_0 = 0

	for iter_63_0, iter_63_1 in ipairs(arg_63_0._unitList):
		var_63_0 = var_63_0 + iter_63_1.GetGearScore()

	for iter_63_2, iter_63_3 in ipairs(arg_63_0._unitList):
		var_0_8.SetCurrent(iter_63_3, "fleetGS", var_63_0)

def var_0_9.SubWarcry(arg_64_0):
	local var_64_0 = arg_64_0.GetSubList()[1]
	local var_64_1 = "battle"
	local var_64_2 = var_64_0.GetIntimacy()
	local var_64_3 = var_0_0.Battle.BattleDataFunction.GetWords(var_64_0.GetSkinID(), var_64_1, var_64_2)

	var_64_0.DispatchVoice(var_64_1)
	var_64_0.DispatchChat(var_64_3, 2.5, var_64_1)

def var_0_9.SetWeaponBlock(arg_65_0, arg_65_1):
	arg_65_0._blockCast = arg_65_0._blockCast + arg_65_1

def var_0_9.GetWeaponBlock(arg_66_0):
	return arg_66_0._blockCast > 0

def var_0_9.CastChargeWeapon(arg_67_0):
	if arg_67_0.GetWeaponBlock():
		return

	local var_67_0 = arg_67_0._chargeWeaponVO.GetCurrentWeapon()

	if var_67_0 != None and var_67_0.GetCurrentState() == var_67_0.STATE_READY:
		var_67_0.Charge()

		local var_67_1 = {}
		local var_67_2 = var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.POINT_HIT_CHARGE, var_67_1)

		arg_67_0.DispatchEvent(var_67_2)

def var_0_9.CancelChargeWeapon(arg_68_0):
	local var_68_0 = arg_68_0._chargeWeaponVO.GetCurrentWeapon()

	if var_68_0 != None and var_68_0.GetCurrentState() == var_68_0.STATE_PRECAST:
		local var_68_1 = {}
		local var_68_2 = var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.POINT_HIT_CANCEL, var_68_1)

		arg_68_0.DispatchEvent(var_68_2)
		var_68_0.CancelCharge()

def var_0_9.UnleashChrageWeapon(arg_69_0):
	if arg_69_0.GetWeaponBlock():
		arg_69_0.CancelChargeWeapon()

		return

	local var_69_0 = arg_69_0._chargeWeaponVO.GetCurrentWeapon()

	if var_69_0 != None and var_69_0.GetCurrentState() == var_69_0.STATE_PRECAST:
		if var_69_0.IsStrikeMode():
			local var_69_1 = arg_69_0._motionVO.GetPos().x + var_0_5.ChargeWeaponConfig.SIGHT_C
			local var_69_2 = math.min(var_69_1, arg_69_0._totalRightBound)

			arg_69_0.fireChargeWeapon(var_69_0, True, Vector3.New(var_69_2, 0, arg_69_0._motionVO.GetPos().z))
		else
			var_69_0.CancelCharge()

		local var_69_3 = {}
		local var_69_4 = var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.POINT_HIT_CANCEL, var_69_3)

		arg_69_0.DispatchEvent(var_69_4)

def var_0_9.QuickTagChrageWeapon(arg_70_0, arg_70_1):
	if arg_70_0.GetWeaponBlock():
		return

	local var_70_0 = arg_70_0._chargeWeaponVO.GetCurrentWeapon()

	if var_70_0 != None and var_70_0.GetCurrentState() == var_70_0.STATE_READY:
		var_70_0.QuickTag()

		if #var_70_0.GetLockList() <= 0:
			var_70_0.CancelQuickTag()
		else
			arg_70_0.fireChargeWeapon(var_70_0, arg_70_1)

def var_0_9.fireChargeWeapon(arg_71_0, arg_71_1, arg_71_2, arg_71_3):
	local var_71_0 = arg_71_1.GetHost()

	local function var_71_1()
		local function var_72_0()
			arg_71_1.Fire(arg_71_3)

		arg_71_1.DispatchBlink(var_72_0)

	if arg_71_2:
		if arg_71_0._IFF == var_0_5.FRIENDLY_CODE:
			arg_71_0._chargeWeaponVO.PlayCutIn(var_71_0, 1 / var_0_5.FOCUS_MAP_RATE)

		arg_71_0._chargeWeaponVO.PlayFocus(var_71_0, var_71_1)
	else
		if arg_71_0._IFF == var_0_5.FRIENDLY_CODE:
			arg_71_0._chargeWeaponVO.PlayCutIn(var_71_0, 1)

		var_71_1()

def var_0_9.UnleashAllInStrike(arg_74_0):
	if arg_74_0.GetWeaponBlock():
		return

	local var_74_0 = arg_74_0._airAssistVO.GetCurrentWeapon()

	if var_74_0 and var_74_0.GetCurrentState() == var_74_0.STATE_READY:
		local var_74_1 = var_74_0.GetHost()

		if arg_74_0._IFF == var_0_5.FRIENDLY_CODE and var_74_1.IsMainFleetUnit():
			arg_74_0._airAssistVO.PlayCutIn(var_74_1, 1)

		var_74_0.CLSBullet()
		var_74_0.DispatchBlink()
		var_74_0.Fire()

def var_0_9.CastTorpedo(arg_75_0):
	if arg_75_0.GetWeaponBlock():
		return

	local var_75_0 = arg_75_0._torpedoWeaponVO.GetCurrentWeapon()

	if var_75_0 != None and var_75_0.GetCurrentState() == var_75_0.STATE_READY:
		var_75_0.Prepar()

def var_0_9.CancelTorpedo(arg_76_0):
	local var_76_0 = arg_76_0._torpedoWeaponVO.GetCurrentWeapon()

	if var_76_0 != None and var_76_0.GetCurrentState() == var_76_0.STATE_PRECAST:
		var_76_0.Cancel()

def var_0_9.UnleashTorpedo(arg_77_0):
	if arg_77_0.GetWeaponBlock():
		arg_77_0.CancelTorpedo()

		return

	local var_77_0 = arg_77_0._torpedoWeaponVO.GetCurrentWeapon()

	if var_77_0 != None and var_77_0.GetCurrentState() == var_77_0.STATE_PRECAST:
		var_77_0.Fire()

def var_0_9.QuickCastTorpedo(arg_78_0):
	if arg_78_0.GetWeaponBlock():
		return

	local var_78_0 = arg_78_0._torpedoWeaponVO.GetCurrentWeapon()

	if var_78_0 != None and var_78_0.GetCurrentState() == var_78_0.STATE_READY:
		var_78_0.Fire(True)

def var_0_9.RemoveManunalTorpedo(arg_79_0, arg_79_1):
	if arg_79_1.IsAttacking():
		arg_79_0.CancelTorpedo()

	arg_79_0._torpedoWeaponVO.RemoveWeapon(arg_79_1)
	arg_79_1.Clear()

def var_0_9.CoupleEncourage(arg_80_0):
	local var_80_0 = {}
	local var_80_1 = {}

	for iter_80_0, iter_80_1 in ipairs(arg_80_0._unitList):
		local var_80_2 = iter_80_1.GetIntimacy()
		local var_80_3 = var_0_7.GetWords(iter_80_1.GetSkinID(), "couple_encourage", var_80_2)

		if #var_80_3 > 0:
			var_80_0[iter_80_1] = var_80_3

	local var_80_4 = var_0_4.CPChatType
	local var_80_5 = var_0_4.CPChatTargetFunc

	local function var_80_6(arg_81_0, arg_81_1)
		local var_81_0 = {}

		if arg_81_0 == var_80_4.GROUP_ID:
			var_81_0.groupIDList = arg_81_1
		elif arg_81_0 == var_80_4.SHIP_TYPE:
			var_81_0.ship_type_list = arg_81_1
		elif arg_81_0 == var_80_4.RARE:
			var_81_0.rarity = arg_81_1[1]
		elif arg_81_0 == var_80_4.NATIONALITY:
			var_81_0.nationality = arg_81_1[1]
		elif arg_81_0 == var_80_4.ILLUSTRATOR:
			var_81_0.illustrator = arg_81_1[1]
		elif arg_81_0 == var_80_4.TEAM:
			var_81_0.teamIndex = arg_81_1[1]

		return var_81_0

	for iter_80_2, iter_80_3 in pairs(var_80_0):
		for iter_80_4, iter_80_5 in ipairs(iter_80_3):
			local var_80_7 = iter_80_5[1]
			local var_80_8 = iter_80_5[2]
			local var_80_9 = iter_80_5[4] or var_80_4.GROUP_ID
			local var_80_10 = var_0_0.Battle.BattleTargetChoise.TargetAllHelp(iter_80_2)

			if type(var_80_9) == "table":
				for iter_80_6, iter_80_7 in ipairs(var_80_9):
					local var_80_11 = var_80_6(iter_80_7, var_80_7[iter_80_6])

					var_80_10 = var_0_0.Battle.BattleTargetChoise[var_80_5[iter_80_7]](iter_80_2, var_80_11, var_80_10)
			elif type(var_80_9) == "number":
				local var_80_12 = var_80_6(var_80_9, var_80_7)

				var_80_10 = var_0_0.Battle.BattleTargetChoise[var_80_5[var_80_9]](iter_80_2, var_80_12, var_80_10)

			if var_80_8 <= #var_80_10:
				local var_80_13 = {
					cp = iter_80_2,
					content = iter_80_5[3],
					linkIndex = iter_80_4
				}

				var_80_1[#var_80_1 + 1] = var_80_13

	if #var_80_1 > 0:
		local var_80_14 = var_80_1[math.random(#var_80_1)]
		local var_80_15 = "link" .. var_80_14.linkIndex

		var_80_14.cp.DispatchVoice(var_80_15)
		var_80_14.cp.DispatchChat(var_80_14.content, 3, var_80_15)

def var_0_9.onUnitUpdateHP(arg_82_0, arg_82_1):
	local var_82_0 = arg_82_1.Dispatcher
	local var_82_1 = arg_82_1.Data.dHP

	for iter_82_0, iter_82_1 in ipairs(arg_82_0._unitList):
		iter_82_1.TriggerBuff(var_0_4.BuffEffectType.ON_FRIENDLY_HP_RATIO_UPDATE, {
			unit = var_82_0,
			dHP = var_82_1
		})

		if iter_82_1 != var_82_0:
			iter_82_1.TriggerBuff(var_0_4.BuffEffectType.ON_TEAMMATE_HP_RATIO_UPDATE, {
				unit = var_82_0,
				dHP = var_82_1
			})

def var_0_9.SetSubUnitData(arg_83_0, arg_83_1):
	arg_83_0._subUntiDataList = arg_83_1

def var_0_9.GetSubUnitData(arg_84_0):
	return arg_84_0._subUntiDataList

def var_0_9.AddSubMarine(arg_85_0, arg_85_1):
	arg_85_1.InitOxygen()

	local var_85_0 = arg_85_1.GetTemplate()
	local var_85_1 = var_0_0.Battle.BattleUnitPhaseSwitcher.New(arg_85_1)

	local function var_85_2()
		return arg_85_1.GetRaidDuration()

	var_85_1.SetTemplateData(var_0_7.GeneratePlayerSubmarinPhase(arg_85_0._subAttackBaseLine, arg_85_0._subRetreatBaseLine, arg_85_1.GetAttrByName("raidDist"), var_85_2, arg_85_1.GetAttrByName("oxyAtkDuration")))

	arg_85_0._unitList[#arg_85_0._unitList + 1] = arg_85_1
	arg_85_0._subList[#arg_85_0._subList + 1] = arg_85_1

	arg_85_1.SetFleetVO(arg_85_0)
	arg_85_1.RegisterEventListener(arg_85_0, var_0_1.UPDATE_HP, arg_85_0.onUnitUpdateHP)

def var_0_9.AddManualSubmarine(arg_87_0, arg_87_1):
	arg_87_0._unitList[#arg_87_0._unitList + 1] = arg_87_1
	arg_87_0._manualSubList[#arg_87_0._manualSubList + 1] = arg_87_1
	arg_87_0._manualSubBench[#arg_87_0._manualSubBench + 1] = arg_87_1
	arg_87_0._maxCount = arg_87_0._maxCount + 1

	arg_87_1.InitOxygen()
	arg_87_1.SetFleetVO(arg_87_0)
	arg_87_1.SetMotion(arg_87_0._motionVO)
	arg_87_1.RegisterEventListener(arg_87_0, var_0_1.UPDATE_HP, arg_87_0.onUnitUpdateHP)

def var_0_9.GetSubList(arg_88_0):
	return arg_88_0._subList

def var_0_9.ShiftManualSub(arg_89_0):
	local var_89_0

	if arg_89_0._manualSubUnit:
		local var_89_1 = arg_89_0._manualSubUnit.GetTorpedoList()

		for iter_89_0, iter_89_1 in ipairs(var_89_1):
			if iter_89_1.IsAttacking():
				arg_89_0.CancelTorpedo()

			arg_89_0._torpedoWeaponVO.RemoveWeapon(iter_89_1)

		if arg_89_0._manualSubUnit.IsAlive():
			table.insert(arg_89_0._manualSubBench, arg_89_0._manualSubUnit)

		var_89_0 = arg_89_0._motionVO.GetPos().Clone()
	else
		var_89_0 = arg_89_0._manualSubList[1].GetPosition().Clone()

	arg_89_0._manualSubUnit = table.remove(arg_89_0._manualSubBench, 1)
	arg_89_0._scoutList[1] = arg_89_0._manualSubUnit

	local var_89_2 = {}

	for iter_89_2, iter_89_3 in ipairs(arg_89_0._manualSubBench):
		for iter_89_4, iter_89_5 in ipairs(arg_89_0._unitList):
			if iter_89_5 == iter_89_3:
				table.insert(var_89_2, iter_89_4)

				break

	for iter_89_6, iter_89_7 in ipairs(arg_89_0._unitList):
		if iter_89_7 == arg_89_0._manualSubUnit:
			table.insert(var_89_2, 1, iter_89_6)

			break

	arg_89_0.refreshFleetFormation(var_89_2)
	arg_89_0._manualSubUnit.SetMainUnitStatic(False)
	arg_89_0._manualSubUnit.SetPosition(var_89_0)
	arg_89_0.UpdateMotion()
	arg_89_0._submarineSpecialVO.SetUseable(False)

	local var_89_3 = arg_89_0._manualSubUnit.GetBuffList()

	for iter_89_8, iter_89_9 in pairs(var_89_3):
		if iter_89_9.IsSubmarineSpecial():
			arg_89_0._submarineSpecialVO.SetCount(1)
			arg_89_0._submarineSpecialVO.SetUseable(True)

			break

	arg_89_0.ChangeSubmarineState(var_0_0.Battle.OxyState.STATE_FREE_DIVE)
	arg_89_0._torpedoWeaponVO.Reset()

	local var_89_4 = arg_89_0._manualSubUnit.GetTorpedoList()

	for iter_89_10, iter_89_11 in ipairs(var_89_4):
		if iter_89_11.GetCurrentState() != iter_89_11.STATE_OVER_HEAT:
			arg_89_0._torpedoWeaponVO.AppendWeapon(iter_89_11)

	for iter_89_12, iter_89_13 in ipairs(var_89_4):
		if iter_89_13.GetCurrentState() == iter_89_13.STATE_OVER_HEAT:
			arg_89_0._torpedoWeaponVO.AppendWeapon(iter_89_13)

	for iter_89_14, iter_89_15 in ipairs(arg_89_0._manualSubBench):
		iter_89_15.SetPosition(var_0_5.SUB_BENCH_POS[iter_89_14])
		iter_89_15.SetMainUnitStatic(True)
		iter_89_15.ChangeOxygenState(var_0_0.Battle.OxyState.STATE_FREE_BENCH)

	arg_89_0._submarineShiftVO.ResetCurrent()

	if #arg_89_0._manualSubBench == 0:
		arg_89_0._submarineShiftVO.SetActive(False)

def var_0_9.ChangeSubmarineState(arg_90_0, arg_90_1, arg_90_2):
	if not arg_90_0._manualSubUnit:
		return

	arg_90_0._manualSubUnit.ChangeOxygenState(arg_90_1)

	if arg_90_2:
		for iter_90_0, iter_90_1 in ipairs(arg_90_0._submarineVOList):
			iter_90_1.ResetCurrent()

		local var_90_0 = arg_90_0._submarineShiftVO.GetMax() - arg_90_0._submarineShiftVO.GetCurrent()

		if arg_90_0._submarineShiftVO.IsOverLoad() and var_90_0 > var_0_5.SR_CONFIG.DIVE_CD:
			-- block empty
		else
			arg_90_0._submarineShiftVO.SetMax(var_0_5.SR_CONFIG.DIVE_CD)
			arg_90_0._submarineShiftVO.ResetCurrent()

	arg_90_0.DispatchEvent(var_0_0.Event.New(var_0_2.MANUAL_SUBMARINE_SHIFT, {
		state = arg_90_1
	}))

def var_0_9.SubmarinBoost(arg_91_0):
	arg_91_0._manualSubUnit.Boost(Vector3.right, var_0_5.SR_CONFIG.BOOST_SPEED, var_0_5.SR_CONFIG.BOOST_DECAY, var_0_5.SR_CONFIG.BOOST_DURATION, var_0_5.SR_CONFIG.BOOST_DECAY_STAMP)
	arg_91_0._submarineBoostVO.ResetCurrent()

def var_0_9.UnleashSubmarineSpecial(arg_92_0):
	if arg_92_0.GetWeaponBlock():
		return

	arg_92_0._submarineSpecialVO.Cast()
	arg_92_0._manualSubUnit.TriggerBuff(var_0_4.BuffEffectType.ON_SUBMARINE_FREE_SPECIAL)

def var_0_9.AppendIndieSonar(arg_93_0, arg_93_1, arg_93_2):
	local var_93_0 = var_0_0.Battle.BattleIndieSonar.New(arg_93_0, arg_93_1, arg_93_2)

	var_93_0.SwitchHost(arg_93_0._motionReferenceUnit)

	arg_93_0._indieSonarList[var_93_0] = True

	var_93_0.Detect()

def var_0_9.RemoveIndieSonar(arg_94_0, arg_94_1):
	for iter_94_0, iter_94_1 in pairs(arg_94_0._indieSonarList):
		if arg_94_1 == iter_94_0:
			arg_94_0._indieSonarList[iter_94_0] = None

			break

def var_0_9.AttachFleetBuff(arg_95_0, arg_95_1):
	local var_95_0 = arg_95_1.GetID()
	local var_95_1 = arg_95_0.GetFleetBuff(var_95_0)

	if var_95_1:
		var_95_1.Stack(arg_95_0)
	else
		arg_95_0._buffList[var_95_0] = arg_95_1

		arg_95_1.Attach(arg_95_0)

def var_0_9.RemoveFleetBuff(arg_96_0, arg_96_1):
	local var_96_0 = arg_96_0.GetFleetBuff(arg_96_1)

	if var_96_0:
		var_96_0.Remove()

def var_0_9.GetFleetBuff(arg_97_0, arg_97_1):
	return arg_97_0._buffList[arg_97_1]

def var_0_9.GetFleetBuffList(arg_98_0):
	return arg_98_0._buffList

def var_0_9.Jamming(arg_99_0, arg_99_1):
	if arg_99_1:
		arg_99_0._chargeWeaponVO.StartJamming()
		arg_99_0._torpedoWeaponVO.StartJamming()
		arg_99_0._airAssistVO.StartJamming()
	else
		arg_99_0._chargeWeaponVO.JammingEliminate()
		arg_99_0._torpedoWeaponVO.JammingEliminate()
		arg_99_0._airAssistVO.JammingEliminate()

def var_0_9.Blinding(arg_100_0, arg_100_1):
	arg_100_0.DispatchEvent(var_0_0.Event.New(var_0_2.FLEET_BLIND, {
		isBlind = arg_100_1
	}))

def var_0_9.UpdateHorizon(arg_101_0):
	arg_101_0.DispatchEvent(var_0_0.Event.New(var_0_2.FLEET_HORIZON_UPDATE, {}))

def var_0_9.AutoBotUpdated(arg_102_0, arg_102_1):
	local var_102_0 = arg_102_1 and var_0_4.BuffEffectType.ON_AUTOBOT or var_0_4.BuffEffectType.ON_MANUAL

	for iter_102_0, iter_102_1 in ipairs(arg_102_0._unitList):
		iter_102_1.TriggerBuff(var_102_0)

def var_0_9.CloakFatalExpose(arg_103_0):
	for iter_103_0, iter_103_1 in ipairs(arg_103_0._cloakList):
		iter_103_1.GetCloak().ForceToMax()

def var_0_9.CloakInVision(arg_104_0, arg_104_1):
	for iter_104_0, iter_104_1 in ipairs(arg_104_0._cloakList):
		iter_104_1.GetCloak().AppendExposeSpeed(arg_104_1)

def var_0_9.CloakOutVision(arg_105_0):
	for iter_105_0, iter_105_1 in ipairs(arg_105_0._cloakList):
		iter_105_1.GetCloak().AppendExposeSpeed(0)

def var_0_9.AttachCloak(arg_106_0, arg_106_1):
	if not arg_106_1.GetCloak():
		arg_106_1.InitCloak()

		arg_106_0._cloakList[#arg_106_0._cloakList + 1] = arg_106_1

def var_0_9.AttachNightCloak(arg_107_0):
	arg_107_0._scoutAimBias = var_0_0.Battle.BattleUnitAimBiasComponent.New()

	arg_107_0._scoutAimBias.ConfigRangeFormula(var_0_3.CalculateMaxAimBiasRange, var_0_3.CalculateBiasDecay)
	arg_107_0._scoutAimBias.Active(arg_107_0._scoutAimBias.STATE_ACTIVITING)
	arg_107_0.DispatchEvent(var_0_0.Event.New(var_0_2.ADD_AIM_BIAS, {
		aimBias = arg_107_0._scoutAimBias
	}))

def var_0_9.GetFleetBias(arg_108_0):
	return arg_108_0._scoutAimBias
