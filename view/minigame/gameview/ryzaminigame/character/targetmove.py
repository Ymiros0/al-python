local var_0_0 = class("TargetMove", import("view.miniGame.gameView.RyzaMiniGame.Reactor"))

def var_0_0.GetBaseOrder(arg_1_0):
	return 2

def var_0_0.InTimeRiver(arg_2_0):
	return True

def var_0_0.Init(arg_3_0, arg_3_1):
	arg_3_0.rtScale = arg_3_0._tf.Find("scale")

	var_0_0.super.Init(arg_3_0, arg_3_1)

def var_0_0.UpdatePos(arg_4_0, arg_4_1):
	arg_4_0.responder.UpdatePos(arg_4_0, arg_4_1)

	for iter_4_0, iter_4_1 in pairs(arg_4_0.rangeDic):
		arg_4_0.responder.RemoveListener(iter_4_0, arg_4_0, iter_4_1)

	arg_4_0.Calling("leave", {
		arg_4_0
	}, {
		{
			0,
			0
		}
	})
	var_0_0.super.UpdatePos(arg_4_0, arg_4_1)

	for iter_4_2, iter_4_3 in pairs(arg_4_0.rangeDic):
		arg_4_0.responder.AddListener(iter_4_2, arg_4_0, iter_4_3)

	arg_4_0.Calling("move", {
		arg_4_0
	}, {
		{
			0,
			0
		}
	})

def var_0_0.SetHide(arg_5_0, arg_5_1):
	arg_5_0.hide = arg_5_1

	arg_5_0.responder.UpdateHide(arg_5_0, arg_5_1)

def var_0_0.GetSpeed(arg_6_0):
	return arg_6_0.speed

var_0_0.SpeedDistance = {
	[0] = 1.5,
	2,
	2.5,
	3,
	3.5,
	4,
	4.5,
	5
}

def var_0_0.GetSpeedDis(arg_7_0):
	return arg_7_0.SpeedDistance[arg_7_0.GetSpeed()]

def var_0_0.TimeUpdate(arg_8_0, arg_8_1):
	arg_8_0.MoveUpdate(NewPos(0, 0))

def var_0_0.MoveUpdate(arg_9_0, arg_9_1):
	if arg_9_1.x == 0 and arg_9_1.y == 0:
		return arg_9_1

	arg_9_0.realPos = arg_9_0.realPos + arg_9_1

	arg_9_0.UpdatePosition()

	local var_9_0 = arg_9_0.realPos - arg_9_0.pos

	for iter_9_0, iter_9_1 in ipairs({
		"x",
		"y"
	}):
		if math.abs(var_9_0[iter_9_1]) > 0.5:
			var_9_0[iter_9_1] = var_9_0[iter_9_1] < 0 and -1 or 1
		else
			var_9_0[iter_9_1] = 0

	if var_9_0.x != 0 or var_9_0.y != 0:
		arg_9_0.UpdatePos(arg_9_0.pos + var_9_0)

local var_0_1 = {
	x = "y",
	y = "x"
}

def var_0_0.MoveDelta(arg_10_0, arg_10_1, arg_10_2):
	if arg_10_1.x == 0 and arg_10_1.y == 0 or arg_10_2 == 0:
		return NewPos(0, 0)

	local function var_10_0(arg_11_0)
		local var_11_0 = arg_11_0 - arg_10_0.realPos

		if var_11_0.x * var_11_0.x < 1 and var_11_0.y * var_11_0.y < 1:
			return True
		else
			return arg_10_0.responder.GetCellPassability(arg_11_0)

	local var_10_1 = {
		x = {
			0,
			0
		},
		y = {
			0,
			0
		}
	}

	for iter_10_0, iter_10_1 in ipairs({
		"x",
		"y"
	}):
		for iter_10_2, iter_10_3 in ipairs({
			-1,
			1
		}):
			local var_10_2 = NewPos(arg_10_0.pos.x, arg_10_0.pos.y)

			var_10_2[iter_10_1] = var_10_2[iter_10_1] + iter_10_3

			if var_10_0(var_10_2):
				var_10_1[iter_10_1][iter_10_2] = var_10_1[iter_10_1][iter_10_2] + iter_10_3

	local var_10_3 = arg_10_0.realPos - arg_10_0.pos
	local var_10_4 = var_10_3 + arg_10_1 * arg_10_2

	var_10_4.x = math.clamp(var_10_4.x, unpack(var_10_1.x))
	var_10_4.y = math.clamp(var_10_4.y, unpack(var_10_1.y))

	if var_10_4.x == 0 and var_10_4.y == 0:
		return var_10_4 - var_10_3
	elif var_10_4.x == 0:
		var_10_4.y = math.clamp(var_10_3.y + arg_10_1.y * arg_10_2, unpack(var_10_1.y))

		return var_10_4 - var_10_3
	elif var_10_4.y == 0:
		var_10_4.x = math.clamp(var_10_3.x + arg_10_1.x * arg_10_2, unpack(var_10_1.x))

		return var_10_4 - var_10_3
	else
		local var_10_5 = NewPos(arg_10_0.pos.x + (var_10_4.x < 0 and -1 or 1), arg_10_0.pos.y + (var_10_4.y < 0 and -1 or 1))

		if not var_10_0(var_10_5):
			local var_10_6 = arg_10_1.y * arg_10_1.y > arg_10_1.x * arg_10_1.x and "y" or "x"
			local var_10_7 = var_0_1[var_10_6]
			local var_10_8 = NewPos(0, 0)

			if var_10_3[var_10_7] * var_10_3[var_10_7] > arg_10_2 * arg_10_2:
				var_10_8[var_10_6] = -var_10_3[var_10_6]
				var_10_8[var_10_7] = (-var_10_3[var_10_7] < 0 and -1 or 1) * math.sqrt(arg_10_2 * arg_10_2 - var_10_8[var_10_6] * var_10_8[var_10_6])
			else
				var_10_8[var_10_7] = -var_10_3[var_10_7]
				var_10_8[var_10_6] = (arg_10_1[var_10_6] < 0 and -1 or 1) * math.sqrt(arg_10_2 * arg_10_2 - var_10_8[var_10_7] * var_10_8[var_10_7])

			local var_10_9 = var_10_3 + var_10_8

			var_10_9.x = math.clamp(var_10_9.x, unpack(var_10_1.x))
			var_10_9.y = math.clamp(var_10_9.y, unpack(var_10_1.y))

			return var_10_9 - var_10_3
		else
			return arg_10_1 * arg_10_2

def var_0_0.GetMoveInfo(arg_12_0):
	return arg_12_0.pos, NewPos(0, 0)

def var_0_0.GetCollideRange(arg_13_0):
	return {
		{
			{
				-0.5,
				0.5
			},
			{
				-0.5,
				0.5
			}
		}
	}

var_0_0.loopDic = {}

def var_0_0.PlayAnim(arg_14_0, arg_14_1):
	if arg_14_0.status != arg_14_1:
		arg_14_0.status = arg_14_1

		if not arg_14_0.loopDic[string.split(arg_14_1, "_")[1]]:
			arg_14_0.lock = True

		arg_14_0.mainTarget.GetComponent(typeof(Animator)).Play(arg_14_1)

return var_0_0
