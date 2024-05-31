local var_0_0 = class("RefluxRequestDataCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0):
	pg.ConnectionMgr.GetInstance().Send(11751, {
		type = 0
	}, 11752, function(arg_2_0)
		getProxy(RefluxProxy).setData(arg_2_0))

return var_0_0
