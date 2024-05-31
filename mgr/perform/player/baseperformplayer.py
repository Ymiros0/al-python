local var_0_0 = class("BasePerformPlayer")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0._anim = arg_1_0._tf.GetComponent(typeof(Animation))

	arg_1_0.Hide()

def var_0_0.Play(arg_2_0, arg_2_1, arg_2_2):
	assert(None, "Play方法必须由子类实现")

def var_0_0.Show(arg_3_0):
	setActive(arg_3_0._go, True)

def var_0_0.Hide(arg_4_0):
	setActive(arg_4_0._go, False)

def var_0_0.Clear(arg_5_0):
	assert(None, "Clear方法必须由子类实现")

def var_0_0.findTF(arg_6_0, arg_6_1, arg_6_2):
	assert(arg_6_0._tf, "transform should exist")

	return findTF(arg_6_2 or arg_6_0._tf, arg_6_1)

return var_0_0
