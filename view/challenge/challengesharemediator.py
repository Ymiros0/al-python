local var_0_0 = class("ChallengeShareMediator", import("..base.ContextMediator"))

def var_0_0.register(arg_1_0):
	local var_1_0 = arg_1_0.contextData.mode
	local var_1_1 = getProxy(ChallengeProxy).getUserChallengeInfo(var_1_0)

	arg_1_0.viewComponent.setLevel(var_1_1.getLevel())

	local var_1_2 = {
		regularFleet = var_1_1.getRegularFleet(),
		submarineFleet = var_1_1.getSubmarineFleet()
	}
	local var_1_3 = var_1_2.regularFleet.getShipsByTeam(TeamType.Main, True)[1]

	arg_1_0.viewComponent.setFlagShipPaint(var_1_3.getPainting())

	local var_1_4 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_2.regularFleet.getShips(True)):
		if iter_1_1.id != var_1_3.id:
			table.insert(var_1_4, iter_1_1.getPainting())

	for iter_1_2, iter_1_3 in ipairs(var_1_2.submarineFleet.getShips(True)):
		if iter_1_3.id != var_1_3.id:
			table.insert(var_1_4, iter_1_3.getPainting())

	arg_1_0.viewComponent.setShipPaintList(var_1_4)

return var_0_0
