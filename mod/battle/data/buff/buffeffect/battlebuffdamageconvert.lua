ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleAttr
local var_0_3 = var_0_0.Battle.BattleConst
local var_0_4 = class("BattleBuffDamageConvert", var_0_0.Battle.BattleBuffEffect)

var_0_0.Battle.BattleBuffDamageConvert = var_0_4
var_0_4.__name = "BattleBuffDamageConvert"
var_0_4.ATTR_PRE = {
	[var_0_3.WeaponDamageAttr.CANNON] = "injureRatioByCannon",
	[var_0_3.WeaponDamageAttr.TORPEDO] = "injureRatioByBulletTorpedo",
	[var_0_3.WeaponDamageAttr.AIR] = "injureRatioByAir"
}

function var_0_4.Ctor(arg_1_0, arg_1_1)
	var_0_4.super.Ctor(arg_1_0, arg_1_1)
end

function var_0_4.SetArgs(arg_2_0, arg_2_1, arg_2_2)
	local var_2_0 = arg_2_0._tempData.arg_list

	arg_2_0._convert = var_2_0.convert_rate
	arg_2_0._duration = var_2_0.duration
	arg_2_0._buffSkinID = var_2_0.buff_skin_id
	arg_2_0._attrTable = {}
end

function var_0_4.onTakeDamage(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	local var_3_0 = arg_3_3.damageAttr

	if var_3_0 then
		local var_3_1 = (arg_3_0._attrTable[var_3_0] or 0) + arg_3_3.damage

		arg_3_0._attrTable[var_3_0] = var_3_1
	end
end

function var_0_4.onRemove(arg_4_0, arg_4_1, arg_4_2)
	local var_4_0 = 0
	local var_4_1

	for iter_4_0, iter_4_1 in pairs(arg_4_0._attrTable) do
		if var_4_0 <= iter_4_1 then
			var_4_0 = iter_4_1
			var_4_1 = iter_4_0
		end
	end

	if not var_4_1 then
		return
	end

	local var_4_2 = var_0_4.ATTR_PRE[var_4_1]
	local var_4_3 = var_0_4.generateBuff(arg_4_0._buffSkinID, arg_4_0._duration, var_4_2, var_4_0 * arg_4_0._convert)
	local var_4_4 = var_0_0.Battle.BattleBuffSelfModifyUnit.New(var_4_3.id, 1, arg_4_1, var_4_3)

	arg_4_1:AddBuff(var_4_4)
end

function var_0_4.generateBuff(arg_5_0, arg_5_1, arg_5_2, arg_5_3)
	return {
		id = arg_5_0,
		icon = arg_5_0,
		time = arg_5_1,
		blink = {
			0,
			0.7,
			1,
			0.3,
			0.3
		},
		effect_list = {
			{
				type = "BattleBuffAddAttr",
				trigger = {
					"onAttach",
					"onRemove"
				},
				arg_list = {
					attr = arg_5_2,
					number = arg_5_3,
					group = arg_5_0
				}
			}
		},
		{
			time = arg_5_1
		},
		name = "代码生成buff",
		init_effect = "jinengchufablue",
		stack = 1,
		picture = "",
		last_effect = "",
		desc = "代码生成buff-指定属性减伤"
	}
end
