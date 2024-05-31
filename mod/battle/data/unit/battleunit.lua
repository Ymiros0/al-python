ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleBuffEvent
local var_0_3 = var_0_0.Battle.BattleConst
local var_0_4 = var_0_0.Battle.BattleVariable
local var_0_5 = var_0_0.Battle.BattleConfig
local var_0_6 = var_0_0.Battle.BattleAttr
local var_0_7 = var_0_0.Battle.BattleDataFunction
local var_0_8 = var_0_0.Battle.UnitState
local var_0_9 = class("BattleUnit")

var_0_0.Battle.BattleUnit = var_0_9
var_0_9.__name = "BattleUnit"

function var_0_9.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_1_0)

	arg_1_0._uniqueID = arg_1_1
	arg_1_0._speedExemptKey = "unit_" .. arg_1_1
	arg_1_0._unitState = var_0_0.Battle.UnitState.New(arg_1_0)
	arg_1_0._move = var_0_0.Battle.MoveComponent.New()
	arg_1_0._weaponQueue = var_0_0.Battle.WeaponQueue.New()

	arg_1_0:Init()
	arg_1_0:SetIFF(arg_1_2)

	arg_1_0._distanceBackup = {}
	arg_1_0._battleProxy = var_0_0.Battle.BattleDataProxy.GetInstance()
	arg_1_0._frame = 0
end

function var_0_9.Retreat(arg_2_0)
	arg_2_0:TriggerBuff(var_0_3.BuffEffectType.ON_RETREAT, {})
end

function var_0_9.SetMotion(arg_3_0, arg_3_1)
	arg_3_0._move:SetMotionVO(arg_3_1)
end

function var_0_9.SetBound(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4, arg_4_5, arg_4_6)
	arg_4_0._move:SetCorpsArea(arg_4_5, arg_4_6)
	arg_4_0._move:SetBorder(arg_4_3, arg_4_4, arg_4_1, arg_4_2)
end

function var_0_9.ActiveCldBox(arg_5_0)
	arg_5_0._cldComponent:SetActive(true)
end

function var_0_9.DeactiveCldBox(arg_6_0)
	arg_6_0._cldComponent:SetActive(false)
end

function var_0_9.SetCldBoxImmune(arg_7_0, arg_7_1)
	arg_7_0._cldComponent:SetImmuneCLD(arg_7_1)
end

function var_0_9.Init(arg_8_0)
	arg_8_0._hostileCldList = {}
	arg_8_0._currentHPRate = 1
	arg_8_0._currentDMGRate = 0
	arg_8_0._tagCount = 0
	arg_8_0._tagIndex = 0
	arg_8_0._tagList = {}
	arg_8_0._aliveState = true
	arg_8_0._isMainFleetUnit = false
	arg_8_0._bulletCache = {}
	arg_8_0._speed = Vector3.zero
	arg_8_0._dir = var_0_3.UnitDir.RIGHT
	arg_8_0._extraInfo = {}
	arg_8_0._GCDTimerList = {}
	arg_8_0._buffList = {}
	arg_8_0._buffStockList = {}
	arg_8_0._labelTagList = {}
	arg_8_0._exposedToSnoar = false
	arg_8_0._moveCast = true
	arg_8_0._remoteBoundBone = {}
end

function var_0_9.Update(arg_9_0, arg_9_1)
	if arg_9_0:IsAlive() and not arg_9_0._isSickness then
		arg_9_0._move:Update()
		arg_9_0._move:FixSpeed(arg_9_0._cldComponent)
		arg_9_0._move:Move(arg_9_0:GetSpeedRatio())
	end

	arg_9_0:UpdateAction()
end

function var_0_9.UpdateWeapon(arg_10_0, arg_10_1)
	if not arg_10_0:IsAlive() or arg_10_0._isSickness then
		return
	end

	if not arg_10_0._antiSubVigilanceState or arg_10_0._antiSubVigilanceState:IsWeaponUseable() then
		local var_10_0 = arg_10_0._move:GetPos()
		local var_10_1 = arg_10_0._weaponRightBound
		local var_10_2 = arg_10_0._weaponLowerBound

		if (var_10_1 == nil or var_10_1 > var_10_0.x) and (var_10_2 == nil or var_10_2 < var_10_0.z) then
			arg_10_0._weaponQueue:Update(arg_10_1)
		end
	end

	if not arg_10_0:IsAlive() then
		return
	end

	arg_10_0:UpdateBuff(arg_10_1)
end

function var_0_9.UpdateAirAssist(arg_11_0)
	if arg_11_0._airAssistList then
		for iter_11_0, iter_11_1 in ipairs(arg_11_0._airAssistList) do
			iter_11_1:Update()
		end
	end
end

function var_0_9.UpdatePhaseSwitcher(arg_12_0)
	if arg_12_0._phaseSwitcher then
		arg_12_0._phaseSwitcher:Update()
	end
end

function var_0_9.SetInterruptSickness(arg_13_0, arg_13_1)
	arg_13_0._isSickness = arg_13_1
end

function var_0_9.SummonSickness(arg_14_0, arg_14_1)
	if arg_14_0._isSickness == true then
		return
	end

	local function var_14_0()
		arg_14_0:RemoveSummonSickness()
	end

	arg_14_0._isSickness = true
	arg_14_0._sicknessTimer = pg.TimeMgr.GetInstance():AddBattleTimer("summonSickness", 0, arg_14_1, var_14_0, true)
end

function var_0_9.RemoveSummonSickness(arg_16_0)
	arg_16_0._isSickness = false

	pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_16_0._sicknessTimer)

	arg_16_0._sicknessTimer = nil
end

function var_0_9.GetTargetedPriority(arg_17_0)
	local var_17_0

	if arg_17_0._aimBias then
		local var_17_1 = arg_17_0._aimBias:GetCurrentState()

		if var_17_1 == arg_17_0._aimBias.STATE_SKILL_EXPOSE or var_17_1 == arg_17_0._aimBias.STATE_TOTAL_EXPOSE then
			var_17_0 = arg_17_0:GetTemplate().battle_unit_type
		else
			var_17_0 = -200
		end
	else
		var_17_0 = arg_17_0:GetTemplate().battle_unit_type
	end

	return var_17_0
end

function var_0_9.PlayFX(arg_18_0, arg_18_1, arg_18_2)
	arg_18_0:DispatchEvent(var_0_0.Event.New(var_0_1.PLAY_FX, {
		fxName = arg_18_1,
		notAttach = not arg_18_2
	}))
end

function var_0_9.SwitchShader(arg_19_0, arg_19_1, arg_19_2, arg_19_3)
	arg_19_0:DispatchEvent(var_0_0.Event.New(var_0_1.SWITCH_SHADER, {
		shader = arg_19_1,
		color = arg_19_2,
		args = arg_19_3
	}))
end

function var_0_9.SendAttackTrigger(arg_20_0)
	arg_20_0:DispatchEvent(var_0_0.Event.New(var_0_1.SPAWN_CACHE_BULLET, {}))
end

function var_0_9.HandleDamageToDeath(arg_21_0)
	local var_21_0 = {
		isMiss = false,
		isCri = true,
		isHeal = false,
		damageReason = var_0_3.UnitDeathReason.DESTRUCT
	}

	arg_21_0:UpdateHP(math.floor(-arg_21_0._currentHP), var_21_0)
end

