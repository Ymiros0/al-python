local var_0_0 = class("EnemyConductor", import("view.miniGame.gameView.RyzaMiniGame.character.MoveEnemy"))

var_0_0.ConfigShildList = {
	2,
	0,
	0,
	0
}
var_0_0.BlockRange = 1

local var_0_1 = {
	"S",
	"E",
	"N",
	"W"
}

def var_0_0.InitUI(arg_1_0, arg_1_1):
	arg_1_0.shieldCount = underscore.rest(arg_1_0.ConfigShildList, 1)
	arg_1_0.rtShieldDic = {
		S = arg_1_0.rtScale.Find("front/Shield_S"),
		E = arg_1_0.rtScale.Find("front/Shield_E"),
		N = arg_1_0.rtScale.Find("back/Shield_N"),
		W = arg_1_0.rtScale.Find("front/Shield_W")
	}

	for iter_1_0, iter_1_1 in ipairs({
		"front",
		"back"
	}):
		eachChild(arg_1_0.rtScale.Find(iter_1_1), function(arg_2_0)
			arg_2_0.Find("Image").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
				setActive(arg_2_0.Find("Image"), False)
				setActive(arg_2_0, False)
				setImageAlpha(arg_2_0, 1))
			arg_2_0.Find("Protect").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
				setActive(arg_2_0.Find("Protect"), False)

				local var_4_0 = (table.indexof(var_0_1, string.split(arg_2_0.name, "_")[2]) - table.indexof(var_0_1, arg_1_0.statusMark) + 4) % 4 + 1

				if arg_1_0.shieldCount[var_4_0] <= 0:
					setImageAlpha(arg_2_0, 0)
					setActive(arg_2_0.Find("Image"), True)))

	var_0_0.super.InitUI(arg_1_0, arg_1_1)

	arg_1_0.hp = arg_1_1.hp or 2
	arg_1_0.hpMax = arg_1_0.hp
	arg_1_0.speed = arg_1_1.speed or 3

def var_0_0.InitRegister(arg_5_0, arg_5_1):
	var_0_0.super.InitRegister(arg_5_0, arg_5_1)
	arg_5_0.Register("block", function(arg_6_0)
		arg_5_0.shieldCount[arg_6_0] = arg_5_0.shieldCount[arg_6_0] - 1

		local var_6_0 = arg_5_0.rtShieldDic[var_0_1[(table.indexof(var_0_1, arg_5_0.statusMark) + arg_6_0 + 2) % 4 + 1]]

		setActive(var_6_0.Find("Protect"), True), {})

def var_0_0.CheckBlock(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	if arg_7_0.pos.x == arg_7_1.x and arg_7_0.pos.y == arg_7_1.y:
		return
	elif arg_7_0.pos.x == arg_7_1.x and math.clamp(arg_7_0.pos.y - arg_7_1.y, -arg_7_2[3], arg_7_2[1]) == arg_7_0.pos.y - arg_7_1.y or arg_7_0.pos.y == arg_7_1.y and math.clamp(arg_7_0.pos.x - arg_7_1.x, -arg_7_2[4], arg_7_2[2]) == arg_7_0.pos.x - arg_7_1.x:
		local var_7_0

		if arg_7_1.x < arg_7_0.pos.x:
			var_7_0 = "W"
		elif arg_7_1.x > arg_7_0.pos.x:
			var_7_0 = "E"
		elif arg_7_1.y < arg_7_0.pos.y:
			var_7_0 = "N"
		elif arg_7_1.y > arg_7_0.pos.y:
			var_7_0 = "S"
		else
			assert(False)

		local var_7_1 = (table.indexof(var_0_1, var_7_0) - table.indexof(var_0_1, arg_7_0.statusMark) + 4) % 4 + 1

		if arg_7_0.shieldCount[var_7_1] > 0:
			local var_7_2 = (table.indexof(var_0_1, var_7_0) + 1) % 4 + 1

			arg_7_2[var_7_2] = math.max(math.max(math.abs(arg_7_0.pos.x - arg_7_1.x), math.abs(arg_7_0.pos.y - arg_7_1.y)) - arg_7_0.BlockRange, 0)
			arg_7_3[var_7_2] = {
				arg_7_0,
				var_7_1
			}

def var_0_0.PlayAnim(arg_8_0, arg_8_1):
	var_0_0.super.PlayAnim(arg_8_0, arg_8_1)

	if arg_8_0.statusMark != string.split(arg_8_0.status, "_")[2]:
		arg_8_0.statusMark = string.split(arg_8_0.status, "_")[2]

		arg_8_0.UpdateShieldDisplay()

def var_0_0.UpdateShieldDisplay(arg_9_0):
	local var_9_0 = table.indexof(var_0_1, arg_9_0.statusMark)

	for iter_9_0 = 0, 3:
		local var_9_1 = arg_9_0.rtShieldDic[var_0_1[(var_9_0 - 1 + iter_9_0) % 4 + 1]]

		eachChild(var_9_1, function(arg_10_0)
			setActive(arg_10_0, False))
		setImageAlpha(var_9_1, 1)
		setActive(var_9_1, arg_9_0.shieldCount[iter_9_0 + 1] > 0)

return var_0_0
