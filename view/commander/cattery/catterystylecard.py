local var_0_0 = class("CatteryStyleCard")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.styleIcon = arg_1_0._tf.Find("mask/icon").GetComponent(typeof(Image))
	arg_1_0.lockTF = findTF(arg_1_0._tf, "lock")
	arg_1_0.mark = findTF(arg_1_0._tf, "mark")

def var_0_0.Update(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.style = arg_2_1
	arg_2_0.styleIcon.sprite = GetSpriteFromAtlas("CatteryStyle/" .. arg_2_1.getConfig("name"), "")

	local var_2_0 = arg_2_1.IsOwn()

	setActive(arg_2_0.lockTF, not var_2_0)
	setActive(arg_2_0.mark, arg_2_2)

def var_0_0.Dispose(arg_3_0):
	return

return var_0_0