function var_0_9.UpdateHP(arg_22_0, arg_22_1, arg_22_2)
	if not arg_22_0:IsAlive() then
		return 0
	end

	local var_22_0 = arg_22_0:IsAlive()

	if not var_22_0 then
		return 0
	end

	local var_22_1 = arg_22_2.isMiss
	local var_22_2 = arg_22_2.isCri
	local var_22_3 = arg_22_2.isHeal
	local var_22_4 = arg_22_2.isShare
	local var_22_5 = arg_22_2.attr
	local var_22_6 = arg_22_2.damageReason
	local var_22_7 = arg_22_2.font
	local var_22_8 = arg_22_2.cldPos
	local var_22_9 = arg_22_2.incorrupt
	local var_22_10

	if not var_22_3 then
		local var_22_11 = {
			damage = -arg_22_1,
			isShare = var_22_4,
			miss = var_22_1,
			cri = var_22_2,
			damageSrc = arg_22_2.srcID,
			damageAttr = var_22_5,
			damageReason = var_22_6
		}

		if not var_22_4 then
			arg_22_0:TriggerBuff(var_0_3.BuffEffectType.ON_BEFORE_TAKE_DAMAGE, var_22_11)

			if var_22_11.capFlag then
				arg_22_0:TriggerBuff(var_0_3.BuffEffectType.ON_DAMAGE_FIX, var_22_11)
			end
		end

		var_22_10 = -var_22_11.damage

		arg_22_0:TriggerBuff(var_0_3.BuffEffectType.ON_TAKE_DAMAGE, var_22_11)

		if arg_22_0._currentHP <= var_22_11.damage then
			arg_22_0:TriggerBuff(var_0_3.BuffEffectType.ON_BEFORE_FATAL_DAMAGE, {})
		end

		arg_22_1 = -var_22_11.damage

		if var_22_10 ~= arg_22_1 then
			({}).absorb = var_22_10 - arg_22_1

			arg_22_0:TriggerBuff(var_0_3.BuffEffectType.ON_SHIELD_ABSORB, var_22_11)
		end

		if var_0_6.IsInvincible(arg_22_0) then
			return 0
		end
	else
		var_22_10 = arg_22_1

		local var_22_12 = {
			damage = arg_22_1,
			isHeal = var_22_3,
			incorrupt = var_22_9
		}

		arg_22_0:TriggerBuff(var_0_3.BuffEffectType.ON_TAKE_HEALING, var_22_12)

		var_22_3 = var_22_12.isHeal
		arg_22_1 = var_22_12.damage

		local var_22_13 = math.max(0, arg_22_0._currentHP + arg_22_1 - arg_22_0:GetMaxHP())

		if var_22_13 > 0 then
			arg_22_0:TriggerBuff(var_0_3.BuffEffectType.ON_OVER_HEALING, {
				overHealing = var_22_13
			})
		end
	end

	local var_22_14 = math.min(arg_22_0:GetMaxHP(), math.max(0, arg_22_0._currentHP + arg_22_1))
	local var_22_15 = var_22_14 - arg_22_0._currentHP

	arg_22_0:SetCurrentHP(var_22_14)

	local var_22_16 = {
		preShieldHP = var_22_10,
		dHP = arg_22_1,
		validDHP = var_22_15,
		isMiss = var_22_1,
		isCri = var_22_2,
		isHeal = var_22_3,
		font = var_22_7
	}

	if var_22_8 and not var_22_8:EqualZero() then
		local var_22_17 = arg_22_0:GetPosition()
		local var_22_18 = arg_22_0:GetBoxSize().x
		local var_22_19 = var_22_17.x - var_22_18
		local var_22_20 = var_22_17.x + var_22_18
		local var_22_21 = var_22_8:Clone()

		var_22_21.x = Mathf.Clamp(var_22_21.x, var_22_19, var_22_20)
		var_22_16.posOffset = var_22_17 - var_22_21
	end

	arg_22_0:UpdateHPAction(var_22_16)

	if not arg_22_0:IsAlive() and var_22_0 then
		arg_22_0:SetDeathReason(arg_22_2.damageReason)
		arg_22_0:DeadAction()
	end

	if arg_22_0:IsAlive() then
		arg_22_0:TriggerBuff(var_0_3.BuffEffectType.ON_HP_RATIO_UPDATE, {
			dHP = arg_22_1,
			unit = arg_22_0,
			validDHP = var_22_15
		})
	end

	return arg_22_1
end

function var_0_9.UpdateHPAction(arg_23_0, arg_23_1)
	arg_23_0:DispatchEvent(var_0_0.Event.New(var_0_1.UPDATE_HP, arg_23_1))
end

function var_0_9.DeadAction(arg_24_0)
	arg_24_0:TriggerBuff(var_0_3.BuffEffectType.ON_SINK, {})
	arg_24_0:DeacActionClear()
end

function var_0_9.DeacActionClear(arg_25_0)
	arg_25_0._aliveState = false

	var_0_6.Spirit(arg_25_0)
	var_0_6.AppendInvincible(arg_25_0)
	arg_25_0:DeadActionEvent()
end

function var_0_9.DeadActionEvent(arg_26_0)
	arg_26_0:DispatchEvent(var_0_0.Event.New(var_0_1.WILL_DIE, {}))
	arg_26_0:DispatchEvent(var_0_0.Event.New(var_0_1.DYING, {}))
end

function var_0_9.SendDeadEvent(arg_27_0)
	arg_27_0:DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.DYING, {}))
end

function var_0_9.SetDeathReason(arg_28_0, arg_28_1)
	arg_28_0._deathReason = arg_28_1
end

function var_0_9.GetDeathReason(arg_29_0)
	return arg_29_0._deathReason or var_0_3.UnitDeathReason.KILLED
end

function var_0_9.DispatchScorePoint(arg_30_0, arg_30_1)
	arg_30_0:DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleUnitEvent.UPDATE_SCORE, {
		score = arg_30_1
	}))
end

function var_0_9.SetTemplate(arg_31_0, arg_31_1, arg_31_2)
	arg_31_0._tmpID = arg_31_1
end

function var_0_9.GetTemplateID(arg_32_0)
	return arg_32_0._tmpID
end

function var_0_9.SetOverrideLevel(arg_33_0, arg_33_1)
	arg_33_0._overrideLevel = arg_33_1
end

function var_0_9.SetSkinId(arg_34_0)
	return
end

function var_0_9.SetGearScore(arg_35_0, arg_35_1)
	arg_35_0._GS = arg_35_1
end

function var_0_9.GetGearScore(arg_36_0)
	return arg_36_0._GS or 0
end

function var_0_9.GetSkinID(arg_37_0)
	return arg_37_0._tmpID
end

function var_0_9.GetDefaultSkinID(arg_38_0)
	return arg_38_0._tmpID
end

function var_0_9.GetSkinAttachmentInfo(arg_39_0)
	return arg_39_0._orbitSkinIDList
end

function var_0_9.GetWeaponBoundBone(arg_40_0)
	return arg_40_0._tmpData.bound_bone
end

function var_0_9.ActionKeyOffsetUseable(arg_41_0)
	return true
end

function var_0_9.RemoveRemoteBoundBone(arg_42_0, arg_42_1)
	arg_42_0._remoteBoundBone[arg_42_1] = nil
end

function var_0_9.SetRemoteBoundBone(arg_43_0, arg_43_1, arg_43_2, arg_43_3)
	local var_43_0 = arg_43_0._remoteBoundBone[arg_43_1] or {}

	var_43_0[arg_43_2] = arg_43_3
	arg_43_0._remoteBoundBone[arg_43_1] = var_43_0
end

function var_0_9.GetRemoteBoundBone(arg_44_0, arg_44_1)
	for iter_44_0, iter_44_1 in pairs(arg_44_0._remoteBoundBone) do
		local var_44_0 = iter_44_1[arg_44_1]

		if var_44_0 then
			local var_44_1 = var_0_0.Battle.BattleTargetChoise.TargetFleetIndex(arg_44_0, {
				fleetPos = var_44_0
			})[1]

			if var_44_1 and var_44_1:IsAlive() then
				local var_44_2 = Clone(var_44_1:GetPosition())

				var_44_2:Set(var_44_2.x, 1.5, var_44_2.z)

				return var_44_2
			end
		end
	end
end

function var_0_9.GetLabelTag(arg_45_0)
	return arg_45_0._labelTagList
end

function var_0_9.ContainsLabelTag(arg_46_0, arg_46_1)
	if arg_46_0._labelTagList == nil then
		return false
	end

	for iter_46_0, iter_46_1 in ipairs(arg_46_1) do
		if table.contains(arg_46_0._labelTagList, iter_46_1) then
			return true
		end
	end

	return false
end

function var_0_9.AddLabelTag(arg_47_0, arg_47_1)
	table.insert(arg_47_0._labelTagList, arg_47_1)

	local var_47_0 = var_0_6.GetCurrent(arg_47_0, "labelTag")

	var_47_0[arg_47_1] = (var_47_0[arg_47_1] or 0) + 1
end

function var_0_9.RemoveLabelTag(arg_48_0, arg_48_1)
	for iter_48_0, iter_48_1 in ipairs(arg_48_0._labelTagList) do
		if iter_48_1 == arg_48_1 then
			table.remove(arg_48_0._labelTagList, iter_48_0)

			local var_48_0 = var_0_6.GetCurrent(arg_48_0, "labelTag")

			var_48_0[arg_48_1] = var_48_0[arg_48_1] - 1

			break
		end
	end
end

function var_0_9.setStandardLabelTag(arg_49_0)
	local var_49_0 = "N_" .. arg_49_0._tmpData.nationality
	local var_49_1 = "T_" .. arg_49_0._tmpData.type

	arg_49_0:AddLabelTag(var_49_0)
	arg_49_0:AddLabelTag(var_49_1)
end

function var_0_9.GetRarity(arg_50_0)
	return
end

function var_0_9.GetIntimacy(arg_51_0)
	return 0
end

function var_0_9.IsBoss(arg_52_0)
	return false
end

function var_0_9.GetSpeedRatio(arg_53_0)
	return var_0_4.GetSpeedRatio(arg_53_0:GetSpeedExemptKey(), arg_53_0._IFF)
end

