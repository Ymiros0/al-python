ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleConst
local var_0_3 = var_0_0.Battle.BattleFormulas
local var_0_4 = var_0_0.Battle.BattleAttr
local var_0_5 = var_0_0.Battle.BattleConfig
local var_0_6 = var_0_0.Battle.BattleUnitEvent
local var_0_7 = var_0_0.Battle.UnitState
local var_0_8 = class("BattleEnemyUnit", var_0_0.Battle.BattleUnit)

var_0_0.Battle.BattleEnemyUnit = var_0_8
var_0_8.__name = "BattleEnemyUnit"

def var_0_8.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_8.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._type = var_0_2.UnitType.ENEMY_UNIT
	arg_1_0._level = arg_1_0._battleProxy.GetDungeonLevel()

def var_0_8.Dispose(arg_2_0):
	if arg_2_0._aimBias:
		arg_2_0._aimBias.Dispose()

	var_0_8.super.Dispose(arg_2_0)

def var_0_8.SetBound(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5, arg_3_6):
	var_0_8.super.SetBound(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5, arg_3_6)

	arg_3_0._weaponRightBound = arg_3_4
	arg_3_0._weaponLowerBound = arg_3_2

def var_0_8.UpdateAction(arg_4_0):
	if arg_4_0._oxyState and arg_4_0._oxyState.GetCurrentDiveState() == var_0_2.OXY_STATE.DIVE:
		if arg_4_0.GetSpeed().x > 0:
			arg_4_0._unitState.ChangeState(var_0_7.STATE_DIVELEFT)
		else
			arg_4_0._unitState.ChangeState(var_0_7.STATE_DIVE)
	elif arg_4_0.GetSpeed().x > 0:
		arg_4_0._unitState.ChangeState(var_0_7.STATE_MOVELEFT)
	else
		arg_4_0._unitState.ChangeState(var_0_7.STATE_MOVE)

def var_0_8.UpdateHP(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	local var_5_0 = var_0_8.super.UpdateHP(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4)

	if arg_5_0._phaseSwitcher:
		arg_5_0._phaseSwitcher.UpdateHP(arg_5_0.GetHPRate())

	return var_5_0

def var_0_8.SetMaster(arg_6_0, arg_6_1):
	arg_6_0._master = arg_6_1

def var_0_8.GetMaster(arg_7_0):
	return arg_7_0._master

def var_0_8.SetTemplate(arg_8_0, arg_8_1, arg_8_2):
	var_0_8.super.SetTemplate(arg_8_0, arg_8_1)

	arg_8_0._tmpData = var_0_1.GetMonsterTmpDataFromID(arg_8_0._tmpID)

	arg_8_0.configWeaponQueueParallel()
	arg_8_0.InitCldComponent()
	arg_8_0.SetAttr()

	arg_8_2 = arg_8_2 or {}

	local var_8_0 = arg_8_0.GetExtraInfo()

	for iter_8_0, iter_8_1 in pairs(arg_8_2):
		var_8_0[iter_8_0] = iter_8_1

	arg_8_0.setStandardLabelTag()

def var_0_8.SetTeamVO(arg_9_0, arg_9_1):
	arg_9_0._team = arg_9_1

def var_0_8.SetFormationIndex(arg_10_0, arg_10_1):
	arg_10_0._formationIndex = arg_10_1

def var_0_8.SetWaveIndex(arg_11_0, arg_11_1):
	arg_11_0._waveIndex = arg_11_1

def var_0_8.SetAttr(arg_12_0):
	var_0_4.SetEnemyAttr(arg_12_0)
	var_0_4.InitDOTAttr(arg_12_0._attr, arg_12_0._tmpData)

def var_0_8.GetTemplate(arg_13_0):
	return arg_13_0._tmpData

def var_0_8.GetRarity(arg_14_0):
	return arg_14_0._tmpData.rarity

def var_0_8.GetLevel(arg_15_0):
	return arg_15_0._overrideLevel or arg_15_0._level or 1

def var_0_8.GetTeam(arg_16_0):
	return arg_16_0._team

def var_0_8.GetWaveIndex(arg_17_0):
	return arg_17_0._waveIndex

def var_0_8.IsShowHPBar(arg_18_0):
	return arg_18_0._IFF != var_0_5.FRIENDLY_CODE

def var_0_8.IsSpectre(arg_19_0):
	local var_19_0
	local var_19_1 = var_0_0.Battle.BattleBuffSetBattleUnitType.ATTR_KEY

	if arg_19_0.GetAttr()[var_19_1] != None:
		var_19_0 = arg_19_0.GetAttrByName(var_19_1)
	else
		var_19_0 = arg_19_0._tmpData.battle_unit_type

	return var_19_0 <= var_0_5.SPECTRE_UNIT_TYPE, var_19_0

def var_0_8.InitCldComponent(arg_20_0):
	var_0_8.super.InitCldComponent(arg_20_0)

	local var_20_0 = {
		type = var_0_2.CldType.SHIP,
		IFF = arg_20_0.GetIFF(),
		UID = arg_20_0.GetUniqueID(),
		Mass = var_0_2.CldMass.L1,
		IsBoss = arg_20_0._isBoss
	}

	arg_20_0._cldComponent.SetCldData(var_20_0)

	if arg_20_0.GetTemplate().friendly_cld != 0:
		arg_20_0._cldComponent.ActiveFriendlyCld()

def var_0_8.ConfigBubbleFX(arg_21_0):
	arg_21_0._bubbleFX = arg_21_0._tmpData.bubble_fx[1]

	arg_21_0._oxyState.SetBubbleTemplate(arg_21_0._tmpData.bubble_fx[2], arg_21_0._tmpData.bubble_fx[3])
