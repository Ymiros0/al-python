ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = var_0_0.Battle.BattleAttr
local var_0_4 = var_0_0.Battle.BattleConst
local var_0_5 = var_0_4.EquipmentType
local var_0_6 = var_0_0.Battle.BattleConfig
local var_0_7 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_8 = var_0_0.Battle.BattleAttr

var_0_0.Battle.BattleCardPuzzlePlayerUnit = class("BattleCardPuzzlePlayerUnit", var_0_0.Battle.BattlePlayerUnit)
var_0_0.Battle.BattleCardPuzzlePlayerUnit.__name = "BattleCardPuzzlePlayerUnit"

local var_0_9 = var_0_0.Battle.BattleCardPuzzlePlayerUnit

def var_0_9.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_9.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

def var_0_9.UpdateHP(arg_2_0, arg_2_1, arg_2_2):
	if not arg_2_0.IsAlive():
		return

	local var_2_0 = arg_2_0.IsAlive()

	if not var_2_0:
		return

	local var_2_1 = arg_2_2.isMiss
	local var_2_2 = arg_2_2.isCri
	local var_2_3 = arg_2_2.isHeal
	local var_2_4 = arg_2_2.isShare
	local var_2_5 = arg_2_2.attr
	local var_2_6 = arg_2_2.font
	local var_2_7 = arg_2_2.cldPos
	local var_2_8 = arg_2_1
	local var_2_9 = arg_2_0.GetCurrentHP()

	if not var_2_3:
		local var_2_10 = {
			damage = -arg_2_1,
			isShare = var_2_4,
			miss = var_2_1,
			cri = var_2_2,
			damageSrc = arg_2_2.srcID,
			damageAttr = var_2_5
		}

		arg_2_0.TriggerBuff(var_0_4.BuffEffectType.ON_TAKE_DAMAGE, var_2_10)

		if var_2_9 <= var_2_10.damage:
			arg_2_0.TriggerBuff(var_0_4.BuffEffectType.ON_BEFORE_FATAL_DAMAGE, {})

		arg_2_1 = -var_2_10.damage

		if var_0_8.IsInvincible(arg_2_0):
			return 0
	else
		local var_2_11 = {
			damage = arg_2_1,
			isHeal = var_2_3
		}

		arg_2_0.TriggerBuff(var_0_4.BuffEffectType.ON_TAKE_HEALING, var_2_11)

		var_2_3 = var_2_11.isHeal
		arg_2_1 = var_2_11.damage

	local var_2_12 = math.min(arg_2_0.GetMaxHP(), math.max(0, var_2_9 + arg_2_1)) - var_2_9
	local var_2_13 = {
		preShieldHP = var_2_8,
		dHP = arg_2_1,
		validDHP = var_2_12,
		isMiss = var_2_1,
		isCri = var_2_2,
		isHeal = var_2_3,
		font = var_2_6
	}

	if var_2_7 and not var_2_7.EqualZero():
		local var_2_14 = arg_2_0.GetPosition()
		local var_2_15 = arg_2_0.GetBoxSize().x
		local var_2_16 = var_2_14.x - var_2_15
		local var_2_17 = var_2_14.x + var_2_15
		local var_2_18 = var_2_7.Clone()

		var_2_18.x = Mathf.Clamp(var_2_18.x, var_2_16, var_2_17)
		var_2_13.posOffset = var_2_14 - var_2_18

	arg_2_0.UpdateHPAction(var_2_13)

	if not arg_2_0.IsAlive() and var_2_0:
		arg_2_0.SetDeathReason(arg_2_2.damageReason)
		arg_2_0.DeadAction()

	if arg_2_0.IsAlive():
		arg_2_0.TriggerBuff(var_0_4.BuffEffectType.ON_HP_RATIO_UPDATE, {
			dHP = arg_2_1,
			unit = arg_2_0
		})

	return arg_2_1

def var_0_9.UpdateHPAction(arg_3_0, arg_3_1):
	arg_3_0.DispatchEvent(var_0_0.Event.New(var_0_7.UPDATE_COMMON_HP, arg_3_1))
	var_0_9.super.UpdateHPAction(arg_3_0, arg_3_1)