function var_0_9.GetSpeedExemptKey(arg_54_0)
	return arg_54_0._speedExemptKey
end

function var_0_9.SetMoveCast(arg_55_0, arg_55_1)
	arg_55_0._moveCast = arg_55_1
end

function var_0_9.IsMoveCast(arg_56_0)
	return arg_56_0._moveCast
end

function var_0_9.SetCrash(arg_57_0, arg_57_1)
	arg_57_0._isCrash = arg_57_1

	if arg_57_1 then
		local var_57_0 = var_0_0.Battle.BattleBuffUnit.New(var_0_5.SHIP_CLD_BUFF)

		arg_57_0:AddBuff(var_57_0)
	else
		arg_57_0:RemoveBuff(var_0_5.SHIP_CLD_BUFF)
	end
end

function var_0_9.IsCrash(arg_58_0)
	return arg_58_0._isCrash
end

function var_0_9.OverrideDeadFX(arg_59_0, arg_59_1)
	arg_59_0._deadFX = arg_59_1
end

function var_0_9.GetDeadFX(arg_60_0)
	return arg_60_0._deadFX
end

function var_0_9.SetEquipment(arg_61_0, arg_61_1)
	arg_61_0._equipmentList = arg_61_1
	arg_61_0._autoWeaponList = {}
	arg_61_0._manualTorpedoList = {}
	arg_61_0._chargeList = {}
	arg_61_0._AAList = {}
	arg_61_0._fleetAAList = {}
	arg_61_0._fleetRangeAAList = {}
	arg_61_0._hiveList = {}
	arg_61_0._totalWeapon = {}

	arg_61_0:setWeapon(arg_61_1)
end

function var_0_9.GetEquipment(arg_62_0)
	return arg_62_0._equipmentList
end

function var_0_9.SetProficiencyList(arg_63_0, arg_63_1)
	arg_63_0._proficiencyList = arg_63_1
end

function var_0_9.SetSpWeapon(arg_64_0, arg_64_1)
	arg_64_0._spWeapon = arg_64_1
end

function var_0_9.GetSpWeapon(arg_65_0)
	return arg_65_0._spWeapon
end

