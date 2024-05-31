local var_0_0 = class("FriendBlackListCard", import(".FriendCard"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.btn = arg_1_0.tf.Find("frame/occupy_btn")

def var_0_0.update(arg_2_0, arg_2_1):
	var_0_0.super.update(arg_2_0, arg_2_1)

return var_0_0
