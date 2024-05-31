ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleDataFunction
local var_0_2 = var_0_0.Battle.BattleFormulas
local var_0_3 = var_0_0.Battle.BattleAttr
local var_0_4 = var_0_0.Battle.BattleConst
local var_0_5 = var_0_4.EquipmentType
local var_0_6 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattlePlayerUnit = class("BattlePlayerUnit", var_0_0.Battle.BattleUnit)
var_0_0.Battle.BattlePlayerUnit.__name = "BattlePlayerUnit"

local var_0_7 = var_0_0.Battle.BattlePlayerUnit

def var_0_7.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_7.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0._type = var_0_4.UnitType.PLAYER_UNIT

def var_0_7.Retreat(arg_2_0):
	var_0_7.super.Retreat(arg_2_0)
	arg_2_0.SetDeathReason(var_0_4.UnitDeathReason.LEAVE)
	arg_2_0.DeacActionClear()
	arg_2_0._battleProxy.ShutdownPlayerUnit(arg_2_0.GetUniqueID())
	arg_2_0._battleProxy.KillUnit(arg_2_0.GetUniqueID())

def var_0_7.DeadActionEvent(arg_3_0):
	arg_3_0.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.WILL_DIE, {}))
	arg_3_0.DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.SHUT_DOWN_PLAYER, {}))
	arg_3_0._unitState.ChangeState(var_0_0.Battle.UnitState.STATE_DEAD)

def var_0_7.IsSpectre(arg_4_0):
	local var_4_0
	local var_4_1 = var_0_0.Battle.BattleBuffSetBattleUnitType.ATTR_KEY

	if arg_4_0.GetAttr()[var_4_1] != None:
		var_4_0 = arg_4_0.GetAttrByName(var_4_1)
	else
		var_4_0 = var_0_6.PLAYER_DEFAULT

	return var_4_0 <= var_0_6.SPECTRE_UNIT_TYPE, var_4_0

def var_0_7.InitCurrentHP(arg_5_0, arg_5_1):
	arg_5_0.SetCurrentHP(math.ceil(arg_5_0.GetMaxHP() * arg_5_1))
	arg_5_0.TriggerBuff(var_0_4.BuffEffectType.ON_HP_RATIO_UPDATE, {})

def var_0_7.SetSkinId(arg_6_0, arg_6_1):
	arg_6_0._skinId = arg_6_1

def var_0_7.GetSkinID(arg_7_0):
	return arg_7_0._skinId

def var_0_7.GetDefaultSkinID(arg_8_0):
	return arg_8_0._tmpData.skin_id

def var_0_7.ActionKeyOffsetUseable(arg_9_0):
	return arg_9_0._skinData.spine_action_offset

def var_0_7.GetShipName(arg_10_0):
	return arg_10_0._shipName or arg_10_0._tmpData.name

def var_0_7.SetShipName(arg_11_0, arg_11_1):
	arg_11_0._shipName = arg_11_1

