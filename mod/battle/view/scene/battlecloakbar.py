ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleCloakBar = class("BattleCloakBar")
var_0_0.Battle.BattleCloakBar.__name = "BattleCloakBar"

local var_0_1 = var_0_0.Battle.BattleCloakBar

var_0_1.FORM_RAD = "radian"
var_0_1.FORM_BAR = "bar"
var_0_1.MIN = 0.31
var_0_1.MAX = 0.69
var_0_1.METER_LENGTH = var_0_1.MAX - var_0_1.MIN
var_0_1.MIN_ANGLE = -31
var_0_1.MAX_ANGLE = 33
var_0_1.RESTORE_LEGHTH = var_0_1.MAX_ANGLE - var_0_1.MIN_ANGLE
var_0_1.BAR_MIN = -62
var_0_1.BAR_MAX = 62
var_0_1.BAR_STEP = var_0_1.BAR_MAX - var_0_1.BAR_MIN

def var_0_1.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_2 = arg_1_2 or var_0_1.FORM_RAD
	arg_1_0._cloakBar = arg_1_1
	arg_1_0._cloakBarGO = arg_1_0._cloakBar.gameObject
	arg_1_0._progress = arg_1_0._cloakBar.Find("progress").GetComponent(typeof(Image))
	arg_1_0._restoreMark = arg_1_0._cloakBar.Find("cloak_restore")
	arg_1_0._lockProgress = arg_1_0._cloakBar.Find("lock").GetComponent(typeof(Image))
	arg_1_0._exposeFX = arg_1_0._cloakBar.Find("top_effect")
	arg_1_0._markContainer = arg_1_0._cloakBar.Find("mark")
	arg_1_0._exposeMark = arg_1_0._cloakBar.Find("mark/2")
	arg_1_0._visionMark = arg_1_0._cloakBar.Find("mark/1")

	setActive(arg_1_0._cloakBar, True)
	setActive(arg_1_0._exposeFX, False)
	setActive(arg_1_0._exposeMark, False)
	setActive(arg_1_0._visionMark, False)

	if arg_1_2 == var_0_1.FORM_RAD:
		arg_1_0._restoreMark.localRotation = Vector3(0, 0, 0)
		arg_1_0.meterConvert = var_0_1.__radMeterConvert
		arg_1_0.restoreConvert = var_0_1.__radRestoreConvert
	else
		arg_1_0.meterConvert = var_0_1.__barMeterConvert
		arg_1_0.restoreConvert = var_0_1.__barRestoreConvert

def var_0_1.SetActive(arg_2_0, arg_2_1):
	setActive(arg_2_0._cloakBar, arg_2_1)

def var_0_1.ConfigCloak(arg_3_0, arg_3_1):
	arg_3_0._cloakComponent = arg_3_1

	arg_3_0.initCloak()

def var_0_1.UpdateCloakProgress(arg_4_0):
	local var_4_0 = arg_4_0._cloakComponent.GetCloakValue() / arg_4_0._meterMaxValue

	arg_4_0._progress.fillAmount = arg_4_0.meterConvert(var_4_0)

	local var_4_1 = arg_4_0._cloakComponent.GetCurrentState()

	if var_4_1 == var_0_0.Battle.BattleUnitCloakComponent.STATE_CLOAK:
		setActive(arg_4_0._exposeFX, False)
	elif var_4_1 == var_0_0.Battle.BattleUnitCloakComponent.STATE_UNCLOAK:
		setActive(arg_4_0._exposeFX, True)

	if var_4_1 == var_0_0.Battle.BattleUnitCloakComponent.STATE_UNCLOAK:
		setActive(arg_4_0._exposeMark, True)
		setActive(arg_4_0._visionMark, False)
	elif arg_4_0._cloakComponent.GetExposeSpeed() > 0:
		setActive(arg_4_0._exposeMark, False)
		setActive(arg_4_0._visionMark, True)
	else
		setActive(arg_4_0._exposeMark, False)
		setActive(arg_4_0._visionMark, False)

local var_0_2 = Vector3.New(-1, 1, 1)
local var_0_3 = Vector3.New(-0.5, 0.5, 1)
local var_0_4 = Vector3.New(0.5, 0.5, 1)

def var_0_1.UpdateCloarBarPosition(arg_5_0, arg_5_1):
	if arg_5_1.x < 0:
		arg_5_0._cloakBar.position = arg_5_1 + Vector3.right
		arg_5_0._cloakBar.localScale = Vector3.one
		arg_5_0._markContainer.localScale = var_0_4
	else
		arg_5_0._cloakBar.position = arg_5_1 + Vector3.left
		arg_5_0._cloakBar.localScale = var_0_2
		arg_5_0._markContainer.localScale = var_0_3

def var_0_1.UpdateCloakConfig(arg_6_0):
	arg_6_0.initCloak()

def var_0_1.UpdateCloakLock(arg_7_0):
	local var_7_0 = arg_7_0._cloakComponent.GetCloakBottom() / arg_7_0._meterMaxValue

	arg_7_0._lockProgress.fillAmount = arg_7_0.meterConvert(var_7_0)

def var_0_1.initCloak(arg_8_0):
	arg_8_0._meterMaxValue = arg_8_0._cloakComponent.GetCloakMax()

	arg_8_0.updateRestoreMark()

def var_0_1.updateRestoreMark(arg_9_0):
	local var_9_0 = arg_9_0._cloakComponent.GetCloakRestoreValue() / arg_9_0._meterMaxValue

	arg_9_0.restoreConvert(var_9_0, arg_9_0._restoreMark)

def var_0_1.__radMeterConvert(arg_10_0):
	return var_0_1.METER_LENGTH * arg_10_0 + var_0_1.MIN

def var_0_1.__radRestoreConvert(arg_11_0, arg_11_1):
	local var_11_0 = var_0_1.RESTORE_LEGHTH * arg_11_0 + var_0_1.MIN_ANGLE

	arg_11_1.localRotation = Quaternion.Euler(0, 0, var_11_0)

def var_0_1.__barMeterConvert(arg_12_0):
	return arg_12_0

def var_0_1.__barRestoreConvert(arg_13_0, arg_13_1):
	local var_13_0 = var_0_1.BAR_STEP * arg_13_0 + var_0_1.BAR_MIN

	arg_13_1.localPosition = Vector3(var_13_0, 0, 0)

def var_0_1.Dispose(arg_14_0):
	arg_14_0._cloakComponent = None
	arg_14_0._cloakBar = None
	arg_14_0._progress = None
	arg_14_0._restoreMark = None
	arg_14_0._exposeFX = None

	Object.Destroy(arg_14_0._cloakBarGO)

	arg_14_0._cloakBarGO = None
