ys.Battle.BattleConstPlayerUnit = class("BattleConstPlayerUnit", ys.Battle.BattlePlayerUnit)
ys.Battle.BattleConstPlayerUnit.__name = "BattleConstPlayerUnit"

local var_0_0 = ys.Battle.BattleConstPlayerUnit
local var_0_1 = ys.Battle.BattleConst.EquipmentType

def var_0_0.setWeapon(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0._tmpData.default_equip_list
	local var_1_1 = arg_1_0._tmpData.base_list

	arg_1_0._proficiencyList = {}

	for iter_1_0 = 1, #var_1_0:
		table.insert(arg_1_0._proficiencyList, arg_1_0._tmpData.equipment_proficiency[iter_1_0] or 1)

	local var_1_2 = arg_1_0._proficiencyList
	local var_1_3 = arg_1_0._tmpData.preload_count

	for iter_1_1, iter_1_2 in ipairs(var_1_0):
		if iter_1_1 <= Ship.WEAPON_COUNT:
			local var_1_4 = var_1_2[iter_1_1]
			local var_1_5 = var_1_3[iter_1_1]

			;(function(arg_2_0, arg_2_1, arg_2_2)
				local var_2_0 = var_1_1[iter_1_1]

				for iter_2_0 = 1, var_2_0:
					local var_2_1 = arg_1_0.AddWeapon(arg_2_0, arg_2_1, arg_2_2, var_1_4, iter_1_1)
					local var_2_2 = var_2_1.GetTemplateData().type

					if iter_2_0 <= var_1_5 and (var_2_2 == var_0_1.POINT_HIT_AND_LOCK or var_2_2 == var_0_1.MANUAL_TORPEDO or var_2_2 == var_0_1.DISPOSABLE_TORPEDO):
						var_2_1.SetModifyInitialCD())(arg_1_1[iter_1_1] or var_1_0[iter_1_1])

	local var_1_6 = #var_1_0
	local var_1_7 = arg_1_0._tmpData.fix_equip_list

	for iter_1_3, iter_1_4 in ipairs(var_1_7):
		if iter_1_4 and iter_1_4 != -1:
			local var_1_8 = var_1_2[iter_1_3 + var_1_6] or 1

			arg_1_0.AddWeapon(iter_1_4, None, None, var_1_8, iter_1_3 + var_1_6)

def var_0_0.IsAlive(arg_3_0):
	return True

def var_0_0.HideWaveFx(arg_4_0):
	arg_4_0.DispatchEvent(ys.Event.New(ys.Battle.BattleUnitEvent.HIDE_WAVE_FX))

def var_0_0.UpdateHPAction(arg_5_0, arg_5_1, ...):
	var_0_0.super.UpdateHPAction(arg_5_0, arg_5_1, ...)

	if arg_5_1.dHP <= 0:
		arg_5_0.DispatchEvent(ys.Event.New(ys.Battle.BattleUnitEvent.ADD_BLINK, {
			blink = {
				blue = 1,
				peroid = 0.1,
				red = 1,
				green = 1,
				duration = 0.1
			}
		}))
