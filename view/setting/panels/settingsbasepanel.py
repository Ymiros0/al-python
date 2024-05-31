local var_0_0 = class("SettingsBasePanel")
local var_0_1 = 0
local var_0_2 = 1
local var_0_3 = 2

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.parentTF = arg_1_1

	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.state = var_0_1

def var_0_0.Init(arg_2_0, arg_2_1):
	if arg_2_0.state == var_0_1:
		arg_2_0.Load(arg_2_1)
	else
		arg_2_1()

def var_0_0.IsLoaded(arg_3_0):
	return arg_3_0.state == var_0_3

def var_0_0.Load(arg_4_0, arg_4_1):
	arg_4_0.state = var_0_2

	PoolMgr.GetInstance().GetUI(arg_4_0.GetUIName(), True, function(arg_5_0)
		arg_4_0.state = var_0_3
		arg_4_0._go = arg_5_0
		arg_4_0._tf = arg_5_0.transform

		setParent(arg_4_0._tf, arg_4_0.parentTF)
		arg_4_0.InitTitle()
		arg_4_0.OnInit()
		arg_4_0.OnUpdate()
		setActive(arg_4_0._tf, True)
		arg_4_1())

def var_0_0.InitTitle(arg_6_0):
	setText(arg_6_0._tf.Find("title"), arg_6_0.GetTitle())
	setText(arg_6_0._tf.Find("title/title_text"), arg_6_0.GetTitleEn())

def var_0_0.Dispose(arg_7_0):
	pg.DelegateInfo.Dispose(arg_7_0)

	if arg_7_0.state >= var_0_3:
		PoolMgr.GetInstance().ReturnUI(arg_7_0.GetUIName(), arg_7_0._go)

def var_0_0.GetUIName(arg_8_0):
	assert(False, "overwrite me !!!")

def var_0_0.GetTitle(arg_9_0):
	assert(False, "overwrite me !!!")

def var_0_0.GetTitleEn(arg_10_0):
	assert(False, "overwrite me !!!")

def var_0_0.OnInit(arg_11_0):
	return

def var_0_0.OnUpdate(arg_12_0):
	return

return var_0_0