function var_0_9.setWeapon(arg_66_0, arg_66_1)
	for iter_66_0, iter_66_1 in ipairs(arg_66_1) do
		local var_66_0 = iter_66_1.equipment.weapon_id

		for iter_66_2, iter_66_3 in ipairs(var_66_0) do
			if iter_66_3 ~= -1 then
				local var_66_1 = var_0_0.Battle.BattleDataFunction.CreateWeaponUnit(iter_66_3, arg_66_0, nil, iter_66_0)

				arg_66_0._totalWeapon[#arg_66_0._totalWeapon + 1] = var_66_1

				local var_66_2 = var_66_1:GetTemplateData().type

				if var_66_2 == var_0_3.EquipmentType.MANUAL_TORPEDO then
					arg_66_0._manualTorpedoList[#arg_66_0._manualTorpedoList + 1] = var_66_1

					arg_66_0._weaponQueue:AppendWeapon(var_66_1)
				elseif var_66_2 == var_0_3.EquipmentType.STRIKE_AIRCRAFT then
					-- block empty
				else
					assert(#var_66_0 < 2, "自动武器一组不允许配置多个")
					arg_66_0:AddAutoWeapon(var_66_1)
				end

				if var_66_2 == var_0_3.EquipmentType.INTERCEPT_AIRCRAFT or var_66_2 == var_0_3.EquipmentType.STRIKE_AIRCRAFT then
					arg_66_0._hiveList[#arg_66_0._hiveList + 1] = var_66_1
				end

				if var_66_2 == var_0_3.EquipmentType.ANTI_AIR then
					arg_66_0._AAList[#arg_66_0._AAList + 1] = var_66_1
				end
			end
		end
	end
end

function var_0_9.CheckWeaponInitial(arg_67_0)
	arg_67_0._weaponQueue:CheckWeaponInitalCD()

	if arg_67_0._airAssistQueue then
		arg_67_0._airAssistQueue:CheckWeaponInitalCD()
	end

	arg_67_0:DispatchEvent(var_0_0.Event.New(var_0_1.INIT_COOL_DOWN, {}))
end

function var_0_9.FlushReloadingWeapon(arg_68_0)
	arg_68_0._weaponQueue:FlushWeaponReloadRequire()

	if arg_68_0._airAssistQueue then
		arg_68_0._airAssistQueue:FlushWeaponReloadRequire()
	end
end

function var_0_9.AddNewAutoWeapon(arg_69_0, arg_69_1)
	local var_69_0 = var_0_7.CreateWeaponUnit(arg_69_1, arg_69_0)

	arg_69_0:AddAutoWeapon(var_69_0)
	arg_69_0:DispatchEvent(var_0_0.Event.New(var_0_0.Battle.BattleBuffEvent.BUFF_EFFECT_NEW_WEAPON, {
		weapon = var_69_0
	}))

	return var_69_0
end

function var_0_9.AddAutoWeapon(arg_70_0, arg_70_1)
	arg_70_0._autoWeaponList[#arg_70_0._autoWeaponList + 1] = arg_70_1

	arg_70_0._weaponQueue:AppendWeapon(arg_70_1)
end

function var_0_9.RemoveAutoWeapon(arg_71_0, arg_71_1)
	arg_71_0._weaponQueue:RemoveWeapon(arg_71_1)

	local var_71_0 = 1
	local var_71_1 = #arg_71_0._autoWeaponList

	while var_71_0 <= var_71_1 do
		if arg_71_0._autoWeaponList[var_71_0] == arg_71_1 then
			arg_71_0:DispatchEvent(var_0_0.Event.New(var_0_1.REMOVE_WEAPON, {
				weapon = arg_71_1
			}))
			table.remove(arg_71_0._autoWeaponList, var_71_0)

			break
		end

		var_71_0 = var_71_0 + 1
	end
end

function var_0_9.RemoveAutoWeaponByWeaponID(arg_72_0, arg_72_1)
	for iter_72_0, iter_72_1 in ipairs(arg_72_0._autoWeaponList) do
		if iter_72_1:GetWeaponId() == arg_72_1 then
			iter_72_1:Clear()
			arg_72_0:RemoveAutoWeapon(iter_72_1)

			break
		end
	end
end

function var_0_9.RemoveAllAutoWeapon(arg_73_0)
	local var_73_0 = #arg_73_0._autoWeaponList

	while var_73_0 > 0 do
		local var_73_1 = arg_73_0._autoWeaponList[var_73_0]

		var_73_1:Clear()
		arg_73_0:RemoveAutoWeapon(var_73_1)

		var_73_0 = var_73_0 - 1
	end
end

function var_0_9.AddFleetAntiAirWeapon(arg_74_0, arg_74_1)
	return
end

function var_0_9.RemoveFleetAntiAirWeapon(arg_75_0, arg_75_1)
	return
end

function var_0_9.AttachFleetRangeAAWeapon(arg_76_0, arg_76_1)
	arg_76_0._fleetRangeAA = arg_76_1

	arg_76_0:DispatchEvent(var_0_0.Event.New(var_0_1.CREATE_TEMPORARY_WEAPON, {
		weapon = arg_76_1
	}))
end

function var_0_9.DetachFleetRangeAAWeapon(arg_77_0)
	arg_77_0:DispatchEvent(var_0_0.Event.New(var_0_1.REMOVE_WEAPON, {
		weapon = arg_77_0._fleetRangeAA
	}))

	arg_77_0._fleetRangeAA = nil
end

function var_0_9.GetFleetRangeAAWeapon(arg_78_0)
	return arg_78_0._fleetRangeAA
end

function var_0_9.ShiftWeapon(arg_79_0, arg_79_1, arg_79_2)
	for iter_79_0, iter_79_1 in ipairs(arg_79_1) do
		arg_79_0:RemoveAutoWeaponByWeaponID(iter_79_1)
	end

	for iter_79_2, iter_79_3 in ipairs(arg_79_2) do
		arg_79_0:AddNewAutoWeapon(iter_79_3):InitialCD()
	end
end

function var_0_9.ExpandWeaponMount(arg_80_0, arg_80_1)
	if arg_80_1 == "airAssist" then
		var_0_7.ExpandAllinStrike(arg_80_0)
	end
end

function var_0_9.ReduceWeaponMount(arg_81_0, arg_81_1)
	return
end

function var_0_9.CeaseAllWeapon(arg_82_0, arg_82_1)
	arg_82_0._ceaseFire = arg_82_1
end

function var_0_9.IsCease(arg_83_0)
	return arg_83_0._ceaseFire
end

function var_0_9.GetAllWeapon(arg_84_0)
	return arg_84_0._totalWeapon
end

function var_0_9.GetTotalWeapon(arg_85_0)
	return arg_85_0._weaponQueue:GetTotalWeaponUnit()
end

function var_0_9.GetAutoWeapons(arg_86_0)
	return arg_86_0._autoWeaponList
end

function var_0_9.GetChargeList(arg_87_0)
	return arg_87_0._chargeList
end

function var_0_9.GetChargeQueue(arg_88_0)
	return arg_88_0._weaponQueue:GetChargeWeaponQueue()
end

function var_0_9.GetAntiAirWeapon(arg_89_0)
	return arg_89_0._AAList
end

function var_0_9.GetFleetAntiAirList(arg_90_0)
	return arg_90_0._fleetAAList
end

function var_0_9.GetFleetRangeAntiAirList(arg_91_0)
	return arg_91_0._fleetRangeAAList
end

function var_0_9.GetTorpedoList(arg_92_0)
	return arg_92_0._manualTorpedoList
end

function var_0_9.GetTorpedoQueue(arg_93_0)
	return arg_93_0._weaponQueue:GetManualTorpedoQueue()
end

function var_0_9.GetWeaponByIndex(arg_94_0, arg_94_1)
	for iter_94_0, iter_94_1 in ipairs(arg_94_0._totalWeapon) do
		if iter_94_1:GetEquipmentIndex() == arg_94_1 then
			return iter_94_1
		end
	end
end

function var_0_9.GetHiveList(arg_95_0)
	return arg_95_0._hiveList
end

function var_0_9.SetAirAssistList(arg_96_0, arg_96_1)
	arg_96_0._airAssistList = arg_96_1
	arg_96_0._airAssistQueue = var_0_0.Battle.ManualWeaponQueue.New(arg_96_0:GetManualWeaponParallel()[var_0_3.ManualWeaponIndex.AIR_ASSIST])

	for iter_96_0, iter_96_1 in ipairs(arg_96_0._airAssistList) do
		arg_96_0._airAssistQueue:AppendWeapon(iter_96_1)
	end
end

function var_0_9.GetAirAssistList(arg_97_0)
	return arg_97_0._airAssistList
end

function var_0_9.GetAirAssistQueue(arg_98_0)
	return arg_98_0._airAssistQueue
end

function var_0_9.GetManualWeaponParallel(arg_99_0)
	return {
		1,
		1,
		1
	}
end

function var_0_9.configWeaponQueueParallel(arg_100_0)
	local var_100_0 = arg_100_0:GetManualWeaponParallel()

	arg_100_0._weaponQueue:ConfigParallel(var_100_0[var_0_3.ManualWeaponIndex.CALIBRATION], var_100_0[var_0_3.ManualWeaponIndex.TORPEDO])
end

function var_0_9.ClearWeapon(arg_101_0)
	arg_101_0._weaponQueue:ClearAllWeapon()

	local var_101_0 = arg_101_0._airAssistList

	if var_101_0 then
		for iter_101_0, iter_101_1 in ipairs(var_101_0) do
			iter_101_1:Clear()
		end
	end
end

function var_0_9.GetSpeed(arg_102_0)
	return arg_102_0._move:GetSpeed()
end

function var_0_9.GetPosition(arg_103_0)
	return arg_103_0._move:GetPos()
end

function var_0_9.GetBornPosition(arg_104_0)
	return arg_104_0._bornPos
end

function var_0_9.GetCLDZCenterPosition(arg_105_0)
	local var_105_0 = arg_105_0._battleProxy.FrameIndex

	if arg_105_0._zCenterFrame ~= var_105_0 then
		arg_105_0._zCenterFrame = var_105_0

		local var_105_1 = arg_105_0:GetCldBox()

		arg_105_0._cldZCenterCache = (var_105_1.min + var_105_1.max) * 0.5
	end

	return arg_105_0._cldZCenterCache
end

function var_0_9.GetBeenAimedPosition(arg_106_0)
	local var_106_0 = arg_106_0:GetCLDZCenterPosition()

	if not var_106_0 then
		return var_106_0
	end

	local var_106_1 = arg_106_0:GetTemplate() and arg_106_0:GetTemplate().aim_offset

	if not var_106_1 then
		return var_106_0
	end

	local var_106_2 = Vector3(var_106_0.x + var_106_1[1], var_106_0.y + var_106_1[2], var_106_0.z + var_106_1[3])

	arg_106_0:biasAimPosition(var_106_2)

	return var_106_2
end

function var_0_9.biasAimPosition(arg_107_0, arg_107_1)
	local var_107_0 = var_0_6.GetCurrent(arg_107_0, "aimBias")

	if var_107_0 > 0 then
		local var_107_1 = var_107_0 * 2
		local var_107_2 = math.random() * var_107_1 - var_107_0
		local var_107_3 = math.random() * var_107_1 - var_107_0

		arg_107_1:Set(arg_107_1.x + var_107_2, arg_107_1.y, arg_107_1.z + var_107_3)
	end

	return arg_107_1
end

function var_0_9.CancelFollowTeam(arg_108_0)
	arg_108_0._move:CancelFormationCtrl()
end

function var_0_9.UpdateFormationOffset(arg_109_0, arg_109_1)
	arg_109_0._move:SetFormationCtrlInfo(Vector3(arg_109_1.x, arg_109_1.y, arg_109_1.z))
end

function var_0_9.GetDistance(arg_110_0, arg_110_1)
	local var_110_0 = arg_110_0._battleProxy.FrameIndex

	if arg_110_0._frame ~= var_110_0 then
		arg_110_0._distanceBackup = {}
		arg_110_0._frame = var_110_0
	end

	local var_110_1 = arg_110_0._distanceBackup[arg_110_1]

	if var_110_1 == nil then
		var_110_1 = Vector3.Distance(arg_110_0:GetPosition(), arg_110_1:GetPosition())
		arg_110_0._distanceBackup[arg_110_1] = var_110_1

		arg_110_1:backupDistance(arg_110_0, var_110_1)
	end

	return var_110_1
end

function var_0_9.backupDistance(arg_111_0, arg_111_1, arg_111_2)
	local var_111_0 = arg_111_0._battleProxy.FrameIndex

	if arg_111_0._frame ~= var_111_0 then
		arg_111_0._distanceBackup = {}
		arg_111_0._frame = var_111_0
	end

	arg_111_0._distanceBackup[arg_111_1] = arg_111_2
end

function var_0_9.GetDirection(arg_112_0)
	return arg_112_0._dir
end

function var_0_9.SetBornPosition(arg_113_0, arg_113_1)
	arg_113_0._bornPos = arg_113_1
end

function var_0_9.SetPosition(arg_114_0, arg_114_1)
	arg_114_0._move:SetPos(arg_114_1)
end

function var_0_9.IsMoving(arg_115_0)
	local var_115_0 = arg_115_0._move:GetSpeed()

	return var_115_0.x ~= 0 or var_115_0.z ~= 0
end

function var_0_9.SetUncontrollableSpeedWithYAngle(arg_116_0, arg_116_1, arg_116_2, arg_116_3)
	local var_116_0 = math.deg2Rad * arg_116_1
	local var_116_1 = Vector3(math.cos(var_116_0), 0, math.sin(var_116_0))

	arg_116_0:SetUncontrollableSpeed(var_116_1, arg_116_2, arg_116_3)
end

function var_0_9.SetUncontrollableSpeedWithDir(arg_117_0, arg_117_1, arg_117_2, arg_117_3)
	local var_117_0 = math.sqrt(arg_117_1.x * arg_117_1.x + arg_117_1.z * arg_117_1.z)

	arg_117_0:SetUncontrollableSpeed(arg_117_1 / var_117_0, arg_117_2, arg_117_3)
end

function var_0_9.SetUncontrollableSpeed(arg_118_0, arg_118_1, arg_118_2, arg_118_3)
	if not arg_118_2 or not arg_118_3 then
		return
	end

	arg_118_0._move:SetForceMove(arg_118_1, arg_118_2, arg_118_3, arg_118_2 / arg_118_3)
end

function var_0_9.ClearUncontrollableSpeed(arg_119_0)
	arg_119_0._move:ClearForceMove()
end

function var_0_9.SetAdditiveSpeed(arg_120_0, arg_120_1)
	arg_120_0._move:UpdateAdditiveSpeed(arg_120_1)
end

function var_0_9.RemoveAdditiveSpeed(arg_121_0)
	arg_121_0._move:RemoveAdditiveSpeed()
end

function var_0_9.Boost(arg_122_0, arg_122_1, arg_122_2, arg_122_3, arg_122_4, arg_122_5)
	arg_122_0._move:SetForceMove(arg_122_1, arg_122_2, arg_122_3, arg_122_4, arg_122_5)
end

function var_0_9.ActiveUnstoppable(arg_123_0, arg_123_1)
	arg_123_0._move:ActiveUnstoppable(arg_123_1)
end

function var_0_9.SetImmuneCommonBulletCLD(arg_124_0)
	arg_124_0._immuneCommonBulletCLD = true
end

function var_0_9.IsImmuneCommonBulletCLD(arg_125_0)
	return arg_125_0._immuneCommonBulletCLD
end

function var_0_9.SetWeaponPreCastBound(arg_126_0, arg_126_1)
	arg_126_0._preCastBound = arg_126_1

	arg_126_0:UpdatePrecastMoveLimit()
end

function var_0_9.EnterGCD(arg_127_0, arg_127_1, arg_127_2)
	if arg_127_0._GCDTimerList[arg_127_2] ~= nil then
		return
	end

	local function var_127_0()
		arg_127_0:RemoveGCDTimer(arg_127_2)
	end

	arg_127_0._weaponQueue:QueueEnterGCD(arg_127_2, arg_127_1)

	arg_127_0._GCDTimerList[arg_127_2] = pg.TimeMgr.GetInstance():AddBattleTimer("weaponGCD", 0, arg_127_1, var_127_0, true)

	arg_127_0:UpdatePrecastMoveLimit()
end

function var_0_9.RemoveGCDTimer(arg_129_0, arg_129_1)
	pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_129_0._GCDTimerList[arg_129_1])

	arg_129_0._GCDTimerList[arg_129_1] = nil

	arg_129_0:UpdatePrecastMoveLimit()
end

function var_0_9.UpdatePrecastMoveLimit(arg_130_0)
	arg_130_0:UpdateMoveLimit()
end

function var_0_9.UpdateMoveLimit(arg_131_0)
	local var_131_0 = arg_131_0:IsMoveAble()

	arg_131_0._move:SetStaticState(not var_131_0)
end

function var_0_9.AddBuff(arg_132_0, arg_132_1, arg_132_2)
	local var_132_0 = arg_132_1:GetID()
	local var_132_1 = {
		unit_id = arg_132_0._uniqueID,
		buff_id = var_132_0
	}
	local var_132_2 = arg_132_0:GetBuff(var_132_0)

	if var_132_2 then
		local var_132_3 = var_132_2:GetLv()
		local var_132_4 = arg_132_1:GetLv()

		if arg_132_2 then
			local var_132_5 = arg_132_0._buffStockList[var_132_0] or {}

			table.insert(var_132_5, arg_132_1)

			arg_132_0._buffStockList[var_132_0] = var_132_5
		else
			var_132_1.buff_level = math.max(var_132_3, var_132_4)

			if var_132_4 <= var_132_3 then
				var_132_2:Stack(arg_132_0)

				var_132_1.stack_count = var_132_2:GetStack()

				arg_132_0:DispatchEvent(var_0_0.Event.New(var_0_2.BUFF_STACK, var_132_1))
			else
				arg_132_0:DispatchEvent(var_0_0.Event.New(var_0_2.BUFF_CAST, var_132_1))
				arg_132_0:RemoveBuff(var_132_0)

				arg_132_0._buffList[var_132_0] = arg_132_1

				arg_132_1:Attach(arg_132_0)
				arg_132_0:DispatchEvent(var_0_0.Event.New(var_0_2.BUFF_ATTACH, var_132_1))
			end
		end
	else
		arg_132_0:DispatchEvent(var_0_0.Event.New(var_0_2.BUFF_CAST, var_132_1))

		arg_132_0._buffList[var_132_0] = arg_132_1

		arg_132_1:Attach(arg_132_0)

		var_132_1.buff_level = arg_132_1:GetLv()

		arg_132_0:DispatchEvent(var_0_0.Event.New(var_0_2.BUFF_ATTACH, var_132_1))
	end

	arg_132_0:TriggerBuff(var_0_3.BuffEffectType.ON_BUFF_ADDED, {
		buffID = var_132_0
	})
end

function var_0_9.SetBuffStack(arg_133_0, arg_133_1, arg_133_2, arg_133_3)
	if arg_133_3 <= 0 then
		arg_133_0:RemoveBuff(arg_133_1)
	else
		local var_133_0 = arg_133_0:GetBuff(arg_133_1)

		if var_133_0 then
			var_133_0:UpdateStack(arg_133_0, arg_133_3)

			return var_133_0
		else
			local var_133_1 = var_0_0.Battle.BattleBuffUnit.New(arg_133_1, arg_133_2)

			arg_133_0:AddBuff(var_133_1)
			var_133_1:UpdateStack(arg_133_0, arg_133_3)

			return var_133_1
		end
	end
end

function var_0_9.UpdateBuff(arg_134_0, arg_134_1)
	local var_134_0 = arg_134_0._buffList

	for iter_134_0, iter_134_1 in pairs(var_134_0) do
		iter_134_1:Update(arg_134_0, arg_134_1)

		if not arg_134_0:IsAlive() then
			break
		end
	end
end

function var_0_9.ConsumeBuffStack(arg_135_0, arg_135_1, arg_135_2)
	local var_135_0 = arg_135_0:GetBuff(arg_135_1)

	if var_135_0 then
		if not arg_135_2 then
			arg_135_0:RemoveBuff(arg_135_1)
		else
			local var_135_1 = var_135_0:GetStack()
			local var_135_2 = math.max(0, var_135_1 - arg_135_2)

			if var_135_2 == 0 then
				arg_135_0:RemoveBuff(arg_135_1)
			else
				var_135_0:UpdateStack(arg_135_0, var_135_2)
			end
		end
	end
end

function var_0_9.RemoveBuff(arg_136_0, arg_136_1, arg_136_2)
	if arg_136_2 and arg_136_0._buffStockList[arg_136_1] then
		local var_136_0 = table.remove(arg_136_0._buffStockList[arg_136_1])

		if var_136_0 then
			var_136_0:Clear()

			return
		end
	end

	local var_136_1 = arg_136_0:GetBuff(arg_136_1)

	if var_136_1 then
		var_136_1:Remove()
	end

	arg_136_0:TriggerBuff(var_0_3.BuffEffectType.ON_BUFF_REMOVED, {
		buffID = arg_136_1
	})
end

function var_0_9.ClearBuff(arg_137_0)
	local var_137_0 = arg_137_0._buffList

	for iter_137_0, iter_137_1 in pairs(var_137_0) do
		iter_137_1:Clear()
	end

	local var_137_1 = arg_137_0._buffStockList

	for iter_137_2, iter_137_3 in pairs(var_137_1) do
		for iter_137_4, iter_137_5 in pairs(iter_137_3) do
			iter_137_5:Clear()
		end
	end
end

function var_0_9.TriggerBuff(arg_138_0, arg_138_1, arg_138_2)
	var_0_0.Battle.BattleBuffUnit.Trigger(arg_138_0, arg_138_1, arg_138_2)
end

function var_0_9.GetBuffList(arg_139_0)
	return arg_139_0._buffList
end

function var_0_9.GetBuff(arg_140_0, arg_140_1)
	arg_140_0._buffList = arg_140_0._buffList

	return arg_140_0._buffList[arg_140_1]
end

function var_0_9.DispatchSkillFloat(arg_141_0, arg_141_1, arg_141_2, arg_141_3)
	local var_141_0 = {
		coverHrzIcon = arg_141_3,
		commander = arg_141_2,
		skillName = arg_141_1
	}

	arg_141_0:DispatchEvent(var_0_0.Event.New(var_0_1.SKILL_FLOAT, var_141_0))
end

function var_0_9.DispatchCutIn(arg_142_0, arg_142_1, arg_142_2)
	local var_142_0 = {
		caster = arg_142_0,
		skill = arg_142_1
	}

	arg_142_0:DispatchEvent(var_0_0.Event.New(var_0_1.CUT_INT, var_142_0))
end

function var_0_9.DispatchCastClock(arg_143_0, arg_143_1, arg_143_2, arg_143_3, arg_143_4, arg_143_5)
	local var_143_0 = {
		isActive = arg_143_1,
		buffEffect = arg_143_2,
		iconType = arg_143_3,
		interrupt = arg_143_4,
		reverse = arg_143_5
	}

	arg_143_0:DispatchEvent(var_0_0.Event.New(var_0_1.ADD_BUFF_CLOCK, var_143_0))
end

function var_0_9.SetAI(arg_144_0, arg_144_1)
	local var_144_0 = var_0_7.GetAITmpDataFromID(arg_144_1)

	arg_144_0._autoPilotAI = var_0_0.Battle.AutoPilot.New(arg_144_0, var_144_0), arg_144_0._move:CancelFormationCtrl()
end

function var_0_9.AddPhaseSwitcher(arg_145_0, arg_145_1)
	arg_145_0._phaseSwitcher = arg_145_1
end

function var_0_9.GetPhaseSwitcher(arg_146_0)
	return arg_146_0._phaseSwitcher
end

function var_0_9.StateChange(arg_147_0, arg_147_1, arg_147_2)
	arg_147_0._unitState:ChangeState(arg_147_1, arg_147_2)
end

function var_0_9.UpdateAction(arg_148_0)
	local var_148_0 = arg_148_0:GetSpeed().x * arg_148_0._IFF

	if arg_148_0._oxyState and arg_148_0._oxyState:GetCurrentDiveState() == var_0_3.OXY_STATE.DIVE then
		if var_148_0 >= 0 then
			arg_148_0._unitState:ChangeState(var_0_8.STATE_DIVE)
		else
			arg_148_0._unitState:ChangeState(var_0_8.STATE_DIVELEFT)
		end
	elseif var_148_0 >= 0 then
		arg_148_0._unitState:ChangeState(var_0_8.STATE_MOVE)
	else
		arg_148_0._unitState:ChangeState(var_0_8.STATE_MOVELEFT)
	end
end

function var_0_9.SetActionKeyOffset(arg_149_0, arg_149_1)
	arg_149_0._actionKeyOffset = arg_149_1

	arg_149_0._unitState:FreshActionKeyOffset()
end

function var_0_9.GetActionKeyOffset(arg_150_0)
	return arg_150_0._actionKeyOffset
end

function var_0_9.GetCurrentState(arg_151_0)
	return arg_151_0._unitState:GetCurrentStateName()
end

function var_0_9.NeedWeaponCache(arg_152_0)
	return arg_152_0._unitState:NeedWeaponCache()
end

function var_0_9.CharacterActionTriggerCallback(arg_153_0)
	arg_153_0._unitState:OnActionTrigger()
end

function var_0_9.CharacterActionEndCallback(arg_154_0)
	arg_154_0._unitState:OnActionEnd()
end

function var_0_9.CharacterActionStartCallback(arg_155_0)
	return
end

function var_0_9.DispatchChat(arg_156_0, arg_156_1, arg_156_2, arg_156_3)
	if not arg_156_1 or #arg_156_1 == 0 then
		return
	end

	local var_156_0 = {
		content = HXSet.hxLan(arg_156_1),
		duration = arg_156_2,
		key = arg_156_3
	}

	arg_156_0:DispatchEvent(var_0_0.Event.New(var_0_1.POP_UP, var_156_0))
end

function var_0_9.DispatchVoice(arg_157_0, arg_157_1)
	local var_157_0 = arg_157_0:GetIntimacy()
	local var_157_1, var_157_2, var_157_3 = ShipWordHelper.GetWordAndCV(arg_157_0:GetSkinID(), arg_157_1, 1, true, var_157_0)

	if var_157_2 then
		local var_157_4 = {
			content = var_157_2,
			key = arg_157_1
		}

		arg_157_0:DispatchEvent(var_0_0.Event.New(var_0_1.VOICE, var_157_4))
	end
end

function var_0_9.GetHostileCldList(arg_158_0)
	return arg_158_0._hostileCldList
end

function var_0_9.AppendHostileCld(arg_159_0, arg_159_1, arg_159_2)
	arg_159_0._hostileCldList[arg_159_1] = arg_159_2
end

function var_0_9.RemoveHostileCld(arg_160_0, arg_160_1)
	pg.TimeMgr.GetInstance():RemoveBattleTimer(arg_160_0._hostileCldList[arg_160_1])

	arg_160_0._hostileCldList[arg_160_1] = nil
end

function var_0_9.GetExtraInfo(arg_161_0)
	return arg_161_0._extraInfo
end

function var_0_9.GetTemplate(arg_162_0)
	return nil
end

function var_0_9.GetTemplateValue(arg_163_0, arg_163_1)
	return arg_163_0:GetTemplate()[arg_163_1]
end

function var_0_9.GetUniqueID(arg_164_0)
	return arg_164_0._uniqueID
end

function var_0_9.SetIFF(arg_165_0, arg_165_1)
	arg_165_0._IFF = arg_165_1

	if arg_165_1 == var_0_5.FRIENDLY_CODE then
		arg_165_0._dir = var_0_3.UnitDir.RIGHT
	elseif arg_165_1 == var_0_5.FOE_CODE then
		arg_165_0._dir = var_0_3.UnitDir.LEFT
	end
end

function var_0_9.GetIFF(arg_166_0)
	return arg_166_0._IFF
end

function var_0_9.GetUnitType(arg_167_0)
	return arg_167_0._type
end

function var_0_9.GetHPRate(arg_168_0)
	return arg_168_0._currentHPRate
end

function var_0_9.GetHP(arg_169_0)
	return arg_169_0._currentHP, arg_169_0:GetMaxHP()
end

function var_0_9.GetCurrentHP(arg_170_0)
	return arg_170_0._currentHP
end

function var_0_9.SetCurrentHP(arg_171_0, arg_171_1)
	arg_171_0._currentHP = arg_171_1
	arg_171_0._currentHPRate = arg_171_0._currentHP / arg_171_0:GetMaxHP()
	arg_171_0._currentDMGRate = 1 - arg_171_0._currentHPRate

	var_0_6.SetCurrent(arg_171_0, "HPRate", arg_171_0._currentHPRate)
	var_0_6.SetCurrent(arg_171_0, "DMGRate", arg_171_0._currentDMGRate)
end

function var_0_9.GetAttr(arg_172_0)
	return var_0_6.GetAttr(arg_172_0)
end

function var_0_9.GetAttrByName(arg_173_0, arg_173_1)
	return var_0_6.GetCurrent(arg_173_0, arg_173_1)
end

function var_0_9.GetMaxHP(arg_174_0)
	return arg_174_0:GetAttrByName("maxHP")
end

function var_0_9.GetReload(arg_175_0)
	return arg_175_0:GetAttrByName("loadSpeed")
end

function var_0_9.GetTorpedoPower(arg_176_0)
	return arg_176_0:GetAttrByName("torpedoPower")
end

function var_0_9.CanDoAntiSub(arg_177_0)
	return arg_177_0:GetAttrByName("antiSubPower") > 0
end

function var_0_9.IsShowHPBar(arg_178_0)
	return false
end

function var_0_9.IsAlive(arg_179_0)
	local var_179_0 = arg_179_0:GetCurrentHP()

	return arg_179_0._aliveState and var_179_0 > 0
end

function var_0_9.SetMainFleetUnit(arg_180_0)
	arg_180_0._isMainFleetUnit = true

	arg_180_0:SetMainUnitStatic(true)
end

function var_0_9.IsMainFleetUnit(arg_181_0)
	return arg_181_0._isMainFleetUnit
end

function var_0_9.SetMainUnitStatic(arg_182_0, arg_182_1)
	arg_182_0._isMainStatic = arg_182_1

	arg_182_0._move:SetStaticState(arg_182_1)
end

function var_0_9.SetMainUnitIndex(arg_183_0, arg_183_1)
	arg_183_0._mainUnitIndex = arg_183_1
end

function var_0_9.GetMainUnitIndex(arg_184_0)
	return arg_184_0._mainUnitIndex or 1
end

function var_0_9.IsMoveAble(arg_185_0)
	local var_185_0 = table.getCount(arg_185_0._GCDTimerList) > 0 or arg_185_0._preCastBound
	local var_185_1 = var_0_6.IsStun(arg_185_0)
	local var_185_2 = arg_185_0:IsMoveCast()

	return not arg_185_0._isMainStatic and (var_185_2 or not var_185_0) and not var_185_1
end

function var_0_9.Reinforce(arg_186_0)
	arg_186_0._isReinforcement = true
end

function var_0_9.IsReinforcement(arg_187_0)
	return arg_187_0._isReinforcement
end

function var_0_9.SetReinforceCastTime(arg_188_0, arg_188_1)
	arg_188_0._reinforceCastTime = arg_188_1
end

function var_0_9.GetReinforceCastTime(arg_189_0)
	return arg_189_0._reinforceCastTime
end

function var_0_9.GetFleetVO(arg_190_0)
	return
end

function var_0_9.SetFormationIndex(arg_191_0, arg_191_1)
	return
end

function var_0_9.SetMaster(arg_192_0)
	return
end

function var_0_9.GetMaster(arg_193_0)
	return nil
end

function var_0_9.IsSpectre(arg_194_0)
	return
end

function var_0_9.Clear(arg_195_0)
	arg_195_0._aliveState = false

	for iter_195_0, iter_195_1 in pairs(arg_195_0._hostileCldList) do
		arg_195_0:RemoveHostileCld(iter_195_0)
	end

	arg_195_0:ClearWeapon()
	arg_195_0:ClearBuff()

	arg_195_0._distanceBackup = {}
end

function var_0_9.Dispose(arg_196_0)
	arg_196_0._exposedList = nil
	arg_196_0._phaseSwitcher = nil

	arg_196_0._weaponQueue:Dispose()

	if arg_196_0._airAssistQueue then
		arg_196_0._airAssistQueue:Clear()

		arg_196_0._airAssistQueue = nil
	end

	arg_196_0._equipmentList = nil
	arg_196_0._totalWeapon = nil

	local var_196_0 = arg_196_0._airAssistList

	if var_196_0 then
		for iter_196_0, iter_196_1 in ipairs(var_196_0) do
			iter_196_1:Dispose()
		end
	end

	for iter_196_2, iter_196_3 in ipairs(arg_196_0._fleetAAList) do
		iter_196_3:Dispose()
	end

	for iter_196_4, iter_196_5 in ipairs(arg_196_0._fleetRangeAAList) do
		iter_196_5:Dispose()
	end

	local var_196_1 = arg_196_0._buffList

	for iter_196_6, iter_196_7 in pairs(var_196_1) do
		iter_196_7:Dispose()
	end

	local var_196_2 = arg_196_0._buffStockList

	for iter_196_8, iter_196_9 in pairs(var_196_2) do
		for iter_196_10, iter_196_11 in pairs(iter_196_9) do
			iter_196_11:Clear()
		end
	end

	arg_196_0._fleetRangeAA = nil
	arg_196_0._aimBias = nil
	arg_196_0._buffList = nil
	arg_196_0._buffStockList = nil
	arg_196_0._cldZCenterCache = nil
	arg_196_0._remoteBoundBone = nil

	arg_196_0:RemoveSummonSickness()
	var_0_0.EventDispatcher.DetachEventDispatcher(arg_196_0)
end

function var_0_9.InitCldComponent(arg_197_0)
	local var_197_0 = arg_197_0:GetTemplate().cld_box
	local var_197_1 = arg_197_0:GetTemplate().cld_offset
	local var_197_2 = var_197_1[1]

	if arg_197_0:GetDirection() == var_0_3.UnitDir.LEFT then
		var_197_2 = var_197_2 * -1
	end

	arg_197_0._cldComponent = var_0_0.Battle.BattleCubeCldComponent.New(var_197_0[1], var_197_0[2], var_197_0[3], var_197_2, var_197_1[3] + var_197_0[3] / 2)
end

function var_0_9.GetBoxSize(arg_198_0)
	return arg_198_0._cldComponent:GetCldBoxSize()
end

function var_0_9.GetCldBox(arg_199_0)
	return arg_199_0._cldComponent:GetCldBox(arg_199_0:GetPosition())
end

function var_0_9.GetCldData(arg_200_0)
	return arg_200_0._cldComponent:GetCldData()
end

function var_0_9.InitOxygen(arg_201_0)
	arg_201_0._maxOxy = arg_201_0:GetAttrByName("oxyMax")
	arg_201_0._currentOxy = arg_201_0:GetAttrByName("oxyMax")
	arg_201_0._oxyRecovery = arg_201_0:GetAttrByName("oxyRecovery")
	arg_201_0._oxyRecoveryBench = arg_201_0:GetAttrByName("oxyRecoveryBench")
	arg_201_0._oxyRecoverySurface = arg_201_0:GetAttrByName("oxyRecoverySurface")
	arg_201_0._oxyConsume = arg_201_0:GetAttrByName("oxyCost")
	arg_201_0._oxyState = var_0_0.Battle.OxyState.New(arg_201_0)

	arg_201_0._oxyState:OnDiveState()
	arg_201_0:ConfigBubbleFX()

	return arg_201_0._oxyState
end

function var_0_9.UpdateOxygen(arg_202_0, arg_202_1)
	if arg_202_0._oxyState then
		arg_202_0._lastOxyUpdateStamp = arg_202_0._lastOxyUpdateStamp or arg_202_1

		arg_202_0._oxyState:UpdateOxygen()

		if arg_202_0._oxyState:GetNextBubbleStamp() and arg_202_1 > arg_202_0._oxyState:GetNextBubbleStamp() then
			arg_202_0._oxyState:FlashBubbleStamp(arg_202_1)
			arg_202_0:PlayFX(arg_202_0._bubbleFX, true)
		end

		arg_202_0._lastOxyUpdateStamp = arg_202_1

		arg_202_0:updateSonarExposeTag()
	end
end

function var_0_9.OxyRecover(arg_203_0, arg_203_1)
	local var_203_0

	if arg_203_1 == var_0_0.Battle.OxyState.STATE_FREE_BENCH then
		var_203_0 = arg_203_0._oxyRecoveryBench
	elseif arg_203_1 == var_0_0.Battle.OxyState.STATE_FREE_FLOAT then
		var_203_0 = arg_203_0._oxyRecovery
	else
		var_203_0 = arg_203_0._oxyRecoverySurface
	end

	local var_203_1 = pg.TimeMgr.GetInstance():GetCombatTime() - arg_203_0._lastOxyUpdateStamp

	arg_203_0._currentOxy = math.min(arg_203_0._maxOxy, arg_203_0._currentOxy + var_203_0 * var_203_1)
end

function var_0_9.OxyConsume(arg_204_0)
	local var_204_0 = pg.TimeMgr.GetInstance():GetCombatTime() - arg_204_0._lastOxyUpdateStamp

	arg_204_0._currentOxy = math.max(0, arg_204_0._currentOxy - arg_204_0._oxyConsume * var_204_0)
end

function var_0_9.ChangeOxygenState(arg_205_0, arg_205_1)
	arg_205_0._oxyState:ChangeState(arg_205_1)
end

function var_0_9.ChangeWeaponDiveState(arg_206_0)
	for iter_206_0, iter_206_1 in ipairs(arg_206_0._autoWeaponList) do
		iter_206_1:ChangeDiveState()
	end
end

function var_0_9.GetOxygenProgress(arg_207_0)
	return arg_207_0._currentOxy / arg_207_0._maxOxy
end

function var_0_9.GetCuurentOxygen(arg_208_0)
	return arg_208_0._currentOxy or 0
end

function var_0_9.ConfigBubbleFX(arg_209_0)
	return
end

function var_0_9.SetDiveInvisible(arg_210_0, arg_210_1)
	arg_210_0._diveInvisible = arg_210_1

	arg_210_0:DispatchEvent(var_0_0.Event.New(var_0_1.SUBMARINE_VISIBLE))
	arg_210_0:DispatchEvent(var_0_0.Event.New(var_0_1.SUBMARINE_DETECTED))
	arg_210_0:dispatchDetectedTrigger()
end

function var_0_9.GetDiveInvisible(arg_211_0)
	return arg_211_0._diveInvisible
end

function var_0_9.GetOxygenVisible(arg_212_0)
	return arg_212_0._oxyState and arg_212_0._oxyState:GetBarVisible()
end

function var_0_9.SetForceVisible(arg_213_0)
	arg_213_0:DispatchEvent(var_0_0.Event.New(var_0_1.SUBMARINE_FORCE_DETECTED))
end

function var_0_9.Detected(arg_214_0, arg_214_1)
	local var_214_0

	if arg_214_0._exposedToSnoar == false and not arg_214_0._exposedOverTimeStamp then
		var_214_0 = true
	end

	if arg_214_1 then
		arg_214_0:updateExposeTimeStamp(arg_214_1)
	else
		arg_214_0._exposedToSnoar = true
	end

	if var_214_0 then
		arg_214_0:DispatchEvent(var_0_0.Event.New(var_0_1.SUBMARINE_DETECTED, {}))
		arg_214_0:dispatchDetectedTrigger()
	end
end

function var_0_9.Undetected(arg_215_0)
	arg_215_0._exposedToSnoar = false

	arg_215_0:updateExposeTimeStamp(var_0_5.SUB_EXPOSE_LASTING_DURATION)
end

function var_0_9.RemoveSonarExpose(arg_216_0)
	arg_216_0._exposedToSnoar = false
	arg_216_0._exposedOverTimeStamp = nil
end

function var_0_9.updateSonarExposeTag(arg_217_0)
	if arg_217_0._exposedOverTimeStamp and not arg_217_0._exposedToSnoar and pg.TimeMgr.GetInstance():GetCombatTime() > arg_217_0._exposedOverTimeStamp then
		arg_217_0._exposedOverTimeStamp = nil

		arg_217_0:DispatchEvent(var_0_0.Event.New(var_0_1.SUBMARINE_DETECTED, {
			detected = false
		}))
		arg_217_0:dispatchDetectedTrigger()
	end
end

function var_0_9.updateExposeTimeStamp(arg_218_0, arg_218_1)
	local var_218_0 = pg.TimeMgr.GetInstance():GetCombatTime() + arg_218_1

	arg_218_0._exposedOverTimeStamp = arg_218_0._exposedOverTimeStamp or 0
	arg_218_0._exposedOverTimeStamp = var_218_0 < arg_218_0._exposedOverTimeStamp and arg_218_0._exposedOverTimeStamp or var_218_0
end

function var_0_9.IsRunMode(arg_219_0)
	return arg_219_0._oxyState and arg_219_0._oxyState:GetRundMode()
end

function var_0_9.GetDiveDetected(arg_220_0)
	return arg_220_0:GetDiveInvisible() and (arg_220_0._exposedOverTimeStamp or arg_220_0._exposedToSnoar)
end

function var_0_9.GetForceExpose(arg_221_0)
	return arg_221_0._oxyState and arg_221_0._oxyState:GetForceExpose()
end

function var_0_9.dispatchDetectedTrigger(arg_222_0)
	if arg_222_0:GetDiveDetected() then
		arg_222_0:TriggerBuff(var_0_3.BuffEffectType.ON_SUB_DETECTED, {})
	else
		arg_222_0:TriggerBuff(var_0_3.BuffEffectType.ON_SUB_UNDETECTED, {})
	end
end

function var_0_9.GetRaidDuration(arg_223_0)
	return arg_223_0:GetAttrByName("oxyMax") / arg_223_0:GetAttrByName("oxyCost")
end

function var_0_9.EnterRaidRange(arg_224_0)
	if arg_224_0:GetPosition().x > arg_224_0._subRaidLine then
		return true
	else
		return false
	end
end

function var_0_9.EnterRetreatRange(arg_225_0)
	if arg_225_0:GetPosition().x < arg_225_0._subRetreatLine then
		return true
	else
		return false
	end
end

function var_0_9.GetOxyState(arg_226_0)
	return arg_226_0._oxyState
end

function var_0_9.GetCurrentOxyState(arg_227_0)
	if not arg_227_0._oxyState then
		return var_0_3.OXY_STATE.FLOAT
	else
		return arg_227_0._oxyState:GetCurrentDiveState()
	end
end

function var_0_9.InitAntiSubState(arg_228_0, arg_228_1, arg_228_2)
	arg_228_0._antiSubVigilanceState = var_0_0.Battle.AntiSubState.New(arg_228_0)

	arg_228_0:DispatchEvent(var_0_0.Event.New(var_0_1.INIT_ANIT_SUB_VIGILANCE, {
		sonarRange = arg_228_1
	}))

	return arg_228_0._antiSubVigilanceState
end

function var_0_9.GetAntiSubState(arg_229_0)
	return arg_229_0._antiSubVigilanceState
end

function var_0_9.UpdateBlindInvisibleBySpectre(arg_230_0)
	local var_230_0, var_230_1 = arg_230_0:IsSpectre()

	if var_230_1 <= var_0_5.SPECTRE_UNIT_TYPE and var_230_1 ~= var_0_5.VISIBLE_SPECTRE_UNIT_TYPE then
		arg_230_0:SetBlindInvisible(true)
	else
		arg_230_0:SetBlindInvisible(false)
	end
end

function var_0_9.SetBlindInvisible(arg_231_0, arg_231_1)
	arg_231_0._exposedList = arg_231_1 and {} or nil
	arg_231_0._blindInvisible = arg_231_1

	arg_231_0:DispatchEvent(var_0_0.Event.New(var_0_1.BLIND_VISIBLE))
end

function var_0_9.GetBlindInvisible(arg_232_0)
	return arg_232_0._blindInvisible
end

function var_0_9.GetExposed(arg_233_0)
	if not arg_233_0._blindInvisible then
		return true
	end

	for iter_233_0, iter_233_1 in pairs(arg_233_0._exposedList) do
		return true
	end
end

function var_0_9.AppendExposed(arg_234_0, arg_234_1)
	if not arg_234_0._blindInvisible then
		return
	end

	local var_234_0 = arg_234_0._exposedList[arg_234_1]

	arg_234_0._exposedList[arg_234_1] = true

	if not var_234_0 then
		arg_234_0:DispatchEvent(var_0_0.Event.New(var_0_1.BLIND_EXPOSE))
	end
end

function var_0_9.RemoveExposed(arg_235_0, arg_235_1)
	if not arg_235_0._blindInvisible then
		return
	end

	arg_235_0._exposedList[arg_235_1] = nil

	arg_235_0:DispatchEvent(var_0_0.Event.New(var_0_1.BLIND_EXPOSE))
end

function var_0_9.SetWorldDeathMark(arg_236_0)
	arg_236_0._worldDeathMark = true
end

function var_0_9.GetWorldDeathMark(arg_237_0)
	return arg_237_0._worldDeathMark
end

function var_0_9.InitCloak(arg_238_0)
	arg_238_0._cloak = var_0_0.Battle.BattleUnitCloakComponent.New(arg_238_0)

	arg_238_0:DispatchEvent(var_0_0.Event.New(var_0_1.INIT_CLOAK))

	return arg_238_0._cloak
end

function var_0_9.CloakOnFire(arg_239_0, arg_239_1)
	if arg_239_0._cloak then
		arg_239_0._cloak:UpdateDotExpose(arg_239_1)
	end
end

function var_0_9.CloakExpose(arg_240_0, arg_240_1)
	if arg_240_0._cloak then
		arg_240_0._cloak:AppendExpose(arg_240_1)
	end
end

function var_0_9.StrikeExpose(arg_241_0)
	if arg_241_0._cloak then
		arg_241_0._cloak:AppendStrikeExpose()
	end
end

function var_0_9.BombardExpose(arg_242_0)
	if arg_242_0._cloak then
		arg_242_0._cloak:AppendBombardExpose()
	end
end

function var_0_9.UpdateCloak(arg_243_0, arg_243_1)
	arg_243_0._cloak:Update(arg_243_1)
end

function var_0_9.UpdateCloakConfig(arg_244_0)
	if arg_244_0._cloak then
		arg_244_0._cloak:UpdateCloakConfig()
		arg_244_0:DispatchEvent(var_0_0.Event.New(var_0_1.UPDATE_CLOAK_CONFIG))
	end
end

function var_0_9.DispatchCloakStateUpdate(arg_245_0)
	if arg_245_0._cloak then
		arg_245_0:DispatchEvent(var_0_0.Event.New(var_0_1.UPDATE_CLOAK_STATE))
	end
end

function var_0_9.GetCloak(arg_246_0)
	return arg_246_0._cloak
end

function var_0_9.AttachAimBias(arg_247_0, arg_247_1)
	arg_247_0._aimBias = arg_247_1

	arg_247_0:DispatchEvent(var_0_0.Event.New(var_0_1.INIT_AIMBIAS))
end

function var_0_9.DetachAimBias(arg_248_0)
	arg_248_0:DispatchEvent(var_0_0.Event.New(var_0_1.REMOVE_AIMBIAS))
	arg_248_0._aimBias:RemoveCrew(arg_248_0)

	arg_248_0._aimBias = nil
end

function var_0_9.ExitSmokeArea(arg_249_0)
	arg_249_0._aimBias:SmokeExitPause()
end

function var_0_9.UpdateAimBiasSkillState(arg_250_0)
	if arg_250_0._aimBias and arg_250_0._aimBias:GetHost() == arg_250_0 then
		arg_250_0._aimBias:UpdateSkillLock()
	end
end

function var_0_9.HostAimBias(arg_251_0)
	if arg_251_0._aimBias then
		arg_251_0:DispatchEvent(var_0_0.Event.New(var_0_1.HOST_AIMBIAS))
	end
end

function var_0_9.GetAimBias(arg_252_0)
	return arg_252_0._aimBias
end

function var_0_9.SwitchSpine(arg_253_0, arg_253_1, arg_253_2)
	arg_253_0:DispatchEvent(var_0_0.Event.New(var_0_1.SWITCH_SPINE, {
		skin = arg_253_1,
		HPBarOffset = arg_253_2
	}))
end

function var_0_9.Freeze(arg_254_0)
	for iter_254_0, iter_254_1 in ipairs(arg_254_0._totalWeapon) do
		iter_254_1:StartJamming()
	end

	if arg_254_0._airAssistList then
		for iter_254_2, iter_254_3 in ipairs(arg_254_0._airAssistList) do
			iter_254_3:StartJamming()
		end
	end
end

function var_0_9.ActiveFreeze(arg_255_0)
	for iter_255_0, iter_255_1 in ipairs(arg_255_0._totalWeapon) do
		iter_255_1:JammingEliminate()
	end

	if arg_255_0._airAssistList then
		for iter_255_2, iter_255_3 in ipairs(arg_255_0._airAssistList) do
			iter_255_3:JammingEliminate()
		end
	end
end

function var_0_9.ActiveWeaponSectorView(arg_256_0, arg_256_1, arg_256_2)
	local var_256_0 = {
		weapon = arg_256_1,
		isActive = arg_256_2
	}

	arg_256_0:DispatchEvent(var_0_0.Event.New(var_0_1.WEAPON_SECTOR, var_256_0))
end
