local var_0_0 = class("InstagramActivityCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()

	print("cmd.", var_1_0.cmd, "arg1.", var_1_0.arg1, "arg2.", var_1_0.arg2, "activity_id.", var_1_0.activity_id)

	local var_1_1 = getProxy(InstagramProxy)

	if ActivityConst.INSTAGRAM_OP_ACTIVE == var_1_0.cmd:
		local var_1_2 = getProxy(ActivityProxy)
		local var_1_3 = var_1_2.getActivityById(var_1_0.activity_id)

		pg.ConnectionMgr.GetInstance().Send(11202, {
			cmd = 1,
			activity_id = var_1_0.activity_id,
			arg1 = var_1_0.arg1 or 0,
			arg2 = var_1_0.arg2 or 0,
			arg3 = var_1_0.arg3 or 0,
			arg_list = {}
		}, 11203, function(arg_2_0)
			if arg_2_0.result == 0:
				local var_2_0 = Instagram.New(arg_2_0.ins_message)

				var_1_1.UpdateMessage(var_2_0)
				var_1_3.UpdateActiveCnt()
				var_1_2.updateActivity(var_1_3)
				arg_1_0.sendNotification(GAME.ACTIVITY_BE_UPDATED, {
					activity = var_1_3
				})
				arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_OP_DONE, {
					cmd = var_1_0.cmd,
					id = var_1_0.arg1
				})

				if var_1_0.callback:
					var_1_0.callback()
			else
				pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))
	elif ActivityConst.INSTAGRAM_OP_LIKE == var_1_0.cmd or ActivityConst.INSTAGRAM_OP_MARK_READ == var_1_0.cmd or ActivityConst.INSTAGRAM_OP_UPDATE == var_1_0.cmd or ActivityConst.INSTAGRAM_OP_SHARE == var_1_0.cmd:
		pg.ConnectionMgr.GetInstance().Send(11701, {
			id = var_1_0.arg1,
			cmd = var_1_0.cmd
		}, 11702, function(arg_3_0)
			if arg_3_0.result == 0:
				if ActivityConst.INSTAGRAM_OP_MARK_READ == var_1_0.cmd:
					local var_3_0 = var_1_1.GetMessageById(var_1_0.arg1)

					var_3_0.isRead = True

					var_1_1.UpdateMessage(var_3_0)
				elif ActivityConst.INSTAGRAM_OP_SHARE != var_1_0.cmd:
					local var_3_1 = Instagram.New(arg_3_0.data)

					var_1_1.UpdateMessage(var_3_1)

				arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_OP_DONE, {
					cmd = var_1_0.cmd,
					id = var_1_0.arg1
				})

				if var_1_0.callback:
					var_1_0.callback()
			else
				pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_3_0.result] .. arg_3_0.result))
	elif ActivityConst.INSTAGRAM_OP_COMMENT == var_1_0.cmd:
		pg.ConnectionMgr.GetInstance().Send(11703, {
			id = var_1_0.arg1,
			discuss = var_1_0.arg2,
			index = var_1_0.arg3
		}, 11704, function(arg_4_0)
			if arg_4_0.result == 0:
				local var_4_0 = Instagram.New(arg_4_0.data)

				var_1_1.UpdateMessage(var_4_0)
				arg_1_0.sendNotification(GAME.ACT_INSTAGRAM_OP_DONE, {
					cmd = var_1_0.cmd,
					id = var_1_0.arg1
				})

				if var_1_0.callback:
					var_1_0.callback()
			else
				pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_4_0.result] .. arg_4_0.result))

return var_0_0
