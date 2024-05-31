local var_0_0 = class("NavalAcademyBuilding")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.parent = arg_1_1
	arg_1_0._tf = arg_1_1.findTF("academyMap/map/" .. arg_1_0.GetGameObjectName())
	arg_1_0.nameTxt = findTF(arg_1_0._tf, "name/Text").GetComponent(typeof(Text))
	arg_1_0.tip = findTF(arg_1_0._tf, "tip")

def var_0_0.Init(arg_2_0):
	onButton(arg_2_0, arg_2_0._tf, function()
		arg_2_0.OnClick(), SFX_PANEL)

	arg_2_0.nameTxt.text = arg_2_0.GetTitle()

	arg_2_0.RefreshTip()
	arg_2_0.OnInit()

def var_0_0.RefreshTip(arg_4_0):
	setActive(arg_4_0.tip, arg_4_0.IsTip())

def var_0_0.OnInit(arg_5_0):
	return

def var_0_0.OnClick(arg_6_0):
	return

def var_0_0.IsTip(arg_7_0):
	return False

def var_0_0.GetTitle(arg_8_0):
	return ""

def var_0_0.GetGameObjectName(arg_9_0):
	assert(False)

def var_0_0.emit(arg_10_0, ...):
	arg_10_0.parent.emit(...)

def var_0_0.Dispose(arg_11_0):
	pg.DelegateInfo.Dispose(arg_11_0)

return var_0_0
