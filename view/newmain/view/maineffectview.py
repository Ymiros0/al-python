local var_0_0 = class("MainEffectView")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.tr = arg_1_1
	arg_1_0.loading = False
	arg_1_0.caches = {}

def var_0_0.GetEffect(arg_2_0, arg_2_1):
	if arg_2_1.propose:
		return "jiehuntexiao"

	return None

def var_0_0.Init(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.GetEffect(arg_3_1)

	arg_3_0.Load(var_3_0)

def var_0_0.Refresh(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0.GetEffect(arg_4_1)

	if var_4_0 and arg_4_0.loading:
		arg_4_0.SetDirty(var_4_0)

		return

	arg_4_0.Load(var_4_0)

def var_0_0.Load(arg_5_0, arg_5_1):
	if arg_5_0.effectName and not arg_5_1:
		arg_5_0.Clear()

		return

	if not arg_5_1 or arg_5_1 == arg_5_0.effectName:
		return

	arg_5_0.Clear()

	arg_5_0.loading = True

	arg_5_0.LoadEffect(arg_5_1, function(arg_6_0)
		arg_5_0.loading = False
		arg_6_0.transform.localPosition = Vector3.zero
		arg_6_0.transform.localScale = Vector3.one
		arg_5_0.effectGo = arg_6_0
		arg_5_0.effectName = arg_5_1)

	arg_5_0.dirty = None

def var_0_0.LoadEffect(arg_7_0, arg_7_1, arg_7_2):
	if arg_7_0.caches[arg_7_1]:
		local var_7_0 = arg_7_0.caches[arg_7_1]

		setActive(var_7_0, True)
		arg_7_2(var_7_0)
	else
		ResourceMgr.Inst.getAssetAsync("Effect/" .. arg_7_1, arg_7_1, UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_8_0)
			if arg_7_0.exited:
				return

			if arg_7_0.IsDirty():
				arg_7_0.Load(arg_7_0.dirty)

				return

			local var_8_0 = Object.Instantiate(arg_8_0, arg_7_0.tr)

			arg_7_0.caches[arg_7_1] = var_8_0

			arg_7_2(var_8_0)), True, True)

def var_0_0.SetDirty(arg_9_0, arg_9_1):
	arg_9_0.dirty = arg_9_1

def var_0_0.IsDirty(arg_10_0):
	return arg_10_0.dirty != None

def var_0_0.Clear(arg_11_0):
	if arg_11_0.effectGo:
		setActive(arg_11_0.effectGo, False)

		arg_11_0.effectGo = None

	arg_11_0.effectName = None
	arg_11_0.loading = None

def var_0_0.Dispose(arg_12_0):
	arg_12_0.Clear()

	for iter_12_0, iter_12_1 in pairs(arg_12_0.caches):
		Object.Destroy(iter_12_1)

	arg_12_0.caches = None
	arg_12_0.exited = True
	arg_12_0.dirty = None

return var_0_0
