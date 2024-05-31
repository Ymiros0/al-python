local var_0_0 = class("AttireApplyCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.type

	if not getProxy(AttireProxy).getAttireFrame(var_1_2, var_1_1):
		return

	local var_1_3 = getProxy(PlayerProxy)
	local var_1_4 = var_1_3.getData()

	pg.ConnectionMgr.GetInstance().Send(11005, {
		id = var_1_1,
		type = var_1_2
	}, 11006, function(arg_2_0)
		if arg_2_0.result == 0:
			var_1_4.updateAttireFrame(var_1_2, var_1_1)
			var_1_3.updatePlayer(var_1_4)
			arg_1_0.sendNotification(GAME.ATTIRE_APPLY_DONE)
		else
			print(arg_2_0.result))

return var_0_0
