local var_0_0 = class("EnemyChaser", import("view.miniGame.gameView.RyzaMiniGame.character.MoveEnemy"))

var_0_0.WeaponName = "Bullet"
var_0_0.ConfigSkillCD = 10
var_0_0.StatusOffset = {
	Attack_E = {
		1,
		0
	},
	Attack_N = {
		0,
		-1
	},
	Attack_W = {
		-1,
		0
	},
	Attack_S = {
		0,
		1
	}
}

def var_0_0.InitUI(arg_1_0, arg_1_1):
	var_0_0.super.InitUI(arg_1_0, arg_1_1)

	arg_1_0.hp = arg_1_1.hp or 1
	arg_1_0.hpMax = arg_1_0.hp
	arg_1_0.speed = arg_1_1.speed or 2
	arg_1_0.skillCD = 0

	arg_1_0.mainTarget.GetComponent(typeof(DftAniEvent)).SetTriggerEvent(function()
		local var_2_0 = arg_1_0.StatusOffset[arg_1_0.status]

		arg_1_0.responder.Create({
			name = arg_1_0.WeaponName,
			pos = {
				arg_1_0.pos.x + var_2_0[1],
				arg_1_0.pos.y + var_2_0[2]
			},
			realPos = {
				arg_1_0.realPos.x + var_2_0[1],
				arg_1_0.realPos.y + var_2_0[2]
			},
			mark = string.split(arg_1_0.status, "_")[2]
		}))

def var_0_0.TimeTrigger(arg_3_0, arg_3_1):
	var_0_0.super.TimeTrigger(arg_3_0, arg_3_1)

	arg_3_0.skillCD = arg_3_0.skillCD - arg_3_1

	if not arg_3_0.lock and arg_3_0.skillCD <= 0 and arg_3_0.responder.SearchRyza(arg_3_0, arg_3_0.search):
		local var_3_0 = arg_3_0.responder.reactorRyza.pos

		if (var_3_0.x == arg_3_0.pos.x or var_3_0.y == arg_3_0.pos.y) and (var_3_0 - arg_3_0.pos).SqrMagnitude() >= 9:
			local var_3_1 = var_3_0 - arg_3_0.pos

			if var_3_1.x > 0:
				arg_3_0.PlayAnim("Attack_E")
			elif var_3_1.x < 0:
				arg_3_0.PlayAnim("Attack_W")
			elif var_3_1.y > 0:
				arg_3_0.PlayAnim("Attack_S")
			elif var_3_1.y < 0:
				arg_3_0.PlayAnim("Attack_N")

			arg_3_0.skillCD = arg_3_0.ConfigSkillCD

return var_0_0
