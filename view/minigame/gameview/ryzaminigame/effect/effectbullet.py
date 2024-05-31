local var_0_0 = class("EffectBullet", import("view.miniGame.gameView.RyzaMiniGame.effect.TargetEffect"))

def var_0_0.GetBaseOrder(arg_1_0):
	if arg_1_0.mark == "N":
		return var_0_0.super.GetBaseOrder(arg_1_0)
	else
		return 500

def var_0_0.InTimeRiver(arg_2_0):
	return True

local var_0_1 = {
	S = {
		0,
		1
	},
	N = {
		0,
		-1
	},
	E = {
		1,
		0
	},
	W = {
		-1,
		0
	}
}

def var_0_0.InitUI(arg_3_0, arg_3_1):
	arg_3_0.mark = arg_3_1.mark

	arg_3_0._tf.Find("Image").GetComponent(typeof(Animator)).Play("Bullet_" .. arg_3_0.mark)

	arg_3_0.dir = NewPos(unpack(var_0_1[arg_3_0.mark]))

def var_0_0.GetSpeedDis(arg_4_0):
	return 2

def var_0_0.TimeUpdate(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.dir * arg_5_0.GetSpeedDis() * arg_5_1

	if not arg_5_0.responder.InRange(arg_5_0.realPos + var_5_0):
		arg_5_0.Destroy()

		return

	arg_5_0.MoveUpdate(var_5_0)
	arg_5_0.TimeTrigger(arg_5_1)

def var_0_0.MoveUpdate(arg_6_0, arg_6_1):
	if arg_6_1.x == 0 and arg_6_1.y == 0:
		return arg_6_1

	arg_6_0.realPos = arg_6_0.realPos + arg_6_1

	arg_6_0.UpdatePosition()

	local var_6_0 = arg_6_0.realPos - arg_6_0.pos + arg_6_1

	if math.abs(var_6_0.x) >= 0.5 or math.abs(var_6_0.y) >= 0.5:
		var_6_0.x = math.abs(var_6_0.x) < 0.5 and 0 or var_6_0.x < 0 and -1 or 1
		var_6_0.y = math.abs(var_6_0.y) < 0.5 and 0 or var_6_0.y < 0 and -1 or 1

		arg_6_0.UpdatePos(arg_6_0.pos + var_6_0)

def var_0_0.UpdatePos(arg_7_0, arg_7_1):
	arg_7_0.responder.UpdatePos(arg_7_0, arg_7_1)
	var_0_0.super.UpdatePos(arg_7_0, arg_7_1)

def var_0_0.TimeTrigger(arg_8_0, arg_8_1):
	if arg_8_0.responder.CollideRyza(arg_8_0):
		arg_8_0.Calling("hit", {
			1,
			arg_8_0.realPos
		}, MoveRyza)
		arg_8_0.Destroy()

def var_0_0.GetCollideRange(arg_9_0):
	local var_9_0 = {
		{
			-0.1875,
			0.1875
		},
		{
			-0.1875,
			0.1875
		}
	}

	if arg_9_0.dir.x < 0:
		var_9_0[1] = {
			-0.5,
			0.25
		}
	elif arg_9_0.dir.x > 0:
		var_9_0[1] = {
			-0.25,
			0.5
		}
	elif arg_9_0.dir.y < 0:
		var_9_0[2] = {
			-0.5,
			0.25
		}
	elif arg_9_0.dir.y > 0:
		var_9_0[1] = {
			-0.25,
			0.5
		}
	else
		assert(False)

	return {
		var_9_0
	}

return var_0_0
