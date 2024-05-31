local var_0_0 = class("MainOverDueAttireSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(AttireProxy).getExpiredChaces()

	if #var_1_0 > 0:
		arg_1_0.Display(AttireExpireDisplayPage, var_1_0, arg_1_1)
	else
		arg_1_1()

def var_0_0.Display(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.page = arg_2_1.New(pg.UIMgr.GetInstance().UIMain)

	function arg_2_0.page.Hide()
		arg_2_0.Clear()
		arg_2_3()

	arg_2_0.page.ExecuteAction("Show", arg_2_2)

def var_0_0.Clear(arg_4_0):
	if arg_4_0.page:
		arg_4_0.page.Destroy()

		arg_4_0.page = None

def var_0_0.Dispose(arg_5_0):
	arg_5_0.Clear()

return var_0_0
