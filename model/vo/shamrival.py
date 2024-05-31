local var_0_0 = class("ShamRival", import(".Rival"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.id = arg_1_1.id
	arg_1_0.level = arg_1_1.level
	arg_1_0.name = arg_1_1.name
	arg_1_0.vanguardShips = {}
	arg_1_0.mainShips = {}

	_.each(arg_1_1.ship_list, function(arg_2_0)
		local var_2_0 = Ship.New(arg_2_0)
		local var_2_1 = var_2_0.getTeamType()

		if var_2_1 == TeamType.Vanguard:
			table.insert(arg_1_0.vanguardShips, var_2_0)
		elif var_2_1 == TeamType.Main:
			table.insert(arg_1_0.mainShips, var_2_0))

return var_0_0
