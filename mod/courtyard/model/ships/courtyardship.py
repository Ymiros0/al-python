local var_0_0 = class("CourtYardShip", import("..map.CourtYardDepthItem"))

var_0_0.STATE_IDLE = 0
var_0_0.STATE_MOVE = 1
var_0_0.STATE_MOVING_ZERO = 2
var_0_0.STATE_MOVING_HALF = 3
var_0_0.STATE_MOVING_ONE = 4
var_0_0.STATE_DRAG = 5
var_0_0.STATE_TOUCH = 6
var_0_0.STATE_GETAWARD = 7
var_0_0.STATE_STOP = 8
var_0_0.STATE_INTERACT = 9
var_0_0.STATE_CANCEL_INTERACT = 10

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.id = arg_1_2.id
	arg_1_0.configId = arg_1_2.configId
	arg_1_0.prefab = arg_1_2.getPrefab()
	arg_1_0.attachments = arg_1_2.getAttachmentPrefab()
	arg_1_0.inimacy = arg_1_2.state_info_3 or 0
	arg_1_0.coin = arg_1_2.state_info_4 or 0
	arg_1_0.skinId = arg_1_2.skinId
	arg_1_0.groupId = arg_1_2.groupId
	arg_1_0.config = pg.ship_data_statistics[arg_1_0.configId]
	arg_1_0.moveTime = math.floor(1 / arg_1_0.config.backyard_speed)

	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_0.id, 1, 1)

	arg_1_0.state = var_0_0.STATE_IDLE
	arg_1_0.moveCnt = 0

def var_0_0.GetLevel(arg_2_0):
	return 2

def var_0_0.GetSkinID(arg_3_0):
	return arg_3_0.skinId

def var_0_0.GetGroupID(arg_4_0):
	return arg_4_0.groupId

def var_0_0.GetObjType(arg_5_0):
	return CourtYardConst.OBJ_TYPE_SHIP

def var_0_0.SetPosition(arg_6_0, arg_6_1):
	var_0_0.super.SetPosition(arg_6_0, arg_6_1)

	if arg_6_0.state == CourtYardShip.STATE_MOVING_HALF:
		return

	arg_6_0.DispatchEvent(CourtYardEvent.SHIP_POSITION_CHANGE, arg_6_1, arg_6_0.GetOffset())

