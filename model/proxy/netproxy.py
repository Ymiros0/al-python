local var_0_0 = class("NetProxy", pm.Proxy)

def var_0_0.onRegister(arg_1_0):
	arg_1_0.event = {}

	arg_1_0.register()

def var_0_0.register(arg_2_0):
	return

def var_0_0.on(arg_3_0, arg_3_1, arg_3_2):
	pg.ConnectionMgr.GetInstance().On(arg_3_1, function(arg_4_0)
		arg_3_2(arg_4_0))
	table.insert(arg_3_0.event, arg_3_1)

def var_0_0.onRemove(arg_5_0):
	arg_5_0.remove()

	for iter_5_0, iter_5_1 in ipairs(arg_5_0.event):
		pg.ConnectionMgr.GetInstance().Off(iter_5_1)

def var_0_0.remove(arg_6_0):
	return

def var_0_0.getRawData(arg_7_0):
	return arg_7_0.data

def var_0_0.getData(arg_8_0):
	return Clone(arg_8_0.data)

return var_0_0
