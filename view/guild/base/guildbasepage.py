local var_0_0 = class("GuildBasePage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	local var_1_0, var_1_1 = arg_1_0.getTargetUI()
	local var_1_2 = getProxy(GuildProxy).getRawData()

	if not var_1_2:
		return arg_1_0.uiname

	local var_1_3 = var_1_2.getFaction()

	if var_1_3 == GuildConst.FACTION_TYPE_BLHX:
		arg_1_0.uiname = var_1_0
	elif var_1_3 == GuildConst.FACTION_TYPE_CSZZ:
		arg_1_0.uiname = var_1_1

	return arg_1_0.uiname

def var_0_0.getTargetUI(arg_2_0):
	assert(False)

def var_0_0.Destroy(arg_3_0):
	if arg_3_0._state == var_0_0.STATES.DESTROY:
		return

	if not arg_3_0.GetLoaded():
		arg_3_0._state = var_0_0.STATES.DESTROY

		return

	arg_3_0._state = var_0_0.STATES.DESTROY

	pg.DelegateInfo.Dispose(arg_3_0)
	arg_3_0.OnDestroy()
	arg_3_0.disposeEvent()
	arg_3_0.cleanManagedTween()

	arg_3_0._tf = None

	local var_3_0 = PoolMgr.GetInstance()
	local var_3_1 = arg_3_0.uiname

	if arg_3_0._go != None and var_3_1:
		var_3_0.ReturnUI(var_3_1, arg_3_0._go)

		arg_3_0._go = None

return var_0_0
