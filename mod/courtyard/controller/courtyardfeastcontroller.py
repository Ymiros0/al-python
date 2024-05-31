local var_0_0 = class("CourtYardFeastController", import(".CourtYardController"))

def var_0_0.ShipBubbleInterActionFinish(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.storey.GetShip(arg_1_1)

	if var_1_0:
		local var_1_1 = var_1_0.GetIsSpecialValue()

		arg_1_0.SendNotification(CourtYardEvent._FEAST_INTERACTION, {
			groupId = arg_1_1,
			special = var_1_1
		})

def var_0_0.UpdateBubble(arg_2_0, arg_2_1, arg_2_2):
	local var_2_0 = arg_2_0.storey.GetShip(arg_2_1)

	assert(var_2_0, arg_2_1)

	if var_2_0:
		var_2_0.UpdateBubble(arg_2_2)

def var_0_0.UpdateChatBubble(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = arg_3_0.storey.GetShip(arg_3_1)

	assert(var_3_0, arg_3_1)

	if var_3_0:
		var_3_0.UpdateChatBubble(arg_3_2)

def var_0_0.ExitAllShip(arg_4_0):
	for iter_4_0, iter_4_1 in pairs(arg_4_0.storey.ships):
		arg_4_0.storey.ExitShip(iter_4_0)

def var_0_0.AddShipWithSpecialPosition(arg_5_0, arg_5_1):
	if not arg_5_0.storey:
		return

	local var_5_0 = arg_5_0.DataToShip(arg_5_1)

	var_5_0.SetPosition(Vector2(25, 11))

	local var_5_1 = arg_5_0.storey.GetAroundEmptyPosition(var_5_0)

	if var_5_1:
		var_5_0.SetPosition(var_5_1)
		arg_5_0.storey.AddShip(var_5_0)
	else
		arg_5_0.SendNotification(CourtYardEvent._NO_POS_TO_ADD_SHIP, var_5_0.id)

def var_0_0.ShipEnterFeast(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_0.storey.GetShip(arg_6_1)

	if var_6_0:
		var_6_0.EnterFeast()

return var_0_0
