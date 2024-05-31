ys = ys or {}

local var_0_0 = ys
local var_0_1 = class("BattleBuffField", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffField = var_0_1
var_0_1.__name = "BattleBuffField"

local var_0_2 = var_0_0.Battle.BattleConst

def var_0_1.Ctor(arg_1_0, arg_1_1):
	var_0_1.super.Ctor(arg_1_0, arg_1_1)

def var_0_1.SetArgs(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._level = arg_2_2.GetLv()
	arg_2_0._caster = arg_2_2.GetCaster()

	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._auraBuffID = var_2_0.buff_id
	arg_2_0._target = var_2_0.target
	arg_2_0._check_target = var_2_0.check_target or "TargetNull"
	arg_2_0._isUpdateAura = var_2_0.FAura

	local var_2_1 = True
	local var_2_2 = type(arg_2_0._target)

	if var_2_2 == "string" and arg_2_0._target == "TargetAllHarm" or var_2_2 == "table" and table.contains(arg_2_0._target, "TargetAllHarm") or var_2_2 == "string" and arg_2_0._target == "TargetAllFoe" or var_2_2 == "table" and table.contains(arg_2_0._target, "TargetAllFoe"):
		var_2_1 = False

	local function var_2_3(arg_3_0)
		for iter_3_0, iter_3_1 in ipairs(arg_3_0):
			if iter_3_1.Active:
				local var_3_0 = arg_2_0.getTargetList(arg_2_1, arg_2_0._target, arg_2_0._tempData.arg_list)

				for iter_3_2, iter_3_3 in ipairs(var_3_0):
					if iter_3_3.GetUniqueID() == iter_3_1.UID:
						local var_3_1 = var_0_0.Battle.BattleBuffUnit.New(arg_2_0._auraBuffID, arg_2_0._level, arg_2_0._caster)

						iter_3_3.AddBuff(var_3_1)

						break

	local function var_2_4(arg_4_0)
		if arg_4_0.Active:
			local var_4_0 = arg_2_0.getTargetList(arg_2_1, arg_2_0._target, arg_2_0._tempData.arg_list)

			for iter_4_0, iter_4_1 in ipairs(var_4_0):
				if iter_4_1.GetUniqueID() == arg_4_0.UID:
					iter_4_1.RemoveBuff(arg_2_0._auraBuffID)

					break

	local var_2_5 = arg_2_0._isUpdateAura and var_2_4 or None
	local var_2_6 = arg_2_0._isUpdateAura and True or False
	local var_2_7 = var_0_0.Battle.BattleDataProxy.GetInstance()
	local var_2_8, var_2_9, var_2_10, var_2_11 = var_2_7.GetFieldBound()
	local var_2_12 = Vector3((var_2_10 + var_2_11) * 0.5, 0, (var_2_8 + var_2_9) * 0.5)
	local var_2_13 = math.abs(var_2_11 - var_2_10)
	local var_2_14 = math.abs(var_2_8 - var_2_9)

	arg_2_0._aura = var_2_7.SpawnLastingCubeArea(var_0_2.AOEField.SURFACE, arg_2_1.GetIFF(), var_2_12, var_2_13, var_2_14, 0, var_2_3, var_2_4, var_2_1, None, var_2_5, var_2_6)

def var_0_1.Clear(arg_5_0):
	arg_5_0._aura.SetActiveFlag(False)

	arg_5_0._aura = None

	var_0_1.super.Clear(arg_5_0)
