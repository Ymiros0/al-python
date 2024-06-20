ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleBuffCastSkill = class("BattleBuffCastSkill", var_0_0.Battle.BattleBuffEffect)
var_0_0.Battle.BattleBuffCastSkill.__name = "BattleBuffCastSkill"

local var_0_1 = var_0_0.Battle.BattleBuffCastSkill

var_0_1.FX_TYPE = var_0_0.Battle.BattleBuffEffect.FX_TYPE_CASTER

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0._castCount = 0
	arg_1_0._fireSkillDMGSum = 0

def var_0_1.GetEffectType(arg_2_0):
	return var_0_1.FX_TYPE

def var_0_1.GetGroupData(arg_3_0):
	return arg_3_0._group

def var_0_1.SetArgs(arg_4_0, arg_4_1, arg_4_2):
	arg_4_0._level = arg_4_2.GetLv()

	local var_4_0 = arg_4_0._tempData.arg_list

	arg_4_0._skill_id = var_4_0.skill_id
	arg_4_0._target = var_4_0.target or "TargetSelf"
	arg_4_0._check_target = var_4_0.check_target
	arg_4_0._check_weapon = var_4_0.check_weapon
	arg_4_0._check_spweapon = var_4_0.check_spweapon
	arg_4_0._check_target_gap = var_4_0.check_target_gap
	arg_4_0._time = var_4_0.time or 0

	local var_4_1 = pg.TimeMgr.GetInstance().GetCombatTime()

	if var_4_0.initialCD:
		arg_4_0._nextEffectTime = var_4_1
	else
		arg_4_0._nextEffectTime = var_4_1 + arg_4_0._time

	arg_4_0._minTargetNumber = var_4_0.minTargetNumber or 0
	arg_4_0._maxTargetNumber = var_4_0.maxTargetNumber or 10000
	arg_4_0._minWeaponNumber = var_4_0.minWeaponNumber or 0
	arg_4_0._maxWeaponNumber = var_4_0.maxWeaponNumber or 10000
	arg_4_0._rant = var_4_0.rant or 10000
	arg_4_0._streak = var_4_0.streakRange
	arg_4_0._dungeonTypeList = var_4_0.dungeonTypeList
	arg_4_0._effectAttachData = var_4_0.effectAttachData
	arg_4_0._group = var_4_0.group
	arg_4_0._srcBuff = arg_4_2

