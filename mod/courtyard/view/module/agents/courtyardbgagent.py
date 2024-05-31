local var_0_0 = class("CourtYardBGAgent", import(".CourtYardAgent"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.prefab = None

def var_0_0.Switch(arg_2_0, arg_2_1, arg_2_2):
	if not arg_2_2:
		return

	local var_2_0 = arg_2_0.prefab and arg_2_0.prefab.name or ""

	if arg_2_1 and var_2_0 != arg_2_2:
		arg_2_0.LoadBG(arg_2_2)
	elif arg_2_1 and var_2_0 == arg_2_2:
		-- block empty
	elif not arg_2_1 and var_2_0 == arg_2_2:
		arg_2_0.Clear()
	else
		assert(False)

def var_0_0.LoadBG(arg_3_0, arg_3_1):
	PoolMgr.GetInstance().GetPrefab("BackyardBG/" .. arg_3_1, arg_3_1, True, function(arg_4_0)
		if arg_3_0.exited:
			PoolMgr.GetInstance().ReturnPrefab("BackyardBG/" .. arg_3_1, arg_3_1, arg_4_0)

		arg_4_0.name = arg_3_1

		setParent(arg_4_0, arg_3_0._tf)
		arg_4_0.transform.SetAsFirstSibling()
		setActive(arg_4_0, True)

		arg_3_0.prefab = arg_4_0)

def var_0_0.Clear(arg_5_0):
	if arg_5_0.prefab:
		local var_5_0 = arg_5_0.prefab.name

		PoolMgr.GetInstance().ReturnPrefab("BackyardBG/" .. var_5_0, var_5_0, arg_5_0.prefab)

		arg_5_0.prefab = None

def var_0_0.ClearByName(arg_6_0, arg_6_1):
	if arg_6_0.prefab and arg_6_0.prefab.name == arg_6_1:
		arg_6_0.Clear()

def var_0_0.Dispose(arg_7_0):
	arg_7_0.Clear(True)

	arg_7_0.exited = True

return var_0_0
