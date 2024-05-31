local var_0_0 = ys.Battle.BattleDataProxy
local var_0_1 = ys.Battle.BattleEvent
local var_0_2 = ys.Battle.BattleFormulas
local var_0_3 = ys.Battle.BattleConst
local var_0_4 = ys.Battle.BattleConfig
local var_0_5 = ys.Battle.BattleDataFunction
local var_0_6 = ys.Battle.BattleAttr
local var_0_7 = ys.Battle.BattleVariable

def var_0_0.__debug__BlockCldUpdate__(arg_1_0, arg_1_1):
	arg_1_0.UpdateCountDown(arg_1_1)

	for iter_1_0, iter_1_1 in pairs(arg_1_0._fleetList):
		iter_1_1.UpdateMotion()

	for iter_1_2, iter_1_3 in pairs(arg_1_0._unitList):
		iter_1_3.Update(arg_1_1)

	for iter_1_4, iter_1_5 in pairs(arg_1_0._bulletList):
		local var_1_0 = iter_1_5.GetSpeed()
		local var_1_1 = iter_1_5.GetPosition()

		if var_1_1.x > arg_1_0._bulletRightBound and var_1_0.x > 0 or var_1_1.z < arg_1_0._bulletLowerBound and var_1_0.z < 0:
			arg_1_0.RemoveBulletUnit(iter_1_5.GetUniqueID())
		elif var_1_1.x < arg_1_0._bulletLeftBound and var_1_0.x < 0 and iter_1_5.GetType() != var_0_3.BulletType.BOMB:
			arg_1_0.RemoveBulletUnit(iter_1_5.GetUniqueID())
		else
			iter_1_5.Update(arg_1_1)

			if var_1_1.z > arg_1_0._bulletUpperBound and var_1_0.z > 0 or iter_1_5.IsOutRange(arg_1_1):
				iter_1_5.OutRange()

	for iter_1_6, iter_1_7 in pairs(arg_1_0._aircraftList):
		iter_1_7.Update(arg_1_1)

		local var_1_2, var_1_3 = iter_1_7.GetIFF()

		if var_1_2 == var_0_4.FRIENDLY_CODE:
			var_1_3 = arg_1_0._totalRightBound
		elif var_1_2 == var_0_4.FOE_CODE:
			var_1_3 = arg_1_0._totalLeftBound

		if iter_1_7.GetPosition().x * var_1_2 > math.abs(var_1_3) and iter_1_7.GetSpeed().x * var_1_2 > 0:
			iter_1_7.OutBound()

		if not iter_1_7.IsAlive():
			arg_1_0.KillAircraft(iter_1_7.GetUniqueID())

	for iter_1_8, iter_1_9 in pairs(arg_1_0._AOEList):
		iter_1_9.Settle()

		if iter_1_9.GetActiveFlag() == False:
			arg_1_0.RemoveAreaOfEffect(iter_1_9.GetUniqueID())

	for iter_1_10, iter_1_11 in pairs(arg_1_0._foeShipList):
		if iter_1_11.GetPosition().x + iter_1_11.GetBoxSize().x < arg_1_0._leftZoneLeftBound:
			iter_1_11.DeadAction()
			arg_1_0.KillUnit(iter_1_11.GetUniqueID())
			arg_1_0.HandleShipMissDamage(iter_1_11, arg_1_0._fleetList[var_0_4.FRIENDLY_CODE])
