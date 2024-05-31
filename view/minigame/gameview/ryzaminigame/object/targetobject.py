local var_0_0 = class("TargetObject", import("view.miniGame.gameView.RyzaMiniGame.Reactor"))

def var_0_0.CellPassability(arg_1_0):
	return False

def var_0_0.FirePassability(arg_2_0):
	return 2

local function var_0_1(arg_3_0)
	local var_3_0 = math.random()

	for iter_3_0, iter_3_1 in ipairs(arg_3_0):
		if var_3_0 < iter_3_1[2]:
			return {
				name = "Item",
				type = iter_3_1[1]
			}
		else
			var_3_0 = var_3_0 - iter_3_1[2]

def var_0_0.TryDrop(arg_4_0, arg_4_1, arg_4_2):
	if not arg_4_1:
		return

	local var_4_0 = var_0_1(arg_4_1)

	if var_4_0:
		var_4_0.drop = arg_4_2
		var_4_0.pos = {
			arg_4_0.pos.x,
			arg_4_0.pos.y
		}

		arg_4_0.responder.Create(var_4_0)

return var_0_0
