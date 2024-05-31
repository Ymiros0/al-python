local var_0_0 = class("RawFurnitureData")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.config = pg.furniture_data_template[arg_1_1.configId]
	arg_1_0.name = arg_1_0.config.name
	arg_1_0.id = arg_1_1.id
	arg_1_0.floor = arg_1_1.floor
	arg_1_0.parent = arg_1_1.parent
	arg_1_0.dir = arg_1_1.dir
	arg_1_0.child = arg_1_1.child
	arg_1_0.position = arg_1_1.position
	arg_1_0.x = arg_1_0.position and arg_1_0.position.x or arg_1_1.x
	arg_1_0.y = arg_1_0.position and arg_1_0.position.y or arg_1_1.y

	if arg_1_0.dir == 1:
		arg_1_0.sizeX = arg_1_0.config.size[1]
		arg_1_0.sizeY = arg_1_0.config.size[2]
	else
		arg_1_0.sizeX = arg_1_0.config.size[2]
		arg_1_0.sizeY = arg_1_0.config.size[1]

def var_0_0.IsCompletion(arg_2_0):
	if not arg_2_0.floor:
		return False

	if not arg_2_0.parent:
		return False

	if not arg_2_0.dir or arg_2_0.dir < 0 or arg_2_0.dir > 2:
		return False

	if not arg_2_0.child:
		return False

	if not arg_2_0.x or not arg_2_0.y:
		return False

	return True

def var_0_0.ExistParnet(arg_3_0):
	return arg_3_0.parent and arg_3_0.parent != 0

def var_0_0.LegalParent(arg_4_0, arg_4_1):
	if not arg_4_1:
		return False

	if not arg_4_1.LegalChild(arg_4_0):
		return False

	return True

def var_0_0.LegalChild(arg_5_0, arg_5_1):
	if not arg_5_1:
		return False

	if arg_5_1.parent != arg_5_0.id:
		return False

	local var_5_0 = {}

	for iter_5_0, iter_5_1 in pairs(arg_5_0.child or {}):
		table.insert(var_5_0, iter_5_0)

	if not table.contains(var_5_0, arg_5_1.id):
		return False

	return True

def var_0_0.InSide(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4):
	if arg_6_0.config.belong == 1 and arg_6_0.config.type != 1 and arg_6_0.config.type != 4 and not arg_6_0.ExistParnet():
		local var_6_0 = arg_6_0.GetAreaByPosition()

		return _.all(var_6_0, function(arg_7_0)
			return arg_7_0.x >= arg_6_1 and arg_7_0.y >= arg_6_2 and arg_7_0.x <= arg_6_3 and arg_7_0.y <= arg_6_4)

	if arg_6_0.config.belong == 3 and arg_6_0.x >= arg_6_3 + 1:
		return False

	if arg_6_0.config.belong == 4 and arg_6_0.y >= arg_6_4 + 1:
		return False

	return True

def var_0_0.GetAreaByPosition(arg_8_0):
	local var_8_0 = {}

	for iter_8_0 = arg_8_0.x, arg_8_0.x + arg_8_0.sizeX - 1:
		for iter_8_1 = arg_8_0.y, arg_8_0.y + arg_8_0.sizeY - 1:
			table.insert(var_8_0, Vector2(iter_8_0, iter_8_1))

	return var_8_0

def var_0_0.MatOrPaper(arg_9_0):
	return arg_9_0.config.type == 5 or arg_9_0.config.type == 10 or arg_9_0.config.type == 1 or arg_9_0.config.type == 4

return var_0_0
