local var_0_0 = class("EnemyBossConductor", import("view.miniGame.gameView.RyzaMiniGame.character.EnemyConductor"))

var_0_0.ConfigShildList = {
	4,
	0,
	0,
	0
}
var_0_0.BlockRange = 2

def var_0_0.InitUI(arg_1_0, arg_1_1):
	var_0_0.super.InitUI(arg_1_0, arg_1_1)

	arg_1_0.hp = arg_1_1.hp or 4
	arg_1_0.hpMax = arg_1_0.hp
	arg_1_0.speed = arg_1_1.speed or 4
	arg_1_0.damageDic = {}

def var_0_0.InitRegister(arg_2_0, arg_2_1):
	var_0_0.super.InitRegister(arg_2_0, arg_2_1)
	arg_2_0.Deregister("burn")

def var_0_0.TimeTrigger(arg_3_0, arg_3_1):
	var_0_0.super.TimeTrigger(arg_3_0, arg_3_1)

	for iter_3_0, iter_3_1 in ipairs(arg_3_0.responder.CollideFire(arg_3_0)):
		if not arg_3_0.damageDic[iter_3_1]:
			arg_3_0.damageDic[iter_3_1] = True

			arg_3_0.Hurt(1)

def var_0_0.GetUIHeight(arg_4_0):
	return 192

return var_0_0
