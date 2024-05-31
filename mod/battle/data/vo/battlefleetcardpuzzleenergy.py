ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_4 = var_0_0.Battle.BattleFormulas
local var_0_5 = var_0_0.Battle.BattleConst
local var_0_6 = var_0_0.Battle.BattleConfig
local var_0_7 = var_0_0.Battle.BattleAttr
local var_0_8 = var_0_0.Battle.BattleDataFunction
local var_0_9 = var_0_0.Battle.BattleAttr
local var_0_10 = var_0_0.Battle.BattleCardPuzzleConfig
local var_0_11 = class("BattleFleetCardPuzzleEnergy")

var_0_0.Battle.BattleFleetCardPuzzleEnergy = var_0_11
var_0_11.__name = "BattleFleetCardPuzzleEnergy"

def var_0_11.Ctor(arg_1_0, arg_1_1):
	arg_1_0._client = arg_1_1
	arg_1_0._fleetAttr = arg_1_0._client.GetAttrManager()

	arg_1_0.init()

def var_0_11.CustomConfig(arg_2_0, arg_2_1):
	local var_2_0 = var_0_8.GetPuzzleDungeonTemplate(arg_2_1)

	arg_2_0._currentEnergy = var_2_0.init_energy
	arg_2_0._generateRate = var_2_0.energy_recovery

def var_0_11.Dispose(arg_3_0):
	return

def var_0_11.GetMaxEnergy(arg_4_0):
	return arg_4_0._maxEnergy

def var_0_11.GetCurrentEnergy(arg_5_0):
	return arg_5_0._currentEnergy

def var_0_11.GetGeneratingProcess(arg_6_0):
	if arg_6_0._currentEnergy == arg_6_0._maxEnergy:
		return 1
	else
		return arg_6_0._energyGenerating

def var_0_11.ConsumeEnergy(arg_7_0, arg_7_1):
	arg_7_0._currentEnergy = math.max(arg_7_0._currentEnergy - arg_7_1, 0)

	arg_7_0._client.EnergyUpdate()

	if arg_7_1 > 0:
		arg_7_0._client.FlushHandOverheat()

def var_0_11.Update(arg_8_0, arg_8_1):
	arg_8_0.update(arg_8_1)

def var_0_11.init(arg_9_0):
	arg_9_0._currentEnergy = var_0_10.baseEnergyInitial
	arg_9_0._maxEnergy = 10
	arg_9_0._generateRate = var_0_10.baseEnergyGenerateSpeedPerSecond
	arg_9_0._energyGenerating = 0

def var_0_11.updateTimeStamp(arg_10_0):
	arg_10_0._lastUpdateTimeStamp = pg.TimeMgr.GetInstance().GetCombatTime()

def var_0_11.Start(arg_11_0):
	arg_11_0.updateTimeStamp()

def var_0_11.update(arg_12_0, arg_12_1):
	if arg_12_0._currentEnergy < arg_12_0._maxEnergy:
		arg_12_0._energyGenerating = (arg_12_1 - arg_12_0._lastUpdateTimeStamp) * arg_12_0.getCurrentSpeed() + arg_12_0._energyGenerating

		if arg_12_0._energyGenerating >= 1:
			arg_12_0._currentEnergy = arg_12_0._currentEnergy + 1

			arg_12_0._client.EnergyUpdate()

			arg_12_0._energyGenerating = 0

	arg_12_0.updateTimeStamp()

def var_0_11.getCurrentSpeed(arg_13_0):
	local var_13_0 = arg_13_0._fleetAttr.GetCurrent("BaseEnergyBoostRate")
	local var_13_1 = arg_13_0._fleetAttr.GetCurrent("BaseEnergyBoostExtra")

	return (math.max(arg_13_0._generateRate * (1 + var_13_0) + var_13_1, 0))

def var_0_11.FillToCooldown(arg_14_0, arg_14_1):
	if arg_14_1 <= arg_14_0._currentEnergy:
		return 0
	else
		local var_14_0 = arg_14_0.getCurrentSpeed()
		local var_14_1 = (1 - arg_14_0._energyGenerating) / var_14_0

		if arg_14_1 - arg_14_0._currentEnergy >= 2:
			var_14_1 = 1 / var_14_0 * (arg_14_1 - arg_14_0._currentEnergy - 1) + var_14_1

		return var_14_1
