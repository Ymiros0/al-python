ys.Battle.BattleCardPuzzleFormulas = ys.Battle.BattleCardPuzzleFormulas or {}

local var_0_0 = ys.Battle.BattleCardPuzzleFormulas
local var_0_1 = ys.Battle.BattleConst
local var_0_2 = pg.gameset
local var_0_3 = ys.Battle.BattleAttr
local var_0_4 = ys.Battle.BattleConfig
local var_0_5 = ys.Battle.BattleConfig.AnitAirRepeaterConfig
local var_0_6 = pg.bfConsts
local var_0_7 = var_0_4.AMMO_DAMAGE_ENHANCE
local var_0_8 = var_0_4.AMMO_DAMAGE_REDUCE

var_0_0.CUSTOM_FORMULA = {
	double_energy = "energy*5+combo+2"
}

function var_0_0.CreateContextCalculateDamage(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	local var_1_0 = var_0_6.NUM1
	local var_1_1 = var_0_6.NUM0
	local var_1_2 = var_0_6.NUM10000
	local var_1_3 = var_0_6.DRATE
	local var_1_4 = var_0_6.ACCURACY
	local var_1_5 = arg_1_0:GetWeaponHostAttr()
	local var_1_6 = arg_1_0:GetWeapon()
	local var_1_7 = arg_1_0:GetWeaponTempData()
	local var_1_8 = var_1_7.type
	local var_1_9 = var_1_7.attack_attribute
	local var_1_10 = var_1_6:GetConvertedAtkAttr()
	local var_1_11 = arg_1_0:GetTemplate()
	local var_1_12 = var_1_11.damage_type
	local var_1_13 = var_1_11.random_damage_rate
	local var_1_14 = arg_1_1._attr
	local var_1_15 = arg_1_3 or var_1_0

	arg_1_2 = arg_1_2 or var_1_1

	local var_1_16 = var_1_14.armorType
	local var_1_17 = var_1_5.formulaLevel - var_1_14.formulaLevel
	local var_1_18 = var_1_0
	local var_1_19 = false
	local var_1_20 = false
	local var_1_21 = var_1_0
	local var_1_22 = arg_1_0:GetCorrectedDMG()
	local var_1_23 = (var_1_0 + arg_1_0:GetWeaponAtkAttr() * var_1_10) * var_1_22

	if var_1_9 == var_0_1.WeaponDamageAttr.CANNON then
		var_1_15 = var_1_0 + var_0_3.GetCurrent(arg_1_1, "injureRatioByCannon") + var_0_3.GetCurrent(arg_1_0, "damageRatioByCannon")
	elseif var_1_9 == var_0_1.WeaponDamageAttr.TORPEDO then
		var_1_15 = var_1_0 + var_0_3.GetCurrent(arg_1_1, "injureRatioByBulletTorpedo") + var_0_3.GetCurrent(arg_1_0, "damageRatioByBulletTorpedo")
	elseif var_1_9 == var_0_1.WeaponDamageAttr.AIR then
		local var_1_24 = var_0_3.GetCurrent(arg_1_0, "airResistPierceActive") == 1 and var_0_3.GetCurrent(arg_1_0, "airResistPierce") or 0

		var_1_15 = var_1_15 * math.min(var_1_3[7] / (var_1_14.antiAirPower + var_1_3[7]) + var_1_24, 1) * (var_1_0 + var_0_3.GetCurrent(arg_1_1, "injureRatioByAir") + var_0_3.GetCurrent(arg_1_0, "damageRatioByAir"))
	elseif var_1_9 == var_0_1.WeaponDamageAttr.ANTI_AIR then
		-- block empty
	elseif var_1_9 == var_0_1.WeaponDamageAttr.ANIT_SUB then
		-- block empty
	end

	local var_1_25 = var_1_5.luck - var_1_14.luck

	if var_0_3.GetCurrent(arg_1_1, "perfectDodge") == 1 then
		var_1_19 = true
	end

	if not var_1_19 then
		var_1_21 = var_1_23

		if var_0_3.GetCurrent(arg_1_0, "GCT") == 1 then
			var_1_20 = true
			var_1_18 = math.max(1, var_0_6.DFT_CRIT_EFFECT + var_0_3.GetCurrent(arg_1_0, "criDamage") - var_0_3.GetCurrent(arg_1_1, "criDamageResist"))
		else
			var_1_20 = false
		end
	else
		var_1_21 = var_1_1

		local var_1_26 = {
			isMiss = true,
			isDamagePrevent = false,
			isCri = var_1_20
		}

		return var_1_21, var_1_26
	end

	local var_1_27 = var_0_6.NUM1
	local var_1_28 = var_0_3.GetCurrent(arg_1_0, "damageRatioBullet")
	local var_1_29 = var_0_3.GetTagAttr(arg_1_0, arg_1_1)
	local var_1_30 = var_0_3.GetCurrent(arg_1_1, "injureRatio")
	local var_1_31 = (var_1_6:GetFixAmmo() or var_1_12[var_1_16] or var_1_27) + var_0_3.GetCurrent(arg_1_0, var_0_4.DAMAGE_AMMO_TO_ARMOR_RATE_ENHANCE[var_1_16])
	local var_1_32 = var_0_3.GetCurrent(arg_1_0, var_0_4.DAMAGE_TO_ARMOR_RATE_ENHANCE[var_1_16])
	local var_1_33 = var_0_3.GetCurrent(arg_1_0, var_0_7[var_1_11.ammo_type])
	local var_1_34 = var_0_3.GetCurrent(arg_1_1, var_0_8[var_1_11.ammo_type])
	local var_1_35 = var_0_3.GetCurrent(arg_1_0, "comboTag")
	local var_1_36 = var_0_3.GetCurrent(arg_1_1, var_1_35)
	local var_1_37 = math.max(var_1_27, math.floor(var_1_21 * var_1_15 * (var_1_27 - arg_1_2) * var_1_31 * (var_1_27 + var_1_32) * var_1_18 * (var_1_27 + var_1_28) * var_1_29 * (var_1_27 + var_1_30) * (var_1_27 + var_1_33 - var_1_34) * (var_1_27 + var_1_36) * (var_1_27 + math.min(var_1_3[1], math.max(-var_1_3[1], var_1_17)) * var_1_3[2])))

	if arg_1_1:GetCurrentOxyState() == var_0_1.OXY_STATE.DIVE then
		var_1_37 = math.floor(var_1_37 * var_1_11.antisub_enhancement)
	end

	local var_1_38 = {
		isMiss = var_1_19,
		isCri = var_1_20,
		damageAttr = var_1_9
	}
	local var_1_39 = arg_1_0:GetDamageEnhance()

	if var_1_39 ~= 1 then
		var_1_37 = math.floor(var_1_37 * var_1_39)
	end

	local var_1_40 = var_1_37 * var_1_14.repressReduce

	if var_1_13 ~= 0 then
		var_1_40 = var_1_40 * (Mathf.RandomFloat(var_1_13) + 1)
	end

	local var_1_41 = var_0_3.GetCurrent(arg_1_0, "damageEnhanceProjectile")
	local var_1_42 = math.max(0, var_1_40 + var_1_41) * arg_1_0:GetWeaponCardPuzzleEnhance()
	local var_1_43 = math.floor(var_1_42)
	local var_1_44 = var_1_11.DMG_font[var_1_16]

	if var_1_41 < 0 then
		var_1_44 = var_0_4.BULLET_DECREASE_DMG_FONT
	end

	return var_1_43, var_1_38, var_1_44
end

function var_0_0.parseCompare(arg_2_0, arg_2_1)
	local var_2_0, var_2_1 = string.find(arg_2_0, "%p+")
	local var_2_2 = string.sub(arg_2_0, var_2_0, var_2_1)
	local var_2_3 = string.sub(arg_2_0, 1, var_2_0 - 1)
	local var_2_4 = string.sub(arg_2_0, var_2_1 + 1, #arg_2_0)
	local var_2_5 = getCompareFuncByPunctuation(var_2_2)
	local var_2_6 = tonumber(var_2_3) or arg_2_1:GetCurrent(var_2_3)
	local var_2_7 = tonumber(var_2_4) or arg_2_1:GetCurrent(var_2_4)

	return var_2_5(var_2_6, var_2_7)
end

function var_0_0.parseFormula(arg_3_0, arg_3_1)
	local var_3_0 = {}
	local var_3_1 = {}

	for iter_3_0 in string.gmatch(arg_3_0, "%w+%.?%w*") do
		table.insert(var_3_0, iter_3_0)
	end

	for iter_3_1 in string.gmatch(arg_3_0, "[^%w%.]") do
		table.insert(var_3_1, iter_3_1)
	end

	local var_3_2 = {}
	local var_3_3 = {}
	local var_3_4 = 1
	local var_3_5 = var_3_0[1]

	var_3_5 = tonumber(var_3_5) or arg_3_1:GetCurrent(var_3_5)

	for iter_3_2, iter_3_3 in ipairs(var_3_1) do
		var_3_4 = var_3_4 + 1

		local var_3_6 = tonumber(var_3_0[var_3_4]) or arg_3_1:GetCurrent(var_3_0[var_3_4])

		if iter_3_3 == "+" or iter_3_3 == "-" then
			table.insert(var_3_3, var_3_5)

			var_3_5 = var_3_6

			table.insert(var_3_2, iter_3_3)
		elseif iter_3_3 == "*" or iter_3_3 == "/" then
			var_3_5 = getArithmeticFuncByOperator(iter_3_3)(var_3_5, var_3_6)
		end
	end

	table.insert(var_3_3, var_3_5)

	local var_3_7 = 1
	local var_3_8 = var_3_3[var_3_7]

	while var_3_7 < #var_3_3 do
		local var_3_9 = getArithmeticFuncByOperator(var_3_2[var_3_7])

		var_3_7 = var_3_7 + 1
		var_3_8 = var_3_9(var_3_8, var_3_3[var_3_7])
	end

	return var_3_8
end
