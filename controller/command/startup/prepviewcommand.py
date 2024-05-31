local var_0_0 = class("PrepViewCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	arg_1_0.facade.registerMediator(GameMediator.New())

return var_0_0
