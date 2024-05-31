ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleOpticalSightView = class("BattleOpticalSightView")

local var_0_2 = var_0_0.Battle.BattleOpticalSightView

var_0_2.__name = "BattleOpticalSightView"
var_0_2.SIGHT_A = var_0_1.ChargeWeaponConfig.SIGHT_A
var_0_2.SIGHT_B = var_0_1.ChargeWeaponConfig.SIGHT_B
var_0_2.SIGHT_C = var_0_1.ChargeWeaponConfig.SIGHT_C

def var_0_2.Ctor(arg_1_0, arg_1_1):
	arg_1_0._sightTF = arg_1_1.Find("Sight")
	arg_1_0._rulerTF = arg_1_1.Find("Ruler")
	arg_1_0._cornerTF = arg_1_1.Find("Corners")
	arg_1_0._active = False

def var_0_2.SetAreaBound(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0._totalLeftBound = arg_2_1
	arg_2_0._totalRightBound = arg_2_2

def var_0_2.SetActive(arg_3_0, arg_3_1):
	arg_3_0._active = arg_3_1

	SetActive(arg_3_0._sightTF, arg_3_1)
	SetActive(arg_3_0._rulerTF, arg_3_1)
	SetActive(arg_3_0._cornerTF, arg_3_1)

def var_0_2.Update(arg_4_0):
	if not arg_4_0._active:
		return

	local var_4_0 = arg_4_0._fleetVO.GetMotion().GetPos().x + var_0_2.SIGHT_C
	local var_4_1 = math.min(var_4_0, arg_4_0._totalRightBound)
	local var_4_2 = var_0_0.Battle.BattleVariable.CameraPosToUICamera(Vector3.New(var_4_1, 0, 5 + arg_4_0._fleetVO.GetMotion().GetPos().z))

	arg_4_0._sightTF.position = var_4_2

	local var_4_3 = Vector3.New(0, var_4_2.y)

	arg_4_0._rulerTF.position = var_4_3

def var_0_2.SetFleetVO(arg_5_0, arg_5_1):
	arg_5_0._fleetVO = arg_5_1

def var_0_2.Dispose(arg_6_0):
	arg_6_0._sightTF = None
	arg_6_0._rulerTF = None
	arg_6_0._cornerTF = None
	arg_6_0._fleetVO = None
