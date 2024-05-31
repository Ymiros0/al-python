local var_0_0 = class("EnemyBossChaser", import("view.miniGame.gameView.RyzaMiniGame.character.EnemyChaser"))

var_0_0.WeaponName = "Laser"
var_0_0.ConfigSkillCD = 10
var_0_0.StatusOffset = setmetatable({}, {
	def __index:(arg_1_0, arg_1_1)
		return {
			0,
			0
		}
})

def var_0_0.InitUI(arg_2_0, arg_2_1):
	var_0_0.super.InitUI(arg_2_0, arg_2_1)

	arg_2_0.hp = arg_2_1.hp or 4
	arg_2_0.hpMax = arg_2_0.hp
	arg_2_0.speed = arg_2_1.speed or 3
	arg_2_0.damageDic = {}

def var_0_0.InitRegister(arg_3_0, arg_3_1):
	return

def var_0_0.TimeTrigger(arg_4_0, arg_4_1):
	var_0_0.super.TimeTrigger(arg_4_0, arg_4_1)

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.responder.CollideFire(arg_4_0)):
		if not arg_4_0.damageDic[iter_4_1]:
			arg_4_0.damageDic[iter_4_1] = True

			arg_4_0.Hurt(1)

def var_0_0.GetUIHeight(arg_5_0):
	return 192

return var_0_0