def var_0_1.onBulletCreate(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	if not arg_5_0.equipIndexRequire(arg_5_3.equipIndex):
		return

	local var_5_0 = arg_5_3._bullet
	local var_5_1 = arg_5_0._tempData.arg_list.bulletTrigger

	local function var_5_2(arg_6_0, arg_6_1)
		if arg_6_0 and arg_6_0.IsAlive():
			arg_5_0.castSkill(arg_6_0, arg_6_1)

	var_5_0.SetBuffFun(var_5_1, var_5_2)

def var_0_1.onTrigger(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	return (arg_7_0.castSkill(arg_7_1, arg_7_3, arg_7_2))

def var_0_1.castSkill(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	local var_8_0 = pg.TimeMgr.GetInstance().GetCombatTime()

	if arg_8_0.IsInCD(var_8_0):
		return "overheat"

	if not var_0_0.Battle.BattleFormulas.IsHappen(arg_8_0._rant):
		return "chance"

	if arg_8_0._check_target:
		local var_8_1 = arg_8_0.getTargetList(arg_8_1, arg_8_0._check_target, arg_8_0._tempData.arg_list)

		if not var_8_1:
			return "check target none"

		local var_8_2 = #var_8_1

		if var_8_2 < arg_8_0._minTargetNumber:
			return "check target min"

		if var_8_2 > arg_8_0._maxTargetNumber:
			return "check target max"

	if arg_8_0._check_target_gap:
		local var_8_3 = arg_8_0.getTargetList(arg_8_1, arg_8_0._check_target_gap[1].target, arg_8_0._check_target_gap[1].arg)
		local var_8_4 = arg_8_0.getTargetList(arg_8_1, arg_8_0._check_target_gap[2].target, arg_8_0._check_target_gap[2].arg)
		local var_8_5 = math.abs(#var_8_3 - #var_8_4)

		if var_8_5 < arg_8_0._minTargetNumber:
			return "check target gap min"

		if var_8_5 > arg_8_0._maxTargetNumber:
			return "check target gap max"

	if arg_8_0._check_weapon:
		local var_8_6 = #var_0_1.GetEquipmentList(arg_8_1, arg_8_0._tempData.arg_list)

		if var_8_6 < arg_8_0._minWeaponNumber:
			return "check weapon min"

		if var_8_6 > arg_8_0._maxWeaponNumber:
			return "check weapon max"

	if arg_8_0._check_spweapon and not var_0_1.FilterSpWeapon(arg_8_1, arg_8_0._tempData.arg_list):
		return "check spweapon"

	if arg_8_0._hpUpperBound or arg_8_0._hpLowerBound:
		local var_8_7

		if not arg_8_2 or not arg_8_2.unit:
			var_8_7 = arg_8_1.GetHPRate()
		else
			var_8_7 = arg_8_2.unit.GetHPRate()

		if not arg_8_0.hpIntervalRequire(var_8_7):
			return "check hp"

	if arg_8_0._attrInterval:
		local var_8_8 = var_0_0.Battle.BattleAttr.GetBase(arg_8_1, arg_8_0._attrInterval)

		if not arg_8_0.attrIntervalRequire(var_8_8):
			return "check interval"

	if arg_8_0._streak and not var_0_1.GetWinningStreak(arg_8_0._streak):
		return "check winning streak"

	if arg_8_0._dungeonTypeList and not var_0_1.GetDungeonType(arg_8_0._dungeonTypeList):
		return "check dungeon"

	if arg_8_0._effectAttachData and not arg_8_0.BuffAttachDataCondition(arg_8_3):
		return "check attach data"

	if not arg_8_0.fleetAttrRequire(arg_8_1):
		return "check fleet attr"

	if arg_8_0._fleetAttrDeltaRequire and arg_8_2 and not arg_8_0.fleetAttrDelatRequire(arg_8_2.delta):
		return "check fleet attr delta"

	if not arg_8_0.stackRequire(arg_8_3):
		return "check buff stack"

	local var_8_9 = arg_8_0.getTargetList(arg_8_1, arg_8_0._target, arg_8_0._tempData.arg_list)

	var_0_1.super.onTrigger(arg_8_0, arg_8_1)

	for iter_8_0, iter_8_1 in ipairs(var_8_9):
		local var_8_10 = True

		if arg_8_0._group:
			local var_8_11 = iter_8_1.GetBuffList()

			for iter_8_2, iter_8_3 in pairs(var_8_11):
				for iter_8_4, iter_8_5 in ipairs(iter_8_3._effectList):
					if iter_8_5.GetEffectType() == var_0_1.FX_TYPE and iter_8_5.GetGroupData():
						local var_8_12 = iter_8_5.GetGroupData()

						if var_8_12.id == arg_8_0._group.id and var_8_12.level > arg_8_0._group.level:
							var_8_10 = False

							break

		if var_8_10:
			arg_8_0.spell(iter_8_1, arg_8_2)

	arg_8_0.enterCoolDown(var_8_0)

def var_0_1.IsInCD(arg_9_0, arg_9_1):
	return arg_9_1 < arg_9_0._nextEffectTime

def var_0_1.spell(arg_10_0, arg_10_1, arg_10_2):
	arg_10_0._skill = arg_10_0._skill or var_0_0.Battle.BattleSkillUnit.GenerateSpell(arg_10_0._skill_id, arg_10_0._level, arg_10_1, attData)

	if arg_10_2 and arg_10_2.target:
		arg_10_0._skill.SetTarget({
			arg_10_2.target
		})

	arg_10_0._skill.Cast(arg_10_1, arg_10_0._commander)

	arg_10_0._castCount = arg_10_0._castCount + 1

def var_0_1.enterCoolDown(arg_11_0, arg_11_1):
	if arg_11_0._time and arg_11_0._time > 0:
		arg_11_0._nextEffectTime = arg_11_1 + arg_11_0._time

def var_0_1.Interrupt(arg_12_0):
	var_0_1.super.Interrupt(arg_12_0)

	if arg_12_0._skill:
		arg_12_0._skill.Interrupt()

def var_0_1.Clear(arg_13_0):
	var_0_1.super.Clear(arg_13_0)

	if arg_13_0._skill:
		arg_13_0._skill.Clear()

		arg_13_0._skill = None

def var_0_1.BuffAttachDataCondition(arg_14_0, arg_14_1):
	local var_14_0 = True
	local var_14_1 = arg_14_1.GetEffectList()

	for iter_14_0, iter_14_1 in ipairs(var_14_1):
		for iter_14_2, iter_14_3 in ipairs(arg_14_0._effectAttachData):
			local var_14_2 = var_0_0.Battle.BattleFormulas.parseCompareBuffAttachData(iter_14_3, iter_14_1)

			var_14_0 = var_14_0 and var_14_2

	return var_14_0

def var_0_1.GetWinningStreak(arg_15_0):
	local var_15_0 = var_0_0.Battle.BattleDataProxy.GetInstance().GetWinningStreak()
	local var_15_1 = arg_15_0[1]
	local var_15_2 = arg_15_0[2]

	return var_15_1 <= var_15_0 and var_15_0 < var_15_2

def var_0_1.GetDungeonType(arg_16_0):
	local var_16_0 = var_0_0.Battle.BattleDataProxy.GetInstance().GetInitData().StageTmpId
	local var_16_1 = pg.expedition_data_template[var_16_0].type

	return table.contains(arg_16_0, var_16_1)

def var_0_1.GetEquipmentList(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_0.GetEquipment()
	local var_17_1 = {}

	for iter_17_0, iter_17_1 in ipairs(var_17_0):
		var_17_1[iter_17_0] = iter_17_1

	local var_17_2 = #var_17_1

	while var_17_2 > 0:
		local var_17_3 = var_17_1[var_17_2].equipment
		local var_17_4 = True

		if not var_17_3:
			var_17_4 = False
		else
			local var_17_5 = var_0_0.Battle.BattleDataFunction.GetEquipDataTemplate(var_17_3.id)

			if arg_17_1.weapon_group and not table.contains(arg_17_1.weapon_group, var_17_5.group):
				var_17_4 = False

			if arg_17_1.index and not table.contains(arg_17_1.index, var_17_2):
				var_17_4 = False

			if arg_17_1.type and not table.contains(arg_17_1.type, var_17_5.type):
				var_17_4 = False

			if arg_17_1.label:
				local var_17_6 = var_0_0.Battle.BattleDataFunction.GetWeaponDataFromID(var_17_3.id).label

				for iter_17_2, iter_17_3 in ipairs(arg_17_1.label):
					if not table.contains(var_17_6, iter_17_3):
						var_17_4 = False

						break

		if not var_17_4:
			table.remove(var_17_1, var_17_2)

		var_17_2 = var_17_2 - 1

	return var_17_1

def var_0_1.FilterSpWeapon(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_0.GetSpWeapon()
	local var_18_1 = True

	;(function()
		if not var_18_0:
			var_18_1 = False

			return

		local var_19_0 = var_0_0.Battle.BattleDataFunction.GetSpWeaponDataFromID(var_18_0.GetConfigID())

		if arg_18_1.type and not table.contains(arg_18_1.type, var_19_0.type):
			var_18_1 = False

		if arg_18_1.label:
			for iter_19_0, iter_19_1 in ipairs(arg_18_1.label):
				if not table.contains(var_19_0.label, iter_19_1):
					var_18_1 = False

					return)()

	return var_18_1 and var_18_0 or None

def var_0_1.GetCastCount(arg_20_0):
	return arg_20_0._castCount

def var_0_1.GetSkillFireDamageSum(arg_21_0):
	arg_21_0._fireSkillDMGSum = math.max(arg_21_0._skill and arg_21_0._skill.GetDamageSum() or 0, arg_21_0._fireSkillDMGSum)

	return arg_21_0._fireSkillDMGSum