def var_0_7.SetTemplate(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	var_0_7.super.SetTemplate(arg_12_0, arg_12_1)

	arg_12_0._tmpData = var_0_1.GetPlayerShipTmpDataFromID(arg_12_0._tmpID)

	arg_12_0.configWeaponQueueParallel()
	arg_12_0.overrideWeaponInfo()
	arg_12_0.overrideSkin(arg_12_0._skinId, True)
	arg_12_0.InitCldComponent()

	arg_12_2.armorType = arg_12_0._tmpData.armor_type

	arg_12_0.setAttrFromOutBattle(arg_12_2, arg_12_3)
	var_0_3.InitDOTAttr(arg_12_0._attr, arg_12_0._tmpData)

	arg_12_0._personality = var_0_1.GetShipPersonality(2)

	for iter_12_0, iter_12_1 in ipairs(arg_12_0._tmpData.tag_list):
		arg_12_0.AddLabelTag(iter_12_1)

	arg_12_0.setStandardLabelTag()

def var_0_7.overrideSkin(arg_13_0, arg_13_1, arg_13_2):
	arg_13_0._skinData = var_0_1.GetPlayerShipSkinDataFromID(arg_13_1)

	local var_13_0 = {
		"prefab",
		"fx_container",
		"bound_bone",
		"smoke"
	}

	if arg_13_2:
		var_13_0[#var_13_0 + 1] = "painting"

	_.each(var_13_0, function(arg_14_0)
		arg_13_0._tmpData[arg_14_0] = arg_13_0._skinData[arg_14_0])

def var_0_7.overrideWeaponInfo(arg_15_0, arg_15_1, arg_15_2):
	if arg_15_0._overrideBaseInfo:
		arg_15_0._tmpData.base_list = arg_15_0._overrideBaseInfo

	if arg_15_0._overridePreloadInfo:
		arg_15_0._tmpData.preload_count = arg_15_0._overridePreloadInfo

def var_0_7.SetWeaponInfo(arg_16_0, arg_16_1, arg_16_2):
	arg_16_0._overrideBaseInfo = arg_16_1
	arg_16_0._overridePreloadInfo = arg_16_2

def var_0_7.SetRarity(arg_17_0, arg_17_1):
	arg_17_0._rarity = arg_17_1

def var_0_7.SetIntimacy(arg_18_0, arg_18_1):
	arg_18_0._intimacy = arg_18_1

def var_0_7.setWeapon(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_0._tmpData.default_equip_list
	local var_19_1 = arg_19_0._tmpData.base_list
	local var_19_2 = arg_19_0._proficiencyList
	local var_19_3 = arg_19_0._tmpData.preload_count

	for iter_19_0, iter_19_1 in ipairs(arg_19_1):
		if iter_19_1 and iter_19_1.skin and iter_19_1.skin != 0 and Equipment.IsOrbitSkin(iter_19_1.skin):
			arg_19_0._orbitSkinIDList = arg_19_0._orbitSkinIDList or {}

			table.insert(arg_19_0._orbitSkinIDList, iter_19_1.skin)

		if iter_19_0 <= Ship.WEAPON_COUNT:
			local var_19_4 = var_19_2[iter_19_0]
			local var_19_5 = var_19_3[iter_19_0]

			local function var_19_6(arg_20_0, arg_20_1, arg_20_2)
				local var_20_0 = var_19_1[iter_19_0]

				for iter_20_0 = 1, var_20_0:
					local var_20_1 = arg_19_0.AddWeapon(arg_20_0, arg_20_1, arg_20_2, var_19_4, iter_19_0)
					local var_20_2 = var_20_1.GetTemplateData().type

					if iter_20_0 <= var_19_5 and (var_20_2 == var_0_5.POINT_HIT_AND_LOCK or var_20_2 == var_0_5.MANUAL_MISSILE or var_20_2 == var_0_5.MANUAL_METEOR or var_20_2 == var_0_5.MANUAL_TORPEDO or var_20_2 == var_0_5.DISPOSABLE_TORPEDO):
						var_20_1.SetModifyInitialCD()

					if iter_19_1.equipment:
						var_20_1.SetSrcEquipmentID(iter_19_1.equipment.id)

			if iter_19_1.equipment and #iter_19_1.equipment.weapon_id > 0:
				local var_19_7 = iter_19_1.equipment.weapon_id

				for iter_19_2, iter_19_3 in ipairs(var_19_7):
					local var_19_8 = var_0_1.GetWeaponPropertyDataFromID(iter_19_3).type
					local var_19_9 = var_0_6.EQUIPMENT_ACTIVE_LIMITED_BY_TYPE[var_19_8]

					if (not var_19_9 or table.contains(var_19_9, arg_19_0._tmpData.type)) and iter_19_3 and iter_19_3 != -1:
						var_19_6(iter_19_3, iter_19_1.equipment.label, iter_19_1.skin)
			else
				local var_19_10 = var_19_0[iter_19_0]
				local var_19_11 = var_0_1.GetWeaponDataFromID(var_19_10)

				var_19_6(var_19_10, var_19_11.label)

	local var_19_12 = #var_19_0
	local var_19_13 = arg_19_0._tmpData.fix_equip_list

	for iter_19_4, iter_19_5 in ipairs(var_19_13):
		if iter_19_5 and iter_19_5 != -1:
			local var_19_14 = var_19_2[iter_19_4 + var_19_12] or 1

			arg_19_0.AddWeapon(iter_19_5, None, None, var_19_14, iter_19_4 + var_19_12).SetFixedFlag()

	if arg_19_0.CanDoAntiSub():
		local var_19_15 = {}

		for iter_19_6 = Ship.WEAPON_COUNT + 1, #arg_19_1:
			local var_19_16 = arg_19_1[iter_19_6]

			if var_19_16 and var_19_16.equipment and #var_19_16.equipment.weapon_id > 0:
				var_19_15[#var_19_15 + 1] = var_19_16.equipment.weapon_id[1]

		for iter_19_7, iter_19_8 in ipairs(arg_19_0._tmpData.depth_charge_list):
			var_19_15[#var_19_15 + 1] = iter_19_8

		local var_19_17 = 20
		local var_19_18 = 1

		for iter_19_9, iter_19_10 in ipairs(var_19_15):
			local var_19_19 = var_0_1.CreateWeaponUnit(iter_19_10, arg_19_0, var_19_18, var_19_17)

			arg_19_0.AddAutoWeapon(var_19_19)

def var_0_7.SetPriorityWeaponSkin(arg_21_0, arg_21_1):
	if not arg_21_0._priorityWeaponSkinID:
		arg_21_0._priorityWeaponSkinID = arg_21_1

def var_0_7.GetPriorityWeaponSkin(arg_22_0):
	return arg_22_0._priorityWeaponSkinID

def var_0_7.AddWeapon(arg_23_0, arg_23_1, arg_23_2, arg_23_3, arg_23_4, arg_23_5, arg_23_6):
	local var_23_0 = var_0_1.CreateWeaponUnit(arg_23_1, arg_23_0, arg_23_4, arg_23_5)

	arg_23_0._totalWeapon[#arg_23_0._totalWeapon + 1] = var_23_0

	if arg_23_2:
		var_23_0.SetEquipmentLabel(arg_23_2)

	local var_23_1 = var_23_0.GetTemplateData().type

	if var_23_1 == var_0_5.POINT_HIT_AND_LOCK or var_23_1 == var_0_5.MANUAL_METEOR or var_23_1 == var_0_5.MANUAL_MISSILE:
		arg_23_0._chargeList[#arg_23_0._chargeList + 1] = var_23_0

		arg_23_0._weaponQueue.AppendChargeWeapon(var_23_0)
	elif var_23_1 == var_0_5.MANUAL_TORPEDO or var_23_1 == var_0_5.DISPOSABLE_TORPEDO or var_23_1 == var_0_5.MANUAL_AAMISSILE:
		arg_23_0._manualTorpedoList[#arg_23_0._manualTorpedoList + 1] = var_23_0

		arg_23_0._weaponQueue.AppendManualTorpedo(var_23_0)
	elif var_23_1 == var_0_5.STRIKE_AIRCRAFT:
		-- block empty
	elif var_23_1 == var_0_5.FLEET_ANTI_AIR:
		arg_23_0.AddFleetAntiAirWeapon(var_23_0)
	elif var_23_1 == var_0_5.FLEET_RANGE_ANTI_AIR:
		arg_23_0.AddFleetRangeAntiAirWeapon(var_23_0)
	else
		arg_23_0.AddAutoWeapon(var_23_0)

	if var_23_1 == var_0_5.STRIKE_AIRCRAFT:
		arg_23_0._hiveList[#arg_23_0._hiveList + 1] = var_23_0

	if var_23_1 == var_0_5.ANTI_AIR:
		arg_23_0._AAList[#arg_23_0._AAList + 1] = var_23_0

	if arg_23_3 and arg_23_3 != 0:
		var_23_0.SetSkinData(arg_23_3)
		arg_23_0.SetPriorityWeaponSkin(arg_23_3)

	return var_23_0

def var_0_7.RemoveWeapon(arg_24_0, arg_24_1):
	local var_24_0 = var_0_1.GetWeaponPropertyDataFromID(arg_24_1).type
	local var_24_1

	if var_24_0 == var_0_5.STRIKE_AIRCRAFT:
		for iter_24_0, iter_24_1 in ipairs(arg_24_0._hiveList):
			if iter_24_1.GetWeaponId() == arg_24_1:
				var_24_1 = iter_24_1

				table.remove(arg_24_0._hiveList, iter_24_0)

				break
	elif var_24_0 == var_0_5.POINT_HIT_AND_LOCK or var_24_0 == var_0_5.MANUAL_METEOR or var_24_0 == var_0_5.MANUAL_MISSILE:
		-- block empty
	elif var_24_0 == var_0_5.MANUAL_TORPEDO:
		for iter_24_2, iter_24_3 in ipairs(arg_24_0._manualTorpedoList):
			if iter_24_3.GetWeaponId() == arg_24_1:
				var_24_1 = iter_24_3

				table.remove(arg_24_0._manualTorpedoList, iter_24_2)
				arg_24_0._weaponQueue.RemoveManualTorpedo(iter_24_3)

				break
	elif var_24_0 == var_0_5.FLEET_ANTI_AIR:
		for iter_24_4, iter_24_5 in ipairs(arg_24_0._fleetAAList):
			if iter_24_5.GetWeaponId() == arg_24_1:
				arg_24_0.RemoveFleetAntiAirWeapon(iter_24_5)

				break
	else
		for iter_24_6, iter_24_7 in ipairs(arg_24_0._autoWeaponList):
			if iter_24_7.GetWeaponId() == arg_24_1:
				var_24_1 = iter_24_7

				var_24_1.Clear()
				arg_24_0.RemoveAutoWeapon(var_24_1)

				break

	if var_24_1:
		for iter_24_8, iter_24_9 in ipairs(arg_24_0._totalWeapon):
			if iter_24_9 == var_24_1:
				table.remove(arg_24_0._totalWeapon, iter_24_8)

				break

	return var_24_1

def var_0_7.RemoveWeaponByLabel(arg_25_0, arg_25_1):
	local var_25_0

	for iter_25_0, iter_25_1 in ipairs(arg_25_0._totalWeapon):
		local var_25_1 = True

		for iter_25_2, iter_25_3 in ipairs(arg_25_1):
			local var_25_2 = iter_25_1.GetEquipmentLabel()

			var_25_1 = var_25_1 and table.contains(var_25_2, iter_25_3)

		if var_25_1:
			var_25_0 = iter_25_1

			table.remove(arg_25_0._totalWeapon, iter_25_0)

	if not var_25_0:
		return

	local var_25_3 = var_25_0.GetType()

	if var_25_3 == var_0_5.STRIKE_AIRCRAFT:
		for iter_25_4, iter_25_5 in ipairs(arg_25_0._hiveList):
			if var_25_0 == iter_25_5:
				table.remove(arg_25_0._hiveList, iter_25_4)

				break
	elif var_25_3 == var_0_5.POINT_HIT_AND_LOCK or var_25_3 == var_0_5.MANUAL_METEOR or var_25_3 == var_0_5.MANUAL_MISSILE:
		-- block empty
	elif var_25_3 == var_0_5.MANUAL_TORPEDO:
		for iter_25_6, iter_25_7 in ipairs(arg_25_0._manualTorpedoList):
			if var_25_0 == iter_25_7:
				table.remove(arg_25_0._manualTorpedoList, iter_25_6)
				arg_25_0._weaponQueue.RemoveManualTorpedo(iter_25_7)

				break
	elif var_25_3 == var_0_5.FLEET_ANTI_AIR:
		for iter_25_8, iter_25_9 in ipairs(arg_25_0._fleetAAList):
			if var_25_0 == iter_25_9:
				arg_25_0.RemoveFleetAntiAirWeapon(iter_25_9)

				break
	elif var_25_3 == var_0_5.INTERCEPT_AIRCRAFT:
		for iter_25_10, iter_25_11 in ipairs(arg_25_0._autoWeaponList):
			if var_25_0 == iter_25_11:
				arg_25_0.RemoveAutoWeapon(var_25_0)

				break
	else
		for iter_25_12, iter_25_13 in ipairs(arg_25_0._autoWeaponList):
			if var_25_0 == iter_25_13:
				arg_25_0.RemoveAutoWeapon(var_25_0)

				break

	return var_25_0

def var_0_7.AddFleetAntiAirWeapon(arg_26_0, arg_26_1):
	arg_26_0._fleetAAList[#arg_26_0._fleetAAList + 1] = arg_26_1

def var_0_7.RemoveFleetAntiAirWeapon(arg_27_0, arg_27_1):
	for iter_27_0, iter_27_1 in ipairs(arg_27_0._fleetAAList):
		if iter_27_1 == arg_27_1:
			table.remove(arg_27_0._fleetAAList, iter_27_0)

			return

def var_0_7.AddFleetRangeAntiAirWeapon(arg_28_0, arg_28_1):
	arg_28_0._fleetRangeAAList[#arg_28_0._fleetRangeAAList + 1] = arg_28_1

def var_0_7.RemoveFleetRangeAntiAirWeapon(arg_29_0, arg_29_1):
	for iter_29_0, iter_29_1 in ipairs(arg_29_0._fleetRangeAAList):
		if iter_29_1 == arg_29_1:
			table.remove(arg_29_0._fleetRangeAAList, iter_29_0)

			return

def var_0_7.ShiftWeapon(arg_30_0, arg_30_1):
	return

def var_0_7.GetManualWeaponParallel(arg_31_0):
	return arg_31_0._tmpData.parallel_max

def var_0_7.CeaseAllWeapon(arg_32_0, arg_32_1):
	if arg_32_1:
		for iter_32_0, iter_32_1 in ipairs(arg_32_0._totalWeapon):
			iter_32_1.Cease()

		local var_32_0 = arg_32_0._buffList

		for iter_32_2, iter_32_3 in pairs(var_32_0):
			iter_32_3.Interrupt()

	var_0_7.super.CeaseAllWeapon(arg_32_0, arg_32_1)

def var_0_7.LeaderSetting(arg_33_0):
	local var_33_0 = arg_33_0.GetIntimacy()
	local var_33_1 = var_0_1.GetWords(arg_33_0.GetSkinID(), "hp_warning", var_33_0)

	if var_33_1 and var_33_1 != "":
		arg_33_0._warningValue = var_0_6.WARNING_HP_RATE * arg_33_0.GetMaxHP()

def var_0_7.UpdateHP(arg_34_0, arg_34_1, arg_34_2, arg_34_3, arg_34_4):
	local var_34_0 = var_0_7.super.UpdateHP(arg_34_0, arg_34_1, arg_34_2, arg_34_3, arg_34_4)

	if arg_34_0._warningValue and arg_34_0._currentHP < arg_34_0._warningValue and not isHeal:
		arg_34_0._warningValue = None

		local var_34_1 = arg_34_0.GetIntimacy()
		local var_34_2 = "hp_warning"
		local var_34_3 = var_0_1.GetWords(arg_34_0.GetSkinID(), var_34_2, var_34_1)

		arg_34_0.DispatchVoice(var_34_2)
		arg_34_0.DispatchChat(var_34_3, 2.5, var_34_2)

	if arg_34_0._mainUnitWarningValue and arg_34_0._currentHP < arg_34_0._mainUnitWarningValue and arg_34_0._currentHP > 0 and not isHeal:
		arg_34_0._mainUnitWarningValue = None

		pg.TipsMgr.GetInstance().ShowTips(i18n("battle_main_emergent", arg_34_0.GetShipName()))

	return var_34_0

def var_0_7.SetMainFleetUnit(arg_35_0):
	var_0_7.super.SetMainFleetUnit(arg_35_0)

	if arg_35_0._IFF == var_0_6.FRIENDLY_CODE:
		arg_35_0._mainUnitWarningValue = var_0_6.WARNING_HP_RATE_MAIN * arg_35_0.GetMaxHP()

def var_0_7.UpdatePrecastMoveLimit(arg_36_0):
	return

def var_0_7.setStandardLabelTag(arg_37_0):
	var_0_7.super.setStandardLabelTag(arg_37_0)

	local var_37_0 = arg_37_0.GetManualWeaponParallel()
	local var_37_1 = #var_37_0

	while var_37_1 > 0:
		if var_37_0[var_37_1] > 1:
			print(var_0_4.PARALLEL_LABEL_TAG[var_37_1])
			arg_37_0.AddLabelTag(var_0_4.PARALLEL_LABEL_TAG[var_37_1])

		var_37_1 = var_37_1 - 1

def var_0_7.ConfigBubbleFX(arg_38_0):
	arg_38_0._bubbleFX = var_0_6.PLAYER_SUB_BUBBLE_FX

	arg_38_0._oxyState.SetBubbleTemplate(var_0_6.PLAYER_SUB_BUBBLE_INIT, var_0_6.PLAYER_SUB_BUBBLE_INTERVAL)

def var_0_7.OxyConsume(arg_39_0):
	var_0_7.super.OxyConsume(arg_39_0)

	if arg_39_0._currentOxy <= 0:
		arg_39_0._fleet.ChangeSubmarineState(var_0_0.Battle.OxyState.STATE_FREE_FLOAT, True)

def var_0_7.SetFormationIndex(arg_40_0, arg_40_1):
	arg_40_0._formationIndex = arg_40_1

def var_0_7.setAttrFromOutBattle(arg_41_0, arg_41_1, arg_41_2):
	var_0_3.SetPlayerAttrFromOutBattle(arg_41_0, arg_41_1, arg_41_2)

def var_0_7.SetFleetVO(arg_42_0, arg_42_1):
	arg_42_0._fleet = arg_42_1
	arg_42_0._subRaidLine, arg_42_0._subRetreatLine = arg_42_0._fleet.GetSubmarineBaseLine()

def var_0_7.GetTemplate(arg_43_0):
	return arg_43_0._tmpData

def var_0_7.GetRarity(arg_44_0):
	return arg_44_0._rarity or arg_44_0._tmpData.rarity

def var_0_7.GetIntimacy(arg_45_0):
	return arg_45_0._intimacy or 0

def var_0_7.GetAutoPilotPreference(arg_46_0):
	return arg_46_0._personality

def var_0_7.GetFleetVO(arg_47_0):
	return arg_47_0._fleet

def var_0_7.InitCldComponent(arg_48_0):
	var_0_7.super.InitCldComponent(arg_48_0)

	local var_48_0 = {
		type = var_0_4.CldType.SHIP,
		IFF = arg_48_0.GetIFF(),
		UID = arg_48_0.GetUniqueID(),
		Mass = var_0_4.CldMass.L2
	}

	arg_48_0._cldComponent.SetCldData(var_48_0)
