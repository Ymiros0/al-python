ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleAimbiasBar = class("BattleAimbiasBar")
var_0_0.Battle.BattleAimbiasBar.__name = "BattleAimbiasBar"

local var_0_1 = var_0_0.Battle.BattleAimbiasBar

var_0_1.WARNING_VALUE = 0.1

function var_0_1.Ctor(arg_1_0, arg_1_1)
	arg_1_0._aimBiasBar = arg_1_1
	arg_1_0._aimBiasBarGO = arg_1_0._aimBiasBar.gameObject
	arg_1_0._progress = arg_1_0._aimBiasBar:Find("bias"):GetComponent(typeof(Image))
	arg_1_0._warning = arg_1_0._aimBiasBar:Find("warning")
	arg_1_0._lock = arg_1_0._aimBiasBar:Find("lock")
	arg_1_0._recovery = arg_1_0._aimBiasBar:Find("recovery")

	setActive(arg_1_0._lock, false)
	setActive(arg_1_0._warning, false)
	setActive(arg_1_0._progress, true)
	setActive(arg_1_0._aimBiasBar, true)
	setActive(arg_1_0._recovery, true)

	arg_1_0._cacheSpeed = 0
	arg_1_0._cacheWarningFlag = 0
	arg_1_0._lockBlock = false
end

function var_0_1.SetActive(arg_2_0, arg_2_1)
	setActive(arg_2_0._aimBiasBar, arg_2_1)
end

function var_0_1.ConfigAimBias(arg_3_0, arg_3_1)
	arg_3_0._aimBiasComponent = arg_3_1
	arg_3_0._hostile = arg_3_1:IsHostile()
end

function var_0_1.UpdateLockStateView(arg_4_0)
	local var_4_0 = arg_4_0._aimBiasComponent:GetCurrentState() == arg_4_0._aimBiasComponent.STATE_SKILL_EXPOSE

	setActive(arg_4_0._lock, var_4_0)

	if var_4_0 then
		setActive(arg_4_0._recovery, false)
		setActive(arg_4_0._warning, false)
	elseif arg_4_0._aimBiasComponent:GetDecayRatioSpeed() < 0 then
		setActive(arg_4_0._recovery, true)
	elseif not arg_4_0._hostile then
		local var_4_1 = arg_4_0._aimBiasComponent:GetCurrentRate()

		if var_4_1 < var_0_1.WARNING_VALUE and var_4_1 > 0 then
			setActive(arg_4_0._warning, true)
		end
	end

	arg_4_0._lockBlock = var_4_0
end

function var_0_1.UpdateAimBiasProgress(arg_5_0)
	local var_5_0 = arg_5_0._aimBiasComponent:GetCurrentRate()

	arg_5_0._progress.fillAmount = var_5_0

	local var_5_1 = arg_5_0._aimBiasComponent:GetDecayRatioSpeed()
	local var_5_2 = var_5_0 - var_0_1.WARNING_VALUE

	if not arg_5_0._lockBlock then
		local var_5_3 = var_5_1 < 0

		if var_5_1 * arg_5_0._cacheSpeed <= 0 then
			setActive(arg_5_0._recovery, var_5_3)
		end

		if not arg_5_0._hostile then
			if var_5_0 <= 0 then
				setActive(arg_5_0._warning, false)
			elseif not var_5_3 and var_5_2 * arg_5_0._cacheWarningFlag < 0 then
				setActive(arg_5_0._warning, var_5_0 < var_0_1.WARNING_VALUE)
			end
		end
	end

	if arg_5_0._hostile and var_5_0 <= 0 then
		setActive(arg_5_0._aimBiasBar, false)
	end

	arg_5_0._cacheSpeed = var_5_1
	arg_5_0._cacheWarningFlag = var_5_2
end

function var_0_1.UpdateAimBiasConfig(arg_6_0)
	return
end

function var_0_1.Dispose(arg_7_0)
	arg_7_0._aimBiasBar = nil
	arg_7_0._progress = nil
	arg_7_0._warning = nil
	arg_7_0._lock = nil
	arg_7_0._aimBiasBarGO = nil
end

function var_0_1.GetGO(arg_8_0)
	return arg_8_0._aimBiasBarGO
end
