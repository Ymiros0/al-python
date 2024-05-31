local var_0_0 = class("WorldCarryItem", import("...BaseEntity"))

var_0_0.Fields = {
	config = "table",
	id = "number",
	offsetRow = "number",
	offsetColumn = "number"
}
var_0_0.EventUpdateOffset = "WorldCarryItem.EventUpdateOffset"

def var_0_0.Setup(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1
	arg_1_0.config = pg.world_carry_item[arg_1_0.id]

	assert(arg_1_0.config, "world_carry_item not exist. " .. arg_1_0.id)

	arg_1_0.offsetRow = 0
	arg_1_0.offsetColumn = 0

def var_0_0.UpdateOffset(arg_2_0, arg_2_1, arg_2_2):
	if arg_2_0.offsetRow != arg_2_1 or arg_2_0.offsetColumn != arg_2_2:
		arg_2_0.offsetRow = arg_2_1
		arg_2_0.offsetColumn = arg_2_2

		arg_2_0.DispatchEvent(var_0_0.EventUpdateOffset)

def var_0_0.GetScale(arg_3_0):
	return Vector3(arg_3_0.config.scale / 100, arg_3_0.config.scale / 100, 1)

def var_0_0.IsAvatar(arg_4_0):
	return arg_4_0.config.enemyicon == 1

return var_0_0