def var_0_0.InActivityRange(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.GetHost().GetStorey().GetRange()

	return arg_7_1.x < var_7_0.x and arg_7_1.y < var_7_0.y and arg_7_1.x >= 0 and arg_7_1.y >= 0

def var_0_0.GetDeathType(arg_8_0):
	return CourtYardConst.DEPTH_TYPE_SHIP

def var_0_0.GetShipType(arg_9_0):
	return CourtYardConst.SHIP_TYPE_SELF

def var_0_0._ChangeState(arg_10_0, arg_10_1, arg_10_2):
	arg_10_0.state = arg_10_1

	arg_10_0.DispatchEvent(CourtYardEvent.SHIP_STATE_CHANGE, arg_10_1, arg_10_2)

def var_0_0.ChangeState(arg_11_0, arg_11_1, arg_11_2):
	arg_11_0.Clear()

	if arg_11_1 == var_0_0.STATE_IDLE:
		arg_11_0.OnStateIdle()
	elif arg_11_1 == var_0_0.STATE_MOVING_ONE:
		arg_11_0.OnStateMoveOne()
	elif (arg_11_1 == var_0_0.STATE_STOP or arg_11_1 == var_0_0.STATE_TOUCH or arg_11_1 == var_0_0.STATE_GETAWARD) and arg_11_0.state == var_0_0.STATE_INTERACT:
		-- block empty
	elif arg_11_1 == var_0_0.STATE_INTERACT:
		arg_11_0.OnInterAction(arg_11_2)
	else
		arg_11_0._ChangeState(arg_11_1)

def var_0_0.ShouldResetPosition(arg_12_0):
	return arg_12_0.state == var_0_0.STATE_STOP or arg_12_0.state == var_0_0.STATE_CANCEL_INTERACT

def var_0_0.WillInteraction(arg_13_0):
	arg_13_0.DispatchEvent(CourtYardEvent.SHIP_WILL_INTERACTION, slot)

def var_0_0.StartInteraction(arg_14_0, arg_14_1, arg_14_2):
	if arg_14_2:
		arg_14_0.interactionSlot = arg_14_1
	else
		arg_14_0.ChangeState(CourtYardShip.STATE_INTERACT, arg_14_1)

def var_0_0.UpdateInteraction(arg_15_0, ...):
	arg_15_0.DispatchEvent(CourtYardEvent.SHIP_UPDATE_INTERACTION, ...)

def var_0_0.ClearInteraction(arg_16_0, arg_16_1, arg_16_2, arg_16_3):
	arg_16_0.interactionSlot = None

	if not arg_16_3:
		arg_16_0.ChangeState(var_0_0.STATE_CANCEL_INTERACT)
		arg_16_0.DispatchEvent(CourtYardEvent.SHIP_STOP_INTERACTION, arg_16_1)

def var_0_0.OnStateIdle(arg_17_0):
	arg_17_0._ChangeState(var_0_0.STATE_IDLE)

	arg_17_0.timer = Timer.New(function()
		arg_17_0.moveCnt = math.random(1, 5)

		arg_17_0._ChangeState(var_0_0.STATE_MOVE), math.random(10, 20), 1)

	arg_17_0.timer.Start()

def var_0_0.OnStateMoveOne(arg_19_0):
	arg_19_0._ChangeState(var_0_0.STATE_MOVING_ONE)
	arg_19_0.ClearMarkPosition()

	arg_19_0.timer = Timer.New(function()
		arg_19_0.moveCnt = arg_19_0.moveCnt - 1

		if arg_19_0.moveCnt <= 0:
			arg_19_0.ChangeState(var_0_0.STATE_IDLE)
		else
			arg_19_0._ChangeState(var_0_0.STATE_MOVE), arg_19_0.moveTime * 0.5, 1)

	arg_19_0.timer.Start()

def var_0_0.OnInterAction(arg_21_0, arg_21_1):
	arg_21_0.interactionSlot = arg_21_1

	arg_21_0._ChangeState(var_0_0.STATE_INTERACT)
	arg_21_0.DispatchEvent(CourtYardEvent.SHIP_START_INTERACTION, arg_21_1)

def var_0_0.GetInterActionData(arg_22_0):
	return arg_22_0.interactionSlot

def var_0_0.Move(arg_23_0, arg_23_1):
	arg_23_0.MarkPosition(arg_23_1)
	arg_23_0.ChangeState(var_0_0.STATE_MOVING_ZERO)

	arg_23_0.timer = Timer.New(function()
		arg_23_0.ChangeState(var_0_0.STATE_MOVING_HALF), arg_23_0.moveTime * 0.5, 1)

	arg_23_0.timer.Start()
	arg_23_0.DispatchEvent(CourtYardEvent.SHIP_MOVE, arg_23_1, arg_23_0.GetOffset())

def var_0_0.GetState(arg_25_0):
	return arg_25_0.state

def var_0_0.GetPrefab(arg_26_0):
	return arg_26_0.prefab

def var_0_0.getPrefab(arg_27_0):
	return arg_27_0.GetPrefab()

def var_0_0.getAttachmentPrefab(arg_28_0):
	return arg_28_0.attachments

def var_0_0.GetMoveTime(arg_29_0):
	return arg_29_0.moveTime

def var_0_0.Clear(arg_30_0):
	if arg_30_0.timer:
		arg_30_0.timer.Stop()

		arg_30_0.timer = None

def var_0_0.ChangeInimacy(arg_31_0, arg_31_1):
	arg_31_0.inimacy = arg_31_1

	arg_31_0.DispatchEvent(CourtYardEvent.SHIP_INIMACY_CHANGE, arg_31_1)

def var_0_0.ChangeCoin(arg_32_0, arg_32_1):
	arg_32_0.coin = arg_32_1

	arg_32_0.DispatchEvent(CourtYardEvent.SHIP_COIN_CHANGE, arg_32_1)

def var_0_0.ClearInimacy(arg_33_0):
	local var_33_0 = arg_33_0.inimacy

	if var_33_0 <= 0:
		return

	arg_33_0.ChangeInimacy(0)
	arg_33_0.ChangeState(var_0_0.STATE_GETAWARD)
	arg_33_0.DispatchEvent(CourtYardEvent.SHIP_GET_AWARD, var_33_0, 2)

def var_0_0.ClearCoin(arg_34_0):
	local var_34_0 = arg_34_0.coin

	if var_34_0 <= 0:
		return

	arg_34_0.ChangeCoin(0)
	arg_34_0.ChangeState(var_0_0.STATE_GETAWARD)
	arg_34_0.DispatchEvent(CourtYardEvent.SHIP_GET_AWARD, var_34_0, 1)

def var_0_0.AddExp(arg_35_0, arg_35_1):
	arg_35_0.DispatchEvent(CourtYardEvent.SHIP_GET_AWARD, arg_35_1, 3)

def var_0_0.GetInterActionBgm(arg_36_0):
	return None

def var_0_0.Dispose(arg_37_0):
	var_0_0.super.Dispose(arg_37_0)
	arg_37_0.Clear()

	local var_37_0 = arg_37_0.GetInterActionData()

	if var_37_0:
		var_37_0.Stop()

return var_0_0
