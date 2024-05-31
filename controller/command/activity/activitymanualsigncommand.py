local var_0_0 = class("ActivityManualSignCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.activity_id
	local var_1_2 = getProxy(ActivityProxy).getActivityById(var_1_1)

	if not var_1_2 or var_1_2.isEnd():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

		return

	if var_1_0.cmd == ManualSignActivity.OP_GET_AWARD and not var_1_2.AnyAwardCanGet():
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_error") .. "1")

		return

	local var_1_3 = {}

	if var_1_0.cmd == ManualSignActivity.OP_GET_AWARD:
		var_1_3 = var_1_2.GetCanGetAwardIndexList()

	pg.ConnectionMgr.GetInstance().Send(11202, {
		activity_id = var_1_1,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.arg1,
		arg2 = var_1_0.arg2,
		arg_list = var_1_3,
		kvargs1 = var_1_0.kvargs1
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.GetTranAwards(var_1_0, arg_2_0)

			if var_1_0.cmd == ManualSignActivity.OP_SIGN:
				arg_1_0.HandleSign(var_1_1)
			elif var_1_0.cmd == ManualSignActivity.OP_GET_AWARD:
				arg_1_0.HandleGetAward(var_1_1)

			arg_1_0.sendNotification(GAME.ACT_MANUAL_SIGN_DONE, {
				awards = var_2_0,
				id = var_1_1
			})
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

def var_0_0.HandleSign(arg_3_0, arg_3_1):
	local var_3_0 = getProxy(ActivityProxy)
	local var_3_1 = var_3_0.getActivityById(arg_3_1)

	var_3_1.Signed()
	var_3_0.updateActivity(var_3_1)

def var_0_0.HandleGetAward(arg_4_0, arg_4_1):
	local var_4_0 = getProxy(ActivityProxy)
	local var_4_1 = var_4_0.getActivityById(arg_4_1)

	var_4_1.GetAllAwards()
	var_4_0.updateActivity(var_4_1)

return var_0_0
