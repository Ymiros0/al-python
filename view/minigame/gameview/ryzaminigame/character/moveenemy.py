local var_0_0 = class("MoveEnemy", import("view.miniGame.gameView.RyzaMiniGame.character.TargetMove"))

def var_0_0.InitUI(arg_1_0, arg_1_1):
	arg_1_0.hp = arg_1_1.hp or 3
	arg_1_0.hpMax = arg_1_0.hp
	arg_1_0.speed = arg_1_1.speed or 1
	arg_1_0.search = arg_1_1.search or 4
	arg_1_0.wander = arg_1_1.wander or 3
	arg_1_0.mainTarget = arg_1_0.rtScale.Find("main")

	arg_1_0.PlayWait()
	arg_1_0.mainTarget.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		arg_1_0.lock = False

		if arg_1_0.hp <= 0:
			arg_1_0.Destroy())

def var_0_0.InitRegister(arg_3_0, arg_3_1):
	arg_3_0.Register("burn", function()
		arg_3_0.Hurt(1), {
		{
			0,
			0
		}
	})

def var_0_0.Hurt(arg_5_0, arg_5_1):
	arg_5_0.hp = arg_5_0.hp - arg_5_1

	arg_5_0.responder.SyncStatus(arg_5_0, "hp", {
		num = arg_5_0.hp,
		max = arg_5_0.hpMax
	})

	if arg_5_0.hp > 0:
		arg_5_0.PlayDamage()
	else
		arg_5_0.DeregisterAll()
		arg_5_0.PlayDead()

var_0_0.SpeedDistance = {
	[0] = 0,
	1,
	1.5,
	2,
	2.5,
	3,
	3.5,
	4
}

def var_0_0.TimeUpdate(arg_6_0, arg_6_1):
	if not arg_6_0.lock:
		local var_6_0, var_6_1 = arg_6_0.GetMoveInfo()
		local var_6_2

		if var_6_0:
			var_6_2 = arg_6_0.MoveDelta(var_6_0, arg_6_0.GetSpeedDis() * arg_6_1)

			arg_6_0.ClearWander()
		else
			local var_6_3
			local var_6_4

			if not arg_6_0.wanderPos:
				arg_6_0.wanderPos = arg_6_0.pos
				arg_6_0.wanderDir = NewPos(0, 0)
				arg_6_0.wanderTime = 1.5

			if arg_6_1 >= arg_6_0.wanderTime:
				arg_6_0.wanderDir = (arg_6_0.wanderPos + NewPos(math.random() * 2 - 1, math.random() * 2 - 1) * arg_6_0.wander - arg_6_0.realPos).Normalize()

			var_6_2 = var_0_0.super.MoveDelta(arg_6_0, arg_6_0.wanderDir, arg_6_0.GetSpeedDis() * arg_6_1)

			if var_6_2.x == 0 and var_6_2.y == 0:
				arg_6_0.wanderTime = arg_6_0.wanderTime - arg_6_1
			else
				arg_6_0.wanderTime = 1.5

			arg_6_0.wanderDir = var_6_2.Normalize()
			var_6_1 = arg_6_0.wanderDir

		if var_6_1.x == 0 and var_6_1.y == 0:
			arg_6_0.PlayWait()
		else
			arg_6_0.PlayMove(RyzaMiniGameConfig.GetFourDirMark(var_6_1))

		arg_6_0.MoveUpdate(var_6_2)

	arg_6_0.TimeTrigger(arg_6_1)

	if arg_6_0.hide:
		arg_6_0.UpdateAlpha()

def var_0_0.MoveDelta(arg_7_0, arg_7_1, arg_7_2):
	local var_7_0 = arg_7_1 - arg_7_0.realPos

	if var_7_0.x == 0 and var_7_0.y == 0:
		return NewPos(0, 0)
	else
		return var_7_0 * math.min(1, arg_7_2 / math.sqrt(var_7_0.SqrMagnitude()))

def var_0_0.GetMoveInfo(arg_8_0):
	if arg_8_0.responder.SearchRyza(arg_8_0, arg_8_0.search):
		local var_8_0 = arg_8_0.responder.Wayfinding(arg_8_0)

		if var_8_0 and #var_8_0 > 0:
			local var_8_1 = var_8_0[#var_8_0]
			local var_8_2 = var_8_1 - arg_8_0.realPos
			local var_8_3 = var_8_1 - arg_8_0.pos

			if var_8_2.SqrMagnitude() > var_8_3.SqrMagnitude():
				var_8_1 = arg_8_0.pos

			local var_8_4 = var_8_1 - arg_8_0.realPos

			if var_8_4.x != 0 or var_8_4.y != 0:
				var_8_4 = var_8_4 * (1 / math.sqrt(var_8_4.SqrMagnitude()))

			return var_8_1, var_8_4

	return None, NewPos(0, 0)

def var_0_0.ClearWander(arg_9_0):
	arg_9_0.wanderPos = None
	arg_9_0.wanderDir = None
	arg_9_0.wanderTime = None

def var_0_0.PlayWait(arg_10_0):
	arg_10_0.PlayAnim("Wait_" .. (string.split(arg_10_0.status, "_")[2] or "S"))

def var_0_0.PlayMove(arg_11_0, arg_11_1):
	arg_11_0.PlayAnim("Move_" .. arg_11_1)

def var_0_0.PlayDamage(arg_12_0):
	if not arg_12_0.lock:
		arg_12_0.PlayAnim("Damage_" .. (string.split(arg_12_0.status, "_")[2] or "S"))

def var_0_0.PlayDead(arg_13_0):
	arg_13_0.SetHide(False)
	arg_13_0.PlayAnim("Dead_" .. (string.split(arg_13_0.status, "_")[2] or "S"))

var_0_0.loopDic = {
	Wait = True,
	Move = True
}

def var_0_0.GetUIHeight(arg_14_0):
	return 128

def var_0_0.SetHide(arg_15_0, arg_15_1):
	var_0_0.super.SetHide(arg_15_0, arg_15_1)
	arg_15_0.UpdateAlpha()

local var_0_1 = 7

def var_0_0.UpdateAlpha(arg_16_0):
	local var_16_0 = 1
	local var_16_1 = not arg_16_0.hide and 1 or arg_16_0.responder.reactorRyza.hide and (arg_16_0.responder.reactorRyza.realPos - arg_16_0.realPos).SqrMagnitude() < var_0_1 * var_0_1 and 0.7 or 0

	GetOrAddComponent(arg_16_0._tf, typeof(CanvasGroup)).alpha = var_16_1

def var_0_0.TimeTrigger(arg_17_0, arg_17_1):
	if arg_17_0.hp > 0 and arg_17_0.responder.CollideRyza(arg_17_0):
		arg_17_0.Calling("hit", {
			1,
			arg_17_0.realPos
		}, MoveRyza)

return var_0_0
