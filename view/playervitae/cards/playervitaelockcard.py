local var_0_0 = class("PlayerVitaeLockCard", import(".PlayerVitaeBaseCard"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.desc = arg_1_0._tf.Find("Text")

def var_0_0.OnUpdate(arg_2_0, arg_2_1, arg_2_2):
	setText(arg_2_0.desc, i18n("secretary_unlock" .. arg_2_1))

def var_0_0.OnDispose(arg_3_0):
	return

return var_0_0
