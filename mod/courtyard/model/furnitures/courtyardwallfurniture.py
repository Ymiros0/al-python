local var_0_0 = class("CourtYardWallFurniture", import(".CourtYardFurniture"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.furniture_data_template[arg_1_2.configId or arg_1_2.id].size[2] = 1

	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

def var_0_0.Init(arg_2_0, arg_2_1):
	arg_2_0.UpdatePosition(arg_2_1)

def var_0_0.UpdatePosition(arg_3_0, arg_3_1):
	arg_3_0.SetPosition(arg_3_1)
	arg_3_0.SetDir(arg_3_0.GetDirection())

def var_0_0.GetInitSize(arg_4_0):
	if arg_4_0.RightDirectionLimited():
		return {
			{
				arg_4_0.sizeY,
				arg_4_0.sizeX
			}
		}
	elif arg_4_0.LeftDirectionLimited():
		return {
			{
				arg_4_0.sizeX,
				arg_4_0.sizeY
			}
		}
	else
		return {
			{
				arg_4_0.sizeX,
				arg_4_0.sizeY
			},
			{
				arg_4_0.sizeY,
				arg_4_0.sizeX
			}
		}

def var_0_0._GetDirection(arg_5_0, arg_5_1):
	if arg_5_0.RightDirectionLimited():
		return 2
	elif arg_5_0.LeftDirectionLimited():
		return 1
	elif arg_5_1.y - arg_5_1.x >= 1:
		return 1
	else
		return 2

def var_0_0.GetWidth(arg_6_0):
	return arg_6_0.config.size[1]

def var_0_0.GetDirection(arg_7_0):
	local var_7_0 = arg_7_0.GetPosition()

	return arg_7_0._GetDirection(var_7_0)

def var_0_0.Rotate(arg_8_0):
	return

def var_0_0.InActivityRange(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.GetHost().GetStorey().GetRange()

	return (arg_9_1.x == var_9_0.x or arg_9_1.y == var_9_0.y) and arg_9_1.x != arg_9_1.y

def var_0_0.LeftDirectionLimited(arg_10_0):
	return arg_10_0.config.belong == 3

def var_0_0.RightDirectionLimited(arg_11_0):
	return arg_11_0.config.belong == 4

def var_0_0.NormalizePosition(arg_12_0, arg_12_1, arg_12_2):
	local var_12_0 = arg_12_0.GetHost().GetStorey().GetRange().x
	local var_12_1 = arg_12_0._GetDirection(arg_12_1) == 1
	local var_12_2 = (var_12_1 and Vector2(arg_12_1.x, arg_12_1.y) or Vector2(arg_12_1.y, arg_12_1.x)).x
	local var_12_3 = arg_12_0.GetWidth()
	local var_12_4 = math.min(var_12_2, var_12_0 - var_12_3)
	local var_12_5 = math.max(arg_12_2, var_12_4)
	local var_12_6 = var_12_1 and Vector2(var_12_5, var_12_0) or Vector2(var_12_0, var_12_5)

	arg_12_0.SetDir(arg_12_0._GetDirection(var_12_6))

	return var_12_6

def var_0_0.SetDir(arg_13_0, arg_13_1):
	var_0_0.super.SetDir(arg_13_0, arg_13_1)
	arg_13_0.DispatchEvent(CourtYardEvent.ROTATE_FURNITURE, arg_13_0.dir)

def var_0_0.CanPutChild(arg_14_0):
	return False

return var_0_0