def var_0_9.SetTemplate(arg_4_0, arg_4_1, arg_4_2, arg_4_3):
	arg_4_0._tmpID = arg_4_1
	arg_4_0._tmpData = Clone(var_0_1.GetPuzzleShipDataTemplate(arg_4_0._tmpID))
	arg_4_0._tmpData.scale = 100
	arg_4_0._tmpData.parallel_max = {
		1,
		1,
		1
	}

	arg_4_0.configWeaponQueueParallel()
	arg_4_0.overrideSkin(arg_4_0._tmpData.skin_id, True)
	arg_4_0.InitCldComponent()
	arg_4_0.setAttrFromOutBattle(arg_4_2, arg_4_3)

	arg_4_0._personality = var_0_1.GetShipPersonality(2)

	var_0_3.SetCurrent(arg_4_0, "srcShipType", arg_4_0._tmpData.type)

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._tmpData.tag):
		arg_4_0.AddLabelTag(iter_4_1)

def var_0_9.GetTemplate(arg_5_0):
	return arg_5_0._tmpData

def var_0_9.InitCurrentHP(arg_6_0):
	return

def var_0_9.InitFleetCurrentHP(arg_7_0, arg_7_1):
	arg_7_0.TriggerBuff(var_0_4.BuffEffectType.ON_HP_RATIO_UPDATE, {})

def var_0_9.SetCurrentHP(arg_8_0, arg_8_1):
	return

def var_0_9.GetCurrentHP(arg_9_0):
	return arg_9_0._fleetCardPuzzleComponent.GetCurrentCommonHP()

def var_0_9.GetMaxHP(arg_10_0):
	return arg_10_0._fleetCardPuzzleComponent.GetTotalCommonHP()

def var_0_9.GetHP(arg_11_0):
	return arg_11_0.GetCurrentHP(), arg_11_0.GetMaxHP()

def var_0_9.GetHPRate(arg_12_0):
	return arg_12_0.GetCurrentHP() / arg_12_0.GetMaxHP()

def var_0_9.SetFleetVO(arg_13_0, arg_13_1):
	var_0_9.super.SetFleetVO(arg_13_0, arg_13_1)

	arg_13_0._fleetCardPuzzleComponent = arg_13_1.GetCardPuzzleComponent()

def var_0_9.LeaderSetting(arg_14_0):
	arg_14_0._warningValue = 1

def var_0_9.SetMainFleetUnit(arg_15_0, arg_15_1):
	arg_15_0._isMainFleetUnit = True

	arg_15_0.SetMainUnitStatic(True)

	arg_15_0._mainUnitWarningValue = 1

def var_0_9.CheckWeaponInitial(arg_16_0):
	return

def var_0_9.setWeapon(arg_17_0):
	local var_17_0 = arg_17_0._tmpData.default_equip

	for iter_17_0, iter_17_1 in ipairs(var_17_0):
		if iter_17_1 != 0:
			local var_17_1 = var_0_1.GetWeaponDataFromID(iter_17_1)

			for iter_17_2, iter_17_3 in ipairs(var_17_1):
				if iter_17_3 != -1:
					local var_17_2 = var_0_0.Battle.BattleDataFunction.CreateWeaponUnit(iter_17_3, arg_17_0, None, iter_17_0)

					arg_17_0._totalWeapon[#arg_17_0._totalWeapon + 1] = var_17_2

					if weaponType == var_0_4.EquipmentType.STRIKE_AIRCRAFT:
						-- block empty
					else
						assert(#var_17_1 < 2, "自动武器一组不允许配置多个")
						arg_17_0.AddAutoWeapon(var_17_2)

					if weaponType == var_0_4.EquipmentType.INTERCEPT_AIRCRAFT or weaponType == var_0_4.EquipmentType.STRIKE_AIRCRAFT:
						arg_17_0._hiveList[#arg_17_0._hiveList + 1] = var_17_2

					if weaponType == var_0_4.EquipmentType.ANTI_AIR:
						arg_17_0._AAList[#arg_17_0._AAList + 1] = var_17_2
