local var_0_0 = class("ShipProfileSkinBtn")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._tf = arg_1_1
	arg_1_0.sctxt = arg_1_0._tf.Find("mask/Text").GetComponent("ScrollText")
	arg_1_0.lockTF = arg_1_0._tf.Find("lock")
	arg_1_0.selected = arg_1_0._tf.Find("selected")
	arg_1_0.timelimitTF = arg_1_0._tf.Find("timelimit")
	arg_1_0.timelimitTxt = arg_1_0._tf.Find("timelimit/Text").GetComponent(typeof(Text))

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	arg_2_0.shipGroup = arg_2_2

	local var_2_0 = arg_2_1.name

	arg_2_0.sctxt.SetText(var_2_0)

	arg_2_0.unlock = arg_2_1.skin_type == ShipSkin.SKIN_TYPE_DEFAULT or arg_2_3 or arg_2_1.skin_type == ShipSkin.SKIN_TYPE_REMAKE and arg_2_0.shipGroup.trans or arg_2_1.skin_type == ShipSkin.SKIN_TYPE_PROPOSE and arg_2_0.shipGroup.married == 1

	setActive(arg_2_0.lockTF, not arg_2_0.unlock)
	arg_2_0.AddTimer(arg_2_1)

def var_0_0.AddTimer(arg_3_0, arg_3_1):
	local var_3_0 = getProxy(ShipSkinProxy).getSkinById(arg_3_1.id)
	local var_3_1 = var_3_0 and var_3_0.isExpireType() and not var_3_0.isExpired()

	setActive(arg_3_0.timelimitTF, var_3_1)
	arg_3_0.RemoveTimer()

	if var_3_1:
		arg_3_0.timer = Timer.New(function()
			arg_3_0.timelimitTxt.text = skinTimeStamp(var_3_0.getRemainTime()), 1, -1)

		arg_3_0.timer.Start()
		arg_3_0.timer.func()

def var_0_0.RemoveTimer(arg_5_0):
	if arg_5_0.timer:
		arg_5_0.timer.Stop()

		arg_5_0.timer = None

def var_0_0.Shift(arg_6_0):
	setActive(arg_6_0.selected, True)

def var_0_0.UnShift(arg_7_0):
	setActive(arg_7_0.selected, False)

def var_0_0.Dispose(arg_8_0):
	arg_8_0.RemoveTimer()

return var_0_0
