﻿local var_0_0 = ys.Battle.BattleDataProxy
local var_0_1 = ys.Battle.BattleEvent
local var_0_2 = ys.Battle.BattleFormulas
local var_0_3 = ys.Battle.BattleConst
local var_0_4 = ys.Battle.BattleConfig
local var_0_5 = ys.Battle.BattleDataFunction
local var_0_6 = ys.Battle.BattleAttr
local var_0_7 = ys.Battle.BattleVariable

function var_0_0.SetupCalculateDamage(arg_1_0, arg_1_1)
	arg_1_0._calculateDamage = arg_1_1 or var_0_2.CreateContextCalculateDamage()
end

function var_0_0.SetupDamageKamikazeAir(arg_2_0, arg_2_1)
	arg_2_0._calculateDamageKamikazeAir = arg_2_1 or var_0_2.CalculateDamageFromAircraftToMainShip
end

function var_0_0.SetupDamageKamikazeShip(arg_3_0, arg_3_1)
	arg_3_0._calculateDamageKamikazeShip = arg_3_1 or var_0_2.CalculateDamageFromShipToMainShip
end

function var_0_0.SetupDamageCrush(arg_4_0, arg_4_1)
	arg_4_0._calculateDamageCrush = arg_4_1 or var_0_2.CalculateCrashDamage
end

function var_0_0.ClearFormulas(arg_5_0)
	arg_5_0._calculateDamage = nil
	arg_5_0._calculateDamageKamikazeAir = nil
	arg_5_0._calculateDamageKamikazeShip = nil
	arg_5_0._calculateDamageCrush = nil
end

function var_0_0.HandleBulletHit(arg_6_0, arg_6_1, arg_6_2)
	if not arg_6_2 then
		assert(false, "HandleBulletHit, but no vehicleData")

		return false
	elseif not arg_6_1 then
		assert(false, "HandleBulletHit, but no bulletData")

		return false
	end

	if var_0_6.IsSpirit(arg_6_2) then
		return false
	end

	if arg_6_1:IsCollided(arg_6_2:GetUniqueID()) == true then
		return
	end

	arg_6_1:Hit(arg_6_2:GetUniqueID(), arg_6_2:GetUnitType())

	local var_6_0 = {
		_bullet = arg_6_1,
		equipIndex = arg_6_1:GetWeapon():GetEquipmentIndex(),
		bulletTag = arg_6_1:GetExtraTag()
	}

	arg_6_1:BuffTrigger(ys.Battle.BattleConst.BuffEffectType.ON_BULLET_COLLIDE, var_6_0)

	if arg_6_2:GetUnitType() == var_0_3.UnitType.PLAYER_UNIT and arg_6_2:GetIFF() == var_0_4.FRIENDLY_CODE then
		ys.Battle.BattleCameraUtil.GetInstance():StartShake(pg.shake_template[var_0_3.ShakeType.HIT])
	end

	return true
end

