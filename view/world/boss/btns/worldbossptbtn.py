local var_0_0 = class("WorldbossPtBtn")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.ptTF = arg_1_1
	arg_1_0.pt = arg_1_1.Find("Text").GetComponent(typeof(Text))
	arg_1_0.ptRecoveTF = arg_1_1.Find("time")
	arg_1_0.ptRecove = arg_1_1.Find("time/Text").GetComponent(typeof(Text))

	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	arg_2_0.ptRecoveTFFlag = False

	onButton(arg_2_0, arg_2_0.ptTF, function()
		arg_2_0.ptRecoveTFFlag = not arg_2_0.ptRecoveTFFlag

		setActive(arg_2_0.ptRecoveTF, arg_2_0.ptRecoveTFFlag), SFX_PANEL)
	setActive(arg_2_0.ptRecoveTF, arg_2_0.ptRecoveTFFlag)
	arg_2_0.Update()

def var_0_0.Update(arg_4_0):
	local var_4_0 = nowWorld().GetBossProxy()
	local var_4_1 = var_4_0.pt or 0

	arg_4_0.pt.text = var_4_1 .. "/" .. var_4_0.GetMaxPt()

	local var_4_2 = pg.gameset.joint_boss_ap_recove_cnt_pre_day.key_value

	arg_4_0.ptRecove.text = i18n("world_boss_pt_recove_desc", var_4_2)

def var_0_0.Dispose(arg_5_0):
	pg.DelegateInfo.Dispose(arg_5_0)

return var_0_0
