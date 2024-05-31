ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleAimbiasBar = class("BattleAimbiasBar")
var_0_0.Battle.BattleAimbiasBar.__name = "BattleAimbiasBar"

local var_0_1 = var_0_0.Battle.BattleAimbiasBar

var_0_1.WARNING_VALUE = 0.1

def var_0_1.Ctor(arg_1_0, arg_1_1):
	arg_1_0._aimBiasBar = arg_1_1
	arg_1_0._aimBiasBarGO = arg_1_0._aimBiasBar.gameObject
	arg_1_0._progress = arg_1_0._aimBiasBar.Find("bias").GetComponent(typeof(Image))
	arg_1_0._warning = arg_1_0._aimBiasBar.Find("warning")
	arg_1_0._lock = arg_1_0._aimBiasBar.Find("lock")
	arg_1_0._recovery = arg_1_0._aimBiasBar.Find("recovery")

	setActive(arg_1_0._lock, False)
	setActive(arg_1_0._warning, False)
	setActive(arg_1_0._progress, True)
	setActive(arg_1_0._aimBiasBar, True)
	setActive(arg_1_0._recovery, True)

	arg_1_0._cacheSpeed = 0
	arg_1_0._cacheWarningFlag = 0
	arg_1_0._lockBlock = False

def var_0_1.SetActive(arg_2_0, arg_2_1):
	setActive(arg_2_0._aimBiasBar, arg_2_1)

def var_0_1.ConfigAimBias(arg_3_0, arg_3_1):
	arg_3_0._aimBiasComponent = arg_3_1
	arg_3_0._hostile = arg_3_1.IsHostile()

def var_0_1.UpdateLockStateView(arg_4_0):
	local var_4_0 = arg_4_0._aimBiasComponent.GetCurrentState() == arg_4_0._aimBiasComponent.STATE_SKILL_EXPOSE

	setActive(arg_4_0._lock, var_4_0)

	if var_4_0:
		setActive(arg_4_0._recovery, False)
		setActive(arg_4_0._warning, False)
	elif arg_4_0._aimBiasComponent.GetDecayRatioSpeed() < 0:
		setActive(arg_4_0._recovery, True)
	elif not arg_4_0._hostile:
		local var_4_1 = arg_4_0._aimBiasComponent.GetCurrentRate()

		if var_4_1 < var_0_1.WARNING_VALUE and var_4_1 > 0:
			setActive(arg_4_0._warning, True)

	arg_4_0._lockBlock = var_4_0

def var_0_1.UpdateAimBiasProgress(arg_5_0):
	local var_5_0 = arg_5_0._aimBiasComponent.GetCurrentRate()

	arg_5_0._progress.fillAmount = var_5_0

	local var_5_1 = arg_5_0._aimBiasComponent.GetDecayRatioSpeed()
	local var_5_2 = var_5_0 - var_0_1.WARNING_VALUE

	if not arg_5_0._lockBlock:
		local var_5_3 = var_5_1 < 0

		if var_5_1 * arg_5_0._cacheSpeed <= 0:
			setActive(arg_5_0._recovery, var_5_3)

		if not arg_5_0._hostile:
			if var_5_0 <= 0:
				setActive(arg_5_0._warning, False)
			elif not var_5_3 and var_5_2 * arg_5_0._cacheWarningFlag < 0:
				setActive(arg_5_0._warning, var_5_0 < var_0_1.WARNING_VALUE)

	if arg_5_0._hostile and var_5_0 <= 0:
		setActive(arg_5_0._aimBiasBar, False)

	arg_5_0._cacheSpeed = var_5_1
	arg_5_0._cacheWarningFlag = var_5_2

def var_0_1.UpdateAimBiasConfig(arg_6_0):
	return

def var_0_1.Dispose(arg_7_0):
	arg_7_0._aimBiasBar = None
	arg_7_0._progress = None
	arg_7_0._warning = None
	arg_7_0._lock = None
	arg_7_0._aimBiasBarGO = None

def var_0_1.GetGO(arg_8_0):
	return arg_8_0._aimBiasBarGO