function var_0_0.HandleDamage(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4)
	if arg_7_2:GetIFF() == var_0_4.FOE_CODE and arg_7_2:IsShowHPBar() then
		arg_7_0:DispatchEvent(ys.Event.New(var_0_1.HIT_ENEMY, arg_7_2))
	end

	local var_7_0 = arg_7_1:GetWeapon()
	local var_7_1 = arg_7_1:GetWeaponHostAttr()
	local var_7_2 = arg_7_1:GetExtraTag()
	local var_7_3 = var_7_0:GetTemplateData()
	local var_7_4 = {
		weaponType = var_7_3.attack_attribute,
		bulletType = arg_7_1:GetType(),
		bulletTag = var_7_2
	}

	arg_7_2:TriggerBuff(var_0_3.BuffEffectType.ON_BULLET_HIT_BEFORE, var_7_4)

	if var_0_6.IsInvincible(arg_7_2) then
		return
	end

	local var_7_5, var_7_6, var_7_7 = arg_7_0._calculateDamage(arg_7_1, arg_7_2, arg_7_3, arg_7_4)
	local var_7_8 = var_7_6.isMiss
	local var_7_9 = var_7_6.isCri
	local var_7_10 = var_7_6.damageAttr

	arg_7_1:AppendDamageUnit(arg_7_2:GetUniqueID())

	local var_7_11 = var_7_3.type
	local var_7_12 = var_7_0:GetEquipmentIndex()
	local var_7_13 = {
		target = arg_7_2,
		damage = var_7_5,
		weaponType = var_7_11,
		equipIndex = var_7_12,
		bulletTag = var_7_2
	}
	local var_7_14 = {
		isHeal = false,
		isMiss = var_7_8,
		isCri = var_7_9,
		attr = var_7_10,
		font = var_7_7,
		cldPos = arg_7_1:GetPosition(),
		srcID = var_7_1.battleUID
	}

	arg_7_1:GetWeapon():WeaponStatistics(var_7_5, var_7_9, var_7_8)

	local var_7_15 = arg_7_2:UpdateHP(var_7_5 * -1, var_7_14)

	arg_7_0:DamageStatistics(var_7_1.id, arg_7_2:GetAttrByName("id"), -var_7_15)

	if not var_7_8 and arg_7_1:GetWeaponTempData().type ~= var_0_3.EquipmentType.ANTI_AIR then
		arg_7_1:BuffTrigger(ys.Battle.BattleConst.BuffEffectType.ON_BULLET_HIT, var_7_13)

		local var_7_16 = arg_7_1:GetHost()

		if var_7_16 and var_7_16:IsAlive() and var_7_16:GetUnitType() ~= ys.Battle.BattleConst.UnitType.AIRFIGHTER_UNIT then
			if table.contains(var_0_3.AircraftUnitType, var_7_16:GetUnitType()) then
				var_7_16 = var_7_16:GetMotherUnit()
			end

			local var_7_17 = var_7_16:GetIFF()

			for iter_7_0, iter_7_1 in pairs(arg_7_0._unitList) do
				if iter_7_1:GetIFF() == var_7_17 and iter_7_1 ~= var_7_16 then
					iter_7_1:TriggerBuff(ys.Battle.BattleConst.BuffEffectType.ON_TEAMMATE_BULLET_HIT, var_7_13)
				end
			end
		end
	end

	local var_7_18 = arg_7_2:GetUnitType()
	local var_7_19 = true

	if var_7_18 ~= var_0_3.UnitType.AIRCRAFT_UNIT and var_7_18 ~= var_0_3.UnitType.AIRFIGHTER_UNIT and var_7_18 ~= var_0_3.UnitType.FUNNEL_UNIT and var_7_18 ~= var_0_3.UnitType.UAV_UNIT then
		var_7_19 = false
	end

	if arg_7_2:IsAlive() then
		if not var_7_19 then
			for iter_7_2, iter_7_3 in ipairs(arg_7_1:GetAttachBuff()) do
				if iter_7_3.hit_ignore or not var_7_8 then
					var_0_0.HandleBuffPlacer(iter_7_3, arg_7_1, arg_7_2)
				end
			end
		end

		if not var_7_8 then
			arg_7_2:TriggerBuff(var_0_3.BuffEffectType.ON_BE_HIT, var_7_4)
		end
	else
		arg_7_1:BuffTrigger(ys.Battle.BattleConst.BuffEffectType.ON_BULLET_KILL, {
			unit = arg_7_2,
			killer = arg_7_1
		})
		arg_7_0:obituary(arg_7_2, var_7_19, arg_7_1)
		arg_7_0:KillCountStatistics(var_7_1.id, arg_7_2:GetAttrByName("id"))
	end

	return var_7_8, var_7_9
end

