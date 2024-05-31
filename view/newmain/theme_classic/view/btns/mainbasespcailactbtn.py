local var_0_0 = class("MainBaseSpcailActBtn")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.root = arg_1_1
	arg_1_0.event = arg_1_2
	arg_1_0.isloading = False

def var_0_0.Init(arg_2_0, arg_2_1):
	arg_2_0.isScale = arg_2_1

	if arg_2_0.isloading:
		return

	if not arg_2_0._tf:
		arg_2_0.isloading = True

		ResourceMgr.Inst.getAssetAsync("ui/" .. arg_2_0.GetUIName(), "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_3_0)
			arg_2_0.isloading = False

			if arg_2_0.exited:
				return

			arg_2_0._tf = Object.Instantiate(arg_3_0, arg_2_0.GetContainer()).transform

			arg_2_0.OnRegister()
			arg_2_0.OnInit()
			onButton(arg_2_0, arg_2_0._tf, function()
				arg_2_0.OnClick(), SFX_MAIN)

			if arg_2_0.shouldHide:
				setActive(arg_2_0._tf, False)), True, True)
	else
		arg_2_0.OnInit()

	arg_2_0.CheckHide()

def var_0_0.Clear(arg_5_0):
	if not IsNil(arg_5_0._tf):
		Destroy(arg_5_0._tf.gameObject)

		arg_5_0._tf = None

		arg_5_0.OnClear()

def var_0_0.Dispose(arg_6_0):
	arg_6_0.exited = True

	pg.DelegateInfo.Dispose(arg_6_0)
	arg_6_0.Clear()

def var_0_0.Refresh(arg_7_0):
	arg_7_0.CheckHide()

def var_0_0.CheckHide(arg_8_0):
	if arg_8_0.shouldHide and not IsNil(arg_8_0._tf):
		setActive(arg_8_0._tf, True)

	arg_8_0.shouldHide = False

def var_0_0.Disable(arg_9_0):
	arg_9_0.shouldHide = True

	arg_9_0.OnDisable()

def var_0_0.GetContainer(arg_10_0):
	assert(False, "overview me !!!")

def var_0_0.InShowTime(arg_11_0):
	assert(False, "overview me !!!")

def var_0_0.GetUIName(arg_12_0):
	return

def var_0_0.OnClick(arg_13_0):
	return

def var_0_0.OnRegister(arg_14_0):
	return

def var_0_0.OnInit(arg_15_0):
	return

def var_0_0.OnClear(arg_16_0):
	return

def var_0_0.OnDisable(arg_17_0):
	return

return var_0_0
