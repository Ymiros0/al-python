ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig
local var_0_2 = var_0_0.Battle.BattleVariable

var_0_0.Battle.BattleSkillUnit = class("BattleSkillUnit")
var_0_0.Battle.BattleSkillUnit.__name = "BattleSkillUnit"

local var_0_3 = var_0_0.Battle.BattleSkillUnit

def var_0_3.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0._id = arg_1_1
	arg_1_0._level = arg_1_2
	arg_1_0._tempData = var_0_0.Battle.BattleDataFunction.GetSkillTemplate(arg_1_1, arg_1_2)
	arg_1_0._cd = arg_1_0._tempData.cd
	arg_1_0._effectList = {}
	arg_1_0._lastEffectTarget = {}

	for iter_1_0, iter_1_1 in ipairs(arg_1_0._tempData.effect_list):
		local var_1_0 = iter_1_1.type

		arg_1_0._effectList[iter_1_0] = var_0_0.Battle[var_1_0].New(iter_1_1, arg_1_2)

	arg_1_0._finaleEffectCount = 0
	arg_1_0._dataProxy = var_0_0.Battle.BattleDataProxy.GetInstance()

def var_0_3.GenerateSpell(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	local var_2_0 = var_0_0.Battle.BattleSkillUnit.New(arg_2_0, arg_2_1)

	var_2_0._attachData = arg_2_3

	return var_2_0

def var_0_3.GetSkillEffectList(arg_3_0):
	return arg_3_0._effectList

def var_0_3.Cast(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = var_0_0.Battle.BattleState.GetInstance()

	if arg_4_0._tempData.focus_duration:
		arg_4_1.DispatchCutIn(arg_4_0._tempData)

	if arg_4_0._tempData.painting == 1:
		if arg_4_2:
			arg_4_1.DispatchSkillFloat(arg_4_2.getSkills()[1].getConfig("name"), arg_4_2.getPainting())
		else
			arg_4_1.DispatchSkillFloat(arg_4_0._tempData.name)
	elif type(arg_4_0._tempData.painting) == "string":
		arg_4_1.DispatchSkillFloat(arg_4_0._tempData.name, None, arg_4_0._tempData.painting)

	local var_4_1 = type(arg_4_0._tempData.castCV)

	if var_4_1 == "string":
		arg_4_1.DispatchVoice(arg_4_0._tempData.castCV)
	elif var_4_1 == "table":
		local var_4_2, var_4_3, var_4_4 = ShipWordHelper.GetWordAndCV(arg_4_0._tempData.castCV.skinID, arg_4_0._tempData.castCV.key)

		pg.CriMgr.GetInstance().PlaySoundEffect_V3(var_4_3)

	if arg_4_0._tempData.sfx:
		var_0_0.Battle.PlayBattleSFX(arg_4_0._tempData.sfx)

	local var_4_5 = arg_4_0._attachData

	for iter_4_0, iter_4_1 in ipairs(arg_4_0._effectList):
		local var_4_6 = iter_4_1.GetTarget(arg_4_1, arg_4_0)

		arg_4_0._lastEffectTarget = var_4_6

		iter_4_1.SetCommander(arg_4_2)

		if iter_4_1.IsFinaleEffect():
			arg_4_0._finaleEffectCount = arg_4_0._finaleEffectCount + 1

			local function var_4_7()
				arg_4_0.callbackCount(arg_4_1)

			iter_4_1.SetFinaleCallback(var_4_7)

		iter_4_1.Effect(arg_4_1, var_4_6, var_4_5)

	local var_4_8 = arg_4_0._tempData.aniEffect

	if var_4_8 and var_4_8 != "":
		local var_4_9 = {
			effect = var_4_8.effect,
			time = var_4_8.time,
			offset = var_4_8.offset,
			posFun = var_4_8.posFun
		}

		arg_4_1.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.ADD_EFFECT, var_4_9))

	if arg_4_0._tempData.action:
		arg_4_1.StateChange(var_0_0.Battle.UnitState.STATE_SKILL_START)

def var_0_3.SetTarget(arg_6_0, arg_6_1):
	arg_6_0._lastEffectTarget = arg_6_1

def var_0_3.Interrupt(arg_7_0):
	for iter_7_0, iter_7_1 in ipairs(arg_7_0._effectList):
		iter_7_1.Interrupt()

def var_0_3.Clear(arg_8_0):
	for iter_8_0, iter_8_1 in ipairs(arg_8_0._effectList):
		iter_8_1.Clear()

def var_0_3.callbackCount(arg_9_0, arg_9_1):
	arg_9_0._finaleEffectCount = arg_9_0._finaleEffectCount - 1

	if arg_9_0._finaleEffectCount == 0 and arg_9_0._tempData.action:
		arg_9_1.StateChange(var_0_0.Battle.UnitState.STATE_SKILL_END)

def var_0_3.GetDamageSum(arg_10_0):
	local var_10_0 = 0

	for iter_10_0, iter_10_1 in ipairs(arg_10_0._effectList):
		var_10_0 = iter_10_1.GetDamageSum() + var_10_0

	return var_10_0

def var_0_3.IsFireSkill(arg_11_0, arg_11_1):
	local var_11_0 = False
	local var_11_1 = var_0_0.Battle.BattleDataFunction.GetSkillTemplate(arg_11_0, arg_11_1)

	for iter_11_0, iter_11_1 in ipairs(var_11_1.effect_list):
		if iter_11_1.type == var_0_0.Battle.BattleSkillFire.__name or iter_11_1.type == var_0_0.Battle.BattleSkillFireSupport.__name:
			var_11_0 = True

			break

	return var_11_0