function var_0_0.HandleMeteoDamage(arg_8_0, arg_8_1, arg_8_2)
	local var_8_0 = var_0_2.GetMeteoDamageRatio(#arg_8_2)

	for iter_8_0, iter_8_1 in ipairs(arg_8_2) do
		arg_8_0:HandleDamage(arg_8_1, iter_8_1, nil, var_8_0[iter_8_0])
	end
end

function var_0_0.HandleDirectDamage(arg_9_0, arg_9_1, arg_9_2, arg_9_3, arg_9_4)
	local var_9_0

	if arg_9_3 then
		var_9_0 = arg_9_3:GetAttrByName("id")
	end

	local var_9_1 = {
		isMiss = false,
		isCri = false,
		isHeal = false,
		damageReason = arg_9_4,
		srcID = var_9_0
	}
	local var_9_2 = arg_9_1:GetAttrByName("id")
	local var_9_3 = arg_9_1:UpdateHP(arg_9_2 * -1, var_9_1)
	local var_9_4 = arg_9_1:IsAlive()

	if arg_9_3 then
		arg_9_0:DamageStatistics(var_9_0, var_9_2, -var_9_3)

		if not var_9_4 then
			arg_9_0:KillCountStatistics(var_9_0, var_9_2)
		end
	end

	if not var_9_4 then
		local var_9_5 = arg_9_1:GetUnitType()
		local var_9_6 = true

		if var_9_5 ~= var_0_3.UnitType.AIRCRAFT_UNIT and var_9_5 ~= var_0_3.UnitType.AIRFIGHTER_UNIT and var_9_5 ~= var_0_3.UnitType.FUNNEL_UNIT and var_9_5 ~= var_0_3.UnitType.UAV_UNIT then
			var_9_6 = false
		end

		arg_9_0:obituary(arg_9_1, var_9_6, arg_9_3)
	end
end

function var_0_0.obituary(arg_10_0, arg_10_1, arg_10_2, arg_10_3)
	for iter_10_0, iter_10_1 in pairs(arg_10_0._unitList) do
		if iter_10_1 ~= arg_10_1 then
			if iter_10_1:GetIFF() == arg_10_1:GetIFF() then
				if arg_10_2 then
					iter_10_1:TriggerBuff(var_0_3.BuffEffectType.ON_FRIENDLY_AIRCRAFT_DYING, {
						unit = arg_10_1,
						killer = arg_10_3
					})
				elseif not arg_10_1:GetWorldDeathMark() then
					iter_10_1:TriggerBuff(var_0_3.BuffEffectType.ON_FRIENDLY_SHIP_DYING, {
						unit = arg_10_1,
						killer = arg_10_3
					})
				end
			elseif arg_10_2 then
				iter_10_1:TriggerBuff(var_0_3.BuffEffectType.ON_FOE_AIRCRAFT_DYING, {
					unit = arg_10_1,
					killer = arg_10_3
				})
			else
				iter_10_1:TriggerBuff(var_0_3.BuffEffectType.ON_FOE_DYING, {
					unit = arg_10_1,
					killer = arg_10_3
				})
			end
		end
	end
end

function var_0_0.HandleAircraftMissDamage(arg_11_0, arg_11_1, arg_11_2)
	if arg_11_2 == nil then
		return
	end

	local var_11_0 = arg_11_2:GetCloakList()

	for iter_11_0, iter_11_1 in ipairs(var_11_0) do
		iter_11_1:CloakExpose(arg_11_0._airExpose)
	end

	local var_11_1 = arg_11_1:GetPosition()
	local var_11_2 = arg_11_2:NearestUnitByType(var_11_1, ShipType.CloakShipTypeList)

	if var_11_2 then
		var_11_2:CloakExpose(arg_11_0._airExposeEX)
	end

	local var_11_3 = arg_11_2:RandomMainVictim({
		"immuneDirectHit"
	})

	if var_11_3 then
		local var_11_4 = arg_11_0._calculateDamageKamikazeAir(arg_11_1, var_11_3)

		var_11_3:TriggerBuff(var_0_3.BuffEffectType.ON_BE_HIT, {})
		arg_11_0:HandleDirectDamage(var_11_3, var_11_4, arg_11_1)
	end
end

function var_0_0.HandleShipMissDamage(arg_12_0, arg_12_1, arg_12_2)
	if arg_12_2 == nil then
		return
	end

	local var_12_0 = arg_12_2:GetCloakList()

	for iter_12_0, iter_12_1 in ipairs(var_12_0) do
		iter_12_1:CloakExpose(arg_12_0._shipExpose)
	end

	local var_12_1 = arg_12_1:GetPosition()
	local var_12_2 = arg_12_2:NearestUnitByType(var_12_1, ShipType.CloakShipTypeList)

	if var_12_2 then
		var_12_2:CloakExpose(arg_12_0._shipExposeEX)
	end

	local var_12_3 = arg_12_2:RandomMainVictim({
		"immuneDirectHit"
	})

	if var_12_3 then
		local var_12_4 = arg_12_1:GetTemplate().type

		if table.contains(TeamType.SubShipType, var_12_4) then
			local var_12_5 = var_0_2.CalculateDamageFromSubmarinToMainShip(arg_12_1, var_12_3)

			var_12_3:TriggerBuff(var_0_3.BuffEffectType.ON_BE_HIT, {})
			arg_12_0:HandleDirectDamage(var_12_3, var_12_5, arg_12_1)

			if var_12_3:IsAlive() and var_0_2.RollSubmarineDualDice(arg_12_1) then
				local var_12_6 = var_0_2.CalculateDamageFromSubmarinToMainShip(arg_12_1, var_12_3)

				var_12_3:TriggerBuff(var_0_3.BuffEffectType.ON_BE_HIT, {})
				arg_12_0:HandleDirectDamage(var_12_3, var_12_6, arg_12_1)
			end
		else
			local var_12_7 = arg_12_0._calculateDamageKamikazeShip(arg_12_1, var_12_3)

			var_12_3:TriggerBuff(var_0_3.BuffEffectType.ON_BE_HIT, {})
			arg_12_0:HandleDirectDamage(var_12_3, var_12_7, arg_12_1)
		end
	end
end

function var_0_0.HandleCrashDamage(arg_13_0, arg_13_1, arg_13_2)
	local var_13_0, var_13_1 = arg_13_0._calculateDamageCrush(arg_13_1, arg_13_2)

	arg_13_0:HandleDirectDamage(arg_13_1, var_13_0, arg_13_2, var_0_3.UnitDeathReason.CRUSH)
	arg_13_0:HandleDirectDamage(arg_13_2, var_13_1, arg_13_1, var_0_3.UnitDeathReason.CRUSH)
end

function var_0_0.HandleBuffPlacer(arg_14_0, arg_14_1, arg_14_2)
	local var_14_0 = var_0_5.GetBuffTemplate(arg_14_0.buff_id).effect_list
	local var_14_1 = false

	if var_14_0[1].type == "BattleBuffDOT" then
		if var_0_2.CaclulateDOTPlace(arg_14_0.rant, var_14_0[1], arg_14_1, arg_14_2) then
			var_14_1 = true
		end
	elseif var_0_2.IsHappen(arg_14_0.rant or 10000) then
		var_14_1 = true
	end

	if var_14_1 then
		local var_14_2 = ys.Battle.BattleBuffUnit.New(arg_14_0.buff_id, arg_14_0.level, arg_14_1)

		var_14_2:SetOrb(arg_14_1, arg_14_0.level)
		arg_14_2:AddBuff(var_14_2)
	end
end

function var_0_0.HandleDOTPlace(arg_15_0, arg_15_1, arg_15_2)
	local var_15_0 = arg_15_0.arg_list
	local var_15_1 = var_0_4.DOT_CONFIG[var_15_0.dotType]
	local var_15_2 = arg_15_1:GetAttrByName(var_15_1.hit)

	if var_0_2.IsHappen(var_15_0.ACC + arg_15_1:GetAttrByName(var_15_1.hit) - arg_15_2:GetAttrByName(var_15_1.resist)) then
		return true
	end

	return false
end

function var_0_0.HandleShipCrashDamageList(arg_16_0, arg_16_1, arg_16_2)
	local var_16_0 = arg_16_1:GetHostileCldList()

	for iter_16_0, iter_16_1 in pairs(var_16_0) do
		if not table.contains(arg_16_2, iter_16_0) then
			arg_16_1:RemoveHostileCld(iter_16_0)
		end
	end

	for iter_16_2, iter_16_3 in ipairs(arg_16_2) do
		if var_16_0[iter_16_3] == nil then
			local var_16_1

			local function var_16_2()
				arg_16_0:HandleCrashDamage(arg_16_0._unitList[iter_16_3], arg_16_1)
			end

			local var_16_3 = pg.TimeMgr.GetInstance():AddBattleTimer("shipCld", nil, var_0_4.SHIP_CLD_INTERVAL, var_16_2, true)

			arg_16_1:AppendHostileCld(iter_16_3, var_16_3)
			var_16_2()

			if not arg_16_1:IsAlive() then
				break
			end
		end
	end
end

function var_0_0.HandleShipCrashDecelerate(arg_18_0, arg_18_1, arg_18_2)
	if arg_18_2 == 0 and arg_18_1:IsCrash() then
		arg_18_1:SetCrash(false)
	elseif arg_18_2 > 0 and not arg_18_1:IsCrash() then
		arg_18_1:SetCrash(true)
	end
end

function var_0_0.HandleWallHitByBullet(arg_19_0, arg_19_1, arg_19_2)
	return (arg_19_1:GetCldFunc()(arg_19_2))
end

function var_0_0.HandleWallHitByShip(arg_20_0, arg_20_1, arg_20_2)
	arg_20_1:GetCldFunc()(arg_20_2)
end

function var_0_0.HandleWallDamage(arg_21_0, arg_21_1, arg_21_2)
	if arg_21_2:GetIFF() == var_0_4.FOE_CODE and arg_21_2:IsShowHPBar() then
		arg_21_0:DispatchEvent(ys.Event.New(var_0_1.HIT_ENEMY, arg_21_2))
	end

	local var_21_0 = var_0_6.GetCurrent(arg_21_1, "id")

	if var_0_6.IsInvincible(arg_21_2) then
		return
	end

	local var_21_1, var_21_2, var_21_3 = arg_21_0._calculateDamage(arg_21_1, arg_21_2)
	local var_21_4 = var_21_2.isMiss
	local var_21_5 = var_21_2.isCri
	local var_21_6 = var_21_2.damageAttr
	local var_21_7 = {
		isHeal = false,
		isMiss = var_21_4,
		isCri = var_21_5,
		attr = var_21_6,
		font = var_21_3,
		cldPos = arg_21_1:GetPosition(),
		srcID = var_21_0
	}
	local var_21_8 = arg_21_2:UpdateHP(var_21_1 * -1, var_21_7)

	arg_21_0:DamageStatistics(var_21_0, arg_21_2:GetAttrByName("id"), -var_21_8)

	if arg_21_2:IsAlive() then
		if not var_21_4 then
			arg_21_2:TriggerBuff(var_0_3.BuffEffectType.ON_BE_HIT, {})
		end
	else
		arg_21_0:obituary(arg_21_2, false, arg_21_1)
		arg_21_0:KillCountStatistics(var_21_0, arg_21_2:GetAttrByName("id"))
	end

	return var_21_4, var_21_5
end
