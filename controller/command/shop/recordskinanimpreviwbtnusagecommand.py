local var_0_0 = class("RecordSkinAnimPreviwBtnUsageCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().isOpen and 1 or 0

	pg.ConnectionMgr.GetInstance().Send(16203, {
		flag = var_1_0
	}, 16204, function(arg_2_0)
		if arg_2_0.ret == 0:
			-- block empty
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_2_0.result] .. arg_2_0.result))

return var_0_0
