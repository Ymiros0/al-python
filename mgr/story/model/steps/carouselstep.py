local var_0_0 = class("CarouselStep", import(".StoryStep"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.bgs = arg_1_1.bgs

def var_0_0.GetMode(arg_2_0):
	return Story.MODE_CAROUSE

def var_0_0.GetBgs(arg_3_0):
	return arg_3_0.bgs

return var_0_0
